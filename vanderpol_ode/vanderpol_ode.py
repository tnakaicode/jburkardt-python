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
## vanderpol_deriv() returns the right hand side of vanderpol_ode().
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

def vanderpol_ode_test ( ):

#*****************************************************************************80
#
## vanderpol_ode_test() solves vanderpol_ode().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'vanderpol_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve vanderpol_ode().' )
#
#  Get parameter values.
#
  mu, t0, y0, tstop = vanderpol_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    mu    = ', mu )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  vanderpol_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'vanderpol_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def vanderpol_parameters ( mu_user = None, t0_user = None, y0_user = None,
  tstop_user = None ):

#*****************************************************************************80
#
## vanderpol_parameters() returns the parameters of vanderpol_ode().
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

def vanderpol_solve_ivp ( ):

#*****************************************************************************80
#
## vanderpol_solve_ivp() calls solve_ivp() for vanderpol_ode().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'vanderpol_solve_ivp():' )
  print ( '  Solve vanderpol_ode() using solve_ivp().' )
#
#  Get parameter values.
#
  mu, t0, y0, tstop = vanderpol_parameters ( )

  dydt = vanderpol_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( dydt, tspan, y0, t_eval = t )
#
#  Time plot of y(t), y'(t).
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'r-', t, sol.y[1], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  s = ( 'vanderpol_ode() solve_ivp, mu = %g' % ( mu ) )
  plt.title ( s )
  plt.legend ( ( 'y(t)', 'y\'(t)' ) )
  filename = 'vanderpol_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.close ( )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], linewidth = 3 )
  plt.plot ( sol.y[0,0], sol.y[1,0], 'g.', markersize = 40 )
  plt.plot ( sol.y[0,-1], sol.y[1,-1], 'r.', markersize = 30 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<-- Y(T) -->' )
  plt.ylabel ( '<-- Y''(T) -->' )
  s = ( 'vanderpol_ode() solve_ivp phase plot, mu = %g' % ( mu ) )
  plt.title ( s )
  filename = 'vanderpol_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'vanderpol_solve_ivp():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  vanderpol_ode_test ( )
  timestamp ( )

