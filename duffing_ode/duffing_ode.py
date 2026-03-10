#! /usr/bin/env python3
#
def duffing_deriv ( t, y ):

#*****************************************************************************80
#
## duffing_deriv() evaluates the right hand side of duffing_ode().
#
#  Discussion:
#
#    x'' + delta x' + alpha x + beta x^3 = gamma * cos ( omega * t )
#
#    y1' = y2
#    y2' = - delta y2 - alpha y1 - beta y1^3 + gamma * cos ( omega * t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y[2]: the time and solution value.
#
#  Output:
#
#    real DYDT[2]: the derivative value.
#
  import numpy as np

  alpha, beta, gamma, delta, omega, t0, y0, tstop = duffing_parameters ( )

  y1 = y[0]
  y2 = y[1]

  dy1dt = y2
  dy2dt = - delta * y2 - alpha * y1 - beta * y1**3 + gamma * np.cos ( omega * t )

  dydt = np.array ( [ dy1dt, dy2dt ] )

  return dydt

def duffing_solve_ivp ( ):

#*****************************************************************************80
#
## duffing_solve_ivp() uses solve_ivp() to solve duffing_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'duffing_solve_ivp():' )
  print ( '  Use solve_ivp() to solve duffing_ode().' )

  alpha, beta, gamma, delta, omega, t0, y0, tstop = duffing_parameters ( )

  f = duffing_deriv
  tspan = np.array ( [ t0, tstop ] )
#
#  Need more steps to get a clear phase plot.
#
  n = 1001
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot T, Y1.
#
  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y1(t) -->' )
  plt.title ( 'duffing_ode(): solve_ivp : y1' )
  filename = 'duffing_solve_ivp_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot T, Y2.
#
  plt.plot ( t, sol.y[1], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y2(t) -->' )
  plt.title ( 'duffing_ode(): solve_ivp: y2' )
  filename = 'duffing_solve_ivp_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot Y1, Y2.
#
  plt.plot ( sol.y[0], sol.y[1], 'c-', linewidth = 1 )
  plt.grid ( True )
  plt.xlabel ( '<-- y1(t) -->' )
  plt.ylabel ( '<-- y2(t) -->' )
  plt.title ( 'duffing_ode(): solve_ivp: phase' )
  filename = 'duffing_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def duffing_ode_test ( ):

#*****************************************************************************80
#
## duffing_ode_test() solves duffing_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'duffing_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve duffing_ode().' )

  alpha, beta, gamma, delta, omega, t0, y0, tstop = duffing_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta  = ', beta )
  print ( '    gamma = ', gamma )
  print ( '    delta = ', delta )
  print ( '    omega = ', omega )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  duffing_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'duffing_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def duffing_parameters ( alpha_user = None, beta_user = None, \
  gamma_user = None, delta_user = None, omega_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## duffing_parameters() returns parameters for duffing_ode().
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#    x'' + delta x' + alpha x + beta x^3 = gamma * cos ( omega * t )
#
#    y1' = y2
#    y2' = - delta y2 - alpha y1 - beta y1^3 + gamma * cos ( omega * t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA_USER, BETA_USER, GAMMA_USER, DELTA_USER, OMEGA_USER: 
#    the coefficients.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[2]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ALPHA, BETA, GAMMA, DELTA, OMEGA: the coefficients.
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
  if not hasattr ( duffing_parameters, "alpha_default" ):
    duffing_parameters.alpha_default = 1.0

  if not hasattr ( duffing_parameters, "beta_default" ):
    duffing_parameters.beta_default = 5.0

  if not hasattr ( duffing_parameters, "gamma_default" ):
    duffing_parameters.gamma_default = 8.0

  if not hasattr ( duffing_parameters, "delta_default" ):
    duffing_parameters.delta_default = 0.02

  if not hasattr ( duffing_parameters, "omega_default" ):
    duffing_parameters.omega_default = 0.5

  if not hasattr ( duffing_parameters, "t0_default" ):
    duffing_parameters.t0_default = 0.0

  if not hasattr ( duffing_parameters, "y0_default" ):
    duffing_parameters.y0_default = np.array ( [ 1.0, 0.0 ] )

  if not hasattr ( duffing_parameters, "tstop_default" ):
    duffing_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    duffing_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    duffing_parameters.beta_default = beta_user

  if ( gamma_user is not None ):
    duffing_parameters.gamma_default = gamma_user

  if ( delta_user is not None ):
    duffing_parameters.delta_default = delta_user

  if ( omega_user is not None ):
    duffing_parameters.omega_default = omega_user

  if ( t0_user is not None ):
    duffing_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    duffing_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    duffing_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = duffing_parameters.alpha_default
  beta = duffing_parameters.beta_default
  gamma = duffing_parameters.gamma_default
  delta = duffing_parameters.delta_default
  omega = duffing_parameters.omega_default
  t0 = duffing_parameters.t0_default
  y0 = duffing_parameters.y0_default
  tstop = duffing_parameters.tstop_default

  return alpha, beta, gamma, delta, omega, t0, y0, tstop

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
  duffing_ode_test ( )
  timestamp ( )

