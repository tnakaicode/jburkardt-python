#! /usr/bin/env python3
#
def cg_csc ( n, a, b, x ):

#*****************************************************************************80
#
## cg_csc() uses the conjugate gradient method for a CSC matrix.
#
#  Discussion:
#
#    The linear system has the form A*x=b, where A is a positive-definite
#    symmetric matrix, stored in Python's Compressed Sparse Column (CSC) format.
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
#    01 September 2014
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
#    real A(N,N), the matrix, in Python's CSC format.
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
  ap = a.dot ( x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP = A*P.
#
    ap = a.dot ( p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr =  np.dot ( p, r )

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

def cg_ge ( n, a, b, x ):

#*****************************************************************************80
#
## cg_ge() uses the conjugate gradient method for a general storage matrix.
#
#  Discussion:
#
#    The linear system has the form A*x=b, where A is a positive-definite
#    symmetric matrix, stored as a full storage matrix.
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
#    31 August 2014
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
  ap = np.dot ( a, x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP = A*P.
#
    ap = np.dot ( a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr =  np.dot ( p, r )

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

def cg_st ( n, nz_num, row, col, a, b, x ):

#*****************************************************************************80
#
## cg_st() uses the conjugate gradient method for a sparse triplet storage matrix.
#
#  Discussion:
#
#    The linear system has the form A*x=b, where A is a positive-definite
#    symmetric matrix, stored as a full storage matrix.
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
#    31 August 2014
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
#    integer NZ_NUM, the number of nonzeros.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero entries.
#
#    real A(NZ_NUM), the nonzero entries.
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
  ap = mv_st ( n, n, nz_num, row, col, a, x )

  r = b - ap
  p = b - ap
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP = A*P.
#
    ap = mv_st ( n, n, nz_num, row, col, a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr =  np.dot ( p, r )

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

def mv_st ( m, n, nz_num, row, col, a, x ):

#*****************************************************************************80
#
## mv_st() multiplies a sparse triple matrix times a vector.
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
#    integer M, N, the number of rows and columns.
#
#    integer NZ_NUM, the number of nonzero values.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices.
#
#    real A(NZ_NUM), the nonzero values in the M by N matrix.
#
#    real X(N), the vector to be multiplied.
#
#  Output:
#
#    real B(M), the product A*X.
#
  import numpy as np

  b = np.zeros ( m )

  for k in range ( 0, nz_num ):
    b[row[k]] = b[row[k]] + a[k] * x[col[k]]

  return b

def nonzeros ( m, n, a ):

#*****************************************************************************80
#
## nonzeros() counts the nonzeros in a matrix.
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
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    integer NNZ, the number of nonzero entries.
#
  nnz = 0;
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( a[i,j] != 0.0 ):
        nnz = nnz + 1

  return nnz

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

def st_to_ge ( n_st, row, col, a_st ):

#*****************************************************************************80
#
## st_to_ge() converts a sparse triplet (ST) matrix to general (GE) storage.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_ST, the number of sparse triplet values.
#
#    integer ROW(N_ST), COL(N_ST), the row and column indices.
#
#    real A_ST(N_ST), the nonzero matrix values.
#
#  Output:
#
#    real A_GE(M,N), the corresponding full storage matrix.
#
  import numpy as np
#
#  Guess the number of rows and columns.
#
  m = max ( row ) + 1
  n = max ( col ) + 1
#
#  Set up the GE matrix.
#
  a_ge = np.zeros ( ( m, n ) )
#
#  Copy the data as a vector.
#
  for k in range ( 0, n_st ):
    a_ge[row[k],col[k]] = a_st[k]

  return a_ge

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

  return

def wathen_bandwidth ( nx, ny ):

#*****************************************************************************80
#
## wathen_bandwidth() returns the bandwidth of the WATHEN matrix.
#
#  Discussion:
#
#    The bandwidth measures the minimal number of contiguous diagonals,
#    including the central diagonal, which contain all the nonzero elements
#    of a matrix.
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
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of A.
#
#  Output:
#
#    integer L, D, U, the lower, diagonal, and upper bandwidths 
#    of the matrix,
#
  l = 3 * nx + 4
  d = 1
  u = 3 * nx + 4

  return l, d, u

def wathen_csc ( nx, ny, rng ):

#*****************************************************************************80
#
## wathen_csc(): Wathen matrix stored in Compressed Sparse Column (CSC) format.
#
#  Discussion:
#
#    The Wathen matrix is a finite element matrix which is sparse.
#
#    The entries of the matrix depend in part on a physical quantity
#    related to density.  That density is here assigned random values between
#    0 and 100.
#
#    The matrix order N is determined by the input quantities NX and NY,
#    which would usually be the number of elements in the X and Y directions.
#
#    The value of N is
#
#      N = 3*NX*NY + 2*NX + 2*NY + 1,
#
#    The matrix is the consistent mass matrix for a regular NX by NY grid
#    of 8 node serendipity elements.
#
#    The local element numbering is
#
#      3--2--1
#      |     |
#      4     8
#      |     |
#      5--6--7
#
#    Here is an illustration for NX = 3, NY = 2:
#
#     23-24-25-26-27-28-29
#      |     |     |     |
#     19    20    21    22
#      |     |     |     |
#     12-13-14-15-16-17-18
#      |     |     |     |
#      8     9    10    11
#      |     |     |     |
#      1--2--3--4--5--6--7
#
#    For this example, the total number of nodes is, as expected,
#
#      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#    The matrix is symmetric positive definite for any positive values of the
#    density RHO(X,Y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real A(*,*), the compressed sparxe column version of the matrix.
#
  from scipy.sparse import coo_matrix
  import numpy as np

  em = np.array \
  ( \
    ( ( 6.0, -6.0,  2.0, -8.0,  3.0, -8.0,  2.0, -6.0 ), \
      (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0 ), \
      ( 2.0, -6.0,  6.0, -6.0,  2.0, -8.0,  3.0, -8.0 ), \
      (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0 ), \
      ( 3.0, -8.0,  2.0, -6.0,  6.0, -6.0,  2.0, -8.0 ), \
      (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0 ), \
      ( 2.0, -8.0,  3.0, -8.0,  2.0, -6.0,  6.0, -6.0 ), \
      (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0 ) )\
  )

  node = np.zeros ( 8, dtype = np.int32 )

  st_num = 8 * 8 * nx * ny
  row = np.zeros ( st_num, dtype = np.int32 )
  col = np.zeros ( st_num, dtype = np.int32 )
  v = np.zeros ( st_num )

  k = 0

  for j in range ( 0, ny ):

    for i in range ( 0, nx ):

      node[0] = ( 3 * ( j + 1 )     ) * nx + 2 * ( j + 1 ) + 2 *  ( i + 1 ) + 1 - 1
      node[1] = node[0] - 1
      node[2] = node[0] - 2

      node[3] = ( 3 * ( j + 1 ) - 1 ) * nx + 2 *  ( j + 1 ) + ( i + 1 ) - 1 - 1
      node[7] = node[3] + 1

      node[4] = ( 3 *  ( j + 1 ) - 3 ) * nx + 2 *  ( j + 1 ) + 2 *  ( i + 1 ) - 3 - 1
      node[5] = node[4] + 1
      node[6] = node[4] + 2

      rho = 100.0 * rng.random ( )

      for krow in range ( 0, 8 ):
        for kcol in range ( 0, 8 ):
          row[k] = node[krow]
          col[k] = node[kcol]
          v[k] = rho * em[krow,kcol]
          k = k + 1
#
#  Convert triplet to a Python COO matrix.
#
  a = coo_matrix ( ( v, ( row, col ) ) )
#
#  Convert COO matrix to CSC format.
#
  a = a.tocsc ( )

  return a

def wathen_ge ( nx, ny, rng ):

#*****************************************************************************80
#
## wathen_ge() returns the Wathen matrix, using general (GE) storage.
#
#  Discussion:
#
#    The Wathen matrix is a finite element matrix which is sparse.
#
#    The entries of the matrix depend in part on a physical quantity
#    related to density.  That density is here assigned random values between
#    0 and 100.
#
#    The matrix order N is determined by the input quantities NX and NY,
#    which would usually be the number of elements in the X and Y directions.
#    The value of N is
#
#      N = 3*NX*NY + 2*NX + 2*NY + 1,
#
#    The matrix is the consistent mass matrix for a regular NX by NY grid
#    of 8 node serendipity elements.
#
#    The local element numbering is
#
#      3--2--1
#      |     |
#      4     8
#      |     |
#      5--6--7
#
#    Here is an illustration for NX = 3, NY = 2:
#
#     23-24-25-26-27-28-29
#      |     |     |     |
#     19    20    21    22
#      |     |     |     |
#     12-13-14-15-16-17-18
#      |     |     |     |
#      8     9    10    11
#      |     |     |     |
#      1--2--3--4--5--6--7
#
#    For this example, the total number of nodes is, as expected,
#
#      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#    The matrix is symmetric positive definite for any positive values of the
#    density RHO(X,Y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  n = wathen_order ( nx, ny )

  A = np.zeros ( ( n, n ) )

  em = np.array \
  ( \
    ( ( 6.0, -6.0,  2.0, -8.0,  3.0, -8.0,  2.0, -6.0 ), \
      (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0 ), \
      ( 2.0, -6.0,  6.0, -6.0,  2.0, -8.0,  3.0, -8.0 ), \
      (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0 ), \
      ( 3.0, -8.0,  2.0, -6.0,  6.0, -6.0,  2.0, -8.0 ), \
      (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0 ), \
      ( 2.0, -8.0,  3.0, -8.0,  2.0, -6.0,  6.0, -6.0 ), \
      (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0 ) )\
  )

  node = np.zeros ( 8, dtype = np.int32 )

  for j in range ( 0, ny ):

    for i in range ( 0, nx ):
#
#  For the element (I,J), determine the indices of the 8 nodes.
#
      node[0] = ( 3 * ( j + 1 )     ) * nx + 2 * ( j + 1 ) + 2 *  ( i + 1 ) + 1 - 1
      node[1] = node[0] - 1
      node[2] = node[0] - 2

      node[3] = ( 3 * ( j + 1 ) - 1 ) * nx + 2 *  ( j + 1 ) + ( i + 1 ) - 1 - 1
      node[7] = node[3] + 1

      node[4] = ( 3 *  ( j + 1 ) - 3 ) * nx + 2 *  ( j + 1 ) + 2 *  ( i + 1 ) - 3 - 1
      node[5] = node[4] + 1
      node[6] = node[4] + 2

      rho = 100.0 * rng.random ( )

      for krow in range ( 0, 8 ):
        for kcol in range ( 0, 8 ):
          A[node[krow],node[kcol]] = A[node[krow],node[kcol]] \
            + rho * em[krow,kcol]

  return A

def wathen_order ( nx, ny ):

#*****************************************************************************80
#
## wathen_order() returns the order of the WATHEN matrix.
#
#  Discussion:
#
#    N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
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
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of A.
#
#  Output:
#
#    integer N, the order of the matrix,
#    as determined by NX and NY.
#
  n = 3 * nx * ny + 2 * nx + 2 * ny + 1

  return n

def wathen_order_test ( ):

#*****************************************************************************80
#
## wathen_order_test() tests wathen_order().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, 1987, pages 449-457.
#
  print ( '' )
  print ( 'wathen_order_test():' )
  print ( '  wathen_order() returns N, the order of a Wathen finite element' )
  print ( '  matrix given NX and NY, the number of rows and columns of' )
  print ( '  nodes in the underlying grid.' )
  print ( '' )
  print ( '       NX / NY: 1       2       3       4       5       6' )
  print ( '' )

  for ny in range ( 1, 11 ):
    print ( '       %2d' % ( ny ), end = '' )
    for nx in range ( 1, 7 ):
      n = wathen_order ( nx, ny )
      print ( '  %5d' % ( n ), end = '' )
    print ( '' )

  return

def wathen_st ( nx, ny, rng ):

#*****************************************************************************80
#
## wathen_st(): Wathen matrix stored in sparse triplet format.
#
#  Discussion:
#
#    When dealing with sparse matrices in MATLAB, it can be much more efficient
#    to work first with a triple of I, J, and X vectors, and only once
#    they are complete, convert to MATLAB's sparse format.
#
#    The Wathen matrix is a finite element matrix which is sparse.
#
#    The entries of the matrix depend in part on a physical quantity
#    related to density.  That density is here assigned random values between
#    0 and 100.
#
#    The matrix order N is determined by the input quantities NX and NY,
#    which would usually be the number of elements in the X and Y directions.
#
#    The value of N is
#
#      N = 3*NX*NY + 2*NX + 2*NY + 1,
#
#    The matrix is the consistent mass matrix for a regular NX by NY grid
#    of 8 node serendipity elements.
#
#    The local element numbering is
#
#      3--2--1
#      |     |
#      4     8
#      |     |
#      5--6--7
#
#    Here is an illustration for NX = 3, NY = 2:
#
#     23-24-25-26-27-28-29
#      |     |     |     |
#     19    20    21    22
#      |     |     |     |
#     12-13-14-15-16-17-18
#      |     |     |     |
#      8     9    10    11
#      |     |     |     |
#      1--2--3--4--5--6--7
#
#    For this example, the total number of nodes is, as expected,
#
#      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#    The matrix is symmetric positive definite for any positive values of the
#    density RHO(X,Y).
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
#    John Burkardt.
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices 
#    of the nonzero entries.
#
#    real A(NZ_NUM), the nonzero values.
#
  import numpy as np

  nz_num = wathen_st_size ( nx, ny )

  em = np.array \
  ( \
    ( ( 6.0, -6.0,  2.0, -8.0,  3.0, -8.0,  2.0, -6.0 ), \
      (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0 ), \
      ( 2.0, -6.0,  6.0, -6.0,  2.0, -8.0,  3.0, -8.0 ), \
      (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0 ), \
      ( 3.0, -8.0,  2.0, -6.0,  6.0, -6.0,  2.0, -8.0 ), \
      (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0 ), \
      ( 2.0, -8.0,  3.0, -8.0,  2.0, -6.0,  6.0, -6.0 ), \
      (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0 ) )\
  )

  node = np.zeros ( 8, dtype = np.int32 )
  row = np.zeros ( nz_num, dtype = np.int32 )
  col = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num )

  k = 0

  for j in range ( 0, ny ):

    for i in range ( 0, nx ):

      node[0] = ( 3 * ( j + 1 )     ) * nx + 2 * ( j + 1 ) + 2 *  ( i + 1 ) + 1 - 1
      node[1] = node[0] - 1
      node[2] = node[0] - 2

      node[3] = ( 3 * ( j + 1 ) - 1 ) * nx + 2 *  ( j + 1 ) + ( i + 1 ) - 1 - 1
      node[7] = node[3] + 1

      node[4] = ( 3 *  ( j + 1 ) - 3 ) * nx + 2 *  ( j + 1 ) + 2 *  ( i + 1 ) - 3 - 1
      node[5] = node[4] + 1
      node[6] = node[4] + 2

      rho = 100.0 * rng.random ( )

      for krow in range ( 0, 8 ):
        for kcol in range ( 0, 8 ):
          row[k] = node[krow]
          col[k] = node[kcol]
          a[k] = rho * em[krow,kcol]
          k = k + 1

  return row, col, a

def wathen_st_size ( nx, ny ):

#*****************************************************************************80
#
## wathen_st_size(): Size of Wathen matrix stored in sparse triplet format.
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
#    John Burkardt.
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#  Output:
#
#    integer NZ_NUM, the number of items of data used to describe
#    the matrix.
#
  nz_num = nx * ny * 64

  return nz_num

def wathen_st_size_test ( ):

#*****************************************************************************80
#
## wathen_st_size_test() tests wathen_st_size().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, 1987, pages 449-457.
#
  print ( '' )
  print ( 'wathen_st_size_test():' )
  print ( '  wathen_st_size() returns NZ_NUM, the number of nonzeros' )
  print ( '  in a sparse triplet format for a Wathen finite element' )
  print ( '  matrix, given NX and NY, the number of rows and columns of' )
  print ( '  nodes in the underlying grid.' )
  print ( '' )
  print ( '       NX / NY: 1       2       3       4       5       6' )
  print ( '' )

  for ny in range ( 1, 11 ):
    print ( '       %2d' % ( ny ), end = '' )
    for nx in range ( 1, 7 ):
      n = wathen_st_size ( nx, ny )
      print ( '  %5d' % ( n ), end = '' )
    print ( '' )

  return

def wathen_xy ( nx, ny ):

#*****************************************************************************80
#
## wathen_xy(): coordinates of Wathen nodes.
#
#  Discussion:
#
#    We will take the region to be the unit square.
#
#    The grid uses quadratic serendipity elements.
#
#    Here is an illustration of the node numbering for NX = 3, NY = 2:
#
#     23-24-25-26-27-28-29
#      |     |     |     |
#     19    20    21    22
#      |     |     |     |
#     12-13-14-15-16-17-18
#      |     |     |     |
#      8     9    10    11
#      |     |     |     |
#      1--2--3--4--5--6--7
#
#    For this example, the total number of nodes is, as expected,
#
#      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#  Output:
#
#    real X(N), Y(N), the node coordinates.
#
  import numpy as np

  n = wathen_order ( nx, ny )

  x = np.zeros ( n )
  y = np.zeros ( n )

  k = 0
  for j in range ( 0, 2 * ny + 1 ):
    if ( np.mod ( j, 2 ) == 0 ):
      x[k:k+2*nx+1] = np.linspace ( 0.0, 1.0, 2*nx + 1 )
      y[k:k+2*nx+1] = ( j - 1 ) / ( 2 * ny ) 
      k = k + 2 * nx + 1 
    else:
      x[k:k+nx+1] = np.linspace ( 0.0, 1.0, nx + 1 ) 
      y[k:k+nx+1] = ( j - 1 ) / ( 2 * ny )
      k = k + nx + 1 

  return x, y

def wathen_xy_test ( ):

#*****************************************************************************80
#
## wathen_xy_test() tests wathen_xy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'wathen_xy_test():' )
  print ( '  wathen_xy() returns the (X,Y) coordinates of nodes.' )

  x, y = wathen_xy ( 5, 5 )

  plt.plot ( x, y, '*' )
  plt.title ( 'Node locations for a Wathen problem' )
  plt.xlabel ( '<-- x -->' )
  plt.ylabel ( '<-- y -->' )
  filename = 'wathen_xy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename, '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def wathen_test01 ( rng ):

#*****************************************************************************80
#
## wathen_test01() assembles, factor and solve using wathen_ge()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np
  import scipy.linalg as la

  print ( '' )
  print ( 'wathen_test01():' )
  print ( '  Assemble, factor and solve a Wathen system' )
  print ( '  defined by wathen_ge().' )
  print ( '' )

  nx = 4
  ny = 4
  print ( '  Elements in X direction NX = %d' % ( nx ) )
  print ( '  Elements in Y direction NY = %d' % ( ny ) )
  print ( '  Number of elements = %d' % ( nx * ny ) )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print ( '  Number of nodes N = %d' % ( n ) )
#
#  Set up a random solution X1.
#
  x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
  a = wathen_ge ( nx, ny, rng )
#
#  Compute the corresponding right hand side B.
#
  b = np.dot ( a, x1 )
#
#  Solve the linear system.
#
  x2 = la.solve ( a, b )
#
#  Compute the norm of the solution error.
#
  e = norm ( x1 - x2 )
  print ( '  Norm of solution error is %g' % ( e ) )

  return

def wathen_test02 ( rng ):

#*****************************************************************************80
#
## wathen_test02() assembles, factors and solves using wathen_csc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np
  import scipy.sparse.linalg as ssl

  print ( '' )
  print ( 'wathen_test02():' )
  print ( '  Assemble, factor and solve a Wathen system' )
  print ( '  defined by wathen_csc().' )
  print ( '' )

  nx = 4
  ny = 4

  print ( '  Elements in X direction NX = %d' % ( nx ) )
  print ( '  Elements in Y direction NY = %d' % ( ny ) )
  print ( '  Number of elements = %d' % ( nx * ny ) )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print ( '  Number of nodes N = %d' % ( n ) )
#
#  Set up a random solution X1.
#
  x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
  a = wathen_csc ( nx, ny, rng )
#
#  Compute the corresponding right hand side B.
#  Oddly enough, to compute A * x1 when A is sparse, you write A.dot(X1).
#
  b = a.dot ( x1 )
#
#  Solve the linear system.
#
  x2 = ssl.spsolve ( a, b )
#
#  Compute the norm of the solution error.
#
  e = norm ( x1 - x2 )
  print ( '  Norm of solution error is ', e )

  return

def wathen_test03 ( rng ):

#*****************************************************************************80
#
## wathen_test03() times wathen_ge() assembly and solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np
  import scipy.linalg as la
  import time
 
  print ( '' )
  print ( 'wathen_test03():' )
  print ( '  For various problem sizes,' )
  print ( '  time the assembly and factorization of a Wathen system' )
  print ( '  using wathen_ge().' )
  print ( '' )
  print ( '    NX  Elements   Nodes   Storage    Assembly      Factor      Error' )
  print ( '' )

  nx = 1
  ny = 1

  for test in range ( 0, 6 ):
#
#  Compute the number of unknowns.
#
    n = wathen_order ( nx, ny )
    storage_ge = n * n
#
#  Set up a random solution X1.
#
    x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
    t0 = time.perf_counter ( )
    a = wathen_ge ( nx, ny, rng )
    t1 = ( time.perf_counter ( ) - t0 )
#
#  Compute the corresponding right hand side B.
#
    b = np.dot ( a, x1 )
#
#  Solve the system.
#
    t0 = time.perf_counter ( )
    x2 = la.solve ( a, b )
    t2 = ( time.perf_counter ( ) - t0 )
#
#  Compute the norm of the solution error.
#
    e = norm ( x1 - x2 )
#
#  Report.
#
    print ( '  %4d      %4d  %6d  %8d  %10.2e  %10.2e  %10.2e' % \
      ( nx, nx * ny, n, storage_ge, t1, t2, e ) )
#
#  Ready for next iteration.
#
    nx = nx * 2
    ny = ny * 2

  return

def wathen_test04 ( rng ):

#*****************************************************************************80
#
## wathen_test04() times wathen_csc() assembly and solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np
  import scipy.sparse.linalg as ssl
  import time

  print ( '' )
  print ( 'wathen_test04():' )
  print ( '  For various problem sizes,' )
  print ( '  time the assembly and factorization of a Wathen system' )
  print ( '  using the wathen_csc() function.' )
  print ( '' )
  print ( '    NX  Elements   Nodes    Assembly      Factor      Error' )
  print ( '' )

  nx = 1
  ny = 1

  for test in range ( 0, 7 ):
#
#  Compute the number of unknowns.
#
    n = wathen_order ( nx, ny )
#
#  Set up a random solution X1.
#
    x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
    t0 = time.perf_counter ( )
    a = wathen_csc ( nx, ny, rng )
    t1 = ( time.perf_counter ( ) - t0 )
#
#  Compute the corresponding right hand side B.
#
    b = a.dot ( x1 )
#
#  Solve the system.
#
    t0 = time.perf_counter ( )
    x2 = ssl.spsolve ( a, b )
    t2 = ( time.perf_counter ( ) - t0 )
#
#  Compute the norm of the solution error.
#
    e = norm ( x1 - x2 )
#
#  Report.
#
    print ( '  %4d      %4d  %6d  %10.2e  %10.2e  %10.2e' % \
      ( nx, nx * ny, n, t1, t2, e ) )
#
#  Ready for next iteration.
#
    nx = nx * 2
    ny = ny * 2

  return

def wathen_test05 ( rng ):

#*****************************************************************************80
#
## wathen_test05() times wathen_ge() and wathen_csc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np
  import scipy.linalg as la
  import scipy.sparse.linalg as ssl
  import time

  print ( '' )
  print ( 'wathen_test05():' )
  print ( '  For various problem sizes, ' )
  print ( '  time the assembly and factorization of a Wathen system' )
  print ( '  wathen_ge() and wathen_csc().' )
  print ( '' )
  print ( '                   NX  Elements   Nodes    Assembly      Factor      Error' )

  nx = 1
  ny = 1

  for test in range ( 0, 6 ):
#
#  Compute the number of unknowns.
#
    n = wathen_order ( nx, ny )
#
#  Set up a random solution X1.
#
    x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
    t0 = time.perf_counter ( )
    a = wathen_ge ( nx, ny, rng )
    t1 = time.perf_counter ( ) - t0
#
#  Compute the corresponding right hand side B.
#
    b = np.dot ( a, x1 )
#
#  Solve the system.
#
    t0 = time.perf_counter ( )
    x2 = la.solve ( a, b )
    t2 = time.perf_counter ( ) - t0
#
#  Compute the maximum solution error.
#
    e = norm ( x1 - x2 )
#
#  Report.
#
    print ( '' )
    print ( '  wathen_ge()    %4d      %4d  %6d  %10.2e  %10.2e  %10.2e' \
      % ( nx, nx * ny, n, t1, t2, e ) )
#
#  Compute the matrix.
#
    t0 = time.perf_counter ( )
    a = wathen_csc ( nx, ny, rng )
    t1 = time.perf_counter ( ) - t0
#
#  Solve the system.
#
    t0 = time.perf_counter ( )
    x2 = ssl.spsolve ( a, b )
    t2 = time.perf_counter ( ) - t0
#
#  Compute the maximum solution error.
#
    e = norm ( x1 - x2 )
#
#  Report.
#
    print ( '  wathen_csc()   %4d      %4d  %6d  %10.2e  %10.2e  %10.2e' \
      % ( nx, nx * ny, n, t1, t2, e ) )
#
#  Ready for next iteration.
#
    nx = nx * 2
    ny = ny * 2

  return

def wathen_test06 ( rng ):

#*****************************************************************************80
#
## wathen_test06() assembles, factor and solves using wathen_ge() + cg_ge().
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
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np

  print ( '' )
  print ( 'wathen_test06():' )
  print ( '  Assemble, factor and solve a Wathen system' )
  print ( '  defined by wathen_ge() and cg_ge().' )
  print ( '' )

  nx = 2
  ny = 2
  print ( '  Elements in X direction NX = %d' % ( nx ) )
  print ( '  Elements in Y direction NY = %d' % ( ny ) )
  print ( '  Number of elements = %d' % ( nx * ny ) )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print ( '  Number of nodes N = %d' % ( n ) )
#
#  Set up a random solution X1.
#
  x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
  a = wathen_ge ( nx, ny, rng )
#
#  Compute the corresponding right hand side B.
#
  b = np.dot ( a, x1 )
#
#  Solve the linear system.
#
  x2 = np.ones ( n )
  x2 = cg_ge ( n, a, b, x2 )
#
#  Compute the maximum solution error.
#
  e = norm ( x1 - x2 )

  print ( '  Maximum solution error is %g' % ( e ) )

  return

def wathen_test07 ( rng ):

#*****************************************************************************80
#
## wathen_test07() assembles, factor and solves using wathen_csc() + cg_csc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np

  print ( '' )
  print ( 'wathen_test07():' )
  print ( '  Assemble, factor and solve a Wathen system' )
  print ( '  defined by wathen_csc() and cg_csc().' )
  print ( '' )

  nx = 2
  ny = 2
  print ( '  Elements in X direction NX = %d' % ( nx ) )
  print ( '  Elements in Y direction NY = %d' % ( ny ) )
  print ( '  Number of elements = %d' % ( nx * ny ) )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print ( '  Number of nodes N = %d' % ( n ) )
#
#  Set up a random solution X1.
#
  x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
  a = wathen_csc ( nx, ny, rng )
#
#  Compute the corresponding right hand side B.
#
  b = a.dot ( x1 )
#
#  Solve the linear system.
#
  x2 = np.ones ( n )
  x2 = cg_csc ( n, a, b, x2 )
#
#  Compute the maximum solution error.
#
  e = norm ( x1 - x2 )
  print ( '  Maximum solution error is %g' % ( e ) )

  print ( '  Normal end of execution.' )
  return

def wathen_test08 ( rng ):

#*****************************************************************************80
#
## wathen_test08() assemble, factor and solve using wathen_st() + cg_st().
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
#    rng(): the current random number generator.
#
  from numpy.linalg import norm
  import numpy as np

  print ( '' )
  print ( 'wathen_test08():' )
  print ( '  Assemble, factor and solve a Wathen system' )
  print ( '  defined by wathen_st() and cg_st().' )
  print ( '' )

  nx = 1
  ny = 1
  print ( '  Elements in X direction NX = %d' % ( nx ) )
  print ( '  Elements in Y direction NY = %d' % ( ny ) )
  print ( '  Number of elements = %d' % ( nx * ny ) )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print ( '  Number of nodes N = %d' % ( n ) )
#
#  Compute the matrix size.
#
  nz_num = wathen_st_size ( nx, ny )
  print ( '  Number of nonzeros = %d\n' % ( nz_num ) )
#
#  Set up a random solution X1.
#
  x1 = rng.random ( size = n )
#
#  Compute the matrix.
#
  row, col, a = wathen_st ( nx, ny, rng )
#
#  Compute the corresponding right hand side B.
#
  b = mv_st ( n, n, nz_num, row, col, a, x1 )
#
#  Solve the linear system.
#
  x2 = np.ones ( n )
  x2 = cg_st ( n, nz_num, row, col, a, b, x2 )
#
#  Compute the solution error norm.
#
  e = norm ( x1 - x2 )
  print ( '  Maximum solution error is %g' % ( e ) )

  return

def wathen_test09 ( rng ):

#*****************************************************************************80
#
## wathen_test09() uses spy() to display the sparsity of the Wathen matrix.
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
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'wathen_test09():' )
  print ( '  Display the sparsity of the Wathen matrix.' )

  fig = plt.figure ( )
  nx = 1
  ny = 1
  n = wathen_order ( nx, ny )
  a = wathen_ge ( nx, ny, rng )
  ax1 = fig.add_subplot ( 231 )
  ax1.spy ( a, markersize = 4 )

  nx = 2
  ny = 2
  n = wathen_order ( nx, ny )
  a = wathen_ge ( nx, ny, rng )
  ax2 = fig.add_subplot ( 232 )
  ax2.spy ( a, markersize = 4 )

  nx = 3
  ny = 3
  n = wathen_order ( nx, ny )
  a = wathen_ge ( nx, ny, rng )
  ax3 = fig.add_subplot ( 233 )
  ax3.spy ( a, markersize = 4 )

  nx = 4
  ny = 4
  n = wathen_order ( nx, ny )
  a = wathen_ge ( nx, ny, rng )
  ax4 = fig.add_subplot ( 234 )
  ax4.spy ( a, markersize = 4 )

  nx = 5
  ny = 5
  n = wathen_order ( nx, ny )
  a = wathen_ge ( nx, ny, rng )
  ax5 = fig.add_subplot ( 235 )
  ax5.spy ( a, markersize = 4 )

  nx = 6
  ny = 6
  n = wathen_order ( nx, ny )
  a = wathen_ge ( nx, ny, rng )
  ax6 = fig.add_subplot ( 236 )
  ax6.spy ( a, markersize = 4 )

  fig.suptitle ( 'WATHEN Matrix Sparsity Pattern' )

  plt.show ( block = False )

  filename = 'wathen_spy.png'
  fig.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.close ( )

  return

def wathen_matrix_test ( ):

#*****************************************************************************80
#
## wathen_matrix_test() tests wathen_matrix().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'wathen_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test wathen_matrix().' )

  rng = default_rng ( )
#
#  Direct Solve
#
  wathen_test01 ( rng )
  wathen_test02 ( rng )
#
#  Timings.
#
  wathen_test03 ( rng )
  wathen_test04 ( rng )
  wathen_test05 ( rng )
#
#  CG Solve
#
  wathen_test06 ( rng )
  wathen_test07 ( rng )
  wathen_test08 ( rng )
#
#  Use SPY to display the sparsity of the matrix.
#
  wathen_test09 ( rng )

  wathen_order_test ( )
  wathen_st_size_test ( )

  wathen_xy_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'wathen_matrix_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  wathen_matrix_test ( )
  timestamp ( )

