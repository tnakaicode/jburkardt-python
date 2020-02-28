#! /usr/bin/env python
#
def line_exp_perp ( p1, p2, p3 ):

#*****************************************************************************80
#
## LINE_EXP_PERP computes a line perpendicular to a line and through a point.
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      ( P1, P2 ) = ( (X1,Y1), (X2,Y2) ).
#
#    The input point P3 should NOT lie on the line (P1,P2).  If it
#    does, then the output value P4 will equal P3.
#
#    P1-----P4-----------P2
#            |
#            |
#           P3
#
#    P4 is also the nearest point on the line (P1,P2) to the point P3.
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
#    Input, real P1(2), P2(2), two points on the line.
#
#    Input, real P3(2), a point (presumably not on the
#    line (P1,P2)), through which the perpendicular must pass.
#
#    Output, real P4(2), a point on the line (P1,P2),
#    such that the line (P3,P4) is perpendicular to the line (P1,P2).
#
#    Output, logical FLAG, is TRUE if the value could not be computed.
#
  import numpy as np

  bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) **2

  p4 = np.zeros ( 2 )

  if ( bot == 0.0 ):
    p4[0] = float ( 'inf' )
    p4[1] = float ( 'inf' )
    flag = 1
#
#  (P3-P1) dot (P2-P1) = Norm(P3-P1) * Norm(P2-P1) * Cos(Theta).
#
#  (P3-P1) dot (P2-P1) / Norm(P3-P1)**2 = normalized coordinate T
#  of the projection of (P3-P1) onto (P2-P1).
#
  t = ( ( p1[0] - p3[0] ) * ( p1[0] - p2[0] ) \
      + ( p1[1] - p3[1] ) * ( p1[1] - p2[1] ) ) / bot

  p4[0] = p1[0] + t * ( p2[0] - p1[0] )
  p4[1] = p1[1] + t * ( p2[1] - p1[1] )

  flag = 0

  return p4, flag

def line_exp_perp_test ( ):

#*****************************************************************************80
#
## LINE_EXP_PERP_TEST tests LINE_EXP_PERP.
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
  from r8vec_print import r8vec_print

  ntest = 3

  print ( '' )
  print ( 'LINE_EXP_PERP_TEST' )
  print ( '  LINE_EXP_PERP is given an explicit line (P1,P2),' )
  print ( '  and another point P3.  It then finds a point' )
  print ( '  P4 on (P1,P2) so that (P1,P2) is perpendicular' )
  print ( '  to (P3,P4).' )

  p1 = np.array ( [ 1.0, 3.0 ] )
  p2 = np.array ( [ 4.0, 0.0 ] )

  p3test = np.array ( [ \
    [ 0.0,  5.0, 5.0 ], \
    [ 0.0, -1.0, 3.0 ] ] )

  r8vec_print ( 2, p1, '  Point P1:' )
  r8vec_print ( 2, p2, '  Point P2:' )

  p3 = np.zeros ( 2 )

  for j in range ( 0, ntest ):

    p3[0] = p3test[0,j]
    p3[1] = p3test[1,j]

    r8vec_print ( 2, p3, '  Point P3:' )

    p4, flag = line_exp_perp ( p1, p2, p3 )

    r8vec_print ( 2, p4, '  Point P4:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'LINE_EXP_PERP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  line_exp_perp_test ( )
  timestamp ( )

