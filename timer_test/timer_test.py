#! /usr/bin/env python3
#
def perf_counter_test ( rng ):

#*****************************************************************************80
#
## perf_counter_test() tests perf_counter() as a timer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from time import perf_counter
  import numpy as np

  n_log_min = 10
  n_log_max = 22
  n_min = 2 ** n_log_min
  n_max = 2 ** n_log_max
  n_rep = 5
  n_test = 1

  print ( '' )
  print ( 'perf_counter_test()' )
  print ( '  perf_counter() times the rng.random function:' )
  print ( '' )
  print ( '    x = rng.random ( size = n )' )
  print ( '' )
  print ( '  Data vectors will be of minimum size ', n_min )
  print ( '  Data vectors will be of maximum size ', n_max )
  print ( '  Number of repetitions of the operation: ', n_rep )
  print ( '' )
  print ( '  Timing results in seconds:' )
  print ( '' )
  print ( '      Size         Rep #1         Rep #2         Rep #3        ', end = '' )
  print ( 'Rep #4         Rep #5' )
  print ( '' )

  for n_log in range ( n_log_min, n_log_max + 1 ):

    n = 2 ** ( n_log )

    print ( '  %8d' % ( n ), end = '' )

    for i_rep in range ( 0, n_rep ):

      seconds = perf_counter ( )

      x = rng.random ( size = n )

      seconds = perf_counter ( ) - seconds

      print ( '  %12f' % ( seconds ), end = '' )

    print ( '' )

  return

def time_test ( rng ):

#*****************************************************************************80
#
## time_test() tests time() to time the rng.random() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from time import time
  import numpy as np

  n_log_min = 10
  n_log_max = 22
  n_min = 2 ** n_log_min
  n_max = 2 ** n_log_max
  n_rep = 5
  n_test = 1

  print ( '' )
  print ( 'time_test():' )
  print ( '  time() times the rng.random() function:' )
  print ( '' )
  print ( '    x = rng.random ( size = n )' )
  print ( '' )
  print ( '  Data vectors will be of minimum size ', n_min )
  print ( '  Data vectors will be of maximum size ', n_max )
  print ( '  Number of repetitions of the operation: ', n_rep )
  print ( '' )
  print ( '  Timing results in seconds:' )
  print ( '' )
  print ( '      Size         Rep #1         Rep #2         Rep #3        ', end = '' )
  print ( 'Rep #4         Rep #5' )
  print ( '' )

  for n_log in range ( n_log_min, n_log_max + 1 ):

    n = 2 ** ( n_log )

    print ( '  %8d' % ( n ), end = '' )

    for i_rep in range ( 0, n_rep ):

      seconds = time ( )

      x = rng.random ( size = n )

      seconds = time ( ) - seconds

      print ( '  %12f' % ( seconds ), end = '' )

    print ( '' )

  return

def timer_test ( ):

#*****************************************************************************80
#
## timer_test() tests timer().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform
 
  print ( '' )
  print ( 'timer_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test timers.' )

  rng = default_rng ( )

  perf_counter_test ( rng )
  time_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'timer_test():' )
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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  timer_test ( )
  timestamp ( )

