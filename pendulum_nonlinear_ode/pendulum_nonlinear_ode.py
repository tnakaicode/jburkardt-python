#! /usr/bin/env python3
#
def pendulum_nonlinear_conserved ( y ):

#*****************************************************************************80
#
## pendulum_nonlinear_conserved(): conserved quantity for pendulum_nonlinear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2020
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

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  u = y[0]
  v = y[1]

  h = ( m * g / l ) * ( 1.0 - np.cos ( u ) ) + 0.5 * m * v**2

  return h

def pendulum_nonlinear_deriv ( t, y ):

#*****************************************************************************80
#
## pendulum_nonlinear_deriv(): right hand side of pendulum_nonlinear_ode().
#
#  Discussion:
#
#    Y1 is the angular displacement
#    Y2 is the angular velocity
#    L is the length of the pendulum (set to 1 here)
#    G is the gravitational coefficient (set to 9.8 here).
#
#    y1' = y2
#    y2' = - ( g / l ) * sin ( y1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2018
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
#    real DYDT(2), the time derivatives of the current state values.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - ( g / l ) * np.sin ( u )

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def pendulum_nonlinear_ode_test ( ):

#*****************************************************************************80
#
## pendulum_nonlinear_ode_test() tests pendulum_nonlinear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pendulum_nonlinear_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve pendulum_nonlinear_ode().' )

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    g =     ', g )
  print ( '    l =     ', l )
  print ( '    m =     ', m )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  pendulum_nonlinear_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pendulum_nonlinear_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def pendulum_nonlinear_solve_ivp ( ):

#*****************************************************************************80
#
## pendulum_nonlinear_solve_ivp() applies solve_ivp() to pendulum_nonlinear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  f = pendulum_nonlinear_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  yd = sol.y * 180.0 / np.pi
#
#  Plot theta, thetadot
#
  plt.plot ( t, yd[0], 'r-', linewidth = 2 )
  plt.plot ( t, yd[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Theta, ThetaDot (degrees) -->' )
  plt.title ( 'pendulum_nonlinear_ode(): Deflection.' )
  filename = 'pendulum_nonlinear_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = pendulum_nonlinear_conserved ( sol.y )

  plt.plot ( t, h, 'b-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'pendulum_nonlinear_ode(): energy' )
  filename = 'pendulum_nonlinear_energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def pendulum_nonlinear_parameters ( g_user = None, l_user = None, \
  m_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## pendulum_nonlinear_parameters() returns parameters for pendulum_nonlinear_ode().
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
#    real Y0_USER: the initial condition.
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
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( pendulum_nonlinear_parameters, "g_default" ):
    pendulum_nonlinear_parameters.g_default = 9.81

  if not hasattr ( pendulum_nonlinear_parameters, "l_default" ):
    pendulum_nonlinear_parameters.l_default = 1.0

  if not hasattr ( pendulum_nonlinear_parameters, "m_default" ):
    pendulum_nonlinear_parameters.m_default = 1.0

  if not hasattr ( pendulum_nonlinear_parameters, "t0_default" ):
    pendulum_nonlinear_parameters.t0_default = 0.0

  if not hasattr ( pendulum_nonlinear_parameters, "y0_default" ):
    u0 = 70.0 * np.pi / 180.0
    v0 = 0.0
    pendulum_nonlinear_parameters.y0_default = np.array ( [ u0, v0 ] )

  if not hasattr ( pendulum_nonlinear_parameters, "tstop_default" ):
    pendulum_nonlinear_parameters.tstop_default = 50.0
#
#  Update defaults if input was supplied.
#
  if ( g_user is not None ):
    pendulum_nonlinear_parameters.g_default = g_user

  if ( l_user is not None ):
    pendulum_nonlinear_parameters.l_default = l_user

  if ( m_user is not None ):
    pendulum_nonlinear_parameters.m_default = m_user

  if ( t0_user is not None ):
    pendulum_nonlinear_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    pendulum_nonlinear_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    pendulum_nonlinear_parameters.tstop_default = tstop_user
#
#  Return values.
#
  g = pendulum_nonlinear_parameters.g_default
  l = pendulum_nonlinear_parameters.l_default
  m = pendulum_nonlinear_parameters.m_default
  t0 = pendulum_nonlinear_parameters.t0_default
  y0 = pendulum_nonlinear_parameters.y0_default
  tstop = pendulum_nonlinear_parameters.tstop_default
  
  return g, l, m, t0, y0, tstop

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
  pendulum_nonlinear_ode_test ( )
  timestamp ( )

