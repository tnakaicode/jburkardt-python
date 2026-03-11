#! /usr/bin/env python3
#
def sparse_test ( ):

#*****************************************************************************80
#
## sparse_test() tests sparse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sparse_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  sparse() is a scipy library of functions for dealing with' )
  print ( '  sparse matrices.' )

  sparse_test01 ( )
  sparse_test02 ( )
  sparse_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sparse_test():' )
  print ( '  Normal end of execution.' )

  return

def sparse_test01 ( ):

#*****************************************************************************80
#
## sparse_test01() creates a tiny sparse matrix.
#
#  Discussion:
#
#    This unrealistic example sets up a tiny matrix:
#
#    11  12   0   0  15
#     0  22  23   0   0
#    31   0  33  34  35
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.sparse import coo_matrix
  import numpy as np

  print ( '' )
  print ( 'sparse_test01()' )
  print ( '  Define a tiny sparse matrix.' )

  i = np.array ( [  0,  0,  0,  1,  1,  2,  2,  2,  2 ] )
  j = np.array ( [  0,  1,  4,  1,  2,  0,  2,  3,  4 ] )
  s = np.array ( [ 11, 12, 15, 22, 23, 31, 33, 34, 35 ] )
  m = 3
  n = 5

  A = coo_matrix ( ( s, ( i, j ) ), shape = ( m, n ), dtype = np.float )
  
  print ( '' )
  print ( '  COO storage:' )
  print ( '' )
  print ( A )

  print ( '' )
  print ( '  Printed as an array:' )
  print ( '' )
  print ( A.toarray() )

  return

def sparse_test02 ( ):

#*****************************************************************************80
#
## sparse_test02() creates a sparse second difference matrix.
#
#  Discussion:
#
#    This is a nice but very simple example.  
#
#    Note in this example that we define three sparse matrices,
#    SUP, DIAG, and SUB, and then define A as the sum of those matrices.
#
#    However, again, each time we define a sparse matrix, we are assuming
#    we have all the information available at one time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.sparse import spdiags
  from scipy.sparse import coo_matrix
  from scipy.sparse.linalg import spsolve
  import numpy as np

  print ( '' )
  print ( 'sparse_test02():' )
  print ( '  Create a sparse second difference matrix.' )
  print ( '  Solve an associated linear system.' )

  n = 5
#
#  We set up the three diagonals of the -1, 2, -1 matrix.
#
  dm1 = -1.0 * np.ones ( n )
  dia = 2.0 * np.ones ( n )
  dp1 = -1.0 * np.ones ( n )
  data = np.array ( [ dm1, dia, dp1 ] )
  diags = np.array ( [ -1, 0, +1 ] )
  A = spdiags ( data, diags, n, n )

  print ( '' )
  print ( '  Matrix in coo format:' )
  print ( '' )
  print ( A )

  print ( '' )
  print ( '  Matrix as an array:' )
  print ( '' )
  print ( A.toarray() )
#
#  It is necessary to convert A to csc format before using spsolve().
#
  A = A.tocsc ( )
#
#  Set up a right hand side b that defines a linear system whose
#  solution is [ 1, 2, 3, ..., n ].
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
#
#  Solve the sparse linear system.
#
  x = spsolve ( A, b )
#
#  Print the solution.
#
  print ( '' )
  print ( '  Solution to linear system:' )
  print ( '' )
  print ( x )
  
  return

def sparse_test03 ( ):

#*****************************************************************************80
#
## sparse_test03() demonstrates SIZE, NNZ and FIND for sparse matrices.
#
#  Discussion:
#
#    Given a sparse matrix A, the MATLAB functions NNZ, SIZE
#    and FIND can return some interesting information.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.sparse import find, random

  print ( '' )
  print ( 'sparse_test03():' )
  print ( '  Retrieve information about a sparse matrix.' )
#
#  Create a matrix with randomly located nonzeros.
#
  m = 5
  n = 6
  A = random ( m, n, density = 0.25 )

  print ( '' )
  print ( '  Print A:' )
  print ( '' )
  print ( A )

  i, j, V = find ( A )
  nnz = len ( i )
  print ( '' )
  print ( '  Number of nonzeros = ', nnz )

  print ( '' )
  print ( '  (i,j,V) output from find() command:' )
  print ( ( i, j, V ) )

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
  sparse_test ( )
  timestamp ( )

