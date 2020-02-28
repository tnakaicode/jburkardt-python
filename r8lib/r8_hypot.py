#! /usr/bin/env python3
#
def r8_hypot ( x, y ):

#*****************************************************************************80
#
## R8_HYPOT returns the value of sqrt ( X^2 + Y^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, the arguments.
#
#    Output, real VALUE, the value of sqrt ( X^2 + Y^2 ).
#
  import numpy as np

  if ( abs ( x ) < abs ( y ) ):
    a = abs ( y )
    b = abs ( x )
  else:
    a = abs ( x )
    b = abs ( y )
#
#  A contains the larger value.
#
  if ( a == 0.0 ):
    value = 0.0
  else:
    value = a * np.sqrt ( 1.0 + ( b / a ) ** 2 )

  return value

def r8_hypot_test ( ):

#*****************************************************************************80
#
## R8_HYPOT_TEST tests R8_HYPOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_HYPOT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_HYPOT returns an accurate value for sqrt(A^2+B^2).' )
  print ( '' )
  print ( '             A          B          R8_HYPOT      sqrt(A^2+B^2)' )
  print ( '' )

  b = 2.0

  for i in range ( 0, 20 ):
    a = 1.0
    b = b / 2.0
    c = r8_hypot ( a, b )
    d = np.sqrt ( a ** 2 + b ** 2 )
    
    print ( '  %12g  %12g  %24.16g  %24.16g' % ( a, b, c, d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_HYPOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_hypot_test ( )
  timestamp ( )


