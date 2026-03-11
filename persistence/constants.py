#! /usr/bin/env python3
#
def constants ( ):

#*****************************************************************************80
#
## constants() stores, and returns constants "g", "c" and "h".
#
#  Discussion:
#
#    Calling g,c,h=constants() returns the values of g, c, and h.
#
#    Because the values never change, and don't need to be computed,
#    we use assignment statements here, instead of persistent data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real G: gravitational constant m^3/s^2/kg
#
#    real C: light speed, m/s.
#
#    real H: Planck's constant, j s;
#
  g = 6.67384E-11
  c = 2.99792458E+8
  h = 6.626070040E-34

  return g, c, h

def constants_test ( ):

#*****************************************************************************80
#
## constants_test() tests constants().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'constants_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test constants(), with the interface:' )
  print ( '    g,c,h = constants()' )

  g, c, h = constants ( )
  print ( '' )
  print ( '    ', g, ',', c, ',', h, ' = constants ( );' )
#
#  Terminate.
#
  print ( '' )
  print ( 'constants_test():' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  constants_test ( )
  timestamp ( )

