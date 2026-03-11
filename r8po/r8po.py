#! /usr/bin/env python3
#
def r8po_test ( ):

#*****************************************************************************80
#
## r8po_test() tests r8po().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8po_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8po().' )

  rng = default_rng ( )

  r8ge_to_r8po_test ( rng )

  r8po_det_test ( )
  r8po_dif2_test ( )
  r8po_fa_test ( )
  r8po_indicator_test ( )
  r8po_inverse_test ( )
  r8po_ml_test ( )
  r8po_mm_test ( )
  r8po_mv_test ( )
  r8po_print_test ( )
  r8po_print_some_test ( )
  r8po_random_test ( rng )
  r8po_sl_test ( )
  r8po_to_r8ge_test ( rng )
  r8po_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8po_test():' )
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

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      b[i,j] = a[i,j]

  return b

def r8ge_to_r8po_test ( rng ):

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
#    12 August 2022
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
  print ( 'r8ge_to_r8po_test():' )
  print ( '  r8ge_to_r8po() converts an R8GE matrix to R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = rng.random ( size = [ n, n ] )

  print ( '' )
  print ( '  The random R8GE matrix:' )
  print ( a )
 
  b = r8ge_to_r8po ( n, a )

  print ( '' )
  print ( '  The R8PO matrix:' )
  print ( b )

  return

def r8po_det ( n, a_lu ):

#*****************************************************************************80
#
## r8po_det() computes the determinant of a matrix factored by R8PO_FA.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A_LU(N,N), the factor from R8PO_FA.
#
#  Output:
#
#    real VALUE, the determinant of A.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i] ** 2

  return value

def r8po_det_test ( ):

#*****************************************************************************80
#
## R8PO_DET_TEST tests R8PO_DET;
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
  import platform

  n = 5

  print ( '' )
  print ( 'R8PO_DET_TEST' )
  print ( '  R8PO_DET finds the determinant of a positive definite symmetric' )
  print ( '  matrix after it has been factored.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = min ( i, j ) + 1

  r8po_print ( n, a, '  The matrix A:' )
#
#  Get R, the Cholesky factor of A.
#
  r = r8po_fa ( n, a )
#
#  Get the determinant of A.
#
  value = r8po_det ( n, r )
  print ( '' )
  print ( '  Determinant of A = ', value )

  return

def r8po_dif2 ( n ):

#*****************************************************************************80
#
## R8PO_DIF2 returns the second difference matrix in R8PO format.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  return a

def r8po_dif2_test ( ):

#*****************************************************************************80
#
## R8PO_DIF2_TEST tests R8PO_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'R8PO_DIF2_TEST' )
  print ( '  R8PO_DIF2 returns the second difference matrix in R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8po_dif2 ( n )

  r8po_print ( n, a, '  The matrix:' )

  return

def r8po_fa ( n, a ):

#*****************************************************************************80
#
## r8po_fa() factors a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#    The positive definite symmetric matrix A has a Cholesky factorization
#    of the form:
#
#      A = R' * R
#
#    where R is an upper triangular matrix with positive elements on
#    its diagonal.  This routine overwrites the matrix A with its
#    factor R.
#
#    This function failed miserably when I wrote "r = a", because of a
#    disastrously misconceived feature of Python, which does not copy
#    one matrix to another, but makes them both point to the same object.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2024
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix in R8PO storage.
#
#  Output:
#
#    real R(N,N), the Cholesky factor R in R8GE storage.
#
#    integer INFO, error flag.
#    0, normal return.
#    K, error condition.  The principal minor of order K is not
#    positive definite, and the factorization was not completed.
#
  import numpy as np

  r = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      r[i,j] = a[i,j]

  for j in range ( 0, n ):

    for k in range ( 0, j ):
      t = 0.0
      for i in range ( 0, k ):
        t = t + r[i,k] * r[i,j]
      r[k,j] = ( r[k,j] - t ) / r[k,k]

    t = 0.0
    for i in range ( 0, j ):
      t = t + r[i,j] ** 2

    s = r[j,j] - t

    if ( s <= 0.0 ):
      print ( '' )
      print ( 'r8po_fa(): Fatal error!' )
      print ( '  Factorization fails on column', j )
      raise Exception ( 'r8po_fa(): Fatal error!' )

    r[j,j] = np.sqrt ( s )
#
#  Since the Cholesky factor is stored in R8GE format, be sure to
#  zero out the lower triangle.
#
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      r[i,j] = 0.0

  return r

def r8po_fa_test ( ):

#*****************************************************************************80
#
## r8po_fa_test() tests r8po_fa();
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

  n = 5

  print ( '' )
  print ( 'R8PO_FA_TEST' )
  print ( '  R8PO_FA factors a positive definite symmetric linear system,' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = min ( i, j ) + 1

  r8po_print ( n, a, '  The matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )

  print ( '' )
  print ( '  The factor R (a R8UT matrix):' )
  print ( r )
#
#  Compute the product R' * R.
#
  rtr = r8ut_mtm ( n, r, r )

  print ( '' )
  print ( '  The product R\' * R:' )
  print ( rtr )

  return

def r8po_indicator ( n ):

#*****************************************************************************80
#
## R8PO_INDICATOR sets up a R8PO indicator matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    integer N, the number of rows and columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(N,N), the R8PO matrix.
#
  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8po_indicator_test ( ):

#*****************************************************************************80
#
## R8PO_INDICATOR_TEST tests R8PO_INDICATOR.
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
  n = 5

  print ( '' )
  print ( 'r8po_indicator_test' )
  print ( '  r8po_indicator sets up an R8PO indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8po_indicator ( n )

  r8po_print ( n, a, '  The R8PO indicator matrix:' )

  return

def r8po_inverse ( n, r ):

#*****************************************************************************80
#
## R8PO_INVERSE computes the inverse of a matrix factored by R8PO_FA.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    integer N, the order of the matrix.
#
#    real R(N,N), the Cholesky factor, in R8GE storage, returned by R8PO_FA.
#
#  Output:
#
#    real B(N,N), the inverse matrix, in R8PO storage.
#
  import numpy as np

  b = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      b[i,j] = r[i,j]
#
#  Compute Inverse ( R ).
#
  for k in range ( 0, n ):

    b[k,k] = 1.0 / b[k,k]
    for i in range ( 0, k ):
      b[i,k] = - b[i,k] * b[k,k]

    for j in range ( k + 1, n ):
      t = b[k,j]
      b[k,j] = 0.0
      for i in range ( 0, k + 1 ):
        b[i,j] = b[i,j] + t * b[i,k]
#
#  Compute Inverse ( R ) * ( Inverse ( R ) )'.
#
  for j in range ( 0, n ):

    for k in range ( 0, j ):
      t = b[k,j]
      for i in range ( 0, k + 1 ):
        b[i,k] = b[i,k] + t * b[i,j]

    t = b[j,j]
    for k in range ( 0, j + 1 ):
      b[k,j] = b[k,j] * t

  return b

def r8po_inverse_test ( ):

#*****************************************************************************80
#
## R8PO_INVERSE_TEST tests R8PO_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'r8po_inverse_test' )
  print ( '  r8po_inverse computes the inverse of' )
  print ( '  a symmetric positive definite matrix' )
  print ( '  factored by R8PO_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = min ( i, j ) + 1

  r8po_print ( n, a, '  Matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )
#
#  Compute the inverse.
#
  b = r8po_inverse ( n, r )

  r8po_print ( n, b, '  Inverse matrix B:' )
#
#  Check.
#
  c = r8po_mm ( n, a, b )

  r8po_print ( n, c, '  Product A * B:' )

  return

def r8po_ml ( n, r, x ):

#*****************************************************************************80
#
## R8PO_ML computes A * x = b after A has been factored by R8PO_FA.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    integer N, the order of the matrix.
#
#    real R(N,N), the Cholesky factor, in R8GE format, returned by R8PO_FA.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )
#
#  Compute R * x = y.
#
  for i in range ( 0, n ):
    b[i] = r[i,i] * x[i]
    for j in range ( i + 1, n ):
      b[i] = b[i] + r[i,j] * x[j]
#
#  Compute R' * y = b.
#
  for i in range ( n - 1, -1, -1 ):
    b[i] = r[i,i] * b[i]
    for j in range ( 0, i ):
      b[i] = b[i] + b[j] * r[j,i]

  return b

def r8po_ml_test ( ):

#*****************************************************************************80
#
## R8PO_ML_TEST tests R8PO_ML.
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
  import numpy as np

  n = 10

  print ( '' )
  print ( 'R8PO_ML_TEST' )
  print ( '  R8PO_ML can compute A*x for an R8PO matrix A' )
  print ( '  even after it has been factored by R8PO_FA.' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = min ( i, j ) + 1
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8po_mv ( n, a, x )
#
#  Factor the matrix.
#
  a_lu = r8po_fa ( n, a )
#
#  Solve the linear system.
#
  x = r8po_sl ( n, a_lu, b )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  for i in range ( 0, n ):
    x[i] = 1.0
#
#  Compute the corresponding right hand side, using the factored matrix.
#
  b = r8po_ml ( n, a, x )
#
#  Solve the linear system.
#
  x = r8po_sl ( n, a, b )
 
  r8vec_print ( n, x, '  Solution:' )

  return

def r8po_mm ( n, a, b ):

#*****************************************************************************80
#
## R8PO_MM multiplies two R8PO matrices.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    integer N, the order of the matrices.
#    N must be positive.
#
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  import numpy as np

  c = r8po_zeros ( n )
  
  for i in range ( 0, n ):

    for j in range ( i, n ):
      for k in range ( 0, n ):

        if ( i <= k ):
          aik = a[i,k]
        else:
          aik = a[k,i]

        if ( k <= j ):
          bkj = b[k,j]
        else:
          bkj = b[j,k]

        c[i,j] = c[i,j] + aik * bkj

  return c

def r8po_mm_test ( ):

#*****************************************************************************80
#
## R8PO_MM_TEST tests R8PO_MM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8po_mm_test' )
  print ( '  r8po_mm computes the product of two' )
  print ( '  symmetric positive definite matrices.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set (the upper half of) matrix A.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8po_print ( n, a, '  Matrix A:' )
#
#  Set (the upper half of) matrix B.
#
  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    b[i,i] = float ( i + i + 1 )
  for i in range ( 0, n - 1 ):
    b[i,i+1] = float ( i + i + 1 + 1 )

  r8po_print ( n, b, '  Matrix B:' )
#
#  Compute the product.
#
  c = r8po_mm ( n, a, b )

  r8po_print ( n, c, '  Product matrix C = A * B:' )

  return

def r8po_mv ( n, a, x ):

#*****************************************************************************80
#
## R8PO_MV multiplies a R8PO matrix times a vector.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
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
    for j in range ( 0, i ):
      b[i] = b[i] + a[j,i] * x[j]
    for j in range ( i, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8po_mv_test ( ):

#*****************************************************************************80
#
## R8PO_MV_TEST tests R8PO_MV.
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
  n = 5

  print ( '' )
  print ( 'R8PO_MV_TEST' )
  print ( '  R8PO_MV computes the product of an R8PO matrix and a vector.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set (the upper half of) matrix A.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8po_print ( n, a, '  Matrix A:' )
#
#  Set the vector V.
#
  v = r8vec_indicator1 ( n )

  r8vec_print ( n, v, '  Vector V:' )
#
#  Compute the product.
#
  w = r8po_mv ( n, a, v )

  r8vec_print ( n, w, '  Product w = A * v:' )

  return

def r8po_print ( n, a, title ):

#*****************************************************************************80
#
## R8PO_PRINT prints a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an SPO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#    string TITLE, a title to be printed.
#
  r8po_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8po_print_test ( ):

#*****************************************************************************80
#
## R8PO_PRINT_TEST tests R8PO_PRINT.
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
  print ( 'r8po_print_test' )
  print ( '  r8po_print prints an R8PO matrix.' )

  n = 5
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0 ], 
    [ 12.0, 22.0, 23.0, 24.0, 25.0, ], 
    [ 13.0, 23.0, 33.0, 34.0, 35.0 ], 
    [ 14.0, 24.0, 34.0, 44.0, 45.0 ],
    [ 14.0, 25.0, 35.0, 45.0, 55.0 ] ], dtype = np.float64 )

  r8po_print ( n, v, '  Here is an R8PO matrix:' )

  return

def r8po_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8PO_PRINT_SOME prints some of a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return
#
#  Print the columns of the matrix, in strips of 5.
#
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
        if ( i <= j ):
          print ( '%12g  ' % ( a[i,j] ), end = '' )
        else:
          print ( '%12g  ' % ( a[j,i] ), end = '' )

      print ( '' )

  return

def r8po_print_some_test ( ):

#*****************************************************************************80
#
## R8PO_PRINT_SOME_TEST tests R8PO_PRINT_SOME.
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
  print ( 'R8PO_PRINT_SOME_TEST' )
  print ( '  R8PO_PRINT_SOME prints some of an R8PO matrix.' )

  n = 5
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0 ], 
    [ 12.0, 22.0, 23.0, 24.0, 25.0, ], 
    [ 13.0, 23.0, 33.0, 34.0, 35.0 ], 
    [ 14.0, 24.0, 34.0, 44.0, 45.0 ],
    [ 14.0, 25.0, 35.0, 45.0, 55.0 ] ], dtype = np.float64 )

  r8po_print_some ( n, v, 0, 3, 3, 4, '  Here is an R8PO matrix:' )

  return

def r8po_random ( n, rng ):

#*****************************************************************************80
#
## r8po_random() randomizes a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#    The matrix computed here is not simply a set of random numbers in
#    the nonzero slots of the R8PO array.  It is also a positive definite
#    matrix.  It is computed by setting a "random" upper triangular
#    Cholesky factor R, and then computing A = R'*R.
#    The randomness is limited by the fact that all the entries of
#    R will be between 0 and 1.  A truly random R is only required
#    to have positive entries on the diagonal.
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
#    integer N, the order of the matrix.
#    N must be positive.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(N,N), the R8PO matrix.
#
  a = r8po_zeros ( n )

  for i in range ( n - 1, -1, -1 ):
#
#  Set row I of R.
#
    for j in range ( i, n ):
      r = rng.random ( )
      a[i,j] = r
#
#  Consider element J of row I, last to first.
#
    for j in range ( n - 1, i - 1, -1 ):
#
#  Add multiples of row I to lower elements of column J.
#
      for i2 in range ( i + 1, j + 1 ):
        a[i2,j] = a[i2,j] + a[i,i2] * a[i,j]
#
#  Reset element J.
#
      a[i,j] = a[i,i] * a[i,j]

  return a

def r8po_random_test ( rng ):

#*****************************************************************************80
#
## r8po_random_test() tests r8po_random().
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
  n = 5

  print ( '' )
  print ( 'r8po_random_test():' )
  print ( '  r8po_random() computes a random positive definite' )
  print ( '  symmetric matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8po_random ( n, rng )

  r8po_print ( n, a, '  The random R8PO matrix:' )

  return

def r8po_sl ( n, r, b ):

#*****************************************************************************80
#
## r8po_sl() solves a R8PO system factored by R8PO_FA.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real R(N,N), the Cholesky factor, in R8GE storage, 
#    returned by R8PO_FA.
#
#    real B(N), the right hand side.
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
#  Solve R' * y = b.
#
  for k in range ( 0, n ):
    t = 0.0
    for i in range ( 0, k ):
      t = t + x[i] * r[i,k]
    x[k] = ( x[k] - t ) / r[k,k]
#
#  Solve R * x = y.
#
  for k in range ( n - 1, -1, -1 ):
    x[k] = x[k] / r[k,k]
    for i in range ( 0, k ):
      x[i] = x[i] - r[i,k] * x[k]

  return x

def r8po_sl_test ( ):

#*****************************************************************************80
#
## R8PO_SL_TEST tests R8PO_SL.
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
  import numpy as np

  n = 5

  print ( '' )
  print ( 'R8PO_SL_TEST' )
  print ( '  R8PO_SL solves a linear system with an R8PO matrix' )
  print ( '  after it has been factored by R8PO_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set (the upper half of) matrix A.
#
  a = r8po_zeros ( n )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8po_print ( n, a, '  Matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )
#
#  Set the right hand side.
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8po_sl ( n, r, b )
  r8vec_print ( n, x, '  Solution x:' )

  return

def r8po_to_r8ge ( n, a ):

#*****************************************************************************80
#
## R8PO_TO_R8GE copies a R8PO matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
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
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8PO matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        b[i,j] = a[i,j]
      else:
        b[i,j] = a[j,i]

  return b

def r8po_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r8po_to_r8ge_test() tests r8po_to_r8ge().
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
#    rng: the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'r8po_to_r8ge_test():' )
  print ( '  r8po_to_r8ge() converts a R8PO matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8po_random ( n, rng )

  r8po_print ( n, a, '  The random R8PO matrix:' )
 
  b = r8po_to_r8ge ( n, a )

  print ( '' )
  print ( '  The random R8GE matrix:' )
  print ( b )

  return

def r8po_zeros ( n ):

#*****************************************************************************80
#
## R8PO_ZEROS zeroes an R8PO matrix.
#
#  Discussion:
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
#    integer N, the order of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A(N,N), the R8PO matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  return a

def r8po_zeros_test ( ):

#*****************************************************************************80
#
## R8PO_ZEROS_TEST tests R8PO_ZEROS.
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
  n = 5

  print ( '' )
  print ( 'r8po_zeros_test' )
  print ( '  r8po_zeros zeros out space for a' )
  print ( '  symmetric positive definite matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8po_zeros ( n )

  r8po_print ( n, a, '  Matrix A:' )

  return

def r8ut_mtm ( n, a, b ):

#*****************************************************************************80
#
## r8ut_mtm() computes C = A' * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will NOT be an R8UT matrix.
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
#    integer N, the order of the matrices.
#    N must be positive.
#
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  import numpy as np

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k_hi = min ( i + 1, j + 1 )
      for k in range ( 0, k_hi ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

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
  r8po_test ( )
  timestamp ( )
