#! /usr/bin/env python3
#
def lindberg_deriv ( t, y ):

#*****************************************************************************80
#
## lindberg_deriv() returns the derivative for lindberg_ode().
#
#  Discussion:
#
#    Note that components y1(t) and y2(t) first sink to extraordinarily
#    small values, and then undergo explosive growth, sometime before t=1.
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
#  Reference:
#
#    Bengt Lindberg,
#    On a dangerous property of methods for stiff differential equations,
#    BIT Numerical Mathematics,
#    Volume 14, 1974, pages 430-436.
#
#    Daniel Watanabe, Qasim Sheikh,
#    One-leg formulas for stiff ordinary differential equations,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 5, Number 2, June 1984, pages 489-496.
#
#  Input:
#
#    real T: the current time.
#
#    real Y(4): the current solution value.
#
#  Output:
#
#    real DYDT(4): the value of dY/dT.
#
  import numpy as np

  y1 = y[0]
  y2 = y[1]
  y3 = y[2]
  y4 = y[3]

  dydt = np.zeros ( 4 )

  dydt[0] =   10.0**4 * y1 * y3 + 10.0**4 * y2 * y4  
  dydt[1] = - 10.0**4 * y1 * y4 + 10.0**4 * y2 * y3 
  dydt[2] = 1.0 - y3
  dydt[3] = - 0.5 * y3 - y4 + 0.5
 
  return dydt

def lindberg_exact ( x ):

#*****************************************************************************80
#
## lindberg_exact() evaluates the exact solution of lindberg_ode().
#
#  Discussion:
#
#    The formula was supplied by Wenlong Pei.
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
#    real x(n): the evaluation points.
#
#  Output:
#
#    real y(n,4): the function values.
#
  import numpy as np

  n = x.shape[0]
  y = np.zeros ( [ n, 4 ] )
  g1 = 10.0**4 * ( x + 2.0 * np.exp ( - x ) - 2.0 )
  g2 = 10.0**4 * ( 1.0 - np.exp ( - x ) - x * np.exp ( -x ) )

  y[:,0] = np.exp ( g1 ) * ( np.cos ( g2 ) + np.sin ( g2 ) )
  y[:,1] = np.exp ( g1 ) * ( np.cos ( g2 ) - np.sin ( g2 ) )
  y[:,2] = 1.0 - 2.0 * np.exp ( - x )
  y[:,3] = x * np.exp ( - x )
 
  return y

def lindberg_solve_ivp ( ):

#*****************************************************************************80
#
## lindberg_solve_ivp() solves lindberg_ode() using solve_ivp().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lindberg_solve_ivp():' )
  print ( '  Solve lindberg_ode() using solve_ivp().' )

  t0, y0, tstop = lindberg_parameters ( )

  f = lindberg_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )
#
#  Because this is a stiff problem, options are BDF, Radau, LSODA.
#
  sol = solve_ivp ( f, tspan, y0, t_eval = t, method = 'Radau' )

  y2 = lindberg_exact ( t )

  plt.clf ( )
  plt.plot ( t, sol.y[0], 'ro', linewidth = 3 )
  plt.plot ( t, y2[:,0], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y1(t) -->' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  plt.title ( 'lindberg_ode(): solve_ivp y1' )
  filename = 'lindberg_solve_ivp_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, sol.y[1], 'ro', linewidth = 3 )
  plt.plot ( t, y2[:,1], 'b-',linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y2(t) -->' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  plt.title ( 'lindberg_ode(): solve_ivp y2' )
  filename = 'lindberg_solve_ivp_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, sol.y[2], 'ro', linewidth = 3 )
  plt.plot ( t, y2[:,2], 'b-',linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y3(t) -->' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  plt.title ( 'lindberg_ode(): solve_ivp y3' )
  filename = 'lindberg_solve_ivp_y3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, sol.y[3], 'ro', linewidth = 3 )
  plt.plot ( t, y2[:,3], 'b-',linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y4(t) -->' )
  plt.legend (  [ 'Computed', 'Exact' ] )
  plt.title ( 'lindberg_ode(): solve_ivp y4' )
  filename = 'lindberg_solve_ivp_y4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def lindberg_ode_test ( ):

#*****************************************************************************80
#
## lindberg_ode_test() tests lindberg_ode().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lindberg_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve lindberg_ode().' )

  t0, y0, tstop = lindberg_parameters ( )
#
#  Reduce the stopping time to 0.55.  
#  By the default stopping time of 1.0, the solution has catastrophically exploded.
#
  tstop = 0.55
  t0, y0, tstop = lindberg_parameters ( t0, y0, tstop )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  lindberg_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lindberg_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def lindberg_parameters ( t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## lindberg_parameters() returns the parameters of lindberg_ode().
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
#    real Y0_USER(4): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0(4): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( lindberg_parameters, "t0_default" ):
    lindberg_parameters.t0_default = 0.0

  if not hasattr ( lindberg_parameters, "y0_default" ):
    lindberg_parameters.y0_default = np.array ( [ 1.0, 1.0, -1.0, 0.0 ] )

  if not hasattr ( lindberg_parameters, "tstop_default" ):
    lindberg_parameters.tstop_default = 3.91
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    lindberg_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    lindberg_parameters.y0_default = y0_user.copy()

  if ( tstop_user is not None ):
    lindberg_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = lindberg_parameters.t0_default
  y0 = lindberg_parameters.y0_default.copy ( )
  tstop = lindberg_parameters.tstop_default
  
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

if ( __name__ == "__main__" ):
  timestamp ( )
  lindberg_ode_test ( )
  timestamp ( )

