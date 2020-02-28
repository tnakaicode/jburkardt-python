#! /usr/bin/env python
#
def i4vec_is_odd_all ( n, x ):

#*****************************************************************************80
#
## I4VEC_IS_ODD_ALL is true if all entries of an I4VEC are odd.
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
#    Input, integer X(N), the vector to be compared against.
#
#    Output, logical VALUE, is true if all entries of X are odd.
#
  value = all ( x[0:n] % 2 == 1 )

  return value

def i4vec_is_odd_all_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_ODD_ALL_TEST tests I4VEC_IS_ODD_ALL.
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
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'I4VEC_IS_ODD_ALL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_ODD_ALL is TRUE if an I4VEC only contains' )
  print ( '  odd entries.' )

  n = 3

  x = np.array ( [ 1, 5, 19 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_all ( n, x ) ):
    print ( '  X is only odd values.' )
  else:
    print ( '  X is NOT only odd values.' )

  x = np.array ( [ 3, 2, 77 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_all ( n, x ) ):
    print ( '  X is only odd values.' )
  else:
    print ( '  X is NOT only odd values.' )

  x = np.array ( [ 2, 4, 88 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_all ( n, x ) ):
    print ( '  X is only odd values.' )
  else:
    print ( '  X is NOT only odd values.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_ODD_ALL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_odd_all_test ( )
  timestamp ( )


