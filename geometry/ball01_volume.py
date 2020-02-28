#! /usr/bin/env python
#
def ball01_volume ( ):

#*****************************************************************************80
#
## BALL01_VOLUME returns the volume of the unit ball.
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
#    Output, real VALUE, the volume of the unit ball.
#
  import numpy as np

  r = 1.0
  value = 4.0 * np.pi * r ** 3 / 3.0

  return value

def ball01_volume_test ( ) :

#*****************************************************************************80
#
## BALL01_VOLUME_TEST tests BALL01_VOLUME.
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
  print ( 'BALL01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BALL01_VOLUME returns the volume of the unit ball.' )

  value = ball01_volume ( )

  print ( '' )
  print ( '  BALL01_VOLUME() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BALL01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ball01_volume_test ( )
  timestamp ( )

