#! /usr/bin/env python3
#
def pagerank_test ( ):

#*****************************************************************************80
#
## pagerank_test() tests pagerank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pagerank_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  pagerank() demonstrates several page rank algorithms.' )

  for test in range ( 0, 5 ):
    print ( '' )
    print ( '  Test', test )
    if ( test == 0 ):
      label = '5 node MacCormick example with a cycle'
      A = mac1_inc ( )
      header = 'mac1'
    elif ( test == 1 ):
      label = '16 node MacCormick example'
      n = 16
      A = mac2_inc ( )
      header = 'mac2'
    elif ( test == 2 ):
      label = '6 node Moler example'
      A = moler_inc ( )
      header = 'moler'
    elif ( test == 3 ):
      label = '6 node example'
      A = six_inc ( )
      header = 'six'
    elif ( test == 4 ):
      label = '15 node Sauer example'
      A = sauer_inc ( )
      header = 'sauer'

    print ( label )
    print ( '  adjacency matrix A:' )
    print ( A )
    T = adjacency_to_transition ( A )
    print ( '  Transition matrix T:' )
    print ( T )
#
#  Plot the directed graph.
#
    digraph_plot ( A, header )
#
#  Compute the rankings.
#
    it_num = 100
    google_rank ( A, it_num )

    it_num = 100
    power_rank ( A, it_num )

    it_num = 10000
    surf_rank ( A, it_num )
#
#  Terminate.
#
  print ( '' )
  print ( 'pagerank_test():' )
  print ( '  Normal end of execution.' )

  return

def digraph_plot ( A, header ):

#*****************************************************************************80
#
## digraph_plot() plots a directed graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N): the adjacency matrix.
#
#    string header: the prefix to be used for the comment, 
#    dot filename, and png filename.
#
  from graphviz import Digraph

  dot = Digraph ( comment = header, format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  n = A.shape[0]

  for i in range ( 0, n ):
    code = str ( i )
    label = str ( i )
    dot.node ( code, label )
#
#  Specify the edges as connections between two nodes.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( A[i,j] ):
         dot.edge ( str ( i ), str ( j ) )

  print ( dot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
  filename = header + '.dot'
  dot.render ( filename, view = False )

  filename = header + '.png'
  print ( '  Graphics saved as "' + filename + '"' )

  return

def google_matrix ( A, p = 0.15 ):

#*****************************************************************************80
#
## google_matrix() converts an adjacency matrix to a Google transition matrix.
#
#  Discussion:
#
#    If the adjacency matrix has a node I with no connectivity,
#    (A(I,1:N) = 0) then we artificially set G(1:N,I)=1/N, so that
#    the transition matrix property of having unit column sums is preserved.
#
#    For nodes with connectivity, we assume that 85 percent of the time
#    we will take a link at random, and 15 percent of the time, we will
#    jump to an arbitrary link.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N): the adjacency matrix.
#
#    real P: the probability that the user will simply jump to a random
#    web page. Default = 0.15
#
#  Output:
#
#    real G(N,N): the Google matrix.
#
  import numpy as np

  n = A.shape[0]
#
#  Compute the row sums of A.
#  s(i) is the number of links on web page i.
#
  s = np.sum ( A, axis = 1 )
#
#  Allocate G.
#
  G = np.zeros ( [ n, n ] )
#
#  Fill any zero row with 1/n.
#
  for i in range ( 0, n ):
    if ( s[i] == 0.0 ):
      G[i,:] = 1.0 / n
    else:
      G[i,:] = ( 1.0 - p ) * A[i,:] / s[i] + p / n
#
#  Transpose so the matrix is a transition/stochastic matrix.
#
  G = np.transpose ( G )

  return G

def google_rank ( A, it_num ):

#*****************************************************************************80
#
## google_rank() uses the power method on the Google matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N): the adjacency matrix.
#
#    integer it_num: the number of iterations to take.
#
  import numpy as np

  print ( '' )
  print ( 'google_rank():' )
  print ( '  Given an NxN adjacency matrix A,' )
  print ( '  compute the Google matrix G,' )
  print ( '  Then start with a vector of N values 1/N,' )
  print ( '  and repeatedly compute x <= G*x' )
  print ( '' )
  print ( '  After many steps, compare last three iterates.' )
  print ( '  If they are close, we are probably at an eigenvector' )
  print ( '  associated with the eigenvalue 1.' )

  n = A.shape[0]
#
#  Compute the Google matrix.
#
  G = adjacency_to_google ( A )

  print ( '' )
  print ( '  x -> G*x -> G*G*x' )
#
#  Carry out many iterations.
#  Normalization is not necessary because G is a transition matrix.
#
  for i in range ( 0, it_num + 1 ):

    if ( i == 0 ):
      x = np.ones ( n ) / n
    else:
      x = np.matmul ( G, x )
#
#  Compare three successive iterates.
#
  Gx = np.matmul ( G, x )
  GGx = np.matmul ( G, Gx )

  Output = np.column_stack ( [ x, Gx, GGx ] )
  print ( '' )
  print ( '  x, G*x, G*G*x' )
  print ( Output )

  return

def adjacency_to_google ( A ):

#*****************************************************************************80
#
## adjacency_to_google() converts an adjacency matrix to a Google transition matrix.
#
#  Discussion:
#
#    If the input adjacency matrix has a node I with no connectivity,
#    (A(I,1:N) = 0) then we artificially set T(1:N,I)=1/N, so that
#    the transition matrix property of having unit column sums is preserved.
#
#    For nodes with connectivity, we assume that 85 percent of the time
#    we will take a link at random, and 15 percent of the time, we will
#    jump to an arbitrary link.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N): the adjacency matrix.
#
#  Output:
#
#    real T(N,N): the transition matrix.
#
  import numpy as np

  n = A.shape[0]

  T = np.zeros ( [ n, n ] )

  s = np.sum ( A, axis = 1 )

  for i in range ( 0, n ):
    if ( s[i] == 0.0 ):
      T[i,:] = 1.0 / n
    else:
      T[i,:] = 0.85 * A[i,:] / s[i] + 0.15 / n

  T = np.transpose ( T )

  return T

def adjacency_to_transition ( A ):

#*****************************************************************************80
#
## adjacency_to_transition() converts an adjacency matrix to a transition matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N), the adjacency matrix.
#
#  Output:
#
#    real T(N,N): the transition matrix.
#
  import numpy as np

  n = A.shape[0]
#
#  Get the row sums.
#
  s = np.sum ( A, axis = 1 )
#
#  Normalize each row so it sums to 1.
#
  T = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    if ( s[i] != 0.0 ):
      T[i,:] = A[i,:] / s[i]
    else:
      T[i,i] = 1.0
#
#  Transpose the matrix.
#
  T = np.transpose ( T )

  return T

def mac1_inc ( ):

#*****************************************************************************80
#
## mac1_inc() returns the adjacency matrix for MacCormick's example 1.
#
#  Discussion:
#
#    This matrix appears on page 35 of the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John MacCormick,
#    Nine Algorithms That Changed the Future: The Ingenious Ideas that 
#    Drive Today's Computers,
#    Princeton University Press,
#    ISBN-13: 978-0691158198.
#
#  Output:
#
#    integer A(5,5), the adjacency matrix.
#
  import numpy as np

  A = np.zeros ( [ 5, 5 ] )

  A[0,1] = 1.0
  A[1,4] = 1.0
  A[2,0] = 1.0
  A[3,0] = 1.0
  A[4,0] = 1.0

  return A

def mac2_inc ( ):

#*****************************************************************************80
#
## mac_inc2() returns the adjacency matrix for MacCormick's example 2.
#
#  Discussion:
#
#    This matrix appears on page 33 of the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John MacCormick,
#    Nine Algorithms That Changed the Future: The Ingenious Ideas that 
#    Drive Today's Computers,
#    Princeton University Press,
#    ISBN-13: 978-0691158198.
#
#  Output:
#
#    integer A(16,16), the adjacency matrix.
#
  import numpy as np

  A = np.zeros ( [ 16, 16 ] )

  A[0,1] = 1.0
  A[0,2] = 1.0
  A[0,5] = 1.0
  A[1,3] = 1.0
  A[2,3] = 1.0
  A[2,4] = 1.0
  A[3,4] = 1.0
  A[4,6] = 1.0
  A[4,7] = 1.0
  A[5,4] = 1.0
  A[5,6] = 1.0
  A[6,14] = 1.0
  A[7,6] = 1.0
  A[7,8] = 1.0
  A[7,9] = 1.0
  A[8,9] = 1.0
  A[9,6] = 1.0
  A[9,10] = 1.0
  A[9,11] = 1.0
  A[9,12] = 1.0
  A[9,13] = 1.0
  A[10,14] = 1.0
  A[11,14] = 1.0
  A[12,14] = 1.0
  A[13,14] = 1.0
  A[14,15] = 1.0
  A[15,0] = 1.0

  return A

def moler_inc ( ):

#*****************************************************************************80
#
## moler_inc() returns the adjacency matrix for a network of Moler.
#
#  Discussion:
#
#    This matrix appears on page 5 of the reference.
#
#    We added a self-link for node 5, which otherwise has no outlinks.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Experiments with Matlab,
#    Chapter 7: Google PageRank,
#    https://www.mathworks.com/moler/exm/chapters/pagerank.pdf
#
#  Output:
#
#    integer A(6,6), the adjacency matrix.
#
  import numpy as np

  A = np.zeros ( [ 6, 6 ] )

  A[0,1] = 1.0
  A[0,5] = 1.0
  A[1,2] = 1.0
  A[1,3] = 1.0
  A[2,3] = 1.0
  A[2,4] = 1.0
  A[2,5] = 1.0
  A[3,0] = 1.0
  A[4,4] = 1.0
  A[5,0] = 1.0

  return A

def power_rank ( A, it_num ):

#*****************************************************************************80
#
## power_rank() uses the power method to seek an eigenvector of a directed graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N): the adjacency matrix.
#
#    integer it_num: the number of iterations to take.
#
  import numpy as np

  print ( '' )
  print ( 'power_rank():' )
  print ( '  Given an NxN adjacency matrix A,' )
  print ( '  compute the transition matrix T,' )
  print ( '  Then start with a vector of N values 1/N,' )
  print ( '  and repeatedly compute x <= T*x' )
  print ( '' )
  print ( '  After many steps, compare last three iterates.' )
  print ( '  If they are close, we are probably at an eigenvector' )
  print ( '  associated with the eigenvalue 1.' )

  n = A.shape[0]
#
#  Compute the transition matrix.
#
  T = adjacency_to_transition ( A )
#
#  Carry out many iterations.
#  Normalization is not necessary because T is a transition matrix.
#
  for i in range ( 0, it_num + 1 ):

    if ( i == 0 ):
      x = np.ones ( n ) / n
    else:
      x = np.matmul ( T, x )
#
#  Compare three successive iterates.
#
  Tx = np.matmul ( T, x )
  TTx = np.matmul ( T, Tx )

  Output = np.column_stack ( [ x, Tx, TTx ] )
  print ( '' )
  print ( '  x -> T*x -> T*T*x' )
  print ( Output )

  return

def sauer_inc ( ):

#*****************************************************************************80
#
## sauer_inc() returns the adjacency matrix for the Sauer example.
#
#  Discussion:
#
#    This matrix appears on page 564 of the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Timothy Sauer,
#    Numerical Analysis,
#    Pearson, 2006,
#    ISBN: 0-321-26898-9,
#    LC: QA297.S348
#
#  Output:
#
#    integer A(15,15): the adjacency matrix.
#
  import numpy as np

  A = np.zeros ( [ 15, 15 ] )

  A[0,1] = 1
  A[0,8] = 1
  A[1,2] = 1
  A[1,4] = 1
  A[1,6] = 1
  A[2,1] = 1
  A[2,5] = 1
  A[2,7] = 1
  A[3,2] = 1
  A[3,11] = 1
  A[4,0] = 1
  A[4,9] = 1
  A[5,9] = 1
  A[5,10] = 1
  A[6,9] = 1
  A[6,10] = 1
  A[7,3] = 1
  A[7,10] = 1
  A[8,4] = 1
  A[8,5] = 1
  A[8,9] = 1
  A[9,12] = 1
  A[10,14] = 1
  A[11,6] = 1
  A[11,7] = 1
  A[11,10] = 1
  A[12,8] = 1
  A[12,13] = 1
  A[13,9] = 1
  A[13,10] = 1
  A[13,12] = 1
  A[13,14] = 1
  A[14,11] = 1
  A[14,13] = 1

  return A

def six_inc ( ):

#*****************************************************************************80
#
## six_inc() returns the adjacency matrix for a 6-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(6,6), the adjacency matrix.
#
  import numpy as np

  A = np.zeros ( [ 6, 6 ] )

  A[0,1] = 1.0
  A[1,2] = 1.0
  A[1,4] = 1.0
  A[2,0] = 1.0
  A[2,3] = 1.0
  A[3,0] = 1.0
  A[4,1] = 1.0
  A[4,5] = 1.0
  A[5,3] = 1.0

  return A

def surf_rank ( A, it_num ):

#*****************************************************************************80
#
## surf_rank() uses the "random surfer" method for node rankings of a digraph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N,N): the adjacency matrix.
#
#    integer it_num: the number of iterations to take.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'surf_rank():' )
  print ( '  Given an NxN adjacency matrix A,' )
  print ( '  compute the transition matrix T,' )
  print ( '  and then repeatedly visit nodes, keeping track of' )
  print ( '  how often you visited.' )
  print ( '' )
  print ( '  15 per cent of the time, simply take a random jump to a node.' )
  print ( '  The rest of the time, follow a random link from the current node.' )
  print ( '' )
  print ( '  When done, the node weight is the number of visits' )
  print ( '  normalized by the total number of visits.' )

  n = A.shape[0]

  v = np.zeros ( n )
#
#  Get the transition matrix from the adjacency matrix.
#
  T = adjacency_to_transition ( A )
#
#  Carry out many moves.
#
  for k in range ( 0, it_num ):

    if ( k == 0 ):

      j = rng.integers ( low = 0, high = n, endpoint = False )

    else:

      p1 = rng.random ( )
      q1 = 0.15

      if ( p1 <= q1 ):

        j = rng.integers ( low = 0, high = n, endpoint = False )

      else:

        p2 = rng.random ( )
        q2 = 0.0
        for i in range ( 0, n ):
          q2 = q2 + T[i,j]
          if ( p2 <= q2 ):
            j = i
            break
 
    v[j] = v[j] + 1
#
#  Normalize the counts.
#
  index = list ( range ( 0, n ) )
  weight = v / it_num

  Output = np.column_stack ( [ index, v, weight ] )
  print ( '' )
  print ( '  index, count, weight' )
  print ( Output )

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
  pagerank_test ( )
  timestamp ( )

