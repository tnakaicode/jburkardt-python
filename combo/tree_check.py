#! /usr/bin/env python
#
def tree_check ( n, t ):

#*****************************************************************************80
#
## TREE_CHECK checks a tree.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of nodes in the tree.
#    N must be positive.
#
#    Input, integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
#    Output, integer CHECK, error flag.
#    1, the data is legal.
#    0, the data is not legal.
#
  import numpy as np
  from edge_degree import edge_degree

  check = True

  if ( n < 1 ):
    check = False
    return check

  for i in range ( 0, 2 ):
    for j in range ( 0, n - 2 ):
      if ( t[i,j] < 1 or n < t[i,j] ):
        check = False
        return check
#
#  Compute the degree of each node.
#
  d = edge_degree ( n, n - 1, t )
#
#  Make a copy of T.
#
  t2 = np.zeros ( [ 2, n - 1 ], dtype = np.int32 )

  for i in range ( 0, 2 ):
    for j in range ( 0, n - 1 ):
      t2[i,j] = t[i,j]
#
#  Delete a node of degree 1, N-1 times.
#
  for k in range ( 0, n - 1 ):

    x = 1

    while ( d[x-1] != 1 ):

      x = x + 1

      if ( n < x ):
        check = False
        return check
#
#  Find its neighbor.
#
    j = 0

    while ( True ):

      if ( t2[0,j] == x ):
        y = t2[1,j]
        break

      if ( t2[1,j] == x ):
        y = t2[0,j]
        break

      j = j + 1

      if ( n - 2 < j ):
        check = False
        return check
#
#  Delete the edge.
#
    t2[0,j] = - t2[0,j]
    t2[1,j] = - t2[1,j]

    d[x-1] = d[x-1] - 1
    d[y-1] = d[y-1] - 1

  return True

def tree_check_test ( ):

#*****************************************************************************80
#
## TREE_CHECK_TEST tests TREE_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'TREE_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TREE_CHECK checks a tree.' )
  print ( '' )
  print ( '  Check?   N    T(1:N)' )
  print ( '' )
  
  for test in range ( 1, 5 ):

    if ( test == 1 ):

      n = 0
      t = np.array ( [ \
        [], \
        [] ], dtype = np.int32 )

    elif ( test == 2 ):

      n = 3
      t = np.array ( [ \
        [ 1, 2 ], \
        [ 2, 3 ] ], dtype = np.int32 )

    elif ( test == 3 ):

      n = 5
      t = np.array ( [ 
        [ 1, 3, 4, 5 ], \
        [ 2, 4, 5, 3 ] ], dtype = np.int32 )

    elif ( test == 4 ):

      n = 6
      t = np.array ( [ \
        [ 1, 2, 3, 4, 5 ], \
        [ 3, 3, 4, 5, 6 ] ], dtype = np.int32 )

    print ( '' )
    check = tree_check ( n, t )
    print ( '      Check = %s' % ( check ) )
    i4mat_print ( 2, n - 1, t, '  Tree:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TREE_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tree_check_test ( )
  timestamp ( )
 
