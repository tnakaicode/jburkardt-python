#! /usr/bin/env python3
#
def arenstorf_deriv ( t, xy ):

#*****************************************************************************80
#
## arenstorf_deriv() evaluates the right hand side of arenstorf_ode().
#
#  Discussion:
#
#    The Arenstorf ODE produces a stable periodic orbit for a three body 
#    problem involving the Earth, the Moon, and a spacecraft.
#
#    Although the orbit should be periodic, and repeats after a time interval
#    of a little more than 17 units, most ODE solvers will have difficulty
#    coming close to periodicity.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    The orbit that put men on the moon,
#    https://www.johndcook.com/blog/
#    Posted 08 February 2020.
#
#    Ernst Hairer, Syvert Norsett, Gerhard Wanner,
#    Solving Ordinary Differential Equations I: Nonstiff Problems,
#    Springer, 1987.
#
#  Input:
#
#    real T, XY(4): the time, and position and speed of the spacecraft.
#
#  Output:
#
#    real DXYDT(4): the value of the derivative.
#
  import numpy as np

  x = xy[0]
  y = xy[1]
  xp = xy[2]
  yp = xy[3]
#
#  mu1 = relative mass of moon, mu2 = relative mass of earth.
#
  mu1, mu2, t0, xy0, tstop = arenstorf_parameters ( )

  d1 = np.sqrt ( ( ( x + mu1 )**2 + y**2 )**3 )
  d2 = np.sqrt ( ( ( x - mu2 )**2 + y**2 )**3 )

  dxdt = xp
  dydt = yp
  dxpdt = x + 2.0 * yp - mu2 * ( x + mu1 ) / d1 - mu1 * ( x - mu2 ) / d2
  dypdt = y - 2.0 * xp - mu2 * y / d1 - mu1 * y / d2

  dxydt = np.array ( [ dxdt, dydt, dxpdt, dypdt ] )

  return dxydt

def arenstorf_ode_test ( ):

#*****************************************************************************80
#
## arenstorf_ode_test() tests arenstorf_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'arenstorf_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test arenstorf_ode().' )
#
#  Get the parameters.
#
  mu1, mu2, t0, xy0, tstop = arenstorf_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    mu1 =   ', mu1 )
  print ( '    mu2 =   ', mu2 )
  print ( '    t0 =    ', t0 )
  print ( '    xy0 =   ', xy0 )
  print ( '    tstop = ', tstop )

  arenstorf_euler ( )
  arenstorf_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'arenstorf_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def arenstorf_euler ( ):

#*****************************************************************************80
#
## arenstorf_euler() uses euler() to solve arenstorf_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  mu1, mu2, t0, xy0, tstop = arenstorf_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )
  n = 101

  t, xy = euler ( arenstorf_deriv, tspan, xy0, n )

  plt.plot ( xy[:,0], xy[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  x  --->' )
  plt.ylabel ( '<---  y  --->' )
  plt.title ( 'arenstorf_euler() phase plot' )
  filename = 'arenstorf_euler_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def arenstorf_solve_ivp ( ):

#*****************************************************************************80
#
## arenstorf_solve_ivp() uses solve_ivp() to solve arenstorf_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  mu1, mu2, t0, xy0, tstop = arenstorf_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( arenstorf_deriv, tspan, xy0, t_eval = t )

  plt.plot ( sol.y[0], sol.y[1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  x  --->' )
  plt.ylabel ( '<---  y  --->' )
  plt.title ( 'arenstorf_solve_ivp() phase plot' )
  filename = 'arenstorf_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def arenstorf_parameters ( mu1_user = None, mu2_user = None, t0_user = None, \
  xy0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## arenstorf_parameters() returns parameters for arenstorf_ode().
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
#    31 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU1_USER: the relative mass of the moon;
#
#    real MU2_USER: the relative mass of the earth.
#
#    real T0_USER: the initial time.
#
#    real XY0_USER[4]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real MU1: the relative mass of the moon;
#
#    real MU2: the relative mass of the earth.
#
#    real T0: the initial time.
#
#    real XY0[4]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( arenstorf_parameters, "mu1_default" ):
    arenstorf_parameters.mu1_default = 0.012277471

  if not hasattr ( arenstorf_parameters, "mu2_default" ):
    arenstorf_parameters.mu2_default = 1.0 - arenstorf_parameters.mu1_default

  if not hasattr ( arenstorf_parameters, "t0_default" ):
    arenstorf_parameters.t0_default = 0.0

  if not hasattr ( arenstorf_parameters, "xy0_default" ):
    arenstorf_parameters.xy0_default = np.array ( [ 0.994, 0.0, 0.0, -2.00158510637908252240537862224 ] )

  if not hasattr ( arenstorf_parameters, "tstop_default" ):
    arenstorf_parameters.tstop_default = 17.0652165601579625588917206249
#
#  Update defaults if input was supplied.
#
  if ( mu1_user is not None ):
    arenstorf_parameters.mu1_default = mu1_user

  if ( mu2_user is not None ):
    arenstorf_parameters.mu2_default = mu2_user

  if ( t0_user is not None ):
    arenstorf_parameters.t0_default = t0_user

  if ( xy0_user is not None ):
    arenstorf_parameters.xy0_default = xy0_user

  if ( tstop_user is not None ):
    arenstorf_parameters.tstop_default = tstop_user
#
#  Return values.
#
  mu1 = arenstorf_parameters.mu1_default
  mu2 = arenstorf_parameters.mu2_default
  t0 = arenstorf_parameters.t0_default
  xy0 = arenstorf_parameters.xy0_default
  tstop = arenstorf_parameters.tstop_default
  
  return mu1, mu2, t0, xy0, tstop

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

  m = np.size ( y0 )

  t0 = tspan[0]
  tstop = tspan[1]
  dt = ( tstop - t0 ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = t0
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

if ( __name__ == '__main__' ):
  timestamp ( )
  arenstorf_ode_test ( )
  timestamp ( )

