#! /usr/bin/env python3
#
def pendulum_elastic_conserved ( y ):

#*****************************************************************************80
#
## pendulum_elastic_conserved(): conserved quantity for pendulum_elastic_ode().
#
#  Discussion:
#
#    In the formula for energy, the reference ambiguously writes
#    ... ( nu + m g / k l )...  which must be ( nu + m g / k / l )!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul D Williams,
#    The RAW Filter: An Improvement to the Robert–Asselin Filter 
#    in Semi-Implicit Integrations,
#    Monthly Weather Review,
#    Volume 139, pages 1996-2007, June 2011.
#
#  Input:
#
#    real Y(:,4): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  import numpy as np

  g, k, l, m, t0, y0, tstop = pendulum_elastic_parameters ( )

  th = y[0]
  thdot = y[1]
  nu = y[2]
  nudot = y[3]

  h = 0.5 * m * l**2 * ( nudot**2 + ( 1.0 + nu )**2 * thdot**2 ) \
    - m * g * l * ( 1.0 + nu ) * np.cos ( th ) \
    + 0.5 * k * l**2 * ( nu + m * g / k / l )**2 \
    + m * g * l \
    - 0.5 * k * ( y0[2] * l )**2

  return h

def pendulum_elastic_deriv ( t, y ):

#*****************************************************************************80
#
## pendulum_elastic_deriv(): right hand side of pendulum_elastic_ode().
#
#  Discussion:
#
#    Y1 is the angular displacement
#    Y2 is the angular velocity
#    Y3 is the strain
#    Y4 is the time derivative of strain
#
#    G is the gravitational coefficient.
#    K is the spring constant
#    L is the length of the pendulum
#    M is the mass
#
#    y1' = y2
#    y2' = ?
#    y3' = y4
#    y4' = ?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul D Williams,
#    The RAW Filter: An Improvement to the Robert–Asselin Filter 
#    in Semi-Implicit Integrations,
#    Monthly Weather Review,
#    Volume 139, pages 1996-2007, June 2011.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(4,1), the current state values.
#
#  Output:
#
#    real DYDT(4,1), the time derivatives of the current state values.
#
  import numpy as np

  g, k, l, m, t0, y0, tstop = pendulum_elastic_parameters ( )

  wlo = np.sqrt ( g / l )
  whi = np.sqrt ( k / m )

  th = y[0]
  thdot = y[1]
  nu = y[2]
  nudot = y[3]

  dydt = np.array ( [ \
    thdot, \
    ( - wlo**2 * np.sin ( th ) - 2.0 * thdot * nudot ) / ( 1.0 + nu ), \
    nudot, \
    - wlo**2 * ( 1.0 - np.cos ( th ) ) - whi**2 * nu + ( 1.0 + nu ) * thdot**2 ] )

  return dydt

def pendulum_elastic_ode_test ( ):

#*****************************************************************************80
#
## pendulum_elastic_ode_test() tests pendulum_elastic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pendulum_elastic_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve pendulum_elastic_ode().' )

  g, k, l, m, t0, y0, tstop = pendulum_elastic_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    g     = ', g )
  print ( '    k     = ', k )
  print ( '    l     = ', l )
  print ( '    m     = ', m )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  pendulum_elastic_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pendulum_elastic_ode_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def pendulum_elastic_parameters ( g_user = None, k_user = None, l_user = None, \
  m_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## pendulum_elastic_parameters(): parameters for pendulum_elastic_ode().
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
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul D Williams,
#    The RAW Filter: An Improvement to the Robert–Asselin Filter 
#    in Semi-Implicit Integrations,
#    Monthly Weather Review,
#    Volume 139, pages 1996-2007, June 2011.
#
#  Input:
#
#    real G_USER: the gravitational constant, in meter / second**2
#
#    real K_USER: the spring constant, in Newton / meter 
#    = kilogram meter / second**2.
#
#    real L_USER: the pendulum length, in meters
#
#    real M_USER: the pendulum mass, in kilograms.
#
#    real T0_USER: the initial time, in seconds
#
#    real Y0_USER(4): the initial values, in radians, and radians per second,
#    units and units per second.
#
#    real TSTOP_USER: the final time, in seconds.
#
#  Output:
#
#    real G: the gravitational constant, in meter / second**2
#
#    real K: the spring constant, in Newton / meter = kilogram meter / second**2.
#
#    real L: the pendulum length, in meters
#
#    real M: the pendulum mass, in kilograms.
#
#    real T0: the initial time, in seconds
#
#    real Y0(4): the initial values, in radians, and radians per second,
#    units and units per second.
#
#    real TSTOP: the final time, in seconds.
#
  import numpy as np

  if not hasattr ( pendulum_elastic_parameters, "g_default" ):
    pendulum_elastic_parameters.g_default = 9.81

  if not hasattr ( pendulum_elastic_parameters, "k_default" ):
    pendulum_elastic_parameters.k_default = 100.0

  if not hasattr ( pendulum_elastic_parameters, "l_default" ):
    pendulum_elastic_parameters.l_default = 1.0

  if not hasattr ( pendulum_elastic_parameters, "m_default" ):
    pendulum_elastic_parameters.m_default = 0.1

  if not hasattr ( pendulum_elastic_parameters, "t0_default" ):
    pendulum_elastic_parameters.t0_default = 0.0

  if not hasattr ( pendulum_elastic_parameters, "y0_default" ):
    pendulum_elastic_parameters.y0_default = np.array ( [ 1.0, 0.0, 0.01, 0.0 ] )

  if not hasattr ( pendulum_elastic_parameters, "tstop_default" ):
    pendulum_elastic_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( g_user is not None ):
    pendulum_elastic_parameters.g_default = g_user

  if ( k_user is not None ):
    pendulum_elastic_parameters.k_default = k_user

  if ( l_user is not None ):
    pendulum_elastic_parameters.l_default = l_user

  if ( m_user is not None ):
    pendulum_elastic_parameters.m_default = m_user

  if ( t0_user is not None ):
    pendulum_elastic_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    pendulum_elastic_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    pendulum_elastic_parameters.tstop_default = tstop_user
#
#  Return values.
#
  g = pendulum_elastic_parameters.g_default
  k = pendulum_elastic_parameters.k_default
  l = pendulum_elastic_parameters.l_default
  m = pendulum_elastic_parameters.m_default
  t0 = pendulum_elastic_parameters.t0_default
  y0 = pendulum_elastic_parameters.y0_default
  tstop = pendulum_elastic_parameters.tstop_default

  return g, k, l, m, t0, y0, tstop

def pendulum_elastic_solve_ivp ( ):

#*****************************************************************************80
#
## pendulum_elastic_solve_ivp() tests pendulum_elastic_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pendulum_elastic_solve_ivp():' )
  print ( '  Use solve_ivp() to solve pendulum_elastic_ode().' )

  g, k, l, m, t0, y0, tstop = pendulum_elastic_parameters ( )

  f = pendulum_elastic_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 501 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot theta, dtheta/dt.
#
  plt.plot ( t, sol.y[0], 'r-', linewidth = 2 )
  plt.plot ( t, sol.y[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Theta, dTheta/dT -->' )
  plt.title ( 'pendulum_elastic_ode(): solve_ivp: angular deflection.' )
  plt.legend ( ( 'Theta', 'dTheta/dT' ) )
  filename = 'pendulum_elastic_solve_ivp_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Theta phase
#
  plt.plot ( sol.y[0], sol.y[1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Theta -->' )
  plt.ylabel ( '<-- ThetaDot -->' )
  plt.title ( 'pendulum_elastic_ode(): solve_ivp: theta phase.' )
  filename = 'pendulum_elastic_solve_ivp_theta_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot Nu, dNu/dT
#
  plt.plot ( t, sol.y[2], 'r-', linewidth = 2 )
  plt.plot ( t, sol.y[3], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Nu, dNu/dT -->' )
  plt.title ( 'pendulum_elastic_ode(): solve_ivp: relative strain.' )
  plt.legend ( ( 'Nu', 'dNu/dT' ) )
  filename = 'pendulum_elastic_solve_ivp_nu.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Nu phase
#
  plt.plot ( sol.y[2], sol.y[3], 'r-', linewidth = 1 )
  plt.grid ( True )
  plt.xlabel ( '<-- Nu -->' )
  plt.ylabel ( '<-- NuDot -->' )
  plt.title ( 'pendulum_elastic_ode(): solve_ivp: nu phase.' )
  filename = 'pendulum_elastic_solve_ivp_nu_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = pendulum_elastic_conserved ( sol.y )

  plt.plot ( t, h, 'r-', 'linewidth', 3 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'pendulum_elastic_ode(): solve_ivp: energy' )
  filename = 'pendulum_elastic_solve_ivp_energy.png'
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
  pendulum_elastic_ode_test ( )
  timestamp ( )

