#! /usr/bin/env python3
#
def r8poly_lagrange_0 ( npol, xpol, xval ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_0 evaluates the Lagrange factor at a point.
#
#  Formula:
#
#    W(X) = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#  Discussion:
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
#    24 January 2004
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
#    Output, real WVAL, the value of the Lagrange factor at XVAL.
#
  import numpy as np

  wval = np.prod ( xval - xpol[:] )

  return wval

def r8poly_lagrange_0_test ( ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_0_TEST tests R8POLY_LAGRANGE_0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2018
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
  print ( 'R8POLY_LAGRANGE_0_TEST' )
  print ( '  R8POLY_LAGRANGE_0 evaluates the Lagrange' )
  print ( '  factor W(X) at a point.' )
  print ( '' )
  print ( '  The number of data points is %d' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = r8vec_even ( npol, xlo, xhi )

  r8vec_print ( npol, xpol, '  Abscissas:' )
#
#  Evaluate W(X).
#
  print ( '' )
  print ( '      X          W(X)' )
  print ( '' )

  nx = 4 * npol - 1

  for ival in range ( 1, nx + 1 ):

    xval = r8vec_even_select ( nx, xlo, xhi, ival )

    w = r8poly_lagrange_0 ( npol, xpol, xval )

    print ( '%12f  %12e' % ( xval, w ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_LAGRANGE_0_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_lagrange_0_test ( )
  timestamp ( )

