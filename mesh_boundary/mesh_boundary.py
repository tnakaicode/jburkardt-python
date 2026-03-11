#! /usr/bin/env python3
#
def mesh_boundary ( element_node ):

#*****************************************************************************80
#
## mesh_boundary() determines the segments forming a mesh boundary.
#
#  Discussion:
#
#    This function can be applied to meshes constructed from
#    a number of 2D polygonal elements.  The elements can be a mixture of
#    triangles, quadrilaterals, or other polygons.  In addition,
#    this function can handle a 3D surface meshed by 2D elements.
#
#    The elements can be linear (vertices only), quadratic (extra nodes 
#    along edges), or higher degree.  However, the input to this function
#    should only list the element nodes that lie on the element boundary,
#    and this must be done in counter clockwise order.
#
#    For instance, a quadratic Lagrange element might have the following
#    form:
#
#      80--90-100
#       |       |
#      79  89  99
#       |       |
#      78--88--98
#
#    Assuming this is element #17, then the corresponding entry in the 
#    element node dictionary should be something like:
#
#      17: np.array ( [ 78, 88, 98, 99, 100, 90, 80, 79 ] )
#
#    so that only the nodes on the element boundary are listed, the nodes
#    are listed in counter clockwise order.
#
#    Currently, the program cannot properly report the existence of
#    internal holes in the mesh.
#
#  Example:
#
#    Consider the following simple quadrilateral mesh:
#
#      1---2---3
#      |   |   |
#      4---5---6
#      |   |   |
#      7---8---9
#
#    for which the element array is:
#
#      element_node = [
#        [ 4, 5, 2, 1 ],
#        [ 5, 6, 3, 2 ],
#        [ 7, 8, 5, 4 ],
#        [ 8, 9, 6, 5 ] ]
#
#    This function will return the boundary segments array: 
#
#      boundary_segments = [
#        [ 1, 4 ]
#        [ 4, 7 ],
#        [ 7, 8 ],
#        [ 8, 9 ],
#        [ 9, 6 ],
#        [ 6, 3 ],
#        [ 3, 2 ],
#        [ 2, 1 ] ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer element_node[element_num,element_order]: element_node[i,j]
#    lists the index or label of the j-th node of the i-th element.  
#    If we think of the values as indexes, they can run from 0 to node_num-1,
#    or from 1 to node_num.  But we can also think of them as simply
#    labels, in which case they can be any set of node_num distinct values.
#
#  Output:
#
#    integer boundary_segments[boundary_segment_num,2]: a list of pairs of
#    nodes which define the line segments forming the boundary.  The line
#    segments are given in sequence, so that the boundary is traced in a
#    counter clockwise direction.
#
  import numpy as np

  element_num = len ( element_node )
#
#  Determine the number of segments.
#
  segment_num = 0
  for e in element_node:
    element_order = len ( element_node[e] )
    segment_num = segment_num + element_order
#
#  Break each element into segments.  
#
  segment = np.zeros ( [ segment_num, 2 ] )
  s = 0
  for e in element_node:
    element_order = len ( element_node[e] )
    j = element_order - 1
    for jp1 in range ( 0, element_order ):
      segment[s,0] = element_node[e][j]
      segment[s,1] = element_node[e][jp1]
      s = s + 1
      j = jp1
#
#  Lexically sort the rows of the array.
#
  segment = sortrows ( segment )
#
#  From the list of segments, 
#  find rows that are not matched by a reversed copy.
#  These are the boundary segments.
#
  boundary_segment_num = 0
  boundary_segments = np.zeros ( [ boundary_segment_num, 2 ] )
  for s in range ( 0, segment_num ):
    s0 = segment[s,0]
    s1 = segment[s,1]
    segment[s,0] = s1
    segment[s,1] = s0
    segment2 = np.unique ( segment, axis = 0 )
    if ( segment2.shape[0] == segment_num ):
      boundary_segment_num = boundary_segment_num + 1
      boundary_segments = np.append ( boundary_segments, [ [ s0, s1 ] ], axis = 0 )
    segment[s,0] = s0
    segment[s,1] = s1
#
#  Reorder the segments to form a loop.
#
  for b1 in range ( 0, boundary_segment_num - 1 ):
    for b2 in range ( b1 + 1, boundary_segment_num ):
      if ( boundary_segments[b2,0] == boundary_segments[b1,1] ):
        t0 = boundary_segments[b1+1,0]
        t1 = boundary_segments[b1+1,1]
        boundary_segments[b1+1,0] = boundary_segments[b2,0]
        boundary_segments[b1+1,1] = boundary_segments[b2,1]
        boundary_segments[b2,0] = t0
        boundary_segments[b2,1] = t1
        continue

  return boundary_segments

def mesh_boundary_test ( ):

#*****************************************************************************80
#
## mesh_boundary_test() tests mesh_boundary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mesh_boundary_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mesh_boundary()' )

  mesh_boundary_test_beam ( )
  mesh_boundary_test_ell ( )
  mesh_boundary_test_hole ( )
  mesh_boundary_test_mixed ( )
  mesh_boundary_test_serendipity ( )
  mesh_boundary_test_square ( )
  mesh_boundary_test_tet ( )
  mesh_boundary_test_tube ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mesh_boundary_test():' )
  print ( '  Normal end of execution.' )

  return

def mesh_boundary_test_beam ( ):

#*****************************************************************************80
#
## mesh_boundary_test_beam() tests a beam quadrilateral mesh.
#
#  Discussion:
#
#    This example is available as mfem file beam-quad.mesh
#
#    Consider the following simple quadrilateral mesh:
#
#      9--10--11--12--13--14--15--16--17
#      |   |   |   |   |   |   |   |   |
#      0---1---2---3---4---5---6---7---8
#
#    for which the element array is:
#
#      element_node = [
#        0,  1, 10,  9 ...
#        1,  2, 11, 10 ...
#        2,  3, 12, 11 ...
#        3,  4, 13, 12 ...
#        4,  5, 14, 13 ...
#        5,  6, 15, 14 ...
#        6,  7, 16, 15 ...
#        7,  8, 17, 16 ]
#
#    The boundary segments array should be computed as: 
#
#      boundary_segments = [
#        [  0,  1 ]
#        [  1,  2 ],
#        [  2,  3 ],
#        [  3,  4 ],
#        [  4,  5 ],
#        [  5,  6 ],
#        [  6,  7 ],
#        [  7,  8 ],
#        [  8, 17 ]
#        [ 17, 16 ],
#        [ 16, 15 ],
#        [ 15, 14 ],
#        [ 14, 13 ],
#        [ 13, 12 ],
#        [ 12, 11 ],
#        [ 11, 10 ],
#        [ 10,  9 ],
#        [  9,  0 ] ]
#
#  Licensing:
# 
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_beam():' )
  print ( '  Boundary of a mesh of 8 linear quadrilaterals.' )

  element_node = { \
    0 : np.array ( [ 0,  1, 10,  9 ] ), \
    1 : np.array ( [ 1,  2, 11, 10 ] ), \
    2 : np.array ( [ 2,  3, 12, 11 ] ), \
    3 : np.array ( [ 3,  4, 13, 12 ] ), \
    4 : np.array ( [ 4,  5, 14, 13 ] ), \
    5 : np.array ( [ 5,  6, 15, 14 ] ), \
    6 : np.array ( [ 6,  7, 16, 15 ] ), \
    7 : np.array ( [ 7,  8, 17, 16 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_ell ( ):

#*****************************************************************************80
#
## mesh_boundary_test_ell() tests a triangular mesh.
#
#  Discussion:
#
#    Consider the following triangular mesh of the L-shaped region:
#
#      5--10--15
#      | \ | \ |
#      4---9--14
#      | \ | \ |
#      3---8--13--18--21--24
#      | \ | \ | \ | \ | \ |
#      2---7--12--17--20--23
#      | \ | \ | \ | \ | \ |
#      1---6--11--16--19--22
#
#    for which the element array is:
#
#      element_node = [
#        1,  6,  2
#        7,  2,  6
#        2,  7,  3
#        8,  3,  7
#        3,  8,  4
#        9,  4,  8
#        4,  9,  5
#       10,  5,  9
#        6, 11,  7
#       12,  7, 11
#        7, 12,  8
#       13,  8, 12
#        8, 13,  9
#       14,  9, 13
#        9, 14, 10
#       15, 10, 14
#       11, 16, 12
#       17, 12, 16
#       12, 17, 13
#       18, 13, 17
#       16, 19, 17
#       20, 17, 19
#       17, 20, 18
#       21, 18, 20
#       19, 22, 20
#       23, 20, 22
#       20, 23, 21
#       24, 21, 23 ]
#
#    The boundary segments array should be computed as: 
#
#      boundary_segments = [
#        [  1,  6 ]
#        [  6, 11 ],
#        [ 11, 16 ],
#        [ 16, 19 ],
#        [ 19, 22 ],
#        [ 22, 23 ],
#        [ 23, 24 ],
#        [ 24, 21 ],
#        [ 21, 18 ]
#        [ 18, 13 ],
#        [ 13, 14 ],
#        [ 14, 15 ],
#        [ 15, 10 ],
#        [ 10,  5 ],
#        [  5,  4 ],
#        [  4,  3 ],
#        [  3,  2 ],
#        [  2,  1 ],
#
#  Licensing:
# 
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_ell():' )
  print ( '  Boundary of a mesh of 24 linear triangles.' )

  element_node = { \
    0 : np.array ( [  1,  6,  2 ] ), \
    1 : np.array ( [  7,  2,  6 ] ), \
    2 : np.array ( [  2,  7,  3 ] ), \
    3 : np.array ( [  8,  3,  7 ] ), \
    4 : np.array ( [  3,  8,  4 ] ), \
    5 : np.array ( [  9,  4,  8 ] ), \
    6 : np.array ( [  4,  9,  5 ] ), \
    7 : np.array ( [ 10,  5,  9 ] ), \
    8 : np.array ( [  6, 11,  7 ] ), \
    9 : np.array ( [ 12,  7, 11 ] ), \
   10 : np.array ( [  7, 12,  8 ] ), \
   11 : np.array ( [ 13,  8, 12 ] ), \
   12 : np.array ( [  8, 13,  9 ] ), \
   13 : np.array ( [ 14,  9, 13 ] ), \
   14 : np.array ( [  9, 14, 10 ] ), \
   15 : np.array ( [ 15, 10, 14 ] ), \
   16 : np.array ( [ 11, 16, 12 ] ), \
   17 : np.array ( [ 17, 12, 16 ] ), \
   18 : np.array ( [ 12, 17, 13 ] ), \
   19 : np.array ( [ 18, 13, 17 ] ), \
   20 : np.array ( [ 16, 19, 17 ] ), \
   21 : np.array ( [ 20, 17, 19 ] ), \
   22 : np.array ( [ 17, 20, 18 ] ), \
   23 : np.array ( [ 21, 18, 20 ] ), \
   24 : np.array ( [ 19, 22, 20 ] ), \
   25 : np.array ( [ 23, 20, 22 ] ), \
   26 : np.array ( [ 20, 23, 21 ] ), \
   27 : np.array ( [ 24, 21, 23 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_hole ( ):

#*****************************************************************************80
#
## mesh_boundary_test_hole() tests a quadrilateral mesh with a hole.
#
#  Discussion:
#
#    Consider the following simple quadrilateral mesh:
#
#      1---2---3---4---5
#      |   |   |   |   |
#      6---7---8---9--10
#      |   |       |   |
#     11--12--13  14--15
#      |   |   |   |   |
#     16--17--18--19--20
#      |   |   |   |   |
#     21--22--23--24--25
#
#    for which the element array is:
#
#      element_node = [
#        [  6,  7,  2,  1 ],
#        [  7,  8,  3,  2 ],
#        [  8,  9,  4,  3 ],
#        [  9, 10,  5,  4 ],
#        [ 11, 12,  7,  6 ],
#        [ 14, 15, 10,  9 ],
#        [ 16, 17, 12, 11 ],
#        [ 17, 18, 13, 12 ],
#        [ 19, 20, 15, 14 ],
#        [ 21, 22, 17, 16 ],
#        [ 22, 23, 18, 17 ],
#        [ 23, 24, 19, 18 ],
#        [ 24, 25, 20, 19 ],
#
#    The boundary segments array should be computed as: 
#
#      boundary_segment = [
#        [  1,  6 ]
#        [  6, 11 ],
#        [ 11, 16 ],
#        [ 16, 21 ],
#        [ 21, 22 ],
#        [ 22, 23 ],
#        [ 23, 24 ],
#        [ 24, 25 ],
#        [ 25, 20 ],
#        [ 20, 15 ],
#        [ 15, 10 ],
#        [ 10,  5 ],
#        [  5,  4 ],
#        [  4,  3 ],
#        [  3,  2 ],
#        [  2,  1 ],
#
#     and for the hole (notice clockwise orientation!)
#
#       [  7,  8 ],
#       [  8,  9 ],
#       [  9, 14 ],
#       [ 14, 19 ],
#       [ 19, 18 ],
#       [ 18, 13 ],
#       [ 13, 12 ],
#       [ 12,  7 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_hole():' )
  print ( '  Boundary of mesh of 13 linear quadrilaterals with a hole.' )

  element_node = { \
    0 : np.array ( [  6,  7,  2,  1 ] ), \
    1 : np.array ( [  7,  8,  3,  2 ] ), \
    2 : np.array ( [  8,  9,  4,  3 ] ), \
    3 : np.array ( [  9, 10,  5,  4 ] ), \
    4 : np.array ( [ 11, 12,  7,  6 ] ), \
    5 : np.array ( [ 14, 15, 10,  9 ] ), \
    6 : np.array ( [ 16, 17, 12, 11 ] ), \
    7 : np.array ( [ 17, 18, 13, 12 ] ), \
    8 : np.array ( [ 19, 20, 15, 14 ] ), \
    9 : np.array ( [ 21, 22, 17, 16 ] ), \
   10 : np.array ( [ 22, 23, 18, 17 ] ), \
   11 : np.array ( [ 23, 24, 19, 18 ] ), \
   12 : np.array ( [ 24, 25, 20, 19 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_mixed ( ):

#*****************************************************************************80
#
## mesh_boundary_test_mixed() tests a mixed element mesh.
#
#  Discussion:
#
#    Consider the following mesh:
#
#      1---2---3---4---5---6---7
#      |       | \     |       |
#      8   *   9  10  11      12
#      |       |     \ |       |
#     13--14--15--16--17--18--19
#              |   | /   
#             20--21

#
#    Element #1 is a Q2 quadratic Lagrange element with 9 nodes, but we
#    suppress the interior node.
#    Elements #2 and #3 are quadratic triangles.
#    Element 4 is a serendipity element.
#    Element 5 is a linear quadrilateral.
#    Element 6 is a linear triangle.
#
#    The (ragged) element node array, to be stored as a dictionary, is:
#
#      element_node = [
#        [ 13, 14, 15,  9,  3,  2,  1,  8 ],
#        [ 15, 16, 17, 10,  3,  9 ],
#        [  5,  4,  3, 10, 17, 11 ],
#        [ 17, 18, 19, 12,  7,  6,  5, 11 ],
#        [ 20, 21, 16, 15 ],
#        [ 16, 21, 17 ] ]
#
#    The boundary segments array should be computed as: 
#
#      boundary_segments = [
#        [  1,  8 ],
#        [  8, 13 ]
#        [ 13, 14 ],
#        [ 14, 15 ],
#        [ 15, 20 ]
#        [ 20, 21 ],
#        [ 21, 17 ],
#        [ 17, 18 ],
#        [ 18, 19 ],
#        [ 19, 12 ],
#        [ 12,  7 ],
#        [  7,  6 ],
#        [  6,  5 ],
#        [  5,  4 ],
#        [  4,  3 ],
#        [  3,  2 ],
#        [  2,  1 ] ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_mixed():' )
  print ( '  Boundary of a mesh involving 6 elements of mixed type.' )

  element_node = { \
  0 : np.array ( [ 13, 14, 15,  9,  3,  2,  1,  8 ] ), \
  1 : np.array ( [ 15, 16, 17, 10,  3,  9 ] ), \
  2 : np.array ( [  5,  4,  3, 10, 17, 11 ] ), \
  3 : np.array ( [ 17, 18, 19, 12,  7,  6,  5, 11 ] ), \
  4 : np.array ( [ 20, 21, 16, 15 ] ), \
  5 : np.array ( [ 16, 21, 17 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_serendipity ( ):

#*****************************************************************************80
#
## mesh_boundary_test_serendipity() tests a serendipity mesh.
#
#  Discussion:
#
#    Consider the following mesh:
#
#      1---2---3---4---5
#      |       |       |
#      6       7       8
#      |       |       |
#      9--10--11--12--13
#              |       |
#             14      15
#              |       |
#             16--17--18
#
#    Note that the elements are "quadratic", which in this case means that
#    each edge involves three nodes.
#
#    The element array is:
#
#      element_node = [
#        [  9, 10, 11,  7,  3,  2,  1,  6 ],
#        [ 11, 12, 13,  8,  5,  4,  3,  7 ],
#        [ 16, 17, 18, 15, 13, 12, 11, 14 ] ]
#
#    The boundary segments array should be computed as: 
#
#      boundary_segments = [
#        [  1,  6 ],
#        [  6,  9 ],
#        [  9, 10 ]
#        [ 10, 11 ],
#        [ 11, 14 ],
#        [ 14, 16 ],
#        [ 16, 17 ],
#        [ 17, 18 ],
#        [ 18, 15 ],
#        [ 15, 13 ],
#        [ 13,  8 ],
#        [  8,  5 ],
#        [  5,  4 ],
#        [  4,  3 ],
#        [  3,  2 ],
#        [  2,  1 ] ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_serendipity():' )
  print ( '  Boundary of a mesh of 3 quadratic serendipity elements.' )

  element_node = { \
    0 : np.array ( [  9, 10, 11,  7,  3,  2,  1,  6 ] ), \
    1 : np.array ( [ 11, 12, 13,  8,  5,  4,  3,  7 ] ), \
    2 : np.array ( [ 16, 17, 18, 15, 13, 12, 11, 14 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_square ( ):

#*****************************************************************************80
#
## mesh_boundary_test_square() tests a simple quadrilateral mesh.
#
#  Discussion:
#
#    Consider the following simple quadrilateral mesh:
#
#      1---2---3
#      |   |   |
#      4---5---6
#      |   |   |
#      7---8---9
#
#    for which the element array is:
#
#      element_node = [
#        [ 4, 5, 2, 1 ],
#        [ 5, 6, 3, 2 ],
#        [ 7, 8, 5, 4 ],
#        [ 8, 9, 6, 5 ] ]
#
#    The boundary segments array should be computed as: 
#
#      boundary_segments = [
#        [ 1, 4 ]
#        [ 4, 7 ],
#        [ 7, 8 ],
#        [ 8, 9 ],
#        [ 9, 6 ],
#        [ 6, 3 ],
#        [ 3, 2 ],
#        [ 2, 1 ] ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_square():' )
  print ( '  Boundary of mesh of 4 linear quadrilaterals.' )

  element_node = { \
    0 : np.array ( [ 4, 5, 2, 1 ] ), \
    1 : np.array ( [ 5, 6, 3, 2 ] ), \
    2 : np.array ( [ 7, 8, 5, 4 ] ), \
    3 : np.array ( [ 8, 9, 6, 5 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_tet ( ):

#*****************************************************************************80
#
## mesh_boundary_test_tet() tests a tetrahedron triangular mesh.
#
#  Discussion:
#
#    This example shows how a 3D surface can be defined by a mesh of
#    2D elements.  It also shows that such a surface might have no 
#    boundary.
#
#    Consider the nodes of a tetrahedron, labeled 1, 2, 3, 4,
#    so that the triangular faces can be defined by the following
#    element array:
#
#      element_node = [
#        0,  1, 2, 3,
#        1,  2, 4, 3,
#        2,  4, 1, 3,
#        3,  1, 4, 2 ]
#
#    The (empty) boundary segments array should be computed as: 
#
#      boundary_segments = 
#      [
#        [
#        ]
#      ]
#
#  Licensing:
# 
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_tet():' )
  print ( '  Boundary of a 3D tetrahedron surface mesh of 4 linear triangles.' )

  element_node = { \
    0 : np.array ( [ 1, 2, 3 ] ), \
    1 : np.array ( [ 2, 4, 3 ] ), \
    2 : np.array ( [ 4, 1, 3 ] ), \
    3 : np.array ( [ 1, 4, 2 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

def mesh_boundary_test_tube ( ):

#*****************************************************************************80
#
## mesh_boundary_test_tube() tests a tube quadrilateral mesh.
#
#  Discussion:
#
#    Note that, for technical reasons, the code would fail on this example
#    if there were only 2 horizontal layers, rather than 3.
#
#    This example shows how a 3D surface can be defined by a mesh of
#    2D elements.
#
#    Consider the following simple quadrilateral mesh:
#
#      0---1---2---3---4
#      |   |   |   |   |
#      5---6---7---8---9
#      |   |   |   |   |
#     10--11--12--13--14
#      |   |   |   |   |
#      0---1---2---3---4
#
#    for which the element array is:
#
#      element_node = [
#        0,  5, 6, 1, 0,
#        1,  6, 7, 2, 1,
#        2,  7, 8, 3, 2,
#        3,  8, 9, 4, 3,
#        4, 10,11, 6, 5,
#        5, 11,12, 7, 6,
#        6, 12,13, 8, 7
#        7, 13,14, 9, 8
#        8,  0, 1,11,10,
#        9,  1, 2,12,11,
#       10,  2, 3,13,12
#       11,  3, 4,14,13
#
#    The boundary segments array should be computed as: 
#
#      boundary_segments = 
#      [
#        [
#          [  0,  5 ],
#          [  5, 10 ],
#          [ 10,  0 ]
#        ], 
#        [
#          [  4, 14 ],
#          [ 14,  9 ],
#          [  9,  4 ]
#        ]
#      ]
#
#  Licensing:
# 
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'mesh_boundary_test_tube():' )
  print ( '  Boundary of a 3D tube mesh of 8 linear quadrilaterals.' )

  element_node = { \
    0 : np.array ( [  5,  6,  1,  0 ] ), \
    1 : np.array ( [  6,  7,  2,  1 ] ), \
    2 : np.array ( [  7,  8,  3,  2 ] ), \
    3 : np.array ( [  8,  9,  4,  3 ] ), \
    4 : np.array ( [ 10, 11,  6,  5 ] ), \
    5 : np.array ( [ 11, 12,  7,  6 ] ), \
    6 : np.array ( [ 12, 13,  8,  7 ] ), \
    7 : np.array ( [ 13, 14,  9,  8 ] ), \
    8 : np.array ( [  0,  1, 11, 10 ] ), \
    9 : np.array ( [  1,  2, 12, 11 ] ), \
   10 : np.array ( [  2,  3, 13, 12 ] ), \
   11 : np.array ( [  3,  4, 14, 13 ] ) }

  print ( '' )
  print ( '  element_node array:' )
  pp = pprint.PrettyPrinter ( indent = 4 )
  pp.pprint ( element_node )

  boundary_segments = mesh_boundary ( element_node )

  print ( '' )
  print ( '  boundary segments returned by mesh_boundary():' )
  print ( boundary_segments )

  return

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

def sortrows_test ( ):

#*****************************************************************************80
#
## sortrows_test() tests sortrows().
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
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'sortrows_test():' )
  print ( '  sortrows() lexically sorts the rows of an array.' )
  print ( '' )
  x = rng.integers ( low = 1, high = 10, size = [ 10, 3 ], endpoint = True )
  print ( '' )
  print ( '  Initial array:' )
  print ( x )

  x = sortrows ( x )

  print ( '' )
  print ( '  Array after sortrows() was applied:' )
  print ( x )

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
  mesh_boundary_test ( )
  timestamp ( )

