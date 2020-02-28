#! /usr/bin/env python3
#
def r8poly_ant_value ( n, poly_cof, xval ):

#*****************************************************************************80
#
## r8poly_ant_value evaluates evaluates the antiderivative of a polynomial.
#
#  Discussion:
#
#    The constant term of the antiderivative is taken to be zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n, the order of the polynomial.
#
#    real poly_cof(0:n), the polynomial coefficients.  
#    poly_cof(I) is the coefficient of X^I.
#
#    real xval, the evaluation point.
#
#  Output:
#
#    real yval, the polynomial value.
#
  yval = 0.0
  for i in range ( n, -1, -1 ):
    yval = ( yval + poly_cof[i] / float ( i + 1 ) ) * xval

  return yval

def r8poly_ant_value_test ( ):

#*****************************************************************************80
#
## r8poly_ant_value_test tests r8poly_ant_value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2019
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
  print ( 'r8poly_ant_value_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8poly_ant_value evaluates the antiderivative of a polynomial at a point' )
  print ( '  using a naive method.' )

  r8poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    antiP(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_ant_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly_ant_value_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_ant_value_test ( )
  timestamp ( )

