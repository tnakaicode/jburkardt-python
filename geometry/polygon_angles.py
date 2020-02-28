#! /usr/bin/env python
#
def polygon_angles ( n, v ):

#*****************************************************************************80
#
## POLYGON_ANGLES computes the interior angles of a polygon.
#
#  Discussion:
#
#    The vertices should be listed in counterclockwise order.
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
#    Input, integer N, the number of vertices of the polygon.
#
#    Input, real V(2,N), the vertices.
#
#    Output, real ANGLE(N), the angles of the polygon,
#    in radians.
#
  import numpy as np
  from angle_radian import angle_radian
  from i4_wrap import i4_wrap

  angle = np.zeros ( n )

  if ( n <= 2 ):
    return angle

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 );
    ip1 = i4_wrap ( i + 1, 0, n - 1 );

    angle[i] = angle_radian ( v[0,im1], v[1,im1], v[0,i], v[1,i], \
      v[0,ip1], v[1,ip1] )

  return angle

def polygon_angles_test ( ):

#*****************************************************************************80
#
## POLYGON_ANGLES_TEST tests POLYGON_ANGLES.
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

  n = 6
  v = np.array ( [ \
    [ 0.0, 1.0, 2.0, 3.0, 3.0, 1.0 ], \
    [ 0.0, 0.0, 1.0, 0.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'POLYGON_ANGLES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_ANGLES computes the angles of a polygon.' )

  print ( '' )
  print ( '  Number of polygonal vertices = %d' % ( n ) )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  angle = polygon_angles ( n, v )

  print ( '' )
  print ( '  Polygonal angles in degrees:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %14.6g' % ( i, angle[i] * 180.0 / np.pi ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_ANGLES_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_angles_test ( )
  timestamp ( )

