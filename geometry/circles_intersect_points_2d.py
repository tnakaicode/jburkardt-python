#! /usr/bin/env python
#
def circles_intersect_points_2d ( r1, center1, r2, center2 ):

#*****************************************************************************80
#
## CIRCLES_INTERSECT_POINTS_2D: intersection points of two circles in 2D.
#
#  Discussion:
#
#    Two circles can intersect in 0, 1, 2 or infinitely many points.
#
#    The 0 and 2 intersection cases are numerically robust the 1 and
#    infinite intersection cases are numerically fragile.  The routine
#    uses a tolerance to try to detect the 1 and infinite cases.
#
#    An implicit circle in 2D satisfies the equation:
#
#      ( X - CENTER(1) )^2 + ( Y - CENTER(2) )^2 = R^2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R1, the radius of the first circle.
#
#    Input, real CENTER1(2), the center of the first circle.
#
#    Input, real R2, the radius of the second circle.
#
#    Input, real CENTER2(2), the center of the second circle.
#
#    Output, integer NUM_INT, the number of intersecting points found.
#    NUM_INT will be 0, 1, 2 or 3.  3 indicates that there are an infinite
#    number of intersection points.
#
#    Output, real P(2,2), if NUM_INT is 1 or 2,
#    the coordinates of the intersecting points.
#
  import numpy as np

  tol = np.finfo ( float ).eps

  p = np.zeros ( [ 2, 2 ] )
#
#  Take care of the case in which the circles have the same center.
#
  t1 = ( abs ( center1[0] - center2[0] ) \
       + abs ( center1[1] - center2[1] ) ) / 2.0

  t2 = ( abs ( center1[0] ) + abs ( center2[0] ) \
       + abs ( center1[1] ) + abs ( center2[1] ) + 1.0 ) / 5.0

  if ( t1 <= tol * t2 ):

    t1 = abs ( r1 - r2 )
    t2 = ( abs ( r1 ) + abs ( r2 ) + 1.0 ) / 3.0

    if ( t1 <= tol * t2 ):
      num_int = 3
    else:
      num_int = 0

    return num_int, p

  distsq = ( center1[0] - center2[0] ) ** 2 + ( center1[1] - center2[1] ) ** 2

  root = 2.0 * ( r1 * r1 + r2 * r2 ) * distsq - distsq * distsq \
    - ( r1 - r2 ) * ( r1 - r2 ) * ( r1 + r2 ) * ( r1 + r2 )

  if ( root < -tol ):
    num_int = 0
    return num_int, p

  sc1 = ( distsq - ( r2 * r2 - r1 * r1 ) ) / distsq

  if ( root < tol ):
    num_int = 1
    for i in range ( 0, 2 ):
      p[i,0] = center1[i] + 0.5 * sc1 * ( center2[i] - center1[i] )
    return num_int, p

  sc2 = np.sqrt ( root ) / distsq

  num_int = 2

  p[0,0] = center1[0] + 0.5 * sc1 * ( center2[0] - center1[0] ) \
                      - 0.5 * sc2 * ( center2[1] - center1[1] )
  p[1,0] = center1[1] + 0.5 * sc1 * ( center2[1] - center1[1] ) \
                      + 0.5 * sc2 * ( center2[0] - center1[0] )

  p[0,1] = center1[0] + 0.5 * sc1 * ( center2[0] - center1[0] ) \
                      + 0.5 * sc2 * ( center2[1] - center1[1] )
  p[1,1] = center1[1] + 0.5 * sc1 * ( center2[1] - center1[1] ) \
                      - 0.5 * sc2 * ( center2[0] - center1[0] )

  return num_int, p

def circles_intersect_points_2d_test ( ):

#*****************************************************************************80
#
## CIRCLES_INTERSECT_POINTS_2D_TEST tests CIRCLES_INTERSECT_POINTS_2D
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from circle_imp_print_2d import circle_imp_print_2d

  ntest = 5
  center1 = np.array ( [ 0.0, 0.0 ] )
  r1 = 5.0
  r2_test = np.array ( [ 0.5, 5.0, 3.0, 3.0, 5.0 ] )
  xc2_test = np.array ( [ 5.0, 7.0710678, 4.0, 6.0, 0.0 ] )
  yc2_test = np.array ( [ 5.0, 7.0710678, 0.0, 0.0, 0.0 ] )

  print ( '' )
  print ( 'CIRCLES_INTERSECT_POINTS_2D_TEST' )
  print ( '  CIRCLES_INTERSECT_POINTS_2D determines the intersections of' )
  print ( '  two circles in 2D.' )

  circle_imp_print_2d ( r1, center1, '  The first circle:' )

  for i in range ( 0, ntest ):

    r2 = r2_test[i]
    center2 = np.array ( [ xc2_test[i], yc2_test[i] ] )

    circle_imp_print_2d ( r2, center2, '  The second circle:' )

    num_int, x = circles_intersect_points_2d ( r1, center1, r2, center2 )

    if ( num_int == 0 ):

      print ( '' )
      print ( '  The circles do not intersect.' )

    elif ( num_int == 1 ):

      print ( '' )
      print ( '  The circles intersect at one point:' )
      print ( '' )
      print ( '    X       Y' )
      print ( '' )
      print ( '  %6f  %6f' % ( x[0,0], x[1,0] ) )

    elif ( num_int == 2 ):

      print ( '' )
      print ( '  The circles intersect at two points:' )
      print ( '' )
      print ( '    X       Y' )
      print ( '' )
      print ( '  %6f  %6f' % ( x[0,0], x[1,0] ) )
      print ( '  %6f  %6f' % ( x[0,1], x[1,1] ) )

    elif ( num_int == 3 ):

      print ( '' )
      print ( '  The circles coincide (infinite intersection).' )

  return

if ( __name__ == '__main__' ):
  circles_intersect_points_2d_test ( )

