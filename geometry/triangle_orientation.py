#! /usr/bin/env python
#
def triangle_orientation ( t ):

#*****************************************************************************80
#
## TRIANGLE_ORIENTATION determines the orientation of a triangle in 2D.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, integer VALUE, reports if the three points lie
#    clockwise on the circle that passes through them.  The possible
#    return values are:
#    0, the points are distinct, noncolinear, and lie counterclockwise
#    on their circle.
#    1, the points are distinct, noncolinear, and lie clockwise
#    on their circle.
#    2, the points are distinct and colinear.
#    3, at least two of the points are identical.
#
  from i4_wrap import i4_wrap

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
## TRIANGLE_ORIENTATION_TEST tests TRIANGLE_ORIENTATION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  from r8mat_transpose_print import r8mat_transpose_print

  print ( '' )
  print ( 'TRIANGLE_ORIENTATION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_ORIENTATION_determines orientation' )
  print ( '  of a triangle.' )

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  i = triangle_orientation ( t )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

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

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

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

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

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

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

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
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_ORIENTATION_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_orientation_test ( )
  timestamp ( )

