#! /usr/bin/env python3
#
def r8_pi_sqrt ( ):

#*****************************************************************************80
#
## R8_PI_SQRT returns the square root of pi as an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the square root of pi.
#
  value = 1.7724538509055160273

  return value

def r8_pi_sqrt_test ( ):

#*****************************************************************************80
#
## R8_PI_SQRT_TEST tests R8_PI_SQRT.
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
  print ( 'R8_PI_SQRT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_PI_SQRT returns the square root of PI.' )
  print ( '' )
  print ( '  R8_PI_SQRT           = %24.16f' % ( r8_pi_sqrt ( ) ) )
  print ( '  sqrt ( 4 * Atan(1) ) = %24.16f' % ( np.sqrt ( 4.0 * np.arctan ( 1.0 ) ) ) )
  print ( '  sqrt ( NP.PI )       = %24.16f' % ( np.sqrt ( np.pi ) ) )
  print ( '' )
  print ( '  NP.PI                = %24.16f' % ( np.pi ) )
  print ( '  R8_PI_SQRT ** 2      = %24.16f' % ( r8_pi_sqrt ( ) ** 2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_PI_SQRT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_pi_sqrt_test ( )
  timestamp ( )

