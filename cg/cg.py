#!/usr/bin/env python3
#
def cg_test ( ):

#*****************************************************************************80
#
## CG_TEST tests the CG library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CG library.' )
#
#  Utilities.
#
  orth_random_test ( )
  pds_random_test ( )
  r8_normal_01_test ( )
  r8_uniform_01_test ( )
  r8mat_house_axh_test ( )
  r8mat_house_form_test ( )
  r8mat_mm_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_uniform_ab_test ( )
  r8vec_house_column_test ( )
  r8vec_norm_test ( )
  r8vec_norm_affine_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )
#
#  Library.
#
  r83_cg_test ( )
  r83s_cg_test ( )
  r83t_cg_test ( )
  r8ge_cg_test ( )
  r8pbu_cg_test ( )
  r8sd_cg_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CG_TEST:' )
  print ( '  Normal end of execution.' )

def orth_random ( n, key ):

#*****************************************************************************80
#
## ORTH_RANDOM returns an ORTH_RANDOM matrix.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
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
 
  seed = key

  for j in range ( 0, n - 1 ):

    for i in range ( 0, j ):
      x_col[i] = 0.0

    for i in range ( j, n ):
      x_col[i], seed = r8_normal_01 ( seed )
#
#  Compute the vector V that defines a Householder transformation matrix
#  H(V) that annihilates the subdiagonal elements of X.
#
    v = r8vec_house_column ( n, x_col, j )
#
#  Postmultiply the matrix A by H'(V) = H(V).
#
    a = r8mat_house_axh ( n, a, v )

  return a

def orth_random_determinant ( n, key ):

#*****************************************************************************80
#
## ORTH_RANDOM_DETERMINANT returns the determinant of the ORTH_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def orth_random_test ( ):

#*****************************************************************************80
#
## ORTH_RANDOM_TEST tests ORTH_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  import platform

  print ( '' )
  print ( 'ORTH_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ORTH_RANDOM computes a random orthogal matrix.' )

  m = 5
  n = m
  key = 123456789

  a = orth_random ( n, key )

  r8mat_print ( m, n, a, '  ORTH_RANDOM matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ORTH_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pds_random ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM returns a random positive definite symmetric matrix.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * lam[k] * q[j,k]

  return a

def pds_random_determinant ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_DETERMINANT returns the determinant of the PDS_RANDOM matrix.
#
#  Discussion:
#
#    This routine will only work properly if the SAME value of SEED
#    is input that was input to PDS_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )

  value = np.prod ( lam )

  return value

def pds_random_eigen_right ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_EIGEN_RIGHT returns the right eigenvectors of the PDS_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real Q(N,N), the matrix.
#

#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )

  return q

def pds_random_eigenvalues ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_EIGENVALUES returns the eigenvalues of the PDS_RANDOM matrix.
#
#  Discussion:
#
#    This routine will only work properly if the SAME value of SEED
#    is input that was input to PDS_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real LAM(N), the eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )

  return lam

def pds_random_inverse ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_INVERSE returns the inverse of the PDS_RANDOM matrix.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * ( 1.0 / lam[k] ) * q[j,k]

  return a

def pds_random_test ( ):

#*****************************************************************************80
#
## PDS_RANDOM_TEST tests PDS_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PDS_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PDS_RANDOM computes the PDS_RANDOM matrix.' )

  n = 5
  key = 123456789
  a = pds_random ( n, key )

  r8mat_print ( n, n, a, '  PDS_RANDOM matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PDS_RANDOM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r83s_cg ( n, a, b, x_init ):

#*****************************************************************************80
#
## R83S_CG uses the conjugate gradient method on an R83S system.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
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
#      A2  A3   0   0   0
#      A1  A2  A3   0   0
#       0  A1  A2  A3   0 
#       0   0  A1  A2  A3
#       0   0   0  A1  A2
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
#    Input, real A(3), the matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, real X_INIT(N), an estimate for the solution, which may be 0.
#
#    Output, real X(N), the approximate solution vector.
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

def r83s_cg_test ( ):

#*****************************************************************************80
#
## R83S_CG_TEST tests R83S_CG.
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

  print ( '' )
  print ( 'R83S_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R83S_CG applies CG to an R83S matrix.' )

  n = 10
#
#  Let A be the -1 2 -1 matrix.
#
  a = r83s_dif2 ( n, n )
#
#  Choose a random solution.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
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

  return

def r83s_dif2 ( m, n ):

#*****************************************************************************80
#
## R83S_DIF2 returns the DIF2 matrix in R83S format.
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
#    Output, real A(3), the matrix.
#
  import numpy as np

  a = np.array ( [ -1.0, 2.0, -1.0 ] )
  
  return a

def r83s_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R83S_MV multiplies an R83S matrix times an R8VEC.
#
#  Discussion:
#
#    The R83S storage format is used for a tridiagonal scalar matrix.
#    The vector A(3) contains the subdiagonal, diagonal, and superdiagonal
#    values that occur on every row.
#
#  Example:
#
#    Here is how an R83S matrix of order 5, stored as (A1,A2,A3), would
#    be interpreted:
#
#      A2  A3   0   0   0
#      A1  A2  A3   0   0
#       0  A1  A2  A3   0 
#       0   0  A1  A2  A3
#       0   0   0  A1  A2
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(3), the R83S matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  ihi = min ( m - 1, n )
  for i in range ( 1, ihi + 1 ):
    b[i] = b[i] + a[0] * x[i-1]

  ihi = min ( m - 1, n - 1 )
  for i in range ( 0, ihi + 1 ):
    b[i] = b[i] + a[1] * x[i]

  ihi = min ( m - 1, n - 2 )
  for i in range ( 0, ihi + 1 ):
    b[i] = b[i] + a[2] * x[i+1]

  return b

def r83s_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## R83S_RES computes the residual R = B-A*X for R83S matrices.
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
#    Input, real A(3), the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  r = r83s_mv ( m, n, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r83_cg ( n, a, b, x_init ):

#*****************************************************************************80
#
## R83_CG uses the conjugate gradient method on an R83 system.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
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
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
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
#    Input, real A(3,N), the matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, real X_INIT(N), an estimate for the solution, which may be 0.
#
#    Output, real X(N), the approximate solution vector.
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
  ap = r83_mv ( n, n, a, x )

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
    ap = r83_mv ( n, n, a, p )
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

    for i in range ( 0, n):
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

def r83_cg_test ( ):

#*****************************************************************************80
#
## R83_CG_TEST tests R83_CG for an R83 matrix.
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

  print ( '' )
  print ( 'R83_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R83_CG applies CG to an R83 matrix.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a = r83_dif2 ( n, n )
#
#  Choose a random solution.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the corresponding right hand side.
#
  b = r83_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r83_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r83_res ( n, n, a, x3, b )
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
  print ( 'R83_CG_TEST' )
  print ( '  Normal end of execution.' )
  return

def r83_dif2 ( m, n ):

#*****************************************************************************80
#
## R83_DIF2 returns the DIF2 matrix in R83 format.
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
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real A(3,N), the matrix.
#
  import numpy as np

  a = np.zeros( [ 3, n ] )

  mn = min ( m, n )

  for j in range ( 0, mn ):
    a[1,j] = +2.0

  for j in range ( 1, mn ):
    a[0,j] = -1.0

  if ( m <= n ):
    for j in range ( 0, mn - 1 ):
      a[2,j] = -1.0
  elif ( n < m ):
    for j in range ( 0, mn ):
      a[2,j] = -1.0
  
  return a

def r83_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R83_MV multiplies a R83 matrix times a vector.
#
#  Discussion:
#
#    THIS FUNCTION SHOULD HANDLE MxN matrices, but for now only
#    handles NxN matrices...
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
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
#    Input, integer N, the order of the linear system.
#
#    Input, real A(3,N), the R83 matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 1, n ):
    b[i] = b[i] + a[0,i] * x[i-1]

  for i in range ( 0, n ):
    b[i] = b[i] + a[1,i] * x[i]

  for i in range ( 0, n - 1 ):
    b[i] = b[i] + a[2,i] * x[i+1]

  return b

def r83_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## R83_RES computes the residual R = B-A*X for R83 matrices.
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
#    Input, real A(3,N), the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  r = r83_mv ( m, n, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r83t_cg ( n, a, b, x_init ):

#*****************************************************************************80
#
## R83T_CG uses the conjugate gradient method on an R83T system.
#
#  Discussion:
#
#    The R83T storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1:N-1,3), the diagonal in
#    entries (1:N,2), and the subdiagonal in (2:N,1).  Thus, the
#    original matrix is "collapsed" horizontally into the array.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 July 2015
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
#    Input, real A(N,3), the matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, real X_INIT(N), an estimate for the solution, which may be 0.
#
#    Output, real X(N), the approximate solution vector.
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
  ap = r83t_mv ( n, n, a, x )

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

def r83t_cg_test ( ):

#*****************************************************************************80
#
## R83T_CG_TEST tests R83T_CG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 June 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R83T_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R83T_CG applies CG to an R83T matrix.' )

  n = 10
#
#  Let A be the -1 2 -1 matrix.
#
  a = r83t_dif2 ( n, n )
#
#  Choose a random solution.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the corresponding right hand side.
#
  b = r83t_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r83t_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r83t_res ( n, n, a, x3, b )
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

  return

def r83t_dif2 ( m, n ):

#*****************************************************************************80
#
## R83T_DIF2 returns the DIF2 matrix in R83T format.
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
#    08 July 2015
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
#    Output, real A(M,3), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, 3 ] )

  mn = min ( m, n )

  for i in range ( 1, mn ):
    a[i,0] = -1.0
  for i in range ( 0, mn ):
    a[i,1] = 2.0
  for i in range ( 0, mn - 1 ):
    a[i,2] = -1.0

  if ( m < n ):
    a[mn-1,2] = -1.0
  elif ( n < m ):
    a[mn,0] = -1.0
  
  return a

def r83t_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R83T_MV multiplies an R83T matrix times an R8VEC.
#
#  Discussion:
#
#    The R83T storage format is used for a tridiagonal matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,3), the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  mn = min ( m, n )

  if ( n == 1 ):
    b[0] = a[0,1] * x[0]
    if ( 1 < m ):
      b[1] = a[1,0] * x[0]
    return b

  b[0]      = a[0,1]       * x[0] \
            + a[0,2]       * x[1]

  for i in range ( 1, mn - 1 ):
    b[i] = a[i,0] * x[i-1] \
         + a[i,1] * x[i] \
         + a[i,2] * x[i+1]

  b[mn-1]   = a[mn-1,0]    * x[mn-2] \
            + a[mn-1,1]    * x[mn-1]

  if ( n < m ):
    b[mn] = b[mn] + a[mn,0] * x[mn-1]
  elif ( m < n ):
    b[mn-1] = b[mn-1] + a[mn-1,2] * x[mn]

  return b

def r83t_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## R83T_RES computes the residual R = B-A*X for R83T matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 July 2015
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
#    Input, real A(M,3), the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  import numpy as np

  r = r83t_mv ( m, n, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

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

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      if ( j == i - 1 ):
        a[i,j] = -1.0
      elif ( j == i ):
        a[i,j] = 2.0
      elif ( j == i + 1 ):
        a[i,j] = -1.0

  return a

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

def r8mat_house_axh ( n, a, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_AXH computes A*H where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real A(N,N), the matrix to be postmultiplied.
#
#    Input, real V(N), a vector defining a Householder matrix.
#
#    Output, real AH(N,N), the product A*H.
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

def r8mat_house_axh_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_AXH_TEST tests R8MAT_HOUSE_AXH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  n = 5

  print ( '' )
  print ( 'R8MAT_HOUSE_AXH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HOUSE_AXH multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )
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

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8mat_house_axh ( n, a, v )

  r8mat_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = r8mat_mm ( n, n, n, a, h )

  r8mat_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = r8mat_mm ( n, n, n, h, a )

  r8mat_print ( n, n, ha, '  H*A should pack column 3:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HOUSE_AXH_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_house_form ( n, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_FORM constructs a Householder matrix from its compact form.
#
#  Discussion:
#
#    H(v) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real V(N,1), the vector defining the Householder matrix.
#
#    Output, real H(N,N), the Householder matrix.
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

def r8mat_house_form_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_FORM_TEST tests R8MAT_HOUSE_FORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  n = 5

  v = np.array ( ( 0.0, 0.0, 1.0, 2.0, 3.0 ) )

  print ( '' )
  print ( 'R8MAT_HOUSE_FORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HOUSE_FORM forms a Householder' )
  print ( '  matrix from its compact form.' )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )
 
  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HOUSE_FORM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8MAT_MM multiplies two R8MAT's.
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

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8mat_mm_test ( ):

#*****************************************************************************80
#
## R8MAT_MM_TEST tests R8MAT_MM.
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
  print ( 'R8MAT_MM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_MM computes a matrix-matrix product C = A * B;' )

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8mat_mm ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_MM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
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
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
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
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8MAT_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_AB - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = np.floor ( seed )

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB_TEST tests R8MAT_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  import platform

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_AB computes a random R8MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_ab ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_normal_01 ( seed ):

#*****************************************************************************80
#
## R8_NORMAL_01 samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return x, seed

def r8_normal_01_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_TEST tests R8_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789
  test_num = 20

  print ( '' )
  print ( 'R8_NORMAL_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NORMAL_01 generates normally distributed' )
  print ( '  random values.' )
  print ( '  Using initial random number seed = %d' % ( seed ) )
  print ( '' )

  for test in range ( 0, test_num ):

    x, seed = r8_normal_01 ( seed )
    print ( '  %f' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NORMAL_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8pbu_cg ( n, mu, a, b, x_init ):

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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 July 2015
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
#    Input, integer MU, the number of superdiagonals.
#    MU must be at least 0, and no more than N-1.
#
#    Input, real A(MU+1,N), the R8PBU matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, real X_INIT(N), an estimate for the solution, which may be 0.
#
#    Output, real X(N), the approximate solution vector.
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
  ap = r8pbu_mv ( n, n, mu, a, x )

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
    ap = r8pbu_mv ( n, n, mu, a, p )
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

def r8pbu_cg_test ( ):

#*****************************************************************************80
#
## R8PBU_CG_TEST tests R8PBU_CG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8PBU_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8PBU_CG applies CG to an R8PBU matrix.' )

  seed = 123456789
  n = 10
  mu = 1
#
#  Let A be the -1 2 -1 matrix.
#
  a = r8pbu_dif2 ( n, n, mu )
#
#  Choose a random solution.
#
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the corresponding right hand side.
#
  b = r8pbu_mv ( n, n, mu, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r8pbu_cg ( n, mu, a, b, x2 )
#
#  Compute the residual.
#
  r = r8pbu_res ( n, n, mu, a, x3, b )
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 July 2015
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer MU, the number of superdiagonals.
#    MU must be at least 0, and no more than N-1.
#
#    Output, real A(MU+1,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ mu+1, n ] )

  for j in range ( 1, n ):
    a[mu-1,j] = -1.0

  for j in range ( 0, n ):
    a[mu,j] = +2.0
 
  return a

def r8pbu_mv ( m, n, mu, a, x ):

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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 July 2015
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
#    Input, integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    Input, real A(MU+1,N), the R8PBU matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(N), the result vector A * x.
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
  for i in range ( mu - 1, -1, - 1 ):
    for j in range ( mu - i, n ):
      ieqn = i + j - mu
      b[ieqn] = b[ieqn] + a[i,j] * x[j]
      b[j] = b[j] + a[i,j] * x[ieqn]

  return b

def r8pbu_res ( m, n, mu, a, x, b ):

#*****************************************************************************80
#
## R8PBU_RES computes the residual R = B-A*X for R8PBU matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 July 2015
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
#    Input, integer MU, the number of superdiagonals in the matrix.
#    MU must be at least 0 and no more than N-1.
#
#    Input, real A(MU+1,N), the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  r = r8pbu_mv ( m, n, mu, a, x )
 
  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r8sd_cg ( n, ndiag, offset, a, b, x_init ):

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
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals#),
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 July 2015
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
#    Input, integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    Input, integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.
#
#    Input, real A(N,NDIAG), the R8SD matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, real X_INIT(N), an estimate for the solution, which may be 0.
#
#    Output, real X(N), the approximate solution vector.
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
  ap = r8sd_mv ( n, n, ndiag, offset, a, x )

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
#  Compute the matrix*vector product AP = A*P.
#
    ap = r8sd_mv ( n, n, ndiag, offset, a, p )
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

def r8sd_cg_test ( ):

#*****************************************************************************80
#
## R8SD_CG_TEST tests R8SD_CG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8SD_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8SD_CG applies CG to an R8SD matrix.' )

  n = 10

  ndiag = 2
  offset = np.zeros ( ndiag, dtype = np.int32 )
  offset[0] = 0
  offset[1] = 1
#
#  Set A to the [-1 2 -1] matrix.
#
  a = r8sd_dif2 ( n, n, ndiag, offset )
#
#  Choose a random solution.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the corresponding right hand side.
#
  b = r8sd_mv ( n, n, ndiag, offset, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x2 = r8sd_cg ( n, ndiag, offset, a, b, x2 )
#
#  Compute the residual.
#
  r = r8sd_res ( n, n, ndiag, offset, a, x2, b )
  r_norm = r8vec_norm ( n, r )
#
#  Compute the error.
#
  e_norm = r8vec_norm_affine ( n, x1, x2 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r8sd_dif2 ( m, n, ndiag, offset ):

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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 July 2015
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 2.
#
#    Input, integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.  It is simply assumed that OFFSET(1) = 0 and OFFSET(2) = 1.
#
#    Output, real A(N,NDIAG), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, ndiag ] )

  for i in range ( 0, n ):
    a[i,0] = 2.0

  for i in range ( 0, n - 1 ):
    a[i,1] = -1.0
 
  return a

def r8sd_mv ( m, n, ndiag, offset, a, x ):

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
#    Assuming there are NDIAG nonzero diagonals (ignoring subdiagonals#),
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    Input, integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.
#
#    Input, real A(N,NDIAG), the R8SD matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(N), the product A * x.
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

def r8sd_res ( m, n, ndiag, offset, a, x, b ):

#*****************************************************************************80
#
## R8SD_RES computes the residual R = B-A*X for R8SD matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 July 2015
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
#    Input, integer NDIAG, the number of diagonals that are stored.
#    NDIAG must be at least 1 and no more than N.
#
#    Input, integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.
#
#    Input, real A(N,NDIAG), the R8SD matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  r = r8sd_mv ( m, n, ndiag, offset, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r8sp_cg ( n, nz_num, row, col, a, b, x_init ):

#*****************************************************************************80
#
## R8SP_CG uses the conjugate gradient method on an R8SP system.
#
#  Discussion:
#
#    The R8SP storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    It is possible that a pair of indices (I,J) may occur more than
#    once.  Presumably, in this case, the intent is that the actual value
#    of A(I,J) is the sum of all such entries.  This is not a good thing
#    to do, but I seem to have come across this in MATLAB.
#
#    The R8SP format is used by CSPARSE ("sparse triplet"), DLAP/SLAP 
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#    The matrix A must be a positive definite symmetric matrix.
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
#    09 July 2015
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
#    Input, integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, real X_INIT(N), an estimate for the solution, which may be 0.
#
#    Output, real X(N), the approximate solution vector.
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
  ap = r8sp_mv ( n, n, nz_num, row, col, a, x )

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
    ap = r8sp_mv ( n, n, nz_num, row, col, a, p )
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

def r8sp_cg_test ( ):

#*****************************************************************************80
#
## R8SP_CG_TEST tests R8SP_CG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8SP_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8SP_CG applies CG to an R8SP matrix.' )

  seed = 123456789
  n = 10
  nz_num = 3 * n - 2
#
#  Set A to the [-1 2 -1] matrix.
#
  row, col, a = r8sp_dif2 ( n, n, nz_num )
#
#  Choose a random solution.
#
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the corresponding right hand side.
#
  b = r8sp_mv ( n, n, nz_num, row, col, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r8sp_cg ( n, nz_num, row, col, a, b, x2 )
#
#  Compute the residual.
#
  r = r8sp_res ( n, n, nz_num, row, col, a, x3, b )
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

  return

def r8sp_dif2 ( m, n, nz_num ):

#*****************************************************************************80
#
## R8SP_DIF2 returns the DIF2 matrix in R8SP format.
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
#    09 July 2015
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    Output, integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    Output, real A(NZ_NUM), the nonzero elements of the matrix.
#
  import numpy as np

  row = np.zeros ( nz_num, dtype = np.int32 )
  col = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num, dtype = np.float64 )

  k = 0
  for i in range ( 0, m ):

    if ( 0 < i ):

      row[k] = i
      col[k] = i - 1
      a[k] = -1.0
      k = k + 1

    row[k] = i
    col[k] = i
    a[k] = 2.0
    k = k + 1

    if ( i < n - 1 ):

      row[k] = i
      col[k] = i + 1
      a[k] = -1.0
      k = k + 1

  return row, col, a

def r8sp_mv ( m, n, nz_num, row, col, a, x ):

#*****************************************************************************80
#
## R8SP_MV multiplies an R8SP matrix by an R8VEC.
#
#  Discussion:
#
#    The R8SP storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    It is possible that a pair of indices (I,J) may occur more than
#    once.  Presumably, in this case, the intent is that the actual value
#    of A(I,J) is the sum of all such entries.  This is not a good thing
#    to do, but I seem to have come across this in MATLAB.
#
#    The R8SP format is used by CSPARSE ("sparse triplet"), DLAP/SLAP 
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of 
#    the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product vector A*X.
#
  import numpy as np

  b = np.zeros ( m, dtype = np.float64 )

  for k in range ( 0, nz_num ):

    i = row[k]
    j = col[k]
    b[i] = b[i] + a[k] * x[j]

  return b

def r8sp_res ( m, n, nz_num, row, col, a, x, b ):

#*****************************************************************************80
#
## R8SP_RES computes the residual R = B-A*X for R8SP matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 July 2015
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
#    Input, integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  r = r8sp_mv ( m, n, nz_num, row, col, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
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
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_house_column ( n, a_vec, k ):

#*****************************************************************************80
#
## R8VEC_HOUSE_COLUMN defines a Householder premultiplier that "packs" a column.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix A.
#
#    Input, real A_VEC(N), a row or column of the matrix A.
#
#    Input, integer K, the "special" entry in A_VEC.
#    The Householder matrix will zero out the entries after this.
#
#    Output, real V(N), a vector of unit L2 norm which defines an
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
## R8VEC_HOUSE_COLUMN_TEST tests R8VEC_HOUSE_COLUMN.
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

  print ( '' )
  print ( 'R8VEC_HOUSE_COLUMN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_HOUSE_COLUMN returns the compact form of' )
  print ( '  a Householder matrix that "packs" a column' )
  print ( '  of a matrix.' )
#
#  Get a random matrix.
#
  n = 4
  r8_lo = 0.0
  r8_hi = 5.0
  seed = 123456789;

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ( '' )
    print ( '  Working on column K = %d' % ( k ) )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8mat_house_form ( n, v )

    r8mat_print ( n, n, h, '  Householder matrix H:' )

    ha = r8mat_mm ( n, n, n, h, a )

    r8mat_print ( n, n, ha, '  Product H*A:' )
#
#  If we set A := HA, then we can successively convert A to upper
#  triangular form.
#
    a = ha
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_HOUSE_COLUMN_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm_affine ( n, v0, v1 ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE returns the affine norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The affine vector L2 norm is defined as:
#
#      R8VEC_NORM_AFFINE(V0,V1) 
#        = sqrt ( sum ( 1 <= I <= N ) ( V1(I) - V0(I) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the vector dimnension.
#
#    Input, real V0(N), the base vector.
#
#    Input, real V1(N), the vector.
#
#    Output, real VALUE, the affine L2 norm.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ): 
    value = value + ( v0[i] - v1[i] ) ** 2
  value =  np.sqrt ( value )

  return value

def r8vec_norm_affine_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE_TEST tests R8VEC_NORM_AFFINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_AFFINE computes the L2 norm of' )
  print ( '  the difference of two R8VECs.' )

  seed = 123456789;

  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  z = np.zeros ( n )
  for i in range ( 0, n ):
    z[i] = x[i] - y[i]

  print ( '' )
  print ( '  R8VEC_NORM_AFFINE(X,Y) = %g' % ( r8vec_norm_affine ( n, x, y ) ) )
  print ( '  R8VEC_NORM (X-Y):        %g' % ( r8vec_norm ( n, z ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L2 norm is desired.
#
#    Output, real VALUE, the L2 norm of A.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = np.sqrt ( value )

  return value

def r8vec_norm_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_TEST tests R8VEC_NORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM computes the L2 norm of an R8VEC.' )

  n = 10
  seed = 123456789
  a, seed = r8vec_uniform_01 ( n, seed )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm ( n, a )

  print ( '' )
  print ( '  L2 norm = %g' % ( a_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
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
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647;

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = numpy.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
 
  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_AB - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_AB computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  cg_test ( )
  timestamp ( )

