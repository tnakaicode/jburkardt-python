#! /usr/bin/env python3
#
def r8_tiny ( ):

#*****************************************************************************80
#
## R8_TINY returns the smallest positive R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, a "tiny" value.
#
  value = 1.0E-30

  return value

def r8_tiny_test ( ):

#*****************************************************************************80
#
## R8_TINY_TEST tests R8_TINY.
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
  import platform

  print ( '' )
  print ( 'R8_TINY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_TINY returns a "tiny" R8;' )
  print ( '' )
  print ( '    R8_TINY = %g' % ( r8_tiny ( ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_TINY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_tiny_test ( )
  timestamp ( )
 
