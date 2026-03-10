#! /usr/bin/env python3
#
def digraph_adj_test ( ):

#*****************************************************************************80
#
## digraph_adj_test() tests digraph_adj().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'digraph_adj_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test digraph_adj().' )

  abc_adjacency_test ( )
  abcd_adjacency_test ( )
  five_adjacency_test ( )
  adjacency_to_google_test ( )
  adjacency_to_transition_test ( )
  moler_adjacency_test ( )
  sauer_adjacency_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'digraph_adj_test():' )
  print ( '  Normal end of execution.' )

  return

def abc_adjacency ( ):

#*****************************************************************************80
#
## abc_adjacency() sets up the adjacency matrix associated with a network.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(3,3): an adjacency matrix.
#
  import numpy as np

  A = np.array ( [ \
    [ 0, 1, 0 ], \
    [ 0, 0, 1 ], \
    [ 1, 0, 0 ] ] )

  return A

def abc_adjacency_test ( ):

#*****************************************************************************80
#
## abc_adjacency_test() tests abc_adjacency().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'abc_adjacency_test():' )
  print ( '  Test abc_adjacency ()' )

  A = abc_adjacency ( )

  print ( '' )
  print ( '  "abc" adjacency matrix A:' )
  print ( A )

  return

def abcd_adjacency ( ):

#*****************************************************************************80
#
## abcd_adjacency () sets up the adjacency matrix associated with a network.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(4,4): an adjacency matrix.
#
  import numpy as np

  A = np.array ( [ \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0 ], \
    [ 1, 0, 0, 1 ], \
    [ 1, 0, 0, 0 ] ] )

  return A

def abcd_adjacency_test ( ):

#*****************************************************************************80
#
## abcd_adjacency_test() tests abcd_adjacency ().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'abcd_adjacency_test():' )
  print ( '  Test abcd_adjacency()' )

  A = abcd_adjacency ( )

  print ( '' )
  print ( '  "abcd" adjacency matrix A:' )
  print ( A )

  return

def five_adjacency ( ):

#*****************************************************************************80
#
## five_adjacency () sets up the adjacency matrix associated with a network.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(5,5): an adjacency matrix.
#
  import numpy as np

  A = np.array ( [ \
    [ 0, 1, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 1 ], \
    [ 1, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0 ] ] )

  return A

def five_adjacency_test ( ):

#*****************************************************************************80
#
## five_adjacency_test() tests five_adjacency ().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'five_adjacency_test():' )
  print ( '  Test five_adjacency ()' )

  A = five_adjacency ( )

  print ( '' )
  print ( '  "five" adjacency matrix A:' )
  print ( A )

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
#    24 February 2023
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
#    real G(N,N): the Google matrix.
#
  import numpy as np

  n = A.shape[0]

  s = np.sum ( A, axis = 1 )

  p = 0.15

  G = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    if ( s[i] == 0.0 ):
      G[i,:] = 1.0 / n
    else:
      G[i,:] = ( 1.0 - p ) * A[i,:] / s[i] + p / n

  G = np.transpose ( G )

  return G

def adjacency_to_google_test ( ):

#*****************************************************************************80
#
## adjacency_to_google_test() tests adjacency_to_google().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'adjacency_to_google_test():' )
  print ( '  Test adjacency_to_google()' )

  A = np.array ( [ \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0 ], \
    [ 1, 0, 0, 1 ], \
    [ 1, 0, 0, 0 ] ] )

  print ( '' )
  print ( '  adjacency matrix A:' )
  print ( A )

  G = adjacency_to_google ( A )

  print ( '' )
  print ( '  Google transition matrix G:' )
  print ( G )

  return

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
#    25 February 2023
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
#
#  Get the number of variables.
#
  n = A.shape[0]
#
#  Get the row sums.
#
  s = np.sum ( A, axis = 1 )
#
#  Allocate T.
#
  T = np.zeros ( [ n, n ] )
#
#  Normalize each row so it sums to 1.
#
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

def adjacency_to_transition_test ( ):

#*****************************************************************************80
#
## adjacency_to_transition_test() tests adjacency_to_transition().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'adjacency_to_transition_test():' )
  print ( '  Test adjacency_to_transition()' )

  A = np.array ( [ \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0 ], \
    [ 1, 0, 0, 1 ], \
    [ 1, 0, 0, 0 ] ] )

  print ( '' )
  print ( '  adjacency matrix A:' )
  print ( A )

  T = adjacency_to_transition ( A )

  print ( '' )
  print ( '  Transition matrix T:' )
  print ( T )

  return

def moler_adjacency ( ):

#*****************************************************************************80
#
## moler_adjacency () returns the adjacency matrix for Moler's example 3.
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
#    24 February 2023
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

  A = np.array ( [ \
    [ 0, 1, 0, 0, 0, 1 ], \
    [ 0, 0, 1, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 1, 1 ], \
    [ 1, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 1, 0 ], \
    [ 1, 0, 0, 0, 0, 0 ] ] )

  return A

def moler_adjacency_test ( ):

#*****************************************************************************80
#
## moler_adjacency_test() tests moler_adjacency ().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'moler_adjacency_test():' )
  print ( '  Test moler_adjacency ()' )

  A = moler_adjacency ( )

  print ( '' )
  print ( '  Moler adjacency matrix A:' )
  print ( A )

  return

def sauer_adjacency ( ):

#*****************************************************************************80
#
## sauer_adjacency () sets up the adjacency matrix associated with a network.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Timothy Sauer,
#    "How search engines rate page quality",
#    Numerical Analysis,
#    Pearson, 2006.
#    ISBN: 0-321-2698-9,
#    LC: QA297.S348
#
#  Output:
#
#    real A(15,15): an adjacency matrix.
#
  import numpy as np

  A = np.array ( [ \
    [ 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ], \
    [ 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ] ] )

  return A

def sauer_adjacency_test ( ):

#*****************************************************************************80
#
## sauer_adjacency_test() tests sauer_adjacency ().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'sauer_adjacency_test():' )
  print ( '  Test sauer_adjacency ()' )

  A = sauer_adjacency ( )

  print ( '' )
  print ( '  Sauer adjacency matrix A:' )
  print ( A )

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
#    06 April 2013
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
  digraph_adj_test ( )
  timestamp ( )

