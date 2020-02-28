#! /usr/bin/env python
#
def ellipse_area3 ( r1, r2 ):

#*****************************************************************************80
#
## ELLIPSE_AREA3 returns the area of an ellipse defined by the axes.
#
#  Discussion:
#
#    The ellipse is described by the formula
#      x^2/r1^2 + y^2/r2^2 = 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R1, R2, the major and minor radii.
#
#    Output, real VALUE, the area of the ellipse.
#
  import numpy as np

  value = np.pi * r1 * r2

  return value

def ellipse_area3_test ( ):

#*****************************************************************************80
#
## ELLIPSE_AREA3_TEST tests ELLIPSE_AREA3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'ELLIPSE_AREA3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSE_AREA3 computes the area of an ellipse.' )

  r1 = 10.0
  r2 = 10.0 / 3.0

  area = ellipse_area3 ( r1, r2 )
  print ( '' )
  print ( '  Ellipse: (x/%g)^2 + (y/%g)^2 = 1' % ( r1, r2 ) )
  print ( '  Area = %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_AREA3_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_area3_test ( )
  timestamp ( )
