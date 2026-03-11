#! /usr/bin/env python3
#
def r83t_test ( ):

#*****************************************************************************80
#
## r83t_test() tests r83t().
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
  print ( 'r83t_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r83t().' )

  rng = default_rng ( )

  r83t_cg_test ( rng )
  r83t_dif2_test ( )
  r83t_gs_sl_test ( )
  r83t_indicator_test ( )
  r83t_jac_sl_test ( )
  r83t_mtv_test ( )
  r83t_mv_test ( )
  r83t_print_test ( )
  r83t_print_some_test ( )
  r83t_random_test ( rng )
  r83t_res_test ( )
  r83t_to_r8ge_test ( )
  r83t_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83t_test():' )
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

def r83t_cg ( n, a, b, x ):

#*****************************************************************************80
#
## r83t_cg() uses the conjugate gradient method on an R83T system.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
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
#    Here is how an R83T matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
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
#    real A(N,3), the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X(N): an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N): the approximate solution vector.
#
  import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r83t_mv ( n, n, a, x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r83t_mv ( n, n, a, p )
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
    x = x + alpha * p
    r = r - alpha * ap
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
    p = r + beta * p

  return x

def r83t_cg_test ( rng ):

#*****************************************************************************80
#
## r83t_cg_test() tests r83t_cg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
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
  print ( 'r83t_cg_test()' )
  print ( '  r83t_cg() applies CG to an R83T matrix.' )

  n = 10
#
#  Let A be the -1 2 -1 matrix.
#
  a = r83t_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83t_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x2 = r83t_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r83t_res ( n, n, a, x2, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x2 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = ', n )
  print ( '  Norm of residual ||Ax-b|| = ', r_norm )
  print ( '  Norm of error ||x1-x2|| = ', e_norm )

  return

def r83t_dif2 ( m, n ):

#*****************************************************************************80
#
## r83t_dif2() returns the DIF2 matrix in R83T format.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is a special case of the TRIS or tridiagonal scalar matrix.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
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
#    28 May 2016
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
#    real A(M,3), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, 3 ] )

  mn = min ( m, n )

  a[1:mn,0]   = -1.0
  a[0:mn,1]   = +2.0
  a[0:mn-1,2] = -1.0

  if ( m < n ):
    a[mn-1,2] = -1.0
  elif ( n < m ):
    a[mn,0] = -1.0
  
  return a

def r83t_dif2_test ( ):

#*****************************************************************************80
#
## r83t_dif2_test() tests r83t_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83T_DIF2_TEST' )
  print ( '  R83T_DIF2 sets an R83T matrix to the second difference.' )

  m = 5
  n = 5

  a = r83t_dif2 ( m, n )
  r83t_print ( m, n, a, '  R83T matrix:' )

  return

def r83t_gs_sl ( n, a, b, x, it_max ):

#*****************************************************************************80
#
## r83t_gs_sl() solves an R83T system using Gauss-Seidel iteration.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
#
#    real A(N,3), the R83T matrix.
#
#    real B(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution to 
#    the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X(N): the updated approximate solution.
#
  import numpy as np

  for i in range ( 0, n ):
    if ( a[i,1] == 0.0 ):
      print ( '' )
      print ( 'R83T_GS_SL - Fatal error!' )
      print ( '  Zero diagonal entry, index = ', i )
      raise Exception ( 'R83T_GS_SL - Fatal error!' )

  x_old = np.zeros ( n )

  for it_num in range ( 0, it_max ):

    x_old = x.copy ( )

    x[0]= ( b[0] - a[0,2] * x[1] ) / a[0,1]

    for i in range ( 1, n - 1 ):
      x[i] = ( b[i] - a[i,0] * x[i-1] - a[i,2] * x[i+1] ) / a[i,1]
    x[n-1] = ( b[n-1] - a[n-1,0] * x[n-2] ) / a[n-1,1]

  return x

def r83t_gs_sl_test ( ):

#*****************************************************************************80
#
## r83t_gs_sl_test() tests r83t_gs_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  it_max = 25

  print ( '' )
  print ( 'r83t_gs_sl_test' )
  print ( '  r83t_gs_sl solves a linear system using' )
  print ( '  Gauss-Seidel iteration, with R83T matrix storage.' )
  print ( '' )
  print ( '  Matrix order N =      ', n )
  print ( '  Iterations per call = ', it_max )
#
#  Set the matrix values.
#
  a = r83t_dif2 ( n, n )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r83t_mv ( n, n, a, x )
#
#  Set the starting solution.
#
  x = np.zeros ( n )
#
#  Solve the linear system.
#
  for i in range ( 0, 3 ):

    x = r83t_gs_sl ( n, a, b, x, it_max )

    r8vec_print ( n, x, '  Current solution estimate:' )

  return

def r83t_indicator ( m, n ):

#*****************************************************************************80
#
## r83t_indicator() sets the indicator matrix in R83T format.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
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
#  Output:
#
#    real A(M,3), the matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ m, 3 ] )

  for i in range ( 0, m ):
    for k in range ( 0, 3 ):
      j = i + k - 1
      if ( 0 <= j and j <= n - 1 ):
        a[i,k] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r83t_indicator_test ( ):

#*****************************************************************************80
#
## r83t_indicator_test() tests r83t_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83T_INDICATOR_TEST' )
  print ( '  R83T_INDICATOR sets an R83T indicator matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 0, 3 ):

    if ( i == 0 ):
      m = 3
      n = 5
    elif ( i == 1 ):
      m = 5
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 3

    a = r83t_indicator ( m, n )
    r83t_print ( m, n, a, '  R83T indicator matrix:' )

  return

def r83t_jac_sl ( n, a, b, x, it_max ):

#*****************************************************************************80
#
## r83t_jac_sl() solves an R83T system using Jacobi iteration.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
#
#    real A(N,3), the R83T matrix.
#
#    real B(N), the right hand side of the linear system.
#
#    real X(N): an approximate solution 
#    to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X(N): the updated approximate solution.
#
  import numpy as np
#
#  No diagonal matrix entry can be zero.
#
  for i in range ( 0, n ):
    if ( a[i,1] == 0.0 ):
      print ( '' )
      print ( 'R83T_JAC_SL - Fatal error!' )
      print ( '  Zero diagonal entry, index = ', i )
      raise Exception ( 'R83T_JAC_SL - Fatal error!' )

  x_new = np.zeros ( n )

  for it_num in range ( 0, it_max ):

    x_new[0] = b[0] - a[0,2] * x[1]
    for i in range ( 1, n - 1 ):
      x_new[i] = b[i] - a[i,0] * x[i-1] - a[i,2] * x[i+1]
    x_new[n-1] = b[n-1] - a[n-1,0] * x[n-2]
#
#  Divide by diagonal terms.
#
    for i in range ( 0, n ):
      x_new[i] = x_new[i] / a[i,1]
#
#  Update.
#
    x = x_new.copy ( )

  return x

def r83t_jac_sl_test ( ):

#*****************************************************************************80
#
## r83t_jac_sl_test() tests r83t_jac_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  it_max = 25

  print ( '' )
  print ( 'r83t_jac_sl_test' )
  print ( '  r83t_jac_sl solves a linear system using' )
  print ( '  Jacobi iteration, with R83T matrix storage.' )
  print ( '' )
  print ( '  Matrix order N =      ', n )
  print ( '  Iterations per call = ', it_max )
#
#  Set the matrix values.
#
  a = r83t_dif2 ( n, n )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r83t_mv ( n, n, a, x )
#
#  Set the starting solution.
#
  x = np.zeros ( n )
#
#  Solve the linear system.
#
  for i in range ( 0, 3 ):

    x = r83t_jac_sl ( n, a, b, x, it_max )

    r8vec_print ( n, x, '  Current solution estimate:' )

  return

def r83t_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r83t_mtv() multiplies an R83T matrix transposed times an R8VEC.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,3), the matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, m ):
    for k in range ( 0, 3 ):
      j = i + k - 1
      if ( 0 <= j and j <= n - 1 ):
        b[j] = b[j] + x[i] * a[i,k]

  return b

def r83t_mtv_test ( ):

#*****************************************************************************80
#
## r83t_mtv_test() tests r83t_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 6

  print ( '' )
  print ( 'R83T_MTV_TEST' )
  print ( '  R83T_MTV multiplies an R83T matrix transposed times a vector.' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )
#
#  Set the matrix.
#
  a = r83t_indicator ( m, n )

  r83t_print ( m, n, a, '  The R83T matrix A:' )

  x = r8vec_indicator1 ( m )

  r8vec_print ( m, x, '  The vector x:' )

  b = r83t_mtv ( m, n, a, x )

  r8vec_print ( n, b, '  The product b = A''*x:' )

  return

def r83t_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r83t_mv() multiplies an R83T matrix times an R8VEC.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,3), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  mn = min ( m, n )

  if ( n == 1 ):
    b[0] = a[0,1] * x[0]
    if ( 1 < m ):
      b[1] = a[1,0] * x[0]
    return b

  b[0] = a[0,1] * x[0] + a[0,2] * x[1]

  for i in range ( 1, mn - 1 ):
    b[i] = a[i,0] * x[i-1] + a[i,1] * x[i] + a[i,2] * x[i+1]

  b[mn-1] = a[mn-1,0] * x[mn-2] + a[mn-1,1] * x[mn-1]

  if ( n < m ):
    b[mn] = b[mn] + a[mn,0] * x[mn-1]
  elif ( m < n ):
    b[mn-1] = b[mn-1] + a[mn-1,2] * x[mn]

  return b

def r83t_mv_test ( ):

#*****************************************************************************80
#
## r83t_mv_test() tests r83t_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 6

  print ( '' )
  print ( 'R83T_MV_TEST' )
  print ( '  R83T_MV multiplies an R83T matrix times a vector.' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )
#
#  Set the matrix.
#
  a = r83t_indicator ( m, n )

  r83t_print ( m, n, a, '  The R83T matrix A:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r83t_mv ( m, n, a, x )

  r8vec_print ( m, b, '  The product b = A*x:' )

  return

def r83t_print ( m, n, a, title ):

#*****************************************************************************80
#
## r83t_print() prints a R83T matrix.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#    N must be positive.
#
#    real A(M,3), the R83 matrix.
#
#    string TITLE, a title.
#
  r83t_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r83t_print_test ( ):

#*****************************************************************************80
#
## r83t_print_test() tests r83t_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83T_PRINT_TEST' )
  print ( '  R83T_PRINT prints an R83T matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 0, 3 ):

    if ( i == 0 ):
      m = 3
      n = 5
    elif ( i == 1 ):
      m = 5
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 3

    a = r83t_indicator ( m, n )
    r83t_print ( m, n, a, '  R83T matrix:' )

  return

def r83t_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r83t_print_some() prints some of an R83T matrix.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the R83 matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column, to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5
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

        if ( i - j + 1 < 0 or 2 < i - j + 1 ):
          print ( '              ', end = '' )
        else:
          print ( '%14g' % ( a[i,j-i+1] ), end = '' )

      print ( '' )

  return

def r83t_print_some_test ( ):

#*****************************************************************************80
#
## r83t_print_some_test() tests r83t_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 9
  n = 9

  print ( '' )
  print ( 'R83T_PRINT_SOME_TEST' )
  print ( '  R83T_PRINT_SOME prints some of an R83T matrix.' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )
#
#  Set the matrix.
#
  a = r83t_indicator ( m, n )

  r83t_print_some ( m, n, a, 3, 5, 6, 8, '  Rows 3:6, Cols 5:8:' )

  return

def r83t_random ( m, n, rng ):

#*****************************************************************************80
#
## r83t_random() returns a random R83T matrix.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
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
#    rng: the current random number generator.
#
#  Output:
#
#    real A(M,3), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, 3 ] )

  for i in range ( 0, m ):
    for k in range ( 0, 3 ):
      j = i + k - 1
      if ( 0 <= j and j <= n - 1 ):
        a[i,k] = rng.random ( )

  return a

def r83t_random_test ( rng ):

#*****************************************************************************80
#
## r83t_random_test() tests r83t_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
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
  print ( 'r83t_random_test():' )
  print ( '  r83t_random() returns a random R83T matrix.' )

  m = 5
  n = 5

  a = r83t_random ( m, n, rng )
  r83t_print ( m, n, a, '  R83T matrix:' )

  return

def r83t_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## r83t_res() computes the residual R = B-A*X for R83T matrices.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
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
#    real A(M,3), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real B(M), the desired result A * x.
#
#  Output:
#
#    real R(M), the residual R = B - A * X.
#
  r = r83t_mv ( m, n, a, x )

  r = b - r

  return r

def r83t_res_test ( ):

#*****************************************************************************80
#
## r83t_res_test() tests r83t_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5

  print ( '' )
  print ( 'R83T_RES_TEST' )
  print ( '  R83T_RES evaluates the residual given an approximate' )
  print ( '  solution of a linear system A*x=b.' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )
#
#  Set the matrix.
#
  a = r83t_dif2 ( m, n )

  r83t_print ( m, n, a, '  The R83T matrix A:' )

  x = r8vec_indicator1 ( n )

  b = r83t_mv ( m, n, a, x )

  r8vec_print ( m, b, '  The right hand side B:' )

  x = np.zeros ( n )
  x = r83t_cg ( n, a, b, x )

  r8vec_print ( n, x, '  The solution X:' )

  r = r83t_res ( m, n, a, x, b )

  r8vec_print ( m, r, '  The residual b-A*x:' )

  return

def r83t_to_r8ge ( m, n, a_r83t ):

#*****************************************************************************80
#
## r83t_to_r8ge() copies an R83T matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_R83T(M,3), the R83T matrix.
#
#  Output:
#
#    real A_R8GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_r8ge = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for k in range ( 0, 3 ):
      j = i + k - 1
      if ( 0 <= j and j <= n - 1 ):
        a_r8ge[i,j] = a_r83t[i,k]

  return a_r8ge

def r83t_to_r8ge_test ( ):

#*****************************************************************************80
#
## r83t_to_r8ge_test() tests r83t_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5

  print ( '' )
  print ( 'R83T_TO_R8GE_TEST' )
  print ( '  R83T_TO_R8GE converts an R83T matrix to R8GE format.' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )
#
#  Set the matrix.
#
  a_r83t = r83t_indicator ( m, n )

  r83t_print ( m, n, a_r83t, '  The R83T indicator matrix:' )

  a_r8ge = r83t_to_r8ge ( m, n, a_r83t )

  print ( '' )
  print ( '  The R8GE format matrix:' )
  print ( a_r8ge )

  return

def r83t_zeros ( m, n ):

#*****************************************************************************80
#
## r83t_zeros() zeros an R83T matrix.
#
#  Discussion:
#
#    The R83T storage format is used for an MxN tridiagonal matrix.
#    The superdiagonal is stored in entries (1:M-1,3), the diagonal in
#    entries (1:M,2), and the subdiagonal in (2:M,1).  Thus, the
#    the rows of the original matrix slide horizontally to form an
#    Mx3 stack of data.
#
#    An R83T matrix of order 3x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#
#    An R83T matrix of order 5x5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#    An R83T matrix of order 5x3 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33  *
#      A43  *   *
#       *   *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2016
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
#  Output:
#
#    real A(M,3), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, 3 ] )

  return a

def r83t_zeros_test ( ):

#*****************************************************************************80
#
## r83t_zeros_test() tests r83t_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83T_ZEROS_TEST' )
  print ( '  R83T_ZEROS sets an R83T matrix to zero.' )

  m = 5
  n = 5

  a = r83t_zeros ( m, n )
  r83t_print ( m, n, a, '  R83T matrix:' )

  return

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
  r83t_test ( )
  timestamp ( )
