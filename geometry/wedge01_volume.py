#! /usr/bin/env python
#
def wedge01_volume ( ):

#*****************************************************************************80
#
## WEDGE01_VOLUME returns the volume of the unit wedge in 3D.
#
#  Discussion:
#
#    The unit wedge is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the volume of the unit wedge.
#
  value = 1.0

  return value

def wedge01_volume_test ( ) :

#*****************************************************************************80
#
## WEDGE01_VOLUME_TEST tests WEDGE01_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEDGE01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEDGE01_VOLUME returns the volume of the unit wedge.' )

  value = wedge01_volume ( )

  print ( '' )
  print ( '  WEDGE01_VOLUME() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEDGE01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wedge01_volume_test ( )
  timestamp ( )


