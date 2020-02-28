#! /usr/bin/env python
#
def lines_exp_int ( p1, p2, q1, q2 ):

#*****************************************************************************80
#
## LINES_EXP_INT determines where two explicit lines intersect in 2D.
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      the line through the points P1, P2.
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
#  Parameters:
#
#    Input, real P1(2,1), P2(2,1), two points on the first line.
#
#    Input, real Q1(2,1), Q2(2,1), two points on the second line.
#
#    Output, integer IVAL, reports on the intersection:
#    0, no intersection, the lines may be parallel or degenerate.
#    1, one intersection point, returned in P.
#    2, infinitely many intersections, the lines are identical.
#
#    Output, real P(2,1), if IVAl = 1, P is
#    the intersection point.  Otherwise, P = 0.
#
  import numpy as np
  from line_exp2imp import line_exp2imp
  from lines_imp_int import lines_imp_int

  ival = False
  p = np.zeros ( 2 )
#
#  Check whether either line is a point.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):
    point_1 = True
  else:
    point_1 = False

  if ( q1[0] == q2[0] and q1[1] == q2[1] ):
    point_2 = True
  else:
    point_2 = False
#
#  Convert the lines to ABC format.
#
  if ( not point_1 ):
    a1, b1, c1 = line_exp2imp ( p1, p2 )

  if ( not point_2 ):
    a2, b2, c2 = line_exp2imp ( q1, q2 )
#
#  Search for intersection of the lines.
#
  if ( point_1 and point_2 ):
    if ( p1[0] == q1[0] and p1[1] == q1[1] ):
      ival = True
      p[0] = p1[0]
      p[1] = p1[1]
  elif ( point_1 ):
    if ( a2 * p1[0] + b2 * p1[1] == c2 ):
      ival = True
      p[0] = p1[0]
      p[1] = p1[1]
  elif ( point_2 ):
    if ( a1 * q1[0] + b1 * q1[1] == c1 ):
      ival = True
      p[0] = q1[0]
      p[1] = q1[1]
  else:
    ival, p = lines_imp_int ( a1, b1, c1, a2, b2, c2 )

  return ival, p

def lines_exp_int_test ( ):

#*****************************************************************************80
#
## LINES_EXP_INT_TEST tests LINES_EXP_INT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'LINES_EXP_INT_TEST' )
  print ( '  LINES_EXP_INT finds intersections of' )
  print ( '  two explicit lines in 2D.' )
  print ( '' )

  for test in range ( 0, 3 ):
#
#  x + 2y - 4 = 0
#  x - y - 1 = 0
#
    if ( test == 0 ):

      p1 = np.array ( [ 0.0,  2.0 ] )
      p2 = np.array ( [ 4.0,  0.0 ] )
      q1 = np.array ( [ 0.0, -1.0 ] )
      q2 = np.array ( [ 1.0,  0.0 ] )
#
#  x + 2y - 4 = 0
#  2x + 4y - 1 = 0
#
    elif ( test == 1 ):

      p1 = np.array ( [ 0.00, 2.00 ] )
      p2 = np.array ( [ 4.00, 0.00 ] )
      q1 = np.array ( [ 0.00, 0.25 ] )
      q2 = np.array ( [ 0.50, 0.00 ] )
#
#  x + 2y - 4 = 0
#  -3x - 6y +12 = 0
#
    elif ( test == 2 ):

      p1 = np.array ( [ 0.0, 2.0 ] )
      p2 = np.array ( [ 4.0, 0.0 ] )
      q1 = np.array ( [ 0.0, 2.0 ] )
      q2 = np.array ( [ 4.0, 0.0 ] )

    print ( '' )
    print ( '  P1  %8f  %8f' % ( p1[0], p1[1] ) )
    print ( '  P2  %8f  %8f' % ( p2[0], p2[1] ) )
    print ( '' )
    print ( '  Q1  %8f  %8f' % ( q1[0], q1[1] ) )
    print ( '  Q2  %8f  %8f' % ( q2[0], q2[1] ) )

    ival, p = lines_exp_int ( p1, p2, q1, q2 )

    if ( ival == 1 ):
      print ( '  Intersection at %8f  %8f' % ( p[0], p[1] ) )
    elif ( ival == 0 ):
      print ( '  Lines are parallel, no intersection.' )
    elif ( ival == 2 ):
      print ( '  Lines are coincident.' )
    else:
      print ( '  Unknown return value of IVAL = %d' % ( ival ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LINE_EXP_INT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lines_exp_int_test ( )
  timestamp ( )
 
