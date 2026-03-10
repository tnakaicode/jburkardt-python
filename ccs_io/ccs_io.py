#! /usr/bin/env python3
#
def ccs_header_print ( icc, ccc, title ):

#*****************************************************************************80
#
## ccs_header_print() prints the header of a CCS matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ICC(NCC), CCC(N+1), row and compressed column indices.
#
#    string TITLE: a title for the matrix.
#
  import numpy as np

  m = np.max ( icc ) + 1
  n = len ( ccc ) - 1
  ncc = len ( icc )

  print ( '' )
  print ( title )
  print ( '  CCS matrix header:' )
  print ( '  Number of rows        M = ', m )
  print ( '  Number of columns     N = ', n )
  print ( '  Number of nonzeros  NCC = ', ncc )
  print ( '  Compressed column indices:' )
  print ( ccc )

  return
def ccs_read_test ( ):

#*****************************************************************************80
#
## ccs_read_test() tests ccs_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2022
#
#  Author:
#
#    John Burkardt
#

  print ( '' )
  print ( 'ccs_read_test():' )
  print ( '  Read a sparse matrix in CCS format from 3 files.' )

  for base in range ( 0, 2 ):

    if ( base == 0 ):
      prefix = 'simple_base0'
      title = 'CCS matrix with base-0 indexing'
    else:
      prefix = 'simple_base1'
      title = 'CCS matrix with base-1 indexing'
#
#  Read the matrix data.
#
    icc, ccc, acc, ncc, n = ccs_read ( prefix )
#
#  Print the matrix.
#
    m = n
    ccs_print ( m, n, ncc, icc, ccc, acc, title )

  return

def ccs_io_test ( ):

#*****************************************************************************80
#
## ccs_io_test() tests ccs_io().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ccs_io_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ccs_io().' )

  ccs_write_test ( )
  ccs_read_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ccs_io_test():' )
  print ( '  Normal end of execution.' )

  return

def ccs_write_test ( ):

#*****************************************************************************80
#
## ccs_write_test() tests ccs_write() using a tiny matrix.
#
#  Discussion:
#
#    This test uses a trivial matrix whose full representation is:
#
#          2  3  0  0  0
#          3  0  4  0  6
#      A = 0 -1 -3  2  0
#          0  0  1  0  0
#          0  4  2  0  1
#
#    The 1-based CC representation is
#
#      #  ICC  CCC  ACC
#     --  ---  ---  ---
#      1    1    1    2
#      2    2         3
#
#      3    1    3    3
#      4    3        -1
#      5    5         4
#
#      6    2    6    4
#      7    3        -3
#      8    4         1
#      9    5         2
#
#     10    3   10    2
#
#     11    2   11    6
#     12    5         1
#
#     13    *   13
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ccs_write_test():' )
  print ( '  Write a sparse matrix in CCS format to 3 files.' )

  m = 5
  n = 5
  ncc = 12

  print ( '' )
  print ( '  Full rows    M = ', m )
  print ( '  Full columns N = ', n )
  print ( '  Full storage   = ', m * n )

  for base in range ( 0, 2 ):

    acc = np.array ( [ \
      2.0,  3.0, \
      3.0, -1.0,  4.0, \
      4.0, -3.0,  1.0, 2.0, \
      2.0, \
      6.0, 1.0 ] )

    if ( base == 0 ):
      ccc = np.array ( [ \
        0, 2, 5, 9, 10, 12 ] )
    else:
      ccc = np.array ( [ \
        1, 3, 6, 10, 11, 13 ] )

    if ( base == 0 ):
      icc = np.array ( [ \
        0, 1, \
        0, 2, 4, \
        1, 2, 3, 4, \
        2, \
        1, 4 ] )
    else:
      icc = np.array ( [ \
        1, 2, \
        1, 3, 5, \
        2, 3, 4, 5, \
        3, \
        2, 5 ] )

    if ( base == 0 ):
      prefix = 'simple_base0'
      title = 'CCS matrix with 0-based indexing'
    else:
      prefix = 'simple_base1'
      title = 'CCS matrix with 1-based indexing'
#
#  Print the matrix.
#
    ccs_print ( m, n, ncc, icc, ccc, acc, title )
#
#  Write the matrix to 3 files.
#
    ccs_write ( prefix, ncc, n, icc, ccc, acc )

  return

def ccs_mv ( m, n, ncc, icc, ccc, acc, x ):

#*****************************************************************************80
#
## ccs_mv() multiplies a CCS matrix by a vector
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 July 2014
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
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NCC, the number of values.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns
#
#    real ACC(NCC), the values.
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
    for k in range ( ccc[j], ccc[j+1] ):
      i = icc[k]
      b[i] = b[i] + acc[k] * x[j]

  return b

def ccs_print ( m, n, ncc, icc, ccc, acc, title ):

#*****************************************************************************80
#
## ccs_print() prints a sparse matrix in CCS format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#
#    integer NCC, the number of elements.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
#    character TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '     #     I     J       A' )
  print ( '  ----  ----  ----  --------------' )
  print ( '' )

  if ( ccc[0] == 0 ):

    j = 0
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+1] <= k ):
        j = j + 1
      print ( '  %4d  %4d  %4d  %16.8g' % ( k, i, j, acc[k] ) )
#
#  Matrix uses 1-based indexing.
#
  else:

    j = 1
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j] <= k + 1 ):
        j = j + 1
      print ( '  %4d  %4d  %4d  %16.8g' % ( k + 1, i, j, acc[k] ) )

  return

def ccs_print_some ( i_min, i_max, j_min, j_max, ncc, n, icc, ccc, acc, title ):

#*****************************************************************************80
#
## ccs_print_some() prints some of a sparse matrix in CCS format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I_MIN, IMAX, the first and last rows to print.
#
#    integer J_MIN, J_MAX, the first and last columns 
#    to print.
#
#    integer NCC, the number of elements.
#
#    integer N, the number of columns.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
#    string TITLE, a title.
#
  if ( ccc[0] == 0 ):

    j = 0
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+2] <= k - 1 ):
        j = j + 1
      if ( i_min <= i and i <= i_max and j_min <= j and j <= j_max ):
        print ( '  %4d  %4d  %4d  %16.8g' % ( k - 1, i, j, acc[k] ) )

  else:

    j = 1
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+1] <= k ):
        j = j + 1
      if ( i_min <= i and i <= i_max and j_min <= j and j <= j_max ):
        print ( '  %4d  %4d  %4d  %16.8g' % ( k, i, j, acc[k] ) )


  return

def ccs_read ( prefix ):

#*****************************************************************************80
#
## ccs_read() reads data about a sparse matrix in CCS format.
#
#  Discussion:
#
#    Three files are presumed to exist:
#    * prefix_icc.txt contains NCC ICC values
#    * prefix_ccc.txt contains N+1 CCC values
#    * prefix_acc.txt contains NCC ACC values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, a common prefix for the filenames.
#
#  Output:
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
#    integer NCC, the number of elements.
#
#    integer N, the number of columns in the matrix.
#
  import numpy as np

  filename_icc = prefix + '_icc.txt'
  icc = np.loadtxt ( filename_icc )

  filename_ccc = prefix + '_ccc.txt'
  ccc = np.loadtxt ( filename_ccc )

  filename_acc = prefix + '_acc.txt'
  acc = np.loadtxt ( filename_acc )

  ncc = len ( icc )
  n = len ( ccc ) - 1

  return icc, ccc, acc, ncc, n

def ccs_write ( prefix, ncc, n, icc, ccc, acc ):

#*****************************************************************************80
#
## ccs_write() writes a sparse matrix in CCS format to 3 files.
#
#  Discussion:
#
#    Three files will be created:
#    * prefix_icc.txt contains NCC ICC values
#    * prefix_ccc.txt contains N+1 CCC values
#    * prefix_acc.txt contains NCC ACC values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, a common prefix for the filenames.
#
#    integer NCC, the number of elements.
#
#    integer N, the number of columns in the matrix.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
  import numpy as np

  filename_icc = prefix + '_icc.txt'
  np.savetxt ( filename_icc, icc )

  filename_ccc = prefix + '_ccc.txt'
  np.savetxt ( filename_ccc, ccc )

  filename_acc = prefix + '_acc.txt'
  np.savetxt ( filename_acc, acc )

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
  ccs_io_test ( )
  timestamp ( )


