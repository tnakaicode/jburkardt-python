#! /usr/bin/env python3
#
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

def stiff_theta_method ( tspan, y0, n, theta ):

#*****************************************************************************80
#
## stiff_theta_method(): theta method + fsolve() on the stiff ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2022
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
  print ( 'stiff_theta_method():' )
  print ( '  Solve stiff ODE using the theta method + fsolve().' )
  print ( '  Using theta = ', theta )

  f = stiff_deriv
  t1, y1 = theta_method ( f, tspan, y0, n, theta )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'ro-', t2, y2, 'b-', 'linewidth', 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  label = 'stiff_ode(): theta_method, theta = ' + str ( theta )
  plt.title ( label )
  plt.legend ( [ 'Computed', 'Exact' ] )

  filename = 'stiff_theta_method_fixed_' + str ( theta ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def theta_method ( f, tspan, y0, n, theta ):

#*****************************************************************************80
#
## theta_method() uses the theta method method + fsolve() to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2022
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
#    real theta: the value of theta.
#    0 <= theta <= 1.
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

    tn = to + dt 
    yn = yo + dt * f ( to, yo )

    yn = fsolve ( theta_residual, yn, args = ( f, to, yo, tn, theta ) )

    t[i+1] = tn
    y[i+1,:] = yn.copy()

  return t, y

def theta_residual ( yn, f, to, yo, tn, theta ):

#*****************************************************************************80
#
## theta_residual() evaluates the theta method residual.
#
#  Discussion:
#
#    We are seeking a value YN defined by the implicit equation:
#
#      YN = YO + ( tn - to ) 
#        * ( theta * F ( TO, YO ) + ( 1.0 - theta ) * F ( TN, YN ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yn: the new solution value.
#
#    function handle f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real tn: the new time value.
#
#    real theta: the value of theta.
#    0 <= theta <= 1.
#
#  Output:
#
#    real value: the theta method residual.
#
  value = yn - yo - ( tn - to ) \
    * ( theta * f ( to, yo ) + ( 1.0 - theta ) * f ( tn, yn ) )

  return value

def theta_method_test ( ):

#*****************************************************************************80
#
## theta_method_test() tests theta_method().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'theta_method_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test theta method().' )
  print ( '  We use a constant stepsize.' )

  lamda, t0, y0, tstop = stiff_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    lamda = ', lamda )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  tspan = np.array ( [ 0.0, 1.0 ] )
  n = 27
  for theta in [ 0.0, 0.5, 1.0 ]:
    stiff_theta_method ( tspan, y0, n, theta )
#
#  Terminate.
#
  print ( '' )
  print ( 'theta_method_test():' )
  print ( '  Normal end of execution.' )

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
  theta_method_test ( )
  timestamp ( )

