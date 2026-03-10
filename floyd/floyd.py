#! /usr/bin/env python3
#
def floyd_test ( ):

#*****************************************************************************80
#
## floyd_test() tests floyd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'floyd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test floyd().' )

  floyd_test01 ( )
  floyd_test02 ( )
  floyd_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'floyd_test():' )
  print ( '  Normal end of execution.' )
  return

def floyd ( A ):

#*****************************************************************************80
#
## floyd() finds the shortest distances between pairs of nodes in a directed graph.
#
#  Discussion:
#
#    We assume we are given the adjacency matrix A of the directed graph.
#
#    The adjacency matrix is NOT assumed to be symmetric.
#
#    If there is not a direct link from node I to node J, the distance
#    would formally be infinity.  We assume that such distances are assigned
#    the value INF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N,N), the one-step distance from node I to node J.
#
#  Output:
#
#    real B(N,N), the shortest total distance from node I to node J.
#
  n = A.shape[0]
  B = A.copy ( )

  for k in range ( 0, n ):
    for j in range ( 0, n ):
      for i in range ( 0, n ):
        B[i,j] = min ( B[i,j], B[i,k] + B[k,j] )

  return B

def floyd_test01 ( ):

#*****************************************************************************80
#
## floyd_test01() tests floyd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'floyd_test01():' )
  print ( '  floyd() uses Floyd''s algorithm to find the' )
  print ( '  shortest distance between all pairs of nodes' )
  print ( '  in a directed graph, starting from the initial array' )
  print ( '  of direct node-to-node distances.' )

  n = 6

  A = np.array ( [ \
    [  0.0,    2.0,    5.0,   np.Inf, np.Inf, np.Inf ], \
    [ np.Inf,  0.0,    7.0,    1.0,   np.Inf,  8.0   ], \
    [ np.Inf, np.Inf,  0.0,    4.0,   np.Inf, np.Inf ], \
    [ np.Inf, np.Inf, np.Inf,  0.0,    3.0,   np.Inf ], \
    [ np.Inf, np.Inf,  2.0,   np.Inf,  0.0,    3.0   ], \
    [ np.Inf,  5.0,   np.Inf,  2.0,    4.0,    0.0   ] ] )

  print ( '' )
  print ( '  Node-to-node one-step distance array A:' )
  print ( A )

  B = floyd ( A )

  print ( '  Node-to-node shortest total distance array B:' )
  print ( B )

  return

def floyd_test02 ( ):

#*****************************************************************************80
#
## floyd_test02() applies Floyd's algorithm to matrices of increasing size.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'floyd_test02():' )
  print ( '  Test floyd() on matrices of increasing order N.' )
  print ( '  The work is roughly N^3.' )
  print ( '')
  print ( '         N   Time (seconds)  Time/N^3' )
  print ( '' )

  n = 1
  while ( n <= 256 ):
    wtime = floyd_test02_sub ( n )
    print ( '  %8d  %12f  %12f' % ( n, wtime, 1000000.0 * wtime / n**3 ) )
    n = n * 2

  return

def floyd_test02_sub ( n ):

#*****************************************************************************80
#
## floyd_test02_sub() tests floyd().
#
#  Discussion:
#
#    The matrix size is input by the user.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the matrix.
#
#  Output:
#
#    real WTIME, the wall clock time required by FLOYD.
#
  from numpy.random import default_rng
  from time import time
  import numpy as np

  rng = default_rng ( )

  A = rng.integers ( low = 1, high = 2, size = [ n, n ], endpoint = True )
  A = A - np.diag ( np.diag ( A ) )
  i1 = np.where ( A == 2 )
  A = A.astype ( float )
  A[i1] = np.Inf

  wtime = time ( )

  B = floyd ( A )

  wtime = time ( ) - wtime

  return wtime

def floyd_test03 ( ):

#*****************************************************************************80
#
## floyd_test03() uses Floyd's method for a triangulation.
#
#  Discussion:
#
#     8  41--42--43--44  45--46--47--48
#     |   | \ | \ | \ |   | \ | \ | \ |
#     7  33--34--35--36  37--38--39--40
#     |   | \ |                   | \ |
#     6  29--30                  31--32
#     |   | \ |                   | \ |
#     5  25--26                  27--28
#     |   | \ |                   | \ |
#     4  21--22                  23--24
#     |   | \ |                   | \ |
#     3  17--18                  19--20
#     |   | \ |                   | \ |
#     2   9--10--11--12--13--14--15--16
#     |   | \ | \ | \ | \ | \ | \ | \ |
#     1   1---2---3---4---5---6---7---8
#     |    
#     +---1---2---3---4---5---6---7---8
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'floyd_test03()' )
  print ( '  floyd() starts with the adjacency matrix A of a' )
  print ( '  triangulation, determines the pairwise distance matrix B.' )

  element_num = 46
  node_num = 48
#
#  element_node entries are 1-based, and so will have to be decremented when used.
#
  element_node = np.array ( [ \
    [  1,  2,  9 ], \
    [  2, 10,  9 ], \
    [  2,  3, 10 ], \
    [  3, 11, 10 ], \
    [  3,  4, 11 ], \
    [  4, 12, 11 ], \
    [  4,  5, 12 ], \
    [  5, 13, 12 ], \
    [  5,  6, 13 ], \
    [  6, 14, 13 ], \
    [  6,  7, 14 ], \
    [  7, 15, 14 ], \
    [  7,  8, 15 ], \
    [  8, 16, 15 ], \
    [  9, 10, 17 ], \
    [ 10, 18, 17 ], \
    [ 15, 16, 19 ], \
    [ 16, 20, 19 ], \
    [ 17, 18, 21 ], \
    [ 18, 22, 21 ], \
    [ 19, 20, 23 ], \
    [ 20, 24, 23 ], \
    [ 21, 22, 25 ], \
    [ 22, 26, 25 ], \
    [ 23, 24, 27 ], \
    [ 24, 28, 27 ], \
    [ 25, 26, 29 ], \
    [ 26, 30, 29 ], \
    [ 27, 28, 31 ], \
    [ 28, 32, 31 ], \
    [ 29, 30, 33 ], \
    [ 30, 34, 33 ], \
    [ 31, 32, 39 ], \
    [ 32, 40, 39 ], \
    [ 33, 34, 41 ], \
    [ 34, 42, 41 ], \
    [ 34, 35, 42 ], \
    [ 35, 43, 42 ], \
    [ 35, 36, 43 ], \
    [ 36, 44, 43 ], \
    [ 37, 38, 45 ], \
    [ 38, 46, 45 ], \
    [ 38, 39, 46 ], \
    [ 39, 47, 46 ], \
    [ 39, 40, 47 ], \
    [ 40, 48, 47 ] ] )

  xy = np.array ( [ \
    [ 1.0, 1.0 ], \
    [ 2.0, 1.0 ], \
    [ 3.0, 1.0 ], \
    [ 4.0, 1.0 ], \
    [ 5.0, 1.0 ], \
    [ 6.0, 1.0 ], \
    [ 7.0, 1.0 ], \
    [ 8.0, 1.0 ], \
    [ 1.0, 2.0 ], \
    [ 2.0, 2.0 ], \
    [ 3.0, 2.0 ], \
    [ 4.0, 2.0 ], \
    [ 5.0, 2.0 ], \
    [ 6.0, 2.0 ], \
    [ 7.0, 2.0 ], \
    [ 8.0, 2.0 ], \
    [ 1.0, 3.0 ], \
    [ 2.0, 3.0 ], \
    [ 7.0, 3.0 ], \
    [ 8.0, 3.0 ], \
    [ 1.0, 4.0 ], \
    [ 2.0, 4.0 ], \
    [ 7.0, 4.0 ], \
    [ 8.0, 4.0 ], \
    [ 1.0, 5.0 ], \
    [ 2.0, 5.0 ], \
    [ 7.0, 5.0 ], \
    [ 8.0, 5.0 ], \
    [ 1.0, 6.0 ], \
    [ 2.0, 6.0 ], \
    [ 7.0, 6.0 ], \
    [ 8.0, 6.0 ], \
    [ 1.0, 7.0 ], \
    [ 2.0, 7.0 ], \
    [ 3.0, 7.0 ], \
    [ 4.0, 7.0 ], \
    [ 5.0, 7.0 ], \
    [ 6.0, 7.0 ], \
    [ 7.0, 7.0 ], \
    [ 8.0, 7.0 ], \
    [ 1.0, 8.0 ], \
    [ 2.0, 8.0 ], \
    [ 3.0, 8.0 ], \
    [ 4.0, 8.0 ], \
    [ 5.0, 8.0 ], \
    [ 6.0, 8.0 ], \
    [ 7.0, 8.0 ], \
    [ 8.0, 8.0 ] ] )
#
#  Decrement the element array.
#
  element_node = element_node - 1
#
#  Initialize distance array to Inf, with 0 diagonal.
#
  A = np.Inf * np.ones ( [ node_num, node_num ] )
#
#  Self distance is 0.
#
  for i in range ( 0, node_num ):
    A[i,i] = 0.0
#
#  Initialize A(i,j) to the one-step distance.
#  That is, if nodes i and j both occur in a common triangle,
#  compute the distance between them.
#
  for element in range ( 0, element_num ):
    n1 = element_node[element,2]
    for i in range ( 0, 3 ):
      n2 = element_node[element,i]
      A[n1,n2] = np.linalg.norm ( xy[n1,:] - xy[n2,:] )
      A[n2,n1] = A[n1,n2]
      n1 = n2

  print ( '  One-step distance matrix:' )
  print ( A )
#
#  Update D to the N-1 step distance.
#
  B = floyd ( A )

  print ( '  Floyd distance matrix:' )
  print ( B )
#
#  We can plot the distance function over the triangulated region.
#
  base = 20
  plt.tricontourf ( xy[:,0], xy[:,1], element_node, B[base-1,:] )
  plt.colorbar ( )
  plt.title ( 'Distance from node' + str ( base ) )
  filename = 'floyd_test03.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

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
  floyd_test ( )
  timestamp ( )


