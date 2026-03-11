#! /usr/bin/env python3
#
def triangle_test ( ):

#*****************************************************************************80
#
## triangle_test() tests triangle().
#
#  Discussion:
#
#    Warning: most of these functions use a triangle dimension of [2,3]
#    but now I am convinced I should use [3,2].
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle().' )

  rng = default_rng ( )

  i4_modp_test ( )
  i4_wrap_test ( )

  segment_point_dist_2d_test ( )

  triangle_angles_test ( )
  triangle_area_test ( )
  triangle_centroid_test ( )
  triangle_circumcircle_test ( )
  triangle_contains_point_test ( )
  triangle_diameter_test ( )
  triangle_edge_length_test ( )
  triangle_incircle_test ( )
  triangle_orientation_test ( )
  triangle_orthocenter_test ( )
  triangle_point_dist_test ( )
  triangle_point_near_test ( )
  triangle_quality_test ( )
  triangle_reference_sample_test ( rng )
  triangle_sample_test ( rng )
  triangle_sample_reflect_test ( rng )
  triangle_xsi_to_xy_test ( rng )
  triangle_xy_to_xsi_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_test():' )
  print ( '  Normal end of execution.' )
  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = i4_modp ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, i4_modp(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  i4_modp    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
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
#  Input:
#
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  i4_modp factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
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
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IVAL, an integer value.
#
#    integer ILO, IHI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of IVAL.
#
  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

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
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test' )
  print ( '  i4_wrap forces an integer to lie within given limits.' )
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

def line_exp2imp_2d ( p1, p2 ):

#*****************************************************************************80
#
## line_exp2imp_2d() converts an explicit line to implicit form in 2D.
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      ( P1, P2 ) = ( (X1,Y1), (X2,Y2) ).
#
#    The implicit form of a line in 2D is:
#
#      A * X + B * Y + C = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2,1), P2(2,1), two points on the line.
#
#  Output:
#
#    real A, B, C, the implicit form of the line.
#

#
#  Take care of degenerate cases.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):
    print ( '' )
    print ( 'line_exp2imp_2d - Fatal error!' )
    print ( '  P1 = P2' )
    print ( '  P1 = %g  %g' % ( p1[0], p1[1] ) )
    print ( '  P2 = %g  %g' % ( p2[0], p2[1] ) )
    raise Exception ( 'line_exp2imp_2d - Fatal error!' )

  a = p2[1] - p1[1]
  b = p1[0] - p2[0]
  c = p2[0] * p1[1] - p1[0] * p2[1]

  norm = a * a + b * b + c * c

  if ( 0.0 < norm ):
    a = a / norm
    b = b / norm
    c = c / norm

  if ( a < 0.0 ):
    a = -a
    b = -b
    c = -c

  return a, b, c

def line_exp_perp_2d ( p1, p2, p3 ):

#*****************************************************************************80
#
## line_exp_perp_2d() computes a line perpendicular to a line and through a point.
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      ( P1, P2 ) = ( (X1,Y1), (X2,Y2) ).
#
#    The input point P3 should NOT lie on the line (P1,P2).  If it
#    does, then the output value P4 will equal P3.
#
#    P1-----P4-----------P2
#            |
#            |
#           P3
#
#    P4 is also the nearest point on the line (P1,P2) to the point P3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2), P2(2), two points on the line.
#
#    real P3(2), a point (presumably not on the
#    line (P1,P2)), through which the perpendicular must pass.
#
#  Output:
#
#    real P4(2), a point on the line (P1,P2),
#    such that the line (P3,P4) is perpendicular to the line (P1,P2).
#
#    logical FLAG, is TRUE if the value could not be computed.
#
  import numpy as np

  bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) **2

  p4 = np.zeros ( 2 )

  if ( bot == 0.0 ):
    p4[0] = float ( 'inf' )
    p4[1] = float ( 'inf' )
    flag = 1
#
#  (P3-P1) dot (P2-P1) = Norm(P3-P1) * Norm(P2-P1) * Cos(Theta).
#
#  (P3-P1) dot (P2-P1) / Norm(P3-P1)**2 = normalized coordinate T
#  of the projection of (P3-P1) onto (P2-P1).
#
  t = ( ( p1[0] - p3[0] ) * ( p1[0] - p2[0] ) \
      + ( p1[1] - p3[1] ) * ( p1[1] - p2[1] ) ) / bot

  p4[0] = p1[0] + t * ( p2[0] - p1[0] )
  p4[1] = p1[1] + t * ( p2[1] - p1[1] )

  flag = 0

  return p4, flag

def lines_exp_int_2d ( p1, p2, q1, q2 ):

#*****************************************************************************80
#
## lines_exp_int_2d() determines where two explicit lines intersect in 2D.
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      the line through the points P1, P2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2,1), P2(2,1), two points on the first line.
#
#    real Q1(2,1), Q2(2,1), two points on the second line.
#
#  Output:
#
#    integer IVAL, reports on the intersection:
#    0, no intersection, the lines may be parallel or degenerate.
#    1, one intersection point, returned in P.
#    2, infinitely many intersections, the lines are identical.
#
#    real P(2,1), if IVAl = 1, P is
#    the intersection point.  Otherwise, P = 0.
#
  import numpy as np

  ival = False
  p = np.zeros ( 2 )
#
#  Check whether either line is a point.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):
    point_1 = True
  else:
    point_1 = False

  if ( q1[0] == q2[0] and q1[1] == q2[1] ):
    point_2 = True
  else:
    point_2 = False
#
#  Convert the lines to ABC format.
#
  if ( not point_1 ):
    a1, b1, c1 = line_exp2imp_2d ( p1, p2 )

  if ( not point_2 ):
    a2, b2, c2 = line_exp2imp_2d ( q1, q2 )
#
#  Search for intersection of the lines.
#
  if ( point_1 and point_2 ):
    if ( p1[0] == q1[0] and p1[1] == q1[1] ):
      ival = True
      p[0] = p1[0]
      p[1] = p1[1]
  elif ( point_1 ):
    if ( a2 * p1[0] + b2 * p1[1] == c2 ):
      ival = True
      p[0] = p1[0]
      p[1] = p1[1]
  elif ( point_2 ):
    if ( a1 * q1[0] + b1 * q1[1] == c1 ):
      ival = True
      p[0] = q1[0]
      p[1] = q1[1]
  else:
    ival, p = lines_imp_int_2d ( a1, b1, c1, a2, b2, c2 )

  return ival, p

def lines_imp_int_2d ( a1, b1, c1, a2, b2, c2 ):

#*****************************************************************************80
#
## lines_imp_int_2d() determines where two implicit lines intersect in 2D.
#
#  Discussion:
#
#    The implicit form of a line in 2D is:
#
#      A * X + B * Y + C = 0
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
#    real A1, B1, C1, define the first line.
#    At least one of A1 and B1 must be nonzero.
#
#    real A2, B2, C2, define the second line.
#    At least one of A2 and B2 must be nonzero.
#
#  Output:
#
#    integer IVAL, reports on the intersection.
#    -1, both A1 and B1 were zero.
#    -2, both A2 and B2 were zero.
#     0, no intersection, the lines are parallel.
#     1, one intersection point, returned in X, Y.
#     2, infinitely many intersections, the lines are identical.
#
#    real P(2,1), if IVAL = 1, then P is
#    the intersection point.  if IVAL = 2, then P is one of the
#    points of intersection.  Otherwise, P = [].
#
  import numpy as np

  p = np.zeros ( 2 )
#
#  Refuse to handle degenerate lines.
#
  if ( a1 == 0.0 and b1 == 0.0 ):
    ival = -1
    return ival, p
  elif ( a2 == 0.0 and b2 == 0.0 ):
    ival = -2
    return ival, p
#
#  Set up and solve a linear system.
#
  a = np.zeros ( [ 2, 3 ] )

  a[0,0] = a1
  a[0,1] = b1
  a[0,2] = - c1

  a[1,0] = a2
  a[1,1] = b2
  a[1,2] = - c2

  a, info = r8mat_solve ( 2, 1, a )
#
#  If the inverse exists, then the lines intersect at the solution point.
#
  if ( info == 0 ):

    ival = 1;
    p[0] = a[0,2]
    p[1] = a[1,2]
#
#  If the inverse does not exist, then the lines are parallel
#  or coincident.  Check for parallelism by seeing if the
#  C entries are in the same ratio as the A or B entries.
#
  else:

    ival = 0

    if ( a1 == 0.0 ):
      if ( b2 * c1 == c2 * b1 ):
        ival = 2
        p[0] = 0.0
        p[1] = - c1 / b1
    else:
      if ( a2 * c1 == c2 * a1 ):
        ival = 2
        if ( abs ( a1 ) < abs ( b1 ) ):
          p[0] = 0.0
          p[1] = - c1 / b1
        else:
          p[0] = - c1 / a1
          p[1] = 0.0

  return ival, p

def r8mat_solve ( n, nrhs, a ):

#*****************************************************************************80
#
## r8mat_solve() uses Gauss-Jordan elimination to solve an N by N linear system.
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
#    integer N, the order of the matrix.
#
#    integer NRHS, the number of right hand sides.  NRHS
#    must be at least 0.
#
#    real A(N,N+NRHS), contains in rows and
#    columns 1 to N the coefficient matrix, and in columns N+1 through
#    N+NRHS, the right hand sides.
#
#  Output:
#
#    real A(N,N+NRHS), the coefficient matrix
#    area has been destroyed, while the right hand sides have
#    been overwritten with the corresponding solutions.
#
#    integer INFO, singularity flag.
#    0, the matrix was not singular, the solutions were computed;
#    J, factorization failed on step J, and the solutions could not
#    be computed.
#
  info = 0

  for j in range ( 0, n ):
#
#  Choose a pivot row IPIVOT.
#
    ipivot = j
    apivot = a[j,j]

    for i in range ( j + 1, n ):
      if ( abs ( apivot ) < abs ( a[i,j] ) ):
        apivot = a[i,j]
        ipivot = i

    if ( apivot == 0.0 ):
      info = j
      return a, info
#
#  Interchange.
#
    for k in range ( 0, n + nrhs ):
      temp        = a[ipivot,k]
      a[ipivot,k] = a[j,k]
      a[j,k]      = temp
#
#  A(J,J) becomes 1.
#
    a[j,j] = 1.0
    for k in range ( j + 1, n + nrhs ):
      a[j,k] = a[j,k] / apivot;
#
#  A(I,J) becomes 0.
#
    for i in range ( 0, n ):

      if ( i != j ):

        factor = a[i,j]
        a[i,j] = 0.0
        for k in range ( j + 1, n + nrhs ):
          a[i,k] = a[i,k] - factor * a[j,k]

  return a, info

def r8mat_solve_test ( ):

#*****************************************************************************80
#
## r8mat_solve_test() tests r8mat_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3
  rhs_num = 2
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0, 14.0,  7.0 ], \
    [ 4.0, 5.0, 6.0, 32.0, 16.0 ], \
    [ 7.0, 8.0, 0.0, 23.0,  7.0 ] ] )

  print ( '' )
  print ( 'r8mat_solve_test' )
  print ( '  r8mat_solve solves linear systems.' )
#
#  Print out the matrix to be inverted.
#
  print ( '' )
  print ( '  The linear system:' )
  print ( a )
#
#  Solve the systems.
#
  a, info = r8mat_solve ( n, rhs_num, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( '  The input matrix was singular.' )
    print ( '  The solutions could not be computed.' )
    return

  print ( '' )
  print ( '  The factored matrix and solutions:' )
  print ( a )

  return

def segment_point_dist_2d ( p1, p2, p ):

#*****************************************************************************80
#
## segment_point_dist_2d(): distance ( line segment, point ) in 2D.
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

def segment_point_dist_2d_test ( ):

#*****************************************************************************80
#
## segment_point_dist_2d_test() tests segment_point_dist_2d();
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
  import platform

  print ( '' )
  print ( 'segment_point_dist_2d_test' )
  print ( '  segment_point_dist_2d computes the distance from a point to a line segment.' )

  p1 = np.array ( [ 1.0, 2.0 ] )
  p2 = np.array ( [ 3.0, 4.0 ] )

  print ( '' )
  print ( '  Segment endpoint 1:' )
  print ( p1 )
  print ( '' )
  print ( '  Segment endpoint 2:' )
  print ( p2 )

  p = np.array ( [ 2.0, 3.0 ] )
  dist = segment_point_dist_2d ( p1, p2, p )
  print ( '' )
  print ( '  Test point P:' )
  print ( p )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 4.0, 5.0 ] )
  dist = segment_point_dist_2d ( p1, p2, p )
  print ( '' )
  print ( '  Test point P:' )
  print ( p )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 1.0, 4.0 ] )
  dist = segment_point_dist_2d ( p1, p2, p )
  print ( '' )
  print ( '  Test point P:' )
  print ( p )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 0.0, 0.0 ] )
  dist = segment_point_dist_2d ( p1, p2, p )
  print ( '' )
  print ( '  Test point P:' )
  print ( p )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  return

def segment_point_near_2d ( p1, p2, p ):

#*****************************************************************************80
#
## segment_point_near_2d() finds the line segment point nearest a point in 2D.
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
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2,1), P2(2,1), the endpoints of the line segment.
#
#    real P(2,1), the point whose nearest neighbor
#    on the line segment is to be determined.
#
#  Output:
#
#    real PN(2,1), the point on the line segment which is
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

  dist = np.sqrt ( ( pn[0] - p[0] ) ** 2 + ( pn[1] - p[1] ) ** 2 )

  return pn, dist, t

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

def triangle_angles ( t ):

#*****************************************************************************80
#
## triangle_angles() computes the angles of a triangle in 2D.
#
#  Discussion:
#
#    The law of cosines is used:
#
#      C^2 = A^2 + B^2 - 2 * A * B * COS ( GAMMA )
#
#    where GAMMA is the angle opposite side C.
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
#    real T(2,3), the triangle vertices.
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
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  angle = np.zeros ( 3 )
#
#  Take care of unlikely special cases.
#
  if ( a == 0.0 and b == 0.0 and c == 0.0 ):
    for i in range ( 0, 3 ):
      angle[i] = 2.0 * np.pi / 3.0
    return angle

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

def triangle_angles_test ( ):

#*****************************************************************************80
#
## triangle_angles_test() tests triangle_angles().
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
  import platform

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_angles_test' )
  print ( '  triangle_angles computes the angles of a triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  angle = triangle_angles ( t )

  print ( '' )
  print ( '      Radians      Degrees' )
  print ( '' )
  for i in range ( 0, 3 ):
    print ( '  %12g  %12g' % ( angle[i], angle[i] * 180.0 / np.pi ) )

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
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real AREA, the area of the triangle.
#
  area = 0.5 * ( \
      t[0,0] * ( t[1,1] - t[1,2] ) \
    + t[0,1] * ( t[1,2] - t[1,0] ) \
    + t[0,2] * ( t[1,0] - t[1,1] ) )

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
  import platform

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_area_test' )
  print ( '  triangle_area computes the area of a triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  area = triangle_area ( t )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )

  return

def triangle_centroid ( t ):

#*****************************************************************************80
#
## triangle_centroid() computes the centroid of a triangle in 2D.
#
#  Discussion:
#
#    The centroid of a triangle can also be considered the
#    center of gravity, or center of mass, assuming that the triangle
#    is made of a thin uniform sheet of massy material.
#
#    The centroid of a triangle is the intersection of the medians.
#
#    A median of a triangle is a line connecting a vertex to the
#    midpoint of the opposite side.
#
#    In barycentric coordinates, in which the vertices of the triangle
#    have the coordinates (1,0,0), (0,1,0) and (0,0,1), the centroid
#    has coordinates (1/3,1/3,1/3).
#
#    In geometry, the centroid of a triangle is often symbolized by "G".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 October 2015
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
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real CENTROID(2), the coordinates of the centroid.
#
  import numpy as np

  centroid = np.zeros ( 2 )

  for i in range ( 0, 2 ):
    for j in range ( 0, 3 ):
      centroid[i] = centroid[i] + t[i,j]
    centroid[i] = centroid[i] / 3.0

  return centroid

def triangle_centroid_test ( ):

#*****************************************************************************80
#
## triangle_centroid_test() tests triangle_centroid();
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
  import platform

  ntest = 4

  print ( '' )
  print ( 'triangle_centroid_test' )
  print ( '  triangle_centroid computes the centroid of a triangle' )

  for i in range ( 0, ntest ):

    if ( i == 0 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 1.0 ] ] )
    elif ( i == 1 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 0.86602539 ] ] )
    elif ( i == 2 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    print ( '' )
    print ( '  Triangle vertices:' )
    print ( t )

    centroid = triangle_centroid ( t )

    print ( '' )
    print ( '  Centroid:' )
    print ( centroid )

  return

def triangle_circumcircle ( t ):

#*****************************************************************************80
#
## triangle_circumcircle() computes the circumcircle of a triangle in 2D.
#
#  Discussion:
#
#    The circumcenter of a triangle is the center of the circumcircle, the
#    circle that passes through the three vertices of the triangle.
#
#    The circumcircle contains the triangle, but it is not necessarily the
#    smallest triangle to do so.
#
#    If all angles of the triangle are no greater than 90 degrees, then
#    the center of the circumscribed circle will lie inside the triangle.
#    Otherwise, the center will lie outside the triangle.
#
#    The circumcenter is the intersection of the perpendicular bisectors
#    of the sides of the triangle.
#
#    In geometry, the circumcenter of a triangle is often symbolized by "O".
#
#    Thanks to Chenguang Zhang for pointing out a mistake in the formula
#    for the center, 02 December 2016.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real R, CENTER(2,1), the circumradius and circumcenter
#    of the triangle.
#
  import numpy as np

  center = np.zeros ( 2 )
#
#  Circumradius.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  bot = ( a + b + c ) * ( - a + b + c ) * (   a - b + c ) * (   a + b - c )

  if ( bot <= 0.0 ):
    r = - 1.0
    return r, center

  r = a * b * c / np.sqrt ( bot )
#
#  Circumcenter.
#
  f = np.zeros ( 2 )

  f[0] = ( t[0,1] - t[0,0] ) ** 2 + ( t[1,1] - t[1,0] ) ** 2
  f[1] = ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2

  top = np.zeros ( 2 )

  top[0] =    ( t[1,2] - t[1,0] ) * f[0] - ( t[1,1] - t[1,0] ) * f[1]
  top[1] =  - ( t[0,2] - t[0,0] ) * f[0] + ( t[0,1] - t[0,0] ) * f[1]

  det  =    ( t[1,2] - t[1,0] ) * ( t[0,1] - t[0,0] ) \
          - ( t[1,1] - t[1,0] ) * ( t[0,2] - t[0,0] ) 

  center[0] = t[0,0] + 0.5 * top[0] / det
  center[1] = t[1,0] + 0.5 * top[1] / det

  return r, center

def triangle_circumcircle_test ( ):

#*****************************************************************************80
#
## triangle_circumcircle_test() tests triangle_circumcircle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_circumcircle_test' )
  print ( '  triangle_circumcircle computes the circumcenter of a triangle.' )

  for i in range ( 0, 4 ):

    if ( i == 0 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 1.0 ] ] )
    elif ( i == 1 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 0.86602539 ] ] )
    elif ( i == 2 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    print ( '' )
    print ( '  Triangle vertices:' )
    print ( t )

    r, center = triangle_circumcircle ( t )

    print ( '' )
    print ( '  Circumcenter:' )
    print ( center )

    print ( '' )
    print ( '  Circumradius: %g' % ( r ) )

  return

def triangle_contains_point ( t, p ):

#*****************************************************************************80
#
## triangle_contains_point() finds if a point is inside a triangle in 2D.
#
#  Discussion:
#
#    The routine assumes that the vertices are given in counter-clockwise
#    order.  If the triangle vertices are actually given in clockwise
#    order, this routine will behave as though the triangle contains
#    no points whatsoever!
#
#    The routine determines if a point P is "to the right of" each of the lines
#    that bound the triangle.  It does this by computing the cross product
#    of vectors from a vertex to its next vertex, and to P.
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
#    real T(2,3), the triangle vertices.
#    The vertices should be given in counter clockwise order.
#
#    real P(2,1), the point to be checked.
#
#  Output:
#
#    logical INSIDE, is TRUE if the point is inside
#    the triangle or on its boundary.
#
  inside = True

  for j in range ( 0, 3 ):

    jp1 = i4_wrap ( j + 1, 0, 2 )

    if ( 0.0 < ( p[0] - t[0,j] ) * ( t[1,jp1] - t[1,j] ) \
             - ( p[1] - t[1,j] ) * ( t[0,jp1] - t[0,j] ) ):
      inside = False
      return inside

  return inside

def triangle_contains_point_test ( ):

#*****************************************************************************80
#
## triangle_contains_point_test() tests triangle_contains_point().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2006
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 7

  p_test = np.array ( [ \
    [ 0.25,   0.75,   1.00,  11.00,   0.00,   0.50,  0.60 ], \
    [ 0.25,   0.25,   1.00,   0.50,   1.00, -10.00,  0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  p = np.zeros ( 2 )

  print ( '' )
  print ( 'triangle_contains_point_test' )
  print ( '  triangle_contains_point reports if a point' )
  print ( '  is inside a triangle' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '     X       Y     Inside' )
  print ( '' )

  for j in range ( 0, test_num ):

    p[0] = p_test[0,j]
    p[1] = p_test[1,j]

    inside = triangle_contains_point ( t, p )

    print ( '  %10g  %10g  %s' % ( p[0], p[1], inside ) )
#
#  Make a copy of the triangle with vertices in reverse order.
#
  print ( '' )
  print ( '  Repeat the test, but reverse the triangle vertex ordering.' )
 
  t2 = np.zeros ( [ 2, 3 ] )
  for j in range ( 0, 3 ):
    for i in range ( 0, 2 ):
      t2[i,j] = t[i,2-j]

  print ( '' )
  print ( '  Triangle vertices (reversed):' )
  print ( t2 )

  print ( '' )
  print ( '     X       Y     Inside' )
  print ( '' )

  for j in range ( 0, test_num ):

    p[0] = p_test[0,j]
    p[1] = p_test[1,j]

    inside = triangle_contains_point ( t2, p )

    print ( '  %10g  %10g  %s' % ( p[0], p[1], inside ) )

  return

def triangle_diameter ( t ):

#*****************************************************************************80
#
## triangle_diameter() computes the diameter of a triangle in 2D.
#
#  Discussion:
#
#    The diameter of a triangle is the diameter of the smallest circle
#    that can be drawn around the triangle.  At least two of the vertices
#    of the triangle will intersect the circle, but not necessarily
#    all three!
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
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real DIAMETER, the diameter of the triangle.
#
  import numpy as np
#
#  Compute the squared length of each side.
#
  asq = ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2
  bsq = ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2
  csq = ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2
#
#  Take care of a zero side.
#
  if ( asq == 0.0 ):
    diameter = np.sqrt ( bsq )
    return diameter
  elif ( bsq == 0.0 ):
    diameter = np.sqrt ( csq )
    return diameter
  elif ( csq == 0.0 ):
    diameter = np.sqrt ( asq )
    return diameter
#
#  Make ASQ the largest.
#
  if ( asq < bsq ):
    temp = asq
    asq = bsq
    bsq = temp

  if ( asq < csq ):
    temp = asq
    asq = csq
    csq = temp
#
#  If ASQ is very large...
#
  if ( bsq + csq < asq ):

    diameter = np.sqrt ( asq )

  else:

    a = np.sqrt ( asq )
    b = np.sqrt ( bsq )
    c = np.sqrt ( csq )

    diameter = 2.0 * a * b * c / np.sqrt ( ( a + b + c ) * ( - a + b + c ) \
      * ( a - b + c ) * ( a + b - c ) )

  return diameter

def triangle_diameter_test ( ):

#*****************************************************************************80
#
## triangle_diameter_test() tests triangle_diameter().
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
  import platform

  print ( '' )
  print ( 'triangle_diameter_test' )
  print ( '  triangle_diameter computes the diameter of' )
  print ( '  the SMALLEST circle around a triangle.' )

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  diameter = triangle_diameter ( t )

  print ( '' )
  print ( '  Diameter = %g' % ( diameter ) )

  t = np.array ( [ \
    [ 4.0, 5.0, 6.0 ], \
    [ 2.0, 4.0, 6.0 ] ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  diameter = triangle_diameter ( t )

  print ( '' )
  print ( '  Diameter = %g' % ( diameter ) )

  t = np.array ( [ \
    [ 4.0, 1.0, 4.0 ], \
    [ 2.0, 5.0, 2.0 ] ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  diameter = triangle_diameter ( t )

  print ( '' )
  print ( '  Diameter = %g' % ( diameter ) )

  return

def triangle_edge_length ( t ):

#*****************************************************************************80
#
## triangle_edge_length() returns edge lengths of a triangle in 2D.
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
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real EDGE_length(3), the length of the edges.
#
  import numpy as np

  edge_length = np.zeros ( 3 )

  for j1 in range ( 0, 3 ):
    j2 = i4_wrap ( j1 + 1, 0, 2 )

    edge_length[j1] = np.sqrt ( ( t[0,j2] - t[0,j1] ) ** 2 \
                              + ( t[1,j2] - t[1,j1] ) ** 2 )

  return edge_length

def triangle_edge_length_test ( ):

#*****************************************************************************80
#
## triangle_edge_length_test() tests triangle_edge_length().
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
  import platform

  print ( '' )
  print ( 'triangle_edge_length_test' )
  print ( '  triangle_edge_length computes the edge lengths' )
  print ( '  of a triangle.' )

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  edge_length = triangle_edge_length ( t )

  print ( '' )
  print ( '  edge lengths:' )
  print ( edge_length )

  t = np.array ( [ \
    [ 4.0, 5.0, 6.0 ], \
    [ 2.0, 4.0, 6.0 ] ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  edge_length = triangle_edge_length ( t )

  print ( '' )
  print ( '  edge lengths:' )
  print ( edge_length )

  t = np.array ( [ \
    [ 4.0, 1.0, 4.0 ], \
    [ 2.0, 5.0, 2.0 ] ] )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  edge_length = triangle_edge_length ( t )

  print ( '' )
  print ( '  edge lengths:' )
  print ( edge_length )

  return

def triangle_incircle ( t ):

#*****************************************************************************80
#
## triangle_incircle() computes the inscribed circle of a triangle in 2D.
#
#  Discussion:
#
#    The inscribed circle of a triangle is the largest circle that can
#    be drawn inside the triangle.  It is tangent to all three sides,
#    and the lines from its center to the vertices bisect the angles
#    made by each vertex.
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
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real R, CENTER(2), the radius and center of the
#    inscribed circle.
#
  import numpy as np

  center = np.zeros ( 2 )
#
#  Compute the length of each side.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  perimeter = a + b + c

  if ( perimeter == 0.0 ):
    center[0] = t[0,0]
    center[1] = t[1,0]
    r = 0.0
    return r, center

  center[0] = (  \
      b * t[0,0] \
    + c * t[0,1] \
    + a * t[0,2] ) / perimeter

  center[1] = (  \
      b * t[1,0] \
    + c * t[1,1] \
    + a * t[1,2] ) / perimeter

  r = 0.5 * np.sqrt ( \
      ( - a + b + c ) \
    * ( + a - b + c ) \
    * ( + a + b - c ) / perimeter )

  return r, center

def triangle_incircle_test ( ):

#*****************************************************************************80
#
## triangle_incircle_test() tests triangle_incircle().
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
  import platform

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_incircle_test' )
  print ( '  triangle_incircle computes the incircle of a triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  r, center = triangle_incircle ( t )

  print ( '' )
  print ( '  incenter:' )
  print ( center )

  print ( '' )
  print ( '  Incircle radius is %g' % ( r ) )

  return

def triangle_orientation ( t ):

#*****************************************************************************80
#
## triangle_orientation() determines the orientation of a triangle in 2D.
#
#  Discussion:
#
#    Three distinct non-colinear points in the plane define a circle.
#    If the points are visited in the order P1, P2, and then
#    P3, this motion defines a clockwise or counterclockwise
#    rotation along the circle.
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
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    integer VALUE, reports if the three points lie
#    clockwise on the circle that passes through them.  The possible
#    return values are:
#    0, the points are distinct, noncolinear, and lie counterclockwise
#    on their circle.
#    1, the points are distinct, noncolinear, and lie clockwise
#    on their circle.
#    2, the points are distinct and colinear.
#    3, at least two of the points are identical.
#
  for j in range ( 0, 3 ):
    jp1 = i4_wrap ( j + 1, 0, 2 )
    if ( t[0,j] == t[0,jp1] and t[1,j] == t[1,jp1] ): 
      value = 3
      return value

  det = ( t[0,0] - t[0,2] ) * ( t[1,1] - t[1,2] ) \
      - ( t[0,1] - t[0,2] ) * ( t[1,0] - t[1,2] )

  if ( det == 0.0 ):
    value = 2
  elif ( det < 0.0 ):
    value = 1
  elif ( 0.0 < det ):
    value = 0

  return value

def triangle_orientation_test ( ):

#*****************************************************************************80
#
## triangle_orientation_test() tests triangle_orientation().
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
  import platform

  print ( '' )
  print ( 'triangle_orientation_test' )
  print ( '  triangle_orientation_determines orientation' )
  print ( '  of a triangle.' )

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  i = triangle_orientation ( t )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  if ( i == 0 ):
    print ( '  The points are counterclockwise.' )
  elif ( i == 1 ):
    print ( '  The points are clockwise.' )
  elif ( i == 2 ):
    print ( '  The points are colinear.' )
  elif ( i == 3 ):
    print ( '  The points are not distinct.' )
  else:
    print ( '  The return value makes no sense.' )

  t = np.array ( [ \
    [ 1.0, 4.0,  1.0 ], \
    [ 5.0, 2.0, -1.0 ] ] )

  i = triangle_orientation ( t )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  if ( i == 0 ):
    print ( '  The points are counterclockwise.' )
  elif ( i == 1 ):
    print ( '  The points are clockwise.' )
  elif ( i == 2 ):
    print ( '  The points are colinear.' )
  elif ( i == 3 ):
    print ( '  The points are not distinct.' )
  else:
    print ( '  The return value makes no sense.' )
#
#  Colinear points
#
  t = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 5.0, 7.0, 9.0 ] ] )

  i = triangle_orientation ( t )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  if ( i == 0 ):
    print ( '  The points are counterclockwise.' )
  elif ( i == 1 ):
    print ( '  The points are clockwise.' )
  elif ( i == 2 ):
    print ( '  The points are colinear.' )
  elif ( i == 3 ):
    print ( '  The points are not distinct.' )
  else:
    print ( '  The return value makes no sense.' )
#
#  Nondistinct points.
#
  t = np.array ( [ \
    [ 1.0, 4.0, 1.0 ], \
    [ 5.0, 2.0, 5.0 ] ] )

  i = triangle_orientation ( t )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  if ( i == 0 ):
    print ( '  The points are counterclockwise.' )
  elif ( i == 1 ):
    print ( '  The points are clockwise.' )
  elif ( i == 2 ):
    print ( '  The points are colinear.' )
  elif ( i == 3 ):
    print ( '  The points are not distinct.' )
  else:
    print ( '  The return value makes no sense.' )

  return

def triangle_orthocenter ( t ):

#*****************************************************************************80
#
## triangle_orthocenter() computes the orthocenter of a triangle in 2D.
#
#  Discussion:
#
#    The orthocenter is defined as the intersection of the three altitudes
#    of a triangle.
#
#    An altitude of a triangle is the line through a vertex of the triangle
#    and perpendicular to the opposite side.
#
#    In geometry, the orthocenter of a triangle is often symbolized by "H".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
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
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real CENTER(2,1), the orthocenter of the triangle.
#
#    logical FLAG, is TRUE if the value could not be computed.
#
  import numpy as np

  p1 = np.zeros ( 2 )
  p1[0] = t[0,0]
  p1[1] = t[1,0]
  p2 = np.zeros ( 2 )
  p2[0] = t[0,1]
  p2[1] = t[1,1]
  p3 = np.zeros ( 2 )
  p3[0] = t[0,2]
  p3[1] = t[1,2]
  center = np.zeros ( 2 )
#
#  Determine a point P23 common to the line (P2,P3) and
#  its perpendicular through P1.
#
  p23, flag = line_exp_perp_2d ( p2, p3, p1 )

  if ( flag ):
    center[0] = float ( 'inf' )
    center[1] = float ( 'inf' )
    return center, flag
#
#  Determine a point P31 common to the line (P3,P1) and
#  its perpendicular through P2.
#
  p31, flag = line_exp_perp_2d ( p3, p1, p2 )

  if ( flag ):
    center[0] = float ( 'inf' )
    center[1] = float ( 'inf' )
    return center, flag
#
#  Determine CENTER, the intersection of the lines (P1,P23) and (P2,P31).
#
  ival, center = lines_exp_int_2d ( p1, p23, p2, p31 )

  if ( ival != 1 ):
    flag = 1
    center[0] = float ( 'inf' )
    center[1] = float ( 'inf' )
    return center, flag

  return center, flag

def triangle_orthocenter_test ( ):

#*****************************************************************************80
#
## triangle_orthocenter_test() tests triangle_orthocenter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_orthocenter_test' )
  print ( '  triangle_orthocenter computes the orthocenter of a triangle.' )

  for i in range ( 0, 4 ):

    if ( i == 0 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 1.0 ] ] )
    elif ( i == 1 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 0.86602539 ] ] )
    elif ( i == 2 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    print ( '' )
    print ( '  Triangle vertices:' )
    print ( t )

    center, flag = triangle_orthocenter ( t )

    print ( '' )
    print ( '  orthocenter:' )
    print ( center )

  return

def triangle_point_dist ( t, p ):

#*****************************************************************************80
#
## triangle_point_dist(): distance ( triangle, point ) in 2D.
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
#    real T(2,3), the triangle vertices.
#
#    real P(2), the point to be checked.
#
#  Output:
#
#    real DIST, the distance from the point to the
#    triangle.
#
  import numpy as np

  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )
#
#  Find the distance to each of the line segments.
#
  dist = float ( 'inf' )

  for j in range ( 0, 3 ):

    jp1 = i4_wrap ( j + 1, 0, 2 )

    p1[0] = t[0,j]
    p1[1] = t[1,j]

    p2[0] = t[0,jp1]
    p2[1] = t[1,jp1]

    dist2 = segment_point_dist_2d ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2

  return dist

def triangle_point_dist_test ( ):

#*****************************************************************************80
#
## triangle_point_dist_test() tests triangle_point_dist().
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
  import platform

  ntest = 7

  ptest = np.array ( [ \
    [ 0.25, 0.75, 1.00, 11.00, 0.00,  0.50,  0.60 ], \
    [ 0.25, 0.25, 1.00,  0.50, 1.00, -10.00, 0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  p = np.zeros ( 2 )

  print ( '' )
  print ( 'triangle_point_dist_test' )
  print ( '  triangle_point_dist computes the distance' )
  print ( '  between a point and a triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '       P       DIST' )
  print ( '' )

  for j in range ( 0, ntest ):

    p[0] = ptest[0,j]
    p[1] = ptest[1,j]

    dist = triangle_point_dist ( t, p )

    print ( '  %10g  %10g  %10g' % ( p[0], p[1], dist ) )

  return

def triangle_point_near ( t, p ):

#*****************************************************************************80
#
## triangle_point_near() computes the nearest point on a triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#    real P(2), the point whose nearest triangle point
#    is to be determined.
#
#  Output:
#
#    real PN(2), the nearest point to P.
#
#    real DIST, the distance from the point to the
#    triangle.
#
  import numpy as np

  pn = np.zeros ( 2 )
  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )
#
#  Find the distance to each of the line segments that make up the edges
#  of the triangle.
#
  dist = float ( 'inf' )

  for j in range ( 0, 3 ):

    jp1 = i4_wrap ( j + 1, 0, 2 )

    p1[0] = t[0,j]
    p1[1] = t[1,j]


    p2[0] = t[0,jp1]
    p2[1] = t[1,jp1]

    pn2, dist2, tval = segment_point_near_2d ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2;
      pn[0] = pn2[0]
      pn[1] = pn2[1]

  return pn, dist

def triangle_point_near_test ( ):

#*****************************************************************************80
#
## triangle_point_near_test() tests triangle_point_near().
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
  import numpy as np
  import platform

  ntest = 7

  ptest = np.array ( [ \
    [ 0.25, 0.75, 1.00, 11.00, 0.00,   0.50, 0.60 ], \
    [ 0.25, 0.25, 1.00,  0.50, 1.00, -10.00, 0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_point_near_test' )
  print ( '  triangle_point_near computes the nearest' )
  print ( '  triangle point to a point.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '           P                PN' )
  print ( '' )

  p = np.zeros ( 2 )

  for j in range ( 0, ntest ):

    p[0] = ptest[0,j]
    p[1] = ptest[1,j]

    [ pn, dist ] = triangle_point_near ( t, p );

    print ( '  %10g  %10g    %10g  %10g' % ( p[0], p[1], pn[0], pn[1] ) )

  return

def triangle_quality ( t ):

#*****************************************************************************80
#
## triangle_quality(): "quality" of a triangle in 2D.
#
#  Discussion:
#
#    The quality of a triangle is 2 times the ratio of the radius of the inscribed
#    circle divided by that of the circumscribed circle.  An equilateral
#    triangle achieves the maximum possible quality of 1.
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
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real QUALITY, the quality of the triangle.
#
  import numpy as np
#
#  Compute the length of each side.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  if ( a * b * c == 0.0 ):
    value = 0.0
  else:
    value = ( - a + b + c ) * ( a - b + c ) * ( a + b - c ) / ( a * b * c )

  return value

def triangle_quality_test ( ):

#*****************************************************************************80
#
## triangle_quality_test() tests triangle_quality().
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
  import platform

  ntest = 4

  print ( '' )
  print ( 'triangle_quality_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  triangle_quality computes the quality of a triangle.' )

  for i in range ( 0, ntest ):
 
    if ( i == 0 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 1.0 ] ] )
    elif ( i == 1 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 0.86602539 ] ] )
    elif ( i == 2 ):
      t = np.array ( [ \
        [ 0.0, 1.0,  0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    print ( '' )
    print ( '  Triangle vertices:' )
    print ( t )

    quality = triangle_quality ( t )

    print ( '' )
    print ( '  Quality = %g' % ( quality ) )

  return

def triangle_reference_sample ( n, rng ):

#*****************************************************************************80
#
## triangle_reference_sample() returns random points in the reference triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to generate.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P(2,N), random points in the triangle.
#
  import numpy as np

  alpha = rng.random ( size = n )
#
#  Interpret R as a percentage of the triangle's area.
#
#  Imagine a line L, parallel to side 1, so that the area between
#  vertex 1 and line L is R percent of the full triangle's area.
#
#  The line L will intersect sides 2 and 3 at a fraction
#  ALPHA = SQRT ( R ) of the distance from vertex 1 to vertices 2 and 3.
#
  for i in range ( 0, n ):
    alpha[i] = np.sqrt ( alpha[i] )
#
#  Now choose, uniformly at random, a point on the line L.
#
  beta = rng.random ( size = n )

  p = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    p[0,j] = ( 1.0 - beta[j] ) * alpha[j]
    p[1,j] =         beta[j]   * alpha[j]

  return p

def triangle_reference_sample_test ( rng ):

#*****************************************************************************80
#
## triangle_reference_sample_test() tests triangle_reference_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 1.0,  0.0 ], \
    [ 0.0, 0.0,  1.0 ] ] )

  print ( '' )
  print ( 'triangle_reference_sample_test():' )
  print ( '  triangle_reference_sample() samples the reference triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '  Sample points (X,Y) and (XSI1,XSI2,XSI3) coordinates:' )
  print ( '' )

  n = 1

  for i in range ( 0, 10 ):

    p = triangle_reference_sample ( n, rng )

    xsi = triangle_xy_to_xsi ( t, p[:,0] )

    print ( '  %10g  %10g    %10g  %10g  %10g' \
      % ( p[0,0], p[1,0], xsi[0], xsi[1], xsi[2] ) )

  return

def triangle_sample ( t, n, rng ):

#*****************************************************************************80
#
## triangle_sample() returns random points in a triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#    integer N, the number of points to generate.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P(2,N), random points in the triangle.
#
  import numpy as np

  alpha = rng.random ( size = n )
#
#  Interpret R as a percentage of the triangle's area.
#
#  Imagine a line L, parallel to side 1, so that the area between
#  vertex 1 and line L is R percent of the full triangle's area.
#
#  The line L will intersect sides 2 and 3 at a fraction
#  ALPHA = SQRT ( R ) of the distance from vertex 1 to vertices 2 and 3.
#
  for i in range ( 0, n ):
    alpha[i] = np.sqrt ( alpha[i] )
#
#  Determine the coordinates of the points on sides 2 and 3 intersected
#  by line L.
#
  p12 = np.zeros ( [ 2, n ] )
  p13 = np.zeros ( [ 2, n ] )

  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      p12[i,j] = ( 1.0 - alpha[j] ) * t[i,0] \
                       + alpha[j]   * t[i,1]

      p13[i,j] = ( 1.0 - alpha[j] ) * t[i,0] \
                       + alpha[j]   * t[i,2]
#
#  Now choose, uniformly at random, a point on the line L.
#
  alpha = rng.random ( size = n )

  p = np.zeros ( [ 2, n ] )

  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      p[i,j] = ( 1.0 - alpha[j] ) * p12[i,j] \
                     + alpha[j]   * p13[i,j]

  return p

def triangle_sample_test ( rng ):

#*****************************************************************************80
#
## triangle_sample_test() tests triangle_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( 'triangle_sample_test():' )
  print ( '  triangle_sample() samples a triangle.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '  Sample points (X,Y) and (XSI1,XSI2,XSI3) coordinates:' )
  print ( '' )

  n = 1

  for i in range ( 0, 10 ):

    p = triangle_sample ( t, n, rng )

    xsi = triangle_xy_to_xsi ( t, p[:,0] )
 
    print ( '  %10g  %10g    %10g  %10g  %10g' % ( p[0,0], p[1,0], xsi[0], xsi[1], xsi[2] ) )

  return

def triangle_sample_reflect ( t, n, rng ):

#*****************************************************************************80
#
## triangle_sample_reflect() returns random points in a triangle.
#
#  Discussion:
#
#    The "reflection" method is used, which is particularly easy to
#    understand and implement.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t(3,2): the triangle vertices.
#
#    integer n: the number of points to generate.
#
#  Output:
#
#    real p(n,2): random points in the triangle.
#
  import numpy as np

  u = rng.random ( size = n )
  v = rng.random ( size = n )
#
#  If 1.0 < u + v, these points are in the parallelogram, but not the triangle.
#  Reflect them.
#
  i = ( 1.0 < u + v )
  u[i] = 1.0 - u[i]
  v[i] = 1.0 - v[i]

  p = np.zeros ( [ n, 2 ] )
  p[:,0] = ( 1.0 - u - v ) * t[0,0] + u * t[1,0] + v * t[2,0]
  p[:,1] = ( 1.0 - u - v ) * t[0,1] + u * t[1,1] + v * t[2,1]

  return p

def triangle_sample_reflect_test ( rng ):

#*****************************************************************************80
#
## triangle_sample_reflect_test() tests triangle_reflect_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 January 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
#
#  Triangle dimension is [3,2]!
#
  t = np.array ( [ \
    [  4.0, 2.0 ], \
    [  1.0, 5.0 ], \
    [ -2.0, 2.0 ] ] )

  print ( '' )
  print ( 'triangle_sample_reflect_test():' )
  print ( '  triangle_sample_reflect() samples a triangle using reflection.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '  Sample points (X,Y) and (XSI1,XSI2,XSI3) coordinates:' )
  print ( '' )

  n = 1

  for i in range ( 0, 10 ):

    p = triangle_sample_reflect ( t, n, rng )
 
    xsi = triangle_xy_to_xsi_new ( t, p[0,:] )

    print ( '  %10g  %10g    %10g  %10g  %10g' \
      % ( p[0,0], p[0,1], xsi[0], xsi[1], xsi[2] ) )

  return

def triangle_xsi_to_xy ( t, xsi ):

#*****************************************************************************80
#
## triangle_xsi_to_xy() converts from barycentric to XY coordinates in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#    real XSI(3,1), the barycentric coordinates of a point.
#    XSI(1) + XSI(2) + XSI(3) should equal 1, but this is not checked.
#
#  Output:
#
#    real P(2,1), the XY coordinates of the point.
#
  import numpy as np

  p = np.zeros ( 2 )

  p[0] = t[0,0] * xsi[0] + t[0,1] * xsi[1] + t[0,2] * xsi[2]
  p[1] = t[1,0] * xsi[0] + t[1,1] * xsi[1] + t[1,2] * xsi[2]

  return p

def triangle_xsi_to_xy_test ( rng ):

#*****************************************************************************80
#
## triangle_xsi_to_xy_test() tests triangle_xsi_to_xy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
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

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( 'triangle_xsi_to_xy_test():' )
  print ( '  triangle_xsi_to_xy() converts XSI to XY coordinates.' )
  print ( '' )
  print ( '  We verify that (X,Y) -> (XSI1,XSI2,XSI3) -> (X,Y)' )
  print ( '  works properly.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '  Sample points:' )
  print ( '' )

  n = 1
  p = np.zeros ( [ 2, n ] )

  for j in range ( 0, 10 ):

    if ( j == 0 ):
      p[0,0] = ( t[0,0] + t[0,1] + t[0,2] ) / 3.0
      p[1,0] = ( t[1,0] + t[1,1] + t[1,2] ) / 3.0
    elif ( j == 1 ):
      p[0,0] = 3.0
      p[1,0] = 0.0
    else:
      p = triangle_sample ( t, n, rng )

    xsi = triangle_xy_to_xsi ( t, p[:,0] )

    p2 = triangle_xsi_to_xy ( t, xsi )

    print ( '' )
    print ( '  %8g  %8g    %8g  %8g  %8g' % ( p[0,0], p[1,0], xsi[0], xsi[1], xsi[2] ) )
    print ( '  %8g  %8g' % ( p2[0], p2[1] ) )

  return

def triangle_xy_to_xsi ( t, p ):

#*****************************************************************************80
#
## triangle_xy_to_xsi() converts from XY to barycentric in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#    real P(2), the XY coordinates of a point.
#
#  Output:
#
#    real XSI(3), the barycentric coordinates of the point.
#    XSI1 + XSI2 + XSI3 should equal 1.
#
  import numpy as np

  xsi = np.zeros ( 3 )

  det = ( t[0,0] - t[0,2] ) * ( t[1,1] - t[1,2] ) \
      - ( t[0,1] - t[0,2] ) * ( t[1,0] - t[1,2] )

  xsi[0] = (   ( t[1,1] - t[1,2] ) * ( p[0] - t[0,2] ) \
             - ( t[0,1] - t[0,2] ) * ( p[1] - t[1,2] ) ) / det

  xsi[1] = ( - ( t[1,0] - t[1,2] ) * ( p[0] - t[0,2] ) \
             + ( t[0,0] - t[0,2] ) * ( p[1] - t[1,2] ) ) / det

  xsi[2] = 1.0 - xsi[0] - xsi[1]

  return xsi

def triangle_xy_to_xsi_new ( t, p ):

#*****************************************************************************80
#
## triangle_xy_to_xsi_new() converts from XY to barycentric in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,2), the triangle vertices.
#
#    real P(2), the XY coordinates of a point.
#
#  Output:
#
#    real XSI(3), the barycentric coordinates of the point.
#    XSI1 + XSI2 + XSI3 should equal 1.
#
  import numpy as np

  xsi = np.zeros ( 3 )

  det = ( t[0,0] - t[2,0] ) * ( t[1,1] - t[2,1] ) \
      - ( t[1,0] - t[2,0] ) * ( t[0,1] - t[2,1] )

  xsi[0] = (   ( t[1,1] - t[2,1] ) * ( p[0] - t[2,0] ) \
             - ( t[1,0] - t[2,0] ) * ( p[1] - t[2,1] ) ) / det

  xsi[1] = ( - ( t[0,1] - t[2,1] ) * ( p[0] - t[2,0] ) \
             + ( t[0,0] - t[2,0] ) * ( p[1] - t[2,1] ) ) / det

  xsi[2] = 1.0 - xsi[0] - xsi[1]

  return xsi

def triangle_xy_to_xsi_test ( rng ):

#*****************************************************************************80
#
## triangle_xy_to_xsi_test() tests triangle_xy_to_xsi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
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

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( 'triangle_xy_to_xsi_test' )
  print ( '  triangle_xy_to_xsi converts XY to XSI coordinates.' )
  print ( '' )
  print ( '  We verify that (X,Y) -> (XSI1,XSI2,XSI3) -> (X,Y)' )
  print ( '  works properly.' )

  print ( '' )
  print ( '  Triangle vertices:' )
  print ( t )

  print ( '' )
  print ( '  Sample points:' )
  print ( '' )

  n = 1
  p = np.zeros ( [ 2, n ] )

  for j in range ( 0, 10 ):

    if ( j == 0 ):
      p[0,0] = ( t[0,0] + t[0,1] + t[0,2] ) / 3.0
      p[1,0] = ( t[1,0] + t[1,1] + t[1,2] ) / 3.0
    elif ( j == 1 ):
      p[0,0] = 3.0
      p[1,0] = 0.0
    else:
      p = triangle_sample ( t, n, rng )

    xsi = triangle_xy_to_xsi ( t, p[:,0] )

    p2 = triangle_xsi_to_xy ( t, xsi )
 
    print ( '' )
    print ( '  %8g  %8g    %8g  %8g  %8g' % ( p[0,0], p[1,0], xsi[0], xsi[1], xsi[2] ) )
    print ( '  %8g  %8g' % ( p2[0], p2[1] ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_test ( )
  timestamp ( )

