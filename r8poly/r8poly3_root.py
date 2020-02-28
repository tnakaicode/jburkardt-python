#! /usr/bin/env python3
#
def r8poly3_root ( a, b, c, d ):

#*****************************************************************************80
#
## R8POLY3_ROOT returns the three roots of a cubic polynomial.
#
#  Discussion:
#
#    The polynomial has the form
#
#      A * X^3 + B * X^2 + C * X + D = 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, D, the coefficients of the polynomial.
#    A must not be zero.
#
#    Output, complex R1, R2, R3, the roots of the polynomial, which
#    will include at least one real root.
#
  import numpy as np
  from r8_sign import r8_sign
  from sys import exit

  if ( a == 0.0 ):
    print ( '' )
    print ( 'R8POLY3_ROOT - Fatal error!' )
    print ( '  A must not be zero!' )
    exit ( 'R8POLY3_ROOT - Fatal error!' )

  q = ( ( b / a ) ** 2 - 3.0 * ( c / a ) ) / 9.0

  r = ( 2.0 * ( b / a ) ** 3 - 9.0 * ( b / a ) * ( c / a ) \
      + 27.0 * ( d / a ) ) / 54.0

  if ( r * r < q * q * q ):

    theta = np.arccos ( r / np.sqrt ( q ** 3 ) )
    r1 = -2.0 * np.sqrt ( q ) * np.cos (   theta                 / 3.0 )
    r2 = -2.0 * np.sqrt ( q ) * np.cos ( ( theta + 2.0 * np.pi ) / 3.0 )
    r3 = -2.0 * np.sqrt ( q ) * np.cos ( ( theta + 4.0 * np.pi ) / 3.0 )

  elif ( q * q * q <= r * r ):

    temp = -r + np.sqrt ( r ** 2 - q ** 3 )
    s1 = r8_sign ( temp ) * ( abs ( temp ) ) ** ( 1.0 / 3.0 )

    temp = -r - np.sqrt ( r ** 2 - q ** 3 )
    s2 = r8_sign ( temp ) * ( abs ( temp ) ) ** ( 1.0 / 3.0 )

    r1 = s1 + s2
    r2 = -0.5 * ( s1 + s2 ) + 0.5j * np.sqrt ( 3.0 ) * ( s1 - s2 )
    r3 = -0.5 * ( s1 + s2 ) - 0.5j * np.sqrt ( 3.0 ) * ( s1 - s2 )

  r1 = r1 - b / ( 3.0 * a )
  r2 = r2 - b / ( 3.0 * a )
  r3 = r3 - b / ( 3.0 * a )

  return r1, r2, r3

def r8poly3_root_test ( ):

#*****************************************************************************80
#
## R8POLY3_ROOT_TEST tests R8POLY3_ROOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  a_test = np.array ( [ 1.0, 9.0, 1.0, 1.0 ] )
  b_test = np.array ( [ -6.0, -36.0, -5.0, -8.0  ] )
  c_test = np.array ( [ 11.0, 54.0, 8.0, 25.0  ] )
  d_test = np.array ( [ -6.0, -27.0, -4.0, -26.0  ] )
#
#  1: Three distinct real roots, 1, 2, 3.
#  2: One repeated real root, 1.5, 1.5, 1.5.
#  3: Two real roots, one repeated, 1, 2, 2.
#  4: One real root, a complex conjugate pair, 2, 3+2I, 3-2I.
#
  print ( '' )
  print ( 'R8POLY3_ROOT_TEST' )
  print ( '  R8POLY3_ROOT finds roots of cubic equations.' )
  print ( '' )
 
  for test in range ( 0, test_num ):
 
    a = a_test[test]
    b = b_test[test]
    c = c_test[test]
    d = d_test[test]

    print ( '' )
    print ( '  Polynomial coefficients:' )
    print ( '' )
    print ( '  A = %f, B = %f, C = %f, D = %f' % ( a, b, c, d ) )
 
    r1, r2, r3 = r8poly3_root ( a, b, c, d )
 
    print ( '' )
    print ( '  Roots:' )
    print ( '' )
    print ( '  %f  %f' % ( r1.real, r1.imag ) )
    print ( '  %f  %f' % ( r2.real, r2.imag ) )
    print ( '  %f  %f' % ( r3.real, r3.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY3_ROOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly3_root_test ( )
  timestamp ( )
 
