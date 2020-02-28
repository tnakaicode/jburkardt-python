#! /usr/bin/env python3
#
def r8poly_lagrange_value ( npol, ipol, xpol, xval ):

#*****************************************************************************80
#
## r8poly_lagrange_value evaluates the IPOL-th Lagrange polynomial.
#
#  Discussion:
#
#    Given NPOL distinct abscissas, XPOL(1:NPOL), the IPOL-th Lagrange
#    polynomial L(IPOL)(X) is defined as the polynomial of degree
#    NPOL - 1 which is 1 at XPOL(IPOL) and 0 at the NPOL - 1 other
#    abscissas.
#
#    A formal representation is:
#
#      L(IPOL)(X) = Product ( 1 <= I <= NPOL, I /= IPOL )
#       ( X - X(I) ) / ( X(IPOL) - X(I) )
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
#    Input, integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    Input, real XPOL(NPOL), the abscissas of the Lagrange
#    polynomials.  The entries in XPOL must be distinct.
#
#    Input, real XVAL, the point at which the IPOL-th 
#    Lagrange polynomial is to be evaluated.
#
#    Output, real PVAL, the value of the IPOL-th Lagrange
#    polynomial at XVAL.
#
#    Output, real DPDX, the derivative of the IPOL-th 
#    Lagrange polynomial at XVAL.
#
  from r8vec_is_distinct import r8vec_is_distinct
  from sys import exit
#
#  Make sure IPOL is legal.
#
  if ( ipol < 0 or npol <= ipol ):
    print ( '' )
    print ( 'r8poly_lagrange_value - Fatal error!' )
    print ( '  0 <= IPOL < NPOL is required.' )
    exit ( 'r8poly_lagrange_value - Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'r8poly_lagrange_value - Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    exit ( 'r8poly_lagrange_value - Fatal error!' )
#
#  Evaluate the polynomial.
#
  pval = 1.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      pval = pval * ( xval - xpol[i] ) / ( xpol[ipol] - xpol[i] )
#
#  Evaluate the derivative, which can be found by summing up the result
#  of differentiating one factor at a time, successively.
#
  dpdx = 0.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      p2 = 1.0
      for j in range ( 0, npol ):

        if ( j == i ):
          p2 = p2                      / ( xpol[ipol] - xpol[j] )
        elif ( j != ipol ):
          p2 = p2 * ( xval - xpol[j] ) / ( xpol[ipol] - xpol[j] )

      dpdx = dpdx + p2

  return pval, dpdx

def r8poly_lagrange_value_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_value_test tests r8poly_lagrange_value().
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
  print ( 'r8poly_lagrange_value_test' )
  print ( '  r8poly_lagrange_value() evaluates a Lagrange' )
  print ( '  interpolating polynomial at a point.' )
  print ( '' )
  print ( '  Number of data points = #d', npol )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1
  xpol = r8vec_even ( npol, xlo, xhi )
 
  r8vec_print ( npol, xpol, '  Abscissas:' )
#
#  Evaluate the polynomials.
#
  print ( '' )
  print ( '  Here are the values of the functions at' )
  print ( '  several points:' )
  print ( '' )
  print ( '      X          L1          L2          L3      L4' )
  print ( '          L5' )
  print ( '' )
 
  nx = 2 * npol - 1
 
  for ival in range ( 1, nx + 1 ):
 
    xval = r8vec_even_select ( nx, xlo, xhi, ival )
    print ( '  %10f' % ( xval ) ),

    for ipol in range ( 0, npol ):
      pval, dpdx =  r8poly_lagrange_value ( npol, ipol, xpol, xval )
 
      print ( '  %10f' % ( pval ) ),

    print ( '' )
 
  print ( '' )
  print ( '  And the derivatives:' )
  print ( '' )
  print ( '      X          L''1         L''2         L''3' )
  print ( '     L''4         L''5' )
  print ( '' )
 
  nx = 2 * npol - 1
 
  for ival in range ( 1, nx + 1 ):
 
    xval = r8vec_even_select ( nx, xlo, xhi, ival )
    print ( '  %10f' % ( xval ) ),

    for ipol in range ( 0, npol ):
      pval, dpdx =  r8poly_lagrange_value ( npol, ipol, xpol, xval )
 
      print ( '  %10f' % ( dpdx ) ),

    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly_lagrange_value_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_lagrange_value_test ( )
  timestamp ( )

