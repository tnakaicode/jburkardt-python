#! /usr/bin/env python3
#
def basketball_dynamic_test ( ):

#*****************************************************************************80
#
## basketball_dynamic_test() tests basketball_dynamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 January 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'basketball_dynamic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  basketball_dynamic() computes the number of ways' )
  print ( '  of achieving a particular score in basketball.' )
  print ( '' )
  print ( '  We assume scoring options are:' )
  print ( '' )
  print ( '  +1 for a free throw.)' )
  print ( '  +2 for a regular basket' )
  print ( '  +3 for a long basket' )
  print ( '' )
  print ( '   Score                  Ways' )
  print ( '' )

  n = 50
  s = basketball_dynamic ( n )

  for i in range ( 0, n + 1 ):
    print ( i, s[i] )

  print ( '' )
  print ( 'basketball_dynamic_test():' )
  print ( '  Normal end of execution.' )

  return

def basketball_dynamic ( n ):

#*****************************************************************************80
#
## basketball_dynamic() counts the ways of getting any basketball score from 0 to N.
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
#    31 January 2025
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
#    integer basketball_dynamic[n+1]: the number of ways of achieving each score 
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
         + ( 3 <= i ) * s[i-3]

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
  basketball_dynamic_test ( )
  timestamp ( )

