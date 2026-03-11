#! /usr/bin/env python3
#
def middle_square_test ( ):

#*****************************************************************************80
#
## middle_square_test() tests middle_square().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'middle_square_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test middle_square()' )

  middle_square_next_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'middle_square_test():' )
  print ( '  Normal end of execution.' )

  return

def middle_square_next ( s, d ):

#*****************************************************************************80
#
## middle_square_next() computes the next middle square random value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    The Middle of the Square,
#    08 August 2022,
#    http://bit-player.org/
#
#  Input:
#
#    integer S, the current seed, of no more than 2*D digits.
#
#    integer D, HALF the number of digits.  
#    Typical values are 2, 3, or 4.
#
#  Output:
#
#    integer R, the next seed.
#

#
#  Square.
#
  r = s * s
#
#  Drop last D digits.
#
  r = ( r // 10**d )
#
#  Drop first D digits.
#
  r = ( r % ( 10 ** ( 2 * d ) ) )

  return r
  
def middle_square_next_test ( ):

#*****************************************************************************80
#
## middle_square_next_test() tests middle_square_next().
#
#  Discussion:
#
#    This function simply demonstrates the results of 10 successive calls
#    to middle_square_next(), for a range of values of d.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 September 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'middle_square_next_test():' )
  print ( '  middle_square_next ( s, d ) applies the middle square algorithm' )
  print ( '  using a 2*d digit seed.' )

  for d in range ( 1, 6 ):

    print ( '' )
    print ( '  Using d = ', d )
    print ( '' )

    s = ( 2147483647 % ( 10 ** ( 2 * d ) ) )

    for i in range ( 0, 11 ):
      print ( '  %2d  %d' % ( i, s ) )
      s = middle_square_next ( s, d )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  middle_square_test ( )
  timestamp ( )


