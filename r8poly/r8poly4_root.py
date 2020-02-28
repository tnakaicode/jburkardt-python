#! /usr/bin/env python3
#
def r8poly4_root ( a, b, c, d, e ):

#*****************************************************************************80
#
## R8POLY4_ROOT returns the four roots of a quartic polynomial.
#
#  Discussion:
#
#    The polynomial has the form:
#
#      A * X^4 + B * X^3 + C * X^2 + D * X + E = 0
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
#    Output, complex R1, R2, R3, R4, the roots of the polynomial.
#
  import numpy as np
  from r8poly3_root import r8poly3_root
  from sys import exit

  if ( a == 0.0 ):
    print ( '' )
    print ( 'R8POLY4_ROOT - Fatal error!' )
    print ( '  A must not be zero!' )
    exit ( 'R8POLY4_ROOT - Fatal error!' )

  a4 = b / a
  b4 = c / a
  c4 = d / a
  d4 = e / a
#
#  Set the coefficients of the resolvent cubic equation.
#
  a3 = 1.0
  b3 = - b4
  c3 = a4 * c4 - 4.0 * d4
  d3 = - a4 * a4 * d4 + 4.0 * b4 * d4 - c4 * c4
#
#  Find the (complex) roots of the resolvent cubic.
#
  r1, r2, r3 = r8poly3_root ( a3, b3, c3, d3 )
#
#  Choose one root of the cubic, here R1.
#
#  Set R = sqrt ( 0.25 * A4^2 - B4 + R1 )
#
  r = np.sqrt ( 0.25 * a4 ** 2 - b4  + r1 + 0j )

  if ( r != 0.0 ):

    p = np.sqrt ( 0.75 * a4 ** 2 - r ** 2 - 2.0 * b4 \
        + 0.25 * ( 4.0 * a4 * b4 - 8.0 * c4 - a4 ** 3 ) / r )

    q = np.sqrt ( 0.75 * a4 ** 2 - r ** 2 - 2.0 * b4 \
        - 0.25 * ( 4.0 * a4 * b4 - 8.0 * c4 - a4 ** 3 ) / r )

  else:

    p = np.sqrt ( 0.75 * a4 ** 2 - 2.0 * b4 + 2.0 * np.sqrt ( r1 ** 2 - 4.0 * d4 ) )
    q = np.sqrt ( 0.75 * a4 ** 2 - 2.0 * b4 - 2.0 * np.sqrt ( r1 ** 2 - 4.0 * d4 ) )
#
#  Set the roots.
#
  r1 = -0.25 * a4 + 0.5 * r + 0.5 * p
  r2 = -0.25 * a4 + 0.5 * r - 0.5 * p
  r3 = -0.25 * a4 - 0.5 * r + 0.5 * q
  r4 = -0.25 * a4 - 0.5 * r - 0.5 * q

  return r1, r2, r3, r4

def r8poly4_root_test ( ):

#*****************************************************************************80
#
## R8POLY4_ROOT_TEST tests R8POLY4_ROOT.
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

  test_num = 7

  a_test = np.array ( [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ] )
  b_test = np.array ( [ -10.0, -5.0, -22.0, -16.0, -20.0, 2.0, 0.0 ] )
  c_test = np.array ( [ 35.0, 1.0, 141.0, 72.0, 150.0, 1.0, 13.0 ] )
  d_test = np.array ( [ -50.0, 21.0, -220.0, -128.0, -500.0, 8.0, 0.0 ] )
  e_test = np.array ( [ 24.0, -18.0, +100.0, 80.0, 625.0, -12.0, 36.0 ] )
#
#  1: Four distinct real roots, 1, 2, 3, 4.
#  2: Three distinct real roots, 1, -2, 3, 3
#  3: Two distinct real roots, 1, 1, 10, 10.
#  4: Two distinct real roots, 2, 2, 2, 10
#  5: One real root, 5, 5, 5, 5
#  6: Two distinct real roots, one complex conjugate pair.
#  7: Two distinct complex conjugate pairs.
#
  print ( '' )
  print ( 'R8POLY4_ROOT_TEST' )
  print ( '  R8POLY4_ROOT finds roots of quartic equations.' )
 
  for test in range ( 0, test_num ):
 
    a = a_test[test]
    b = b_test[test]
    c = c_test[test]
    d = d_test[test]
    e = e_test[test]

    print ( '' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  D = %f' % ( d ) )
    print ( '  E = %f' % ( e ) )

    r1, r2, r3, r4 = r8poly4_root ( a, b, c, d, e )

    print ( '' )
    print ( '  Roots:' )
    print ( '' )
    print ( '  %f  %f'% ( r1.real, r1.imag ) )
    print ( '  %f  %f'% ( r2.real, r2.imag ) )
    print ( '  %f  %f'% ( r3.real, r3.imag ) )
    print ( '  %f  %f'% ( r4.real, r4.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY4_ROOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly4_root_test ( )
  timestamp ( )
 
 
