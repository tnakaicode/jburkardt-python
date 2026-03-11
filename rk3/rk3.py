#! /usr/bin/env python3
#
def rk3_test ( ):

#*****************************************************************************80
#
## rk3_test() tests rk3().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 May 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rk3_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rk3() for solving an ordinary differential equation.' )

  tspan = np.array ( [ 0.0, 2.0 ] )
  y0 = 5.1765
  n = 100
  rk3_humps_test ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 200
  rk3_predator_prey_test ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 1.0 ] )
  y0 = np.array ( [ 0.0 ] )
  n = 27
  rk3_stiff_test ( tspan, y0, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'rk3_test():' )
  print ( '  Normal end of execution.' )
  return

def rk3 ( f, tspan, y0, n ):

#*****************************************************************************80
#
## rk3() uses a Runge-Kutta order 3 explicit method to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real tspan[2]: the starting and ending times.
#
#    real y0[m]: the initial conditions. 
#
#    integer n: the number of steps.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the solution estimates.
#
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  t[0] = tspan[0];
  y[0,:] = y0

  for i in range ( 0, n ):

    k1 = dt * f ( t[i],            y[i,:] )
    k2 = dt * f ( t[i] + dt,       y[i,:] + k1 )
    k3 = dt * f ( t[i] + 0.5 * dt, y[i,:] + 0.25 * k1 + 0.25 * k2 )

    t[i+1] = t[i] + dt;
    y[i+1,:] = y[i,:] + ( k1 + k2 + 4.0 * k3 ) / 6.0

  return t, y

def rk3_humps_test ( tspan, y0, n ):

#*****************************************************************************80
#
## rk3_humps_test() solves humps_ode() using rk3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
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
  print ( 'rk3_humps_test():' )
  print ( '  Solve the humps_ode() using rk3().' )

  t, y = rk3 ( humps_deriv, tspan, y0, n )

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
  plt.title ( 'humps ODE solved by rk3()' )

  filename = 'rk3_humps.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def rk3_predator_prey_test ( tspan, y0, n ):

#*****************************************************************************80
#
## rk3_predator_prey_test(): solve predator_prey_ode() by rk3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
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
  print ( 'rk3_predator_prey_test():' )
  print ( '  Solve the predator_prey_ode() using rk3().' )

  t, y = rk3 ( predator_prey_deriv, tspan, y0, n )

  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator prey ode solved by rk3()' )

  filename = 'rk3_predator_prey.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def humps_deriv ( x, y ):

#*****************************************************************************80
#
## humps_deriv() evaluates the derivative of humps_ode().
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
#    07 May 2025
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

def predator_prey_deriv ( t, rf ):

#*****************************************************************************80
#
## predator_prey_deriv() evaluates the right hand side of predator_prey_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
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
#    real RF[2], the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real DRFDT[2], the right hand side of the 2 ODE's.
#
  import numpy as np

  r = rf[0]
  f = rf[1]

  drdt =    2.0 * r - 0.001 * r * f
  dfdt = - 10.0 * f + 0.002 * r * f

  drfdt = np.array ( [ drdt, dfdt ] )

  return drfdt

def rk3_stiff_test ( tspan, y0, n ):

#*****************************************************************************80
#
## rk3_stiff_test() uses rk3() on the stiff ODE.
#
#  Discussion:
#
#    fsolve() is used to solve the backward Euler equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TSPAN(2): the first and last times.
#
#    real Y0: the initial condition.
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rk3_stiff_test():' )
  print ( '  Use rk3() to solve the stiff ODE.' )

  t1, y1 = rk3 ( stiff_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'ro-', linewidth = 3 )
  plt.plot ( t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff ode with rk3(): time plot' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  filename = 'rk3_stiff.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_deriv ( t, y ):

#*****************************************************************************80
#
## stiff_deriv() evaluates the right hand side of the stiff equation.
#
#  Discussion:
#
#    y' = 50 * ( cos(t) - y )
#    y(0) = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y: the time and solution value.
#
#  Output:
#
#    real DYDT: the derivative value.
#
  import numpy as np

  dydt = 50.0 * ( np.cos ( t ) - y )

  return dydt

def stiff_exact ( t ):

#*****************************************************************************80
#
## stiff_exact() evaluates the exact solution of the stiff equation.
#
#  Discussion:
#
#    y' = 50 * ( cos(t) - y )
#    y(0) = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the evaluation times.
#
#  Output:
#
#    real Y(:): the exact solution values.
#
  import numpy as np

  value = 50.0 * ( np.sin ( t ) + 50.0 * np.cos(t) \
    - 50.0 * np.exp ( - 50.0 * t ) ) / 2501.0

  return value

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
  rk3_test ( )
  timestamp ( )
 
