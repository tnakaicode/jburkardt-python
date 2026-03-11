#! /usr/bin/env python3
#
def traffic_simulation ( cycle_num ):

#*****************************************************************************80
#
## traffic_simulation() simulates the cars waiting at one traffic light.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    Original MATLAB version by Brian Hahn, Dan Valentine.
#    This version by John Burkardt.
#
#  Reference:
#
#    Brian Hahn, Dan Valentine,
#    Essential MATLAB for Engineers and Scientists,
#    Academic Press, 2009,
#    ISBN13: 978-0123748836,
#    LC: TA345.V34.
#
#  Input:
#
#    integer CYCLE_NUM, the number of 10-second time cycles to model.
#
#  Local:
#
#    integer CARS, the number of cars waiting at the light.
#
#    integer CARS_IN, the total number of cars that have come.
#
#    integer CARS_OUT, the total number of cars that have left.
#
#    integer CYCLE, the number of time cycles that have elapsed.
#
#    integer CYCLE_LENGTH, the number of seconds in one time cycle.
#
#    integer GREEN_CYCLES, the number of 10-second time cycles that 
#    a green light lasts.
#
#    integer GREEN_TIMER, keeps track of the number of time cycles the
#    green light has been on.
#
#    integer LIGHT, the state of the light.
#    'r', the light is now red.
#    'g', the light is now green.
#
#    real P, the probability that a new car will come to the light
#    in the next second.
#
#    integer RED_CYCLES, the number of 10-second time cycles that 
#    a red light lasts.
#
#    integer RED_TIMER, keeps track of the number of time cycles the
#    red light has been on.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  rng = default_rng ( )
#
#  Initialize.
#
  cars = 0
  cars_in = 0
  cars_out = 0
  car_wait_cycles = 0
  cycle = 0
  cycle_length = 10
  green_cycles = 2
  green_timer = 0
  light = 'r'
  p = 0.3
  red_cycles = 4
  red_timer = 0
#
#  Set up the plot data.
#
  plot_data = np.zeros ( [ 2, cycle_num + 1 ] )
#
#  Handle the "0"-th cycle.
#
  plot_data[0,cycle] = cycle
  plot_data[1,cycle] = cars

  prq ( cars, light, cycle )
#
#  Handle cycles 1 through CYCLE_NUM.
#
  for cycle in range ( 1, cycle_num + 1 ):
#
#  Each second of the cycle, choose a random number.
#  If it is less than P, then a new car appeared at the light at that second.
#
    r = rng.random ( size = cycle_length )
    cars_new = np.sum ( r < p )
    cars = cars + cars_new
    cars_in = cars_in + cars_new
#
#  Handle this time cycle depending on whether the light is green or red.
#
    if ( light == 'g' ):
      cars, cars_out, light, green_timer = go ( green_cycles, cars, \
        cars_out, light, green_timer )
    else:
      cars, light, red_timer = stop ( red_cycles, cars, light, red_timer )
#
#  At the end of this cycle, how many cars are waiting?
#
    car_wait_cycles = car_wait_cycles + cars
#
#  Print the current status.
#
    prq ( cars, light, cycle )

    plot_data[0,cycle] = cycle
    plot_data[1,cycle] = cars
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( plot_data[0,:], plot_data[1,:], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'Time Cycles' )
  plt.ylabel ( 'Cars Waiting' )
  plt.title ( 'Traffic waiting at a Light' )
  filename = 'sim_' + str ( cycle_num ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Report the data.
#
  print ( '' )
  print ( '  Number of cycles =          ', cycle_num )
  print ( '  Simulated time in seconds = ', cycle_num * cycle_length )
  print ( '  Number of cars in =         ', cars_in )
  print ( '  Number of cars waiting =    ', cars )
  print ( '  Number of cars out =        ', cars_out )
  print ( '  Percentage Out/In =         ', 100 * cars_out / cars_in )
  wait_average_seconds = car_wait_cycles * cycle_length / cars_in
  print ( '  Average wait in seconds =   ', wait_average_seconds )
  wait_average_lights = car_wait_cycles / cars_in / ( red_cycles + green_cycles )
  print ( '  Average wait in cycles      ', wait_average_lights )

  return

def go ( green_cycles, cars, cars_out, light, green_timer ):

#*****************************************************************************80
#
## go() simulates traffic when the light is green.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    Original MATLAB version by Brian Hahn, Dan Valentine.
#    This version by John Burkardt.
#
#  Reference:
#
#    Brian Hahn, Dan Valentine,
#    Essential MATLAB for Engineers and Scientists,
#    Academic Press, 2009,
#    ISBN13: 978-0123748836,
#    LC: TA345.V34.
#
#  Input:
#
#    integer GREEN_CYCLES, the number of 10-second time cycles that 
#    a green light lasts.
#
#    integer CARS, the number of cars stopped at the light.
#
#    integer CARS_OUT, the total number of cars that have gone
#    through the light.
#
#    integer LIGHT, the state of the light.
#    'r', the light is now red.
#    'g', the light is now green.
#
#    integer GREEN_TIMER, keeps track of the number of time cycles the
#    green light has been on.
#
#  Output:
#
#    integer CARS, the number of cars stopped at the light.
#
#    integer CARS_OUT, the total number of cars that have gone
#    through the light.
#
#    integer LIGHT, the state of the light.
#    'r', the light is now red.
#    'g', the light is now green.
#
#    integer GREEN_TIMER, keeps track of the number of time cycles the
#    green light has been on.
#

#
#  In one 10-second time cycle, we estimate 8 cars can move out.
#
  cars_through = min ( 8, cars )

  cars = cars - cars_through
  cars_out = cars_out + cars_through
#
#  Advance the timer.  If the green light has timed out, reset the timer 
#  and switch to red.
#
  green_timer = green_timer + 1

  if ( green_cycles <= green_timer ):
    light = 'r'
    green_timer = 0

  return cars, cars_out, light, green_timer

def stop ( red_cycles, cars, light, red_timer ):

#*****************************************************************************80
#
## stop() simulates the traffic when the light is red.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    Original MATLAB version by Brian Hahn, Dan Valentine.
#    This version by John Burkardt.
#
#  Reference:
#
#    Brian Hahn, Dan Valentine,
#    Essential MATLAB for Engineers and Scientists,
#    Academic Press, 2009,
#    ISBN13: 978-0123748836,
#    LC: TA345.V34.
#
#  Input:
#
#    integer RED_CYCLES, the number of 10-second time cycles that 
#    a red light lasts.
#
#    integer CARS, the number of cars stopped at the light.
#
#    integer LIGHT, the state of the light.
#    'r', the light is now red.
#    'g', the light is now green.
#
#    integer RED_TIMER, keeps track of the number of time cycles the
#    red light has been on.
#
#  Output:
#
#    integer CARS, the number of cars stopped at the light.
#
#    integer LIGHT, the state of the light.
#    'r', the light is now red.
#    'g', the light is now green.
#
#    integer RED_TIMER, keeps track of the number of time cycles the
#    red light has been on.
#

#
#  Advance the timer.
#  If the red light has timed out, reset the timer and switch to green.
#
  red_timer = red_timer + 1

  if ( red_cycles <= red_timer ):
    light = 'g'
    red_timer = 0

  return cars, light, red_timer

def prq ( cars, light, cycle ):

#*****************************************************************************80
#
## prq() prints the current traffic waiting at the light.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    Original MATLAB version by Brian Hahn, Dan Valentine.
#    This version by John Burkardt.
#
#  Reference:
#
#    Brian Hahn, Dan Valentine,
#    Essential MATLAB for Engineers and Scientists,
#    Academic Press, 2009,
#    ISBN13: 978-0123748836,
#    LC: TA345.V34.
#
#  Input:
#
#    integer CARS, the number of cars stopped at the light.
#
#    integer LIGHT, the state of the light.
#    'r', the light is now red.
#    'g', the light is now green.
#
#    integer CYCLE, the current 10-second time cycle.
#
  print ('  Cycle', cycle )
  if ( light == 'r' ):
    print ( 'R  ' )
  else:
    print ( 'G  ' )
  i = cars
  c = ( i // 100 )
  i = i - 100 * c
  for j in range ( 0, c ):
    print ( 'C', end = '' )
  x =  ( i // 10 )
  i = i - 10 * x
  for j in range ( 0, x ):
    print ( 'X', end = '' )
  for j in range ( 0, i ):
    print ( 'I', end = '' )
  print ( '' )

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

def traffic_simulation_test ( ):

#*****************************************************************************80
#
## traffic_simulation_test() tests traffic_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'traffic_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test traffic_simulation().' )

  traffic_simulation ( 25 )
  traffic_simulation ( 50 )
  traffic_simulation ( 100 )
  traffic_simulation ( 200 )
#
#  Terminate.
#
  print ( '' )
  print ( 'traffic_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  traffic_simulation_test ( )
  timestamp ( )

