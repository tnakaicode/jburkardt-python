#! /usr/bin/env python3
#
def r8pbu_test ( ):

#*****************************************************************************80
#
## r8pbu_test() tests r8pbu().
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
  print ( 'r8pbu_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8pbu().' )

  rng = default_rng ( )

  r8pbu_cg_test ( rng )
  r8pbu_det_test ( rng )
  r8pbu_dif2_test ( )
  r8pbu_fa_test ( rng )
  r8pbu_indicator_test ( )
  r8pbu_ml_test ( rng )
  r8pbu_mv_test ( rng )
  r8pbu_print_test ( )
  r8pbu_print_some_test ( )
  r8pbu_random_test ( rng )
  r8pbu_res_test ( rng )
  r8pbu_sl_test ( rng )
  r8pbu_sor_test ( )
  r8pbu_to_r8ge_test ( )
  r8pbu_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8pbu_test():' )
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

def r8pbu_cg ( n, mu, a, b, x ):

#*****************************************************************************80
#
## R8PBU_CG uses the conjugate gradient method on an R8PBU system.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#    The matrix A must be a positive definite symmetric band matrix.
#
#    The method is designed to reach the solution after N computational
#    steps.  However, roundoff may introduce unacceptably large errors for
#    some problems.  In such a case, calling the routine again, using
#    the computed solution as the new starting estimate, should improve
#    the results.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2016
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
#    integer MU, the number of superdiagonals.
#    MU must be at least 0, and no more than N-1.
#
#    real A(MU+1,N), the R8PBU matrix.
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
  ap = r8pbu_mv ( n, mu, a, x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r8pbu_mv ( n, mu, a, p )
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

def r8pbu_cg_test ( rng ):

#*****************************************************************************80
#
## r8pbu_cg_test() tests r8pbu_cg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
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
  print ( 'r8pbu_cg_test():' )
  print ( '  r8pbu_cg() applies CG to an R8PBU matrix.' )

  n = 10
  mu = 1
#
#  Let A be the -1 2 -1 matrix.
#
  a = r8pbu_dif2 ( n, n, mu )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r8pbu_mv ( n, mu, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x2 = r8pbu_cg ( n, mu, a, b, x2 )
#
#  Compute the residual.
#
  r = r8pbu_res ( n, n, mu, a, x2, b )
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

def r8pbu_det ( n, mu, a_lu ):

#*****************************************************************************80
#
## r8pbu_det() computes the determinant of a matrix factored by R8PBU_FA.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, Philadelphia, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals of the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    real A_LU(MU+1,N), the LU factors from R8PBU_FA.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for j in range ( 0, n ):
    det = det * a_lu[mu,j]
  det = det * det

  return det

def r8pbu_det_test ( rng ):

#*****************************************************************************80
#
## r8pbu_det_test() tests r8pbu_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
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

  n = 10
  mu = 3

  print ( '' )
  print ( 'r8pbu_det_test():' )
  print ( '  r8pbu_det() computes the determinant of a positive definite' )
  print ( '  symmetric banded matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8pbu_random ( n, mu, rng )

  r8pbu_print ( n, mu, a, '  The R8PBU matrix:' )
#
#  Copy the matrix into a general array.
#
  a2 = r8pbu_to_r8ge ( n, mu, a )
#
#  Factor the matrix.
#
  a_lu, info = r8pbu_fa ( n, mu, a )

  r8pbu_print ( n, mu, a_lu, '  The R8PBU factored matrix:' )
#
#  Compute the determinant.
#
  a_det = r8pbu_det ( n, mu, a_lu )

  print ( '' )
  print ( '  R8PBU_DET computes the determinant = ', a_det )
#
#  Factor the general matrix.
#
  a2_det = np.linalg.det ( a2 )

  print ( '  np.linalg.det() computes the determinant =  ', a2_det )

  return

def r8pbu_dif2 ( m, n, mu ):

#*****************************************************************************80
#
## R8PBU_DIF2 returns the DIF2 matrix in R8PBU format.
#
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
#    03 June 2016
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
#    integer M, N, the number of rows and columns.
#
#    integer MU, the number of superdiagonals.
#    MU must be at least 0, and no more than N-1.
#
#  Output:
#
#    real A(MU+1,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ mu + 1, n ] )

  for j in range ( 1, n ):
    a[mu-1,j] = -1.0

  for j in range ( 0, n ):
    a[mu,j] =  +2.0
 
  return a

def r8pbu_dif2_test ( ):

#*****************************************************************************80
#
## R8PBU_DIF2_TEST tests R8PBU_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  mu = 1

  print ( '' )
  print ( 'R8PBU_DIF2_TEST' )
  print ( '  R8PBU_DIF2 sets up a R8PBU second difference matrix.' )
  print ( '' )
  print ( '  Matrix order M = ', m )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_dif2 ( m, n, mu )

  r8pbu_print ( n, mu, a, '  The R8PBU second difference matrix:' )

  return

def r8pbu_fa ( n, mu, a ):

#*****************************************************************************80
#
## R8PBU_FA factors a R8PBU matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#    The matrix A must be a positive definite symmetric band matrix.
#
#    Once factored, linear systems A*x=b involving the matrix can be solved
#    by calling R8PBU_SL.  No pivoting is performed.  Pivoting is not necessary
#    for positive definite symmetric matrices.  If the matrix is not positive
#    definite, the algorithm may behave correctly, but it is also possible
#    that an illegal divide by zero will occur.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, Philadelphia, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals of the matrix.
#    MU must be at least 0, and no more than N-1.
#
#    real A(MU+1,N), the N by N matrix, stored in LINPACK
#    positive definite symmetric band matrix storage.
#
#  Output:
#
#    real A_LU(MU+1,N), information describing a factored form
#    of the matrix, that can be used to solve linear systems
#    A*x=b, using R8PBU_SL.
#
#    integer INFO, singularity flag.
#    0, the matrix is nonsingular.
#    nonzero, the matrix is singular.
#
  import numpy as np

  info = 0
  a_lu = a.copy ( )

  for j in range ( 1, n + 1 ):

    ik = mu + 1
    jk = max ( j - mu, 1 )
    mm = max ( mu + 2 - j, 1 )

    s = 0.0

    for k in range ( mm, mu + 1 ):

      t = 0.0
      for i in range ( ik, ik + k - mm ):
        t = t + a_lu[i-1,jk-1] * a_lu[mm+i-ik-1,j-1]

      a_lu[k-1,j-1] = ( a_lu[k-1,j-1] - t ) / a_lu[mu,jk-1]

      s = s + a_lu[k-1,j-1] * a_lu[k-1,j-1]

      ik = ik - 1
      jk = jk + 1

    s = a_lu[mu,j-1] - s

    if ( s <= 0.0 ):
      info = j
      print ( '' )
      print ( 'R8PBU_FA - Fatal error!' )
      print ( '  Nonpositive pivot on step ', info )
      return a_lu, info

    a_lu[mu,j-1] = np.sqrt ( s )

  return a_lu, info

def r8pbu_fa_test ( rng ):

#*****************************************************************************80
#
## r8pbu_fa_test() tests r8pbu_fa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 50
  mu = 1
 
  print ( '' )
  print ( 'r8pbu_fa_test():' )
  print ( '  r8pbu_fa() factors an R8PBU matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix values.
#
  a = r8pbu_random ( n, mu, rng )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the right hand side.
#
  b = r8pbu_mv ( n, mu, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8pbu_fa ( n, mu, a )
#
#  Solve the linear system.
#
  x = r8pbu_sl ( n, mu, a_lu, b )
 
  r8vec_print_some ( n, x, 10, '  Solution:' )

  return

def r8pbu_indicator ( n, mu ):

#*****************************************************************************80
#
## R8PBU_INDICATOR sets up a R8PBU indicator matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#  Output:
#
#    real A(MU+1,N), the R8PBU matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ mu + 1, n ] )
#
#  Set the meaningful values.
#
  for i in range ( 0, n ):
    jhi = min ( i + mu + 1, n )
    for j in range ( i, jhi ):
      a[mu+i-j,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8pbu_indicator_test ( ):

#*****************************************************************************80
#
## R8PBU_INDICATOR_TEST tests R8PBU_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9
  mu = 3

  print ( '' )
  print ( 'R8PBU_INDICATOR_TEST' )
  print ( '  R8PBU_INDICATOR sets up a R8PBU indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_indicator ( n, mu )

  r8pbu_print ( n, mu, a, '  The R8PBU indicator matrix:' )

  return

def r8pbu_ml ( n, mu, a_lu, x ):

#*****************************************************************************80
#
## R8PBU_ML multiplies a vector times a matrix that was factored by R8PBU_FA.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals of the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    real A_LU(MU+1,N), the matrix, as factored by R8PBU_FA.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = x.copy ( )
#
#  Multiply U * X = Y.
#
  for k in range ( 1, n + 1 ):

    ilo = max ( 1, k - mu )
    for i in range ( ilo, k ):
      b[i-1] = b[i-1] + a_lu[mu+i-k,k-1] * b[k-1]

    b[k-1] = a_lu[mu,k-1] * b[k-1]
#
#  Multiply L * Y = B.
#
  for k in range ( n, 0, -1 ):

    jhi = min ( k + mu + 1, n + 1 )
    for j in range ( k + 1, jhi ):
      b[j-1] = b[j-1] + a_lu[mu+k-j,j-1] * b[k-1]

    b[k-1] = a_lu[mu,k-1] * b[k-1]

  return b

def r8pbu_ml_test ( rng ):

#*****************************************************************************80
#
## r8pbu_ml_test() tests r8pbu_ml().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10
  mu = 3

  print ( '' )
  print ( 'r8pbu_ml_test():' )
  print ( '  r8pbu_ml() computes A*x' )
  print ( '  where A has been factored by R8PBU_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8pbu_random ( n, mu, rng )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8pbu_mv ( n, mu, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8pbu_fa ( n, mu, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8PBU_ML_TEST - Fatal error!' )
    print ( '  R8PBU_FA declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    return
#
#  Now multiply factored matrix times solution to get right hand side again.
#
  b2 = r8pbu_ml ( n, mu, a_lu, x )

  r8vec2_print_some ( n, b, b2, 10, '  A*x and PLU*x' )

  return

def r8pbu_mv ( n, mu, a, x ):

#*****************************************************************************80
#
## R8PBU_MV multiplies an R8PBU matrix by an R8VEC.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    real A(MU+1,N), the R8PBU matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the result vector A * x.
#
  import numpy as np

  b = np.zeros ( n )
#
#  Multiply X by the diagonal of the matrix.
#
  for i in range ( 0, n ):
    b[i] = a[mu,i] * x[i]
#
#  Multiply X by the superdiagonals of the matrix.
#
  for i in range ( mu, 0, -1 ):
    for j in range ( mu + 2 - i, n + 1 ):
      ieqn = i + j - mu - 1
      b[ieqn-1] = b[ieqn-1] + a[i-1,j-1] * x[j-1]
      b[j-1] = b[j-1] + a[i-1,j-1] * x[ieqn-1]

  return b

def r8pbu_mv_test ( rng ):

#*****************************************************************************80
#
## r8pbu_mv_test() tests r8pbu_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 5
  mu = 2

  print ( '' )
  print ( 'r8pbu_mv_test():' )
  print ( '  r8pbu_mv() computes A*x' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8pbu_random ( n, mu, rng )
  r8pbu_print ( n, mu, a, '  Matrix A:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Vector x:' )
#
#  Compute the corresponding right hand side.
#
  b = r8pbu_mv ( n, mu, a, x )
  r8vec_print ( n, b, '  Product b=A*x' )

  return

def r8pbu_print ( n, mu, a, title ):

#*****************************************************************************80
#
## R8PBU_PRINT prints a R8PBU matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the upper (and lower) bandwidth.
#    MU must be nonnegative, and no greater than N-1.
#
#    real A(MU+1,N), the R8PBU matrix.
#
#    string TITLE, a title to be printed.
#
  r8pbu_print_some ( n, mu, a, 0, 0, n - 1, n - 1, title )

  return

def r8pbu_print_test ( ):

#*****************************************************************************80
#
## R8PBU_PRINT_TEST tests R8PBU_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  mu = 3

  print ( '' )
  print ( 'R8PBU_PRINT_TEST' )
  print ( '  R8PBU_PRINT prints an R8PBU matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_indicator ( n, mu )

  r8pbu_print ( n, mu, a, '  The R8PBU matrix:' )

  return

def r8pbu_print_some ( n, mu, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8PBU_PRINT_SOME prints some of a R8PBU matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the upper (and lower) bandwidth.
#    MU must be nonnegative, and no greater than N-1.
#
#    real A(MU+1,N), the R8PBU matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title to print.
#
  print ( '' )
  print ( title )

  incx = 5
#
#  Temporarily bump up by 1.
#
  ilo = ilo + 1
  jlo = jlo + 1
  ihi = ihi + 1
  jhi = jhi + 1
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
      print ( '%7d       ' % ( j - 1 ), end = '' )

    print ( '' )
    print ( '  Row' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 1 )
    i2lo = max ( i2lo, j2lo - mu )
    i2hi = min ( ihi, n )
    i2hi = min ( i2hi, j2hi + mu )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i - 1 ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( i <= j and j <= i + mu ):
          aij = a[mu+i-j,j-1]
        elif ( i - mu <= j and j <= i ):
          aij = a[mu+j-i,i-1]
        else:
          aij = 0.0

        if ( mu < i - j or mu < j - i ):
          print ( '              ', end = '' )
        else:
          print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8pbu_print_some_test ( ):

#*****************************************************************************80
#
## R8PBU_PRINT_SOME_TEST tests R8PBU_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9
  mu = 4

  print ( '' )
  print ( 'R8PBU_PRINT_SOME_TEST' )
  print ( '  R8PBU_PRINT_SOME prints some of an R8PBU matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_indicator ( n, mu )

  r8pbu_print_some ( n, mu, a, 3, 4, 7, 8, '  Row(3:7), Col(4:8):' )

  return

def r8pbu_random ( n, mu, rng ):

#*****************************************************************************80
#
## r8pbu_random() randomizes a R8PBU matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#    The matrix returned will be positive definite, but of limited
#    randomness.  The off diagonal elements are random values between
#    0 and 1, and the diagonal element of each row is selected to
#    ensure strict diagonal dominance.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(MU+1,N), the dPBU matrix.
#
  import numpy as np

  a = np.zeros ( [ mu + 1, n ] )
#
#  Set the off diagonal values.
#
  for i in range ( 0, n ):
    jhi = min ( i + mu + 1, n ) 
    for j in range ( i + 1, jhi ):
      a[mu+i-j,j] = rng.random ( )
#
#  Set the diagonal values.
#
  for i in range ( 0, n ):

    sum2 = 0.0
    jlo = max ( 0, i - mu )
    for j in range ( jlo, i ):
      sum2 = sum2 + abs ( a[mu+j-i,i] )

    jhi = min ( i + mu + 1, n )
    for j in range ( i + 1, jhi ):
      sum2 = sum2 + abs ( a[mu+i-j,j] )

    r = rng.random ( )

    a[mu,i] = ( 1.0 + r ) * ( sum2 + 0.01 )

  return a

def r8pbu_random_test ( rng ):

#*****************************************************************************80
#
## r8pbu_random_test() tests r8pbu_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 9
  mu = 3

  print ( '' )
  print ( 'r8pbu_random_test():' )
  print ( '  r8pbu_random() sets up a random R8PBU matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_random ( n, mu, rng )

  r8pbu_print ( n, mu, a, '  The R8PBU matrix:' )

  return

def r8pbu_res ( m, n, mu, a, x, b ):

#*****************************************************************************80
#
## r8pbu_res() computes the residual R = B-A*X for R8PBU matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2016
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
#    integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    real A(MU+1,N), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real B(M), the desired result A * x.
#
#  Output:
#
#    real R(M), the residual R = B - A * X.
#
  r = r8pbu_mv ( n, mu, a, x )

  r = b - r

  return r

def r8pbu_res_test ( rng ):

#*****************************************************************************80
#
## r8pbu_res_test() tests r8pbu_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = m
  mu = 2

  print ( '' )
  print ( 'r8pbu_res_test():' )
  print ( '  r8pbu_res() returns the residual b-A*x where A is' )
  print ( '  a positive definite symmetric band matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix values.
#
  a = r8pbu_random ( n, mu, rng )
  r8pbu_print ( n, mu, a, '  Matrix A:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Exact solution x:' )
#
#  Compute the right hand side.
#
  b = r8pbu_mv ( n, mu, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Jostle the solution.
#
  e = rng.random ( size = n )
  x2 = x + 0.01 * e
  r8vec_print ( n, x2, '  Approximate solution x2:' )
#
#  Compute the residual.
#
  r = r8pbu_res ( m, n, mu, a, x2, b )
 
  r8vec_print ( n, r, '  Residual r = b-A*x2:' )

  return

def r8pbu_sl ( n, mu, a_lu, b ):

#*****************************************************************************80
#
## R8PBU_SL solves a R8PBU system factored by R8PBU_FA.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, Philadelphia, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals of the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    real A_LU(MU+1,N), the matrix, as factored by R8PBU_FA.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution vector.
#
  x = b.copy ( )
#
#  Solve L * Y = B.
#
  for k in range ( 1, n + 1 ):
    ilo = max ( 1, k - mu )
    t = 0.0
    for i in range ( ilo, k ):
      t = t + x[i-1] * a_lu[mu+i-k,k-1]
    x[k-1] = ( x[k-1] - t ) / a_lu[mu,k-1]
#
#  Solve U * X = Y.
#
  for k in range ( n, 0, -1 ):

    x[k-1] = x[k-1] / a_lu[mu,k-1]

    ilo = max ( 1, k - mu )
    for i in range ( ilo, k ):
      x[i-1] = x[i-1] - x[k-1] * a_lu[mu+i-k,k-1]

  return x

def r8pbu_sl_test ( rng ):

#*****************************************************************************80
#
## r8pbu_sl_test() tests r8pbu_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 50
  mu = 1

  print ( '' )
  print ( 'r8pbu_sl_test():' )
  print ( '  r8pbu_sl() solves a linear system factored by R8PBU_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix values.
#
  a = r8pbu_random ( n, mu, rng )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the right hand side.
#
  b = r8pbu_mv ( n, mu, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8pbu_fa ( n, mu, a )
#
#  Solve the linear system.
#
  x = r8pbu_sl ( n, mu, a_lu, b )
 
  r8vec_print_some ( n, x, 10, '  Solution:' )

  return
 
def r8pbu_sor ( n, mu, a, b, eps, itchk, itmax, omega, x ):

#*****************************************************************************80
#
## R8PBU_SOR uses SOR iteration to solve a R8PBU linear system.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#    The matrix A must be a positive definite symmetric band matrix.
#
#    A relaxation factor OMEGA may be used.
#
#    The iteration will proceed until a convergence test is met,
#    or the iteration limit is reached.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0, and no more than N-1.
#
#    real A(MU+1,N), the R8PBU matrix.
#
#    real B(N), the right hand side of the system.
#
#    real EPS, convergence tolerance for the system.  The vector
#    b - A * x is computed every ITCHK iterations, and if the maximum
#    entry of this vector is of norm less than EPS, the program
#    will return.
#
#    integer ITCHK, the interval between convergence checks.  ITCHK steps
#    will be taken before any check is made on whether the iteration
#    has converged.  ITCHK should be at least 1 and no greater
#    than ITMAX.
#
#    integer ITMAX, the maximum number of iterations allowed.  The
#    program will return to the user if this many iterations are taken
#    without convergence.
#
#    real OMEGA, the relaxation factor.  OMEGA must be strictly between
#    0 and 2.  Use OMEGA = 1 for no relaxation, classical Jacobi iteration.
#
#    real X(N), a starting vector for the iteration.
#
#  Output:
#
#    real X_NEW(N), the current approximation to the solution.
#
#    integer ITKNT, the number of iterations taken.
#
  itknt = 0
  x_new = x.copy ( )

  if ( itchk <= 0 or itmax < itchk ):
    print ( '' )
    print ( 'R8PBU_SOR - Fatal error!' )
    print ( '  Illegal ITCHK = ', itchk )
    raise Exception ( 'R8PFU_SOR - Fatal error!' )

  if ( itmax <= 0 ):
    print ( '' )
    print ( 'R8PBU_SOR - Fatal error!' )
    print ( '  Nonpositive ITMAX = ', itmax )
    raise Exception ( 'R8PFU_SOR - Fatal error!' )

  if ( omega <= 0.0 or 2.0 <= omega ):
    print ( '' )
    print ( 'R8PBU_SOR - Fatal error!' )
    print ( '  Illegal value of OMEGA = ', omega )
    raise Exception ( 'R8PFU_SOR - Fatal error!' )

  itknt = 0
#
#  Take ITCHK steps of the iteration before doing a convergence check.
#
  while ( itknt <= itmax ):

    for it in range ( 0, itchk ):
#
#  Compute XTEMP(I) = B(I) + A(I,I) * X(I) - SUM ( 1 <= J <= N ) A(I,J) * X(J).
#
      xtemp = r8pbu_mv ( n, mu, a, x_new )

      for i in range ( 0, n ):
        xtemp[i] = x_new[i] + ( b[i] - xtemp[i] ) / a[mu,i]
#
#  Compute the next iterate as a weighted combination of the
#  old iterate and the just computed standard Jacobi iterate.
#
      if ( omega != 1.0 ):
        xtemp = ( 1.0 - omega ) * x_new + omega * xtemp

      itknt = itknt + 1
#
#  Copy the new result into the old result vector.
#
      x_new = xtemp.copy ( )
#
#  Compute the maximum residual, the greatest entry in the vector
#  RESID(I) = B(I) - A(I,J) * X(J).
#
    xtemp = r8pbu_mv ( n, mu, a, x_new )

    err = 0.0
    for i in range ( 0, n ):
      err = max ( err, abs ( b[i] - xtemp[i] ) )
#
#  Test to see if we can quit because of convergence,
#
    if ( err <= eps ):
      return x_new, itknt

  print ( '' )
  print ( 'R8PBU_SOR - Warning!' )
  print ( '  The iteration did not converge.' )

  return x_new, itknt

def r8pbu_sor_test ( ):

#*****************************************************************************80
#
## R8PBU_SOR_TEST tests R8PBU_SOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 50
  mu = 1

  print ( '' )
  print ( 'R8PBU_SOR_TEST' )
  print ( '  R8PBU_SOR, SOR routine for iterative' )
  print ( '  solution of A*x=b.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Upper bandwidth MU = ', mu )

  for k in range ( 1, 4 ):
 
    if ( k == 1 ):
      omega = 0.25
    elif ( k == 2 ):
      omega = 0.75
    else:
      omega = 1.00
#
#  Set matrix values.
#
    a = np.zeros ( [ mu + 1, n ] )

    for j in range ( 0, n ):
      a[1,j] = 2.0

    for j in range ( 1, n ):
      a[0,j] = -1.0
#
#  Set the desired solution.
#
    x = np.zeros ( n )
    for i in range ( 0, n ):
      t = np.pi * float ( i ) / float ( n - 1 )
      x[i] = np.sin ( t )
#
#  Compute the right hand side.
#
    b = r8pbu_mv ( n, mu, a, x )
#
#  Set the initial solution estimate.
#
    x = np.ones ( n )
 
    itchk = 1
    itmax = 8000
    eps = 0.0001

    x, itknt = r8pbu_sor ( n, mu, a, b, eps, itchk, itmax, omega, x )
#
#  Compute residual, A*x-b
#
    b2 = r8pbu_mv ( n, mu, a, x )
 
    err = 0.0
    for i in range ( 0, n ):
      err = max ( err, abs ( b2[i] - b[i] ) )
 
    print ( '' )
    print ( '  SOR iteration.' )
    print ( '' )
    print ( '  Relaxation factor OMEGA = ', omega )
    print ( '  Iterations taken = ', itknt )

    r8vec_print_some ( n, x, 10, '  Solution:' )

    print ( '' )
    print ( '  Maximum error = ', err )

  return

def r8pbu_to_r8ge ( n, mu, a ):

#*****************************************************************************80
#
## R8PBU_TO_R8GE copies a R8PBU matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#    N must be positive.
#
#    integer MU, the upper bandwidth of A1.
#    MU must be nonnegative, and no greater than N-1.
#
#    real A(MU+1,N), the R8PBU matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j and j <= i + mu ):
        b[i,j] = a[mu+i-j,j]
      elif ( i - mu <= j and j < i ):
        b[i,j] = a[mu+j-i,i]

  return b

def r8pbu_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8PBU_TO_R8GE_TEST tests R8PBU_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9
  mu = 3

  print ( '' )
  print ( 'R8PBU_TO_R8GE_TEST' )
  print ( '  R8PBU_TO_R9GE converts an R8PBU matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_indicator ( n, mu )

  r8pbu_print ( n, mu, a, '  The R8PBU matrix:' )

  a_r8ge = r8pbu_to_r8ge ( n, mu, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8pbu_zeros ( n, mu ):

#*****************************************************************************80
#
## R8PBU_ZEROS zeros a R8PBU matrix.
#
#  Discussion:
#
#    The R8PBU storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and upper triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#    The matrix returned will be positive definite, but of limited
#    randomness.  The off diagonal elements are random values between
#    0 and 1, and the diagonal element of each row is selected to
#    ensure strict diagonal dominance.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#  Output:
#
#    real A(MU+1,N), the R8PBU matrix.
#
  import numpy as np

  a = np.zeros ( [ mu + 1, n ] )

  return a

def r8pbu_zeros_test ( ):

#*****************************************************************************80
#
## R8PBU_ZEROS_TEST tests R8PBU_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9
  mu = 3

  print ( '' )
  print ( 'R8PBU_ZEROS_TEST' )
  print ( '  R8PBU_ZEROS sets up an R8PBU zero matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth MU = ', mu )

  a = r8pbu_zeros ( n, mu )

  r8pbu_print ( n, mu, a, '  The R8PBU zero matrix:' )

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

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## r8vec_print_some() prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
## r8vec2_print_some() prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_print, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vectors.
#
#    real X1(N), X2(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

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
  r8pbu_test ( )
  timestamp ( )
