#! /usr/bin/env python
#
def r8mat_cholesky_factor ( n, a ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_FACTOR computes the Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric and positive semidefinite.
#
#    For a positive semidefinite symmetric matrix A, the Cholesky factorization
#    is a lower triangular matrix L such that:
#
#      A = L * L'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of the matrix A.
#
#    Input, real A(N,N), the matrix.
#
#    Output, real C(N,N), the N by N lower triangular Cholesky factor.
#
#    Output, boolean FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[0:j,j] = 0.0

    for i in range ( j, n ):

      sum2 = c[j,i]
      for k in range ( 0, j ):
        sum2 = sum2 - c[j,k] * c[i,k]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[i,j] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[i,j] = sum2 / c[j,j]
        else:
          c[i,j] = 0.0

  return c, flag

def r8mat_cholesky_factor_test ( ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_FACTOR_TEST tests R8MAT_CHOLESKY_FACTOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  n = 5

  print ( '' )
  print ( 'R8MAT_CHOLESKY_FACTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_CHOLESKY_FACTOR determines the' )
  print ( '  lower triangular Cholesky factorization' )
  print ( '  of a positive definite symmetric matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_CHOLESKY_FACTOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_cholesky_factor_test ( )
  timestamp ( )


