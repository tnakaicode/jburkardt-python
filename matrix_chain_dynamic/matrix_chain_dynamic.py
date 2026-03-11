#! /usr/bin/env python3
#
def matrix_chain_dynamic_test ( ):

#*****************************************************************************80
#
## matrix_chain_dynamic_test() tests matrix_chain_dynamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'matrix_chain_dynamic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test matrix_chain_dynamic().' )

  for test in range ( 1, 11 ):

    if ( test == 1 ):
      dims = np.array ( [ 40, 20, 30, 10, 30 ], dtype = int )
    elif ( test == 2 ):
      dims = np.array ( [ 1, 2, 3, 4, 3 ], dtype = int )
    elif ( test == 3 ):
      dims = np.array ( [ 10, 20, 30 ], dtype = int )
    elif ( test == 4 ):
      dims = np.array ( [ 10, 30, 5, 60 ], dtype = int )
    elif ( test == 5 ):
      dims = np.array ( [ 10, 20 ], dtype = int )
    elif ( test == 6 ):
      dims = np.array ( [ 40, 20, 0, 10, 30 ], dtype = int )
    elif ( test == 7 ):
      dims = np.array ( [ 1, 100, 1, 100, 1 ], dtype = int )
    elif ( test == 8 ):
      dims = np.array ( [ 100, 50, 1, 50, 100 ], dtype = int )
    elif ( test == 9 ):
      dims = np.array ( [ 1, 50, 100, 50, 1 ], dtype = int )
    elif ( test == 10 ):
      dims = np.array ( [ 4, 10, 3, 12, 20, 7 ], dtype = int )

    print ( '' )
    n = len ( dims )
    print ( '  Number of matrices in product = ', n )
    print ( '  Matrix dimensions:', end = '' )
    for i in range ( 0, n ):
      print ( '  ', dims[i], end = '' )
    print ( '' )
    orderings = catalan_number ( n - 2 )
    print ( '  Possible orderings = ', orderings ) 
    cost = matrix_chain_dynamic ( dims )
    print ( '  Minimal cost = ', cost )
#
#  Terminate.
#
  print ( '' )
  print ( 'matrix_chain_dynamic_test():' )
  print ( '  Normal end of execution.' )

  return

def catalan_number ( n ):

#*****************************************************************************80
#
## catalan_number() computes the N-th Catalan number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the Catalan number.
#
#  Output:
#
#    integer C: the value of the Catalan number.
#
  import numpy as np

  if ( n < 0 ):
    c = 0
    return c
 
  c = 1
#
#  The extra parentheses ensure that the integer division is
#  done AFTER the integer multiplication.
#
  for i in range ( 1, n + 1 ):
    c = ( c * 2 * ( 2 * i - 1 ) ) // ( i + 1 )

  return c

def matrix_chain_dynamic ( dims ):

#*****************************************************************************80
#
## matrix_chain_dynamic() finds the lowest cost to form a multiple matrix product.
#
#  Discussion:
#
#    This code represents a dynamic programming approach from 
#    a Wikipedia article.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 December 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein,
#    Introduction to Algorithms,
#    MIT Press, 2001,
#    ISBN: 978-0-262-03293-3,
#    LC: QA76.C662.
#
#  Input:
#
#    integer dims(n+1): matrix dimension information.  Matrix A(i)
#    has dimensions dims(i) x dims(i+1).  All entries must be positive.
#
#  Output:
#
#    integer cost: the minimal cost, in terms of scalar multiplications,
#    for the optimal ordering of the matrix multiplications.
#
  import numpy as np

  cost = 0
#
#  N is the number of matrices in the product.
#
  n = dims.size - 1
  if ( n < 2 ):
    return cost

  if ( np.any ( dims <= 0 ) ):
    return cost
#
#  m[i,j] = Minimum number of scalar multiplications (i.e., cost)
#  needed to compute the matrix A[i]A[i+1]...A[j] = A[i..j]
#  The cost is zero when multiplying one matrix.
#
#  K is the index of the subsequence split that achieved minimal cost
#
  m = np.iinfo(np.int32).max * np.ones ( [ n, n ], dtype = int )
  for i in range ( 0, n ):
    m[i,i] = 0
  s = - np.ones ( [ n, n ], dtype = int )

  for len in range ( 2, n + 2 ):
    for i in range ( 1, n + 2 - len ):
      j = i - 1 + len
      for k in range ( i, j ):
        cost = m[i-1,k-1] + m[k,j-1] + dims[i-1] * dims[k] * dims[j]
        if ( cost <= m[i-1,j-1] ):
          m[i-1,j-1] = cost
          s[i-1,j-1] = k 

  return cost

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

if ( __name__ == "__main__" ):
  timestamp ( )
  matrix_chain_dynamic_test ( )
  timestamp ( )
