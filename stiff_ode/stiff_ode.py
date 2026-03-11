#! /usr/bin/env python3
#
def stiff_ode_test ( ):

#*****************************************************************************80
#
## stiff_ode_test() tests stiff_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'stiff_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve stiff_ode().' )

  lamda, t0, y0, tstop = stiff_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    lamda = ', lamda )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 27
  stiff_euler_test ( n )

  n = 27
  stiff_euler_backward_test ( n )

  n = 27
  stiff_midpoint_test ( n )

  stiff_solve_ivp_test ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'stiff_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def stiff_deriv ( t, y ):

#*****************************************************************************80
#
## stiff_deriv() evaluates the right hand side of stiff_ode().
#
#  Discussion:
#
#    y' = lamda * ( cos(t) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y: the time and solution value.
#
#  Output:
#
#    real DYDT: the derivative value.
#
  import numpy as np

  lamda, t0, y0, tstop = stiff_parameters ( )

  dydt = lamda * ( np.cos ( t ) - y )

  return dydt

def stiff_euler ( n ):

#*****************************************************************************80
#
## stiff_euler() uses the Euler method on stiff_ode().
#
#  Discussion:
#
#    y' = lamda * ( cos(t) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  lamda, t0, y0, tstop = stiff_parameters ( )

  dt = ( tstop - t0 ) / n

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1] = y[i] + dt * lamda * ( np.cos ( t[i] ) - y[i] )

  return t, y

def stiff_euler_test ( n ):

#*****************************************************************************80
#
## stiff_euler_test() solves stiff_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
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
  print ( 'stiff_euler_test():' )
  print ( '  Solve stiff_ode() using the Euler method.' )

  t1, y1 = stiff_euler ( n )

  t0 = 0.0
  tstop = 1.0

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'r-o', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff_ode(): euler() solution' )
  plt.legend ( )
  filename = 'stiff_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_euler_backward ( n ):

#*****************************************************************************80
#
## stiff_euler_backward() uses the backward Euler method on stiff_ode().
#
#  Discussion:
#
#    y' = lamda * ( cos(t) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  lamda, t0, y0, tstop = stiff_parameters ( )

  dt = ( tstop - t0 ) / n

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1] = ( y[i] + dt * lamda * np.cos ( t[i+1] ) ) / ( 1.0 + lamda * dt )

  return t, y

def stiff_euler_backward_test ( n ):

#*****************************************************************************80
#
## stiff_euler_backward_test() solves stiff_ode() using stiff_euler_backward().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2020
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
  print ( 'stiff_backward_euler_test():' )
  print ( '  Solve stiff_ode() using the backward Euler method.' )

  t1, y1 = stiff_euler_backward ( n )

  t0 = 0.0
  tstop = 1.0

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'r-o', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff_ode(): backward Euler method' )
  plt.legend ( )
  filename = 'stiff_euler_backward.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_exact ( t ):

#*****************************************************************************80
#
## stiff_exact() evaluates the exact solution of stiff_ode().
#
#  Discussion:
#
#    y' = lamda * ( cos(t) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the evaluation times.
#
#  Output:
#
#    real Y(:): the exact solution values.
#
  import numpy as np

  lamda, t0, y0, tstop = stiff_parameters ( )

  value = lamda * \
    ( np.sin ( t ) + lamda * np.cos(t) - lamda * np.exp ( - lamda * t ) ) \
    / ( lamda**2 + 1.0 )

  return value

def stiff_midpoint ( n ):

#*****************************************************************************80
#
## stiff_midpoint() uses the midpoint method on stiff_ode().
#
#  Discussion:
#
#    y' = lamda * ( cos(t) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  lamda, t0, y0, tstop = stiff_parameters ( )

  dt = ( tstop - t0 ) / n

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1] = \
      ( \
        y[i] + lamda * 0.5 * dt * ( \
                                    np.cos ( t[i] ) - y[i] + np.cos ( t[i+1] ) \
                                  ) \
      ) \
      / ( 1.0 + lamda * 0.5 * dt )

  return t, y

def stiff_midpoint_test ( n ):

#*****************************************************************************80
#
## stiff_midpoint_test() solves stiff_ode() using stiff_midpoint().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
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
  print ( 'stiff_midpoint_test():' )
  print ( '  Solve stiff_ode() using midpoint().' )

  t1, y1 = stiff_midpoint ( n )

  t0 = 0.0
  tstop = 1.0

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'r-o', linewidth = 3, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff_ode(): midpoint method' )
  plt.legend ( )
  filename = 'stiff_midpoint.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_solve_ivp_test ( n ):

#*****************************************************************************80
#
## stiff_solve_ivp_test() solves stiff_ode() using solve_ivp().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stiff_solve_ivp_test():' )
  print ( '  Solve stiff_ode() using solve_ivp().' )

  lamda, t0, y0, tstop = stiff_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 28 )

# sol = solve_ivp ( stiff_deriv, tspan, [ y0 ], t_eval = t )
  sol = solve_ivp ( stiff_deriv, tspan, [ y0 ] )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( sol.t, sol.y[0], 'ro', markersize = 10, label = 'Computed' )
# plt.plot ( t, sol.y[0], 'ro', markersize = 10, label = 'Computed' )
  plt.plot ( t2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff_ode(): solve_ivp()' )
  plt.legend ( )
  filename = 'stiff_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_parameters ( lamda_user = None, t0_user = None, y0_user = None, 
  tstop_user = None ):

#*****************************************************************************80
#
## stiff_parameters() returns parameters for stiff_ode().
#
#  Discussion:
#
#    This function keeps track of the current default values for the variables.
#    If the user calls with no arguments, the defaults are returned.
#    The user may instead call with one or more arguments, in which case
#    these values will replace the old defaults.
#
#    Thanks to Detelina Stoyanova who tracked down this method for creating,
#    modifying, and reading "persistent" or "static" variables in Python.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real LAMDA_USER, a parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real LAMDA, a parameter.
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#

#
#  Initialize the default values.
#
  if not ( hasattr ( stiff_parameters, "lamda_default" ) ):
    stiff_parameters.lamda_default = 50.0

  if not ( hasattr ( stiff_parameters, "t0_default" ) ):
    stiff_parameters.t0_default = 0.0

  if not ( hasattr ( stiff_parameters, "y0_default" ) ):
    stiff_parameters.y0_default = 0.0

  if not ( hasattr ( stiff_parameters, "tstop_default" ) ):
    stiff_parameters.tstop_default = 1.0
#
#  Any user supplied value replaces the current default.
#
  if ( lamda_user is not None ):
    stiff_parameters.lamda_default = lamda_user

  if ( t0_user is not None ):
    stiff_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    stiff_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    stiff_parameters.tstop_default = tstop_user
#
#  Return the current default values.
#
  lamda = stiff_parameters.lamda_default
  t0    = stiff_parameters.t0_default
  y0    = stiff_parameters.y0_default
  tstop = stiff_parameters.tstop_default

  return lamda, t0, y0, tstop

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
  stiff_ode_test ( )
  timestamp ( )

