#! /usr/bin/env python3
#
def predator_prey_conserved ( y ):

#*****************************************************************************80
#
## predator_prey_conserved() evaluates a conserved quantity.
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
#    real Y[2]: the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real H: the value of the conserved quantity.
#
  import numpy as np

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  y_equi = predator_prey_equilibrium ( )
  h_equi = delta * y_equi[0] - gamma * np.log ( y_equi[0] ) \
    + beta * y_equi[1] - alpha * np.log ( y_equi[1] )

  r = y[0]
  f = y[1]

  h = delta * r - gamma * np.log ( r ) + beta * f - alpha * np.log ( f ) \
    - h_equi;

  return h

def predator_prey_deriv ( t, rf ):

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

def predator_prey_equilibrium ( ):

#*****************************************************************************80
#
## predator_prey_equilibrium() returns the predator prey equilibrium solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real Y_EQUI[2]: the equilibrium solution.
#
  import numpy as np

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  y_equi = np.array ( [ gamma/delta, alpha/beta ] )

  return y_equi

def predator_prey_events ( t, y ):

#*****************************************************************************80
#
## predator_prey_events() defines an event as the initial value for the first component.
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
#  Reference:
#
#    John D Cook,
#    Calculating the period of Van der Pol Oscillators,
#    https://www.johndcook.com/blog/2019/12/26/van-der-pol-period/
#    26 December 2019.
#
#  Input:
#
#    real T, Y[*]: a time and ODE solution.
#
#  Output:
#
#    real EVENT: a quantity which is zero if an "event" has occurred.
#
  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  return y[0] - y0[0]

def predator_prey_parameters ( alpha_user = None, beta_user = None, \
  gamma_user = None, delta_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## predator_prey_parameters() returns parameter values.
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

def predator_prey_ode_period_test ( ):

#*****************************************************************************80
#
## predator_prey_ode_period_test() tests predator_prey_ode.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'predator_prey_ode_period_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve the predator prey ODE and estimate the period.' )
#
#  Restore the default parameters.
#
  alpha = 2.0
  beta = 0.001
  gamma = 10.0
  delta = 0.002
  t0 = 0.0
  y0 = np.array ( [ 5000, 100 ] )
  tstop = 10.0
  predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Vary alpha.
#
  print ( )
  print ( '      ALPHA       Beta      Gamma      Delta    NP       Pobs     Predic      Tstop          H' )
  print ( )

  for alpha in [ 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0 ]:
#
#  Update the parameters.
#
    predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Estimate the period, so we can set TSTOP to at least 5 periods.
#
    p_nonlinear = predator_prey_period ( )
#
#  Get energy H.
#
    h = predator_prey_conserved ( y0 )
#
#  Solve the ODE.
#
    p, nperiods = predator_prey_solve_ivp ( )

    print ( alpha, beta, gamma, delta, nperiods, p, p_nonlinear, tstop, h )
#
#  Restore the default parameters.
#
  alpha = 2.0
  beta = 0.001
  gamma = 10.0
  delta = 0.002
  t0 = 0.0
  y0 = np.array ( [ 5000, 100 ] )
  tstop = 10.0
  predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Vary beta.
#
  print ( )
  print ( '      Alpha       BETA      Gamma      Delta    NP       Pobs     Predic      Tstop          H' )
  print ( )

  for beta in [ 0.0005, 0.001, 0.002, 0.005 ]:
#
#  Update the parameters.
#
    predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Estimate the period, so we can set TSTOP to at least 5 periods.
#
    p_nonlinear = predator_prey_period ( )
#
#  Get energy H.
#
    h = predator_prey_conserved ( y0 )
#
#  Solve the ODE.
#
    p, nperiods = predator_prey_solve_ivp ( )

    print ( alpha, beta, gamma, delta, nperiods, p, p_nonlinear, tstop, h )
#
#  Restore the default parameters.
#
  alpha = 2.0
  beta = 0.001
  gamma = 10.0
  delta = 0.002
  t0 = 0.0
  y0 = np.array ( [ 5000, 100 ] )
  tstop = 10.0
  predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Vary gamma.
#
  print ( )
  print ( '      Alpha       Beta      GAMMA      Delta    NP       Pobs     Predic      Tstop          H' )
  print ( )

  for gamma in [ 5.0, 7.5, 10.0, 15.0 ]:
#
#  Update the parameters.
#
    predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Estimate the period, so we can set TSTOP to at least 5 periods.
#
    p_nonlinear = predator_prey_period ( )
#
#  Get energy H.
#
    h = predator_prey_conserved ( y0 )
#
#  Solve the ODE.
#
    p, nperiods = predator_prey_solve_ivp ( )

    print ( alpha, beta, gamma, delta, nperiods, p, p_nonlinear, tstop, h )
#
#  Restore the default parameters.
#
  alpha = 2.0
  beta = 0.001
  gamma = 10.0
  delta = 0.002
  t0 = 0.0
  y0 = np.array ( [ 5000, 100 ] )
  tstop = 10.0
  predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Vary delta.
#
  print ( )
  print ( '      Alpha       Beta      Gamma      DELTA    NP       Pobs     Predic      Tstop          H' )
  print ( )

  for delta in [ 0.001, 0.002, 0.003, 0.004, 0.005 ]:
#
#  Update the parameters.
#
    predator_prey_parameters ( alpha, beta, gamma, delta, t0, y0, tstop )
#
#  Estimate the period, so we can set TSTOP to at least 5 periods.
#
    p_nonlinear = predator_prey_period ( )
#
#  Get energy H.
#
    h = predator_prey_conserved ( y0 )
#
#  Solve the ODE.
#
    p, nperiods = predator_prey_solve_ivp ( )

    print ( alpha, beta, gamma, delta, nperiods, p, p_nonlinear, tstop, h )
#
#  Terminate.
#
  print ( '' )
  print ( 'predator_prey_ode_period_test():' )
  print ( '  Normal end of execution.' )
  return

def predator_prey_period ( ):

#*****************************************************************************80
#
## predator_prey_period() computes the period of the predator prey limit cycle.
#
#  Discussion:
#
#    The period estimate of Shagi-Di Shi is based on the full nonlinear equation.
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
#  Reference:
#
#    Shagi-Di Shih,
#    The period of a Lotka-Volterra System,
#    Taiwanese Journal of Mathematics,
#    Volume 1, Number 4, December 1997, pages 451-470.
#
#  Output:
#
#    real P: the estimated period.
#
  from scipy.integrate import quad
#
#  Get the system parameters.
#
  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )
#
#  Rename two parameters to accord with his notation.
#
  a = alpha
  d = gamma
#
#  Compute the energy.
#
  E = predator_prey_conserved ( y0 )
#
#  The period is defined as an integral.
#
  p, err = quad ( lambda s : predator_prey_period_integrand ( s, E, a, d ), \
    0.0, E )

  p = p / a / d

  return p

def predator_prey_period_integrand ( s, E, a, d ):

#*****************************************************************************80
#
## predator_prey_period_integrand() is the integrand for the period integral.
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
#  Reference:
#
#    Shagi-Di Shih,
#    The period of a Lotka-Volterra System,
#    Taiwanese Journal of Mathematics,
#    Volume 1, Number 4, December 1997, pages 451-470.
#
#  Input:
#
#    real S: the independent variable.
#
#    real E: the energy.
#
#    real A, D: two parameter values.
#
#  Output:
#
#    real VALUE: the value of the integrand at S.
#
  value = predator_prey_period_phi ( s / d ) \
    * predator_prey_period_phi ( ( E - s ) / a )

  return value

def predator_prey_period_phi ( s ):

#*****************************************************************************80
#
## predator_prey_period_phi() evaluates the phi(s) function.
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
#  Reference:
#
#    Shagi-Di Shih,
#    The period of a Lotka-Volterra System,
#    Taiwanese Journal of Mathematics,
#    Volume 1, Number 4, December 1997, pages 451-470.
#
#  Input:
#
#    real S: the independent variable.
#
#  Output:
#
#    real VALUE: the value of phi(s).
#
  from scipy.special import lambertw
  import numpy as np

  d1 = 1.0 + lambertw ( - np.exp ( - 1.0 - s ), 0 )
  d1 = d1.real
  d2 = 1.0 + lambertw ( - np.exp ( - 1.0 - s ), -1 )
  d2 = d2.real
  value = 1.0 / d1 - 1.0 / d2

  return value

def predator_prey_period_linear ( ):

#*****************************************************************************80
#
## predator_prey_period_linear() estimate period of predator prey limit cycle.
#
#  Discussion:
#
#    The period estimate of Lotka is based on the linear terms only.
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
#  Reference:
#
#    Alfred Lotka,
#    Undamped oscillations derived from the law of mass action,
#    Journal of the American Chemical Society,
#    Volume 42, 1920, pages 1595-1599.
#
#  Output:
#
#    real P: the estimated period.
#
  import numpy as np

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  p = 2.0 * np.pi / np.sqrt ( alpha * gamma )

  return p

def predator_prey_solve_ivp ( ):

#*****************************************************************************80
#
## predator_prey_solve_ivp() solves the predator prey ODE using solve_ivp().
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
  import numpy as np
#
#  Get parameter values.
#
  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )
#
#  Solve the system.
#
  dydt = predator_prey_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( dydt, tspan, y0, t_eval = t, events = predator_prey_events )
#
#  Estimate the period.
#
  zeros = sol.t_events[0]
  nz = len ( zeros )
  if ( nz < 3 ):
    p = np.NaN
    nperiods = np.NaN
  else:
    p = zeros[nz-1] - zeros[nz-3]
    nperiods = np.floor ( nz / 2 )

  return p, nperiods

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
  predator_prey_ode_period_test ( )
  timestamp ( )

