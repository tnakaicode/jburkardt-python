#! /usr/bin/env python
#
def r8vec_is_ascending ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_ASCENDING determines if an R8VEC is (weakly) ascending.
#
#  Example:
#
#    X = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.5, 9.8 )
#
#    value = true
#
#    The sequence is not required to be strictly ascending.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the array.
#
#    Input, real X(N), the array to be examined.
#
#    Output, logical VALUE, is true if the entries of X ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i+1] < x[i] ):
      value = False
      break

  return value

def r8vec_is_ascending_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_ASCENDING_TEST tests R8VEC_IS_ASCENDING.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_ASCENDING_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_ASCENDING is TRUE if the entries of an R8VEC' )
  print ( '  are ascending.' )

  n = 4

  x = np.array ( [ 1.0, 2.0, 0.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending ( n, x ) ):
    print ( '  X is ascending.' )
  else:
    print ( '  X is NOT ascending.' )

  x = np.array ( [ 1.0, 2.0, 2.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending ( n, x ) ):
    print ( '  X is ascending.' )
  else:
    print ( '  X is NOT ascending.' )

  x = np.array ( [ 1.0, 2.0, 4.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending ( n, x ) ):
    print ( '  X is ascending.' )
  else:
    print ( '  X is NOT ascending.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_ASCENDING_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_ascending_test ( )
  timestamp ( )

