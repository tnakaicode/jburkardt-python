#! /usr/bin/env python
#
def i4vec_is_equal ( n, a, b ):

#*****************************************************************************80
#
## I4VEC_IS_EQUAL is TRUE if two I4VEC's are equal.
#
#  Example:
#
#    A = ( 9, 7, 7, 3, 2, 1, -8 )
#    B = ( 9, 7, 6, 3, 2, 1, -8 )
#    I4VEC_IS_EQUAL = FALSE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the arrays.
#
#    Input, integer A(N), B(N), the arrays to be compared.
#
#    Output, logical VALUE, is TRUE if the arrays are equal.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( a[i] != b[i] ):
      value = False
      break

  return value

def i4vec_is_equal_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_EQUAL_TEST tests I4VEC_IS_EQUAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec2_print import i4vec2_print

  n = 4
  test_num = 4

  a_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 2, 2 ], \
    [ 1, 2, 2, 4 ], \
    [ 1, 2, 3, 4 ] ] )

  b_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 1, 2 ], \
    [ 4, 1, 1, 3 ], \
    [ 1, 2, 3, 4 ] ] )

  print ( '' )
  print ( 'I4VEC_IS_EQUAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_EQUAL is TRUE if two I4VECs are equal.' )

  for i in range ( 0, test_num ):

    a = a_test[i,0:n].copy ( )
    b = b_test[i,0:n].copy ( )

    i4vec2_print ( n, a, b, '  Vectors A and B:' )

    value = i4vec_is_equal ( n, a, b )

    print ( '  I4VEC_IS_EQUAL(A,B) = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_EQUAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_equal_test ( )
  timestamp ( )
