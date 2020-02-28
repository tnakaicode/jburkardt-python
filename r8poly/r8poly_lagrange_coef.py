#! /usr/bin/env python3
#
def r8poly_lagrange_coef ( npol, ipol, xpol ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_COEF returns the coefficients of a Lagrange polynomial.
#
#  Discussion:
#
#    Given distinct abscissas XPOL(1:NPOL), the IPOL-th Lagrange
#    polynomial L(IPOL)(X) is defined as the polynomial of degree
#    NPOL - 1 which is 1 at XPOL(IPOL) and 0 at the NPOL - 1 other
#    abscissas.
#
#    A formal representation is:
#
#      L(IPOL)(X) = Product ( 1 <= I <= NPOL, I /= IPOL )
#       ( X - X(I) ) / ( X(IPOL) - X(I) )
#
#    However sometimes it is desirable to be able to write down
#    the standard polynomial coefficients of L(IPOL)(X).
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
#  Parameters:
#
#    Input, integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    Input, integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    Input, real XPOL(NPOL), the abscissas of the
#    Lagrange polynomials.  The entries in XPOL must be distinct.
#
#    Output, real PCOF(1:NPOL), the standard polynomial
#    coefficients of the IPOL-th Lagrange polynomial:
#      L(IPOL)(X) = SUM ( 0 <= I <= NPOL-1 ) PCOF(I+1) * X^I
#
  import numpy as np
  from r8vec_is_distinct import r8vec_is_distinct
  from sys import exit
#
#  Make sure IPOL is legal.
#
  if ( ipol < 1 or npol < ipol ):
    print ( '' )
    print ( 'R8POLY_LAGRANGE_COEF - Fatal error!' )
    print ( '  1 <= IPOL <= NPOL is required.' )
    exit ( 'R8POLY_LAGRANGE_COEF - Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'R8POLY_LAGRANGE_COEF - Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    exit ( 'R8POLY_LAGRANGE_COEF - Fatal error!' )

  pcof = np.zeros ( npol )

  pcof[0] = 1.0

  indx = 0

  for i in range ( 1, npol + 1 ):

    if ( i != ipol ):

      indx = indx + 1

      for j in range ( indx, -1, -1 ):

        pcof[j] = - xpol[i-1] * pcof[j] / ( xpol[ipol-1] - xpol[i-1] )

        if ( 0 < j ):
          pcof[j] = pcof[j] + pcof[j-1] / ( xpol[ipol-1] - xpol[i-1] )

  return pcof

def r8poly_lagrange_coef_test ( ):

#*****************************************************************************80
#
## R8POLY_LAGRANGE_COEF_TEST tests R8POLY_LAGRANGE_COEF.
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
  from r8poly_print import r8poly_print
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  npol = 5

  print ( '' )
  print ( 'R8POLY_LAGRANGE_COEF_TEST' )
  print ( '  R8POLY_LAGRANGE_COEF returns the coefficients' )
  print ( '  for a Lagrange basis polynomial.' )

  xpol = r8vec_indicator1 ( npol )

  r8vec_print ( npol, xpol, '  Abscissas:' )

  for ipol in range ( 1, npol + 1 ):

    pcof = r8poly_lagrange_coef ( npol, ipol, xpol )

    r8poly_print ( npol-1, pcof, '  The Lagrange basis polynomial:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_LAGRANGE_COEF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_lagrange_coef_test ( )
  timestamp ( )

