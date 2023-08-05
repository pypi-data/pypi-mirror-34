# coding: utf8

""" Measure correlation of a given field with two different approach.

View examples in the gallery.

How to import
-------------
>>> import spam.measures.covariance as cov


"""
from __future__ import print_function

import numpy

def alongAxis(im, d, mask=None, axis=[0,1,2]):
    """ 
    Compute the covariance function of 2D or 3D images along specific axis.

    This function computes the covariance of a field (grey values or binary) with or without a mask. The covariance is computed at integer distances (in voxels). No interpolation is made but specific direction can be asked.

    Parameters
    ----------
        im : array, string
            The image as a name of an input file (grey or binary) or directly an array

        d : array
            The list of distances (in voxels) considered to compute the covariance. It can't be bigger than the size of image and it has to be integers.                                                                                                              
        
        mask : array, optional
            The name of the mask file (binary, 1 for phase of interest) or directly an array

        axis : array, default=[0,1,2]
            The list of axis in wich the direction is computed.

    Returns
    -------
        c : array
            A 2D array with list of values of the covariance at the different distances for each axis.

    Examples
    --------
    
        >>> import numpy
        >>> import tifffile
        >>> im = tifffile.imread( "snow.tif" )
        This image of size 100x100x100 is a field of grey values
        >>> d = numpy.arange( 0, )
        array([ 0,  1,  2,  3,  4])
        >>> c = cov.alongAxis( im, d )
        array([[86833030., 74757580., 53643410., 35916468.],                 # axis 0
        .      [86833030., 76282920., 56910720., 39792388.],                 # axis 1
        .      [86833030., 76410500., 57040076., 39938920.]], dtype=float32) # axis 2

    """
    import spam.helpers.imageManipulation as iman

    # convert scalar into array of size 1
    if isinstance(d, int):
        d = numpy.array([d])
    if isinstance(d[0], (long, float)):
        print( 'spam.measures.covariance.alongAxis: d={}. Should be a list of integers.'.format(type(d[0])) )
        print( 'exit function.' )
        return -1
    if max(d) >= im.shape[0] or max(d) >= im.shape[1] or max(d) >= im.shape[2]:
        print( 'spam.measures.covariance.alongAxis: max(d)={}. Should be smaller than the image.'.format(max(d)) )
        print( 'exit function.' )
        return -1

    # Step 0: apply mask
    if mask is not None:
        im = numpy.multiply(im, mask)

    # Step 1: Calculate expectation and variance
    if mask is not None:
        E = numpy.mean(im, dtype=numpy.float32) * \
            numpy.size(mask)/float(numpy.sum(mask))
        V = ((numpy.mean(numpy.multiply(im, im), dtype=numpy.float64)
              * numpy.size(mask)/float(numpy.sum(mask))) - E*E)
    else:
        E = numpy.mean(im, dtype=numpy.float32)
        V = numpy.var(im, dtype=numpy.float32)

    # Step 2: Compute covariance c(d)
    axis = [axis] if isinstance(axis, int) else axis
    c = numpy.zeros((len(axis), len(d)), dtype=numpy.float32)
    for j, a in enumerate(axis):
        for (i, x) in enumerate(d):
            if mask is not None:
                # Step 2.1: Take the effectif part and compute the pairs of number
                mask_eff = numpy.logical_and(mask, iman.singleShift(mask, x, a, sub=False))
                n = numpy.sum(mask_eff)
                # Step 2.2: multiply the image
                im_multi = numpy.multiply( im, iman.singleShift(im, x, a, sub=0) )
                im_multi = numpy.multiply( im_multi, mask_eff, dtype=numpy.float32 )
            else:
                # Step 2.1: Compute the pairs of numbers
                size = im.shape[a]
                n = (size-x)*size**2
                # Step 2.2: Multiply the image
                im_multi = numpy.multiply(im, iman.singleShift(im, x, a, sub=0), dtype=numpy.float32)
            n_multi = numpy.sum(im_multi)
            # Step 2.3: Compute covariance
            c[j, i] = float(numpy.sum(im_multi)) / float(n) - E*E if n > 0 else 0.0

    return c


def subPixel(im, distance=25, step=10, normType=None, n_threads=1):
    """Compute the covariance function of 2D or 3D images.

    The correlation function is computed on the zero mean image.
    The code behind -- for pre-allocation reasons -- works on a number of unique distances,
    which in 3D is closely unders=estimated by the square of the distance asked for.
    To change this a pre-allocated precision (i.e., 0.2 px) and distance could be used in the C-code.
    A sub pixel interpolation of the grey values in made.


    Parameters
    ----------
        im : array
            The image. It is automatically converted into a 32 bit float ``<f4``.

        distance : int, optional
            The approximate distance in pixels over which to make this measurement.

        step : int, optional
            The step parameter, which is how many pixels to jump when moving the pixel of interest
            when calculating the correaltion function (this is the best way to save time).
            The smaller the step the longer the computational time and the better the measure of each value of the covariance.

        normType : string, optional
            Select the of normalisation for the covariance output.
            ``normType="None"``: no normalisation,
            ``normType="variance"``: divide the covariance by the variance of the image,
            ``normType="first"``: divide the covariance by its value at 0.

        n_threads : int, optional
            Number of threads for the c++ ``#pragma`` command using ``openmp``.

    Returns
    -------
        d : array
            The list of distances in pixel where the correlation is computed.

        c : array
            The list of calues of the covariance at the different distances.

    Examples
    --------
    
        >>> import numpy
        >>> import tifffile
        >>> im = tifffile.imread( "snow.tif" )
        This image of size 100x100x100 is a field of grey values
        >>> d = numpy.arange( 0, 4 )
        array([ 0,  1,  2,  3,  4])
        >>> c = cov.subPixel( im, distance=2 )
        (array([0.        , 1.        , 1.41421354, 1.73205078]), # distances
        array( [89405248. , 77995006. , 69534446. , 62701681.]))  # covariance

    Warning
    -------
        The multithread version is bugged... openmp gives random values.
    """

    import spam.measures.measuresToolkit

    # Make sure the image is in the right format for us:
    im = im.astype('<f4')

    # If 2D image pad with false 1st dimension
    if len(im.shape) == 2:
        # Make them degraded 3D images
        im = im.reshape((1,) + im.shape)

    # allocate memory
    n_unique_distances = distance**2
    output = numpy.zeros((n_unique_distances, 2), dtype='<f8')

    # call cpp function
    spam.measures.measuresToolkit.computeCorrelationFunction(
        im - im.mean(), output, step, n_threads)

    if normType is not None:
        if normType == "variance":
            # normalise covariance function to a correlation function by dividing by the variance of the image.
            imVar = im.std()**2
            output[:, 1] = output[:, 1] / imVar
        elif normType == "first":
            # normalise covariance function by its first value. Basically it forces it to be 1 at 0.
            output[:, 1] = output[:, 1] / output[0, 1]

    d = output[:, 0]
    c = output[:, 1]

    return (d, c)


def analyticalBeta(d, lc, b):
    """
    Sample correlation function: Beta correlation function

    $$C(d) = \exp(-(d/l_c)^b) $$

    Parameters
    ----------
        d : array
            The list of distances where the function is evaluated.

        lc : float
            The correlation length.

        b : float
            The first parameter of the function. If ``b=2`` this is the gaussian function

    Returns
    -------
        c : array
            The list of values of the function corresponding to the given distances.

    """

    c = numpy.exp(-numpy.float_power(d/lc, b))

    return (c)


def analyticalGaussian(d, lc):
    """
    Sample correlation function: Gaussian correlation function


    $$C(d) = \exp(-(d/l_c)^2) $$

    Parameters
    ----------
        d : array
            The list of distances where the function is evaluated.

        lc : float
            The correlation length.

    Returns
    -------
       array :
            The list of values of the function corresponding to the given distances.

    """

    return numpy.exp(-numpy.float_power(d/lc, 2))


def fit(d, c, functionType="gaussian"):
    """For autofitting, a helper function...

    Parameters
    ----------
        d : array
            The list of distances of the covariance.

        c: array
            The list of value of covariance corresponding to the distances.

        functionType : ``{"gaussian","beta"}``
            The type of covariance function

    Returns
    -------
        popt : array
            The optimisation parameters

    """

    import scipy.optimize

    if functionType == "gaussian":
        [popt, pvar] = scipy.optimize.curve_fit(
            analyticalGaussian, d, c)
    elif functionType == "beta":
        [popt, pvar] = scipy.optimize.curve_fit(
            analyticalBeta, d, c)

    return popt
