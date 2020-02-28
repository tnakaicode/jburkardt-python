#! /usr/bin/env python
#
def circle_lune_area_by_angle_2d ( r, center, theta1, theta2 ):

#*****************************************************************************80
#
## CIRCLE_LUNE_AREA_BY_ANGLE_2D returns the area of a circular lune in 2D.
#
#  Discussion:
#
#    A lune is formed by drawing a circular arc, and joining its endpoints.
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
#  Parameters:
#
#    Input, real R, the radius of the circle.
#
#    Input, real CENTER(2,1), the center of the circle.
#
#    Input, real THETA1, THETA2, the angles of the rays
#    that begin and end the arc.
#
#    Output, real AREA, the area of the lune.
#
  from circle_sector_area_2d import circle_sector_area_2d
  from circle_triangle_area_2d import circle_triangle_area_2d

  sector = circle_sector_area_2d ( r, center, theta1, theta2 )
  triangle = circle_triangle_area_2d ( r, center, theta1, theta2 )
  area = sector - triangle

  return area

def circle_lune_area_by_angle_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_LUNE_AREA_BY_ANGLE_2D_TEST tests CIRCLE_LUNE_AREA_BY_ANGLE_2D.
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
  print ( 'CIRCLE_LUNE_AREA_BY_ANGLE_2D_TEST' )
  print ( '  CIRCLE_LUNE_AREA_BY_ANGLE_2D computes the area of a' )
  print ( '  circular lune, defined by joining the endpoints' )
  print ( '  of a circular arc.' )
  print ( '' )
  print ( '      R            Theta1      Theta2        Area' )
  print ( '' )

  for i in range ( 0, n_test + 1 ): 

    theta1 = 0.0
    theta2 = i * 2.0 * np.pi / n_test

    area = circle_lune_area_by_angle_2d ( r, center, theta1, theta2 )

    print ( '  %10f  %10f  %10f  %10f' % ( r, theta1, theta2, area ) )

  return

if ( __name__ == '__main__' ):
  circle_lune_area_by_angle_2d_test ( )

