#! /usr/bin/env python3
#
def i4mat_shortest_path ( n, m ):

#*****************************************************************************80
#
## i4mat_shortest_path() computes the shortest distance between all pairs of points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Floyd,
#    Algorithm 97, Shortest Path,
#    Communications of the ACM,
#    Volume 5, Number 6, June 1962, page 345.
#
#  Input:
#
#    integer N, the number of points.
#
#    integer M(N,N).  M(I,J) contains the length of the direct link between 
#    nodes I and J, or Inf if there is no direct link.
#
#  Output:
#
#    integer M(N,N).  M(I,J) contains the distance between nodes I and J,
#    that is, the length of the shortest path between them.  If there
#    is no such path, then M(I,J) will remain Inf.
#
  import numpy as np

  huge = 2147483647

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( m[j,i] < huge ):
        for k in range ( 0, n ):
          if ( m[i,k] < huge ):
            s = m[j,i] + m[i,k]
            if ( s < m[j,k] ):
              m[j,k] = s

  return m

def i4mat_shortest_path_test ( ):

#*****************************************************************************80
#
## i4mat_shortest_path_test() tests i4mat_shortest_path().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6

  a = np.array ( [ \
    [  0,  2,  5, -1, -1, -1 ], \
    [ -1,  0,  7,  1, -1,  8 ], \
    [ -1, -1,  0,  4, -1, -1 ], \
    [ -1, -1, -1,  0,  3, -1 ], \
    [ -1, -1,  2, -1,  0,  3 ], \
    [ -1,  5, -1,  2,  4,  0 ] ] )

  huge = 2147483647

  print ( '' )
  print ( 'i4mat_shortest_path_test():' )
  print ( '  i4mat_shortest_path() uses Floyd\'s algorithm to find the' )
  print ( '  shortest distance between all pairs of nodes' )
  print ( '  in a directed graph, starting from the initial array' )
  print ( '  of direct node-to-node distances.' )

  print ( '' )
  print ( '  In the initial direct distance array, if' )
  print ( '    A(I,J) = Inf,' )
  print ( '  this indicates there is NO directed link from' )
  print ( '  node I to node J.  In that case, the value of' )
  print ( '  of A(I,J) is essentially "infinity".' )

  print ( '')
  print ( '  Initial direct-link distances:' )
  print ( a )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == -1 ):
        a[i,j] = huge

  a = i4mat_shortest_path ( n, a )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == huge ):
        a[i,j] = -1

  print ( '' )
  print ( '  In the final shortest distance array, if' )
  print ( '    A(I,J) = -1,' )
  print ( '  this indicates there is NO directed path from' )
  print ( '  node I to node J.' )
  print ( '' )
  print ( '  Final distance matrix:' )
  print ( a )

  return

def r8mat_shortest_path ( n, m ):

#*****************************************************************************80
#
## r8mat_shortest_path() computes the shortest distance between all pairs of points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Floyd,
#    Algorithm 97, Shortest Path,
#    Communications of the ACM,
#    Volume 5, Number 6, June 1962, page 345.
#
#  Input:
#
#    integer N, the number of points.
#
#    real M(N,N).  M(I,J) contains the length of the direct link between 
#    nodes I and J, or Inf if there is no direct link.
#
#  Output:
#
#    real M(N,N).  M(I,J) contains the distance between nodes I and J,
#    that is, the length of the shortest path between them.  If there
#    is no such path, then M(I,J) will remain Inf.
#
  import numpy as np

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( m[j,i] < np.inf ):
        for k in range ( 0, n ):
          if ( m[i,k] < np.inf ):
            s = m[j,i] + m[i,k]
            if ( s < m[j,k] ):
              m[j,k] = s

  return m

def r8mat_shortest_path_test ( ):

#*****************************************************************************80
#
## r8mat_shortest_path_test() tests r8mat_shortest_path().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6

  a = np.array ( [ \
    [  0.0,  2.0,  5.0, -1.0, -1.0, -1.0 ], \
    [ -1.0,  0.0,  7.0,  1.0, -1.0,  8.0 ], \
    [ -1.0, -1.0,  0.0,  4.0, -1.0, -1.0 ], \
    [ -1.0, -1.0, -1.0,  0.0,  3.0, -1.0 ], \
    [ -1.0, -1.0,  2.0, -1.0,  0.0,  3.0 ], \
    [ -1.0,  5.0, -1.0,  2.0,  4.0,  0.0 ] ] )
 
  print ( '' )
  print ( 'r8mat_shortest_path_test():' )
  print ( '  r8mat_shortest_path() uses Floyd\'s algorithm to find the' )
  print ( '  shortest distance between all pairs of nodes' )
  print ( '  in a directed graph, starting from the initial array' )
  print ( '  of direct node-to-node distances.' )

  print ( '' )
  print ( '  In the initial direct distance array, if' )
  print ( '    A(I,J) = Inf,' )
  print ( '  this indicates there is NO directed link from' )
  print ( '  node I to node J.  In that case, the value of' )
  print ( '  of A(I,J) is essentially "infinity".' )
  print ( '' )
  print ( '  Initial direct-link distances:' )
  print ( a )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == -1.0 ):
        a[i,j] = np.inf

  a = r8mat_shortest_path ( n, a )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == np.inf ):
        a[i,j] = -1.0

  print ( '' )
  print ( '  In the final shortest distance array, if' )
  print ( '    A(I,J) = -1,' )
  print ( '  this indicates there is NO directed path from' )
  print ( '  node I to node J.' )
  print ( '' )
  print ( '  Final distance matrix:' )
  print ( a )

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

  return None

def toms097_test ( ):

#*****************************************************************************80
#
## toms097_test() tests toms097().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'toms097_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test toms097().' )

  i4mat_shortest_path_test ( )
  r8mat_shortest_path_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms097_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms097_test ( )
  timestamp ( )

