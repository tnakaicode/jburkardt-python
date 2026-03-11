#! /usr/bin/env python3
#
def euler ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## euler() approximates the solution to an ODE using Euler's method.
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

  for i in range ( 0, n + 1 ):
    if ( i == 0 ):
      t[i]   = t0
      y[i,:] = y0
    else:
      t[i]   = t[i-1]   + dt
      y[i,:] = y[i-1,:] + dt * ( dydt ( t[i-1], y[i-1,:] ) )

  return t, y

def pendulum_conserved ( u, v ):

#*****************************************************************************80
#
## pendulum_conserved() returns a conserved quantity for pendulum_ode().
#
#  Discussion:
#
#    This conserved quantity can be regarded as the total energy of
#    the system.
#
#    To my bafflement, solve_ivp returns the solution as a 2xn array,
#    when any sensible person would expect an nx2 array.  To deal with
#    this annoying choice, I've had to require that the user split up
#    the solution into separate vectors u and v before calling this
#    function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(:,2): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  h = 0.5 * m * g * l * u**2 + 0.5 * m * v**2

  return h

def pendulum_deriv ( t, y ):

#*****************************************************************************80
#
## pendulum_deriv() returns the right hand side of pendulum_ode().
#
#  Discussion:
#
#    Y1 is the angular displacement
#    Y2 is the angular velocity
#
#    G is the gravitational coefficient.
#    L is the length of the pendulum.
#    M is the pendulum mass.
#
#    u' = v
#    v' = - ( g / l ) * u
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the current time.
#
#    real Y(2), the current state values.
#
#  Output:
#
#    real dydt(2), the time derivatives of the current state values.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - ( g / l ) * u

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def pendulum_euler ( n ):

#*****************************************************************************80
#
## pendulum_euler() solves pendulum_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pendulum_euler():' )
  print ( '  Solve pendulum_ode() using euler().' )

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  f = pendulum_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = euler ( f, tspan, y0, n )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = pendulum_exact ( t2 )
#
#  Plot u = theta.
#
  plt.plot ( t1, y1[:,0], 'ro', \
             t2, y2[:,0], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular deflection (radians) -->' )
  plt.title ( 'pendulum euler theta' )
  plt.legend ( ( 'euler', 'exact' ) )
  filename = 'pendulum_euler_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot v = thetadot.
#
  plt.plot ( t1, y1[:,1], 'ro', \
             t2, y2[:,1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular velocity (radians/sec) -->' )
  plt.title ( 'pendulum euler thetadot' )
  plt.legend ( ( 'euler', 'exact' ) )
  filename = 'pendulum_euler_thetadot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h1 = pendulum_conserved ( y1[:,0], y1[:,1] )

  plt.plot ( t1, h1, 'b-', linewidth = 2 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'pendulum euler: Energy' )
  filename = 'pendulum_euler_energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def pendulum_exact ( t ):

#*****************************************************************************80
#
## pendulum_exact() returns the exact solution for pendulum_ode().
#
#  Discussion:
#
#    This solution satisfies the pendulum ODE:
#
#    u' = v
#    v' = - ( g / l ) * u
#
#    u(t0) = u0 = y0(1)
#    v(t0) = v0 = y0(2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the current time.
#
#  Output:
#
#    real Y(2): the exact solution.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  p = np.sqrt ( g / l )

  u =               y0[0] * np.cos ( p * ( t - t0 ) ) \
    + ( 1.0 / p ) * y0[1] * np.sin ( p * ( t - t0 ) )

  v =       - p   * y0[0] * np.sin ( p * ( t - t0 ) ) \
    +               y0[1] * np.cos ( p * ( t - t0 ) )

  y = np.column_stack ( ( u, v ) )

  return y

def pendulum_ode_test ( ):

#*****************************************************************************80
#
## pendulum_ode_test() tests pendulum_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pendulum_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve pendulum_ode().' )

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  p = pendulum_period ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    gravity (m/s^2)   = ', g )
  print ( '    length (m)        = ', l )
  print ( '    mass (g)          = ', m )
  print ( '    t0 (s)            = ', t0 )
  print ( '    u0,v0 (rad,rad/s) = ', y0 )
  print ( '    tstop (s)         = ', tstop )
  print ( '    period (s)        = ', p )

  n = 1000
  pendulum_euler ( n )

  pendulum_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pendulum_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def pendulum_parameters ( g_user = None, l_user = None, \
  m_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## pendulum_parameters() returns parameters for pendulum_ode().
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real G_USER: the gravitational constant, in meters/second^2
#
#    real L_USER: the pendulum length in meters
#
#    real M_USER: the pendulum mass, in grams.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[2]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real G: the gravitational constant, in meters/second^2
#
#    real L: the pendulum length in meters
#
#    real M: the pendulum mass, in grams.
#
#    real T0: the initial time.
#
#    real Y0[2]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( pendulum_parameters, "g_default" ):
    pendulum_parameters.g_default = 9.81

  if not hasattr ( pendulum_parameters, "l_default" ):
    pendulum_parameters.l_default = 1.0

  if not hasattr ( pendulum_parameters, "m_default" ):
    pendulum_parameters.m_default = 1.0

  if not hasattr ( pendulum_parameters, "t0_default" ):
    pendulum_parameters.t0_default = 0.0

  if not hasattr ( pendulum_parameters, "y0_default" ):
    u0 = np.pi / 3.0
    v0 = 0.0
    pendulum_parameters.y0_default = np.array ( [ u0, v0 ] )

  if not hasattr ( pendulum_parameters, "tstop_default" ):
    pendulum_parameters.tstop_default = 20.0
#
#  Update defaults if input was supplied.
#
  if ( g_user is not None ):
    pendulum_parameters.g_default = g_user

  if ( l_user is not None ):
    pendulum_parameters.l_default = l_user

  if ( m_user is not None ):
    pendulum_parameters.m_default = m_user

  if ( t0_user is not None ):
    pendulum_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    pendulum_parameters.y0_default = y0_user.copy ( )

  if ( tstop_user is not None ):
    pendulum_parameters.tstop_default = tstop_user
#
#  Return values.
#
  g = pendulum_parameters.g_default
  l = pendulum_parameters.l_default
  m = pendulum_parameters.m_default
  t0 = pendulum_parameters.t0_default
  y0 = pendulum_parameters.y0_default.copy ( )
  tstop = pendulum_parameters.tstop_default
  
  return g, l, m, t0, y0, tstop

def pendulum_period ( ):

#*****************************************************************************80
#
## pendulum_period() returns the period for pendulum_ode().
#
#  Discussion:
#
#    The period is the smallest time interval P such that, for any T and X,
#      Y(T,X) = Y(T+P,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real P: the period of the pendulum.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  p = 2.0 * np.pi * np.sqrt ( l / g )

  return p

def pendulum_solve_ivp ( ):

#*****************************************************************************80
#
## pendulum_solve_ivp() solves pendulum_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pendulum_solve_ivp():' )
  print ( '  Solve pendulum_ode() using solve_ivp().' )

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  f = pendulum_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  ye = pendulum_exact ( t )
#
#  Plot u = theta.
#
  plt.plot ( t, sol.y[0,:], 'ro', \
             t, ye[:,0], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular deflection (radians) -->' )
  plt.title ( 'pendulum_ode(): theta: solve_ivp' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'pendulum_solve_ivp_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot v = thetadot.
#
  plt.plot ( t, sol.y[1,:], 'ro', \
             t, ye[:,1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular velocity (radians/sec) -->' )
  plt.title ( 'pendulum_ode(): thetadot: solve_ivp' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'pendulum_solve_ivp_thetadot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = pendulum_conserved ( sol.y[0,:], sol.y[1,:] )

  plt.plot ( t, h, 'b-', linewidth = 2 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'pendulum_ode(): Energy' )
  filename = 'pendulum_solve_ivp_energy.png'
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
  pendulum_ode_test ( )
  timestamp ( )

