#! /usr/bin/env python
#
def i4poly_div ( na, a, nb, b ):

#*****************************************************************************80
#
## I4POLY_DIV computes the quotient and remainder of two polynomials.
#
#  Discussion:
#
#    Normally, the quotient and remainder would have rational coefficients.
#    This routine assumes that the special case applies that the quotient
#    and remainder are known beforehand to be integral.
#
#    The polynomials are assumed to be stored in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#    Since MATLAB will not allow 0-based indices, the algorithm has been
#    crudely modified by adding one to all array indices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the dimension of A.
#
#    Input, integer A(1:NA+1), the coefficients of the polynomial to be divided.
#
#    Input, integer NB, the dimension of B.
#
#    Input, integer B(1:NB+1), the coefficients of the divisor polynomial.
#
#    Output, integer NQ, the degree of Q.
#    If the divisor polynomial is zero, NQ is returned as -1.
#
#    Output, integer Q(1:NA-NB+1), contains the quotient of A/B.
#    If A and B have full degree, Q should be dimensioned Q(1:NA-NB+1).
#    In any case, Q(1:NA+1) should be enough.
#
#    Output, integer NR, the degree of R.
#    If the divisor polynomial is zero, NR is returned as -1.
#
#    Output, integer R(1:NB), contains the remainder of A/B.
#    If B has full degree, R should be dimensioned R(1:NB).
#    Otherwise, R will actually require less space.
#
  import numpy as np
  from i4poly_degree import i4poly_degree

  na2 = i4poly_degree ( na, a )
  nb2 = i4poly_degree ( nb, b )

  if ( b[nb2] == 0 ):
    nq = -1
    q = np.zeros ( 0 )
    nr = -1
    r = np.zeros ( 0 )
    return nq, q, nr, r

  a2 = np.zeros ( na + 1, dtype = np.int32 )
  for i in range ( 0, na + 1 ):
    a2[i] = a[i]

  nq = na2 - nb2
  q = np.zeros ( nq + 1, dtype = np.int32 )

  for i in range ( nq, -1, -1 ):
    q[i] = a2[i+nb2] // b[nb2]
    a2[i+nb2] = 0
    for j in range ( 0, nb2 ):
      a2[i+j] = a2[i+j] - q[i] * b[j]

  nr = nb2 - 1
  r = np.zeros ( nr + 1, dtype = np.int32 )

  for i in range ( 0, nr + 1 ):
    r[i] = a2[i]

  return nq, q, nr, r

def i4poly_div_test ( ):

#*****************************************************************************80
#
## I4POLY_DIV_TEST tests I4POLY_DIV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4poly_print import i4poly_print

  ntest = 2

  print ( '' )
  print ( 'I4POLY_DIV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4POLY_DIV computes the quotient and' )
  print ( '  remainder for polynomial division.' )
  print ( '' )
#
#  1: Divide X^3 + 2*X^2 - 5*X - 6  by X-2.  
#     Quotient is 3+4*X+X^2, remainder is 0.
#
#  2: Divide X^4 + 3*X^3 + 2*X^2 - 2  by  X^2 + X - 3.
#     Quotient is X^2 + 2*X + 3, remainder 8*X + 7.
#
  for test in range ( 0, ntest ):

    if ( test == 0 ):
      na = 3
      a = np.array ( [ -6, -5, 2, 1 ] )
      nb = 1
      b = np.array ( [ -2, 1 ] )
    elif ( test == 1 ):
      na = 4
      a = np.array ( [ -2, 5, 2, 3, 1 ] )
      nb = 2
      b = np.array ( [ -3, 1, 1 ] )

    i4poly_print ( na, a, '  The polynomial to be divided, A:' )
    i4poly_print ( nb, b, '  The divisor polynomial, B:' )

    nq, q, nr, r = i4poly_div ( na, a, nb, b )
 
    i4poly_print ( nq, q, '  The quotient polynomial, Q:' )
    i4poly_print ( nr, r, '  The remainder polynomial, R:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4POLY_DIV_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_div_test ( )
  timestamp ( )

