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

def ripple_deriv ( t, y ):

#*****************************************************************************80
#
## ripple_deriv() evaluates the derivative of ripple_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Ripples and Hyperbolas,
#    https://www.johndcook.com/blog/2020/11/06/ripples-and-hyperbolas/
#    Posted 06 November 2020.
#
#    Wendell Mills, Boris Weisfeiler, Allan Krall,
#    Discovering Theorems with a Computer: The Case of y‘ = sin(xy). 
#    The American Mathematical Monthly, 
#    Volume 86, Number 9, November 1979, pages 733-739.
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT: the value of the derivative.
#
  import numpy as np

  dydt = np.sin ( t * y )

  return dydt

def ripple_euler ( n ):

#*****************************************************************************80
#
## ripple_euler() solves ripple_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Ripples and Hyperbolas,
#    https://www.johndcook.com/blog/2020/11/06/ripples-and-hyperbolas/
#    Posted 06 November 2020.
#
#    Wendell Mills, Boris Weisfeiler, Allan Krall,
#    Discovering Theorems with a Computer: The Case of y‘ = sin(xy). 
#    The American Mathematical Monthly, 
#    Volume 86, Number 9, November 1979, pages 733-739.
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ripple_euler()' )
  print ( '  Use euler() to solve ripple_ode().' )

  t0, y0, tstop = ripple_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  f = ripple_deriv
#
#  Plot the solution curve.
#
  for i in range ( 1, 8 ):

    y0 = float ( i )

    t, y = euler ( f, tspan, y0, n )
    plt.plot ( t, y, 'r-', linewidth = 3 )

  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X(T) --->'  )
  plt.title ( 'ripple_ode() euler: time plot' )
  filename = 'ripple_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def ripple_ode_test ( ):

#*****************************************************************************80
#
## ripple_ode_test() tests ripple_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ripple_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  ripple_ode() models an equation with ripples and hyperbolas.' )

  t0, y0, tstop = ripple_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  n = 1000
  ripple_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'ripple_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def ripple_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## ripple_parameters() returns parameters for ripple_ode().
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
  if not hasattr ( ripple_parameters, "t0_default" ):
    ripple_parameters.t0_default = 0.0

  if not hasattr ( ripple_parameters, "y0_default" ):
    ripple_parameters.y0_default = 7.0

  if not hasattr ( ripple_parameters, "tstop_default" ):
    ripple_parameters.tstop_default = 25.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    ripple_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    ripple_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    ripple_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = ripple_parameters.t0_default
  y0 = ripple_parameters.y0_default
  tstop = ripple_parameters.tstop_default
  
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
  ripple_ode_test ( )
  timestamp ( )

