#! /usr/bin/env python
#
def circle_sector_area_2d ( r, center, theta1, theta2 ):

#*****************************************************************************80
#
## CIRCLE_SECTOR_AREA_2D returns the area of a circular sector in 2D.
#
#  Discussion:
#
#    A sector is contained within a circular arc and the lines joining each
#    endpoint of the arc to the center of the circle.
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
#    that delimit the sector.
#
#    Output, real AREA, the area of the sector.
#
  area = 0.5 * r * r * ( theta2 - theta1 )

  return area

def circle_sector_area_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_SECTOR_AREA_2D_TEST tests CIRCLE_SECTOR_AREA_2D.
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
  print ( 'CIRCLE_SECTOR_AREA_2D_TEST' )
  print ( '  CIRCLE_SECTOR__AREA2D computes the area of a' )
  print ( '  circular sector, defined by joining the endpoints' )
  print ( '  of a circular arc.' )
  print ( '' )
  print ( '      R            Theta1      Theta2        Area' )
  print ( '' )

  for i in range ( 0, n_test + 1 ):

    theta1 = 0.0
    theta2 = i * 2.0 * np.pi / n_test

    area = circle_sector_area_2d ( r, center, theta1, theta2 )

    print ( '  %10f  %10f  %10f  %10f' % ( r, theta1, theta2, area ) )

  return

if ( __name__ == '__main__' ):
  circle_sector_area_2d_test ( )

