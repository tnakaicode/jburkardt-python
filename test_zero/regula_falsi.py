#! /usr/bin/env python
#
def regula_falsi ( fatol, step_max, prob, xatol, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## REGULA_FALSI carries out the Regula Falsi method to seek a root of F(X) = 0.
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
#    Input/output, real XA, XB, two points at which the 
#    function differs in sign.  On output, these values have been adjusted
#    to a smaller interval.
#
#    Input/output, real FXA, FXB, the value of the function 
#    at XA and XB.
# 
  from p00 import p00_fx
  from r8_sign import r8_sign
  from sys import exit
#
#  The method requires a change-of-sign interval.
#
  if ( r8_sign ( fxa ) == r8_sign ( fxb ) ):
    print ( '' )
    print ( 'REGULA_FALSI - Fatal error!' )
    print ( '  Function does not change sign at endpoints.' )
    exit ( 'REGULA_FALSI - Fatal error!' )
#
#  Make A the root with negative F, B the root with positive F.
#
  if ( 0.0 < fxa ):
    t = xa
    xa = xb
    xb = t
    t = fxa
    fxa = fxb
    fxb = t

  print ( '' )
  print ( 'REGULA FALSI' )
  print ( '' )
  print ( '  Step            XA            XB             F(XA)         F(XB)' )
  print ( '' )

  step_num = 0
  print ( '  %4d  %14g  %14g  %14g  %14g' % ( step_num, xa, xb, fxa, fxb ) )

  for step_num in range ( 1, step_max + 1 ):

    if ( abs ( xa - xb ) < xatol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      return xa, xb, fxa, fxb

    if ( abs ( fxa ) <= fatol or abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      return xa, xb, fxa, fxb

    xc = ( fxa * xb - fxb * xa ) / ( fxa - fxb )
    fxc = p00_fx ( prob, xc )

    if ( fxc < 0.0 ):
      xa = xc
      fxa = fxc
    else:
      xb = xc
      fxb = fxc

    print ( '  %4d  %14g  %14g  %14g  %14g' % ( step_num, xa, xb, fxa, fxb ) )

  print ( '' )
  print ( '  Took maximum number of steps without convergence.' )

  return xa, xb, fxa, fxb

def regula_falsi_test ( ):

#*****************************************************************************80
#
## REGULA_FALSI_TEST tests the regula falsi method.
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
  from p00 import p00_root
  from p00 import p00_root_num
  from p00 import p00_start
  from p00 import p00_start_num

  print ( '' )
  print ( 'REGULA_FALSI_TEST' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

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

    xa2, xb2, fxa2, fxb2 = regula_falsi ( fatol, step_max, prob, xatol, \
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
  print ( 'REGULA_FALSI_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  regula_falsi_test ( )
  timestamp ( )

