#! /usr/bin/env python
#
def circle_area ( r ):

#*****************************************************************************80
#
## CIRCLE_AREA returns the area of a circle.
#
#  Integration region:
#
#    Points (X,Y) such that
#
#      ( X - XC )^2 + ( Y - YC )^2 <= R^2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the circle.
#
#    Output, real VALUE, the area of the circle.
#
  import numpy as np

  value = np.pi * r * r

  return value

def circle_area_test ( ):

#*****************************************************************************80
#
## CIRCLE_AREA_TEST tests CIRCLE_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'CIRCLE_AREA_TEST' )
  print ( '  CIRCLE_AREA computes the area of a circle of radius R.' )
  print ( '' )
  print ( '      R            Area' )
  print ( '' )

  r = 1.0
  for i in range ( 0, 4 ):
    area = circle_area ( r )
    print ( '  %10f  %10f' % ( r, area ) )
    r = r * 2

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  circle_area_test ( )
  timestamp ( )

