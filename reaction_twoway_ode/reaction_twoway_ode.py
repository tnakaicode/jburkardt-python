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

def midpoint ( f, tspan, y0, n ):

#*****************************************************************************80
#
## midpoint() uses the implicit midpoint method to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real tspan[2]: the starting and ending times.
#
#    real y0[m]: the initial conditions. 
#
#    integer n: the number of steps.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the solution estimates.
#
  from scipy.optimize import fsolve
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  t[0] = tspan[0];
  y[0,:] = y0

  for i in range ( 0, n ):

    to = t[i]
    yo = y[i,:]

    th = to + 0.5 * dt
    yh = yo + 0.5 * dt * f ( to, yo )
    yh = fsolve ( midpoint_residual, yh, args = ( f, to, yo, th ) )

    tp = to + dt
    yp = 2.0 * yh - yo

    t[i+1]   = tp
    y[i+1,:] = yp

  return t, y

def midpoint_residual ( yh, f, to, yo, th ):

#*****************************************************************************80
#
## midpoint_residual() evaluates the midpoint residual.
#
#  Discussion:
#
#    We are seeking a value YH defined by the implicit equation:
#
#      YH = YO + ( TH - TO ) * F ( TH, YH )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yh: the estimated solution value at the midpoint time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real th: the midpoint time.
#
#  Output:
#
#    real value: the midpoint residual.
#
  value = yh - yo - ( th - to ) * f ( th, yh );

  return value

def reaction_twoway_conserved ( y1, y2 ):

#*****************************************************************************80
#
## reaction_twoway_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(:,2): the variable values.
#
#  Output:
#
#    real H(:): the conserved quantity.
#
  h = y1 + y2

  return h

def reaction_twoway_deriv ( t, y ):

#*****************************************************************************80
#
## reaction_twoway_deriv(): right hand side of reaction_twoway_ode().
#
#  Discussion:
#
#    The reactions involve chemicals W1 and W2, and have the form
#
#    dW1dt = - k1 W1(t) + k2 W2(t)
#    dW2dt = + k1 W1(t) - k2 W2(t)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    real T, Y(2): the time and variable values.
#
#  Output:
#
#    real DYDT(2): the right hand sides of the ODE.
#
  import numpy as np

  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )

  w1 = y[0]
  w2 = y[1]

  dw1dt = - k1 * w1 + k2 * w2
  dw2dt = + k1 * w1 - k2 * w2
 
  dydt = np.array ( [ dw1dt, dw2dt ] )

  return dydt

def reaction_twoway_euler ( n ):

#*****************************************************************************80
#
## reaction_twoway_euler() solves reaction_twoway_ode() using euler().
#
#  Discussion:
#
#    The reference suggests an experiment in which the Forward Euler method
#    is used, with a timestep of 1/50.  The problem is to be solved three
#    times, with the second reaction coefficient, k2, set to 10 (the default), 
#    100, and 1000.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    integer N, the number of time steps, including the initial value.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'reaction_twoway_euler():' )
  print ( '  Solve reaction_twoway_ode() using euler()' )
#
#  Get parameter values.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )
#
#  Solve the equation.
#
  f = reaction_twoway_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( f, tspan, y0, n )

  print ( '' )
  print ( '  Number of steps will be ', n )
  print ( '  Stepsize will be ', ( tstop - t0 ) / ( n - 1 ) )
#
#  Evaluate exact solution.
#
  ye = reaction_twoway_exact ( t )
#
#  Plot.
#
  plt.plot ( t, y[:,0], 'ro', linewidth = 3 )
  plt.plot ( t, y[:,1], 'go', linewidth = 3 )
  plt.plot ( t, ye[0,:], 'c-', linewidth = 3 )
  plt.plot ( t, ye[1,:], 'm-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  Concentrations  --->' )
  title_string = ( 'reaction_twoway_ode(): euler: solution, k2 = %g' % ( k2 ) )
  plt.title ( title_string )
  plt.legend ( ( 'W1', 'W2', 'W1exact', 'W2exact', 'x axis' ) )
  filename = 'reaction_twoway_euler_solution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = reaction_twoway_conserved ( y[:,0], y[:,1] )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h[0],h[0]]), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  conserved quantity  --->' )
  title_string = ( 'reaction_twoway_ode(): euler conservation k2 = %g' % ( k2 ) )
  plt.title ( title_string )
  plt.legend ( ( 'h', 'h initial', 'x axis' ) )
  filename = 'reaction_twoway_euler_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def reaction_twoway_exact ( t ):

#*****************************************************************************80
#
## reaction_twoway_exact() returns the exact solution of reaction_twoway_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    real T: the current time.
#
#  Output:
#
#    real Y(2): the exact solution.
#
  import numpy as np

  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )

  w10 = y0[0]
  w20 = y0[1]

  w1 = ( k2 * ( w10 + w20 ) \
     + np.exp ( - ( k1 + k2 ) * t ) * ( k1 * w10 - k2 * w20 ) ) / ( k1 + k2 )
  w2 = ( k1 * ( w10 + w20 ) \
     - np.exp ( - ( k1 + k2 ) * t ) * ( k1 * w10 - k2 * w20 ) ) / ( k1 + k2 )

  y = np.array ( [ w1, w2 ] )

  return y

def reaction_twoway_midpoint ( n ):

#*****************************************************************************80
#
## reaction_twoway_midpoint() solves reaction_twoway_ode() using midpoint().
#
#  Discussion:
#
#    The reference suggests an experiment in which the Forward midpoint method
#    is used, with a timestep of 1/50.  The problem is to be solved three
#    times, with the second reaction coefficient, k2, set to 10 (the default), 
#    100, and 1000.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    integer N, the number of time steps, including the initial value.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'reaction_twoway_midpoint():' )
  print ( '  Solve reaction_twoway_ode() using midpoint()' )
#
#  Get parameter values.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )
#
#  Solve the equation.
#
  f = reaction_twoway_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = midpoint ( f, tspan, y0, n )

  print ( '' )
  print ( '  Number of steps will be ', n )
  print ( '  Stepsize will be', ( tstop - t0 ) / ( n - 1 ) )
#
#  Evaluate exact solution.
#
  ye = reaction_twoway_exact ( t )
#
#  Plot.
#
  plt.plot ( t, y[:,0], 'ro', linewidth = 3 )
  plt.plot ( t, y[:,1], 'go', linewidth = 3 )
  plt.plot ( t, ye[0,:], 'c-', linewidth = 3 )
  plt.plot ( t, ye[1,:], 'm-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  Concentrations  --->' )
  title_string = ( 'reaction_twoway_ode(): midpoint: solution, k2 = %g' % ( k2 ) )
  plt.title ( title_string )
  plt.legend ( ( 'W1', 'W2', 'W1exact', 'W2exact', 'x axis' ) )
  filename = 'reaction_twoway_midpoint_solution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = reaction_twoway_conserved ( y[:,0], y[:,1] )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h[0],h[0]]), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  conserved quantity  --->' )
  title_string = ( 'reaction_twoway_ode(): midpoint conservation k2 = %g' % ( k2 ) )
  plt.title ( title_string )
  plt.legend ( ( 'h', 'h initial', 'x axis' ) )
  filename = 'reaction_twoway_midpoint_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def reaction_twoway_solve_ivp ( ):

#*****************************************************************************80
#
## reaction_twoway_solve_ivp() solves reaction_twoway_ode() using solve_ivp().
#
#  Discussion:
#
#    The reference suggests an experiment in which the Forward Euler method
#    is used, with a timestep of 1/50.  The problem is to be solved three
#    times, with the second reaction coefficient, k2, set to 10 (the default), 
#    100, and 1000.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'reaction_twoway_solve_ivp():' )
  print ( '  Solve reaction_twoway_ode() using solve_ivp()' )
#
#  Get parameter values.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )
#
#  Solve the equation.
#
  f = reaction_twoway_deriv
  tspan = np.array ( [ t0, tstop ] )

  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Evaluate exact solution.
#
  ye = reaction_twoway_exact ( t )
#
#  Plot.
#
  plt.plot ( t, sol.y[0], 'ro', linewidth = 3 )
  plt.plot ( t, sol.y[1], 'go', linewidth = 3 )
  plt.plot ( t, ye[0,:], 'c-', linewidth = 3 )
  plt.plot ( t, ye[1,:], 'm-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  Concentrations  --->' )
  title_string = ( 'reaction_twoway_ode() solve_ip: solution, k2 = %g' % ( k2 ) )
  plt.title ( title_string )
  plt.legend ( ( 'W1', 'W2', 'W1exact', 'W2exact', 'x axis' ) )
  filename = 'reaction_twoway_solve_ip_solution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = reaction_twoway_conserved ( sol.y[0], sol.y[1] )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h[0],h[0]]), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  conserved quantity  --->' )
  title_string = ( 'reaction_twoway_ode() solve_ip conservation k2 = %g' % ( k2 ) )
  plt.title ( title_string )
  plt.legend ( ( 'h', 'h initial', 'x axis' ) )
  filename = 'reaction_twoway_solve_ip_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def reaction_twoway_ode_test ( ):

#*****************************************************************************80
#
## reaction_twoway_ode_test() solves reaction_twoway_ode().
#
#  Discussion:
#
#    The reference suggests an experiment in which the Forward Euler method
#    is used, with a timestep of 1/50.  The problem is to be solved three
#    times, with the second reaction coefficient, k2, set to 10 (the default), 
#    100, and 1000.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'reaction_twoway_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve reaction_twoway_ode().' )
  print ( '' )
  print ( '  Reaction differential equation:' )
  print ( '    dW1/dt = - k1 W1 + k2 W2' )
  print ( '    dW2/dt = + k1 W1 - k2 W2' )
#
#  Get parameter values.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )
#
#  Report parameter values.
#
  print ( '' )
  print ( '  parameters:' )
  print ( '    k1    = ', k1, ', (reaction rate)' )
  print ( '    k2    = ', k2, ', (reaction rate)' )
  print ( '    t0    = ', t0, ', (initial time, in seconds s)' )
  print ( '    w10   = ', y0[0], ', (initial amount of species W1)' )
  print ( '    w20   = ', y0[1], ', (initial amount of species W2)' )
  print ( '    tstop = ', tstop, ', (final time, in seconds s)' )
#
#  Call the solvers.
#
  n = 51
  reaction_twoway_euler ( n )

  n = 51
  reaction_twoway_midpoint ( n )

  reaction_twoway_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'reaction_twoway_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def reaction_twoway_parameters ( k1_user = None, k2_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## reaction_twoway_parameters() returns parameters for reaction_twoway_ode().
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
#    03 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real K1_USER, K2_USER: the reaction rates.
#    The value of K2 is suggested to be 10, 100, or 1000.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real K1, K2: the reaction rates.
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
  if not hasattr ( reaction_twoway_parameters, "k1_default" ):
    reaction_twoway_parameters.k1_default = 1.0

  if not hasattr ( reaction_twoway_parameters, "k2_default" ):
    reaction_twoway_parameters.k2_default = 10.0

  if not hasattr ( reaction_twoway_parameters, "t0_default" ):
    reaction_twoway_parameters.t0_default = 0.0

  if not hasattr ( reaction_twoway_parameters, "y0_default" ):
    reaction_twoway_parameters.y0_default = np.array ( [ 0.1, 0.9 ] )

  if not hasattr ( reaction_twoway_parameters, "tstop_default" ):
    reaction_twoway_parameters.tstop_default = 1.0
#
#  Update defaults if input was supplied.
#
  if ( k1_user is not None ):
    reaction_twoway_parameters.k1_default = k1_user

  if ( k2_user is not None ):
    reaction_twoway_parameters.k2_default = k2_user

  if ( t0_user is not None ):
    reaction_twoway_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    reaction_twoway_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    reaction_twoway_parameters.tstop_default = tstop_user
#
#  Return values.
#
  k1 = reaction_twoway_parameters.k1_default
  k2 = reaction_twoway_parameters.k2_default
  t0 = reaction_twoway_parameters.t0_default
  y0 = reaction_twoway_parameters.y0_default
  tstop = reaction_twoway_parameters.tstop_default
  
  return k1, k2, t0, y0, tstop

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
  reaction_twoway_ode_test ( )
  timestamp ( )

