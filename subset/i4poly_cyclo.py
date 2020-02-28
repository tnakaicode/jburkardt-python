#! /usr/bin/env python
#
def i4poly_cyclo ( n ):

#*****************************************************************************80
#
## I4POLY_CYCLO computes a cyclotomic polynomial.
#
#  Discussion:
#
#    For 1 <= N, let
#
#      I = SQRT ( - 1 )
#      L = EXP ( 2 * PI * I / N )
#
#    Then the N-th cyclotomic polynomial is defined by
#
#      PHI(NX) = Product ( 1 <= K <= N and GCD(K,N) = 1 ) ( X - L^K )
#
#    We can use the Moebius MU function to write
#
#      PHI(NX) = Product ( mod ( D, N ) = 0 ) ( X^D - 1 )^MU(N/D)
#
#    There is a sort of inversion formula:
#
#      X^N - 1 = Product ( mod ( D, N ) = 0 ) PHI(DX)
#
#  Example:
#
#     N  PHI
#
#     0  1
#     1  X - 1
#     2  X + 1
#     3  X^2 + X + 1
#     4  X^2 + 1
#     5  X^4 + X^3 + X^2 + X + 1
#     6  X^2 - X + 1
#     7  X^6 + X^5 + X^4 + X^3 + X^2 + X + 1
#     8  X^4 + 1
#     9  X^6 + X^3 + 1
#    10  X^4 - X^3 + X^2 - X + 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Raymond Seroul,
#    Programming for Mathematicians,
#    Springer Verlag, 2000, page 269.
#
#  Parameters:
#
#    Input, integer N, the index of the cyclotomic polynomial desired.
#
#    Output, integer PHI(1:N+1), the N-th cyclotomic polynomial.
#
  import numpy as np
  from i4_moebius import i4_moebius
  from i4poly_div import i4poly_div
  from i4poly_mul import i4poly_mul
  from sys import exit

  max_poly = 100

  num = np.zeros ( max_poly )
  num[0] = 1
  num_n = 0

  den = np.zeros ( max_poly )
  den[0] = 1
  den_n = 0

  for d in range ( 1, n + 1 ):
#
#  For each divisor D of N, ...
#
    if ( ( n % d ) == 0 ):

      arg = ( n // d )
      mu = i4_moebius ( arg )
#
#  ...multiply the numerator or denominator by (X^D-1).
#
      factor = np.zeros ( d + 1 )

      factor[0] = -1
      for i in range ( 1, d ):
        factor[i] = 0
      factor[d] = 1

      if ( mu == +1 ):

        if ( max_poly < num_n + d ):
          print ( '' )
          print ( 'I4POLY_CYCLO - Fatal error!' )
          print ( '  Numerator polynomial degree too high.' )
          exit ( 'I4POLY_CYCLO - Fatal error!' )

        num = i4poly_mul ( num_n, num, d, factor )

        num_n = num_n + d

      elif ( mu == -1 ):

        if ( max_poly < den_n + d ):
          print ( '' )
          print ( 'I4POLY_CYCLO - Fatal error!' )
          print ( '  Denominator polynomial degree too high.' )
          exit ( 'I4POLY_CYCLO - Fatal error!' )

        den = i4poly_mul ( den_n, den, d, factor )

        den_n = den_n + d
#
#  PHI = NUM / DEN
#
  nq, q, nr, rem = i4poly_div ( num_n, num, den_n, den )

  phi = np.zeros ( n + 1 )
  for i in range ( 0, nq + 1 ):
    phi[i] = q[i]

  return phi

def i4poly_cyclo_test ( ):

#*****************************************************************************80
#
## I4POLY_CYCLO_TEST tests I4POLY_CYCLO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4poly_print import i4poly_print
  
  print ( '' )
  print ( 'I4POLY_CYCLO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4POLY_CYCLO computes cyclotomic polynomials.' )

  for n in range ( 0, 11 ):

    print ( '' )
    print ( '  N = %d' % ( n ) )

    phi = i4poly_cyclo ( n )

    i4poly_print ( n, phi, '  The cyclotomic polynomial:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4POLY_CYCLO_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_cyclo_test ( )
  timestamp ( )

