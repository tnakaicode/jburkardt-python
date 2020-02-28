#! /usr/bin/env python3
#
def r8poly_lagrange_1 ( npol, xpol, xval ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_1 evaluates the first derivative of the Lagrange factor.
#
#  Formula:
#
#    W(XPOL(1:NPOL))(X) = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#    W'(XPOL(1:NPOL))(X)
#      = Sum ( 1 <= J <= NPOL ) Product ( I /= J ) ( X - XPOL(I) )
#
#    We also have the recursion:
#
#      W'(XPOL(1:NPOL))(X) = d/dX ( ( X - XPOL(NPOL) ) * W(XPOL(1:NPOL-1))(X) )
#                    = W(XPOL(1:NPOL-1))(X)
#                    + ( X - XPOL(NPOL) ) * W'(XPOL(1:NPOL-1))(X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NPOL, the number of abscissas.
#
#    Input, real XPOL(NPOL), the abscissas, which should be distinct.
#
#    Input, real XVAL, the point at which the Lagrange factor is to be
#    evaluated.
#
#    Output, real DWDX, the derivative of W with respect to XVAL.
#
  dwdx = 0.0
  w = 1.0

  for i in range ( 0, npol ):

    dwdx = w + ( xval - xpol[i] ) * dwdx
    w = w * ( xval - xpol[i] )

  return dwdx

def r8poly_lagrange_1_test ( ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_1_TEST tests R8POLY_LAGRANGE_1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 August 2018
#
#  Author:
#
#    John Burkardt
#
  from r8vec_even import r8vec_even
  from r8vec_even_select import r8vec_even_select
  from r8vec_print import r8vec_print

  npol = 5

  print ( '' )
  print ( 'R8POLY_LAGRANGE_1_TEST' )
  print ( '  R8POLY_LAGRANGE_1 evaluates the Lagrange' )
  print ( '  factor W''(X) at a point.' )
  print ( '' )
  print ( '  The number of data points is %d' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = r8vec_even ( npol, xlo, xhi )

  r8vec_print ( npol, xpol, '  Abscissas:' )

  print ( '' )
  print ( '      X          W''(X)' )
  print ( '' )

  nx = 4 * npol - 1

  for ival in range ( 1, nx + 1 ):

    xval = r8vec_even_select ( nx, xlo, xhi, ival )

    dwdx = r8poly_lagrange_1 ( npol, xpol, xval )

    print ( '  %12f  %12f' % ( xval, dwdx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_LAGRANGE_1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_lagrange_1_test ( )
  timestamp ( )

