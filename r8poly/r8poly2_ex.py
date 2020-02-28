#! /usr/bin/env python3
#
def r8poly2_ex ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## R8POLY2_EX finds the extremal point of a parabola determined by three points.
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
#    Output, real X, Y, the X coordinate of the extremal point
#    of the parabola, and the value of the parabola at that point.
#
#    Output, integer IERROR, error flag.
#    0, no error.
#    1, two of the X values are equal.
#    2, the data lies on a straight line there is no finite extremal
#    point.
#
  ierror = 0
  x = x1
  y = y1

  if ( x1 == x2 or x2 == x3 or x3 == x1 ):
    ierror = 1
    return x, y, ierror

  if ( y1 == y2 and y2 == y3 and y3 == y1 ):
    return x, y, ierror

  bot = ( x2 - x3 ) * y1 - ( x1 - x3 ) * y2 + ( x1 - x2 ) * y3

  if ( bot == 0.0 ):
    ierror = 2
    return x, y, ierror

  x = 0.5 * ( \
          x1 * x1 * ( y3 - y2 ) \
        + x2 * x2 * ( y1 - y3 ) \
        + x3 * x3 * ( y2 - y1 ) ) / bot

  y = ( \
         ( x - x2 ) * ( x - x3 ) * ( x2 - x3 ) * y1 \
       - ( x - x1 ) * ( x - x3 ) * ( x1 - x3 ) * y2 \
       + ( x - x1 ) * ( x - x2 ) * ( x1 - x2 ) * y3 ) / \
       ( ( x1 - x2 ) * ( x2 - x3 ) * ( x1 - x3 ) )

  return x, y, ierror

def r8poly2_ex_test ( ):

#*****************************************************************************80
#
## R8POLY2_EX_TEST tests R8POLY2_EX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8POLY2_EX_TEST' )
  print ( '  R8POLY2_EX finds the extreme value' )
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

  xmin, ymin, ierror = r8poly2_ex ( x1, y1, x2, y2, x3, y3 )

  print ( '' )
  print ( '  R8POLY2_EX returns XMIN = %f, YMIN = %f' % ( xmin, ymin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY2_EX_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly2_ex_test ( )
  timestamp ( )


