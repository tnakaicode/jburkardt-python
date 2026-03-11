#! /usr/bin/env python3
#
def poisson_fixed_events ( lam, event_num, rng ):

#*****************************************************************************80
#
## poisson_fixed_events() simulates a given number of Poisson events.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real lam: the average number of events per unit time.
#
#    integer EVENT_NUM, the number of events to wait for.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real T(EVENT_NUM+1), the time at which a total of 0, 1, 2, ...
#    and EVENT_NUM events were observed.
#
#    real W(EVENT_NUM+1), the waiting time until the I-th event occurred.
#
  import numpy as np
#
#  Poisson waiting times follow an exponential distribution.
#
  w = np.zeros ( event_num + 1 )
  w[1:event_num+1] = - np.log ( rng.random ( event_num ) ) / lam
#
#  The time til event I is the sum of the waiting times 0 through I.
#
  t = np.cumsum ( w )

  return t, w

def poisson_fixed_events_test ( rng ):

#*****************************************************************************80
#
## poisson_fixed_events_test() tests poisson_fixed_events().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'poisson_fixed_events_test():' )
  print ( '  poisson_fixed_events() simulates a Poisson process' )
  print ( '  until a given number of events have occurred.' )
  print ( '' )
  print ( '  Simulate a Poisson process, for which, on average,' )
  print ( '  lam events occur per unit time.' )
  print ( '  Run until you have observed EVENT_NUM events.' )
 
  lam = 0.5
  event_num = 1000

  print ( '' )
  print ( '  lam =', lam )
  print ( '  EVENT_NUM =', event_num )

  t, w = poisson_fixed_events ( lam, event_num, rng )

  print ( '' )
  print ( '  Minimum wait =', np.min ( w[1:] ) )
  print ( '  Average wait =', np.sum ( w[1:] ) / event_num )
  print ( '  Maximum wait =', np.max ( w[1:] ) )

  print ( '' )
  print ( ' Count            Time            Wait' )
  print ( '' )
  for i in range ( 0, 6 ):
    print ( '  %4d  %14g  %14g' % ( i, t[i], w[i] ) )

  print ( '  ....  ..............  ..............' )
  for i in range ( event_num - 5, event_num + 1 ):
    print ( '  %4d  %14g  %14g' % ( i, t[i], w[i] ) )

  plt.clf ( )
  y = np.linspace ( 1, event_num + 1, event_num + 1 )
  plt.plot ( t, y, linewidth = 2 )
  plt.xlabel ( '<--Time-->' )
  plt.ylabel ( '<--Events observed-->' )
  plt.grid ( True )
  s = 'Observation of ' + str ( event_num ) + ' successive Poisson events'
  plt.title ( s )

  filename = 'poisson_timeline.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  bins = 40
  plt.clf ( )
  plt.hist ( w, bins )
  plt.xlabel ( '<--Waiting time-->' )
  plt.ylabel ( '<--Frequency-->' )
  plt.grid ( True )
  plt.title ( 'Frequency histogram of Poisson waiting times' )

  filename = 'poisson_times.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def poisson_fixed_time ( lam, time, rng ):

#*****************************************************************************80
#
## poisson_fixed_time() counts the Poisson events in a fixed time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real lam, the average number of events per unit time.
#
#    real TIME, the amount of time to observe.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer N, the number of Poisson events observed.
#
  import numpy as np

  n = 0
  t = 0.0

  while ( t < time ):
    dt = - np.log ( rng.random ( ) ) / lam
    n = n + 1
    t = t + dt

  return n

def poisson_fixed_time_test ( rng ):

#*****************************************************************************80
#
## poisson_fixed_time_test() tests poisson_fixed_time().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  lam = 0.5
  t = 1000.0
  test_num = 20000

  print ( '' )
  print ( 'poisson_fixed_time_test():' )
  print ( '  poisson_fixed_time() simulates a Poisson process' )
  print ( '  counting the number of events that occur during' )
  print ( '  a given time.' )
  print ( '' )
  print ( '  Simulate a Poisson process, for which, on average,' )
  print ( '  lam events occur per unit time.' )
  print ( '  Run for a total of', t, 'time units.' )
  print ( '  lam =', lam )

  n = np.zeros ( test_num )
  for test in range ( 0, test_num ):
    n[test] = poisson_fixed_time ( lam, t, rng )

  n_mean = np.mean ( n )
  n_var = np.var ( n )
  n_std = np.std ( n )
  print ( '' )
  print ( '  Mean number of events =', n_mean )
  print ( '  Variance =', n_var, '  STD = ', n_std )

  bins = 30
  plt.hist ( n, bins )
  plt.xlabel ( '<--Number of events-->' )
  plt.ylabel ( '<--Frequency-->' )
  plt.grid ( True )
  plt.title ( ' Number of Poisson events observed over 1000 time units' )

  filename = 'poisson_events.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def poisson_next_event ( lam, rng ):

#*****************************************************************************80
#
## poisson_next_event() simulates the occurrence of a single Poisson event.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real lam, the average number of events per unit time.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real T, the time at which the Poisson event was observed.
#
  import numpy as np

  t = - np.log ( rng.random ( ) ) / lam

  return t

def poisson_next_event_test ( rng ):

#*****************************************************************************80
#
## poisson_next_event_test() tests poisson_next_event().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'poisson_next_event_test():' )
  print ( '  poisson_next_event() simulates a Poisson process' )
  print ( '  until a single event has occurred.' )
  print ( '' )
  print ( '  Simulate a Poisson process, for which, on average,' )
  print ( '  lam events occur per unit time.' )
 
  lam = 0.5

  print ( '' )
  print ( '  lam =', lam )

  t_total = 0.0
  event = 0
  while ( t_total < 10.0 ):
    t = poisson_next_event ( lam, rng )
    event = event + 1
    t_total = t_total + t
    print ( '  Event #', event, 'at time', t_total, ', after waiting', t )

  return

def poisson_simulation_test ( ):

#*****************************************************************************80
#
## poisson_simulation_test() tests poisson_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'poisson_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test poisson_simulation().' )

  rng = default_rng ( )

  poisson_fixed_events_test ( rng )
  poisson_fixed_time_test ( rng )
  poisson_next_event_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'poisson_simulation_test():' )
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
  poisson_simulation_test ( )
  timestamp ( )

