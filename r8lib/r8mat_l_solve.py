#! /usr/bin/env python
#
def r8mat_l_solve ( n, a, b ):

#*****************************************************************************80
#
## R8MAT_L_SOLVE solves a lower triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
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
#    Input, integer N, the number of rows and columns of
#    the matrix A.
#
#    Input, real A(N,N), the N by N lower triangular matrix.
#
#    Input, real B(N), the right hand side of the linear system.
#
#    Output, real X(N), the solution of the linear system.
#
  import numpy as np

  x = np.zeros ( n )
#
#  Solve L * x = b.
#
  for i in range ( 0, n ):
    x[i] = b[i]
    for j in range ( 0, i ):
      x[i] = x[i] - a[i,j] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_l_solve_test ( ):

#*****************************************************************************80
#
## R8MAT_L_SOLVE_TEST tests R8MAT_L_SOLVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2015
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
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 2.0,  3.0,  0.0,  0.0 ], \
    [ 4.0,  5.0,  6.0,  0.0 ], \
    [ 7.0,  8.0,  9.0, 10.0 ] ] )

  b = np.array ( [ 1.0, 8.0, 32.0, 90.0 ] )

  print ( '' )
  print ( 'R8MAT_L_SOLVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_L_SOLVE solves a lower triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_l_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = r8vec_norm ( n, r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_L_SOLVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_l_solve_test ( )
  timestamp ( )
 
