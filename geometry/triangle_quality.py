#! /usr/bin/env python
#
def triangle_quality ( t ):

#*****************************************************************************80
#
## TRIANGLE_QUALITY: "quality" of a triangle in 2D.
#
#  Discussion:
#
#    The quality of a triangle is 2 times the ratio of the radius of the inscribed
#    circle divided by that of the circumscribed circle.  An equilateral
#    triangle achieves the maximum possible quality of 1.
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
#    Output, real QUALITY, the quality of the triangle.
#
  import numpy as np
#
#  Compute the length of each side.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  if ( a * b * c == 0.0 ):
    value = 0.0
  else:
    value = ( - a + b + c ) * ( a - b + c ) * ( a + b - c ) / ( a * b * c )

  return value

def triangle_quality_test ( ):

#*****************************************************************************80
#
## TRIANGLE_QUALITY_TEST tests TRIANGLE_QUALITY.
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

  ntest = 4

  print ( '' )
  print ( 'TRIANGLE_QUALITY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_QUALITY computes the quality of a triangle.' )

  for i in range ( 0, ntest ):
 
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
        [ 0.0, 1.0,  0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

    quality = triangle_quality ( t )

    print ( '' )
    print ( '  Quality = %g' % ( quality ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_QUALITY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_quality_test ( )
  timestamp ( )
 
