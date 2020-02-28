#! /usr/bin/env python
#
def r8_acosh ( x ):

#*****************************************************************************80
#
## R8_ACOSH evaluates the arc-hyperbolic cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the arc-hyperbolic cosine of X.
#
  import numpy as np
  from machine import r8_mach
  from sys import exit

  dln2 = 0.69314718055994530941723212145818
  xmax = 1.0 / np.sqrt ( r8_mach ( 3 ) )

  if ( x < 1.0 ):
    print ( '' )
    print ( 'R8_ACOSH - Fatal error!' )
    print ( '  X < 1.0' )
    exit ( 'R8_ACOSH - Fatal error!' )
  elif ( x < xmax ):
    value = np.log ( x + np.sqrt ( x * x - 1.0 ) )
  else:
    value = dln2 + np.log ( x )

  return value

def r8_acosh_test ( ):

#*****************************************************************************80
#
#% R8_ACOSH_TEST tests R8_ACOSH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from arccosh_values import arccosh_values

  print ( '' )
  print ( 'R8_ACOSH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ACOSH evaluates the hyperbolic arccosine function' )
  print ( '' )
  print ( '             X      ARCCOSH(X)  R8_ACOSH(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arccosh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_acosh ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ACOSH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_acosh_test ( )
  timestamp ( )
