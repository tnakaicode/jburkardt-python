#! /usr/bin/env python
#
def circle_imp_point_dist_2d ( r, center, p ):

#*****************************************************************************80
#
## CIRCLE_IMP_POINT_DIST_2D: distance ( implicit circle, point ) in 2D.
#
#  Discussion:
#
#    The distance is zero if the point is on the circle.
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
#    Input, real R, the radius of the circle.
#
#    Input, real CENTER(2,1), the center of the circle.
#
#    Input, real P(2,1), the point to be checked.
#
#    Output, real DIST, the distance of the point to the circle.
#
  import numpy as np

  r2 = np.sqrt ( ( p[0] - center[0] ) ** 2 + ( p[1] - center[1] ) ** 2 )

  dist = abs ( r2 - r )

  return dist

def circle_imp_point_dist_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_IMP_POINT_DIST_2D_TEST tests CIRCLE_IMP_POINT_DIST_2D.
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
  from r8vec_uniform_ab import r8vec_uniform_ab

  ntest = 5
  center = np.array ( [ 0.0, 0.0 ] )
  r = 5.0
  seed = 123456789

  print ( '' )
  print ( 'CIRCLE_IMP_POINT_DIST_2D_TEST' )
  print ( '  CIRCLE_IMP_POINT_DIST_2D checks, by finding the' )
  print ( '  distance D from a point (X,Y) to a circle.' )

  print ( '' )
  print ( '  Circle has center (%f,%f) and radius %f' % ( center[0], center[1], r ) )

  print ( '' )
  print ( '       X       Y       D' )
  print ( '' )

  for i in range ( 0, 10 ):

    p, seed = r8vec_uniform_ab ( 2, -10.0, +10.0, seed )
    d = circle_imp_point_dist_2d ( r, center, p )
    print ( '  %8.4f  %8.4f  %8.4f' % ( p[0], p[1], d ) )

  return

if ( __name__ == '__main__' ):
  circle_imp_point_dist_2d_test ( )

