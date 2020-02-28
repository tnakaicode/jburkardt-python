#! /usr/bin/env python
#
def r8_beta ( a, b ):

#*****************************************************************************80
#
## R8_BETA evaluates the beta function of R8 arguments.
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
#    Input, real A, B, the arguments.
#
#    Output, real VALUE, the beta function of A and B.
#
  import numpy as np
  from r8_gaml import r8_gaml
  from r8_gamma import r8_gamma
  from r8_lbeta import r8_lbeta
  from machine import r8_mach
  from sys import exit

  xmin, xmax = r8_gaml ( )
  alnsml = np.log ( r8_mach ( 1 ) )

  if ( a <= 0.0 or b <= 0.0 ):
    print ( '' )
    print ( 'R8_BETA - Fatal error!' )
    print ( '  A and B must be greater than 0.' )
    exit ( 'R8_BETA - Fatal error!' )

  if ( a + b < xmax ):
    value = r8_gamma ( a ) * r8_gamma ( b ) / r8_gamma ( a + b )
  else:
    value = r8_lbeta ( a, b )
    value = np.exp ( value )

  return value

def r8_beta_test ( ):

#*****************************************************************************80
#
## R8_BETA_TEST tests R8_BETA.
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
  from beta_values import beta_values

  print ( '' )
  print ( 'R8_BETA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_BETA evaluates the Beta function.' )
  print ( '' )
  print ( '             A               B      BETA(A,B)  R8_BETA(A,B)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx1 = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_beta ( a, b )

    print ( '  %14.6g  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_BETA_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_beta_test ( )
  timestamp ( )
