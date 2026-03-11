#! /usr/bin/env python3
#
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

def vanderpol_deriv ( t, y ):

#*****************************************************************************80
#
## vanderpol_deriv() returns the right hand side of the vanderpol ODE.
#
#  Discussion:
#
#    The parameter MU is defined by the function vanderpol_mu()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(2), the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2), the value of the derivative.
#
  import numpy as np

  mu, t0, y0, tstop = vanderpol_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = mu * ( 1.0 - u**2 ) * v - u

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def vanderpol_events ( t, y ):

#*****************************************************************************80
#
## vanderpol_events() defines an event as a zero value for the first component.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 November 2020
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
  return y[0]

def vanderpol_ode_period_test ( ):

#*****************************************************************************80
#
## vanderpol_ode_period_test() solves the van der Pol ODE.
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'vanderpol_ode_period_test:' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve the van der Pol oscillator ODE, and estimate' )
  print ( '  the period of the limit cycle.' )
#
#  Get default parameter values.
#
  [ mu, t0, y0, tstop ] = vanderpol_parameters ( )
#
#  Reset mu.
#
  print ( "" )
  print ( "        Mu     Periods     P(obs)    P(predicted)     TStop" )
  print ( "" )

  for mu in [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 100.0, 1000.0 ]:
#
#  Estimate the period, so we can set TSTOP to at least 5 periods.
#
    p_predict = vanderpol_period ( mu )
    tstop = max ( 100.0, 5.0 * p_predict )
#
#  Update MU and TSTOP.
#
    vanderpol_parameters ( mu, t0, y0, tstop )
#
#  Solve the ODE.
#
    p, nperiods = vanderpol_solve_ivp ( )

    print ( mu, nperiods, p, p_predict, tstop )
#
#  Terminate.
#
  print ( '' )
  print ( 'vanderpol_ode_period_test():' )
  print ( '  Normal end of execution.' )
  return

def vanderpol_parameters ( mu_user = None, t0_user = None, y0_user = None,
  tstop_user = None ):

#*****************************************************************************80
#
## vanderpol_parameters() returns the parameters of the vanderpol ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 December 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real mu_user: the parameter.
#
#    real t0_user: the initial time.
#
#    real y0_user[2]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real mu: the parameter.
#
#    real t0: the initial time.
#
#    real y0(2): the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( vanderpol_parameters, "mu_default" ):
    vanderpol_parameters.mu_default = 2.0

  if not hasattr ( vanderpol_parameters, "t0_default" ):
    vanderpol_parameters.t0_default = 0.0

  if not hasattr ( vanderpol_parameters, "y0_default" ):
    vanderpol_parameters.y0_default = np.array ( [ 1.0, 0.0 ] )

  if not hasattr ( vanderpol_parameters, "tstop_default" ):
    vanderpol_parameters.tstop_default = 40.0
#
#  Update defaults if input was supplied.
#
  if ( mu_user is not None ):
    vanderpol_parameters.mu_default = mu_user

  if ( t0_user is not None ):
    vanderpol_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    vanderpol_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    vanderpol_parameters.tstop_default = tstop_user
#
#  Return values.
#
  mu = vanderpol_parameters.mu_default
  t0 = vanderpol_parameters.t0_default
  y0 = vanderpol_parameters.y0_default
  tstop = vanderpol_parameters.tstop_default

  return mu, t0, y0, tstop

def vanderpol_period ( mu ):

#*****************************************************************************80
#
## vanderpol_period() estimates the period of the vanderpol limit cycle.
#
#  Discussion:
#
#    Five approximations are available for the period.  These estimates
#    seen to disagree for low values of mu.  The formula of Urabe
#    is evaluated here.
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
#    Mary Cartwright,
#    Van der Pol's equation for relaxation oscillations,
#    Contributions to the theory of nonlinear oscillations, II,
#    Annals of Mathematical Studies 29,
#    Princeton, 1952, pages 3-18.
#
#    John D Cook,
#    Calculating the period of Van der Pol Oscillators,
#    https://www.johndcook.com/blog/2019/12/26/van-der-pol-period/
#    26 December 2019.
#
#    Anatolii Dorodnitsyn,
#    Asymptotic solution of Van der Pol's equation,
#    Prikladnaia Matematika i Mekhanika, 
#    (Journal of Applied Mathematics and Mechanics),
#    American Mathematical Society Translation 88.
#
#    Roger Grimshaw,
#    Nonlinear Ordinary Differential Equations,
#    CRC Press, 1991, pages 160-163.
#
#    Minoru Urabe,
#    Journal of Science of Hiroshima University,
#    Series A, Volume 24, Number 2, October 1960, pages 197-199.
#
#  Input:
#
#    real MU: the parameter.
#
#  Output:
#
#    real P: the estimated period.
#
  import numpy as np

  if ( mu == 0.0 ):

    p1 = 2.0 * np.pi
    p2 = 2.0 * np.pi
    p3 = 2.0 * np.pi
    p4 = 2.0 * np.pi
    p5 = 2.0 * np.pi

  else:
#
#  Cook
#
    p1 = ( 3.0 - 2.0 * np.log ( 2.0 ) ) * mu
#
#  Cartwright
#
    p2 = ( 3.0 - 2.0 * np.log ( 2.0 ) ) * mu + 2.0 * np.pi / mu**(1.0/3.0)
#
#  Grimshaw.
#
    alpha = 2.338
    p3 = ( 3.0 - 2.0 * np.log ( 2.0 ) ) * mu + 2.0 * alpha / mu**(1.0/3.0)
#
#  Dorodnicyn.
#
    alpha = 2.338107
    b0 = 0.1723
    d = 0.4889

    p4 = ( 3.0 - 2.0 * np.log ( 2.0 ) ) * mu \
      + 3.0 * alpha / mu**(1.0/3.0) \
      - 22.0 / 9.0 * np.log ( mu ) / mu \
      + ( 3.0 * np.log ( 2.0 ) - np.log ( 3.0 ) - 1.0 / 6.0 + b0 - 2.0 * d ) / mu
#
#  Urabe
#
    alpha = 2.338107
    b0 = 0.1723
    d = 0.4889

    p5 = ( 3.0 - 2.0 * np.log ( 2.0 ) ) * mu \
      + 3.0 * alpha / mu**(1.0/3.0) \
      - 1.0 / 3.0 *  np.log ( mu ) / mu \
      + ( 3.0 * np.log ( 2.0 ) - np.log ( 3.0 ) - 1.5 + b0 - 2.0 * d ) / mu

  p = p5

  return p

def vanderpol_solve_ivp ( ):

#*****************************************************************************80
#
## vanderpol_solve_ivp() calls solve_ivp() to solve the van der Pol ODE.
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
#  Output:
#
#    real p: an estimate of the period.
#
#    integer nperiods: the number of full periods observed.
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Get parameter values.
#
  mu, t0, y0, tstop = vanderpol_parameters ( )
#
#  Solve the system.
#
  dydt = vanderpol_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( dydt, tspan, y0, t_eval = t, events = vanderpol_events )
#
#  Estimate the period.
#
  zeros = sol.t_events[0]
  nz = len ( zeros )
  if ( nz < 3 ):
    nperiods = np.NAN
  else:
    p = zeros[nz-1] - zeros[nz-3]
    nperiods = np.floor ( nz / 2 )

  return p, nperiods

if ( __name__ == '__main__' ):
  timestamp ( )
  vanderpol_ode_period_test ( )
  timestamp ( )

