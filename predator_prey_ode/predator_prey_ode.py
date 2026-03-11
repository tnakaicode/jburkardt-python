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

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  tfirst = tspan[0]
  tlast = tspan[1]
  dt = ( tlast - tfirst ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = tspan[0]
  y[0,:] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( dydt ( t[i], y[i,:] ) )

  return t, y

def midpoint ( f, tspan, y0, n ):

#*****************************************************************************80
#
## midpoint() uses the implicit midpoint method to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2021
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
  from scipy.optimize import fsolve
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

    to = t[i]
    yo = y[i,:]

    th = to + 0.5 * dt
    yh = yo + 0.5 * dt * f ( to, yo )
    yh = fsolve ( midpoint_residual, yh, args = ( f, to, yo, th ) )

    tp = to + dt
    yp = 2.0 * yh - yo

    t[i+1]   = tp
    y[i+1,:] = yp

  return t, y

def midpoint_residual ( yh, f, to, yo, th ):

#*****************************************************************************80
#
## midpoint_residual() evaluates the midpoint residual.
#
#  Discussion:
#
#    We are seeking a value YH defined by the implicit equation:
#
#      YH = YO + ( TH - TO ) * F ( TH, YH )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yh: the estimated solution value at the midpoint time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real th: the midpoint time.
#
#  Output:
#
#    real value: the midpoint residual.
#
  value = yh - yo - ( th - to ) * f ( th, yh );

  return value

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

def predator_prey_deriv ( t, y ):

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
#    real Y[2], the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real DYDT[2], the right hand side of the 2 ODE's.
#
  import numpy as np

  r = y[0]
  f = y[1]

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  drdt =   alpha * r - beta  * r * f
  dfdt = - gamma * f + delta * r * f

  dydt = np.array ( [ drdt, dfdt ] )

  return dydt

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

def predator_prey_ode_test ( ):

#*****************************************************************************80
#
## predator_prey_ode_test() tests predator_prey_ode().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'predator_prey_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve predator_prey_ode().' )

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta  = ', beta )
  print ( '    gamma = ', gamma )
  print ( '    delta = ', delta )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 200
  predator_prey_euler ( n )

  n = 200
  predator_prey_midpoint ( n )

  n = 200
  predator_prey_rk4 ( n )

  predator_prey_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'predator_prey_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def predator_prey_euler ( n ):

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
#    22 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_euler():\n' );
  print ( '  Solve predator_prey_ode() using euler().\n' );

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( predator_prey_deriv, tspan, y0, n )

  plt.plot ( y[:,0], y[:,1], 'ro', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator_prey_ode(): euler()' )
  filename = 'predator_prey_euler_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def predator_prey_midpoint ( n ):

#*****************************************************************************80
#
## predator_prey_midpoint() solves predator_prey_ode() using midpoint().
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
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_midpoint():\n' );
  print ( '  Solve predator_prey_ode() system using midpoint().\n' );

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, y = midpoint ( predator_prey_deriv, tspan, y0, n )

  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], 'ro', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator_prey_ode(): midpoint()' )
  filename = 'predator_prey_midpoint_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def predator_prey_rk4 ( n ):

#*****************************************************************************80
#
## predator_prey_rk4() solves predator_prey_ode() using rk4().
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
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_rk4:\n' );
  print ( '  Solve predator_prey_ode() using rk4().\n' );

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, y = rk4 ( predator_prey_deriv, tspan, y0, n )

  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], 'ro', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator_prey_ode() solved by rk4()' )
  filename = 'predator_prey_rk4_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

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

  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], 'ro', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator_prey_ode(): solve_ivp()' )
  filename = 'predator_prey_solve_ivp_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rk4 ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## rk4() approximates the solution to an ODE using the RK4 method.
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

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  tfirst = tspan[0]
  tlast = tspan[1]
  dt = ( tlast - tfirst ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = tspan[0]
  y[0,:] = y0

  for i in range ( 0, n ):

    f1 = dydt ( t[i],            y[i,:] )
    f2 = dydt ( t[i] + dt / 2.0, y[i,:] + dt * f1 / 2.0 )
    f3 = dydt ( t[i] + dt / 2.0, y[i,:] + dt * f2 / 2.0 )
    f4 = dydt ( t[i] + dt,       y[i,:] + dt * f3 )

    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( f1 + 2.0 * f2 + 2.0 * f3 + f4 ) / 6.0

  return t, y

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
  predator_prey_ode_test ( )
  timestamp ( )

