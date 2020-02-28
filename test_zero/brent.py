#! /usr/bin/env python
#
def brent ( fatol, step_max, prob, xatol, xrtol, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## BRENT implements the Brent bisection-based zero finder.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization without Derivatives,
#    Prentice Hall, 1973.
#
#  Parameters:
#
#    Input, real FATOL, an absolute error tolerance for the
#    function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    Input, integer STEP_MAX, the maximum number of steps allowed
#    for an iteration.
#
#    Input, integer PROB, the index of the function whose root is
#    to be sought.
#
#    Input, real XATOL, XRTOL, absolute and relative error
#    tolerances for the root.
#
#    Input/output, real XA, XB, two points at which the
#    function differs in sign.  On output, these values have been adjusted
#    to a smaller interval.
#
#    Input/output, real FXA, FXB, the value of the function
#    at XA and XB.
#
  from p00 import p00_fx
#
#  Initialization.
#
  print ( '' )
  print ( 'BRENT' )
  print ( '' )
  print ( '  Step      XA            XB             F(XA)         F(XB)' )
  print ( '' )

  step_num = 0

  fxa = p00_fx ( prob, xa )
  fxb = p00_fx ( prob, xb )
#
#  Check that f(ax) and f(bx) have different signs.
#
  if ( ( fxa < 0.0 and fxb < 0.0 ) or \
       ( 0.0 < fxa and 0.0 < fxb ) ):
    print ( '' )
    print ( 'BRENT - Fatal error!' )
    print ( '  F(XA) and F(XB) have same sign.' )
    return xa, xb, fxa, fxb

  xc = xa
  fxc = fxa
  d = xb - xa
  e = d

  while ( True ):

    print ( '  %4d  %14e  %14e  %12e  %12e' % ( step_num, xb, xc, fxb, fxc ) )

    step_num = step_num + 1

    if ( step_max < step_num ):
      print ( '' )
      print ( '  Maximum number of steps taken.' )
      break

    if ( abs ( fxc ) < abs ( fxb ) ):
      xa = xb
      xb = xc
      xc = xa
      fxa = fxb
      fxb = fxc
      fxc = fxa

    xtol = 2.0 * xrtol * abs ( xb ) + 0.5 * xatol
#
#  XM is the halfwidth of the current change-of-sign interval.
#
    xm = 0.5 * ( xc - xb )

    if ( abs ( xm ) <= xtol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      break

    if ( abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      break
#
#  See if a bisection is forced.
#
    if ( abs ( e ) < xtol or abs ( fxa ) <= abs ( fxb ) ):

      d = xm
      e = d

    else:

      s = fxb / fxa
#
#  Linear interpolation.
#
      if ( xa == xc ):

        p = 2.0 * xm * s
        q = 1.0 - s
#
#  Inverse quadratic interpolation.
#
      else:

        q = fxa / fxc
        r = fxb / fxc
        p = s * ( 2.0 * xm * q * ( q - r ) - ( xb - xa ) * ( r - 1.0 ) )
        q = ( q - 1.0 ) * ( r - 1.0 ) * ( s - 1.0 )

      if ( 0.0 < p ):
        q = - q
      else:
        p = - p

      s = e
      e = d

      if ( 3.0 * xm * q - abs ( xtol * q ) <= 2.0 * p or \
           abs ( 0.5 * s * q ) <= p ):
        d = xm
        e = d
      else:
        d = p / q
#
#  Save in XA, FXA the previous values of XB, FXB.
#
    xa = xb
    fxa = fxb
#
#  Compute the new value of XB, and evaluate the function there.
#
    if ( xtol < abs ( d ) ):
      xb = xb + d
    elif ( 0.0 < xm ):
      xb = xb + xtol
    elif ( xm <= 0.0 ):
      xb = xb - xtol

    fxb = p00_fx ( prob, xb )
#
#  If the new FXB has the same sign as FXC, then replace XC by XA.
#
    if ( ( 0.0 < fxb and 0.0 < fxc ) or \
         ( fxb < 0.0 and fxc < 0.0 ) ):
      xc = xa
      fxc = fxa
      d = xb - xa
      e = d

  return xa, xb, fxa, fxb

def brent_test ( ):

#*****************************************************************************80
#
## BRENT_TEST tests the Brent method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  from p00 import p00_fx
  from p00 import p00_prob_num
  from p00 import p00_root
  from p00 import p00_root_num
  from p00 import p00_start
  from p00 import p00_start_num

  print ( '' )
  print ( 'BRENT_TEST' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06
  xrtol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 2 ):
      print ( '  Do not have two starting values for this problem.' )
      continue

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )

    if ( ( fxa < 0.0 and fxb < 0.0 ) or ( 0.0 < fxa and 0.0 < fxb ) ):
      print ( '  First two starting points agree in sign.' )
      continue

    xa2, xb2, fxa2, fxb2 = brent ( fatol, step_max, prob, xatol, xrtol, \
      xa, xb, fxa, fxb )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14e                  %14e' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BRENT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  brent_test ( )
  timestamp ( )

