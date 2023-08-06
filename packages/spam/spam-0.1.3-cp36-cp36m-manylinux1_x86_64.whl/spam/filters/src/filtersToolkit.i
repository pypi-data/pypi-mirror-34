/* File: filtersToolkit.i */

%module filtersToolkit

%{
#define SWIG_FILE_WITH_INIT
#include "movingFiltersToolkit.hpp"
%}

%include "numpy.i"

%init %{
import_array();
%}

/* WARNING, these names here must be exactly the same as the hpp file (not necessarily the cpp) */
%apply (int DIM1, int DIM2, int DIM3, float* IN_ARRAY3)      { ( int nz1, int ny1, int nx1, float *imIn ) };
%apply (int DIM1, int DIM2, int DIM3, float* INPLACE_ARRAY3) { ( int nz2, int ny2, int nx2, float *imOu ) };
%apply (int DIM1, int DIM2, int DIM3, float* IN_ARRAY3)      { ( int nz3, int ny3, int nx3, float *stEl ) };

%include "movingFiltersToolkit.hpp"
