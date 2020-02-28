#! /usr/bin/env python
#
def circle01_length ( ):

#*****************************************************************************80
#
## CIRCLE01_LENGTH: length of the circumference of the unit circle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the length.
#
  import numpy as np

  r = 1.0
  value = 2.0 * np.pi * r

  return value

def circle01_length_test ( ) :

#*****************************************************************************80
#
## CIRCLE01_LENGTH tests CIRCLE01_LENGTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CIRCLE01_LENGTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CIRCLE01_LENGTH returns the length of the unit circle.' )

  value = circle01_length ( )

  print ( '' )
  print ( '  CIRCLE01_LENGTH() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CIRCLE01_LENGTH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  circle01_length_test ( )

