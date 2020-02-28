#! /usr/bin/env python3
#
def polygon_expand ( n, v, h ):

#*****************************************************************************80
#
## POLYGON_EXPAND expands a polygon in.
#
#  Discussion:
#
#    This routine simple moves each vertex of the polygon outwards
#    in such a way that the sides of the polygon advance by H.
#
#    This approach should always work if the polygon is convex, or
#    star-shaped.  But for general polygons, it is possible
#    that this procedure, for large enough H, will create a polygon
#    whose sides intersect.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of sides of the polygon.
#
#    Input, real V(2,N), the coordinates of the vertices.
#
#    Input, real H, the expansion amount.
#
#    Output, real W(2,N), the "expanded" coordinates.
#
  import numpy as np
  from angle_half import angle_half
  from angle_radian import angle_radian
  from i4_wrap import i4_wrap

  w = np.zeros ( [ 2, n ] )
#
#  Consider each angle, formed by the nodes P(I-1), P(I), P(I+1).
#
  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    ip1 = i4_wrap ( i + 1, 0, n - 1 )
#
#        P1
#        /
#       /   P4
#      /  .
#     / .
#    P2--------->P3
#
    p4 = angle_half ( v[0,im1], v[1,im1], v[0,i], v[1,i], v[0,ip1], v[1,ip1] )
#
#  Compute the value of the half angle.
#
    angle = angle_radian ( v[0,im1], v[1,im1], v[0,i], v[1,i], p4[0], p4[1] )
#
#  The stepsize along the ray must be adjusted so that the sides
#  move out by H.
#
    h2 = h / np.sin ( angle )

    w[0,i] = v[0,i] - h2 * ( p4[0] - v[0,i] )
    w[1,i] = v[1,i] - h2 * ( p4[1] - v[1,i] )

  return w

def polygon_expand_test ( ):

#*****************************************************************************80
#
## POLYGON_EXPAND_TEST tests POLYGON_EXPAND;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  n = 4

  v = np.array ( [ \
    [ 1.0, 5.0, 2.0, 1.0 ], \
    [ 1.0, 1.0, 4.0, 3.0 ] ] )

  print ( '' )
  print ( 'POLYGON_EXPAND_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_EXPAND "expands" a polygon by an amount H.' )

  h = 0.5

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  print ( '' )
  print ( '  The expansion amount H = %g' % ( h ) )

  w = polygon_expand ( n, v, h )

  r8mat_transpose_print ( 2, n, w, '  The expanded polygon:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_EXPAND_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_expand_test ( )
  timestamp ( )
