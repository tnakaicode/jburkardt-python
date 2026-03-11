#! /usr/bin/env python3
#
def backward_euler ( f, tspan, y0, n ):

#*****************************************************************************80
#
## backward_euler() uses backward Euler to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2020
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

  t[0] = 0.0;
  y[0,:] = y0

  for i in range ( 0, n ):

    to = t[i]
    yo = y[i,:]
    tp = t[i] + dt
    yp = yo + dt * f ( to, yo )

    yp = fsolve ( backward_euler_residual, yp, args = ( f, to, yo, tp ) )

    t[i+1]   = tp
    y[i+1,:] = yp[:]

  return t, y

def backward_euler_residual ( yp, f, to, yo, tp ):

#*****************************************************************************80
#
## backward_euler_residual() evaluates the backward Euler residual.
#
#  Discussion:
#
#    We are seeking a value YP defined by the implicit equation:
#
#      YP = YO + ( TP - TO ) * F ( TP, YP )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yp: the estimated solution value at the new time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real tp: the new time.
#
#  Output:
#
#    real value: the residual.
#
  value = yp - yo - ( tp - to ) * f ( tp, yp );

  return value

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

def unstable_backward_euler ( n ):

#*****************************************************************************80
#
## unstable_backward_euler() uses the backward Euler method on the unstable ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'unstable_backward_euler():' )
  print ( '  Solve the unstable ODE using backward_euler().' )

  mu, t0, y0, tstop = unstable_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, y = backward_euler ( unstable_deriv, tspan, y0, n )

  plt.clf ( )
  plt.plot ( t, y[:,0], 'r-', linewidth = 2 )
  plt.plot ( t, y[:,1], 'b-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- Y, dYdT --->' )
  plt.title ( 'unstable ODE solved by backward_euler()' )

  filename = 'unstable_backward_euler_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def unstable_deriv ( t, y ):

#*****************************************************************************80
#
## unstable_deriv() evaluates the derivative of the unstable ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(2): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2): the value of the derivative.
#
  import numpy as np

  mu, t0, y0, tstop = unstable_parameters ( )

  A = np.array ( [ \
    [          mu,  1.0 / mu ], \
    [  - 1.0 / mu,        mu ] ] )
 
  dydt = np.matmul ( A, y )

  return dydt

def unstable_exact ( t ):

#*****************************************************************************80
#
## unstable_exact() returns the exact solution of the unstable ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2021
#
#  Author:
#
#    John Burkardt
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

  mu, t0, y0, tstop = unstable_parameters ( )

  u = np.exp ( mu * t ) * ( np.cos ( t / mu ) - mu**2 * np.sin ( t / mu ) )

  v = mu * np.exp ( mu * t ) * (              np.cos ( t / mu ) \
    - mu**2 * np.sin ( t / mu ) ) \
    +      np.exp ( mu * t ) * ( - 1.0 / mu * np.sin ( t / mu ) \
    - mu    * np.cos ( t / mu ) )

  y = np.array ( [ u, v ] )

  return y

def unstable_midpoint ( n ):

#*****************************************************************************80
#
## unstable_midpoint() uses the midpoint method on the unstable ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'unstable_midpoint():' )
  print ( '  Solve the unstable ODE using midpoint().' )

  mu, t0, y0, tstop = unstable_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, y = midpoint ( unstable_deriv, tspan, y0, n )

  plt.clf ( )
  plt.plot ( t, y[:,0], 'r-', linewidth = 2 )
  plt.plot ( t, y[:,1], 'b-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- Y, dYdT --->' )
  plt.title ( 'unstable ODE solved by midpoint()' )

  filename = 'unstable_midpoint_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def unstable_ode_test ( ):

#*****************************************************************************80
#
## unstable_ode_test() tests unstable_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'unstable_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test unstable_ode().' )

  mu, t0, y0, tstop = unstable_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    mu    = ', mu )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 1200
  unstable_backward_euler ( n )

  unstable_midpoint ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'unstable_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def unstable_parameters ( mu_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## unstable_parameters() returns parameters for unstable_ode().
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
#    29 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU_USER: the parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real MU: the parameter.
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  if not hasattr ( unstable_parameters, "mu_default" ):
    unstable_parameters.mu_default = 0.1

  if not hasattr ( unstable_parameters, "t0_default" ):
    unstable_parameters.t0_default = 0.0

  if not hasattr ( unstable_parameters, "y0_default" ):
    unstable_parameters.y0_default = np.array ( [ 1.0, 0.0 ] )

  if not hasattr ( unstable_parameters, "tstop_default" ):
    unstable_parameters.tstop_default = 30.0
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( mu_user is not None ):
    unstable_parameters.mu_default = mu_user

  if ( t0_user is not None ):
    unstable_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    unstable_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    unstable_parameters.tstop_default = tstop_user
#
#  Return values.
#
  mu = unstable_parameters.mu_default
  t0 = unstable_parameters.t0_default
  y0 = unstable_parameters.y0_default
  tstop = unstable_parameters.tstop_default
  
  return mu, t0, y0, tstop

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
  unstable_ode_test ( )
  timestamp ( )

