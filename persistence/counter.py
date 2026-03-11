#! /usr/bin/env python3
#
def counter ( ):

#*****************************************************************************80
#
## counter() simply reports how many times it has been called.
#
#  Discussion:
#
#    If you can get a function like this to work, you have made a good
#    start at implementing persistent data
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Persistent:
#
#    int CALLS: the number of times this function has been called.
#
  if not hasattr ( counter, "calls" ):
    counter.calls = 0

  counter.calls = counter.calls + 1

  print ( "counter() has been called ", counter.calls, " times." )

  return

def counter_test ( ):

#*****************************************************************************80
#
## counter_test() tests counter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'counter_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test counter(), with the interface:' )
  print ( '    counter()' )
  print ( '' )

  for i in range ( 1, 11 ):
    counter ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'counter_test():' )
  print ( '  Normal end of execution.' )

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
  counter_test ( )
  timestamp ( )

