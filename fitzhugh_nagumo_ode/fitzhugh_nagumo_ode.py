#! /usr/bin/env python3
#
def fitzhugh_nagumo_deriv ( t, y ):

#*****************************************************************************80
#
## fitzhugh_nagumo_deriv() returns right hand side of fitzhugh_nagumo_ode().
#
#  Discussion:
#
#    The parameter MU is defined by the function vanderpol_mu()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(2), the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2), the value of the derivative.
#
  import numpy as np

  a, b, c, d, t0, y0, tstop = fitzhugh_nagumo_parameters ( )

  v = y[0]
  w = y[1]

  dvdt = v - v**3 / 3.0 - w + d
  dwdt = ( v + a - b * w ) / c

  dydt = np.array ( [ dvdt, dwdt ] )

  return dydt

def fitzhugh_nagumo_solve_ivp ( ):

#*****************************************************************************80
#
## fitzhugh_nagumo_solve_ivp() calls solve_ivp() to solve fitzhugh_nagumo_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fitzhugh_nagumo_solve_ivp():' )
  print ( '  Solve fitzhugh_nagumo_ode() using solve_ivp().' )

  a, b, c, d, t0, y0, tstop = fitzhugh_nagumo_parameters ( )

  dydt = fitzhugh_nagumo_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( dydt, tspan, y0, t_eval = t )
#
#  Time plot of v(t), w(t).
#
  plt.plot ( t, sol.y[0], linewidth = 3 )
  plt.plot ( t, sol.y[1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- V(T), W(T) -->' )
  plt.title ( 'fitzhugh_nagumo_ode(): solve_ivp' )
  plt.legend ( ( 'v(t)', 'w(t)' ) )
  filename = 'fitzhugh_nagumo_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], linewidth = 3 )
  plt.plot ( sol.y[0,0], sol.y[1,0], 'g.', markersize = 40 )
  plt.plot ( sol.y[0,-1], sol.y[1,-1], 'r.', markersize = 30 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<-- V(T) -->' )
  plt.ylabel ( '<-- W(T) -->' )
  plt.title ( 'fitzhugh_nagumo_ode(): solve_ivp phase plot' )
  filename = 'fitzhugh_nagumo_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def fitzhugh_nagumo_ode_test ( ):

#*****************************************************************************80
#
## fitzhugh_nagumo_ode_test() solves fitzhugh_nagumo_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fitzhugh_nagumo_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve fitzhugh_nagumo_ode().' )
#
#  Get parameter values.
#
  a, b, c, d, t0, y0, tstop = fitzhugh_nagumo_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a     = ', a )
  print ( '    b     = ', b )
  print ( '    c     = ', c )
  print ( '    d     = ', d )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  fitzhugh_nagumo_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fitzhugh_nagumo_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def fitzhugh_nagumo_parameters ( a_user = None, b_user = None, c_user = None, \
  d_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## fitzhugh_nagumo_parameters() returns parameters of fitzhugh_nagumo_ode().
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
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER, B_USER, C_USER, D_USER: the parameters.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER(2): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A, B, C, D: the parameters.
#
#    real T0: the initial time.
#
#    real Y0(2): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
  if not hasattr ( fitzhugh_nagumo_parameters, "a_default" ):
    fitzhugh_nagumo_parameters.a_default = 0.7

  if not hasattr ( fitzhugh_nagumo_parameters, "b_default" ):
    fitzhugh_nagumo_parameters.b_default = 0.8

  if not hasattr ( fitzhugh_nagumo_parameters, "c_default" ):
    fitzhugh_nagumo_parameters.c_default = 12.5

  if not hasattr ( fitzhugh_nagumo_parameters, "d_default" ):
    fitzhugh_nagumo_parameters.d_default = 0.5

  if not hasattr ( fitzhugh_nagumo_parameters, "t0_default" ):
    fitzhugh_nagumo_parameters.t0_default = 0.0

  if not hasattr ( fitzhugh_nagumo_parameters, "y0_default" ):
    fitzhugh_nagumo_parameters.y0_default = np.array ( [ 0.0, 0.0 ] )

  if not hasattr ( fitzhugh_nagumo_parameters, "tstop_default" ):
    fitzhugh_nagumo_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    fitzhugh_nagumo_parameters.a_default = a_user

  if ( b_user is not None ):
    fitzhugh_nagumo_parameters.b_default = b_user

  if ( c_user is not None ):
    fitzhugh_nagumo_parameters.c_default = c_user

  if ( d_user is not None ):
    fitzhugh_nagumo_parameters.d_default = d_user

  if ( t0_user is not None ):
    fitzhugh_nagumo_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    fitzhugh_nagumo_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    fitzhugh_nagumo_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = fitzhugh_nagumo_parameters.a_default
  b = fitzhugh_nagumo_parameters.b_default
  c = fitzhugh_nagumo_parameters.c_default
  d = fitzhugh_nagumo_parameters.d_default
  t0 = fitzhugh_nagumo_parameters.t0_default
  y0 = fitzhugh_nagumo_parameters.y0_default
  tstop = fitzhugh_nagumo_parameters.tstop_default
  
  return a, b, c, d, t0, y0, tstop

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
  fitzhugh_nagumo_ode_test ( )
  timestamp ( )


