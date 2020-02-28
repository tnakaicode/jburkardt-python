#! /usr/bin/env python
#
def r8_lngam ( x ):

#*****************************************************************************80
#
## R8_LNGAM evaluates the log of the absolute value of gamma of an R8 argument.
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
#    Output, real VALUE, the logarithm of the absolute value of
#    the gamma function of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_gamma import r8_gamma
  from r8_lgmc import r8_lgmc
  from machine import r8_mach
  from sys import exit

  sq2pil = 0.91893853320467274178032973640562
  sqpi2l = +0.225791352644727432363097614947441

  xmax = r8_mach ( 2 ) / np.log ( r8_mach ( 2 ) )
  dxrel = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( y <= 10.0 ):
    value = np.log ( abs ( r8_gamma ( x ) ) )
    return value

  if ( xmax < y ):
    print ( '' )
    print ( 'R8_LNGAM - Fatal error!' )
    print ( '  Result overflows, |X| too big.' )
    exit ( 'R8_LNGAM - Fatal error!' )

  if ( 0.0 < x ):
    value = sq2pil + ( x - 0.5 ) * np.log ( x ) - x + r8_lgmc ( y )
    return value

  sinpiy = abs ( np.sin ( np.pi * y ) )

  if ( sinpiy == 0.0 ):
    print ( '' )
    print ( 'R8_LNGAM - Fatal error!' )
    print ( '  X is a negative integer.' )
    exit ( 'R8_LNGAM - Fatal error!' )

  value = sqpi2l + ( x - 0.5 ) * np.log ( y ) - x - np.log ( sinpiy ) - r8_lgmc ( y )

  if ( abs ( ( x - r8_aint ( x - 0.5 ) ) * value / x ) < dxrel ):
    print ( '' )
    print ( 'R8_LNGAM - Warning!' )
    print ( '  Result is half precision because' )
    print ( '  X is too near a negative integer.' )

  return value

def r8_lngam_test ( ):

#*****************************************************************************80
#
## R8_LNGAM_TEST tests R8_LNGAM.
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
  from gamma_log_values import gamma_log_values

  print ( '' )
  print ( 'R8_LNGAM_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LNGAM evaluates the logarithm of the Gamma function.' )
  print ( '' )
  print ( '             X        LNGAM(X)  R8_LNGAM(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_lngam ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LNGAM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_lngam_test ( )
  timestamp ( )
