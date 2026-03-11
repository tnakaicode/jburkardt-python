#! /usr/bin/env python3
#
def r8sto_test ( ):

#*****************************************************************************80
#
## r8sto_test() tests r8sto().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8sto_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8sto().' )

  r8sto_dif2_test ( )
  r8sto_indicator_test ( )
  r8sto_inverse_test ( )
  r8sto_mv_test ( )
  r8sto_print_test ( )
  r8sto_print_some_test ( )
  r8sto_random_test ( )
  r8sto_sl_test ( )
  r8sto_to_r8ge_test ( )
  r8sto_yw_sl_test ( )
  r8sto_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8sto_test():' )
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

def r8sto_dif2 ( n ):

#*****************************************************************************80
#
## R8STO_DIF2 sets the second difference as an R8STO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a real symmetric Toeplitz matrix, which 
#    is constant along diagonals.  Only the first row is stored.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N), the R8STO matrix.
#
  import numpy as np

  a = np.zeros ( n )

  a[0] = 2.0
  a[1] = -1.0

  return a

def r8sto_dif2_test ( ):

#*****************************************************************************80
#
## r8sto_dif2_test() tests r8sto_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8sto_dif2_test():' )
  print ( '  r8sto_dif2() sets up a R8STO second difference matrix.' )

  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8sto_dif2 ( n )

  r8sto_print ( n, a, '  The matrix:' )

  return

def r8sto_indicator ( n ):

#*****************************************************************************80
#
## R8STO_INDICATOR sets up a R8STO indicator matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2015
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
#    real A(N), the R8STO matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( n )

  i = 0
  k = 0
  for j in range ( 0, n ):
    a[k] = fac * ( i + 1 ) + ( j + 1 )
    k = k + 1

  return a

def r8sto_indicator_test ( ):

#*****************************************************************************80
#
## R8STO_INDICATOR_TEST tests R8STO_INDICATOR.
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
  n = 5

  print ( '' )
  print ( 'r8sto_indicator_test():' )
  print ( '  r8sto_indicator() sets up a R8STO indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8sto_indicator ( n )

  r8sto_print ( n, a, '  The R8STO indicator matrix:' )

  return

def r8sto_inverse ( n, a ):

#*****************************************************************************80
#
## r8sto_inverse() computes the inverse of an R8STO matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#    For this routine, the matrix is also required to be positive definite.
#
#    The original implementation of the algorithm assumed that the
#    diagonal element was 1.  The algorithm has been modified so that
#    this is no longer necessary.
#
#    The inverse matrix is NOT guaranteed to be a Toeplitz matrix.  
#    It is guaranteed to be symmetric and persymmetric.
#    The inverse matrix is returned in general storage, that is,
#    as an "SGE" matrix.
#
#  Example:
#
#    To compute the inverse of
#
#     1.0 0.5 0.2
#     0.5 1.0 0.5
#     0.2 0.5 1.0
#
#    we input:
#
#      N = 3
#      A = { 1.0, 0.5, 0.2 }
#
#    with output:
#
#      B = ( 1/56) * [ 75, -40,   5,
#                     -40,  96, -40,
#                       5, -40,  75 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Section 4.7.3, "Computing the Inverse",
#    Matrix Computations,
#    Third Edition,
#    Johns Hopkins, 1996.
#
#  Input:
#
#    int N, the order of the system.
#
#    double A[N], the R8STO matrix.
#
#  Output:
#
#    double B[N*N], the inverse of the matrix.
#
  import numpy as np

  a2 = np.zeros ( n - 1 )
  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    a2[i] = a[i+1] / a[0]

  v = r8sto_yw_sl ( n-1, a2 )
#
#  Compute the N-th entry of V.
#
  t = 0.0
  for i in range ( 0, n - 1 ):
    t = t + a2[i] * v[i]

  vn = 1.0 / ( 1.0 + t )
#
#  Reverse the first N-1 entries of V.
#
  ihi = ( n - 1 ) // 2

  for i in range ( 0, ihi ):
    j = n - 2 - i
    t    = v[i]
    v[i] = v[j]
    v[j] = t
#
#  Scale the entries.
#
  for i in range ( 0, n - 1 ):
    v[i] = vn * v[i]
#
#  Set the boundaries of B.
#
  b[0,0] = vn;
  for j in range ( 1, n ):
    b[0,j] = v[n-j-1]

  for j in range ( 0, n - 1 ):
    b[n-1,j] = v[j]
  b[n-1,n-1] = vn

  for i in range ( 1, n - 1 ):
    b[i,0] = v[n-1-i]
    b[i,n-1] = v[i]
#
#  Fill the interior.
#
  ihi = 1 + ( n - 1 ) // 2

  for i in range ( 2, ihi + 1 ):
    for j in range ( i, n - i + 2 ):
      t = b[i-2,j-2] + ( v[n-j] * v[n-i] - v[i-2] * v[j-2] ) / vn
      b[i-1,j-1] = t
      b[j-1,i-1] = t
      b[n-i,n-j] = t
      b[n-j,n-i] = t
#
#  Scale B.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      b[i,j] = b[i,j] / a[0]

  return b

def r8sto_inverse_test ( ):

#*****************************************************************************80
#
## r8sto_inverse_test() tests r8sto_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  a = np.array ( [ 4.0, 2.0, 0.8 ] )

  print ( '' )
  print ( 'R8STO_INVERSE_TEST' )
  print ( '  R8STO_INVERSE computes the inverse of a positive' )
  print ( '  definite symmetric Toeplitz matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  r8sto_print ( n, a, '  The symmetric Toeplitz matrix A:' )

  b = r8sto_inverse ( n, a )

  print ( '' )
  print ( '  The inverse matrix B:' )
  print ( b )

  a2 = r8sto_to_r8ge ( n, a )

  c = np.dot ( a2, b )

  print ( '' )
  print ( '  The product C = A * B:' )
  print ( c )

  return

def r8sto_mv ( n, a, x ):

#*****************************************************************************80
#
## r8sto_mv() multiplies a R8STO matrix times a vector.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8STO matrix.
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
      b[i] = b[i] + a[i-j] * x[j]
    for j in range ( i, n ):
      b[i] = b[i] + a[j-i] * x[j] 

  return b

def r8sto_mv_test ( ):

#*****************************************************************************80
#
## r8sto_mv_test() tests r8sto_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8STO_MV_TEST' )
  print ( '  R8STO_MV computes b=A*x, where A is an R8STO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8sto_random ( n )
  r8sto_print ( n, a, '  The R8STO matrix:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8sto_mv ( n, a, x )
  r8vec_print ( n, b, '  b=A*x:' )

  return

def r8sto_print ( n, a, title ):

#*****************************************************************************80
#
## r8sto_print() prints an R8STO matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int N, the order of the matrix.
#    N must be positive.
#
#    double A[N], the R8STO matrix.
#
#    string TITLE, a title.
#
  r8sto_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8sto_print_test ( ):

#*****************************************************************************80
#
## r8sto_print_test() tests r8sto_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8STO_PRINT_TEST' )
  print ( '  R8STO_PRINT prints an R8STO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8sto_indicator ( n )

  r8sto_print ( n, a, '  The R8STO matrix:' )

  return

def r8sto_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8sto_print_some() prints out a portion of an R8STO matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer  N, the number of rows and columns of the matrix.
#
#    real A(N), the matrix to be printed.
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

  if ( n <= 0 ):
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
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( i <= j ):
          aij = a[j-i]
        else:
          aij = a[i-j]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8sto_print_some_test ( ):

#*****************************************************************************80
#
## r8sto_print_some_test() tests r8sto_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8STO_PRINT_SOME_TEST' )
  print ( '  R8STO_PRINT_SOME prints some of an R8STO matrix.' )

  n = 5

  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8sto_indicator ( n )

  r8sto_print_some ( n, a, 1, 0, 4, 2, '  Rows 1:4, Cols 0:2' )

  return

def r8sto_random ( n ):

#*****************************************************************************80
#
## r8sto_random() randomizes a R8STO matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
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
#    real A(N), the R8STO matrix.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  a = rng.random ( size = n )

  return a

def r8sto_random_test ( ):

#*****************************************************************************80
#
## r8sto_random_test() tests r8sto_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8STO_RANDOM_TEST' )
  print ( '  R8STO_RANDOM randomizes an R8STO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8sto_random ( n )

  r8sto_print ( n, a, '  The R8STO matrix:' )

  return

def r8sto_sl ( n, a, b ):

#*****************************************************************************80
#
## R8STO_SL solves an R8STO system.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#    The matrix is also required to be positive definite.
#
#    This implementation of the algorithm assumes that the diagonal element
#    (the first element of A) is 1.
#
#    Note that there is a typographical error in the presentation
#    of this algorithm in the reference, and another in the presentation
#    of a sample problem.  Both involve sign errors.  A minor error
#    makes the algorithm incorrect for the case N = 1.
#
#  Example:
#
#    To solve
#
#     1.0 0.5 0.2    x1    4.0
#     0.5 1.0 0.5 *  x2 = -1.0
#     0.2 0.5 1.0    x3    3.0
#
#    we input:
#
#      N = 3
#      A = (/ 1.0, 0.5, 0.2 /)
#      B = (/ 4.0, -1.0, 3.0 /)
#
#    with output:
#
#      X = (/ 355, -376, 285 /) / 56
#        = (/ 6.339, -6.714, 5.089 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Section 4.7.3, "The General Right Hand Side Problem",
#    Matrix Computations,
#    Third Edition,
#    Johns Hopkins, 1996.
#
#  Input:
#
#    int N, the order of the system.
#
#    double A[N], the R8STO matrix, with the EXTRA CONDITION
#    that the first entry is 1.
#
#    double B[N], the right hand side of the linear system.
#
#  Output:
#
#    double R8STO_SL[N], the solution of the linear system.
#
  import numpy as np

  x = np.zeros ( n )
  y = np.zeros ( n )

  k = 0
  beta = 1.0
  x[k] = b[k] / beta

  if ( k < n - 1 ):
    y[k] = - a[k+1] / beta

  for k in range ( 1, n ):

    beta = ( 1.0 - y[k-1] * y[k-1] ) * beta

    x[k] = b[k]
    for i in range ( 1, k + 1 ):
      x[k] = x[k] - a[i] * x[k-i]
    x[k] = x[k] / beta

    for i in range ( 1, k + 1 ):
      x[i-1] = x[i-1] + x[k] * y[k-i] 

    if ( k < n - 1 ):

      y[k] = - a[k+1]
      for i in range ( 1, k + 1 ):
        y[k] = y[k] - a[i] * y[k-i]
      y[k] = y[k] / beta

      for i in range ( 1, k + 1 ):
        y[i-1] = y[i-1] + y[k] * y[k-i]

  return x

def r8sto_sl_test ( ):

#*****************************************************************************80
#
## R8STO_SL_TEST tests R8STO_SL.
#
#  Discussion:
#
#    Modifications to this test routine were suggested by Zhang Yunong
#    of the EEE Department of Strathclyde University.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  a = np.array ( [ 1.0,  0.5,  0.2 ] )
  b = np.array ( [ 4.0, -1.0,  3.0 ] )

  print ( '' )
  print ( 'R8STO_SL_TEST' )
  print ( '  R8STO_SL solves a positive definite symmetric' )
  print ( '  Toeplitz system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  r8sto_print ( n, a, '  The symmetric Toeplitz matrix A:' )

  r8vec_print ( n, b, '  The right hand side vector B:' )

  x = r8sto_sl ( n, a, b )

  r8vec_print ( n, x, '  The solution X:' )

  r = r8sto_mv ( n, a, x )

  for i in range ( 0, n ):
    r[i] = r[i] - b[i]

  err_max = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of residual error A * x - b = ', err_max )

  return

def r8sto_to_r8ge ( n, a ):

#*****************************************************************************80
#
## R8STO_TO_R8GE copies a R8STO matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8STO matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      b[i,j] = a[i-j]
    for j in range ( i, n ):
      b[i,j] = a[j-i]

  return b

def r8sto_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8STO_TO_R8GE_TEST tests R8STO_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8STO_TO_R8GE_TEST' )
  print ( '  R8STO_TO_R8GE converts a matrix from R8STO to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a_r8sto = r8sto_random ( n )
  r8sto_print ( n, a_r8sto, '  The R8STO matrix:' )

  a_r8ge = r8sto_to_r8ge ( n, a_r8sto )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8sto_yw_sl ( n, b ):

#*****************************************************************************80
#
## R8STO_YW_SL solves the Yule-Walker equations for an R8STO matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#    The matrix is also required to be positive definite.
#
#    This implementation of the algorithm assumes that the diagonal element
#    is 1.
#
#    The real symmetric Toeplitz matrix can be described by N numbers, which,
#    for convenience, we will label B(0:N-1).  We assume there is one more
#    number, B(N).  If we let A be the symmetric Toeplitz matrix whose first
#    row is B(0:N-1), then the Yule-Walker equations are:
#
#      A * X = -B(1:N)
#
#  Example:
#
#    To solve
#
#     1.0 0.5 0.2    x1   0.5
#     0.5 1.0 0.5 *  x2 = 0.2
#     0.2 0.5 1.0    x3   0.1
#
#    we input:
#
#      N = 3
#      B = (/ 0.5, 0.2, 0.1 /)
#
#    with output:
#
#      X = (/ -75, 12, -5 /) / 140
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Section 4.7.2, "Solving the Yule-Walker Equations",
#    Matrix Computations,
#    Third Edition,
#    Johns Hopkins, 1996.
#
#  Input:
#
#    int N, the order of the system.
#
#    double B[N], defines the linear system.  The first entry of the
#    symmetric Toeplitz matrix is assumed to be a 1, which is NOT stored.  The N-1
#    remaining elements of the first row of are stored in B, followed by
#    the remaining scalar that defines the linear system.
#
#  Output:
#
#    double X[N], the solution of the linear system.
#
  import numpy as np

  x = np.zeros ( n )
  x2 = np.zeros ( n )

  x[0] = - b[0]
  beta = 1.0
  alpha = - b[0]

  for i in range ( 1, n ):
 
    beta = ( 1.0 - alpha * alpha ) * beta

    alpha = b[i]
    for j in range ( 1, i + 1 ):
      alpha = alpha + b[i-j] * x[j-1];

    alpha = - alpha / beta

    for j in range ( 1, i + 1 ):
      x2[j-1] = x[j-1]

    for j in range ( 1, i + 1 ):
      x[j-1] = x[j-1] + alpha * x2[i-j]

    x[i] = alpha

  return x

def r8sto_yw_sl_test ( ):

#*****************************************************************************80
#
## R8STO_YW_SL_TEST tests R8STO_YW_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  r = np.array ( [ 1.0, 0.5, 0.2, 0.1 ] )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = r[i]

  print ( '' )
  print ( 'R8STO_YW_SL_TEST' )
  print ( '  R8STO_YW_SL solves the Yule-Walker equations for a' )
  print ( '  symmetric Toeplitz system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  r8sto_print ( n, a, "  The symmetric Toeplitz matrix:" )

  b = np.zeros ( n )
  for i in range ( 0, n ):
    b[i] = - r[i+1]

  r8vec_print ( n, b, '  The right hand side, B:' )

  for i in range ( 0, n ):
    b[i] = - b[i]

  x = r8sto_yw_sl ( n, b )

  r8vec_print ( n, x, "  The computed solution, X:" )

  b = r8sto_mv ( n, a, x )

  r8vec_print ( n, b, "  The product A*x:" )

  return

def r8sto_zeros ( n ):

#*****************************************************************************80
#
#% R8STO_ZEROS zeros an R8STO matrix.
#
#  Discussion:
#
#    The R8STO storage format is used for a symmetric Toeplitz matrix.
#    It stores the N elements of the first row.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2015
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
#    real A(N), the R8STO matrix.
#
  import numpy as np

  a = np.zeros ( n )

  return a

def r8sto_zeros_test ( ):

#*****************************************************************************80
#
## R8STO_ZEROS_TEST tests R8STO_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8STO_ZEROS_TEST' )
  print ( '  R8STO_ZEROS zeros an R8STO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8sto_zeros ( n )

  r8sto_print ( n, a, '  The R8STO matrix:' )

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
  r8sto_test ( )
  timestamp ( )
 
