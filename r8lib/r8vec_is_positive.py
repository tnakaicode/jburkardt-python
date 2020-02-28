#! /usr/bin/env python
#
def r8vec_is_positive ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_POSITIVE is true if an R8VEC only contains  strictly positive entries.
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
#    strictly positive entries.
#
  import numpy as np

  value = np.all ( 0.0 < x[0:n] )

  return value

def r8vec_is_positive_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_POSITIVE_TEST tests R8VEC_IS_POSITIVE.
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
  print ( 'R8VEC_IS_POSITIVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_POSITIVE is TRUE if an R8VEC only contains' )
  print ( '  strictly positive entries.' )

  n = 3

  x = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_positive ( n, x ) ):
    print ( '  X contains only positive entries.' )
  else:
    print ( '  X does NOT contain only positive entries.' )

  x = np.array ( [ 2.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_positive ( n, x ) ):
    print ( '  X contains only positive entries.' )
  else:
    print ( '  X does NOT contain only positive entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_positive ( n, x ) ):
    print ( '  X contains only positive entries.' )
  else:
    print ( '  X does NOT contain only positive entries.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_POSITIVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_positive_test ( )
  timestamp ( )
