#! /usr/bin/env python3
#
def r8cbb_test ( ):

#*****************************************************************************80
#
## r8cbb_test() tests r8cbb().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8cbb_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8cbb().' )

  rng = default_rng ( )

  r8cbb_add_test ( )
  r8cbb_dif2_test ( )
  r8cbb_fa_test ( rng )
  r8cbb_get_test ( rng )
  r8cbb_indicator_test ( )
  r8cbb_mtv_test ( )
  r8cbb_mv_test ( )
  r8cbb_print_test ( rng )
  r8cbb_print_some_test ( rng )
  r8cbb_random_test ( rng )
  r8cbb_set_test ( )
  r8cbb_sl_test ( rng )
  r8cbb_to_r8ge_test ( )
  r8cbb_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8cbb_test():' )
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
      print ( 'R8CB_NP_FA(): Fatal error!' )
      print ( '  Zero pivot on step ', info )
      raise Exception ( 'R8CB_NP_FA(): Fatal error!' )
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
    print ( 'R8CB_NP_FA(): Fatal error!' )
    print ( '  Zero pivot on step ', info )
    raise Exception ( 'R8CB_NP_FA(): Fatal error!' )

  return a_lu, info

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

def r8cbb_add ( n1, n2, ml, mu, a, i, j, value ):

#*****************************************************************************80
#
## r8cbb_add() adds a value to an entry of a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= n1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
#    integer I, J, the indices of the entry to be incremented.
#
#    real VALUE, the value to be added to the (I,J) entry.
#
#  Output:
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the modified R8CBB matrix.
#
  import numpy as np

# a = np.zeros ( ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2 )

  if ( value == 0.0 ):
    return a
#
#   Check for I or J out of bounds.
#
  if ( i < 0 or n1 + n2 <= i ):
    print ( '' )
    print ( 'R8CBB_ADD(): Fatal error!' )
    print ( '  Illegal input value of row index I = ', i )
    raise Exception ( 'R8CBB_ADD(): Fatal error!' )

  if ( j < 0 or n1 + n2 <= j ):
    print ( '' )
    print ( 'R8CBB_ADD(): Fatal error!' )
    print ( '  Illegal input value of column index J = ', j )
    raise Exception ( 'R8CBB_ADD(): Fatal error!' )
#
#  The A1 block of the matrix.
#
#  Check for out of band problems.
#
  if ( i < n1 and j < n1 ):

    if ( mu < j - i or ml < i - j ):
      print ( '' )
      print ( 'R8CBB_ADD(): Fatal error!' )
      print ( '  Unable to add to entry (', i, ',', j, ').' )
      raise Exception ( 'R8CBB_ADD(): Fatal error!' )
 
    ij = ( i - j + mu ) + j * ( ml + mu + 1 )
#
#  The A2 block of the matrix:
#
  elif ( i < n1 and n1 <= j ):
    ij = ( ml + mu + 1 ) * n1 + ( j - n1 ) * n1 + i
#
#  The A3 and A4 blocks of the matrix.
#
  elif ( n1 <= i ):
    ij = ( ml + mu + 1 ) * n1 + n2 * n1 + j * n2 + ( i - n1 )

  a[ij] = a[ij] + value

  return a

def r8cbb_add_test ( ):

#*****************************************************************************80
#
## R8CBB_ADD_TEST tests R8CBB_ADD.
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
  n1 = 3
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 0
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_ADD_TEST' )
  print ( '  R8CBB_ADD adds a value to elements of an R8CBB matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Initialize matrix to indicator matrix.
#
  a = r8cbb_indicator ( n1, n2, ml, mu )
#
#  Print initial matrix.
#
  r8cbb_print ( n1, n2, ml, mu, a, '  Matrix before additions:' )
#
#  Add 100 to band diagonal.
#
  for i in range ( 0, n1 ):
    j = i
    value = 100.0
    a = r8cbb_add ( n1, n2, ml, mu, a, i, j, value )
#
#  Add 200 to right border.
#
  for i in range ( 0, n1 ):
    for j in range ( n1, n1 + n2 ):
      value = 200.0
      a = r8cbb_add ( n1, n2, ml, mu, a, i, j, value )
#
#  Add 400 to offdiagonals in lower right dense matrix.
#
  for i in range ( n1, n1 + n2 ):
    for j in range ( n1, n1 + n2 ):
      if ( i != j ):
        value = 400.0
        a = r8cbb_add ( n1, n2, ml, mu, a, i, j, value )

  r8cbb_print ( n1, n2, ml, mu, a, '  The matrix after additions:' )

  return

def r8cbb_dif2 ( n1, n2, ml, mu ):

#*****************************************************************************80
#
## R8CBB_DIF2 sets up an R8CBB second difference matrix.
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
#    integer N1, N2, the order of the banded and dense 
#    blocks.  N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    1 <= ML, 1 <= MU.
#
#  Output:
#
#    real A((ML+MU+1)*N1+2*N1*N2+N2*N2), the R8CBB matrix.
#
  import numpy as np

  a = np.zeros ( ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2 )

  if ( ml < 1 or mu < 1 ):
    print ( '' )
    print ( 'R8CBB_DIF2(): Fatal error!' )
    print ( '  1 <= ML and 1 <= MU required.' )
    raise Exception ( 'R8CBB_DIF2(): Fatal error!' )

  for i in range ( 1, n1 + n2 ):
    j = i - 1
    value = - 1.0
    a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  for i in range ( 0, n1 + n2 ):
    j = i
    value = 2.0
    a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  for i in range ( 0, n1 + n2 - 1 ):
    j = i + 1
    value = - 1.0
    a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  return a

def r8cbb_dif2_test ( ):

#*****************************************************************************80
#
## R8CBB_DIF2_TEST tests R8CBB_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_DIF2_TEST' )
  print ( '  R8CBB_DIF2 sets up an R8CBB second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cbb_dif2 ( n1, n2, ml, mu )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB second difference matrix:' )

  return

def r8cbb_fa ( n1, n2, ml, mu, a ):

#*****************************************************************************80
#
## R8CBB_FA factors a R8CBB matrix.
#
#  Discussion:
#
#    Note that in C++ and FORTRAN, we can look at A as an abstract
#    vector, but then look at parts of A as storing a two dimensional
#    array.  MATLAB assigns an inherent dimensionality to a data object,
#    and gets very unhappy when you try to manipulate the data yourself.
#    This means that the MATLAB implementation of this routine requires
#    the use of temporary 2D arrays.
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#
#    Once the matrix has been factored by R8CBB_FA, R8CBB_SL may be called
#    to solve linear systems involving the matrix.
#
#    R8CBB_FA uses special non-pivoting versions of LINPACK routines to
#    carry out the factorization.  The special version of the banded
#    LINPACK solver also results in a space saving, since no entries
#    need be set aside for fill in due to pivoting.
#
#    The linear system must be border banded, of the form:
#
#      ( A1 A2 ) (X1) = (B1)
#      ( A3 A4 ) (X2)   (B2)
#
#    where A1 is a (usually big) banded square matrix, A2 and A3 are
#    column and row strips which may be nonzero, and A4 is a dense
#    square matrix.
#
#    The algorithm rewrites the system as:
#
#         X1 + inverse(A1) A2 X2 = inverse(A1) B1
#
#      A3 X1 +             A4 X2 = B2
#
#    and then rewrites the second equation as
#
#      ( A4 - A3 inverse(A1) A2 ) X2 = B2 - A3 inverse(A1) B1
#
#    The algorithm will certainly fail if the matrix A1 is singular,
#    or requires pivoting.  The algorithm will also fail if the A4 matrix,
#    as modified during the process, is singular, or requires pivoting.
#    All these possibilities are in addition to the failure that will
#    if the total matrix A is singular.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A( (ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the compact 
#    border-banded coefficient matrix.
#
#  Output:
#
#    real A_LU( (ML+MU+1)*N1 + 2*N1*N2 + N2*N2).
#    information describing a partial factorization
#    of the original coefficient matrix.  
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np

  nband = ( ml + mu + 1 ) * n1
#
#  A_LU should be as big as A.
#
  a_lu = a.copy ( )
#
#  A1 is the compact band matrix portion of A.
#  A1_LU is the LU factorization of A1.
#  A_LU can store A1_LU.
#
  if ( 0 < n1 ):

    a1 = r8vec_to_r8cb ( n1, n1, ml, mu, a )

    a1_lu, info = r8cb_np_fa ( n1, ml, mu, a1 )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8CBB_FA(): Fatal error!' )
      print ( '  R8CB_NP_FA returned INFO = ', info )
      print ( '  Factoring failed for column INFO.' )
      print ( '  The band matrix A1 is singular.' )
      print ( '  This algorithm cannot continue!' )
      raise Exception ( 'R8CBB_FA(): Fatal error!' )

    a_lu[0:nband] = r8cb_to_r8vec ( n1, n1, ml, mu, a1_lu )

  if ( 0 < n1 and 0 < n2 ):
#
#  A2 is the N1 x N2 strip to the right of A1.
#  Let B2 be column J of A2.
#  Let X2 solve A1 * X2 = - B2.
#  Store each X2 into A_LU.
#
    b2 = np.zeros ( n1 )

    job = 0

    for j in range ( 0, n2 ):
      b2[0:n1] = - a[nband+j*n1:nband+j*n1+n1]
      x2 = r8cb_np_sl ( n1, ml, mu, a1_lu, b2, job )
      a_lu[nband+j*n1:nband+j*n1+n1] = x2[0:n1]
#
#  Set A4 := A4 + A3*A2
#
    for i in range ( 0, n2 ):
      for j in range ( 0, n1 ):
        ij = nband + n1 * n2 + j * n2 + i
        for k in range ( 0, n2 ):
          ik = nband + 2 * n1 * n2 + k * n2 + i
          jk = nband + k * n1 + j
          a_lu[ik] = a_lu[ik] + a_lu[ij] * a_lu[jk]
#
#  Factor A4.
#
  if ( 0 < n2 ):

    a4 = r8vec_to_r8ge ( n2, n2, a_lu[nband+2*n1*n2:nband+2*n1*n2+n2*n2] )

    a4_lu, info = r8ge_np_fa ( n2, a4 )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8CBB_FA(): Fatal error!' )
      print ( '  R8GE_NP_FA returned INFO = ',info )
      print ( '  This indicates singularity in column INFO' )
      info = n1 + info
      print ( '  of the A4 submatrix, which is column ', info )
      print ( '  of the full matrix.' )
      print ( '' )
      print ( '  It is possible that the full matrix is ' )
      print ( '  nonsingular, but the algorithm R8CBB_FA may' )
      print ( '  not be used for this matrix.' )
      raise Exception ( 'R8CBB_FA(): Fatal error!' )

    a_lu[nband+2*n1*n2:nband+2*n1*n2+n2*n2] = r8ge_to_r8vec ( n2, n2, a4_lu )

  return a_lu, info

def r8cbb_fa_test ( rng ):

#*****************************************************************************80
#
## r8cbb_fa_test() tests r8cbb_fa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'r8cbb_fa_test():' )
  print ( '  r8cbb_fa() factors an R8CBB matrix, with no pivoting.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_random ( n1, n2, ml, mu, rng )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8cbb_mv ( n1, n2, ml, mu, a, x )
#
#  Factor the matrix
#
  a_lu, info = r8cbb_fa ( n1, n2, ml, mu, a )

  r8cbb_print ( n1, n2, ml, mu, a_lu, '  The factored matrix:' )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8CBB_FA_TEST(): Fatal error!' )
    print ( '  R8CBB_FA claims the matrix is singular.' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'R8CBB_FA_TEST(): Fatal error!' )
#
#  Solve the system.
#
  r8vec_print ( n, b, '  The right hand side vector:' )

  x = r8cbb_sl ( n1, n2, ml, mu, a_lu, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8cbb_get ( n1, n2, ml, mu, a, i, j ):

#*****************************************************************************80
#
## R8CBB_GET returns the value of an entry of a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
#    integer I, J, the row and column of the entry to retrieve.
#
#  Output:
#
#    real VALUE, the value of the (I,J) entry.
#

#
#  Check for I or J out of bounds.
#
  if ( i < 0 or n1 + n2 <= i ):
    print ( '' )
    print ( 'R8CBB_GET(): Fatal error!' )
    print ( '  Illegal input value of row index I = ', i )
    raise Exception ( 'R8CBB_GET(): Fatal error!' )

  if ( j < 0 or n1 + n2 <= j ):
    print ( '' )
    print ( 'R8CBB_GET(): Fatal error!' )
    print ( '  Illegal input value of column index J = ', j )
    raise Exception ( 'R8CBB_GET(): Fatal error!' )
#
#  The A1 block of the matrix.
#
#  Check for out of band problems.
#
  if ( i <= n1 and j <= n1 ):

    if ( mu < ( j - i ) or ml < ( i - j ) ):
      value = 0.0
      return value

    ij = ( i - j + mu ) + j * ( ml + mu + 1 )
#
#  The A2 block of the matrix:
#
  elif ( i <= n1 and n1 < j ):

    ij = ( ml + mu + 1 ) * n1 + ( j - n1 ) * n1 + i
#
#  The A3 and A4 blocks of the matrix.
#
  elif ( n1 < i ):

    ij = ( ml + mu + 1 ) * n1 + n2 * n1 + j * n2 + ( i - n1 )

  value = a[ij]

  return value

def r8cbb_get_test ( rng ):

#*****************************************************************************80
#
## r8cbb_get_test() tests r8cbb_get().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n1 = 3
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 0
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'r8cbb_get_test()' )
  print ( '  r8cbb_get() gets a value of an element of an R8CBB matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set matrix to indicator matrix.
#
  a = r8cbb_indicator ( n1, n2, ml, mu )
#
#  Print matrix.
#
  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix to be queried:' )
#
#  Request random entries.
#
  print ( '' )
  for k in range ( 0, 10 ):
    i = rng.integers ( 0, n1 + n2, endpoint = False )
    j = rng.integers ( 0, n1 + n2, endpoint = False )
    value = r8cbb_get ( n1, n2, ml, mu, a, i, j )
    print ( '  A(', i, ',', j, ') = ', value )

  return

def r8cbb_indicator ( n1, n2, ml, mu ):

#*****************************************************************************80
#
## r8cbb_indicator() sets up a R8CBB indicator matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the R8BB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
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
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative and no greater than N1-1.
#
#  Output:
#
#    real A((ML+MU+1)*N1+2*N1*N2+N2*N2), the R8CBB matrix.
#
  import numpy as np

  a = np.zeros ( ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2 )

  fac = 10 ** ( i4_log_10 ( n1 + n2 ) + 1 )
#
#  Set the banded matrix A1.
#
  for j in range ( 0, n1 ):
    for row in range ( 0, ml + mu + 1 ):
      i = row + j - mu
      if ( 1 <= i and i <= n1 ):
        a[row+j*(ml+mu+1)] = float ( fac * ( i + 1 ) + ( j + 1 ) )
#
#  Set the N1 by N2 rectangular strip A2.
#
  base = ( ml + mu + 1 ) * n1

  for i in range ( 0, n1 ):
    for j in range ( n1, n1 + n2 ):
      a[base + i + (j-n1)*n1 ] = float ( fac * ( i + 1 ) + ( j + 1 ) )
#
#  Set the N2 by N1 rectangular strip A3.
#
  base = ( ml + mu + 1 ) * n1 + n1 * n2

  for i in range ( n1, n1 + n2 ):
    for j in range ( 0, n1 ):
      a[base + i - n1 + j*n2 ] = float ( fac * ( i + 1 ) + ( j + 1 ) )
#
#  Set the N2 by N2 square A4.
#
  base = ( ml + mu + 1 ) * n1 + n1 * n2 + n2 * n1

  for i in range ( n1, n1 + n2 ):
    for j in range ( n1, n1 + n2 ):
      a[base + i-n1 + (j-n1)*n2 ] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8cbb_indicator_test ( ):

#*****************************************************************************80
#
## R8CBB_INDICATOR_TEST tests R8CBB_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_INDICATOR_TEST' )
  print ( '  R8CBB_INDICATOR sets up an R8CBB indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cbb_indicator ( n1, n2, ml, mu )

  r8cbb_print ( n1, n2, ml, mu, a, '  The compact border-banded matrix:' )

  return

def r8cbb_mtv ( n1, n2, ml, mu, a, x ):

#*****************************************************************************80
#
## R8CBB_MTV multiplies a vector by a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= n1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
#    real X(N1+N2), the vector to multiply the matrix.
#
#  Output:
#
#    real B(N1+N2), the product X * A.
#
  import numpy as np
#
#  Set B to zero.
#
  b = np.zeros ( n1 + n2 )
#
#  Multiply by A1.
#
  for j in range ( 0, n1 ):
    ilo = max ( 0, j - mu )
    ihi = min ( n1 - 1, j + ml )
    ij = j * ( ml + mu + 1 ) - j + mu
    for k in range ( ilo, ihi + 1 ):
      b[j] = b[j] + x[k] * a[k+ij]
#
#  Multiply by A2.
#
  for j in range ( n1, n1 + n2 ):
    ij = ( ml + mu + 1 ) * n1 + ( j - n1 ) * n1
    for k in range ( 0, n1 ):
      b[j] = b[j] + x[k] * a[k+ij]
#
#  Multiply by A3 and A4.
#
  for j in range ( 0, n1 + n2 ):
    ij = ( ml + mu + 1 ) * n1 + n1 * n2 + j * n2 - n1
    for k in range ( n1, n1 + n2 ):
      b[j] = b[j] + x[k] * a[k+ij]

  return b

def r8cbb_mtv_test ( ):

#*****************************************************************************80
#
## R8CBB_MTV_TEST tests R8CBB_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 6
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_MTV_TEST' )
  print ( '  R8CBB_MTV computes b=A\'*x, where A is an R8CBB matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_indicator ( n1, n2, ml, mu )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix A:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8cbb_mtv ( n1, n2, ml, mu, a, x )

  r8vec_print ( n, b, '  The product b=A\'*x:' )

  return

def r8cbb_mv ( n1, n2, ml, mu, a, x ):

#*****************************************************************************80
#
## R8CBB_MV multiplies a R8CBB matrix times a vector.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
#    real X(N1+N2), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N1+N2), the result of multiplying A by X.
#
  import numpy as np
#
#  Set B to zero.
#
  b = np.zeros ( n1 + n2 )
#
#  Multiply by A1.
#
  for j in range ( 0, n1 ):
    ilo = max ( 0, j - mu )
    ihi = min ( n1 - 1, j + ml )
    ij = j * ( ml + mu + 1 ) - j + mu
    for i in range ( ilo, ihi + 1 ):
      b[i] = b[i] + a[i+ij] * x[j]
#
#  Multiply by A2.
#
  for j in range ( n1, n1 + n2 ):
    ij = ( ml + mu + 1 ) * n1 + ( j - n1 ) * n1
    for i in range ( 0, n1 ):
      b[i] = b[i] + a[i+ij] * x[j]
#
#  Multiply by A3 and A4.
#
  for j in range ( 0, n1 + n2 ):
    ij = ( ml + mu + 1 ) * n1 + n1 * n2 + j * n2 - n1
    for i in range ( n1, n1 + n2 ):
      b[i] = b[i] + a[i+ij] * x[j]

  return b

def r8cbb_mv_test ( ):

#*****************************************************************************80
#
## R8CBB_MV_TEST tests R8CBB_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 6
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_MV_TEST' )
  print ( '  R8CBB_MV computes b=A*x, where A is an R8CBB matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_indicator ( n1, n2, ml, mu )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix A:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8cbb_mv ( n1, n2, ml, mu, a, x )

  r8vec_print ( n, b, '  The product b=A*x:' )

  return

def r8cbb_print ( n1, n2, ml, mu, a, title ):

#*****************************************************************************80
#
## R8CBB_PRINT prints a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A((ML+MU+1)*N1+2*N1*N2+N2*N2), the R8CBB matrix.
#
#    string TITLE, a title to be printed.
#
  r8cbb_print_some ( n1, n2, ml, mu, a, 0, 0, n1 + n2 - 1, n1 + n2 - 1, title )

  return

def r8cbb_print_test ( rng ):

#*****************************************************************************80
#
## r8cbb_print_test() tests r8cbb_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'r8cbb_print_test():' )
  print ( '  r8cbb_print() prints an R8CBB matrix' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_random ( n1, n2, ml, mu, rng )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix:' )

  return

def r8cbb_print_some ( n1, n2, ml, mu, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8cbb_print_some() prints some of a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A((ML+MU+1)*N1+2*N1*N2+N2*N2), the R8CBB matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n1 + n2 - 1 )
    j2hi = min ( j2hi, jhi )

    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n1 + n2 - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )

      for j in range ( j2lo, j2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
        aij = r8cbb_get ( n1, n2, ml, mu, a, i, j )

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8cbb_print_some_test ( rng ):

#*****************************************************************************80
#
## r8cbb_print_some_test() tests r8cbb_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'r8cbb_print_some_test():' )
  print ( '  r8cbb_print_some() prints some of an R8CBB matrix' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_random ( n1, n2, ml, mu, rng )

  r8cbb_print_some ( n1, n2, ml, mu, a, 1, 9, 10, 10, '  Rows 1-10, Cols 9-10' )

  return

def r8cbb_random ( n1, n2, ml, mu, rng ):

#*****************************************************************************80
#
## R8CBB_RANDOM randomizes a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative and no greater than N1-1.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
  import numpy as np

  a = np.zeros ( ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2 )

  for j in range ( 0, n1 ):
    for row in range ( 0, ml + mu + 1 ):
      i = row + j - mu
      if ( 0 <= i and i < n1 ):
        a[row+j*(ml+mu+1)] = rng.random ( )
#
#  Randomize the rectangular strips A2+A3+A4.
#
  klo = ( ml + mu + 1 ) * n1
  khi = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2
  for k in range ( klo, khi ):
    a[k] = rng.random ( )

  return a

def r8cbb_random_test ( rng ):

#*****************************************************************************80
#
## r8cbb_random_test() tests r8cbb_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'r8cbb_random_test():' )
  print ( '  r8cbb_random() generates a random R8CBB matrix' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_random ( n1, n2, ml, mu, rng )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix:' )

  return

def r8cbb_set ( n1, n2, ml, mu, a, i, j, value ):

#*****************************************************************************80
#
## R8CBB_SET sets the value of an entry in a R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
#    integer I, J, the row and column of the entry to set.
#
#    real VALUE, the value to be assigned to the (I,J) entry.
#
#  Output:
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the updated R8CBB matrix.
#

#
#  Check for I or J out of bounds.
#
  if ( i < 0 or n1 + n2 <= i ):
    print ( '' )
    print ( 'R8CBB_SET(): Fatal error!' )
    print ( '  Illegal input value of row index I = ', i )
    raise Exception ( 'R8CBB_SET(): Fatal error!' )

  if ( j < 0 or n1 + n2 <= j ):
    print ( '' )
    print ( 'R8CBB_SET(): Fatal error!' )
    print ( '  Illegal input value of column index J = ', j )
    raise Exception ( 'R8CBB_SET(): Fatal error!' )
#
#  The A1 block of the matrix.
#
#  Check for out of band problems.
#
  if ( i < n1 and j < n1 ):

    if ( mu < j - i or ml < i - j ):
      print ( '' )
      print ( 'R8CBB_SET(): Fatal error!' )
      print ( '  Unable to set entry (', i, ',', j, ').' )
      raise Exception ( 'R8CBB_SET(): Fatal error!' )

    ij = ( i - j + mu ) + j * ( ml + mu + 1 )
#
#  The A2 block of the matrix:
#
  elif ( i < n1 and n1 <= j ):
    ij = ( ml + mu + 1 ) * n1 + ( j - n1 ) * n1 + i
#
#  The A3 and A4 blocks of the matrix.
#
  elif ( n1 <= i ):
    ij = ( ml + mu + 1 ) * n1 + n2 * n1 + j * n2 + ( i - n1 )
  else:
    print ( '' )
    print ( 'R8CBB_SET(): Fatal error!' )
    print ( '  Unable to set entry (', i, ',', j, ').' )
    raise Exception ( 'R8CBB_SET(): Fatal error!' )

  a[ij] = value

  return a

def r8cbb_set_test ( ):

#*****************************************************************************80
#
## R8CBB_SET_TEST tests R8CBB_SET.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 4
  n2 = 1
  n = n1 + n2
  ml = 2
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_SET_TEST' )
  print ( '  R8CBB_SET sets the value of an element of an R8CBB matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Initialize matrix to zero.
#
  a = r8cbb_zeros ( n1, n2, ml, mu )
#
#  Set matrix entries to the "indicator" values.
#
  for i in range ( 0, n1 ):
    jlo = max ( 0, i - ml )
    jhi = min ( n1, i + mu )
    for j in range ( jlo, jhi + 1 ):
      value = float ( 10 * ( i + 1 ) + ( j + 1 ) )
      a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  for i in range ( 0, n1 ):
    for j in range ( n1, n1 + n2 ):
      value = float ( 10 * ( i + 1 ) + ( j + 1 ) )
      a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  for i in range ( n1, n1 + n2 ):
    for j in range ( 0, n1 ):
      value = float ( 10 * ( i + 1 ) + ( j + 1 ) )
      a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  for i in range ( n1, n1 + n2 ):
    for j in range ( n1, n1 + n2 ):
      value = float ( 10 * ( i + 1 ) + ( j + 1 ) )
      a = r8cbb_set ( n1, n2, ml, mu, a, i, j, value )

  r8cbb_print ( n1, n2, ml, mu, a, '  The matrix after additions:' )

  return

def r8cbb_sl ( n1, n2, ml, mu, a_lu, b ):

#*****************************************************************************80
#
## R8CBB_SL solves a R8CBB system factored by R8CBB_FA.
#
#  Discussion:
#
#    Note that in C++ and FORTRAN, we can look at A as an abstract
#    vector, but then look at parts of A as storing a two dimensional
#    array.  MATLAB assigns an inherent dimensionality to a data object,
#    and gets very unhappy when you try to manipulate the data yourself.
#    This means that the MATLAB implementation of this routine requires
#    the use of temporary 2D arrays.
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#    The linear system A * x = b is decomposable into the block system:
#
#      ( A1 A2 ) * (X1) = (B1)
#      ( A3 A4 )   (X2)   (B2)
#
#    where A1 is a (usually big) banded square matrix, A2 and A3 are
#    column and row strips which may be nonzero, and A4 is a dense
#    square matrix.
#
#    All the arguments except B are input quantities only, which are
#    not changed by the routine.  They should have exactly the same values
#    they had on return from R8CBB_FA.
#
#    If more than one right hand side is to be solved, with the same
#    matrix, R8CBB_SL should be called repeatedly.  However, R8CBB_FA only
#    needs to be called once to create the factorization.
#
#    See the documentation of R8CBB_FA for details on the matrix storage.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A_LU( (ML+MU+1)*N1 + 2*N1*N2 + N2*N2).
#    the compact border banded matrix, as factored by R8CBB_FA.
#
#    real B(N1+N2), the right hand side of the linear system.
#
#  Output:
#
#    real X(N1+N2), the solution.
#
  import numpy as np

  x = np.zeros ( n1 + n2 )

  nband = ( ml + mu + 1 ) * n1
#
#  Set B1 := inverse(A1) * B1.
#
  if ( 0 < n1 ):

    a1_lu = r8vec_to_r8cb ( n1, n1, ml, mu, a_lu[0:nband] )

    job = 0

    x[0:n1] = r8cb_np_sl ( n1, ml, mu, a1_lu, b[0:n1], job )
#
#  Modify the right hand side of the second linear subsystem.
#  Replace B2 by B2-A3*B1.
#
  for j in range ( 0, n1 ):
    for i in range ( 0, n2 ):
      ij = nband + n1 * n2 + j * n2 + i
      b[n1+i] = b[n1+i] - a_lu[ij] * x[j]
#
#  Solve A4*B2 = B2.
#
  if ( 0 < n2 ):

    a4_lu = r8vec_to_r8ge ( n2, n2, a_lu[nband+2*n1*n2:nband+2*n1*n2+n2*n2] )

    job = 0
    x[n1:n1+n2] = r8ge_np_sl ( n2, a4_lu, b[n1:n1+n2], job )
#
#  Modify the first subsolution.
#  Set B1 = B1+A2*B2.
#
  for i in range ( 0, n1 ):
    for j in range ( 0, n2 ):
      ij = nband + j * n1 + i
      x[i] = x[i] + a_lu[ij] * x[n1+j]

  return x

def r8cbb_sl_test ( rng ):

#*****************************************************************************80
#
## r8cbb_sl_test() tests r8cbb_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'r8cbb_sl_test():' )
  print ( '  r8cbb_sl() solves a linear system factored by R8CBB_FA' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8cbb_random ( n1, n2, ml, mu, rng )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8cbb_mv ( n1, n2, ml, mu, a, x )
#
#  Factor the matrix
#
  a_lu, info = r8cbb_fa ( n1, n2, ml, mu, a )

  r8cbb_print ( n1, n2, ml, mu, a_lu, '  The factored matrix:' )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8CBB_SL_TEST(): Fatal error!' )
    print ( '  R8CBB_FA claims the matrix is singular.' )
    print ( '  The value of INFO is ', info )
    raise Exception ( 'R8CBB_SL_TEST(): Fatal error!' )
#
#  Solve the system.
#
  r8vec_print ( n, b, '  The right hand side vector:' )

  x = r8cbb_sl ( n1, n2, ml, mu, a_lu, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8cbb_to_r8ge ( n1, n2, ml, mu, a ):

#*****************************************************************************80
#
## R8CBB_TO_R8GE copies a R8CBB matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= n1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative, and no greater than N1-1.
#
#    real A((ML+MU+1)*N1+2*N1*N2+N2*N2), the R8CBB matrix.
#
#  Output:
#
#    real B(N1+N2,N1+N2), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n1 + n2, n1 + n2 ] )

  for i in range ( 0, n1 ):
    for j in range ( 0, n1 ):

      if ( i - ml <= j and j <= i + mu ):
        ij = ( i - j + mu ) + j * ( ml + mu + 1 )
        b[i,j] = a[ij]

  for i in range ( 0, n1 ):
    for j in range ( n1, n1 + n2 ):
      ij = ( ml + mu + 1 ) * n1 + ( j - n1 ) * n1 + i
      b[i,j] = a[ij]

  for i in range ( n1, n1 + n2 ):
    for j in range ( 0, n1 + n2 ):
      ij = ( ml + mu + 1 ) * n1 + n2 * n1 + j * n2 + ( i - n1 )
      b[i,j] = a[ij]

  return b

def r8cbb_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8CBB_TO_R8GE_TEST tests R8CBB_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_TO_R8GE_TEST' )
  print ( '  R8CBB_TO_R8GE converts an R8CBB matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cbb_indicator ( n1, n2, ml, mu )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB matrix:' )

  a_r8ge = r8cbb_to_r8ge ( n1, n2, ml, mu, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8cbb_zeros ( n1, n2, ml, mu ):

#*****************************************************************************80
#
## R8CBB_ZEROS zeros an R8CBB matrix.
#
#  Discussion:
#
#    The R8CBB storage format is for a compressed border banded matrix.  
#    Such a matrix has the logical form:
#
#      A1 | A2
#      ---+---
#      A3 | A4
#
#    with A1 a (usually large) N1 by N1 banded matrix, while A2, A3 and A4
#    are dense rectangular matrices of orders N1 by N2, N2 by N1, and N2 by N2,
#    respectively.  
#
#    The R8CBB format is the same as the DBB format, except that the banded
#    matrix A1 is stored in compressed band form rather than standard
#    banded form.  In other words, we do not include the extra room
#    set aside for fill in during pivoting.
#
#    A should be defined as a vector.  The user must then store
#    the entries of the four blocks of the matrix into the vector A.
#    Each block is stored by columns.
#
#    A1, the banded portion of the matrix, is stored in
#    the first (ML+MU+1)*N1 entries of A, using the obvious variant
#    of the LINPACK general band format.
#
#    The following formulas should be used to determine how to store
#    the entry corresponding to row I and column J in the original matrix:
#
#    Entries of A1:
#
#      1 <= I <= N1, 1 <= J <= N1, (J-I) <= MU and (I-J) <= ML.
#
#      Store the I, J entry into location
#      (I-J+MU+1)+(J-1)*(ML+MU+1).
#
#    Entries of A2:
#
#      1 <= I <= N1, N1+1 <= J <= N1+N2.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+(J-N1-1)*N1+I.
#
#    Entries of A3:
#
#      N1+1 <= I <= N1+N2, 1 <= J <= N1.
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#
#    Entries of A4:
#
#      N1+1 <= I <= N1+N2, N1+1 <= J <= N1+N2
#
#      Store the I, J entry into location
#      (ML+MU+1)*N1+N1*N2+(J-1)*N2+(I-N1).
#      (same formula used for A3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the order of the banded and dense blocks.
#    N1 and N2 must be nonnegative, and at least one must be positive.
#
#    integer ML, MU, the lower and upper bandwidths.
#    ML and MU must be nonnegative and no greater than N1-1.
#
#  Output:
#
#    real A((ML+MU+1)*N1 + 2*N1*N2 + N2*N2), the R8CBB matrix.
#
  import numpy as np

  nn = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  a = np.zeros ( nn )

  return a

def r8cbb_zeros_test ( ):

#*****************************************************************************80
#
## R8CBB_ZEROS_TEST tests R8CBB_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2016
#
#  Author:
#
#    John Burkardt
#
  n1 = 8
  n2 = 2
  n = n1 + n2
  ml = 1
  mu = 1
  na = ( ml + mu + 1 ) * n1 + 2 * n1 * n2 + n2 * n2

  print ( '' )
  print ( 'R8CBB_ZEROS_TEST' )
  print ( '  R8CBB_ZEROS zeros an R8CBB matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Matrix suborder N1 = ', n1 )
  print ( '  Matrix suborder N2 = ', n2 )
  print ( '  Lower bandwidth ML = ', ml )
  print ( '  Upper bandwidth MU = ', mu )

  a = r8cbb_zeros ( n1, n2, ml, mu )

  r8cbb_print ( n1, n2, ml, mu, a, '  The R8CBB zero matrix:' )

  return

def r8ge_np_fa ( n, a ):

#*****************************************************************************80
#
## r8ge_np_fa() factors a R8GE matrix by nonpivoting Gaussian elimination.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_np_fa is a version of the LINPACK routine R8GEFA, but uses no
#    pivoting.  It will fail if the matrix is singular, or if any zero
#    pivot is encountered.
#
#    If r8ge_np_fa successfully factors the matrix, R8GE_NP_SL may be called
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
      print ( 'r8ge_np_fa(): Fatal error!' )
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
    print ( 'r8ge_np_fa(): Fatal error!' )
    print ( '  Zero pivot on step ', info )
    raise Exception ( 'r8ge_np_fa(): Fatal error!' )

  return a_lu, info

def r8ge_np_sl ( n, a_lu, b, job ):

#*****************************************************************************80
#
## r8ge_np_sl() solves a system factored by r8ge_np_fa().
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
#    real A_LU(N,N), the matrix as factored by r8ge_np_fa.
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
  r8cbb_test ( )
  timestamp ( )
