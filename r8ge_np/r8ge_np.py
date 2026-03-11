#! /usr/bin/env python3
#
def r8ge_np_test ( ):

#*****************************************************************************80
#
## r8ge_np_test() tests r8ge_np().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ge_np_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ge_np().' )

  r8ge_np_det_test ( )
  r8ge_np_fa_test ( )
  r8ge_np_inverse_test ( )
  r8ge_np_ml_test ( )
  r8ge_np_sl_test ( )
  r8ge_np_trf_test ( )
  r8ge_np_trm_test ( )
  r8ge_np_trs_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8ge_np_test():' )
  print ( '  Normal end of execution.' )
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
#    real  C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = np.zeros ( [ n1, n3 ] )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

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

def r8ge_random ( m, n ):

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
#  Output:
#
#    real A(M,N), the R8GE matrix.
#
  from numpy.random import default_rng
  import numpy as np
 
  rng = default_rng ( )

  a = rng.random ( size = [ m, n ] )

  return a

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

def r8ge_np_det ( n, a_lu ):

#*****************************************************************************80
#
## R8GE_NP_DET computes the determinant of a matrix factored by R8GE_NP_FA.
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
#    06 June 2016
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
#    real A_LU(N,N), the LU factors from R8GE_NP_FA.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for i in range ( 0, n ):
    det = det * a_lu[i,i]

  return det

def r8ge_np_det_test ( ):

#*****************************************************************************80
#
## R8GE_NP_DET_TEST tests R8GE_NP_DET.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R8GE_NP_DET_TEST' )
  print ( '  R8GE_NP_DET computes the determinant of a matrix' )
  print ( '  that was factored by R8GE_NP_FA,' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ge_dif2 ( n, n )
#
#  Factor the matrix.
#
  a, info = r8ge_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_np_det_test(): Fatal error!' )
    print ( '  R8GE_NP_FA declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_det_test(): Fatal error!' )
#
#  Get the determinant.
#
  det = r8ge_np_det ( n, a )
  print ( '' )
  print ( '  Determinant of -1, 2, -1 matrix is ', det )
  print ( '  Exact value is ', n + 1 )

  return

def r8ge_np_fa ( n, a ):

#*****************************************************************************80
#
## R8GE_NP_FA factors a R8GE matrix by nonpivoting Gaussian elimination.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_NP_FA is a version of the LINPACK routine R8GEFA, but uses no
#    pivoting.  It will fail if the matrix is singular, or if any zero
#    pivot is encountered.
#
#    If R8GE_NP_FA successfully factors the matrix, R8GE_NP_SL may be called
#    to solve linear systems involving the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
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
#    real A(N,N), the matrix to be factored.
#
#  Output:
#
#    real A_LU(N,N), information about the factorization,
#    which must be passed unchanged to R8GE_NP_SL for solutions.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  a_lu = a.copy ( )
  info = 0

  for k in range ( 1, n ):

    if ( a_lu[k-1,k-1] == 0.0 ):
      info = k
      print ( '' )
      print ( 'R8GE_NP_FA - Fatal error!' )
      print ( '  Zero pivot on step ', info )
      raise Exception ( 'r8ge_np_fa(): Fatal error!' )

    for i in range ( k + 1, n + 1 ):
      a_lu[i-1,k-1] = - a_lu[i-1,k-1] / a_lu[k-1,k-1]

    for j in range ( k + 1, n + 1 ):
      for i in range ( k + 1, n + 1 ):
        a_lu[i-1,j-1] = a_lu[i-1,j-1] + a_lu[i-1,k-1] * a_lu[k-1,j-1]

  if ( a_lu[n-1,n-1] == 0.0 ):
    info = n
    print ( '' )
    print ( 'R8GE_NP_FA - Fatal error!' )
    print ( '  Zero pivot on step ', info )
    raise Exception ( 'r8ge_np_fa(): Fatal error!' )

  return a_lu, info

def r8ge_np_fa_test ( ):

#*****************************************************************************80
#
## R8GE_NP_FA_TEST tests R8GE_NP_FA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'R8GE_NP_FA_TEST' )
  print ( '  R8GE_NP_FA LU factors an R8GE matrix without pivoting.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
  x = np.ones ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8ge_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_FA_TEST - Fatal error!' )
    print ( '  R8GE_NP_FA declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_fa_test(): Fatal error!' )
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_np_sl ( n, a_lu, b, job )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_np_ml ( n, a_lu, x, job )
#
#  Solve the system
#
  job = 0
  x = r8ge_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_np_ml ( n, a_lu, x, job )
#
#  Solve the system
#
  job = 1
  x = r8ge_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_np_inverse ( n, a_lu ):

#*****************************************************************************80
#
## R8GE_NP_INVERSE computes the inverse of a matrix factored by R8GE_NP_FA.
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
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix A.
#
#    real A_LU(N,N), the factor information computed by R8GE_NP_FA.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np

  b = a_lu.copy ( )
#
#  Compute Inverse(U).
#
  for k in range ( 1, n + 1 ):

    b[k-1,k-1] = 1.0 / b[k-1,k-1]
    for i in range ( 1, k ):
      b[i-1,k-1] = - b[i-1,k-1] * b[k-1,k-1]

    for j in range ( k + 1, n + 1 ):
      temp = b[k-1,j-1]
      b[k-1,j-1] = 0.0
      for i in range ( 1, k + 1 ):
        b[i-1,j-1] = b[i-1,j-1] + temp * b[i-1,k-1]
#
#  Form Inverse(U) * Inverse(L).
#
  work = np.zeros ( n )

  for k in range ( n - 1, 0, -1 ):

    for i in range ( k + 1, n + 1 ):
      work[i-1] = b[i-1,k-1]
      b[i-1,k-1] = 0.0

    for j in range ( k + 1, n + 1 ):
      for i in range ( 1, n + 1 ):
        b[i-1,k-1] = b[i-1,k-1] + b[i-1,j-1] * work[j-1]

  return b

def r8ge_np_inverse_test ( ):

#*****************************************************************************80
#
## R8GE_NP_INVERSE_TEST tests R8GE_NP_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8GE_NP_INVERSE_TEST' )
  print ( '  R8GE_NP_INVERSE computes the inverse of a matrix' )
  print ( '  that was factored by R8GE_NP_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )

  print ( '' )
  print ( '  The R8GE random matrix, A' )
  print ( a )
#
#  Factor and invert the matrix.
#
  a_lu, info = r8ge_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_INVERSE_TEST - Fatal error!' )
    print ( '  R8GE_NP_FA declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_inverse_test(): Fatal error!' )

  b = r8ge_np_inverse ( n, a_lu )

  print ( '' )
  print ( '  The inverse matrix, B' )
  print ( b )
#
#  Compute A * B = C.
#
  c = r8ge_mm ( n, n, n, a, b )

  print ( '' )
  print ( '  C = A * B, the product' )
  print ( c )

  return

def r8ge_np_ml ( n, a_lu, x, job ):

#*****************************************************************************80
#
## R8GE_NP_ML computes A * x or x * A, for a matrix factored by R8GE_NP_FA.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    The matrix A is assumed to have been factored by R8GE_NP_FA.
#
#    R8GE_NP_ML allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
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
#    real A_LU(N,N), the matrix factors computed by R8GE_NP_FA.
#
#    real X(N), the vector to be multiplied.
#
#    integer JOB, determines the multiplication to
#    be carried out:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * X.
#
#  Output:
#
#    real B(N), the result of the multiplication.
#
  import numpy as np

  b = x.copy ( )

  if ( job == 0 ):
#
#  Compute U * X = Y:
#
    for i in range ( 1, n + 1 ):
      t = 0.0
      for j in range ( i, n + 1 ):
        t = t + a_lu[i-1,j-1] * b[j-1]
      b[i-1] = t
#
#  Compute L * Y = B:
#
    for j in range ( n - 1, 0, -1 ):
      for i in range ( j + 1, n + 1 ):
        b[i-1] = b[i-1] - a_lu[i-1,j-1] * b[j-1]

  else:
#
#  Compute L' * X = Y:
#
    for j in range ( 1, n ):
      for i in range ( j + 1, n + 1 ):
        b[j-1] = b[j-1] - b[i-1] * a_lu[i-1,j-1]
#
#  Compute U' * Y = B:
#
    for j in range ( n, 0, -1 ):
      t = 0.0
      for i in range ( 1, j + 1 ):
        t = t + b[i-1] * a_lu[i-1,j-1]
      b[j-1] = t

  return b

def r8ge_np_ml_test ( ):

#*****************************************************************************80
#
## R8GE_NP_ML_TEST tests R8GE_NP_ML.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R8GE_NP_ML_TEST' )
  print ( '  R8GE_NP_ML computes A*x or A\'*x for a matrix A' )
  print ( '  already factored by R8GE_NP_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

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
    a_lu, info = r8ge_np_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8GE_NP_ML_TEST - Fatal error!' )
      print ( '  R8GE_NP_FA declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'r8ge_np_ml_test(): Fatal error!' )
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8ge_np_ml ( n, a_lu, x, job )

    if ( job == 0 ):
      r8vec2_print ( b, b2, '  A*x and PLU*x' )
    else:
      r8vec2_print ( b, b2, '  A\'*x and (PLU)\'*x' )

  return

def r8ge_np_sl ( n, a_lu, b, job ):

#*****************************************************************************80
#
## R8GE_NP_SL solves a system factored by R8GE_NP_FA.
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
#    06 June 2016
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
#    real A_LU(N,N), the matrix as factored by R8GE_NP_FA.
#
#    real B(N), the right hand side vector B.
#
#    integer JOB.
#    If JOB is zero, the routine will solve A * x = b.
#    If JOB is nonzero, the routine will solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution.
#
  x = b.copy ( )
#
#  Solve A * x = b.
#
  if ( job == 0 ):

    for k in range ( 1, n ):
      for i in range ( k + 1, n + 1 ):
        x[i-1] = x[i-1] + a_lu[i-1,k-1] * x[k-1]

    for k in range ( n, 0, -1 ):
      x[k-1] = x[k-1] / a_lu[k-1,k-1]
      for i in range ( 1, k ):
        x[i-1] = x[i-1] - a_lu[i-1,k-1] * x[k-1]
#
#  Solve A' * X = B.
#
  else:

    for k in range ( 1, n + 1 ):
      t = 0.0
      for i in range ( 1, k ):
        t = t + x[i-1] * a_lu[i-1,k-1]
      x[k-1] = ( x[k-1] - t ) / a_lu[k-1,k-1]

    for k in range ( n - 1, 0, -1 ):
      for i in range ( k + 1, n + 1 ):
        x[k-1] = x[k-1] + x[i-1] * a_lu[i-1,k-1]

  return x

def r8ge_np_sl_test ( ):

#*****************************************************************************80
#
## R8GE_NP_SL_TEST tests R8GE_NP_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'R8GE_NP_SL_TEST' )
  print ( '  R8GE_NP_SL solves a linear system factored by R8GE_NP_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ge_random ( n, n )
#
#  Set the desired solution.
#
  x = np.ones ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8ge_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_SL_TEST - Fatal error!' )
    print ( '  R8GE_NP_FA declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_sl_test(): Fatal error!' )
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_np_sl ( n, a_lu, b, job )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_np_ml ( n, a_lu, x, job )
#
#  Solve the system
#
  job = 0
  x = r8ge_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_np_ml ( n, a_lu, x, job )
#
#  Solve the system
#
  job = 1
  x = r8ge_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_np_trf ( m, n, a ):

#*****************************************************************************80
#
## R8GE_NP_TRF computes the LU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_NP_TRF is a nonpivoting version of R8GE_TRF, and will fail if
#    a zero element is encountered along the diagonal.
#
#    The factorization has the form
#      A = L * U
#    where L is lower triangular with unit diagonal elements (lower
#    trapezoidal if N < M), and U is upper triangular (upper trapezoidal
#    if M < N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix A.  0 <= M.
#
#    integer N, the number of columns of the matrix A.  0 <= N.
#
#    real A(M,N), the matrix to be factored.
#
#  Output:
#
#    real A_LU(M,N), the factors L and U from the factorization
#    A = L*U the unit diagonal elements of L are not stored.
#
#    integer INFO.
#    = 0: successful exit
#    < 0: if INFO = -K, the K-th argument had an illegal value
#    > 0: if INFO = K, U(K,K) is exactly zero. The factorization
#         has been completed, but the factor U is exactly
#         singular, and division by zero will occur if it is used
#         to solve a system of equations.
#
  info = 0
  a_lu = a.copy ( )
#
#  Test the input.
#
  if ( m < 0 ):
    info = -1
    print ( '' )
    print ( 'R8GE_NP_TRF - Fatal error!' )
    print ( '  M < 0.' )
    raise Exception ( 'r8ge_np_trf(): Fatal error!' )

  if ( n < 0 ):
    info = -2
    print ( '' )
    print ( 'R8GE_NP_TRF - Fatal error!' )
    print ( '  n < 0.' )
    raise Exception ( 'r8ge_np_trf(): Fatal error!' )

  if ( m == 0 or n == 0 ):
    return a_lu, info

  for j in range ( 1, min ( m, n ) + 1 ):
#
#  Compute elements J+1:M of the J-th column.
#
    if ( a[j-1,j-1] != 0.0 ):
      for i in range ( j + 1, m + 1 ):
        a_lu[i-1,j-1] = a_lu[i-1,j-1] / a_lu[j-1,j-1]
    elif ( info == 0 ):
      info = j
#
#  Update the trailing submatrix.
#
    if ( j < min ( m, n ) ):

      for ii in range ( j + 1, m + 1 ):
        for k in range ( j + 1, n + 1 ):
          a_lu[ii-1,k-1] = a_lu[ii-1,k-1] - a_lu[ii-1,j-1] * a_lu[j-1,k-1]

  return a_lu, info

def r8ge_np_trf_test ( ):

#*****************************************************************************80
#
## R8GE_NP_TRF_TEST tests R8GE_NP_TRF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 10
  n = m
  nrhs = 1

  print ( '' )
  print ( 'R8GE_NP_TRF_TEST' )
  print ( '  R8GE_NP_TRF factors an R8GE matrix without pivoting,' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
#
#  Set the matrix.
#
  a = r8ge_random ( m, n )
#
#  Set the desired solution.
#
  x = np.ones ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( m, n, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8ge_np_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRF_TEST - Fatal error!' )
    print ( '  R8GE_NP_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trf_test(): Fatal error!' )
#
#  Solve the linear system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'N', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )
   
  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRF_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trf_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_np_trm ( m, n, a_lu, x, job )
#
#  Solve the system
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'N', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRF_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trf_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_np_trm ( m, n, a_lu, x, job )
#
#  Solve the system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'T', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_np_trf_test(): Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trf_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_np_trm ( m, n, a_lu, x, job ):

#*****************************************************************************80
#
## R8GE_NP_TRM computes A * x or A' * x, for a matrix factored by R8GE_NP_TRF.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    The matrix A is assumed to have been factored by R8GE_NP_TRF.
#
#    R8GE_NP_TRM allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
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
#    integer M, N, the number of rows and columns in the matrix.
#    M and N must be positive.
#
#    real A_LU(M,N), the M by N matrix factors computed by R8GE_NP_TRF.
#
#    real X(*), the vector to be multiplied.
#    If JOB is 0, X must have dimension N.
#    If JOB is nonzero, X must have dimension M.
#
#    integer JOB, determines the multiplication to
#    be carried out:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * X.
#
#  Output:
#
#    real B(*), the result of the multiplication.
#    If JOB is 0, B must have dimension M.
#    If JOB is nonzero, B must have dimension N.
#
  import numpy as np

  if ( job == 0 ):

    b = np.zeros ( m )
#
#  Compute U * X = Y:
#
    for i in range ( 1, m + 1 ):
      for j in range ( i, n + 1 ):
        b[i-1] = b[i-1] + a_lu[i-1,j-1] * x[j-1]
#
#  Compute L * Y = B:
#
    for i in range ( min ( m, n + 1 ), 1, -1 ):
      t = 0.0
      for j in range ( 1, i ):
        t = t + a_lu[i-1,j-1] * b[j-1]
      b[i-1] = b[i-1] + t

  else:

    b = np.zeros ( n )
#
#  Compute L' * X = Y:
#
    for i in range ( 1, min ( m, n ) + 1 ):
      b[i-1] = x[i-1]
      for j in range ( i + 1, m + 1 ):
        b[i-1] = b[i-1] + x[j-1] * a_lu[j-1,i-1]
#
#  Compute U' * Y = B:
#
    for j in range ( min ( m, n ), 0, -1 ):
      t = 0.0;
      for i in range ( 1, j + 1 ):
        t = t + b[i-1] * a_lu[i-1,j-1]
      b[j-1] = t

  return b

def r8ge_np_trm_test ( ):

#*****************************************************************************80
#
## R8GE_NP_TRM_TEST tests R8GE_NP_TRM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 10
  n = m
  nrhs = 1

  print ( '' )
  print ( 'R8GE_NP_TRM_TEST' )
  print ( '  R8GE_NP_TRM computes A*x after A has been factored by R8GE_NP_TRF.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
#
#  Set the matrix.
#
  a = r8ge_random ( m, n )
#
#  Set the desired solution.
#
  x = np.ones ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( m, n, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8ge_np_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_np_trm_test(): Fatal error!' )
    print ( '  R8GE_NP_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trm_test(): Fatal error!' )
#
#  Solve the linear system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'N', a_lu, b_mat )
   
  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRM_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trm_test(): Fatal error!' )

  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_np_trm ( m, n, a_lu, x, job )
#
#  Solve the system
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'N', a_lu, b_mat )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRM_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trm_test(): Fatal error!' )

  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_np_trm ( m, n, a_lu, x, job )
#
#  Solve the system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'T', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRM_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trm_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution of transposed system:' )

  return

def r8ge_np_trs ( n, nrhs, trans, a_lu, b ):

#*****************************************************************************80
#
## R8GE_NP_TRS solves a system of linear equations factored by R8GE_NP_TRF.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_NP_TRS is a nonpivoting version of R8GE_TRS.
#
#    R8GE_TRS solves a system of linear equations
#      A * x = b  or  A' * X = B
#    with a general N by N matrix A using the LU factorization computed
#    by R8GE_NP_TRF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
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
#    integer N, the order of the matrix A.  0 <= N.
#
#    integer NRHS, the number of right hand sides.  0 <= NRHS.
#
#    character TRANS, specifies the form of the system of equations:
#    'N':  A * x = b  (No transpose)
#    'T':  A'* X = B  (Transpose)
#    'C':  A'* X = B  (Conjugate transpose = Transpose)
#
#    real A_LU(N,N), the LU factors from R8GE_NP_TRF.
#
#    real B(N,NRHS), the right hand side matrix B.
#
#  Output:
#
#    real X(N,NRHS), the solution matrix X.
#
#    integer INFO
#    = 0:  successful exit
#    < 0:  if INFO = -I, the I-th argument had an illegal value.
#
  info = 0
  x = b.copy ( )

  if ( trans != 'n' and \
       trans != 'N' and \
       trans != 't' and \
       trans != 'T' and \
       trans != 'c' and \
       trans != 'C' ):
    info = -1
    raise Exception ( 'r8ge_np_trs(): Fatal error!' )

  if ( n < 0 ):
    info = -2
    raise Exception ( 'r8ge_np_trs(): Fatal error!' )

  if ( nrhs < 0 ):
    info = -3
    raise Exception ( 'r8ge_np_trs(): Fatal error!' )

  if ( n == 0 or nrhs == 0 ):
    return x, info

  if ( trans == 'n' or trans == 'N' ):
#
#  Solve L * x = b, overwriting b with x.
#
    for k in range ( 1, nrhs + 1 ):
      for j in range ( 1, n ):
        for i in range ( j + 1, n + 1 ):
          x[i-1,k-1] = x[i-1,k-1] - a_lu[i-1,j-1] * x[j-1,k-1]
#
#  Solve U * x = b, overwriting b with x.
#
    for k in range ( 1, nrhs + 1 ):
      for j in range ( n, 0, -1 ):
        x[j-1,k-1] = x[j-1,k-1] / a_lu[j-1,j-1]
        for i in range ( 1, j ):
          x[i-1,k-1] = x[i-1,k-1] - a_lu[i-1,j-1] * x[j-1,k-1]

  else:
#
#  Solve U' * x = b, overwriting b with x.
#
    for k in range ( 1, nrhs + 1 ):
      for j in range ( 1, n + 1 ):
        x[j-1,k-1] = x[j-1,k-1] / a_lu[j-1,j-1]
        for i in range ( j + 1, n + 1 ):
          x[i-1,k-1] = x[i-1,k-1] - a_lu[j-1,i-1] * x[j-1,k-1]
#
#  Solve L' * x = b, overwriting b with x.
#
    for k in range ( 1, nrhs + 1 ):
      for j in range ( n, 1, -1 ):
        for i in range ( 1, j ):
          x[i-1,k-1] = x[i-1,k-1] - a_lu[j-1,i-1] * x[j-1,k-1]

  return x, info

def r8ge_np_trs_test ( ):

#*****************************************************************************80
#
## R8GE_NP_TRS_TEST tests R8GE_NP_TRS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 10
  n = m
  nrhs = 1

  print ( '' )
  print ( 'R8GE_NP_TRS_TEST' )
  print ( '  R8GE_NP_TRS solves a linear system factored by R8GE_NP_TRF.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
#
#  Set the matrix.
#
  a = r8ge_random ( m, n )
#
#  Set the desired solution.
#
  x = np.ones ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( m, n, a, x )
#
#  Factor the matrix.
#
  a_lu, info = r8ge_np_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRS_TEST - Fatal error!' )
    print ( '  R8GE_NP_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trs_test(): Fatal error!' )
#
#  Solve the linear system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'N', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )
   
  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRS_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trs_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_np_trm ( m, n, a_lu, x, job )
#
#  Solve the system
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'N', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_NP_TRS_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trs_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_np_trm ( m, n, a_lu, x, job )
#
#  Solve the system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8ge_np_trs ( n, nrhs, 'T', a_lu, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8ge_np_trs_test(): Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8ge_np_trs_test(): Fatal error!' )

  r8vec_print ( n, x, '  Solution of transposed system:' )

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
  r8ge_np_test ( )
  timestamp ( )

