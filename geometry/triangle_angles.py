#! /usr/bin/env python
#
def triangle_angles ( t ):

#*****************************************************************************80
#
## TRIANGLE_ANGLES computes the angles of a triangle in 2D.
#
#  Discussion:
#
#    The law of cosines is used:
#
#      C^2 = A^2 + B^2 - 2 * A * B * COS ( GAMMA )
#
#    where GAMMA is the angle opposite side C.
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
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real ANGLE(3), the angles opposite
#    sides P1-P2, P2-P3 and P3-P1, in radians.
#
  import numpy as np
#
#  Compute the length of each side.
#
  a = np.sqrt ( ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2 )
  b = np.sqrt ( ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2 )
  c = np.sqrt ( ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2 )

  angle = np.zeros ( 3 )
#
#  Take care of unlikely special cases.
#
  if ( a == 0.0 and b == 0.0 and c == 0.0 ):
    for i in range ( 0, 3 ):
      angle[i] = 2.0 * np.pi / 3.0
    return angle

  if ( c == 0.0 or a == 0.0 ):
    angle[0] = np.pi
  else:
    angle[0] = np.arccos ( ( c * c + a * a - b * b ) / ( 2.0 * c * a ) )

  if ( a == 0.0 or b == 0.0 ):
    angle[1] = np.pi
  else:
    angle[1] = np.arccos ( ( a * a + b * b - c * c ) / ( 2.0 * a * b ) )

  if ( b == 0.0 or c == 0.0 ):
    angle[2] = np.pi
  else:
    angle[2] = np.arccos ( ( b * b + c * c - a * a ) / ( 2.0 * b * c ) )

  return angle

def triangle_angles_test ( ):

#*****************************************************************************80
#
## TRIANGLE_ANGLES_TEST tests TRIANGLE_ANGLES.
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

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_ANGLES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_ANGLES computes the angles of a triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  angle = triangle_angles ( t )

  print ( '' )
  print ( '      Radians      Degrees' )
  print ( '' )
  for i in range ( 0, 3 ):
    print ( '  %12g  %12g' % ( angle[i], angle[i] * 180.0 / np.pi ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_ANGLES_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_angles_test ( )
  timestamp ( )
