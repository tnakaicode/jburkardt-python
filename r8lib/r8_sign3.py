#! /usr/bin/env python3
#
def r8_sign3 ( x ):

#*****************************************************************************80
#
## R8_SIGN3 returns the three-way sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive, 0 if zero, and -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose sign is desired.
#
#    Output, real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  elif ( x == 0.0 ):
    value = 0.0;
  else:
    value = +1.0
 
  return value

def r8_sign3_test ( ):

#*****************************************************************************80
#
## R8_SIGN3_TEST tests R8_SIGN3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'R8_SIGN3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SIGN3 returns the three-way sign of an R8.' )
  print ( '' )
  print ( '    R8  R8_SIGN3(R8)' )
  print ( '' )

  for test in range ( 0, 5 ):
    r8 = r8_test[test]
    s = r8_sign3 ( r8 )
    print ( '  %8g  %8g' % ( r8, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SIGN3_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sign3_test ( )
  timestamp ( )
 
