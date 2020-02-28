#! /usr/bin/env python
#
def triangle_circumcircle ( t ):

#*****************************************************************************80
#
## TRIANGLE_CIRCUMCIRCLE computes the circumcircle of a triangle in 2D.
#
#  Discussion:
#
#    The circumcenter of a triangle is the center of the circumcircle, the
#    circle that passes through the three vertices of the triangle.
#
#    The circumcircle contains the triangle, but it is not necessarily the
#    smallest triangle to do so.
#
#    If all angles of the triangle are no greater than 90 degrees, then
#    the center of the circumscribed circle will lie inside the triangle.
#    Otherwise, the center will lie outside the triangle.
#
#    The circumcenter is the intersection of the perpendicular bisectors
#    of the sides of the triangle.
#
#    In geometry, the circumcenter of a triangle is often symbolized by "O".
#
#    Thanks to Chenguang Zhang for pointing out a mistake in the formula
#    for the center, 02 December 2016.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real R, CENTER(2,1), the circumradius and circumcenter
#    of the triangle.
#
  import numpy as np

  center = np.zeros ( 2 )
#
#  Circumradius.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  bot = ( a + b + c ) * ( - a + b + c ) * (   a - b + c ) * (   a + b - c )

  if ( bot <= 0.0 ):
    r = - 1.0
    return r, center

  r = a * b * c / np.sqrt ( bot )
#
#  Circumcenter.
#
  f = np.zeros ( 2 )

  f[0] = ( t[0,1] - t[0,0] ) ** 2 + ( t[1,1] - t[1,0] ) ** 2
  f[1] = ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2

  top = np.zeros ( 2 )

  top[0] =    ( t[1,2] - t[1,0] ) * f[0] - ( t[1,1] - t[1,0] ) * f[1]
  top[1] =  - ( t[0,2] - t[0,0] ) * f[0] + ( t[0,1] - t[0,0] ) * f[1]

  det  =    ( t[1,2] - t[1,0] ) * ( t[0,1] - t[0,0] ) \
          - ( t[1,1] - t[1,0] ) * ( t[0,2] - t[0,0] ) 

  center[0] = t[0,0] + 0.5 * top[0] / det
  center[1] = t[1,0] + 0.5 * top[1] / det

  return r, center

def triangle_circumcircle_test ( ):

#*****************************************************************************80
#
## TRIANGLE_CIRCUMCIRCLE_TEST tests TRIANGLE_CIRCUMCIRCLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'TRIANGLE_CIRCUMCIRCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_CIRCUMCIRCLE computes the circumcenter of a triangle.' )

  for i in range ( 0, 4 ):

    if ( i == 0 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 1.0 ] ] )
    elif ( i == 1 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 0.86602539 ] ] )
    elif ( i == 2 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

    r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' );

    r, center = triangle_circumcircle ( t )

    r8vec_print ( 2, center, '  Circumcenter' )

    print ( '' )
    print ( '  Circumradius: %g' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_CIRCUMCIRCLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_circumcircle_test ( )
  timestamp ( )
 
