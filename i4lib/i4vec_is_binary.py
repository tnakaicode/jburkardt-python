#! /usr/bin/env python
#
def i4vec_is_binary ( n, x ):

#*****************************************************************************80
#
## I4VEC_IS_BINARY is true if an I4VEC only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, integer X(N), the vector to be compared against.
#
#    Output, logical I4VEC_IS_BINARY, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, n ):

    if ( x[i] != 0 and x[i] != 1 ):
      value = False
      break

  return value

def i4vec_is_binary_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_BINARY_TEST tests I4VEC_IS_BINARY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'I4VEC_IS_BINARY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_BINARY is TRUE if an I4VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1, 0, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0, 2, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_BINARY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_binary_test ( )
  timestamp ( )
