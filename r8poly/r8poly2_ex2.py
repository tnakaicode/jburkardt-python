#! /usr/bin/env python
#
def r8poly2_ex2 ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## R8POLY2_EX2 finds the extremal point of a parabola determined by three points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X1, Y1, X2, Y2, X3, Y3, the coordinates of 
#    three points on the parabola.  X1, X2 and X3 must be distinct.
#
#    Output, real X, Y, the X coordinate of the extremal 
#    point of the parabola, and the value of the parabola at that point.
#
#    Output, real A, B, C, the coefficients that define the
#    parabola: P(X) = A * X^2 + B * X + C.
#
#    Output, integer IERROR, error flag.
#    0, no error.
#    1, two of the X values are equal.
#    2, the data lies on a straight line there is no finite extremal
#    point.
#
  import numpy as np
  from r8mat_inverse_3d import r8mat_inverse_3d

  ierror = 0
  x = x1
  y = y1
  a = 0.0
  b = 0.0
  c = 0.0

  if ( x1 == x2 or x2 == x3 or x3 == x1 ):
    ierror = 1
    return x, y, a, b, c, ierror

  if ( y1 == y2 and y2 == y3 and y3 == y1 ):
    x = x1
    y = y1
    return x, y, a, b, c, ierror
#
#  Set up the Vandermonde matrix.
#
  v = np.array ( [ \
    [ 1.0, x1, x1 * x1 ], \
    [ 1.0, x2, x2 * x2 ], \
    [ 1.0, x3, x3 * x3 ] ] )
#
#  Get the inverse.
#
  w, det = r8mat_inverse_3d ( v )
#
#  Compute the parabolic coefficients.
#
  c = w[0,0] * y1 + w[0,1] * y2 + w[0,2] * y3
  b = w[1,0] * y1 + w[1,1] * y2 + w[1,2] * y3
  a = w[2,0] * y1 + w[2,1] * y2 + w[2,2] * y3
#
#  Determine the extremal point.
#
  if ( a == 0.0 ):
    ierror = 2
    return x, y, a, b, c, ierror

  x = -b / ( 2.0 * a )
  y = a * x * x + b * x + c

  return x, y, a, b, c, ierror

def r8poly2_ex2_test ( ):

#*****************************************************************************80
#
## R8POLY2_EX2_TEST tests R8POLY2_EX2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8POLY2_EX2_TEST' )
  print ( '  R8POLY2_EX2 finds the extreme value' )
  print ( '  of a parabola determined by three points.' )

  a =  2.0
  b = -4.0
  c = 10.0

  x1 = 1.0
  y1 = a * x1 * x1 + b * x1 + c
  x2 = 2.0
  y2 = a * x2 * x2 + b * x2 + c
  x3 = 3.0
  y3 = a * x3 * x3 + b * x3 + c

  print ( '' )
  print ( '  Parabolic coefficients:' )
  print ( '  A = %f, B = %f, C = %f' % ( a, b, c ) )
  print ( '' )
  print ( '  Point 1: (%g,%g)' % ( x1, y1 ) )
  print ( '  Point 1: (%g,%g)' % ( x2, y2 ) )
  print ( '  Point 1: (%g,%g)' % ( x3, y3 ) )

  a = 0.0
  b = 0.0
  c = 0.0

  xmin, ymin, a, b, c, ierror = r8poly2_ex2 ( x1, y1, x2, y2, x3, y3 )

  print ( '\n' )
  print ( '  R8POLY2_EX2 returns XMIN = %f, YMIN = %f' % ( xmin, ymin ) )
  print ( '  and A = %f, B = %f, C = %f' % ( a, b, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY2_EX2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly2_ex2_test ( )
  timestamp ( )


