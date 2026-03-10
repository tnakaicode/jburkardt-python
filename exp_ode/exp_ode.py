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
#    real value: the backward Euler residual.
#
  value = yp - yo - ( tp - to ) * f ( tp, yp );

  return value

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

def exp_backward_euler_test ( n ):

#*****************************************************************************80
#
## exp_backward_euler() uses the backward Euler method on exp_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2020
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
  print ( 'exp_backward_euler_test():' )
  print ( '  Solve exp_ode() using the backward Euler method.' )

  alpha, t0, y0, tstop = exp_parameters ( )

  f = exp_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = backward_euler ( f, tspan, y0, n )

  print ( '  Number of equal steps n = ', n )

  y2 = exp_exact ( t1 )
  e = rms ( y1[:,0] - y2 )
  print ( '  RMS error norm = ', e )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = exp_exact ( t2 )

  plt.plot ( t1, y1, 'r-o', t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'exp_ode(): backward_euler method' )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = 'exp_backward_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def exp_deriv ( t, y ):

#*****************************************************************************80
#
## exp_deriv() evaluates the right hand side of exp_ode().
#
#  Discussion:
#
#    y' = alpha * y
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2020
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
  alpha, t0, y0, tstop = exp_parameters ( )

  dydt = alpha * y

  return dydt

def exp_euler_test ( n ):

#*****************************************************************************80
#
## exp_euler() uses euler() on exp_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2020
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
  print ( 'exp_euler_test()' )
  print ( '  Solve exp_ode() using euler().' )

  alpha, t0, y0, tstop = exp_parameters ( )

  f = exp_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = euler ( f, tspan, y0, n )

  print ( '  Number of equal steps n = ', n )
  y2 = exp_exact ( t1 )
  e = rms ( y1[:,0] - y2 )
  print ( '  RMS error norm = ', e )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = exp_exact ( t2 )

  plt.clf ( )
  plt.plot ( t1, y1, 'r-o', t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'exp_ode(): Euler method' )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = 'exp_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def exp_exact ( t ):

#*****************************************************************************80
#
## exp_exact() evaluates the exact solution of exp_ode().
#
#  Discussion:
#
#    y' = alpha * y
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2020
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

  alpha, t0, y0, tstop = exp_parameters ( )

  value = y0 * np.exp ( alpha * ( t - t0 ) )

  return value

def exp_midpoint_test ( n ):

#*****************************************************************************80
#
## exp_midpoint() uses midpoint() on exp_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2020
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
  print ( 'exp_midpoint_test():' )
  print ( '  Solve exp_ode() using midpoint().' )

  alpha, t0, y0, tstop = exp_parameters ( )

  f = exp_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = midpoint ( f, tspan, y0, n )

  print ( '  Number of equal steps n = ', n )
  y2 = exp_exact ( t1 )
  e = rms ( y1[:,0] - y2 )
  print ( '  RMS error norm = ', e )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = exp_exact ( t2 )

  plt.plot ( t1, y1, 'r-o', t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'exp_ode(): midpoint method' )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = 'exp_midpoint.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def exp_ode_test ( ):

#*****************************************************************************80
#
## exp_ode_test() tests exp_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'exp_ode_test' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve exp_ode().' )

  alpha, t0, y0, tstop = exp_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 80
  exp_euler_test ( n )

  n = 80
  exp_backward_euler_test ( n )

  n = 20
  exp_midpoint_test ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'exp_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def exp_parameters ( alpha_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## exp_parameters() returns parameters for exp_ode().
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
#    04 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA_USER: the coefficient.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ALPHA: the coefficient.
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
  if not hasattr ( exp_parameters, "alpha_default" ):
    exp_parameters.alpha_default = 1.0

  if not hasattr ( exp_parameters, "t0_default" ):
    exp_parameters.t0_default = 0.0

  if not hasattr ( exp_parameters, "y0_default" ):
    exp_parameters.y0_default = 1.0

  if not hasattr ( exp_parameters, "tstop_default" ):
    exp_parameters.tstop_default = 5.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    exp_parameters.alpha_default = alpha_user

  if ( t0_user is not None ):
    exp_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    exp_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    exp_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = exp_parameters.alpha_default
  t0 = exp_parameters.t0_default
  y0 = exp_parameters.y0_default
  tstop = exp_parameters.tstop_default
  
  return alpha, t0, y0, tstop

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
#    21 October 2020
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

def rms ( a ):

#*****************************************************************************80
#
## rms() returns the RMS norm of a vector.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = sqrt ( 1/N * sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N), the vector whose norm is desired.
#
#  Output:
#
#    real VALUE, the RMS norm of A.
#
  import numpy as np

  n = a.shape[0]
  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i]**2
  value = np.sqrt ( value / n )

  return value

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
  exp_ode_test ( )
  timestamp ( )

