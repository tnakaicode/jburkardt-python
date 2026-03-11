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

def quadex_backward_euler ( n ):

#*****************************************************************************80
#
## quadex_backward_euler() applies backward_euler() to quadex_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2020
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

  t0, y0, tstop = quadex_parameters ( )

  dydt = quadex_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = backward_euler ( dydt, tspan, y0, n )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = quadex_exact ( t2 )

  plt.plot ( t1, y1, 'r-', t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  s = ( 'quadex_ode(), backward euler method, n = %d' % ( n ) )
  plt.title ( s )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = ( 'quadex_backward_euler_%d.png' % ( n ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def quadex_deriv ( t, y ):

#*****************************************************************************80
#
## quadex_deriv() evaluates the right hand side of quadex_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:), Y(:), the arguments of the derivative.
#
#  Output:
#
#    real DYDT(:), the value of the derivative.
#
  dydt = 5.0 * ( y - t**2 )

  return dydt

def quadex_euler ( n ):

#*****************************************************************************80
#
## quadex_euler() applies euler() to quadex_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2020
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

  t0, y0, tstop = quadex_parameters ( )

  dydt = quadex_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = euler ( dydt, tspan, y0, n )

  t2 = np.linspace ( t0, tstop, 101 )
  y2 = quadex_exact ( t2 )

  plt.plot ( t1, y1, 'r-', t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  s = ( 'quadex_ode(), euler method, n = %d' % ( n ) )
  plt.title ( s )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = ( 'quadex_euler_%d.png' % ( n ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def quadex_exact ( t ):

#*****************************************************************************80
#
## quadex_exact() evaluates the exact solution of quadex_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the evaluation time.
#
#  Output:
#
#    real VALUE, the solution at the given time.
#
  import numpy as np

  c = 0.0
  value = c * np.exp ( 5.0 * t ) + t**2 + 2.0 * t / 5.0 + 2.0 / 25.0

  return value

def quadex_ode_test ( ):

#*****************************************************************************80
#
## quadex_ode_test() tests quadex_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'quadex_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  quadex_ode() is a stiff ODE with a quadratic solution.' )

  t0, y0, tstop = quadex_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 2500
  quadex_euler ( n )

  n = 2500
  quadex_backward_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'quadex_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def quadex_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## quadex_parameters() returns parameters for quadex_ode().
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
  if not hasattr ( quadex_parameters, "t0_default" ):
    quadex_parameters.t0_default = 0.0

  if not hasattr ( quadex_parameters, "y0_default" ):
    quadex_parameters.y0_default = 2.0 / 25.0

  if not hasattr ( quadex_parameters, "tstop_default" ):
    quadex_parameters.tstop_default = 2.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    quadex_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    quadex_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    quadex_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = quadex_parameters.t0_default
  y0 = quadex_parameters.y0_default
  tstop = quadex_parameters.tstop_default
  
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
  quadex_ode_test ( )
  timestamp ( )

