#! /usr/bin/env python3
#
def prim_test ( ):

#*****************************************************************************80
#
## prim_test() tests prim().
#
#  Discussion:
#
#    Original Graph     Spanning Tree
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
  print ( 'prim_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Use Prim\'s algorithm to compute a minimal weight' )
  print ( '  spanning tree for a weighted graph.' )
#
#  The weight array should be symmetric.  It should have 0's on the diagonal.
#  Off diagonal entries should be strictly positive.  If there is no link
#  from node I to node J, then weight[i,j] should be set to np.inf.
#
  weight = np.array ( [ \
    [      0,      2, np.inf,      6, np.inf ], \
    [      2,      0,      3,      8,      5 ], \
    [ np.inf,      3,      0, np.inf,      7 ], \
    [      6,      8, np.inf,      0,      9 ], \
    [ np.inf,      5,      7,      9,      0 ] ] )

  nv = weight.shape[0]

  print ( '' )
  print ( '  The node-to-node distance matrix' )
  pprint.pprint ( weight )
#
#  Call the Prim algorithm.
#
  links = prim ( weight )
#
#  Report the links (i,j) and associated weight for the spanning tree.
#
  print ( '' )
  print ( '  #  I  J  weight(I,J)' )
  for l in range ( 0, nv - 1 ):
    i = links[l,0]
    j = links[l,1]
    print ( '  %d  %d  %d  %g' % ( l, i, j, weight[i,j] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'prim_test():' )
  print ( '  Normal end of execution.' )

  return

def prim ( weight ):

#*****************************************************************************80
#
## prim() applies Prim's algorithm to find a minimal spanning tree.
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
#  Input:
#
#    real weight[vn,vn]: weight[i,j] is the weight of the link from
#    node i to node j.
#
#  Output:
#
#    integer links[vn-1,2]: the k-th link in the minimal spanning tree
#    joins node i=links[k,0] to node j=links[k,1].
#
  import numpy as np

  vn = weight.shape[0]
#
#  Initialize the link information.
#
  ln = 0
  links = -1 * np.ones ( [ vn - 1, 2 ], dtype = int )
#
#  Initialize the connected list to node 0, and the unconnected list
#  to all the other nodes.
#
  connected = [ 0 ]
  unconnected = list ( range ( 0, vn ) )
  unconnected.remove ( 0 )
#
#  If node I is not connected, but it has a link to a connected node,
#  consider the weight of that link as a candidate for the shortest.
#
  while ( True ):

    vibest = -1
    wbest = np.Inf

    for vi in unconnected:
      for vj in connected:
        wij = weight[vi,vj]
        if ( wij < wbest ):
          vibest = vi
          vjbest = vj
          wbest = wij

    if ( vibest == -1 ):
      break
#
#  Add the shortest link.
#
    links[ln,0] = vibest
    links[ln,1] = vjbest
    connected.append ( vibest )
    unconnected.remove ( vibest )
    ln = ln + 1

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
  prim_test ( )
  timestamp ( )

