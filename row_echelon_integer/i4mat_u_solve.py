#! /usr/bin/env python
#
def i4mat_u_solve ( n, a, b ):

#*****************************************************************************80
#
## I4MAT_U_SOLVE solves an upper triangular linear system.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's, stored by (I,J) -> [I+J*M].
#
#    Note that, although A and B are integer valued, the solution X
#    may, in general, be real-valued.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2018
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
#    Input, integer A(N,N), the N by N upper triangular matrix.
#
#    Input, integer B(N), the right hand side of the linear system.
#
#    Output, real X(N), the solution of the linear system.
#
  import numpy as np
#
#  Solve U * x = b.
#
  x = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    x[i] = b[i]
    for j in range ( i + 1, n ):
      x[i] = x[i] - a[i,j] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def i4mat_u_solve_test ( ):

#*****************************************************************************80
#
## I4MAT_U_SOLVE_TEST tests I4MAT_U_SOLVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from i4vec_print import i4vec_print
  from r8vec_print import r8vec_print

  n = 4

  a = np.array ( [ \
    [ 1.0,  2.0,  4.0,  7.0 ], \
    [ 0.0,  3.0,  5.0,  8.0 ], \
    [ 0.0,  0.0,  6.0,  9.0 ], \
    [ 0.0,  0.0,  0.0, 10.0 ] ] )

  b = np.array ( [ 45.0, 53.0, 54.0, 40.0 ] )

  print ( '' )
  print ( 'I4MAT_U_SOLVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_U_SOLVE solves an upper triangular system.' )

  i4mat_print ( n, n, a, '  Input matrix A:' )

  i4vec_print ( n, b, '  Right hand side b:' )

  x = i4mat_u_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_U_SOLVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_u_solve_test ( )
  timestamp ( )
 
