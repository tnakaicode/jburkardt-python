#! /usr/bin/env python
#
def line_imp2exp ( a, b, c ):

#*****************************************************************************80
#
## LINE_IMP2EXP converts an implicit line to explicit form in 2D.
#
#  Discussion:
#
#    The implicit form of line in 2D is:
#
#      A * X + B * Y + C = 0
#
#    The explicit form of a line in 2D is:
#
#      ( P1, P2 ).
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
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Parameters:
#
#    Input, real A, B, C, the implicit line parameters.
#
#    Output, real P1(2), P2(2), two points on the line.
#
  import numpy as np
  from sys import exit

  normsq = a * a + b * b

  if ( normsq == 0.0 ):
    print ( '' )
    print ( 'LINE_IMP2EXP - Fatal error!' )
    print ( '  A * A + B * B = 0.' )
    exit ( 'LINE_IMP2EXP - Fatal error!' )

  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )

  p1[0] = - a * c / normsq
  p1[1] = - b * c / normsq

  if ( abs ( b ) < abs ( a ) ):
    p2[0] = - ( a - b / a ) * c / normsq
    p2[1] = - ( b + 1.0 ) * c / normsq
  else:
    p2[0] = - ( a + 1.0 ) * c / normsq
    p2[1] = - ( b - a / b ) * c / normsq

  return p1, p2

def line_imp2exp_test ( ):

#*****************************************************************************80
#
## LINE_IMP2EXP_TEST tests LINE_IMP2EXP.
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
  from line_exp2imp import line_exp2imp
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'LINE_IMP2EXP_TEST' )
  print ( '  LINE_IMP2EXP converts implicit to explicit lines.' )

  a = 1.0
  b = 2.0
  c = 3.0

  print ( '' )
  print ( '  Implicit line A, B, C = %f  %f  %f' % ( a, b, c ) )

  p1, p2 = line_imp2exp ( a, b, c )

  r8vec_print ( 2, p1, '  The point P1:' )
  r8vec_print ( 2, p2, '  The point P2:' )

  a, b, c = line_exp2imp ( p1, p2 )

  print ( '  Recovered A, B, C =  %f  %f  %f' % ( a, b, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LINE_IMP2EXP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  line_imp2exp_test ( )
  timestamp ( )

