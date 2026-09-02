#! /usr/bin/env python3
#
def ccs_to_ge_test ( ):

#*****************************************************************************80
#
## ccs_to_ge_test() tests ccs_to_ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ccs_to_ge_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ccs_to_ge().' )

  ccs_to_ge_test01 ( )
  ccs_to_ge_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ccs_to_ge_test():' )
  print ( '  Normal end of execution.' )

  return

def ccs_to_ge_test01 ( ):

#*****************************************************************************80
#
## ccs_to_ge_test01() tests ccs_to_ge() using a 1-based CCS matrix.
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
#    The 1-based CCS representation is
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
#    15 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m = 5
  n = 5
  ncc = 12

  acc = np.array ( [ \
    2.0,  3.0, \
    3.0, -1.0,  4.0, \
    4.0, -3.0,  1.0, 2.0, \
    2.0, \
    6.0, 1.0 ] )

  ccc = np.array ( [ \
    1, 3, 6, 10, 11, 13 ] )

  icc = np.array ( [ \
    1, 2, \
    1, 3, 5, \
    2, 3, 4, 5, \
    3, \
    2, 5 ] )

  print ( '' )
  print ( 'ccs_to_ge_test01()' )
  print ( '  Convert a 1-based CCS matrix to GE format.' )
#
#  Print the CCS matrix.
#
  ccs_print ( m, n, ncc, icc, ccc, acc, '  The CCS matrix:' )
#
#  Convert it.
#
  Age = ccs_to_ge ( m, n, ncc, icc, ccc, acc )
#
#  Print the GE matrix.
#
  print ( '' )
  print ( '  The GE matrix:' )
  pprint.pprint ( Age )

  return

def ccs_to_ge_test02 ( ):

#*****************************************************************************80
#
## ccs_to_ge_test02() tests ccs_to_st() using a 0-based CCS matrix.
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
#    The 0-based CCS representation is
#
#      #  ICC  CCC  ACC
#     --  ---  ---  ---
#      0    0    0    2
#      1    1         3
#
#      2    0    2    3
#      3    2        -1
#      4    4         4
#
#      5    1    5    4
#      6    2        -3
#      7    3         1
#      8    4         2
#
#      9    2    9    2
#
#     10    1   10    6
#     11    4         1
#
#     12    *   12
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m = 5
  n = 5
  ncc = 12

  acc = np.array ( [ \
    2.0,  3.0, \
    3.0, -1.0,  4.0, \
    4.0, -3.0,  1.0, 2.0, \
    2.0, \
    6.0, 1.0 ] )

  ccc = np.array ( [ \
    0, 2, 5, 9, 10, 12 ] )

  icc = np.array ( [ \
    0, 1, \
    0, 2, 4, \
    1, 2, 3, 4, \
    2, \
    1, 4  ] )

  print ( '' )
  print ( 'ccs_to_ge_test02():' )
  print ( '  Convert a 0-based CCS matrix to GE format.' )
#
#  Print the CCS matrix.
#
  ccs_print ( m, n, ncc, icc, ccc, acc, '  The CCS matrix:' )
#
#  Convert it.
#
  Age = ccs_to_ge ( m, n, ncc, icc, ccc, acc )
#
#  Print the GE matrix.
#
  print ( '' )
  print ( '  The GE matrix:' )
  pprint.pprint ( Age )

  return

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
#    22 June 2022
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

def ccs_to_ge ( m, n, ncc, icc, ccc, Accs ):

#*****************************************************************************80
#
## ccs_to_ge() converts sparse matrix information from CCS to GE format.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NCC, the number of elements.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real Accs(NCC), the values.
#
#  Output:
#
#    real Age(M,N): the matrix data in GE format.
#
  import numpy as np

  Age = np.zeros ( [ m, n ] )

  nst = 0

  if ( ccc[0] == 0 ):

    jlo = 0
    jhi = n - 1
  
    for j in range ( jlo, jhi + 1 ):

      klo = ccc[j]
      khi = ccc[j+1]

      for k in range ( klo, khi ):

        i = icc[k]
        Age[i,j] = Accs[nst]
        nst = nst + 1

  else:

    jlo = 0
    jhi = n - 1
  
    for j in range ( jlo, jhi + 1 ):

      klo = ccc[j] - 1
      khi = ccc[j+1] - 1

      for k in range ( klo, khi ):

        i = icc[k]
        Age[i-1,j] = Accs[nst]
        nst = nst + 1

  return Age

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
  ccs_to_ge_test ( )
  timestamp ( )
