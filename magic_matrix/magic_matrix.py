#! /usr/bin/env python3
#
def magic_matrix_test ( ):

#*****************************************************************************80
#
## magic_matrix_test() tests magic_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'magic_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test magic_matrix()' )

  magic_list_test ( )
  magic_nparray_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'magic_matrix_test():' )
  print ( '  Normal end of execution.' )

def magic_list ( n ):

#*****************************************************************************80
#
## magic_list() returns a magic matrix of odd order n as a list of lists.
#
#  Discussion:
#
#    Every row and column of the matrix has the same sum.
#
#    The algorithm proceeds as follows:
#
#    a) Start in the middle of the top row, and let k = 1
#    b) Insert k into the grid.
#    c) If k = n^2, you are done.
#    d) Increment k.
#    e) Move diagonally up and to the right, but wrap to the first
#       column, or to the last row, if you leave the grid.
#    f) If that cell is already occupied, drop down one space from
#       your current position.
#    g) Return to step (b).  
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 January 2023
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Collison,
#    Algorithms 117 and 118:
#    Magic square (even order) and Magic square (odd order),
#    Communications of the ACM,
#    Volume 5, Number 8, pages 435-436.
#
#    Maurice Kraitchik,
#    Mathematical Recreations,
#    Norton, 1942, pages 149-152.
#
#    Christian Hill,
#    Learning Scientific Programming with Python,
#    Cambridge University Press,
#    Second Edition, 2020,
#    ISBN: 978-1108745918
#
#  Input:
#
#    integer n: the number of rows and columns in the matrix,
#    which must be odd.
#
#  Output:
#
#    integer A(n,n): the magic matrix, as a list.
#
  if ( ( n % 2 ) != 1 ):
    print ( '' )
    print ( 'magic_list: Fatal error!' )
    print ( '  Input value n must be an odd integer.' )
    raise Exception ( 'magic_list(): Fatal error!' )
#
#  Awkwardly create an n x n list of lists.
#
  row = []
  for j in range ( 0, n ):
    row.append ( 0 )

  A = []
  for i in range ( 0, n ):
    A.append ( row.copy() )
#
#  Now fill it with integers 1 through n**2.
#
  k = 1
  i = 0
  j = n // 2

  while ( k <= n**2 ):

    A[i][j] = k
    k = k + 1

    new_i = ( i - 1 ) % n
    new_j = ( j + 1 ) % n

    if ( A[new_i][new_j] ):
      i = i + 1
    else:
      i = new_i
      j = new_j

  return A

def magic_list_test ( ):

#*****************************************************************************80
#
## magic_list_test() tests magic_list().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 February 2025
#
#  Author:
#
#    John Burkardt
#
  import pprint

  pp = pprint.PrettyPrinter ( indent = 2 )

  print ( '' )
  print ( 'magic_list_test():' )
  print ( '  magic_list() creates a magic matrix as a list of lists.' )

  for n in [ 3, 5 ]:

    A = magic_list ( n )
    print ( '' )
    print ( '  Magic matrix for n =', n )
    pp.pprint ( A )

    print ( '  Row sums:' )
    for i in range ( 0, n ):
      rsum = 0
      for j in range ( 0, n ):
        rsum = rsum + A[i][j]
      print ( ' ', rsum, end = '' )
    print ( '' )

    print ( '  Column sums:' )
    for j in range ( 0, n ):
      csum = 0
      for i in range ( 0, n ):
        csum = csum + A[i][j]
      print ( ' ', csum, end = '' )
    print ( '' )

    print ( '  Diagonal sum:' )
    dsum = 0
    for i in range ( 0, n ):
      dsum = dsum + A[i][i]
    print ( ' ', dsum )

    print ( '  Antidiagonal sum:' )
    asum = 0
    for i in range ( 0, n ):
      asum = asum + A[i][n-1-i]
    print ( ' ', asum )

  return

def magic_nparray ( n ):

#*****************************************************************************80
#
## magic_nparray() returns a magic matrix of odd order n as a numpy array.
#
#  Discussion:
#
#    Every row and column of the matrix has the same sum.
#
#    The algorithm proceeds as follows:
#
#    a) Start in the middle of the top row, and let k = 1
#    b) Insert k into the grid.
#    c) If k = n^2, you are done.
#    d) Increment k.
#    e) Move diagonally up and to the right, but wrap to the first
#       column, or to the last row, if you leave the grid.
#    f) If that cell is already occupied, drop down one space from
#       your current position.
#    g) Return to step (b).  
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 January 2023
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Collison,
#    Algorithms 117 and 118:
#    Magic square (even order) and Magic square (odd order),
#    Communications of the ACM,
#    Volume 5, Number 8, pages 435-436.
#
#    Maurice Kraitchik,
#    Mathematical Recreations,
#    Norton, 1942, pages 149-152.
#
#    Christian Hill,
#    Learning Scientific Programming with Python,
#    Cambridge University Press,
#    Second Edition, 2020,
#    ISBN: 978-1108745918
#
#  Input:
#
#    integer n: the number of rows and columns in the matrix,
#    which must be odd.
#
#  Output:
#
#    integer A(n,n): the magic matrix.
#
  import numpy as np

  if ( ( n % 2 ) != 1 ):
    print ( '' )
    print ( 'magic_nparray(): Fatal error!' )
    print ( '  Input value n must be an odd integer.' )
    raise Exception ( 'magic_nparray(): Fatal error!' )

  A = np.zeros ( [ n, n ], dtype = int )

  k = 1
  i = 0
  j = n // 2

  while ( k <= n**2 ):

    A[i,j] = k
    k = k + 1

    new_i = ( i - 1 ) % n
    new_j = ( j + 1 ) % n

    if ( A[new_i,new_j] ):
      i = i + 1
    else:
      i = new_i
      j = new_j

  return A

def magic_nparray_test ( ):

#*****************************************************************************80
#
## magic_nparray_test() tests magic_nparray().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'magic_nparray_test():' )
  print ( '  magic_nparray() creates a magic matrix as a numpy array.' )

  for n in [ 3, 5 ]:

    A = magic_nparray ( n )
    print ( '' )
    print ( '  Magic matrix for n =', n )
    print ( A )

    print ( '  Row sums:' )
    rsum = np.sum ( A, axis = 1 )
    print ( rsum )

    print ( '  Column sums:' )
    csum = np.sum ( A, axis = 0 )
    print ( csum )

    print ( '  Diagonal sum:' )
    dsum = np.trace ( A )
    print ( dsum )

    print ( '  Antidiagonal sum:' )
    asum = np.trace ( np.flipud ( A ) )
    print ( asum )

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
  magic_matrix_test ( )
  timestamp ( )

