#! /usr/bin/env python3
#
def rubber_band_deriv ( t, y ):

#*****************************************************************************80
#
## rubber_band_deriv() evaluates the right hand side of rubber_band_ode().
#
#  Discussion:
#
#    The original equation has the form:
#
#      y'' + 0.01 y' + a y(+) - b y(-) = 10 + lam sin ( mu t )
#
#    where y(+)=max(y,0) and y(-)=max(-y,0).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 April 2020
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt
#
#  Reference:
#
#    Lisa Humphreys, Ray Shammas,
#    Finding Unpredictable Behavior in a Simple Ordinary Differential Equation. 
#    The College Mathematics Journal, 
#    Volume 31, Number 5, November 2000, pages 338-346.
#
#    John D Cook,
#    A spring, a rubber band, and chaos
#    https://www.johndcook.com/blog/
#    26 April 2020.
#
#  Input
#
#    real T: the current time.
#
#    real Y(2): the current values of Y and Y'.
#
#  Output:
#
#    real DYDT(2): the current values of Y' and Y''.
#
  import numpy as np

  a, b, lam, mu, t0, y0, tstop = rubber_band_parameters ( )

  u = y[0]
  v = y[1]

  up = y[1]
  vp = 10.0 + lam * np.sin ( mu * t ) - 0.01 * v - a * max ( u, 0.0 ) \
    + b * max ( -u, 0.0 )
  
  dydt = np.array ( [ up, vp ] )

  return dydt

def rubber_band_ode_test ( ):

#*****************************************************************************80
#
## rubber_band_ode_test() solves rubber_band_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 April 2020
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rubber_band_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve rubber_band_ode().' )

  a, b, lam, mu, t0, y0, tstop = rubber_band_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a =     ', a )
  print ( '    b =     ', b )
  print ( '    lam =   ', lam )
  print ( '    mu =    ', mu )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  rubber_band_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rubber_band_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def rubber_band_solve_ivp ( ):

#*****************************************************************************80
#
## rubber_band_solve_ivp() solves rubber_band_ode() using solve_ivp().
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
  import matplotlib.pyplot as plt
  import numpy as np
  from scipy.integrate import solve_ivp

  a, b, lam, mu, t0, y0, tstop = rubber_band_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 301 )
  
  sol = solve_ivp ( rubber_band_deriv, tspan, y0, t_eval = t )
#
#  Plot the result.
#
  plt.plot ( sol.t, sol.y[0], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( "<-- t -->" )
  plt.ylabel ( "<-- y(t) -->" )
  plt.title ( 'rubber_band_ode(): solve_ivp' )
  filename = 'rubber_band_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rubber_band_parameters ( a_user = None, b_user = None, \
  lam_user = None, mu_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## rubber_band_parameters() returns parameters for rubber_band_ode().
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
#    real A_USER, B_USER: the coefficients of y+ and y-.
#
#    real LAM_USER: the coefficient of the sinusoidal forcing term.
#
#    real MU_USER: the coefficient of time in the sinusoidal forcing term.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A, B: the coefficients of y+ and y-.
#
#    real LAM: the coefficient of the sinusoidal forcing term.
#
#    real MU: the coefficient of time in the sinusoidal forcing term.
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
  if not hasattr ( rubber_band_parameters, "a_default" ):
    rubber_band_parameters.a_default = 17.0

  if not hasattr ( rubber_band_parameters, "b_default" ):
    rubber_band_parameters.b_default = 1.0

  if not hasattr ( rubber_band_parameters, "lam_default" ):
    rubber_band_parameters.lam_default = 15.4

  if not hasattr ( rubber_band_parameters, "mu_default" ):
    rubber_band_parameters.mu_default = 0.75

  if not hasattr ( rubber_band_parameters, "t0_default" ):
    rubber_band_parameters.t0_default = 0.0

  if not hasattr ( rubber_band_parameters, "y0_default" ):
    rubber_band_parameters.y0_default = np.array ( [ 1.0, 0.0 ] )

  if not hasattr ( rubber_band_parameters, "tstop_default" ):
    rubber_band_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    rubber_band_parameters.a_default = a_user

  if ( b_user is not None ):
    rubber_band_parameters.b_default = b_user

  if ( lam_user is not None ):
    rubber_band_parameters.lam_default = lam_user

  if ( mu_user is not None ):
    rubber_band_parameters.mu_default = mu_user

  if ( t0_user is not None ):
    rubber_band_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    rubber_band_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    rubber_band_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = rubber_band_parameters.a_default
  b = rubber_band_parameters.b_default
  lam = rubber_band_parameters.lam_default
  mu = rubber_band_parameters.mu_default
  t0 = rubber_band_parameters.t0_default
  y0 = rubber_band_parameters.y0_default
  tstop = rubber_band_parameters.tstop_default
  
  return a, b, lam, mu, t0, y0, tstop

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
  rubber_band_ode_test ( )
  timestamp ( )

