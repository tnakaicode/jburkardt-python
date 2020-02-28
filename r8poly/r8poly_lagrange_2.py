#! /usr/bin/env python3
#
def r8poly_lagrange_2 ( npol, xpol, xval ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_2 evaluates the second derivative of the Lagrange factor.
#
#  Formula:
#
#    W(X)  = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#    W'(X) = Sum ( 1 <= J <= NPOL )
#            Product ( I /= J ) ( X - XPOL(I) )
#
#    W"(X) = Sum ( 1 <= K <= NPOL )
#            Sum ( J =/ K )
#            Product ( I /= K, J ) ( X - XPOL(I) )
#
#    For a set of points XPOL(I), 1 <= I <= NPOL, the IPOL-th Lagrange basis
#    polynomial L(IPOL)(X), has the property:
#
#      L(IPOL)( XPOL(J) ) = delta ( IPOL, J )
#
#    and may be expressed as:
#
#      L(IPOL)(X) = W(X) / ( ( X - XPOL(IPOL) ) * W'(XPOL(IPOL)) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    Input, real XPOL(NPOL), the abscissas, which should be distinct.
#
#    Input, real XVAL, the point at which the Lagrange factor is to be
#    evaluated.
#
#    Output, real DW2DX2, the second derivative of W with respect to XVAL.
#
  dw2dx2 = 0.0

  for k in range ( 0, npol ):

    for j in range ( 0, npol ):

      if ( j != k ):
        term = 1.0

        for i in range ( 0, npol ):
          if ( i != j and i != k ):
            term = term * ( xval - xpol[i] )

        dw2dx2 = dw2dx2 + term

  return dw2dx2

def r8poly_lagrange_2_test ( ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_2_TEST tests R8POLY_LAGRANGE_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
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
  print ( 'R8POLY_LAGRANGE_2_TEST' )
  print ( '  R8POLY_LAGRANGE_2 evaluates the Lagrange' )
  print ( '  factor W"(X) at a point.' )
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
  print ( '      X          W"(X)' )
  print ( '' )

  nx = 4 * npol - 1

  for ival in range ( 1, nx + 1 ):

    xval = r8vec_even_select ( nx, xlo, xhi, ival )
    dw2dx2 = r8poly_lagrange_2 ( npol, xpol, xval )

    print ( ' %12f  %12e' % ( xval, dw2dx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_LAGRANGE_2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_lagrange_2_test ( )
  timestamp ( )

