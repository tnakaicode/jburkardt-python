#! /usr/bin/env python
#
def cone_volume ( r, h ):

#*****************************************************************************80
#
## CONE_VOLUME returns the volume of a cone in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the base of the cone.
#
#    Input, real H, the height of the cone.
#
#    Output, real VALUE, the volume of the cone.
#
  import numpy as np

  value = ( np.pi / 3.0 ) * h * r * r

  return value

def cone_volume_test ( ):

#*****************************************************************************80
#
## CONE_VOLUME_TEST tests CONE_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'CONE_VOLUME_TEST' )
  print ( '  CONE_VOLUME computes the volume of a cone.' )
  print ( '' )
  print ( '        R        H        ConeVolume' )
  print ( '' )

  r = 1.0
  h = 1.0
  for i in range ( 0, 5 ):
    print ( '  %14.8f  %14.8f  %14.8f' % ( r, h, cone_volume ( r, h ) ) )
    h = h * 2.0

  print ( '' )

  r = 1.0
  h = 1.0
  for i in range ( 0, 5 ):
    print ( '  %14.8f  %14.8f  %14.8f' % ( r, h, cone_volume ( r, h ) ) )
    r = r * 2.0
#
#  Terminate.
#
  print ( '' )
  print ( 'CONE_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cone_volume_test ( )
  timestamp ( )

