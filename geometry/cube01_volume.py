#! /usr/bin/env python
#
def cube01_volume ( ):

#*****************************************************************************80
#
## CUBE01_VOLUME returns the volume of the unit cube in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the volume.
#
  value = 1.0;

  return value

def cube01_volume_test ( ) :

#*****************************************************************************80
#
## CUBE01_VOLUME tests CUBE01_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CUBE01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CUBE01_VOLUME returns the volume of the unit cube.' )

  value = cube01_volume ( )

  print ( '' )
  print ( '  CUBE01_VOLUME() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CUBE01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cube01_volume_test ( )
  timestamp ( )

