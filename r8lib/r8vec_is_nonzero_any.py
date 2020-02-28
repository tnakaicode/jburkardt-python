#! /usr/bin/env python
#
def r8vec_is_nonzero_any ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_NONZERO_ANY is true if any entry is nonzero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
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
#    nonzero entries.
#
  import numpy as np

  value = np.any ( x[0:n] != 0.0 )

  return value

def r8vec_is_nonzero_any_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_NONZERO_ANY_TEST tests R8VEC_IS_NONZERO_ANY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_NONZERO_ANY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_NONZERO_ANY is TRUE if an R8VEC contains' )
  print ( '  any nonzero entry.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonzero_any ( n, x ) ):
    print ( '  X contains at least one nonzero entry.' )
  else:
    print ( '  X contains NO nonzero entries.' )

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonzero_any ( n, x ) ):
    print ( '  X contains at least one nonzero entry.' )
  else:
    print ( '  X contains NO nonzero entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonzero_any ( n, x ) ):
    print ( '  X contains at least one nonzero entry.' )
  else:
    print ( '  X contains NO nonzero entries.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_NONZERO_ANY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_nonzero_any_test ( )
  timestamp ( )
