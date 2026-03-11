#! /usr/bin/env python3
#
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
  i = int ( i )

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

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test() tests i4_log_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test():' )
  print ( '  i4_log_10(): whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def r8ge_cg ( n, a, b, x ):

#*****************************************************************************80
#
## r8ge_cg() uses the conjugate gradient method on an R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
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
#    06 July 2015
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
#    real A(N,N), the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X(N), an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N), the approximate solution.
#
  import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r8ge_mv ( n, n, a, x )

  r = np.zeros ( n, dtype = np.float64 )
  for i in range ( 0, n ):
    r[i] = b[i] - ap[i]

  p = np.zeros ( n, dtype = np.float64 )
  for i in range ( 0, n ):
    p[i] = b[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r8ge_mv ( n, n, a, p )
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

def r8ge_cg_test ( rng ):

#*****************************************************************************80
#
## r8ge_cg_test() tests r8ge_cg() for a full storage matrix.
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
  print ( 'r8ge_cg_test():' )
  print ( '  r8ge_cg() applies CG to an R8GE matrix.' )
#
#  Choose a random positive definite symmetric matrix A.
#
  n = 10
  key = 123456789

  a = r8ge_spd_random ( n, key )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r8ge_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r8ge_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r8ge_co ( n, a ):

#*****************************************************************************80
#
## r8ge_co() factors a R8GE matrix and estimates its condition number.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    For the system A * X = B, relative perturbations in A and B
#    of size EPSILON may cause relative perturbations in X of size
#    EPSILON/RCOND.
#
#    If RCOND is so small that the logical expression
#      1.0 + rcond == 1.0
#    is true, then A may be singular to working precision.  In particular,
#    RCOND is zero if exact singularity is detected or the estimate
#    underflows.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979
#
#  Input:
#
#    integer N, the order of the matrix A.
#
#    real A(N,N), a matrix to be factored.
#
#  Output:
#
#    real A_LU(N,N), the LU factorization of the matrix.
#
#    integer PIVOT(N), the pivot indices.
#
#    real RCOND, an estimate of the reciprocal condition number of A.
#
#    real Z(N), a work vector whose contents are usually unimportant.
#    If A is close to a singular matrix, then Z is an approximate null vector
#    in the sense that
#      norm ( A * Z ) = RCOND * norm ( A ) * norm ( Z ).
#
  import numpy as np
#
#  Compute the L1 norm of A.
#
  anorm = 0.0
  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + abs ( a[i,j] )
    anorm = max ( anorm, t )
#
#  Compute the LU factorization.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
#
#  RCOND = 1 / ( norm(A) * (estimate of norm(inverse(A))) )
#
#  estimate of norm(inverse(A)) = norm(Z) / norm(Y)
#
#  where
#    A * Z = Y
#  and
#    A' * Y = E
#
#  The components of E are chosen to cause maximum local growth in the
#  elements of W, where U'*W = E.  The vectors are frequently rescaled
#  to avoid overflow.
#
#  Solve U' * W = E.
#
  ek = 1.0
  z = np.zeros ( n )

  for k in range ( 0, n ):

    if ( z[k] != 0.0 ):
      ek = - r8_sign ( z[k] ) * abs ( ek )

    if ( abs ( a_lu[k,k] ) < abs ( ek - z[k] ) ):
      s = abs ( a_lu[k,k] ) / abs ( ek - z[k] )
      for i in range ( 0, n ):
        z[i] = s * z[i]
      ek = s * ek

    wk = ek - z[k]
    wkm = - ek - z[k]
    s = abs ( wk )
    sm = abs ( wkm )

    if ( a_lu[k,k] != 0.0 ):
      wk = wk / a_lu[k,k]
      wkm = wkm / a_lu[k,k]
    else:
      wk = 1.0
      wkm = 1.0

    if ( k + 1 <= n - 1 ):

      for j in range ( k + 1, n ):
        sm = sm + abs ( z[j] + wkm * a_lu[k,j] )
        z[j] = z[j] + wk * a_lu[k,j]
        s = s + abs ( z[j] )

      if ( s < sm ):
        t = wkm - wk
        wk = wkm
        for i in range ( k + 1, n ):
          z[i] = z[i] + t * a_lu[k,i]

    z[k] = wk

  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )
  for i in range ( 0, n ):
    z[i] = z[i] / t
#
#  Solve L' * Y = W
#
  for k in range ( n - 1, -1, -1 ):

    for i in range ( k + 1, n ):
      z[k] = z[k] + a_lu[i,k] * z[k]

    t = abs ( z[k] )

    if ( 1.0 < t ):
      for i in range ( 0, n ):
        z[i] = z[i] / t

    l = pivot[k]
    t    = z[l]
    z[l] = z[k]
    z[k] = t

  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t

  ynorm = 1.0
#
#  Solve L * V = Y.
#
  for k in range ( 0, n ):

    l = pivot[k]
    t    = z[l]
    z[l] = z[k]
    z[k] = t

    for i in range ( k + 1, n ):
      z[i] = z[i] + t * a_lu[i,k]

    if ( 1.0 < abs ( z[k] ) ):
      ynorm = ynorm / abs ( z[k] )
      for i in range ( 0, n ):
        z[i] = z[i] / abs ( z[k] )

  s = 0.0
  for i in range ( 0, n ):
    s = s + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / s

  ynorm = ynorm / s
#
#  Solve U * Z = V.
#
  for k in range ( n - 1, -1, -1 ):

    if ( abs ( a_lu[k,k] ) < abs ( z[k] ) ):
      s = abs ( a_lu[k,k] ) / abs ( z[k] )
      for i in range ( 0, n ):
        z[i] = s * z[i]
      ynorm = s * ynorm

    if ( a_lu[k,k] != 0.0 ):
      z[k] = z[k] / a_lu[k,k]
    else:
      z[k] = 1.0

    for i in range ( 0, k ):
      z[i] = z[i] - z[k] * a_lu[i,k]
#
#  Normalize Z in the L1 norm.
#
  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t

  ynorm = ynorm / t

  if ( anorm != 0.0E+00 ):
    rcond = ynorm / anorm
  else:
    rcond = 0.0

  return a_lu, pivot, rcond, z

def r8ge_co_test ( ):

#*****************************************************************************80
#
## r8ge_co_test() tests r8ge_co().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  x = 2.0
  y = 3.0

  print ( '' )
  print ( 'r8ge_co_test():' )
  print ( '  r8ge_co() estimates the condition number of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = x + y
      else:
        a[i,j] = y

  a_norm_l1 = 0.0
  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + abs ( a[i,j] )
    a_norm_l1 = max ( a_norm_l1, t )

  a_lu, pivot, info = r8ge_fa ( n, a )

  a_inverse = r8ge_inverse ( n, a_lu, pivot )

  a_inverse_norm_l1 = 0.0
  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + abs ( a_inverse[i,j] )
    a_inverse_norm_l1 = max ( a_inverse_norm_l1, t )

  cond_l1 = a_norm_l1 * a_inverse_norm_l1

  print ( '' )
  print ( '  The L1 condition number is %g' % ( cond_l1 ) )
#
#  Factor the matrix.
#
  a_lu, pivot, rcond, z = r8ge_co ( n, a )

  print ( '' )
  print ( '  The r8ge_co estimate is %g' % ( 1.0 / rcond ) )

  return

def r8ge_copy ( m, n, a ):

#*****************************************************************************80
#
## r8ge_copy() copies an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix to be copied.
#
#  Output:
#
#    real B(M,N), the copied matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[i,j] = a[i,j]

  return b

def r8ge_copy_test ( ):

#*****************************************************************************80
#
## r8ge_copy_test() tests r8ge_copy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_copy_test():' )
  print ( '  r8ge_copy() copies an R8GE matrix.' )

  a = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a, '  Indicator matrix A:' )

  b = r8ge_copy ( m, n, a )

  r8ge_print ( m, n, b, '  B = copy of A:' )

  return

def r8ge_det ( n, a_lu, pivot ):

#*****************************************************************************80
#
## r8ge_det(): determinant of a matrix factored by r8ge_fa or r8ge_trf.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
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
#  Reference:
#
#    Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979,
#    ISBN13: 978-0-898711-72-1,
#    LC: QA214.L56.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa 
#    or r8ge_trf.
#
#    integer PIVOT(N), as computed by r8ge_fa or r8ge_trf.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i]
    if ( pivot[i] != i ):
      value = - value

  return value

def r8ge_det_test ( ):

#*****************************************************************************80
#
## r8ge_det_test() tests r8ge_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  x = 2.0
  y = 3.0

  print ( '' )
  print ( 'r8ge_det_test():' )
  print ( '  r8ge_det() computes the determinant of an R8GE matrix.' )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = x + y
      else:
        a[i,j] = y
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
#
#  Compute the determinant.
#
  det = r8ge_det ( n, a_lu, pivot )

  exact = x ** ( n - 1 ) * ( x + n * y )

  print ( '' )
  print ( '  r8ge_det computes the determinant = %g' % ( det ) )
  print ( '  Exact determinant =                 %g' % ( exact ) )

  return

def r8ge_dif2 ( m, n ):

#*****************************************************************************80
#
## r8ge_dif2() returns the DIF2 matrix in R8GE format.
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
#    06 July 2015
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
#    real A(M,N), the matrix.
#
  import numpy as np

  a = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      if ( j == i - 1 ):
        a[i,j] = -1.0
      elif ( j == i ):
        a[i,j] = 2.0
      elif ( j == i + 1 ):
        a[i,j] = -1.0

  return a

def r8ge_dif2_test ( ):

#*****************************************************************************80
#
## r8ge_dif2_test() tests r8ge_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_dif2_test():' )
  print ( '  r8ge_dif2 returns the second difference matrix.' )

  a = r8ge_dif2 ( m, n )

  r8ge_print ( m, n, a, '  DIF2 matrix:' )

  return

def r8ge_dilu ( m, n, a ):

#*****************************************************************************80
#
## r8ge_dilu() produces the diagonal incomplete LU factor of an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the R8GE matrix.
#
#  Output:
#
#    real D(M), the DILU factor.
#
  import numpy as np

  d = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    if ( i < n ):
      d[i] = a[i,i]

  mn = min ( m, n )

  for i in range ( 0, mn ):
    d[i] = 1.0 / d[i]
    for j in range ( i + 1, mn ):
      d[j] = d[j] - a[j,i] * d[i] * a[i,j]

  return d

def r8ge_dilu_test ( ):

#*****************************************************************************80
#
## r8ge_dilu_test() tests r8ge_dilu().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ncol = 3
  nrow = 3
  n = nrow * ncol
  m = n

  print ( '' )
  print ( 'r8ge_dilu_test():' )
  print ( '  r8ge_dilu returns the DILU factors of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, nrow * ncol ):
    for j in range ( 0, nrow * ncol ):

      if ( i == j ):
        a[i,j] = 4.0
      elif ( i == j + 1 or i == j - 1 or i == j + nrow or i == j - nrow ):
        a[i,j] = -1.0
      else:
        a[i,j] = 0.0

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Compute the incomplete LU factorization.
#
  d = r8ge_dilu ( m, n, a )

  r8vec_print ( m, d, '  DILU factor:' )

  return

def r8ge_fa ( n, a ):

#*****************************************************************************80
#
## r8ge_fa() performs a LINPACK style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_fa is a simplified version of the LINPACK routine R8GEFA.
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
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(N,N), the matrix to be factored.
#
#  Output:
#
#    real A_LU(N,N), an upper triangular matrix and 
#    the multipliers used to obtain it.  The factorization 
#    can be written A = L * U, where L is a product of 
#    permutation and unit lower triangular matrices and U 
#    is upper triangular.
#
#    integer PIVOT(N), a vector of pivot indices.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np

  a_lu = r8ge_zeros ( n, n )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_lu[i,j] = a[i,j]

  info = 0

  pivot = np.zeros ( n, dtype = np.int32 )

  for k in range ( 0, n - 1 ):
#
#  Find L, the index of the pivot row.
#
    l = k
    for i in range ( k + 1, n ):
      if ( abs ( a_lu[l,k] ) < abs ( a_lu[i,k] ) ):
        l = i

    pivot[k] = l
#
#  If the pivot index is zero, the algorithm has failed.
#
    if ( a_lu[l,k] == 0.0 ):
      info = k
      return a_lu, pivot, info
#
#  Interchange rows L and K if necessary.
#
    if ( l != k ):
      t         = a_lu[l,k]
      a_lu[l,k] = a_lu[k,k]
      a_lu[k,k] = t
#
#  Normalize the values that lie below the pivot entry A(K,K).
#
    for i in range ( k + 1, n ):
      a_lu[i,k] = - a_lu[i,k] / a_lu[k,k]
#
#  Row elimination with column indexing.
#
    for j in range ( k + 1, n ):

      if ( l != k ):
        t         = a_lu[l,j]
        a_lu[l,j] = a_lu[k,j]
        a_lu[k,j] = t

      for i in range ( k + 1, n ):
        a_lu[i,j] = a_lu[i,j] + a_lu[i,k] * a_lu[k,j]

  pivot[n-1] = n - 1

  if ( a_lu[n-1,n-1] == 0.0 ):
    info = n - 1

  return a_lu, pivot, info

def r8ge_fa_test01 ( ):

#*****************************************************************************80
#
## r8ge_fa_test01() tests r8ge_fa(), r8ge_sl().
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
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8ge_fa_test01' )
  print ( '  For a matrix in general storage,' )
  print ( '  r8ge_fa computes the LU factors,' )
  print ( '  r8ge_sl solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_fa_test01 - Warning!' )
    print ( '  r8ge_fa declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )

    return
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  for i in range ( 0, n ):
    x[i] = 1.0
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 1
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_fa_test02 ( ):

#*****************************************************************************80
#
## r8ge_fa_test02() tests r8ge_fa(), r8ge_sl().
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
  import numpy as np

  n = 5
 
  print ( '' )
  print ( 'r8ge_fa_test02' )
  print ( '  For a matrix in general storage,' )
  print ( '  r8ge_fa computes the LU factors,' )
  print ( '  r8ge_sl solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )

  r8ge_print ( n, n, a, '  The matrix:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_fa_test02 - Warning!' )
    print ( '  r8ge_fa declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
#
#  Display the gory details.
#
  r8ge_print ( n, n, a_lu, '  The compressed LU factors:' )

  i4vec_print ( n, pivot, '  The pivot vector P:' )
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8ge_fs ( n, a, b ):

#*****************************************************************************80
#
## r8ge_fs() factors and solves a R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_fs does not save the LU factors of the matrix, and hence cannot
#    be used to efficiently solve multiple linear systems, or even to
#    factor A at one time, and solve a single linear system at a later time.
#
#    r8ge_fs uses partial pivoting, but no pivot vector is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
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
#    real A(N,N), the coefficient matrix of the linear system.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  info = 0
  x = b.copy ( )

  for jcol in range ( 0, n ):
#
#  Find the maximum element in column I.
#
    piv = abs ( a[jcol,jcol] )
    ipiv = jcol
    for i in range ( jcol + 1, n ):
      if ( piv < abs ( a[i,jcol] ) ):
        piv = abs ( a[i,jcol] )
        ipiv = i

    if ( piv == 0.0 ):
      info = jcol
      return
#
#  Switch rows JCOL and IPIV, and B.
#
    if ( jcol != ipiv ):

      for j in range ( 0, n ):
        t         = a[jcol,j]
        a[jcol,j] = a[ipiv,j]
        a[ipiv,j] = t

      t       = x[jcol]
      x[jcol] = x[ipiv]
      x[ipiv] = t
#
#  Scale the pivot row.
#
    t = a[jcol,jcol]
    a[jcol,jcol] = 1.0
    for k in range ( jcol + 1, n ):
      a[jcol,k] = a[jcol,k] / t
    x[jcol] = x[jcol] / t
#
#  Use the pivot row to eliminate lower entries in that column.
#
    for i in range ( jcol + 1, n ):
      if ( a[i,jcol] != 0.0 ):
        t = - a[i,jcol]
        a[i,jcol] = 0.0
        for k in range ( jcol + 1, n ):
          a[i,k] = a[i,k] + t * a[jcol,k]
        x[i] = x[i] + t * x[jcol]
#
#  Back solve.
#
  for jcol in range ( n - 1, 0, -1 ):
    for k in range ( 0, jcol ):
      x[k] = x[k] - a[k,jcol] * x[jcol]

  return x

def r8ge_fs_test ( ):

#*****************************************************************************80
#
## r8ge_fs_test() tests r8ge_fs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'r8ge_fs_test():' )
  print ( '  r8ge_fs factors and solves a linear system involving' )
  print ( '  an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor and solve the system.
#
  x = r8ge_fs ( n, a, b )
 
  r8vec_print ( n, x, '  Solution:' )

  return

def r8ge_fss ( n, a, nb, b ):

#*****************************************************************************80
#
## r8ge_fss() factors and solves a R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    This routine does not save the LU factors of the matrix, and hence cannot
#    be used to efficiently solve multiple linear systems, or even to
#    factor A at one time, and solve a single linear system at a later time.
#
#    This routine uses partial pivoting, but no pivot vector is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2009
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
#    real A(N,N), the coefficient matrix of the linear system.
#
#    integer NB, the number of right hand sides.
#
#    real B(N,NB), the right hand side of the linear system.
#
#  Output:
#
#    real B(N,NB), the solution of the linear system.
#
  import numpy as np

  info = 0

  for jcol in range ( 0, n ):
#
#  Find the maximum element in column I.
#
    piv = abs ( a[jcol,jcol] )
    ipiv = jcol
    for i in range ( jcol + 1, n ):
      if ( piv < abs ( a[i,jcol] ) ):
        piv = abs ( a[i,jcol] )
        ipiv = i

    if ( piv == 0.0 ):
      info = jcol
      return
#
#  Switch rows JCOL and IPIV, and B.
#
    if ( jcol != ipiv ):

      for j in range ( 0, n ):
        t         = a[jcol,j]
        a[jcol,j] = a[ipiv,j]
        a[ipiv,j] = t

      for j in range ( 0, nb ):
        t         = b[jcol,j]
        b[jcol,j] = b[ipiv,j]
        b[ipiv,j] = t
#
#  Scale the pivot row.
#
    t = a[jcol,jcol]
    a[jcol,jcol] = 1.0
    for k in range ( jcol + 1, n ):
      a[jcol,k] = a[jcol,k] / t
    for k in range ( 0, nb ):
      b[jcol,k] = b[jcol,k] / t
#
#  Use the pivot row to eliminate lower entries in that column.
#
    for i in range ( jcol + 1, n ):
      if ( a[i,jcol] != 0.0 ):
        t = - a[i,jcol]
        a[i,jcol] = 0.0
        for k in range ( jcol + 1, n ):
          a[i,k] = a[i,k] + t * a[jcol,k]
        for k in range ( 0, nb ):
          b[i,k] = b[i,k] + t * b[jcol,k]
#
#  Back solve.
#
  for j in range ( 0, nb ):
    for jcol in range ( n - 1, 0, -1 ):
      for k in range ( 0, jcol ):
        b[k,j] = b[k,j] - a[k,jcol] * b[jcol,j]

  return b

def r8ge_fss_test ( ):

#*****************************************************************************80
#
## r8ge_fss_test() tests r8ge_fss().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  nb = 3

  print ( '' )
  print ( 'r8ge_fss_test():' )
  print ( '  r8ge_fss factors and solves multiple linear systems' )
  print ( '  associated with an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solutions.
#
  x = np.zeros ( [ n, 3 ] )

  for i in range ( 0, n ):
    x[i,0] = 1.0
    x[i,1] = i + 1
    x[i,2] = ( i % 3 ) + 1

  b = r8ge_mm ( n, n, nb, a, x )
#
#  Factor and solve the system.
#
  x = r8ge_fss ( n, a, nb, b )
 
  r8ge_print ( n, nb, x, '  Solution:' )

  return

def r8ge_hilbert ( m, n ):

#*****************************************************************************80
#
## r8ge_hilbert() returns the Hilbert matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#    1/1 1/2 1/3 1/4 1/5
#    1/2 1/3 1/4 1/5 1/6
#    1/3 1/4 1/5 1/6 1/7
#    1/4 1/5 1/6 1/7 1/8
#    1/5 1/6 1/7 1/8 1/9
#
#  Rectangular Properties:
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#  Square Properties:
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is totally positive.
#
#    A is a Cauchy matrix.
#
#    A is nonsingular.
#
#    A is very ill-conditioned.
#
#    The entries of the inverse of A are all integers.
#
#    The sum of the entries of the inverse of A is N*N.
#
#    The ratio of the absolute values of the maximum and minimum
#    eigenvalues is roughly EXP(3.5*N).
#
#    The determinant of the Hilbert matrix of order 10 is
#    2.16417... * 10^(-53).
#
#    If the (1,1) entry of the 5 by 5 Hilbert matrix is changed
#    from 1 to 24/25, the matrix is exactly singular.  And there
#    is a similar rule for larger Hilbert matrices.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MD Choi,
#    Tricks or treats with the Hilbert matrix,
#    American Mathematical Monthly,
#    Volume 90, 1983, pages 301-312.
#
#    Robert Gregory, David Karney,
#    Example 3.8,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 33,
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    Society for Industrial and Applied Mathematics, Philadelphia, PA,
#    USA, 1996; section 26.1.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition
#    Addison-Wesley, Reading, Massachusetts, 1973, page 37.
#
#    Morris Newman and John Todd,
#    Example A13,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, 1958, pages 466-476.
#
#    Joan Westlake,
#    Test Matrix A12,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / ( i + j + 1 )

  return a

def r8ge_hilbert_test ( ):

#*****************************************************************************80
#
## r8ge_hilbert_test() tests r8ge_hilbert().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_hilbert_test():' )
  print ( '  r8ge_hilbert returns the Hilbert matrix.' )

  a = r8ge_hilbert ( m, n )

  r8ge_print ( m, n, a, '  Hilbert matrix:' )

  return

def r8ge_hilbert_inverse ( n ):

#*****************************************************************************80
#
## r8ge_hilbert_inverse() returns the inverse of the Hilbert matrix.
#
#  Formula:
#
#    A(I,J) =  (-1)^(I+J) * (N+I-1)! * (N+J-1)! /
#           [ (I+J-1) * ((I-1)!*(J-1)!)^2 * (N-I)! * (N-J)! ]
#
#  Example:
#
#    N = 5
#
#       25    -300     1050    -1400     630
#     -300    4800   -18900    26880  -12600
#     1050  -18900    79380  -117600   56700
#    -1400   26880  -117600   179200  -88200
#      630  -12600    56700   -88200   44100
#
#  Properties:
#
#    A is symmetric.
#
#    Because A is symmetric, it is normal, so diagonalizable.
#
#    A is almost impossible to compute accurately by general routines
#    that compute the inverse.
#
#    A is integral.
#
#    The sum of the entries of A is N^2.
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
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the inverse Hilbert matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )
#
#  Set the (1,1) entry.
#
  a[0,0] = n * n
#
#  Define Row 1, Column J by recursion on Row 1 Column J-1
#
  i = 0
  for j in range ( 1, n ):
    a[i,j] = - a[i,j-1] * float ( ( n + j ) * ( i + j ) * ( n - j ) ) \
      / float ( ( i + j + 1 ) * j * j )
#
#  Define Row I by recursion on row I-1
#
  for i in range ( 1, n ):
    for j in range ( 0, n ):

      a[i,j] = - a[i-1,j] * float ( ( n + i ) * ( i + j ) * ( n - i ) ) \
        / float ( ( i + j + 1 ) * i * i )

  return a

def r8ge_hilbert_inverse_test ( ):

#*****************************************************************************80
#
## r8ge_hilbert_inverse_test() tests r8ge_hilbert_inverse().
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
  n = 4

  print ( '' )
  print ( 'r8ge_hilbert_inverse_test():' )
  print ( '  r8ge_hilbert_inverse computes the inverse of the' )
  print ( '  Hilbert matrix, stored as an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ge_hilbert ( n, n )
  r8ge_print ( n, n, a, '  Matrix A:' )

  b = r8ge_hilbert_inverse ( n )

  r8ge_print ( n, n, b, '  Inverse matrix B:' )
#
#  Check.
#
  c = r8ge_mm ( n, n, n, a, b )

  r8ge_print ( n, n, c, '  Product A * B:' )

  return

def r8ge_house_axh ( n, a, v ):

#*****************************************************************************80
#
## r8ge_house_axh() computes A*H where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real A(N,N), the matrix to be postmultiplied.
#
#    real V(N), a vector defining a Householder matrix.
#
#  Output:
#
#    real AH(N,N), the product A*H.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ah = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ah[i,j] = a[i,j]
      for k in range ( 0, n ):
        ah[i,j] = ah[i,j] - 2.0 * a[i,k] * v[k] * v[j] / vtv
            
  return ah

def r8ge_house_axh_test ( ):

#*****************************************************************************80
#
## r8ge_house_axh_test() tests r8ge_house_axh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'R8G_house_AXH_test():' )
  print ( '  r8ge_house_axh multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0

  a = r8ge_random_ab ( n, n, r8_lo, r8_hi )

  r8ge_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A packs column 3 of A.
#
  k = 3
  km1 = k - 1
  a_col = np.zeros ( n )
  for i in range ( 0, n ):
    a_col[i] = a[i,km1]

  v = r8vec_house_column ( n, a_col, km1 )

  r8vec_print ( n, v, '  Compact vector V so column 3 of H*A is packed:' )

  h = r8ge_house_form ( n, v )

  r8ge_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8ge_house_axh ( n, a, v )

  r8ge_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = r8ge_mm ( n, n, n, a, h )

  r8ge_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = r8ge_mm ( n, n, n, h, a )

  r8ge_print ( n, n, ha, '  H*A should pack column 3:' )

  return

def r8ge_house_form ( n, v ):

#*****************************************************************************80
#
## r8ge_house_form() constructs a Householder matrix from its compact form.
#
#  Discussion:
#
#    H(v) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real V(N,1), the vector defining the Householder matrix.
#
#  Output:
#
#    real H(N,N), the Householder matrix.
#
  import numpy as np

  v_dot_v = 0.0
  for i in range ( 0, n ):
    v_dot_v = v_dot_v + v[i] * v[i]

  c = - 2.0 / v_dot_v

  h = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    h[j,j] = 1.0
    for i in range ( 0, n ):
      h[i,j] = h[i,j] + c * v[i] * v[j]
            
  return h

def r8ge_house_form_test ( ):

#*****************************************************************************80
#
## r8ge_house_form_test() tests r8ge_house_form().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  v = np.array ( ( 0.0, 0.0, 1.0, 2.0, 3.0 ) )

  print ( '' )
  print ( 'r8ge_house_form_test():' )
  print ( '  r8ge_house_form forms a Householder' )
  print ( '  matrix from its compact form.' )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8ge_house_form ( n, v )
 
  r8ge_print ( n, n, h, '  Householder matrix H:' )

  return

def r8ge_identity ( m, n ):

#*****************************************************************************80
#
## r8ge_identity() copies the identity matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of A.
#
#  Output:
#
#    real A(M,N), the identity matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  return a

def r8ge_identity_test ( ):

#*****************************************************************************80
#
## r8ge_identity_test() tests r8ge_identity().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_identity_test():' )
  print ( '  r8ge_identity returns the identity matrix.' )

  a = r8ge_identity ( m, n )

  r8ge_print ( m, n, a, '  Identity matrix:' )

  return

def r8ge_ilu ( m, n, a ):

#*****************************************************************************80
#
## r8ge_ilu() produces the incomplete LU factors of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    The incomplete LU factors of the M by N matrix A are:
#
#      L, an M by M unit lower triangular matrix,
#      U, an M by N upper triangular matrix
#
#    with the property that L and U are computed in the same way as
#    the usual LU factors, except that, whenever an off diagonal element
#    of the original matrix is zero, then the corresponding value of
#    U is forced to be zero.
#
#    This condition means that it is no longer the case that A = L*U.
#
#    On the other hand, L and U will have a simple sparsity structure
#    related to that of A.  The incomplete LU factorization is generally
#    used as a preconditioner in iterative schemes applied to sparse
#    matrices.  It is presented here merely for illustration.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the R8GE matrix.
#
#  Output:
#
#    real L(M,M), the M by M unit lower triangular factor.
#
#    real U(M,N), the M by N upper triangular factor.
#
  import numpy as np

  l = np.zeros ( [ m, m ] )

  for i in range ( 0, m ):
    l[i,i] = 1.0

  u = r8ge_copy ( m, n, a )

  for j in range ( 0, min ( m - 1, n ) ):
#
#  Zero out the entries in column J, from row J+1 to M.
#
    for i in range ( j + 1, m ):

      if ( u[i,j] != 0.0 ):

        l[i,j] = u[i,j] / u[j,j]
        u[i,j] = 0.0

        for k in range ( j + 1, n ):
          if ( u[i,k] != 0.0 ):
            u[i,k] = u[i,k] - l[i,j] * u[j,k]

  return l, u

def r8ge_ilu_test ( ):

#*****************************************************************************80
#
## r8ge_ilu_test() tests r8ge_ilu().
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
  import numpy as np

  ncol = 3
  nrow = 3
  n = nrow * ncol
  m = n

  print ( '' )
  print ( 'r8ge_ilu_test():' )
  print ( '  r8ge_ilu returns the ILU factors of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, nrow * ncol ):
    for j in range ( 0, nrow * ncol ):

      if ( i == j ):
        a[i,j] = 4.0
      elif ( i == j + 1 or i == j - 1 or i == j + nrow or i == j - nrow ):
        a[i,j] = -1.0
      else:
        a[i,j] = 0.0

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Compute the incomplete LU factorization.
#
  l, u = r8ge_ilu ( m, n, a )

  r8ge_print ( m, m, l, '  Factor L:' )

  r8ge_print ( m, n, u, '  Factor U:' )

  lu = r8ge_mm ( m, m, n, l, u )

  r8ge_print ( m, n, lu, '  Product L*U:' )

  return

def r8ge_indicator ( m, n ):

#*****************************************************************************80
#
## r8ge_indicator() sets an R8GE indicator matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = fac * ( i + 1 ) +  ( j + 1 )

  return a

def r8ge_indicator_test ( ):

#*****************************************************************************80
#
## r8ge_indicator_test() tests r8ge_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_indicator_test():' )
  print ( '  r8ge_indicator returns the indicator matrix.' )

  a = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a, '  Indicator matrix:' )

  return

def r8ge_inverse ( n, a_lu, pivot ):

#*****************************************************************************80
#
## r8ge_inverse() computes the inverse of a matrix factored by r8ge_fa.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_inverse is a simplified standalone version of the LINPACK routine
#    R8GEDI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix A.
#
#    real A_LU(N,N), the factor information computed by r8ge_fa.
#
#    integer PIVOT(N), the pivot vector from r8ge_fa.
#
#  Output:
#
#    real A_inverse(N,N), the inverse matrix.
#
  import numpy as np

  a_inverse = r8ge_copy ( n, n, a_lu )
#
#  Compute Inverse(U).
#
  for k in range ( 0, n ):

    a_inverse[k,k] = 1.0 / a_inverse[k,k]
    for i in range ( 0, k ):
      a_inverse[i,k] = -a_inverse[i,k] * a_inverse[k,k]

    for j in range ( k + 1, n ):

      temp = a_inverse[k,j]
      a_inverse[k,j] = 0.0
      for i in range ( 0, k + 1 ):
        a_inverse[i,j] = a_inverse[i,j] + a_inverse[i,k] * temp
#
#  Form Inverse(U) * Inverse(L).
#
  work = np.zeros ( n )

  for k in range ( n - 2, -1, -1 ):

    for i in range ( k + 1, n ):
      work[i] = a_inverse[i,k]
      a_inverse[i,k] = 0.0

    for j in range ( k + 1, n ):
      for i in range ( 0, n ):
        a_inverse[i,k] = a_inverse[i,k] + a_inverse[i,j] * work[j]

    if ( pivot[k] != k ):

      for i in range ( 0, n ):
        t                     = a_inverse[i,k]
        a_inverse[i,k]        = a_inverse[i,pivot[k]]
        a_inverse[i,pivot[k]] = t

  return a_inverse

def r8ge_inverse_test ( ):

#*****************************************************************************80
#
## r8ge_inverse_test() tests r8ge_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  x = 2.0
  y = 3.0

  print ( '' )
  print ( 'r8ge_inverse_test():' )
  print ( '  r8ge_inverse computes the inverse of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        a[i,i] = x + y
      else:
        a[i,j] = y

  r8ge_print ( n, n, a, '  Matrix A:' )
#
#  Factor and invert the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_inverse_test - Fatal error!' )
    print ( '  r8ge_fa reports the matrix is singular.' )
    return

  a_inverse = r8ge_inverse ( n, a_lu, pivot )

  r8ge_print ( n, n, a_inverse, '  Inverse matrix B:' )
#
#  Check.
#
  c = r8ge_mm ( n, n, n, a, a_inverse )

  r8ge_print ( n, n, c, '  Product matrix:' )

  return

def r8ge_ml ( n, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## r8ge_ml() computes A * x or A' * x, using r8ge_fa factors.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that r8ge_fa has overwritten the original matrix
#    information by LU factors.  r8ge_ml is able to reconstruct the
#    original matrix from the LU factor data.
#
#    r8ge_ml allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
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
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa.
#
#    integer PIVOT(N), the pivot vector computed by r8ge_fa.
#
#    real X(N), the vector to be multiplied.
#
#    integer JOB, specifies the operation to be done:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * X.
#
#  Output:
#
#    real B(N), the result of the multiplication.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    b[i] = x[i]

  if ( job == 0 ):
#
#  Y = U * X.
#
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        b[i] = b[i] + a_lu[i,j] * b[j]
      b[j] = a_lu[j,j] * b[j]
#
#  B = PL * Y = PL * U * X = A * x.
#
    for j in range ( n - 2, -1, -1 ):

      for i in range ( j + 1, n ):
        b[i] = b[i] - a_lu[i,j] * b[j]
      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

  else:
#
#  Y = (PL)' * X:
#
    for j in range ( 0, n - 1 ):

      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

      for i in range ( j + 1, n ):
        b[j] = b[j] - b[i] * a_lu[i,j]
#
#  B = U' * Y = ( PL * U )' * X = A' * X.
#
    for i in range ( n - 1, -1, -1 ):
      for j in range ( i + 1, n ):
        b[j] = b[j] + b[i] * a_lu[i,j]
      b[i] = b[i] * a_lu[i,i]

  return b

def r8ge_ml_test ( ):

#*****************************************************************************80
#
## r8ge_ml_test() tests r8ge_ml().
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
  n = 10

  print ( '' )
  print ( 'r8ge_ml_test():' )
  print ( '  r8ge_ml computes A*x or A\'*X' )
  print ( '  where A has been factored by r8ge_fa.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8ge_mv ( n, n, a, x )
    else:
      b = r8ge_mtv ( n, n, a, x )
#
#  Factor the matrix.
#
    a_lu, pivot, info = r8ge_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'r8ge_ml_test - Fatal error!' )
      print ( '  r8ge_fa declares the matrix is singular!' )
      print ( '  The value of INFO is %d,' % ( info ) )
      return
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8ge_ml ( n, a_lu, pivot, x, job )

    if ( job == 0 ):
      r8vec2_print_some ( n, b, b2, 10, '  A*x and PLU*x' )
    else:
      r8vec2_print_some ( n, b, b2, 10, '  A\'*x and (PLU)\'*x' )

  return

def r8ge_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8ge_mm() multiplies two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = r8ge_zeros ( n1, n3 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8ge_mm_test ( ):

#*****************************************************************************80
#
## r8ge_mm_test() tests r8ge_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8ge_mm_test():' )
  print ( '  r8ge_mm computes a matrix-matrix product C = A * B;' )

  a = r8ge_zeros ( n1, n2 )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8ge_mm ( n1, n2, n3, a, b )

  r8ge_print ( n1, n2, a, '  A:' )
  r8ge_print ( n2, n3, b, '  B:' )
  r8ge_print ( n1, n3, c, '  C = A*B:' )

  return

def r8ge_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8ge_mtm() computes A' * B for two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A' * B.
#
  import numpy as np

  c = r8ge_zeros ( n1, n3 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8ge_mtm_test ( ):

#*****************************************************************************80
#
## r8ge_mtm_test() tests r8ge_mtm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 Augsut 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8ge_mtm_test():' )
  print ( '  r8ge_mtm computes a matrix-matrix product C = A\' * B;' )

  a = r8ge_zeros ( n2, n1 )

  for i in range ( 0, n2 ): 
    for j in range ( 0, n1 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = a

  c = r8ge_mtm ( n1, n2, n3, a, b )

  r8ge_print ( n2, n1, a, '  A:' )
  r8ge_print ( n2, n3, b, '  B:' )
  r8ge_print ( n1, n3, c, '  C = A\'*B:' )

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

def r8ge_mtv_test ( ):

#*****************************************************************************80
#
## r8ge_mtv_test() tests r8ge_mtv().
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
  print ( 'r8ge_mtv_test():' )
  print ( '  r8ge_mtv computes a matrix product b=A\'*x for an R8GE matrix.' )

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

    a = r8ge_indicator ( m, n )
    r8ge_print ( m, n, a, '  The matrix A:' )

    x = r8vec_indicator1 ( m )
    r8vec_print ( m, x, '  The vector x:' )

    b = r8ge_mtv ( m, n, a, x )
    r8vec_print ( n, b, '  The vector b=A\'*x:' )

  return

def r8ge_mu ( m, n, a_lu, trans, pivot, x ):

#*****************************************************************************80
#
## r8ge_mu() computes A * x or A' * x, using r8ge_trf factors.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that r8ge_trf has overwritten the original matrix
#    information by PLU factors.  r8ge_mu is able to reconstruct the
#    original matrix from the PLU factor data.
#
#    r8ge_mu allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#
#    real A_LU(M,N), the LU factors from r8ge_trf.
#
#    character TRANS, specifies the form of the system of equations:
#    'N':  A * x = b  (No transpose)
#    'T':  A'* X = B  (Transpose)
#    'C':  A'* X = B  (Conjugate transpose = Transpose)
#
#    integer PIVOT(*), the pivot vector computed by r8ge_trf.
#
#    real X(*), the vector to be multiplied.
#    For the untransposed case, X should have N entries.
#    For the transposed case, X should have M entries.
#
#  Output:
#
#    real B(*), the result of the multiplication.
#    For the untransposed case, B should have M entries.
#    For the transposed case, B should have N entries.
#
  import numpy as np

  npiv = min ( m - 1, n )
  mn_max = max ( m, n )

  if ( trans == 'n' or trans == 'N' ):
#
#  Y[MN] = U[MNxN] * X[N].
#
    b = np.zeros ( m )
    y = np.zeros ( n )

    for j in range ( 0, n ):

      for i in range ( 0, min ( j + 1, m ) ):
        y[i] = y[i] + a_lu[i,j] * x[j]
#
#  Z[M] = L[MxMN] * Y[MN] = L[MxMN] * U[MNxN] * X[N].
#
    for i in range ( 0, m ):

      if ( i <= n - 1 ):
        b[i] = y[i]
      else:
        b[i] = 0.0

    for j in range ( min ( m - 2, n - 1 ), -1, -1 ):
      for i in range ( j + 1, m ):
        b[i] = b[i] + a_lu[i,j] * y[j]
#
#  B = P * Z = P * L * Y = P * L * U * X = A * x.
#
    for j in range ( npiv - 1, -1, -1 ):

      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

  elif ( trans == 't' or trans == 'T' or trans == 'c' or trans == 'C' ):

    b = np.zeros ( n )
#
#  Y = transpose(P) * X:
#
    for i in range ( 0, npiv ):

      k = pivot[i]

      if ( k != i ):
        t    = x[k]
        x[k] = x[i]
        x[i] = t

    for i in range ( 0, n ):

      if ( i <= m - 1 ):
        b[i] = x[i]
      else:
        b[i] = 0.0
#
#  Z = tranpose(L) * Y:
#
    for j in range ( 0, min ( m - 1, n ) ):
      for k in range ( j + 1, m ):
        b[j] = b[j] + x[k] * a_lu[k,j]
#
#  B = U' * Z.
#
    for i in range ( m - 1, -1, -1 ):
      for j in range ( i + 1, n ):
        b[j] = b[j] + b[i] * a_lu[i,j]
      if ( i <= n - 1 ):
        b[i] = b[i] * a_lu[i,i]
#
#  Now restore X.
#
    for i in range ( npiv - 1, -1, -1 ):

      k = pivot[i]

      if ( k != i ):
        t    = x[k]
        x[k] = x[i]
        x[i] = t

  else:

    print ( '' )
    print ( 'r8ge_mu - Fatal error!' )
    print ( '  Illegal value of TRANS = %c' % ( trans ) )
    raise Exception ( 'r8ge_mu - Fatal error!' )

  return b

def r8ge_mu_test ( ):

#*****************************************************************************80
#
## r8ge_mu_test() tests r8ge_mu().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 3

  print ( '' )
  print ( 'r8ge_mu_test():' )
  print ( '  r8ge_mu computes A*x or A\'*X' )
  print ( '  where A has been factored by r8ge_trf.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  for job in range ( 0, 2 ):

    if ( job == 0 ):
      trans = 'N'
    else:
      trans = 'T'
#
#  Set the matrix.
#
    amn = r8ge_random ( m, n )

    if ( job == 0 ):

      xn = r8vec_indicator1 ( n )

      cm = r8ge_mv ( m, n, amn, xn )

    else:

      xm = r8vec_indicator1 ( m )

      cn = r8ge_mtv ( m, n, amn, xm )
#
#  Factor the matrix.
#
    amn_lu, pivot, info = r8ge_trf ( m, n, amn )

    if ( info != 0 ):
      print ( '' )
      print ( 'r8ge_mu_test - Fatal error!' )
      print ( '  r8ge_trf declares the matrix is singular!' )
      print ( '  The value of INFO is %d' % ( info ) )
      continue
#
#  Now multiply the factored matrix times solution to get right hand side again.
#
    if ( job == 0 ):

      bm = r8ge_mu ( m, n, amn_lu, trans, pivot, xn )

      r8vec2_print_some ( m, cm, bm, 10, '  A*x and PLU*x' )

    else:

      bn = r8ge_mu ( m, n, amn_lu, trans, pivot, xm )

      r8vec2_print_some ( n, cn, bn, 10, '  A\'*x and (PLU)\'*x' )

  print ( '' )
  print ( '  Matrix is %d by %d' % ( n, m ) )

  for job in range ( 0, 2 ):

    if ( job == 0 ):
      trans = 'N'
    else:
      trans = 'T'
#
#  Set the matrix.
#
    anm = r8ge_random ( n, m )

    if ( job == 0 ):

      xm = r8vec_indicator1 ( m )

      cn = r8ge_mv ( n, m, anm, xm )

    else:

      xn = r8vec_indicator1 ( n )

      cm = r8ge_mtv ( n, m, anm, xn )
#
#  Factor the matrix.
#
    anm_lu, pivot, info = r8ge_trf ( n, m, anm )

    if ( info != 0 ):
      print ( '' )
      print ( 'r8ge_mu_test - Fatal error!' )
      print ( '  r8ge_trf declares the matrix is singular!' )
      print ( '  The value of INFO is %d' % ( info ) )
      continue
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    if ( job == 0 ):

      bn = r8ge_mu ( n, m, anm_lu, trans, pivot, xm )

      r8vec2_print_some ( n, cn, bn, 10, '  A*x and PLU*x' )

    else:

      bm = r8ge_mu ( n, m, anm_lu, trans, pivot, xn )

      r8vec2_print_some ( m, cm, bm, 10, '  A\'*x and (PLU)\'*x' )

  return

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

def r8ge_mv_test ( ):

#*****************************************************************************80
#
## r8ge_mv_test() tests r8ge_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_mv_test():' )
  print ( '  r8ge_mv computes a matrix product b=A*x for an R8GE matrix.' )

  a = r8ge_indicator ( m, n )
  r8ge_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector X:' )

  b = r8ge_mv ( m, n, a, x )
  r8vec_print ( n, b, '  The vector b=A*x:' )

  return

def r8ge_orth_random ( n, key ):

#*****************************************************************************80
#
## r8ge_orth_random() returns a random orthogonal matrix.
#
#  Properties:
#
#    The inverse of A is equal to A'.
#
#    A is orthogonal: A * A'  = A' * A = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    Columns and rows of A have unit Euclidean norm.
#
#    Distinct pairs of columns of A are orthogonal.
#
#    Distinct pairs of rows of A are orthogonal.
#
#    The L2 vector norm of A*x = the L2 vector norm of x for any vector x.
#
#    The L2 matrix norm of A*B = the L2 matrix norm of B for any matrix B.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    All the eigenvalues of A have modulus 1.
#
#    All singular values of A are 1.
#
#    All entries of A are between -1 and 1.
#
#  Discussion:
#
#    Thanks to Eugene Petrov, B I Stepanov Institute of Physics,
#    National Academy of Sciences of Belarus, for convincingly
#    pointing out the severe deficiencies of an earlier version of
#    this routine.
#
#    Essentially, the computation involves saving the Q factor of the
#    QR factorization of a matrix whose entries are normally distributed.
#    However, it is only necessary to generate this matrix a column at
#    a time, since it can be shown that when it comes time to annihilate
#    the subdiagonal elements of column K, these (transformed) elements of
#    column K are still normally distributed random values.  Hence, there
#    is no need to generate them at the beginning of the process and
#    transform them K-1 times.
#
#    For computational efficiency, the individual Householder transformations
#    could be saved, as recommended in the reference, instead of being
#    accumulated into an explicit matrix format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pete Stewart,
#    Efficient Generation of Random Orthogonal Matrices With an Application
#    to Condition Estimators,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 3, June 1980, pages 403-409.
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng_key = default_rng ( key )
#
#  Start with A = the identity matrix.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
#
#  Now behave as though we were computing the QR factorization of
#  some other random matrix.  Generate the N elements of the first column,
#  compute the Householder matrix H1 that annihilates the subdiagonal elements,
#  and set A := A * H1' = A * H.
#
#  On the second step, generate the lower N-1 elements of the second column,
#  compute the Householder matrix H2 that annihilates them,
#  and set A := A * H2' = A * H2 = H1 * H2.
#
#  On the N-1 step, generate the lower 2 elements of column N-1,
#  compute the Householder matrix HN-1 that annihilates them, and
#  and set A := A * H(N-1)' = A * H(N-1) = H1 * H2 * ... * H(N-1).
#  This is our random orthogonal matrix.
#
  x_col = np.zeros ( n )
 
  for j in range ( 0, n - 1 ):

    for i in range ( 0, j ):
      x_col[i] = 0.0

    for i in range ( j, n ):
      x_col[i] = rng_key.standard_normal ( )
#
#  Compute the vector V that defines a Householder transformation matrix
#  H(V) that annihilates the subdiagonal elements of X.
#
    v = r8vec_house_column ( n, x_col, j )
#
#  Postmultiply the matrix A by H'(V) = H(V).
#
    a = r8ge_house_axh ( n, a, v )

  return a

def r8ge_orth_random_test ( ):

#*****************************************************************************80
#
## r8ge_orth_random_test() tests r8ge_orth_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_orth_random_test():' )
  print ( '  r8ge_orth_random computes a random orthogonal matrix.' )

  m = 5
  n = m
  key = 123456789

  a = r8ge_orth_random ( n, key )

  r8ge_print ( m, n, a, '  orth_random matrix:' )

  return

def r8ge_spd_random ( n, key ):

#*****************************************************************************80
#
## r8ge_spd_random() returns a random symmetric positive definite matrix.
#
#  Discussion:
#
#    The matrix returned will have eigenvalues in the range [0,1].
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is positive definite: 0 < x'*A*x for nonzero x.
#
#    The eigenvalues of A will be real.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng_key = default_rng ( key )
#
#  Get a random set of eigenvalues.
#
  lam = rng_key.random ( size = n )
#
#  Get a random orthogonal matrix Q.
#
  q = r8ge_orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * lam[k] * q[j,k]

  return a

def r8ge_spd_random_test ( ):

#*****************************************************************************80
#
## r8ge_spd_random_test() tests r8ge_spd_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8ge_spd_random_test():' )
  print ( '  r8ge_spd_random computes the spd_random matrix.' )

  n = 5
  key = 123456789
  a = r8ge_spd_random ( n, key )

  r8ge_print ( n, n, a, '  spd_random matrix:' )

  return

def r8ge_plu ( m, n, a ):

#*****************************************************************************80
#
## r8ge_plu() produces the PLU factors of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    The PLU factors of the M by N matrix A are:
#
#      P, an M by M permutation matrix P,
#      L, an M by M unit lower triangular matrix,
#      U, an M by N upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the R8GE matrix.
#
#  Output:
#
#    real P(M,M), the M by M permutation factor.
#
#    real L(M,M), the M by M unit lower triangular factor.
#
#    real U(M,N), the M by N upper triangular factor.
#
  l = r8ge_identity ( m, m )
  p = r8ge_identity ( m, m )
  u = r8ge_copy ( m, n, a )
#
#  On step J, find the pivot row and the pivot value.
#
  for j in range ( 0, min ( m - 1, n ) ):

    pivot_value = 0.0
    pivot_row = -1

    for i in range ( j, m ):

      if ( pivot_value < abs ( u[i,j] ) ):
        pivot_value = abs ( u[i,j] )
        pivot_row = i
#
#  If the pivot row is nonzero, swap rows J and PIVOT_ROW.
#
    if ( pivot_row != -1 ):

      for k in range ( 0, n ):
        t = u[j,k]
        u[j,k] = u[pivot_row,k]
        u[pivot_row,k] = t

      for k in range ( 0, m ):
        t = l[j,k]
        l[j,k] = l[pivot_row,k]
        l[pivot_row,k] = t

      for k in range ( 0, m ):
        t = l[k,j]
        l[k,j] = l[k,pivot_row]
        l[k,pivot_row] = t

      for k in range ( 0, m ):
        t = p[k,j]
        p[k,j] = p[k,pivot_row]
        p[k,pivot_row] = t
#
#  Zero out the entries in column J, from row J+1 to M.
#
      for i in range ( j + 1, m ):

        if ( u[i,j] != 0.0 ):

          l[i,j] = u[i,j] / u[j,j]
          u[i,j] = 0.0
          for k in range ( j + 1, n ):
            u[i,k] = u[i,k] - l[i,j] * u[j,k]

  return p, l, u

def r8ge_plu_test ( ):

#*****************************************************************************80
#
## r8ge_plu_test() tests r8ge_plu().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4
  
  print ( '' )
  print ( 'r8ge_plu_test():' )
  print ( '  r8ge_plu returns the PLU factors of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = r8ge_random ( m, n )

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Compute the PLU factors.
#
  p, l, u = r8ge_plu ( m, n, a )

  r8ge_print ( m, m, p, '  Factor P:' )

  r8ge_print ( m, m, l, '  Factor L:' )

  r8ge_print ( m, n, u, '  Factor U:' )

  lu = r8ge_mm ( m, m, n, l, u )
  plu = r8ge_mm ( m, m, n, p, lu )
        
  r8ge_print ( m, n, plu, '  Product P*L*U:')

  return

def r8ge_poly ( n, a ):

#*****************************************************************************80
#
## r8ge_poly() computes the characteristic polynomial of a R8GE matrix.
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
#    07 February 2016
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
#    real A(N,N), the R8GE matrix.
#
#  Output:
#
#    real P(1:N+1), the coefficients of the characteristic
#    polynomial of A.  P(I+1) contains the coefficient of X**I.
#
  import numpy as np
#
#  Initialize WORK1 to the identity matrix.
#
  work1 = r8ge_identity ( n, n )

  p = np.zeros ( n + 1 )
  p[n] = 1.0

  for order in range ( n - 1, -1, -1 ):
#
#  Work2 = A * WORK1.
#
    work2 = r8ge_mm ( n, n, n, a, work1 )
#
#  Take the trace.
#
    trace = 0.0
    for i in range ( 0, n ):
      trace = trace + work2[i,i]
#
#  P(ORDER) = -Trace ( WORK2 ) / ( N - ORDER )
#
    p[order] = - trace / ( n - order )
#
#  WORK1 := WORK2 + P(ORDER) * Identity.
#
    work1 = r8ge_copy ( n, n, work2 )

    for i in range ( 0, n ):
      work1[i,i] = work1[i,i] + p[order]

  return p

def r8ge_poly_test ( ):

#*****************************************************************************80
#
## r8ge_poly_test() tests r8ge_poly().
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
  import numpy as np

  n = 12

  print ( '' )
  print ( 'r8ge_poly_test():' )
  print ( '  r8ge_poly computes the characteristic polynomial of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  p_true = np.array ( [ \
         1.0,    -23.0,    231.0,  -1330.0,   4845.0, \
    -11628.0,  18564.0, -19448.0,  12870.0,  -5005.0, \
      1001.0,    -78.0,      1.0 ] )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( min ( i, j ) + 1 )
#
#  Get the characteristic polynomial.
#
  p = r8ge_poly ( n, a )
#
#  Compare.
#
  r8vec2_print_some ( n+1, p, p_true, 10, 'I, P(I), True P(I)' )

  return

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ge_print() prints an R8GE matrix.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_test ( ):

#*****************************************************************************80
#
## r8ge_print_test() tests r8ge_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_test():' )
  print ( '  r8ge_print prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8GE:' )

  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ge_print_some() prints out a portion of an R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row', end = '' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## r8ge_print_some_test() tests r8ge_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_some_test():' )
  print ( '  r8ge_print_some prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Rows 0:2, Cols 3:5:' )

  return

def r8ge_random ( m, n, rng ):

#*****************************************************************************80
#
## r8ge_random() randomizes a R8GE matrix.
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
#    rng: the current random number generator.
#
#  Output:
#
#    real A(M,N), the R8GE matrix.
#
  import numpy as np

  r = rng.random ( size = [ m, n ] )

  return r

def r8ge_random_test ( rng ):

#*****************************************************************************80
#
## r8ge_random_test() tests r8ge_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2016
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

  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_random_test():' )
  print ( '  r8ge_random computes a random R8GE.' )
  print ( '' )
  print ( '  0 <= X <= 1' )

  v = r8ge_random ( m, n, rng )

  r8ge_print ( m, n, v, '  Random R8GE:' )

  return

def r8ge_random_ab ( m, n, a, b, rng ):

#*****************************************************************************80
#
## r8ge_random_ab() returns a scaled pseudorandom R8GE.
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
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A, B, the range of the pseudorandom values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
  import numpy as np

  r = a + ( b - a ) * rng.random ( size = [ m, n ] )

  return r

def r8ge_random_ab_test ( rng ):

#*****************************************************************************80
#
## r8ge_random_ab_test() tests r8ge_random_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2015
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

  m = 5
  n = 4
  a = -1.0
  b = +5.0

  print ( '' )
  print ( 'r8ge_random_ab_test():' )
  print ( '  r8ge_random_ab computes a random R8GE.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )

  v = r8ge_random_ab ( m, n, a, b, rng )

  r8ge_print ( m, n, v, '  Random R8GE:' )

  return

def r8ge_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## r8ge_res() computes the residual vector for an R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
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
#    integer M, N, the number of rows and columns of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the original, UNFACTORED R8GE matrix.
#
#    real X(N), the estimated solution.
#
#    real B(M), the right hand side vector.
#
#  Output:
#
#    real R(M), the residual vector, b - A * x.
#
  import numpy as np

  r = np.zeros ( m )

  for i in range ( 0, m ):
    r[i] = b[i]
    for j in range ( 0, n ):
      r[i] = r[i] - a[i,j] * x[j]

  return r

def r8ge_res_test ( ):

#*****************************************************************************80
#
## r8ge_res_test() tests r8ge_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8ge_res_test():' )
  print ( '  r8ge_res computes b-A*x, where A is an R8GE matrix.' )
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

    a = r8ge_random ( m, n )
    x = r8vec_indicator1 ( n )
    b = r8ge_mv ( m, n, a, x )
    r = r8ge_res ( m, n, a, x, b )
    r8vec_print ( m, r, '  Residual A*x-b:' )

  return

def r8ge_sl ( n, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## r8ge_sl() solves a system factored by r8ge_fa.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_sl is a simplified version of the LINPACK routine R8GESL.
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
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa.
#
#    integer PIVOT(N), the pivot vector from r8ge_fa.
#
#    real B(N), the right hand side vector.
#
#    integer JOB, specifies the operation.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Solve A * x = b.
#
  if ( job == 0 ):
#
#  Solve PL * Y = B.
#
    for k in range ( 0, n - 1 ):

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

      for i in range ( k + 1, n ):
        x[i] = x[i] + a_lu[i,k] * x[k]
#
#  Solve U * X = Y.
#
    for k in range ( n - 1, -1, -1 ):
      x[k] = x[k] / a_lu[k,k]
      for i in range ( 0, k ):
        x[i] = x[i] - a_lu[i,k] * x[k]
#
#  Solve A' * X = B.
#
  else:
#
#  Solve U' * Y = B.
#
    for k in range ( 0, n ):
      for i in range ( 0, k ):
        x[k] = x[k] - x[i] * a_lu[i,k]
      x[k] = x[k] / a_lu[k,k]
#
#  Solve ( PL )' * X = Y.
#
    for k in range ( n - 2, -1, -1 ):
      for i in range ( k + 1, n ):
        x[k] = x[k] + x[i] * a_lu[i,k]

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

  return x

def r8ge_sl_test ( ):

#*****************************************************************************80
#
## r8ge_sl_test() tests r8ge_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8ge_sl_test():' )
  print ( '  r8ge_sl solves a linear system that was factored' )
  print ( '  by r8ge_fa.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_sl_test - Fatal error!' )
    print ( '  r8ge_fa declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = np.ones ( n )
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 1
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_sl_it ( n, a, a_lu, pivot, b, job, x ):

#*****************************************************************************80
#
## r8ge_sl_it() applies one step of iterative refinement following r8ge_sl.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that:
#
#    * the original matrix A has been factored by r8ge_fa
#    * the linear system A * x = b has been solved once by r8ge_sl.
#
#    (Actually, it is not necessary to solve the system once using r8ge_sl.
#    You may simply supply the initial estimated solution X = 0.)
#
#    Each time this routine is called, it will compute the residual in
#    the linear system, apply one step of iterative refinement, and
#    add the computed correction to the current solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
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
#    real A(N,N), the original, UNFACTORED R8GE matrix.
#
#    real A_LU(N,N), the LU factors from r8ge_fa.
#
#    integer PIVOT(N), the pivot vector from r8ge_fa.
#
#    real B(N), the right hand side vector.
#
#    integer JOB, specifies the operation.
#    0, solve A*X=B.
#    nonzero, solve A'*X=B.
#
#    real X(N), an estimate of the solution of A * x = b.
#
#  Output:
#
#    real X(N), an improved estimate of the solution.
#
#    real DX(N), contains the correction terms added to X.
#

#
#  Compute the residual vector.
#
  r = r8ge_res ( n, n, a, x, b )
#
#  Solve A * dx = r
#
  dx = r8ge_sl ( n, a_lu, pivot, r, job )
#
#  Add dx to x.
#
  for i in range ( 0, n ):
    x[i] = x[i] + dx[i]

  return x, dx

def r8ge_sl_it_test ( ):

#*****************************************************************************80
#
## r8ge_sl_it_test() tests r8ge_sl_it().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6

  print ( '' )
  print ( 'r8ge_sl_it_test():' )
  print ( '  r8ge_sl_it applies one step of iterative' )
  print ( '  refinement to a r8ge_sl solution.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the coefficient matrix.
#
  a = r8ge_hilbert_inverse ( n )
#
#  Set the right hand side b.
#
  b = np.zeros ( n )
  b[n-1] = 1.0
#
#  Compute the factored coefficient matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_sl_it_test - Fatal error!' )
    print ( '  r8ge_fa declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return
#
#  Solve the system.
#
  job = 1
  x = r8ge_sl ( n, a_lu, pivot, b, job )
#
#  Compute and print the residual.
#
  r = r8ge_res ( n, n, a, x, b )

  r8vec2_print_some ( n, x, r, 10, '  i, x, b-A*x' )
#
#  Take a few steps of iterative refinement.
#
  for j in range ( 1, 6 ):

    print ( '' )
    print ( 'Iterative refinement step %d' % ( j ) )
#
#  Improve the solution.
#
    x_new, r = r8ge_sl_it ( n, a, a_lu, pivot, b, job, x )

    r8vec_print_some ( n, r, 10, '  I, DX:' )
#
#  Compute and print the residual.
#
    r = r8ge_res ( n, n, a, x_new, b )

    r8vec2_print_some ( n, x_new, r, 10, '  i, x, b-A*x' )

    x = x_new.copy ( )

  return

def r8ge_to_r8gb ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## r8ge_to_r8gb() copies a R8GE matrix to a R8GB matrix.
#
#  Discussion:
#
#    It usually doesn't make sense to try to store a general matrix
#    in a band matrix format.  You can always do it, but it will take
#    more space, unless the general matrix is actually banded.
#
#    The purpose of this routine is to allow a user to set up a
#    banded matrix in the easy-to-use general format, and have this
#    routine take care of the compression of the data into general
#    format.  All the user has to do is specify the bandwidths.
#
#    Note that this routine "believes" what the user says about the
#    bandwidth.  It will assume that all entries in the general matrix
#    outside of the bandwidth are zero.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    The R8GB storage format is for an M by N banded matrix, with lower
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML
#    extra superdiagonals, which may be required to store nonzero entries
#    generated during Gaussian elimination.
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine will copy nonzero
#    values it finds in these extra bands, so that both unfactored
#    and factored matrices can be handled.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer M, the number of rows of the matrices.
#    M must be positive.
#
#    integer N, the number of columns of the matrices.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths of the matrix.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(M,N), the R8GE matrix.
#
#  Output:
#
#    real B(2*ML+MU+1,N), the R8GB matrix.
#
  import numpy as np

  b = np.zeros ( [ 2*ml+mu+1, n ] )

  for i in range ( 1, m + 1 ):
    jlo = max ( i - ml, 1 )
    jhi = min ( i + mu, n )
    for j in range ( jlo, jhi + 1 ):
      b[ml+mu+i-j,j-1] = a[i-1,j-1]

  return b

def r8ge_to_r8gb_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8gb_test() tests r8ge_to_r8gb().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  ml = 2
  mu = 1

  print ( '' )
  print ( 'r8ge_to_r8gb_test():' )
  print ( '  r8ge_to_r8gb converts an R8GE matrix to R8GB format.' )
  print ( '' )
  print ( '  Matrix order M = %d, N = %d' % ( m, n ) )
  print ( '  R8GB bands ML = %d, MU = %d' % ( ml, mu ) )

  a = r8ge_random ( m, n )

  r8ge_print ( m, n, a, '  The random R8GE matrix:' )
 
  b = r8ge_to_r8gb ( m, n, ml, mu, a )

  r8gb_print ( m, n, ml, mu, b, '  The R8GB matrix:' )

  return

def r8ge_to_r8lt ( m, n, a_ge ):

#*****************************************************************************80
#
## r8ge_to_r8lt() copies an R8GE matrix to an R8LT matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_GE(M,N), the R8GE matrix.
#
#  Output:
#
#    real A_LT(M,N), the R8LT matrix.
#
  import numpy as np

  a_lt = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( j, m ):
      a_lt[i,j] = a_ge[i,j]

  return a_lt

def r8ge_to_r8lt_test ( rng ):

#*****************************************************************************80
#
## r8ge_to_r8lt_test() tests r8ge_to_r8lt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2015
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
  n = 4

  print ( '' )
  print ( 'r8ge_to_r8lt_test():' )
  print ( '  r8ge_to_r8lt() converts an R8GE matrix to R8LT format.' )

  a_ge = r8ge_random ( m, n, rng )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_lt = r8ge_to_r8lt ( m, n, a_ge )

  r8lt_print ( m, n, a_lt, '  The R8LT matrix:' )

  return

def r8ge_to_r8po ( n, a ):

#*****************************************************************************80
#
## r8ge_to_r8po() copies an R8GE matrix to an R8PO matrix.
#
#  Discussion:
#
#    The R8PO format assumes the matrix is square and symmetric; it is also 
#    typically assumed that the matrix is positive definite.  These are not
#    required here.  The copied R8PO matrix simply zeros out the lower triangle
#    of the R8GE matrix.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8PO storage format is used for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_fa, or inverted by R8PO_inverse.  For clarity, the lower triangle
#    is set to zero.
#
#    R8PO storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8GE matrix.
#
#  Output:
#
#    real B(N,N), the R8PO matrix.
#
  import numpy as np

  b = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      b[i,j] = a[i,j]

  return b

def r8ge_to_r8po_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8po_test() tests r8ge_to_r8po().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8ge_to_r8po_test():' )
  print ( '  r8ge_to_r8po converts an R8GE matrix to R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ge_random ( n, n )

  r8ge_print ( n, n, a, '  The random R8GE matrix:' )
 
  b = r8ge_to_r8po ( n, a )

  r8po_print ( n, b, '  The R8PO matrix:' )

  return

def r8ge_to_r8ut ( m, n, a_ge ):

#*****************************************************************************80
#
## r8ge_to_r8ut() copies an R8GE matrix to an R8UT matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_GE(M,N), the R8GE matrix.
#
#  Output:
#
#    real A_UT(M,N), the R8UT matrix.
#
  import numpy as np

  a_ut = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a_ut[i,j] = a_ge[i,j]

  return a_ut

def r8ge_to_r8ut_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8ut_test() tests r8ge_to_r8ut().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_to_r8ut_test():' )
  print ( '  r8ge_to_r8ut converts an R8GE matrix to R8UT format.' )

  a_ge = r8ge_random ( m, n )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_ut = r8ge_to_r8ut ( m, n, a_ge )

  r8ut_print ( m, n, a_ut, '  The R8UT matrix:' )

  return

def r8ge_to_r8vec ( m, n, a ):

#*****************************************************************************80
#
## r8ge_to_r8vec() copies an R8GE matrix to an R8VEC.
#
#  Discussion:
#
#    In C++ and FORTRAN, this routine is not really needed.  In MATLAB,
#    a data item carries its dimensionality implicitly, and so cannot be
#    regarded sometimes as a vector and sometimes as an array.
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
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M,N), the array to be copied.
#
#  Output:
#
#    real X(M*N), the vector.
#
  import numpy as np

  x = np.zeros ( m * n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      x[k] = a[i,j]
      k = k + 1

  return x

def r8ge_to_r8vec_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8vec_test() tests r8ge_to_r8vec().
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
  m = 4
  n = 3

  print ( '' )
  print ( 'r8ge_to_r8vec_test():' )
  print ( '  r8ge_to_r8vec converts an R8GE matrix to an R8VEC vector.' )

  a_r8ge = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a_r8ge, '  R8GE matrix:' )

  a_r8vec = r8ge_to_r8vec ( m, n, a_r8ge )

  r8vec_print ( m * n, a_r8vec, '  Corresponding R8VEC vector:' )

  return

def r8ge_to_r8vm ( m, n, a_ge ):

#*****************************************************************************80
#
## r8ge_to_r8vm() copies an R8GE matrix to an R8VM matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_GE(M,N), the R8GE matrix.
#
#  Output:
#
#    real A_VM(N), the R8VM matrix.
#
  import numpy as np

  a_vm = np.zeros ( n )

  for j in range ( 0, n ):
    a_vm[j] = a_ge[1,j]

  return a_vm

def r8ge_to_r8vm_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8vm_test() tests r8ge_to_r8vm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_to_r8vm_test():' )
  print ( '  r8ge_to_r8vm converts an R8GE matrix to R8VM format.' )

  a_ge = r8ge_random ( m, n )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_vm = r8ge_to_r8vm ( m, n, a_ge )

  r8vm_print ( m, n, a_vm, '  The R8VM matrix:' )

  return

def r8ge_transpose ( m, n, a ):

#*****************************************************************************80
#
## r8ge_transpose() makes a transposed copy of an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix to be copied.
#
#  Output:
#
#    real B(N,M), a copy of the transposed matrix.
#
  import numpy as np

  b = r8ge_zeros ( n, m )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j,i] = a[i,j]

  return b

def r8ge_transpose_test ( ):

#*****************************************************************************80
#
## r8ge_transpose_test() tests r8ge_transpose().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_transpose_test():' )
  print ( '  r8ge_transpose makes a transposed copy of an R8GE matrix.' )

  a = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a, '  Indicator matrix A:' )

  b = r8ge_transpose ( m, n, a )

  r8ge_print ( n, m, b, '  B = A\':' )

  return

def r8ge_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ge_transpose_print() prints an R8GE matrix, transposed.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8ge_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_transpose_print_test ( ):

#*****************************************************************************80
#
## r8ge_transpose_print_test() tests r8ge_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_transpose_print_test():' )
  print ( '  r8ge_transpose_print prints the transpose of an R8GE matrix.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8ge_transpose_print ( m, n, v, '  Here is an R8GE matrix, transposed:' )

  return

def r8ge_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ge_transpose_print_some() prints a portion of an R8GE matrix, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col', end = '' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ge_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8ge_transpose_print_some_test() tests r8ge_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_transpose_print_some_test():' )
  print ( '  r8ge_transpose_print_some prints some of an R8GE matrix, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8ge_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8GE matrix, rows 0:2, cols 3:5:' )

  return

def r8ge_trf ( m, n, a ):

#*****************************************************************************80
#
## r8ge_trf() performs a LAPACK-style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_trf is a standalone version of the LAPACK routine R8GETRF.
#
#    The factorization uses partial pivoting with row interchanges,
#    and has the form
#      A = P * L * U
#    where P is a permutation matrix, L is lower triangular with unit
#    diagonal elements (lower trapezoidal if N < M), and U is upper
#    triangular (upper trapezoidal if M < N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#  Input:
#
#    integer M, the number of rows of the matrix A.  0 <= M.
#
#    integer N, the number of columns of the matrix A.  0 <= N.
#
#    real A(M,N), the M by N matrix to be factored.
#
#  Output:
#
#    real A_LU(M,N), the factors L and U from the factorization
#    A = P*L*U the unit diagonal elements of L are not stored.
#
#    integer PIVOT(min(M,N)), the pivot indices
#    for 1 <= I <= min(M,N), row i of the matrix was interchanged with
#    row PIVOT(I).
#
#    integer INFO.
#    = 0: successful computation.
#    < 0: if INFO = -K, the K-th argument had an illegal value
#    > 0: if INFO = K, U(K,K) is exactly zero. The factorization
#         has been completed, but the factor U is exactly
#         singular, and division by zero will occur if it is used
#         to solve a system of equations.
#
  import numpy as np

  a_lu = r8ge_copy ( m, n, a )

  pivot = np.zeros ( n, dtype = np.int32 )
#
#  Test the input parameters.
#
  info = 0

  if ( m < 0 ):
    info = -1
    return a_lu, pivot, info

  if ( n < 0 ):
    info = -2
    return a_lu, pivot, info

  if ( m == 0 or n == 0 ):
    return a_lu, pivot, info

  for j in range ( 0, min ( m, n ) ):
#
#  Find the pivot.
#
    t = abs ( a_lu[j,j] )
    jp = j
    for i in range ( j + 1, m ):
      if ( t < abs ( a_lu[i,j] ) ):
        t = abs ( a_lu[i,j] )
        jp = i

    pivot[j] = jp
#
#  Apply the interchange to columns 1:N.
#  Compute elements J+1:M of the J-th column.
#
    if ( a_lu[jp,j] != 0.0 ):

      if ( jp != j ):
        for jj in range ( 0, n ):
          t           = a_lu[j,jj]
          a_lu[j,jj]  = a_lu[jp,jj]
          a_lu[jp,jj] = t

      if ( j < m - 1 ):
        for i in range ( j + 1, m ):
          a_lu[i,j] = a_lu[i,j] / a_lu[j,j]

    elif ( info == 0 ):

      info = j
#
#  Update the trailing submatrix.
#
    if ( j < min ( m, n ) - 1 ):

      for ii in range ( j + 1, m ):
        for k in range ( j + 1, n ):
          a_lu[ii,k] = a_lu[ii,k] - a_lu[ii,j] * a_lu[j,k]

  return a_lu, pivot, info

def r8ge_trf_test ( ):

#*****************************************************************************80
#
## r8ge_trf_test() tests r8ge_trf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  m = n
  nrhs = 1

  print ( '' )
  print ( 'r8ge_trf_test():' )
  print ( '  r8ge_trf computes the LU factors of an R8GE matrix,' )
  print ( '  so that r8ge_trs can solve the factored system.' )
  print ( '' )
  print ( '  Number of matrix rows M = %d' % ( m ) )
  print ( '  Number of matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( i == j - 1 ):
        a[i,j] = - 1.0
      elif ( i == j + 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  a_lu, pivot, info = r8ge_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_trf_test - Fatal error!' )
    print ( '  r8ge_trf declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'N', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_trf_test - Fatal error!' )
    print ( '  r8ge_trs returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution:' )

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'T', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_trf_test - Fatal error!' )
    print ( '  r8ge_trs returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8ge_trs ( n, nrhs, trans, a_lu, pivot, b ):

#*****************************************************************************80
#
## r8ge_trs() solves a system of linear equations factored by r8ge_trf.
#
#  Discussion:
#
#    Note that in MATLAB we will have peculiar and maddening problems
#    if our input data B is actually a vector in fact, if B is a vector,
#    we must do something like call r8vec_to_r8ge in order to make it
#    look like a 2D array to MATLAB.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_trs is a standalone version of the LAPACK routine R8GETRS.
#
#    r8ge_trs solves a system of linear equations
#      A * x = b  or  A' * X = B
#    with a general N by N matrix A using the PLU factorization computed
#    by r8ge_trf.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#  Input:
#
#    integer N, the order of the matrix A.  0 <= N.
#
#    integer NRHS, the number of right hand sides.  0 <= NRHS.
#
#    character TRANS, specifies the form of the system of equations:
#    'N':  A * x = b  (No transpose)
#    'T':  A'* X = B  (Transpose)
#    'C':  A'* X = B  (Conjugate transpose = Transpose)
#
#    real A_LU(N,N), the LU factors from r8ge_trf.
#
#    integer PIVOT(N), the pivot indices from r8ge_trf.
#
#    real B(N,NRHS), the right hand side matrix B.
#
#  Output:
#
#    real X(N,NRHS), the solution matrix X.
#
#    integer INFO
#    = 0:  successful computation.
#    < 0:  if INFO = -I, the I-th argument had an illegal value.
#
  x = r8ge_copy ( n, nrhs, b )

  info = 0

  if ( trans != 'n' and trans != 'N' and trans != 't' and trans != 'T' and \
       trans != 'c' and trans != 'C' ):
    info = -1
    return x, info
  elif ( n < 0 ):
    info = -2
    return x, info
  elif ( nrhs < 0 ):
    info = -3
    return x, info

  if ( n == 0 or nrhs == 0 ):
    return x, info

  if ( trans == 'n' or trans == 'N' ):
#
#  Apply row interchanges to the right hand sides.
#
    for i in range ( 0, n ):
      if ( pivot[i] != i ):
        for k in range ( 0, nrhs ):
          t             = x[i,k]
          x[i,k]        = x[pivot[i],k]
          x[pivot[i],k] = t
#
#  Solve L * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( 0, n - 1 ):
        for i in range ( j + 1, n ):
          x[i,k] = x[i,k] - a_lu[i,j] * x[j,k]
#
#  Solve U * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( n - 1, -1, -1 ):
        x[j,k] = x[j,k] / a_lu[j,j]

  else:
#
#  Solve U' * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( 0, n ):
        x[j,k] = x[j,k] / a_lu[j,j]
        for i in range ( j + 1, n ):
          x[i,k] = x[i,k] - a_lu[j,i] * x[j,k]
#
#  Solve L' * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( n - 1, 0, -1 ):
        for i in range ( 0, j ):
          x[i,k] = x[i,k] - a_lu[j,i] * x[j,k]
#
#  Apply row interchanges to the solution vectors.
#
    for i in range ( n - 1, -1, -1 ):
      if ( pivot[i] != i ):
        for k in range ( 0, nrhs ):
          t             = x[i,k]
          x[i,k]        = x[pivot[i],k]
          x[pivot[i],k] = t

  return x, info

def r8ge_trs_test ( ):

#*****************************************************************************80
#
## r8ge_trs_test() tests r8ge_trs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  m = n
  nrhs = 1

  print ( '' )
  print ( 'r8ge_trs_test():' )
  print ( '  r8ge_trs solves a linear system' )
  print ( '  that has been factored by r8ge_trf.' )
  print ( '' )
  print ( '  Number of matrix rows M = %d' % ( m ) )
  print ( '  Number of matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( i == j - 1 ):
        a[i,j] = - 1.0
      elif ( i == j + 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  a_lu, pivot, info = r8ge_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_trs_test - Fatal error!' )
    print ( '  r8ge_trf declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'N', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_trs_test - Fatal error!' )
    print ( '  r8ge_trs returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution:' )

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'T', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_trs_test - Fatal error!' )
    print ( '  r8ge_trs returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8ge_zeros ( m, n ):

#*****************************************************************************80
#
## r8ge_zeros() zeroes an R8GE matrix.
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
#    01 August 2015
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
#  Output:
#
#    real A(M,N), the zeroed out matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ge_zeros_test ( ):

#*****************************************************************************80
#
## r8ge_zeros_test() tests r8ge_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_zeros_test():' )
  print ( '  r8ge_zeros zeros out space for a general matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ge_zeros ( m, n )

  r8ge_print ( m, n, a, '  Matrix A:' )

  return

def r8vec_to_r8ge ( m, n, x ):

#*****************************************************************************80
#
## r8vec_to_r8ge() copies an R8VEC into a R8GE matrix.
#
#  Discussion:
#
#    In C++  and FORTRAN, this routine is not really needed.  In MATLAB,
#    a data item carries its dimensionality implicitly, and so cannot be
#    regarded sometimes as a vector and sometimes as an array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M*N), the vector to be copied into the array.
#
#  Output:
#
#    real A(M,N), the array.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  
  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = x[k]
      k = k + 1

  return a

def r8vec_house_column ( n, a_vec, k ):

#*****************************************************************************80
#
## r8vec_house_column() defines a Householder premultiplier that "packs" a column.
#
#  Discussion:
#
#    The routine returns a vector V that defines a Householder
#    premultiplier matrix H(V) that zeros out the subdiagonal entries of
#    column K of the matrix A.
#
#       H(V) = I - 2 * v * v'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix A.
#
#    real A_VEC(N), a row or column of the matrix A.
#
#    integer K, the "special" entry in A_VEC.
#    The Householder matrix will zero out the entries after this.
#
#  Output:
#
#    real V(N), a vector of unit L2 norm which defines an
#    orthogonal Householder premultiplier matrix H with the property
#    that the K-th column of H*A is zero below the diagonal.
#
  import numpy as np

  v = np.zeros ( n )

  if ( k < 0 or n - 1 <= k ):
    return v

  s = 0.0
  for i in range ( k, n ):
    s = s + a_vec[i] ** 2
  s = np.sqrt ( s )

  if ( s == 0.0 ):
    return v

  if ( a_vec[k] < 0.0 ):
    v[k] = a_vec[k] - abs ( s )
  else:
    v[k] = a_vec[k] + abs ( s )

  for i in range ( k + 1, n ):
    v[i] = a_vec[i]

  s = 0.0
  for i in range ( k, n ):
    s = s + v[i] ** 2
  s = np.sqrt ( s )

  for i in range ( k, n ):
    v[i] = v[i] / s

  return v

def r8vec_house_column_test ( ):

#*****************************************************************************80
#
## r8vec_house_column_test() tests r8vec_house_column().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_house_column_test():' )
  print ( '  r8vec_house_column returns the compact form of' )
  print ( '  a Householder matrix that "packs" a column' )
  print ( '  of a matrix.' )
#
#  Get a random matrix.
#
  n = 4
  r8_lo = 0.0
  r8_hi = 5.0

  a = r8ge_random_ab ( n, n, r8_lo, r8_hi )

  r8ge_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ( '' )
    print ( '  Working on column K = %d' % ( k ) )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8ge_house_form ( n, v )

    r8ge_print ( n, n, h, '  Householder matrix H:' )

    ha = r8ge_mm ( n, n, n, h, a )

    r8ge_print ( n, n, ha, '  Product H*A:' )
#
#  If we set A := HA, then we can successively convert A to upper
#  triangular form.
#
    a = ha

  return

def r8vec_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8vec_to_r8ge_test() tests r8vec_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 3

  print ( '' )
  print ( 'r8ge_to_r8vec_test():' )
  print ( '  r8ge_to_r8vec converts an R8GE matrix to an R8VEC vector.' )

  a_r8vec = r8vec_indicator1 ( m * n )
  
  r8vec_print ( m * n, a_r8vec, '  The R8VEC vector:' )

  a_r8ge = r8vec_to_r8ge ( m, n, a_r8vec )

  r8ge_print ( m, n, a_r8ge, '  Corresponding R8GE matrix:' )

  return
 
def r8lt_det ( n, a ):

#*****************************************************************************80
#
## r8lt_det() computes the determinant of an R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 August 2015
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
#    real A(N,N), the R8LT matrix.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for i in range ( 0, n ):
    det = det * a[i,i]

  return det

def r8lt_det_test ( rng ):

#*****************************************************************************80
#
## r8lt_det_test() tests r8lt_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 August 2015
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

  print ( '' )
  print ( 'r8lt_det_test():' )
  print ( '  r8lt_det() computes the determinant of an R8LT matrix.' )

  a = r8lt_random ( n, n, rng )

  r8lt_print ( n, n, a, '  The matrix A:' )
#
#  Compute the determinant.
#
  det = r8lt_det ( n, a )

  print ( '' )
  print ( '  Determinant is %g' % ( det ) )

  return

def r8lt_indicator ( m, n ):

#*****************************************************************************80
#
## r8lt_indicator() sets up a R8LT indicator matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#    M and N must be positive.
#
#  Output:
#
#    real A(M,N), the R8LT matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8lt_zeros ( m, n )
  for j in range ( 0, n ):
    for i in range ( j, m ):
      a[i,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8lt_indicator_test ( ):

#*****************************************************************************80
#
## r8lt_indicator_test() tests r8lt_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8lt_indicator_test():' )
  print ( '  r8lt_indicator sets up an indicator matrix in R8LT format' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = r8lt_indicator ( m, n )

  r8lt_print ( m, n, a, '  The indicator matrix:' )

  return

def r8lt_inverse ( n, a ):

#*****************************************************************************80
#
## r8lt_inverse() computes the inverse of a R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix to be inverted.
#
#  Output:
#
#    real A_INV(N,N), the inverse matrix.
#
  import numpy as np
#
#  Check.
#
  for i in range ( 0, n ):
    if ( a[i,i] == 0.0 ):
      print ( '' )
      print ( 'r8lt_inverse - Fatal error!' )
      print ( '  Zero diagonal element.' )
      raise Exception ( 'r8lt_inverse - Fatal error!' )

  a_inv = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_inv[i,j] = a[i,j]

  for j in range ( 0, n ):

    for i in range ( 0, n ):

      if ( i < j ):

        a_inv[i,j] = 0.0

      elif ( i == j ):

        a_inv[i,j] = 1.0 / a_inv[i,j]

      elif ( j < i ):

        t = 0.0
        for k in range ( j, i ):
          t = t + a_inv[i,k] * a_inv[k,j]
        a_inv[i,j] = - t / a_inv[i,i]

  return a_inv

def r8lt_inverse_test ( rng ):

#*****************************************************************************80
#
## r8lt_inverse_test() tests r8lt_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2015
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

  print ( '' )
  print ( 'r8lt_inverse_test():' )
  print ( '  r8lt_inverse() computes the inverse of an R8LT matrix.' )

  a = r8lt_random ( n, n, rng )

  r8lt_print ( n, n, a, '  The matrix A:' )
#
#  Compute the inverse matrix B.
#
  b = r8lt_inverse ( n, a )

  r8lt_print ( n, n, b, '  The inverse matrix B:' )
#
#  Check
#
  c = r8lt_mm ( n, a, b )

  r8lt_print ( n, n, c, '  The product A * B:' )

  return

def r8lt_mm ( n, a, b ):

#*****************************************************************************80
#
## r8lt_mm() multiplies two R8LT matrices.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2015
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
#    real A(N,N), B(N,N), the R8LT factor matrices.
#
#  Output:
#
#    real C(N,N), the R8LT product matrix.
#
  import numpy as np

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      for k in range ( j, i + 1 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]
 
  return c

def r8lt_mm_test ( ):

#*****************************************************************************80
#
## r8lt_mm_test() tests r8lt_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  print ( '' )
  print ( 'r8lt_mm_test():' )
  print ( '  r8lt_mm computes C = A * B for R8LT matrices.' )
 
  a = r8lt_zeros ( n, n )
 
  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      a[i,j] = 1.0

  r8lt_print ( n, n, a, '  The matrix A:' )

  c = r8lt_mm ( n, a, a )
  r8lt_print ( n, n, c, '  The product C = A * A' )

  return

def r8lt_mtm ( n, a, b ):

#*****************************************************************************80
#
## r8lt_mtm() computes C=A'*B for R8LT matrices.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2015
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
#    real A(N,N), B(N,N), the R8LT factor matrices.
#
#  Output:
#
#    real C(N,N), the R8LT product matrix.
#
  import numpy as np

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k = min ( i, j )
      for l in range ( k, n ):
        c[i,j] = c[i,j] + a[l,i] * b[l,j]
 
  return c

def r8lt_mtm_test ( ):

#*****************************************************************************80
#
## r8lt_mtm_test() tests r8lt_mtm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8lt_mtm_test():' )
  print ( '  r8lt_mtm computes C = A\' * B for R8LT matrices.' )
 
  a = r8lt_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      a[i,j] = 1.0

  r8lt_print ( n, n, a, '  The matrix A:' )

  c = r8lt_mtm ( n, a, a )

  r8ge_print ( n, n, c, '  The product C = A\' * A' )

  return

def r8lt_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8lt_mtv() multiplies a vector by a R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2015
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
#    real A(M,N), the R8LT matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( j, m ):
      b[j] = b[j] + x[i] * a[i,j]

  return b

def r8lt_mtv_test ( ):

#*****************************************************************************80
#
## r8lt_mtv_test() tests r8lt_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8lt_mtv_test():' )
  print ( '  r8lt_mtv computes A\'*x for an R8LT matrix.' )

  a = r8lt_indicator ( m, n )
  r8lt_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector x' )

  b = r8lt_mtv ( m, n, a, x )
  r8vec_print ( n, b, '  b = A\'*x:' )

  return

def r8lt_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8lt_mv() multiplies a R8LT matrix times a vector.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2015
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
#    real A(M,N), the R8LT matrix.
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
    for j in range ( 0, min ( i + 1, n ) ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8lt_mv_test ( ):

#*****************************************************************************80
#
## r8lt_mv_test() tests r8lt_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8lt_mv_test():' )
  print ( '  r8lt_mv computes A*x for an R8LT matrix.' )

  a = r8lt_indicator ( m, n )
  r8lt_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  The vector x' )

  b = r8lt_mv ( m, n, a, x )
  r8vec_print ( m, b, '  b = A*x:' )

  return

def r8lt_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8lt_print() prints an R8LT matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8lt_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8lt_print_test ( ):

#*****************************************************************************80
#
## r8lt_print_test() tests r8lt_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8lt_print_test():' )
  print ( '  r8lt_print prints an R8LT matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0,  0.0,  0.0,  0.0,  0.0,  0.0 ], 
    [ 21.0, 22.0,  0.0,  0.0,  0.0,  0.0 ], 
    [ 31.0, 32.0, 33.0,  0.0,  0.0,  0.0 ], 
    [ 41.0, 42.0, 43.0, 44.0,  0.0,  0.0 ] ], dtype = np.float64 )

  r8lt_print ( m, n, v, '  The R8LT matrix:' )

  return

def r8lt_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8lt_print_some() prints some of an R8LT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row', end = '' )

    i2lo = max ( ilo, 0 )
    i2lo = max ( i2lo, j2lo )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8lt_print_some_test ( ):

#*****************************************************************************80
#
## r8lt_print_some_test() tests r8lt_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8lt_print_some_test():' )
  print ( '  r8lt_print_some prints some of an R8LT matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0,  0.0,  0.0,  0.0,  0.0,  0.0 ], 
    [ 21.0, 22.0,  0.0,  0.0,  0.0,  0.0 ], 
    [ 31.0, 32.0, 33.0,  0.0,  0.0,  0.0 ], 
    [ 41.0, 42.0, 43.0, 44.0,  0.0,  0.0 ] ], dtype = np.float64 )

  r8lt_print_some ( m, n, v, 1, 1, 3, 2, '  Rows 1-3, Columns 1-2:' )

  return

def r8lt_random ( m, n, rng ):

#*****************************************************************************80
#
## r8lt_random() randomizes an R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#    M and N must be positive.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(M,N), the R8LT matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( j, m ):
      r = rng.random ( )
      a[i,j] = r

  return a

def r8lt_random_test ( rng ):

#*****************************************************************************80
#
## r8lt_random_test() tests r8lt_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2015
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
  n = 4

  print ( '' )
  print ( 'r8lt_random_test():' )
  print ( '  r8lt_random() randomizes an R8LT matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8lt_random ( m, n, rng )

  r8lt_print ( m, n, a, '  Matrix A:' )

  return

def r8lt_sl ( n, a, b ):

#*****************************************************************************80
#
## r8lt_sl() solves A*x=b, where A is an R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#    No factorization of the lower triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8LT matrix.
#
#    real B(N), the right hand side.
#    On the solution vector.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for j in range ( 0, n ):
    x[j] = b[j]

  for j in range ( 0, n ):
    x[j] = x[j] / a[j,j]
    for i in range ( j + 1, n ):
      x[i] = x[i] - a[i,j] * x[j]

  return x

def r8lt_sl_test ( ):

#*****************************************************************************80
#
## r8lt_sl_test() tests r8lt_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8lt_sl_test():' )
  print ( '  r8lt_sl() solves A*x=b for an R8LT matrix A.' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j <= i ):
        a[i,j] = j + 1
      else:
        a[i,j] = 0.0

  r8lt_print ( n, n, a, '  The R8LT matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8lt_mv ( n, n, a, x )
#
#  Solve the linear system.
#
  x = r8lt_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8lt_slt ( n, a, b ):

#*****************************************************************************80
#
## r8lt_sl() solves A'*x=b, where A is an R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#    No factorization of the lower triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8LT matrix.
#
#    real B(N), the right hand side.
#    On the solution vector.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]

  for i in range ( n - 1, -1, -1 ):
    x[i] = x[i] / a[i,i]
    for j in range ( 0, i ):
      x[j] = x[j] - a[i,j] * x[i]

  return x

def r8lt_slt_test ( ):

#*****************************************************************************80
#
## r8lt_slt_test() tests r8lt_slt().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8lt_slt_test():' )
  print ( '  r8lt_slt() solves A\'*x=b for an R8LT matrix A' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j <= i ):
        a[i,j] = j + 1
      else:
        a[i,j] = 0.0

  r8lt_print ( n, n, a, '  The R8LT matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8lt_mtv ( n, n, a, x )
#
#  Solve the linear system.
#
  x = r8lt_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8lt_to_r8ge ( m, n, a_lt ):

#*****************************************************************************80
#
## r8lt_to_r8ge() copies an R8LT matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
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
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_LT(M,N), the R8LT matrix.
#
#  Output:
#
#    real A_GE(N,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( j, m ):
      a_ge[i,j] = a_lt[i,j]

  return a_ge

def r8lt_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8lt_to_r8ge_test() tests r8lt_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8lt_to_r8ge_test():' )
  print ( '  r8lt_to_r8ge() converts an R8LT matrix to R8GE format.' )

  m = 4
  n = 6
  a_lt = np.array ( [ \
    [ 11.0,  0.0,  0.0,  0.0,  0.0,  0.0 ], 
    [ 21.0, 22.0,  0.0,  0.0,  0.0,  0.0 ], 
    [ 31.0, 32.0, 33.0,  0.0,  0.0,  0.0 ], 
    [ 41.0, 42.0, 43.0, 44.0,  0.0,  0.0 ] ], dtype = np.float64 )

  r8lt_print ( m, n, a_lt, '  The R8LT matrix:' )

  a_ge = r8lt_to_r8ge ( m, n, a_lt )

  r8ge_print ( m, n, a_ge, '  The R8GE matrix: ' )

  return

def r8lt_zeros ( m, n ):

#*****************************************************************************80
#
## r8lt_zeros() zeroes an R8LT matrix.
#
#  Discussion:
#
#    The R8LT storage format is used for an M by N lower triangular matrix,
#    and sets aside storage even for the entries that must be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2015
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
#    real A(M,N), the R8LT matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8lt_zeros_test ( ):

#*****************************************************************************80
#
## r8lt_zeros_test() tests r8lt_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8lt_zeros_test():' )
  print ( '  r8lt_zeros zeros out space for an R8LT matrix.' )

  a = r8lt_zeros ( m, n )

  r8lt_print ( m, n, a, '  Matrix A:' )

  return

def r8lt_test ( ):

#*****************************************************************************80
#
## r8lt_test() tests r8lt().
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
  print ( 'r8lt_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8lt().' )

  rng = default_rng ( )

  i4_log_10_test ( )

  r8ge_print_test ( )
  r8ge_print_some_test ( )
  r8ge_to_r8lt_test ( rng )

  r8lt_det_test ( rng )
  r8lt_indicator_test ( )
  r8lt_inverse_test ( rng )
  r8lt_mm_test ( )
  r8lt_mtm_test ( )
  r8lt_mtv_test ( )
  r8lt_mv_test ( )
  r8lt_print_test ( )
  r8lt_print_some_test ( )
  r8lt_random_test ( rng )
  r8lt_sl_test ( )
  r8lt_slt_test ( )
  r8lt_to_r8ge_test ( )
  r8lt_zeros_test ( )

  r8vec_indicator1_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8lt_test():' )
  print ( '  Normal end of execution.' )
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
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

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
    print ( '%6d  %12g' % ( i, a[i] ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  r8lt_test ( )
  timestamp ( )

