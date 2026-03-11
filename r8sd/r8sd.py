#! /usr/bin/env python3
#
def r8sd_test ( ):

#*****************************************************************************80
#
## r8sd_test() tests r8sd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8sd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8sd().' )

  rng = default_rng ( )

  r8sd_cg_test ( )
  r8sd_dif2_test ( )
  r8sd_indicator_test ( )
  r8sd_mv_test ( )
  r8sd_print_test ( )
  r8sd_print_some_test ( )
  r8sd_random_test ( rng )
  r8sd_res_test ( rng )
  r8sd_to_r8ge_test ( )
  r8sd_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8sd_test():' )
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

def r8sd_cg ( n, ndiag, offset, a, b, x ):

#*****************************************************************************80
#
## R8SD_CG uses the conjugate gradient method on an R8SD linear system.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero
#    entries occur along a few diagonals, but for which these diagonals are 
#    not all close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals%),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#    For the conjugate gradient method to be applicable, the matrix A must 
#    be a positive definite symmetric matrix.
#
#    The method is designed to reach the solution to the linear system
#      A * x = b
#    after N computational steps.  However, roundoff may introduce
#    unacceptably large errors for some problems.  In such a case,
#    calling the routine a second time, using the current solution estimate
#    as the new starting guess, should result in improved results.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 July 2016
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
#
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.
#
#    real A(N,NDIAG), the R8SD matrix.
#
#    real B(N), the right hand side vector.
#
#    real X(N): an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N): the approximate solution vector.  Note that repeated
#    calls to this routine, using the value of X output on the previous
#    call, MAY improve the solution.
#
  import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r8sd_mv ( n, ndiag, offset, a, x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP = A*P.
#
    ap = r8sd_mv ( n, ndiag, offset, a, p )
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

def r8sd_cg_test ( ):

#*****************************************************************************80
#
## R8SD_CG_TEST tests R8SD_CG.
#
#  Discussion:
#
#    NX and NY are the number of grid points in the X and Y directions.
#    N is the number of unknowns.
#    NDIAG is the number of nonzero diagonals we will store.  We only
#      store the main diagonal, and the superdiagonals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ndiag = 3
  nx = 10
  ny = 10
  n = nx * ny
  offset = np.array ( [ 0, 1, nx ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_CG_TEST' )
  print ( '  R8SD_CG applies the conjugate gradient method' )
  print ( '  to a symmetric positive definite linear' )
  print ( '  system stored by diagonals.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Number of diagonals is ', ndiag )
  print ( '' )
#
#  Now we compute the numbers that go into the diagonals.  For this
#  problem, we could simply store a column of 4's, and two columns of
#  -1's, but I wanted to go through the motions of thinking about the
#  value of each entry.  "K" counts the row of the original matrix
#  that we are working on.
#
  a = np.zeros ( [ n, 3 ] )

  k = 0
  for j in range ( 0, ny ):
    for i in range ( 0, nx ):
#
#  Central
#
      a[k,0] = 4.0
#
#  East ( = West )
#
      if ( i != nx - 1 ):
        a[k,1] = -1.0
#
#  North ( = South )
#
      if ( j != ny - 1 ):
        a[k,2] = -1.0

      k = k + 1
#
#  Print some of the matrix.
#
  r8sd_print_some ( n, ndiag, offset, a, 0, 0, 9, 9, \
    '  Rows 0-9, Cols 0-9:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )

  k = 0
  for j in range ( 0, ny ):
    for i in range ( 0, nx ):
      x[k] = float ( 10 * ( i + 1 ) + ( j + 1 ) )
      k = k + 1
#
#  Compute the corresponding right hand side.
#
  b = r8sd_mv ( n, ndiag, offset, a, x )

  r8vec_print_some ( n, b, 10, '  Right hand side:' )
#
#  Set X to zero so no one accuses us of cheating.
#
  x = np.zeros ( n )
#
#  Call the conjugate gradient method.
#
  x = r8sd_cg ( n, ndiag, offset, a, b, x )
#
#  Compute the residual, A*x-b
#
  b2 = r8sd_mv ( n, ndiag, offset, a, x )
 
  err = max ( abs ( b2 - b ) )
 
  r8vec_print_some ( n, x, 10, '  Solution:' )

  print ( '' )
  print ( '  Maximum residual = ', err )
#
#  Note that if we're not satisfied with the solution, we can
#  again, using the computed X as our starting estimate.
#
#
#  Call the conjugate gradient method AGAIN.
#
  x = r8sd_cg ( n, ndiag, offset, a, b, x )
#
#  Compute the residual, A*x-b
#
  b2 = r8sd_mv ( n, ndiag, offset, a, x )
 
  err = max ( abs ( b2 - b ) )
 
  r8vec_print_some ( n, x, 10, '  Second attempt at solution:' )

  print ( '' )
  print ( '  Maximum residual of second attempt = ', err )

  return

def r8sd_dif2 ( n, ndiag, offset ):

#*****************************************************************************80
#
## R8SD_DIF2 returns the DIF2 matrix in R8SD format.
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
#    18 July 2016
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
#    integer N, the order of the matrix.
#
#    integer NDIAG, the number of diagonals that are stored.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.  It is simply assumed that OFFSET(1) = 0 and OFFSET(2) = 1.
#
#  Output:
#
#    real A(N,NDIAG), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, ndiag ] )

  a[0:n,  0] =  2.0
  a[0:n-1,1] = -1.0
 
  return a

def r8sd_dif2_test ( ):

#*****************************************************************************80
#
## R8SD_DIF2_TEST tests R8SD_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  ndiag = 2
  offset = np.array ( [ 0, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_DIF2_TEST' )
  print ( '  R8SD_DIF2 sets up a R8SD second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_dif2 ( n, ndiag, offset )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

  return

def r8sd_indicator ( n, ndiag, offset ):

#*****************************************************************************80
#
## R8SD_INDICATOR sets up a R8SD indicator matrix.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals!),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
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
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#  Output:
#
#    real A(N,NDIAG), the R8SD matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ n, ndiag ] )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        a[i,jdiag] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8sd_indicator_test ( ):

#*****************************************************************************80
#
## R8SD_INDICATOR_TEST tests R8SD_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_INDICATOR_TEST' )
  print ( '  R8SD_INDICATOR sets up a R8SD indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_indicator ( n, ndiag, offset )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD indicator matrix:' )

  return

def r8sd_mv ( n, ndiag, offset, a, x ):

#*****************************************************************************80
#
## R8SD_MV multiplies an R8SD matrix by an R8VEC.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero 
#    entries occur along a few diagonals, but for which these diagonals are not 
#    all close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals%),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns.
#
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.
#
#    real A(N,NDIAG), the R8SD matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      if ( 0 <= offset[jdiag] ):
        j = i + offset[jdiag]
        if ( 0 <= j and j < n ):
          b[i] = b[i] + a[i,jdiag] * x[j]
          if ( offset[jdiag] != 0 ):
            b[j] = b[j] + a[i,jdiag] * x[i]

  return b

def r8sd_mv_test ( ):

#*****************************************************************************80
#
## R8SD_MV_TEST tests R8SD_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_MV_TEST' )
  print ( '  R8SD_MV computes b=A*x, where A is an R8SD matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_indicator ( n, ndiag, offset )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8sd_mv ( n, ndiag, offset, a, x )

  r8vec_print ( n, b, '  The product b=A*x' )

  return

def r8sd_print ( n, ndiag, offset, a, title ):

#*****************************************************************************80
#
## R8SD_PRINT prints a R8SD matrix.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals!),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8SD matrix.
#
#    string TITLE, a title to be printed.
#
  r8sd_print_some ( n, ndiag, offset, a, 0, 0, n - 1, n - 1, title )

  return

def r8sd_print_test ( ):

#*****************************************************************************80
#
## R8SD_PRINT_TEST tests R8SD_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_PRINT_TEST' )
  print ( '  R8SD_PRINT prints an R8SD matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_indicator ( n, ndiag, offset )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

  return

def r8sd_print_some ( n, ndiag, offset, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8SD_PRINT_SOME prints some of a R8SD matrix.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals!),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8SD matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  import numpy as np

  print ( '' )
  print ( title )

  incx = 5

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )

      for j in range ( j2lo, j2hi + 1 ):

        aij = 0.0

        for jdiag in range ( 0, ndiag ):
          if ( j - i == offset[jdiag] ):
            aij = a[i,jdiag]
          elif ( i - j == offset[jdiag] ):
            aij = a[j,jdiag]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8sd_print_some_test ( ):

#*****************************************************************************80
#
## R8SD_PRINT_SOME_TEST tests R8SD_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_PRINT_SOME_TEST' )
  print ( '  R8SD_PRINT_SOME prints some of an R8SD matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_indicator ( n, ndiag, offset )

  r8sd_print_some ( n, ndiag, offset, a, 2, 3, 8, 7, '  Rows 2-8, Cols 3-7:' )

  return

def r8sd_random ( n, ndiag, offset, rng ):

#*****************************************************************************80
#
## r8sd_random() randomizes a R8SD matrix.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals!),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
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
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(N,NDIAG), the R8SD matrix.
#
  import numpy as np

  a = np.zeros ( [ n, ndiag ] )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        a[i,jdiag] = rng.random ( )

  return a

def r8sd_random_test ( rng ):

#*****************************************************************************80
#
## r8sd_random_test() tests r8sd_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
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
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'r8sd_random_test():' )
  print ( '  r8sd_random() randomizes an R8SD matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_random ( n, ndiag, offset, rng )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

  return

def r8sd_res ( n, ndiag, offset, a, x, b ):

#*****************************************************************************80
#
## R8SD_RES computes the residual R = B-A*X for R8SD matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.
#
#    real A(N,NDIAG), the R8SD matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real B(N), the desired result A * x.
#
#  Output:
#
#    real R(N), the residual R = B - A * X.
#
  r = r8sd_mv ( n, ndiag, offset, a, x )

  r = b - r

  return r

def r8sd_res_test ( rng ):

#*****************************************************************************80
#
## r8sd_res_test() tests r8sd_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 July 2016
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
  ndiag = 2
  offset = np.array ( [ 0, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'r8sd_res_test():' )
  print ( '  r8sd_res() computes a residual r=b-A*x' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Number of diagonals is ', ndiag )

  a = r8sd_random ( n, ndiag, offset, rng )
#
#  Print the matrix.
#
  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8sd_mv ( n, ndiag, offset, a, x )

  r8vec_print ( n, b, '  The product b=A*x' )
#
#  Make X2, a bad copy of X.
#
  x2 = np.zeros ( n )

  for i in range ( 0, n ):
    e = rng.random ( )
    x2[i] = x[i] + 0.1 * e

  r8vec_print ( n, x2, '  The defective vector x2:' )
#
#  Compute R = B-A*X2.
#
  r = r8sd_res ( n, ndiag, offset, a, x2, b )
  
  r8vec_print ( n, r, '  Residual r=b-A*x2:' )

  return

def r8sd_to_r8ge ( n, ndiag, offset, a ):

#*****************************************************************************80
#
## r8sd_to_r8ge() copies a R8SD matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals!),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
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
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8SD matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        b[i,j] = a[i,jdiag]
        if ( i != j ):
          b[j,i] = a[i,jdiag]

  return b

def r8sd_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8SD_TO_R8GE_TEST tests R8SD_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_TO_R8GE_TEST' )
  print ( '  R8SD_TO_R8GE converts an R8SD matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_indicator ( n, ndiag, offset )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

  a_r8ge = r8sd_to_r8ge ( n, ndiag, offset, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8sd_zeros ( n, ndiag, offset ):

#*****************************************************************************80
#
## R8SD_ZEROS zeros an R8SD matrix.
#
#  Discussion:
#
#    The R8SD storage format is for symmetric matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0, and 
#    each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals!),
#    we then create an array B that has N rows and NDIAG columns, and simply
#    "collapse" the matrix A to the left:
#
#  Example:
#
#    The "offset" value is printed above each column.
#
#    Original matrix               New Matrix
#
#       0   1   2   3   4   5       0   1   3   5
#
#      11  12   0  14   0  16      11  12  14  16
#      21  22  23   0  25   0      22  23  25  --
#       0  32  33  34   0  36      33  34  36  --
#      41   0  43  44  45   0      44  45  --  --
#       0  52   0  54  55  56      55  56  --  --
#      61   0  63   0  65  66      66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
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
#    integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#  Output:
#
#    real A(N,NDIAG), the R8SD matrix.
#
  import numpy as np

  a = np.zeros ( [ n, ndiag ] )

  return a

def r8sd_zeros_test ( ):

#*****************************************************************************80
#
## R8SD_ZEROS_TEST tests R8SD_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  ndiag = 3
  offset = np.array ( [ 0, 1, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8SD_ZEROS_TEST' )
  print ( '  R8SD_ZEROS zeros an R8SD matrix.' )
  print ( '' )
  print ( '  Matrix order N =         ', n )
  print ( '  Matrix diagonals NDIAG = ', ndiag )

  a = r8sd_zeros ( n, ndiag, offset )

  r8sd_print ( n, ndiag, offset, a, '  The R8SD matrix:' )

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
  r8sd_test ( )
  timestamp ( )
 
