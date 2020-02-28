#! /usr/bin/env python
#
def r8_cosh ( x ):

#*****************************************************************************80
#
## R8_COSH evaluates the hyperbolic cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
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
#    Output, real VALUE, the hyperbolic cosine of X.
#
  import numpy as np
  from r8_exp import r8_exp
  from machine import r8_mach

  ymax = 1.0 / np.sqrt ( r8_mach ( 3 ) )

  y = r8_exp ( abs ( x ) )

  if ( y < ymax ):
    value = 0.5 * ( y + 1.0 / y )
  else:
    value = 0.5 * y

  return value

def r8_cosh_test ( ):

#*****************************************************************************80
#
## R8_COSH_TEST tests R8_COSH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from cosh_values import cosh_values

  print ( '' )
  print ( 'R8_COSH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_COSH evaluates the hyperbolic cosine function.' )
  print ( '' )
  print ( '             X         COSH(X)  R8_COSH(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cosh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cosh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_COSH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cosh_test ( )
  timestamp ( )

