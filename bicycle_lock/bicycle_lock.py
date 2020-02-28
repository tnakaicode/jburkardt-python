#! /usr/bin/env python3
#
def bicycle_lock_test ( ):

#*****************************************************************************80
#
## BICYCLE_LOCK_TEST tests BICYCLE_LOCK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
  import platform
  import random

  print ( '' )
  print ( 'BICYCLE_LOCK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BICYCLE_LOCK determines a bicycle lock combination.' )
  print ( '  A bicycle combination lock consists of 3 dials,' )
  print ( '  each having 10 symbols, 0 through 9.' )
#
#  Set the combination randomly.
#  We can think of the combination as a number between 0 and 999.
#
  random.seed ( 'shuffle' )
  c = random.randint ( 0, 999 )

  print ( '  The "secret" combination is %d' % ( c ) )

  step = bicycle_lock ( c )

  if ( step == -1 ):
    print ( '' )
    print ( '  The combination was not found!' )
  else:
    print ( '' )
    print ( '  The combination was found on step %d' % ( step ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BICYCLE_LOCK_TEST' )
  print ( '  Normal end of execution.' )
  return

def bicycle_lock ( c ):

#*****************************************************************************80
#
## BICYCLE_LOCK finds the combination on a typical bicycle lock.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 May 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer C, the bicycle lock combination.
#
#    Output, integer STEP, the step on which the combination was found.
#
  step = 0

  for a in range ( 0, 1000 ):

    step = step + 1

    if ( a == c ):
      print ( '' )
      print ( '  The combination is %d' % ( c ) )
      return step

  step = -1

  return step

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  bicycle_lock_test ( )
  timestamp ( )

