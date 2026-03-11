#! /usr/bin/env python3
#
def r8gd_test ( ):

#*****************************************************************************80
#
## r8gd_test() tests r8gd().
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
  print ( 'r8gd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8gd().' )

  r8gd_dif2_test ( )
  r8gd_indicator_test ( )
  r8gd_mtv_test ( )
  r8gd_mv_test ( )
  r8gd_print_test ( )
  r8gd_print_some_test ( )
  r8gd_random_test ( )
  r8gd_to_r8ge_test ( )
  r8gd_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8gd_test():' )
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

def r8gd_dif2 ( n, ndiag, offset ):

#*****************************************************************************80
#
## R8GD_DIF2 sets up an R8GD second difference matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.  
#    3 <= NDIAG.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal
#    storage.  The values -1, 0 and +1 should occur in OFFSET.
#
#  Output:
#
#    real A(N,NDIAG), the R8GD matrix.
#
  import numpy as np

  if ( ndiag < 3 ):
    print ( '' )
    print ( 'R8GD_DIF2 - Fatal error!' )
    print ( '  NDIAG must be at least 3.' )
    raise Exception ( 'R8GD_DIF2 - Fatal error!' )

  a = np.zeros ( [ n, ndiag ] )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        if ( offset[jdiag] == 0 ):
          a[i,jdiag] = 2.0
        elif ( offset[jdiag] == -1 or offset[jdiag] == +1 ):
          a[i,jdiag] = -1.0

  return a

def r8gd_dif2_test ( ):

#*****************************************************************************80
#
## R8GD_DIF2_TEST tests R8GD_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  ndiag = 3

  print ( '' )
  print ( 'R8GD_DIF2_TEST' )
  print ( '  R8GD_DIF2 sets up an R8GD second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -1, 0, 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_dif2 ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The R8GD second difference matrix:' )

  return

def r8gd_indicator ( n, ndiag, offset ):

#*****************************************************************************80
#
## R8GD_INDICATOR sets up a R8GD indicator matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
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
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#  Output:
#
#    real A(N,NDIAG), the R8GD matrix.
#
  import numpy as np

  a = np.zeros ( [ n, ndiag ] )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        a[i,jdiag] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8gd_indicator_test ( ):

#*****************************************************************************80
#
## R8GD_INDICATOR_TEST tests R8GD_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_INDICATOR_TEST' )
  print ( '  R8GD_INDICATOR sets up an R8GD indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_indicator ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The general diagonal matrix:' )

  return

def r8gd_mtv ( n, ndiag, offset, a, x ):

#*****************************************************************************80
#
## R8GD_MTV multiplies a vector by a R8GD matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
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
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8GD matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product X*A.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        b[j] = b[j] + x[i] * a[i,jdiag]

  return b

def r8gd_mtv_test ( ):

#*****************************************************************************80
#
## R8GD_MTV_TEST tests R8GD_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_MTV_TEST' )
  print ( '  R8GD_MTV computes A\'*x, where A is an R8GD matrix' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_random ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The general diagonal matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8gd_mtv ( n, ndiag, offset, a, x )

  r8vec_print ( n, b, '  A\' * x:' )

  return

def r8gd_mv ( n, ndiag, offset, a, x ):

#*****************************************************************************80
#
## R8GD_MV multiplies a R8GD matrix by a vector.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Example:
#
#    The "offset" value is printed near the first entry of each diagonal
#    in the original matrix, and above the columns in the new matrix.
#
#    Original matrix               New Matrix
#
#      0    1   2   3   4   5        -3  -2   0   1   3   5
#       \    \   \   \   \   \
#        11  12   0  14   0  16      --  --  11  12  14  16
#   -1 =  0  22  23   0  25   0      --  --  22  23  25  --
#   -2 = 31   0  33  34   0  36      --  31  33  34  36  --
#   -3 = 41  42   0  44  45   0      41  42  44  45  --  --
#   -4 =  0  52  53   0  55  56      52  53  55  56  --  --
#   -5 =  0   0  63  64  65  66      63  64  66  --  --  --
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
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
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8GD matrix.
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
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        b[i] = b[i] + a[i,jdiag] * x[j]

  return b

def r8gd_mv_test ( ):

#*****************************************************************************80
#
## R8GD_MV_TEST tests R8GD_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_MV_TEST' )
  print ( '  R8GD_MV computes A * x, where A is an R8GD matrix' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_random ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The general diagonal matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8gd_mv ( n, ndiag, offset, a, x )

  r8vec_print ( n, b, '  A * x:' )

  return

def r8gd_print ( n, ndiag, offset, a, title ):

#*****************************************************************************80
#
## R8GD_PRINT prints a R8GD matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8GD matrix.
#
#    string TITLE, a title to be printed.
#
  r8gd_print_some ( n, ndiag, offset, a, 0, 0, n - 1, n - 1, title )

  return

def r8gd_print_test ( ):

#*****************************************************************************80
#
## R8GD_PRINT_TEST tests R8GD_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_PRINT_TEST' )
  print ( '  R8GD_PRINT prints an R8GD matrix.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_random ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The R8GD matrix:' )

  return

def r8gd_print_some ( n, ndiag, offset, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8GD_PRINT_SOME prints some of a R8GD matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8GD matrix.
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

        aij = 0.0
        off = j - i
        for jdiag in range ( 0, ndiag ):
          if ( off == offset[jdiag] ):
            aij = a[i,jdiag]
            break

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8gd_print_some_test ( ):

#*****************************************************************************80
#
## R8GD_PRINT_SOME_TEST tests R8GD_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_PRINT_SOME_TEST' )
  print ( '  R8GD_PRINT_SOME prints some of an R8GD matrix.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_indicator ( n, ndiag, offset )

  r8gd_print_some ( n, ndiag, offset, a, 3, 3, 6, 6, '  Rows 3-6, Cols 3-6:' )

  return

def r8gd_random ( n, ndiag, offset ):

#*****************************************************************************80
#
## r8gd_random() randomizes a R8GD matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
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
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#  Output:
#
#    real A(N,NDIAG), the R8GD matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ n, ndiag ] )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        a[i,jdiag] = rng.random ( )

  return a

def r8gd_random_test ( ):

#*****************************************************************************80
#
## r8gd_random_test() tests r8gd_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_RANDOM_TEST' )
  print ( '  R8GD_RANDOM generates a random R8GD matrix.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_random ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The general diagonal matrix:' )

  return

def r8gd_to_r8ge ( n, ndiag, offset, a ):

#*****************************************************************************80
#
## R8GD_TO_R8GE copies a R8GD matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
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
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#    real A(N,NDIAG), the R8GD matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for jdiag in range ( 0, ndiag ):
      j = i + offset[jdiag]
      if ( 0 <= j and j < n ):
        b[i,j] = a[i,jdiag]

  return b

def r8gd_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8GD_TO_R8GE_TEST tests R8GD_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ndiag = 4

  print ( '' )
  print ( 'R8GD_TO_R8GE_TEST' )
  print ( '  R8GD_TO_R8GE converts an R8GD matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -2, 0, 1, n - 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_indicator ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The R8GD matrix:' )

  a_r8ge = r8gd_to_r8ge ( n, ndiag, offset, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8gd_zeros ( n, ndiag, offset ):

#*****************************************************************************80
#
## R8GD_ZEROS zeros an R8GD matrix.
#
#  Discussion:
#
#    The R8GD storage format is suitable for matrices whose only nonzero entries
#    occur along a few diagonals, but for which these diagonals are not all
#    close enough to the main diagonal for band storage to be efficient.
#
#    In that case, we assign the main diagonal the offset value 0.
#    Each successive superdiagonal gets an offset value 1 higher, until
#    the highest superdiagonal (the A(1,N) entry) is assigned the offset N-1.
#    Similarly, the subdiagonals are assigned offsets of -1 through -(N-1).
#
#    Now, assuming that only a few of these diagonals contain nonzeros,
#    then for the I-th diagonal to be saved, we stored its offset in
#    OFFSET(I), and its entries in column I of the matrix.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
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
#    integer NDIAG, the number of diagonals of the matrix
#    that are stored in the array.
#    NDIAG must be at least 1, and no more than 2 * N - 1.
#
#    integer OFFSET(NDIAG), the offsets for the diagonal storage.
#
#  Output:
#
#    real A(N,NDIAG), the R8GD matrix.
#
  import numpy as np

  a = np.zeros ( [ n, ndiag ] )

  return a

def r8gd_zeros_test ( ):

#*****************************************************************************80
#
## R8GD_ZEROS_TEST tests R8GD_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  ndiag = 3

  print ( '' )
  print ( 'R8GD_ZEROS_TEST' )
  print ( '  R8GD_ZEROS zeros an R8GD matrix.' )
  print ( '' )
  print ( '  Matrix order N            = ', n )
  print ( '  Number of diagonals NDIAG = ', ndiag )
#
#  Set the matrix.
#
  offset = np.array ( [ -1, 0, 1 ] )

  print ( '' )
  print ( '  The offset vector:' )
  print ( offset )

  a = r8gd_zeros ( n, ndiag, offset )

  r8gd_print ( n, ndiag, offset, a, '  The zero R8GD matrix:' )

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
  r8gd_test ( )
  timestamp ( )
 
