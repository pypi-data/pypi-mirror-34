#include <stdio.h>
#include <math.h>
#include <iostream>
#include "checkPointInsideTetrahedron.hpp"
#include <Eigen/Dense>

 
char checkPointInsideTetrahedron( short Z, short Y, short X, Eigen::Matrix<float, 4, 3> pTetMatrix )
{
//     printf( "%i %i %i\n-------\n", Z, Y, X );
//     for ( unsigned char i = 0; i < 4; i++ )
//     {
//       for ( unsigned char j = 0; j < 3; j++ )
//       {
//           printf( "%f ", pTetMatrix(i,j] );
//       }
//       printf( "\n" );
//     }
//     printf( "\n" );
    
    Eigen::Matrix4f jacTet;
    jacTet(0,0) = 1;
    jacTet(1,0) = 1;
    jacTet(2,0) = 1;
    jacTet(3,0) = 1;
    
    /* fill in jacTet, which is the jacobian of the tetrahedron (first row padded with ones) */
    for ( unsigned char i = 0; i < 4; i++ )
    {
        for ( unsigned char j = 0; j < 3; j++ )
        {
            jacTet(i,j+1) = pTetMatrix(i,j);
        }
    }
    
    /* Copy jacTet into tmp, and copy z,y,x overwriting a different line (this is the outside loop, l)
     * then: calculate the determinant and if negative, return false */
//     double tmp[4][4];
    Eigen::Matrix4f tmp;
    for ( unsigned char l = 0; l < 4; l++ )
    {
        for ( unsigned char i = 0; i < 4; i++ )
        {
            for ( unsigned char j = 0; j < 4; j++ )
            {
                if ( i == l )
                {
                    tmp(i,0) = 1;
                    tmp(i,1) = Z;
                    tmp(i,2) = Y;
                    tmp(i,3) = X;
                }
                else
                {
                    tmp(i,j) = jacTet(i,j);
                }
            }
        }
        /* computer determinant, and if negative return false */
//         if ( det4( tmp ) < 0 ) return 0;
        if ( tmp.determinant() < 0 ) return 0;
    }
      
    /* if we survived, all the dets were positive, return 1 */
    return 1;
}
