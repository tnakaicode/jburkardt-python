#! /usr/bin/env python3
#
def r8cb_test ( ):

#*****************************************************************************80
#
## r8cb_test() tests r8cb().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8cb_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8cb().' )

  r8cb_det_test ( )
  r8cb_dif2_test ( )
  r8cb_indicator_test ( )
  r8cb_ml_test ( )
  r8cb_mtv_test ( )
  r8cb_mv_test ( )
  r8cb_np_fa_test ( )
  r8cb_np_sl_test ( )
  r8cb_print_test ( )
  r8cb_print_some_test ( )
  r8cb_random_test ( )
  r8cb_to_r8ge_test ( )
  r8cb_to_r8vec_test ( )
  r8cb_zeros_test ( )
  r8vec_to_r8cb_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8cb_test():' )
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

def r8cb_det ( n, ml, mu, a_lu ):

#*****************************************************************************80
#
## r8cb_det() computes the determinant of a R8CB matrix factored by R8CB_NP_FA.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2016
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
#    real A_LU(ML+MU+1,N), the LU factors from R8CB_NP_FA.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for j in range ( 0, n ):
    det = det * a_lu[mu,j]
 
  return det

def r8cb_det_test ( ):

#*****************************************************************************80
#
## r8cb_det_test() tests r8cb_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.linalg import det

  n = 5
  ml = 1
  mu = 1

  print ( '' )
  print ( 'r8cb_det_test():' )
  print ( '  r8cb_det() computes the determinant of a matrix' )
  print ( '  that has been factored by R8CB_NP_FA.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cb_dif2 ( n, n )

  r8cb_print ( n, n, ml, mu, a, '  The compact band matrix:' )
#
#  Copy the matrix into a general array.
#
  a2 = r8cb_to_r8ge ( n, n, ml, mu, a )
#
#  Factor the matrix.
#
  a_lu, info = r8cb_np_fa ( n, ml, mu, a )
#
#  Compute the determinant.
#
  determ = r8cb_det ( n, ml, mu, a_lu )

  print ( '' )
  print ( '  R8CB_DET computes the determinant         = ', determ )
#
#  Compare with scipy.linalg.det()
#
  determ = det ( a2 )

  print ( '  scipy.linalg.det computes the determinant = ', determ )

  return

def r8cb_dif2 ( m, n ):

#*****************************************************************************80
#
## r8cb_dif2() sets up an R8CB second difference matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer m, n: the order of the matrix.
#
#  Output:
#
#    real a(3,n): the R8CB matrix.
#
  import numpy as np

  ml = 1
  mu = 1
  a = np.zeros ( [ ml + mu + 1, n ] )

  for j in range ( 0, n ):

    for diag in range ( 0, ml + mu + 1 ):

      i = diag + j - mu

      if ( i == j ):
        a[diag,j] = 2.0
      elif ( i == j - 1 ):
        if ( 0 < j ):
          a[diag,j] = -1.0
      elif ( i == j + 1 ):
        if ( j < n - 1 ):
          a[diag,j] = -1.0

  return a

def r8cb_dif2_test ( ):

#*****************************************************************************80
#
## r8cb_dif2_test() tests r8cb_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
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
  print ( 'r8cb_dif2_test()' )
  print ( '  r8cb_dif2() returns the second difference matrix as an R8CB matrix' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_dif2 ( m, n )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB second difference matrix:' )

  return

def r8cb_indicator ( m, n, ml, mu ):

#*****************************************************************************80
#
## r8cb_indicator() sets up a R8CB indicator matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically ML+MU+1 by N.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
#    real A(ML+MU+1,N), the R8CB matrix.
#
  import numpy as np

  a = np.zeros ( [ ml + mu + 1, n ] )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )
  k = 0

  for j in range ( 0, n ):
    for diag in range ( 0, ml + mu + 1 ):

      i = diag + j - mu

      if ( 0 <= i and i < m ):
        value = float ( fac * ( i + 1 ) + ( j + 1 ) )
      else:
        k = k + 1
        value = - k

      a[diag,j] = value

  return a

def r8cb_indicator_test ( ):

#*****************************************************************************80
#
## R8CB_INDICATOR_TEST tests R8CB_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 2
  mu = 3

  print ( '' )
  print ( 'R8CB_INDICATOR_TEST' )
  print ( '  R8CB_INDICATOR computes the indicator matrix in R8CB format' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB indicator matrix:' )

  return

def r8cb_ml ( n, ml, mu, a_lu, x, job ):

#*****************************************************************************80
#
## R8CB_ML computes A * x or A' * X, using R8CB_NP_FA factors.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#    It is assumed that R8CB_NP_FA has overwritten the original matrix
#    information by LU factors.  R8CB_ML is able to reconstruct the
#    original matrix from the LU factor data.
#
#    R8CB_ML allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
#    real A_LU(ML+MU+1,N), the compact band matrix, factored by R8CB_NP_FA.
#
#    real X(N), the vector to be multiplied.
#
#    integer JOB, specifies the operation to be done:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * x.
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
        b[i-1] = b[i-1] + a_lu[i-j+mu,j-1] * b[j-1]
      b[j-1] = a_lu[j-j+mu,j-1] * b[j-1]
#
#  B = PL * Y = PL * U * X = A * x.
#
    for j in range ( n - 1, 0, -1 ):

      ihi = min ( n, j + ml )
      for i in range ( j + 1, ihi + 1 ):
        b[i-1] = b[i-1] - a_lu[i-j+mu,j-1] * b[j-1]

  else:
#
#  Y = ( PL )' * X.
#
    for j in range ( 1, n ):

      jhi = min ( n, j + ml )
      for i in range ( j + 1, jhi + 1 ):
        b[j-1] = b[j-1] - b[i-1] * a_lu[i-j+mu,j-1]
#
#  B = U' * Y = ( PL * U )' * X = A' * X.
#
    for i in range ( n, 0, -1 ):

      jhi = min ( n, i + ml + mu )
      for j in range ( i + 1, jhi + 1 ):
        b[j-1] = b[j-1] + b[i-1] * a_lu[i-j+mu,j-1]
      b[i-1] = b[i-1] * a_lu[i-i+mu,i-1]

  return b

def r8cb_ml_test ( ):

#*****************************************************************************80
#
## R8CB_ML_TEST tests R8CB_ML.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8CB_ML_TEST' )
  print ( '  R8CB_ML computes A*x or A\'*x for an R8CB matrix A' )
  print ( '  after A has been factored by R8CB_FA.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r8cb_random ( n, n, ml, mu )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8cb_mv ( n, n, ml, mu, a, x )
    else:
      b = r8cb_mtv ( n, n, ml, mu, a, x )
#
#  Factor the matrix.
#
    a_lu, info = r8cb_np_fa ( n, ml, mu, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8CB_ML_TEST - Fatal error!' )
      print ( '  R8CB_FA declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'R8CB_ML_TEST - Fatal error!' )
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8cb_ml ( n, ml, mu, a_lu, x, job )

    if ( job == 0 ):
      r8vec2_print ( b, b2, '  A*x and PLU*x' )
    else:
      r8vec2_print ( b, b2, '  A\'*x and (PLU)\'*x' )

  return

def r8cb_mtv ( m, n, ml, mu, a, x ):

#*****************************************************************************80
#
## R8CB_MTV multiplies a vector by a R8CB matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A(ML+MU+1,N), the R8CB matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product X*A.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, m ):
    jlo = max ( 0, i - ml )
    jhi = min ( n - 1, i + mu )
    for j in range ( jlo, jhi + 1 ):
      b[j] = b[j] + x[i] * a[i-j+mu,j]

  return b

def r8cb_mtv_test ( ):

#*****************************************************************************80
#
## R8CB_MTV_TEST tests R8CB_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'R8CB_MTV_TEST' )
  print ( '  R8CB_MTV computes b=A\'*x, where A is an R8CB matrix' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( m, x, '  The vector x:' )

  b = r8cb_mtv ( m, n, ml, mu, a, x )

  r8vec_print ( n, b, '  The product b=A\'*x:' )

  return

def r8cb_mv ( m, n, ml, mu, a, x ):

#*****************************************************************************80
#
## R8CB_MV multiplies a R8CB matrix times a vector.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A(ML+MU+1,N), the R8CB matrix.
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
    jlo = max ( 0, i - ml )
    jhi = min ( n - 1, i + mu )
    for j in range ( jlo, jhi + 1 ):
      b[i] = b[i] + a[i-j+mu,j] * x[j]

  return b

def r8cb_mv_test ( ):

#*****************************************************************************80
#
## R8CB_MV_TEST tests R8CB_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 8
  ml = 2
  mu = 1

  print ( '' )
  print ( 'R8CB_MV_TEST' )
  print ( '  R8CB_MV computes b=A*x, where A is an R8CB matrix' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( m, x, '  The vector x:' )

  b = r8cb_mv ( m, n, ml, mu, a, x )

  r8vec_print ( n, b, '  The product b=A*x:' )

  return

def r8cb_np_fa ( n, ml, mu, a ):

#*****************************************************************************80
#
## r8cb_np_fa() factors a R8CB matrix by Gaussian elimination.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#    R8CB_NP_FA is a version of the LINPACK routine R8GBFA, modifed to use
#    no pivoting, and to be applied to the R8CB compressed band matrix storage
#    format.  It will fail if the matrix is singular, or if any zero
#    pivot is encountered.
#
#    If R8CB_NP_FA successfully factors the matrix, R8CB_NP_SL may be called
#    to solve linear systems involving the matrix.
#
#    The matrix is stored in a compact version of LINPACK general
#    band storage, which does not include the fill-in entires.
#    The following program segment will store the entries of a banded
#    matrix in the compact format used by this routine:
#
#      m = mu+1
#      do j = 1, n
#        i1 = max ( 1, j-mu )
#        i2 = min ( n, j+ml )
#        do i = i1, i2
#          k = i-j+m
#          a(k,j) = afull(i,j)
#        end do
#      end do
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
#    real A(ML+MU+1,N), the compact band matrix.
#
#  Output:
#
#    real A_LU(ML+MU+1,N), the LU factors of the matrix.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  a_lu = a.copy ( )
#
#  The value of M is MU + 1 rather than ML + MU + 1.
#
  m = mu + 1
  info = 0
  ju = 0

  for k in range ( 1, n ):
#
#  If our pivot entry A(MU+1,K) is zero, then we must give up.
#
    if ( a_lu[m,k-1] == 0.0 ):
      info = k
      print ( '' )
      print ( 'R8CB_NP_FA - Fatal error!' )
      print ( '  Zero pivot on step ', info )
      raise Exception ( 'R8CB_NP_FA - Fatal error!' )
#
#  LM counts the number of nonzero elements that lie below the current
#  diagonal entry, A(K,K).
#
#  Multiply the LM entries below the diagonal by -1/A(K,K), turning
#  them into the appropriate "multiplier" terms in the L matrix.
#
    lm = min ( ml, n - k )

    for i in range ( m + 1, m + lm + 1 ):
      a_lu[i-1,k-1] = - a_lu[i-1,k-1] / a_lu[m-1,k-1]
#
#  MM points to the row in which the next entry of the K-th row is, A(K,J).
#  We then add L(I,K)*A(K,J) to A(I,J) for rows I = K+1 to K+LM.
#
    ju = max ( ju, mu + k )
    ju = min ( ju, n )
    mm = m

    for j in range ( k + 1, ju + 1 ):
      mm = mm - 1
      for i in range ( 0, lm ):
        a_lu[mm+i,j-1] = a_lu[mm+i,j-1] + a_lu[mm-1,j-1] * a_lu[m+i,k-1]

  if ( a_lu[m-1,n-1] == 0.0 ):
    info = n
    print ( '' )
    print ( 'R8CB_NP_FA - Fatal error!' )
    print ( '  Zero pivot on step ', info )
    raise Exception ( 'R8CB_NP_FA - Fatal error!' )

  return a_lu, info

def r8cb_np_fa_test ( ):

#*****************************************************************************80
#
## R8CB_NP_FA_TEST tests R8CB_NP_FA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8CB_NP_FA_TEST' )
  print ( '  R8CB_NP_FA factors an R8CB matrix with no pivoting' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r8cb_random ( n, n, ml, mu )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the right hand side.
#
    if ( job == 0 ):
      b = r8cb_mv ( n, n, ml, mu, a, x )
    else:
      b = r8cb_mtv ( n, n, ml, mu, a, x )
#
#  Factor the matrix.
#
    a_lu, info = r8cb_np_fa ( n, ml, mu, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8CB_NP_FA_TEST - Fatal error!' )
      print ( '  R8CB_NP_FA claims the matrix is singular.' )
      print ( '  The value of info is ', info )
      raise Exception ( 'R8CB_NP_FA_TEST - Fatal error!' )
#
#  Solve the system.
#
    x = r8cb_np_sl ( n, ml, mu, a_lu, b, job )

    if ( job == 0 ):
      r8vec_print ( n, x, '  Solution:' )
    else:
      r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8cb_np_sl ( n, ml, mu, a_lu, b, job ):

#*****************************************************************************80
#
## R8CB_NP_SL solves a R8CB system factored by R8CB_NP_FA.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#    R8CB_NP_SL can also solve the related system A' * x = b.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
#    real A_LU(ML+MU+1,N), the compact band matrix, factored by R8CB_NP_FA.
#
#    real B(N), the right hand side of the linear system.
#
#    integer JOB.
#    If JOB is zero, the routine will solve A * x = b.
#    If JOB is nonzero, the routine will solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  x = b.copy ( )
#
#  The value of M is ML + 1, rather than MU + ML + 1.
#
  m = mu + 1
#
#  Solve A * x = b.
#
  if ( job == 0 ):
#
#  Solve PL * Y = B.
#
    if ( 0 < ml ):

      for k in range ( 1, n ):

        lm = min ( ml, n - k )
        
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
#  Solve ( PL )' * X = Y.
#
    if ( 1 <= ml ):

      for k in range ( n - 1, 0, -1 ):

        lm = min ( ml, n - k )

        for i in range ( 1, lm + 1 ):
          x[k-1] = x[k-1] + a_lu[m+i-1,k-1] * x[k+i-1]

  return x

def r8cb_np_sl_test ( ):

#*****************************************************************************80
#
## R8CB_NP_SL_TEST tests R8CB_NP_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10
  ml = 1
  mu = 2

  print ( '' )
  print ( 'R8CB_NP_SL_TEST' )
  print ( '  R8CB_NP_SL solves a linear system factored by R8CB_NP_FA.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r8cb_random ( n, n, ml, mu )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the right hand side.
#
    if ( job == 0 ):
      b = r8cb_mv ( n, n, ml, mu, a, x )
    else:
      b = r8cb_mtv ( n, n, ml, mu, a, x )
#
#  Factor the matrix.
#
    a_lu, info = r8cb_np_fa ( n, ml, mu, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8CB_NP_SL_TEST - Fatal error!' )
      print ( '  R8CB_NP_FA claims the matrix is singular.' )
      print ( '  The value of info is ', info )
      raise Exception ( 'R8CB_NP_SL_TEST - Fatal error!' )
#
#  Solve the system.
#
    x = r8cb_np_sl ( n, ml, mu, a_lu, b, job )

    if ( job == 0 ):
      r8vec_print ( n, x, '  Solution:' )
    else:
      r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8cb_print ( m, n, ml, mu, a, title ):

#*****************************************************************************80
#
## R8CB_PRINT prints a R8CB matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(ML+MU+1,N), the R8CB matrix.
#
#    string TITLE, a title to be printed.
#
  r8cb_print_some ( m, n, ml, mu, a, 0, 0, m - 1, n - 1, title )

  return

def r8cb_print_test ( ):

#*****************************************************************************80
#
## R8CB_PRINT_TEST tests R8CB_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 2
  mu = 3

  print ( '' )
  print ( 'R8CB_PRINT_TEST' )
  print ( '  R8CB_PRINT prints an R8CB matrix' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB matrix:' )

  return

def r8cb_print_some ( m, n, ml, mu, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8CB_PRINT_SOME prints some of a R8CB matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    real A(ML+MU+1,N), the R8CB matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
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
          print ( '%14g' % ( a[i-j+mu,j] ), end = '' )

      print ( '' )

  return

def r8cb_print_some_test ( ):

#*****************************************************************************80
#
## R8CB_PRINT_SOME_TEST tests R8CB_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 2
  mu = 3

  print ( '' )
  print ( 'R8CB_PRINT_SOME_TEST' )
  print ( '  R8CB_PRINT_SOME prints some of an R8CB matrix' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print_some ( m, n, ml, mu, a, 3, 3, 6, 6, '  Rows 3-6, Cols 3-6:' )

  return

def r8cb_random ( m, n, ml, mu ):

#*****************************************************************************80
#
## R8CB_RANDOM randomizes a R8CB matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#  Output:
#
#    real A(ML+MU+1,N), the R8CB matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ ml + mu + 1, n ] )
#
#  Set the entries that correspond to matrix elements.
#
  for j in range ( 0, n ):

    ilo = max ( 0, j - mu )
    ihi = min ( m - 1, j + ml )

    for i in range ( ilo, ihi + 1 ):
      a[i-j+mu,j] = rng.uniform ( )

  return a

def r8cb_random_test ( ):

#*****************************************************************************80
#
## r8cb_random_test() tests r8cb_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 2
  mu = 3

  print ( '' )
  print ( 'R8CB_RANDOM_TEST' )
  print ( '  R8CB_RANDOM randomizes an R8CB matrix' )
  print ( '' )
  print ( '  Matrix order M     = ', m )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cb_random ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB random matrix:' )

  return

def r8cb_to_r8ge ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## r8cb_to_r8ge() copies a R8CB matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrices.
#
#    integer ML, MU, the lower and upper bandwidths of A.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#    real A(ML+MU+1,N), the R8CB matrix.
#
#  Output:
#
#    real B(M,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( j - mu <= i and i <= j + ml ):
        b[i,j] = a[i-j+mu,j]

  return b

def r8cb_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8cb_to_r8ge_test() tests r8cb_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 2
  mu = 3

  print ( '' )
  print ( 'R8CB_TO_R8GE_TEST' )
  print ( '  R8CB_TO_R8GE converts an R8CB matrix to R8GE format' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB matrix:' )

  a_r8ge = r8cb_to_r8ge ( m, n, ml, mu, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8cb_to_r8vec ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## r8cb_to_r8vec() copies a R8CB matrix to an R8VEC.
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
#    26 July 2016
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
#    real A(ML+MU+1,N), the array to be copied.
#
#  Output:
#
#    real X((ML+MU+1)*N), the vector.
#
  import numpy as np

  x = np.zeros ( ( ml + mu + 1 ) * n )

  for j in range ( 0, n ):

    ilo = max ( mu - j, 0 )
    ihi = mu + min ( ml, m - j - 1 )
    for i in range ( ilo, ihi + 1 ):
      x[i+j*(ml+mu+1)] = a[i,j]

  return x

def r8cb_to_r8vec_test ( ):

#*****************************************************************************80
#
## R8CB_TO_R8VEC_TEST tests R8CB_TO_R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
  print ( 'R8CB_TO_R8VEC_TEST' )
  print ( '  R8CB_TO_R8VEC converts an R8CB matrix to an R8VEC.' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB indicator matrix:' )

  x = r8cb_to_r8vec ( m, n, ml, mu, a )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, ml + mu + 1 ):
      print ( '%4d  %4d  %4d  %14g' % ( i, j, k, x[k] ) )
      k = k + 1

  a = r8vec_to_r8cb ( m, n, ml, mu, x )

  r8cb_print ( m, n, ml, mu, a, '  The recovered R8CB indicator matrix:' )

  return

def r8cb_zeros ( m, n, ml, mu ):

#*****************************************************************************80
#
## R8CB_ZEROS zeros an R8CB matrix.
#
#  Discussion:
#
#    The R8CB storage format is appropriate for a compact banded matrix.
#    It is assumed that the matrix has lower and upper bandwidths ML and MU,
#    respectively.  The matrix is stored in a way similar to that used
#    by LINPACK and LAPACK for a general banded matrix, except that in
#    this mode, no extra rows are set aside for possible fillin during pivoting.
#    Thus, this storage mode is suitable if you do not intend to factor
#    the matrix, or if you can guarantee that the matrix can be factored
#    without pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N-1.
#
#  Output:
#
#    real A(ML+MU+1,N), the R8CB matrix.
#
  import numpy as np

  a = np.zeros ( [ ml + mu + 1, n ] )

  return a

def r8cb_zeros_test ( ):

#*****************************************************************************80
#
## r8cb_zeros_test() tests r8cb_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2016
#
#  Author:
#
#    John Burkardt
#
  m = 8
  n = 10
  ml = 2
  mu = 3

  print ( '' )
  print ( 'r8cb_zeros_test()' )
  print ( '  r8cb_zeros() zeros an R8CB matrix' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_zeros ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB zero matrix:' )

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

def r8vec_to_r8cb ( m, n, ml, mu, x ):

#*****************************************************************************80
#
## r8vec_to_r8cb() copies an R8VEC into a R8CB matrix.
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
#    26 July 2016
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
#    real X((ML+MU+1)*N), the vector to be copied into the array.
#
#  Output:
#
#    real A(ML+MU+1,N), the array.
#
  import numpy as np

  a = np.zeros ( [ ml + mu + 1, n ] )

  for j in range ( 0, n ):
    for k in range ( 0, ml + mu + 1 ):
      i = k + j - mu
      if ( 0 <= i and i < m ):
        a[k,j] = x[k+j*(ml+mu+1)]

  return a

def r8vec_to_r8cb_test ( ):

#*****************************************************************************80
#
## R8VEC_TO_R8CB_TEST tests R8VEC_TO_R8CB.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2016
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
  print ( 'R8VEC_TO_R8CB_TEST' )
  print ( '  R8VEC_TO_R8CB converts an R8VEC to an R8CB matrix.' )
  print ( '' )
  print ( '  Matrix rows M      = ', m )
  print ( '  Matrix columns N   = ', n )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cb_indicator ( m, n, ml, mu )

  r8cb_print ( m, n, ml, mu, a, '  The R8CB indicator matrix:' )

  x = r8cb_to_r8vec ( m, n, ml, mu, a )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, ml + mu + 1 ):
      print ( '%4d  %4d  %4d  %14g' % ( i, j, k, x[k] ) )
      k = k + 1

  a = r8vec_to_r8cb ( m, n, ml, mu, x )

  r8cb_print ( m, n, ml, mu, a, '  The recovered R8CB indicator matrix:' )

  return

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
  r8cb_test ( )
  timestamp ( )
