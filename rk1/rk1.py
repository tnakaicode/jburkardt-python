#! /usr/bin/env python3
#
def rk1 ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## rk1() solves an ODE using a Runge-Kutta order 1 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function dydt: points to a function that evaluates the right
#    hand side of the ODE.
#
#    real tspan[2]: contains the initial and final times.
#
#    real y0[m]: an array containing the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the times and solution values.
#
  import numpy as np

  m = np.size ( y0 )

  t0 = tspan[0]
  tstop = tspan[1]
  dt = ( tstop - t0 ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = t0
  y[0,:] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( dydt ( t[i], y[i,:] ) )

  return t, y

def rk1_test ( ):

#*****************************************************************************80
#
## rk1_test() tests rk1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 November 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rk1_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rk1().' )

  tspan = np.array ( [ 0.0, 2.0 ] )
  y0 = 5.1765
  n = 100
  humps_rk1 ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 200
  predator_prey_rk1 ( tspan, y0, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'rk1_test():' )
  print ( '  Normal end of execution.' )
  return

def humps_deriv ( x, y ):

#*****************************************************************************80
#
## humps_deriv() evaluates the derivative of the humps function.
#
#  Discussion:
#
#    y = 1.0 / ( ( x - 0.3 )^2 + 0.01 ) \
#      + 1.0 / ( ( x - 0.9 )^2 + 0.04 ) \
#      - 6.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x[:], y[:]: the arguments.
#
#  Output:
#
#    real yp[:]: the value of the derivative at x.
#
  yp = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 )**2 + 0.01 )**2 \
       - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 )**2 + 0.04 )**2

  return yp

def humps_rk1 ( tspan, y0, n ):

#*****************************************************************************80
#
## humps_rk1() solves the humps ODE using rk1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real tspan[2]: the time span
#
#    real y0[2]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'humps_rk1():' )
  print ( '  Solve humps_ode() system using rk1().' )

  t, y = rk1 ( humps_deriv, tspan, y0, n )

  plt.clf ( )

  plt.plot ( t, y, 'r-', linewidth = 2 )

  a = tspan[0]
  b = tspan[1]
  if ( a <= 0.0 and 0.0 <= b ):
    plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y(T) --->' )
  plt.title ( 'humps rk1(): time plot' )

  filename = 'humps_rk1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def predator_prey_deriv ( t, y ):

#*****************************************************************************80
#
## predator_prey_deriv() evaluates the right hand side of the system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Input:
#
#    real T, the current time.
#
#    real Y[2], the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real DYDT[2], the right hand side of the ODE.
#
  import numpy as np

  r = y[0]
  f = y[1]

  drdt =    2.0 * r - 0.001 * r * f
  dfdt = - 10.0 * f + 0.002 * r * f

  dydt = np.array ( [ drdt, dfdt ] )

  return dydt

def predator_prey_rk1 ( tspan, y0, n ):

#*****************************************************************************80
#
## predator_prey_rk1() solves the predator prey ODE using rk1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real tspan[2]: the time span
#
#    real y0[2]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_rk1():' )
  print ( '  Solve predator_prey_ode() using rk1().' )

  t, y = rk1 ( predator_prey_deriv, tspan, y0, n )

  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator prey, rk1: phase' )

  filename = 'predator_prey_rk1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

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
  rk1_test ( )
  timestamp ( )

