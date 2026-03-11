## /usr/bin/env python3
#
def lapack_test ( ):

#*****************************************************************************80
#
## lapack_test() tests lapack().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lapack_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lapack().' )

  dgbtrf_test ( )

  dgecon_test ( )
  dgeev_test ( )
  dgeqrf_test ( )
  dgesvd_test ( )
  dgetrf_test ( )
  dgetri_test ( )

  dgtsv_test ( )

  dormqr_test ( )

  dpbtrf_test ( )
  dpbtrs_test ( )

  dpotrf_test ( )
  dpotri_test ( )

  dsyev_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lapack_test():' )
  print ( '  Normal end of execution.' )

  return

def clement1_matrix ( n ):

#*****************************************************************************80
#
## clement1_matrix() returns the CLEMENT1 matrix.
#
#  Formula:
#
#    if ( J = I+1 )
#      A(I,J) = sqrt(I*(N-I))
#    else if ( I = J+1 )
#      A(I,J) = sqrt(J*(N-J))
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#       .    sqrt(4)    .       .       .
#    sqrt(4)    .    sqrt(6)    .       .
#       .    sqrt(6)    .    sqrt(6)    .
#       .       .    sqrt(6)    .    sqrt(4)
#       .       .       .    sqrt(4)    .
#
#  Properties:
#
#    A is tridiagonal.
#
#    A is banded, with bandwidth 3.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The diagonal of A is zero.
#
#    A is singular if N is odd.
#
#    About 64 percent of the entries of the inverse of A are zero.
#
#    The eigenvalues are plus and minus the numbers
#
#      N-1, N-3, N-5, ..., (1 or 0).
#
#    If N is even,
#
#      det ( A ) = (-1)**(N/2) * (N-1) * (N+1)**(N/2)
#
#    and if N is odd,
#
#      det ( A ) = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i + 1 ):
        A[i,j] = np.sqrt ( float ( ( i + 1 ) * ( n - i - 1 ) ) )
      elif ( i == j + 1 ):
        A[i,j] = np.sqrt ( float ( ( j + 1 ) * ( n - j - 1 ) ) )
      else:
        A[i,j] = 0.0

  return A

def dgbtrf_test ( ):

#*****************************************************************************80
#
## dgbtrf_test() tests dgbtrf().
#
#  Discussion:
#
#    The problem is just an enlarged version of the
#    problem for n = 5, which is:
#
#    Matrix A is ( 2 -1  0  0  0)    right hand side b is  (1)
#                (-1  2 -1  0  0)                          (0)
#                ( 0 -1  2 -1  0)                          (0)
#                ( 0  0 -1  2 -1)                          (0)
#                ( 0  0  0 -1  2)                          (1)
#
#
#    Solution is   (1)
#                  (1)
#                  (1)
#                  (1)
#                  (1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 September 2006
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgbtrf
  from scipy.linalg.lapack import dgbtrs

  print ( '' )
  print ( 'dgbtrf_test():' )
  print ( '  dgbtrf() factors a general band matrix.' )
  print ( '  dgbtrs() solves a factored system.' )
  print ( '  For a double precision real matrix (D)' )
  print ( '  in general band storage mode (GB):' )

  n = 5
  kl = 1
  ku = 1
#
#  Define the matrix.
#
  AB = np.zeros ( [ 2 * kl + 1 + ku, n ] )
  m = kl + ku
  AB[m-1,1:n]   = -1.0
  AB[m,0:n]   = 2.0
  AB[m+1,0:n-1] = -1.0

  print ( '' )
  print ( '  Band matrix has kl = ', kl, ' ku = ', ku )
#
#  Assign values to matrix A and right hand side b.
#
  b = np.zeros ( n )
  b[0] = 1.0
  b[n-1] = 1.0
#
#  Factor the matrix.
#
  LU, ipiv, info = dgbtrf ( AB, kl, ku )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgbtrf failed.' )
    print ( '  info = ', info )
    return
#
#  Solve the linear system.
#
  x, info = dgbtrs ( LU, kl, ku, b, ipiv )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgbtrs failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Solution x (all should be 1)' )
  print ( x )

  return

def dgecon_test ( ):

#*****************************************************************************80
#
## dgecon_test() tests dgecon().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg import norm
  from scipy.linalg.lapack import dgetrf
  from scipy.linalg.lapack import dgecon

  print ( '' )
  print ( 'dgecon_test():' )
  print ( '  dgecon() computes the condition of a matrix that has been' )
  print ( '  factored by dgetrf.' )
#
#  Set the matrix.
#
  A = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Compute matrix 1-norm.
#
  anorm = norm ( A, 1 )
  print ( '' )
  print ( '  Matrix 1-norm is ', anorm )
#
#  Factor the matrix.
#
  LU, piv, info = dgetrf ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgetrf failed.' )
    print ( '  info = ', info )
    return
#
#  Compute the reciprocal condition number.
#
  rcond, info = dgecon ( LU, anorm )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgecon failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Reciprocal condition number for 1-norm is', rcond )

  return

def dgeev_test ( ):

#*****************************************************************************80
#
## dgeev_test() tests dgeev().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgeev

  print ( '' )
  print ( 'dgeev_test():' )
  print ( '  dgeev() computes the eigenvalues and eigenvectors' )
  print ( '  of a matrix.' )

  n = 5
  A = clement1_matrix ( n )

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Get the eigen information
#
  wr, wi, vr, vi, info = dgeev ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgeev failed.' )
    print ( '  info = ', info )
    return
#
#  Display values.
#
  print ( '' )
  print ( '  Eigenvalues:' )
  print ( np.column_stack ( ( wr, wi ) ) )

  print ( '' )
  print ( '  Eigenvectors (real parts):' )
  print ( vr )
  print ( '' )
  print ( '  Eigenvectors (imaginary parts):' )
  print ( vi )

  return

def dgeqrf_test ( ):

#*****************************************************************************80
#
## dgeqrf_test() tests dgeqrf().
#
#  Discussion:
#
#    dgeqrf() computes the QR factorization of an M by N matrix A:
#
#      A(MxN) = Q(MxK) * R(KxN)
#
#    where K = min ( M, N ).
#
#    dorgqr() computes the explicit form of the Q factor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgeqrf
  from scipy.linalg.lapack import dorgqr

  print ( '' )
  print ( 'dgeqrf_test()' )
  print ( '  dgeqrf() computes the QR factorization:' )
  print ( '    A = Q * R' )
  print ( '  dorgqr() computes the explicit form of the Q factor.' )
  print ( '  For a double precision real matrix (D)' )
  print ( '  in general storage mode (GE):' )
#
#  Set the matrix.
#
  m = 4
  n = 3

  A = np.array ( [ \
    [ 1.0,  2.0, 3.0 ], \
    [ 4.0,  5.0, 6.0 ], \
    [ 7.0,  8.0, 0.0 ], \
    [ 5.0, 13.0, 3.0 ] ] )

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Compute the QR factorization.
#
  QR, tau, work, info = dgeqrf ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgeqrf failed.' )
    print ( '  info = ', info )
    return
#
#  Construct R.
#
  k = min ( m, n )
  R = np.zeros ( [ k, n ] )
  for i in range ( 0, k ):
    R[i,i:n] = QR[i,i:n]
#
#  Construct Q.
#
  Q, work, info = dorgqr ( QR, tau )

  if ( info != 0 ):
    print ( '' )
    print ( '  dorgqr failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Q:' )
  print ( Q )

  print ( '' )
  print ( '  R:' )
  print ( R )

  QR = np.matmul ( Q, R )

  print ( '' )
  print ( '  Q * R:' )
  print ( QR )

  return

def dgesvd_test ( ):

#*****************************************************************************80
#
## dgesvd_test() tests dgesvd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgesvd

  print ( '' )
  print ( 'dgesvd_test():' )
  print ( '  dgesvd() computes the singular value decomposition' )
  print ( '  of a matrix.' )
#
#  Set the matrix.
#
  A = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Compute the SVD.
#
  U, S, VT, info = dgesvd ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgesvd failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  U:' )
  print ( U )
  print ( '  S:' )
  print ( S )
  print ( '  vt:' )
  print ( VT )
#
#  Reconstruct A = U * S * V'.
#
  SV = np.dot ( np.diag ( S ), VT )
  USV = np.dot ( U, SV )
  print ( '' )
  print ( '  U*S*VT:' )
  print ( USV )

  return

def dgetrf_test ( ):

#*****************************************************************************80
#
## dgetrf_test() tests dgetrf().
#
#  Discussion:
#
#    The problem is just an enlarged version of the
#    problem for n = 5, which is:
#
#    Matrix A is ( N -1 -1 -1 -1)    right hand side b is  (1)
#                (-1  N -1 -1 -1)                          (1)
#                (-1 -1  N -1 -1)                          (1)
#                (-1 -1 -1  N -1)                          (1)
#                (-1 -1 -1 -1  N)                          (1)
#
#    Solution is   (1)
#                  (1)
#                  (1)
#                  (1)
#                  (1)
#
#    For this problem, no pivoting is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgetrf
  from scipy.linalg.lapack import dgetrs

  print ( '' )
  print ( 'dgetrf_test():' )
  print ( '  DGETRF factors a general matrix;' )
  print ( '  DGETRS solves a linear system;' )
  print ( '  For a double precision real matrix (D)' )
  print ( '  in general storage mode (GE):' )

  n = 5
#
#  Assign values to matrix A and right hand side b.
#
  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        A[i,j] = n
      else:
        A[i,j] = -1.0

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )

  b = np.ones ( n )

  print ( '' )
  print ( '  The right hand side b:' )
  print ( b )
#
#  Factor the matrix.
#
  LU, piv, info = dgetrf ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgetrf failed.' )
    print ( '  info = ', info )
    return
#
#  Solve the linear system.
#
  x, info = dgetrs ( LU, piv, b )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgetrs failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  The solution x (all entries should equal 1):' )
  print ( x )

  return

def dgetri_test ( ):

#*****************************************************************************80
#
## dgetri_test() tests dgetri().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgetrf
  from scipy.linalg.lapack import dgetri

  print ( '' )
  print ( 'dgetri_test():' )
  print ( '  dgetri() computes the inverse of a matrix that has been' )
  print ( '  factored by dgetrf.' )
#
#  Set the matrix.
#
  A = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Factor the matrix.
#
  LU, piv, info = dgetrf ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgetrf failed.' )
    print ( '  info = ', info )
    return
#
#  Compute the inverse.
#
  Ainv, info = dgetri ( LU, piv )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgetri failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Ainv:' )
  print ( Ainv )
#
#  Compute I = A * Ainv
#
  I = np.dot ( A, Ainv )
  print ( '' )
  print ( '  A * Ainv:' )
  print ( I )

  return

def dgtsv_test ( ):

#*****************************************************************************80
#
## dgtsv_test() tests dgtsv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dgtsv

  print ( '' )
  print ( 'dgtsv_test():' )
  print ( '  dgtsv() factors and solves a linear system' )
  print ( '  with a general tridiagonal matrix' )
  print ( '  for a double precision real matrix (D)' )
  print ( '  in general tridiagonal storage mode (GT).' )
#
#  Subdiagonal.
#  Diagonal.
#  Superdiagonal.
#
  n = 5
  c = -1.0 * np.ones ( n - 1 )
  d =  2.0 * np.ones ( n )
  e = -1.0 * np.ones ( n - 1 )
#
#  Right hand side.
#
  b = np.zeros ( n )
  b[n-1] = n + 1
#
#  Factor and solve the linear system.
#
  du2, d, du, x, info = dgtsv ( c, d, e, b )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgtsv failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Solution x (should be 1, 2, 3, ... ):' )
  print ( x )

  return

def dormqr_test ( ):

#*****************************************************************************80
#
## dormqr_test() tests dormqr().
#
#  Discussion:
#
#    We want to solve the MxN linear system A*x=b using the QR approach:
#
#    Factor A:
#
#      A = Q * R                        (step 1)
#
#    Transform:
#
#               A * x =               b
#      ==>  Q * R * x =               b
#      ==>      R * x =          Q' * b  (step 2)
#      ==>          x = inv(R) * Q' * b. (step 3)
#
#    Step 1) DGEQRF computes the QR factorization of an M by N matrix A:
#    A(MxN) = Q(MxK) * R(KxN) where K = min ( M, N ).
#
#    Step 2) DORMQR can multiply Q' * b, putting the result back into b.
#
#    Step 3) We could call a LAPACK routine to solve the upper triangular
#    system R * x = Q' * b.  Instead, we will try this part ourselves.
#
#
#    LAPACK makes this process tricky because of two things it does
#    for efficiency:
#
#    *) LAPACK computes the Q and R factors in a
#       compressed and encoded form, overwriting the matrix A and
#       storing some extra information in a vector called TAU.
#
#    *) LAPACK defines K = min ( M, N ), and
#       does NOT compute the QR factorization as an MxM Q
#       times an MxN R.  Instead, it computes an MxK Q times
#       a KxN R.  This saves it worrying about zeroes, but it
#       means the programmer has to worry about proper storage
#       and correct dimensioning.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2011
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  from scipy.linalg.lapack import dgeqrf
  from scipy.linalg.lapack import dormqr
  import numpy as np

  print ( '' )
  print ( 'dormqr_test():' )
  print ( '  dormqr() computes Q\' * b.' )
  print ( '  after dgeqrf() computes the QR factorization:' )
  print ( '    A = Q * R' )
  print ( '  storing a double precision real matrix (D)' )
  print ( '  in general storage mode (GE).' )
  print ( '' )
  print ( '  We use these routines to carry out a QR' )
  print ( '  solve of an M by N linear system A * x = b.' )
  print ( '' )
  print ( '  In this case, our M x N matrix A has more rows' )
  print ( '  than columns:' )
  print ( '' )

  m = 8
  n = 6
  k = min ( m, n )

  print ( '  M = ', m )
  print ( '  N = ', n )
#
#  Set the matrix A.
#
  rng = default_rng ( )

  A = rng.random ( [ m, n ] )
  print ( '' )
  print ( '  A:' )
  print ( A )
#
#  Set the solution x and right hand side b.
#  linspace() makes sense, arange() does not!
#
  x = np.linspace ( 1, n, n )

  b = np.matmul ( A, x )
#
#  Compute the QR factorization of A.
#
  QR, tau, work, info = dgeqrf ( A )

  if ( info != 0 ):
    print ( '' )
    print ( '  dgeqrf failed.' )
    print ( '  info = ', info )
    return
#
#  Copy the KxN matrix R out of Q.
#
  R = np.zeros ( [ k, n ] )
  for i in range ( 0, k ):
    R[i,i:n] = QR[i,i:n]
#
#  Multiply qtb = Q' * b.
#  Have no idea why lwork is here.  Fake it.
#
  lwork = len ( work )
  qtb, work, info = dormqr ( 'L', 'T', QR, tau, b, lwork )

  if ( info != 0 ):
    print ( '' )
    print ( '  dormqr failed.' )
    print ( '  info = ', info )
    return
#
#  STEP 3: Compute inv(R) * Q' * b, or, equivalently,
#  solve R * x = Q' * b.
#
  for j in range ( n - 1, -1, -1 ):
    x[j] = qtb[j] / R[j,j]
    for i in range ( 0, n ):
      qtb[i] = qtb[i] - R[i,j] * x[j]

  print ( '' )
  print ( '  Computed solution x:' )
  print ( x )

  return

def dpbtrf_test ( ):

#*****************************************************************************80
#
## dpbtrf_test() tests dpbtrf().
#
#  Discussion:
#
#    We want to compute the lower triangular Cholesky factor L
#    of a symmetric positive definite (SPD) band matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dpbtrf

  print ( '' )
  print ( 'dpbtrf_test():' )
  print ( '  dpbtrf() computes' )
  print ( '  the lower Cholesky factor A = L*L\' or' )
  print ( '  the upper Cholesky factor A = U\'*U;' )
  print ( '  For a double precision real matrix (D)' )
  print ( '  in positive definite band storage mode (PB):' )
#
#  Zero out the matrix.
#
  n = 5
  nband = 1
  AB = np.zeros ( [ nband+1, n ] )
#
#  Store the diagonal of a symmetric band matrix.
#
  AB[1,0:n] = 2.0
#
#  Store the superdiagonal of a symmetric band matrix.
#
  AB[0,1:n] = -1.0

  print ( '' )
  print ( 'AB:' )
  print ( AB )
#
#  Get the lower triangular Cholesky factor L:
#
  L, info = dpbtrf ( AB )

  if ( info != 0 ):
    print ( '' )
    print ( '  dpbtrf failed.' )
    print ( '  info = ', info )
    return
#
#  Print the relevant entries of L:
#
  print ( '' )
  print ( '  The lower Cholesky factor L:' )
  print ( '' )

  l_row = np.zeros ( n )

  for i in range ( 0, n ):
    l_row = np.zeros ( n )
    for j in range ( 0, n ):
 
      if ( 0 <= i - j + 1 and i - j + 1 <= nband ):
        l_row[j] = L[i-j+1,j]

    print ( l_row )

  return

def dpbtrs_test ( ):

#*****************************************************************************80
#
## dpbtrs_test() tests dpbtrs().
#
#  Discussion:
#
#    Solve a linear system A*x=b, where A is in positive definite
#    band storage.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dpbtrf
  from scipy.linalg.lapack import dpbtrs

  print ( '' )
  print ( 'dpbtrs_test():' )
  print ( '  dpbtrs() solves a linear system factored by dpbtrf().' )
#
#  Zero out the matrix.
#
  n = 5
  nband = 1
  AB = np.zeros ( [ nband+1, n ] )
#
#  Store the diagonal of a symmetric band matrix.
#
  AB[1,0:n] = 2.0
#
#  Store the superdiagonal of a symmetric band matrix.
#
  AB[0,1:n] = -1.0

  print ( '' )
  print ( 'AB:' )
  print ( AB )
#
#  Get the lower triangular Cholesky factor L:
#
  L, info = dpbtrf ( AB )

  if ( info != 0 ):
    print ( '' )
    print ( '  dpbtrf failed.' )
    print ( '  info = ', info )
    return
#
#  Set the right hand side.
#
  b = np.zeros ( n )
  b[0] = 1.0
  b[n-1] = 1.0
#
#  Solve the linear system.
#
  x, info = dpbtrs ( L, b )

  if ( info != 0 ):
    print ( '' )
    print ( '  dpbtrs failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Solution X:' );
  print ( x )

  return

def dpotrf_test ( ):

#*****************************************************************************80
#
## dpotrf_test() tests dpotrf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 September 2006
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dpotrf

  print ( '' )
  print ( 'dpotrf_test():' )
  print ( '  dpotrf() computes the Cholesky factorization R\'*R' )
  print ( '  for a double precision real matrix (D)' )
  print ( '  in positive definite storage mode (PO).' )
  n = 5
#
#  Define a square matrix.
#
  A = np.zeros ( [ n, n ] )

  for i in range ( 1, n ):
    A[i,i-1] = -1.0

  for i in range ( 0, n ):
    A[i,i] = 2.0

  for i in range ( 0, n - 1 ):
    A[i,i+1] = -1.0
#
#  Positive definite storage mode only saves upper half.
#  So make a copy with only that information.
#
  Ahalf = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      Ahalf[i,j] = A[i,j]

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Factor the matrix.
#
  R, info = dpotrf ( Ahalf )

  if ( info != 0 ):
    print ( '' )
    print ( '  dpotrf failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Cholesky factor R:' )
  print ( R )

  RtR = np.matmul ( R.T, R )

  print ( '' )
  print ( '  R\' * R:' )
  print ( RtR )

  return

def dpotri_test ( ):

#*****************************************************************************80
#
## dpotri_test() tests dpotri().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dpotrf
  from scipy.linalg.lapack import dpotri

  print ( '' )
  print ( 'dpotri_test():' )
  print ( '  dpotri() computes the inverse' )
  print ( '  for a double precision real matrix (D)' )
  print ( '  in positive definite storage mode (PO).' )

  n = 5
#
#  Define a square matrix.
#
  A = np.zeros ( [ n, n ] )

  for i in range ( 1, n ):
    A[i,i-1] = -1.0

  for i in range ( 0, n ):
    A[i,i] = 2.0

  for i in range ( 0, n - 1 ):
    A[i,i+1] = -1.0
#
#  Positive definite storage mode only saves upper half.
#  So make a copy with only that information.
#
  Ahalf = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      Ahalf[i,j] = A[i,j]

  print ( '' )
  print ( '  The matrix A:' )
  print ( A )
#
#  Factor the matrix.
#
  C, info = dpotrf ( Ahalf )

  if ( info != 0 ):
    print ( '' )
    print ( '  dpotrf failed.' )
    print ( '  info = ', info )
    return
#
#  Print the Cholesky factor.
#
  print ( '' )
  print ( '  The Cholesky factor C:' )
  print ( C )
#
#  Compute the inverse matrix.
#
  Ainvhalf, info = dpotri ( C )

  if ( info != 0 ):
    print ( '' )
    print ( '  dpotri failed.' )
    print ( '  info = ', info )
    return
#
#  We only got "half" the answer.  
#  Make a full matrix copy.
#
  Ainv = Ainvhalf.copy ( )
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      Ainv[i,j] = Ainv[j,i]

  print ( '' )
  print ( '  Inverse matrix Ainv:' )
  print ( Ainv )

  I = np.matmul ( A, Ainv )
  
  print ( '' )
  print ( '  Product I = A * Ainv:' )
  print ( I )

  return

def dsyev_test ( ):

#*****************************************************************************80
#
## dsyev_test() tests dsyev().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.linalg.lapack import dsyev

  print ( '' )
  print ( 'dsyev_test()' )
  print ( '  dsyev() computes eigenvalues and eigenvectors' )
  print ( '  For a double precision real matrix (D)' )
  print ( '  in symmetric storage mode (SY).' )
#
#  Set A.
#
  n = 5
  A = clement1_matrix ( n )

  Ahalf = A.copy()
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      Ahalf[i,j] = 0.0

  print ( '' )
  print ( '  (symmetric half) of A:' )
  print ( Ahalf )
#
#  Compute the eigenvalues and eigenvectors.
#
  w, V, info = dsyev ( Ahalf )

  if ( info != 0 ):
    print ( '' )
    print ( '  dsyev failed.' )
    print ( '  info = ', info )
    return

  print ( '' )
  print ( '  Eigenvalues w:' )
  print ( w )

  print ( '' )
  print ( '  Eigenvector matrix V:' )
  print ( V )

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
  lapack_test ( )
  timestamp ( )

