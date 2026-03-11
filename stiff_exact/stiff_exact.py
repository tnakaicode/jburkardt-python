#! /usr/bin/env python3
#
def stiff_exact_test ( ):

#*****************************************************************************80
#
## stiff_exact_test() tests stiff_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'stiff_exact_test()' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test stiff_exact(), which evaluates exact solutions' )
  print ( '  of the stiff ODE.' )

  lamda, t0, y0, tstop = stiff_parameters ( )
  print ( '' )
  print ( '  parameters:' )
  print ( '    lamda = ', lamda )
  print ( '    t0     = ', t0 )
  print ( '    y0     = ', y0 )
  print ( '    tstop  = ', tstop )

  stiff_value ( )

  stiff_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'stiff_exact_test():' )
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
#    15 June 2025
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

  dydt = lamda * ( np.cos ( t - t0 ) - y )

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
#    15 June 2025
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

  mu = y0 - lamda**2 / ( lamda**2 + 1.0 )

  value = lamda    * np.sin ( t - t0 ) / ( lamda**2 + 1.0 ) \
        + lamda**2 * np.cos ( t - t0 ) / ( lamda**2 + 1.0 ) \
        + mu * np.exp ( - lamda * ( t - t0 ) )

  return value

def stiff_solve_ivp ( ):

#*****************************************************************************80
#
## stiff_solve_ivp() solves the stiff ODE using solve_ivp().
#
#  Discussion:
#
#    y' = lamda * ( cos(t-t0) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2025
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Retrieve default values.
#
  lamda, t0, y0, tstop = stiff_parameters ( ) 
#
#  Default with t0 = 0, y0 = 0.
#
  t0 = 0.0
  y0 = 0.0
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  tspan = np.array ( [ t0, tstop ] )
  sol1 = solve_ivp ( stiff_deriv, tspan,  [ y0 ] )
#
#  Try t0=0, y0=0.9.
#
  t0 = 0.0
  y0 = 0.9
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  tspan = np.array ( [ t0, tstop ] )
  sol2 = solve_ivp ( stiff_deriv, tspan, [ y0 ] )
#
#  Try t0=0, y0=1.5.
#
  t0 = 0.0
  y0 = 1.5
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  tspan = np.array ( [ t0, tstop ] )
  sol3 = solve_ivp ( stiff_deriv, tspan, [ y0 ] )
#
# t0 = 0.25, y0 = 0.5
#
  t0 = 0.25
  y0 = 0.5
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  tspan = np.array ( [ t0, tstop ] )
  sol4 = solve_ivp ( stiff_deriv, tspan, [ y0 ] )
#
#  Plot them.
#
  plt.clf()
  plt.plot ( sol1.t, sol1.y[0], linewidth = 2 )
  plt.plot ( sol2.t, sol2.y[0], linewidth = 2 )
  plt.plot ( sol3.t, sol3.y[0], linewidth = 2 )
  plt.plot ( sol4.t, sol4.y[0], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y(t)  --->' )
  plt.title ( 'stiff ODE with solve_ivp()' )
  plt.legend ( [ '(0,0)', '(0,0.9)', '(0,1.5)', '(0.25,0.5)' ] )
  filename = 'stiff_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def stiff_parameters ( lamda_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## stiff_parameters() returns parameters of the stiff ODE.
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
#    15 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real lamda_USER: a parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real lamda: a parameter.
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#

#
#  Initialize defaults.
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
#  Update defaults if input was supplied.
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
#  Return values.
#
  lamda = stiff_parameters.lamda_default
  t0 = stiff_parameters.t0_default
  y0 = stiff_parameters.y0_default
  tstop = stiff_parameters.tstop_default

  return lamda, t0, y0, tstop

def stiff_value ( ):

#*****************************************************************************80
#
## stiff_value() evaluates the exact solution for various initial conditions.
#
#  Discussion:
#
#    y' = lamda * ( cos(t-t0) - y )
#    y(t0) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  nt = 101
#
#  Retrieve default values.
#
  lamda, t0, y0, tstop = stiff_parameters ( ) 
#
#  Default with t0 = 0, y0 = 0.
#
  t0 = 0.0
  y0 = 0.0
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  t1 = np.linspace ( t0, tstop, nt )
  y1 = stiff_exact ( t1 )
#
#  Try t0=0, y0=0.9.
#
  t0 = 0.0
  y0 = 0.9
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  t2 = np.linspace ( t0, tstop, nt )
  y2 = stiff_exact ( t2 )
#
#  Try t0=0, y0=1.5.
#
  t0 = 0.0
  y0 = 1.5
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  t3 = np.linspace ( t0, tstop, nt )
  y3 = stiff_exact ( t3 )
#
# t0 = 0.25, y0 = 0.5
#
  t0 = 0.25
  y0 = 0.5
  lamda, t0, y0, tstop = stiff_parameters ( lamda, t0, y0, tstop )
  t4 = np.linspace ( t0, tstop, nt )
  y4 = stiff_exact ( t4 )
#
#  Plot them.
#
  plt.clf ( )
  plt.plot ( t1, y1, linewidth = 2 )
  plt.plot ( t2, y2, linewidth = 2 )
  plt.plot ( t3, y3, linewidth = 2 )
  plt.plot ( t4, y4, linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y(t)  --->' )
  plt.title ( 'stiff exact solution' )
  plt.legend ( [ '(0,0)', '(0,0.9)', '(0,1.5)', '(0.25,0.5)' ] )
  filename = 'stiff_value.png'
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
  stiff_exact_test ( )
  timestamp ( )


