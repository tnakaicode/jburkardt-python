#! /usr/bin/env python
#
def triangle_incircle ( t ):

#*****************************************************************************80
#
## TRIANGLE_INCIRCLE computes the inscribed circle of a triangle in 2D.
#
#  Discussion:
#
#    The inscribed circle of a triangle is the largest circle that can
#    be drawn inside the triangle.  It is tangent to all three sides,
#    and the lines from its center to the vertices bisect the angles
#    made by each vertex.
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
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real R, CENTER(2), the radius and center of the
#    inscribed circle.
#
  import numpy as np

  center = np.zeros ( 2 )
#
#  Compute the length of each side.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  perimeter = a + b + c

  if ( perimeter == 0.0 ):
    center[0] = t[0,0]
    center[1] = t[1,0]
    r = 0.0
    return r, center

  center[0] = (  \
      b * t[0,0] \
    + c * t[0,1] \
    + a * t[0,2] ) / perimeter

  center[1] = (  \
      b * t[1,0] \
    + c * t[1,1] \
    + a * t[1,2] ) / perimeter

  r = 0.5 * np.sqrt ( \
      ( - a + b + c ) \
    * ( + a - b + c ) \
    * ( + a + b - c ) / perimeter )

  return r, center

def triangle_incircle_test ( ):

#*****************************************************************************80
#
## TRIANGLE_INCIRCLE_TEST tests TRIANGLE_INCIRCLE.
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
  from r8vec_print import r8vec_print

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_INCIRCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_INCIRCLE computes the incircle of a triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  r, center = triangle_incircle ( t )

  r8vec_print ( 2, center, '  Incenter' )

  print ( '' )
  print ( '  Incircle radius is %g' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_INCIRCLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_incircle_test ( )
  timestamp ( )
 
