#include <stdio.h>
#include <math.h>
#include <cmath>
#include <iostream>
//#include <stdlib.h> /* abs */
#include "movingFiltersToolkit.hpp"
// #include <Eigen/Dense>

/* 2017-05-23 Emmanuel Roubin
 *

 */

/*              Image sizes, ZYX and images*/
void average(   int nz1,   int ny1,  int nx1, float* imIn,	\
		int nz2,   int ny2,  int nx2, float* imOu,	\
		int nz3,   int ny3,  int nx3, float* stEl )
{
  // int variable to build index to 1D-images from x,y,z coordinates

  // get the box of the image
  unsigned zMin = nz3/2; unsigned zMax = nz1-nz3/2;
  unsigned yMin = ny3/2; unsigned yMax = ny1-ny3/2;
  unsigned xMin = nx3/2; unsigned xMax = nx1-nx3/2;

  // std::cout << "START C++ moving average" << std::endl;
  // std::cout << "z range: " << zMin << " - " << zMax << std::endl;
  // std::cout << "y range: " << yMin << " - " << yMax << std::endl;
  // std::cout << "x range: " << xMin << " - " << xMax << std::endl;


  /* loop over the structural element to get the sum */
  unsigned idSt = 0;
  float stEl_sum = 0.0;
  for( int k=-nz3/2; k<=nz3/2; k++ ) {
    for( int j=-ny3/2; j<=ny3/2; j++ ) {
      for( int i=-nx3/2; i<=nx3/2; i++ ) {
	stEl_sum += stEl[ idSt ];
	idSt++;
      }
    }
  }
  
  // loop over the image
  for( unsigned z=zMin; z<zMax; z++ ) {
    for( unsigned y=yMin; y<yMax; y++ ) {
      for( unsigned x=xMin; x<xMax; x++ ) {

	// index of output image
	unsigned idImOu = z * ny1 * nx1 + y * nx1 + x;

	// tmp voxel values of the output and
	float im_sum = 0.0;
	//float im_sum2 = 0.0;

	// loop over the structural element
	unsigned idSt = 0;
	for( int k=-nz3/2; k<=nz3/2; k++ ) {
	  for( int j=-ny3/2; j<=ny3/2; j++ ) {
	    for( int i=-nx3/2; i<=nx3/2; i++ ) {
	      unsigned idImIn = ( z+k ) * ny1 * nx1 + ( y+j ) * nx1 + ( x+i );
	      im_sum += stEl[ idSt ] * imIn[ idImIn ];
	      //im_sum2 += (stEl[ idSt ] * imIn[ idImIn ])*(stEl[ idSt ] * imIn[ idImIn ]);
	      idSt++;
	    }
	  }
	}

	imOu[ idImOu ] = im_sum/stEl_sum;
	//imOu[ idImOu ] = (im_sum2 - im_sum * im_sum/stEl_sum)/stEl_sum;

      }
    }
  }

  //std::cout << "STOP C++ moving average" << std::endl;
}


//int  sgn(double d){
  // float eps = 0.0000000000000000000001;
  // return d<-eps?-1:d>eps;
  // }


void variance(  int nz1,   int ny1,  int nx1, float* imIn,	\
		int nz2,   int ny2,  int nx2, float* imOu,	\
		int nz3,   int ny3,  int nx3, float* stEl )
{
  // int variable to build index to 1D-images from x,y,z coordinates

  // get the box of the image
  unsigned zMin = nz3/2; unsigned zMax = nz1-nz3/2;
  unsigned yMin = ny3/2; unsigned yMax = ny1-ny3/2;
  unsigned xMin = nx3/2; unsigned xMax = nx1-nx3/2;

  // std::cout << "\nSTART C++ moving variance" << std::endl;
  // std::cout << "z range: " << zMin << " - " << zMax << std::endl;
  // std::cout << "y range: " << yMin << " - " << yMax << std::endl;
  // std::cout << "x range: " << xMin << " - " << xMax << std::endl;


  /* loop over the structural element to get the sum */
  unsigned idSt = 0;
  float stEl_sum = 0.0;
  for( int k=-nz3/2; k<=nz3/2; k++ ) {
    for( int j=-ny3/2; j<=ny3/2; j++ ) {
      for( int i=-nx3/2; i<=nx3/2; i++ ) {
	stEl_sum += stEl[ idSt ];
	idSt++;
      }
    }
  }

  // loop over the image
  for( unsigned z=zMin; z<zMax; z++ ) {
    for( unsigned y=yMin; y<yMax; y++ ) {
      for( unsigned x=xMin; x<xMax; x++ ) {

	// index of output image
	unsigned idImOu = z * ny1 * nx1 + y * nx1 + x;

	// tmp voxel values of the output and
	float im_sum = 0.0;
	float im_sum2 = 0.0;

	// loop over the structural element
	unsigned idSt = 0;
	for( int k=-nz3/2; k<=nz3/2; k++ ) {
	  for( int j=-ny3/2; j<=ny3/2; j++ ) {
	    for( int i=-nx3/2; i<=nx3/2; i++ ) {
	      unsigned idImIn = ( z+k ) * ny1 * nx1 + ( y+j ) * nx1 + ( x+i );
	      im_sum += stEl[ idSt ] * imIn[ idImIn ];
	      im_sum2 += (stEl[ idSt ] * imIn[ idImIn ])*(stEl[ idSt ] * imIn[ idImIn ]);
	      idSt++;
	    }
	  }
	}

	imOu[ idImOu ] = (im_sum2 - im_sum * im_sum/stEl_sum)/stEl_sum;
      }
    }
  }

  // std::cout << "STOP C++ moving variance" << std::endl;
  // std::cout << "abs(-min) = " << std::abs(-4.62e-07) << std::endl;
  // std::cout << " \n*** that was Olga's 1rst C++ function :) " << std::endl;
}
