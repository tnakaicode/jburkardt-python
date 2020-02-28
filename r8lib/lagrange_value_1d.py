#! /usr/bin/env python
#
def lagrange_value_1d ( nd, xd, yd, ni, xi ):

#*****************************************************************************80
#
## LAGRANGE_VALUE_1D evaluates the Lagrange interpolant.
#
#  Discussion:
#
#    The Lagrange interpolant L(ND,XD,YD)(X) is the unique polynomial of
#    degree ND-1 which interpolates the points (XD(I),YD(I)) for I = 1
#    to ND.
#
#    The Lagrange interpolant can be constructed from the Lagrange basis
#    polynomials.  Given ND distinct abscissas, XD(1:ND), the I-th Lagrange 
#    basis polynomial LB(ND,XD,I)(X) is defined as the polynomial of degree 
#    ND - 1 which is 1 at  XD(I) and 0 at the ND - 1 other abscissas.
#
#    Given data values YD at each of the abscissas, the value of the
#    Lagrange interpolant may be written as
#
#      L(ND,XD,YD)(X) = sum ( 1 <= I <= ND ) LB(ND,XD,I)(X) * YD(I)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data points.
#    ND must be at least 1.
#
#    Input, real XD(ND,1), the data points.
#
#    Input, real YD(ND,1), the data values.
#
#    Input, integer NI, the number of interpolation points.
#
#    Input, real XI(NI,1), the interpolation points.
#
#    Output, real YI(NI,1), the interpolated values.
#
  import numpy as np
  from lagrange_basis_1d import lagrange_basis_1d

  lb = lagrange_basis_1d ( nd, xd, ni, xi )

  yi = np.dot ( lb, yd )

  return yi

def lagrange_value_1d_test ( ):

#*****************************************************************************80
#
## LAGRANGE_VALUE_1D_TEST tests LAGRANGE_VALUE_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec2_print import r8vec2_print

  nd = 4
  ni = 21
#
#  Values of f(x) = x^3 - 12 x^2 + 39 x -28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
#
  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
  yd = np.array ( [ -28.0, +10.0, -8.0, +162.0 ] )
 
  print ( '' )
  print ( 'LAGRANGE_VALUE_1D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAGRANGE_VALUE_1D evaluates a Lagrange 1D interpolant.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  r8vec2_print ( ni, xi, yi, '  Table of interpolant values:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_VALUE_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lagrange_value_1d_test ( )
  timestamp ( )

