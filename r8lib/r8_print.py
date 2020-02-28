#! /usr/bin/env python3
#
def r8_print ( r, title ):

#*****************************************************************************80
#
## R8_PRINT prints an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the value to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '%s  %g' % ( title, r ) )

  return

def r8_print_test ( ):

#*****************************************************************************80
#
## R8_PRINT_TEST tests R8_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 October 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_PRINT prints an R8 with a label.' )
  print ( '' )
  r8_print ( np.pi, '  The value np.pi:' )
  r8_print ( 1.0, '  The value 1.0:' )
  r8_print ( -123456789, '  The value -123456789:' )
  r8_print ( 1.23456789, '  The value 1.23456789:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_print_test ( )
  timestamp ( )

