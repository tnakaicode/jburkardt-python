#! /usr/bin/env python
#
def r8vec_is_binary ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_BINARY is true if an R8VEC only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, real X(N), the vector to be compared against.
#
#    Output, real VALUE, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, n ):

    if ( x[i] != 0.0 and x[i] != 1.0 ):
      value = False
      break

  return value

def r8vec_is_binary_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_BINARY_TEST tests R8VEC_IS_BINARY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_BINARY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_BINARY is TRUE if an R8VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0.0, 2.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_BINARY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_binary_test ( )
  timestamp ( )
