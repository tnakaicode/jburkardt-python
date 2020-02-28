#! /usr/bin/env python
#
def r8mat_cholesky_solve ( n, l, b ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_SOLVE solves a Cholesky factored linear system A * x = b.
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
#  Parameters:
#
#    Input, integer N, the number of rows and columns of the matrix A.
#
#    Input, real L(N,N), the N by N Cholesky factor of the
#    system matrix A.
#
#    Input, real B(N), the right hand side of the linear system.
#
#    Output, real X(N), the solution of the linear system.
#
  from r8mat_l_solve import r8mat_l_solve
  from r8mat_lt_solve import r8mat_lt_solve
#
#  Solve L * y = b.
#
  x = r8mat_l_solve ( n, l, b )
#
#  Solve L' * x = y.
#
  x = r8mat_lt_solve ( n, l, x )

  return x

def r8mat_cholesky_solve_test ( ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_SOLVE_TEST tests R8MAT_CHOLESKY_SOLVE.
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
  from r8mat_cholesky_factor import r8mat_cholesky_factor
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8MAT_CHOLESKY_SOLVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_CHOLESKY_SOLVE solves a linear system' )
  print ( '  using the lower triangular Cholesky factorization,' )
  print ( '  for a positive definite symmetric matrix.' )
  
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
#  Solve a linear system.
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
  r8vec_print ( n, b, '  Right hand side b:' )
  x = r8mat_cholesky_solve ( n, l, b )

  r8vec_print ( n, x, '  Computed solution x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_CHOLESKY_SOLVE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_cholesky_solve_test ( )
  timestamp ( )


