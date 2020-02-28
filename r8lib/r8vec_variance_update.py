#! /usr/bin/env python
#
def r8vec_variance_update ( nm1, mean_nm1, variance_nm1, xn ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_UPDATE updates the variance of an R8VEC with one new value.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NM1, the number of entries in the old vector.
#
#    Input, real MEAN_NM1, the mean of the old vector.
#
#    Input, real VARIANCE_NM1, the variance of the old vector.
#
#    Input, real XN, the new N-th entry of the vector.
#
#    Output, integer N, the number of entries in the new vector.
#
#    Output, real MEAN_N, the mean of the new vector.
#
#    Output, real VARIANCE_N, the variance of the new vector.
#
  import numpy as np

  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
    variance_n = 0.0
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n
    variance_n = ( variance_nm1 * nm1 + ( xn - mean_nm1 ) * ( xn - mean_n ) ) / n

  return n, mean_n, variance_n

def r8vec_variance_update_test ( ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_UPDATE_TEST tests R8VEC_VARIANCE_UPDATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8_uniform_01 import r8_uniform_01
  from r8vec_variance import r8vec_variance

  print ( '' )
  print ( 'R8VEC_VARIANCE_UPDATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_VARIANCE_UPDATE updates the variance of a vector' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R                VARIANCE          VARIANCE_UPDATE' )
  print ( '' )

  n_max = 10

  a = np.zeros ( n_max )
  mean_n = 0.0
  variance_n = 0.0
  seed = 123456789

  for i in range ( 1, n_max ):

    r, seed = r8_uniform_01 ( seed )
    a[i-1] = r
    variance = r8vec_variance ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    variance_nm1 = variance_n
    n, mean_n, variance_n = r8vec_variance_update ( nm1, mean_nm1, variance_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, variance, variance_n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_VARIANCE_UPDATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_variance_update_test ( )
  timestamp ( )

