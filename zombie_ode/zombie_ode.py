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

def zombie_conserved ( y ):

#*****************************************************************************80
#
## zombie_conserved() returns a conserved quantity for zombie_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2020
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

  h = np.sum ( y, axis = 1 )

  return h

def zombie_deriv ( t, y ):

#*****************************************************************************80
#
## zombie_deriv() returns the right hand side of zombie_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2020
#
#  Reference:
#
#    Philip Munz, Ioan Hudea, Joe Imad, Robert Smith,
#    When Zombies Attack!: Mathematical Modelling of an Outbreak
#    of Zombie Infection,
#    Infection Disease Modelling Progress, 
#    Editors: J M Tchuenche, C Chiyaka,
#    Nova Science Publishers, 2009.
#
#  Input:
#
#    real t: the current time.
#
#    real y(3): the current solution.
#
#  Output:
#
#    real dydt(3): the right hand side of the zombie ODE.
#
  import numpy as np

  alpha, beta, gamma, delta, t0, y0, tstop = zombie_parameters ( )

  s = y[0]
  z = y[1]
  r = y[2]

  dsdt = - beta * s * z                             - delta * s 
  dzdt =   beta * s * z - alpha * s * z + gamma * r
  drdt =                  alpha * s * z - gamma * r + delta * s

  dydt = np.array ( [ dsdt, dzdt, drdt ] )

  return dydt

def zombie_euler ( n ):

#*****************************************************************************80
#
## zombie_euler() uses the Euler method to solve zombie_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'zombie_euler():' )
  print ( '  Use the euler method on the zombie ODE.' )

  alpha, beta, gamma, delta, t0, y0, tstop = zombie_parameters ( )

  f = zombie_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( f, tspan, y0, n )
#
#  Plot the solution.
#
  plt.plot ( t, y, linewidth = 2 )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- Population --->' )
  plt.title ( 'zombie_ode() euler: time plot' )
  plt.grid ( True )
  plt.legend ( ( 'Humans', 'Zombies', 'Suspended Zombies' ) )
  filename = 'zombie_euler_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot the conserved quantity.
#
  h = zombie_conserved ( y )

  p0 = np.sum ( y[0,:] )

  plt.plot ( t, h, 'b-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'r--', linewidth= 2 )
  plt.plot ( tspan, np.array ( [ p0, p0 ] ), 'r--', linewidth = 2 )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- Total population --->' )
  plt.title ( 'zombie_ode(): population conservation' )
  plt.grid ( True )
  filename = 'zombie_euler_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def zombie_ode_test ( ):

#*****************************************************************************80
#
## zombie_ode_test() tests zombie_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'zombie_ode_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve zombie_ode().' )

  alpha, beta, gamma, delta, t0, y0, tstop = zombie_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta  = ', beta )
  print ( '    gamma = ', gamma )
  print ( '    delta = ', delta )
  print ( '    t0    = ', t0  )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 2000
  zombie_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'zombie_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def zombie_parameters ( alpha_user = None, beta_user = None, \
  gamma_user = None, delta_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## zombie_parameters() returns parameters for zombie_ode().
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
#    real ALPHA_USER: zombie destruction rate.
#
#    real BETA_USER: new zombie rate.
#
#    real GAMMA_USER: zombie resurrection rate.
#
#    real DELTA_USER: background death rate.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ALPHA: zombie destruction rate.
#
#    real BETA: new zombie rate.
#
#    real GAMMA: zombie resurrection rate.
#
#    real DELTA: background death rate.
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
  if not hasattr ( zombie_parameters, "alpha_default" ):
    zombie_parameters.alpha_default = 0.008

  if not hasattr ( zombie_parameters, "beta_default" ):
    zombie_parameters.beta_default = 0.0095

  if not hasattr ( zombie_parameters, "gamma_default" ):
    zombie_parameters.gamma_default = 0.02

  if not hasattr ( zombie_parameters, "delta_default" ):
    zombie_parameters.delta_default = 0.0001

  if not hasattr ( zombie_parameters, "t0_default" ):
    zombie_parameters.t0_default = 0.0

  if not hasattr ( zombie_parameters, "y0_default" ):
    zombie_parameters.y0_default = np.array ( [ 500.0, 0.0, 0.0 ] )

  if not hasattr ( zombie_parameters, "tstop_default" ):
    zombie_parameters.tstop_default = 20.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    zombie_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    zombie_parameters.beta_default = beta_user

  if ( gamma_user is not None ):
    zombie_parameters.gamma_default = gamma_user

  if ( delta_user is not None ):
    zombie_parameters.delta_default = delta_user
  if ( t0_user is not None ):
    zombie_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    zombie_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    zombie_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = zombie_parameters.alpha_default
  beta = zombie_parameters.beta_default
  gamma = zombie_parameters.gamma_default
  delta = zombie_parameters.delta_default
  t0 = zombie_parameters.t0_default
  y0 = zombie_parameters.y0_default
  tstop = zombie_parameters.tstop_default
  
  return alpha, beta, gamma, delta, t0, y0, tstop

if ( __name__ == '__main__' ):
  timestamp ( )
  zombie_ode_test ( )
  timestamp ( )

