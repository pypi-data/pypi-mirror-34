from __future__ import print_function

import numpy
import tifffile

import spam.helpers


def simu(lengths=(1, 1, 1), nNodes=(10, 10, 10), covariance={'type': 'stable', 'alpha': 2},
         seed='NA', method=None, maxGB=1, dim=2, nRea=1, data=None, given=None,
         tifFile=None, fieldFile=None, vtkFile=None,
         verbose=False, RprintLevel=0):
    """Generate a Correlated Random Field based on the package RandomFields (cran-R). Wrapping is handled by the module rpy2.

        * cran-R: https://cran.r-project.org/
        * Package RandomFields (Martin Schlather): https://cran.r-project.org/web/packages/RandomFields/index.html
        * rpy2: https://pypi.python.org/pypi/rpy2

    Parameters
    ----------
    lengths : array of float, default=(1,1,1)
        Length of the definition domain in every directions (should be size of dim).
    nNodes : array of int, default=(10,10,10)
        Number of nodes in every directions (should be size of dim).
    covariance : dictionary (default {'type':'stable', 'alpha':2})
        Sets the type of covariance and its parameters. It defines the 'RMmodel'. Note: stable with alpha = 2 is the Gaussian covariance function.
    seed : string, default='NA'
        Defines the seed for the generator of random numbers. If seed=0, all realisations are the same.
    method : string, default=None
        Describe the RP method for R. If `None` given the default behavior is used (R looks for the best one). Works with method=`circulant` (FFT needs a lot of memory) method=`tbm` (turning band method)
    dim : int
        spatial dimention
    nRea: int, default=1
        number of realisations
    given: string
        string input for given in RFsimulation for conditional simulations. Ex. given='c(0,1)' sets node at x=0 and x=1.
    data: string
        string input for data in RFsimulation for conditional simulations. Ex. data='c(0,0)' sets values for node 1 and 2 at 0.
    maxGB: float,default=1
        set the maximum memory that R can use.
    RprintLevel: int, default=3
        The print level of R. The higher it is the more information is printed.
    verbose: bool, default=False
        Verbose mode if True.
    fieldFile: string, default=None
        If not None, the base name of the tif files saved.
    fieldFile: string, default=None
        If not None, the base name of the field files saved. One file is saved for each realisation.
        These file can be used as input for ``spam.mesh.projection``.
    vtkFile: string, default=None
        If not None, the base name of the vtk files saved.

    Returns
    -------
    array:
        The realisations of the random fields. ``shape = (nx, ny, nz, nRea)``

    """

    # rpy2
    import rpy2.robjects.packages as rpackages
    from rpy2.robjects import r

    if verbose:
        print('*** Welcome to spam.excursions.randomfields.simu()')
    # step 0: defines shortcuts
    if dim > 1:
        l = (lengths, lengths, lengths) if isinstance(
            lengths, float) else lengths
        n = (nNodes, nNodes, nNodes) if isinstance(nNodes, int) else nNodes
        nCells = [_-1 for _ in n]
    else:
        l = lengths
        n = nNodes
        nCells = nNodes-1

    if verbose:
        print('*\tLengths        : {}'.format(l))
        print('*\tNumber of nodes: {}'.format(n))
        print('*\tNumber of cells: {}'.format(nCells))
        print('*\tCovariance:')
        for key, value in covariance.items():
            print('*\t\t {}: {}'.format(key, value))
        print('*')

    # Step 1: R and RandomFields preparation
    # Step 1.1: import package
    if verbose:
        print('* Import R package RandomFields')
    try:
        rpackages.importr("RandomFields")
    except:
        if verbose:
            print('*\tFail import.')
        if verbose:
            print('*\tTrying to install package RandomFields.')
        # from rpy2.robjects.vectors import StrVector
        utils = rpackages.importr('utils')
        utils.chooseCRANmirror(ind=1)
        utils.install_packages('RandomFields')
        rpackages.importr('RandomFields')
        if verbose:
            print('*\tPackage successfully installed and loaded.')

    # Step 1.2: RMmodel
    if covariance['type'] == 'stable':
        if 'variance' not in covariance:
            covariance['variance'] = 1.0
        if 'correlation_length' not in covariance:
            covariance['correlation_length'] = 1.0
        if 'alpha' not in covariance:
            covariance['alpha'] = 2
        _r_RMmodel = 'RMstable(var={variance}, scale={correlation_length}, alpha={alpha})'.format(
            **covariance)
    elif covariance['type'] == 'matern':
        if 'variance' not in covariance:
            covariance['variance'] = 1
        if 'correlation_length' not in covariance:
            covariance['correlation_length'] = 1
        if 'nu' not in covariance:
            covariance['nu'] = 2
        _r_RMmodel = 'RMmatern(nu={nu}, var={variance}, scale={correlation_length})'.format(
            **covariance)
    elif covariance['type'] == 'bessel':
        if 'variance' not in covariance:
            covariance['variance'] = 1
        if 'correlation_length' not in covariance:
            covariance['correlation_length'] = 1
        if 'nu' not in covariance:
            covariance['nu'] = 2
        _r_RMmodel = 'RMbessel(nu={nu}, var={variance}, scale={correlation_length})'.format(
            **covariance)
    elif covariance['type'] == 'dampedcos':
        if 'variance' not in covariance:
            covariance['variance'] = 1
        if 'correlation_length' not in covariance:
            covariance['correlation_length'] = 1
        if 'lambda' not in covariance:
            covariance['lambda'] = 0
        _r_RMmodel = 'RMdampedcos(lambda={lambda},var={variance}, scale={correlation_length})'.format(
            **covariance)
    elif covariance['type'] == 'sinepower':
        if 'variance' not in covariance:
            covariance['variance'] = 1
        if 'correlation_length' not in covariance:
            covariance['correlation_length'] = 1
        if 'alpha' not in covariance:
            covariance['alpha'] = 2
        _r_RMmodel = 'RMstable(var={variance}, scale={correlation_length}, alpha={alpha})'.format(
            **covariance)
    else:
        _r_RMmodel = covariance
    if verbose:
        print('*\tRMmodel: {}'.format(_r_RMmodel))

    # Step 1.3: RPmodel (add circulant if necessary)
    if method is not None:
        _r_RPmodel = "RP{method}({rm})".format(method=method, rm=_r_RMmodel)
    else:
        _r_RPmodel = _r_RMmodel
    if verbose:
        print('*\tRPmodel: {}'.format(_r_RPmodel))

    # Step 1.4: Options
    _r_printlevel = RprintLevel
    _r_options = 'RFoptions(seed={},spConform=FALSE,printlevel={})'.format(
        seed, _r_printlevel)
    if verbose:
        print('*\tOptions: {}'.format(_r_options))

    # Step 1.5: Grid, RFsimulate and sequence
    _r_grid = 'NULL'
    _r_RFsimulate = 'RFsimulate'
    if dim == 1:
        _r_x = 'seq(0.0, {}, {})'.format(l, float(l)/(n-1))
    else:
        _r_x = 'seq(0.0, {}, {})'.format(l[0], float(l[0])/(n[0]-1))
    if dim > 1:
        _r_y = 'seq(0.0, {}, {})'.format(l[1], float(l[1])/(n[1]-1))
    if dim > 2:
        _r_z = 'seq(0.0, {}, {})'.format(l[2], float(l[2])/(n[2]-1))

    # step 2: transform _r_string into r objects
    if verbose:
        print('* Convert R object')
    rpmo = r(_r_RPmodel)
    rfsi = r(_r_RFsimulate)
    opti = r(_r_options)
    grid = r(_r_grid)
    if dim > 0:
        x = r(_r_x)
    if dim > 1:
        y = r(_r_y)
    if dim > 2:
        z = r(_r_z)

    if data is not None:
        data = r(data)
    else:
        data = r('NULL')
    if given is not None:
        given = r(given)
    else:
        given = r('NULL')

    # Step 3: launch r command
    if verbose:
        print('* Simulate Random Field')
    if verbose:
        print('<R>')
    if dim == 1:
        rf = numpy.array(
            rfsi(model=rpmo, x=x, grid=grid, n=nRea, given=given, data=data)).astype('<f4')
    if dim == 2:
        rf = numpy.array(
            rfsi(model=rpmo, x=x, y=y, grid=grid, n=nRea)).astype('<f4')
    if dim == 3:
        rf = numpy.array(
            rfsi(model=rpmo, x=x, y=y, z=z, grid=grid, n=nRea, maxGB=maxGB)).astype('<f4')

    if verbose:
        print('</R>')

    # save one tif for each realisation
    if tifFile:
        if verbose:
            print('* Save image(s):')
        for i in range(nRea):
            currentName = '{tifFile}_{rea:05d}.tif'.format(tifFile=tifFile, rea=i)
            if verbose:
                print('*\t{}'.format(currentName))
            if dim == 1:
                if verbose:
                    print('# /!\ Impossible do make tif with 1D Fields')
            elif dim == 2:
                if nRea == 1:
                    tifffile.imsave(currentName, rf.astype('<f4'))
                else:
                    tifffile.imsave(currentName, rf[:, :, i].astype('<f4'))
            elif dim == 3:
                if nRea == 1:
                    tifffile.imsave(currentName, rf.astype('<f4'))
                else:
                    tifffile.imsave(currentName, rf[:, :, :, i].astype('<f4'))

    # save dat files with good format for projmorpho ## only 3D
    if fieldFile:
        if verbose:
            print('* Save realisations in  field files:')
        for i in range(nRea):
            currentName = '{o}_{i:05d}'.format(o=fieldFile, i=i)
            if verbose:
                print('*\t{}.dat'.format(currentName))
            with open('{}.dat'.format(currentName), 'w') as f:
                f.write('{}, {}, {}\n'.format(*l))
                f.write('0,0,0\n')
                f.write('{}, {}, {}\n'.format(*nCells))
                if nRea == 1:
                    for val in rf.flatten():
                        f.write('{}\n'.format(str(val)))
                else:
                    for val in rf[:, :, :, i].flatten():
                        f.write('{}\n'.format(str(val)))

    # save dat files with good format for projmorpho ## only 3D
    if vtkFile and dim == 3:
        if verbose:
            print('* Save realisations in several vtk files:')
        for i in range(nRea):
            currentName = '{o}_{i:05d}'.format(o=vtkFile, i=i)
            if verbose:
                print('*\t{}.vtk'.format(currentName))

            if nRea == 1:
                # tmp = rf.ravel()
                tmp = rf
            else:
                # tmp = rf[:, :, :, i].ravel()
                tmp = rf[:, :, :, i]

            spam.helpers.writeStructuredVTK(aspectRatio=l, pointData={'RandomField': tmp}, fileName="{}.vtk".format(currentName))

    if verbose:
        print('*')
        print('*** See you soon.')

    return rf


def parametersLogToGauss(muLog, stdLog, lcLog=1):
    """ Gives the underlying Gaussian standard deviation and mean value
    of the log normal distribution of standard deviation and mean value.

    Parameters
    ----------
        muLog: float
            Mean value of the log normal distribution.
        stdLog: float
            Standard deviation of the log normal distribution.
        lcLog: float, default=1
            Correlation length of the underlying log normal correlated Random Field.

    Returns
    -------
        muGauss: float
            Mean value of the Gaussian distribution.
        stdGauss: float
            Standard deviation of the Gaussian distribution.
        lcGauss: float
            Correlation length of the underlying Gaussian correlated Random Field.


    """
    stdGauss = numpy.sqrt(numpy.log(1.0 + stdLog**2/muLog**2))
    muGauss = numpy.log(muLog) - 0.5*stdGauss**2
    lcGauss = (-1.0/numpy.log(numpy.log(1+stdLog**2 * numpy.exp(-1.0/lcLog)/muLog**2) / stdLog**2))**(0.5)

    return muGauss, stdGauss, lcGauss


def fieldGaussToUniform(g, a=0.0, b=1.0):
    """Transforms a Gaussian Random Field into a uniform Random Field.

    Parameters
    ----------
        g: array
            The values of the Gaussian Random Fields.
        a: float, default=0.0
            The minimum borne of the uniform distribution.
        b: float, default=1.0
            The maximum borne of the uniform distribution.

    Return
    ------
        array:
            The uniform Random Field.
    """
    from scipy.special import erf
    return float(a) + 0.5*float(b)*(1.0 + erf(g/2.0**0.5))


def fieldUniformToGauss(g, a=0.0, b=1.0):
    """Transforms a uniform Random Field into a Gaussian Random Field.

    Parameters
    ----------
        g: array
            The values of the uniform Random Fields.
        a: float, default=0.0
            The minimum borne of the uniform distribution.
        b: float, default=1.0
            The maximum borne of the uniform distribution.

    Return
    ------
        array:
            The Gaussian Random Field.
    """
    from scipy.special import erfinv
    return 2.0**0.5*erfinv(2.0*(g-float(a))/float(b) - 1.0)


# old stuff


def _read_from_dat(dat_file, nNodes=None, verbose=False):
    if nNodes is None:
        print("need to read it in the dat file")
        return -1
    else:
        if isinstance(nNodes, int):
            if verbose:
                print('* Dimension 1')
            flat = numpy.loadtxt(dat_file, comments="#", delimiter=" ")
            nRea = flat.shape[0]
            rf = numpy.zeros((nNodes, nRea), dtype=numpy.float32)
            for i in range(nRea):
                rf[:, i] = flat[i]
        else:
            if verbose:
                print('* Dimension {}'.format(len(nNodes)))
            if len(nNodes) == 2:
                flat = numpy.loadtxt(dat_file, comments="#", delimiter=" ")
                nRea = flat.shape[0]
                rf = numpy.zeros(
                    (nNodes[0], nNodes[1], nRea), dtype=numpy.float32)
                for i in range(nRea):
                    rf[:, :, i] = flat[i, :].reshape(nNodes[0], nNodes[1])
            if len(nNodes) == 3:
                flat = numpy.loadtxt(dat_file, comments="#", delimiter=" ")
                nRea = flat.shape[0]
                rf = numpy.zeros(
                    (nNodes[0], nNodes[1], nNodes[2], nRea), dtype=numpy.float32)
                for i in range(nRea):
                    rf[:, :, :, i] = flat[i, :].reshape(
                        nNodes[0], nNodes[1], nNodes[2])

        if verbose:
            print('* Shape {}'.format(rf.shape))
        return rf


def _uniform_parameters_to_moments(a, b):
    """
    gives the mean and the standard deviation of a uniform distribution based on its parameters
    """
    std = float(b)/(2.0*3.0**0.5)
    mu = float(a) + 0.5*float(b)
    return (mu, std)


def _uniform_moments_to_parameters(mu, std):
    """
    gives the parameters a and b of a uniform distribution based on its mean and the standard deviation
    """
    b = 2.0*3**0.5*float(std)
    a = float(mu) - 0.5*b
    return (a, b)
