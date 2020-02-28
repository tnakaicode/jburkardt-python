#! /usr/bin/env python
#
def triangle_xy_to_xsi ( t, p ):

#*****************************************************************************80
#
## TRIANGLE_XY_TO_XSI converts from XY to barycentric in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Input, real P(2), the XY coordinates of a point.
#
#    Output, real XSI(3), the barycentric coordinates of the point.
#    XSI1 + XSI2 + XSI3 should equal 1.
#
  import numpy as np

  xsi = np.zeros ( 3 )

  det = ( t[0,0] - t[0,2] ) * ( t[1,1] - t[1,2] ) \
      - ( t[0,1] - t[0,2] ) * ( t[1,0] - t[1,2] )

  xsi[0] = (   ( t[1,1] - t[1,2] ) * ( p[0] - t[0,2] ) \
             - ( t[0,1] - t[0,2] ) * ( p[1] - t[1,2] ) ) / det

  xsi[1] = ( - ( t[1,0] - t[1,2] ) * ( p[0] - t[0,2] ) \
             + ( t[0,0] - t[0,2] ) * ( p[1] - t[1,2] ) ) / det

  xsi[2] = 1.0 - xsi[0] - xsi[1]

  return xsi

def triangle_xy_to_xsi_test ( ):

#*****************************************************************************80
#
## TRIANGLE_XY_TO_XSI_TEST tests TRIANGLE_XY_TO_XSI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print
  from triangle_sample import triangle_sample
  from triangle_xsi_to_xy import triangle_xsi_to_xy

  seed = 123456789
  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_XY_TO_XSI_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_XY_TO_XSI converts XY to XSI coordinates.' )
  print ( '' )
  print ( '  We verify that (X,Y) -> (XSI1,XSI2,XSI3) -> (X,Y)' )
  print ( '  works properly.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '  Sample points:' )
  print ( '' )

  p = np.zeros ( 2 )

  for j in range ( 0, 10 ):

    if ( j == 0 ):
      p[0] = ( t[0,0] + t[0,1] + t[0,2] ) / 3.0
      p[1] = ( t[1,0] + t[1,1] + t[1,2] ) / 3.0
    elif ( j == 1 ):
      p[0] = 3.0
      p[1] = 0.0
    else:
      p, seed = triangle_sample ( t, 1, seed )

    xsi = triangle_xy_to_xsi ( t, p )

    p2 = triangle_xsi_to_xy ( t, xsi )

    print ( '' )
    print ( '  %8g  %8g    %8g  %8g  %8g' % ( p[0], p[1], xsi[0], xsi[1], xsi[2] ) )
    print ( '  %8g  %8g' % ( p2[0], p2[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_XY_TO_XSI_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_xy_to_xsi_test ( )
  timestamp ( )
 
