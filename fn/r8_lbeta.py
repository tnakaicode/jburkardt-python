#! /usr/bin/env python
#
def r8_lbeta ( a, b ):

#*****************************************************************************80
#
## R8_LBETA evaluates the logarithm of the beta function of R8 arguments.
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
#    Output, real VALUE, the logarithm of the beta function of A
#    and B.
#
  import numpy as np
  from r8_gamma import r8_gamma
  from r8_lgmc import r8_lgmc
  from r8_lngam import r8_lngam
  from r8_lnrel import r8_lnrel
  from sys import exit

  sq2pil = 0.91893853320467274178032973640562

  p = min ( a, b )
  q = max ( a, b )

  if ( p <= 0.0 ):

    print ( '' )
    print ( 'R8_LBETA - Fatal error!' )
    print ( '  Both arguments must be greater than 0.' )
    exit ( 'R8_LBETA - Fatal error!' )

  elif ( p < 10.0 and q <= 10.0 ):

    value = np.log ( r8_gamma ( p ) * ( r8_gamma ( q ) / r8_gamma ( p + q ) ) )

  elif ( p < 10.0 ):

    corr = r8_lgmc ( q ) - r8_lgmc ( p + q )

    value = r8_lngam ( p ) + corr + p - p * np.log ( p + q ) + \
      ( q - 0.5 ) * r8_lnrel ( - p / ( p + q ) )

  else:

    corr = r8_lgmc ( p ) + r8_lgmc ( q ) - r8_lgmc ( p + q )

    value = - 0.5 * np.log ( q ) + sq2pil + corr \
      + ( p - 0.5 ) * np.log ( p / ( p + q ) ) \
      + q * r8_lnrel ( - p / ( p + q ) )

  return value

def r8_lbeta_test ( ):

#*****************************************************************************80
#
## R8_LBETA_TEST tests R8_LBETA.
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
  from beta_log_values import beta_log_values

  print ( '' )
  print ( 'R8_LBETA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LBETA evaluates the logarithm of the Beta function.' )
  print ( '' )
  print ( '             A               B     LBETA(A,B)  R8_LBETA(A,B)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx1 = beta_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_lbeta ( a, b )

    print ( '  %14.4f  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LBETA_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_lbeta_test ( )
  timestamp ( )

