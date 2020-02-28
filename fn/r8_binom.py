#! /usr/bin/env python
#
def r8_binom ( n, m ):

#*****************************************************************************80
#
## R8_BINOM evaluates the binomial coefficient using R8 arithmetic.
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
#    Input, integer N, M, the arguments.
#
#    Output, real VALUE, the binomial coefficient.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_lgmc import r8_lgmc
  from r8_lnrel import r8_lnrel
  from machine import r8_mach
  from sys import exit

  sq2pil = 0.91893853320467274178032973640562

  bilnmx = np.log ( r8_mach ( 2 ) ) - 0.0001
  fintmx = 0.9 / r8_mach ( 3 )

  if ( n < 0 ):
    value = 0.0
    return value

  if ( m < 0 ):
    value = 0.0
    return value

  if ( n < m ):
    value = 0.0
    return value

  k = min ( m, n - m )

  if ( k <= 20 and k * np.log ( max ( n, 1 ) ) <= bilnmx ):

    value = 1.0

    for i in range ( 1, k + 1 ):
      value = value * float ( n - i + 1 ) / float ( i )

  else:

    if ( k < 9 ):
      print ( '' )
      print ( 'R8_BINOM - Fatal error!' )
      print ( '  Result overflows.' )
      print ( '  N or M is too big.' )
      exit ( 'R8_BINOM - Fatal error!' )

    xn = float ( n + 1 )
    xk = float ( k + 1 )
    xnk = float ( n - k + 1 )

    corr = r8_lgmc ( xn ) - r8_lgmc ( xk ) - r8_lgmc ( xnk )

    value = xk * np.log ( xnk / xk ) \
      - xn * r8_lnrel ( - ( xk - 1.0 ) / xn ) \
      - 0.5 * np.log ( xn * xnk / xk ) + 1.0 - sq2pil + corr

    if ( bilnmx < value ):
      print ( '' )
      print ( 'R8_BINOM - Fatal error!' )
      print ( '  Result overflows.' )
      print ( '  N or M is too big.' )
      exit ( 'R8_BINOM - Fatal error!' )

    value = np.exp ( value )

  if ( value < fintmx ):
    value = r8_aint ( value + 0.5 )

  return value

def r8_binom_test ( ):

#*****************************************************************************80
#
#% R8_BINOM_TEST tests R8_BINOM.
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
  from binomial_values import binomial_values

  print ( '' )
  print ( 'R8_BINOM_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_BINOM evaluates the binomial coefficient.' )
  print ( '' )
  print ( '             A               B     BINOM(A,B)  R8_BINOM(A,B)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx1 = binomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_binom ( a, b )

    print ( '  %14d  %14d  %14d  %14d  %14.6g' \
      % ( a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_BINOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_binom_test ( )
  timestamp ( )

