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

def humps_deriv ( t, y ):

#*****************************************************************************80
#
## humps_deriv() returns the derivative of humps_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the current time.
#
#    real Y: the current solution value.
#
#  Output:
#
#    real DYDT: the value of dY/dT.
#
  dydt = - 2.0 * ( t - 0.3 ) / ( ( t - 0.3 )**2 + 0.01 )**2 \
         - 2.0 * ( t - 0.9 ) / ( ( t - 0.9 )**2 + 0.04 )**2

  return dydt

def humps_euler ( n ):

#*****************************************************************************80
#
## humps_euler() solves humps_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'humps_euler():' )

  t0, y0, tstop = humps_parameters ( )
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( humps_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = humps_exact ( t2 )

  plt.plot ( t, y, 'ro-', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.legend ( )
  plt.title ( 'humps_ode(): euler' )

  filename = 'humps_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def humps_exact ( x ):

#*****************************************************************************80
#
## humps_exact() evaluates the solution of humps_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
    + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
    - 6.0

  return y

def humps_ode_test ( ):

#*****************************************************************************80
#
## humps_ode_test() tests humps_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'humps_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve humps_ode().' )

  t0, y0, tstop = humps_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  n = 20

  humps_euler ( n )

  humps_rk4 ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'humps_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def humps_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## humps_parameters() returns parameters for humps_ode().
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
#    28 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
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
  if not hasattr ( humps_parameters, "t0_default" ):
    humps_parameters.t0_default = 0.0

  if not hasattr ( humps_parameters, "y0_default" ):
    humps_parameters.y0_default = humps_exact ( humps_parameters.t0_default )

  if not hasattr ( humps_parameters, "tstop_default" ):
    humps_parameters.tstop_default = 2.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    humps_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    humps_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    humps_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = humps_parameters.t0_default
  y0 = humps_parameters.y0_default
  tstop = humps_parameters.tstop_default
  
  return t0, y0, tstop

def humps_rk4 ( n ):

#*****************************************************************************80
#
## humps_rk4() solves humps_ode() using rk4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'humps_rk4():' )

  t0, y0, tstop = humps_parameters ( )
  tspan = np.array ( [ t0, tstop ] )

  t, y = rk4 ( humps_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = humps_exact ( t2 )

  plt.plot ( t, y, 'ro-', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.legend ( )
  plt.title ( 'humps_ode(): rk4' )

  filename = 'humps_rk4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def rk4 ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## rk4() approximates the solution to an ODE using the RK4 method.
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

    f1 = dydt ( t[i],            y[i,:] )
    f2 = dydt ( t[i] + dt / 2.0, y[i,:] + dt * f1 / 2.0 )
    f3 = dydt ( t[i] + dt / 2.0, y[i,:] + dt * f2 / 2.0 )
    f4 = dydt ( t[i] + dt,       y[i,:] + dt * f3 )

    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( f1 + 2.0 * f2 + 2.0 * f3 + f4 ) / 6.0

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
  humps_ode_test ( )
  timestamp ( )

