#! /usr/bin/env python
#
def ellipse_area2 ( a, b, c, d ):

#*****************************************************************************80
#
## ELLIPSE_AREA2 returns the area of an ellipse defined by an equation.
#
#  Discussion:
#
#    The ellipse is described by the formula
#      a x^2 + b xy + c y^2 = d
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, coefficients on the left hand side.
#
#    Input, real D, the right hand side.
#
#    Output, real VALUE, the area of the ellipse.
#
  import numpy as np

  value = 2.0 * d * d * np.pi / np.sqrt ( 4.0 * a * c - b * b )

  return value

def ellipse_area2_test ( ):

#*****************************************************************************80
#
## ELLIPSE_AREA2_TEST tests ELLIPSE_AREA2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'ELLIPSE_AREA2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSE_AREA2 computes the area of an ellipse.' )

  a = 5.0
  b = 2.0
  c = 2.0
  d = 10.0

  area = ellipse_area2 ( a, b, c, d )
  print ( '' )
  print ( '  Ellipse: %g * x^2 + %g * xy + %g * y^2 = %g' % ( a, b, c, d ) )
  print ( '  Area = %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_AREA2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_area2_test ( )
  timestamp ( )
