#! /usr/bin/env python
#
def r8_betai ( x, pin, qin ):

#*****************************************************************************80
#
## R8_BETAI evaluates the incomplete beta ratio of R8 arguments.
#
#  Discussion:
#
#    The incomplete Beta function ratio is the probability that a
#    random variable from a beta distribution having parameters
#    P and Q will be less than or equal to X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Nancy Bosten, EL Battiste,
#    Remark on Algorithm 179:
#    Incomplete Beta Ratio,
#    Communications of the ACM,
#    Volume 17, Number 3, March 1974, pages 156-157.
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
#    Input, real X, the upper limit of integration.
#    0.0 <= X <= 1.0.
#
#    Input, real PIN, the first distribution parameter.
#    0.0 < PIN.
#
#    Input, real QIN, the second distribution parameter.
#    0.0 < QIN.
#
#    Output, real VALUE, the incomplete beta function ratio.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_lbeta import r8_lbeta
  from machine import r8_mach

  eps = r8_mach ( 3 )
  alneps = np.log ( eps )
  sml = r8_mach ( 1 )
  alnsml = np.log ( sml )

  if ( x < 0.0 or 1.0 < x ):
    print ( '' )
    print ( 'R8_BETAI - Fatal error!' )
    print ( '  0 <= X <= 1 is required.' )
    exit ( 'R8_BETAI - Fatal error!' )

  if ( pin <= 0.0 or qin <= 0.0 ):
    print ( '' )
    print ( 'R8_BETAI - Fatal error!' )
    print ( '  P or Q <= 0.0.' )
    exit ( 'R8_BETAI - Fatal error!' )

  y = x
  p = pin
  q = qin

  if ( p < q or 0.8 <= x ):

    if ( 0.2 <= x ):
      y = 1.0 - y
      p = qin
      q = pin

  if ( ( p + q ) * y / ( p + 1.0 ) < eps ):

    value = 0.0

    xb = p * np.log ( max ( y, sml ) ) - np.log ( p ) - r8_lbeta ( p, q )

    if ( alnsml < xb and y != 0.0 ):
      value = np.exp ( xb )

    if ( y != x or p != pin ):
      value = 1.0 - value

    return value

  ps = q - r8_aint ( q )
  if ( ps == 0.0 ):
    ps = 1.0

  xb = p * np.log ( y ) - r8_lbeta ( ps, p ) - np.log ( p )

  if ( xb < alnsml ):

    value = 0.0

  else:

    value = np.exp ( xb )
    term = value * p

    if ( ps != 1.0 ):

      n = int ( r8_aint ( max ( alneps / np.log ( y ), 4.0 ) ) )
      for i in range ( 1, n + 1 ):
        term = term * ( i - ps ) * y / float ( i )
        value = value + term / ( p + i )
#
#  Now evaluate the finite sum.
#
  if ( 1.0 < q ):

    xb = p * np.log ( y ) + q * np.log ( 1.0 - y ) - r8_lbeta ( p, q ) - np.log ( q )
    ib = r8_aint ( max ( xb / alnsml, 0.0 ) )
    term = np.exp ( xb - ib * alnsml )
    c = 1.0 / ( 1.0 - y )
    p1 = q * c / ( p + q - 1.0 )

    finsum = 0.0
    n = int ( r8_aint ( q ) )
    if ( q == n ):
      n = n - 1

    for i in range ( 1, n + 1 ):

      if ( p1 <= 1.0 and term / eps <= finsum ):
        break

      term = ( q - i + 1.0 ) * c * term / ( p + q - i )

      if ( 1.0 < term ):
        ib = ib - 1
        term = term * sml

      if ( ib == 0 ):
        finsum = finsum + term

    value = value + finsum

  if ( y != x or p != pin ):
    value = 1.0 - value

  if ( value < 0.0 ):
    value =  0.0

  if ( 1.0 < value ):
    value = 1.0

  return value

def r8_betai_test ( ):

#*****************************************************************************80
#
## R8_BETAI_TEST tests R8_BETAI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from beta_inc_values import beta_inc_values

  print ( '' )
  print ( 'R8_BETAI_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_BETAI evaluates the incomplete Beta function.' )
  print ( '' )
  print ( '             X               A               B     BETAI(A,B)  R8_BETAI(A,B)  Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx1 = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_betai ( x, a, b )

    print ( '  %14.4f  %14.4f  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( x, a, b, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_BETAI_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_betai_test ( )
  timestamp ( )
