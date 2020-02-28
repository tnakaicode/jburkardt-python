#! /usr/bin/env python
#
def r8vec_mean_running ( n, v ):

#*****************************************************************************80
#
## R8VEC_MEAN_RUNNING computes the running mean of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of items.
#
#    Input, real V(N), the data.
#
#    Output, real A(N+1), the running means.  A(I) is the average value
#    of the first I-1 values in V.
#
  import numpy as np

  a = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    a[i] = a[i-1] + v[i-1]
#
#  Average.
#
  for i in range ( 1, n + 1 ):
    a[i] = a[i] / float ( i )

  return a

def r8vec_mean_running_test ( ):

#*****************************************************************************80
#
## R8VEC_MEAN_RUNNING_TEST tests R8VEC_MEAN_RUNNING.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_MEAN_RUNNING_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MEAN_RUNNING returns the running means of an R8VEC.' )

  n = 10
  a = -5.0
  b = +10.0
  seed = 123456789

  r, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, r, '  Random R8VEC:' )

  s = r8vec_mean_running ( n, r )

  r8vec_print ( n + 1, s, '  Running means:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MEAN_RUNNING_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_mean_running_test ( )
  timestamp ( )
