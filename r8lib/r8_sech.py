#! /usr/bin/env python3
#
def r8_sech ( x ):

#*****************************************************************************80
#
## R8_SECH evaluates the hyperbolic secant, while avoiding COSH overflow.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the function.
#
#    Output, real R8_SECH, the value of the function.
#
  import numpy as np

  log_huge = 80.0

  if ( log_huge < abs ( x ) ):
    value = 0.0
  else:
    value = 1.0 / np.cosh ( x )

  return value

def r8_sech_test ( ):

#*****************************************************************************80
#
## R8_SECH_TEST tests R8_SECH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_SECH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SECH computes the hyperbolic secant.' )
  print ( '' )
  print ( '  X    R8_SECH(X)' )
  print ( '' )
 
  for i in range ( -10, 11 ):
    x = float ( i ) / 10.0
    fx = r8_sech ( x )
    print ( '  %10.4g  %14.6g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SECH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sech_test ( )
  timestamp ( )
