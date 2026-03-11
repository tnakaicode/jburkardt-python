#! /usr/bin/env python3
#
def r8ccs_test ( ):

#*****************************************************************************80
#
## r8ccs_test() tests r8ccs().
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 February 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ccs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ccs().' )

  rng = default_rng ( )

  r8ccs_dif2_test ( )
  r8ccs_get_test ( rng )
  r8ccs_ijk_test ( rng )
  r8ccs_inc_test ( rng )
  r8ccs_indicator_test ( )
  r8ccs_kij_test ( rng )
  r8ccs_mtv_test ( rng )
  r8ccs_mv_test ( rng )
  r8ccs_print_test ( rng )
  r8ccs_print_some_test ( )
  r8ccs_random_test ( rng )
  r8ccs_read_test ( )
  r8ccs_set_test ( rng )
  r8ccs_to_r8ge_test ( )
  r8ccs_write_test ( )
  r8ccs_zeros_test ( )
  r8ge_to_r8ccs_test ( )

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
#    I4_LOG_10 ( I ) + 1 is the number of decimal digits in I.
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

def i4vec_search_binary_a ( n, a, b ):

#*****************************************************************************80
#
## i4vec_search_binary_a() searches an ascending sorted I4VEC.
#
#  Discussion:
#
#    Binary search is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 26.
#
#  Input:
#
#    integer N, the number of elements in the vector.
#
#    integer A(N), the array to be searched.  A must
#    be sorted in ascending order.
#
#    integer B, the value to be searched for.
#
#  Output:
#
#    integer INDX, the result of the search.
#    -1, B does not occur in A.
#    I, A(I) = B.
#
  indx = - 1

  low = 0
  high = n - 1

  while ( low <= high ):

    mid = ( ( low + high ) // 2 )

    if ( a[mid] == b ):
      indx = mid
      break
    elif ( a[mid] < b ):
      low = mid + 1
    elif ( b < a[mid] ):
      high = mid - 1

  return indx

def r8ccs_dif2 ( m, n, nz_num ):

#*****************************************************************************80
#
## r8ccs_dif2() sets the second difference as a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#  Output:
#
#    integer COLPTR(N+1), indicate where each column's data begins.
#
#    integer ROW(NZ_NUM), the row indices.
#
#    real A(NZ_NUM), the nonzero entries.
#
  import numpy as np
#
#  Column pointers
#
  colptr = np.zeros ( n + 1, dtype = np.int32 )

  colptr[0] = 0
  colptr[1] = 2
  for j in range ( 2, n ):
    colptr[j] = colptr[j-1] + 3
  colptr[n] = colptr[n-1] + 2
#
#  Row indices
#
  rowind = np.zeros ( nz_num, dtype = np.int32 )

  k = 0
  rowind[k] = 0
  k = k + 1
  rowind[k] = 1
  k = k + 1
  for j in range ( 1, n - 1 ):
    for i in range ( j - 1, j + 2 ):
      rowind[k] = i
      k = k + 1

  rowind[k] = m - 2
  k = k + 1
  rowind[k] = m - 1
  k = k + 1
#
#  Values
#
  a = np.zeros ( nz_num, dtype = np.float64 )

  k = 0

  j = 0
  i = 0
  a[k] = 2.0
  k = k + 1
  i = 1
  a[k] = -1.0
  k = k + 1

  for j in range ( 1, n - 1 ):
    i = j - 1
    a[k] = -1.0
    k = k + 1
    i = j
    a[k] =  2.0
    k = k + 1
    i = j + 1
    a[k] = -1.0
    k = k + 1

  j = n - 1
  i = m - 2
  a[k] = -1.0
  k = k + 1
  i = m - 1
  a[k] = 2.0
  k = k + 1

  return colptr, rowind, a

def r8ccs_dif2_test ( ):

#*****************************************************************************80
#
## r8ccs_dif2_test() tests r8ccs_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ccs_dif2_test():' )
  print ( '  r8ccs_dif2() returns the second difference as a CCS matrix.' )

  m = 5
  n = 5
  nz_num = 13
#
#  Set the matrix.
#
  colptr, rowind, a = r8ccs_dif2 ( m, n, nz_num )
#
#  Print the matrix.
#
  title = 'The second difference matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  return

def r8ccs_get ( m, n, nz_num, colptr, rowind, a, i, j ):

#*****************************************************************************80
#
## r8ccs_get() gets a value of a CCS matrix.
#
#  Discussion:
#
#    It is legal to request entries of the matrix for which no storage
#    was set aside.  In that case, a zero value will be returned.
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer COLPTR(N+1), indicate where each column's data begins.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    real A(NZ_NUM), the nonzero entries.
#
#    integer I, J, the indices of the value to retrieve.
#
#  Output:
#
#    real AIJ, the value of A(I,J).
#

#
#  Seek sparse index K corresponding to full index (I,J).
#
  k = r8ccs_ijk ( m, n, nz_num, colptr, rowind, i, j )
#
#  If no K was found, then be merciful, and simply return 0.
#
  if ( k == -1 ):
    aij = 0.0
  else:
    aij = a[k]

  return aij

def r8ccs_get_test ( rng ):

#*****************************************************************************80
#
## r8ccs_get_test() tests r8ccs_get().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = np.int32 )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ], dtype = np.int32 )

  print ( '' )
  print ( 'r8ccs_get_test():' )
  print ( '  r8ccs_get() gets an entry of a matrix in the CCS format.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  print ( '' )
  print ( '  r8ccs_get() retrieves 10 entries.' )
  print ( '' )
  print ( '         I         J         K      VALUE' )
  print ( '' )

  for test in range ( 0, 10 ):
    k = rng.integers ( low = 0, high = nz_num, endpoint = False )
    i, j = r8ccs_kij ( m, n, nz_num, colptr, rowind, k )
    value = r8ccs_get ( m, n, nz_num, colptr, rowind, a, i, j )
    print ( '  %8d  %8d  %8d  %14.6g' % ( i, j, k, value ) )

  return

def r8ccs_ijk ( m, n, nz_num, colptr, rowind, i, j ):

#*****************************************************************************80
#
## r8ccs_ijk() seeks K, the sparse index of (I,J), the full index of a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer COLPTR(N+1), indicate where each column's data begins.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    integer I, J, the indices of the value to retrieve.
#
#  Output:
#
#    integer K, the index of the sparse matrix in which entry
#    (I,J) is stored, or -1 if no such entry exists.
#
  import numpy as np
#
#  Determine the part of ROW containing row indices of entries in column J.
#
  k1 = colptr[j]
  k2 = colptr[j+1] - 1

  print ( k1 )
  print ( k2 )
#
#  Seek the location K for which ROWIND(K) = I.
#
  rowsub = np.zeros ( k2 + 1 - k1 )
  for i2 in range ( 0, k2 + 1 - k1 ):
    rowsub[i2] = rowind[k1+i2]
  k = i4vec_search_binary_a ( k2+1-k1, rowsub, i )

  if ( k != -1 ):
    k = k + k1

  return k

def r8ccs_ijk_test ( rng ):

#*****************************************************************************80
#
## r8ccs_ijk_test() tests r8ccs_ijk().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
  
  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = int )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ], dtype = int )
  test_num = 20

  print ( '' )
  print ( 'r8ccs_ijk_test():' )
  print ( '  r8ccs_ijk() gets K from (I,J) for a CCS matrix.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  print ( '' )
  print ( '  r8ccs_ijk() locates some (I,J) entries.' )
  print ( '' )
  print ( '         I         J         K' )
  print ( '' )

  for test in range ( 0, test_num ):
    i = rng.integers ( low = 0, high = m, endpoint = False )
    j = rng.integers ( low = 0, high = n, endpoint = False )
    k = r8ccs_ijk ( m, n, nz_num, colptr, rowind, i, j )
    print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  return

def r8ccs_inc ( m, n, nz_num, colptr, rowind, a, i, j, aij ):

#*****************************************************************************80
#
## r8ccs_inc() increments a value of a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer COLPTR(N+1), indicate where each column's data begins.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    real A(NZ_NUM), the nonzero entries.
#
#    integer I, J, the indices of the value to retrieve.
#
#    real AIJ, the value to be added to A(I,J).
#
#  Output:
#
#    real A(NZ_NUM), entry (I,J) has been incremented.
#

#
#  Seek sparse index K corresponding to full index (I,J).
#
  k = r8ccs_ijk ( m, n, nz_num, colptr, rowind, i, j )
#
#  If no K was found, we fail.
#
  if ( k == -1 ):
    print ( '' )
    print ( 'r8ccs_inc(): Fatal error!' )
    print ( '  r8ccs_ijk() could not find the entry.' )
    print ( '  Row I = ', i )
    print ( '  Col J = ', j )
    raise Exception ( 'r8ccs_inc(): Fatal error!' )

  a[k] = a[k] + aij

  return a

def r8ccs_inc_test ( rng ):

#*****************************************************************************80
#
## r8ccs_inc_test() tests r8ccs_inc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = int )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ], dtype = int )

  print ( '' )
  print ( 'r8ccs_inc_test():' )
  print ( '  r8ccs_inc() increments entries in a CCS matrix.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  print ( '' )
  print ( '  r8ccs_inc() increments 10 entries at random.' )
  print ( '' )
  print ( '         I         J         K       NEW_VALUE' )
  print ( '' )

  for test in range ( 0, 10 ):
    k = rng.integers ( low = 0, high = nz_num, endpoint = False )
    i, j = r8ccs_kij ( m, n, nz_num, colptr, rowind, k )
    value = 20.0 + test
    a = r8ccs_inc ( m, n, nz_num, colptr, rowind, a, i, j, value )
    value = r8ccs_get ( m, n, nz_num, colptr, rowind, a, i, j )
    print ( '  %8d  %8d  %8d  %14f' % ( i, j, k, value ) )

  r8ccs_print ( m, n, nz_num, colptr, rowind, a, '  The final CCS matrix:' )

  return

def r8ccs_indicator ( m, n, nz_num, colptr, rowind ):

#*****************************************************************************80
#
## r8ccs_indicator() sets up a CCS indicator matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#  Output:
#
#    real A(NZ_NUM), the matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( nz_num )

  for j in range ( 0, n ):
    for k in range ( colptr[j], colptr[j+1] ):
      i = rowind[k]
      a[k] = fac * ( i + 1 ) + ( j + 1 )

  return a

def r8ccs_indicator_test ( ):

#*****************************************************************************80
#
## r8ccs_indicator_test() tests r8ccs_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_indicator_test():' )
  print ( '  r8ccs_indicator() sets up a CCS indicator matrix;' )
#
#  Set the matrix.
#
  a = r8ccs_indicator ( m, n, nz_num, colptr, rowind )
#
#  Print the matrix.
#
  title = 'An indicator matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  return

def r8ccs_kij ( m, n, nz_num, colptr, rowind, k ):

#*****************************************************************************80
#
## r8ccs_kij() seeks (I,J), the full index of K, the sparse index of a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer COLPTR(N+1), indicate where each column's data begins.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    integer K, the sparse index of an entry of the matrix.
#    1 <= K <= NZ_NUM.
#
#  Output:
#
#    integer I, J, the full indices corresponding to the sparse
#    index K.
#
  i = -1
  j = -1

  if ( k < 0 or nz_num <= k ):
    return i, j
#
#  The row index is easy.
#
  i = rowind[k]
#
#  Determine the column by bracketing in COLPTR.
#
  for jj in range ( 0, n ):
    k1 = colptr[jj]
    k2 = colptr[jj+1] - 1
    if ( k1 <= k and k <= k2 ):
      j = jj
      break

  if ( j == -1 ):
    return i, j

  return i, j

def r8ccs_kij_test ( rng ):

#*****************************************************************************80
#
## r8ccs_kij_test() tests r8ccs_kij().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_kij_test():' )
  print ( '  r8ccs_kij() gets (I,J) from K in a CCS matrix.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  print ( '' )
  print ( '  r8ccs_kij() locates some K entries.' )
  print ( '' )
  print ( '         K         I         J' )
  print ( '' )

  for test in range ( 0, 20 ):
    k = rng.integers ( low = 0, high = nz_num, endpoint = False )
    i, j = r8ccs_kij ( m, n, nz_num, colptr, rowind, k )
    print ( '  %8d  %8d  %8d' % ( k, i, j ) )

  return

def r8ccs_mtv ( m, n, nz_num, colptr, rowind, a, x ):

#*****************************************************************************80
#
## r8ccs_mtv() multiplies a vector times a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real A(NZ_NUM), the matrix.
#
#    real X(M), the vector to be multiplied.
#
#  Output:
#
#    real B(N), the product A'*X.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for k in range ( colptr[j], colptr[j+1] ):
      i = rowind[k]
      b[j] = b[j] + a[k] * x[i]

  return b

def r8ccs_mtv_test ( rng ):

#*****************************************************************************80
#
## r8ccs_mtv_test() tests r8ccs_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12
  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )
 
  print ( '' )
  print ( 'r8ccs_mtv_test():' )
  print ( '  r8ccs_mtv() computes b=A\'*x, where A is a CCS matrix.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  x = np.zeros ( n )
  x[0] = 1.0
  x[n-1] = -1.0

  print ( '  x:' )
  print ( x )

  b = r8ccs_mtv ( m, n, nz_num, colptr, rowind, a, x )

  print ( '  b=A\'*x:' )
  print ( b )

  return

def r8ccs_mv ( m, n, nz_num, colptr, rowind, a, x ):

#*****************************************************************************80
#
## r8ccs_mv() multiplies a CCS matrix times a vector.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real A(NZ_NUM), the matrix.
#
#    real X(N), the vector to be multiplied.
#
#  Output:
#
#    real B(M), the product A*X.
#
  import numpy as np

  b = np.zeros ( m )

  for j in range ( 0, n ):
    for k in range ( colptr[j], colptr[j+1] ):
      i = rowind[k]
      b[i] = b[i] + a[k] * x[j]

  return b

def r8ccs_mv_test ( rng ):

#*****************************************************************************80
#
## r8ccs_mv_test() tests r8ccs_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  m = 5
  n = 5
  nz_num = 12
  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_mv_test():' )
  print ( '  r8ccs_mv() computes b=A*x, where A is a CCS matrix.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  x = np.zeros ( n )
  x[0] = 1.0
  x[n-1] = -1.0

  print ( '  x:' )
  print ( x )

  b = r8ccs_mv ( m, n, nz_num, colptr, rowind, a, x )

  print ( '  b=A*x:' )
  print ( b )

  return

def r8ccs_print ( m, n, nz_num, colptr, rowind, a, title ):

#*****************************************************************************80
#
## r8ccs_print() prints a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real A(NZ_NUM), the matrix.
#
#    string TITLE, a title.
# 
  r8ccs_print_some ( m, n, nz_num, colptr, rowind, a, 0, 0, m - 1, n - 1, title )

  return

def r8ccs_print_test ( rng ):

#*****************************************************************************80
#
## r8ccs_print_test() tests r8ccs_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12
  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_print_test():' )
  print ( '  r8ccs_print() prints a CCS matrix.' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  return

def r8ccs_print_header ( m, n, nz_num, colptr, rowind, title ):

#*****************************************************************************80
#
## r8ccs_print_header() prints the header of a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    string TITLE, a title.
# 
  print ( '' )
  print ( title )
  print ( '  Matrix rows M =          ', m )
  print ( '  Matrix columns N =       ', n )
  print ( '  Matrix nonzeros NZ_NUM = ', nz_num )
  print ( '  The COLPTR vector:' )
  print ( colptr )
  print ( '  The ROWIND vector:' )
  print ( rowind )

  return

def r8ccs_print_some ( m, n, nz_num, colptr, rowind, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ccs_print_some() prints some of a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real A(NZ_NUM), the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  incx = 5

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

      print ( '%4d' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j in range ( j2lo, j2hi + 1 ):

        aij = 0.0

        for k in range ( colptr[j], colptr[j+1] ):
          if ( rowind[k] == i ):
            aij = a[k]
            break

        print ( '  %12g' % ( aij ), end = '' )

      print ( '' )

  return

def r8ccs_print_some_test ( ):

#*****************************************************************************80
#
## r8ccs_print_some_test() tests r8ccs_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 10
  n = 10
  nz_num = 28

  colptr = np.array ( [ 0, 2, 5, 8, 11, 14, 17, 20, 23, 26, 28 ] )
  rowind = np.array ( [ \
    1,  2,  \
    1,  2,  3, \
    2,  3,  4, \
    3,  4,  5, \
    4,  5,  6, \
    5,  6,  7, \
    6,  7,  8, \
    7,  8,  9, \
    8,  9, 10, \
    9, 10 ] )

  print ( '' )
  print ( 'r8ccs_print_some_test():' )
  print ( '  r8ccs_print_some() prints some of a CCS matrix.' )
#
#  Set the matrix.
#
  a = r8ccs_indicator ( m, n, nz_num, colptr, rowind )
#
#  Print the matrix.
#
  title = 'The indicator matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  title = 'Rows 1-5, Cols 4-7:'
  r8ccs_print_some ( m, n, nz_num, colptr, rowind, a, 1, 4, 5, 7, title )

  return

def r8ccs_random ( m, n, nz_num, colptr, rowind, rng ):

#*****************************************************************************80
#
## r8ccs_random() randomizes a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(NZ_NUM), the matrix.
#
  import numpy as np

  a = rng.standard_normal ( size = nz_num )

  return a

def r8ccs_random_test ( rng ):

#*****************************************************************************80
#
## r8ccs_random_test() tests r8ccs_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_random_test():' )
  print ( '  r8ccs_random() randomizes a CCS matrix;' )
#
#  Set the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  return

def r8ccs_read ( col_file, row_file, a_file, m, n, nz_num ):

#*****************************************************************************80
#
## r8ccs_read() reads a CCS matrix from three files.
#
#  Discussion:
#
#    This routine needs the values of M, N, and NZ_NUM, which can be
#    determined by a call to r8ccs_read_size().
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    string COL_FILE, ROW_FILE, A_FILE, the names of the
#    files containing the column pointers, row indices, and matrix entries.
#
#    integer M, N, the number of rows and columns in the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#  Output:
#
#    integer COLPTR(N+1), the column pointers.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    real A(NZ_NUM), the nonzero elements
#    of the matrix.
#
  import numpy as np

  colptr = np.zeros ( nz_num, dtype = np.int32 )
  rowind = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num, dtype = np.float64 )
#
#  Read the column information.
#
  input_unit = open ( col_file, 'r' )

  k = 0

  for line in input_unit:
    words = line.split ( )
    colptr[k] = int ( words[0] )
    k = k + 1

  input_unit.close ( )
#
#  Read the row information.
#
  input_unit = open ( row_file, 'r' )

  k = 0

  for line in input_unit:
    words = line.split ( )
    rowind[k] = int ( words[0] )
    k = k + 1

  input_unit.close ( )
#
#  Read the value information.
#
  input_unit = open ( a_file, 'r' )

  k = 0

  for line in input_unit:
    words = line.split ( )
    a[k] = float ( words[0] )
    k = k + 1

  input_unit.close ( )

  return colptr, rowind, a

def r8ccs_read_size ( col_file, row_file ):

#*****************************************************************************80
#
## r8ccs_read_size() reads the sizes of a CCS matrix from a file.
#
#  Discussion:
#
#    The value of M is "guessed" to be the largest value that occurs in
#    the ROW file.  However, if a row index of 0 is encountered, then
#    the value of M is incremented by 1.
#
#    The value of N is the number of records in the COL file minus 1.
#
#    The value of NZ_NUM is simply the number of records in the ROW file.
#
#    The value of BASE is 0 or 1, depending on whether the program
#    "guesses" that the row and column indices are 0-based or 1-based.
#    Although the first entry of the COL array might be used as evidence,
#    this program makes its determination based on whether it encounters
#    a 0 index in the ROW file.
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    string COL_FILE, ROW_FILE, the names of the
#    column and row files that describe the structure of the matrix.
#
#  Output:
#
#    integer M, N, the inferred number of rows and columns
#    in the sparse matrix.
#
#    integer NZ_NUM, the number of nonzero entries in the
#    sparse matrix.
#
#    integer BASE, is 0 if the row indexing is believed
#    to be 0-based, and 1 if the row-index is believed to be
#    1-based.  In uncertain cases, BASE = 1 is the default.
#

#
#  Default values.
#
  m = -1
  n = -1
  nz_num = 0
  base = 1
#
#  Check the COL file first.
#
  input_unit = open ( col_file, 'r' )

  n = 0

  for line in input_unit:
    words = line.split ( )
    k = int ( words[0] )
    n = n + 1

  n = n - 1

  input_unit.close ( )
#
#  Check the ROW file.
#
  input_unit = open ( row_file, 'r' )

  base = 1
  m = 0

  for line in input_unit:
    words = line.split ( )
    i = int ( words[0] )
    nz_num = nz_num + 1
    m = max ( m, i )
    if ( i == 0 ):
      base = 0

  input_unit.close ( )

  return m, n, nz_num, base

def r8ccs_read_test ( ):

#*****************************************************************************80
#
## r8ccs_read_test() tests r8ccs_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  a_file = 'r8ccs_a.txt';
  col_file = 'r8ccs_col.txt';
  row_file = 'r8ccs_row.txt';

  print ( '' )
  print ( 'r8ccs_read_test():' )
  print ( '  r8ccs_read() reads a CCS matrix from a file.' )
#
#  Read the matrix sizes, and the matrix values.
#
  m, n, nz_num, base = r8ccs_read_size ( col_file, row_file )

  colptr, rowind, a = r8ccs_read ( col_file, row_file, a_file, m, n, nz_num )

  if ( base == 1 ):
    print ( '' )
    print ( '  ROWIND and COLPTR indexing is 1-based.' )
    colptr = colptr - 1
    rowind = rowind - 1
    print ( '  ROWIND and COLPTR indexing rebased at 0.' )
#
#  Print the matrix.
#
  title = 'The CCS matrix read from the file:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  return

def r8ccs_set ( m, n, nz_num, colptr, rowind, a, i, j, aij ):

#*****************************************************************************80
#
## r8ccs_set() sets a value of a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer COLPTR(N+1), indicate where each column's data begins.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    real A(NZ_NUM), the nonzero entries.
#
#    integer I, J, the indices of the value to retrieve.
#
#    real AIJ, the new value of A(I,J).
#
#  Output:
#
#    real A(NZ_NUM), the entry of A corresponding to (I,J)
#    has been reset.
#

#
#  Seek sparse index K corresponding to full index (I,J).
#
  k = r8ccs_ijk ( m, n, nz_num, colptr, rowind, i, j )
#
#  If no K was found, we fail.
#
  if ( k == -1 ):
    print ( '' )
    print ( 'r8ccs_set(): Fatal error!' )
    print ( '  r8ccs_ijk() could not find the entry.' )
    print ( '  Row I = ', i )
    print ( '  Col J = ', j )
    raise Exception ( 'r8ccs_set(): Fatal error!' )

  a[k] = aij

  return a

def r8ccs_set_test ( rng ):

#*****************************************************************************80
#
## r8ccs_set_test() tests r8ccs_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_set_test():' )
  print ( '  r8ccs_set() sets entries in a CCS matrix' )
#
#  Randomize the matrix.
#
  a = r8ccs_random ( m, n, nz_num, colptr, rowind, rng )
#
#  Print the matrix.
#
  title = 'A random CCS matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  print ( '' )
  print ( '  r8ccs_set() sets 10 entries at random.' )
  print ( '' )
  print ( '         I         J         K      NEW_VALUE' )
  print ( '' )

  for test in range ( 0, 10 ):
    k = rng.integers ( low = 0, high = nz_num, endpoint = False )
    i, j = r8ccs_kij ( m, n, nz_num, colptr, rowind, k )
    value = 100.0 + test
    a = r8ccs_set ( m, n, nz_num, colptr, rowind, a, i, j, value )
    print ( '  %8d  %8d  %8d  %14f' % ( i, j, k, value ) )

  r8ccs_print ( m, n, nz_num, colptr, rowind, a, '  The final CCS matrix:' )

  return

def r8ccs_to_r8ge ( m, n, nz_num, colptr, rowind, a ):

#*****************************************************************************80
#
## r8ccs_to_r8ge() converts a CCS matrix to GE format.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real A(NZ_NUM), the CCS matrix.
#
#  Output:
#
#    real B(M,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for k in range ( colptr[j], colptr[j+1] ):
      i = rowind[k]
      b[i,j] = a[k]

  return b

def r8ccs_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8ccs_to_r8ge_test() tests r8ccs_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_to_r8ge_test():' )
  print ( '  r8ccs_to_r8ge() converts a matrix from CCS to GE format;' )
#
#  Set the matrix.
#
  a_r8cc = r8ccs_indicator ( m, n, nz_num, colptr, rowind )
#
#  Print the matrix.
#
  title = 'An indicator matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a_r8cc, title )
#
#  Make a GE copy of the CCS matrix.
#
  a_r8ge = r8ccs_to_r8ge ( m, n, nz_num, colptr, rowind, a_r8cc )

  print ( '  The GE matrix:' )
  print ( a_r8ge )

  return

def r8ccs_write ( col_file, row_file, a_file, m, n, nz_num, colptr, rowind, a ):

#*****************************************************************************80
#
## r8ccs_write() writes a CCS matrix to three files.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    string COL_FILE, ROW_FILE, A_FILE, the names of the
#    files containing the column pointers, row entries, and matrix entries.
#
#    integer M, N, the number of rows and columns in the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer COLPTR(N+1), the column pointers.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#

#
#  Write the column information.
#
  output_unit = open ( col_file, 'w' )

  for k in range ( 0, n + 1 ):
    s = '%d\n' % ( colptr[k] )
    output_unit.write ( s )

  output_unit.close ( )
#
#  Write the row information.
#
  output_unit = open ( row_file, 'w' )

  for k in range ( 0, nz_num ):
    s = '%d\n' % ( rowind[k] )
    output_unit.write ( s )

  output_unit.close ( )
#
#  Write the value information.
#
  output_unit = open ( a_file, 'w' )

  for k in range ( 0, nz_num ):
    s = '%d\n' % ( a[k] )
    output_unit.write ( s )

  output_unit.close ( )

  return

def r8ccs_write_test ( ):

#*****************************************************************************80
#
## r8ccs_write_test() tests r8ccs_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  a_file = 'r8ccs_a.txt'
  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  col_file = 'r8ccs_col.txt'
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )
  row_file = 'r8ccs_row.txt'

  print ( '' )
  print ( 'r8ccs_write_test():' )
  print ( '  r8ccs_write() writes a CCS matrix to 3 files' )
#
#  Set the matrix.
#
  a = r8ccs_indicator ( m, n, nz_num, colptr, rowind )
#
#  Print the matrix.
#
  title = 'An indicator matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )
#
#  Write the matrix to files.
#
  r8ccs_write ( col_file, row_file, a_file, m, n, nz_num, colptr, rowind, a )

  return

def r8ccs_zeros ( m, n, nz_num, colptr, rowind ):

#*****************************************************************************80
#
## r8ccs_zeros() zeros a CCS matrix.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
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
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#  Output:
#
#    real A(NZ_NUM), the matrix.
#
  import numpy as np

  a = np.zeros ( nz_num )

  return a

def r8ccs_zeros_test ( ):

#*****************************************************************************80
#
## r8ccs_zeros_test() tests r8ccs_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  nz_num = 12

  colptr = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  rowind = np.array ( [ 0, 1, 3, 0, 1, 2, 4, 3, 4, 0, 1, 4 ] )

  print ( '' )
  print ( 'r8ccs_zeros_test():' )
  print ( '  r8ccs_zeros() zeros a CCS matrix;' )
#
#  Set the matrix.
#
  a = r8ccs_zeros ( m, n, nz_num, colptr, rowind )
#
#  Print the matrix.
#
  title = 'Zero matrix in CCS format:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, a, title )

  return

def r8ge_to_r8ccs ( m, n, Age ):

#*****************************************************************************80
#
## r8ge_to_r8ccs() converts a GE matrix to CCS format.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix.
#
#    real Age(M,N), the GE matrix.
#
#  Output:
#
#    integer NZ_NUM, the number of nonzero elements in A.
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real Accs(NZ_NUM), the CCS matrix.
#
  import numpy as np

  nz_num = np.count_nonzero ( Age )
  colptr = np.zeros ( n + 1, dtype = int )
  rowind = np.zeros ( nz_num, dtype = int )
  Accs = np.zeros ( nz_num, dtype = float )
  
  k = 0
  colptr[0] = 0
  for j in range ( 0, n ):
    colptr[j+1] = colptr[j]
    for i in range ( 0, m ):
      if ( Age[i,j] != 0.0 ):
        Accs[k] = Age[i,j]
        rowind[k] = i
        colptr[j+1] = colptr[j+1] + 1
        k = k + 1;

  return nz_num, colptr, rowind, Accs

def r8ge_to_r8ccs_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8ccs_test() tests r8ge_to_r8ccs().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m = 5
  n = 5

  Age = np.array ( [ \
    [ 11, 12, 13,  0, 15 ], \
    [  0,  0, 23,  0,  0 ], \
    [ 31,  0, 33,  0, 35 ], \
    [ 41, 42,  0, 44,  0 ], \
    [  0, 52,  0, 54, 55 ] ] )

  print ( '' )
  print ( 'r8ge_to_r8ccs_test():' )
  print ( '  r8ge_to_r8ccs() converts an r8ge matrix to r8ccs format.' )
#
#  Print the matrix.
#
  print ( '' )
  print ( '  The GE matrix:' )
  pprint.pprint ( Age )
#
#  Make a GE copy of the CCS matrix.
#
  nz_num, colptr, rowind, Accs = r8ge_to_r8ccs ( m, n, Age )

  title = 'The r8ccs version of the matrix:'
  r8ccs_print_header ( m, n, nz_num, colptr, rowind, title )
  r8ccs_print ( m, n, nz_num, colptr, rowind, Accs, title )

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
  r8ccs_test ( )
  timestamp ( )

