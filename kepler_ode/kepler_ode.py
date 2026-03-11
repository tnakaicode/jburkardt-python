#! /usr/bin/env python3
#
def kepler_conserved ( y ):

#*****************************************************************************80
#
## kepler_conserved() evaluates conservation for kepler_ode().
#
#  Discussion:
#
#    We consider a Kepler two-body gravitational problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric Numerical Integration:
#    Structure-Preserving Algorithms for Ordinary Differential Equations,
#    Springer, 2006,
#    ISSN: 0179-3632
#
#  Input:
#
#    real Y(N,4): the current solution.
#
#  Output:
#
#    real H1(N): the value of energy.
#
#    real H2(N): the value of angular momentum.
#
  import numpy as np

  q1 = y[0]
  q2 = y[1]
  p1 = y[2]
  p2 = y[3]

  h1 = 0.5 * ( p1**2 + p2**2 ) - 1.0 / np.sqrt ( q1**2 + q2**2 )

  h2 = q1 * p2 - q2 * p1

  return h1, h2

def kepler_deriv ( t, y ):

#*****************************************************************************80
#
## kepler_deriv evaluates the derivative of kepler_ode().
#
#  Discussion:
#
#    We consider a Kepler problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric Numerical Integration:
#    Structure-Preserving Algorithms for Ordinary Differential Equations,
#    Springer, 2006,
#    ISSN: 0179-3632
#
#  Input:
#
#    real T, Y(4): the arguments of the derivative.
#
#  Output:
#
#    real DPQDT: the value of the derivative.
#
  import numpy as np

  q1 = y[0]
  q2 = y[1]
  p1 = y[2]
  p2 = y[3]

  dq1dt = p1
  dq2dt = p2
  dp1dt =         - q1 / np.sqrt ( ( q1**2 + q2**2 )**3 )
  dp2dt =         - q2 / np.sqrt ( ( q1**2 + q2**2 )**3 )

  dydt = np.array ( [ dq1dt, dq2dt, dp1dt, dp2dt ] )

  return dydt

def kepler_solve_ivp ( ):

#*****************************************************************************80
#
## kepler_solve_ivp() uses solve_ivp() to solve kepler_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'kepler_solve_ivp_test():' )
  print ( '  Use solve_ivp() to solve kepler_ode().' )

  e, t0, y0, tstop = kepler_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( kepler_deriv, tspan, y0, t_eval = t )

  plt.plot ( t, sol.y[0], 'r-', linewidth = 2 )
  plt.plot ( t, sol.y[1], 'g-', linewidth = 2 )
  plt.plot ( t, sol.y[2], 'b-', linewidth = 2 )
  plt.plot ( t, sol.y[3], 'm-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  p,q  --->' )
  plt.title ( 'kepler_ode(): solve_ivp: Time Plot'  )
  plt.legend ( ( 'P', 'P\'', 'Q', 'Q\'' ) )
  filename = 'kepler_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( sol.y[0], sol.y[1], 'bo' )
  plt.grid ( True )
  plt.xlabel ( '<---  q1  --->' )
  plt.ylabel ( '<---  q2  --->' )
  plt.title ( 'kepler_ode(): solve_ivp: Phase Plot' )
  filename = 'kepler_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h1, h2 = kepler_conserved ( sol.y )

  plt.plot ( t, h1, 'r-', linewidth = 3 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ h1[0], h1[0] ] ), \
    'b--', linewidth = 3 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ 0.0, 0.0 ] ), \
    'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H1(T) -->' )
  plt.title ( 'kepler_ode(): solve_ivp: H1(T)' )
  filename = 'kepler_solve_ivp_h1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, h2, 'r-', linewidth = 3 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ h2[0], h2[0] ] ), \
    'b--', linewidth = 3 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ 0.0, 0.0 ] ), \
    'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H2(T) -->' )
  plt.title ( 'kepler_ode(): solve_ivp: H2(T)' )
  filename = 'kepler_solve_ivp_h2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def kepler_ode_test ( ):

#*****************************************************************************80
#
## kepler_ode_test() tests kepler_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    real E: the eccentricity.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'kepler_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve kepler_ode().' )

  e, t0, y0, tstop = kepler_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    e     = ', e )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  kepler_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'kepler_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def kepler_parameters ( e_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## kepler_parameters() returns parameters for kepler_ode().
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
#    real E_USER: the orbital eccentricity.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[4]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real E: the orbital eccentricity.
#
#    real T0: the initial time.
#
#    real Y0[4]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( kepler_parameters, "e_default" ):
    kepler_parameters.e_default = 0.6

  if not hasattr ( kepler_parameters, "t0_default" ):
    kepler_parameters.t0_default = 0.0

  if not hasattr ( kepler_parameters, "y0_default" ):
    e = kepler_parameters.e_default
    kepler_parameters.y0_default = np.array ( [ 1.0-e, 0.0, 0.0, np.sqrt((1.0+e)/(1.0-e)) ] )

  if not hasattr ( kepler_parameters, "tstop_default" ):
    kepler_parameters.tstop_default = 120.0
#
#  Update defaults if input was supplied.
#
  if ( e_user is not None ):
    kepler_parameters.e_default = e_user

  if ( t0_user is not None ):
    kepler_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    kepler_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    kepler_parameters.tstop_default = tstop_user
#
#  Return values.
#
  e = kepler_parameters.e_default
  t0 = kepler_parameters.t0_default
  y0 = kepler_parameters.y0_default
  tstop = kepler_parameters.tstop_default
  
  return e, t0, y0, tstop

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
  kepler_ode_test ( )
  timestamp ( )

