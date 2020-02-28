#! /usr/bin/env python
#
def i4vec_is_zero ( n, x ):

#*****************************************************************************80
#
## I4VEC_IS_ZERO is true if all entries of an I4VEC are 0
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
#    Output, logical VALUE, is true if all entries of X are 0.
#
  value = all ( x[0:n] == 0 )

  return value

def i4vec_is_zero_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_ZERO_TEST tests I4VEC_IS_ZERO.
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
  print ( 'I4VEC_IS_ZERO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_ZERO is TRUE if an I4VEC only contains' )
  print ( '  0 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_zero ( n, x ) ):
    print ( '  X is only zeros.' )
  else:
    print ( '  X is NOT only zeros.' )

  x = np.array ( [ 0, 1, 2 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_zero ( n, x ) ):
    print ( '  X is only zeros.' )
  else:
    print ( '  X is NOT only zeros.' )

  x = np.array ( [ 1, 1, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_zero ( n, x ) ):
    print ( '  X is only zeros.' )
  else:
    print ( '  X is NOT only zeros.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_ZERO_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_zero_test ( )
  timestamp ( )


