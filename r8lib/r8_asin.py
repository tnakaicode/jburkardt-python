#! /usr/bin/env python3
#
def r8_asin ( s ):

#*****************************************************************************80
#
## R8_ASIN computes the arc sine function, with argument truncation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real S, the argument.
#
#    Output, real VALUE, the arc-sine of S.
#
  import numpy as np
 
  s2 = max ( s,  - 1.0 )
  s2 = min ( s2, +1.0 )
  
  value = np.arcsin ( s2 )

  return value

def r8_asin_test ( ):

#*****************************************************************************80
#
## R8_ASIN_TEST tests R8_ASIN.
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
  print ( 'R8_ASIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ASIN computes the arc-sine of an angle.' )
  print ( '' )
  print ( '       S            R8_ASIN(S)        ARCSIN(S)' )
  print ( '' )

  for test in range ( -1, 14 ):

    s = float ( test - 6 ) / 6.0

    if ( -1.0 <= s and s <= 1.0 ):
      print ( '  %14.6g  %14.6g  %14.6g' % ( s, r8_asin ( s ), np.arcsin ( s ) ) )
    else:
      print ( '  %14.6g  %14.6g' % ( s, r8_asin ( s ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ASIN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_asin_test ( )
  timestamp ( )

