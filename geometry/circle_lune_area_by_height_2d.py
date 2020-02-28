#! /usr/bin/env python
#
def circle_lune_area_by_height_2d ( r, h ):

#*****************************************************************************80
#
## CIRCLE_LUNE_AREA_BY_HEIGHT_2D computes the area of a circular lune.
#
#  Discussion:
#
#    Draw the chord connecting two points on the circumference of a circle.
#    The region between the chord and the circumference is a "lune".
#    We wish to know the area of this region.
#
#    The distance from the center of the circle to the midpoint of the chord
#    is the "height" H of the lune.  It is natural to expect 0 <= H <= R.
#    However, if we allow -R <= H < 0 as well, this allows us to include
#    lunes which involve more than half the circle's area.
#
#    If H < -R or R < H, then no lune is formed and we have zero area.
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
#    Input, real H, the height of the lune.
#
#    Output, real AREA, the area of the lune.
#
  import numpy as np

  if ( -r <= h and h <= r ):
    area = r ** 2 * np.arccos ( h / r ) - h * np.sqrt ( r ** 2 - h ** 2 )
  else:
    area = 0.0

  return area

def circle_lune_area_by_height_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_LUNE_AREA_BY_HEIGHT_2D_TEST tests CIRCLE_LUNE_AREA_BY_HEIGHT_2D.
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
  n_test = 6

  r = 2.0

  print ( '' )
  print ( 'CIRCLE_LUNE_AREA_BY_HEIGHT_2D_TEST' )
  print ( '  CIRCLE_LUNE_AREA_BY_HEIGHT_2D computes the area of a' )
  print ( '  circular lune based on the "height" of the circular triangle.' )
  print ( '' )
  print ( '      R            H        Area' )
  print ( '' )

  for i in range ( - n_test, n_test + 1 ):

    h = i * r / n_test

    area = circle_lune_area_by_height_2d ( r, h )

    print ( '  %10f  %10f  %10f' % ( r, h, area ) )

  return

if ( __name__ == '__main__' ):
  circle_lune_area_by_height_2d_test ( )

