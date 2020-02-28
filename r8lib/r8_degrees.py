#! /usr/bin/env python3
#
def r8_degrees ( radians ):

#*****************************************************************************80
#
## R8_DEGREES converts an angle from radian to degree measure.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real RADIANS, the angle measurement in radians.
#
#    Output, real VALUE, the angle measurement in degrees.
#
  import numpy as np

  value = radians * 180.0 / np.pi

  return value

def r8_degrees_test ( ):

#*****************************************************************************80
#
## R8_DEGREES_TEST tests R8_DEGREES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 12

  print ( '' )
  print ( 'R8_DEGREES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_DEGREES converts an angle from radians to degrees..' )
  print ( '' )
  print ( '	 Radians         Degrees' )
  print ( '' )

  for test in range ( 0, 13 ):
    r = np.pi * test / 12
    d = r8_degrees ( r )
    print ( '  %14f  %14f' % ( r, d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_DEGREES_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_degrees_test ( )
  timestamp ( )
 
