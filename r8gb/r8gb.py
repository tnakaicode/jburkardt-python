#! /usr/bin/env python3
#
def r8gb_test ( ):

#*****************************************************************************80
#
## r8gb_test() tests r8gb().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8gb_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8gb().' )

  r8gb_det_test ( )
  r8gb_dif2_test ( )
  r8gb_fa_test ( )
  r8gb_indicator_test ( )
  r8gb_ml_test ( )
  r8gb_mtv_test ( )
  r8gb_mu_test ( )
  r8gb_mv_test ( )
  r8gb_nz_num_test ( )
  r8gb_print_test ( )
  r8gb_print_some_test ( )
  r8gb_random_test ( )
  r8gb_sl_test ( )
  r8gb_to_r8ge_test ( )
  r8gb_to_r8st_test ( )
# r8gb_to_r8sp_test ( )
  r8gb_to_r8vec_test ( )
  r8gb_trf_test ( )
  r8gb_trs_test ( )
  r8gb_zeros_test ( )

# r8ge_to_r8gb_test ( )

  r8vec_to_r8gb_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8gb_test():' )
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

def r8gb_det ( n, ml, mu, a_lu, pivot ):

#*****************************************************************************80
#
## r8gb_det() computes the determinant of a matrix factored by r8gb_fa or R8GB_TRF.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A_LU(2*ML+MU+1,N), the LU factors from r8gb_fa or R8GB_TRF.
#
#    integer PIVOT(N), the pivot vector, as computed by r8gb_fa
#    or R8GB_TRF.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0

  for j in range ( 1, n + 1 ):
    det = det * a_lu[ml+mu,j-1]

  for i in range ( 1, n + 1 ):
    if ( pivot[i-1] != i ):
      det = - det

  return det

def r8gb_det_test ( ):

#*****************************************************************************80
#
## r8gb_det_test() tests r8gb_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 10
  n = m
  ml = 3
  mu = 2

  print ( '' )
  print ( 'r8gb_det_test():' )
  print ( '  r8gb_det() computes the determinant of an R8GB matrix' )
  print ( '  which has been factored by r8gb_fa.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )
#
#  Set the matrix.
#
  a = r8gb_random ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  A random R8GB matrix:' )
#
#  Copy the matrix into a general array.
#
  a2 = r8gb_to_r8ge ( m, n, ml, mu, a )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8gb_fa ( n, ml, mu, a )
#
#  Compute the determinant.
#
  det = r8gb_det ( n, ml, mu, a_lu, pivot )

  print ( '' )
  print ( '  r8gb_det() computes the determinant = ', det )
#
#  Recompute the determinant, using the R8GE matrix.
#
  determ = np.linalg.det ( a2 )

  print ( '  np.linalg.det() computes the determinant = ', determ )

  return

def r8gb_dif2 ( m, n, ml, mu ):

#*****************************************************************************80
#
## r8gb_dif2() sets up an R8GB second difference matrix.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#  Output:
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
  import numpy as np

  a = np.zeros ( [ 2 * ml + mu + 1, n ] )

  for j in range ( 1, n + 1 ):

    for diag in range ( 1, 2 * ml + mu + 2 ):

      i = diag + j - ml - mu - 1

      if ( i == j ):
        a[diag-1,j-1] = 2.0
      elif ( i == j - 1 or i == j + 1 ):
        a[diag-1,j-1] = -1.0

  return a

def r8gb_dif2_test ( ):

#*****************************************************************************80
#
## r8gb_dif2_test() tests r8gb_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  ml = 1
  mu = 1

  print ( '' )
  print ( 'r8gb_dif2_test():' )
  print ( '  r8gb_dif2() returns an R8GB second difference matrix.' )
  print ( '' )
  print ( '  Matrix rows M       = ', m )
  print ( '  Matrix columns N    = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_dif2 ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB second difference matrix:' )

  return

def r8gb_fa ( n, ml, mu, a ):

#*****************************************************************************80
#
## r8gb_fa() performs a LINPACK-style PLU factorization of a R8GB matrix.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    The following program segment will set up the input.
#
#      m = ml + mu + 1
#      do j = 1, n
#        i1 = max ( 1, j-mu )
#        i2 = min ( n, j+ml )
#        do i = i1, i2
#          k = i - j + m
#          a(k,j) = afull(i,j)
#        end do
#      end do
#
#    This uses rows ML+1 through 2*ML+MU+1 of the array A.
#    In addition, the first ML rows in the array are used for
#    elements generated during the triangularization.
#    The total number of rows needed in A is 2*ML+MU+1.
#    The ML+MU by ML+MU upper left triangle and the
#    ML by ML lower right triangle are not referenced.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2016
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
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A(2*ML+MU+1,N), the matrix in band storage.  The
#    columns of the matrix are stored in the columns of the array,
#    and the diagonals of the matrix are stored in rows ML+1 through
#    2*ML+MU+1.
#
#  Output:
#
#    real ALU(2*ML+MU+1,N), the LU factors in band storage.  
#    The L and U matrices are stored in a single array.
#
#    integer PIVOT(N), the pivot vector.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np

  alu = a.copy ( )
  pivot = np.zeros ( n, dtype = np.int32 )

  m = ml + mu + 1
  info = 0
#
#  Zero out the initial fill-in columns.
#
  j0 = mu + 2
  j1 = min ( n, m ) - 1

  for jz in range ( j0, j1 + 1 ):
    i0 = m + 1 - jz
    for i in range ( i0, ml + 1 ):
      alu[i-1,jz-1] = 0.0

  jz = j1
  ju = 0

  for k in range ( 1, n ):
#
#  Zero out the next fill-in column.
#
    jz = jz + 1

    if ( jz <= n ):
      for i in range ( 1, ml + 1 ):
        alu[i-1,jz-1] = 0.0
#
#  Find L = pivot index.
#
    lm = min ( ml, n - k )

    l = m

    for j in range ( m + 1, m + lm + 1 ):
      if ( abs ( alu[l-1,k-1] ) < abs ( alu[j-1,k-1] ) ):
        l = j

    pivot[k-1] = l + k - m
#
#  Zero pivot implies this column already triangularized.
#
    if ( alu[l-1,k-1] == 0.0 ):
      info = k
      print ( '' )
      print ( 'r8gb_fa(): Fatal error!' )
      print ( '  Zero pivot on step ', info )
      raise Exception ( 'r8gb_fa(): Fatal error!' )
#
#  Interchange if necessary.
#
    t = alu[l-1,k-1]
    alu[l-1,k-1] = alu[m-1,k-1]
    alu[m-1,k-1] = t
#
#  Compute multipliers.
#
    for i in range ( m + 1, m + lm + 1 ):
      alu[i-1,k-1] = - alu[i-1,k-1] / alu[m-1,k-1]
#
#  Row elimination with column indexing.
#
    ju = max ( ju, mu + pivot[k-1] )
    ju = min ( ju, n )
    mm = m

    for j in range ( k + 1, ju + 1 ):

      l = l - 1
      mm = mm - 1

      if ( l != mm ):
        t = alu[l-1,j-1]
        alu[l-1,j-1] = alu[mm-1,j-1]
        alu[mm-1,j-1] = t

      for i in range ( 0, lm ):
        alu[mm+i,j-1] = alu[mm+i,j-1] + alu[mm-1,j-1] * alu[m+i,k-1]

  pivot[n-1] = n

  if ( alu[m-1,n-1] == 0.0 ):
    info = n
    print ( '' )
    print ( 'r8gb_fa - Fatal error!' )
    print ( '  Zero pivot on step ', info )
    raise Exception ( 'r8gb_fa(): Fatal error!' )

  return alu, pivot, info

def r8gb_fa_test ( ):

#*****************************************************************************80
#
## r8gb_fa_test() tests r8gb_fa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = m
  ml = 1
  mu = 2

  print ( '' )
  print ( 'r8gb_fa_test():' )
  print ( '  r8gb_fa() computes the PLU factors of an R8GB matrix.' )
  print ( '' )
  print ( '  Number of matrix rows M    = ', m )
  print ( '  Number of matrix columns N = ', n )
  print ( '  Lower bandwidth ML         = ', ml )
  print ( '  Upper bandwidth MU         = ', mu )
#
#  Set the matrix.
#
  a = r8gb_random ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The banded matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8gb_mv ( m, n, ml, mu, a, x )
#
#  Factor the matrix.
#
  alu, pivot, info = r8gb_fa ( n, ml, mu, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8gb_fa_test - Fatal error!' )
    print ( '  r8gb_fa declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8gb_fa_test(): Fatal error!' )
#
#  Solve the linear system.
#
  job = 0
  x = r8gb_sl ( n, ml, mu, alu, pivot, b, job )

  r8vec_print ( n, x, '  Solution to A*x=b:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8gb_ml ( n, ml, mu, alu, pivot, x, job )

  r8vec_print ( n, b, '  Right hand side of transposed system:' )
#
#  Solve the linear system.
#
  job = 1
  x = r8gb_sl ( n, ml, mu, alu, pivot, b, job )

  r8vec_print ( n, x, '  Solution to A''x=b:' )

  return

def r8gb_indicator ( m, n, ml, mu ):

#*****************************************************************************80
#
## r8gb_indicator() sets up a R8GB indicator matrix.
#
#  Discussion:
#
#    Note that the R8GB storage format includes extra room for
#    fillin entries that occur during Gauss elimination.  This routine
#    will supply zero values for those entries.
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#  Output:
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
  import numpy as np

  a = np.zeros ( [ 2 * ml + mu + 1, n ] )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )
  k = 0

  for j in range ( 1, n + 1 ):
    for diag in range ( 1, 2 * ml + mu + 2 ):

      i = diag + j - ml - mu - 1

      if ( 1 <= i and i <= m and i - ml <= j and j <= i + mu ):
        a[diag-1,j-1] = float ( fac * i + j )
      elif ( 1 <= i and i <= m and i - ml <= j and j <= i + mu + ml ):
        value = 0.0
      else:
        k = k + 1
        a[diag-1,j-1] = - float ( k )

  return a

def r8gb_indicator_test ( ):

#*****************************************************************************80
#
## r8gb_indicator_test() tests r8gb_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 10
  n = 8
  ml = 3
  mu = 2

  print ( '' )
  print ( 'r8gb_indicator_test():' )
  print ( '  r8gb_indicator() returns an R8GB indicator matrix.' )
  print ( '' )
  print ( '  Matrix rows M       = ', m )
  print ( '  Matrix columns N    = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB indicator matrix:' )

  return

def r8gb_ml ( n, ml, mu, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## R8GB_ML computes A * x or A' * X, using r8gb_fa factors.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    It is assumed that r8gb_fa has overwritten the original matrix
#    information by LU factors.  R8GB_ML is able to reconstruct the
#    original matrix from the LU factor data.
#
#    R8GB_ML allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A_LU(2*ML+MU+1,N), the LU factors from r8gb_fa.
#
#    integer PIVOT(N), the pivot vector computed by r8gb_fa.
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
  b = x.copy ( )

  if ( job == 0 ):
#
#  Y = U * X.
#
    for j in range ( 1, n + 1 ):
      ilo = max ( 1, j - ml - mu )
      for i in range ( ilo, j ):
        b[i-1] = b[i-1] + a_lu[i-j+ml+mu,j-1] * b[j-1]
      b[j-1] = a_lu[j-j+ml+mu,j-1] * b[j-1]
#
#  B = PL * Y = PL * U * X = A * x.
#
    for j in range ( n - 1, 0, -1 ):

      ihi = min ( n, j + ml )
      for i in range ( j + 1, ihi + 1 ):
        b[i-1] = b[i-1] - a_lu[i-j+ml+mu,j-1] * b[j-1]

      k = pivot[j-1]

      if ( k != j ):
        temp = b[k-1]
        b[k-1] = b[j-1]
        b[j-1] = temp

  else:
#
#  Y = ( PL )' * X.
#
    for j in range ( 1, n ):

      k = pivot[j-1]

      if ( k != j ):
        temp = b[k-1]
        b[k-1] = b[j-1]
        b[j-1] = temp

      jhi = min ( n, j + ml )
      for i in range ( j + 1, jhi + 1 ):
        b[j-1] = b[j-1] - b[i-1] * a_lu[i-j+ml+mu,j-1]
#
#  B = U' * Y = ( PL * U )' * X = A' * X.
#
    for i in range ( n, 0, -1 ):

      jhi = min ( n, i + ml + mu )
      for j in range ( i + 1, jhi + 1 ):
        b[j-1] = b[j-1] + b[i-1] * a_lu[i-j+ml+mu,j-1]
      b[i-1] = b[i-1] * a_lu[i-i+ml+mu,i-1]

  return b

def r8gb_ml_test ( ):

#*****************************************************************************80
#
## R8GB_ML_test tests R8GB_ML.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 10
  n = m
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_ML_test' )
  print ( '  R8GB_ML computes A*x or A''*X' )
  print ( '  where A has been factored by r8gb_fa().' )
  print ( '' )
  print ( '  Matrix rows M              = ', m )
  print ( '  Matrix columns N           = ', n )
  print ( '  Lower bandwidth ML         = ', ml )
  print ( '  Upper bandwidth MU         = ', mu )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r8gb_random ( m, n, ml, mu )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8gb_mv ( m, n, ml, mu, a, x )
    else:
      b = r8gb_mtv ( m, n, ml, mu, a, x )
#
#  Factor the matrix.
#
    a_lu, pivot, info = r8gb_fa ( n, ml, mu, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8GB_ML_test - Fatal error!' )
      print ( '  r8gb_fa declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'r8gm_ml(): Fatal error!' )
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8gb_ml ( n, ml, mu, a_lu, pivot, x, job )

    if ( job == 0 ):
      r8vec2_print ( b, b2, '  A*x and PLU*x' )
    else:
      r8vec2_print ( b, b2, '  A''*x and (PLU)''*x' )

  return

def r8gb_mtv ( m, n, ml, mu, a, x ):

#*****************************************************************************80
#
## R8GB_MTV multiplies a vector by a R8GB matrix.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    LINPACK and LAPACK storage of general band matrices requires
#    an extra ML upper diagonals for possible fill in entries during
#    Gauss elimination.  This routine does not access any entries
#    in the fill in diagonals, because it assumes that the matrix
#    has NOT had Gauss elimination applied to it.  If the matrix
#    has been Gauss eliminated, then the routine R8GB_MU must be
#    used instead.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product X*A.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 1, n + 1 ):
    ilo = max ( 1, j - mu )
    ihi = min ( m, j + ml )
    for i in range ( ilo, ihi + 1 ):
      b[j-1] = b[j-1] + x[i-1] * a[i-j+ml+mu,j-1]

  return b

def r8gb_mtv_test ( ):

#*****************************************************************************80
#
## R8GB_MTV_test tests R8GB_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_MTV_test' )
  print ( '  R8GB_MTV computes b=A''*x, where A is an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M       = ', m )
  print ( '  Matrix columns N    = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_random ( m, n, ml, mu )
  r8gb_print ( m, n, ml, mu, a, '  The random R8GB matrix:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  x:' )

  b = r8gb_mtv ( m, n, ml, mu, a, x )
  r8vec_print ( n, b, '  b=A''*x:' )

  return

def r8gb_mu ( n, ml, mu, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## R8GB_MU computes A * x or A' * X, using R8GB_TRF factors.
#
#  Warning:
#
#    This routine must be updated to allow for rectangular matrices.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#    It is assumed that R8GB_TRF has overwritten the original matrix
#    information by LU factors.  R8GB_MU is able to reconstruct the
#    original matrix from the LU factor data.
#
#    R8GB_MU allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A_LU(2*ML+MU+1,N), the LU factors from R8GB_TRF.
#
#    integer PIVOT(N), the pivot vector computed by R8GB_TRF.
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
  b = x.copy ( )

  if ( job == 0 ):
#
#  Y = U * X.
#
    for j in range ( 1, n + 1 ):
      ilo = max ( 1, j - ml - mu )
      for i in range ( ilo, j ):
        b[i-1] = b[i-1] + a_lu[i-j+ml+mu,j-1] * b[j-1]
      b[j-1] = a_lu[j-j+ml+mu,j-1] * b[j-1]
#
#  B = PL * Y = PL * U * X = A * x.
#
    for j in range ( n - 1, 0, -1 ):

      ihi = min ( n, j + ml )
      for i in range ( j + 1, ihi + 1 ):
        b[i-1] = b[i-1] + a_lu[i-j+ml+mu,j-1] * b[j-1]

      k = pivot[j-1]

      if ( k != j ):
        t      = b[k-1]
        b[k-1] = b[j-1]
        b[j-1] = t

  else:
#
#  Y = ( PL )' * X.
#
    for j in range ( 1, n ):

      k = pivot[j-1]

      if ( k != j ):
        t      = b[k-1]
        b[k-1] = b[j-1]
        b[j-1] = t

      jhi = min ( n, j + ml )

      for i in range ( j + 1, jhi + 1 ):
        b[j-1] = b[j-1] + b[i-1] * a_lu[i-j+ml+mu,j-1]
#
#  B = U' * Y = ( PL * U )' * X = A' * X.
#
    for i in range ( n, 0, -1 ):

      jhi = min ( n, i + ml + mu )

      for j in range ( i + 1, jhi + 1 ):
        b[j-1] = b[j-1] + b[i-1] * a_lu[i-j+ml+mu,j-1]
      b[i-1] = b[i-1] * a_lu[i-i+ml+mu,i-1]

  return b

def r8gb_mu_test ( ):

#*****************************************************************************80
#
## R8GB_MU_test tests R8GB_MU.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 10
  n = m
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_MU_test' )
  print ( '  R8GB_MU computes A*x or A''*X' )
  print ( '  where A has been factored by R8GB_TRF.' )
  print ( '' )
  print ( '  Matrix rows M              = ', m )
  print ( '  Matrix columns N           = ', n )
  print ( '  Lower bandwidth ML         = ', ml )
  print ( '  Upper bandwidth MU         = ', mu )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r8gb_random ( m, n, ml, mu )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8gb_mv ( m, n, ml, mu, a, x )
    else:
      b = r8gb_mtv ( m, n, ml, mu, a, x )
#
#  Factor the matrix.
#
    a_lu, pivot, info = r8gb_trf ( m, n, ml, mu, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8GB_MU_test - Fatal error!' )
      print ( '  R8GB_TRF declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'r8gb_mu_test(): Fatal error!' )
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8gb_mu ( n, ml, mu, a_lu, pivot, x, job )

    if ( job == 0 ):
      r8vec2_print ( b, b2, '  A*x and PLU*x' )
    else:
      r8vec2_print ( b, b2, '  A''*x and (PLU)''*x' )

  return

def r8gb_mv ( m, n, ml, mu, a, x ):

#*****************************************************************************80
#
## R8GB_MV multiplies a R8GB matrix times a vector.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    LINPACK and LAPACK storage of general band matrices requires
#    an extra ML upper diagonals for possible fill in entries during
#    Gauss elimination.  This routine does not access any entries
#    in the fill in diagonals, because it assumes that the matrix
#    has NOT had Gauss elimination applied to it.  If the matrix
#    has been Gauss eliminated, then the routine R8GB_MU must be
#    used instead.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 1, m + 1 ):
    jlo = max ( 1, i - ml )
    jhi = min ( n, i + mu )
    for j in range ( jlo, jhi + 1 ):
      b[i-1] = b[i-1] + a[i-j+ml+mu,j-1] * x[j-1]

  return b

def r8gb_mv_test ( ):

#*****************************************************************************80
#
## R8GB_MV_test tests R8GB_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_MV_test' )
  print ( '  R8GB_MV computes b=A*x, where A is an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M       = ', m )
  print ( '  Matrix columns N    = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_random ( m, n, ml, mu )
  r8gb_print ( m, n, ml, mu, a, '  The random R8GB matrix:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  x:' )

  b = r8gb_mv ( m, n, ml, mu, a, x )
  r8vec_print ( n, b, '  b=A*x:' )

  return

def r8gb_nz_num ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## R8GB_NZ_NUM counts the nonzeros in a R8GB matrix.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine will examine
#    values it finds in these extra bands, so that both unfactored
#    and factored matrices can be handled.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
#  Output:
#
#    integer NZ_NUM, the number of nonzero entries in A.
#
  nz_num = 0

  for i in range ( 1, m + 1 ):
    jlo = max ( 1, i - ml )
    jhi = min ( n, i + mu + ml )
    for j in range ( jlo, jhi + 1 ):
      if ( a[i-j+ml+mu,j-1] != 0.0 ):
        nz_num = nz_num + 1

  return nz_num

def r8gb_nz_num_test ( ):

#*****************************************************************************80
#
## R8GB_NZ_NUM_test tests R8GB_NZ_NUM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 10
  n = m
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_NZ_NUM_test' )
  print ( '  R8GB_NZ_NUM counts the nonzero entries in an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M =              ', m )
  print ( '  Matrix columns N =           ', n )
  print ( '  Lower bandwidth ML         = ', ml )
  print ( '  Upper bandwidth MU         = ', mu )
#
#  Set the matrix.
#
  a = r8gb_random ( m, n, ml, mu )
#
#  Make some zero entries.
#
  for j in range ( 1, n + 1 ):
    for diag in range ( 1, 2 * ml + mu + 2 ):
      if ( a[diag-1,j-1] < 0.3 ):
        a[diag-1,j-1] = 0.0

  r8gb_print ( m, n, ml, mu, a, '  The R8GB matrix:' )

  nz_num = r8gb_nz_num ( m, n, ml, mu, a )

  print ( '' )
  print ( '  Nonzero entries = ', nz_num )

  return

def r8gb_print ( m, n, ml, mu, a, title ):

#*****************************************************************************80
#
## R8GB_PRINT prints a banded matrix.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1..
#
#    real A(2*ML+MU+1,N), the M by N band matrix, stored in LINPACK
#    or LAPACK general band storage mode.
#
#    string TITLE, a title to be printed.
#
  r8gb_print_some ( m, n, ml, mu, a, 0, 0, m - 1, n - 1, title )

  return

def r8gb_print_test ( ):

#*****************************************************************************80
#
## R8GB_PRINT_test tests R8GB_PRINT.
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
  m = 8
  n = 10
  ml = 1
  mu = 3

  print ( '' )
  print ( 'R8GB_PRINT_test' )
  print ( '  R8GB_PRINT prints an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB matrix:' )

  return

def r8gb_print_some ( m, n, ml, mu, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8GB_PRINT_SOME prints some of a banded matrix.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    Only entries in rows ILO to IHI, columns JLO to JHI are considered.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1..
#
#    real A(2*ML+MU+1,N), the M by N band matrix, stored in LINPACK
#    or LAPACK general band storage mode.
#
#    integer ILO, JLO, IHI, JHI, designate the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
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
    i2lo = max ( i2lo, j2lo - mu )

    i2hi = min ( ihi, m - 1 )
    i2hi = min ( i2hi, j2hi + ml )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )

      for j in range ( j2lo, j2hi + 1 ):

        if ( mu < j - i or ml < i - j ):
          print ( '              ', end = '' )
        else:
          print ( '%14g' % ( a[i-j+ml+mu,j] ), end = '' )

      print ( '' )

  return

def r8gb_print_some_test ( ):

#*****************************************************************************80
#
## R8GB_PRINT_SOME_test tests R8GB_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 1
  mu = 3

  print ( '' )
  print ( 'R8GB_PRINT_SOME_test' )
  print ( '  R8GB_PRINT_SOME prints some of an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print_some ( m, n, ml, mu, a, 4, 3, 6, 9, '  Rows(4-6), Cols (3-9)' )

  return

def r8gb_random ( m, n, ml, mu ):

#*****************************************************************************80
#
## r8gb_random() randomizes a R8GB matrix.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine assumes it is setting
#    up an unfactored matrix, so it only uses the first MU upper bands,
#    and does not place nonzero values in the fillin bands.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#  Output:
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ 2 * ml + mu + 1, n ] )

  for j in range ( 1, n + 1 ):
    for irow in range ( 1, 2 * ml + mu + 2 ):
      i = irow + j - ml - mu - 1
      if ( ml < irow and 1 <= i and i <= m ):
        r = rng.random ( )
        a[irow-1,j-1] = r
  
  return a

def r8gb_random_test ( ):

#*****************************************************************************80
#
## r8gb_random_test() tests r8gb_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_RANDOM_test' )
  print ( '  R8GB_RANDOM returns a random R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M       = ', m )
  print ( '  Matrix columns N    = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_random ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The random R8GB matrix:' )

  return

def r8gb_sl ( n, ml, mu, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## r8gb_sl() solves a system factored by r8gb_fa.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A_LU(2*ML+MU+1,N), the LU factors from r8gb_fa.
#
#    integer PIVOT(N), the pivot vector from r8gb_fa.
#
#    real B(N), the right hand side vector.
#
#    integer JOB.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution.
#
  x = b.copy ( )

  m = mu + ml + 1
#
#  Solve A * x = b.
#
  if ( job == 0 ):
#
#  Solve L * Y = B.
#
    if ( 1 <= ml ):

      for k in range ( 1, n ):

        lm = min ( ml, n - k )
        l = pivot[k-1]

        if ( l != k ):
          t      = x[l-1]
          x[l-1] = x[k-1]
          x[k-1] = t
        
        for i in range ( 1, lm + 1 ):
          x[k+i-1] = x[k+i-1] + x[k-1] * a_lu[m+i-1,k-1]
#
#  Solve U * X = Y.
#
    for k in range ( n, 0, -1 ):

      x[k-1] = x[k-1] / a_lu[m-1,k-1]
      lm = min ( k, m ) - 1
      la = m - lm
      lb = k - lm

      for i in range ( 0, lm ):
        x[lb+i-1] = x[lb+i-1] - x[k-1] * a_lu[la+i-1,k-1]
#
#  Solve A' * X = B.
#
  else:
#
#  Solve U' * Y = B.
#
    for k in range ( 1, n + 1 ):
      lm = min ( k, m ) - 1
      la = m - lm
      lb = k - lm
      for i in range ( 0, lm ):
        x[k-1] = x[k-1] - a_lu[la+i-1,k-1] * x[lb+i-1]
      x[k-1] = x[k-1] / a_lu[m-1,k-1]
#
#  Solve L' * X = Y.
#
    if ( 1 <= ml ):

      for k in range ( n - 1, 0, -1 ):

        lm = min ( ml, n - k )

        for i in range ( 1, lm + 1 ):
          x[k-1] = x[k-1] + a_lu[m+i-1,k-1] * x[k+i-1]
        l = pivot[k-1]

        if ( l != k ):
          t      = x[l-1]
          x[l-1] = x[k-1]
          x[k-1] = t

  return x

def r8gb_sl_test ( ):

#*****************************************************************************80
#
## R8GB_SL_test tests R8GB_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = m
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_SL_test' )
  print ( '  R8GB_SL solves a linear system factored by r8gb_fa.' )
  print ( '' )
  print ( '  Number of matrix rows M    = ', m )
  print ( '  Number of matrix columns N = ', n )
  print ( '  Lower bandwidth ML         = ', ml )
  print ( '  Upper bandwidth MU         = ', mu )
#
#  Set the matrix.
#
  a = r8gb_random ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The banded matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8gb_mv ( m, n, ml, mu, a, x )
#
#  Factor the matrix.
#
  alu, pivot, info = r8gb_fa ( n, ml, mu, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GB_SL_test - Fatal error!' )
    print ( '  r8gb_fa declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8gb_sl_test(): Fatal error!' )
#
#  Solve the linear system.
#
  job = 0
  x = r8gb_sl ( n, ml, mu, alu, pivot, b, job )

  r8vec_print ( n, x, '  Solution to A*x=b:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8gb_ml ( n, ml, mu, alu, pivot, x, job )

  r8vec_print ( n, b, '  Right hand side of transposed system:' )
#
#  Solve the linear system.
#
  job = 1
  x = r8gb_sl ( n, ml, mu, alu, pivot, b, job )

  r8vec_print ( n, x, '  Solution to A''x=b:' )

  return

def r8gb_to_r8ge ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## R8GB_TO_R8GE copies a R8GB matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
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
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrices.
#    M must be positive.
#
#    integer N, the number of columns of the matrices.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths of A1.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
#  Output:
#
#    real B(M,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )
 
  for i in range ( 1, m + 1 ):
    for j in range ( 1, n + 1 ):
      if ( i - ml <= j and j <= i + mu ):
        b[i-1,j-1] = a[ml+mu+i-j,j-1]

  return b

def r8gb_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8GB_TO_R8GE_test tests R8GB_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'R8GB_TO_R8GE_test' )
  print ( '  R8GB_TO_R8GE copies an R8GB matrix to an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB matrix:' )

  a_r8ge = r8gb_to_r8ge ( m, n, ml, mu, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8gb_to_r8st ( m, n, ml, mu, a, nz_num ):

#*****************************************************************************80
#
## r8gb_to_r8st() copies a R8GB matrix to a R8ST matrix.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine will copy nonzero
#    values it finds in these extra bands, so that both unfactored
#    and factored matrices can be handled.
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#    This routine reorders the entries of A so that the first N entries
#    are exactly the diagonal entries of the matrix, in order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrices.
#    M must be positive.
#
#    integer N, the number of columns of the matrices.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths of A1.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
#    integer NZ_NUM, the number of nonzero entries in A.
#
#  Output:
#
#    integer SYM, is 0 if the matrix is not symmetric, and 1
#    if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#    For this routine, SYM is always output 0.
#
#    integer ROW(NZ_NUM), the row indices.
#
#    integer COL(NZ_NUM), the column indices.
#
#    real B(NZ_NUM), the r8st matrix.
#
  import numpy as np

  row = np.zeros ( nz_num, dtype = int )
  col = np.zeros ( nz_num, dtype = int )
  b = np.zeros ( nz_num, dtype = float )

  sym = 0
  nz = 0

  for i in range ( 1, m + 1 ):
    for j in range ( 1, n + 1 ):
      if ( i - ml <= j and j <= i + mu + ml ):
        if ( a[ml+mu+i-j,j-1] != 0.0 ):

          if ( nz_num <= nz ):
            print ( '' )
            print ( 'R8GB_TO_r8st - Fatal error!' )
            print ( '  NZ_NUM = ', nz_num )
            print ( '  But the matrix has more nonzeros than that!' )
            raise Exception ( 'R8GB_TO_r8st - Fatal error!' )

          row[nz] = i
          col[nz] = j
          b[nz] = a[ml+mu+i-j,j-1]
          nz = nz + 1

  if ( nz < nz_num ):
    print ( '' )
    print ( 'R8GB_TO_r8st - Warning!' )
    print ( '  NZ_NUM = ', nz_num )
    print ( '  But the number of nonzeros is ', nz )

  return sym, row, col, b

def r8gb_to_r8st_test ( ):

#*****************************************************************************80
#
## r8gb_to_r8st_test() tests r8gb_to_r8st().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'R8GB_TO_r8st_test' )
  print ( '  R8GB_TO_r8st copies a R8GB matrix to a r8st matrix.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB matrix:' )

  nz_num = r8gb_nz_num ( m, n, ml, mu, a )

  print ( '  Nonzeros NZ_NUM =    ', nz_num )

  sym, row, col, b = r8gb_to_r8st ( m, n, ml, mu, a, nz_num )

  r8st_print ( m, n, nz_num, sym, row, col, b, '  The r8st matrix:' )

  return

def r8gb_to_r8sp ( m, n, ml, mu, a, nz_num ):

#*****************************************************************************80
#
## r8gb_to_r8sp() copies a R8GB matrix to a R8SP matrix.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine will copy nonzero
#    values it finds in these extra bands, so that both unfactored
#    and factored matrices can be handled.
#
#    The R8SP storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    It is possible that a pair of indices (I,J) may occur more than
#    once.  Presumably, in this case, the intent is that the actual value
#    of A(I,J) is the sum of all such entries.  This is not a good thing
#    to do, but I seem to have come across this in MATLAB.
#
#    The R8SP format is used by CSPARSE ("sparse triplet"), SLAP 
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrices.
#    M must be positive.
#
#    integer N, the number of columns of the matrices.
#    N must be positive.
#
#    integer ML, MU, the lower and upper bandwidths of A1.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
#    integer NZ_NUM, the number of nonzero entries in A.
#    This number can be obtained by calling R8GB_NZ_NUM.
#
#  Output:
#
#    integer ROW(NZ_NUM), the row indices.
#
#    integer COL(NZ_NUM), the column indices.
#
#    real B(NZ_NUM), the R8SP matrix.
#
  import numpy as np

  b = np.zeros ( nz_num )
  col = np.zeros ( nz_num, dtype = np.int32 )
  row = np.zeros ( nz_num, dtype = np.int32 )

  nz = 0

  for i in range ( 1, m + 1 ):

    jlo = max ( 1, i - ml )
    jhi = min ( n, i + mu + ml )

    for j in range ( jlo, jhi + 1 ):

      if ( a[ml+mu+i-j,j-1] == 0.0 ):
        continue

      if ( nz_num <= nz ):
        print ( '' )
        print ( 'R8GB_TO_R8SP - Fatal error!' )
        print ( '  NZ_NUM = ', nz_num )
        print ( '  But the matrix has more nonzeros than that!' )
        raise Exception ( 'R8GB_TO_DS3 - Fatal error!' )

      row[nz] = i
      col[nz] = j
      b[nz] = a[ml+mu+i-j,j-1]
      nz = nz + 1

  if ( nz < nz_num ):
    print ( '' )
    print ( 'R8GB_TO_R8SP - Warning!' )
    print ( '  NZ_NUM = ', nz_num )
    print ( '  But the number of nonzeros is ', nz )

  return row, col, b

def r8gb_to_r8sp_test ( ):

#*****************************************************************************80
#
## R8GB_TO_R8SP_test tests R8GB_TO_R8SP.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'R8GB_TO_R8SP_test' )
  print ( '  R8GB_TO_R8SP copies an R8GB matrix to an R8SP matrix.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB matrix:' )

  nz_num = r8gb_nz_num ( m, n, ml, mu, a )

  print ( '  Nonzeros NZ_NUM =    ', nz_num )

  row, col, a_r8sp = r8gb_to_r8sp ( m, n, ml, mu, a, nz_num )

  r8sp_print ( m, n, nz_num, row, col, a_r8sp, '  The R8SP matrix:' )

  return

def r8gb_to_r8vec ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## r8gb_to_r8vec() copies a R8GB matrix to an R8VEC.
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
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer ML, MU, the lower and upper bandwidths.
#
#    real A(2*ML+MU+1,N), the array to be copied.
#
#  Output:
#
#    real X((2*ML+MU+1)*N), the vector.
#
  import numpy as np

  x = np.zeros ( ( 2 * ml + mu + 1 ) * n )

  for j in range ( 1, n + 1 ):

    ihi = min ( ml + mu, ml + mu + 1 - j )
    for i in range ( 1, ihi + 1 ):
      x[i+(j-1)*(2*ml+mu+1)-1] = 0.0

    ilo = max ( ihi + 1, 1 )
    ihi = min ( 2 * ml + mu + 1, ml + mu + m + 1 - j )
    for i in range ( ilo, ihi + 1 ):
      x[i+(j-1)*(2*ml+mu+1)-1] = a[i-1,j-1]

    ilo = ihi + 1
    ihi = 2 * ml + mu + 1
    for i in range ( ilo, ihi + 1 ):
      x[i+(j-1)*(2*ml+mu+1)-1] = 0.0

  return x

def r8gb_to_r8vec_test ( ):

#*****************************************************************************80
#
## R8GB_TO_R8VEC_test tests R8GB_TO_R8VEC.
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
  m = 5
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'R8GB_TO_R8VEC_test' )
  print ( '  R8GB_TO_R8VEC converts an R8GB matrix to an R8VEC.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB indicator matrix:' )

  x = r8gb_to_r8vec ( m, n, ml, mu, a )

  k = 0
  for j in range ( 1, n + 1 ):
    for i in range ( 1, 2 * ml + mu + 2 ):
      k = k + 1
      print ( '%4d  %4d  %4d  %14f' % ( i, j, k, x[k-1] ) )

  return

def r8gb_trf ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## R8GB_TRF performs a LAPACK-style PLU factorization of a R8GB matrix.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#    This is a simplified, standalone version of the LAPACK
#    routine R8GBTRF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, the number of subdiagonals within the band of A.
#    0 <= ML.
#
#    integer MU, the number of superdiagonals within the band of A.
#    0 <= MU.
#
#    real A(2*ML+MU+1,N), the matrix A in band storage.
#
#  Output:
#
#    real A_LU(2*ML+MU+1,N), information about the PLU factorization.
#
#    integer PIVOT(min(M,N)), the pivot indices
#    for 1 <= i <= min(M,N), row i of the matrix was interchanged with
#    row IPIV(i).
#
#    integer INFO, error flag.
#    = 0: successful exit
#    < 0: an input argument was illegal
#    > 0: if INFO = +i, U(i,i) is exactly zero. The factorization
#         has been completed, but the factor U is exactly
#         singular, and division by zero will occur if it is used
#         to solve a system of equations.
#
  import numpy as np

  info = 0
  a_lu = a.copy ( )

  pivot = np.zeros ( n, dtype = np.int32 )
#
#  KV is the number of superdiagonals in the factor U, allowing for fill-in.
#
  kv = mu + ml
#
#  Set fill-in elements in columns MU+2 to KV to zero.
#
  for j in range ( mu + 2, min ( kv, n ) + 1 ):
    for i in range ( kv - j + 2, ml + 1 ):
      a_lu[i-1,j-1] = 0.0
#
#  JU is the index of the last column affected by the current stage
#  of the factorization.
#
  ju = 1

  for j in range ( 1, min ( m, n ) + 1 ):
#
#  Set the fill-in elements in column J+KV to zero.
#
    if ( j + kv <= n ):
      for i in range ( 1, ml + 1 ):
        a_lu[i-1,j+kv-1] = 0.0
#
#  Find the pivot and test for singularity.
#  KM is the number of subdiagonal elements in the current column.
#
    km = min ( ml, m - j )

    piv = abs ( a_lu[kv,j-1] )
    jp = kv + 1

    for i in range ( kv + 2, kv + km + 2 ):
      if ( piv < abs ( a_lu[i-1,j-1] ) ):
        piv = abs ( a_lu[i-1,j-1] )
        jp = i

    jp = jp - kv

    pivot[j-1] = jp + j - 1

    if ( a_lu[kv+jp-1,j-1] != 0.0 ):

      ju = max ( ju, min ( j + mu + jp - 1, n ) )
#
#  Apply interchange to columns J to JU.
#
      if ( jp != 1 ):

        for i in range ( 0, ju - j + 1 ):
          t                     = a_lu[kv+jp-i-1,j+i-1]
          a_lu[kv+jp-i-1,j+i-1] = a_lu[kv-i,j+i-1]
          a_lu[kv-i,j+i-1]      = t
#
#  Compute the multipliers.
#
      if ( 0 < km ):

        for i in range ( kv + 2, kv + km + 2 ):
          a_lu[i-1,j-1] = a_lu[i-1,j-1] / a_lu[kv,j-1]
#
#  Update the trailing submatrix within the band.
#
        if ( j < ju ):

          for k in range ( 1, ju - j + 1 ):

            if ( a_lu[kv-k,j+k-1] != 0.0 ):

              for i in range ( 1, km + 1 ):
                a_lu[kv+i-k,j+k-1] = a_lu[kv+i-k,j+k-1] \
                  - a_lu[kv+i,j-1] * a_lu[kv-k,j+k-1]

    else:
#
#  If pivot is zero, set INFO to the index of the pivot
#  unless a zero pivot has already been found.
#
      if ( info == 0 ):
        info = j

  return a_lu, pivot, info

def r8gb_trf_test ( ):

#*****************************************************************************80
#
## R8GB_TRF_test tests R8GB_TRF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10
  m = n
  ml = 1
  mu = 2
  nrhs = 1

  print ( '' )
  print ( 'R8GB_TRF_test' )
  print ( '  R8GB_TRF computes the PLU factors of an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8gb_random ( m, n, ml, mu )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8gb_mv ( m, n, ml, mu, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8gb_trf ( m, n, ml, mu, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GB_TRF_test - Fatal error!' )
    print ( '  R8GB_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8gb_trf_test(): Fatal error!' )
#
#  Solve the linear system.
#  Note that, because of quirks in MATLAB, we need to copy our vector-based
#  data to and from 2D arrays.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8gb_trs ( n, ml, mu, nrhs, 'N', a_lu, pivot, b_mat )
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
  b = r8gb_mu ( n, ml, mu, a_lu, pivot, x, job )
#
#  Solve the linear system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8gb_trs ( n, ml, mu, nrhs, 'T', a_lu, pivot, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )
  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8gb_trs ( n, ml, mu, nrhs, trans, a_lu, pivot, b ):

#*****************************************************************************80
#
## R8GB_TRS solves a linear system factored by R8GB_TRF.
#
#  Discussion:
#
#    The R8GB storage format is for an M by N banded matrix, with lower 
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML 
#    extra superdiagonals, which may be required to store nonzero entries 
#    generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer N, the order of the matrix A.
#    N must be positive.
#
#    integer ML, the number of subdiagonals within the band of A.
#    ML must be at least 0, and no greater than N - 1.
#
#    integer MU, the number of superdiagonals within the band of A.
#    MU must be at least 0, and no greater than N - 1.
#
#    integer NRHS, the number of right hand sides and the number of
#    columns of the matrix B.  NRHS must be positive.
#
#    character TRANS, specifies the form of the system.
#    'N':  A * x = b  (No transpose)
#    'T':  A'* X = B  (Transpose)
#    'C':  A'* X = B  (Conjugate transpose = Transpose)
#
#    real A_LU(2*ML+MU+1,N), the LU factors from R8GB_TRF.  
#
#    integer PIVOT(N), the pivot indices for 1 <= I <= N, row I
#    of the matrix was interchanged with row PIVOT(I).
#
#    real B(N,NRHS), the right hand side vectors.
#
#  Output:
#
#    real X(N,NRHS), the solution vectors, X.
#
#    integer INFO, error flag.
#    = 0:  successful exit
#    < 0: if INFO = -K, the K-th argument had an illegal value
#

#
#  Test the input.
#
  info = 0

  if ( trans != 'N' and trans != 'n' and \
       trans != 'T' and trans != 't' and \
       trans != 'C' and trans != 'c' ):
    info = -1
    return
  elif ( n <= 0 ):
    info = -2
    return
  elif ( ml < 0 ):
    info = -3
    return
  elif ( mu < 0 ):
    info = -4
    return
  elif ( nrhs <= 0 ):
    info = -5
    return

  x = b.copy ( )

  kd = mu + ml + 1
#
#  Solve A * x = b.
#
#  Solve L * x = b, overwriting b with x.
#
#  L is represented as a product of permutations and unit lower
#  triangular matrices L = P(1) * L(1) * ... * P(n-1) * L(n-1),
#  where each transformation L(i) is a rank-one modification of
#  the identity matrix.
#
  if ( trans == 'N' or trans == 'n' ):

    if ( 0 < ml ):

      for j in range ( 1, n ):

        lm = min ( ml, n - j )
        l = pivot[j-1]

        for k in range ( 1, nrhs + 1 ):
          t          = x[l-1,k-1]
          x[l-1,k-1] = x[j-1,k-1]
          x[j-1,k-1] = t

        for k in range ( 1, nrhs + 1 ):
          if ( x[j-1,k-1] != 0.0 ):
            for i in range ( 0, lm ):
              x[j+i,k-1] = x[j+i,k-1] - a_lu[kd+i,j-1] * x[j-1,k-1]
#
#  Solve U * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):

      for j in range ( n, 0, -1 ):
        if ( x[j-1,k] != 0.0 ):
          l = ml + mu + 1 - j
          x[j-1,k] = x[j-1,k] / a_lu[ml+mu,j-1]
          for i in range ( j - 1, max ( 1, j - ml - mu ) - 1, -1 ):
            x[i-1,k] = x[i-1,k] - a_lu[l+i-1,j-1] * x[j-1,k]

  else:
#
#  Solve A' * x = b.
#
#  Solve U' * x = b, overwriting b with x.
#
    for i in range ( 1, nrhs + 1 ):

      for j in range ( 1, n + 1 ):
        temp = x[j-1,i-1]
        l = ml + mu + 1 - j
        for k in range ( max ( 1, j - ml - mu ), j ):
          temp = temp - a_lu[l+k-1,j-1] * x[k-1,i-1]
        x[j-1,i-1] = temp / a_lu[ml+mu,j-1]
#
#  Solve L' * x = b, overwriting b with x.
#
    if ( 0 < ml ):

      for j in range ( n - 1, 0, -1 ):

        lm = min ( ml, n - j )

        for k in range ( 1, nrhs + 1 ):
          t = 0.0
          for i in range ( 0, lm ):
            t = t + x[j+i,k-1] * a_lu[kd+i,j-1]
          x[j-1,k-1] = x[j-1,k-1] - t

        l = pivot[j-1]

        for i in range ( 1, nrhs + 1 ):
          t          = x[l-1,i-1]
          x[l-1,i-1] = x[j-1,i-1]
          x[j-1,i-1] = t

  return x, info

def r8gb_trs_test ( ):

#*****************************************************************************80
#
## R8GB_TRS_test tests R8GB_TRS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10
  m = n
  ml = 1
  mu = 2
  nrhs = 1

  print ( '' )
  print ( 'R8GB_TRS_test' )
  print ( '  R8GB_TRS solves a linear system factored by R8GB_TRS.' )
  print ( '' )
  print ( '  Matrix rows M =      ', m )
  print ( '  Matrix columns N =   ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8gb_random ( m, n, ml, mu )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8gb_mv ( m, n, ml, mu, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8gb_trf ( m, n, ml, mu, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GB_TRS_test - Fatal error!' )
    print ( '  R8GB_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'r8gb_trs_test(): Fatal error!' )
#
#  Solve the linear system.
#  Note that, because of quirks in MATLAB, we need to copy our vector-based
#  data to and from 2D arrays.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8gb_trs ( n, ml, mu, nrhs, 'N', a_lu, pivot, b_mat )
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
  b = r8gb_mu ( n, ml, mu, a_lu, pivot, x, job )
#
#  Solve the linear system.
#
  b_mat = r8vec_to_r8ge ( n, nrhs, b )
  x_mat, info = r8gb_trs ( n, ml, mu, nrhs, 'T', a_lu, pivot, b_mat )
  x = r8ge_to_r8vec ( n, nrhs, x_mat )
  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8gb_zeros ( m, n, ml, mu ):

#*****************************************************************************80
#
## R8GB_ZEROS zeros an R8GB matrix.
#
#  Discussion:
#
#    An M by N banded matrix A with lower bandwidth ML and upper bandwidth MU
#    is assumed to be entirely zero, except for the main diagonal, and
#    entries in the ML nearest subdiagonals, and MU nearest superdiagonals.
#
#    LINPACK and LAPACK "R8GB" storage for such a matrix generally includes
#    room for ML extra superdiagonals, which may be required to store
#    nonzero entries generated during Gaussian elimination.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine assumes it is setting
#    up an unfactored matrix, so it only uses the first MU upper bands,
#    and does not place nonzero values in the fillin bands.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#  Output:
#
#    real A(2*ML+MU+1,N), the R8GB matrix.
#
  import numpy as np

  a = np.zeros ( [ 2 * ml + mu + 1, n ] )
  
  return a

def r8gb_zeros_test ( ):

#*****************************************************************************80
#
## R8GB_ZEROS_test tests R8GB_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8GB_ZEROS_test' )
  print ( '  R8GB_ZEROS returns an R8GB zero matrix.' )
  print ( '' )
  print ( '  Matrix rows M       = ', m )
  print ( '  Matrix columns N    = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_zeros ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB zero matrix:' )

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

def r8st_print ( m, n, nz_num, sym, row, col, a, title ):

#*****************************************************************************80
#
## r8st_print() prints a r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    integer SYM: the symmetry option. (ignored for now)
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    string TITLE, a title.
#
  r8st_print_some ( m, n, nz_num, row, col, a, 0, 0, m - 1, n - 1, title )

  return

def r8st_print_some ( m, n, nz_num, row, col, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8st_print_some() prints some of an r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M,  N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROW[NZ_NUM], COL[NZ_NUM], the row and column indices
#    of the nonzero elements.
#
#    real A[NZ_NUM], the nonzero elements 
#    of the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  import numpy as np

  incx = 5
  index = np.zeros ( incx, dtype = np.int32 )

  print ( '' )
  print ( title )
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )

    print ( '  Col: ', end = '' )
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      nonzero = False
 
      for j2 in range ( 0, inc ):
        index[j2] = -1

      for k in range ( 0, nz_num ):

        if ( i == row[k] and j2lo <= col[k] and col[k] <= j2hi ):

          j2 = col[k] - j2lo + 1

          if ( a[k] != 0.0 ):
            index[j2-1] = k
            nonzero = True

      if ( nonzero ):

        print ( '%5d ' % ( i ), end = '' )

        for j2 in range ( 0, inc ):

          if ( 0 <= index[j2] ):
            aij = a[index[j2]]
          else:
            aij = 0.0

          print ( '%14g' % ( aij ), end = '' )

        print ( '' )

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

def r8vec_to_r8gb ( m, n, ml, mu, x ):

#*****************************************************************************80
#
## r8vec_to_r8gb() copies an R8VEC into a R8GB matrix.
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
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer ML, MU, the lower and upper bandwidths.
#
#    real X((2*ML+MU+1)*N), the vector to be copied into the array.
#
#  Output:
#
#    real A(2*ML+MU+1,N), the array.
#
  import numpy as np

  a = np.zeros ( [ 2 * ml + mu + 1, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, 2 * ml + mu + 1 ):

      if ( 0 <= i + j - ml - mu and i + j - ml - mu <= m - 1 ):
        a[i,j] = x[i+j*(2*ml+mu+1)]

  return a

def r8vec_to_r8gb_test ( ):

#*****************************************************************************80
#
## r8vec_to_r8gb_test() tests r8vec_to_r8gb().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'r8vec_to_r8gb_test()' )
  print ( '  r8vec_to_r8gb() converts an R8VEC to an R8GB matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Lower bandwidth ML  = ', ml )
  print ( '  Upper bandwidth MU  = ', mu )

  a = r8gb_indicator ( m, n, ml, mu )

  r8gb_print ( m, n, ml, mu, a, '  The R8GB indicator matrix:' )

  x = r8gb_to_r8vec ( m, n, ml, mu, a )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, 2 * ml + mu + 1 ):
      print ( '%4d  %4d  %4d  %14g' % ( i, j, k, x[k] ) )
      k = k + 1

  a = r8vec_to_r8gb ( m, n, ml, mu, x )

  r8gb_print ( m, n, ml, mu, a, '  The recovered R8GB indicator matrix:' )

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
  r8gb_test ( )
  timestamp ( )
 
