#! /usr/bin/env python3
#
def r8poly_deriv ( n, c, p ):

#*****************************************************************************80
#
## R8POLY_DERIV returns the derivative of a polynomial.
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
#    Input, integer N, the degree of the polynomial.
#
#    Input, real C(1:N+1), the polynomial coefficients.
#    C(I+1) is the coefficient of X**I.
#
#    Input, integer P, the order of the derivative.
#    0 means no derivative is taken.
#    1 means first derivative,
#    2 means second derivative and so on.
#    Values of P less than 0 are meaningless.  Values of P greater
#    than N are meaningful, but the code will behave as though the
#    value of P was N.
#
#    Output, real CP(1:N+1-P), the polynomial coefficients of
#    the derivative.
#
  import numpy as np

  if ( n <= p ):
    cp = np.zeros ( 1 )
    return cp

  cp_temp = c.copy ( )

  for d in range ( 1, p + 1 ):
    for i in range ( 0, n + 1 - d ):
      cp_temp[i] = float ( i + 1 ) * cp_temp[i+1]
    cp_temp[n-d+1] = 0.0

  cp = cp_temp[0:n+1-p].copy ( )

  return cp

def r8poly_deriv_test ( ):

#*****************************************************************************80
#
## R8POLY_DERIV_TEST tests R8POLY_DERIV.
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
  from r8poly_print import r8poly_print
  from r8vec_indicator1 import r8vec_indicator1
  from roots_to_r8poly import roots_to_r8poly

  n = 4

  print ( '' )
  print ( 'R8POLY_DERIV_TEST' )
  print ( '  R8POLY_DERIV computes the coefficients of' )
  print ( '  the derivative of a polynomial.' )

  x = r8vec_indicator1 ( n )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( n, c, '  The initial polynomial' )

  for d in range ( 0, n + 1 ):
    cp = r8poly_deriv ( n, c, d )
    label = '  The derivative of order %d' % ( d )
    r8poly_print ( n - d, cp, label )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_deriv_test ( )
  timestamp ( )

