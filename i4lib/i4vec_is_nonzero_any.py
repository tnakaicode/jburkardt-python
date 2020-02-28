#! /usr/bin/env python
#
def i4vec_is_nonzero_any ( n, x ):

#*****************************************************************************80
#
## I4VEC_IS_NONZERO_ANY is true if any entry of an I4VEC is nonzero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2018
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
#    Output, logical VALUE, is true if any entry of X is not 0.
#
  value = any ( x[0:n] != 0 )

  return value

def i4vec_is_nonzero_any_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_NONZERO_ANY_TEST tests I4VEC_IS_NONZERO_ANY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'I4VEC_IS_NONZERO_ANY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_NONZERO_ANY is TRUE if an I4VEC contains' )
  print ( '  at least one nonzero entry.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonzero_any ( n, x ) ):
    print ( '  X has at least one nonzero entry.' )
  else:
    print ( '  X has no nonzero entries.' )

  x = np.array ( [ 0, -1, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonzero_any ( n, x ) ):
    print ( '  X has at least one nonzero entry.' )
  else:
    print ( '  X has no nonzero entries.' )

  x = np.array ( [ 1, 3, 99 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonzero_any ( n, x ) ):
    print ( '  X has at least one nonzero entry.' )
  else:
    print ( '  X has no nonzero entries.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_NONZERO_ANY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_nonzero_any_test ( )
  timestamp ( )
