#! /usr/bin/env python3
#
def gear_ode_test ( ):

#*****************************************************************************80
#
## gear_ode_test() tests gear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import pprint

  print ( '' )
  print ( 'gear_ode_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Solve gear_ode().' )

  C, t0, y0, tstop = gear_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    C:' )
  pprint.pprint ( C )
  print ( '    t0    = ', t0 )
  print ( '    y0:' )
  pprint.pprint ( y0 )
  print ( '    tstop = ', tstop )

  n = 1500
  gear_euler_test ( n )

  n = 50
  gear_euler_backward_test ( n )

  n = 200
  gear_midpoint_test ( n )

  gear_solve_ivp_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gear_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def gear_deriv ( t, y ):

#*****************************************************************************80
#
## gear_deriv() evaluates the right hand side of gear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(2): the time and solution value.
#
#  Output:
#
#    real DYDT(2): the derivative value.
#
  import numpy as np

  C, t0, y0, tstop = gear_parameters ( )

  dydt = np.matmul ( - C, y )

  return dydt

def gear_euler ( n ):

#*****************************************************************************80
#
## gear_euler() uses the Euler method on gear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
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
#    real T(N+1), Y(N+1, 2): the times and estimated solutions.
#
  import numpy as np

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, 2 ] )

  C, t0, y0, tstop = gear_parameters ( )

  dt = ( tstop - t0 ) / n

  t[0] = t0
  y[0,:] = y0.copy()

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] - dt * np.matmul ( C, y[i,:] )

  return t, y

def gear_euler_test ( n ):

#*****************************************************************************80
#
## gear_euler_test() solves gear_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
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
  print ( 'gear_euler_test():' )
  print ( '  Solve gear_ode() using the Euler method.' )

  C, t0, y0, tstop = gear_parameters ( )

  t1, y1 = gear_euler ( n )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = gear_exact ( t2 )

  plt.plot ( t1, y1[:,0], 'r-', linewidth = 3, label = 'Computed y' )
  plt.plot ( t1, y1[:,1], 'm-', linewidth = 3, label = 'Computed y\'' )
  plt.plot ( t2, y2[:,0], 'b--', linewidth = 3, label = 'Exact y' )
  plt.plot ( t2, y2[:,1], 'c--', linewidth = 3, label = 'Exact y\'' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'gear_ode(): euler() solution' )
  plt.legend ( )
  filename = 'gear_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def gear_euler_backward ( n ):

#*****************************************************************************80
#
## gear_euler_backward() uses the backward Euler method on gear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2026
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
#    real T(N+1), Y(N+1,2): the times and estimated solutions.
#
  import numpy as np

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, 2 ] )

  C, t0, y0, tstop = gear_parameters ( )

  dt = ( tstop - t0 ) / n

  t[0] = t0
  y[0,:] = y0.copy()

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = np.linalg.solve ( np.eye ( 2 ) + C * dt, y[i,:] )

  return t, y

def gear_euler_backward_test ( n ):

#*****************************************************************************80
#
## gear_euler_backward_test() solves gear_ode() using gear_euler_backward().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
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
  print ( 'gear_backward_euler_test():' )
  print ( '  Solve gear_ode() using the backward Euler method.' )

  C, t0, y0, tstop = gear_parameters ( )

  t1, y1 = gear_euler_backward ( n )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = gear_exact ( t2 )

  plt.plot ( t1, y1[:,0], 'r-', linewidth = 3, label = 'Computed y' )
  plt.plot ( t1, y1[:,1], 'm-', linewidth = 3, label = 'Computed y\'' )
  plt.plot ( t2, y2[:,0], 'b--', linewidth = 3, label = 'Exact y' )
  plt.plot ( t2, y2[:,1], 'c--', linewidth = 3, label = 'Exact y\'' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'gear_ode(): backward Euler method' )
  plt.legend ( )
  filename = 'gear_euler_backward.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def gear_exact ( t ):

#*****************************************************************************80
#
## gear_exact() evaluates the exact solution of gear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
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
#    real Y(:,2): the exact solution values.
#
  import numpy as np

  tvec = np.atleast_1d ( t )
  n = tvec.shape[0]
  y = np.zeros ( [ n, 2 ] )

  y[:,0] = 2.0 * np.exp ( - t ) - np.exp ( - 1000 * t )
  y[:,1] =     - np.exp ( - t ) + np.exp ( - 1000 * t )

  return y

def gear_midpoint ( n ):

#*****************************************************************************80
#
## gear_midpoint() uses the midpoint method on gear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2026
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
#    real T(N+1), Y(N+1,2): the times and estimated solutions.
#
  import numpy as np

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, 2 ] )

  C, t0, y0, tstop = gear_parameters ( )

  dt = ( tstop - t0 ) / n

  t[0] = t0
  y[0,:] = y0.copy()

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    yh = np.linalg.solve ( np.eye ( 2 ) + C * 0.5 * dt, y[i,:] )
    y[i+1,:] = 2.0 * yh - y[i,:]

  return t, y

def gear_midpoint_test ( n ):

#*****************************************************************************80
#
## gear_midpoint_test() solves gear_ode() using gear_midpoint().
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
  print ( 'gear_midpoint_test():' )
  print ( '  Solve gear_ode() using midpoint().' )

  C, t0, y0, tstop = gear_parameters ( )

  t1, y1 = gear_midpoint ( n )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = gear_exact ( t2 )

  plt.plot ( t1, y1[:,0], 'r-', linewidth = 3, label = 'Computed y' )
  plt.plot ( t1, y1[:,1], 'm-', linewidth = 3, label = 'Computed y\'' )
  plt.plot ( t2, y2[:,0], 'b--', linewidth = 3, label = 'Exact y' )
  plt.plot ( t2, y2[:,1], 'c--', linewidth = 3, label = 'Exact y\'' )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'gear_ode(): midpoint method' )
  plt.legend ( )
  filename = 'gear_midpoint.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def gear_parameters ( C_user = None, t0_user = None, y0_user = None, 
  tstop_user = None ):

#*****************************************************************************80
#
## gear_parameters() returns parameters for gear_ode().
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
#    real C_USER[2,2], a parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[2]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real C[2,2], a parameter.
#
#    real T0: the initial time.
#
#    real Y0[2]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize the default values.
#
  if not ( hasattr ( gear_parameters, "C_default" ) ):
    gear_parameters.C_default = np.array ( [ \
      [ - 998.0, - 1998 ], \
      [ + 999.0, + 1999 ] ] )

  if not ( hasattr ( gear_parameters, "t0_default" ) ):
    gear_parameters.t0_default = 0.0

  if not ( hasattr ( gear_parameters, "y0_default" ) ):
    gear_parameters.y0_default = np.array ( [ 1.0, 0.0 ] )

  if not ( hasattr ( gear_parameters, "tstop_default" ) ):
    gear_parameters.tstop_default = 1.0
#
#  Any user supplied value replaces the current default.
#
  if ( C_user is not None ):
    gear_parameters.C_default = C_user.copy ( )

  if ( t0_user is not None ):
    gear_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    gear_parameters.y0_default = y0_user.copy ( )

  if ( tstop_user is not None ):
    gear_parameters.tstop_default = tstop_user
#
#  Return the current default values.
#
  C     = gear_parameters.C_default.copy ( )
  t0    = gear_parameters.t0_default
  y0    = gear_parameters.y0_default.copy ( )
  tstop = gear_parameters.tstop_default

  return C, t0, y0, tstop

def gear_solve_ivp_test ( ):

#*****************************************************************************80
#
## gear_solve_ivp_test() solves gear_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2026
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gear_solve_ivp_test():' )
  print ( '  Solve gear_ode() using solve_ivp().' )

  C, t0, y0, tstop = gear_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( gear_deriv, tspan, y0 )

  n = (sol.t).shape[0]
  print ( '  solve_ivp() took ', n, ' steps.' )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = gear_exact ( t2 )

  plt.plot ( sol.t, sol.y[0], 'ro', markersize = 10, label = 'Computed y' )
  plt.plot ( sol.t, sol.y[1], 'mo', markersize = 10, label = 'Computed y\'' )
  plt.plot ( t2, y2[:,0], 'b--', linewidth = 3, label = 'Exact y' )
  plt.plot ( t2, y2[:,1], 'c--', linewidth = 3, label = 'Exact y\'' )

  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'gear_ode(): solve_ivp()' )
  plt.legend ( )
  filename = 'gear_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

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
  gear_ode_test ( )
  timestamp ( )

