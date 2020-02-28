#! /usr/bin/env python
#
def triangle_xsi_to_xy ( t, xsi ):

#*****************************************************************************80
#
## TRIANGLE_XSI_TO_XY converts from barycentric to XY coordinates in 2D.
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
#    Input, real XSI(3,1), the barycentric coordinates of a point.
#    XSI(1) + XSI(2) + XSI(3) should equal 1, but this is not checked.
#
#    Output, real P(2,1), the XY coordinates of the point.
#
  import numpy as np

  p = np.zeros ( 2 )

  p[0] = t[0,0] * xsi[0] + t[0,1] * xsi[1] + t[0,2] * xsi[2]
  p[1] = t[1,0] * xsi[0] + t[1,1] * xsi[1] + t[1,2] * xsi[2]

  return p

def triangle_xsi_to_xy_test ( ):

#*****************************************************************************80
#
#% TRIANGLE_XSI_TO_XY_TEST tests TRIANGLE_XSI_TO_XY.
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
  from triangle_xy_to_xsi import triangle_xy_to_xsi

  seed = 123456789
  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_XSI_TO_XY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_XSI_TO_XY converts XSI to XY coordinates.' )
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
  print ( 'TRIANGLE_XSI_TO_XY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_xsi_to_xy_test ( )
  timestamp ( )
 
