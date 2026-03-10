#! /usr/bin/env python3
#
def graph_dist_test ( ):

#*****************************************************************************80
#
## graph_dist_test() tests graph_dist().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'graph_dist_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test graph_dist(), which implements graph algorithms.' )

  graph_dist_all_test ( )
  graph_dist_check_test ( )
  graph_dist_min_span_tree_test ( )
  graph_dist_min_span_tree_alternate_test ( )
  graph_dist_min_span_tree2_test ( )
  graph_dist_min_span_tree3_test ( )
  graph_dist_one_test ( )
  graph_dist_pairing_greedy_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'graph_dist_test():' )
  print ( '  Normal end of execution.' )

  return

def graph_arc_weight_print ( nedge, inode, jnode, wnode, title ):

#*****************************************************************************80
#
## graph_arc_weight_print() prints out a weighted graph from an edge list.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NEDGE, the number of edges.
#
#    integer INODE(NEDGE), JNODE(NEDGE), the beginning
#    and end nodes of the edges.
#
#    real WNODE(NEDGE), the weights of the edges.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )

  for i in range ( 0, nedge ):
    print ( '%8d    %8d%8d  %g' % ( i, inode[i], jnode[i], wnode[i] ) )

  return

def graph_dist_all ( dist, nnode ):

#*****************************************************************************80
#
## graph_dist_all() finds the distance from every node to every other node.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Gibbons,
#    Algorithmic Graph Theory,
#    Cambridge University Press, 1985,
#    ISBN 0-521-28881-9.
#
#  Input:
#
#    real DIST(NNODE,NNODE).
#    DIST(I,J) is the length of the edge FROM node I TO node J.
#    DIST(I,J) = Inf if there is no direct edge from I to J.
#
#    integer NNODE, the number of nodes.
#
#  Output:
#
#    real PATH_DIST(NNODE,NNODE).  This array contains the
#    lengths of the shortest paths from each node to another node.
#    PATH_DIST(I,J) is the length of the shortest path from node I
#    to node J.  If PATH_DIST(I,J) = Inf, there is no path from node
#    I to node J.
#
  import numpy as np

  path_dist = np.zeros ( [ nnode, nnode ] )

  for k in range ( 0, nnode ):

    for i in range ( 0, nnode ):
      for j in range ( 0, nnode ):

        path_dist[i,j] = dist[i,j]

        if ( ( dist[i,k] != np.inf ) and ( dist[k,j] != np.inf ) ):

          path_dist[i,j] = min ( path_dist[i,j], dist[i,k] + dist[k,j] )
#
#  Update the distance array.
#
    dist = path_dist.copy()

  return path_dist

def graph_dist_all_test ( ):

#*****************************************************************************80
#
## graph_dist_all_test() tests graph_dist_all().
#
#  The graph is:
#
#  N3 --3-- N2 --4-- N4 --5-- N5
#
#     \      |      /
#       6    2     1
#        \   |    /
#
#            N1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'graph_dist_all_test():' )
  print ( '  graph_dist_all() computes the distance between' )
  print ( '  all pairs of nodes.' )
  print ( '' )

  nnode = 5
 
  dist = np.array ( [ \
    [ 0.0,    2.0,    5.0,    1.0,    np.inf ], \
    [ 2.0,    0.0,    3.0,    4.0,    np.inf ], \
    [ 6.0,    3.0,    0.0,    np.inf, np.inf ], \
    [ 1.0,    4.0,    np.inf, 0.0,    5.0    ], \
    [ np.inf, np.inf, np.inf, 5.0,    0.0    ] ] )
 
  graph_dist_print ( dist, nnode, '  Immediate node distance matrix:' )

  path_dist = graph_dist_all ( dist, nnode )
 
  graph_dist_print ( path_dist, nnode, '  Total node distance matrix:' )
 
  return

def graph_dist_check_test ( ):

#*****************************************************************************80
#
## graph_dist_check_test() tests graph_dist_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 15

  A = np.array ( [ \
    [  0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46 ], \
    [ 29,  0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21 ], \
    [ 82, 55,  0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51 ], \
    [ 46, 46, 68,  0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64 ], \
    [ 68, 42, 46, 82,  0, 74, 23, 52, 21, 46, 82, 58, 46, 65, 23 ], \
    [ 52, 43, 55, 15, 74,  0, 61, 23, 55, 31, 33, 37, 51, 29, 59 ], \
    [ 72, 43, 23, 72, 23, 61,  0, 42, 23, 31, 77, 37, 51, 46, 33 ], \
    [ 42, 23, 43, 31, 52, 23, 42,  0, 33, 15, 37, 33, 33, 31, 37 ], \
    [ 51, 23, 41, 62, 21, 55, 23, 33,  0, 29, 62, 46, 29, 51, 11 ], \
    [ 55, 31, 29, 42, 46, 31, 31, 15, 29,  0, 51, 21, 41, 23, 37 ], \
    [ 29, 41, 79, 21, 82, 33, 77, 37, 62, 51,  0, 65, 42, 59, 61 ], \
    [ 74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65,  0, 61, 11, 55 ], \
    [ 23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61,  0, 62, 23 ], \
    [ 72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62,  0, 59 ], \
    [ 46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59,  0 ] ] )

  print ( '' )
  print ( 'graph_dist_check_test():' )
  print ( '  graph_dist_check() checks a distance matrix.' )

  ierror = graph_dist_check ( A, nnode )

  print ( '' )

  if ( ierror == 0 ):
    print ( 'The distance matrix passed all tests.' )
  else:
    print ( 'The distance matrix failed test ', ierror )

  return

def graph_dist_check ( dist, nnode ):

#*****************************************************************************80
#
## graph_dist_check() checks a distance matrix for consistency.
#
#  Discussion:
#
#    The checks made are:
#
#      1): dist[I,I) = 0
#      2): dist[I,J) > 0 for I different from J
#      3): dist[I,J) = dist[J,I) for I different from J.
#      4): dist[I,J) + dist[J,K) >= dist[I,K).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real dist[NNODE,NNODE), the distance matrix.
#    dist[I,J) is the distance FROM node I TO node J.
#
#    integer NNODE, the number of nodes.
#
#  Output:
#
#    integer IERROR, error flag.
#    0, no errors.
#    1, dist[I,I] is nonzero for some I
#    2, dist[I,J] <= 0 for some distinct I, J
#    3, dist[I,J] not equal to dist[J,I] for some distinct I, J.
#    4, dist[I,J] + dist[J,K] < dist[I,K] for some I, J, K.
#
  ierror = 0

  for i in range ( 0, nnode ):
    if ( dist[i,i] != 0.0 ):
      ierror = 1
      print ( '' )
      print ( 'graph_dist_check(): Failed test #1:' )
      print ( '  dist[I,I] nonzero for I = ', i )
      return ierror

  for i in range ( 0, nnode ):
    for j in range ( 0, nnode ):
      if ( i != j ):
        if ( dist[i,j] <= 0.0 ):
          ierror = 2
          print ( '' )
          print ( 'graph_dist_check(): Failed test #2:' )
          print ( '  dist[', i, ',', j, '] <= 0' )
          return ierror

  for i in range ( 0, nnode ):
    for j in range ( 0, i ):
      if ( dist[i,j] != dist[j,i] ):
        ierror = 3
        print ( '' )
        print ( 'graph_dist_check(): Failed test #3:' )
        print ( '  dist[', i, ',', j, '] not equal to dist[', j, ',', i, ']' )
        return ierror

  for i in range ( 0, nnode ):
    for j in range ( 0, nnode ):
      for k in range ( 0, i ):
        if ( dist[i,j] + dist[j,k] < dist[i,k] ):
          ierror = 4
          print ( '' )
          print ( 'graph_dist_check(): Failed test #4:' )
          print ( '  dist[I,J] + dist[J,K] < dist[I,K]' )
          print ( '  I = ', i, ', j = ', j, ', K = ', k )
          print ( '  dist[I,J] =', dist[i,j] )
          print ( '  dist[J,K] =', dist[j,k] )
          print ( '  dist[I,K] =', dist[i,k] )
          return ierror

  return ierror

def graph_dist_min_span_tree ( nnode, dist ):

#*****************************************************************************80
#
## graph_dist_min_span_tree() computes a spanning tree of minimal length.
#
#  Discussion:
#
#    Because of the swapping between positive and negative indices,
#    some awkward coding had to be done here.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2025
#
#  Author:
#
#    Original FORTRAN77 version by Albert Nijenhuis, Herbert Wilf.
#    This version by John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer NNODE, the number of nodes.
#
#    real DIST(NNODE,NNODE).  DIST(I,J) = distance from node I to node J.
#
#  Output:
#
#    integer ITREE(NNODE-1), JTREE(NNODE-1), the pairs of
#    nodes that form the edges of the tree.
#
  import numpy as np

  itree = np.zeros ( nnode - 1, dtype = int )
  for i in range ( 0, nnode - 1 ):
    itree[i] = i

  jtree = - nnode * np.ones ( nnode - 1, dtype = int )

  for j in range ( 1, nnode ):
#
#  Choose the node IMIN whose tree edge ( ITREE(IMIN)=IMIN, JTREE(IMIN) )
#  will be set.
#
    dmin = np.inf

    for i in range ( 1, nnode ):

      it = jtree[i-1]

      if ( it < 0 ):

        d = dist[-it-1,i-1]

        if ( d < dmin ):
          dmin = d
          imin = i

    jtree[imin-1] = - jtree[imin-1]

    for i in range ( 1, nnode ):

      it = jtree[i-1]

      if ( it < 0 ):
        if ( dist[i-1,imin-1] < dist[i-1,-it-1] ):
          jtree[i-1] = - imin

  jtree = jtree - 1
 
  return itree, jtree

def graph_dist_min_span_tree_test ( ):

#*****************************************************************************80
#
## graph_dist_min_span_tree_test() tests graph_dist_min_span_tree().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 5

  dist = np.array ( [ \
    [   0.0, 100.0, 125.0, 120.0, 110.0 ], \
    [ 100.0,   0.0,  40.0,  65.0,  60.0 ], \
    [ 125.0,  40.0,   0.0,  45.0,  55.0 ], \
    [ 120.0,  65.0,  45.0,   0.0,  50.0 ], \
    [ 110.0,  60.0,  55.0,  50.0,   0.0 ] ] )

  print ( '' )
  print ( 'graph_dist_min_span_tree_test():' )
  print ( '  graph_dist_min_span_tree() finds a minimum spanning tree.' )
  print ( '' )

  graph_dist_print ( dist, nnode, '  The graph:' )

  itree, jtree = graph_dist_min_span_tree ( nnode, dist )
 
  wtree = np.zeros ( nnode - 1 )
  for i in range ( 0, nnode - 1 ):
    wtree[i] = dist[itree[i],jtree[i]]
 
  graph_arc_weight_print ( nnode-1, itree, jtree, wtree, '  The minimal spanning tree:' )
 
  print ( '' )
  print ( '  The length of the minimal tree is ', np.sum ( wtree ) )
 
  return

def graph_dist_min_span_tree_alternate_test ( ):

#*****************************************************************************80
#
## graph_dist_min_span_tree_alternate_test() tests graph_dist_min_span_tree().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 57

  print ( '' )
  print ( 'graph_dist_min_span_tree_alternate_test()' )
  print ( '  graph_dist_min_span_tree() finds a minimum ' )
  print ( '  spanning tree.' )
  print ( '' )
  print ( '  Read distance data for 57 cities from file.' )
#
#  Read the data.
#
  filename = '57_city_distances.txt'
  dist = np.loadtxt ( filename )
#
#  Compute the tree.
#
# klass, itree, jtree = graph_dist_min_span_tree2 ( nnode, dist )
  itree, jtree = graph_dist_min_span_tree ( nnode, dist )
 
  wtree = np.zeros ( nnode - 1 )
  for i in range ( 0, nnode - 1 ):
    wtree[i] = dist[itree[i],jtree[i]]
 
  graph_arc_weight_print ( nnode-1, itree, jtree, wtree, '  The weighted tree:' )

  print ( '' )
  print ( '  The length of the minimal tree is ', np.sum ( wtree ) )

  return

def graph_dist_min_span_tree2 ( nnode, dist ):

#*****************************************************************************80
#
## graph_dist_min_span_tree2() computes a spanning tree of minimal length.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NNODE, the number of nodes.
#
#    real DIST(NNODE,NNODE).  DIST(I,J) = distance from node I to node J.
#
#  Output:
#
#    integer klass(NNODE), lists the nodes in the order in
#    which they joined the tree.
#
#    integer ITREE(NNODE-1), JTREE(NNODE-1), the pairs of
#    nodes that form the edges of the tree.
#
  import numpy as np

  klass = np.zeros ( nnode, dtype = int )
  itree = np.zeros ( nnode - 1, dtype = int )
  jtree = np.zeros ( nnode - 1 , dtype = int )
  
  if ( nnode <= 1 ):
    return klass, itree, jtree
#
#  All the nodes start out in the negative klass.
#
  npos = 0

  for i in range ( 0, nnode ):
    klass[i] = i + 1
#
#  Find the shortest edge (I,J).
#
  unset = True
  dmin = 0.0

  for i in range ( 0, nnode ):
    for j in range ( i + 1, nnode ):

      if ( unset ):
        smaller = True
      elif ( dist[i,j] < dmin ):
        smaller = True
      else:
        smaller = False

      if ( smaller ):
        imin = i
        jmin = j
        dmin = dist[i,j]
        unset = False
#
#  Carry nodes IMIN and JMIN into the positive klass.
#
  klass[npos], klass[imin] = klass[imin], klass[npos]
  npos = npos + 1

  klass[npos], klass[jmin] = klass[jmin], klass[npos]
  npos = npos + 1

  itree[0] = imin
  jtree[0] = jmin
#
#  Now, repeatedly, find the shortest edge connecting a negative
#  and positive node.  Move the negative node to the positive klass and
#  repeat.
#
  for k in range ( 1, nnode - 1 ):

    unset = True
    dmin = 0.0
    imin = - 99
    jmin = - 99

    for ii in range ( 0, npos ):

      i = klass[ii] - 1

      for jj in range ( npos, nnode ):

        j = klass[jj] - 1

        if ( unset ):
          smaller = True
        elif ( dist[i,j] < dmin ):
          smaller = True
        else:
          smaller = False

        if ( smaller ):
          imin = i
          jmin = j
          jjmin = jj
          dmin = dist[i,j]
          unset = False

    klass[npos], klass[jjmin] = klass[jjmin], klass[npos]
    npos = npos + 1

    itree[k] = imin
    jtree[k] = jmin

  return klass, itree, jtree

def graph_dist_min_span_tree2_test ( ):

#*****************************************************************************80
#
## graph_dist_min_span_tree2_test() tests graph_dist_min_span_tree2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 5

  dist = np.array ( [ \
    [   0.0, 100.0, 125.0, 120.0, 110.0 ], \
    [ 100.0,   0.0,  40.0,  65.0,  60.0 ], \
    [ 125.0,  40.0,   0.0,  45.0,  55.0 ], \
    [ 120.0,  65.0,  45.0,   0.0,  50.0 ], \
    [ 110.0,  60.0,  55.0,  50.0,   0.0 ] ] )

  print ( '' )
  print ( 'graph_dist_min_span_tree2_test():' )
  print ( '  graph_dist_min_span_tree() finds a minimum spanning tree.' )
  print ( '' )
 
  graph_dist_print ( dist, nnode, '  The graph:' )

  klass, itree, jtree = graph_dist_min_span_tree2 ( nnode, dist )
 
  wtree = np.zeros ( nnode - 1, dtype = int )

  for i in range ( 0, nnode - 1 ):
    wtree[i] = dist[itree[i],jtree[i]]
 
  graph_arc_weight_print ( nnode-1, itree, jtree, wtree, '  The minimal spanning tree:' )
 
  print ( '' )
  print ( '  The length of the minimal tree is ', np.sum ( wtree ) )
 
  return

def graph_dist_min_span_tree3 ( nnode, dist ):

#*****************************************************************************80
#
## graph_dist_min_span_tree3() finds a minimum spanning tree.
#
#  Discussion:
#
#    The input graph is represented by a distance matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hang Tong Lau,
#    Combinatorial Heuristic Algorithms in FORTRAN,
#    Springer Verlag, 1986.
#
#  Input:
#
#    integer NNODE, the number of nodes.
#
#    real DIST(NNODE,NNODE), an NNODE by NNODE distance
#    matrix.  DIST(I,J) is the distance from node I to node J.  The matrix
#    should be symmetric.  If there is no arc from node I to node J,
#    set DIST(I,J) = HUGE(1.0).
#
#  Output:
#
#    integer INODE(NNODE), JNODE(NNODE) entries 1 through
#    NNODE-1 describe the edges of the spanning tree as pairs of nodes.
#
  import numpy as np

  inode = np.zeros ( nnode, dtype = int )
  jnode = np.zeros ( nnode, dtype = int )

  work = np.inf * np.ones ( nnode )
  iwork1 = np.zeros ( nnode, dtype = int )
  iwork2 = np.zeros ( nnode, dtype = int )
#
#  Find the first non-zero arc.
#
  for ij in range ( 0, nnode ):
    flag = False
    for kj in range ( 0, nnode ):
      if ( dist[ij,kj] < np.inf ):
        i = ij
        flag = True
        break

    if ( flag ):
      break

  work[i] = 0
  iwork1[i] = 1
  tree_length = 0.0
  kk4 = nnode - 1

  for jj in range ( 0, kk4 ):

    work = np.inf * np.ones ( nnode )

    for i in range ( 0, nnode ):
#
#  For each forward arc originating at node I calculate
#  the length of the path to node I
#
      if ( iwork1[i] == 1 ):
        for j in range ( 0, nnode ):
          if ( dist[i,j] < np.inf and iwork1[j] == 0 ):
            d = tree_length + dist[i,j]
            if ( d < work[j] ):
              work[j] = d
              iwork2[j] = i
#
#  Find the minimum potential.
#
    d = np.inf
    ient = -1

    for i in range ( 0, nnode ):
      if ( iwork1[i] == 0 and work[i] < d ):
        d = work[i]
        ient = i
        itr = iwork2[i]
#
#  Include the node in the current path.
#
    if ( d < np.inf ):
      iwork1[ient] = 1
      tree_length = tree_length + dist[itr,ient]
      inode[jj] = itr
      jnode[jj] = ient

  return inode, jnode

def graph_dist_min_span_tree3_test ( ):

#*****************************************************************************80
#
## graph_dist_min_span_tree3_test() tests graph_dist_min_span_tree3().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 5

  dist = np.array ( [ \
    [   0.0, 100.0, 125.0, 120.0, 110.0 ], \
    [ 100.0,   0.0,  40.0,  65.0,  60.0 ], \
    [ 125.0,  40.0,   0.0,  45.0,  55.0 ], \
    [ 120.0,  65.0,  45.0,   0.0,  50.0 ], \
    [ 110.0,  60.0,  55.0,  50.0,   0.0 ] ] )

  print ( '' )
  print ( 'graph_dist_min_span_tree3_test():' )
  print ( '  graph_dist_min_span_tree3() finds a minimum spanning tree.' )
  print ( '' )
 
  graph_dist_print ( dist, nnode, '  The graph:' )

  itree, jtree = graph_dist_min_span_tree3 ( nnode, dist )
 
  wtree = np.zeros ( nnode - 1 )
  for i in range ( 0, nnode - 1 ):
    wtree[i] = dist[itree[i],jtree[i]]
 
  graph_arc_weight_print ( nnode-1, itree, jtree, wtree, '  The minimal spanning tree:' )
 
  print ( '' )
  print ( '  The length of the minimal tree is ', np.sum ( wtree ) )
 
  return

def graph_dist_one ( dist, inode, nnode ):

#*****************************************************************************80
#
## graph_dist_one() computes the distance from one node to all others in a graph.
#
#  Discussion:
#
#    This routine can handle both ordinary graphs and directed graphs.
#
#    In an ordinary graph, a connection between two nodes is always guaranteed
#    to be "symmetric".  That is, if node I is connected to node J by
#    an edge of length D, then node J is connected to node I, and the
#    distance is again D.
#
#    In a directed graph, if node I is connect to node J by an edge of
#    length D, then nothing is known about a possible connection from
#    node J back to node I.  In particular, it is possible that:
#
#    * there is no direct edge from node J to node I
#    * the edge from node J to node I exists, but is a different "length"
#      than the edge from node I to node J.
#
#    The program computes:
#
#    * PATH_DIST, an array of distances from node INODE to all other nodes
#
#    * DAD, an array which can be used to determine the path from
#      node INODE to any particular node.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Gibbons,
#    Algorithmic Graph Theory,
#    Cambridge University Press, 1985,
#    ISBN 0-521-28881-9.
#
#  Input:
#
#    real DIST(NNODE,NNODE).  DIST contains the weighted
#    adjacency information defining the graph, or directed graph.
#    The diagonal entries of DIST, that is, DIST(I,I), should be set to 0.
#    The value of the typical off diagonal element DIST(I,J) should
#    represent the length, or weight, of the edge from node I to
#    node J.  If the graph is undirected, then DIST(I,J) should always
#    equal DIST(J,I).  For a directed graph, these quantities may differ.
#    If there is no edge from node I to node J, then it would be natural
#    to set DIST(I,J) to Inf. 
#    All the entries in DIST should be non-negative.  The algorithm will
#    NOT work correctly if negative edge lengths are input.
#    Off-diagonal elements DIST(I,J) may be set to zero.  This simply
#    means that two nodes are "very close", like St Paul and Minneapolis.
#
#    integer INODE, the base node, from which distances to
#    the other nodes are to be calculated.
#
#    integer NNODE, the number of nodes.
#
#  Output:
#
#    real PATH_DIST(NNODE).  On output, for every value
#    of I from 1 to NNODE, PATH_DIST(I) contains the distance from node INODE
#    to node I in the graph.  Of course, PATH_DIST(INODE) is zero.  Moreover,
#    if PATH_DIST(I) = DINFIN, then this is the program's way of reporting that
#    there is NO path from node INODE to node I.
#
#    integer DAD(NNODE), information defining the shortest
#    path from node INODE to any node I, which presumably will be of
#    total distance PATH_DIST(I).
#    The path from node I to node INODE, is recorded "in reverse"
#    in DAD.  The last node is INODE, of course.  The previous node
#    is DAD(INODE).  The next node is DAD(DAD(INODE)) and
#    so on, until INODE itself is reached.
#    If the distance from node I to node INODE is Inf, then
#    DAD will still record a path it's just probably of no interest.
#
#    integer PATH(NNODE).  The value of PATH(I) records
#    the step on which the distance from INODE to node I was
#    determined.  There will be NNODE steps, and on each step
#    just one such distance is computed.
#
  import numpy as np
#
#  Initialize the data.
#
  dad = inode * np.ones ( nnode )
  path = -1 * np.ones ( nnode )
  path_dist = dist[inode,:]
#
#  On step 1, we connect node INODE itself.
#
  dad[inode] = inode
  path[inode] = 0
#
#  On steps ISTEP = 2 through NNODE, we try to add just one more node.
#
#  Of all the nodes which are not yet connected to INODE (because PATH
#  is 0 for this node), choose the one whose distance is least.
#
  for istep in range ( 1, nnode ):

    dmin = np.inf
    imin = 0

    for j in range ( 0, nnode ):

      if ( path[j] == -1 ):
        if ( path_dist[j] <= dmin ):
          dmin = path_dist[j]
          imin = j;
#
#  If we found no new node to add, then any remaining nodes cannot
#  be connected.
#
    if ( dmin == np.inf ):
      return path_dist, dad, path
#
#  Now add the closest node, labeled IMIN, to the list.
#
    path[imin] = istep
#
#  Update the distances of the remaining unconnected nodes.
#
    for j in range ( 0, nnode ):

      if ( path[j] == -1 ):

        dtemp = path_dist[imin] + dist[imin,j]

        if ( dtemp < path_dist[j] ):
          path_dist[j] = dtemp
          dad[j] = imin

  return path_dist, dad, path

def graph_dist_one_test ( ):

#*****************************************************************************80
#
## graph_dist_one_test() tests graph_dist_one().
#
#  Discussion:
#
#    This example appears on page 15 of the reference book by Gibbons.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 5

  print ( '' )
  print ( 'graph_dist_one_test():' )
  print ( '  graph_dist_one() computes the distance from one' )
  print ( '  node to all others in a graph.' )
  print ( '' )
 
  dist = np.array ( [ \
    [ 0.0,    1.0,    3.0,    np.inf, np.inf ], \
    [ 2.0,    0.0,    1.0,    np.inf, 2.0    ], \
    [ np.inf, np.inf, 0.0,    2.0,    3.0    ], \
    [ np.inf, np.inf, 1.0,    0.0,    np.inf ], \
    [ 1.0,    3.0,    np.inf, 6.0,    0.0    ] ] )

  graph_dist_print ( dist, nnode, '  Edge Distance Matrix:' )

  inode = 4
  print ( '' )
  print ( 'The starting node is ', inode )
  print ( '' )

  path_dist, idad, path = graph_dist_one ( dist, inode, nnode )

  print ( '' )
  print ( '  Node    Distance   Path Idad' )
  print ( '' )
 
  for i in range ( 0, nnode ):
    print ( '%5d %14.6g %5d %5d' % ( i, path_dist[i], path[i], idad[i] ) )
 
  print ( '' )
  print ( '  Here are the paths for each node:' )
  print ( '' )
 
  itemp = -1 * np.ones ( nnode, dtype = int )

  for i in range ( 0, nnode ):

    length = 0
    itemp[length] = i
 
    while ( itemp[length] != inode ):
      length = length + 1
      itemp[length] = idad[itemp[length-1]]
 
    for j in range ( 0, length + 1 ):
      print ( '  ', itemp[j], end = '' )

    print ( '' )
 
  return

def graph_dist_pairing_greedy ( maxit, nodeb, noder, nnode, tol, xb, xr, yb, yr ):

#*****************************************************************************80
#
## graph_dist_pairing_greedy() pairs two sets of nodes using the least total distance.
#
#  Discussion:
#
#    The method is iterative, and is not guaranteed to find the best
#    possible arrangement.  This is particulary true because it is a
#    "local" method, which only considers pairwise switches of the
#    red nodes that reduce the total distance.  This means that a
#    "locally minimizing" pairing might be found which is not the
#    global minimizer.
#
#    On the other hand, in the absence of a theoretical plan for how
#    to reach the global minimizer, the brute force search would
#    require that EVERY possible pairing be considered, and its total
#    distance computed.  This means that a total of factorial(NNODE)
#    graphs would have to be generated.
#
#    The approach used here, on each iterative step, looks at a
#    maximum of NNODE * (NNODE-1] graphs, which represents a
#    significantly more efficient method.
#
#    It would not be hard to extend this approach to a method which
#    considers switches of THREE red nodes at a time, though the
#    work there involve looking at NNODE * (NNODE-1] * (NNODE-2]
#    graphs, and as we increase the number of graphs we examine,
#    we begin to approach the factorial(NNODE) rate for the brute force
#    algorithm.
#
#    It also would not be hard to extend this method to a case where
#    there are three sets of nodes, arranged in triples, and again
#    the total distance is to be minimized.
#
#    If it is suspected that the pairing returned is only
#    a local minimizer, then the user is advised to restart the
#    calculation after randomly permuting the entries of NODER, so that
#    the routine starts from a different point in the space of graphs.
#
#    The routine is given:
#
#      an initial ordering of the black and red nodes, so that
#      ( NODEb[I), NODEr[I) ) represents the I-th pair,
#
#      the X and Y coordinates of the black and red nodes,
#
#      a maximum number of iterations, and a relative distance
#      decrease requirement,
#
#    and computes:
#
#      a new ordering of the red nodes, contained in NODER, which should
#      reduce the total distance between corresponding red and black
#      nodes.
#
#    The approach can be applied to a variety of problems including:
#
#    1] We are given two sets of NNODE points, which we will call the
#       "red" and "black " groups, and the (X,Y) coordinates of each
#       point.  We may imagine these points as forming the two sets of
#       nodes of a bipartite graph lying in the (X,Y) plane.  We wish
#       to choose a pairing of red and black nodes which results in
#       the shortest total arc length.
#
#    2] We are given two sets of NNODE complex quantities, which we
#       believe are approximations to the same (unknown) set of
#       quantities.  We wish to arrange this data into NNODE pairs,
#       each containing a unique element from each set of data, which
#       minimizes the sum of squares of the discrepancies between the
#       pairs.  In particular, the two sets of data might be two
#       separate estimates of the complex eigenvalues of a matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MAXIT, the maximum number of iterations
#    allowed.  Each iteration considers, one at a time, each black node, and
#    seeks to switch its red neighbor for another red neighbor that
#    reduces the total distance.
#
#    integer NODEb[NNODE), the "labels" of the black
#    nodes.  You probably want to just set NODEb[I) = I, for i = 1 to NNODE.
#    The entries in NODEB will not be changed.
#
#    integer NODEr[NNODE), the initial "labels" of the red nodes.
#    You probably want to just set the input value of NODEr[I) = I,
#    for i = 1 to NNODE.  The values of ( NODEb[I), NODEr[I) ) contain the
#    labels of the I-th pair of black and red nodes.
#
#    integer NNODE, the number of nodes in the black and red sets.
#
#    real TOL.
#    TOL is the relative decrease that the user demands in the
#    total distance, after each iterative step.  If we denote
#    the distance before the iterative step as OLDTOT, and the
#    distance after the iterative step as TOTAL, then the
#    routine will try another iterative step as long as "enough"
#    progress was made on this step.  Enough progress was made
#    whenever OLDTOT - TOTAL < TOL * TOTAL
#
#    real Xb[NNODE), the X coordinates of the black nodes.
#
#    real Xr[NNODE), the X coordinates of the red nodes.
#
#    real Yb[NNODE), the Y coordinates of the black nodes.
#
#    real Yr[NNODE), the Y coordinates of the red nodes.
#
#  Output:
#
#    integer NODEr[NNODE), the updated "labels" of the red nodes.
#    If a better pairing of the nodes has been found,
#    this will be reflected in the newly permuted values of NODER.
#
  import numpy as np
#
#  Compute the total distance of the starting pairing.
#
  total = 0.0
  for indx in range ( 0, nnode ):
    nodeb1 = nodeb[indx]
    noder1 = noder[indx]
    total = total + np.sqrt ( \
      ( xb[nodeb1] - xr[noder1] )**2 + ( yb[nodeb1] - yr[noder1] )**2 )

  print ( '' )
#
#  Begin the iterations.
#
  for it in range ( 0, maxit ):

    if ( total == 0.0 ):
      print ( '' )
      print ( 'graph_dist_pairing_greedy(): Early termination.' )
      print ( '  Total discrepancy is low enough.' )
      return noder
#
#  Save the current total distance for comparison at the end of the
#  iteration.
#
    oldtot = total
    nswap = 0
#
#  Consider each black node, by running through indices INDX1 = 1
#  through NNODE of the NODEB array.
#
    for indx1 in range ( 0, nnode ):
#
#  Get the labels of the current INDX1-th pair of black and red nodes.
#
      nodeb1 = nodeb[indx1]
      noder1 = noder[indx1]
#
#  Look at the black node with INDX2 = 1 through NNODE, but ignore
#  the case where INDX1 = INDX2.
#
      for indx2 in range ( 0, nnode ):
#
#  Get the labels of the current INDX2-th pair of black and red nodes.
#
        nodeb2 = nodeb[indx2]
        noder2 = noder[indx2]

        if ( indx2 != indx1 ):
#
#  Compute the total distance between (NODEB1,NODER1] and
#  (NODEB2,NODER2], and compare it to the total where we switch the
#  red nodes.
#
          dist1 = np.sqrt ( ( xb[nodeb1] - xr[noder1] )**2   \
                          + ( yb[nodeb1] - yr[noder1] )**2 ) \
                + np.sqrt ( ( xb[nodeb2] - xr[noder2] )**2   \
                          + ( yb[nodeb2] - yr[noder2] )**2 )

          dist2 = np.sqrt ( ( xb[nodeb1] - xr[noder2] )**2   \
                          + ( yb[nodeb1] - yr[noder2] )**2 ) \
                + np.sqrt ( ( xb[nodeb2] - xr[noder1] )**2   \
                          + ( yb[nodeb2] - yr[noder1] )**2 )
#
#  If the new arrangement is any shorter, take it, by shuffling the
#  red nodes only, and update the total distance.
#
          if ( dist2 < dist1 ):
            node_temp = noder[indx1]
            noder[indx1] = noder[indx2]
            noder[indx2] = node_temp
            nswap = nswap + 1
#
#  We've checked all pairs of nodes,
#  print the new total distance, and see if we may
#  continue, or should give up.
#
    total = 0.0
    for indx1 in range ( 0, nnode ):

      nodeb1 = nodeb[indx1]
      noder1 = noder[indx1]

      total = total + np.sqrt ( ( xb[nodeb1] - xr[noder1] )**2 \
                              + ( yb[nodeb1] - yr[noder1] )**2 )

    print ( '  On step ', it )
    print ( '  discrepancy = ', total )
    print ( '  Swaps made was ', nswap )

    if ( oldtot - total <= tol * oldtot ):

      temp = ( oldtot - total ) / oldtot
      print ( '' )
      print ( 'graph_dist_pairing_greedy(): Warning:' )
      print ( '  The relative change in the discrepancy ' )
      print ( '  was only', temp )
      print ( '  which is less than the tolerance TOL =', tol )
      print ( '  Bailing out of the iteration.' )
      print ( '' )
      return noder

  print ( '' )
  print ( 'graph_dist_pairing_greedy(): Note:' )
  print ( '  The discrepancy has decreased by at least the' )
  print ( '  tolerance on every step.' )
  print ( '' )
  print ( '  Increasing the number of iterations might' )
  print ( '  provide further improvement at this rate.' )

  return noder

def graph_dist_pairing_greedy_test ( ):

#*****************************************************************************80
#
## graph_dist_pairing_greedy_test() tests graph_dist_pairing_greedy().
#
#  Discussion:
#
#    Random data is used in setting up the problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nnode = 15
  nnodeh = 7
#
#  Set the maximum number of iterations.
#
  maxit = 10
#
#  Set the range of the X and Y coordinates.
#
  xhi = 10.0
  xlo = 0.0
  yhi = 5.0
  ylo = 3.0
#
#  Set the relative tolerance for the stepwise distance decrease.
#
  tol = 0.05
#
#  Say hello.
#
  print ( '' )
  print ( 'graph_dist_pairing_greedy_test():' )
  print ( '  graph_dist_pairing_greedy() tries to minimize the total' )
  print ( '  distance in a pairing of black and red nodes.' )
  print ( '' )
  print ( '  Try to find a pairing of two sets of nodes' )
  print ( '  with a low discrepancy.' )
  print ( '' )
  print ( '  Relative tolerance for step decrease = ', tol )
  print ( '  Maximum number of steps = ', maxit )
  print ( '  X range is ', xlo, ' to ', xhi )
  print ( '  Y range is ', ylo, ' to ', yhi )
#
#  Make an arbitrary pairing of the nodes.
#
  nodeb = np.zeros ( nnode, dtype = int )
  noder = np.zeros ( nnode, dtype = int )

  for indx in range ( 0, nnode ):
    nodeb[indx] = indx
    noder[indx] = indx
#
#  Make up a random set of X, Y coordinates for the nodes.
#
  xb = xlo + ( xhi - xlo ) * np.random.random ( nnode )
  xr = xlo + ( xhi - xlo ) * np.random.random ( nnode )
  yb = ylo + ( yhi - ylo ) * np.random.random ( nnode )
  yr = ylo + ( yhi - ylo ) * np.random.random ( nnode )
#
#  We will jump back here if we restart with a permuted NODER.
#
  for ido in range ( 0, 2 ):
 
    print ( '' )
    print ( '  Initial black node coordinates:' )
    print ( '' )
    print ( '    I   Black   X             Y' )
    print ( '' )
 
    for indx in range ( 0, nnode ):
      print ( '%8d  %8d  %g  %g' % ( indx, nodeb[indx], xb[indx], yb[indx] ) )
 
    print ( '' )
    print ( 'Initial red node coordinates:' )
    print ( '' )
    print ( '    I    Red    X             Y' )
    print ( '' )
 
    for indx in range ( 0, nnode ):
      print ( '%8d  %8d  %g  %g' % ( indx, noder[indx], xr[indx], yr[indx] ) )
 
    print ( '' )
    print ( '  Initial pairing of nodes:' )
    print ( '' )
    print ( '    I   Black  Red    Distance' )
    print ( '' )
 
    for indx in range ( 0, nnode ):
      nodeb1 = nodeb[indx]
      noder1 = noder[indx]
      dist = np.sqrt ( ( xb[nodeb1] - xr[noder1] )**2 + \
                       ( yb[nodeb1] - yr[noder1] )**2 )

      print ( '  %d  %d  %d  %g' % ( indx, nodeb1, noder1, dist ) )
 
    total = 0.0
    for indx in range ( 0, nnode ):
      nodeb1 = nodeb[indx]
      noder1 = noder[indx]
      total = total + np.sqrt ( ( xb[nodeb1] - xr[noder1] )**2 \
                              + ( yb[nodeb1] - yr[noder1] )**2 )
 
    print ( '' )
    print ( 'Total discrepancy of initial pairing = ', total )
#
#  Seek a better pairing.
#
    noder = graph_dist_pairing_greedy ( maxit, nodeb, noder, nnode, \
      tol, xb, xr, yb, yr )
 
    print ( '' )
    print ( '  Final black node coordinates:' )
    print ( '' )
    print ( '    I   Black   X             Y' )
    print ( '' )
 
    for indx in range ( 0, nnode ):
      print ( '%8d  %8d  %g  %g' % ( indx, nodeb[indx], xb[indx], yb[indx] ) )
 
    print ( '' )
    print ( 'Final red node coordinates:' )
    print ( '' )
    print ( '    I    Red    X             Y' )
    print ( '' )
 
    for indx in range ( 0, nnode ):
      print ( '%8d  %8d  %g  %g' % ( indx, noder[indx], xr[indx], yr[indx] ) )
 
    print ( '' )
    print ( 'Final pairing of nodes:' )
    print ( '' )
    print ( '    I   Black  Red    Distance' )
    print ( '' )
 
    for indx in range ( 0, nnode ):

      nodeb1 = nodeb[indx]
      noder1 = noder[indx]

      dist = np.sqrt ( ( xb[nodeb1] - xr[noder1] )**2 \
                     + ( yb[nodeb1] - yr[noder1] )**2 )

      print ( '  %d  %d  %d  %g' % ( indx, nodeb1, noder1, dist ) )
 
    total = 0.0
    for indx in range ( 0, nnode ):
      nodeb1 = nodeb[indx]
      noder1 = noder[indx]
      dist = np.sqrt ( ( xb[nodeb1] - xr[noder1] )**2 \
                     + ( yb[nodeb1] - yr[noder1] )**2 )

      total = total + dist
  
    print ( '' )
    print ( '  Total discrepancy of final pairing = ', total )
#
#  On the second try, reverse the ordering of the red nodes.
#  Any random permutation would be worth trying.
#
    if ( ido == 0 ):
 
      noder = np.flip ( noder )
 
      print ( '' )
      print ( '  Try reversing NODER!' )
  
  return

def graph_dist_print ( dist, nnode, title ):

#*****************************************************************************80
#
## graph_dist_print() prints a distance matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DIST(NNODE,NNODE), the distance matrix.
#    DIST(I,J) is the distance from node I to node J.
#
#    integer NNODE, the number of nodes.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( dist )

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
  graph_dist_test ( )
  timestamp ( )

