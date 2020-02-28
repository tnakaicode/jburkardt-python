#! /usr/bin/env python
#
def r8ge_cg ( n, a, b, x ):

#*****************************************************************************80
#
## R8GE_CG uses the conjugate gradient method on an R8GE system.
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A(N,N), the matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input/output, real X(N).
#    On input, an estimate for the solution, which may be 0.
#    On output, the approximate solution vector.
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

def r8ge_cg_test ( ):

#*****************************************************************************80
#
## R8GE_CG_TEST tests R8GE_CG for a full storage matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from pds_random import pds_random
  from r8vec_norm import r8vec_norm
  from r8vec_norm_affine import r8vec_norm_affine
  from r8vec_uniform_01 import r8vec_uniform_01

  print ( '' )
  print ( 'R8GE_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_CG applies CG to an R8GE matrix.' )
#
#  Choose a random positive definite symmetric matrix A.
#
  n = 10
  key = 123456789

  a = pds_random ( n, key )
#
#  Choose a random solution.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
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
  r_norm = r8vec_norm ( n, r )
#
#  Compute the error.
#
  e_norm = r8vec_norm_affine ( n, x1, x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_CG_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_det ( n, a_lu, pivot ):

#*****************************************************************************80
#
## R8GE_DET: determinant of a matrix factored by R8GE_FA or R8GE_TRF.
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA 
#    or R8GE_TRF.
#
#    Input, integer PIVOT(N), as computed by R8GE_FA or R8GE_TRF.
#
#    Output, real DET, the determinant of the matrix.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i]
    if ( pivot[i] != i ):
      value = - value

  return value

def r8ge_dif2 ( m, n ):

#*****************************************************************************80
#
## R8GE_DIF2 returns the DIF2 matrix in R8GE format.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real A(M,N), the matrix.
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

def r8ge_dilu ( m, n, a ):

#*****************************************************************************80
#
## R8GE_DILU produces the diagonal incomplete LU factor of an R8GE matrix.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the R8GE matrix.
#
#    Output, real D(M), the DILU factor.
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

def r8ge_fa ( n, a ):

#*****************************************************************************80
#
## R8GE_FA performs a LINPACK style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_FA is a simplified version of the LINPACK routine R8GEFA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A(N,N), the matrix to be factored.
#
#    Output, real A_LU(N,N), an upper triangular matrix and 
#    the multipliers used to obtain it.  The factorization 
#    can be written A = L * U, where L is a product of 
#    permutation and unit lower triangular matrices and U 
#    is upper triangular.
#
#    Output, integer PIVOT(N), a vector of pivot indices.
#
#    Output, integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np
  from sys import exit

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
## R8GE_FA_TEST01 tests R8GE_FA, R8GE_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform
  from r8vec_print import r8vec_print

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FA_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_FA computes the LU factors,' )
  print ( '  R8GE_SL solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )
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
    print ( 'R8GE_FA_TEST01 - Warning!' )
    print ( '  R8GE_FA declares the matrix is singular!' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FA_TEST01' )
  print ( '  Normal end of execution.' )
  return

def r8ge_fa_test02 ( ):

#*****************************************************************************80
#
## R8GE_FA_TEST02 tests R8GE_FA, R8GE_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform
  from i4vec_print import i4vec_print
  from r8vec_print import r8vec_print

  n = 5
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FA_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_FA computes the LU factors,' )
  print ( '  R8GE_SL solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )

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
    print ( 'R8GE_FA_TEST02 - Warning!' )
    print ( '  R8GE_FA declares the matrix is singular!' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FA_TEST02' )
  print ( '  Normal end of execution.' )
  return

def r8ge_identity ( n ):

#*****************************************************************************80
#
## R8GE_IDENTITY copies the identity matrix to an R8GE matrix.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the N by N identity matrix.
#
  import numpy as np

  a = r8ge_zeros ( n, n )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def r8ge_ml ( n, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## R8GE_ML computes A * x or A' * x, using R8GE_FA factors.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that R8GE_FA has overwritten the original matrix
#    information by LU factors.  R8GE_ML is able to reconstruct the
#    original matrix from the LU factor data.
#
#    R8GE_ML allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA.
#
#    Input, integer PIVOT(N), the pivot vector computed by R8GE_FA.
#
#    Input, real X(N), the vector to be multiplied.
#
#    Input, integer JOB, specifies the operation to be done:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * X.
#
#    Output, real B(N), the result of the multiplication.
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

def r8ge_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8GE_MM multiplies two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A * B.
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
## R8GE_MM_TEST tests R8GE_MM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'R8GE_MM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MM computes a matrix-matrix product C = A * B;' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8GE_MTM computes A' * B for two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A' * B.
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
## R8GE_MTM_TEST tests R8GE_MTM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'R8GE_MTM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MTM computes a matrix-matrix product C = A\' * B;' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MTM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## R8GE_MTV multiplies a vector by a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8GE matrix.
#
#    Input, real X(M), the vector to be multiplied by A.
#
#    Output, real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j] = x[i] * a[i,j]

  return b

def r8ge_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R8GE_MV multiplies an R8GE matrix times a vector.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8GE matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8GE_PRINT prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_test ( ):

#*****************************************************************************80
#
## R8GE_PRINT_TEST tests R8GE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8GE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PRINT prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8GE_PRINT_SOME prints out a portion of an R8GE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## R8GE_PRINT_SOME_TEST tests R8GE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8GE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PRINT_SOME prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8GE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_random ( m, n, seed ):

#*****************************************************************************80
#
## R8GE_RANDOM randomizes a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real A(M,N), the R8GE matrix.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8GE_RANDOM - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8GE_RANDOM - Fatal error!' )

  r = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8ge_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## R8GE_RES computes the residual vector for an R8GE system.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of 
#    the matrix.  M and N must be positive.
#
#    Input, real A(M,N), the original, UNFACTORED R8GE matrix.
#
#    Input, real X(N), the estimated solution.
#
#    Input, real B(M), the right hand side vector.
#
#    Output, real R(M), the residual vector, b - A * x.
#
  import numpy as np

  r = np.zeros ( m )

  for i in range ( 0, m ):
    r[i] = b[i]
    for j in range ( 0, n ):
      r[i] = r[i] - a[i,j] * x[j]

  return r

def r8ge_sl ( n, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## R8GE_SL solves a system factored by R8GE_FA.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_SL is a simplified version of the LINPACK routine R8GESL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA.
#
#    Input, integer PIVOT(N), the pivot vector from R8GE_FA.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, integer JOB, specifies the operation.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#    Output, real X(N), the solution vector.
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

def r8ge_to_r8po ( n, a ):

#*****************************************************************************80
#
## R8GE_TO_R8PO copies an R8GE matrix to an R8PO matrix.
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
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#    R8PO storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the R8GE matrix.
#
#    Output, real B(N,N), the R8PO matrix.
#
  import numpy as np
  from r8po import r8po_zeros

  b = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      b[i,j] = a[i,j]

  return b

def r8ge_to_r8po_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8PO_TEST tests R8GE_TO_R8PO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8po import r8po_print

  n = 5
  seed = 123456789

  print ( '' )
  print ( 'R8GE_TO_R8PO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8PO converts an R8GE matrix to R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a, seed = r8ge_random ( n, n, seed )

  r8ge_print ( n, n, a, '  The random R8GE matrix:' )
 
  b = r8ge_to_r8po ( n, a )

  r8po_print ( n, b, '  The R8PO matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8PO_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_zeros ( m, n ):

#*****************************************************************************80
#
## R8GE_ZEROS zeroes an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#    N must be positive.
#
#    Output, real A(M,N), the zeroed out matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ge_zeros_test ( ):

#*****************************************************************************80
#
## R8GE_ZEROS_TEST tests R8GE_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_ZEROS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_ZEROS zeros out space for a general matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ge_zeros ( m, n )

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_ZEROS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8ge_cg_test ( )
  r8ge_fa_test01 ( )
  r8ge_fa_test02 ( )
  r8ge_mm_test ( )
  r8ge_mtm_test ( )
  r8ge_print_test ( )
  r8ge_print_some_test ( )
  r8ge_to_r8po_test ( )
  r8ge_zeros_test ( )
  timestamp ( )
 
