#! /usr/bin/env python3
#
def football_dynamic_test ( ):

#*****************************************************************************80
#
## football_dynamic_test() tests football_dynamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 January 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'football_dynamic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  football_dynamic() computes the number of ways' )
  print ( '  of achieving a particular score in football.' )
  print ( '' )
  print ( '  We assume scoring options are:' )
  print ( '' )
  print ( '  +1 for a one point safety (returned conversion' )
  print ( '     after the other team scores a touchdown.)' )
  print ( '  +2 for a safety' )
  print ( '  +3 for a field goal' )
  print ( '  +6 for a touchdown with no followup' )
  print ( '  +7 for a touchdown with a point bonus' )
  print ( '  +8 for a touchdown with two point conversion' )
  print ( '' )
  print ( '   Score                  Ways' )
  print ( '' )
#
#  You get a score of N points by
#    N-1 + a 1 point safety,
#    N-2 + a safety, or
#    N-3 + a field goal, or
#    N-6 + a touchdown with no followup
#    N-7 + a touchdown with a point bonus, or
#    N-8 + a touchdown with two point conversion.
#
  n = 50
  s = football_dynamic ( n )

  for i in range ( 0, n + 1 ):
    print ( i, s[i] )

  print ( '' )
  print ( 'football_dynamic_test():' )
  print ( '  Normal end of execution.' )

  return

def football_dynamic ( n ):

#*****************************************************************************80
#
## football_dynamic() counts the ways of getting any football score from 0 to N.
#
#  Discussion:
#
#    This code was updated to use logical factors. 
#    For instance, (1<=i) is 0 if i < 1, and 1 otherwise.
#    This enables the computation to be written as a single formula.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the highest score to be considered.
#
#  Output:
#
#    integer football_dynamic[n+1]: the number of ways of achieving each score 
#    from 0 to n.
#
  import numpy as np

  s = np.zeros ( n + 1, dtype = int )
#
#  Only one way to get a score of 0.
#
  s[0] = 1

  for i in range ( 1, n + 1 ):
 
    s[i] = ( 1 <= i ) * s[i-1] \
         + ( 2 <= i ) * s[i-2] \
         + ( 3 <= i ) * s[i-3] \
         + ( 6 <= i ) * s[i-6] \
         + ( 7 <= i ) * s[i-7] \
         + ( 8 <= i ) * s[i-8]

  return s

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
  football_dynamic_test ( )
  timestamp ( )

