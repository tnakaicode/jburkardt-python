#! /usr/bin/env python3
#
def mesh_etoe_test ( ):

#*****************************************************************************80
#
## mesh_etoe_test() tests mesh_etoe().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mesh_etoe_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mesh_etoe().' )

  boxy_test ( )
  pool_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mesh_etoe_test():' )
  print ( '  Normal end of execution.' )

  return

def boxy_test ( ):

#*****************************************************************************80
#
## boxy_test() tests mesh_etoe() on a triangulation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'boxy_test():' )
  print ( '  mesh_etoe() is applied to a triangulation.' )
#
#  Load the ETOV information.
#
  etov = np.loadtxt ( 'boxy_elements.txt', dtype = int )
#
#  Decrease each vertex index by 1.
#
  etov = etov - 1
#
#  Get the ETOE information.
#
  etoe = mesh_etoe ( etov )
#
#  Display ETOE.
#
  print ( '' )
  print ( '  ETOE' )
  print ( '' )
  print ( etoe )

  return

def mesh_etoe ( etov ):

#*****************************************************************************80
#
## mesh_etoe() determines the element-to-element connectivity.
#
#  Discussion:
#
#    A triangulation of a set of nodes can be completely described by
#    the coordinates of the nodes, and the list of nodes that make up
#    each triangle.  However, in some cases, it is necessary to know
#    triangle adjacency information, that is, which triangle, if any,
#    is adjacent to a given triangle on a particular side.
#
#    This routine creates a data structure recording this information.
#
#    The primary amount of work occurs in sorting a list of 3 * TRIANGLE_NUM
#    data items.
#
#    This routine was modified to use columns instead of rows.
#
#  Example:
#
#    The input information from ETOV:
#
#    E           ETOV
#    --------   ---------------
#     1         3      4      1
#     2         3      1      2
#     3         3      2      8
#     4         2      1      5
#     5         8      2     13
#     6         8     13      9
#     7         3      8      9
#     8        13      2      5
#     9         9     13      7
#    10         7     13      5
#    11         6      7      5
#    12         9      7      6
#    13        10      9      6
#    14         6      5     12
#    15        11      6     12
#    16        10      6     11
#
#    The output information in TRIANGLE_NEIGHBOR:
#
#    E          Neighboring E
#    --------  ---------------------
#
#     1        -1     -1      2
#     2         1      4      3
#     3         2      5      7
#     4         2     -1      8
#     5         3      8      6
#     6         5      9      7
#     7         3      6     -1
#     8         5      4     10
#     9         6     10     12
#    10         9      8     11
#    11        12     10     14
#    12         9     11     13
#    13        -1     12     16
#    14        11     -1     15
#    15        16     14     -1
#    16        13     15     -1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ETOV(E_NUM,E_ORDER), the nodes that make up each element.
#
#  Output:
#
#    integer ETOE(E_NUM,E_ORDER), the elements incident on a given element. 
#    ETOE(5,0) is the index of the element which touches element 5 on side 0.
#
  import numpy as np

  e_num, e_order = etov.shape
#
#  Step 1.
#  From the list of vertices for element E, of the form: (V1,V2,...VO)
#  construct the neighbor relations:
#
#    (VO,V1,1,E)
#    (V1,V2,2,E)
#    (V2,V3,3,E)
#    ...
#    (VO-1,VO,O,E)
#
#  but sort the first two components.
#
  r = np.zeros ( [ e_order * e_num, 4 ], dtype = int )
  
  row = 0

  for e in range ( 0, e_num ):

    v2 = etov[e,e_order-1]

    for o in range ( 0, e_order ):

      v1 = v2
      v2 = etov[e,o]
      r[row,0] = min ( v1, v2 )
      r[row,1] = max ( v1, v2 )
      r[row,2] = o
      r[row,3] = e
      row = row + 1
#
#  Step 2. Sort the data.  Compare MATLAB "sortrows()".
#
  r = r[np.lexsort(r.T[::-1])]
#
#  Step 3. Neighboring elements show up as consecutive rows with
#  identical first two entries.
#
  etoe = - np.ones ( [ e_num, e_order ] )

  row = 0

  while ( True ):

    if ( e_num * e_order <= row + 1 ):
      break

    if ( ( r[row,0] != r[row+1,0] ) or ( r[row,1] != r[row+1,1] ) ):
      row = row + 1
    else:
      s1 = r[row,2]
      e1 = r[row,3]
      s2 = r[row+1,2]
      e2 = r[row+1,3]
      etoe[e1,s1] = e2
      etoe[e2,s2] = e1
      row = row + 2 

  return etoe

def pool_test ( ):

#*****************************************************************************80
#
## pool_test() tests mesh_etoe() on a quadrilateral mesh.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pool_test():' )
  print ( '  mesh_etoe() is applied to a quadrilateral mesh.' )
#
#  Load the ETOV information.
#
  etov = np.loadtxt ( 'pool_elements.txt', dtype = int )
#
#  Decrease each vertex index by 1.
#
  etov = etov - 1
#
#  Get the ETOE information.
#
  etoe = mesh_etoe ( etov )
#
#  Display ETOE.
#
  print ( '' )
  print ( '  ETOE' )
  print ( '' )
  print ( etoe )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  mesh_etoe_test ( )
  timestamp ( )

