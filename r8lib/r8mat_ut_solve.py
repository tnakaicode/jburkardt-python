#! /usr/bin/env python
#
def r8mat_ut_solve ( n, a, b ):

#*****************************************************************************80
#
## R8MAT_UT_SOLVE solves a transposed upper triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#    Given the upper triangular matrix A, the linear system to be solved is:
#
#      A' * x = b
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns
#    of the matrix.
#
#    Input, real A(N,N), the N by N upper triangular matrix.
#
#    Input, real B(N,1), the right hand side of the linear system.
#
#    Output, real X(N,1), the solution of the linear system.
#
  import numpy as np
#
#  Solve U' * x = b.
#
  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
    for j in range ( 0, i ):
      x[i] = x[i] - a[j,i] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_ut_solve_test ( ):

#*****************************************************************************80
#
## R8MAT_UT_SOLVE_TEST tests R8MAT_UT_SOLVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8vec_norm import r8vec_norm
  from r8vec_print import r8vec_print

  n = 4

  a = np.array ( [ \
    [ 1.0,  2.0,  4.0,  7.0 ], \
    [ 0.0,  3.0,  5.0,  8.0 ], \
    [ 0.0,  0.0,  6.0,  9.0 ], \
    [ 0.0,  0.0,  0.0, 10.0 ] ] )

  b = np.array ( [ 1.0, 8.0, 32.0, 90.0 ] )

  print ( '' )
  print ( 'R8MAT_UT_SOLVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UT_SOLVE solves a transposed upper triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_ut_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( np.transpose ( a ), x ) - b

  rnorm = r8vec_norm ( n, r )

  print ( '' )
  print ( '  Norm of A\'*x-b = %g' % ( rnorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UT_SOLVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_ut_solve_test ( )
  timestamp ( )
 
