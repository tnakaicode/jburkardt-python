#! /usr/bin/env python
#
def i4vec_is_lt_any ( n, a, b ):

#*****************************************************************************80
#
## I4VEC_IS_LT_ANY: ( any ( A < B ) ) for I4VEC's.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
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
#    Input, integer N, the number of entries.
#
#    Input, integer A(N), the first vector.
#
#    Input, integer B(N), the second vector.
#
#    Output, logical I4VEC_IS_LT_ANY is 1 if any entry
#    of A is less than the corresponding entry of B.
#
  import numpy as np

  value = np.any ( a[0:n] < b[0:n] )

  return value

def i4vec_is_lt_any_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_LT_ANY_TEST tests I4VEC_IS_LT_ANY.
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
  print ( 'I4VEC_IS_BINARY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_BINARY is TRUE if an I4VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  y = np.array ( [ 1, 2, 3 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  i4vec_transpose_print ( n, y, '  Y:' )
  if ( i4vec_is_lt_any ( n, x, y ) ):
    print ( '  Some X is < some Y.' )
  else:
    print ( '  NO X is < any Y.' )

  x = np.array ( [ 3, 2, 1 ] )
  y = np.array ( [ 1, 2, 3 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  i4vec_transpose_print ( n, y, '  Y:' )
  if ( i4vec_is_lt_any ( n, x, y ) ):
    print ( '  Some X is < some Y.' )
  else:
    print ( '  NO X is < any Y.' )

  x = np.array ( [ 2, 3, 4 ] )
  y = np.array ( [ 1, 2, 3 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  i4vec_transpose_print ( n, y, '  Y:' )
  if ( i4vec_is_lt_any ( n, x, y ) ):
    print ( '  Some X is < some Y.' )
  else:
    print ( '  NO X is < any Y.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_LT_ANY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_lt_any_test ( )
  timestamp ( )
