#! /usr/bin/env python3
#
def polygon_integral_x ( n, v ):

#*****************************************************************************80
#
## POLYGON_INTEGRAL_x integrates the function X over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = (1/6) * sum ( 1 <= I <= N )
#      ( X(I)^2 + X(I) * X(I-1) + X(I-1)^2 ) * ( Y(I) - Y(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#    Note that the integral of 1 over a polygon is the area of the polygon.
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
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Parameters:
#
#    Input, integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    Input, real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#    Output, real RESULT, the value of the integral.
#
  from i4_wrap import i4_wrap
  from sys import exit

  result = 0.0;

  if ( n < 3 ):
    print ( '' )
    print ( 'POLYGON_INTEGRAL_X - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    exit ( 'POLYGON_INTEGRAL_X - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result + ( v[0,i] ** 2 + v[0,i] * v[0,im1] + v[0,im1] ** 2 ) \
      * ( v[1,i] - v[1,im1] )

  result = result / 6.0

  return result

def polygon_integral_x_test ( ):

#*****************************************************************************80
#
## POLYGON_INTEGRAL_X_TEST tests POLYGON_INTEGRAL_X.
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

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'POLYGON_INTEGRAL_X_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_INTEGRAL_X integrates x over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_x ( n1, v1 )
  print ( '' )
  print ( '  x:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_x ( n2, v2 )
  print ( '' )
  print ( '  x:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_INTEGRAL_X_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_integral_x_test ( )
  timestamp ( )
