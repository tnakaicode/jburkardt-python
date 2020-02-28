#! /usr/bin/env python3
#
def r8_heaviside ( x ):

#*****************************************************************************80
#
## R8_HEAVISIDE evaluates the Heaviside function.
#
#  Discussion:
#
#    The Heaviside function is 0 for x < 0, 1 for x > 0, and 1/2 for x = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
#
  if ( x < 0.0 ):
    value = 0.0
  elif ( x == 0.0 ):
    value = 0.5
  else:
    value = 1.0
  
  return value

def r8_heaviside_test ( ):

#*****************************************************************************80
#
## R8_HEAVISIDE_TEST tests R8_HEAVISIDE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_HEAVISIDE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_HEAVISIDE evaluates the Heaviside step function.' )
  print ( '' )
  print ( '             x  heaviside(x)' )
  print ( '' )

  for i in range ( -5, +6 ):
    x = float ( i ) / 5.0
    y = r8_heaviside ( x )
    
    print ( '  %12g  %12g' % ( x, y ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_HEAVISIDE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_heaviside_test ( )
  timestamp ( )

