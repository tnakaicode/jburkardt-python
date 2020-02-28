#! /usr/bin/env python
#
def mountain ( n, x, y ):

#*****************************************************************************80
#
## MOUNTAIN enumerates the mountains.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, ...
#    N must be positive.
#
#    Input, integer X, Y, ...
#    0 <= X <= 2 * N,
#
#    Output, integer VALUE, the value of the "mountain function"
#    M ( N, X, Y ), which is the number of all mountain ranges from
#    (X,Y) to (2*N,0) which do not drop below sea level.
#
  from i4_choose import i4_choose
  from sys import exit
#
#  Check.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'MOUNTAIN - Fatal error!' )
    print ( '  N <= 0.' )
    print ( '  N = %d' % ( n ) )
    exit ( 'MOUNTAIN - Fatal error!' )

  if ( x < 0 ):
    print ( '' )
    print ( 'MOUNTAIN - Fatal error!' )
    print ( '  X < 0.' )
    print ( '  X = %d' % ( x ) )
    exit ( 'MOUNTAIN - Fatal error!' )

  if ( 2 * n < x ):
    print ( '' )
    print ( 'MOUNTAIN - Fatal error!' )
    print ( '  2 * N < X.' )
    print ( '  X = %d' % ( x ) )
    print ( '  N = %d' % ( n ) )
    exit ( 'MOUNTAIN - Fatal error!' )
#
#  Special cases.
#
  if ( y < 0 ):
    value = 0
    return value

  if ( 2 * n < x + y ):
    value = 0
    return value

  if ( ( ( x + y ) % 2 ) == 1 ):
    value = 0
    return value

  a = 2 * n - x
  b = n - ( ( x + y ) // 2 )
  c = n - 1 - ( ( x + y ) // 2 )

  value = i4_choose ( a, b ) - i4_choose ( a, c )

  return value

def mountain_test ( ):

#*****************************************************************************80
#
## MOUNTAIN_TEST tests MOUNTAIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'MOUNTAIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MOUNTAIN computes mountain numbers.' )
  print ( '' )
  print ( '   Y    MXY' )
  print ( '' )

  for y in range ( 0, n + 1 ):
    print ( '  %2d   ' % ( y ), end = '' )
    for x in range ( 0, 2 * n + 1 ):
      mxy = mountain ( n, x, y )
      print ( '%4d' % ( mxy ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'MOUNTAIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  mountain_test ( )
  timestamp ( )
 
