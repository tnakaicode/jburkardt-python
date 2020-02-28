#! /usr/bin/env python3
#
def r8poly_lagrange_factor ( npol, xpol, xval ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_FACTOR evaluates the polynomial Lagrange factor at a point.
#
#  Formula:
#
#    W(X) = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#  Discussion:
#
#    Suppose F(X) is at least N times continuously differentiable in the
#    interval [A,B].  Pick NPOL distinct points XPOL(I) in [A,B] and compute
#    the interpolating polynomial P(X) of order NPOL ( and degree NPOL-1)
#    which passes through all the points ( XPOL(I), F(XPOL(I)) ).
#    Then in the interval [A,B], the maximum error
#
#      abs ( F(X) - P(X) )
#
#    is bounded by:
#
#      C * FNMAX * W(X)
#
#    where
#
#      C is a constant,
#      FNMAX is the maximum value of the NPOL-th derivative of F in [A,B],
#      W(X) is the Lagrange factor.
#
#    Thus, the value of W(X) is useful as part of an estimated bound
#    for the interpolation error.
#
#    Note that the Chebyshev abscissas have the property that they minimize
#    the value of W(X) over the interval [A,B].  Hence, if the abscissas may
#    be chosen arbitrarily, the Chebyshev abscissas have this advantage over
#    other choices.
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
#    Input, real XPOL(NPOL), the abscissas, which should 
#    be distinct.
#
#    Input, real XVAL, the point at which the Lagrange 
#    factor is to be evaluated.
#
#    Output, real WVAL, the value of the Lagrange factor at XVAL.
#
#    Output, real DWDX, the derivative of W with respect to XVAL.
#
  import numpy as np

  wval = np.prod ( xval - xpol[:] )

  dwdx = 0.0

  for i in range ( 0, npol ):

    term = 1.0

    for j in range ( 0, npol ):
      if ( i != j ):
        term = term * ( xval - xpol[j] )

    dwdx = dwdx + term

  return wval, dwdx

def r8poly_lagrange_factor_test ( ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_FACTOR_TEST tests R8POLY_LAGRANGE_FACTOR.
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
  import numpy as np
  from r8vec_even_select import r8vec_even_select
  from r8vec_print import r8vec_print

  npol = 5

  print ( '' )
  print ( 'R8POLY_LAGRANGE_FACTOR_TEST' )
  print ( '  R8POLY_LAGRANGE_FACTOR evaluates the Lagrange' )
  print ( '  factor W(X) at a point.' )
  print ( '' )
  print ( '  For this test, we use %d functions.' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = np.zeros ( npol)

  for i in range ( 0, npol ):
    xpol[i] = ( ( npol - i ) * xlo \
              + (        i ) * xhi )\
              / ( npol             )
 
  r8vec_print ( npol, xpol, '  Abscissas:' )
#
#  Evaluate W(X) and W'(X).
#
  print ( '' )
  print ( '      X          W(X)          W''(X)' )
  print ( '' )
  
  for i in range ( 0, 2 * npol ):

    xval = r8vec_even_select ( 2 * npol - 1, xhi, xlo, i )
 
    wval, dwdx = r8poly_lagrange_factor ( npol, xpol, xval )
 
    print ( '  %10f  %10f  %10f' % ( xval, wval, dwdx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_LAGRANGE_FACTOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_lagrange_factor_test ( )
  timestamp ( )


