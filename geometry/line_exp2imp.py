#! /usr/bin/env python
#
def line_exp2imp ( p1, p2 ):

#*****************************************************************************80
#
## LINE_EXP2IMP converts an explicit line to implicit form in 2D.
#
#  Discussion:
#
#    The explicit form of a line in 2D is:
#
#      ( P1, P2 ) = ( (X1,Y1), (X2,Y2) ).
#
#    The implicit form of a line in 2D is:
#
#      A * X + B * Y + C = 0
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
#    Output, real A, B, C, the implicit form of the line.
#
  from sys import exit
#
#  Take care of degenerate cases.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):
    print ( '' )
    print ( 'LINE_EXP2IMP - Fatal error!' )
    print ( '  P1 = P2' )
    print ( '  P1 = %g  %g' % ( p1[0], p1[1] ) )
    print ( '  P2 = %g  %g' % ( p2[0], p2[1] ) )
    exit ( 'LINE_EXP2IMP - Fatal error!' )

  a = p2[1] - p1[1]
  b = p1[0] - p2[0]
  c = p2[0] * p1[1] - p1[0] * p2[1]

  norm = a * a + b * b + c * c

  if ( 0.0 < norm ):
    a = a / norm
    b = b / norm
    c = c / norm

  if ( a < 0.0 ):
    a = -a
    b = -b
    c = -c

  return a, b, c

def line_exp2imp_test ( ):

#*****************************************************************************80
#
## LINE_EXP2IMP_TEST tests LINE_EXP2IMP.
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
  from line_imp2exp import line_imp2exp
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'LINE_EXP2IMP_TEST' )
  print ( '  LINE_EXP2IMP converts explicit to implicit lines.' )

  a = 1.0
  b = 2.0
  c = 3.0

  print ( '' )
  print ( '  Implicit line A, B, C = %f  %f  %f' % ( a, b, c ) )

  p1, p2 = line_imp2exp ( a, b, c )

  r8vec_print ( 2, p1, '  The point P1:' )
  r8vec_print ( 2, p2, '  The point P2:' )

  [ a, b, c ] = line_exp2imp ( p1, p2 )

  print ( '  Recovered A, B, C =  %f  %f  %f' % ( a, b, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LINE_EXP2IMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  line_exp2imp_test ( )
  timestamp ( )

