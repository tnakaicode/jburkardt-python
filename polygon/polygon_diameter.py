#! /usr/bin/env python3
#
def polygon_diameter ( n, v ):

#*****************************************************************************80
#
## POLYGON_DIAMETER computes the diameter of a polygon.
#
#  Discussion:
#
#    The diameter of a polygon is the maximum distance between any
#    two points on the polygon.  It is guaranteed that this maximum
#    distance occurs between two vertices of the polygon.  It is
#    sufficient to check the distance between all pairs of vertices.
#    This is an N^2 algorithm.  There is an algorithm by Shamos which
#    can compute this quantity in order N time instead.
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
#    Output, real DIAMETER, the diameter of the polygon.
#
  import numpy as np

  diameter = 0.0

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      diameter = max ( diameter, \
        np.sqrt ( ( v[0,i] - v[0,j] ) ** 2 + ( v[1,i] - v[1,j] ) ** 2 ) )

  return diameter

def polygon_diameter_test ( ):

#*****************************************************************************80
#
## POLYGON_DIAMETER_TEST tests POLYGON_DIAMETER;
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
  diameter_exact = 2.0
  v = np.array ( [ \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'POLYGON_DIAMETER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_DIAMETER computes the diameter of a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  diameter = polygon_diameter ( n, v )

  print ( '' )
  print ( '  Diameter ( computed ) %g' % ( diameter ) )
  print ( '  Diameter ( exact )    %g' % ( diameter_exact ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_DIAMETER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_diameter_test ( )
  timestamp ( )
