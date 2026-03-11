#! /usr/bin/env python3
#
def r8bto_test ( ):

#*****************************************************************************80
#
## r8bto_test() tests r8bto().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8bto_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8bto().' )

  r8bto_dif2_test ( )
  r8bto_indicator_test ( )
  r8bto_mtv_test ( )
  r8bto_mv_test ( )
  r8bto_print_test ( )
  r8bto_print_some_test ( )
  r8bto_random_test ( )
  r8bto_to_r8ge_test ( )
  r8bto_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8bto_test():' )
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

def r8bto_dif2 ( m, l ):

#*****************************************************************************80
#
## R8BTO_DIF2 sets up an R8BTO second difference matrix.
#
#  Discussion:
#
#    To get the second difference matrix, it is assumed that M is 1%
#
#    The "indicator matrix" simply has a value like I*10+J at every
#    entry of a dense matrix, or at every entry of a compressed storage
#    matrix for which storage is allocated. 
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Example:
#
#    M = 2, L = 3
#
#    1 2 | 3 4 | 5 6
#    5 5 | 6 6 | 7 7
#    ----+-----+-----
#    7 8 | 1 2 | 3 4
#    8 8 | 5 5 | 6 6
#    ----+-----+-----
#    9 0 | 7 8 | 1 2
#    9 9 | 8 8 | 5 5
#
#    X = (/ 1, 2, 3, 4, 5, 6 /)
#
#    B = (/ 91, 134, 73, 125, 97, 129 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#    For the second different matrix, M should be 1.
#
#    integer L, the number of blocks in a row or column.
#
#  Output:
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
  import numpy as np

  a = np.zeros ( [ m, m, 2 * l - 1 ] )
#
#  Blocks 1 to L form the first row.
#
  j = 0

  for k in range ( 0, l ):

    if ( k == 0 ):
      value = 2.0
    elif ( k == 1 ):
      value = -1.0
    else:
      value = 0.0

    for j2 in range ( 0, m ):
      for i in range ( 0, m ):
        a[i,j2,k] = value
#
#  Blocks L+1 through 2*L-1 form the remainder of the first column.
#
  i = m

  for k in range ( l, 2 * l - 1 ):

    if ( k == l ):
      value = -1.0
    else:
      value = 0.0

    for i2 in range ( 0, m ):
      for j in range ( 0, m ):
        a[i2,j,k] = value

  return a

def r8bto_dif2_test ( ):

#*****************************************************************************80
#
## R8BTO_DIF2_TEST tests R8BTO_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 5
  m = 1

  print ( '' )
  print ( 'R8BTO_DIF2_TEST' )
  print ( '  R8BTO_DIF2 sets up an R8BTO version of' )
  print ( '  the second difference matrix (assuming M = 1 ).' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', m * l )

  a = r8bto_dif2 ( m, l )

  r8bto_print ( m, l, a, '  The R8BTO second difference matrix:' )

  return

def r8bto_indicator ( m, l ):

#*****************************************************************************80
#
## r8bto_indicator() sets up a R8BTO indicator matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Example:
#
#    M = 2, L = 3
#
#    1 2 | 3 4 | 5 6
#    5 5 | 6 6 | 7 7
#    ----+-----+-----
#    7 8 | 1 2 | 3 4
#    8 8 | 5 5 | 6 6
#    ----+-----+-----
#    9 0 | 7 8 | 1 2
#    9 9 | 8 8 | 5 5
#
#    X = (/ 1, 2, 3, 4, 5, 6 /)
#
#    B = (/ 91, 134, 73, 125, 97, 129 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#  Output:
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
  import numpy as np

  a = np.zeros ( [ m, m, 2 * l - 1 ] )

  fac = 10 ** ( i4_log_10 ( m * l ) + 1 )
#
#  Blocks 1 to L form the first row.
#
  j = 0

  for k in range ( 0, l ):

    for j2 in range ( 0, m ):
      j = j + 1
      for i in range ( 0, m ):
        a[i,j2,k] = float ( fac * ( i + 1 ) + j )
#
#  Blocks L+1 through 2*L-1 form the remainder of the first column.
#
  i = m

  for k in range ( l, 2 * l - 1 ):

    for i2 in range ( 0, m ):
      i = i + 1
      for j in range ( 0, m ):
        a[i2,j,k] = float ( fac * ( i + 1 ) + j )

  return a

def r8bto_indicator_test ( ):

#*****************************************************************************80
#
## R8BTO_INDICATOR_TEST tests R8BTO_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 3
  m = 2

  print ( '' )
  print ( 'R8BTO_INDICATOR_TEST' )
  print ( '  R8BTO_INDICATOR sets up an R8BTO indicator matrix' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', m * l )

  a = r8bto_indicator ( m, l )

  r8bto_print ( m, l, a, '  The block Toeplitz matrix:' )

  return

def r8bto_mtv ( m, l, a, x ):

#*****************************************************************************80
#
## R8BTO_MTV multiplies a vector by a R8BTO matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Example:
#
#    M = 2, L = 3
#
#    1 2 | 3 4 | 5 6
#    5 5 | 6 6 | 7 7
#    ----+-----+-----
#    7 8 | 1 2 | 3 4
#    8 8 | 5 5 | 6 6
#    ----+-----+-----
#    9 0 | 7 8 | 1 2
#    9 9 | 8 8 | 5 5
#
#    X = (/ 1, 2, 3, 4, 5, 6 /)
#
#    B = (/ 163, 122, 121, 130, 87, 96 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
#    real X(M*L), the vector to be multiplied.
#
#  Output:
#
#    real B(M*L), the product X * A.
#
  import numpy as np

  b = np.zeros ( [ m, l ] )
#
#  Construct the right hand side by blocks.
#
  for i in range ( 0, l ):

    for j in range ( 0, i + 1 ):
      for i2 in range ( 0, m ):
        t = 0.0
        for j2 in range ( 0, m ):
          t = t + a[i2,j2,i-j] * x[j2,j]
        b[i2,i] = b[i2,i] + t

    for j in range ( i + 1, l ):
      for i2 in range ( 0, m ):
        t = 0.0
        for j2 in range ( 0, m ):
          t = t + a[i2,j2,l-1+j-i] * x[j2,j]
        b[i2,i] = b[i2,i] + t

  return b

def r8bto_mtv_test ( ):

#*****************************************************************************80
#
## R8BTO_MTV_TEST tests R8BTO_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  l = 3
  m = 2
  n = m * l
  
  a = np.array \
  (\
    [\
      [\
        [ 1, 3, 5, 7, 9 ],\
        [ 2, 4, 6, 8, 0 ]\
      ],\
      [\
        [ 5, 6, 7, 8, 9 ],\
        [ 5, 6, 7, 8, 9 ]\
      ]
    ]\
  )

  print ( '' )
  print ( 'R8BTO_MTV_TEST' )
  print ( '  R8BTO_MTV computes A\'* x for an R8BTO matrix.' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', n )

  r8bto_print ( m, l, a, '  The block Toeplitz matrix:' )

  x = np.zeros ( [ m, n ] )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      x[i,j] = fac * ( i + 1 ) +  ( j + 1 )
   
  print ( '' )
  print ( '  The matrix x:' )
  print ( x )

  b = r8bto_mtv ( m, l, a, x )

  print ( '' )
  print ( '  The product A\'*x:' )
  print ( b )

  return

def r8bto_mv ( m, l, a, x ):

#*****************************************************************************80
#
## R8BTO_MV multiplies a R8BTO matrix times a vector.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Example:
#
#    M = 2, L = 3
#
#    1 2 | 3 4 | 5 6
#    5 5 | 6 6 | 7 7
#    ----+-----+-----
#    7 8 | 1 2 | 3 4
#    8 8 | 5 5 | 6 6
#    ----+-----+-----
#    9 0 | 7 8 | 1 2
#    9 9 | 8 8 | 5 5
#
#    X = (/ 1, 2, 3, 4, 5, 6 /)
#
#    B = (/ 91, 134, 73, 125, 79, 138 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
#    real X(M,L), the vector to be multiplied.
#
#  Output:
#
#    real B(M,L), the product A * X.
#
  import numpy as np

  b = np.zeros ( [ m, l ] )
#
#  Construct the right hand side by blocks.
#
  for i in range ( 0, l ):

    for j in range ( 0, i ):
      for i2 in range ( 0, m ):
        t = 0.0
        for j2 in range ( 0, m ):
          t = t + a[i2,j2,l-1+i-j] * x[j2,j]
        b[i2,i] = b[i2,i] + t

    for j in range ( i, l ):
      for i2 in range ( 0, m ):
        t = 0.0
        for j2 in range ( 0, m ):
          t = t + a[i2,j2,j-i] * x[j2,j]
        b[i2,i] = b[i2,i] + t

  return b

def r8bto_mv_test ( ):

#*****************************************************************************80
#
## R8BTO_MV_TEST tests R8BTO_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  l = 3
  m = 2
  n = m * l

  a = np.array \
  (\
    [\
      [\
        [ 1, 3, 5, 7, 9 ],\
        [ 2, 4, 6, 8, 0 ]\
      ],\
      [\
        [ 5, 6, 7, 8, 9 ],\
        [ 5, 6, 7, 8, 9 ]\
      ]
    ]\
  )
  
  print ( '' )
  print ( 'R8BTO_MV_TEST' )
  print ( '  R8BTO_MV computes A * x.' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', n )

  r8bto_print ( m, l, a, '  The block Toeplitz matrix:' )

  x = np.zeros ( [ m, n ] )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      x[i,j] = fac * ( i + 1 ) +  ( j + 1 )
   
  print ( '' )
  print ( '  The matrix x:' )
  print ( x )

  b = r8bto_mtv ( m, l, a, x )

  print ( '' )
  print ( '  The product A*x:' )
  print ( b )

  return

def r8bto_print ( m, l, a, title ):

#*****************************************************************************80
#
## R8BTO_PRINT prints a R8BTO matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
#    string TITLE, a title to be printed.
#
  r8bto_print_some ( m, l, a, 0, 0, m * l - 1, m * l - 1, title )

  return

def r8bto_print_test ( ):

#*****************************************************************************80
#
## R8BTO_PRINT_TEST tests R8BTO_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 3
  m = 2

  print ( '' )
  print ( 'R8BTO_PRINT_TEST' )
  print ( '  R8BTO_PRINT prints an R8BTO matrix' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', m * l )

  a = r8bto_indicator ( m, l )

  r8bto_print ( m, l, a, '  The R8BTO matrix:' )

  return

def r8bto_print_some ( m, l, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8BTO_PRINT_SOME prints some of a R8BTO matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  n = m * l

  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or l <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return
#
#  Print the columns of the matrix, in strips of 5.
#
  for j3lo in range ( jlo, jhi + 1, incx ):

    j3hi = j3lo + incx - 1
    j3hi = min ( j3hi, n - 1 )
    j3hi = min ( j3hi, jhi )

    inc = j3hi + 1 - j3lo

    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j3lo, j3hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i3lo = max ( ilo, 0 )
    i3hi = min ( ihi, n - 1 )

    for i in range ( i3lo, i3hi + 1 ):

      print ( '%4d :' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j3 in range ( 0, inc ):

        j = j3lo + j3
#
#  i = M * ( i1 - 1 ) + i2
#  j = M * ( j1 - 1 ) + j2
#
        i1 = int ( i / m )
        i2 = i - m * i1
        j1 = int ( j / m )
        j2 = j - m * j1

        if ( i1 <= j1 ):
          aij = a[i2,j2,j1-i1]
        else:
          aij = a[i2,j2,l-1+i1-j1]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8bto_print_some_test ( ):

#*****************************************************************************80
#
## R8BTO_PRINT_SOME_TEST tests R8BTO_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 3
  m = 2

  print ( '' )
  print ( 'R8BTO_PRINT_SOME_TEST' )
  print ( '  R8BTO_PRINT_SOME prints some of an R8BTO matrix' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', m * l )

  a = r8bto_indicator ( m, l )

  r8bto_print_some ( m, l, a, 1, 3, 6, 4, '  Row (1:6), Cols (3:4):' )

  return

def r8bto_random ( m, l ):

#*****************************************************************************80
#
## R8BTO_RANDOM randomizes a R8BTO matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#  Output:
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ m, m, 2 * l - 1 ] )

  for i in range ( 0, m ):
    for j in range ( 0, m ):
      for k in range ( 2 * l - 1 ):
        a[i,j,k] = rng.random ( )

  return a

def r8bto_random_test ( ):

#*****************************************************************************80
#
## r8bto_random_test() tests r8bto_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 3
  m = 2

  print ( '' )
  print ( 'R8BTO_RANDOM_TEST' )
  print ( '  R8BTO_RANDOM returns a random R8BTO matrix' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', m * l )

  a = r8bto_random ( m, l )

  r8bto_print ( m, l, a, '  The random RBTO matrix:' )

  return

def r8bto_to_r8ge ( m, l, a ):

#*****************************************************************************80
#
## R8BTO_TO_R8GE copies a R8BTO matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the R8BTO matrix.
#
#    integer L, the number of blocks in a row or column of the
#    R8BTO matrix.
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  n = m * l
  b = np.zeros ( [ n, n ] )

  for i in range ( 1, n + 1 ):

    i1 = ( i - 1 ) // m + 1
    i2 = i - m * ( i1 - 1 )

    for j in range ( 1, n + 1 ):

      j1 = ( j - 1 ) // m + 1
      j2 = j - m * ( j1 - 1 )

      if ( i1 <= j1 ):
        b[i-1,j-1] = a[i2-1,j2-1,j1+1-i1-1]
      else:
        b[i-1,j-1] = a[i2-1,j2-1,l+i1-j1-1]

  return b

def r8bto_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8BTO_TO_R8GE_TEST tests R8BTO_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 3
  m = 2
  n = m * l

  print ( '' )
  print ( 'R8BTO_TO_R8GE_TEST' )
  print ( '  R8BTO_TO_R8GE converts an R8BTO matrix to R8GE format' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', n )

  a = r8bto_indicator ( m, l )

  r8bto_print ( m, l, a, '  The R8BTO matrix:' )

  a_r8ge = r8bto_to_r8ge ( m, l, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8bto_zeros ( m, l ):

#*****************************************************************************80
#
## R8BTO_ZEROS zeros an R8BTO matrix.
#
#  Discussion:
#
#    The R8BTO storage format is for a block Toeplitz matrix. The matrix
#    can be regarded as an L by L array of blocks, each of size M by M.
#    The full matrix has order N = M * L.  The L by L matrix is Toeplitz,
#    that is, along its diagonal, the blocks repeat.
#
#    Storage for the matrix consists of the L blocks of the first row,
#    followed by the L-1 blocks of the first column (skipping the first row).
#    These items are stored in the natural way in an (M,M,2*L-1) array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the blocks of the matrix A.
#
#    integer L, the number of blocks in a row or column of A.
#
#  Output:
#
#    real A(M,M,2*L-1), the R8BTO matrix.
#
  import numpy as np

  a = np.zeros ( [ m, m, 2 * l - 1 ] )

  return a

def r8bto_zeros_test ( ):

#*****************************************************************************80
#
## R8BTO_ZEROS_TEST tests R8BTO_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2016
#
#  Author:
#
#    John Burkardt
#
  l = 2
  m = 3

  print ( '' )
  print ( 'R8BTO_ZEROS_TEST' )
  print ( '  R8BTO_ZEROS zeros an R8BTO matrix.' )
  print ( '' )
  print ( '  Block order M =  ', m )
  print ( '  Block number L = ', l )
  print ( '  Matrix order N = ', m * l )

  a = r8bto_zeros ( m, l )

  r8bto_print ( m, l, a, '  The zero R8BTO matrix:' )

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
  r8bto_test ( )
  timestamp ( )

