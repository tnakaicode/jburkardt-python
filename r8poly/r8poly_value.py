#! /usr/bin/env python3
#
def r8poly_value ( m, c, x ):

#*****************************************************************************80
#
## R8POLY_VALUE evaluates a polynomial using a naive method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the degree.
#
#    Input, real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the polynomial value.
#
  value = c[0]
  xi = 1.0
  for i in range ( 1, m + 1 ):
    xi = xi * x
    value = value + c[i] * xi

  return value

def r8poly_value_test ( ):

#*****************************************************************************80
#
## R8POLY_VALUE_TEST tests R8POLY_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8poly_print import r8poly_print

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'R8POLY_VALUE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_VALUE evaluates a polynomial at a point' )
  print ( '  using a naive method.' )

  r8poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_value_test ( )
  timestamp ( )

