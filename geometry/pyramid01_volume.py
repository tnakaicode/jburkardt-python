#! /usr/bin/env python
#
def pyramid01_volume ( ):

#*****************************************************************************80
#
## PYRAMID01_VOLUME returns the volume of a unit pyramid.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    The integration region:
#
#      - ( 1 - Z ) <= X <= 1 - Z
#      - ( 1 - Z ) <= Y <= 1 - Z
#                0 <= Z <= 1.
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
#    Output, real VALUE, the volume of the pyramid.
#
  value = 4.0 / 3.0;

  return value

def pyramid01_volume_test ( ) :

#*****************************************************************************80
#
## PYRAMID01_VOLUME_TEST tests PYRAMID01_VOLUME.
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

  print ( '' )
  print ( 'PYRAMID01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PYRAMID01_VOLUME returns the volume of the unit pyramid.' )

  value = pyramid01_volume ( )

  print ( '' )
  print ( '  PYRAMID01_VOLUME() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PYRAMID01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pyramid01_volume_test ( )
  timestamp ( )

