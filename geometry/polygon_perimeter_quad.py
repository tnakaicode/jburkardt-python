#! /usr/bin/env python
#
def polygon_perimeter_quad ( n, v, hmax, f ):

#*****************************************************************************80
#
## POLYGON_PERIMETER computes the perimeter of a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
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
#    Input, real HMAX, the maximum length of a quadrature interval.
#
#    Input, def F ( X, Y ), a function whose integral over the perimeter 
#    is desired.
#
#    Output, real VALUE, the estimated integral.
#
  import numpy as np
  from i4_ceiling import i4_ceiling
  from i4_wrap import i4_wrap

  value = 0.0

  for i in range ( 0, n ):

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    l = np.sqrt ( ( v[0,ip1] - v[0,i] ) ** 2 + ( v[1,ip1] - v[1,i] ) ** 2 )
    m = i4_ceiling ( l / hmax )
    dxy = l / float ( m )

    for j in range ( 1, 2 * m, 2 ):
      x = ( ( 2 * m - j ) * v[0,i] \
          + (         j ) * v[0,ip1] ) \
          / ( 2 * m     )
      y = ( ( 2 * m - j ) * v[1,i] \
          + (         j ) * v[1,ip1] ) \
          / ( 2 * m     )
      fxy = f ( x, y )
      value = value + fxy * dxy

  return value

def polygon_perimeter_quad_test ( ):

#*****************************************************************************80
#
## POLYGON_PERIMETER_QUAD_TEST tests POLYGON_PERIMETER_QUAD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
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
  print ( 'POLYGON_PERIMETER_QUAD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_PERIMETER_QUAD estimates the integral of' )
  print ( '  a function over the perimeter of a polygon using' )
  print ( '  the composite midpoint rule over each side.' )

  r8mat_transpose_print ( 2, n1, v1, '  Vertices of polygon V1:' )

  hmax = 0.5
  value = polygon_perimeter_quad ( n1, v1, hmax, f1 )
  print ( '' )
  print ( '  Using HMAX = %g, estimated integral of 1 over perimeter = %g' % ( hmax, value ) )

  print ( '' )
  hmax = 2.0
  for i in range ( 0, 3 ):
    hmax = hmax / 2.0
    value = polygon_perimeter_quad ( n1, v1, hmax, fx2 )
    print ( '  Using HMAX = %g, estimated integral of x^2 over perimeter = %g' % ( hmax, value ) )

  r8mat_transpose_print ( 2, n2, v2, '  Vertices of polygon V2:' )

  hmax = 0.5
  value = polygon_perimeter_quad ( n2, v2, hmax, f1 )
  print ( '' )
  print ( '  Using HMAX = %g, estimated integral of 1 over perimeter = %g' % ( hmax, value ) )

  print ( '' )
  hmax = 2.0
  for i in range ( 0, 3 ):
    hmax = hmax / 2.0
    value = polygon_perimeter_quad ( n2, v2, hmax, fx2 )
    print ( '  Using HMAX = %g, estimated integral of x^2 over perimeter = %g' % ( hmax, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_PERIMETER_TEST' )
  print ( '  Normal end of execution.' )
  return

def f1 ( x, y ):

#*****************************************************************************80
#
## F1 evaluates f(x,y) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  value = 1.0

  return value

def fx2 ( x, y ):

#*****************************************************************************80
#
## FX2 evaluates f(x,y) = x^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  value = x ** 2

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_perimeter_quad_test ( )
  timestamp ( )
