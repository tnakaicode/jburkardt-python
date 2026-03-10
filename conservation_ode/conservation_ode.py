#! /usr/bin/env python3
#
def conservation_ode_test ( ):

#*****************************************************************************80
#
## conservation_ode_test() tests conservation_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( 'conservation_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  conservation_ode() reports on the accuracy of an ODE solver' )
  print ( '  by monitoring the value of a quantity that should be conserved.' )

  pendulum_solve_ivp ( )
  predator_prey_euler ( )
  predator_prey_solve_ivp ( )
  rigid_body_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'conservation_ode_test():' )
  print ( '  Normal end of execution.' )

  return

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
  t[0] = t0
  y[0,:] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( dydt ( t[i], y[i,:] ) )

  return t, y

def pendulum_conserved ( y ):

#*****************************************************************************80
#
## pendulum_conserved() returns a conserved quantity for pendulum_ode().
#
#  Discussion:
#
#    This conserved quantity can be regarded as the total energy of
#    the system.
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

  u = y[0]
  v = y[1]

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
#    31 October 2020
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
#    v' = - sqrt ( g / l ) * u
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
#    31 October 2020
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

  y = np.array ( [ u, v ] )

  return y

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
    pendulum_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    pendulum_parameters.tstop_default = tstop_user
#
#  Return values.
#
  g = pendulum_parameters.g_default
  l = pendulum_parameters.l_default
  m = pendulum_parameters.m_default
  t0 = pendulum_parameters.t0_default
  y0 = pendulum_parameters.y0_default
  tstop = pendulum_parameters.tstop_default
  
  return g, l, m, t0, y0, tstop

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
  plt.plot ( t, sol.y[0], 'ro', \
             t, ye[0], 'b-', linewidth = 2 )
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
  plt.plot ( t, sol.y[1], 'ro', \
             t, ye[1], 'b-', linewidth = 2 )
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
  h = pendulum_conserved ( sol.y )

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

def predator_prey_conserved ( rf ):

#*****************************************************************************80
#
## predator_prey_conserved() evaluates a conserved quantity of predator_prey_ode().
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
#    real RF[N,2]: the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real H[N]: the value of the conserved quantity.
#
  import numpy as np

  r = rf[:,0]
  f = rf[:,1]

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  h = delta * r - gamma * np.log ( r ) + beta * f - alpha * np.log ( f )

  return h

def predator_prey_deriv ( t, rf ):

#*****************************************************************************80
#
## predator_prey_deriv() evaluates right hand side of predator_prey_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2020
#
#  Author:
#
#    John Burkardt
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

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  drdt =   alpha * r - beta  * r * f
  dfdt = - gamma * f + delta * r * f

  drfdt = np.array ( [ drdt, dfdt ] )

  return drfdt

def predator_prey_euler ( ):

#*****************************************************************************80
#
## predator_prey_euler() solves predator_prey_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2023
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_euler():\n' );
  print ( '  Solve predator_prey_ode() using euler().\n' );

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  n = 200

  t, y = euler ( predator_prey_deriv, tspan, y0, n )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator_prey_ode(): euler() phase plot' )
  filename = 'predator_prey_euler_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Conservation plot.
#
  h = predator_prey_conserved ( y )

  plt.clf ( )
  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( t, np.zeros ( t.size ), 'k--', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- h(t) --->' )
  plt.title ( 'predator_prey_ode(): euler() conservation plot' )
  filename = 'predator_prey_euler_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def predator_prey_parameters ( alpha_user = None, beta_user = None, \
  gamma_user = None, delta_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## predator_prey_parameters() returns parameter values for predator_prey_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA_USER: a parameter value.
#
#    real BETA_USER: a parameter value.
#
#    real GAMMA_USER: a parameter value.
#
#    real DELTA_USER: a parameter value.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[2]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ALPHA: a parameter value.
#
#    real BETA: a parameter value.
#
#    real GAMMA: a parameter value.
#
#    real DELTA: a parameter value.
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
  if not hasattr ( predator_prey_parameters, "alpha_default" ):
    predator_prey_parameters.alpha_default = 2.0

  if not hasattr ( predator_prey_parameters, "beta_default" ):
    predator_prey_parameters.beta_default = 0.001

  if not hasattr ( predator_prey_parameters, "gamma_default" ):
    predator_prey_parameters.gamma_default = 10.0

  if not hasattr ( predator_prey_parameters, "delta_default" ):
    predator_prey_parameters.delta_default = 0.002

  if not hasattr ( predator_prey_parameters, "t0_default" ):
    predator_prey_parameters.t0_default = 0.0

  if not hasattr ( predator_prey_parameters, "y0_default" ):
    predator_prey_parameters.y0_default = np.array ( [ 5000.0, 100.0 ] )

  if not hasattr ( predator_prey_parameters, "tstop_default" ):
    predator_prey_parameters.tstop_default = 5.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    predator_prey_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    predator_prey_parameters.beta_default = beta_user

  if ( gamma_user is not None ):
    predator_prey_parameters.gamma_default = gamma_user

  if ( delta_user is not None ):
    predator_prey_parameters.delta_default = delta_user

  if ( t0_user is not None ):
    predator_prey_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    predator_prey_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    predator_prey_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = predator_prey_parameters.alpha_default
  beta = predator_prey_parameters.beta_default
  gamma = predator_prey_parameters.gamma_default
  delta = predator_prey_parameters.delta_default
  t0 = predator_prey_parameters.t0_default
  y0 = predator_prey_parameters.y0_default
  tstop = predator_prey_parameters.tstop_default

  return alpha, beta, gamma, delta, t0, y0, tstop

def predator_prey_solve_ivp ( ):

#*****************************************************************************80
#
## predator_prey_solve_ivp() solves predator_prey_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2020
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_solve_ivp():\n' );
  print ( '  Solve predator_prey_ode() using solve_ivp().\n' );

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( predator_prey_deriv, tspan, y0, t_eval = t )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator_prey_ode(): solve_ivp() phase plot' )
  filename = 'predator_prey_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Conservation plot.
#
  h = predator_prey_conserved ( np.transpose ( sol.y ) )

  plt.clf ( )
  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( t, np.zeros ( t.size ), 'k--', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- h(t) --->' )
  plt.title ( 'predator_prey_ode(): solve_ivp() conservation plot' )
  filename = 'predator_prey_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rigid_body_conserved ( xyz ):

#*****************************************************************************80
#
## rigid_body_conserved() evaluates conserved quantities for rigid_body_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer,
#    Solving differential equations on manifolds,
#    Universite de Geneve,
#    June 2011.
#
#  Input:
#
#    real XYZ[:,3]: the current coordinates.
#
#  Output:
#
#    real H1[:], H2[]: the conserved quantities.
#
  import numpy as np

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  h1 = x**2 + y**2 + z**2

  h2 = x**2 / i1 + y**2 / i2 + z**2 / i3

  return h1, h2

def rigid_body_deriv ( t, xyz ):

#*****************************************************************************80
#
## rigid_body_deriv() evaluates the derivative of rigid_body_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer,
#    Solving differential equations on manifolds,
#    Universite de Geneve,
#    June 2011.
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric numerical integration,
#    Springer, 2006.
#
#  Input:
#
#    real T, XYZ[3]: the arguments of the derivative.
#
#  Output:
#
#    real DXYZDT[3]: the value of the derivative.
#
  import numpy as np

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = ( 1.0 / i3 - 1.0 / i2 ) * z * y
  dydt = ( 1.0 / i1 - 1.0 / i3 ) * x * z
  dzdt = ( 1.0 / i2 - 1.0 / i1 ) * y * x

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def rigid_body_parameters ( i1_user = None, i2_user = None, \
  i3_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## rigid_body_parameters() returns parameters for rigid_body_ode().
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
#    04 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real I1_USER: a moment of inertia.
#
#    real I2_USER: a moment of inertia.
#
#    real I3_USER: a moment of inertia.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real I1: a moment of inertia.
#
#    real I2: a moment of inertia.
#
#    real I3: a moment of inertia.
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
  if not hasattr ( rigid_body_parameters, "i1_default" ):
    rigid_body_parameters.i1_default = 1.0 / 6.0

  if not hasattr ( rigid_body_parameters, "i2_default" ):
    rigid_body_parameters.i2_default = 1.0

  if not hasattr ( rigid_body_parameters, "i3_default" ):
    rigid_body_parameters.i3_default = 2.0 / 3.0

  if not hasattr ( rigid_body_parameters, "t0_default" ):
    rigid_body_parameters.t0_default = 0.0

  if not hasattr ( rigid_body_parameters, "y0_default" ):
    y01 = np.cos ( 0.9 )
    y02 = 0.0
    y03 = np.sin ( 0.9 )
    rigid_body_parameters.y0_default = np.array ( [ y01, y02, y03 ] )

  if not hasattr ( rigid_body_parameters, "tstop_default" ):
    rigid_body_parameters.tstop_default = 50.0
#
#  Update defaults if input was supplied.
#
  if ( i1_user is not None ):
    rigid_body_parameters.i1_default = i1_user

  if ( i2_user is not None ):
    rigid_body_parameters.i2_default = i2_user

  if ( i3_user is not None ):
    rigid_body_parameters.i3_default = i3_user

  if ( t0_user is not None ):
    rigid_body_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    rigid_body_parameters.y0_default = y0_user.copy()

  if ( tstop_user is not None ):
    rigid_body_parameters.tstop_default = tstop_user
#
#  Return values.
#
  i1 = rigid_body_parameters.i1_default
  i2 = rigid_body_parameters.i2_default
  i3 = rigid_body_parameters.i3_default
  t0 = rigid_body_parameters.t0_default
  y0 = rigid_body_parameters.y0_default
  tstop = rigid_body_parameters.tstop_default
  
  return i1, i2, i3, t0, y0, tstop

def rigid_body_solve_ivp ( ):

#*****************************************************************************80
#
## rigid_body_solve_ivp() solves rigid_body_ode() with solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib as mpl
  from mpl_toolkits.mplot3d import Axes3D
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rigid_body_solve_ivp():' )
  print ( '  Solve rigid_body_ode() using solve_ivp().' )
  print ( '  rigid_body_ode() models motion on the surface of a sphere.' )

  i1, i2, i3, t0, y0, tstop = rigid_body_parameters ( )

  f = rigid_body_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  plt.plot ( t, sol.y[0], linewidth = 3 )
  plt.plot ( t, sol.y[1], linewidth = 3 )
  plt.plot ( t, sol.y[2], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- X,Y,Z -->' )
  plt.title ( 'rigid_body_ode(): solve ivp: (X(t),Y(t),Z(t))' )
  plt.legend ( ( 'X(t)', 'Y(t)', 'Z(t)' ) )
  filename = 'rigid_body_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  fig = plt.figure ( )
# ax = fig.gca ( projection = '3d' )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( sol.y[0], sol.y[1], sol.y[2], linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->' )
  ax.set_ylabel ( '<-- Y -->' )
  ax.set_zlabel ( '<-- Z -->' )
  ax.set_title ( 'rigid_body_ode(): solve ivp: (x,y,z)(t)'  )
  filename = 'rigid_body_solve_ivp_plot3d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h1, h2 = rigid_body_conserved ( sol.y )

  plt.plot ( t, h1, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h1[0],h1[0] ] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H1(T) -->' )
  plt.title ( 'rigid_body_ode(): solve ivp: H1(T)' )
  filename = 'rigid_body_solve_ivp_h1_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, h2, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h2[0],h2[0] ] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H2(T) -->' )
  plt.title ( 'rigid_body_ode(): solve ivp: H2(T)' )
  filename = 'rigid_body_solve_ivp_h2_conservation.png'
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
  conservation_ode_test ( )
  timestamp ( )

