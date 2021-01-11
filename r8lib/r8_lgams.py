#! /usr/bin/env python
#
def r8_lgams ( x ):

#*****************************************************************************80
#
## R8_LGAMS evaluates the log of |gamma(x)| and sign, for an R8 argument.
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
#    Output, real ALGAM, the logarithm of the absolute value of
#    gamma ( X ).
#
#    Output, real SGNGAM, the sign (+1 or -1 ) of gamma ( X ).
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_lngam import r8_lngam

  algam = r8_lngam ( x )
  sgngam = 1.0

  if ( x <= 0.0 ):

    k = np.floor ( ( ( - r8_aint ( x ) ) % 2.0 ) + 0.1 )

    if ( k == 0 ):
      sgngam = - 1.0

  return algam, sgngam

def r8_lgams_test ( ):

#*****************************************************************************80
#
## R8_LGAMS_TEST tests R8_LGAMS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 May 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from gamma_log_values import gamma_log_values

  print ( '' )
  print ( 'R8_LGAMS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LGAMS evaluates the sign of Gamma(x) and ' )
  print ( '  the logarithm of the absolute value of Gamma(x).' )
  print ( '' )
  print ( '             X        LNGAM(X)  Sign(Gamma(x))   Log(|Gamma(x)|)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, slngam = r8_lgams ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g' \
      % ( x, fx1, slngam, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LGAMS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_lgams_test ( )
  timestamp ( )

