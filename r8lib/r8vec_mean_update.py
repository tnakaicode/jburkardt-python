#! /usr/bin/env python
#
def r8vec_mean_update ( nm1, mean_nm1, xn ):

#*****************************************************************************80
#
## R8VEC_MEAN_UPDATE updates the mean of an R8VEC with one new value.
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
#    Input, real XN, the new N-th entry of the vector.
#
#    Output, integer N, the number of entries in the new vector.
#
#    Output, real MEAN_N, the mean of the new vector.
#
  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n

  return n, mean_n

def r8vec_mean_update_test ( ):

#*****************************************************************************80
#
## R8VEC_MEAN_UPDATE_TEST tests R8VEC_MEAN_UPDATE.
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
  from r8vec_mean import r8vec_mean

  print ( '' )
  print ( 'R8VEC_MEAN_UPDATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MEAN_UPDATE updates the mean of a vector' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R               MEAN         MEAN_UPDATE' )
  print ( '' )

  n_max = 10
  a = np.zeros ( n_max )
  seed = 123456789
  mean_n = 0.0

  for i in range ( 1, n_max ):

    r, seed = r8_uniform_01 ( seed )
    a[i-1] = r
    mean = r8vec_mean ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    n, mean_n = r8vec_mean_update ( nm1, mean_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, mean, mean_n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MEAN_UPDATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_mean_update_test ( )
  timestamp ( )

