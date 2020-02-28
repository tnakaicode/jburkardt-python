#! /usr/bin/env python
#
def circle_triangle_area_2d ( r, center, theta1, theta2 ):

#*****************************************************************************80
#
## CIRCLE_TRIANGLE_AREA_2D returns the area of a circle triangle in 2D.
#
#  Discussion:
#
#    A circle triangle is formed by drawing a circular arc, and considering
#    the triangle formed by the endpoints of the arc plus the center of
#    the circle.
#
#    Note that for angles greater than PI, the triangle will actually
#    have NEGATIVE area.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 May 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the circle.
#
#    Input, real CENTER(2,1), the center of the circle.
#
#    Input, real THETA1, THETA2, the angles of the rays that
#    delimit the arc.
#
#    Output, real AREA, the (signed) area
#    of the triangle.
#
  import numpy as np

  area = 0.5 * r * r * np.sin ( theta2 - theta1 );

  return area

def circle_triangle_area_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_TRIANGLE_AREA_2D_TEST tests CIRCLE_TRIANGLE_AREA_2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_test = 12

  center = np.array ( [ 0.0, 0.0 ] )
  r = 2.0

  print ( '' )
  print ( 'CIRCLE_TRIANGLE_AREA_2D_TEST' )
  print ( '  CIRCLE_TRIANGLE_AREA_2D computes the area of a' )
  print ( '  circular triangle.' )
  print ( '' )
  print ( '      R            Theta1      Theta2        Area' )
  print ( '' )

  for i in range ( 0, n_test + 1 ):

    theta1 = 0.0
    theta2 = i * 2.0 * np.pi / n_test

    area = circle_triangle_area_2d ( r, center, theta1, theta2 )

    print ( '  %10f  %10f  %10f  %10f' % ( r, theta1, theta2, area ) )

  return

if ( __name__ == '__main__' ):
  circle_triangle_area_2d_test ( )

