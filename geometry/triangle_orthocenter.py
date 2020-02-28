#! /usr/bin/env python
#
def triangle_orthocenter ( t ):

#*****************************************************************************80
#
## TRIANGLE_ORTHOCENTER computes the orthocenter of a triangle in 2D.
#
#  Discussion:
#
#    The orthocenter is defined as the intersection of the three altitudes
#    of a triangle.
#
#    An altitude of a triangle is the line through a vertex of the triangle
#    and perpendicular to the opposite side.
#
#    In geometry, the orthocenter of a triangle is often symbolized by "H".
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2015
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
#    Output, real CENTER(2,1), the orthocenter of the triangle.
#
#    Output, logical FLAG, is TRUE if the value could not be computed.
#
  import numpy as np
  from line_exp_perp import line_exp_perp
  from lines_exp_int import lines_exp_int

  p1 = np.zeros ( 2 )
  p1[0] = t[0,0]
  p1[1] = t[1,0]
  p2 = np.zeros ( 2 )
  p2[0] = t[0,1]
  p2[1] = t[1,1]
  p3 = np.zeros ( 2 )
  p3[0] = t[0,2]
  p3[1] = t[1,2]
  center = np.zeros ( 2 )
#
#  Determine a point P23 common to the line (P2,P3) and
#  its perpendicular through P1.
#
  p23, flag = line_exp_perp ( p2, p3, p1 )

  if ( flag ):
    center[0] = float ( 'inf' )
    center[1] = float ( 'inf' )
    return center, flag
#
#  Determine a point P31 common to the line (P3,P1) and
#  its perpendicular through P2.
#
  p31, flag = line_exp_perp ( p3, p1, p2 )

  if ( flag ):
    center[0] = float ( 'inf' )
    center[1] = float ( 'inf' )
    return center, flag
#
#  Determine CENTER, the intersection of the lines (P1,P23) and (P2,P31).
#
  ival, center = lines_exp_int ( p1, p23, p2, p31 )

  if ( ival != 1 ):
    flag = 1
    center[0] = float ( 'inf' )
    center[1] = float ( 'inf' )
    return center, flag

  return center, flag

def triangle_orthocenter_test ( ):

#*****************************************************************************80
#
#% TRIANGLE_ORTHOCENTER_TEST tests TRIANGLE_ORTHOCENTER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2015
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
  print ( 'TRIANGLE_ORTHOCENTER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_ORTHOCENTER computes the orthocenter of a triangle.' )

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

    center, flag = triangle_orthocenter ( t )

    r8vec_print ( 2, center, '  Orthocenter' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_ORTHOCENTER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_orthocenter_test ( )
  timestamp ( )
