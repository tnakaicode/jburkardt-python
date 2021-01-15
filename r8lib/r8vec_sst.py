#! /usr/bin/env python
#
def r8vec_sst ( n, x ):

#*****************************************************************************80
#
## R8VEC_SST computes a "slow" sine transform of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 1 <= I <= N,
#
#      Y(I) = Sum ( 1 <= J <= N ) X(J) * sin ( PI * I * J / ( N + 1 ) )
#
#    Applying the routine twice in succession should yield the original data,
#    multiplied by N / 2.  This is a good check for correctness and accuracy.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real X(N), the data sequence.
#
#    Output, real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      y[j] = y[j] + 2.0 * x[i] \
        * np.sin ( float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( n + 1 ) )

  return y

def r8vec_sst_test ( ):

#*****************************************************************************80
#
## R8VEC_SST_TEST tests R8VEC_SST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print_part import r8vec_print_part
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 256
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'R8VEC_SST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SST does a forward or backward slow sine transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  seed = 123456789

  c, seed = r8vec_uniform_ab ( n, alo, ahi, seed )

  r8vec_print_part ( n, c, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  d = r8vec_sst ( n, c )

  r8vec_print_part ( n, d, 1, 10, '  The sine coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  e = r8vec_sst ( n, d )

  for i in range ( 0, n ):
    e[i] = e[i] / 2.0 / float ( n + 1 )

  r8vec_print_part ( n, e, 1, 10, '  The retrieved data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SST_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_sst_test ( )
  timestamp ( )
 
