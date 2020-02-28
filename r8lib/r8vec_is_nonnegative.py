#! /usr/bin/env python
#
def r8vec_is_nonnegative ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_NONNEGATIVE is true if an R8VEC only contains nonnegative entries.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2018
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
#    nonnegative entries.
#
  import numpy as np

  value = np.all ( 0.0 <= x[0:n] )

  return value

def r8vec_is_nonnegative_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_NONNEGATIVE_TEST tests R8VEC_IS_NONNEGATIVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_NONNEGATIVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_NONNEGATIVE is TRUE if an R8VEC only contains' )
  print ( '  nonnegative entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonnegative ( n, x ) ):
    print ( '  X contains only nonnegative entries.' )
  else:
    print ( '  X does NOT contain only nonnegative entries.' )

  x = np.array ( [ -1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonnegative ( n, x ) ):
    print ( '  X contains only nonnegative entries.' )
  else:
    print ( '  X does NOT contain only nonnegative entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonnegative ( n, x ) ):
    print ( '  X contains only nonnegative entries.' )
  else:
    print ( '  X does NOT contain only nonnegative entries.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_NONNEGATIVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_nonnegative_test ( )
  timestamp ( )
