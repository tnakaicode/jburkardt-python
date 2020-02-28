#! /usr/bin/env python3
#
def r8poly_ant_coef ( n, poly_cof ):

#*****************************************************************************80
#
## r8poly_ant_coef integrates a polynomial in standard form.
#
#  Discussion:
#
#    The antiderivative of a polynomial P(X) is any polynomial Q(X)
#    with the property that d/dX Q(X) = P(X).
#
#    This routine chooses the antiderivative whose constant term is zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real POLY_COF(1:N+1), the polynomial coefficients.
#    POLY_COF(1) is the constant term, and POLY_COF(N+1) is the
#    coefficient of X^(N).
#
#  Output:
#
#    real POLY_COF2(1:N+2), the coefficients of
#    the antiderivative polynomial, in standard form.  The constant
#    term is set to zero.
#
  import numpy as np

  poly_cof2 = np.zeros ( n + 2 )
#
#  Set the constant term.
#
  poly_cof2[0] = 0.0
#
#  Integrate the polynomial.
#
  for i in range ( 1, n + 2 ):
    poly_cof2[i] = poly_cof[i-1] / float ( i )

  return poly_cof2

def r8poly_ant_coef_test ( ):

#*****************************************************************************80
#
## r8poly_ant_coef_test tests r8poly_ant_coef().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8poly_print import r8poly_print

  n = 5

  print ( '' )
  print ( 'r8poly_ant_coef_test' )
  print ( '  r8poly_ant_coef() computes the coefficients of the' )
  print ( '  antiderivative of a polynomial' )

  poly_cof = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    poly_cof[i] = float ( n + 1 - i )

  r8poly_print ( n, poly_cof, '  Polynomial p(x):' )

  poly_cof2 = r8poly_ant_coef ( n, poly_cof )

  r8poly_print ( n+1, poly_cof2, '  Antideriv(p(x)):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly_ant_coef_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_ant_coef_test ( )
  timestamp ( )

