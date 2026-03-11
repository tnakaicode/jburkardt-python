#! /usr/bin/env python3
#
def r8sm_test ( ):

#*****************************************************************************80
#
## r8sm_test() tests r8sm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8sm_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8sm().' )

  r8sm_indicator_test ( )
  r8sm_ml_test ( )
  r8sm_mtv_test ( )
  r8sm_mv_test ( )
  r8sm_print_test ( )
  r8sm_print_some_test ( )
  r8sm_random_test ( )
  r8sm_sl_test ( )
  r8sm_to_r8ge_test ( )
  r8sm_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8sm_test():' )
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
#    r8ge_fa() is a simplified version of the LINPACK routine SGEFA.
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

  a_lu = np.zeros ( [ n, n ] )

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

def r8ge_ml ( n, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## r8ge_ml() computes A * x or A' * x, using factors from r8ge_fa().
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that r8ge_fa has overwritten the original matrix
#    information by LU factors.  r8ge_ml() is able to reconstruct the
#    original matrix from the LU factor data.
#
#    r8ge_ml() allows the user to check that the solution of a linear
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
#    real A_LU(N,N), the LU factors from r8ge_fa().
#
#    integer PIVOT(N), the pivot vector computed by r8ge_fa().
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

  b = x.copy ( )

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

def r8ge_sl ( n, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## r8ge_sl() solves a system factored by r8ge_fa().
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_sl() is a simplified version of the LINPACK routine SGESL.
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

def r8sm_indicator ( m, n ):

#*****************************************************************************80
#
## r8sm_indicator() returns the indicator matrix as an R8SM matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  u = - np.ones ( m )

  v = np.linspace ( 1, n, n )

  a = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = float ( fac * ( i + 1 ) )
 
  return a, u, v

def r8sm_indicator_test ( ):

#*****************************************************************************80
#
## r8sm_indicator_test() tests r8sm_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8sm_indicator_test():' )
  print ( '  r8sm_indicator() sets up an R8SM indicator matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_indicator ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM indicator matrix:' )

  return

def r8sm_ml ( n, a_lu, u, v, pivot, x, job ):

#*****************************************************************************80
#
## r8sm_ml() multiplies a factored square R8SM matrix times a vector.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
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
#    real A_LU(N,N), the LU factors from R8GE_FA.
#
#    real U(N), V(N), the Sherman Morrison vectors.
#
#    integer PIVOT(N), the pivot vector computed by R8GE_FA.
#
#    real X(N), the vector to be multiplied.
#
#    integer JOB, specifies the operation to be done:
#    JOB = 0, compute (A-u*v') * x.
#    JOB nonzero, compute (A-u*v')' * x.
#
#  Output:
#
#    real B(N), the result of the multiplication.
#
  import numpy as np

  b = r8ge_ml ( n, a_lu, pivot, x, job )

  if ( job == 0 ):

    b = b - u * np.dot ( v, x )

  else:

    b = b - v * np.dot ( u, x )

  return b

def r8sm_ml_test ( ):

#*****************************************************************************80
#
## r8sm_ml_test() tests r8sm_ml().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 7
  n = m

  print ( '' )
  print ( 'R8SM_ML_TEST' )
  print ( '  R8SM_ML computes A*x or A\'*X' )
  print ( '  where A is a Sherman Morrison matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a, u, v = r8sm_random ( m, n )

    r8sm_print ( m, n, a, u, v, '  The Sherman Morrison matrix:' )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8sm_mv ( m, n, a, u, v, x )
    else:
      b = r8sm_mtv ( m, n, a, u, v, x )
#
#  Factor the matrix.
#
    a_lu, pivot, info = r8ge_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8SM_ML_TEST - Fatal error!' )
      print ( '  R8GE_FA declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'r8sm_ml_test(): Fatal error!' )
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8sm_ml ( n, a_lu, u, v, pivot, x, job )

    if ( job == 0 ):
      r8vec2_print_some ( n, b, b2, 10, '  A*x and PLU*x' )
    else:
      r8vec2_print_some ( n, b, b2, 10, '  A\'*x and (PLU)\'*x' )

  return

def r8sm_mtv ( m, n, a, u, v, x ):

#*****************************************************************************80
#
## r8sm_mtv() multiplies a vector by a R8SM matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
#    real X(M), the vector to be multiplied.
#
#  Output:
#
#    real B(N), the product (A-u*v')' * x.
#
  import numpy as np

  ux = 0.0
  for i in range ( 0, m ):
    ux = ux + u[i] * x[i]

  b = np.zeros ( n )
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j] = b[j] + x[i] * a[i,j]
    b[j] = b[j] - v[j] * ux

  return b

def r8sm_mtv_test ( ):

#*****************************************************************************80
#
## r8sm_mtv_test() tests r8sm_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8SM_MTV_TEST' )
  print ( '  R8SM_MTV computes A\'*x=b, where A is an R8SM matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_indicator ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM matrix:' )

  x = r8vec_indicator1 ( m )

  r8vec_print ( m, x, '  The vector x:' )

  b = r8sm_mtv ( m, n, a, u, v, x )

  r8vec_print ( n, b, '  The product b=A''*x:' )

  return

def r8sm_mv ( m, n, a, u, v, x ):

#*****************************************************************************80
#
## r8sm_mv() multiplies a R8SM matrix times a vector.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors U and V.
#
#    real X(N), the vector to be multiplied by (A-u*v').
#
#  Output:
#
#    real B(M), the product (A-u*v') * x.
#
  import numpy as np

  vx = 0.0
  for j in range ( 0, n ):
    vx = vx + v[j] * x[j]

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i] = b[i] + a[i,j] * x[j]
    b[i] = b[i] - u[i] * vx

  return b

def r8sm_mv_test ( ):

#*****************************************************************************80
#
## r8sm_mv_test() tests r8sm_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8SM_MV_TEST' )
  print ( '  R8SM_MV computes A*x=b, where A is an R8SM matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_indicator ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8sm_mv ( m, n, a, u, v, x )

  r8vec_print ( m, b, '  The product b=A*x:' )

  return

def r8sm_print ( m, n, a, u, v, title ):

#*****************************************************************************80
#
## r8sm_print() prints a R8SM matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
#    string TITLE, a title to be printed.
#
  r8sm_print_some ( m, n, a, u, v, 0, 0, m - 1, n - 1, title )

  return

def r8sm_print_test ( ):

#*****************************************************************************80
#
## r8sm_print_test() tests r8sm_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8SM_PRINT_TEST' )
  print ( '  R8SM_PRINT prints an R8SM matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_indicator ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM matrix:' )

  return

def r8sm_print_some ( m, n, a, u, v, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8sm_print_some() prints some of a R8SM matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
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
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :  ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        aij = a[i,j] - u[i] * v[j]
        print ( '  %12g' % ( aij ), end = '' )

      print ( '' )

  return

def r8sm_print_some_test ( ):

#*****************************************************************************80
#
## r8sm_print_some_test() tests r8sm_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 9
  n = 9

  print ( '' )
  print ( 'R8SM_PRINT_SOME_TEST' )
  print ( '  R8SM_PRINT_SOME prints some of an R8SM matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_indicator ( m, n )

  r8sm_print_some ( m, n, a, u, v, 2, 3, 5, 7, '  Rows 2-5, Cols 3-7:' )

  return

def r8sm_random ( m, n ):

#*****************************************************************************80
#
## r8sm_random() randomizes a R8SM matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = rng.random ( size = [ m, n ] )

  u = rng.random ( size = m )

  v = rng.random ( size = n )

  return a, u, v

def r8sm_random_test ( ):

#*****************************************************************************80
#
## r8sm_random_test() tests r8sm_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8SM_RANDOM_TEST' )
  print ( '  R8SM_RANDOM sets up an R8SM random matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_random ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM random matrix:' )

  return

def r8sm_sl ( n, a_lu, u, v, b, pivot, job ):

#*****************************************************************************80
#
## r8sm_sl() solves a square R8SM system that has been factored.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#    It is assumed that A has been decomposed into its LU factors
#    by R8GE_FA.  The Sherman Morrison formula allows
#    us to solve linear systems involving (A-u*v') by solving linear
#    systems involving A and adjusting the results.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kahaner, Moler, and Nash
#    Numerical Methods and Software,
#    Prentice Hall, 1989
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from R8GE_FA.
#
#    real U(N), V(N), the R8SM vectors U and V.
#
#    real B(N), the right hand side vector.
#
#    integer PIVOT(N), the pivot vector produced by R8GE_FA.
#
#    integer JOB, specifies the system to solve.
#    0, solve (A-u*v') * X = B.
#    nonzero, solve (A-u*v')' * X = B.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  if ( job == 0 ):
#
#  Solve A' * w = v.
#
    job_local = 1
    w = r8ge_sl ( n, a_lu, pivot, v, job_local )
#
#  Set beta = w' * b.
#
    beta = 0.0
    for i in range ( 0, n ):
      beta = beta + w[i] * b[i]
#
#  Solve A * x = b.
#
    job_local = 0
    x = r8ge_sl ( n, a_lu, pivot, b, job_local )
#
#  Solve A * w = u.
#
    job_local = 0
    w = r8ge_sl ( n, a_lu, pivot, u, job_local )
#
#  Set alpha = 1 / ( 1 - v' * w ).
#
    alpha = 1.0 - np.dot ( v, w )

  else:
#
#  Solve A * w = u.
#
    job_local = 0
    w = r8ge_sl ( n, a_lu, pivot, u, job_local )
#
#  Set beta = w' * b.
#
    beta = 0.0
    for i in range ( 0, n ):
      beta = beta + w[i] * b[i]
#
#  Solve A' * x = b.
#
    job_local = 1
    x = r8ge_sl ( n, a_lu, pivot, b, job_local )
#
#  Solve A' * w = v.
#
    job_local = 1
    w = r8ge_sl ( n, a_lu, pivot, v, job_local )
#
#  Set alpha = 1 / ( 1 - u' * w ).
#
    alpha = 1.0 - np.dot ( u, w )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'R8SM_SL - Fatal error!' )
    print ( '  The divisor ALPHA is zero.' )
    raise Exception ( 'R8SM_SL - Fatal error!' )

  alpha = 1.0 / alpha
#
#  Set b = b + alpha * beta * w.
#
  for i in range ( 0, n ):
    x[i] = x[i] + alpha * beta * w[i]

  return x

def r8sm_sl_test ( ):

#*****************************************************************************80
#
## r8sm_sl_test() tests r8sm_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = m

  print ( '' )
  print ( 'R8SM_SL_TEST' )
  print ( '  R8SM_SL implements the Sherman-Morrison method' )
  print ( '  for solving a perturbed linear system.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  for job in range ( 1, -1, -1 ):
#
#  Set the matrix.
#
    a, u, v = r8sm_random ( m, n )

    r8sm_print ( m, n, a, u, v, '  The Sherman-Morrison matrix A:' )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8sm_mv ( m, n, a, u, v, x )
    else:
      b = r8sm_mtv ( m, n, a, u, v, x )

    r8vec_print ( n, b, '  The right hand side vector B:' )
#
#  Factor the matrix.
#
    a_lu, pivot, info = r8ge_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8SM_SL_TEST - Fatal error!' )
      print ( '  R8GE_FA declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'r8sm_sl_test(): Fatal error!' )
#
#  Solve the linear system.
#
    x = r8sm_sl ( n, a_lu, u, v, b, pivot, job )
 
    if ( job == 0 ):
      r8vec_print ( n, x, '  Solution to A * X = B:' )
    else:
      r8vec_print ( n, x, '  Solution to A'' * X = B:' )

  return

def r8sm_to_r8ge ( m, n, a, u, v ):

#*****************************************************************************80
#
## r8sm_to_r8ge() copies a R8SM matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
#  Output:
#
#    real B(M,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i,j] = a[i,j] - u[i] * v[j]

  return b

def r8sm_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8sm_to_r8ge_test() tests r8sm_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8SM_TO_R8GE_TEST' )
  print ( '  R8SM_TO_R8GE converts an R8SM matrix to R8GE format.' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_indicator ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM matrix:' )

  a_r8ge = r8sm_to_r8ge ( m, n, a, u, v )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8sm_zeros ( m, n ):

#*****************************************************************************80
#
## r8sm_zeros() zeros an R8SM matrix.
#
#  Discussion:
#
#    The R8SM storage format is used for an M by N Sherman Morrison matrix B,
#    which is defined by an M by N matrix A, an M vector U, and
#    an N vector V, by B = A - U * V'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(M,N), the R8SM matrix.
#
#    real U(M), V(N), the R8SM vectors.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  u = np.zeros ( m )
  v = np.zeros ( n )

  return a, u, v

def r8sm_zeros_test ( ):

#*****************************************************************************80
#
## r8sm_zeros_test() tests r8sm_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8SM_ZEROS_TEST' )
  print ( '  R8SM_ZEROS sets up an R8SM zero matrix' )
  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )

  a, u, v = r8sm_zeros ( m, n )

  r8sm_print ( m, n, a, u, v, '  The R8SM zeros matrix:' )
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
  r8sm_test ( )
  timestamp ( )
 
