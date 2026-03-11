#! /usr/bin/env python3
#
def r83s_test ( ):

#*****************************************************************************80
#
## r83s_test() tests r83s().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83s_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r83s().' )

  rng = default_rng ( )

  r83s_cg_test ( rng )
  r83s_dif2_test ( )
  r83s_gs_sl_test ( rng )
  r83s_indicator_test ( )
  r83s_jac_sl_test ( rng )
  r83s_mtv_test ( rng )
  r83s_mv_test ( rng )
  r83s_print_test ( )
  r83s_print_some_test ( )
  r83s_random_test ( rng )
  r83s_res_test ( rng )
  r83s_to_r8ge_test ( rng )
  r83s_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83s_test():' )
  print ( '  Normal end of execution.' )
  return

def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10() returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def r83s_cg ( n, a, b, x_init ):

#*****************************************************************************80
#
## r83s_cg() uses the conjugate gradient method on an R83S system.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#    The matrix A must be a positive definite symmetric band matrix.
#
#    The method is designed to reach the solution after N computational
#    steps.  However, roundoff may introduce unacceptably large errors for
#    some problems.  In such a case, calling the routine again, using
#    the computed solution as the new starting estimate, should improve
#    the results.
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Beckman,
#    The Solution of Linear Equations by the Conjugate Gradient Method,
#    in Mathematical Methods for Digital Computers,
#    edited by John Ralston, Herbert Wilf,
#    Wiley, 1967,
#    ISBN: 0471706892,
#    LC: QA76.5.R3.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(3), the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X_INIT(N), an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N), the approximate solution vector.
#
  import numpy as np

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = x_init[i]
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r83s_mv ( n, n, a, x )

  r = np.zeros ( n )
  for i in range ( 0, n ):
    r[i] = b[i] - ap[i]

  p = np.zeros ( n )
  for i in range ( 0, n ):
    p[i] = b[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r83s_mv ( n, n, a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr = np.dot ( p, r )

    if ( pap == 0.0 ):
      return x

    alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
    for i in range ( 0, n ):
      x[i] = x[i] + alpha * p[i]

    for i in range ( 0, n ):
      r[i] = r[i] - alpha * ap[i]
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
    rap = np.dot ( r, ap )

    beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
    for i in range ( 0, n ):
      p[i] = r[i] + beta * p[i]

  return x

def r83s_cg_test ( rng ):

#*****************************************************************************80
#
## r83s_cg_test() tests r83s_cg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r83s_cg_test():' )
  print ( '  r83s_cg() applies CG to an R83S matrix.' )

  n = 10
#
#  Let A be the -1 2 -1 matrix.
#
  a = r83s_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83s_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r83s_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r83s_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = ', n )
  print ( '  Norm of residual ||Ax-b|| = ', r_norm )
  print ( '  Norm of error ||x1-x2|| = ', e_norm )

  return

def r83s_dif2 ( m, n ):

#*****************************************************************************80
#
## r83s_dif2() returns the DIF2 matrix in R83S format.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#    A is tridiagonal.
#    Because A is tridiagonal, it has property A (bipartite).
#    A is a special case of the TRIS or tridiagonal scalar matrix.
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#    A is Toeplitz: constant along diagonals.
#    A is symmetric: A' = A.
#    Because A is symmetric, it is normal.
#    Because A is normal, it is diagonalizable.
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#    A is positive definite.
#    A is an M matrix.
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#    A has an LU factorization A = L * U, without pivoting.
#      The matrix L is lower bidiagonal with subdiagonal elements:
#        L(I+1,I) = -I/(I+1)
#      The matrix U is upper bidiagonal, with diagonal elements
#        U(I,I) = (I+1)/I
#      and superdiagonal elements which are all -1.
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#    The eigenvalues are
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#    The corresponding eigenvector X(I) has entries
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#    Simple linear systems:
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#    det ( A ) = N + 1.
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.68
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Birkhauser, 1980,
#    ISBN: 0817608117,
#    LC: QA297.T58.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(3), the matrix.
#
  import numpy as np

  a = np.array ( [ -1.0, 2.0, -1.0 ] )
  
  return a

def r83s_dif2_test ( ):

#*****************************************************************************80
#
## r83s_dif2_test() tests r83s_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83S_DIF2_TEST' )
  print ( '  R83S_DIF2 sets an R83S matrix to the second difference.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83s_dif2 ( m, n )
    r83s_print ( m, n, a, '  Second difference in R83S format:' )

  return

def r83s_gs_sl ( n, a, b, x, it_max ):

#*****************************************************************************80
#
## r83s_gs_sl() solves an R83S system using Gauss-Seidel iteration.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A(I-J+2).
#
#    This routine simply applies a given number of steps of the
#    iteration to an input approximate solution.  On first call, you can
#    simply pass in the zero vector as an approximate solution.  If
#    the returned value is not acceptable, you may call again, using
#    it as the starting point for additional iterations.
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(3), the R83S matrix.
#
#    real B(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X(N), an approximate solution to the system.
#

#
#  No diagonal matrix entry can be zero.
#
  if ( a[1] == 0.0 ):
    print ( '' )
    print ( 'R83S_GS_SL - Fatal error!' )
    print ( '  Zero diagonal entry.' )
    raise Exception ( 'R83S_GS_SL - Fatal error!' )

  for it_num in range ( 0, it_max ):

    x[0] =   ( b[0]                 - a[2] * x[1]   ) / a[1]
    for i in range ( 1, n - 1 ):
      x[i] = ( b[i] - a[0] * x[i-1] - a[2] * x[i+1] ) / a[1]
    x[n-1] =   ( b[n-1] - a[0] * x[n-2]                 ) / a[1]

  return x

def r83s_gs_sl_test ( rng ):

#*****************************************************************************80
#
## r83s_gs_sl_test() tests r83s_gs_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r83s_gs_sl_test():' )
  print ( '  r83s_gs_sl() applies Gauss-Seidel iteration with an R83S matrix' )
  print ( '  to solve a linear system A*x=b.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a = r83s_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83s_mv ( n, n, a, x1 )
#
#  Call the Gauss-Seidel routine.
#
  x2 = np.ones ( n )
  it_max = 100
  x3 = r83s_gs_sl ( n, a, b, x2, it_max )
#
#  Compute the residual.
#
  r = r83s_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = ', n )
  print ( '  Norm of residual ||Ax-b|| = ', r_norm )
  print ( '  Norm of error ||x1-x2|| = ', e_norm )

  return

def r83s_indicator ( m, n ):

#*****************************************************************************80
#
## r83s_indicator() sets an R83S indicator matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A(I-J+2).
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(3), the R83S matrix.
#
  import numpy as np

  a = np.array ( [ 3.0, 2.0, 1.0 ] )

  return a

def r83s_indicator_test ( ):

#*****************************************************************************80
#
## r83s_indicator_test() tests r83s_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83S_INDICATOR_TEST' )
  print ( '  R83S_INDICATOR sets an R83S indicator matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83s_indicator ( m, n )
    r83s_print ( m, n, a, '  R83S indicator matrix:' )

  return

def r83s_jac_sl ( n, a, b, x, it_max ):

#*****************************************************************************80
#
## r83s_jac_sl() solves an R83S system using Jacobi iteration.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A(I-J+2).
#
#    This routine simply applies a given number of steps of the
#    iteration to an input approximate solution.  On first call, you can
#    simply pass in the zero vector as an approximate solution.  If
#    the returned value is not acceptable, you may call again, using
#    it as the starting point for additional iterations.
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(3), the R83S matrix.
#
#    real B(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X(N), an approximate solution 
#    to the system.
#
  import numpy as np
#
#  No diagonal matrix entry can be zero.
#
  if ( a[1] == 0.0 ):
    print ( '' )
    print ( 'R83S_JAC_SL - Fatal error!' )
    print ( '  Zero diagonal entry.' )
    raise Exception ( 'R83S_JAC_SL - Fatal error!' )

  x_new = np.zeros ( n )

  for it_num in range ( 0, it_max ):

    x_new[0] = b[0] - a[2] * x[1]
    for i in range ( 1, n - 1 ):
      x_new[i] = b[i] - a[0] * x[i-1] - a[2] * x[i+1]
    x_new[n-1] = b[n-1] - a[0] * x[n-2]
#
#  Divide by diagonal terms.
#
    for i in range ( 0, n ):
      x[i] = x_new[i] / a[1]

  return x

def r83s_jac_sl_test ( rng ):

#*****************************************************************************80
#
## r83s_jac_sl_test() tests r83s_jac_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r83s_jac_sl_test():' )
  print ( '  r83s_jac_sl() applies Jacobi iteration with an R83S matrix' )
  print ( '  to solve a linear system A*x=b.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a = r83s_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83s_mv ( n, n, a, x1 )
#
#  Call the Jacobi routine.
#
  x2 = np.ones ( n )
  it_max = 100
  x3 = r83s_jac_sl ( n, a, b, x2, it_max )
#
#  Compute the residual.
#
  r = r83s_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = ', n )
  print ( '  Norm of residual ||Ax-b|| = ', r_norm )
  print ( '  Norm of error ||x1-x2|| = ', e_norm )

  return

def r83s_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r83s_mtv() computes b=A'*x, where A is an R83S matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A(I-J+2).
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3), the R83S matrix.
#
#    real X(M), the vector to be multiplied by A'.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      b[j] = b[j] + a[i-j+1] * x[i]

  return b

def r83s_mtv_test ( rng ):

#*****************************************************************************80
#
## r83s_mtv_test() tests r83s_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83s_mtv_test():' )
  print ( '  r83s_mtv() computes b=A\'*x, where A is an R83S matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a_83s = r83s_random ( m, n, rng )
    x = r8vec_indicator1 ( m )
    ax_83s = r83s_mtv ( m, n, a_83s, x )
    a_ge = r83s_to_r8ge ( m, n, a_83s )
    ax_ge = r8ge_mtv ( m, n, a_ge, x )
    r8vec2_print ( ax_83s, ax_ge, '  Product comparison:' )

  return

def r83s_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r83s_mv() multiplies an R83S matrix times an R8VEC.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(3), the R83S matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      b[i] = b[i] + a[i-j+1] * x[j]

  return b

def r83s_mv_test ( rng ):

#*****************************************************************************80
#
## r83s_mv_test() tests r83s_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83s_mv_test():' )
  print ( '  r83s_mv() computes b=A*x, where A is an R83S matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a_83s = r83s_random ( m, n, rng )
    x = r8vec_indicator1 ( n )
    ax_83s = r83s_mv ( m, n, a_83s, x )
    a_ge = r83s_to_r8ge ( m, n, a_83s )
    ax_ge = r8ge_mv ( m, n, a_ge, x )
    r8vec2_print ( ax_83s, ax_ge, '  Product comparison:' )

  return

def r83s_print ( m, n, a, title ):

#*****************************************************************************80
#
## r83s_print() prints an R83S matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3), the R83S matrix.
#
#    string TITLE, a title.
#
  r83s_print_some ( m, n, a, 1, 1, m, n, title )

  return

def r83s_print_test ( ):

#*****************************************************************************80
#
## r83s_print_test() tests r83s_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83S_PRINT_TEST' )
  print ( '  R83S_PRINT prints an R83S matrix.' )

  m = 5
  n = 5
  a = r83s_indicator ( m, n )
  r83s_print ( m, n, a, '  R83S matrix:' )

  return

def r83s_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r83s_print_some() prints some of a R83 matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3), the R83S matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column, to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )
    print ( '  Col: ', end = '' )
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )
    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2lo = max ( i2lo, j2lo - 1 )
    i2hi = min ( ihi, m - 1 )
    i2hi = min ( i2hi, j2hi + 1 )

    for i in range ( i2lo, i2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      print ( '%5d:' % ( i ), end = '' )

      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( i - j + 2 < 1 or 3 < i - j + 2 ):
          print ( '              ', end = '' )
        else:
          print ( '%14g' % ( a[i-j+1] ), end = '' )

      print ( '' )

  return

def r83s_print_some_test ( ):

#*****************************************************************************80
#
## r83s_print_some_test() tests r83s_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83S_PRINT_SOME_TEST' )
  print ( '  R83S_PRINT_SOME prints some of an R83S matrix.' )

  m = 5
  n = 5
  a = r83s_indicator ( m, n )
  r83s_print_some ( m, n, a, 2, 2, 5, 4, '  Rows 2-5, Cols 2-4:' )

  return

def r83s_random ( m, n, rng ):

#*****************************************************************************80
#
## r83s_random() randomizes an R83S matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(3), the R83 matrix.
#
  a = rng.random ( size = 3 )

  return a

def r83s_random_test ( rng ):

#*****************************************************************************80
#
## r83s_random_test() tests r83s_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 Septemer 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83s_random_test():' )
  print ( '  r83s_random() randomizes an R83S matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83s_random ( m, n, rng )
    r83s_print ( m, n, a, '  Random R83S matrix:' )

  return

def r83s_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## r83s_res() computes the residual R = B-A*X for R83S matrices.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real B(M), the desired result A * x.
#
#  Output:
#
#    real R(M), the residual R = B - A * X.
#
  r = r83s_mv ( m, n, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r83s_res_test ( rng ):

#*****************************************************************************80
#
## r83s_res_test() tests r83s_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83s_res_test():' )
  print ( '  r83s_res() computes b-A*x, where A is an R83S matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in  range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83s_random ( m, n, rng )
    x = r8vec_indicator1 ( n )
    b = r83s_mv ( m, n, a, x )
    r = r83s_res ( m, n, a, x, b )
    r8vec_print ( m, r, '  Residual A*x-b:' )

  return

def r83s_to_r8ge ( m, n, a_83s ):

#*****************************************************************************80
#
## r83s_to_r8ge() copies an R83S matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_83S(3), the R83S matrix.
#
#  Output:
#
#    real A_GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      a_ge[i,j] = a_83s[i-j+1]

  return a_ge

def r83s_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r83s_to_r8ge_test() tests r83s_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83s_to_r8ge_test():' )
  print ( '  r83s_to_r8ge() converts an R83S matrix to R8GE format.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a_83s = r83s_random ( m, n, rng )
    r83s_print ( m, n, a_83s, '  R83s matrix:' )

    a_ge = r83s_to_r8ge ( m, n, a_83s )

    print ( '' )
    print ( '  The R8GE matrix:' )
    print ( a_ge )

  return

def r83s_zeros ( m, n ):

#*****************************************************************************80
#
## r83s_zeros() zeros an R83S matrix.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#    RGE A(I,J) = R83S A[I-J+1].
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A1   0   0   0
#      A3  A2  A1   0   0
#       0  A3  A2  A1   0 
#       0   0  A3  A2  A1
#       0   0   0  A3  A2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(3,1), the R83 matrix.
#
  import numpy as np

  a = np.zeros ( 3 )
 
  return a

def r83s_zeros_test ( ):

#*****************************************************************************80
#
## r83s_zeros_test() tests r83s_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r83s_zeros_test():' )
  print ( '  r83s_zeros() zeros an R83S matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83s_zeros ( m, n )
    r83s_print ( m, n, a, '  Zeroed R83S matrix:' )

  return

def r8ge_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ge_mtv() multiplies a vector by a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8GE matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j] = b[j] + x[i] * a[i,j]

  return b

def r8ge_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ge_mv() multiplies an R8GE matrix times a vector.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8GE matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return


def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  r83s_test ( )
  timestamp ( )

