#! /usr/bin/env python
#
def r8vec_sht ( n, a  ):

#*****************************************************************************80
#
## R8VEC_SHT computes a "slow" Hartley transform of an R8VEC.
#
#  Discussion:
#
#    The discrete Hartley transform B of a set of data A is
#
#      B(I) = 1/sqrt(N) * Sum ( 0 <= J <= N-1 ) A(J) * CAS(2*PI*I*J/N)
#
#    Here, the data and coefficients are indexed from 0 to N-1.
#
#    With the above normalization factor of 1/sqrt(N), the Hartley
#    transform is its own inverse.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ralph Hartley,
#    A More Symmetrical Fourier Analysis Applied to Transmission Problems,
#    Proceedings of the Institute of Radio Engineers,
#    Volume 30, pages 144-150, 1942.
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real A(N), the data to be transformed.
#
#    Output, real B(N), the transformed data.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      theta = 2.0 * np.pi * float ( ( i * j ) % n ) / float ( n )
      b[i] = b[i] + a[j] * ( np.cos ( theta ) + np.sin ( theta ) )

  for i in range ( 0, n ):
    b[i] = b[i] / np.sqrt ( n )

  return b

def r8vec_sht_test ( ):

#*****************************************************************************80
#
## R8VEC_SHT_TEST tests R8VEC_SHT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print_part import r8vec_print_part
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 17
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'R8VEC_SHT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SHT does a forward or backward slow Hartley transform.' )
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
  d = r8vec_sht ( n, c )

  r8vec_print_part ( n, d, 1, 10, '  The Hartley coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  e = r8vec_sht ( n, d )

  r8vec_print_part ( n, e, 1, 10, '  The retrieved data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SHT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_sht_test ( )
  timestamp ( )
 
