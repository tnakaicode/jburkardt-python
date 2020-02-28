#! /usr/bin/env python
#
def r8poly2_rroot ( a, b, c ):

#*****************************************************************************80
#
## R8POLY2_RROOT returns the real parts of the roots of a quadratic polynomial.
#
#  Example:
#
#    A    B    C       roots              R1   R2
#   --   --   --     ------------------   --   --
#    1   -4    3     1          3          1    3
#    1    0    4     2*i      - 2*i        0    0
#    1   -6   10     3 +   i    3 -   i    3    3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the coefficients of the quadratic
#    polynomial A * X^2 + B * X + C = 0 whose roots are desired.
#    A must not be zero.
#
#    Output, real R1, R2, the real parts of the roots
#    of the polynomial.
#
  import numpy as np
  from r8_sign import r8_sign
  from sys import exit

  if ( a == 0.0 ):
    print ( '' )
    print ( 'R8POLY2_RROOT - Fatal error!' )
    print ( '  The coefficient A is zero.' )
    exit ( 'R8POLY2_RROOT - Fatal error!' )

  disc = b * b - 4.0 * a * c

  if ( 0.0 <= disc ):
    q = ( b + r8_sign ( b ) * np.sqrt ( disc ) )
    r1 = - 0.5 * q / a
    r2 = - 2.0 * c / q
  else:
    r1 = - b / 2.0 / a
    r2 = - b / 2.0 / a

  return r1, r2

def r8poly2_rroot_test ( ):

#*****************************************************************************80
#
## R8POLY2_RROOT_TEST tests R8POLY2_RROOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  a_test = np.array ( [  2.0,    1.0,  1.0, 1.0,  1.0 ] )
  b_test = np.array ( [ -2.0,  -20.0, -2.0, 0.0, -6.0 ] )
  c_test = np.array ( [ -24.0, 100.0, 10.0, 1.0, 10.0 ] )
 
  print ( '' )
  print ( 'R8POLY2_RROOT_TEST' )
  print ( '  R8POLY2_RROOT finds the real parts of quadratic equation roots.' )
  print ( '' )
  print ( '         A         B         C     R1         R2' )
  print ( '' )

  for test in range ( 0, test_num ):

    a = a_test[test]
    b = b_test[test]
    c = c_test[test]

    r1, r2 = r8poly2_rroot ( a, b, c )
 
    print ( '  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f' % ( a, b, c, r1, r2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY2_RROOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly2_rroot_test ( )
  timestamp ( )

