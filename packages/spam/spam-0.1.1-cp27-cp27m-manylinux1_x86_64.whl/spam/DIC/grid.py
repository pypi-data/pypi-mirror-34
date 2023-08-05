﻿from __future__ import print_function

import numpy
import spam.DIC.correlate
import spam.DIC.transformationOperator
import Queue
##import spam.DIC

def makeGrid( imageSize, nodeSpacing ):
    """
        Define a grid of correlation points.

        Parameters
        ----------
        imageSize : 3-item list
            Size of volume to spread the grid inside

        nodeSpacing : 3-item list or int
            Spacing between nodes

        Returns
        -------
        nodePositions : nPointsx3 numpy.array
            Array containing Z, Y, X positions of each point in the grid
    """
    if len( imageSize ) != 3:
        print( "\tgrid.makeGrid(): imageSize doesn't have three dimensions, exiting" )
        return

    if type( nodeSpacing ) == int or type( nodeSpacing ) == float:
        nodeSpacing = [ nodeSpacing ]*3
    elif len( nodeSpacing) != 3:
        print( "\tgrid.makeGrid(): nodeSpacing is not an int or float and doesn't have three dimensions, exiting" )
        return

    if imageSize[0] == 1:   twoD = True
    else:                   twoD = False

    # Note: in this cheap node spacing, the first node is always at a distance of --nodeSpacing-- from the origin
    # The following could just be done once in principle...
    nodesMgrid = numpy.mgrid[ nodeSpacing[0]:imageSize[0]:nodeSpacing[0],
                              nodeSpacing[1]:imageSize[1]:nodeSpacing[1],
                              nodeSpacing[2]:imageSize[2]:nodeSpacing[2] ]

    # If twoD then overwrite nodesMgrid
    if twoD:
        nodesMgrid = numpy.mgrid[        0      :      1     :      1       ,
                                  nodeSpacing[1]:imageSize[1]:nodeSpacing[1],
                                  nodeSpacing[2]:imageSize[2]:nodeSpacing[2] ]



    nodesDim = (nodesMgrid.shape[1],nodesMgrid.shape[2],nodesMgrid.shape[3])

    numberOfNodes = int( nodesMgrid.shape[1] * nodesMgrid.shape[2] * nodesMgrid.shape[3] )

    nodePositions = numpy.zeros( ( numberOfNodes, 3 ) )

    nodePositions[:,0] = nodesMgrid[0].ravel()
    nodePositions[:,1] = nodesMgrid[1].ravel()
    nodePositions[:,2] = nodesMgrid[2].ravel()

    return nodePositions, nodesDim




def pixelSearch( im1, im2, nodePositions, halfWindowSize, searchRange,
                 Ffield = None,
                 minSubVolume=None,
                 im1mask=None,
                 greyThreshold = [ -numpy.inf, numpy.inf ]):
    """
        This function handles grid-based local correlation, offering an initial rough dispalcement-only guess.
        At the moment matching of windows is done with a Normalised-Correlation-Coefficient approach.

        Parameters
        ----------
        im1 : 3D numpy array
            A 3D image of greylevels defining a reference configuration for the pixel search

        im2 : 3D numpy array
            A deformed 3D image of greylevels

        nodePositions : nPoints*3 numpy array
            Array containing Z, Y, X positions of each point in the grid, as returned by ``makeGrid`` for example

        halfWindowSize : 3-item list or int
            Size of subvolumes to perform the image correlation on, as a data range taken either side of the voxel on which the node is placed.
            The subvolume will be 2*halfWindowSize + 1 pixels on each side.
            A general recommendation is to make this half the node spacing

        searchRange : dictionary
            Search range as a dictionary containing 3 keys: 'zRange', 'yRange', and 'xRange',
            Each of which contains a list with two items

        Ffield : nPoints*4*4 numpy array, optional
            Optional field of ``F`` transformation operators defined for each node.
            Currently, only the translational components of F will be taken into account.
            Default = No displacement

        minSubVolume : int, optional
            Minimum number of pixels in a subvolume for it to be correlated (only considered in the case of im1mask).
            Expressed as a % of subvolume volume.
            Default = 50% of subvolume

        im1mask : 3D boolean numpy array, optional
            A mask for im1 which is true in the zones to correlate.
            Default = None

        greyThreshold : list of two floats, optional
            Threshold for the mean greylevel in each im1 subvolume.
            If the mean is below the first value or above the second value, the grid point is not correlated.
            Default = [ -inf, inf ]

        Returns
        -------
        Dictionary containing:

        Keys
            Ffield : nNodes*4*4 numpy array of floats
                For each node, the measured transformatio operator (displacement only)

            pixelSearchCC : nNodes numpy array of floats
                For each node, the NCC score obtained
    """
    numberOfNodes = nodePositions.shape[0]

    # Check input sanity
    if type( halfWindowSize ) == int or type( halfWindowSize ) == float:
        halfWindowSize = [ halfWindowSize ]*3

    # Check minSubVolume
    if minSubVolume is None:
        minSubVolume = int( ((1+min(halfWindowSize)*2)**3) * 0.5 )
    else:
        minSubVolume = int( ((1+min(halfWindowSize)*2)**3) * minSubVolume )

    # Check F field
    if Ffield is None:
        Ffield = numpy.zeros( ( numberOfNodes, 4, 4 ) )
        for nodeNumber in xrange( numberOfNodes ): Ffield[nodeNumber] = numpy.eye( 4 )
    else:
        # Add initial displacement guess to search range
        for nodeNumber in xrange( numberOfNodes ): 
            searchRange['zRange'][0] += Ffield[nodeNumber,0,3]
            searchRange['zRange'][1] += Ffield[nodeNumber,0,3]
            searchRange['yRange'][0] += Ffield[nodeNumber,1,3]
            searchRange['yRange'][1] += Ffield[nodeNumber,1,3]
            searchRange['xRange'][0] += Ffield[nodeNumber,2,3]
            searchRange['xRange'][1] += Ffield[nodeNumber,2,3]

    # Create pixelSearchCC vector
    pixelSearchCC = numpy.zeros( ( numberOfNodes ) )

    print( "\tStarting Pixel search" )

    # Start loop over nodes
    for nodeNumber in xrange( numberOfNodes ):
        print( "\r\t\tCorrelating node {:04d} of {:04d}".format( nodeNumber+1, numberOfNodes ) ), 

        # Prepare slice for im1 -- this is always in the same place
        subVolSlice1 = [slice(int(nodePositions[nodeNumber,0]-halfWindowSize[0]), int(nodePositions[nodeNumber,0]+halfWindowSize[0]+1) ),
                        slice(int(nodePositions[nodeNumber,1]-halfWindowSize[1]), int(nodePositions[nodeNumber,1]+halfWindowSize[1]+1) ),
                        slice(int(nodePositions[nodeNumber,2]-halfWindowSize[2]), int(nodePositions[nodeNumber,2]+halfWindowSize[2]+1) ) ]

        # Extract it...
        imagette1 = im1[subVolSlice1].copy()

        # Check Mask volume condition
        if im1mask is not None: maskVolCondition = im1mask[subVolSlice1].sum() > minSubVolume
        else:                   maskVolCondition = True

        # Check it satisfies the volume and greyscale criteria
        if numpy.nanmean( imagette1 ) > greyThreshold[0] and numpy.nanmean( imagette1 ) < greyThreshold[1] and maskVolCondition:
            returns = spam.DIC.correlate.pixelSearch(   imagette1, im2,
                                                        searchRange  = searchRange,
                                                        searchCentre = nodePositions[ nodeNumber, 0:3 ] )
            Ffield[ nodeNumber, 0:3, 3 ] += returns['transformation']['t']
            pixelSearchCC[ nodeNumber ]   = returns['cc']

        # Either not enough data or below the threshold
        else:
            Ffield[ nodeNumber, 0:3, 3 ] = numpy.NaN
            pixelSearchCC[ nodeNumber ]  = numpy.NaN

    return { 'Ffield': Ffield,
             'pixelSearchCC': pixelSearchCC}





def subPixel(   im1, im2,
                nodePositions, halfWindowSize,
                Ffield = None,
                margin = None,
                maxIterations = None,
                minFchange = None,
                interpolationOrder = None,
                minSubVolume=None, im1mask=None,
                im2mask = None,
                greyThreshold = [ -numpy.inf, numpy.inf ],
                mpi = False):
    """
        This function handles grid-based local correlation, performing a "lucasKanade" subpixel refinement.
        Here we minimise a residual which is the difference between im1 and im2.

        Parameters
        ----------
        im1 : 3D numpy array
            A 3D image of greylevels defining a reference configuration for the pixel search

        im2 : 3D numpy array
            A deformed 3D image of greylevels

        nodePositions : nPoints*3 numpy array
            Array containing Z, Y, X positions of each point in the grid, as returned by ``makeGrid`` for example

        halfWindowSize : 3-item list or int
            Size of subvolumes to perform the image correlation on, as a data range taken either side of the voxel on which the node is placed.
            The subvolume will be 2*halfWindowSize + 1 pixels on each side.
            A general recommendation is to make this half the node spacing

        Ffield : nPoints*4*4 numpy array, optional (default = No displacement)
            Optional field of ``F`` transformation operators defined for each node

        margin : int or list, optional (default = None (use ``lucasKanade``'s default))
            Margin to extract for subpixel interpolation

        maxIterations : int, optional (default = None (use ``lucasKanade``'s default))
            Number of iterations for subpixel refinement

        minFchange : float, optional (default = None (use ``lucasKanade``'s default))
            Stop iterating when norm of F gets below this value

        interpolationOrder : int, optional (default = None (use ``lucasKanade``'s default))
            Greyscale interpolation order

        minSubVolume : int, optional (default = 50% of subvolume)
            Minimum number of pixels in a subvolume for it to be correlated (only considered in the case of im1mask).
            Expressed as a % of subvolume volume

        im1mask : 3D boolean numpy array, optional (default = None)
            A mask for the whole of im1 which is true in the zones to correlate.
            This is NOT used to mask the image, but to detect subvolumes that
            Fall inside the mask (see minSubVolume for proportion)

        im2mask : 3D boolean numpy array, optional (default = None)
            A mask for the whole of im2 which is true in the zones to correlate.
            This is IS used to mask the image, in LucasKanade

        greyThreshold : list of two floats, optional
            Threshold for the mean greylevel in each im1 subvolume.
            If the mean is below the first value or above the second value, the grid point is not correlated.
            Default = [ -inf, inf ]

        mpi : bool, optional (default = False)
            Are we being called by an MPI run?
    """

    # Check input sanity
    if type( margin ) == int or type( margin ) == float:
        margin = [ margin ]*3

    # Detect unpadded 2D image first:
    if len( im1.shape ) == 2:
        # pad them
        im1 = im1[numpy.newaxis, ...]
        im2 = im2[numpy.newaxis, ...]

    # Detect 2D images
    if im1.shape[0] == 1:   twoD = True
    else:                   twoD = False

    if interpolationOrder == 1: interpolator = 'C'
    else:                       interpolator = 'python'
    # Override interpolator for python in 2D
    if twoD:                    interpolator = 'python'

    numberOfNodes = nodePositions.shape[0]

    def getImagettes( nodeNumber, im1, im2, Ffield, nodePositions, margin, halfWindowSize, greyThreshold, im1mask, im2mask):
        # Initialise defaults
        #imagette1mask = None
        imagette2mask = None
        Finit = None
        nodeDisplacement = None

        # Make sure all components of F are real numbers
        if numpy.isfinite( Ffield[ nodeNumber ] ).sum() == 16:
            nodeDisplacement = numpy.round(Ffield[nodeNumber][0:3,-1])

            # Prepare im1 imagette -- and move it + 1 for the margin which is always 1
            subVolSlice1 = [slice( int(nodePositions[nodeNumber,0] - halfWindowSize[0] - nodeDisplacement[0] - margin[0] - 1 ), int( nodePositions[nodeNumber,0] + halfWindowSize[0] - nodeDisplacement[0] + margin[0] + 1 + 1 ) ),
                            slice( int(nodePositions[nodeNumber,1] - halfWindowSize[1] - nodeDisplacement[1] - margin[1] - 1 ), int( nodePositions[nodeNumber,1] + halfWindowSize[1] - nodeDisplacement[1] + margin[1] + 1 + 1 ) ),
                            slice( int(nodePositions[nodeNumber,2] - halfWindowSize[2] - nodeDisplacement[2] - margin[2] - 1 ), int( nodePositions[nodeNumber,2] + halfWindowSize[2] - nodeDisplacement[2] + margin[2] + 1 + 1 ) ) ]

            # Extract it
            imagette1 = im1[subVolSlice1].copy()

            # If there is a mask defined for im1, comupte the coverage of this correlation window
            # Check Mask volume condition
            if im1mask is not None:
                imagette1mask = im1mask[subVolSlice1]
                maskVolCondition = imagette1mask.sum() > minSubVolume
            else:
                #imagette1mask = None
                maskVolCondition = True

            # Check if out extracted imagette 1 is above grey threshold, if there is enough under the mask if defined, and that dispalcements are not NaN
            if numpy.nanmean( imagette1 ) > greyThreshold[0] and numpy.nanmean( imagette1 ) < greyThreshold[1] and maskVolCondition:

                # prepare slice for imagette 2 -- this is fixed + 1 for the margin which is always 1
                subVolSlice2 = [slice( int(nodePositions[nodeNumber,0] - halfWindowSize[0] - 1), int(nodePositions[nodeNumber,0] + halfWindowSize[0] + 1 + 1 ) ),
                                slice( int(nodePositions[nodeNumber,1] - halfWindowSize[1] - 1), int(nodePositions[nodeNumber,1] + halfWindowSize[1] + 1 + 1 ) ),
                                slice( int(nodePositions[nodeNumber,2] - halfWindowSize[2] - 1), int(nodePositions[nodeNumber,2] + halfWindowSize[2] + 1 + 1 ) ) ]

                imagette2 = im2[subVolSlice2].copy()

                # If there is a mask defined for im2, extract it and return it
                # Check Mask volume condition
                if im2mask is not None:
                    imagette2mask = im2mask[subVolSlice2]
                else:
                    imagette2mask = None

                # Extract initial F for correlation, remove int() part of displacement since it's already used to extract imagette2
                Finit = Ffield[nodeNumber].copy()
                Finit[0:3,-1] -= nodeDisplacement.copy()
                #print "Finit:\n", Finit, '\n'
                #Finit = numpy.eye(4)

                if ( numpy.array( imagette1.shape ) - numpy.array( imagette2.shape ) == numpy.array(margin)*2 ).all():
                    returnStatus = 2

                # Failed innermost condition -- im1 and im2 margin alignment -- this is a harsh condition
                else:
                    returnStatus = -4
                    imagette1 = None
                    imagette2 = None

            # Failed mask or greylevel condition
            else:
                returnStatus = -5
                imagette1 = None
                imagette2 = None

        # Failed non-NaN components in F
        else:
            returnStatus = -6
            imagette1 = None
            imagette2 = None

        return { 'imagette1': imagette1, 'imagette2': imagette2,
                 'imagette2mask': imagette2mask,
                 'returnStatus': returnStatus,
                 'Finit': Finit,
                 'nodeDisplacement': nodeDisplacement }



    if mpi:
        import mpi4py.MPI

        mpiComm = mpi4py.MPI.COMM_WORLD
        mpiSize = mpiComm.Get_size()
        mpiRank = mpiComm.Get_rank()
        mpiStatus = mpi4py.MPI.Status()

        boss = mpiSize-1

        numberOfWorkers = mpiSize - 1
        workersActive   = numpy.zeros( numberOfWorkers )
    else:
        numberOfWorkers = 1
        workersActive = numpy.array( [ 0 ] )

    # Check input sanity
    if type( halfWindowSize ) == int or type( halfWindowSize ) == float:
        halfWindowSize = [ halfWindowSize ]*3

    # Check minSubVolume
    if minSubVolume is None:
        minSubVolume = int( ((1+min(halfWindowSize)*2)**3) * 0.5 )
    else:
        minSubVolume = int( ((1+min(halfWindowSize)*2)**3) * minSubVolume )

    # Check F field
    if Ffield is None:
        Ffield = numpy.zeros( ( numberOfNodes, 4, 4 ) )
        for nodeNumber in xrange( numberOfNodes ): Ffield[nodeNumber] = numpy.eye( 4 )

    # Add nodes to a queue -- mostly useful for MPI
    q = Queue.Queue() 
    for node in range( numberOfNodes ): q.put( node )
    finishedNodes   = 0

    subpixelError        = numpy.zeros( ( numberOfNodes ) )
    subpixelIterations   = numpy.zeros( ( numberOfNodes ) )
    subpixelReturnStatus = numpy.zeros( ( numberOfNodes ) )
    subpixelDeltaFnorm   = numpy.zeros( ( numberOfNodes ) )

    writeReturns = False

    #print( "\n\n\tStarting Node correlation 2 (subpixel)" )
    while finishedNodes != numberOfNodes:
        # If there are workers not working, satify their requests...
        #   Note: this condition is alyas true if we are not in MPI and there are jobs to do
        if workersActive.sum() < numberOfWorkers and not q.empty():
            worker  = numpy.where( workersActive == False )[0][0]
            # Get the next node off the queue
            nodeNumber    = q.get()

            imagetteReturns = getImagettes( nodeNumber, im1, im2, Ffield, nodePositions, margin, halfWindowSize, greyThreshold, im1mask, im2mask)

            if imagetteReturns[ 'returnStatus' ] == 2:
                if mpi:
                    # build message for lukas kanade worker
                    m = {   'nodeNumber'  : nodeNumber,
                            'im1'         : imagetteReturns['imagette1'],
                            'im2'         : imagetteReturns['imagette2'],
                            'im2mask'     : imagetteReturns['imagette2mask'],
                            'Finit'       : imagetteReturns['Finit'],
                            #'FinitBinRatio' : FinitBinRatio,
                            'margin'        : 1, # see top of this file for compensation
                            'maxIterations' : maxIterations,
                            'minFchange'  : minFchange,
                            'interpolationOrder' : interpolationOrder,
                            'interpolator'  : interpolator,
                            'nodeDisplacement' : imagetteReturns['nodeDisplacement']
                        }

                    #print "\tBoss: sending node {} to worker {}".format( nodeNumber, worker )
                    mpiComm.send( m, dest=worker, tag=1 )

                    # Mark this worker as working
                    workersActive[ worker ] = True

                    # NOTE: writeReturns is defined later when receiving messages


                else: # Not MPI
                    returns = spam.DIC.correlate.lucasKanade(   imagetteReturns['imagette1'],
                                                                imagetteReturns['imagette2'],
                                                                im2mask            = imagetteReturns['imagette2mask'],
                                                                Finit              = imagetteReturns['Finit'],
                                                                margin             = 1, # see top of this file for compensation
                                                                maxIterations      = maxIterations,
                                                                minFchange         = minFchange,
                                                                interpolationOrder = interpolationOrder,
                                                                verbose            = False,
                                                                imShowProgress     = None)
                    nodeDisplacement = imagetteReturns['nodeDisplacement']
                    writeReturns = True

            else: # Regardless of MPI or single proc
                # Failed to extract imagettes or something
                subpixelError[        nodeNumber ] = numpy.inf
                subpixelIterations[   nodeNumber ] = 0
                subpixelReturnStatus[ nodeNumber ] = imagetteReturns['returnStatus']
                subpixelDeltaFnorm[   nodeNumber ] = numpy.inf
                finishedNodes                     += 1

        # Otherwise spend time looking waiting for replies from workers
        elif mpi:
            message = mpiComm.recv( source=mpi4py.MPI.ANY_SOURCE, tag=2, status=mpiStatus)
            tag     = mpiStatus.Get_tag()
            if tag == 2:
                worker          = message[0]
                nodeNumber      = message[1]
                returns         = message[2]
                nodeDisplacement= message[3]
                #print "\tBoss: received node {} from worker {}".format( nodeNumber, worker )
                workersActive[worker]   = False
                writeReturns            = True                
            else:
                print ("\tBoss: Don't recognise tag ", tag)

        # If we have new DVC returns, save them in our output matrices
        if writeReturns:
                finishedNodes          += 1 
                writeReturns = False
                # Overwrite transformation operator for this node
                Ffield[ nodeNumber ] = returns['Fcentre']
                # Add back in the translation from the initial guess
                Ffield[ nodeNumber, 0:3, 3 ] += nodeDisplacement

                subpixelError[        nodeNumber ] = returns['error']
                subpixelIterations[   nodeNumber ] = returns['iterationNumber']
                subpixelReturnStatus[ nodeNumber ] = returns['returnStatus']
                subpixelDeltaFnorm[   nodeNumber ] = returns['deltaFnorm']
                print( "\r\t\tCorrelating node {:04d} of {:04d}".format( nodeNumber+1, numberOfNodes ), end='' )
                print( "\terror={:05.0f}\titerations={:02d}\tdeltaFnorm={:0.5f}\treturnStat={:+1d}              ".format( returns['error'], returns['iterationNumber'], returns['deltaFnorm'], returns['returnStatus'] ), end='' )



    # tidy up, send message type 3 to all workers
    if mpi:
        for worker in range( numberOfWorkers ): mpiComm.send( None, dest=worker, tag=3 )

    return {    "Ffield": Ffield,
                "subpixelError": subpixelError,
                "subpixelIterations": subpixelIterations,
                "subpixelReturnStatus": subpixelReturnStatus,
                "subpixelDeltaFnorm": subpixelDeltaFnorm,
             }
