#! /usr/bin/env python3
#
def sir_conserved ( y ):

#*****************************************************************************80
#
## sir_conserved() returns a conserved quantity for sir_ode().
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
#    real Y(:,3): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  import numpy as np

  h = np.sum ( y, axis = 0 )

  return h

def sir_deriv ( t, y ):

#*****************************************************************************80
#
## sir_deriv() evaluates the right hand side of sir_ode().
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
#    real T: the time.
#
#    real y(3), the susceptible, infected, and recovered populations.
#
#  Output:
#
#    real dydt(3), the values of dSdt, dIdt, dRdt.
#
  import numpy as np

  alpha, beta, gamma, t0, y0, tstop = sir_parameters ( )

  S = y[0]
  I = y[1]
  R = y[2]

  N = S + I + R
  dSdt = - alpha * S * I / N            + gamma * R
  dIdt =   alpha * S * I / N - beta * I
  dRdt =                       beta * I - gamma * R

  dydt = np.array ( [ dSdt, dIdt, dRdt ] )

  return dydt

def sir_solve_ivp ( ):

#*****************************************************************************80
#
## sir_solve_ivp() solves sir_ode() using solve_ivp().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sir_solve_ivp():' )
  print ( '  Solve sir_ode() using solve_ivp().' )

  alpha, beta, gamma, t0, y0, tstop = sir_parameters ( )
#
#  Compute the approximate solution.
#
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( tspan[0], tspan[1], 101 )

  sol = solve_ivp ( sir_deriv, tspan, y0, t_eval = t )
#
#  Plot S(t), I(t), R(t).
#
  plt.plot ( t, sol.y[0], 'g', linewidth = 3 )
  plt.plot ( t, sol.y[1], 'r', linewidth = 3 )
  plt.plot ( t, sol.y[2], 'b', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Cases -->' )
  plt.legend ( ( 'Susceptible', 'Infected', 'Recovered' ) )
  s = ( 'sir_ode() solve_ivp: alpha = %g, beta = %g, gamma = %g' \
    % ( alpha, beta, gamma ) )
  plt.title ( s )
  filename = 'sir_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot N(t) = S(t) + I(t) + R(t).
#
  h = sir_conserved ( sol.y )

  plt.plot ( t, h, 'c-', linewidth = 3 )
  plt.plot ( [ t0, tstop ], [ 0.0, 0.0 ], 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- N(t) -->' )
  s = ( 'sir_ode() solve_ivp: alpha = %g, beta = %g, gamma = %g' \
    % ( alpha, beta, gamma ) )
  plt.title ( s )
  filename = 'sir_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def sir_ode_test ( ):

#*****************************************************************************80
#
## sir_ode_test() tests sir_ode().
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
  print ( 'sir_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve sir_ode().' )

  alpha, beta, gamma, t0, y0, tstop = sir_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta  = ', beta )
  print ( '    gamma = ', gamma )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  sir_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sir_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def sir_parameters ( alpha_user = None, beta_user = None, \
  gamma_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## sir_parameters() returns parameters for sir_ode().
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
#    02 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA_USER: the parameter.
#
#    real BETA_USER: the parameter.
#
#    real GAMMA_USER: the parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[3]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ALPHA: the parameter.
#
#    real BETA: the parameter.
#
#    real GAMMA: the parameter.
#
#    real T0: the initial time.
#
#    real Y0[3]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( sir_parameters, "alpha_default" ):
    sir_parameters.alpha_default = 0.0075

  if not hasattr ( sir_parameters, "beta_default" ):
    sir_parameters.beta_default = 0.0050

  if not hasattr ( sir_parameters, "gamma_default" ):
    sir_parameters.gamma_default = 0.0010

  if not hasattr ( sir_parameters, "t0_default" ):
    sir_parameters.t0_default = 0.0

  if not hasattr ( sir_parameters, "y0_default" ):
    sir_parameters.y0_default = np.array ( [ 99.0, 1.0, 0.0 ] )

  if not hasattr ( sir_parameters, "tstop_default" ):
    sir_parameters.tstop_default = 5000.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    sir_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    sir_parameters.beta_default = beta_user

  if ( gamma_user is not None ):
    sir_parameters.gamma_default = gamma_user

  if ( t0_user is not None ):
    sir_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    sir_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    sir_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = sir_parameters.alpha_default
  beta = sir_parameters.beta_default
  gamma = sir_parameters.gamma_default
  t0 = sir_parameters.t0_default
  y0 = sir_parameters.y0_default
  tstop = sir_parameters.tstop_default
  
  return alpha, beta, gamma, t0, y0, tstop

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
  sir_ode_test ( )
  timestamp ( )

