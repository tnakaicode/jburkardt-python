#! /usr/bin/env python
#
def r8vec_sign3_running ( n, v ):

#*****************************************************************************80
#
## R8VEC_SIGN3_RUNNING computes the running threeway sign of an R8VEC.
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
#    Output, real S(N+1), the running threeway sign.  S(I) is:
#    -1 if the sum of the first I-1 values in V is negative
#     0, if zero
#    +1, if positive.
#
  import numpy as np

  s = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    s[i] = s[i-1] + v[i-1]

  for i in range ( 0, n + 1 ):
    if ( s[i] < 0.0 ):
      s[i] = -1.0
    elif ( s[i] == 0.0 ):
      s[i] = 0.0
    else:
      s[i] = +1.0

  return s

def r8vec_sign3_running_test ( ):

#*****************************************************************************80
#
## R8VEC_SIGN3_RUNNING_TEST tests R8VEC_SIGN3_RUNNING.
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
  print ( 'R8VEC_SIGN3_RUNNING_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SIGN3_RUNNING returns the running sign3 of an R8VEC.' )

  n = 10
  a = -5.0
  b = +10.0
  seed = 123456789

  r, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, r, '  Random R8VEC:' )

  s = r8vec_sign3_running ( n, r )

  r8vec_print ( n + 1, s, '  Running sign3:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SIGN3_RUNNING_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_sign3_running_test ( )
  timestamp ( )
