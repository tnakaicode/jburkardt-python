#! /usr/bin/env python
#
def r8vec_is_negative ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_NEGATIVE is true if an R8VEC only contains negative entries.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2018
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
#    negative entries.
#
  import numpy as np

  value = np.all ( x[0:n] < 0.0 )

  return value

def r8vec_is_negative_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_NEGATIVE_TEST tests R8VEC_IS_NEGATIVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_NEGATIVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_NEGATIVE is TRUE if an R8VEC only contains' )
  print ( '  negative entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative ( n, x ) ):
    print ( '  X contains only negative entries.' )
  else:
    print ( '  X does NOT contain only negative entries.' )

  x = np.array ( [ -1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative ( n, x ) ):
    print ( '  X contains only negative entries.' )
  else:
    print ( '  X does NOT contain only negative entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative ( n, x ) ):
    print ( '  X contains only negative entries.' )
  else:
    print ( '  X does NOT contain only negative entries.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_NEGATIVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_negative_test ( )
  timestamp ( )
