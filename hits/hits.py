#! /usr/bin/env python3
#
def hits_test ( ):

#*****************************************************************************80
#
## hits_test() tests hits().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hits_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  hits() computes the hub and authority scores for nodes' )
  print ( '  in a directed network.' )
#
#  N=4 example.
#
  hits_iteration_test01 ( )
  hits_svd_test01 ( )
#
#  N=5 example.
#
  hits_iteration_test02 ( )
  hits_svd_test02 ( )
#
#  "Small" example.
#
  filename = 'small_sparse.txt'
  hits_iteration_test03 ( filename )
  hits_svd_test03 ( filename )
#
#  "Medium" example.
#
  filename = 'medium_sparse.txt'
  hits_iteration_test03 ( filename )
  hits_svd_test03 ( filename )
#
#  "Large" example.
#
  filename = 'large_sparse.txt'
  hits_iteration_test03 ( filename )
  hits_svd_test03 ( filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'hits_test():' )
  print ( '  Normal end of execution.' )

  return

def hits_iteration ( A, k ):

#*****************************************************************************80
#
## hits_iteration() carries out the HITS algorithm as an iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), the system matrix.
#
#    integer K, the number of iterations.
#
#  Output:
#
#    real AUTH(N), the authority indices.
#
#    real HUB(N), the hub indices.
#
  import numpy as np

  m, n = A.shape
  auth = np.ones ( n )
  hub = np.ones ( m )

  for step in range ( 0, k ):
    
    for j in range ( 0, n ):
      in_nodes = np.nonzero ( A[:,j] )
      auth[j] = np.sum ( hub[in_nodes] )

    auth = auth / np.linalg.norm ( auth )

    for i in range ( 0, m ):
      out_nodes = np.nonzero ( A[i,:] )
      hub[i] = np.sum ( auth[out_nodes] )

    hub = hub / np.linalg.norm ( hub )

  return auth, hub

def hits_iteration_test01 ( ):

#*****************************************************************************80
#
## hits_iteration_test01() applies the HITS iteration to the 4x4 example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hits_iteration_test01():' )
  print ( '  4x4 directed adjacency matrix example' )
  print ( '  Compute authority and hub rankings using HITS iterative algorithm.' )
#
#  Set the adjacency matrix:
#
  A = np.array ( [ \
    [ 0, 1, 1, 1 ], \
    [ 0, 0, 1, 1 ], \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0 ] ] )

  n = 4

  matrix_print ( n, n, A, '  The adjacency matrix' )
#
#  Apply iterative algorithm.
#
  steps = 10
  print ( '' )
  print ( '  The HITS iterative algorithm will use', steps, 'steps.' )
  auth, hub = hits_iteration ( A, steps )

  r8vec2_print ( auth, hub, '  Computed authority and hub vectors' )

  auth2 = np.array ( [ 0.0000, 0.4597, 0.6280, 0.6280 ] )
  hub2 =  np.array ( [ 0.7887, 0.5774, 0.2113, 0.0000 ] )

  r8vec2_print ( auth2, hub2, '  Expected authority and Hub vectors' )

  return

def hits_iteration_test02 ( ):

#*****************************************************************************80
#
## hits_iteration_test02() applies the HITS iteration to the 5x5 example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hits_iteration_test02():' )
  print ( '  5x5 directed adjacency matrix example' )
  print ( '  Compute authority and hub rankings using HITS iterative algorithm.' )
#
#  Set the adjacency matrix:
#
  n = 5
  A = np.array ( [ \
    [ 0, 0, 0, 0, 0 ], \
    [ 1, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 0 ], \
    [ 1, 1, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 0 ] ] )

  matrix_print ( n, n, A, '  The adjacency matrix' )
#
#  Apply the iterative algorithm.
#
  steps = 10
  print ( '' )
  print ( '  The HITS iterative algorithm will use', steps, 'steps', steps )
  auth, hub = hits_iteration ( A, steps )

  r8vec2_print ( auth, hub, '  Computed authority and hub vectors' )

  return

def hits_iteration_test03 ( filename ):

#*****************************************************************************80
#
## hits_iteration_test03() applies the HITS iteration to a sparse matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.sparse import coo_matrix
  import numpy as np

  print ( '' )
  print ( 'hits_iteration_test03():' )
  print ( '  Data read from sparse matrix file "#s"', filename )
  print ( '  Compute authority and hub rankings using HITS iterative algorithm.' )
#
#  Get the adjacency matrix:
#
  i, j, value = np.loadtxt ( filename ).T
  i = i.astype(int) - 1
  j = j.astype(int) - 1
  Asparse = coo_matrix( ( value, (i,j) ) )
  A = Asparse.toarray()

  nonzeros = np.count_nonzero ( A )
  print ( '  Number of nonzero elements = ', nonzeros )

  m, n = A.shape
  print ( '  Number of records m = ', m )
  print ( '  Number of nodes   n = ', n )  
#
#  Apply iterative algorithm.
#
  steps = 30
  print ( '' )
  print ( '  The HITS iterative algorithm will use', steps, 'steps.' )
  auth, hub = hits_iteration ( A, steps )

  r8vec2_print ( auth, hub, '  Computed authority and hub vectors' )

  return

def hits_svd ( A ):

#*****************************************************************************80
#
## hits_svd() uses the singular value decomposition (SVD) for the HITS algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), the system matrix.
#
#  Output:
#
#    real AUTH(N), the authority indices.
#
#    real HUB(N), the hub indices.
#
  import numpy as np

  U, S, V = np.linalg.svd ( A )
  hub = np.abs ( U[:,0] )
  auth = np.abs ( V[0,:] )

  return auth, hub

def hits_svd_test01 ( ):

#*****************************************************************************80
#
## hits_svd_test01() applies the HITS SVD algorithm to the 4x4 example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hits_svd_test01():' )
  print ( '  4x4 directed adjacency matrix example' )
  print ( '  Compute authority and hub rankings using HITS SVD algorithm.' )
#
#  Set the adjacency matrix:
#
  A = np.array ( [ \
    [ 0, 1, 1, 1 ], \
    [ 0, 0, 1, 1 ], \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0 ] ] )

  n = 4

  matrix_print ( n, n, A, '  The adjacency matrix' )
#
#  Apply the SVD algorithm.
#
  auth, hub = hits_svd ( A )

  r8vec2_print ( auth, hub, '  Computed authority and hub vectors' )

  auth2 = np.array ( [ 0.0000, 0.4597, 0.6280, 0.6280 ] )
  hub2 =  np.array ( [ 0.7887, 0.5774, 0.2113, 0.0000 ] )

  r8vec2_print ( auth2, hub2, '  Expected authority and Hub vectors' )

  return

def hits_svd_test02 ( ):

#*****************************************************************************80
#
## hits_svd_test02() applies the HITS SVD algorithm to the 5x5 example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hits_svd_test02():' )
  print ( '  5x5 directed adjacency matrix example' )
  print ( '  Compute authority and hub rankings using HITS SVD algorithm.' )
#
#  Set the adjacency matrix:
#
  A = np.array ( [ \
    [ 0, 0, 0, 0, 0 ], \
    [ 1, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 0 ], \
    [ 1, 1, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 0 ] ] )

  n = 5

  matrix_print ( n, n, A, '  The adjacency matrix' )
#
#  Apply the SVD algorithm.
#
  auth, hub = hits_svd ( A )

  r8vec2_print ( auth, hub, '  Computed authority and hub vectors' )

  return

def hits_svd_test03 ( filename ):

#*****************************************************************************80
#
## hits_svd_test03() applies the HITS SVD algorithm to a sparse matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.sparse import coo_matrix
  import numpy as np

  print ( '' )
  print ( 'hits_svd_test03():' )
  print ( '  Data read from sparse matrix file "' + filename + '"' )
  print ( '  Compute authority and hub rankings using HITS SVD algorithm.' )
#
#  Get the adjacency matrix:
#
  i, j, value = np.loadtxt ( filename ).T
  i = i.astype(int) - 1
  j = j.astype(int) - 1
  Asparse = coo_matrix( ( value, (i,j) ) )
# A = Asparse.todense()
  A = Asparse.toarray()

  nonzeros = np.count_nonzero ( A )
  print ( '  Number of nonzero elements = ', nonzeros )

  m, n = A.shape
  print ( '  Number of records m = ', m )
  print ( '  Number of nodes   n = ', n )  
#
#  Apply the SVD algorithm.
#
  auth, hub = hits_svd ( A )

  r8vec2_print ( auth, hub, '  Computed authority and hub vectors' )

  return

def matrix_print ( m, n, A, label ):

#*****************************************************************************80
#
## matrix_print() prints a matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the dimensions of the matrix.
#
#    real A(M,N), the matrix values.
#
#    character LABEL, a label for the data.
#
  print ( '' )
  print ( label )
  print ( '' )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      print ( '%8.4f' % ( A[i,j] ), end = '' )
    print ( '' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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
  hits_test ( )
  timestamp ( )

