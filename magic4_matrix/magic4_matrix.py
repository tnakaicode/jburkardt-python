#! /usr/bin/env python3
#
def magic4_matrix_test ( ):

#*****************************************************************************80
#
## magic4_matrix_test() tests magic4_matrix().
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
  import platform

  print ( '' )
  print ( 'magic4_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  magic4_matrix() creates a magic matrix whose order' )
  print ( '  n is a multiple of 4.' )

  for n in [ 4, 8, 12 ]:

    A = magic4_matrix ( n )
    print ( '' )
    print ( '  Magic matrix for n =', n )
    print ( A )

    print ( '' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'magic4_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def magic4_matrix ( n ):

#*****************************************************************************80
#
## magic4_matrix() returns a magic matrix of order n, where n is a multiple of 4.
#
#  Discussion:
#
#    Every row and column of the matrix has the same sum.
#
#    The algorithm proceeds as follows:
#
#    Number the cells consecutively, 1, 2, ..., n^2.
#    Divide the matrix into 4x4 blocks, draw an X in each block,
#    and in the x-ed out cells replace k by n^2+1-k.
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
#    John Burkardt.
#
#  Input:
#
#    integer n: the number of rows and columns in the matrix,
#    which must be a multiple of 4.
#
#  Output:
#
#    integer A(n,n): the magic matrix.
#
  import numpy as np

  if ( ( n % 4 ) != 0 ):
    print ( '' )
    print ( 'magic4_matrix(): Fatal error!' )
    print ( '  Input value n must be a multiple of 4.' )
    raise Exception ( 'magic4_matrix(): Fatal error!' )

  A = np.zeros ( [ n, n ], dtype = int )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      m1 = ( abs ( i - j ) ) % 4
      m2 = ( i + j + 1 ) % 4
      k1 = i * n + j + 1
      k2 = n * n + 1 - k1
      if ( ( m1 == 0 or m2 == 0 ) ):
        A[i,j] = k2
      else:
        A[i,j] = k1

  return A

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
  magic4_matrix_test ( )
  timestamp ( )

