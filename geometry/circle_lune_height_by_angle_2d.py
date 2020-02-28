#! /usr/bin/env python
#
def circle_lune_height_by_angle_2d ( r, angle ):

#*****************************************************************************80
#
## CIRCLE_LUNE_HEIGHT_BY_ANGLE_2D computes the height of a circular lune.
#
#  Discussion:
#
#    Draw the chord connecting two points on the circumference of a circle.
#    The region between the chord and the circumference is a "lune".
#    The lune subtends a given angle between 0 and 2 pi.
#
#    The distance from the center of the circle to the midpoint of the chord
#    is the "height" H of the lune and we wish to determine this value.
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
#    Input, real ANGLE, the angle subtended by the lune.
#
#    Output, real HEIGHT, the height of the lune
#
  import numpy as np

  height = r * np.cos ( angle / 2.0 )

  return height

def circle_lune_height_by_angle_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_LUNE_HEIGHT_BY_ANGLE_2D_TEST tests CIRCLE_LUNE_HEIGHT_BY_ANGLE_2D.
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

  r = 2.0

  print (  '' )
  print ( 'CIRCLE_LUNE_HEIGHT_BY_ANGLE_2D_TEST' )
  print ( '  CIRCLE_LUNE_HEIGHT_BY_ANGLE_2D computes the height of' )
  print ( '  the triangle of a circular lune, given the subtended angle.' )
  print ( '' )
  print ( '      R            Angle        Height' )
  print ( '' )

  for i in range ( 0, n_test + 1 ):

    angle = i * 2.0 * np.pi / n_test

    height = circle_lune_height_by_angle_2d ( r, angle )

    print ( '  %10f  %10f  %10f' % ( r, angle, height ) )

  return

if ( __name__ == '__main__' ):
  circle_lune_height_by_angle_2d_test ( )
