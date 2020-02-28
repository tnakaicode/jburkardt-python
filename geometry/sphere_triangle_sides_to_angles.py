#! /usr/bin/env python
#
def sphere_triangle_sides_to_angles ( r, aside, bside, cside ):

#*****************************************************************************80
#
## SPHERE_TRIANGLE_SIDES_TO_ANGLES computes spherical triangle angles in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the sphere.
#
#    Input, real ASIDE, BSIDE, CSIDE, the (geodesic) length of the 
#    sides of the triangle.
#
#    Output, real A, B, C, the spherical angles of the triangle.
#    Angle A is opposite the side of length ASIDE, and so on.
#
  import numpy as np

  asu = aside / r
  bsu = bside / r
  csu = cside / r
  ssu = ( asu + bsu + csu ) / 2.0

  tan_a2 = np.sqrt ( ( np.sin ( ssu - bsu ) * np.sin ( ssu - csu ) ) / \
                     ( np.sin ( ssu )       * np.sin ( ssu - asu ) ) )

  a = 2.0 * np.arctan ( tan_a2 )

  tan_b2 = np.sqrt ( ( np.sin ( ssu - asu ) * np.sin ( ssu - csu ) ) / \
                     ( np.sin ( ssu )       * np.sin ( ssu - bsu ) ) )

  b = 2.0 * np.arctan ( tan_b2 )

  tan_c2 = np.sqrt ( ( np.sin ( ssu - asu ) * np.sin ( ssu - bsu ) ) / \
                     ( np.sin ( ssu )       * np.sin ( ssu - csu ) ) )

  c = 2.0 * np.arctan ( tan_c2 )

  return a, b, c

def sphere_triangle_sides_to_angles_test ( ):

#*****************************************************************************80
#
## SPHERE_TRIANGLE_SIDES_TO_ANGLES_TEST tests SPHERE_TRIANGLE_SIDES_TO_ANGLES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
  from degrees_to_radians import degrees_to_radians
  from radians_to_degrees import radians_to_degrees

  r = 10.0

  print ( '' )
  print ( 'SPHERE_TRIANGLE_SIDES_TO_ANGLES_TEST' )
  print ( '  SPHERE_TRIANGLE_SIDES_TO_ANGLES takes the sides of a' )
  print ( '  spherical triangle and determines the angles.' )

  aside = 121.0 + ( 15.4 / 60.0 )
  bside = 104.0 + ( 54.7 / 60.0 )
  cside =  65.0 + ( 42.5 / 60.0 )

  aside = degrees_to_radians ( aside )
  bside = degrees_to_radians ( bside )
  cside = degrees_to_radians ( cside )

  aside = r * aside
  bside = r * bside
  cside = r * cside
#
#  Get the spherical angles.
#
  a, b, c = sphere_triangle_sides_to_angles ( r, aside, bside, cside )

  print ( '' )
  print ( '  A       = %8f (radians)' % ( a ) )
  a = radians_to_degrees ( a )
  print ( '  A       = %8f (degrees)' % ( a ) )
  a = 117.0 + ( 58.0 / 60.0 )
  print ( '  Correct = %8f (radians)' % ( a ) )

  print ( '' )
  print ( '  B       = %8f (radians)' % ( b ) )
  b = radians_to_degrees ( b )
  print ( '  B       = %8f (degrees)' % ( b ) )
  b = 93.0 + ( 13.8 / 60.0 )
  print ( '  Correct = %8f (radians)' % ( b ) )

  print ( '' )
  print ( '  C       = %8f (radians)' % ( c ) )
  c = radians_to_degrees ( c )
  print ( '  C       = %8f (degrees)' % ( c ) )
  c = 70.0 + ( 20.6 / 60.0 )
  print ( '  Correct = %8f (radians)' % ( c ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_triangle_sides_to_angles_test ( )
  timestamp ( )

