#! /usr/bin/env python
#
def r8vec_eq ( n, a, b ):

#*****************************************************************************80
#
## I4VEC_EQ is TRUE if two R8VEC's are equal.
#
#  Example:
#
#    A = ( 9, 7, 7, 3, 2, 1, -8 )
#    B = ( 9, 7, 6, 3, 2, 1, -8 )
#    R8VEC_EQ = FALSE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the arrays.
#
#    Input, real A(N), B(N), the arrays to be compared.
#
#    Output, logical VALUE, is TRUE if the arrays are equal.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( a[i] != b[i] ):
      value = False
      break

  return value

def r8vec_eq_test ( ):

#*****************************************************************************80
#
## R8VEC_EQ_TEST tests R8VEC_EQ.
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
  from r8vec2_print import r8vec2_print

  n = 4
  test_num = 4

  a_test = np.array ( [ \
    [ 1.1, 3.2, 2.3, 4.4 ], \
    [ 2.1, 2.2, 2.3, 2.4 ], \
    [ 1.1, 2.2, 2.3, 4.4 ], \
    [ 1.1, 2.2, 3.3, 4.4 ] ], dtype = np.float64 )

  b_test = np.array ( [ \
    [ 1.1, 3.2, 2.3, 4.4 ], \
    [ 2.1, 2.2, 1.3, 2.4 ], \
    [ 4.1, 1.2, 1.3, 3.4 ], \
    [ 1.1, 2.2, 3.3, 4.4 ] ], dtype = np.float64 )

  print ( '' )
  print ( 'R8VEC_EQ_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_EQ is TRUE if two R8VECs are equal.' )

  for i in range ( 0, test_num ):

    a = a_test[i,0:n].copy ( )
    b = b_test[i,0:n].copy ( )

    r8vec2_print ( n, a, b, '  Vectors A and B:' )

    value = r8vec_eq ( n, a, b )

    print ( '  R8VEC_EQ(A,B) = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_EQ_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_eq_test ( )
  timestamp ( )
