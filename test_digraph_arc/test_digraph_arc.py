#! /usr/bin/env python3
#
def test_digraph_arc_test ( ):

#*****************************************************************************80
#
## test_digraph_arc_test() tests test_digraph_arc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_digraph_arc_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test test_digraph_arc().' )

  digraph_arc_abc_test ( )
  digraph_arc_abcd_test ( )
  digraph_arc_cycler_test ( )
  digraph_arc_five_test ( )
  digraph_arc_moler_test ( )
  digraph_arc_sauer_test ( )
  digraph_arc_sixty_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_digraph_arc_test():' )
  print ( '  Normal end of execution.' )

  return

def digraph_arc_abc ( ):

#*****************************************************************************80
#
## digraph_arc_abc() returns the arc list for a 3-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(3,2), the arc list.
#
  import numpy as np

  arc_num = 3

  L = np.array ( [ \
    [ 1, 2 ], \
    [ 2, 3 ], \
    [ 3, 1 ] ] )

  L = L - 1

  return L

def digraph_arc_abc_test ( ):

#*****************************************************************************80
#
## digraph_arc_abc_test() tests digraph_arc_abc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_abc_test():' )
  print ( '  Test digraph_arc_abc()' )

  L = digraph_arc_abc ( )

  print ( '' )
  print ( '  "abc" arc list L:' )
  pprint.pprint ( L )

  return

def digraph_arc_abcd ( ):

#*****************************************************************************80
#
## digraph_arc_abcd() returns the arc list for a 4-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(5,2), the arc list.
#
  import numpy as np

  arc_num = 5

  L = np.array ( [ \
    [ 1, 2 ], \
    [ 2, 3 ], \
    [ 3, 1 ], \
    [ 3, 4 ], \
    [ 4, 1 ] ] )

  L = L - 1

  return L

def digraph_arc_abcd_test ( ):

#*****************************************************************************80
#
## digraph_arc_abcd_test() tests digraph_arc_abcd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_abcd_test():' )
  print ( '  Test digraph_arc_abcd()' )

  L = digraph_arc_abcd ( )

  print ( '' )
  print ( '  "abcd" arc list L:' )
  pprint.pprint ( L )

  return

def digraph_arc_cycler ( ):

#*****************************************************************************80
#
## digraph_arc_cycler() returns the arc list for a 9-node example.
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
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(16,2), the arc list.
#
  import numpy as np

  arc_num = 16

  L = np.array ( [ \
    [ 1, 3 ], \
    [ 1, 5 ], \
    [ 2, 6 ], \
    [ 2, 8 ], \
    [ 3, 4 ], \
    [ 3, 6 ], \
    [ 3, 7 ], \
    [ 4, 3 ], \
    [ 5, 2 ], \
    [ 6, 5 ], \
    [ 6, 8 ], \
    [ 7, 7 ], \
    [ 7, 9 ], \
    [ 8, 1 ], \
    [ 9, 5 ], \
    [ 9, 7 ] ] )

  L = L - 1

  return L

def digraph_arc_cycler_test ( ):

#*****************************************************************************80
#
## digraph_arc_cycler_test() tests digraph_arc_cycler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_cycler_test():' )
  print ( '  Test digraph_arc_cycler()' )

  L = digraph_arc_cycler ( )

  print ( '' )
  print ( '  "cycler" arc list L:' )
  pprint.pprint ( L )

  return

def digraph_arc_five ( ):

#*****************************************************************************80
#
## digraph_arc_five() returns the arc list for a 5-node example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(5,2), the arc list.
#
  import numpy as np

  arc_num = 5

  L = np.array ( [ \
    [ 1, 2 ], \
    [ 2, 5 ], \
    [ 3, 1 ], \
    [ 4, 1 ], \
    [ 5, 1 ] ] )

  return L

def digraph_arc_five_test ( ):

#*****************************************************************************80
#
## digraph_arc_five_test() tests digraph_arc_five().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_five_test():' )
  print ( '  Test digraph_arc_five()' )

  L = digraph_arc_five ( )

  print ( '' )
  print ( '  "five" arc list L:' )
  pprint.pprint ( L )

  return

def digraph_arc_moler ( ):

#*****************************************************************************80
#
## digraph_arc_moler() returns the arc list for a network of Moler.
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
#    25 April 2026
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
#    integer L(10,2), the arc list.
#
  import numpy as np

  arc_num = 10

  L = np.array ( [ \
    [ 1, 2 ], \
    [ 1, 6 ], \
    [ 2, 3 ], \
    [ 2, 4 ], \
    [ 3, 4 ], \
    [ 3, 5 ], \
    [ 3, 6 ], \
    [ 4, 1 ], \
    [ 5, 5 ], \
    [ 6, 1 ] ] )

  L = L - 1

  return L

def digraph_arc_moler_test ( ):

#*****************************************************************************80
#
## digraph_arc_moler_test() tests digraph_arc_moler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_moler_test():' )
  print ( '  Test digraph_arc_moler()' )

  L = digraph_arc_moler ( )

  print ( '' )
  print ( '  Moler arc list L:' )
  pprint.pprint ( L )

  return

def digraph_arc_sauer ( ):

#*****************************************************************************80
#
## digraph_arc_sauer() returns the arc list for the Sauer example.
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
#    25 April 2026
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
#    integer L(34,2), the arc list.
#
  import numpy as np

  arc_num = 34

  L = np.array ( [ \
   [ 5,  1 ], \
   [ 1,  2 ], \
   [ 3,  2 ], \
   [ 2,  3 ], \
   [ 4,  3 ], \
   [ 8,  4 ], \
   [ 2,  5 ], \
   [ 9,  5 ], \
   [ 3,  6 ], \
   [ 9,  6 ], \
   [ 2,  7 ], \
   [12,  7 ], \
   [ 3,  8 ], \
   [12,  8 ], \
   [ 1,  9 ], \
   [13,  9 ], \
   [ 5, 10 ], \
   [ 6, 10 ], \
   [ 7, 10 ], \
   [ 9, 10 ], \
   [14, 10 ], \
   [ 6, 11 ], \
   [ 7, 11 ], \
   [ 8, 11 ], \
   [12, 11 ], \
   [14, 11 ], \
   [ 4, 12 ], \
   [15, 12 ], \
   [10, 13 ], \
   [14, 13 ], \
   [13, 14 ], \
   [15, 14 ], \
   [11, 15 ], \
   [14, 15 ] ] )

  L = L - 1

  return L

def digraph_arc_sauer_test ( ):

#*****************************************************************************80
#
## digraph_arc_sauer_test() tests digraph_arc_sauer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_sauer_test()' )
  print ( '  Test digraph_arc_sauer()' )

  L = digraph_arc_sauer ( )

  print ( '' )
  print ( '  Sauer arc list L:' )
  pprint.pprint ( L )

  return

def digraph_arc_sixty ( ):

#*****************************************************************************80
#
## digraph_arc_sixty() sets the arc list for the sixty digraph.
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
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(54,2), the arc list.
#
  import numpy as np

  node_num = 12
  arc_num = 54
  L = np.zeros ( [ arc_num, 2 ], dtype = int )

  d = np.array ( [ 60, 30, 20, 15, 12, 10, 6, 5, 4, 3, 2, 1 ], dtype = int )

  arc_id = 0
  for i in range ( 0, node_num ):
    for j in range ( 0, node_num ):
      if ( ( d[i] % d[j] ) == 0 ):
        L[arc_id,0] = i
        L[arc_id,1] = j
        arc_id = arc_id + 1

  return L

def digraph_arc_sixty_test ( ):

#*****************************************************************************80
#
## digraph_arc_sixty_test() tests digraph_arc_sixty().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'digraph_arc_sixty_test():' )
  print ( '  Test digraph_arc_sixty()' )

  L = digraph_arc_sixty ( )

  print ( '' )
  print ( '  "sixty" arc list L:' )
  pprint.pprint ( L )

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
  test_digraph_arc_test ( )
  timestamp ( )


