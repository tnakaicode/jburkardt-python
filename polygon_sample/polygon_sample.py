#! /usr/bin/env python3
#
def polygon_sample_test ( ):

#*****************************************************************************80
#
## polygon_sample_test() tests polygon_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'polygon_sample_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polygon_sample()' )

  rng = default_rng ( )

  n = 1000

  v = np.array ( [ \
    [  0,   0 ], \
    [ 10,   7 ], \
    [ 12,   3 ], \
    [ 20,   8 ], \
    [ 13,  17 ], \
    [ 10,  12 ], \
    [ 12,  14 ], \
    [ 14,   9 ], \
    [  8,  10 ], \
    [  6,  14 ], \
    [ 10,  15 ], \
    [  7,  18 ], \
    [  0,  16 ], \
    [  1,  13 ], \
    [  3,  15 ], \
    [  5,   8 ], \
    [ -2,   9 ], \
    [  5,   5 ] ])

  nv = v.shape[0]

  print ( '' )
  print ( '  Number of points N =    ', n )
  print ( '  Number of vertices NV = ', nv )
  print ( '' )
  print ( '  Polygonal vertices:' )
  print ( v )

  p = polygon_sample ( nv, v, n, rng )
  triangles = polygon_triangulate ( nv, v[:,0], v[:,1] )

  for picture in range ( 1, 5 ):

    plt.clf ( )
#
#  Plot sample points.
#
    if ( 4 <= picture ):
      plt.plot ( p[:,0], p[:,1], 'bo', markersize = 2 )
#
#  Plot triangulation lines.
#
    if ( 3 <= picture ):
      for i in range ( 0, nv - 3 ):
        i1 = triangles[i,0]
        i2 = triangles[i,1]
        plt.plot ( [ v[i1,0], v[i2,0] ], \
                   [ v[i1,1], v[i2,1] ], \
                   linewidth = 3, color = 'm' )
#
#  Plot polygon edges.
#
    if ( 2 <= picture ):
      im1 = nv - 1
      for i in range ( 0, nv ):
        plt.plot ( [ v[im1,0], v[i,0] ], \
                   [ v[im1,1], v[i,1] ], 'r-', linewidth = 3 )
        im1 = i
#
#  Plot vertices.
#
    plt.plot ( v[:,0], v[:,1], 'g.', markersize = 15 )

    plt.xlabel ( '<--- X --->' )
    plt.ylabel ( '<--- Y --->' )
    plt.grid ( 'on' )
    plt.axis ( 'equal' )
    if ( picture == 1 ):
      plt.title ( 'polygon vertices' )
      filename = 'polygon_vertices.png'
    elif ( picture == 2 ):
      plt.title ( 'polygon edges' )
      filename = 'polygon_edges.png'
    elif ( picture == 3 ):
      plt.title ( 'polygon triangulation' )
      filename = 'polygon_triangulation.png'
    else:
      plt.title ( 'polygon sample points' )
      filename = 'polygon_sample.png'

    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_sample_test():' )
  print ( '  Normal end of execution.' )

  return

def angle_degree ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## angle_degree() returns the degree angle defined by three points.
#
#  Discussion:
#
#        P1
#        /
#       /
#      /7
#     /
#    P2--------->P3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X3, Y3, the coordinates of the points
#    P1, P2, P3.
#
#  Output:
#
#    real VALUE, the angle swept out by the rays, measured
#    in degrees.  0 <= VALUE < 360.  If either ray has zero length,
#    then VALUE is set to 0.
#
  import numpy as np

  x = ( x3 - x2 ) * ( x1 - x2 ) + ( y3 - y2 ) * ( y1 - y2 )

  y = ( x3 - x2 ) * ( y1 - y2 ) - ( y3 - y2 ) * ( x1 - x2 )

  if ( x == 0.0 and y == 0.0 ):
    value = 0.0
    return value

  value = np.arctan2 ( y, x )

  if ( value < 0.0 ):
    value = value + 2.0 * np.pi

  value = 180.0 * value / np.pi

  return value

def between ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## between() is TRUE if vertex C is between vertices A and B.
#
#  Discussion:
#
#    The points must be (numerically) collinear.
#
#    Given that condition, we take the greater of XA - XB and YA - YB
#    as a "scale" and check where C's value lies.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the coordinates of 
#    the vertices.
#
#  Output:
#
#    bool VALUE, is TRUE if C is between A and B.
#
  if ( not collinear ( xa, ya, xb, yb, xc, yc ) ):
    value = False
  elif ( abs ( ya - yb ) < abs ( xa - xb ) ):
    xmax = max ( xa, xb )
    xmin = min ( xa, xb )
    value = ( xmin <= xc and xc <= xmax )
  else:
    ymax = max ( ya, yb )
    ymin = min ( ya, yb )
    value = ( ymin <= yc and yc <= ymax )

  return value

def collinear ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## collinear() returns a measure of collinearity for three points.
#
#  Discussion:
#
#    In order to deal with collinear points whose coordinates are not
#    numerically exact, we compare the area of the largest square
#    that can be created by the line segment between two of the points
#    to (twice) the area of the triangle formed by the points.
#
#    If the points are collinear, their triangle has zero area.
#    If the points are close to collinear, then the area of this triangle
#    will be small relative to the square of the longest segment.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2016
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the coordinates of 
#    the vertices.
#
#  Output:
#
#    bool VALUE, is TRUE if the points are judged 
#    to be collinear.
#
  r8_eps = 2.220446049250313E-016

  area = triangle_area ( xa, ya, xb, yb, xc, yc )

  side_ab_sq = ( xa - xb ) ** 2 + ( ya - yb ) ** 2
  side_bc_sq = ( xb - xc ) ** 2 + ( yb - yc ) ** 2
  side_ca_sq = ( xc - xa ) ** 2 + ( yc - ya ) ** 2

  side_max_sq = max ( side_ab_sq, max ( side_bc_sq, side_ca_sq ) )

  if ( side_max_sq <= r8_eps ):
    value = True
  elif ( 2.0 * abs ( area ) <= r8_eps * side_max_sq ):
    value = True
  else:
    value = False

  return value

def diagonal ( im1, ip1, n, prev_node, next_node, x, y ):

#*****************************************************************************80
#
## diagonal(): VERTEX(IM1) to VERTEX(IP1) is a proper internal diagonal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer IM1, IP1, the indices of two vertices.
#
#    integer N, the number of vertices.
#
#    integer PREV_NODE(N), the previous neighbor of each vertex.
#
#    integer NEXT_NODE(N), the next neighbor of each vertex.
#
#    real X(N), Y(N), the coordinates of each vertex.
#
#  Output:
#
#    bool VALUE, the value of the test.
#  
  value1 = in_cone ( im1, ip1, n, prev_node, next_node, x, y )
  value2 = in_cone ( ip1, im1, n, prev_node, next_node, x, y )
  value3 = diagonalie ( im1, ip1, n, next_node, x, y )

  value = ( value1 and value2 and value3 )

  return value

def diagonalie ( im1, ip1, n, next_node, x, y ):

#*****************************************************************************80
#
## diagonalie() is true if VERTEX(IM1):VERTEX(IP1) is a proper diagonal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer IM1, IP1, the indices of two vertices.
#
#    integer N, the number of vertices.
#
#    integer NEXT_NODE(N), the next neighbor of each vertex.
#
#    real X(N), Y(N), the coordinates of each vertex.
#
#  Output:
#
#    bool VALUE, the value of the test.
#
  first = im1
  j = first
  jp1 = next_node[first]

  value = True
#
#  For each edge VERTEX(J):VERTEX(JP1) of the polygon:
#
  while ( True ):
#
#  Skip any edge that includes vertex IM1 or IP1.
#
    if ( j == im1 or j == ip1 or jp1 == im1 or jp1 == ip1 ):
      pass
    else:

      value2 = intersect ( \
        x[im1], y[im1], x[ip1], y[ip1], x[j], y[j], x[jp1], y[jp1] )

      if ( value2 ):
        value = False
        break

    j = jp1
    jp1 = next_node[j]

    if ( j == first ):
      break

  return value

def in_cone ( im1, ip1, n, prev_node, next_node, x, y ):

#*****************************************************************************80
#
## in_cone() is TRUE if the diagonal VERTEX(IM1):VERTEX(IP1) is strictly internal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer IM1, IP1, the indices of two vertices.
#
#    integer N, the number of vertices.
#
#    integer PREV_NODE(N), the previous neighbor of each vertex.
#
#    integer NEXT_NODE(N), the next neighbor of each vertex.
#
#    real X(N), Y(N), the coordinates of each vertex.
#
#  Output:
#
#    bool VALUE, the value of the test.
#
  im2 = prev_node[im1]
  i = next_node[im1]

  t1 = triangle_area ( x[im1], y[im1], x[i], y[i], x[im2], y[im2] )

  if ( 0.0 <= t1 ):

    t2 = triangle_area ( x[im1], y[im1], x[ip1], y[ip1], x[im2], y[im2] )
    t3 = triangle_area ( x[ip1], y[ip1], x[im1], y[im1], x[i], y[i] )
    value = ( ( 0.0 < t2 ) and ( 0.0 < t3 ) )

  else:

    t4 = triangle_area ( x[im1], y[im1], x[ip1], y[ip1], x[i], y[i] )
    t5 = triangle_area ( x[ip1], y[ip1], x[im1], y[im1], x[im2], y[im2] )
    value = not ( ( 0.0 <= t4 ) and ( 0.0 <= t5 ) )

  return value

def intersect ( xa, ya, xb, yb, xc, yc, xd, yd ):

#*****************************************************************************80
#
## intersect() is true if lines VA:VB and VC:VD intersect.
#
#  Discussion:
#
#    Thanks to Gene Dial for correcting the call to intersect_prop(),
#    08 September 2016.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2016
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y 
#    coordinates of the four vertices.
#
#  Output:
#
#    bool VALUE, the value of the test.
#
  if ( intersect_prop ( xa, ya, xb, yb, xc, yc, xd, yd ) ):
    value = True
  elif ( between ( xa, ya, xb, yb, xc, yc ) ):
    value = True
  elif ( between ( xa, ya, xb, yb, xd, yd ) ):
    value = True
  elif ( between ( xc, yc, xd, yd, xa, ya ) ):
    value = True
  elif ( between ( xc, yc, xd, yd, xb, yb ) ):
    value = True
  else:
    value = False

  return value

def intersect_prop ( xa, ya, xb, yb, xc, yc, xd, yd ):

#*****************************************************************************80
#
## intersect_prop() is TRUE if lines VA:VB and VC:VD have a proper intersection.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    FORTRAN90 version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y 
#    coordinates of the four vertices.
#
#  Output:
#
#    bool VALUE, the result of the test.
#
  if ( collinear ( xa, ya, xb, yb, xc, yc ) ):
    value = False
  elif ( collinear ( xa, ya, xb, yb, xd, yd ) ):
    value = False
  elif ( collinear ( xc, yc, xd, yd, xa, ya ) ):
    value = False
  elif ( collinear ( xc, yc, xd, yd, xb, yb ) ):
    value = False
  else:
    t1 = triangle_area ( xa, ya, xb, yb, xc, yc )
    t2 = triangle_area ( xa, ya, xb, yb, xd, yd )
    t3 = triangle_area ( xc, yc, xd, yd, xa, ya )
    t4 = triangle_area ( xc, yc, xd, yd, xb, yb )

    value1 = ( 0.0 < t1 )
    value2 = ( 0.0 < t2 )
    value3 = ( 0.0 < t3 )
    value4 = ( 0.0 < t4 )

    value = ( l4_xor ( value1, value2 ) ) and ( l4_xor ( value3, value4 ) )
 
  return value

def l4_xor ( l1, l2 ):

#*****************************************************************************80
#
## l4_xor() returns the exclusive OR of two L4's.
#
#  Discussion:
#
#    An L4 is a logical value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#   John Burkardt
#
#  Input:
#
#    bool L1, L2, two values whose exclusive OR 
#    is needed.
#
#  Output:
#
#    bool VALUE, the exclusive OR of L1 and L2.
#
  value1 = (       l1   and ( not l2 ) )
  value2 = ( ( not l1 ) and       l2   )

  value = ( value1 or value2 )

  return value

def polygon_area ( n, x, y ):

#*****************************************************************************80
#
## polygon_area() returns the area of a polygon.
#
#  Discussion:
#
#    The vertices should be listed in counter-clockwise order so that
#    the area will be positive.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2016
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of vertices.
#
#    real X(N), Y(N), the vertex coordinates.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
  area = 0.0
  im1 = n - 1

  for i in range ( 0, n ):
    area = area + x[im1] * y[i] - x[i] * y[im1]
    im1 = i

  area = 0.5 * area

  return area

def polygon_sample ( nv, v, n, rng ):

#*****************************************************************************80
#
## polygon_sample() uniformly samples a polygon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NV, the number of vertices.
#
#    real V(NV,2), the vertices of the polygon, listed in
#    counterclockwise order.
#
#    integer N, the number of points to create.
#
#    rng: the random number generator.
#
#  Output:
#
#    real S(2,N), the points.
#
  import numpy as np
#
#  Triangulate the polygon.
#
  x = np.zeros ( nv )
  y = np.zeros ( nv )
  for j in range ( 0, nv ):
    x[j] = v[j,0]
    y[j] = v[j,1]

  triangles = polygon_triangulate ( nv, x, y )
#
#  Determine the areas of each triangle.
#
  area_triangle = np.zeros ( nv - 2 )

  area_polygon = 0.0
  for i in range ( 0, nv - 2 ):
    area_triangle[i] = triangle_area ( \
      v[triangles[i,0],0], v[triangles[i,0],1], \
      v[triangles[i,1],0], v[triangles[i,1],1], \
      v[triangles[i,2],0], v[triangles[i,2],1] )
    area_polygon = area_polygon + area_triangle[i]
#
#  Normalize the areas.
#
  area_relative = np.zeros ( nv - 1 )

  for i in range ( 0, nv - 2 ):
    area_relative[i] = area_triangle[i] / area_polygon
#
#  Replace each area by the sum of itself and all previous ones.
#
  area_cumulative = np.zeros ( nv - 2 )

  area_cumulative[0] = area_relative[0]
  for i in range ( 1, nv - 2 ):
    area_cumulative[i] = area_relative[i] + area_cumulative[i-1]

  s = np.zeros ( [ n, 2 ] )

  for j in range ( 0, n ):
#
#  Choose triangle I at random, based on areas.
#
    area_percent = rng.random ( )

    for k in range ( 0, nv - 2 ):

      i = k

      if ( area_percent <= area_cumulative[k] ):
        break
#
#  Now choose a point at random in triangle I.
#
    r = rng.random ( size = 2 )

    if ( 1.0 < r[0] + r[1] ):
      r[0] = 1.0 - r[0]
      r[1] = 1.0 - r[1]

    s[j,0] = ( 1.0 - r[0] - r[1] ) * v[triangles[i,0],0] \
                   + r[0]          * v[triangles[i,1],0] \
                          + r[1]   * v[triangles[i,2],0]

    s[j,1] = ( 1.0 - r[0] - r[1] ) * v[triangles[i,0],1] \
                   + r[0]          * v[triangles[i,1],1] \
                          + r[1]   * v[triangles[i,2],1]

  return s

def polygon_triangulate ( n, x, y ):

#******************************************************************************/
#
## polygon_triangulate() determines a triangulation of a polygon.
#
#  Discussion:
#
#    There are N-3 triangles in the triangulation.
#
#    For the first N-2 triangles, the first edge listed is always an
#    internal diagonal.
#
#    Thanks to Gene Dial for pointing out a mistake in the area calculation,
#    10 September 2016.
#
#    Thanks to Gene Dial for suggesting that the next() array should be
#    renamed next_node() to avoid the Python keyword next, 22 September 2016.
#
#    Gene Dial requested an angle tolerance of about 1 millionth radian or 
#    5.7E-05 degrees, 26 June 2018.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2025
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    This version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer N, the number of vertices.
#
#    real X[N], Y[N], the coordinates of each vertex.
#
#  Output:
#
#    integer TRIANGLES[N-2,3], the triangles.
#
  import numpy as np

  angle_tol = 5.7E-05
#
#  We must have at least 3 vertices.
#
  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_triangulate(): Fatal error!' )
    print ( '  N < 3' )
    raise Exception ( 'polygon_triangulate(): Fatal error!' )
#
#  Consecutive vertices cannot be equal.
#
  node_m1 = n - 1
  for node in range ( 0, n ):
    if ( x[node_m1] == x[node] and y[node_m1] == y[node] ):
      print ( '' )
      print ( 'polygon_triangulate(): Fatal error!' )
      print ( '  Two consecutive nodes are identical.' )
      raise Exception ( 'polygon_triangulate(): Fatal error!' )

    node_m1 = node
#
#  No node can be the vertex of an angle less than 1 degree 
#  in absolute value.
#
  node1 = n - 1

  for node2 in range ( 0, n ):

    node3 = ( ( node2 + 1 ) % n )

    angle = angle_degree ( \
      x[node1], y[node1], \
      x[node2], y[node2], \
      x[node3], y[node3] )

    if ( abs ( angle ) <= angle_tol ):
      print ( '' )
      print ( 'polygon_triangulate(): Fatal error!' )
      print ( '  Polygon has an angle %g smaller than %g degrees.' \
        % ( angle, angle_tol ) )
      print ( '  occurring at node %d' % ( node2 ) )
      raise Exception ( 'polygon_triangulate(): Fatal error!' )

    node1 = node2
#
#  Area must be positive.
#
  area = polygon_area ( n, x, y )

  if ( area <= 0.0 ):
    print ( '' )
    print ( 'polygon_triangulate(): Fatal error!' )
    print ( '  Polygon has zero or negative area.' )
    raise Exception ( 'polygon_triangulate(): Fatal error!' )

  triangles = np.zeros ( [ n - 2,  3 ], dtype = np.int32 )
#
#  PREV_NODE and NEXT_NODE point to the previous and next nodes.
#
  prev_node = np.zeros ( n, dtype = np.int32 )
  next_node = np.zeros ( n, dtype = np.int32 )

  i = 0
  prev_node[i] = n - 1
  next_node[i] = i + 1

  for i in range ( 1, n - 1 ):
    prev_node[i] = i - 1
    next_node[i] = i + 1

  i = n - 1
  prev_node[i] = i - 1
  next_node[i] = 0
#
#  EAR indicates whether the node and its immediate neighbors form an ear
#  that can be sliced off immediately.
#
  ear = np.zeros ( n, dtype = bool )
  for i in range ( 0, n ):
    ear[i] = diagonal ( prev_node[i], next_node[i], n, prev_node, \
      next_node, x, y )

  triangle_num = 0

  i2 = 0

  while ( triangle_num < n - 3 ):
#
#  If I2 is an ear, gather information necessary to carry out
#  the slicing operation and subsequent "healing".
#
    if ( ear[i2] ):
      i3 = next_node[i2]
      i4 = next_node[i3]
      i1 = prev_node[i2]
      i0 = prev_node[i1]
#
#  Make vertex I2 disappear.
#
      next_node[i1] = i3
      prev_node[i3] = i1
#
#  Update the earity of I1 and I3, because I2 disappeared.
#
      ear[i1] = diagonal ( i0, i3, n, prev_node, next_node, x, y )
      ear[i3] = diagonal ( i1, i4, n, prev_node, next_node, x, y )
#
#  Add the diagonal [I3, I1, I2] to the list.
#
      triangles[triangle_num,0] = i3
      triangles[triangle_num,1] = i1
      triangles[triangle_num,2] = i2
      triangle_num = triangle_num + 1
#
#  Try the next vertex.
#
    i2 = next_node[i2]
#
#  The last triangle is formed from the three remaining vertices.
#
  i3 = next_node[i2]
  i1 = prev_node[i2]

  triangles[triangle_num,0] = i3
  triangles[triangle_num,1] = i1
  triangles[triangle_num,2] = i2
  triangle_num = triangle_num + 1

  return triangles

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

def triangle_area ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## triangle_area() computes the signed area of a triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the coordinates of
#    the vertices of the triangle, given in counterclockwise order.
#
#  Output:
#
#    real VALUE, the signed area of the triangle.
#
  value = 0.5 * ( ( xb - xa ) * ( yc - ya ) - ( xc - xa ) * ( yb - ya ) )

  return value

if ( __name__ == '__main__' ):
  timestamp ( )
  polygon_sample_test ( )
  timestamp ( )

