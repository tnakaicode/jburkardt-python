#! /usr/bin/env python
#
def r8poly_n2p ( n, a, xarray ):

#*****************************************************************************80
#
## R8POLY_N2P converts a real polynomial from Newton form to power sum form.
#
#  Discussion:
#
#    This is done by shifting all the Newton abscissas to zero.
#
#    Actually, what happens is that the abscissas of the Newton form
#    are all shifted to zero, which means that A is the power sum
#    polynomial description and A, XARRAY is the Newton polynomial
#    description.  It is only because all the abscissas are shifted to
#    zero that A can be used as both a power sum and Newton polynomial
#    coefficient array.
#
#    The Newton form of a polynomial is described by an array of N coefficients
#    A and N abscissas X:
#
#      p(x) =   a(1)
#             + a(2) * (x-x(1))
#             + a(3) * (x-x(1)) * (x-x(2))
#             ...
#             + a(n) * (x-x(1)) * (x-x(2)) * ... * (x-x(n-1))
#
#    X(N) does not occur explicitly in the formula for the evaluation of p(x),
#    although it is used in deriving the coefficients A.
#
#    The power sum form of a polynomial is:
#
#      p(x) = a(1) + a(2)*x + ... + a(n-1)*x^(n-2) + a(n)*x^(n-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A(N), the coefficients of the polynomial in Newton
#    form.
#
#    Input, real XARRAY(N), the abscissas of the Newton form of the
#    polynomial.
#
#    Output, real A(N), the coefficients in power sum form.
#
  from r8poly_nx import r8poly_nx

  x = 0.0
  for i in range ( 0, n ):
    a, xarray = r8poly_nx ( n, a, xarray, x )

  return a

def r8poly_n2p_test ( ):

#*****************************************************************************80
#
## R8POLY_N2P_TEST tests R8POLY_N2P.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8poly_p2n import r8poly_p2n
  from r8poly_print import r8poly_print
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 4
  ap = r8vec_indicator1 ( n )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = 2.0 * ap[i]
 
  print ( '' )
  print ( 'R8POLY_N2P_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_N2P: Newton => power sum' )

  r8poly_print ( n - 1, ap, '  The power sum polynomial:' )
 
  an = r8poly_p2n ( n, ap, x )
 
  r8vec_print ( n, an,  '  Newton polynomial coefficients:' )
  r8vec_print ( n, x,  '  Newton polynomial abscissas:' )
 
  ap2 = r8poly_n2p ( n, an, x )
 
  r8poly_print ( n-1, ap2, '  The recovered power sum polynomial:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_N2P_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_n2p_test ( )
  timestamp ( )

