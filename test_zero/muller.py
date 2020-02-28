#! /usr/bin/env python
#
def muller ( fatol, step_max, prob, xatol, xrtol, xa, xb, xc, fxa, fxb, fxc ):

#*****************************************************************************80
#
## MULLER carries out Muller's method for a real root of a nonlinear function.
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
#    Input, real XATOL, XRTOL, absolute and relative error
#    tolerances  for the root.
#
#    Input/output, real XA, XB, XC, three points.
#
#    Input/output, real FXA, FXB, FXC, the value of the
#    function at XA, XB, and XC.
#
  from p00 import p00_fx
  from r8poly2_rroot import r8poly2_rroot
#
#  Initialization.
#
  print ( '' )
  print ( 'MULLER' )
  print ( '' )
  print ( '  Step      XA           XB           XC' )
  print ( '          F(XA)        F(XB)        F(XC)' )
  print ( '' )

  i = 0

  print ( '  %4d  %14g  %14g  %14g' % ( i,  xa,  xb,  xc ) )
  print ( '        %14g  %14g  %14g' % ( fxa, fxb, fxc ) )

  for i in range ( 1, step_max + 1 ):
#
#  Determine the coefficients
#    A, B, C
#  of the polynomial
#    Y(X) = A * (X-X2)^2 + B * (X-X2) + C
#  which goes through the data:
#    (X1,Y1), (X2,Y2), (X3,Y3).
#
    a = ( ( fxa - fxc ) * ( xb - xc ) \
        - ( fxb - fxc ) * ( xa - xc ) ) / \
          ( ( xa - xc ) * ( xb - xc ) * ( xa - xb ) )

    b = ( ( fxb - fxc ) * ( xa - xc ) * ( xa - xc ) \
        - ( fxa - fxc ) * ( xb - xc ) * ( xb - xc ) ) / \
        ( ( xa - xc ) * ( xb - xc ) * ( xa - xb ) )

    c = fxc
#
#  Get the real roots of the polynomial,
#  unless A = 0, in which case the algorithm is breaking down.
#
    if ( a != 0.0 ):

      z1, z2 = r8poly2_rroot ( a, b, c )

    elif ( b != 0.0 ):

      z2 = - c / b

    else:

      print ( '' )
      print ( '  Polynomial fitting has failed.' )
      print ( '  Muller\'s algorithm breaks down.' )
      return xa, xb, xc, fxa, fxb, fxc

    xd = xc + z2
#
#  Set XA, YA, based on which of XA and XB is closer to XD.
#
    if ( abs ( xd - xb ) < abs ( xd - xa ) ):
      t = xa
      xa = xb
      xb = t
      t = fxa
      fxa = fxb
      fxb = t
#
#  Set XB, YB, based on which of XB and XC is closer to XD.
#
    if ( abs ( xd - xc ) < abs ( xd - xb ) ):
      t = xb
      xb = xc
      xc = t
      t = fxb
      fxb = fxc
      fxc = t
#
#  Set XC, YC.
#
    xc = xd
    fxc = p00_fx ( prob, xc )

    print ( '  %4d  %14g  %14g  %14g' % ( i,  xa,  xb,  xc ) )
    print ( '        %14g  %14g  %14g' % ( fxa, fxb, fxc ) )
#
#  Estimate the relative significance of the most recent correction.
#
    if ( abs ( z2 ) <= xrtol * abs ( xc ) + xatol ):
      print ( '' )
      print ( '  Stepsize small enough for convergence.' )
      return xa, xb, xc, fxa, fxb, fxc

    if ( abs ( fxc ) < fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      return xa, xb, xc, fxa, fxb, fxc

  print ( '' )
  print ( '  Took maximum number of steps without convergence.' )

  return xa, xb, xc, fxa, fxb, fxc

def muller_test ( ):

#*****************************************************************************80
#
## MULLER_TEST tests the Muller method.
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
  print ( 'MULLER_TEST' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06
  xrtol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 3 ):
      print ( '  Do not have three starting values for this problem.' )
      continue

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    xc = p00_start ( prob, 3 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )
    fxc = p00_fx ( prob, xc )

    xa2, xb2, xc2, fxa2, fxb2, fxc2 = muller ( fatol, step_max, prob, xatol, \
      xrtol, xa, xb, xc, fxa, fxb, fxc )

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
  print ( 'MULLER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  muller_test ( )
  timestamp ( )

