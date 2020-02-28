#! /usr/bin/env python
#
def spofa ( a, lda, n ):

#*****************************************************************************80
#
## SPOFA factors a real symmetric positive definite matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    FORTRAN77 version by Cleve Moler.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real A(LDA,N), the symmetric matrix to be factored.  Only the 
#    diagonal and upper triangle are accessed.
#
#    Input, integer LDA, the leading dimension of the array A.
#    N <= LDA.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A_FAC(LDA,N), an upper triangular matrix R such that
#    A = R' * R.  If INFO is nonzero, the factorization was not completed.
#
#    Output, integer INFO, error flag.
#    0, no error was detected.
#    K, the leading minor of order K is not positive definite.
#
  import numpy as np

  a_fac = a.copy ( )

  for i in range ( 1, n ):
    for j in range ( 0, i ):
      a_fac[i,j] = 0.0

  info = 0

  for j in range ( 0, n ):
    s = 0.0
    for k in range ( 0, j ):
      t = a_fac[k,j]
      for i in range ( 0, k ):
        t = t - a_fac[i,k] * a_fac[i,j]
      t = t / a_fac[k,k]
      a_fac[k,j] = t
      s = s + t * t

    s = a_fac[j,j] - s
    if ( s <= 0.0 ):
      info = j + 1
      return a_fac, info

    a_fac[j,j] = np.sqrt ( s )

  return a_fac, info

def spofa_test ( ):

#*****************************************************************************80
#
## SPOFA_TEST tests SPOFA.
#
#  Discussion:
#
#    SPOFA factors a positive definite symmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  lda = n

  print ( '' )
  print ( 'SPOFA_TEST' )
  print ( '  SPOFA computes the LU factors of a positive definite symmetric matrix,' )
#
#  Set the matrix A.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    a[i,i] = 2.0
    if ( 0 < i ):
      a[i,i-1] = -1.0
    if ( i < n - 1 ):
      a[i,i+1] = -1.0

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '    ' ),
    for j in range ( 0, n ):
      print ( '%g' % ( a[i,j] ) ),
    print ( '' )
#
#  Factor the matrix.
#
  print ( '' )
  print ( '  Call SPOFA to factor the matrix.' )

  a_lu, info = spofa ( a, lda, n )
 
  if ( info != 0 ):
    print ( '' )
    print ( '  Error, SPOFA returns INFO = %d' % ( info ) )
    return

  print ( '' )
  print ( '  Upper triangular factor U:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '    ' ),
    for j in range ( 0, n ):
      print ( '%8g' % ( a_lu[i,j] ) ),
    print ( '' )

  uut = np.dot ( np.transpose ( a_lu ), a_lu )

  print ( '' )
  print ( '  Product Ut * U:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '    ' ),
    for j in range ( 0, n ):
      print ( '%8g' % ( uut[i,j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPOFA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  spofa_test ( )
  timestamp ( )


