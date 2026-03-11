#! /usr/bin/env python3
#
def i4_gcd ( i, j ):

#*****************************************************************************80
#
## i4_gcd() finds the greatest common divisor of I and J.
#
#  Discussion:
#
#    Only the absolute values of I and J are
#    considered, so that the result is always nonnegative.
#
#    If I or J is 0, i4_gcd is returned as max ( 1, abs ( I ), abs ( J ) ).
#
#    If I and J have no common factor, i4_gcd is returned as 1.
#
#    Otherwise, using the Euclidean algorithm, i4_gcd is the
#    largest common factor of I and J.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, two numbers whose greatest common divisor
#    is desired.
#
#  Output:
#
#    integer VALUE, the greatest common divisor of I and J.
#
  value = 1
#
#  Return immediately if either I or J is zero.
#
  if ( i == 0 ):
    value = max ( 1, abs ( j ) )
    return value
  elif ( j == 0 ):
    value = max ( 1, abs ( i ) )
    return value
#
#  Set IP to the larger of I and J, IQ to the smaller.
#  This way, we can alter IP and IQ as we go.
#
  ip = max ( abs ( i ), abs ( j ) )
  iq = min ( abs ( i ), abs ( j ) )
#
#  Carry out the Euclidean algorithm.
#
  while ( True ):

    ir = ( ip % iq )

    if ( ir == 0 ):
      break

    ip = iq
    iq = ir

  value = iq

  return value

def i4_gcd_test ( ):

#*****************************************************************************80
#
## i4_gcd_test() tests i4_gcd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ( '' )
  print ( 'i4_gcd_test():' )
  print ( '  i4_gcd() computes the greatest common factor' )
  print ( '' )
  print ( '     I     J   i4_gcd' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_gcd ( i, j )
    print ( '  %6d  %6d  %6d' % ( i, j, k ) )

  return

def i4_lcm ( i, j ) :

#*****************************************************************************80
#
## i4_lcm() computes the least common multiple of two I4's.
#
#  Discussion:
#
#    The least common multiple may be defined as
#
#      LCM(I,J) = ABS( I * J ) / GCD(I,J)
#
#    where GCD(I,J) is the greatest common divisor of I and J.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the integers whose LCM is desired.
#
#  Output:
#
#    integer VALUE, the least common multiple of I and J.
#    VALUE is never negative.  VALUE is 0 if either I or J is zero.
#
  value = abs ( i * ( j // i4_gcd ( i, j ) ) )

  return value

def i4_lcm_test ( ):

#*****************************************************************************80
#
## i4_lcm_test() tests i4_lcm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ( '' )
  print ( 'i4_lcm_test():' )
  print ( '  i4_lcm() computes the least common multiple.' )
  print ( '' )
  print ( '       I       J  i4_lcm' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_lcm ( i, j )
    print ( '  %6d  %6d  %6d' % ( i, j, k ) )

  return

def i4vec_lcm ( n, v ):

#*****************************************************************************80
#
## i4vec_lcm() returns the least common multiple of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The value LCM returned has the property that it is the smallest integer
#    which is evenly divisible by every element of V.
#
#    The entries in V may be negative.
#
#    If any entry of V is 0, then LCM is 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of V.
#
#    integer V(N), the vector.
#
#  Output:
#
#    integer VALUE, the least common multiple of V.
#
  value = 1

  for i in range ( 0, n ):

    if ( v[i] == 0 ):
      value = 0
      return value

    value = i4_lcm ( value, v[i] )

  return value

def i4vec_lcm_test ( ):

#*****************************************************************************80
#
## i4vec_lcm_test() tests i4vec_lcm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  i4vec = np.array ( [ \
    2**3 *3    *5    *7*11    *13, \
    2    *3**2 *5    *7*11    *13, \
    2    *3    *5**3 *7*11    *13, \
    2    *3    *5    *7*11**2 *13 ] )

  print ( '' )
  print ( 'i4vec_lcm_test():' )
  print ( '  i4vec_lcm() computes the least common multiple of the' )
  print ( '  entries in an I4VEC.' )

  print ( '' )
  print ( '  i4vec:' )
  print ( i4vec )

  value = i4vec_lcm ( n, i4vec )

  print ( '' )
  print ( '  i4vec_lcm = ', value )

  return

def polygon_area_3d ( n, v ):

#*****************************************************************************80
#
## polygon_area_3d() computes the area of a polygon in 3D.
#
#  Discussion:
#
#    The computation is not valid unless the vertices of the polygon
#    lie in a plane, so that the polygon that is defined is "flat".
#
#    The polygon does not have to be "regular", that is, neither its
#    sides nor its angles need to be equal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allen Van Gelder,
#    Efficient Computation of Polygon Area and Polyhedron Volume,
#    Graphics Gems V,
#    edited by Alan Paeth,
#    AP Professional, 1995.
#
#  Input:
#
#    integer N, the number of vertices.
#
#    real V(3,N), the coordinates of the vertices.
#    The vertices should be listed in neighboring order.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
#    real NORMAL[3], the unit normal vector to the polygon.
#
  import numpy as np

  normal = np.zeros ( 3 )

  for i in range ( 0, n ):
#
#  When i = n - 1, ip1 = 0
#
    ip1 = ( ( i + 1 ) % n )
#
#  Compute the cross product vector.
#
    cross = np.zeros ( 3 )
    cross[0] = v[i,1] * v[ip1,2] - v[i,2] * v[ip1,1]
    cross[1] = v[i,2] * v[ip1,0] - v[i,0] * v[ip1,2]
    cross[2] = v[i,0] * v[ip1,1] - v[i,1] * v[ip1,0]

    normal = normal + cross

  area = np.linalg.norm ( normal )

  if ( area != 0.0 ):
    normal = normal / area
  else:
    normal = 1.0 / np.sqrt ( 3.0 )

  area = 0.5 * area

  return area, normal

def r8vec_angle_3d ( u, v ):

#*****************************************************************************80
#
## r8vec_angle_3d() computes the angle between two vectors in 3D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real U(3), V(3), the vectors.
#
#  Output:
#
#    real ANGLE, the angle between the two vectors.
#
  import numpy as np

  uv_dot = np.dot ( u, v )
  u_norm = np.linalg.norm ( u )
  v_norm = np.linalg.norm ( v )

  angle_cos = uv_dot / u_norm / v_norm

  angle = np.arccos ( angle_cos )

  return angle

def r8vec_cross_product_3d ( v1, v2 ):

#*****************************************************************************80
#
## r8vec_cross_product_3d() computes the cross product of two R8VEC's in 3D.
#
#  Discussion:
#
#    The cross product in 3D can be regarded as the determinant of the
#    symbolic matrix:
#
#          [  i  j  k ]
#      det [ x1 y1 z1 ]
#          [ x2 y2 z2 ]
#
#      = ( y1 * z2 - z1 * y2 ) * i
#      + ( z1 * x2 - x1 * z2 ) * j
#      + ( x1 * y2 - y1 * x2 ) * k
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real V1[3], V2[3], the two vectors.
#
#  Output:
#
#    real V3[3], the cross product vector.
#
  import numpy as np

  v3 = np.zeros ( 3 )

  v3[0] = v1[1] * v2[2] - v1[2] * v2[1]
  v3[1] = v1[2] * v2[0] - v1[0] * v2[2]
  v3[2] = v1[0] * v2[1] - v1[1] * v2[0]

  return v3

def shape_print ( point_num, face_num, face_order_max, point_coord, \
  face_order, face_point ):

#*****************************************************************************80
#
## shape_print() prints information about a polyhedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer POINT_NUM, the number of points in the shape.
#
#    integer FACE_NUM, the number of faces in the shape.
#
#    integer FACE_ORDER_MAX, the number of vertices per face.
#
#    real POINT_COORD(POINT_NUM,3), the vertices.
#
#    integer FACE_ORDER(FACE_NUM), the number of vertices per face.
#
#    integer FACE_POINT(FACE_NUM,FACE_ORDER_MAX) FACE_POINT(I,J)
#    contains the index of the J-th point in the I-th face.  The
#    points are listed in the counter-clockwise direction defined
#    by the outward normal at the face.
#
  print ( '' )
  print ( 'shape_print():' )
  print ( '  Information about a polytope.' )
  print ( '' )
  print ( '  The number of vertices is ', point_num )
  print ( '' )
  print ( '  Vertices:' )
  print ( '' )
  print ( '     Index          X               Y               Z' )
  print ( '' )
  for i in range ( 0, point_num ):
    print ( i, point_coord[i,:] )

  print ( '' )
  print ( '  The number of faces is ', face_num )
  print ( '  The maximum order of any face is ', face_order_max )
  print ( '' )
  print ( '     Index     Order         Indices of Nodes in Face' )
  print ( '                      ' )

  for i in range ( 0, face_num ):
    print ( i, face_order[i], end = ' ' )
    for j in range ( 0, face_order[i] ):
      print ( face_point[i,j], end = ' ' )
    print ( '' )

  return

def tetrahedron_test ( ):

#*****************************************************************************80
#
## tetrahedron_test() tests tetrahedron().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'tetrahedron_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tetrahedron().' )

  rng = default_rng ( )

  tetrahedron_barycentric_test ( rng )
  tetrahedron_centroid_test ( )
  tetrahedron_circumsphere_test ( )
  tetrahedron_contains_point_test ( )
  tetrahedron_dihedral_angles_test ( )
  tetrahedron_edge_length_test ( )
  tetrahedron_edges_test ( )
  tetrahedron_face_angles_test ( )
  tetrahedron_face_areas_test ( )
  tetrahedron_insphere_test ( )
  tetrahedron_lattice_layer_point_next_test ( )
  tetrahedron_lattice_point_next_test ( )
  tetrahedron_quality1_test ( )
  tetrahedron_quality2_test ( )
  tetrahedron_quality3_test ( )
  tetrahedron_quality4_test ( )
  tetrahedron_rhombic_shape_test ( )
  tetrahedron_sample_test ( rng )
  tetrahedron_shape_test ( )
  tetrahedron_solid_angles_test ( )
  tetrahedron_volume_test ( )

  tetrahedron01_lattice_point_num_test ( )
  tetrahedron01_sample_test ( rng )
  tetrahedron01_volume_test ( )

  triangle_angles_3d_test ( )
  triangle_area_3d_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'tetrahedron_test():' )
  print ( '  Normal end of execution.' )
  return

def tetrahedron_barycentric ( tetra, p ):

#*****************************************************************************80
#
## tetrahedron_barycentric() returns barycentric coordinates of a point in 3D.
#
#  Discussion:
#
#    The barycentric coordinates of a point (X,Y,Z) with respect to
#    a tetrahedron are a set of four values C(1:4), each associated
#    with a vertex of the tetrahedron.  The values must sum to 1.
#    If all the values are between 0 and 1, the point is contained
#    within the tetrahedron.
#
#    The barycentric coordinate of point X related to vertex A can be
#    interpreted as the ratio of the volume of the tetrahedron with 
#    vertex A replaced by vertex X to the volume of the original 
#    tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA(4,3) the tetrahedron vertices.
#
#    real P(3), the point to be checked.
#
#  Output:
#
#    real D(4), the barycentric coordinates of (X,Y,Z) with
#    respect to the tetrahedron.
#
  import numpy as np
#
#  Set up the linear system
#
#    ( X2-X1  X3-X1  X4-X1 ) C1    X - X1
#    ( Y2-Y1  Y3-Y1  Y4-Y1 ) C2  = Y - Y1
#    ( Z2-Z1  Z3-Z1  Z4-Z1 ) C3    Z - Z1
#
#  which is satisfied by the barycentric coordinates of (X,Y,Z).
#
  A = np.zeros ( [ 3, 3 ] )
  for i in range ( 0, 3 ):
    for j in range ( 0, 3 ):
      A[i,j] = tetra[j+1,i] - tetra[0,i]

  b = np.zeros ( 3 )
  for i in range ( 0, 3 ):
    b[i] = p[i] - tetra[0,i]
#
#  Solve the linear system.
#
  c = np.linalg.solve ( A, b )
  
  d = np.zeros ( 4 )
  d[0] = 1.0 - np.sum ( c )
  d[1:4] = c[0:3]

  return d

def tetrahedron_barycentric_test ( rng ):

#*****************************************************************************80
#
## tetrahedron_barycentric_test() tests tetrahedron_barycentric().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0, 4.0, 3.0 ], \
    [ 2.0, 4.0, 3.0 ], \
    [ 1.0, 6.0, 3.0 ], \
    [ 1.0, 4.0, 4.0 ] ] )

  print ( '' )
  print ( 'tetrahedron_barycentric_test():' )
  print ( '  tetrahedron_barycentric() converts XYZ to XSI.' )
  print ( '  We are computing the XSI coordinates just to verify' )
  print ( '  that the points are inside the tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron vertices' )
  print ( t )

  print ( '' )
  print ( '  (X,Y,Z)   (XSI1,XSI2,XSI3,XSI4):' )
  print ( '' )

  for i in range ( 0, 10 ):
    p = tetrahedron_sample ( t, 1, rng )
    p = p.flatten ( )
    xsi = tetrahedron_barycentric ( t, p )
    print ( p, xsi )

  return

def tetrahedron_centroid ( tetra ):

#*****************************************************************************80
#
## tetrahedron_centroid() computes the centroid of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA(4,3) the tetrahedron vertices.
#
#  Output:
#
#    real CENTROID(3), the coordinates of the centroid.
#
  import numpy as np

  centroid = np.sum ( tetra, axis = 0 ) / 4.0

  return centroid

def tetrahedron_centroid_test ( ):

#*****************************************************************************80
#
## tetrahedron_centroid_test() tests tetrahedron_centroid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [  0.000000,  0.942809, -0.333333 ], \
    [ -0.816496, -0.816496, -0.333333 ], \
    [  0.816496, -0.816496, -0.333333 ], \
    [  0.000000,  0.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_centroid_test():' )
  print ( '  tetrahedron_centroid() computes the centroid of a tetrahedron' )

  print ( '' )
  print ( '  tetrahedron vertices' )
  print ( t )

  centroid = tetrahedron_centroid ( t )

  print ( '' )
  print ( '  tetrahedron centroid():' )
  print ( centroid )

  return

def tetrahedron_circumsphere ( tetra ):

#*****************************************************************************80
#
## tetrahedron_circumsphere() computes the circumsphere of a tetrahedron in 3D.
#
#  Discussion:
#
#    The circumsphere, or circumscribed sphere, of a tetrahedron is the sphere
#    that passes through the four vertices.  The circumsphere is not necessarily
#    the smallest sphere that contains the tetrahedron.
#
#    Surprisingly, the diameter of the sphere can be found by solving
#    a 3 by 3 linear system.  This is because the vectors P2 - P1,
#    P3 - P1 and P4 - P1 are secants of the sphere, and each forms a
#    right triangle with the diameter through P1.  Hence, the dot product of
#    P2 - P1 with that diameter is equal to the square of the length
#    of P2 - P1, and similarly for P3 - P1 and P4 - P1.  This determines
#    the diameter vector originating at P1, and hence the radius and
#    center.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Adrian Bowyer, John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    real TETRA[4,3] the tetrahedron vertices.
#
#  Output:
#
#    real R, CENTER[3], the center of the circumscribed sphere, and its radius.  
#
  import numpy as np
#
#  Set up the linear system.
#
  A = np.zeros ( [ 3, 3 ] )

  A[:,:] = tetra[1:4,:]

  for i in range ( 0, 3 ):
    for j in range ( 0, 3 ):
      A[i,j] = A[i,j] - tetra[0,j]

  x = np.zeros ( 3 )
  for i in range ( 0, 3 ):
    x[i] = np.sum ( A[i,:]**2 )
#
#  Solve the linear system.
#
  c = np.linalg.solve ( A, x )
#
#  Compute R, X, Y, Z.
#
  r = 0.5 * np.linalg.norm ( c )

  center = np.zeros ( 3 )
  center = tetra[0,:] + 0.5 * c

  return r, center

def tetrahedron_circumsphere_test ( ):

#*****************************************************************************80
#
## tetrahedron_circumsphere_test() tests tetrahedron_circumsphere()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  tetra = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0 ], \
    [ -0.288675134594813,  0.5, 0.0 ], \
    [ -0.288675134594813, -0.5, 0.0 ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  print ( '' )
  print ( 'tetrahedron_circumsphere_test():' )
  print ( '  tetrahedron_circumsphere() computes the circumsphere' )
  print ( '  of a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron vertices:' )
  print ( tetra )

  r, center = tetrahedron_circumsphere ( tetra  )

  print ( '' )
  print ( '  tetrahedron circumsphere center:' )
  print ( center )

  print ( '' )
  print ( '  Circumsphere radius is ', r )
 
  return

def tetrahedron_contains_point ( tetra, p ):

#*****************************************************************************80
#
## tetrahedron_contains_point() finds if a point is inside a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA[4,3], the tetrahedron vertices.
#
#    real P(3), the point to be checked.
#
#  Output:
#
#    logical INSIDE, is TRUE if (X,Y,Z) is inside
#    the tetrahedron or on its boundary.
#
  import numpy as np

  c = tetrahedron_barycentric ( tetra, p )
#
#  If the point is in the tetrahedron, its barycentric coordinates
#  must be nonnegative.
#
  if ( np.any ( c < 0.0 ) ):
    inside = False
  else:
    inside = True

  return inside

def tetrahedron_contains_point_test ( ):

#*****************************************************************************80
#
## tetrahedron_contains_point_test() tests tetrahedron_contains_point()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  tetra = np.array ( [ \
    [  0.000000,  0.942809, -0.333333 ], \
    [ -0.816496, -0.816496, -0.333333 ], \
    [  0.816496, -0.816496, -0.333333 ], \
    [  0.000000,  0.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_contains_point_test():' )
  print ( '  tetrahedron_contains_point() finds if a point' )
  print ( '  is inside a tetrahderon' )

  print ( '' )
  print ( '  tetrahedron vertices:' )
  print ( tetra )

  print ( '' )
  print ( '  P, Inside_Tetra?' )
  print ( '' )
#
#  Test 1
#
  c = np.array ( [ 0.0, 0.1, 0.2, 0.7 ] )
  p = np.dot ( c, tetra )
  inside = tetrahedron_contains_point ( tetra, p )
  print ( p, inside )
#
#  Test 2
#
  c = np.array ( [ -1.3, 2.0, 0.2, 0.1 ] )
  p = np.dot ( c, tetra )
  inside = tetrahedron_contains_point ( tetra, p )
  print ( p, inside )
#
#  Test 3
#
  c = np.array ( [ 0.8, 0.6, -0.5, 0.1 ] )
  p = np.dot ( c, tetra )
  inside = tetrahedron_contains_point ( tetra, p )
  print ( p, inside )

  return

def tetrahedron_dihedral_angles ( tetra ):

#*****************************************************************************80
#
## tetrahedron_dihedral_angles() computes dihedral angles of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA[4,3], the vertices of the tetrahedron,
#    which can be labeled as A, B, C and D.
#
#  Output:
#
#    real ANGLE(6), the dihedral angles along the
#    axes AB, AC, AD, BC, BD and CD, respectively.
#
  import numpy as np

  ab = tetra[1,:] - tetra[0,:]
  ac = tetra[2,:] - tetra[0,:]
  ad = tetra[3,:] - tetra[0,:]
  bc = tetra[2,:] - tetra[1,:]
  bd = tetra[3,:] - tetra[1,:]
 
  abc_normal = r8vec_cross_product_3d ( ac, ab )
  abd_normal = r8vec_cross_product_3d ( ab, ad )
  acd_normal = r8vec_cross_product_3d ( ad, ac )
  bcd_normal = r8vec_cross_product_3d ( bc, bd )

  angle = np.zeros ( 6 )

  angle[0] = r8vec_angle_3d ( abc_normal, abd_normal )
  angle[1] = r8vec_angle_3d ( abc_normal, acd_normal )
  angle[2] = r8vec_angle_3d ( abd_normal, acd_normal )
  angle[3] = r8vec_angle_3d ( abc_normal, bcd_normal )
  angle[4] = r8vec_angle_3d ( abd_normal, bcd_normal )
  angle[5] = r8vec_angle_3d ( acd_normal, bcd_normal )

  angle[:] = np.pi - angle[:]

  return angle

def tetrahedron_dihedral_angles_test ( ):

#*****************************************************************************80
#
## tetrahedron_dihedral_angles_test() tests tetrahedron_dihedral_angles().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [ 0.000000,  0.942809, -0.333333 ], \
    [-0.816496, -0.816496, -0.333333 ], \
    [ 0.816496, -0.816496, -0.333333 ], \
    [ 0.000000,  0.000000,  1.000000 ] ] )
  t2 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  1.000000,  0.000000 ], \
    [ 0.000000,  0.000000,  1.000000 ] ] )
  t3 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  2.000000,  0.000000 ], \
    [ 0.000000,  0.000000,  4.000000 ] ] )
  t4 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  1.000000,  0.000000 ], \
    [ 1.000000,  1.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_dihedral_angles_test():' )
  print ( '  tetrahedron_dihedral_angles() computes the dihedral angles' )
  print ( '  of a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  angle = tetrahedron_dihedral_angles ( t1 )
  print ( '' )
  print ( '  Dihedral angles:' )
  print ( angle )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  angle = tetrahedron_dihedral_angles ( t2 )
  print ( '' )
  print ( '  Dihedral angles:' )
  print ( angle )

  print ( '' )
  print ( '  tetrahedron3 vertices:' )
  print ( t3 )
  angle = tetrahedron_dihedral_angles ( t3 )
  print ( '' )
  print ( '  Dihedral angles:' )
  print ( angle )

  print ( '' )
  print ( '  tetrahedron4 vertices:' )
  print ( t4 )
  angle = tetrahedron_dihedral_angles ( t4 )
  print ( '' )
  print ( '  Dihedral angles:' )
  print ( angle )

  return

def tetrahedron_edge_length ( tetra ):

#*****************************************************************************80
#
## tetrahedron_edge_length() returns edge lengths of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA(4,3), the tetrahedron vertices.
#
#  Output:
#
#    real EDGE_LENGTH(6), the length of the edges.
#
  import numpy as np

  edge_length = np.zeros ( 6 )

  k = 0
  for i1 in range ( 0, 3 ):
    for i2 in range ( i1 + 1, 4 ):
      edge_length[k] = np.linalg.norm ( tetra[i2,:] - tetra[i1,:] )
      k = k + 1

  return edge_length

def tetrahedron_edge_length_test ( ):

#*****************************************************************************80
#
## tetrahedron_edge_length_test() tests tetrahedron_edge_length().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.0               ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  print ( '' )
  print ( 'tetrahedron_edge_length_test():' )
  print ( '  tetrahedron_edge_length() computes the edge lengths.' )

  print ( '' )
  print ( '  tetrahedron vertices' )
  print ( t )

  edge_length = tetrahedron_edge_length ( t )

  print ( '' )
  print ( '  tetrahedron edge lengths:' )
  print ( edge_length )

  return

def tetrahedron_edges ( tetra ):

#*****************************************************************************80
#
## tetrahedron_edges() computes the edges of a tetrahedron.
#
#  Discussion:
#
#    The vertices are A, B, C, D.  The edge from A to B is denoted by AB.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 May 2022
#
#  Author:
#
#    Original FORTRAN77 version by Barry Joe.
#    This version by John Burkardt.
#
#  Reference:
#
#    Barry Joe,
#    GEOMPACK - a software package for the generation of meshes
#    using geometric algorithms,
#    Advances in Engineering Software,
#    Volume 13, pages 325-331, 1991.
#
#  Input:
#
#    real TETRA[4,3], the vertices of the tetrahedron.
#
#  Output:
#
#    real AB(3), AC(3), AD(3), BC(3), BD(3), CD(3), the edges.
#
  ab = tetra[1,:] - tetra[0,:]
  ac = tetra[2,:] - tetra[0,:]
  ad = tetra[3,:] - tetra[0,:]
  bc = tetra[2,:] - tetra[1,:]
  bd = tetra[3,:] - tetra[1,:]
  cd = tetra[3,:] - tetra[2,:]

  return ab, ac, ad, bc, bd, cd

def tetrahedron_edges_test ( ):

#*****************************************************************************80
#
## tetrahedron_edges_test() tests tetrahedron_edges().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.0               ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  print ( '' )
  print ( 'tetrahedron_edges_test():' )
  print ( '  tetrahedron_edges() computes the edges.' )

  print ( '' )
  print ( '  tetrahedron vertices' )
  print ( t )

  ab, ac, ad, bc, bd, cd = tetrahedron_edges ( t )

  print ( '' )
  print ( '  tetrahedron edges:' )
  print ( '  ab:', ab )
  print ( '  ac:', ac )
  print ( '  ad:', ad )
  print ( '  bc:', bc )
  print ( '  bd:', bd )
  print ( '  cd:', cd )

  return

def tetrahedron_face_angles ( tetra ):

#*****************************************************************************80
#
## tetrahedron_face_angles() returns the 12 face angles of a tetrahedron.
#
#  Discussion:
#
#    The tetrahedron has 4 triangular faces.  This routine computes the
#    3 planar angles associated with each face.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA(4,3) the tetrahedron vertices.
#
#  Output:
#
#    real ANGLES(4,3), the face angles.
#
  import numpy as np

  angles = np.zeros ( [ 4, 3 ] )
  tri = np.zeros ( [ 3, 3 ] )
#
#  Face 123
#
  tri[0:3,0:3] = tetra[0:3,0:3]
  angles[0,:] = triangle_angles_3d ( tri )
#
#  Face 124
#
  tri[0:2,:] = tetra[0:2,:]
  tri[2,:] = tetra[3,:]
  angles[1,:] = triangle_angles_3d ( tri )
#
#  Face 134
#
  tri[0,:] = tetra[0,:]
  tri[1:3,:] = tetra[2:4,:]
  angles[2,:] = triangle_angles_3d ( tri )
#
#  Face 234
#
  tri = tetra[1:4,:]
  angles[3,:] = triangle_angles_3d ( tri )

  return angles

def tetrahedron_face_angles_test ( ):

#*****************************************************************************80
#
## tetrahedron_face_angles_test() tests tetrahedron_face_angles()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [ 0.000000,  0.942809, -0.333333 ], \
    [-0.816496, -0.816496, -0.333333 ], \
    [ 0.816496, -0.816496, -0.333333 ], \
    [ 0.000000,  0.000000,  1.000000 ] ] )
  t2 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  1.000000,  0.000000 ], \
    [ 0.000000,  0.000000,  1.000000 ] ] )
  t3 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  2.000000,  0.000000 ], \
    [ 0.000000,  0.000000,  4.000000 ] ] )
  t4 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  1.000000,  0.000000 ], \
    [ 1.000000,  1.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_face_angles_test():' )
  print ( '  tetrahedron_face_angles() computes the 6 pairwise angles' )
  print ( '  of the 4 faces of a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  angles = tetrahedron_face_angles ( t1 )
  print ( '' )
  print ( '  Face angles:' )
  print ( angles )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  angles = tetrahedron_face_angles ( t2 )
  print ( '' )
  print ( '  Face angles:' )
  print ( angles )

  print ( '' )
  print ( '  tetrahedron3 vertices:' )
  print ( t3 )
  angles = tetrahedron_face_angles ( t3 )
  print ( '' )
  print ( '  Face angles:' )
  print ( angles )

  print ( '' )
  print ( '  tetrahedron4 vertices:' )
  print ( t4 )
  angles = tetrahedron_face_angles ( t4 )
  print ( '' )
  print ( '  Face angles:' )
  print ( angles )

  return

def tetrahedron_face_areas ( tetra ):

#*****************************************************************************80
#
## tetrahedron_face_areas() returns the 4 face areas of a tetrahedron.
#
#  Discussion:
#
#    The tetrahedron has 4 triangular faces.  This routine computes the
#    area associated with each face.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA[4,3] the tetrahedron vertices.
#
#  Output:
#
#    real AREAS(4), the face areas.
#
  import numpy as np

  areas = np.zeros ( 4 )

  tri = np.zeros ( [ 3, 3 ] )
#
#  Face 012
#
  tri[0:3,:] = tetra[0:3,0:3]
  areas[0] = triangle_area_3d ( tri )
#
#  Face 013
#
  tri[0:2,:] = tetra[0:2,:]
  tri[2,:] = tetra[3,:]
  areas[1] = triangle_area_3d ( tri )
#
#  Face 023
#
  tri[0,:] = tetra[0,:]
  tri[1:3,:] = tetra[2:4,:]
  areas[2] = triangle_area_3d ( tri )
#
#  Face 123
#
  tri[0:3,:] = tetra[1:4,:]
  areas[3] = triangle_area_3d ( tri )

  return areas

def tetrahedron_face_areas_test ( ):

#*****************************************************************************80
#
## tetrahedron_face_areas_test() tests tetrahedron_face_areas().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
     [ 0.000000,  0.942809, -0.333333 ], \
     [-0.816496, -0.816496, -0.333333 ], \
     [ 0.816496, -0.816496, -0.333333 ], \
     [ 0.000000,  0.000000,  1.000000 ] ] )
  t2 = np.array ( [ \
     [ 0.000000,  0.000000,  0.000000 ], \
     [ 1.000000,  0.000000,  0.000000 ], \
     [ 0.000000,  1.000000,  0.000000 ], \
     [ 0.000000,  0.000000,  1.000000 ] ] )
  t3 = np.array ( [ \
     [ 0.000000,  0.000000,  0.000000 ], \
     [ 1.000000,  0.000000,  0.000000 ], \
     [ 0.000000,  2.000000,  0.000000 ], \
     [ 0.000000,  0.000000,  4.000000 ] ] )
  t4 = np.array ( [ \
     [ 0.000000,  0.000000,  0.000000 ], \
     [ 1.000000,  0.000000,  0.000000 ], \
     [ 0.000000,  1.000000,  0.000000 ], \
     [ 1.000000,  1.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_face_areas_test():' )
  print ( '  tetrahedron_face_areas() computes the areas of the' )
  print ( '  4 faces of a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  areas = tetrahedron_face_areas ( t1 )
  print ( '' )
  print ( '  Face areas:' )
  print ( areas )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  areas = tetrahedron_face_areas ( t2 )
  print ( '' )
  print ( '  Face areas:' )
  print ( areas )

  print ( '' )
  print ( '  tetrahedron3 vertices:' )
  print ( t3 )
  areas = tetrahedron_face_areas ( t3 )
  print ( '' )
  print ( '  Face areas:' )
  print ( areas )

  print ( '' )
  print ( '  tetrahedron4 vertices:' )
  print ( t4 )
  areas = tetrahedron_face_areas ( t4 )
  print ( '' )
  print ( '  Face areas:' )
  print ( areas )

  return

def tetrahedron_insphere ( tetra ):

#*****************************************************************************80
#
## tetrahedron_insphere() finds the insphere of a tetrahedron.
#
#  Discussion:
#
#    The insphere of a tetrahedron is the inscribed sphere, which touches
#    each face of the tetrahedron at a single point.
#
#    The points of contact are the centroids of the triangular faces
#    of the tetrahedron.  Therefore, the point of contact for a face
#    can be computed as the average of the vertices of that face.
#
#    The sphere can then be determined as the unique sphere through
#    the four given centroids.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Schneider, David Eberly,
#    Geometric Tools for Computer Graphics,
#    Elsevier, 2002,
#    ISBN: 1558605940,
#    LC: T385.G6974.
#
#  Input:
#
#    real TETRA[4,3], the vertices of the tetrahedron.
#
#  Output:
#
#    real R, PC[3], the radius and the center of the sphere.
#
  import numpy as np

  v21 = tetra[1,:] - tetra[0,:]
  v31 = tetra[2,:] - tetra[0,:]
  v41 = tetra[3,:] - tetra[0,:]
  v32 = tetra[2,:] - tetra[1,:]
  v42 = tetra[3,:] - tetra[1,:]
  v43 = tetra[3,:] - tetra[2,:]

  n123 = r8vec_cross_product_3d ( v21, v31 )
  n124 = r8vec_cross_product_3d ( v41, v21 )
  n134 = r8vec_cross_product_3d ( v31, v41 )
  n234 = r8vec_cross_product_3d ( v42, v32 )

  l123 = np.linalg.norm ( n123 )
  l124 = np.linalg.norm ( n124 )
  l134 = np.linalg.norm ( n134 )
  l234 = np.linalg.norm ( n234 )

  pc = ( l234 * tetra[0,:]   \
       + l134 * tetra[1,:]   \
       + l124 * tetra[2,:]   \
       + l123 * tetra[3,:] ) \
       / ( l234 + l134 + l124 + l123 )

  B = np.zeros ( [ 4, 4 ] )
  B[:,0:3] = tetra[:,0:3]
  B[:,3] = 1.0

  gamma = abs ( np.linalg.det ( B ) )

  r = gamma / ( l234 + l134 + l124 + l123 )

  return r, pc

def tetrahedron_insphere_test ( ):

#*****************************************************************************80
#
## tetrahedron_insphere_test() tests tetrahedron_insphere().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  tetra = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0 ], \
    [ -0.288675134594813,  0.5, 0.0 ], \
    [ -0.288675134594813, -0.5, 0.0 ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  print ( '' )
  print ( 'tetrahedron_insphere_test():' )
  print ( '  tetrahedron_insphere() computes the insphere' )
  print ( '  of a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron vertices:' )
  print ( tetra )

  r, pc = tetrahedron_insphere ( tetra )

  print ( '' )
  print ( '  insphere center:' )
  print ( pc )

  print ( '' )
  print ( '  Insphere radius is ', r )

  return

def tetrahedron_lattice_layer_point_next ( c, v, more ):

#*****************************************************************************80
#
## tetrahedron_lattice_layer_point_next(): next tetrahedron lattice layer point.
#
#  Discussion:
#
#    The tetrahedron lattice layer L is bounded by the lines
#
#      0 <= X,
#      0 <= Y,
#      0 <= Z,
#      L - 1 < X / C(1) + Y / C(2) + Z/C(3) <= L.
#
#    In particular, layer L = 0 always contains the single point (0,0).
#
#    This function returns, one at a time, the points that lie within 
#    a given tetrahedron lattice layer.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C(4), coefficients defining the 
#    lattice layer in entries 1 to 3, and the laver index in C(4).  
#    The coefficients should be positive, and C(4) must be nonnegative.
#
#    integer V(3).  On first call for a given layer,
#    the input value of V is not important.  On a repeated call for the same
#    layer, the input value of V should be the output value from the previous 
#    call.
#
#    logical MORE.  Set MORE to FALSE to indicate
#    that this is the first call for a given layer.  Thereafter, the input
#    value should be the output value from the previous call.  \
#
#  Output:
#
#    integer V(3).  V contains the next lattice layer point.
#
#    logical MORE.
#    MORE is TRUE if the returned value V is a new point.
#    If the output value is FALSE, then no more points were found,
#    and V was reset to 0, and the lattice layer has been exhausted.
#
  import numpy as np

  n = 3
#
#  Treat layer C(N+1) = 0 specially.
#
  if ( c[3] == 0 ):
    if ( not more ):
      v[:] = 0
      more = True
    else:
      more = False

    return v, more
#
#  Compute the first point.
#
  if ( not more ):

    v[0] = ( c[3] - 1 ) * c[0] + 1
    v[1:3] = 0
    more = True

  else:

    c1n = i4vec_lcm ( n, c )

    rhs1 = c1n * ( c[3] - 1 )
    rhs2 = c1n *   c[3]
#
#  Can we simply increase X?
#
    v[0] = v[0] + 1

    lhs = ( c1n / c[0] ) * v[0] \
        + ( c1n / c[1] ) * v[1] \
        + ( c1n / c[2] ) * v[2]
#
#  No.  Increase Y, and set X so we just exceed RHS1...if possible.
#
    if ( rhs2 < lhs ):

      v[1] = v[1] + 1

      v[0] = np.floor ( ( c[0] * ( rhs1 - ( c1n / c[1] ) * v[1] \
                                        - ( c1n / c[2] ) * v[2] ) ) / c1n )
      v[0] = max ( v[0], 0 )

      lhs = ( c1n / c[0] ) * v[0] \
          + ( c1n / c[1] ) * v[1] \
          + ( c1n / c[2] ) * v[2]

      if ( lhs <= rhs1 ):
        v[0] = v[0] + 1
        lhs = lhs + c1n / c[0]
#
#  We have increased Y by 1.  Have we stayed below the upper bound?
#
      if ( rhs2 < lhs ):
#
#  No.  Increase Z, and set X so we just exceed RHS1...if possible.
#
        v[2] = v[2] + 1
        v[1] = 0
        v[0] = np.floor ( ( c[0] * ( rhs1 - ( c1n / c[1] ) * v[1] \
                                       - ( c1n / c[2] ) * v[2] ) ) / c1n )
        v[0] = max ( v[0], 0 )

        lhs = ( c1n / c[0] ) * v[0] \
            + ( c1n / c[1] ) * v[1] \
            + ( c1n / c[2] ) * v[2]

        if ( lhs <= rhs1 ):
          v[0] = v[0] + 1
          lhs = lhs + c1n / c[0]

        if ( rhs2 < lhs ):
          more = False
          v[:] = 0

  return v, more

def tetrahedron_lattice_layer_point_next_test ( ):

#*****************************************************************************80
#
## tetrahedron_lattice_layer_point_next_test() tests tetrahedron_lattice_layer_point_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'tetrahedron_lattice_layer_point_next_test():' )
  print ( '  tetrahedron_lattice_layer_point_next() returns the next' )
  print ( '  point in a tetrahedron lattice layer defined by:' )
  print ( '' )
  print ( '    C(4) - 1 < X(1)/C(1) + X(2)/C(2) +X(3)/C(3) <= C(4).' )

  c = np.zeros ( 4 )
  c[0] = 2
  c[1] = 3
  c[2] = 4
  v = np.zeros ( n )

  print ( '' )
  print ( '  N = ', n )
  print ( '  C = ', c )

  for layer in range ( 0, 3 ):

    print ( '' )
    print ( '  Layer', layer )
    print ( '' )

    c[3] = layer
    more = False
    i = 0

    while ( True ):
      v, more = tetrahedron_lattice_layer_point_next ( c, v, more )
      if ( not more ):
        print ( '  No more.' )
        break
      i = i + 1
      print ( i, v )

  return

def tetrahedron_lattice_point_next ( c, v, more ):

#*****************************************************************************80
#
## tetrahedron_lattice_point_next() returns the next tetrahedron lattice point.
#
#  Discussion:
#
#    The lattice tetrahedron is defined by the vertices:
#
#      (0,0,0), (C(4)/C[0],0,0), (0,C(4)/C[1],0) and (0,0,C(4)/C[2])
#
#    The lattice tetrahedron is bounded by the lines
#
#      0 <= X,
#      0 <= Y
#      0 <= Z,
#      X / C[0] + Y / C[1] + Z / C[2] <= C(4)
#
#    Lattice points are listed one at a time, starting at the origin,
#    with X increasing first.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C[4], coefficients defining the
#    lattice tetrahedron.  These should be positive.
#
#    integer V[3].  On first call, the input
#    value is not important.  On a repeated call, the input value should
#    be the output value from the previous call.  
#
#    logical MORE.  On set MORE to FALSE to indicate
#    that this is the first call for a given tetrahedron.  Thereafter, the input
#    value should be the output value from the previous call.  
#
#  Output:
#
#    integer V[3],  V contains
#    the next lattice point.
#
#    logical MORE, MORE is TRUE if not only is the returned value V a lattice point,
#    but the routine can be called again for another lattice point.
#    If the output value is FALSE, then no more lattice points were found,
#    and V was reset to 0, and the routine should not be called further
#    for this tetrahedron.
#
  n = 3

  if ( not more ):

    v[:] = 0
    more = True

  else:

    c1n = i4vec_lcm ( n, c )

    rhs = c1n * c[n]

    lhs =        c[1] * c[2] * v[0] \
        + c[0] *        c[2] * v[1] \
        + c[0] * c[1]        * v[2]

    if ( lhs + c1n / c[0] <= rhs ):

      v[0] = v[0] + 1

    else:

      lhs = lhs - c1n * v[0] / c[0]
      v[0] = 0

      if ( lhs + c1n / c[1] <= rhs ):

        v[1] = v[1] + 1

      else:

        lhs = lhs - c1n * v[1] / c[1]
        v[1] = 0

        if ( lhs + c1n / c[2] <= rhs ):

          v[2] = v[2] + 1

        else:

          v[2] = 0
          more = False

  return v, more

def tetrahedron_lattice_point_next_test ( ):

#*****************************************************************************80
#
## tetrahedron_lattice_point_next_test() tests tetrahedron_lattice_point_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'tetrahedron_lattice_point_next_test():' )
  print ( '  tetrahedron_lattice_point_next() returns the next lattice' )
  print ( '  point in a tetrahedron defined by:' )
  print ( '' )
  print ( '    0 <= X[0]/C[0] + X[1]/C[1] + X[2]/C[2] <= C[3]' )

  c = np.array ( [ 4, 3, 2, 1 ] )
  v = np.zeros ( n )
  more = False

  print ( '' )
  print ( '  N = ', n )
  print ( '  C = ', c )
  print ( '' )

  i = 0

  while ( True ):

    v, more = tetrahedron_lattice_point_next ( c, v, more )

    if ( not more ):
      print ( '  No more.' )
      break

    i = i + 1
    print ( i, v )

  return

def tetrahedron_quality1 ( tetra ):

#*****************************************************************************80
#
## tetrahedron_quality1(): "quality" of a tetrahedron.
#
#  Discussion:
#
#    The quality of a tetrahedron is 3.0 times the ratio of the radius of
#    the inscribed sphere divided by that of the circumscribed sphere.
#
#    An equilateral tetrahredron achieves the maximum possible quality of 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA[4,3], the tetrahedron vertices.
#
#  Output:
#
#    real QUALITY, the quality of the tetrahedron.
#
  r_out, pc = tetrahedron_circumsphere ( tetra )

  r_in, pc = tetrahedron_insphere ( tetra )

  quality = 3.0 * r_in / r_out

  return quality

def tetrahedron_quality1_test ( ):

#*****************************************************************************80
#
## tetrahedron_quality1_test() tests tetrahedron_quality1()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.816496580927726 ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  t2 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.0               ], \
    [  0.0,                0.0, 0.408248290463863 ] ] )

  print ( '' )
  print ( 'tetrahedron_quality1_test():' )
  print ( '  tetrahedron_quality1() computes quality measure #1' )
  print ( '  for a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  quality1 = tetrahedron_quality1 ( t1 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality1 )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  quality1 = tetrahedron_quality1 ( t2 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality1 )

  return

def tetrahedron_quality2 ( tetra ):

#*****************************************************************************80
#
## tetrahedron_quality2(): "quality" of a tetrahedron.
#
#  Discussion:
#
#    The quality measure #2 of a tetrahedron is:
#
#      QUALITY2 = 2 * sqrt ( 6 ) * RIN / LMAX
#
#    where
#
#      RIN = radius of the inscribed sphere
#      LMAX = length of longest side of the tetrahedron.
#
#    An equilateral tetrahredron achieves the maximum possible quality of 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Qiang Du, Desheng Wang,
#    The Optimal Centroidal Voronoi Tesselations and the Gersho's
#    Conjecture in the Three-Dimensional Space,
#    Computers and Mathematics with Applications,
#    Volume 49, 2005, pages 1355-1373.
#
#  Input:
#
#    real TETRA[4,3], the tetrahedron vertices.
#
#  Output:
#
#    real QUALITY2, the quality of the tetrahedron.
#
  import numpy as np

  edge_length = tetrahedron_edge_length ( tetra )

  l_max = np.max ( edge_length )

  r_in, pc = tetrahedron_insphere ( tetra )

  quality2 = 2.0 * np.sqrt ( 6.0 ) * r_in / l_max

  return quality2

def tetrahedron_quality2_test ( ):

#*****************************************************************************80
#
## tetrahedron_quality2_test() tests tetrahedron_quality2()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.816496580927726 ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  t2 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.0               ], \
    [  0.0,                0.0, 0.408248290463863 ] ] )

  print ( '' )
  print ( 'tetrahedron_quality2_test():' )
  print ( '  tetrahedron_quality2() computes quality measure #2' )
  print ( '  for a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  quality2 = tetrahedron_quality2 ( t1 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality2 )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  quality2 = tetrahedron_quality2 ( t2 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality2 )

  return

def tetrahedron_quality3 ( tetra ):

#*****************************************************************************80
#
## tetrahedron_quality3() computes the mean ratio of a tetrahedron.
#
#  Discussion:
#
#    This routine computes QUALITY3, the eigenvalue or mean ratio of
#    a tetrahedron.
#
#      QUALITY3 = 12 * ( 3 * volume )^(2/3) / (sum of square of edge lengths).
#
#    This value may be used as a shape quality measure for the tetrahedron.
#
#    For an equilateral tetrahedron, the value of this quality measure
#    will be 1.  For any other tetrahedron, the value will be between
#    0 and 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    Original FORTRAN77 version by Barry Joe.
#    This version by John Burkardt.
#
#  Reference:
#
#    Barry Joe,
#    GEOMPACK - a software package for the generation of meshes
#    using geometric algorithms,
#    Advances in Engineering Software,
#    Volume 13, pages 325-331, 1991.
#
#  Input:
#
#    real TETRA(4,3), the vertices of the tetrahedron.
#
#  Output:
#
#    real QUALITY3, the mean ratio of the tetrahedron.
#
  import numpy as np
#
#  Compute the vectors representing the sides of the tetrahedron.
#
  ab = tetra[1,:] - tetra[0,:]
  ac = tetra[2,:] - tetra[0,:]
  ad = tetra[3,:] - tetra[0,:]
  bc = tetra[2,:] - tetra[1,:]
  bd = tetra[3,:] - tetra[1,:]
  cd = tetra[3,:] - tetra[2,:]
#
#  Compute the lengths of the sides.
#
  lab = np.linalg.norm ( ab )
  lac = np.linalg.norm ( ac )
  lad = np.linalg.norm ( ad )
  lbc = np.linalg.norm ( bc )
  lbd = np.linalg.norm ( bd )
  lcd = np.linalg.norm ( cd )
#
#  Compute the volume.
#
  vol = np.abs ( \
      ab[0] * ( ac[1] * ad[2] - ac[2] * ad[1] ) \
    + ab[1] * ( ac[2] * ad[0] - ac[0] * ad[2] ) \
    + ab[2] * ( ac[0] * ad[1] - ac[1] * ad[0] ) ) / 6.0

  denom = lab**2 + lac**2 + lad**2 + lbc**2 + lbd**2 + lcd**2

  if ( denom == 0.0 ):
    quality3 = 0.0
  else:
    quality3 = 12.0 * ( 3.0 * vol ) ** ( 2.0 / 3.0 ) / denom

  return quality3

def tetrahedron_quality3_test ( ):

#*****************************************************************************80
#
## tetrahedron_quality3_test() tests tetrahedron_quality3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.816496580927726 ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  t2 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.0               ], \
    [  0.0,                0.0, 0.408248290463863 ] ] )

  print ( '' )
  print ( 'tetrahedron_quality3_test()' )
  print ( '  tetrahedron_quality3() computes quality measure #3' )
  print ( '  for a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  quality3 = tetrahedron_quality3 ( t1 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality3 )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  quality3 = tetrahedron_quality3 ( t2 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality3 )

  return

def tetrahedron_quality4 ( tetra ):

#*****************************************************************************80
#
## tetrahedron_quality4() computes the minimum solid angle of a tetrahedron.
#
#  Discussion:
#
#    This routine computes a quality measure for a tetrahedron, based
#    on the sine of half the minimum of the four solid angles.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2022
#
#  Author:
#
#    Original FORTRAN77 version by Barry Joe.
#    This version by John Burkardt.
#
#  Reference:
#
#    Barry Joe,
#    GEOMPACK - a software package for the generation of meshes
#    using geometric algorithms,
#    Advances in Engineering Software,
#    Volume 13, pages 325-331, 1991.
#
#  Input:
#
#    real TETRA(4,3), the vertices of the tetrahedron.
#
#  Output:
#
#    real QUALITY4, the value of the quality measure.
#
  import numpy as np
#
#  Compute the vectors that represent the sides.
#
  ab = tetra[1,:] - tetra[0,:]
  ac = tetra[2,:] - tetra[0,:]
  ad = tetra[3,:] - tetra[0,:]
  bc = tetra[2,:] - tetra[1,:]
  bd = tetra[3,:] - tetra[1,:]
  cd = tetra[3,:] - tetra[2,:]
#
#  Compute the lengths of the sides.
#
  lab = np.linalg.norm ( ab )
  lac = np.linalg.norm ( ac )
  lad = np.linalg.norm ( ad )
  lbc = np.linalg.norm ( bc )
  lbd = np.linalg.norm ( bd )
  lcd = np.linalg.norm ( cd )
#
#  Compute the volume
#
  volume = np.abs ( \
      ab[0] * ( ac[1] * ad[2] - ac[2] * ad[1] ) \
    + ab[1] * ( ac[2] * ad[0] - ac[0] * ad[2] ) \
    + ab[2] * ( ac[0] * ad[1] - ac[1] * ad[0] ) ) / 6.0

  quality4 = 1.0

  l1 = lab + lac
  l2 = lab + lad
  l3 = lac + lad

  denom = ( l1 + lbc ) * ( l1 - lbc ) \
        * ( l2 + lbd ) * ( l2 - lbd ) \
        * ( l3 + lcd ) * ( l3 - lcd )

  if ( denom <= 0.0 ):
    quality4 = 0.0
  else:
    quality4 = min ( quality4, 12.0 * volume / np.sqrt ( denom ) )

  l1 = lab + lbc
  l2 = lab + lbd
  l3 = lbc + lbd

  denom = ( l1 + lac ) * ( l1 - lac ) \
        * ( l2 + lad ) * ( l2 - lad ) \
        * ( l3 + lcd ) * ( l3 - lcd )

  if ( denom <= 0.0 ):
    quality4 = 0.0
  else:
    quality4 = min ( quality4, 12.0 * volume / np.sqrt ( denom ) )

  l1 = lac + lbc
  l2 = lac + lcd
  l3 = lbc + lcd

  denom = ( l1 + lab ) * ( l1 - lab ) \
        * ( l2 + lad ) * ( l2 - lad ) \
        * ( l3 + lbd ) * ( l3 - lbd )

  if ( denom <= 0.0 ):
    quality4 = 0.0
  else:
    quality4 = min ( quality4, 12.0 * volume / np.sqrt ( denom ) )

  l1 = lad + lbd
  l2 = lad + lcd
  l3 = lbd + lcd

  denom = ( l1 + lab ) * ( l1 - lab ) \
        * ( l2 + lac ) * ( l2 - lac ) \
        * ( l3 + lbc ) * ( l3 - lbc )

  if ( denom <= 0.0 ):
    quality4 = 0.0
  else:
    quality4 = min ( quality4, 12.0 * volume / np.sqrt ( denom ) )

  quality4 = quality4 * 1.5 * np.sqrt ( 6.0 )

  return quality4

def tetrahedron_quality4_test ( ):

#*****************************************************************************80
#
## tetrahedron_quality4_test() tests tetrahedron_quality4()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.816496580927726 ], \
    [  0.0,                0.0, 0.816496580927726 ] ] )

  t2 = np.array ( [ \
    [  0.577350269189626,  0.0, 0.0               ], \
    [ -0.288675134594813,  0.5, 0.0               ], \
    [ -0.288675134594813, -0.5, 0.0               ], \
    [  0.0,                0.0, 0.408248290463863 ] ] )


  print ( '' )
  print ( 'tetrahedron_quality4_test():' )
  print ( '  tetrahedron_quality4() computes quality measure #4' )
  print ( '  for a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron vertices:' )
  print ( t1 )
  quality4 = tetrahedron_quality4 ( t1 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality4 )

  print ( '' )
  print ( '  tetrahedron vertices:' )
  print ( t2 )
  quality4 = tetrahedron_quality4 ( t2 )
  print ( '' )
  print ( '  Tetrahedron quality is ', quality4 )

  return

def tetrahedron_rhombic_size ( ):

#*****************************************************************************80
#
## tetrahedron_rhombic_size() gives "sizes" for a rhombic tetrahedron.
#
#  Discussion:
#
#    Call this routine first, in order to learn the required dimensions
#    of arrays to be set up by tetrahedron_rhombic_shape().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer POINT_NUM, the number of vertices.
#
#    integer EDGE_NUM, the number of edges.
#
#    integer FACE_NUM, the number of faces.
#
#    integer FACE_ORDER_MAX, the maximum order of any face.
#
  point_num = 10
  edge_num = 6
  face_num = 4
  face_order_max = 6

  return point_num, edge_num, face_num, face_order_max

def tetrahedron_rhombic_shape ( point_num, face_num, face_order_max ):

#*****************************************************************************80
#
## tetrahedron_rhombic_shape() describes a rhombic tetrahedron.
#
#  Discussion:
#
#    Call tetrahedron_rhombic_size() first, to get dimension information.
#
#    The tetrahedron is described using 10 nodes.  If we label the vertices
#    P0, P1, P2 and P3, then the extra nodes lie halfway between vertices,
#    and have the labels P01, P02, P03, P12, P13 and P23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Anwei Liu, Barry Joe,
#    Quality Local Refinement of Tetrahedral Meshes Based
#    on 8-Subtetrahedron Subdivision,
#    Mathematics of Computation,
#    Volume 65, Number 215, July 1996, pages 1183-1200.
#
#  Input:
#
#    integer POINT_NUM, the number of points in the shape.
#
#    integer FACE_NUM, the number of faces in the shape.
#
#    integer FACE_ORDER_MAX, the maximum number of vertices per face.
#
#  Output:
#
#    real POINT_COORD[POINT_NUM,3], the vertices.
#
#    integer FACE_ORDER(FACE_NUM), the number of vertices
#    for each face.
#
#    integer FACE_POINT(FACE_NUM,FACE_ORDER_MAX) FACE_POINT(I,J)
#    contains the index of the J-th point in the I-th face.  The
#    points are listed in the counter clockwise direction defined
#    by the outward normal at the face.
#
  import numpy as np

  a =           1.0   / np.sqrt ( 3.0 )
  b = np.sqrt ( 2.0 ) / np.sqrt ( 3.0 )
  c = np.sqrt ( 3.0 ) /           6.0
  d =           1.0   / np.sqrt ( 6.0 )
  z = 0.0
#
#  Set the point coordinates.
#
  point_coord = np.array ( [ \
    [ -b,  z,  z ], \
    [  z, -a,  z ], \
    [  z,  a,  z ], \
    [  z,  z,  b ], \
    [ -d, -c,  z ], \
    [ -d,  c,  z ], \
    [ -d,  z,  d ], \
    [  z,  z,  z ], \
    [  z, -c,  d ], \
    [  z,  c,  d ] ] )
#
#  Set the face orders.
#
  face_order = np.array ( [ 6, 6, 6, 6 ] )
#
#  Set faces.
#
  face_point = np.array ( [ \
    [ 0,  4,  1,  8,  3,  6 ], \
    [ 1,  7,  2,  9,  3,  8 ], \
    [ 2,  5,  0,  6,  3,  9 ], \
    [ 0,  5,  2,  7,  1,  4 ] ] )

  return point_coord, face_order, face_point

def tetrahedron_rhombic_shape_test ( ):

#*****************************************************************************80
#
## tetrahedron_rhombic_shape_test() tests tetrahedron_rhombic_shape().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'tetrahedron_rhombic_shape_test():' )
  print ( '  tetrahedron_rhombic_size() returns dimension information' )
  print ( '  tetrahedron_rhombic_shape() returns face and order info.' )
  print ( '' )
  print ( '  We will use this information to compute the' )
  print ( '  areas and centers of each face.' )

  point_num, edge_num, face_num, face_order_max = tetrahedron_rhombic_size ( )

  print ( '' )
  print ( '  Number of points =   ', point_num )
  print ( '  Number of edges =    ', edge_num )
  print ( '  Number of faces =    ', face_num )
  print ( '  Maximum face order = ', face_order_max )

  point_coord, face_order, face_point = \
    tetrahedron_rhombic_shape ( point_num, face_num, face_order_max )

  shape_print ( point_num, face_num, face_order_max, \
    point_coord, face_order, face_point )
#
#  Compute the area of each face.
#
  print ( '' )
  print ( '  Face  Order  Area' )
  print ( '' )

  for face in range ( 0, face_num ):

    v = np.zeros ( [ face_order[face], 3 ] )
    for j in range ( 0, face_order[face] ):
      point = face_point[face,j]
      v[j,:] = point_coord[point,:]

    area, normal = polygon_area_3d ( face_order[face], v )

    print ( face, face_order[face], area )
#
#  Find the center of each face.
#
  print ( '' )
  print ( '  Face  Center' )
  print ( '' )

  for face in range ( 0, face_num ):

    center = np.zeros ( 3 )

    for j in range ( 0, face_order[face] ):
      k = face_point[face,j]
      center = center + point_coord[k,:]

    center = center / face_order[face]

    print ( face, center )

  return

def tetrahedron_sample ( t, n, rng ):

#*****************************************************************************80
#
## tetrahedron_sample() returns random points in a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(4,3), the tetrahedron vertices.
#
#    integer N, the number of points to generate.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real P(N,3), random points in the tetrahedron.
#
  import numpy as np

  p = np.zeros ( [ n, 3 ] )

  for i in range ( 0, n ):

    r = rng.random ( )
#
#  Interpret R as a percentage of the tetrahedron's volume.
#
#  Imagine a plane, parallel to face 1, so that the volume between
#  vertex 1 and the plane is R percent of the full tetrahedron volume.
#
#  The plane will intersect sides 12, 13, and 14 at a fraction
#  ALPHA = R^1/3 of the distance from vertex 1 to vertices 2, 3, and 4.
#
    alpha = r ** ( 1.0 / 3.0 )
#
#  Determine the coordinates of the points on sides 12, 13 and 14 intersected
#  by the plane, which form a triangle TR.
#
    tr = np.zeros ( [ 3, 3 ] )

    tr[:,0] = alpha * t[0,:] + ( 1.0 - alpha ) * t[1,:]
    tr[:,1] = alpha * t[0,:] + ( 1.0 - alpha ) * t[2,:]
    tr[:,2] = alpha * t[0,:] + ( 1.0 - alpha ) * t[3,:]
#
#  Now choose, uniformly at random, a point in this triangle.
#
    r = rng.random ( )
#
#  Interpret R as a percentage of the triangle's area.
#
#  Imagine a line L, parallel to side 1, so that the area between
#  vertex 1 and line L is R percent of the full triangle's area.
#
#  The line L will intersect sides 2 and 3 at a fraction
#  ALPHA = SQRT ( R ) of the distance from vertex 1 to vertices 2 and 3.
#
    alpha = np.sqrt ( r )
#
#  Determine the coordinates of the points on sides 2 and 3 intersected
#  by line L.
#
    p12 = alpha * tr[:,0] + ( 1.0 - alpha ) * tr[:,1]
    p13 = alpha * tr[:,0] + ( 1.0 - alpha ) * tr[:,2]
#
#  Now choose, uniformly at random, a point on the line L.
#
    beta = rng.random ( )

    p[i,:] = beta * p12[:] + ( 1.0 - beta ) * p13[:]

  return p

def tetrahedron_sample_test ( rng ):

#*****************************************************************************80
#
## tetrahedron_sample_test() tests tetrahedron_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  t = np.array ( [ \
     [ 1.0, 4.0, 3.0 ], \
     [ 2.0, 4.0, 3.0 ], \
     [ 1.0, 6.0, 3.0 ], \
     [ 1.0, 4.0, 4.0 ] ] )

  print ( '' )
  print ( 'tetrahedron_sample_test():' )
  print ( '  tetrahedron_sample() samples a tetrahedron.' )
  print ( '  We are computing the XSI coordinates just to verify' )
  print ( '  that the points are inside the tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron vertices' )
  print ( t )

  print ( '' )
  print ( '  (X,Y,Z)   (XSI1,XSI2,XSI3,XSI4):' )
  print ( '' )

  for i in range ( 0, 10 ):
    p = tetrahedron_sample ( t, 1, rng )
    p = p.flatten ( )
    xsi = tetrahedron_barycentric ( t, p )
    print ( p, xsi )

  return

def tetrahedron_shape ( point_num, face_num, face_order_max ):

#*****************************************************************************80
#
## tetrahedron_shape() describes a tetrahedron.
#
#  Discussion:
#
#    Call tetrahedron_size() first, to get dimension information.
#
#    The vertices lie on the unit sphere.
#
#    The dual of the tetrahedron is the tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer POINT_NUM, the number of points in the shape.
#
#    integer FACE_NUM, the number of faces in the shape.
#
#    integer FACE_ORDER_MAX, the maximum number of vertices per face.
#
#  Output:
#
#    real POINT_COORD[POINT_NUM,3], the vertices.
#
#    integer FACE_ORDER(FACE_NUM), the number of vertices
#    for each face.
#
#    integer FACE_POINT[FACE_NUM,FACE_ORDER_MAX) FACE_POINT(I,J)
#    contains the index of the J-th point in the I-th face.  The
#    points are listed in the counter-clockwise direction defined
#    by the outward normal at the face.
#
  import numpy as np
#
#  Set the point coordinates.
#
  point_coord = np.array ( [ \
      [  0.942809,    0.000000,   -0.333333 ], \
      [ -0.471405,    0.816497,   -0.333333 ], \
      [ -0.471405,   -0.816497,   -0.333333 ], \
      [  0.000000,    0.000000,    1.000000 ] ] )
#
#  Set the face orders.
#
  face_order = np.array ( [ 3, 3, 3, 3 ] )
#
#  Set faces.
#
  face_point = np.array ( [ \
     [ 0, 2, 1 ], \
     [ 0, 1, 3 ], \
     [ 0, 3, 2 ], \
     [ 1, 2, 3 ] ] )

  return point_coord, face_order, face_point

def tetrahedron_size ( ):

#*****************************************************************************80
#
## tetrahedron_size() gives "sizes" for a tetrahedron.
#
#  Discussion:
#
#    Call this routine first, in order to learn the required dimensions
#    of arrays to be set up by tetrahedron_shape().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer POINT_NUM, the number of vertices.
#
#    integer EDGE_NUM, the number of edges.
#
#    integer FACE_NUM, the number of faces.
#
#    integer FACE_ORDER_MAX, the maximum order of any face.
#
  point_num = 4
  edge_num = 6
  face_num = 4
  face_order_max = 3

  return point_num, edge_num, face_num, face_order_max

def tetrahedron_shape_test ( ):

#*****************************************************************************80
#
## tetrahedron_shape_test() tests tetrahedron_shape().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'tetrahedron_shape_test():' )
  print ( '  tetrahedron_size() returns dimension information' )
  print ( '  tetrahedron_shape() returns face and order info.' )
  print ( '' )
  print ( '  We will use this information to compute the' )
  print ( '  areas and centers of each face.' )

  point_num, edge_num, face_num, face_order_max = tetrahedron_size ( )

  print ( '' )
  print ( '  Number of points =   ', point_num )
  print ( '  Number of edges =    ', edge_num )
  print ( '  Number of faces =    ', face_num )
  print ( '  Maximum face order = ', face_order_max )

  point_coord, face_order, face_point = \
    tetrahedron_shape ( point_num, face_num, face_order_max )

  shape_print ( point_num, face_num, face_order_max, \
    point_coord, face_order, face_point )
#
#  Compute the area of each face.
#
  print ( '' )
  print ( '  Face  Order  Area' )
  print ( '' )

  for face in range ( 0, face_num ):

    v = np.zeros ( [ face_order[face], 3 ] )
    for j in range ( 0, face_order[face] ):
      point = face_point[face,j]
      v[j,:] = point_coord[point,:]

    area, normal = polygon_area_3d ( face_order[face], v )

    print ( face, face_order[face], area )
#
#  Find the center of each face.
#
  print ( '' )
  print ( '  Face  Center' )
  print ( '' )

  for face in range ( 0, face_num ):

    center = np.zeros ( 3 )

    for j in range ( 0, face_order[face] ):
      k = face_point[face,j]
      center = center + point_coord[k,:]

    center = center / face_order[face]

    print ( face, center )

  return

def tetrahedron_solid_angles ( tetra ):

#*****************************************************************************80
#
## tetrahedron_solid_angles() computes solid angles of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TETRA(4,3), the vertices of the tetrahedron.
#
#  Output:
#
#    real ANGLE[3], the solid angles.
#
  import numpy as np

  dihedral_angles = tetrahedron_dihedral_angles ( tetra )

  angle = np.zeros ( 4 )
  angle[0] = dihedral_angles[0] + dihedral_angles[1] + dihedral_angles[2] - np.pi
  angle[1] = dihedral_angles[0] + dihedral_angles[3] + dihedral_angles[4] - np.pi
  angle[2] = dihedral_angles[1] + dihedral_angles[3] + dihedral_angles[5] - np.pi
  angle[3] = dihedral_angles[2] + dihedral_angles[4] + dihedral_angles[5] - np.pi

  return angle

def tetrahedron_solid_angles_test ( ):

#*****************************************************************************80
#
## tetrahedron_solid_angles_test() tests tetrahedron_solid_angles()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t1 = np.array ( [ \
    [ 0.000000,  0.942809, -0.333333 ], \
    [-0.816496, -0.816496, -0.333333 ], \
    [ 0.816496, -0.816496, -0.333333 ], \
    [ 0.000000,  0.000000,  1.000000 ] ] )
  t2 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  1.000000,  0.000000 ], \
    [ 0.000000,  0.000000,  1.000000 ] ] )
  t3 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  2.000000,  0.000000 ], \
    [ 0.000000,  0.000000,  4.000000 ] ] )
  t4 = np.array ( [ \
    [ 0.000000,  0.000000,  0.000000 ], \
    [ 1.000000,  0.000000,  0.000000 ], \
    [ 0.000000,  1.000000,  0.000000 ], \
    [ 1.000000,  1.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_solid_angles_test():' )
  print ( '  tetrahedron_solid_angles() computes the solid angles' )
  print ( '  associated with the vertices of a tetrahedron.' )

  print ( '' )
  print ( '  tetrahedron1 vertices:' )
  print ( t1 )
  angle = tetrahedron_solid_angles ( t1 )
  print ( '' )
  print ( '  solid angles:' )
  print ( angle )

  print ( '' )
  print ( '  tetrahedron2 vertices:' )
  print ( t2 )
  angle = tetrahedron_solid_angles ( t2 )
  print ( '' )
  print ( '  solid angles:' )
  print ( angle )

  print ( '' )
  print ( '  tetrahedron3 vertices:' )
  print ( t3 )
  print ( '' )
  print ( '  solid angles:' )
  print ( angle )

  print ( '' )
  print ( '  tetrahedron4 vertices:' )
  print ( t4 )
  angle = tetrahedron_solid_angles ( t4 )
  print ( '' )
  print ( '  solid angles:' )
  print ( angle )

  return

def tetrahedron_volume ( tetra ):

#*****************************************************************************80
#
## tetrahedron_volume() computes the volume of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real tetra(4,3): the vertices of the tetrahedron.
#
#  Output:
#
#    real volume: the volume of the tetrahedron.
#
  import numpy as np

  a = np.zeros ( [ 4, 4 ] )
  a[0:4,0:3] = tetra[0:4,0:3]
  a[0:4,3] = 1.0

  volume = np.abs ( np.linalg.det ( a ) ) / 6.0

  return volume

def tetrahedron_volume_test ( ):

#*****************************************************************************80
#
## tetrahedron_volume_test() tests tetrahedron_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [  0.000000,  0.942809, -0.333333 ], \
    [ -0.816496, -0.816496, -0.333333 ], \
    [  0.816496, -0.816496, -0.333333 ], \
    [  0.000000,  0.000000,  1.000000 ] ] )

  print ( '' )
  print ( 'tetrahedron_volume_test():' )
  print ( '  tetrahedron_volume() computes the volume of a tetrahedron' )

  print ( '' )
  print ( '  tetrahedron vertices' )
  print ( t )

  volume = tetrahedron_volume ( t )

  print ( '' )
  print ( '  Volume = ', volume )

  return

def tetrahedron01_lattice_point_num ( s ):

#*****************************************************************************80
#
## tetrahedron01_lattice_point_num() counts lattice points.
#
#  Discussion:
#
#    The tetrahedron is assumed to be the unit tetrahedron:
#
#    ( (0,0,0), (1,0,0), (0,1,0), (0,0,1) )
#
#    or a copy of this tetrahedron scaled by an integer S:
#
#    ( (0,0,0), (S,0,0), (0,S,0), (0,0,S) ).
#
#    The routine returns the number of integer lattice points that appear
#    inside the tetrahedron, or on its faces, edges or vertices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 July 2009
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Matthias Beck, Sinai Robins,
#    Computing the Continuous Discretely,
#    Springer, 2006,
#    ISBN13: 978-0387291390,
#    LC: QA640.7.B43.
#
#  Input:
#
#    integer S, the scale factor, 0 <= S.
#
#  Output:
#
#    integer N, the number of lattice points.
#
  n = ( ( s + 3 ) * ( s + 2 ) * ( s + 1 ) ) // 6

  return n

def tetrahedron01_lattice_point_num_test ( ):

#*****************************************************************************80
#
## tetrahedron01_lattice_point_num_test() tests tetrahedron01_lattice_point_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tetrahedron01_lattice_point_num_test():' )
  print ( '  tetrahedron01_lattice_point_num() counts' )
  print ( '  lattice points inside the unit tetrahedron.' )

  print ( '' )
  for s in range ( 0, 11 ):
    n = tetrahedron01_lattice_point_num ( s )
    print ( '  ', s, '  ', n )

  return

def tetrahedron01_sample ( n, rng ):

#*****************************************************************************80
#
## tetrahedron01_sample() samples the unit tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Krieger, 1992,
#    ISBN: 0894647644,
#    LC: QA298.R79.
#
#  Input:
#
#    integer N, the number of points.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(3,N), the points.
#
  import numpy as np

  m = 3

  x = np.zeros ( [ m, n ] )
  el = np.zeros ( m + 1 )

  for j in range ( 0, n ):

    e = rng.random ( size = m + 1 )

    el_sum = 0.0
    for i in range ( 0, m + 1 ):
      el[i] = - np.log ( e[i] )
      el_sum = el_sum + el[i]

    for i in range ( 0, m ):
      x[i,j] = el[i] / el_sum

  return x

def tetrahedron01_sample_test ( rng ):

#*****************************************************************************80
#
## tetrahedron01_sample_test() tests tetrahedron01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'tetrahedron01_sample_test()' )
  print ( '  tetrahedron01_sample() samples the unit tetrahedron.' )

  m = 3
  n = 10
  x = tetrahedron01_sample ( n, rng )

  print ( '' )
  print ( '  Sample points in the unit tetrahedron:' )
  print ( x )

  return

def tetrahedron01_volume ( ):

#*****************************************************************************80
#
## tetrahedron01_volume() returns the volume of the unit tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VOLUME, the volume.
#
  value = 1.0 / 6.0

  return value

def tetrahedron01_volume_test ( ) :

#*****************************************************************************80
#
## tetrahedron01_volume_test() tests tetrahedron01_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tetrahedron01_volume_test():' )
  print ( '  tetrahedron01_volume() returns the volume of the unit tetrahedron.' )

  value = tetrahedron01_volume ( )

  print ( '' )
  print ( '  tetrahedron01_volume() = ', value )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def triangle_angles_3d ( t ):

#*****************************************************************************80
#
## triangle_angles_3d() computes the angles of a triangle in 3D.
#
#  Discussion:
#
#    The law of cosines is used:
#
#      C * C = A * A + B * B - 2 * A * B * COS ( GAMMA )
#
#    where GAMMA is the angle opposite side C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,3), the triangle vertices.
#
#  Output:
#
#    real ANGLE(3), the angles opposite
#    sides P1-P2, P2-P3 and P3-P1, in radians.
#
  import numpy as np
#
#  Compute the length of each side.
#
  a = np.linalg.norm ( t[0,:] - t[1,:] )
  b = np.linalg.norm ( t[1,:] - t[2,:] )
  c = np.linalg.norm ( t[2,:] - t[0,:] )

  angle = np.zeros ( 3 )
#
#  Take care of a special case.
#
  if ( a == 0.0 and b == 0.0 and c == 0.0 ):
    angle[0:3] = 2.0 * np.pi / 3.0
  else:

    if ( c == 0.0 or a == 0.0 ):
      angle[0] = np.pi
    else:
      angle[0] = np.arccos ( ( c * c + a * a - b * b ) / ( 2.0 * c * a ) )

    if ( a == 0.0 or b == 0.0 ):
      angle[1] = np.pi
    else:
      angle[1] = np.arccos ( ( a * a + b * b - c * c ) / ( 2.0 * a * b ) )

    if ( b == 0.0 or c == 0.0 ):
      angle[2] = np.pi
    else:
      angle[2] = np.arccos ( ( b * b + c * c - a * a ) / ( 2.0 * b * c ) )

  return angle

def triangle_angles_3d_test ( ):

#*****************************************************************************80
#
## triangle_angles_3d_test() tests triangle_angles_3d()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2005
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
  print ( 'triangle_angles_3d_test():' )
  print ( '  triangle_angles_3d() computes the angles of a triangle in 3D.' )
  print ( '' )
  print ( '  triangle vertices:' )
  print ( t )

  angle = triangle_angles_3d ( t )

  print ( '' )
  print ( '      Radians      Degrees' )
  print ( '' )

  for i in range ( 0, 3 ):
    print ( angle[i], angle[i] * 180.0 / np.pi )

  return

def triangle_area_3d ( t ):

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
#    07 May 2022
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
#    real T(3,3), the triangle vertices.
#
#  Output:
#
#    real AREA, the area of the triangle.
#
  import numpy as np
#
#  Compute the cross product vector.
#
  cross = np.zeros ( 3 )

  cross[0] = ( t[1,1] - t[0,1] ) * ( t[2,2] - t[0,2] ) \
           - ( t[1,2] - t[0,2] ) * ( t[2,1] - t[0,1] )

  cross[1] = ( t[1,2] - t[0,2] ) * ( t[2,0] - t[0,0] ) \
           - ( t[1,0] - t[0,0] ) * ( t[2,2] - t[0,2] )

  cross[2] = ( t[1,0] - t[0,0] ) * ( t[2,1] - t[0,1] ) \
           - ( t[1,1] - t[0,1] ) * ( t[2,0] - t[0,0] )

  area = 0.5 * np.linalg.norm ( cross )

  return area

def triangle_area_3d_test ( ):

#*****************************************************************************80
#
## triangle_area_3d_test() tests triangle_area_3d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0,   2.4142137,  1.7071068 ], \
    [ 2.0,   3.4142137,  2.7071068 ], \
    [ 3.0,   3.0,        4.0       ] ] )     

  print ( '' )
  print ( 'triangle_area_3d_test():' )
  print ( '  triangle_area_3d() computes the area of a triangle in 3D.' )

  print ( '' )
  print ( '  triangle vertices:' )
  print ( t )

  area = triangle_area_3d ( t )

  print ( '' )
  print ( '  Area = ', area )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  tetrahedron_test ( )
  timestamp ( )

