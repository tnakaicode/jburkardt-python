#! /usr/bin/env python
#
def r8mat_solve ( n, nrhs, a ):

#*****************************************************************************80
#
## R8MAT_SOLVE uses Gauss-Jordan elimination to solve an N by N linear system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer NRHS, the number of right hand sides.  NRHS
#    must be at least 0.
#
#    Input, real A(N,N+NRHS), contains in rows and
#    columns 1 to N the coefficient matrix, and in columns N+1 through
#    N+NRHS, the right hand sides.
#
#    Output, real A(N,N+NRHS), the coefficient matrix
#    area has been destroyed, while the right hand sides have
#    been overwritten with the corresponding solutions.
#
#    Output, integer INFO, singularity flag.
#    0, the matrix was not singular, the solutions were computed;
#    J, factorization failed on step J, and the solutions could not
#    be computed.
#
  info = 0

  for j in range ( 0, n ):
#
#  Choose a pivot row IPIVOT.
#
    ipivot = j
    apivot = a[j,j]

    for i in range ( j + 1, n ):
      if ( abs ( apivot ) < abs ( a[i,j] ) ):
        apivot = a[i,j]
        ipivot = i

    if ( apivot == 0.0 ):
      info = j
      return a, info
#
#  Interchange.
#
    for k in range ( 0, n + nrhs ):
      temp        = a[ipivot,k]
      a[ipivot,k] = a[j,k]
      a[j,k]      = temp
#
#  A(J,J) becomes 1.
#
    a[j,j] = 1.0
    for k in range ( j + 1, n + nrhs ):
      a[j,k] = a[j,k] / apivot;
#
#  A(I,J) becomes 0.
#
    for i in range ( 0, n ):

      if ( i != j ):

        factor = a[i,j]
        a[i,j] = 0.0
        for k in range ( j + 1, n + nrhs ):
          a[i,k] = a[i,k] - factor * a[j,k]

  return a, info

def r8mat_solve_test ( ):

#*****************************************************************************80
#
## R8MAT_SOLVE_TEST tests R8MAT_SOLVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  n = 3
  rhs_num = 2
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0, 14.0,  7.0 ], \
    [ 4.0, 5.0, 6.0, 32.0, 16.0 ], \
    [ 7.0, 8.0, 0.0, 23.0,  7.0 ] ] )

  print ( '' )
  print ( 'R8MAT_SOLVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_SOLVE solves linear systems.' )
#
#  Print out the matrix to be inverted.
#
  r8mat_print ( n, n + rhs_num, a, '  The linear system:' )
#
#  Solve the systems.
#
  a, info = r8mat_solve ( n, rhs_num, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( '  The input matrix was singular.' )
    print ( '  The solutions could not be computed.' )
    return

  r8mat_print ( n, n + rhs_num, a, '  Factored matrix and solutions:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_SOLVE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_solve_test ( )
  timestamp ( )

