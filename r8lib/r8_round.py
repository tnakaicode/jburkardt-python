#! /usr/bin/env python3
#
def r8_round ( x ):

#*****************************************************************************80
#
## R8_ROUND sets an R8 to the nearest integral value.
#
#  Example:
#
#        X        R8_ROUND
#
#      1.3         1.0
#      1.4         1.0
#      1.5         1.0 or 2.0
#      1.6         2.0
#      0.0         0.0
#     -0.7        -1.0
#     -1.1        -1.0
#     -1.6        -2.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the value.
#
#    Output, real R8_ROUND, the rounded value.
#
  if ( x < 0.0 ):
    value = - int ( - x + 0.5 )
  else:
    value =   int ( + x + 0.5 )

  return value

def r8_round_test ( ):

#*****************************************************************************80
#
## R8_ROUND_TEST tests R8_ROUND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8_uniform_01 import r8_uniform_01

  seed = 123456789

  print ( '' )
  print ( 'R8_ROUND_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ROUND rounds a real number to a real number with integer value.' )
  print ( '' )
  print ( '  X     XROUND' )
  print ( '' )
  s = + 1.0

  for i in range ( 0, 10 ):

    x, seed = r8_uniform_01 ( seed )
    x = s * 100.0 * x
    xround = r8_round ( x )
    print ( ' %f  %f' % ( x, xround ) )
    s = - s
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ROUND_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_round_test ( )
  timestamp ( )
 
