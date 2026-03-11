#! /usr/bin/env python3
#
def tough_deriv ( t, y ):

#*****************************************************************************80
#
## tough_deriv() returns the right hand side of tough_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Syvert Norsett, Gerhard Wanner,
#    Solving Ordinary Differential Equations, I: Nonstiff Problems,
#    Springer, 1987.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(4), the current state values.
#
#  Output:
#
#    real DYDT(4), the time derivatives of the current state values.
#
  import numpy as np

  y1 = y[0]
  y2 = y[1]
  y3 = y[2]
  y4 = y[3]

  dy1dt = 2.0 * t * y2**0.2 * y4
  dy2dt = 10.0 * t * np.exp ( 5.0 * ( y2 - 1.0 ) ) * y4
  dy3dt = 2.0 * t * y4
  dy4dt = - 2.0 * t * np.log ( y1 )

  dydt = np.array ( [ dy1dt, dy2dt, dy3dt, dy4dt ] )

  return dydt

def tough_exact ( t ):

#*****************************************************************************80
#
## tough_exact() returns the exact solution for tough_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Syvert Norsett, Gerhard Wanner,
#    Solving Ordinary Differential Equations, I: Nonstiff Problems,
#    Springer, 1987.
#
#  Input:
#
#    real T(:): the current time.
#
#  Output:
#
#    real Y(4): the exact solution.
#
  import numpy as np

  y1 = np.exp ( np.sin ( t**2 ) )
  y2 = np.exp ( 5.0 * np.sin ( t**2 ) )
  y3 = np.sin ( t**2 ) + 1.0
  y4 = np.cos ( t**2 )

  y = np.array ( [ y1, y2, y3, y4 ] )

  return y

def tough_ode_test ( ):

#*****************************************************************************80
#
## tough_ode_test() tests tough_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tough_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve tough_ode().' )

  t0, y0, tstop = tough_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  tough_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'tough_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def tough_parameters ( t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## tough_parameters() returns parameters for tough_ode().
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
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time, in seconds
#
#    real Y0_USER(4): the initial values.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time, in seconds
#
#    real Y0(4): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( tough_parameters, "t0_default" ):
    tough_parameters.t0_default = 0.0

  if not hasattr ( tough_parameters, "y0_default" ):
    tough_parameters.y0_default = np.array ( [ 1.0, 1.0, 1.0, 1.0 ] )

  if not hasattr ( tough_parameters, "tstop_default" ):
    tough_parameters.tstop_default = 3.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    tough_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    tough_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    tough_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = tough_parameters.t0_default
  y0 = tough_parameters.y0_default
  tstop = tough_parameters.tstop_default
  
  return t0, y0, tstop

def tough_solve_ivp ( ):

#*****************************************************************************80
#
## tough_solve_ivp() solves tough_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'tough_solve_ivp():' )
  print ( '  Solve tough_ode() using solve_ivp().' )

  t0, y0, tstop = tough_parameters ( )

  f = tough_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )
#
#  LSODA is one of the few options which at least provides some output,
#  although it very quickly fails.
#
  sol = solve_ivp ( f, tspan, y0, method = 'LSODA', t_eval = t )

  print ( 'sol.status = ', sol.status )

  ye = tough_exact ( t )
#
#  Plot y1.
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'ro', linewidth = 2 )
  plt.plot ( t, ye[0], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Y1(t) -->' )
  plt.title ( 'tough_ode() solve_ivp: y1-' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'tough_solve_ivp_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot y2.
#
  plt.clf ( )
  plt.plot ( t, sol.y[1], 'ro', linewidth = 2 )
  plt.plot ( t, ye[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Y2(t) -->' )
  plt.title ( 'tough_ode() solve_ivp: y2' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'tough_solve_ivp_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Plot y3.
#
  plt.clf ( )
  plt.plot ( t, sol.y[2], 'ro', linewidth = 2 )
  plt.plot ( t, ye[2], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Y3(t) -->' )
  plt.title ( 'tough_ode() solve_ivp: y3' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'tough_solve_ivp_y3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot y4.
#
  plt.clf ( )
  plt.plot ( t, sol.y[3], 'ro', linewidth = 2 )
  plt.plot ( t, ye[3], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Y4(t) -->' )
  plt.title ( 'tough_ode() solve_ivp: y4' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'tough_solve_ivp_y4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
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
  tough_ode_test ( )
  timestamp ( )

