#! /usr/bin/env python
#
def r8mat_cholesky_factor_upper ( n, a ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_FACTOR_UPPER: upper Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric and positive semidefinite.
#
#    For a positive semidefinite symmetric matrix A, the upper Cholesky 
#    factorization is an upper triangular matrix R such that:
#
#      A = R' * R
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2017
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
#    Output, real C(N,N), the N by N upper triangular Cholesky factor.
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

    c[j,0:j] = 0.0

    for i in range ( j, n ):

      sum2 = c[i,j]
      for k in range ( 0, j ):
        sum2 = sum2 - c[k,j] * c[k,i]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[j,i] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[j,i] = sum2 / c[j,j]
        else:
          c[j,i] = 0.0

  return c, flag

def r8mat_cholesky_factor_upper_test ( ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_FACTOR_UPPER_TEST tests R8MAT_CHOLESKY_FACTOR_UPPER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2017
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
  print ( 'R8MAT_CHOLESKY_FACTOR_UPPER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_CHOLESKY_FACTOR_UPPER determines the' )
  print ( '  upper triangular Cholesky factorization' )
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
  r, flag = r8mat_cholesky_factor_upper ( n, a )
  r8mat_print ( n, n, r, '  Cholesky factor R:' )
  d = np.dot ( r.transpose ( ), r )
  r8mat_print ( n, n, d, '  Product R\' * R:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_CHOLESKY_FACTOR_UPPER_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_cholesky_factor_upper_test ( )
  timestamp ( )


