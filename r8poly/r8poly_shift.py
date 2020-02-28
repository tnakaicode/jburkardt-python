#! /usr/bin/env python3
#
def r8poly_shift ( scale, shift, n, poly_cof ):

#*****************************************************************************80
#
## R8POLY_SHIFT adjusts the coefficients of a polynomial for a new argument.
#
#  Discussion:
#
#    Assuming P(X) is a polynomial in the argument X, of the form:
#
#      P(X) =
#          C(N) * X^(N-1)
#        + ...
#        + C(2) * X
#        + C(1),
#
#    and that Z is related to X by the formula:
#
#      Z = SCALE * X + SHIFT
#
#    then this routine computes coefficients C for the polynomial Q(Z):
#
#      Q(Z) =
#          C(N) * Z^(N-1)
#        + ...
#        + C(2) * Z
#        + C(1)
#
#    so that:
#
#      Q(Z(X)) = P(X)e
#
#  Example:
#
#    P(X) = 2 * X^2 - X + 6
#
#    Z = 2.0 * X + 3.0
#
#    Q(Z) = 0.5 *         Z^2 -  3.5 * Z + 12
#
#    Q(Z(X)) = 0.5 * ( 4.0 * X^2 + 12.0 * X +  9 )
#            - 3.5 * (              2.0 * X +  3 )
#                                            + 12
#
#            = 2.0         * X^2 -  1.0 * X +  6
#
#            = P(X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real SHIFT, SCALE, the shift and scale applied to X,
#    so that Z = SCALE * X + SHIFT.
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real POLY_COF(N), the coefficient array in terms of the X variable.
#
#    Output, real POLY_COF(N), the coefficient array in terms of the Z variable.
#
  for i in range ( 0, n ):
    poly_cof[(i+1):n] = poly_cof[(i+1):n] / scale

  for i in range ( 0, n ):
    for j in range ( n - 2, i - 1, -1 ):
      poly_cof[j] = poly_cof[j] - shift * poly_cof[j+1]

  return poly_cof

def r8poly_shift_test ( ):

#*****************************************************************************80
#
## R8POLY_SHIFT_TEST tests R8POLY_SHIFT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print

  print ( '' )
  print ( 'R8POLY_SHIFT_TEST' )
  print ( '  R8POLY_SHIFT shifts an R8POLY p(x) to q(z)' )
  print ( '  where z=scale*x+shift.' )

  order = 3
  degree = 2

  c = np.array ( [ 6.0, -1.0, 2.0 ] )
  r8poly_print ( degree, c, '  p(x):' )

  scale = 2.0
  shift = 3.0
  print ( '' )
  print ( '  z = scale * x + shift' )
  print ( '  Scale = %g' % ( scale ) )
  print ( '  Shift = %g' % ( shift ) )

  c2 = r8poly_shift ( scale, shift, order, c )
  r8poly_print ( degree, c2, '  q(z):' )

  c3 = np.array ( [ 12.0, -3.5, 0.5 ] )
  r8poly_print ( degree, c3, '  Expected q(z):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_SHIFT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_shift_test ( )
  timestamp ( )

