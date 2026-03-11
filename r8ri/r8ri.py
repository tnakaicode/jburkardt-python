#! /usr/bin/env python3
#
def r8ri_test ( ):

#*****************************************************************************80
#
## r8ri_test() tests r8ri().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ri_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ri().' )

  r8ri_dif2_test ( )
  r8ri_indicator_test ( )
  r8ri_mtv_test ( )
  r8ri_mv_test ( )
  r8ri_print_test ( )
  r8ri_print_some_test ( )
  r8ri_random_test ( )
  r8ri_to_r8ge_test ( )
  r8ri_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8ri_test():' )
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

def r8ri_dif2 ( n ):

#*****************************************************************************80
#
## R8RI_DIF2 stores the second difference matrix in R8RI format.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.  NZ = 3*N-1.
#
#  Output:
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
  import numpy as np

  nz = 3 * n - 1
  ija = np.zeros ( nz, dtype = np.int32 )
  a = np.zeros ( nz )
#
#  Diagonal elements of A.
#
  a[0:n] = 2.0
#
#  First N entries of IJA store first offdiagonal of each row.
#
  k = n + 1

  for i in range ( 0, n ):
    ija[i] = k
    if ( i == 0 or i == n - 1 ):
      k = k + 1
    else:
      k = k + 2
#
#  IJA(N+1) stores one beyond last element of A.
#
  ija[n] = k
  a[n] = 0.0
#
#  IJA(N+2), A(N+2) and beyond store column and value.
#
  k = n

  for i in range ( 0, n ):

    if ( i == 0 ):
      k = k + 1
      ija[k] = i + 1
      a[k] = - 1.0
    elif ( i < n - 1 ):
      k = k + 1
      ija[k] = i - 1
      a[k] = - 1.0
      k = k + 1
      ija[k] = i + 1
      a[k] = - 1.0
    elif ( i == n - 1 ):
      k = k + 1
      ija[k] = i - 1
      a[k] = - 1.0

  return nz, ija, a

def r8ri_dif2_test ( ):

#*****************************************************************************80
#
## R8RI_DIF2_TEST tests R8RI_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8RI_DIF2_TEST' )
  print ( '  R8RI_DIF2 sets up an R8RI indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  nz, ija, a = r8ri_dif2 ( n )

  r8ri_print ( n, nz, ija, a, '  The R8RI second difference matrix:' )

  return

def r8ri_indicator ( n, nz, ija ):

#*****************************************************************************80
#
## R8RI_INDICATOR returns the R8RI indicator matrix for given sparsity.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.  NZ = 3*N-1.
#
#    integer IJA(NZ), the index vector.
#
#  Output:
#
#    real A(NZ), the value vector.
#
  import numpy as np

  a = np.zeros ( nz )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )
#
#  Diagonal elements of A.
#
  for i in range ( 0, n ):
    a[i] = float ( fac * ( i + 1 ) + ( i + 1 ) )

  for i in range ( 0, n ):
    for k in range ( ija[i], ija[i+1] ):
      j = ija[k]
      a[k] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8ri_indicator_test ( ):

#*****************************************************************************80
#
## R8RI_INDICATOR_TEST tests R8RI_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 11

  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_INDICATOR_TEST' )
  print ( '  R8RI_INDICATOR returns an R8RI indicator matrix' )
  print ( '  for a given sparsity pattern.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  a = r8ri_indicator ( n, nz, ija )

  r8ri_print ( n, nz, ija, a, '  The R8RI matrix:' )

  return

def r8ri_mtv ( n, nz, ija, a, x ):

#*****************************************************************************80
#
## R8RI_MTV multiplies the transpose of an R8RI matrix times a vector.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
#    real X(N), the vector to be multiplied.
#
#  Output:
#
#    real B(N), the product A'*X.
#
  import numpy as np

  if ( ija[0] != n + 1 ):
    print ( '' )
    print ( 'R8RI_MTV - Fatal error!' )
    print ( '  The values IJA(1) and N are inconsistent.' )
    raise Exception ( 'R8RI_MTV - Fatal error!' )

  b = np.zeros ( n )

  b[0:n] = a[0:n] * x[0:n]

  for i in range ( 0, n ):
    for k in range ( ija[i], ija[i+1] ):
      j = ija[k]
      b[j] = b[j] + a[k] * x[i]

  return b

def r8ri_mtv_test ( ):

#*****************************************************************************80
#
## R8RI_MTV_TEST tests R8RI_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 11

  a = np.array ( [ \
    3.0, 4.0, 5.0, 0.0, 8.0, \
    0.0, 1.0, 7.0, 9.0, 2.0, \
    6.0 ] )

  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_MTV_TEST' )
  print ( '  R8RI_MTV computes b=A\'*x, where A is an R8RI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  r8ri_print ( n, nz, ija, a, '  The R8RI matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8ri_mtv ( n, nz, ija, a, x )

  r8vec_print ( n, b, '  The product b=A\'*x' )

  return

def r8ri_mv ( n, nz, ija, a, x ):

#*****************************************************************************80
#
## R8RI_MV multiplies an R8RI matrix times a vector.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
#    real X(N), the vector to be multiplied.
#
#  Output:
#
#    real B(N), the product A*X.
#
  import numpy as np

  if ( ija[0] != n + 1 ):
    print ( '' )
    print ( 'R8RI_MV - Fatal error!' )
    print ( '  The values IJA[0] and N are inconsistent.' )
    raise Exception ( 'R8RI_MV - Fatal error!' )

  b = np.zeros ( n )

  b[0:n] = a[0:n] * x[0:n]

  for i in range ( 0, n ):
    for k in range (  ija[i], ija[i+1] ):
      b[i] = b[i] + a[k] * x[ija[k]]

  return b

def r8ri_mv_test ( ):

#*****************************************************************************80
#
## R8RI_MV_TEST tests R8RI_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 11

  a = np.array ( [ \
    3.0, 4.0, 5.0, 0.0, 8.0, \
    0.0, 1.0, 7.0, 9.0, 2.0, \
    6.0 ] )

  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_MV_TEST' )
  print ( '  R8RI_MV computes b=A*x, where A is an R8RI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  r8ri_print ( n, nz, ija, a, '  The R8RI matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r8ri_mv ( n, nz, ija, a, x )

  r8vec_print ( n, b, '  The product b=A*x' )

  return

def r8ri_print ( n, nz, ija, a, title ):

#*****************************************************************************80
#
## R8RI_PRINT prints an R8RI matrix.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
#    string TITLE, a title.
#
  r8ri_print_some ( n, nz, ija, a, 0, 0, n - 1, n - 1, title )

  return

def r8ri_print_test ( ):

#*****************************************************************************80
#
## R8RI_PRINT_TEST tests R8RI_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 1
  a = np.array ( [ \
    3.0, 4.0, 5.0, 0.0, 8.0, \
    0.0, 1.0, 7.0, 9.0, 2.0, \
    6.0 ] )

  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_PRINT_TEST' )
  print ( '  R8RI_PRINT prints an R8RI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  r8ri_print ( n, nz, ija, a, '  The R8RI matrix:' )

  return

def r8ri_print_some ( n, nz, ija, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8RI_PRINT_SOME prints some of an R8RI matrix.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  import numpy as np

  aij = np.zeros ( n )

  incx = 5

  print ( '' )
  print ( title )
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
#
#  Print out (up to) 5 entries in row I, J2LO <= J <= J2HI.
#
#  1) Assume everything is zero.
#
      aij[j2lo:j2hi+1] = 0.0
#
#  2) Diagonal entry.
#
      if ( j2lo <= i and i <= j2hi ):
        aij[i] = a[i]
#
#  3) Now examine all the offdiagonal entries.
#
      for k in range ( ija[i], ija[i+1] ):
        j = ija[k]
        if ( j2lo <= j and j <= j2hi ):
          aij[j] = a[k]
      print ( '%5d  ' % ( i ), end = '' )

      for j in range ( j2lo, j2hi + 1 ):
        print ( '%14.6g' % ( aij[j] ), end = '' )
      print ( '' )

  return

def r8ri_print_some_test ( ):

#*****************************************************************************80
#
## R8RI_PRINT_SOME_TEST tests R8RI_PRINT_SOME.
#
#  Discussion:
#
#    The matrix is related to the discrete 2D Laplacian on a 3x3 grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9
  nz = 34

  a = np.array ( [ \
    4.0,  4.0,  4.0,  4.0,  4.0, \
    4.0,  4.0,  4.0,  4.0,  0.0, \
   -1.0, -1.0, -1.0, -1.0, -1.0, \
   -1.0, -1.0, -1.0, -1.0, -1.0, \
   -1.0, -1.0, -1.0, -1.0, -1.0, \
   -1.0, -1.0, -1.0, -1.0, -1.0, \
   -1.0, -1.0, -1.0, -1.0 ] )

  ija = np.array ( [ \
     10, 12, 15, 17, 20, \
     24, 27, 29, 32, 34, \
      1,  3,  0,  2,  4, \
      1,  5,  0,  4,  6, \
      1,  3,  5,  7,  2, \
      4,  8,  3,  7,  4, \
      6,  8,  5,  7 ] )

  print ( '' )
  print ( 'R8RI_PRINT_SOME_TEST' )
  print ( '  R8RI_PRINT_SOME prints some of an R8RI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  r8ri_print_some ( n, nz, ija, a, 0, 3, 8, 5, '  Rows 0-8, Cols 3-5:' )

  return

def r8ri_random ( n, nz, ija ):

#*****************************************************************************80
#
## R8RI_RANDOM randomizes an R8RI matrix for given sparsity.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form, using an index
#    array IJA and a value array A.  The first N entries of A store the
#    diagonal elements in order.  The first N entries of IJA store the index
#    of the first off-diagonal element of the corresponding row if there is
#    no off-diagonal element in that row, it is one greater than the index
#    in A of the most recently stored element in the previous row.
#    Location 1 of IJA is always equal to N+2 location N+1 of IJA is one
#    greater than the index in A of the last off-diagonal element of the
#    last row.  Location N+1 of A is not used.  Entries in A with index
#    N+2 or greater contain the off-diagonal values, ordered by row, and
#    then by column.  Entries in IJA with index N+2 or greater contain the
#    column number of the corresponding element in A.
#
#  Example:
#
#    A:
#      3 0 1 0 0
#      0 4 0 0 0
#      0 7 5 9 0
#      0 0 0 0 2
#      0 0 0 6 8
#
#    NZ = 11
#
#    IJA:
#      7  8  8 10 11 12  3  2  4  5  4
#
#    A:
#      3  4  5  0  8  *  1  7  9  2  6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.  NZ = 3*N-1.
#
#    integer IJA(NZ), the index vector.
#
#  Output:
#
#    real A(NZ), the value vector.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
#
#  Diagonal elements of A.
#
  a = np.zeros ( nz )

  for i in range ( 0, n ):
    a[i] = rng.random ( )

  for i in range ( 0, n ):
    for k in range ( ija[i], ija[i+1] ):
      j = ija[k]
      a[k] = rng.random ( )

  return a

def r8ri_random_test ( ):

#*****************************************************************************80
#
## R8RI_RANDOM_TEST tests R8RI_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 11

  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_RANDOM_TEST' )
  print ( '  R8RI_RANDOM randomizes an R8RI matrix' )
  print ( '  for a given sparsity pattern.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  a = r8ri_random ( n, nz, ija )

  r8ri_print ( n, nz, ija, a, '  The R8RI matrix:' )

  return

def r8ri_to_r8ge ( n, nz, ija, a ):

#*****************************************************************************80
#
## R8RI_TO_R8GE converts an R8RI matrix to R8GE form.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form.
#
#    A R8GE matrix is in general storage.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
#  Output:
#
#    real A_R8GE(N,N), the matrix stored in GE 
#    or "general" format.
#
  import numpy as np

  a_r8ge = np.zeros ( [ n, n ] )

  for k in range ( 0, n ):
    i = k
    j = k
    a_r8ge[i,j] = a[k]

  for i in range ( 0, n ):
    for k in range ( ija[i], ija[i+1] ):
      j = ija[k]
      a_r8ge[i,j] = a[k]

  return a_r8ge

def r8ri_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8RI_TO_R8GE_TEST tests R8RI_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 11
  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_TO_R8GE_TEST' )
  print ( '  R8RI_TO_R8GE converts an R8RI matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  a = r8ri_indicator ( n, nz, ija )

  r8ri_print ( n, nz, ija, a, '  The R8RI matrix:' )

  a_r8ge = r8ri_to_r8ge ( n, nz, ija, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8ri_zeros ( n, nz, ija ):

#*****************************************************************************80
#
## R8RI_ZEROS zeros an R8RI matrix.
#
#  Discussion:
#
#    An R8RI matrix is in row indexed sparse storage form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Press, Brian Flannery, Saul Teukolsky, William Vetterling,
#    Numerical Recipes in FORTRAN: The Art of Scientific Computing,
#    Third Edition,
#    Cambridge University Press, 2007,
#    ISBN13: 978-0-521-88068-8,
#    LC: QA297.N866.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the size required for the RI
#    or "row indexed" sparse storage.
#
#    integer IJA(NZ), the index vector.
#
#    real A(NZ), the value vector.
#
  import numpy as np

  a = np.zeros ( nz )

  return a

def r8ri_zeros_test ( ):

#*****************************************************************************80
#
## R8RI_ZEROS_TEST tests R8RI_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 11
  ija = np.array ( [ \
     6,  7,  7,  9, 10, \
    11,  2,  1,  3,  4, \
     3 ] )

  print ( '' )
  print ( 'R8RI_ZEROS_TEST' )
  print ( '  R8RI_ZEROS zeros an R8RI indicator matrix' )
  print ( '  for a given sparsity pattern.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Storage NZ =     ', nz )

  a = r8ri_zeros ( n, nz, ija )

  r8ri_print ( n, nz, ija, a, '  The zero R8RI matrix:' )

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
  r8ri_test ( )
  timestamp ( )

