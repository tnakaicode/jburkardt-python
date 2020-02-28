#! /usr/bin/env python
#
def secant ( fatol, step_max, prob, xatol, xmin, xmax, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## SECANT carries out the secant method to seek a root of F(X) = 0.
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
#    Input, real XATOL, an absolute error tolerance for the root.
#
#    Input, real XMAX, XMIN, the interval in which the root should
#    be sought.
#
#    Input/output, real XA, XB, two points at which the 
#    function differs in sign.  On output, these values have been adjusted
#    to a smaller interval.
#
#    Input/output, real FXA, FXB, the value of the function 
#    at XA and XB.
#
  from p00 import p00_fx

  print ( '' )
  print ( 'SECANT' )
  print ( '' )
  print ( '  Step             X             F(X)' )
  print ( '' )

  step_num = -1
  print ( '  %4d  %14g  %14g' % ( step_num, xa, fxa ) )

  if ( abs ( fxa ) <= fatol ):
    print ( '' )
    print ( '  Function small enough for convergence.' )
    return xa, xb, fxa, fxb

  step_num = 0
  print ( '  %4d  %14g  %14g' % ( step_num, xb, fxb ) )

  for step_num in range ( 1, step_max + 1 ):

    if ( abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      return xa, xb, fxa, fxb

    if ( abs ( xa - xb ) < xatol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      return xa, xb, fxa, fxb

    if ( xb < xmin or xmax < xb ):
      print ( '' )
      print ( '  Iterate has left the region [%g,%g].' % ( xmin, xmax ) )
      return xa, xb, fxa, fxb

    if ( fxa == fxb ):
      print ( '' )
      print ( '  F(A) = F(B), algorithm fails.' )
      return xa, xb, fxa, fxb

    xc = ( fxa * xb - fxb * xa ) / ( fxa - fxb )

    fxc = p00_fx ( prob, xc )

    xa = xb
    fxa = fxb
    xb = xc
    fxb = fxc
    print ( '  %4d  %14g  %14g' % ( step_num, xb, fxb ) )

  print ( '' )
  print ( '  Took maximum number of steps.' )

  return xa, xb, fxa, fxb

def secant_test ( ):

#*****************************************************************************80
#
## SECANT_TEST tests the secant method.
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
  from p00 import p00_fx
  from p00 import p00_prob_num
  from p00 import p00_rang
  from p00 import p00_root
  from p00 import p00_root_num
  from p00 import p00_start
  from p00 import p00_start_num

  print ( '' )
  print ( 'SECANT_TEST' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 2 ):
      print ( '  Do not have two starting values for this problem.' )
      continue

    rang = p00_rang ( prob )
    xmin = rang[0]
    xmax = rang[1]

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )

    xa2, xb2, fxa2, fxb2 = secant ( fatol, step_max, prob, xatol, xmin, xmax, \
      xa, xb, fxa, fxb )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14g                  %14g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SECANT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  secant_test ( )
  timestamp ( )

