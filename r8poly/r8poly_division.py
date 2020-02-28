#! /usr/bin/env python3
#
def r8poly_division ( na, a, nb, b ):

#*****************************************************************************80
#
## r8poly_division computes the quotient and remainder of two polynomials.
#
#  Discussion:
#
#    The polynomials are assumed to be stored in power sum form.
#
#    The power sum form of a polynomial is:
#
#      p(x) = a(0) + a(1) * x + ... + a(n-1) * x^(n-1) + a(n) * x^(n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the dimension of A.
#
#    Input, real A(1:NA+1), the coefficients of the polynomial to be divided.
#
#    Input, integer NB, the dimension of B.
#
#    Input, real B(1:NB+1), the coefficients of the divisor polynomial.
#
#    Output, integer NQ, the degree of Q.
#    If the divisor polynomial is zero, NQ is returned as -1.
#
#    Output, real Q(1:NA-NB+1), contains the quotient of A/B.
#    If A and B have full degree, Q should be dimensioned Q(0:NA-NB).
#    In any case, Q(0:NA) should be enough.
#
#    Output, integer NR, the degree of R.
#    If the divisor polynomial is zero, NR is returned as -1.
#
#    Output, real R(1:NB), contains the remainder of A/B.
#    If B has full degree, R should be dimensioned R(0:NB-1).
#    Otherwise, R will actually require less space.
#
  import numpy as np
  from r8poly_degree import r8poly_degree

  na2 = r8poly_degree ( na, a )
  nb2 = r8poly_degree ( nb, b )

  if ( b[nb2] == 0.0 ):
    nq = -1
    q = np.zeros ( 0 )
    nr = -1
    r = np.zeros ( 0 )
    return nq, q, nr, r

  a2 = np.zeros ( na + 1 )
  for i in range ( 0, na + 1 ):
    a2[i] = a[i]

  nq = na2 - nb2
  q = np.zeros ( nq + 1 )

  for i in range ( nq, -1, -1 ):
    q[i] = a2[i+nb2] / b[nb2]
    a2[i+nb2] = 0.0
    for j in range ( 0, nb2 ):
      a2[i+j] = a2[i+j] - q[i] * b[j]

  nr = nb2 - 1
  r = np.zeros ( nr + 1 )
  for i in range ( 0, nr + 1 ):
    r[i] = a2[i]

  return nq, q, nr, r

def r8poly_division_test ( ):

#*****************************************************************************80
#
## r8poly_division_test tests r8poly_division.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8poly_print import r8poly_print

  print ( '' )
  print ( 'r8poly_division_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8poly_division computes the quotient and' )
  print ( '  remainder for polynomial division.' )
#
#  1: Divide X^3 + 2*X^2 - 5*X - 6  by X-2.  
#     Quotient is 3+4*X+X^2, remainder is 0.
#
#  2: Divide X^4 + 3*X^3 + 2*X^2 - 2  by  X^2 + X - 3.
#     Quotient is X^2 + 2*X + 3, remainder 8*X + 7.
#
#  3: Divide X^3 - 2*X^2 + 0*X - 4  by  X - 3.
#     Quotient is X^2 + X + 3, remainder 5.
#
  ntest = 3
  
  for test in range ( 0,  ntest ):

    if ( test == 0 ):
      na = 3
      a = np.array ( [ -6.0, -5.0, 2.0, 1.0 ] )
      nb = 1
      b = np.array ( [ -2.0, 1.0 ] )
    elif ( test == 1 ):
      na = 4
      a = np.array ( [ -2.0, 5.0, 2.0, 3.0, 1.0 ] )
      nb = 2
      b = np.array ( [ -3.0, 1.0, 1.0 ] )
    elif ( test == 2 ):
      na = 3
      a = np.array ( [ -4.0, 0.0, -2.0, 1.0 ] )
      nb = 1
      b = np.array ( [ -3.0, 1.0 ] )

    r8poly_print ( na, a, '  The polynomial to be divided, A:' )
    r8poly_print ( nb, b, '  The divisor polynomial, B:' )

    nq, q, nr, r = r8poly_division ( na, a, nb, b )
 
    r8poly_print ( nq, q, '  The quotient polynomial, Q:' )
    r8poly_print ( nr, r, '  The remainder polynomial, R:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly_division_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_division_test ( )
  timestamp ( )

