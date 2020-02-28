#! /usr/bin/env python
#
def newton ( fatol, step_max, prob, xatol, xmin, xmax, xa, fxa ):

#*****************************************************************************80
#
## NEWTON carries out Newton's method to seek a root of F(X) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 May 2011
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
#    Input, real XMIN, XMAX, the interval in which the root should
#    be sought.
#
#    Input/output, real XA.  On input, the starting point for
#    the iteration.  On output, the current approximation to the root.
#
#    Input/output, real FXA, the function value at XA.
#
  from p00 import p00_fx
  from p00 import p00_fx1

  step = 0.0

  print ( '' )
  print ( 'NEWTON' )
  print ( '' )
  print ( '  Step         X             F(X)      FP(X)' )
  print ( '' )

  step_num = 0
  fp = p00_fx1 ( prob, xa )

  print ( '  %4d  %12g  %12g  %12g' % ( step_num, xa, fxa, fp ) )

  for step_num in range ( 1, step_max + 1 ):

    if ( xa < xmin or xmax < xa ):
      print ( '' )
      print ( '  The iterate X = %g' % ( xa ) )
      print ( '  has left the region [%g,%g].' % ( xmin, xmax ) )
      return xa, fxa

    if ( abs ( fxa ) <= fatol ):
      print ( '' )
      print ( '  The function norm is small enough for convergence.' )
      return xa, fxa

    if ( 1 < step_num and abs ( step ) <= xatol ):
      print ( '' )
      print ( '  The stepsize is small enough for convergence.' )
      return xa, fxa

    if ( fp == 0.0 ):
      print ( '' )
      print ( '  F\'(X)=0, the algorithm fails.' )
      return xa, fxa

    step = fxa / fp

    xa = xa - step

    fxa = p00_fx ( prob, xa )
    fp = p00_fx1 ( prob, xa )

    print ( '  %4d  %12g  %12g  %12g' % ( step_num, xa, fxa, fp ) )

  print ( '' )
  print ( '  Took maximum number of steps without convergence.' )

  return xa, fxa

def newton_test ( ):

#*****************************************************************************80
#
## NEWTON_TEST tests the Newton method.
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
  from p00 import p00_rang
  from p00 import p00_root
  from p00 import p00_root_num
  from p00 import p00_start

  print ( '' )
  print ( 'NEWTON_TEST' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem %d' % ( prob ) )

    rang = p00_rang ( prob )
    xmin = rang[0]
    xmax = rang[1]
    xa = p00_start ( prob, 1 )
    fxa = p00_fx ( prob, xa )
 
    xa2, fxa2 = newton ( fatol, step_max, prob, xatol, xmin, xmax, xa, fxa )

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
  print ( 'NEWTON_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  newton_test ( )
  timestamp ( )

