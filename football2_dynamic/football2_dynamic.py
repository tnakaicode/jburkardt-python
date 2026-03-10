#! /usr/bin/env python3
#
def football2_dynamic_test ( ):

#*****************************************************************************80
#
## football2_dynamic_test() tests football2_dynamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'football2_dynamic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  football2_dynamic() computes the number of ways' )
  print ( '  of achieving a particular score in football.' )
  print ( '' )
  print ( '  For this program, the order in which points are achieved' )
  print ( '  matters, so 6+3 and 3+6 are considered to be two distinct' )
  print ( '  ways of reaching a score of 9, even though both ways involve' )
  print ( '  the same facts, a field goal and a touchdown with no followup.' )
  print ( '' )
  print ( '  We assume scoring options are:' )
  print ( '' )
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
#    N-2 + a safety, or
#    N-3 + a field goal, or
#    N-6 + a touchdown with no followup
#    N-7 + a touchdown with a point bonus, or
#    N-8 + a touchdown with two point conversion.
#
  n = 50
  s = football2_dynamic ( n )

  for i in range ( 0, n + 1 ):
    print ( i, s[i] )

  print ( '' )
  print ( 'football2_dynamic_test():' )
  print ( '  Normal end of execution.' )

  return

def football2_dynamic ( n ):

#*****************************************************************************80
#
## football2_dynamic() counts the ways of getting any football score from 0 to N.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2023
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

  for i in range ( 0, n + 1 ):
 
    if ( i == 0 ):
      s[i] = 1
#
#  Add 2 points for a safety.
#
    if ( 2 <= i ):
      s[i] = s[i] + s[i-2]
#
#  Add 3 points for a field goal.
#
    if ( 3 <= i ):
      s[i] = s[i] + s[i-3]
#
#  Add 6 points for a touchdown with no conversion.
#
    if ( 6 <= i ):
      s[i] = s[i] + s[i-6]
#
#  Add 7 points for a touchdown with 1 point conversion.
#
    if ( 7 <= i ):
      s[i] = s[i] + s[i-7]
#
#  Add 8 points for a touchdown with 2 point conversion.
#
    if ( 8 <= i ):
      s[i] = s[i] + s[i-8]

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
  football2_dynamic_test ( )
  timestamp ( )

