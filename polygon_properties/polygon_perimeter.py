#! /usr/bin/env python3
#
def polygon_perimeter ( n, v ):

#*****************************************************************************80
#
## POLYGON_PERIMETER computes the perimeter of a polygon.
#
#  Discussion:
#
#    The perimeter is simply the sum of the side lengths.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 October 2015
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
#    Output, real PERIMETER, the perimeter.
#
  import numpy as np

  perimeter = 0.0

  im1 = n - 1

  for i in range ( 0, n ):
    l = np.sqrt ( ( v[0,im1] - v[0,i] ) ** 2 + ( v[1,im1] - v[1,i] ) ** 2 )
    perimeter = perimeter + l
    im1 = i

  return perimeter

def polygon_perimeter_test ( ):

#*****************************************************************************80
#
## POLYGON_PERIMETER_TEST tests POLYGON_PERIMETER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  n1 = 4
  n2 = 3
 
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ]  )
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'POLYGON_PERIMETER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_PERIMETER computes the perimeter of a polygon.' )

  r8mat_transpose_print ( 2, n1, v1, '  Vertices of polygon V1:' )

  perimeter = polygon_perimeter ( n1, v1 )
  print ( '' )
  print ( '  Perimeter of V1 = %g' % ( perimeter ) )

  r8mat_transpose_print ( 2, n2, v2, '  Vertices of polygon V2:' )

  perimeter = polygon_perimeter ( n2, v2 )
  print ( '' )
  print ( '  Perimeter of V2 = %g' % ( perimeter ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_PERIMETER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_perimeter_test ( )
  timestamp ( )
