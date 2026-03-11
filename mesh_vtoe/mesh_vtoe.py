#! /usr/bin/env python3
#
def mesh_vtoe_test ( ):

#*****************************************************************************80
#
## mesh_vtoe_test() tests mesh_vtoe().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mesh_vtoe_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mesh_vtoe().' )

  boxy_test ( )
  pool_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mesh_vtoe_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def mesh_vtoe ( e_order, e_num, etov, v_num ):

#*****************************************************************************80
#
## mesh_vtoe() determines vertex-to-element information.
#
#  Discussion:
#
#    The input information from ETOV:
#
#    E_ORDER = 3
#    E_NUM = 16
#    V_NUM = 13
#
#    E          ETOV
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
#    The output information in VTOE_POINTER(V_NUM+1), VTOE(E_ORDER*E_NUM):
#
#    V   VTOE_POINTER   VTOE
#    --  ------------   -------
#
#     1         1        1
#                        2
#                        4
#     2         4        2
#                        3
#                        4
#                        5
#                        8
#     3         9        1
#                        2
#                        3
#                        7
#     4        13        1
#     5        14        4
#                        8
#                       10
#                       11
#                       14
#     6        19       11
#                       12
#                       13
#                       14
#                       15
#                       16
#     7        25        9
#                       10
#                       11
#                       12
#     8        29        3
#                        5
#                        6
#                        7
#     9        33        6
#                        7
#                        9
#                       12
#                       13
#    10        38       13
#                       16
#    11        40       15
#                       16
#    12        42       14
#                       15
#    13        44        5
#                        6 
#                        8
#                        9
#                       10
#              49
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E_ORDER, the order of the elements.
#
#    integer E_NUM, the number of elements.
#
#    integer ETOV(E_ORDER,E_NUM), the vertices that 
#    make up each element.
#
#    integer V_NUM, the number of vertices.
#
#  Output:
#
#    integer VTOE_POINTER(V_NUM+1), a pointer into the
#    array VTOE.  Information for node V is stored in VTOE entries
#    VTOE_POINTER(V) through VTOE_POINTER(V+1)-1.
#
#    integer VTOE(E_ORDER*E_NUM), the elements that contain each vertex.
#
  import numpy as np
#
#  Step 1.
#  From ETOV, create a list of pairs (V,E).
#
  ve = np.zeros ( [ e_order * e_num, 2 ], dtype = int )

  k = 0
  for e in range ( 0, e_num ):
    for o in range ( 0, e_order ):
      ve[k,0] = etov[o,e]
      ve[k,1] = e
      k = k + 1
#
#  Sort the rows of VE.
#
  ve = sortrows ( ve ) 
#
#  STEP 2:
#  Create the pointer array.
#  (Some of this coding is done this way to allow for the case where
#  some nodes are not used.  They still need an entry VTOE_POINTER.)
#
  vtoe_pointer = np.zeros ( v_num + 1, dtype = int )

  old = 0
  for k in range ( 0, e_order * e_num ):
    new = ve[k,0]
    if ( new != old ):
      for v in range ( old + 1, new + 1 ):
        vtoe_pointer[v] = k
      old = new
  vtoe_pointer[v_num] = e_order * e_num
#
#  STEP 3:
#  Create VTOE.
#
  vtoe = np.zeros ( e_order * e_num )

  vtoe[0:e_order * e_num] = ve[0:e_order * e_num,1]

  return vtoe_pointer, vtoe

def sortrows ( x ):

#*****************************************************************************80
#
## sortrows() lexically sorts the rows of an array.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    array x[]: the array to be sorted.
#
#  Output:
#
#    array x[]: the sorted array.
#
  import numpy as np

  x = x[ np.lexsort ( x.T[::-1] ) ]

  return x

def boxy_test ( ):

#*****************************************************************************80
#
## boxy_test() tests mesh_vtoe().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'boxy_test():' )
  print ( '  Test mesh_vtoe() on the boxy mesh data.' )
#
#  Load the ETOV information.
#
  etov = np.loadtxt ( 'boxy_elements.txt' )
  etov = etov.T
  etov = etov.astype ( int )
  element_order = etov.shape[0]
  element_num = etov.shape[1]
#
#  Assume that the number of vertices is the same as the maximum
#  vertex index.
#
  v_base = np.min ( etov )
  v_num = np.max ( etov )

  if ( v_base == 0 ):
    v_num = v_num + 1
#
#  Get the VTOE information.
#
  vtoe_pointer, vtoe = mesh_vtoe ( element_order, element_num, etov, v_num )
#
#  Display VTOE_POINTER.
#
  print ( '' )
  print ( '  VTOE_POINTER' )
  print ( '' )
  for v in range ( 0, v_num + 1 ):
    print ( '  %3d:  %4d' % ( v, vtoe_pointer[v] ) )
#
#  Display VTOE.
#
  print ( '' )
  print ( '  VTOE' )
  print ( '' )
  for v in range ( 0, v_num ):
    print ( '  %3d:  ' % ( v ), end = '' )
    for k in range ( vtoe_pointer[v], vtoe_pointer[v+1] ):
      print ( ' %d' % ( vtoe[k] ), end = '' )
    print ( '' )

  return

def pool_test ( ):

#*****************************************************************************80
#
## pool_test() tests mesh_vtoe().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pool_test():' )
  print ( '  Test mesh_vtoe() on the quadrilateral pool mesh data.' )
#
#  Load the ETOV information.
#
  etov = np.loadtxt ( 'pool_elements.txt' )
  etov = etov.T
  etov = etov.astype ( int )
  element_order = etov.shape[0]
  element_num = etov.shape[1]
#
#  Assume that the number of vertices is the same as the maximum
#  vertex index.
#
  v_base = np.min ( etov )
  v_num = np.max ( etov )

  if ( v_base == 0 ):
    v_num = v_num + 1
#
#  Get the VTOE information.
#
  vtoe_pointer, vtoe = mesh_vtoe ( element_order, element_num, etov, v_num )
#
#  Display VTOE_POINTER.
#
  print ( '' )
  print ( '  VTOE_POINTER' )
  print ( '' )
  for v in range ( 0, v_num + 1 ):
    print ( '  %3d:  %4d' % ( v, vtoe_pointer[v] ) )
#
#  Display VTOE.
#
  print ( '' )
  print ( '  VTOE' )
  print ( '' )
  for v in range ( 0, v_num ):
    print ( '  %3d:  ' % ( v ), end = '' )
    for k in range ( vtoe_pointer[v], vtoe_pointer[v+1] ):
      print ( ' %d' % ( vtoe[k] ), end = '' )
    print ( '' )

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
  mesh_vtoe_test ( )
  timestamp ( )

