#! /usr/bin/env python3
#
def kruskal_test ( ):

#*****************************************************************************80
#
## kruskal_test() tests kruskal().
#
#  Discussion:
#
#    Original Graph     Spanning Tree
#
#
#    0---1              0---1
#    |  /|\             |   |\
#    | / | \            |   | \
#    |/  |  |           |   |  |
#    3   2  |           3   2  |
#     \  |  |                  |
#      \ | /                  /
#       \|/                  /
#        4                  4
#
#    The weights are not shown here.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import pprint

  print ( '' )
  print ( 'kruskal_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Use Kruskal\'s algorithm to compute a minimal weight' )
  print ( '  spanning tree for a weighted graph.' )
#
#  Define array of weights and pairs of nodes.
#
  for problem in range ( 0, 2 ):

    if ( problem == 0 ):

      print ( '' )
      print ( '  Problem 0:' )

      edges = np.array ( [ \
        [ 2, 0, 1 ], \
        [ 6, 0, 3 ], \
        [ 3, 1, 2 ], \
        [ 8, 1, 3 ], \
        [ 5, 1, 4 ], \
        [ 7, 2, 4 ], \
        [ 9, 3, 4 ] ] )

    else:

      print ( '' )
      print ( '  Problem 1:' )

      edges = np.array ( [ \
        [  7, 0, 1 ], \
        [  5, 0, 3 ], \
        [  8, 1, 2 ], \
        [  9, 1, 3 ], \
        [  7, 1, 4 ], \
        [  5, 2, 4 ], \
        [ 15, 3, 4 ], \
        [  6, 3, 5 ], \
        [  8, 4, 5 ], \
        [  9, 4, 6 ], \
        [ 11, 5, 6 ] ] )

    print ( '' )
    print ( '  W  I  J for full set of edges' )
    pprint.pprint ( edges )
#
#  Apply Kruskal algorithm.
#
    tree_edges = kruskal ( edges )

    print ( '' )
    print ( '  W  I  J for spanning tree' )
    pprint.pprint ( tree_edges )

    print ( '  Tree weight is ', np.sum ( tree_edges[:,0] ) )

  return

def kruskal ( edges ):

#*****************************************************************************80
#
## kruskal() applies Kruskal's algorithm to find a minimal spanning tree.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Kruskal,
#    On the shortest spanning subtree of a graph and the traveling salesman problem,
#    Proceedings of the American Mathematical Society,
#    Volume 7, Number 1, pages 48-50, 1956.
#
#  Input:
#
#    edges[edge_num,3]: the weight, start node, end node of each edge.
#
#  Output:
#
#    integer links[vn-1,2]: the k-th link in the minimal spanning tree
#    joins node i=links[k,0] to node j=links[k,1].
#
  import numpy as np
  import pprint
#
#  Infer the number of nodes by the largest value in the last two columns.
#  Assume nodes are numbered 0 ... v_num-1
#
  e_num = edges.shape[0]
  v_num = np.max ( edges[:,1:] ) + 1
#
#  Assign each node to its own tree: 0, 1, 2, ..., v_num-1
#
  tree_label = np.arange ( v_num, dtype = int )
  tree = [ set() for i in range ( 0, v_num ) ]
  for i in range ( 0, v_num ):
    tree[i] = { i }
#
#  Sort the edge array ( w, i, j ) by weight.
#  Careful, the i and j are now default floats.
#
  sort_indices = edges[:,0].argsort()
  edges = edges[sort_indices]
#
#  Set aside space for output array.
#
  links = np.zeros ( [ v_num - 1, 3 ], dtype = int )
#
#  Process the sorted edges.
#
  w_total = 0.0
  k = 0
  k2 = 0

  for k in range ( 0, e_num ):

    w = edges[k,0]
    i = edges[k,1]
    j = edges[k,2]
#
#  If this edge joins two distinct trees, merge the trees.
#
    if ( tree_label[i] != tree_label[j] ):
      i, j = min ( i, j ), max ( i, j )
      l = ( tree_label == tree_label[j] )
      tree_label[l] = tree_label[i]
      tree[i] = tree[i].union ( tree[j] )
      w_total = w_total + w
#
#  Copy information to output array.
#
      links[k2,:] = edges[k,:]
      k2 = k2 + 1

  return links

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
  kruskal_test ( )
  timestamp ( )


