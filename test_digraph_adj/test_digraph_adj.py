#! /usr/bin/env python3
#
def test_digraph_adj_test ( ):

#*****************************************************************************80
#
## test_digraph_adj_test() tests test_digraph_adj().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_digraph_adj_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test test_digraph_adj().' )

  digraph_adj_example_abc_test ( )
  digraph_adj_example_abcd_test ( )
  digraph_adj_example_cycler_test ( )
  digraph_adj_example_five_test ( )
  digraph_adj_example_moler_test ( )
  digraph_adj_example_sauer_test ( )
  digraph_adj_example_sixty_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_digraph_adj_test():' )
  print ( '  Normal end of execution.' )

  return

def digraph_adj_example_abc ( ):

#*****************************************************************************80
#
## digraph_adj_example_abc() returns the adjacency matrix for a 3-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(3,3), the adjacency matrix.
#
  import numpy as np

  node_num = 3

  A = np.array ( [ \
    [ 0, 1, 0 ], \
    [ 0, 0, 1 ], \
    [ 1, 0, 0 ] ] )

  return A

def digraph_adj_example_abc_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_abc_test() tests digraph_adj_example_abc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_abc_test():' )
  print ( '  Test digraph_adj_example_abc()' )

  A = digraph_adj_example_abc ( )

  print ( '' )
  print ( '  "abc" adjacency matrix A:' )
  pprint.pprint ( A )

  return

def digraph_adj_example_abcd ( ):

#*****************************************************************************80
#
## digraph_adj_example_abcd() returns the adjacency matrix for a 4-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(4,4), the adjacency matrix.
#
  import numpy as np

  node_num = 4

  A = np.array ( [ \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0 ], \
    [ 1, 0, 0, 1 ], \
    [ 1, 0, 0, 0 ] ] )

  return A

def digraph_adj_example_abcd_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_abcd_test() tests digraph_adj_example_abcd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_abcd_test():' )
  print ( '  Test digraph_adj_example_abcd()' )

  A = digraph_adj_example_abcd ( )

  print ( '' )
  print ( '  "abcd" adjacency matrix A:' )
  pprint.pprint ( A )

  return 

def digraph_adj_example_cycler ( ):

#*****************************************************************************80
#
## digraph_adj_example_cycler() returns the adjacency matrix for a 9-node example.
#
#  Diagram:
#  
#           A
#           V
#    9--><--7---<--3--><---4
#    |            /|      /
#    V           A |     /
#    |          /  |    /
#    5----<----1   V   A
#    |        /    |  /
#    V       A     | /
#    |      /      |/
#    2-->---8---<--6
#     \------>----/
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(9,9), the adjacency matrix.
#
  import numpy as np

  node_num = 9

  A = np.array ( [ \
   [ 0,0,1,0,1,0,0,0,0 ], \
   [ 0,0,0,0,0,1,0,1,0 ], \
   [ 0,0,0,1,0,1,1,0,0 ], \
   [ 0,0,1,0,0,0,0,0,0 ], \
   [ 0,1,0,0,0,0,0,0,0 ], \
   [ 0,0,0,1,0,0,0,1,0 ], \
   [ 0,0,0,0,0,0,1,0,1 ], \
   [ 1,0,0,0,0,0,0,0,0 ], \
   [ 0,0,0,0,1,0,1,0,0 ] ] )

  return A

def digraph_adj_example_cycler_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_cycler_test() tests digraph_adj_example_cycler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_cycler_test():' )
  print ( '  Test digraph_adj_example_cycler()' )

  A = digraph_adj_example_cycler ( )

  print ( '' )
  print ( '  "cycler" adjacency matrix A:' )
  pprint.pprint ( A )

  return

def digraph_adj_example_five ( ):

#*****************************************************************************80
#
## digraph_adj_example_five() returns the adjacency matrix for a 5-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(5,5), the adjacency matrix.
#
  import numpy as np

  node_num = 5

  A = np.array ( [ \
    [ 0, 1, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 1 ], \
    [ 1, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0 ] ] )

  return A

def digraph_adj_example_five_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_five_test() tests digraph_adj_example_five().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_five_test():' )
  print ( '  Test digraph_adj_example_five()' )

  A = digraph_adj_example_five ( )

  print ( '' )
  print ( '  "five" adjacency matrix A:' )
  pprint.pprint ( A )

  return

def digraph_adj_example_moler ( ):

#*****************************************************************************80
#
## digraph_adj_example_moler() returns the adjacency matrix for a network of Moler.
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
#    01 March 2020
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

  node_num = 6

  A = np.array ( [ \
    [ 0,1,0,0,0,1 ], \
    [ 0,0,1,1,0,0 ], \
    [ 0,0,0,1,1,1 ], \
    [ 1,0,0,0,0,0 ], \
    [ 0,0,0,0,1,0 ], \
    [ 1,0,0,0,0,0 ] ] )

  return A

def digraph_adj_example_moler_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_moler_test() tests digraph_adj_example_moler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_moler_test():' )
  print ( '  Test digraph_adj_example_moler()' )

  A = digraph_adj_example_moler ( )

  print ( '' )
  print ( '  Moler adjacency matrix A:' )
  pprint.pprint ( A )

  return

def digraph_adj_print ( A, title ):

#*****************************************************************************80
#
## digraph_adj_print() prints an adjacency matrix.
#
#  Discussion:
#
#    This routine actually allows the entries to have ANY value.
#    Values between 0 and 9 will be printed as is.  Other values will
#    be printed as '*'.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,npde_num): the adjacency matrix.  
#
#    character ( len = * ) TITLE: a title.
#
  node_num = A.shape[0]

  print ( title )
  print ( '' )

  for i in range ( 0, node_num ):
    for j in range ( 0, node_num ):
      print (  A[i,j], end = '' )
    print ( '' )

  return

def digraph_adj_example_sauer ( ):

#*****************************************************************************80
#
## digraph_adj_example_sauer() returns the adjacency matrix for the Sauer example.
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
#    28 February 2020
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

  node_num = 15

  A = np.array ( [ \
  [ 0,1,0,0,0,0,0,0,1,0,0,0,0,0,0 ], \
  [ 0,0,1,0,1,0,1,0,0,0,0,0,0,0,0 ], \
  [ 0,1,0,0,0,1,0,1,0,0,0,0,0,0,0 ], \
  [ 0,0,1,0,0,0,0,0,0,0,0,1,0,0,0 ], \
  [ 1,0,0,0,0,0,0,0,0,1,0,0,0,0,0 ], \
  [ 0,0,0,0,0,0,0,0,0,1,1,0,0,0,0 ], \
  [ 0,0,0,0,0,0,0,0,0,1,1,0,0,0,0 ], \
  [ 0,0,0,1,0,0,0,0,0,0,1,0,0,0,0 ], \
  [ 0,0,0,0,1,1,0,0,0,1,0,0,0,0,0 ], \
  [ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0 ], \
  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ], \
  [ 0,0,0,0,0,0,1,1,0,0,1,0,0,0,0 ], \
  [ 0,0,0,0,0,0,0,0,1,0,0,0,0,1,0 ], \
  [ 0,0,0,0,0,0,0,0,0,1,1,0,1,0,1 ], \
  [ 0,0,0,0,0,0,0,0,0,0,0,1,0,1,0 ] ] )

  return A

def digraph_adj_example_sauer_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_sauer_test() tests digraph_adj_example_sauer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_sauer_test()' )
  print ( '  Test digraph_adj_example_sauer()' )

  A = digraph_adj_example_sauer ( )

  print ( '' )
  print ( '  Sauer adjacency matrix A:' )
  pprint.pprint ( A )

  return

def digraph_adj_example_sixty ( ):

#*****************************************************************************80
#
## digraph_adj_example_sixty() sets the adjacency matrix for the sixty digraph.
#
#  Discussion:
#
#    The nodes of the digraph are divisors of 60.  There is a link from I to
#    J if divisor I can be divided by divisor J.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(node_num,node_num), the adjacency information.
#    A(I,J) is 1 if there is a direct link from node I to node J.
#
  import numpy as np

  node_num = 12
  A = np.zeros ( [ node_num, node_num ] )

  d = np.array ( [ 60, 30, 20, 15, 12, 10, 6, 5, 4, 3, 2, 1 ], dtype = int )

  for i in range ( 0, node_num ):
    for j in range ( 0, node_num ):
      if ( i == j ):
        A[i,j] = 0
      elif ( ( d[i] % d[j] ) == 0 ):
        A[i,j] = 1
      else:
        A[i,j] = 0

  return A

def digraph_adj_example_sixty_test ( ):

#*****************************************************************************80
#
## digraph_adj_example_sixty_test() tests digraph_adj_example_sixty().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_adj_example_sixty_test():' )
  print ( '  Test digraph_adj_example_sixty()' )

  A = digraph_adj_example_sixty ( )

  print ( '' )
  print ( '  "sixty" adjacency matrix A:' )
  pprint.pprint ( A )

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
  test_digraph_adj_test ( )
  timestamp ( )


