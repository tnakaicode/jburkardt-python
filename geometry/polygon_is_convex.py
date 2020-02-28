#! /usr/bin/env python
#
def polygon_is_convex ( n, v ):

#*****************************************************************************80
#
## POLYGON_IS_CONVEX determines whether a polygon is convex.
#
#  Discussion:
#
#    If the polygon has less than 3 distinct vertices, it is
#    classified as convex degenerate.
#
#    If the polygon "goes around" more than once, it is classified
#    as NOT convex.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Schorn and Frederick Fisher,
#    Testing the Convexity of a Polygon,
#    Graphics Gems IV, 
#    edited by Paul Heckbert,
#    AP Professsional, 1994.
#
#  Parameters
#
#    Input, integer N, the number of vertices.
#
#    Input, real V(2,N), the coordinates of the vertices of the polygon.  
#
#    Output, integer VALUE:
#    -1, the polygon is not convex
#     0, the polygon has less than 3 vertices it is "degenerately" convex
#     1, the polygon is convex and counterclockwise
#     2, the polygon is convex and clockwise.
#
  import numpy as np
  from i4_wrap import i4_wrap
  from r8_atan import r8_atan

  RAD_TO_DEG = 180.0 / np.pi

  CONVEX_CCW = 1
  CONVEX_CW = 2
  DEGENERATE_CONVEX = 0
  NOT_CONVEX = -1
  tol = 1.0

  exterior_total = 0.0
#
#  If there are not at least 3 distinct vertices, we are done.
#
  if ( n < 3 ):
    value = DEGENERATE_CONVEX
    return value

  sense = 0.0
#
#  Consider each polygonal vertex I.
#
  for i in range ( 0, n ):

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    ip2 = i4_wrap ( i + 2, 0, n - 1 )

    dot =   ( v[0,ip2] - v[0,ip1] ) * ( v[0,i] - v[0,ip1] ) \
          + ( v[1,ip2] - v[1,ip1] ) * ( v[1,i] - v[1,ip1] )

    cross =   ( v[0,ip2] - v[0,ip1] ) * ( v[1,i] - v[1,ip1] ) \
            - ( v[0,i]   - v[0,ip1] ) * ( v[1,ip2] - v[1,ip1] )

    angle = r8_atan ( cross, dot )
#
#  See if the turn defined by this vertex is our first indication of
#  the "sense" of the polygon, or if it disagrees with the previously
#  defined sense.
#
    if ( sense == 0.0 ):

      if ( angle < 0.0 ):
        sense = -1.0
      elif ( 0.0 < angle ):
        sense = +1.0

    elif ( sense == 1.0 ):

      if ( angle < 0.0 ):
        value = NOT_CONVEX
        return value

    elif ( sense == -1.0 ):

      if ( 0.0 < angle ):
        value = NOT_CONVEX
        return value
#
#  If the exterior total is greater than 360, then the polygon is
#  going around again.
#
    angle = r8_atan ( -cross, -dot )

    exterior_total = exterior_total + angle

    if ( 360.0 + tol < abs ( exterior_total ) * RAD_TO_DEG ):
      value = NOT_CONVEX
      return value

  if ( sense == 1.0 ):
    value = CONVEX_CCW
  elif ( sense == -1.0 ):
    value = CONVEX_CW

  return value

def polygon_is_convex_test ( ):

#*****************************************************************************80
#
## POLYGON_IS_CONVEX_TEST tests POLYGON_IS_CONVEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  n_max = 10
  test_num = 11

  print ( '' )
  print ( 'POLYGON_IS_CONVEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_IS_CONVEX determines if a polygon is convex.' )

  for test in range ( 0, test_num ):

    if ( test == 0 ):
      n = 1
      v = np.array ( [ \
        [ 0.0 ], \
        [ 0.0 ] ] )
      title = '  A point:'
    elif ( test == 1 ):
      n = 2
      v = np.array ( [ \
        [ 0.0, 1.0 ], \
        [ 0.0, 2.0 ] ] )
      title = '  A line:'
    elif ( test == 2 ):
      n = 3
      v = np.array ( [ \
        [ 0.0, 2.0, 1.0 ], \
        [ 0.0, 0.0, 0.0 ] ] )
      title = '  A triangle:'
    elif ( test == 3 ):
      n = 3
      v = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )
      title = '  A CCW triangle:'
    elif ( test == 4 ):
      n = 3
      v = np.array ( [ \
        [ 0.0, 0.0, 1.0 ], \
        [ 0.0, 2.0, 0.0 ] ] )
      title = '  A CW triangle:'
    elif ( test == 5 ):
      n = 4
      v = np.array ( [ \
        [ 1.0, 2.0, 3.0, 0.0 ], \
        [ 0.0, 0.0, 1.0, 1.0 ] ] )
      title = '  Polygon with large angle:'
    elif ( test == 6 ):
      n = 5
      v = np.array ( [ \
        [ 0.0, 0.5, 1.0, 1.0, 0.0 ], \
        [ 0.0, 0.5, 0.0, 1.0, 1.0 ] ] )
      title = '  Polygon with huge angle:'
    elif ( test == 7 ):
      n = 5
      v = np.zeros ( [ 2, n ] )
      for i in range ( 0, n ):
        angle = i * 4.0 * np.pi / float ( n )
        v[0,i] = np.cos ( angle )
        v[1,i] = np.sin ( angle )
      title = '  A five-pointed star:'
    elif ( test == 8 ):
      n = 6
      v = np.zeros ( [ 2, n ] )
      for i in range ( 0, n ):
        angle = i * 2.0 * np.pi / float ( n )
        v[0,i] = np.cos ( angle )
        v[1,i] = np.sin ( angle )
      title = '  A hexagon:'
    elif ( test == 9 ):
      n = 6
      v = np.array ( [ \
        [ 0.0, 2.0, 1.0, 0.0, 2.0, 1.0 ], \
        [ 0.0, 0.0, 1.0, 0.0, 0.0, 1.0 ] ] )
      title = '  A triangle twice:'
    elif ( test == 10 ):
      n = 8
      v = np.array ( [ \
        [ 1.0, 3.0, 3.0, 0.0, 0.0, 2.0, 2.0, 1.0 ], \
        [ 0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 1.0 ] ] )
      title = '  Square knot:'

    r8mat_transpose_print ( 2, n, v, title )

    result = polygon_is_convex ( n, v )

    if ( result == -1 ):
      print ( '  The polygon is not convex.' )
    elif ( result == 0 ):
      print ( '  The polygon is degenerate and convex.' )
    elif ( result == 1 ):
      print ( '  The polygon is convex and counterclockwise.' )
    elif ( result == 2 ):
      print ( '  The polygon is convex and clockwise.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_IS_CONVEX_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_is_convex_test ( )
  timestamp ( )


