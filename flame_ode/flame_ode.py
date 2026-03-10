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

def flame_deriv ( t, y ):

#*****************************************************************************80
#
## flame_deriv() evaluates the derivative of flame_ode().
#
#  Discussion:
#
#    1 equation.
#
#    Moler attributes this problem to Lawrence Shampine.
#
#    The equation describes the radius of a ball of flame that
#    begins, at time 0, at DELTA.
#
#      Y(0) = DELTA
#
#    The rate of fuel consumption is proportional to the volume, and
#    the rate of fuel intake is proportional to the area of the ball.
#    We take the constant of proportionality to be 1.
#
#      Y' = Y^2 - Y^3
#
#    The data is normalized so that Y = 1 is the equilibrium solution.
#
#    The computation is to be made from T = 0 to T = 2/DELTA.
#
#    For values of DELTA close to 1, such as 0.01, the equation is
#    not stiff.  But for DELTA = 0.0001, the equation can become
#    stiff as the solution approaches the equilibrium solution Y = 1,
#    and computed solutions may be wildly inaccurate or cautious
#    solvers may take very small timesteps.
#
#    The exact solution involves the Lambert W function, defined by
#
#      W(z) * exp ( W(z) ) = z
#
#    and if we set
#
#      A = ( 1 / DELTA - 1 )
#
#    then
#
#      Y(T) = 1 / ( W(A*exp(A-T)) + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Cleve's Corner: Stiff Differential Equations,
#    MATLAB News and Notes,
#    May 2003, pages 12-13.
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT: the value of the derivative.
#
  dydt = y**2 * ( 1.0 - y )

  return dydt

def flame_exact ( t ):

#*****************************************************************************80
#
## flame_exact() evaluates the exact solution of flame_ode().
#
#  Discussion:
#
#    1 equation.
#
#    Moler attributes this problem to Lawrence Shampine.
#
#    The equation describes the radius of a ball of flame that
#    begins, at time 0, at DELTA.
#
#      Y(0) = DELTA
#
#    The rate of fuel consumption is proportional to the volume, and
#    the rate of fuel intake is proportional to the area of the ball.
#    We take the constant of proportionality to be 1.
#
#      Y' = Y^2 - Y^3
#
#    The data is normalized so that Y = 1 is the equilibrium solution.
#
#    The computation is to be made from T = 0 to T = 2/DELTA.
#
#    For values of DELTA close to 1, such as 0.01, the equation is
#    not stiff.  But for DELTA = 0.0001, the equation can become
#    stiff as the solution approaches the equilibrium solution Y = 1,
#    and computed solutions may be wildly inaccurate or cautious
#    solvers may take very small timesteps.
#
#    The exact solution involves the Lambert W function, defined by
#
#      W(z) * exp ( W(z) ) = z
#
#    and if we set
#
#      A = ( 1 / DELTA - 1 )
#
#    then
#
#      Y(T) = 1 / ( W(A*exp(A-T)) + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Cleve's Corner: Stiff Differential Equations,
#    MATLAB News and Notes,
#    May 2003, pages 12-13.
#
#  Input:
#
#    real T(:): the times.
#
#  Output:
#
#    real Y(:), the exact solution values.
#
  from scipy.special import lambertw
  import numpy as np

  t0, y0, tstop = flame_parameters ( )

  a = ( 1.0 - y0[0] ) / y0[0]
  y = 1.0 / np.real ( lambertw ( a * np.exp ( a - ( t - t0 ) ) ) + 1.0 )

  return y

def flame_ode_test ( ):

#*****************************************************************************80
#
## flame_ode_test() tests flame_ode().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'flame_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  solve_ivp() solves flame_ode().' )

  t0, y0, tstop = flame_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  flame_ode_euler ( )
  flame_ode_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'flame_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def flame_ode_euler ( ):

#*****************************************************************************80
#
## flame_ode_euler() applies euler() to flame_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2023
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  t0, y0, tstop = flame_parameters ( )

  t_span = np.array ( [ t0, tstop ] )
  n = 101

  t, y = euler ( flame_deriv, t_span, y0, n )
  ye = flame_exact ( t )
#
#  Plot the solution curve.
#
  plt.plot ( t, y, 'ro', linewidth = 3 )
  plt.plot ( t, ye, 'b-', linewidth = 2 )
  s = ( 'flame_ode(): DELTA = ', y0[0] )
  plt.title ( s )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y(T) --->' )
  plt.legend ( ( 'yapprox', 'yexact' ) )
  filename = 'flame_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def flame_ode_solve_ivp ( ):

#*****************************************************************************80
#
## flame_ode_solve_ivp() applies solve_ivp() to flame_ode().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  t0, y0, tstop = flame_parameters ( )

  t_span = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( flame_deriv, t_span, y0, t_eval = t )
  ye = flame_exact ( t )
#
#  Plot the solution curve.
#
  plt.plot ( t, sol.y[0], 'ro', linewidth = 3 )
  plt.plot ( t, ye, 'b-', linewidth = 2 )
  s = ( 'flame_ode(): DELTA = ', y0[0] )
  plt.title ( s )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X(T) --->' )
  plt.legend ( ( 'yapprox', 'yexact' ) )
  filename = 'flame_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def flame_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## flame_parameters() returns the parameters of flame_ode().
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
  if not hasattr ( flame_parameters, "t0_default" ):
    flame_parameters.t0_default = 0.0

  if not hasattr ( flame_parameters, "y0_default" ):
    flame_parameters.y0_default = np.array ( [ 0.01 ] )

  if not hasattr ( flame_parameters, "tstop_default" ):
    flame_parameters.tstop_default = 2.0 / flame_parameters.y0_default[0]
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    flame_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    flame_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    flame_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = flame_parameters.t0_default
  y0 = flame_parameters.y0_default
  tstop = flame_parameters.tstop_default
  
  return t0, y0, tstop

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
  flame_ode_test ( )
  timestamp ( )

