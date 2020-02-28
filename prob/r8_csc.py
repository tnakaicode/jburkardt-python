#! /usr/bin/env python
#
def r8_csc ( theta ):

#*****************************************************************************80
#
## R8_CSC returns the cosecant of X.
#
#  Discussion:
#
#    R8_CSC ( THETA ) = 1.0 / SIN ( THETA )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real THETA, the angle, in radians, whose cosecant is desired.
#    It must be the case that SIN ( THETA ) is not zero.
#
#    Output, real VALUE, the cosecant of THETA.
#
  import numpy as np
  from sys import exit

  value = np.sin ( theta )

  if ( value == 0.0 ):
    print ( '' )
    print ( 'R8_CSC - Fatal error!' )
    print ( '  Cosecant undefined for THETA = %g' % ( theta ) )
    exit ( 'R8_CSC - Fatal error!' )

  value = 1.0 / value

  return value

def r8_csc_test ( ):

#*****************************************************************************80
#
## R8_CSC_TEST tests R8_CSC.
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

  print ( '' )
  print ( 'R8_CSC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CSC computes the cosecant of an angle.' )
  print ( '' )
  print ( '  ANGLE    R8_CSC(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    r = angle / 2.0 / np.pi
    if ( ( i % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_csc ( r ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CSC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_csc_test ( )
  timestamp ( )

