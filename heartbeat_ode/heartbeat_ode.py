#! /usr/bin/env python3
#
def heartbeat_deriv ( t, y ):

#*****************************************************************************80
#
## heartbeat_deriv() evaluates the derivative for heartbeat_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(1,2): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2,1): the value of the derivative.
#
  import numpy as np

  a, epsilon, gamma, t0, y0, tstop = heartbeat_parameters ( )

  dydt = np.array ( [ \
    - 1.0 / epsilon * ( y[0]**3 - a * y[0] + y[1] ), \
    y[0] - gamma ] )

  return dydt

def heartbeat_solve_ivp ( ):

#*****************************************************************************80
#
## heartbeat_solve_ivp() uses solve_ivp() to solve heartbeat_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 March 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'heartbeat_solve_ivp():' )
  print ( '  Use solve_ivp() to solve heartbeat_ode().' )

  a, epsilon, gamma, t0, y0, tstop = heartbeat_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t = np.linspace ( t0, tstop, 101 )
  
  sol = solve_ivp ( heartbeat_deriv, tspan, y0, t_eval = t )
#
#  Plot T, Y1.
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.grid ( 'on' )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y1(t) -->' )
  plt.title ( 'heartbeat_ode(): solve_ivp: y1' )
  filename = 'heartbeat_solve_ivp_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot T, Y2.
#
  plt.clf ( )
  plt.plot ( t, sol.y[1], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y2(t) -->' )
  plt.title ( 'heartbeat_ode(): solve_ivp: y2' )
  filename = 'heartbeat_solve_ivp_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot Y1, Y2.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], 'c-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- y1(t) -->' )
  plt.ylabel ( '<-- y2(t) -->' )
  plt.title ( 'heartbeat_ode(): solve_ivp: phase' )
  filename = 'heartbeat_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def heartbeat_ode_test ( ):

#*****************************************************************************80
#
## heartbeat_ode_test() solves heartbeat_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'heartbeat_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve heartbeat_ode().' )

  a, epsilon, gamma, t0, y0, tstop = heartbeat_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a       = ', a )
  print ( '    epsilon = ', epsilon )
  print ( '    gamma   = ', gamma )
  print ( '    t0      = ', t0 )
  print ( '    y0      = ', y0 )
  print ( '    tstop   = ', tstop )

  heartbeat_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'heartbeat_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def heartbeat_parameters ( a_user = None, epsilon_user = None, \
  gamma_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## heartbeat_parameters() returns parameters for heartbeat_ode().
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
#    20 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER: the muscle tension.
#
#    real EPSILON_USER: controls the sharpness of the response.
#
#    real GAMMA_USER: the typical fiber length.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER(2): the initial condition at time T0.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A: the muscle tension.
#
#    real EPSILON: controls the sharpness of the response.
#
#    real GAMMA: the typical fiber length.
#
#    real T0: the initial time.
#
#    real Y0(2): the initial condition at time T0.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if ( not hasattr ( heartbeat_parameters, "a_default" ) ):
    heartbeat_parameters.a_default = 0.81

  if ( not hasattr ( heartbeat_parameters, "epsilon_default" ) ):
    heartbeat_parameters.epsilon_default = 0.001

  if ( not hasattr ( heartbeat_parameters, "gamma_default" ) ):
    heartbeat_parameters.gamma_default = 0.45

  if ( not hasattr ( heartbeat_parameters, "t0_default" ) ):
    heartbeat_parameters.t0_default = 0.0

  if ( not hasattr ( heartbeat_parameters, "y0_default" ) ):
    heartbeat_parameters.y0_default = np.array ( [ 1.0, 1.0 ] )

  if ( not hasattr ( heartbeat_parameters, "tstop_default" ) ):
    heartbeat_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    heartbeat_parameters.a_default = a_user

  if ( epsilon_user is not None ):
    heartbeat_parameters.epsilon_default = epsilon_user

  if ( gamma_user is not None ):
    heartbeat_parameters.gamma_default = gamma_user

  if ( t0_user is not None ):
    heartbeat_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    heartbeat_parameters.y0_default = y0_user.copy()

  if ( tstop_user is not None ):
    heartbeat_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = heartbeat_parameters.a_default
  epsilon = heartbeat_parameters.epsilon_default
  gamma = heartbeat_parameters.gamma_default
  t0 = heartbeat_parameters.t0_default
  y0 = heartbeat_parameters.y0_default
  tstop = heartbeat_parameters.tstop_default

  return a, epsilon, gamma, t0, y0, tstop

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
  heartbeat_ode_test ( )
  timestamp ( )

