#! /usr/bin/env python
#
def circles_intersect_area_2d ( r1, r2, d ):

#*****************************************************************************80
#
## CIRCLES_INTERSECT_AREA_2D: area of the intersection of two circles.
#
#  Discussion:
#
#    Circles of radius R1 and R2 are D units apart.  What is the area of
#    intersection?
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
#    Input, real R1, R2, the radiuses of the circles.
#    R1 and R2 should be positive.
#
#    Input, real D, the distance between the circular centers.
#    D must be positive, and should be no greater than R1 + R2.
#
#    Output, real AREA, the area of the intersection.
#
  import numpy as np
  from circle_lune_area_by_height_2d import circle_lune_area_by_height_2d

  if ( r1 + r2 < d ):
    area = 0.0
  elif ( d == 0.0 ):
    area = np.pi * ( min ( r1, r2 ) ) ** 2
  else:
    h1 = 0.5 * ( d ** 2 + r1 ** 2 - r2 ** 2 ) / d
    area1 = circle_lune_area_by_height_2d ( r1, h1 )
    h2 = 0.5 * ( d ** 2 - r1 ** 2 + r2 ** 2 ) / d
    area2 = circle_lune_area_by_height_2d ( r2, h2 )
    area = area1 + area2

  return area

def circles_intersect_area_2d_test ( ):

#*****************************************************************************80
#
## CIRCLES_INTERSECT_AREA_2D_TEST tests CIRCLES_INTERSECT_AREA_2D
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

  ntest = 6
  r1_test = np. array ( [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ] )
  r2_test = np. array ( [ 0.5, 0.5, 0.5, 1.0, 1.0, 1.0 ] )
  d_test =  np. array ( [ 1.5, 1.0, 0.5, 1.5, 1.0, 0.0 ] )

  print ( '' )
  print ( 'CIRCLES_INTERSECT_AREA_2D_TEST' )
  print ( '  CIRCLES_INTERSECT_AREA_2D determines the area of the' )
  print ( '  intersection of two circes of radius R1 and R2,' )
  print ( '  with a distance D between the centers.' )
  print ( '' )
  print ( '      R1      R2       D    Area' )
  print ( '' )

  for i in range ( 0, ntest ):

    r1 = r1_test[i]
    r2 = r2_test[i]
    d = d_test[i]
    area = circles_intersect_area_2d ( r1, r2, d )

    print ( '  %6f  %6f  %6f  %6f' % ( r1, r2, d, area ) )

  return

if ( __name__ == '__main__' ):
  circles_intersect_area_2d_test ( )

