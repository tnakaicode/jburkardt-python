#! /usr/bin/env python3
#
def r8_chop ( place, x ):

#*****************************************************************************80
#
## R8_CHOP chops an R8 to a given number of binary places.
#
#  Example:
#
#    3.875 = 2 + 1 + 1/2 + 1/4 + 1/8.
#
#    The following values would be returned for the 'chopped' value of
#    3.875:
#
#    PLACE  Value
#
#       1      2
#       2      3     = 2 + 1
#       3      3.5   = 2 + 1 + 1/2
#       4      3.75  = 2 + 1 + 1/2 + 1/4
#       5+     3.875 = 2 + 1 + 1/2 + 1/4 + 1/8
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
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PLACE, the number of binary places to preserve.
#    PLACE = 0 means return the integer part of X.
#    PLACE = 1 means return the value of X, correct to 1/2.
#    PLACE = 2 means return the value of X, correct to 1/4.
#    PLACE = -1 means return the value of X, correct to 2.
#
#    Input, real X, the number to be chopped.
#
#    Output, real VALUE, the chopped number.
#
  from r8_log_2 import r8_log_2
  from r8_sign import r8_sign

  s = r8_sign ( x )
  x = abs ( x )
  temp = int ( r8_log_2 ( x ) )
  fac = 2.0 ** ( temp - place + 1 )
  value = s * ( int ( x / fac ) ) * fac

  return value

def r8_chop_test ( ):

#*****************************************************************************80
#
## R8_CHOP_TEST tests R8_CHOP.
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
  print ( 'R8_CHOP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHOP chops an R8 to IPLACE places' )
  print ( '' )
  print ( ' PLACE           X         R8_CHOP' )
  print ( '' )

  x = np.pi

  for place in range ( 0, 33 ):
    print ( '  %4d  %24.16g  %24.16g' % ( place, x, r8_chop ( place, x )  ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHOP_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_chop_test ( )
  timestamp ( )
 
