#! /usr/bin/env python3
#
def angle_rad ( p1, p2, p3 ):

#*****************************************************************************80
#
## angle_rad() returns the angle swept out between two rays.
#
#  Discussion:
#
#    Except for the zero angle case, it should be true that
#
#      ANGLE_RAD(P1,P2,P3) + ANGLE_RAD(P3,P2,P1) = 2 * PI
#
#        P1
#        /
#       /
#      /
#     /
#    P2--------->P3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2), P2(2), P3(2), define the rays
#    P1 - P2 and P3 - P2 which in turn define the angle.
#
#  Output:
#
#    real VALUE, the angle swept out by the rays, measured
#    in radians.  0 <= VALUE < 2*PI.  If either ray has zero length,
#    then VALUE is set to 0.
#
  import numpy as np

  p = np.zeros ( 2 )

  p[0] = ( p3[0] - p2[0] ) * ( p1[0] - p2[0] ) \
       + ( p3[1] - p2[1] ) * ( p1[1] - p2[1] )

  p[1] = ( p3[0] - p2[0] ) * ( p1[1] - p2[1] ) \
       - ( p3[1] - p2[1] ) * ( p1[0] - p2[0] )

  if ( p[0] == 0.0 and p[1] == 0.0 ):
    value = 0.0
    return value

  value = np.arctan2 ( p[1], p[0] )

  if ( value < 0.0 ):
    value = value + 2.0 * np.pi

  return value

def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test():' )
  print ( '  i4_wrap() forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  i4_wrap(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )

  return

def line_exp_point_dist_signed ( p1, p2, p ):

#*****************************************************************************80
#
## line_exp_point_dist_signed(): signed distance ( explicit line, point ).
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      ( P1, P2 ) = ( (X1,Y1), (X2,Y2) ).
#
#    The signed distance has two interesting properties:
#
#    *  The absolute value of the signed distance is the
#        usual (Euclidean) distance.
#
#    *  Points with signed distance 0 lie on the line,
#       points with a negative signed distance lie on one side
#         of the line,
#       points with a positive signed distance lie on the
#         other side of the line.
#
#    Assuming that C is nonnegative, then if a point is a positive
#    distance away from the line, it is on the same side of the
#    line as the point (0,0), and if it is a negative distance
#    from the line, it is on the opposite side from (0,0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2), P2(2), two points on the line.
#
#    real P(2), the point whose signed distance is desired.
#
#  Output:
#
#    real DIST_SIGNED, the signed distance from the point to the line.
#
  import numpy as np
#
#  If the explicit line degenerates to a point, the computation is easy.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):

    dist_signed = np.linalg.norm ( p1 - p )
#
#  Convert the explicit line to the implicit form A * X + B * Y + C = 0.
#  This makes the computation of the signed distance  to (X,Y) easy.
#
  else:

    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0] * p1[1] - p1[0] * p2[1]

    dist_signed = ( a * p[0] + b * p[1] + c ) / np.sqrt ( a * a + b * b )

  return dist_signed

def parallelogram_area ( p ):

#*****************************************************************************80
#
## parallelogram_area() computes the area of a parallelogram.
#
#  Discussion:
#
#    A parallelogram is a polygon having four sides, with the property
#    that each pair of opposite sides is paralell.
#
#    Given the first three vertices of the parallelogram,
#    P1, P2, and P3, the fourth vertex must satisfy
#
#      P4 = P1 + ( P3 - P2 )
#
#    This routine uses the fact that the norm of the cross product
#    of two vectors is the area of the parallelogram they form:
#
#      Area = ( P3 - P2 ) x ( P1 - P2 ).
#
#        P4<-----P3
#        /       /
#       /       /
#      P1----->P2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P(4,2), the parallelogram vertices, in counterclockwise order.
#
#  Output:
#
#    real AREA, the (signed) area.
#

#
#  Compute the cross product vector, which only has a single
#  nonzero component.
#
  area = ( p[1,0] - p[0,0] ) * ( p[2,1] - p[0,1] ) \
       - ( p[1,1] - p[0,1] ) * ( p[2,0] - p[0,0] )

  return area

def parallelogram_area_3d ( p ):

#*****************************************************************************80
#
## parallelogram_area_3d() computes the area of a parallelogram in 3D.
#
#  Discussion:
#
#    A parallelogram is a polygon having four sides, with the property
#    that each pair of opposite sides is paralell.
#
#    A parallelogram in 3D must have the property that it is "really"
#    a 2D object, that is, that the four vertices that define it lie
#    in some plane.
#
#    Given the first three vertices of the parallelogram (in 2D or 3D),
#    P1, P2, and P3, the fourth vertex must satisfy
#
#      P4 = P1 + ( P3 - P2 )
#
#    This routine uses the fact that the norm of the cross product
#    of two vectors is the area of the parallelogram they form:
#
#      Area = ( P3 - P2 ) x ( P1 - P2 ).
#
#        P4<-----P3
#        /       /
#       /       /
#      P1----->P2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P[4,3], the parallelogram vertices,
#    given in counterclockwise order.  The fourth vertex is ignored.
#
#  Output:
#
#    real AREA, the area
#
  import numpy as np
#
#  Compute the cross product vector.
#
  cross = np.zeros ( 3 )

  cross[0] = ( p[1,1] - p[0,1] ) * ( p[2,2] - p[0,2] ) \
           - ( p[1,2] - p[0,2] ) * ( p[2,1] - p[0,1] )

  cross[1] = ( p[1,2] - p[0,2] ) * ( p[2,0] - p[0,0] ) \
           - ( p[1,0] - p[0,0] ) * ( p[2,2] - p[0,2] )

  cross[2] = ( p[1,0] - p[0,0] ) * ( p[2,1] - p[0,1] ) \
           - ( p[1,1] - p[0,1] ) * ( p[2,0] - p[0,0] )

  area = np.linalg.norm ( cross )

  return area

def polygon_angles ( n, v ):

#*****************************************************************************80
#
## polygon_angles() computes the interior angles of a polygon.
#
#  Discussion:
#
#    The vertices should be listed in counterclockwise order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V[N,2], the vertices.
#
#  Output:
#
#    real ANGLE(N), the angles of the polygon, in radians.
#
  import numpy as np

  angle = np.zeros ( n )

  if ( n <= 2 ):
    return angle

  for i in range ( 0, n ):

    im1 = ( ( i - 1 ) % n )
    ip1 = ( ( i + 1 ) % n )

    angle[i] = angle_rad ( v[im1,:], v[i,:], v[ip1,:] )

  return angle

def polygon_angles_test ( ):

#*****************************************************************************80
#
## polygon_angles_test() tests polygon_angles().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 3.0, 0.0 ], \
    [ 3.0, 2.0 ], \
    [ 1.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_angles_test():' )
  print ( '  polygon_angles() computes the angles of a polygon.' )

  print ( '' )
  print ( '  Number of polygonal vertices =', n )

  print ( '' )
  print ( '  polygon vertices:' )
  print ( v )

  angle = polygon_angles ( n, v )

  print ( '' )
  print ( '  Polygonal angles in degrees:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %14.6g' % ( i, angle[i] * 180.0 / np.pi ) )

  return

def quadrilateral_angles ( q ):

#*****************************************************************************80
#
## quadrilateral_angles() computes the angles of a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2], the X and Y coordinates
#    of the corners of the quadrilateral.  The corners should be
#    specified in clockwise or counterclockwise order.
#
#  Output:
#
#    real ANGLES(4), the angles of the quadrilateral in radians.
#
  angles = polygon_angles ( 4, q )

  return angles

def quadrilateral_angles_test ( ):

#*****************************************************************************80
#
## quadrilateral_angles_test() tests quadrilateral_angles().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_angles_test():' )
  print ( '  quadrilateral_angles() returns the angles of a quadrilateral' )
  print ( '  in radians.' )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  angles = quadrilateral_angles ( q )
  print ( '' )
  print ( '  angles:' )
  print ( angles )
  print ( '  Angles sum to', np.sum ( angles ) )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  angles = quadrilateral_angles ( q )
  print ( '' )
  print ( '  angles:' )
  print ( angles )
  print ( '  Angles sum to', np.sum ( angles ) )

  q = np.array ( [ \
    [ 0.0,  0.0 ], \
    [ 1.0,  0.0 ], \
    [ 0.25, 0.25 ], \
    [ 0.0,  1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  angles = quadrilateral_angles ( q )
  print ( '' )
  print ( '  angles:' )
  print ( angles )
  print ( '  Angles sum to', np.sum ( angles ) )

  q = np.array ( [ \
    [  0.0, 0.0 ], \
    [  1.0, 0.0 ], \
    [ -0.5, 0.5 ], \
    [  0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  angles = quadrilateral_angles ( q )
  print ( '' )
  print ( '  angles:' )
  print ( angles )
  print ( '  Angles sum to', np.sum ( angles ) )

  return

def quadrilateral_area ( quad ):

#*****************************************************************************80
#
## quadrilateral_area() computes the area of a quadrilateral.
#
#  Discussion:
#
#    This algorithm should be able to handle nonconvex quadrilaterals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real QUAD[4,2], the quadrilateral vertex coordinates in 
#    counter clockwise order.
#
#  Output:
#
#    real AREA, the area of the quadrilateral.
#
  import numpy as np

  area = 0.0
  t = np.zeros ( [ 3, 2 ] )

  t[0:3,0:2] = quad[0:3,0:2]  
  area = area + triangle_area ( t )

  t[0:2,0:2] = quad[2:4,0:2]
  t[  2,0:2] = quad[0  ,0:2]
  
  area = area + triangle_area ( t )

  return area

def quadrilateral_area2 ( q ):

#*****************************************************************************80
#
## quadrilateral_area2() computes the area of a quadrilateral.
#
#  Discussion:
#
#    A quadrilateral is a polygon defined by 4 vertices.
#
#    This algorithm computes the area of the related
#    Varignon parallelogram first.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2]: the vertices, in counter clockwise order.
#
#  Output:
#
#    real AREA, the area of the quadrilateral.
#
  import numpy as np
#
#  Define a parallelogram by averaging consecutive vertices.
#
  p = np.zeros ( [ 4, 2 ] )

  im1 = 3
  for i in range ( 0, 4 ):
    p[i,0:2] = 0.5 * ( q[im1,0:2] + q[i,0:2] )
    im1 = i
#
#  Compute the area.
#
  area = parallelogram_area ( p )
#
#  The quadrilateral's area is twice that of the parallelogram.
#
  area = 2.0 * area

  return area

def quadrilateral_area_test ( ):

#*****************************************************************************80
#
## quadrilateral_area_test() tests quadrilateral_area()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'quadrilateral_area_test():' )
  print ( '  quadrilateral_area()  finds the area of a quadrilateral' )
  print ( '  quadrilateral_area2() finds the area of a quadrilateral' )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  area = quadrilateral_area ( q )

  print ( '' )
  print ( '  quadrilateral_area area is =', area )
 
  area = quadrilateral_area2 ( q )

  print ( '  quadrilateral_area2 area =', area )

  return

def quadrilateral_area_3d ( q ):

#*****************************************************************************80
#
## quadrilateral_area_3d() computes the area of a quadrilateral in 3D.
#
#  Discussion:
#
#    A quadrilateral is a polygon defined by 4 vertices.
#
#    It is assumed that the four vertices of the quadrilateral
#    are coplanar.
#
#    This algorithm computes the area of the related
#    Varignon parallelogram first.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,3], the vertices, specified in counter clockwise order.
#
#  Output:
#
#    real AREA, the area of the quadrilateral.
#
  import numpy as np

  p = np.zeros ( [ 4, 3 ] )
#
#  Define a parallelogram by averaging consecutive vertices.
#
  im1 = 3
  for i in range ( 0, 4 ):
    p[i,:] = 0.5 * ( q[i,:] + q[im1,:] )
    im1 = i
#
#  Compute the area.
#
  area = parallelogram_area_3d ( p )
#
#  The quadrilateral's area is twice that of the parallelogram.
#
  area = 2.0 * area

  return area

def quadrilateral_area_3d_test ( ):

#*****************************************************************************80
#
## quadrilateral_area_3d_test() tests quadrilateral_area_3d_test()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  q = np.array ( [ \
    [ 2.0, 2.0, 0.0 ], \
    [ 0.0, 0.0, 0.0 ], \
    [ 1.0, 1.0, 1.0 ], \
    [ 3.0, 3.0, 1.0 ] ] )

  print ( '' )
  print ( 'quadrilateral_area_3d_test():' )
  print ( '  quadrilateral_area_3d() finds the area of a quadrilateral in 3D.' )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  area = quadrilateral_area_3d ( q )

  print ( '' )
  print ( '  Area is', area )

  t1 = q[0:3,0:3].copy ( )  
  area1 = triangle_area_3d ( t1 )

  t2 = np.zeros ( [ 3, 3, ] )
  t2[0:3,0:2] = q[0:3,2:4].copy ( )
  t2[0:3,2] =   q[0:3,0].copy ( )
  area2 = triangle_area_3d ( t2 )

  print ( '  Area by 2 calls to triangle_area_3d() =', area1 + area2 )

  return

def quadrilateral_contains_point ( q, p ):

#*****************************************************************************80
#
## quadrilateral_contains_point() finds if a point is inside a convex quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2], the vertices of the quadrilateral.
#
#    real P[2], the point to be checked.
#
#  Output:
#
#    logical INSIDE, is TRUE if the point is in the quadrilateral.
#

#
#  This will only handle convex quadrilaterals.
#
  inside = False

  angle_1 = angle_rad ( q[0,:], q[1,:], q[2,:] )
  angle_2 = angle_rad ( q[0,:], q[1,:], p      )

  if ( angle_1 < angle_2 ):
    return inside

  angle_1 = angle_rad ( q[1,:], q[2,:], q[3,:] )
  angle_2 = angle_rad ( q[1,:], q[2,:], p      )

  if ( angle_1 < angle_2 ):
    return inside

  angle_1 = angle_rad ( q[2,:], q[3,:], q[0,:] )
  angle_2 = angle_rad ( q[2,:], q[3,:], p      )

  if ( angle_1 < angle_2 ):
    return inside

  angle_1 = angle_rad ( q[3,:], q[0,:], q[1,:] )
  angle_2 = angle_rad ( q[3,:], q[0,:], p      )

  if ( angle_1 < angle_2 ):
    return inside

  inside = True

  return inside

def quadrilateral_contains_point_test ( ):

#*****************************************************************************80
#
## quadrilateral_contains_point_test() quadrilateral_contains_point().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 7

  ptest = np.array ( [ \
    [  0.25,   0.25 ], \
    [  0.75,   0.25 ], \
    [  1.00,   1.00 ], \
    [ 11.00,   0.50 ], \
    [  0.00,   0.50 ], \
    [  0.50, -10.00 ], \
    [  2.00,   2.00 ] ] )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'quadrilateral_contains_point_test()' )
  print ( '  quadrilateral_contains_point() tells if a point is inside' )
  print ( '  a quadrilateral.' )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  print ( '' )
  print ( '        P        Contains  Dist    Dist' )
  print ( '                          Signed  Unsigned' )
  print ( '' )

  for i in range ( 0, ntest ):

    p = ptest[i,:].copy ( )

    inside = quadrilateral_contains_point ( q, p )

    print ( '  %12f  %12f  %s' % ( p[0], p[1], str ( inside ) ) )

  return

def quadrilateral_is_convex ( q ):

#*****************************************************************************80
#
## quadrilateral_is_convex() determines whether a quadrilateral is convex.
#
#  Discussion:
#
#    Actually, this function ignores the ordering of the nodes.
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
#  Input:
#
#    real Q[4,2], the coordinates of the
#    nodes of the quadrilateral, given in counterclockwise order.
#
#  Output:
#
#    logical VALUE, is TRUE if the quadrilateral is convex.
#
  import numpy as np

  angles = quadrilateral_angles ( q )
  angle_sum = np.sum ( angles )
  angle_sum_tol = 1.0

  value = ( \
    np.all ( 0.0 < angles         ) and \
    np.all (       angles < np.pi ) and \
           ( abs ( angle_sum - 2.0 * np.pi ) < angle_sum_tol ) )

  return value

def quadrilateral_is_convex_test ( rng ):

#*****************************************************************************80
#
## quadrilateral_is_convex_test() tests quadrilateral_is_convex().
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
  print ( '' )
  print ( 'quadrilateral_is_convex_test():' )
  print ( '  quadrilateral_is_convex() is true if a quadrilateral is convex.' )

  for test in range ( 0, 5 ):

    q = quadrilateral_random_simple ( rng )
    print ( '' )
    print ( '  quadrilateral vertices:' )
    print ( q )
    value = quadrilateral_is_convex ( q )
    print ( '  quadrilateral_is_convex ( q ) =', value )

  return

def quadrilateral_is_simple ( q ):

#*****************************************************************************80
#
## quadrilateral_is_simple() determines whether a quadrilateral is simple.
#
#  Discussion:
#
#    A simple quadrilateral is one that is non-degenerate.
#
#    Visually speaking, a degenerate quadrilateral is one in which
#    one side crosses another the shape looks twisted or folded.
#    Angles and areas and centroids and similar quantities
#    become difficult to define or compute for degenerate quadrilaterals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2]: the coordinates of the
#    nodes of the quadrilateral, given in counterclockwise order.
#
#  Output:
#
#    logical VALUE, is TRUE if the quadrilateral is simple.
#
  import numpy as np

  angles = quadrilateral_angles ( q )
  angle_sum = np.sum ( angles )
#
#  A degenerate quadrilateral would typically have an angle sum of 4 pi
#  degrees, so this test could be loosened.
#
  value = ( abs ( angle_sum - 2.0 * np.pi ) < 100.0 * np.finfo(float).eps )

  return value

def quadrilateral_is_simple_test ( ):

#*****************************************************************************80
#
## quadrilateral_is_simple_test() tests quadrilateral_is_simple().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_is_simple_test():' )
  print ( '  quadrilateral_is_simple() is true if a quadrilateral is "simple",' )
  print ( '  that is, non-degenerate.' )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  value = quadrilateral_is_simple ( q )
  print ( '  quadrilateral_is_simple ( q ) =', value )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  value = quadrilateral_is_simple ( q )
  print ( '  quadrilateral_is_simple ( q ) =', value )

  q = np.array ( [ \
    [ 0.0,  0.0 ], \
    [ 1.0,  0.0 ], \
    [ 0.25, 0.25 ], \
    [ 0.0,  1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  value = quadrilateral_is_simple ( q )
  print ( '  quadrilateral_is_simple ( q ) =', value )

  q = np.array ( [ \
    [  0.0, 0.0 ], \
    [  1.0, 0.0 ], \
    [ -0.5, 0.5 ], \
    [  0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )
  value = quadrilateral_is_simple ( q )
  print ( '  quadrilateral_is_simple ( q ) =', value )

  return

def quadrilateral_perimeter ( q ):

#*****************************************************************************80
#
## quadrilateral_perimeter() computes the perimater of a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2], the coordinates
#    of the corners of the quadrilateral.  The corners should be
#    specified in clockwise or counterclockwise order.
#
#  Output:
#
#    real PERIMETER, the length of the perimeter.
#
  import numpy as np

  perimeter = 0.0
  im1 = 3
  for i in range ( 0, 4 ):
    perimeter = perimeter + np.linalg.norm ( q[i,:] - q[im1,:] )
    im1 = i

  return perimeter

def quadrilateral_perimeter_test ( ):

#*****************************************************************************80
#
## quadrilateral_perimeter_test() tests quadrilateral_perimeter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_perimeter_test():' )
  print ( '  quadrilateral_perimeter() computes the perimeter of' )
  print ( '  a quadrilateral.' )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral:' )
  print ( q )
  value = quadrilateral_perimeter ( q )
  print ( '  quadrilateral_perimeter =', value )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral:' )
  print ( q )
  value = quadrilateral_perimeter ( q )
  print ( '  quadrilateral_perimeter =', value )

  q = np.array ( [ \
    [ 0.0,  0.0 ], \
    [ 1.0,  0.0 ], \
    [ 0.25, 0.25 ], \
    [ 0.0,  1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral:' )
  print ( q )
  value = quadrilateral_perimeter ( q )
  print ( '  quadrilateral_perimeter =', value )

  q = np.array ( [ \
    [  0.0, 0.0 ], \
    [  1.0, 0.0 ], \
    [ -0.5, 0.5 ], \
    [  0.0, 1.0 ] ] )

  print ( '' )
  print ( '  quadrilateral:' )
  print ( q )
  value = quadrilateral_perimeter ( q )
  print ( '  quadrilateral_perimeter =', value )

  return

def quadrilateral_point_dist ( q, p ):

#*****************************************************************************80
#
## quadrilateral_point_dist(): distance ( quadrilateral, point ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2], the quadrilateral vertices.
#
#    real P[2], the point to be checked.
#
#  Output:
#
#    real DIST, the distance from the point to the quadrilateral.
#
  import numpy as np

  nside = 4
#
#  Find the distance to each of the line segments.
#
  dist = np.inf

  for j in range ( 0, nside ):

    jp1 = ( ( j + 1 ) % nside )

    dist2 = segment_point_dist ( q[j,:], q[jp1,:], p )

    if ( dist2 < dist ):
      dist = dist2

  return dist

def quadrilateral_point_dist_test ( ):

#*****************************************************************************80
#
## quadrilateral_point_dist_test() tests quadrilateral_point_dist().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 7

  ptest = np.array ( [ \
    [  0.25,   0.25 ], \
    [  0.75,   0.25 ], \
    [  1.00,   1.00 ], \
    [ 11.00,   0.50 ], \
    [  0.00,   0.50 ], \
    [  0.50, -10.00 ], \
    [  2.00,   2.00 ] ] )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'quadrilateral_point_dist_test()' )
  print ( '  quadrilateral_point_dist() computes the distance from a' )
  print ( '  point to a quadrilateral.' )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  print ( '' )
  print ( '        P        Dist' )
  print ( '' )

  for i in range ( 0, ntest ):

    dist = quadrilateral_point_dist ( q, ptest[i,:] )

    print ( '  ( %12f  %12f )  %10f' % ( ptest[i,0], ptest[i,1], dist ) )

  return

def quadrilateral_point_dist_signed ( q, p ):

#*****************************************************************************80
#
## quadrilateral_point_dist_signed(): signed distance ( quadrilateral, point ).
#
#  Discussion:
#
#    The quadrilateral must be convex.  DIST_SIGNED is actually the maximum
#    of the signed distances from the point to each of the four lines that
#    make up the quadrilateral.
#
#    Essentially, if the point is outside the convex quadrilateral,
#    only one of the signed distances can be positive, or two can
#    be positive and equal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2], the vertices of the quadrilateral.
#
#    real P[2], the point which is to be checked.
#
#  Output:
#
#    real DIST_SIGNED, the signed distance from the
#    point to the convex quadrilateral.  If DIST_SIGNED is
#    0.0, the point is on the boundary
#    negative, the point is in the interior
#    positive, the point is in the exterior.
#

#
#  Compare the signed distance from each line segment to the point,
#  with the signed distance to the midpoint of the opposite line.
#
#  The signed distances should all be negative if the point is inside.
#
#  Side 12
#
  dis12 = line_exp_point_dist_signed ( q[0,:], q[1,:], p )

  pm = 0.5 * ( q[2,:] + q[3,:] )

  dis = line_exp_point_dist_signed ( q[0,:], q[1,:], pm )

  if ( 0.0 < dis ):
    dis = -dis
    dis12 = -dis12
#
#  Side 23
#
  dis23 = line_exp_point_dist_signed ( q[1,:], q[2,:], p )

  pm = 0.5 * ( q[3,:] + q[0,:] )

  dis = line_exp_point_dist_signed ( q[1,:], q[2,:], pm )

  if ( 0.0 < dis ):
    dis = -dis
    dis23 = -dis23
#
#  Side 34
#
  dis34 = line_exp_point_dist_signed ( q[2,:], q[3,:], p )

  pm = 0.5 * ( q[0,:] + q[1,:] )

  dis = line_exp_point_dist_signed ( q[2,:], q[3,:], pm )

  if ( 0.0 < dis ):
    dis = -dis
    dis34 = -dis34
#
#  Side 41
#
  dis41 = line_exp_point_dist_signed ( q[3,:], q[0,:], p )

  pm = 0.5 * ( q[1,:] + q[2,:] )

  dis = line_exp_point_dist_signed ( q[3,:], q[0,:], pm )

  if ( 0.0 < dis ):
    dis = -dis
    dis41 = -dis41

  dist_signed = max ( dis12, max ( dis23, max ( dis34, dis41 ) ) )

  return dist_signed

def quadrilateral_point_dist_signed_test ( ):

#*****************************************************************************80
#
## quadrilateral_point_dist_signed_test() tests quadrilateral_point_dist_signed().
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

  ntest = 7

  ptest = np.array ( [ \
    [  0.25,   0.25 ], \
    [  0.75,   0.25 ], \
    [  1.00,   1.00 ], \
    [ 11.00,   0.50 ], \
    [  0.00,   0.50 ], \
    [  0.50, -10.00 ], \
    [  2.00,   2.00 ] ] )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'quadrilateral_point_dist_signed_test():' )
  print ( '  quadrilateral_point_dist_signed() computes the signed distance' )
  print ( '  from a point to a quadrilateral.' )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  print ( '' )
  print ( '        P        Dist' )
  print ( '' )

  for i in range ( 0, ntest ):

    dist_signed = quadrilateral_point_dist_signed ( q, ptest[i,:] )

    print ( '  ( %12f  %12f )  %10f' % ( ptest[i,0], ptest[i,1], dist_signed ) )

  return

def quadrilateral_point_near ( q, p ):

#*****************************************************************************80
#
## quadrilateral_point_near() computes the nearest point on a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[4,2], the quadrilateral vertices.
#
#    real P(2), the point whose nearest quadrilateral point
#    is to be determined.
#
#  Output:
#
#    real PN(2), the nearest point to P.
#
#    real DIST, the distance from the point to the quadrilateral.
#
  import numpy as np

  nside = 4
#
#  Find the distance to each of the line segments that make up the edges
#  of the quadrilateral.
#
  dist = np.inf
  pn = np.zeros ( 2 )

  for j in range ( 0, nside ):

    jp1 = ( ( j + 1 ) % nside )

    pn2, dist2, tval = segment_point_near ( q[j,:], q[jp1,:], p )

    if ( dist2 < dist ):
      dist = dist2
      pn = pn2.copy ( )

  return pn, dist

def quadrilateral_point_near_test ( ):

#*****************************************************************************80
#
## quadrilateral_point_near_test() tests quadrilateral_point_near().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 7

  ptest = np.array ( [ \
    [  0.25,   0.25 ], \
    [  0.75,   0.25 ], \
    [  1.00,   1.00 ], \
    [ 11.00,   0.50 ], \
    [  0.00,   0.50 ], \
    [  0.50, -10.00 ], \
    [  2.00,   2.00 ] ] )

  q = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'quadrilateral_point_near_test()' )
  print ( '  quadrilateral_point_near() computes the nearest quadrilateral' )
  print ( '  point to a given point.' )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  print ( '' )
  print ( '        P1       P2' )
  print ( '' )

  for i in range ( 0, ntest ):

    p2, dist = quadrilateral_point_near ( q, ptest[i,:] )

    print ( '  (%12f  %12f)  (%12f  %12f)' \
      % ( ptest[i,0], ptest[i,1], p2[0], p2[1] ) )

  return

def quadrilateral_random ( rng ):

#*****************************************************************************80
#
## quadrilateral_random() returns a random quadrilateral.
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
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real Q[4,2]: the quadrilateral coordinates in counterclockwise order.
#
  q = rng.standard_normal ( [ 4, 2 ] )

  return q

def quadrilateral_random_test ( rng ):

#*****************************************************************************80
#
## quadrilateral_random_test() tests quadrilateral_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_random_test():' )
  print ( '  quadrilateral_random() returns a random quadrilateral' )
  print ( '  within the unit square.' )

  for i in range ( 0, 5 ):

    q = quadrilateral_random ( rng )

    print ( '' )
    print ( '  quadrilateral vertices:' )
    print ( q )
    value = quadrilateral_is_simple ( q )
    print ( '  quadrilateral_is_simple ( q ) =', value )
    value = quadrilateral_is_convex ( q )
    print ( '  quadrilateral_is_convex ( q ) =', value )
    angles = quadrilateral_angles ( q )
    angles = angles * 180.0 / np.pi
    print ( '' )
    print ( '  angles (in degrees):' )
    print ( angles )
    angle_sum = np.sum ( angles )
    print ( '  Angle sum =', angle_sum )
    area = quadrilateral_area ( q )
    print ( '  Area =', area )
    perimeter = quadrilateral_perimeter ( q )
    print ( '  Perimeter =', perimeter )

  return

def quadrilateral_random_convex ( rng ):

#*****************************************************************************80
#
## quadrilateral_random_convex() returns a random convex quadrilateral.
#
#  Description:
#
#    The quadrilateral is constrained in that the vertices must all lie
#    with the unit square.
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
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real Q[4,2], the coordinates of the
#    nodes of the quadrilateral, given in counterclockwise order.
#
  from scipy.spatial import ConvexHull

  while ( True ):
#
#  Generate a random quadrilateral.
#
    q_random = quadrilateral_random ( rng )
#
#  Break if the quadrilateral is convex.
#
    if ( quadrilateral_is_convex ( q_random ) ):
      break
#
#  Determine the convex hull.
#
  hull = ConvexHull ( q_random )
#
#  Make an ordered copy of the random points.
#
  q = [ q_random[hull.vertices,0], q_random[hull.vertices,1] ]
 
  return q

def quadrilateral_random_convex_test ( rng ):

#*****************************************************************************80
#
## quadrilateral_random_convex_test() tests quadrilateral_random_convex().
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
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'quadrilateral_random_convex_test():' )
  print ( '  quadrilateral_random_convex() returns a random convex quadrilateral.' )
  print ( '' )

  q = quadrilateral_random_convex ( rng )

  print ( '' )
  print ( '  quadrilateral vertices:' )
  print ( q )

  return

def quadrilateral_random_simple ( rng ):

#*****************************************************************************80
#
## quadrilateral_random_simple() returns a random simple quadrilateral.
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
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real Q[4,2], the coordinates of the nodes of the quadrilateral.
#
  while ( True ):
#
#  Generate 4 random points.
#
    q = quadrilateral_random ( rng )
#
#  Break if the quadrilateral is simple.
#
    if ( quadrilateral_is_simple ( q ) ):
      break

  return q

def quadrilateral_random_simple_test ( rng ):

#*****************************************************************************80
#
## quadrilateral_random_simple_test() tests quadrilateral_random_simple().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_random_simple_test()' )
  print ( '  quadrilateral_random_simple() returns a random simple quadrilateral.' )

  for i in range ( 0, 5 ):

    q = quadrilateral_random_simple ( rng )

    print ( '' )
    print ( '  quadrilateral vertices:' )
    print ( q )
    angles = quadrilateral_angles ( q )
    angles = angles * 180.0 / np.pi
    print ( '' )
    print ( '  angles in degrees:' )
    print ( angles )
    angle_sum = np.sum ( angles )
    print ( '  Angle sum =', angle_sum )
    area = quadrilateral_area ( q )
    print ( '  Area =', area )
    perimeter = quadrilateral_perimeter ( q )
    print ( '  Perimeter =', perimeter )

  return

def quadrilateral_test ( ):

#*****************************************************************************80
#
## quadrilateral_test() tests quadrilateral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'quadrilateral_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  quadrilateral() contains functions for geometric computations' )
  print ( '  involving quadrilaterals.' )

  rng = default_rng ( )

  i4_wrap_test ( )

  polygon_angles_test ( )

  quadrilateral_angles_test ( )
  quadrilateral_area_test ( )
  quadrilateral_area_3d_test ( )
  quadrilateral_contains_point_test ( )
  quadrilateral_is_convex_test ( rng )
  quadrilateral_is_simple_test ( )
  quadrilateral_perimeter_test ( )
  quadrilateral_point_dist_signed_test ( )
  quadrilateral_point_dist_test ( )
  quadrilateral_point_near_test ( )
  quadrilateral_random_test ( rng )
  quadrilateral_random_convex_test ( rng )
  quadrilateral_random_simple_test ( rng )

  segment_point_dist_test ( )
  segment_point_near_test ( rng )

  triangle_area_test ( )
  triangle_area_3d_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'quadrilateral_test():' )
  print ( '  Normal end of execution.' )

  return

def segment_point_dist ( p1, p2, p ):

#*****************************************************************************80
#
## segment_point_dist(): distance ( line segment, point ) in 2D.
#
#  Discussion:
#
#    A line segment is the finite portion of a line that lies between
#    two points.
#
#    The nearest point will satisfy the condition
#
#      PN = (1-T) * P1 + T * P2.
#
#    T will always be between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2), P2(2), the endpoints of the line segment.
#
#    real P(2), the point whose nearest neighbor on the line
#    segment is to be determined.
#
#  Output:
#
#    real DIST, the distance from the point to the line segment.
#
  import numpy as np
#
#  If the line segment is actually a point, then the answer is easy.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):

    t = 0.0

  else:

    bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) ** 2

    t = ( ( p[0] - p1[0] ) * ( p2[0] - p1[0] ) \
        + ( p[1] - p1[1] ) * ( p2[1] - p1[1] ) ) / bot

    t = max ( t, 0.0 )
    t = min ( t, 1.0 )

  pn = np.zeros ( 2 )

  pn[0] = p1[0] + t * ( p2[0] - p1[0] )
  pn[1] = p1[1] + t * ( p2[1] - p1[1] )

  dist = np.sqrt ( ( pn[0] - p[0] ) ** 2 + ( pn[1] - p[1] ) ** 2 )

  return dist

def segment_point_dist_test ( ):

#*****************************************************************************80
#
## segment_point_dist_test() tests segment_point_dist().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'segment_point_dist_test():' )
  print ( '  segment_point_dist() computes the distance from a point to a line segment.' )

  p1 = np.array ( [ 1.0, 2.0 ] )
  p2 = np.array ( [ 3.0, 4.0 ] )

  print ( '' )
  print ( '  segment endpoint p1:' )
  print ( p1 )
  print ( '' )
  print ( '  segment endpoint p2:' )
  print ( p2 )

  p = np.array ( [ 2.0, 3.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  print ( '' )
  print ( '  test point p:' )
  print ( p )

  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 4.0, 5.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  print ( '' )
  print ( '  test point p:' )
  print ( p )

  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 1.0, 4.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  print ( '' )
  print ( '  test point p:' )
  print ( p )

  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 0.0, 0.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  print ( '' )
  print ( '  test point p:' )
  print ( p )

  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  return

def segment_point_near ( p1, p2, p ):

#*****************************************************************************80
#
## segment_point_near() finds the line segment point nearest a point.
#
#  Discussion:
#
#    A line segment is the finite portion of a line that lies between
#    two points.
#
#    The nearest point will satisfy the condition
#
#      PN = (1-T) * P1 + T * P2.
#
#    T will always be between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2), P2(2), the endpoints of the line segment.
#
#    real P(2), the point whose nearest neighbor
#    on the line segment is to be determined.
#
#  Output:
#
#    real PN(2), the point on the line segment which is
#    nearest the point (X,Y).
#
#    real DIST, the distance from the point to the
#    nearest point on the line segment.
#
#    real T, the relative position of the point (XN,YN)
#    to the points (X1,Y1) and (X2,Y2).
#
  import numpy as np
#
#  If the line segment is actually a point, then the answer is easy.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):

    t = 0.0

  else:

    bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) ** 2

    t = ( ( p[0] - p1[0] ) * ( p2[0] - p1[0] ) \
        + ( p[1] - p1[1] ) * ( p2[1] - p1[1] ) ) / bot

    t = max ( t, 0.0 )
    t = min ( t, 1.0 )

  pn = np.zeros ( 2 )

  pn[0] = p1[0] + t * ( p2[0] - p1[0] )
  pn[1] = p1[1] + t * ( p2[1] - p1[1] )

  dist = np.linalg.norm ( pn - p )

  return pn, dist, t

def segment_point_near_test ( rng ):

#*****************************************************************************80
#
## segment_point_near_test() tests segment_point_near().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  test_num = 3

  print ( '' )
  print ( 'segment_point_near_test():' )
  print ( '  segment_point_near() computes the nearest point' )
  print ( '  from a line segment to a point in 2D.' )

  for test in range ( 0, test_num ):

    p1 = rng.random ( size = 2 )
    p2 = rng.random ( size = 2 )
    p = rng.random ( size = 2 )

    pn, dist, t = segment_point_near ( p1, p2, p )

    print ( '' )
    print ( '  TEST = %d' % ( test ) )
    print ( '  P1 =   %12f  %12f' % ( p1[0], p1[1] ) )
    print ( '  P2 =   %12f  %12f' % ( p2[0], p2[1] ) )
    print ( '  P =    %12f  %12f' % ( p[0], p[1] ) )
    print ( '  PN =   %12f  %12f' % ( pn[0], pn[1] ) )
    print ( '  DIST = %12f' % ( dist ) )
    print ( '  T =    %12f' % ( t ) )

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

def triangle_area ( t ):

#*****************************************************************************80
#
## triangle_area() computes the area of a triangle in 2D.
#
#  Discussion:
#
#    If the triangle's vertices are given in counterclockwise order,
#    the area will be positive.  If the triangle's vertices are given
#    in clockwise order, the area will be negative!
#
#    An earlier version of this routine always returned the absolute
#    value of the computed area.  I am convinced now that that is
#    a less useful result!  For instance, by returning the signed 
#    area of a triangle, it is possible to easily compute the area 
#    of a nonconvex polygon as the sum of the (possibly negative) 
#    areas of triangles formed by node 1 and successive pairs of vertices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T[3,2], the triangle vertices.
#
#  Output:
#
#    real AREA, the area of the triangle.
#
  area = 0.5 * ( \
      t[0,0] * ( t[1,1] - t[2,1] ) \
    + t[1,0] * ( t[2,1] - t[0,1] ) \
    + t[2,0] * ( t[0,1] - t[1,1] ) )

  return area

def triangle_area_test ( ):

#*****************************************************************************80
#
## triangle_area_test() tests triangle_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 1.0 ], \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_area_test():' )
  print ( '  triangle_area() computes the area of a triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  area = triangle_area ( t )

  print ( '' )
  print ( '  Triangle area is ', area )

  return

def triangle_area_3d ( v ):

#*****************************************************************************80
#
## triangle_area_3d() computes the area of a triangle in 3D.
#
#  Discussion:
#
#    This routine uses the fact that the norm of the cross product vector
#    is the area of the parallelogram they form.  The triangle they
#    form has half that area.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    real V[3,3], the triangle vertices.  
#    The first row contains the coordinates of the first vertex.
#
#  Output:
#
#    real AREA, the area of the triangle.
#
  import numpy as np

  cross = np.zeros ( 3 )

  cross[0] = ( v[1,1] - v[0,1] ) * ( v[2,2] - v[0,2] ) \
           - ( v[1,2] - v[0,2] ) * ( v[2,1] - v[0,1] )

  cross[1] = ( v[1,2] - v[0,2] ) * ( v[2,0] - v[0,0] ) \
           - ( v[1,0] - v[0,0] ) * ( v[2,2] - v[0,2] )

  cross[2] = ( v[1,0] - v[0,0] ) * ( v[2,1] - v[0,1] ) \
           - ( v[1,1] - v[0,1] ) * ( v[2,0] - v[0,0] )

  area = 0.5 * np.linalg.norm ( cross )

  return area

def triangle_area_3d_test ( ):

#*****************************************************************************80
#
## triangle_area_3d_test() tests triangle_area_3d();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0,       2.0,       3.0 ], \
    [ 2.4142137, 3.4142137, 3.0 ], \
    [ 1.7071068, 2.7071068, 4.0 ] ] )

  print ( '' )
  print ( 'triangle_area_3d():' )
  print ( '  triangle_area_3d() computes the area' )
  print ( '  of a triangle in 3D.' )
  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  area = triangle_area_3d ( t )

  print ( '' )
  print ( '  Computed area is ', area )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  quadrilateral_test ( )
  timestamp ( )

