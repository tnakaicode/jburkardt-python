#! /usr/bin/env python
#
def tetrahedron01_volume ( ):

#*****************************************************************************80
#
## TETRAHEDRON01_VOLUME returns the volume of the unit tetrahedron.
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
#    Output, real VOLUME, the volume.
#
  value = 1.0 / 6.0;

  return value

def tetrahedron01_volume_test ( ) :

#*****************************************************************************80
#
## TETRAHEDRON01_VOLUME_TEST tests TETRAHEDRON01_VOLUME.
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
  print ( 'TETRAHEDRON01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TETRAHEDRON01_VOLUME returns the volume of the unit tetrahedron.' )

  value = tetrahedron01_volume ( )

  print ( '' )
  print ( '  TETRAHEDRON01_VOLUME() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TETRAHEDRON01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron01_volume_test ( )
  timestamp ( )

