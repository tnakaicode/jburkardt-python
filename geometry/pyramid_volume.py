#! /usr/bin/env python
#
def pyramid_volume ( r, h ):

#*****************************************************************************80
#
## PYRAMID_VOLUME returns the volume of a pyramid.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    The integration region:
#
#      - ( R - Z ) <= X <= R - Z
#      - ( R - Z ) <= Y <= R - Z
#                0 <= Z <= H.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the "radius" of the pyramid, that is, half the
#    length of one of the sides of the square base.
#
#    Input, real H, the height of the pyramid.
#
#    Output, real VALUE, the volume of the pyramid.
#
  value = ( 4.0 / 3.0 ) * h * r * r;

  return value

def pyramid_volume_test ( ) :

#*****************************************************************************80
#
## PYRAMID_VOLUME_TEST tests PYRAMID_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'PYRAMID_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PYRAMID_VOLUME returns the volume of a pyramid.' )

  print ( '' )
  print ( '     Radius     Height     Volume' )
  print ( '' )

  seed = 123456789
  for i in range ( 0, 5 ):
    r, seed = r8_uniform_ab ( 1.0, 10.0, seed )
    h, seed = r8_uniform_ab ( 1.0, 10.0, seed )
    volume = pyramid_volume ( r, h )
    print ( '  %8.4f  %8.4f  %8.4f' % ( r, h, volume ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PYRAMID_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pyramid_volume_test ( )
  timestamp ( )

