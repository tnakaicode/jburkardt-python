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

def logistic_deriv ( t, y ):

#*****************************************************************************80
#
## logistic_deriv() returns the derivative of logistic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2022
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
  r, k, t0, y0, tstop = logistic_parameters ( )

  dydt = r * y * ( 1.0 - y / k )

  return dydt

def logistic_euler ( n ):

#*****************************************************************************80
#
## logistic_euler() solves logistic_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2022
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
  print ( 'logistic_euler():' )

  r, k, t0, y0, tstop = logistic_parameters ( )
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( logistic_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = logistic_exact ( t2 )

  plt.plot ( t, y, 'ro-', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.legend ( )
  plt.title ( 'logistic_ode(): euler' )

  filename = 'logistic_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def logistic_exact ( t ):

#*****************************************************************************80
#
## logistic_exact() evaluates the solution of logistic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  import numpy as np

  r, k, t0, y0, tstop = logistic_parameters ( )

  y = ( k * y0 * np.exp ( r * ( t - t0 ) ) ) \
    / ( k + y0 * ( np.exp ( r * ( t - t0 ) ) - 1.0 ) )

  return y

def logistic_ode_test ( ):

#*****************************************************************************80
#
## logistic_ode_test() tests logistic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'logistic_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve logistic_ode().' )

  r, k, t0, y0, tstop = logistic_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    r =     ', r )
  print ( '    k =     ', k )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  n = 20

  logistic_euler ( n )

  logistic_rk4 ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'logistic_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def logistic_parameters ( r_user = None, k_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## logistic_parameters() returns parameters for logistic_ode().
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
#    02 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r_user: the growth rate.
#
#    real k_user: the carrying capacity.
#
#    real t0_user: the initial time.
#
#    real y0_user: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real r: the growth rate.
#
#    real k: the carrying capacity.
#
#    real t0: the initial time.
#
#    real y0: the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( logistic_parameters, "r_default" ):
    logistic_parameters.r_default = 1.0

  if not hasattr ( logistic_parameters, "k_default" ):
    logistic_parameters.k_default = 1.0

  if not hasattr ( logistic_parameters, "t0_default" ):
    logistic_parameters.t0_default = 0.0

  if not hasattr ( logistic_parameters, "y0_default" ):
    logistic_parameters.y0_default = 0.5

  if not hasattr ( logistic_parameters, "tstop_default" ):
    logistic_parameters.tstop_default = 8.0
#
#  Update defaults if input was supplied.
#
  if ( r_user is not None ):
    logistic_parameters.r_default = r_user

  if ( k_user is not None ):
    logistic_parameters.k_default = k_user

  if ( t0_user is not None ):
    logistic_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    logistic_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    logistic_parameters.tstop_default = tstop_user
#
#  Return values.
#
  r = logistic_parameters.r_default
  k = logistic_parameters.k_default
  t0 = logistic_parameters.t0_default
  y0 = logistic_parameters.y0_default
  tstop = logistic_parameters.tstop_default
  
  return r, k, t0, y0, tstop

def logistic_rk4 ( n ):

#*****************************************************************************80
#
## logistic_rk4() solves logistic_ode() using rk4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2022
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
  print ( 'logistic_rk4():' )

  r, k, t0, y0, tstop = logistic_parameters ( )
  tspan = np.array ( [ t0, tstop ] )

  t, y = rk4 ( logistic_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = logistic_exact ( t2 )

  plt.plot ( t, y, 'ro-', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.legend ( )
  plt.title ( 'logistic_ode(): rk4' )

  filename = 'logistic_rk4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
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
  logistic_ode_test ( )
  timestamp ( )

