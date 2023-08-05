﻿import numpy
import spam.mesh.structured as smesh

# Default structural element
#       0 0 0
#       0 1 0
#       0 0 0
#    0 1 0
#    1 2 1
#    0 1 0
# 0 0 0
# 0 1 0
# 0 0 0
structEl = smesh.structuringElement(radius=1, order=1).astype( '<f4' )
structEl[1, 1, 1] = 2.0

def average( im, structEl=structEl ):
    """ This function calculates the average map of a grey scale image over a structuring element

        Parameters
        ----------
        im1 : 3D numpy array
            The grey scale image for which the average map will be calculated

        structEl : 3D numpy array, optional
            The structural element defining the local window-size of the operation
            Note that the value of each component is considered as a weight (ponderation) for the operation
            (see `spam.mesh.structured.structuringElement` for details about the structural element)
            Default = radius = 1 (3x3x3 array), order = 1 (`diamond` shape)

        Returns
        -------
        imFiltered : 3D numpy array
            The averaged image
    """
    import spam.filters.filtersToolkit as mft

    imFiltered = numpy.zeros_like( im ).astype('<f4')
    mft.average( im, imFiltered, structEl )

    return imFiltered

def variance( im, structEl=structEl ):
    """" This function calculates the variance map of a grey scale image over a structuring element

        Parameters
        ----------
        im1 : 3D numpy array
            The grey scale image for which the variance map will be calculated

        structEl : 3D numpy array, optional
            The structural element defining the local window-size of the operation
            Note that the value of each component is considered as a weight (ponderation) for the operation
            (see `spam.mesh.structured.structuringElement` for details about the structural element)
            Default = radius = 1 (3x3x3 array), order = 1 (`diamond` shape)

        Returns
        -------
        imFiltered : 3D numpy array
            The variance image
    """
    import spam.filters.filtersToolkit as mft

    imFiltered = numpy.zeros_like( im ).astype('<f4')
    mft.variance( im, imFiltered, structEl )

    return imFiltered


### old equivalent 100% python stuff... way slower

# def _moving_average( im, struct=default_struct ):
#     """
#     Calculate the average of a grayscale image over a 3x3x3 structuring element
#     The output is float32 since results is sometimes outof the uint bounds during computation
#     PARAMETERS:
#     - im (numpy.array): The grayscale image to be treated
#     - struct (array of int): the structural element.
#        Note that the value of each component is considerred as a weight (ponderation) for the operation
#     RETURNS:
#     - o_im (numpy.array float32): The averaged image
#     HISTORY:
#     2016-03-24 (JBC): First version of the function
#     2016-04-05 (ER): generalisation using structural elements
#     2016-05-03 (ER): add progress bar
#     """
#     # Step 1: init output_image as float 32 bits
#     o_im = numpy.zeros( im.shape, dtype='<f4' )
#     # Step 2: structutral element
#     structural_element_size = int( len( struct )/2 )
#     structural_element_weight = float( struct.sum() )
#     if prlv>5:
#         import progressbar
#         max_values = len( numpy.argwhere( struct ) )
#         bar = progressbar.ProgressBar( maxval=max_values, widgets=['Average filter: ', progressbar.Percentage(), progressbar.Bar('=', '[', ']')] )
#         bar.start()
#     for i, c in enumerate( numpy.argwhere( struct ) ):
#         # convert structural element coordinates into shift to apply
#         shift_to_apply = c-structural_element_size
#         # get the local weight from the structural element value
#         current_voxel_weight = float( struct[c[0], c[1], c[2]] )
#         # if prlv>5: print '   Shift {} of weight {}'.format( shift_to_apply, current_voxel_weight )
#         # output_image = output_image + ( voxel_weight * image / element_weight )
#         o_im += current_voxel_weight*sman.multiple_shifts( im, shifts=shift_to_apply )/structural_element_weight
#         if prlv>5: bar.update( i+1 )
#     if prlv>5: bar.finish()
#     return o_im
#
# def _moving_variance( im, struct=default_struct ):
#     """
#     Calculate the variance of a grayscale image over a 3x3x3 structuring element
#     The output is float32 since results is sometimes outof the uint bounds during computation
#     PARAMETERS:
#     - image (numpy.array): The grayscale image to be treat
#     RETURNS:
#     - o_im (numpy.array): The varianced image
#     HISTORY:
#     2016-04-05 (ER): First version of the function
#     """
#     # Step 1: return E(im**2) - E(im)**2
#     return moving_average( numpy.square( im.astype('<f4') ), struct=struct ) - numpy.square( moving_average( im, struct=struct ) )
