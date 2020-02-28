#! /usr/bin/env python3
#
def r8_is_integer ( r ):

#*****************************************************************************80
#
## R8_IS_INTEGER determines if an R8 represents an integer value.
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
#    Input, real R, the number to be checked.
#
#    Output, logical VALUE, is TRUE if R is an integer value.
#
  import numpy as np

  value = ( r == np.round ( r ) )

  return value

def r8_is_integer_test ( ):

#*****************************************************************************80
#
## R8_IS_INTEGER_TEST tests R8_IS_INTEGER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_IS_INTEGER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_IS_INTEGER reports whether an R8 stores an integer value.' )
  print ( '' )

  for i in range ( - 8, 16 ):
    r = float ( i ) / 7.0
    v = r8_is_integer ( r )
    print ( '  %8.4f  %s' % ( r, v ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_IS_INTEGER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_is_integer_test ( )
  timestamp ( )
 
