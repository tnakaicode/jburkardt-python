#! /usr/bin/env python3
#
def cauchy_fixed ( f, tspan, y0, n, theta ):

#*****************************************************************************80
#
## cauchy_fixed() uses the Cauchy method + fixed point to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle f: evaluates the right hand side of the ODE.  
#
#    real tspan(2): the starting and ending times.
#
#    real y0(m): the initial conditions. 
#
#    integer n: the number of steps.
#
#    real theta: the value of theta, 0 < theta <= 1.
#
#  Output:
#
#    real t(n+1,1), y(n+1,m): the solution estimates.
#
  import numpy as np

  m = len ( y0 )
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  it_max = 10

  t[0] = tspan[0]
  y[0,:] = y0.copy ( )

  for i in range ( 0, n ):
    xm = t[i] + theta * dt 
    ym = y[i,:]
    for j in range ( 0, it_max ):
      ym = y[i,:] + theta * dt * f ( xm, ym )
    t[i+1] = t[i] + dt
    y[i+1,:] = (       1.0 / theta ) * ym \
             + ( 1.0 - 1.0 / theta ) * y[i,:]

  return t, y

def cauchy_fsolve ( f, tspan, y0, n, theta ):

#*****************************************************************************80
#
## cauchy_fsolve() uses the Cauchy method + fsolve() to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle f: evaluates the right hand side of the ODE.  
#
#    real tspan(2): the starting and ending times.
#
#    real y0(m): the initial conditions. 
#
#    integer n: the number of steps.
#
#    real theta: the value of theta, 0 < theta <= 1.
#
#  Output:
#
#    real t(n+1,1), y(n+1,m): the solution estimates.
#
  from scipy.optimize import fsolve
  import numpy as np

  m = len ( y0 )
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  t[0] = tspan[0]
  y[0,:] = y0.copy ( )

  for i in range ( 0, n ):

    to = t[i]
    yo = y[i,:]

    tc = to + theta * dt 
    yc = yo + theta * dt * f ( to, yo )
    yc = fsolve ( backward_euler_residual, yc, args = ( f, to, yo, tc ) )

    tp = to + dt
    yp = ( yc + ( theta - 1.0 ) * yo ) / theta

    t[i+1] = tp
    y[i+1,:] = yp.copy()

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
  value = yp - yo - ( tp - to ) * f ( tp, yp )

  return value

def cauchy_method_test ( ):

#*****************************************************************************80
#
## cauchy_method_test() tests cauchy_method().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cauchy_method_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cauchy_method().' )
  print ( '  We use a constant stepsize.' )

  lamda, t0, y0, tstop = stiff_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    lamda = ', lamda )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  tspan = np.array ( [ 0.0, 1.0 ] )
  n = 40

  for theta in [ 0.25, 0.5, 0.75 ]:
    stiff_cauchy_fixed_test ( tspan, y0, n, theta )

  for theta in [ 0.25, 0.5, 0.75 ]:
    stiff_cauchy_fsolve_test ( tspan, y0, n, theta )
#
#  Terminate.
#
  print ( '' )
  print ( 'cauchy_method_test():' )
  print ( '  Normal end of execution.' )

  return

def stiff_cauchy_fixed_test ( tspan, y0, n, theta ):

#*****************************************************************************80
#
## stiff_cauchy_fixed_test(): Cauchy method + fixed point on the stiff ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TSPAN(2): the first and last times.
#
#    real Y0: the initial condition.
#
#    integer N: the number of steps to take.
#
#    real THETA: the value of theta
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stiff_cauchy_fixed_test()' )
  print ( '  Solve stiff ODE using the Cauchy method + fixed point.' )
  print ( '  Using theta =', theta )

  f = stiff_deriv
  t1, y1 = cauchy_fixed ( f, tspan, y0, n, theta )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'ro-', t2, y2, 'b-', 'linewidth', 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  label = 'stiff_ode(): cauchy_fixed, theta = ' + str ( theta )
  plt.title ( label )
  plt.legend ( [ 'Computed', 'Exact' ] )

  filename = 'stiff_cauchy_fixed_' + str ( theta ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_cauchy_fsolve_test ( tspan, y0, n, theta ):

#*****************************************************************************80
#
## stiff_cauchy_fsolve_test: Cauchy method + fsolve() on the stiff ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TSPAN(2): the first and last times.
#
#    real Y0: the initial condition.
#
#    integer N: the number of steps to take.
#
#    real THETA: the value of theta
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stiff_cauchy_fsolve_test():' )
  print ( '  Solve stiff ODE using the Cauchy method + fsolve().' )
  print ( '  Using theta = ', theta )

  f = stiff_deriv
  t1, y1 = cauchy_fsolve ( f, tspan, y0, n, theta )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'ro-', t2, y2, 'b-', 'linewidth', 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  label = 'stiff_ode(): cauchy_fsolve, theta = ' + str ( theta )
  plt.title ( label )
  plt.legend ( [ 'Computed', 'Exact' ] )

  filename = 'stiff_cauchy_fsolve_' + str ( theta ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

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
#    04 May 2021
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
  import numpy as np
#
#  Initialize the default values.
#
  if not ( hasattr ( stiff_parameters, "lamda_default" ) ):
    stiff_parameters.lamda_default = 50.0

  if not ( hasattr ( stiff_parameters, "t0_default" ) ):
    stiff_parameters.t0_default = 0.0

  if not ( hasattr ( stiff_parameters, "y0_default" ) ):
    stiff_parameters.y0_default = np.array ( [ 0.0 ] )

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
  cauchy_method_test ( )
  timestamp ( )

