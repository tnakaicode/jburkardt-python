#! /usr/bin/env python
#
def polygon_contains_point ( x, y, px, py ):

#*****************************************************************************80
#
## POLYGON_CONTAINS_POINT finds if a point is inside a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, the coordinates of the point to be tested.
#
#    Input, real PX(N), PY(N), the coordinates of the vertices of the polygon.
#
#    Output, logical INSIDE, is TRUE if the point is inside the polygon.
#
  n = len ( px )
  inside = False

  px1 = px[0]
  py1 = py[0]
  xints = x - 1.0
  for i in range ( 0, n + 1 ):
    px2 = px[i%n]
    py2 = py[i%n]
    if ( min ( py1, py2 ) < y ):
      if ( y <= max ( py1, py2 ) ):
        if ( x <= max ( px1, px2 ) ):
          if ( py1 != py2 ):
            xints = ( y - py1 ) * ( px2 - px1 ) / ( py2 - py1 ) + px1
          if ( px1 == px2 or x <= xints ):
            inside = not inside
    px1 = px2
    py1 = py2

  return inside

def polygon_contains_point_test ( ):

#*****************************************************************************80
#
## POLYGON_CONTAINS_POINT_TEST tests POLYGON_CONTAINS_POINT.c
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec2_print import r8vec2_print

  n = 5
  test_num = 4

  x_test = np.array ( [ 1.0, 3.0, 0.0, 0.5 ] )

  y_test = np.array ( [ 1.0, 4.0, 2.0, -0.25 ] )

  px = np.array ( [ 0.0, 1.0, 2.0, 1.0, 0.0 ] )
 
  py = np.array ( [ 0.0, 0.0, 1.0, 2.0, 2.0 ] )

  print ( '' )
  print ( 'POLYGON_CONTAINS_POINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_CONTAINS_POINT determines if' )
  print ( '  a point is in a polygon.' )

  r8vec2_print ( n, px, py, '  The polygon vertices:' )

  print ( '' )
  print ( '        X         Y     Inside?' )
  print ( '' )

  for test in range ( 0, test_num ):
 
    x = x_test[test]
    y = y_test[test]
 
    inside = polygon_contains_point ( x, y, px, py )

    print ( '  %8.2f  %8.2f    %s' % ( x, y, inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_CONTAINS_POINT_TEST' )
  print ( '  Normal end of execution.' )
  return
 
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_contains_point_test ( )
  timestamp ( )

