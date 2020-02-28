#! /usr/bin/env python
#
def diophantine_solution_minimize ( a, b, x, y ):

#*****************************************************************************80
#
## DIOPHANTINE_SOLUTION_MINIMIZE: minimal solution of a Diophantine equation.
#
#  Discussion:
#
#    Given a solution (X,Y) of a Diophantine equation:
#
#      A * X + B * Y = C.
#
#    then there are an infinite family of solutions of the form
#
#      ( X(i), Y(i) ) = ( X + i * B, Y - i * A )
#
#    An integral solution of minimal Euclidean norm can be found by
#    tentatively moving along the vectors (B,-A) and (-B,A) one step
#    at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998, page 446.
#
#  Parameters:
#
#    Input, integer A, B, the coefficients of the Diophantine equation.
#    A and B are assumed to be relatively prime.
#
#    Input, integer X, Y, on input, a solution of the Diophantine equation.
#
#    Output, integer X, Y, a solution of minimal Euclidean norm.
#

#
#  Compute the minimum for T real, and then look nearby.
#
  t = float ( - b * x + a * y ) / float ( a * a + b * b )

  x = x + int ( round ( t ) ) * b
  y = y - int ( round ( t ) ) * a
#
#  Look nearby.
#
  norm = x * x + y * y

  while ( True ):

    x2 = x + b
    y2 = y - a

    norm2 = x2 * x2 + y2 * y2

    if ( norm <= norm2 ):
      break

    x = x2
    y = y2
    norm = norm2

  while ( True ):

    x2 = x - b
    y2 = y + a

    norm2 = x2 * x2 + y2 * y2

    if ( norm <= norm2 ):
      break

    x = x2
    y = y2
    norm = norm2

  return x, y

def diophantine_solution_minimize_test ( ):

#*****************************************************************************80
#
## DIOPHANTINE_SOLUTION_MINIMIZE_TEST tests DIOPHANTINE_SOLUTION_MINIMIZE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DIOPHANTINE_SOLUTION_MINIMIZE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIOPHANTINE_SOLUTION_MINIMIZE computes a minimal' )
  print ( '  Euclidean norm solution of a Diophantine equation:' )
  print ( '    A * X + B * Y = C' )

  a = 4096
  b = -15625
  c = 46116
  x = 665499996
  y = 174456828

  r = a * x + b * y - c

  print ( '' )
  print ( '  Coefficients:' )
  print ( '    A = %12d' % ( a ) )
  print ( '    B = %12d' % ( b ) )
  print ( '    C = %12d' % ( c ) )
  print ( '  Solution:' )
  print ( '    X = %12d' % ( x ) )
  print ( '    Y = %12d' % ( y ) )
  print ( '  Residual R = A * X + B * Y - C:' )
  print ( '    R = %12d' % ( r ) )

  x, y = diophantine_solution_minimize ( a, b, x, y )

  r = a * x + b * y - c

  print ( '' )
  print ( '  The minimized solution:' )
  print ( '    X = %12d' % ( x ) )
  print ( '    Y = %12d' % ( y ) )
  print ( '  Residual R = A * X + B * Y - C:' )
  print ( '    R = %12d' % ( r ) )

  x = 15621
  y = 4092

  r = a * x + b * y - c

  print ( '' )
  print ( '  The minimal positive solution:' )
  print ( '    X = %12d' % ( x ) )
  print ( '    Y = %12d' % ( y ) )
  print ( '  Residual R = A * X + B * Y - C:' )
  print ( '    R = %12d' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIOPHANTINE_SOLUTION_MINIMIZE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diophantine_solution_minimize_test ( )
  timestamp ( )

