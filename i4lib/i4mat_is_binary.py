#! /usr/bin/env python
#
def i4mat_is_binary ( m, n, x ):

#*****************************************************************************80
#
## I4MAT_IS_BINARY is true if an I4MAT only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the dimension of the array.
#
#    Input, integer X(M,N), the array to be checked.
#
#    Output, logical I4MAT_IS_BINARY, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      if ( x[i,j] != 0 and x[i,j] != 1 ):
        value = False
        break

  return value

def i4mat_is_binary_test ( ):

#*****************************************************************************80
#
## I4MAT_IS_BINARY_TEST tests I4MAT_IS_BINARY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4MAT_IS_BINARY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_IS_BINARY is TRUE if an I4MAT only contains' )
  print ( '  0 or 1 entries.' )

  m = 2
  n = 3

  x = np.array ( [ \
    [ 0, 1, 0 ], \
    [ 1, 0, 1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ \
    [ 1, 1, 1 ], \
    [ 1, 1, 1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ \
    [ 0, 1, 0 ], \
    [ 1, 2, 1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_IS_BINARY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_is_binary_test ( )
  timestamp ( )
