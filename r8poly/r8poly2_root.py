#! /usr/bin/env python3
#
def r8poly2_root ( a, b, c ):

#*****************************************************************************80
#
## R8POLY2_ROOT returns the two roots of a quadratic polynomial.
#
#  Discussion:
#
#    The polynomial has the form:
#
#      A * X^2 + B * X + C = 0 
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
#    Input, real A, B, C, the coefficients of the polynomial.
#    A must not be zero.
#
#    Output, complex R1, R2, the roots of the polynomial, which
#    might be real and distinct, real and equal, or complex conjugates.
#
  import cmath
  import numpy as np
  from r8_sign import r8_sign
  from sys import exit

  if ( a == 0.0 ):
    print ( '' )
    print ( 'R8POLY2_ROOT - Fatal error!' )
    print ( '  The coefficient A is zero.' )
    exit ( 'R8POLY2_ROOT - Fatal error!' )

  disc = b * b - 4.0 * a * c
  q = - 0.5 * ( b + r8_sign ( b ) * cmath.sqrt ( disc ) )
  r1 = q / a
  r2 = c / q

  return r1, r2

def r8poly2_root_test ( ):

#*****************************************************************************80
#
## R8POLY2_ROOT_TEST tests R8POLY2_ROOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 3

  a_test = np.array ( [ 2.0, 1.0, 1.0 ] )
  b_test = np.array ( [ -2.0, -20.0, -2.0 ] )
  c_test = np.array ( [ -24.0, 100.0, 10.0 ] )
 
  print ( '' )
  print ( 'R8POLY2_ROOT_TEST' )
  print ( '  R8POLY2_ROOT finds quadratic equation roots.' )
  print ( '' )
  print ( '         A         B         C   R1.real   R1.imag   R2.real   R2.imag' )
  print ( '' )

  for test in range ( 0, test_num ):

    a = a_test[test]
    b = b_test[test]
    c = c_test[test]

    r1, r2 = r8poly2_root ( a, b, c )
 
    print ( '  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f' \
      % ( a, b, c, r1.real, r1.imag, r2.real, r2.imag ) )
#
#  Terminate.
# 
  print ( '' )
  print ( 'R8POLY2_ROOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly2_root_test ( )
  timestamp ( )

