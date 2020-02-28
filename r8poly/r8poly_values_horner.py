#! /usr/bin/env python3
#
def r8poly_values_horner ( m, c, n, x ):

#*****************************************************************************80
#
## R8POLY_VALUES_HORNER evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    can be evaluated at the vector x by the command
#
#      pval = r8poly_value ( m, c, n, x )
#
#    Note that C must actually be dimensioned of size M+1.
#
#    Unfortunately, the natural MATLAB function to use, polyval(),
#    assumes that the polynomial coefficients are given in the
#    opposite order, so that c1 multiplies x^(m-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the degree.
#
#    Input, real C(M+1,1), the polynomial coefficients.  
#    C(I+1) is the coefficient of X^I.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N,1), the evaluation points.
#
#    Output, real P(N,1), the polynomial values.
#
  import numpy as np

  p = np.zeros ( n )

  for j in range ( 0, n ):
    p[j] = c[m]
    for i in range ( m - 1, -1, -1 ):
      p[j] = p[j] * x[j] + c[i]

  return p

def r8poly_values_horner_test ( ):

#*****************************************************************************80
#
## R8POLY_VALUES_HORNER_TEST tests R8POLY_VALUES_HORNER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8poly_print import r8poly_print
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'R8POLY_VALUES_HORNER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_VALUES_HORNER evaluates a polynomial at a' )
  print ( '  point, using Horner\'s method.' )

  m = 4
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )
  r8poly_print ( m, c, '  The polynomial:' )

  n = 16
  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  p = r8poly_values_horner ( m, c, n, x )

  r8vec2_print ( n, x, p, '  X, P(X):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_VALUES_HORNER_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_values_horner_test ( )
  timestamp ( )

