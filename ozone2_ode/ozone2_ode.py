#! /usr/bin/env python3
#
def ozone2_conserved ( y ):

#*****************************************************************************80
#
## ozone2_conserved() evaluates a quantity that should be conserved.
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
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    real Y(4): the current solution.
#
#  Output:
#
#    real H: the conserved quantity.
#
  y1 = y[0]
  y2 = y[1]
  y3 = y[2]
  y4 = y[3]

  h = y1 + y3 + y4

  return h

def ozone2_deriv ( t, y ):

#*****************************************************************************80
#
## ozone2_deriv() evaluates the derivative of ozone2_ode().
#
#  Discussion:
#
#    u1 = O
#    u2 = NO
#    u3 = NO2
#    u4 = O3
#    sigma = NO2 source term
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
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time dependent advection-diffusion-reaction equations,
#    Springer, 2003,
#    ISBN13: 978-3-662-09017-6.
#
#  Input:
#
#    real T, Y(4): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(4): the value of the derivative.
#
  import numpy as np

  k1 = ozone2_k1 ( t )
  k2, k3, sigma2, t0, y0, tstop = ozone2_parameters ( )

  y1 = y[0]
  y2 = y[1]
  y3 = y[2]
  y4 = y[3]

  dy1dt = + k1 * y3 - k2 * y1
  dy2dt = + k1 * y3           - k3 * y2 * y4 + sigma2
  dy3dt = - k1 * y3           + k3 * y2 * y4
  dy4dt =           + k2 * y1 - k3 * y2 * y4

  dydt = np.array ( [ dy1dt, dy2dt, dy3dt, dy4dt ] )

  return dydt

def ozone2_k1 ( t ):

#*****************************************************************************80
#
## ozone2_k1() evaluates rate coefficient k1 for ozone2_ode().
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
#    real T: the current time, in seconds from sunrise.
#
#  Output:
#
#    real K1: the rate coefficient.
#
  import numpy as np

  t_hours = t / 3600.0
  hour = ( t_hours % 24.0 )

  if ( 4.0 <= hour and hour <= 20.0 ):
    t_bar = t_hours - 24 * np.floor ( t_hours / 24.0 )
    s = ( np.sin ( np.pi * ( t_bar - 4.0 ) / 16.0 ) ) ** 0.2
    k1 = 1.0E-05 * np.exp ( 7.0 * s )
  else:
    k1 = 1.0E-40

  return k1

def ozone2_ode_test ( ):

#*****************************************************************************80
#
## ozone2_ode_test() solves ozone2_ode().
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
  print ( 'ozone2_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve ozone2_ode().' )

  k2, k3, sigma2, t0, y0, tstop = ozone2_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    k2     = ', k2 )
  print ( '    k3     = ', k3 )
  print ( '    sigma2 = ', sigma2 )
  print ( '    t0     = ', t0 )
  print ( '    y0     = ', y0 )
  print ( '    tstop  = ', tstop )

  ozone2_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ozone_ode_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def ozone2_parameters ( k2_user = None, k3_user = None, sigma2_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## ozone2_parameters() returns parameters for ozone2_ode().
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
#    real K2_USER, K3_USER: rate parameters
#
#    real SIGMA2_USER, nitrogen oxide source term.
#
#    real T0_USER: the initial time, in seconds.
#
#    real Y0_USER[4]: the initial condition.
#
#    real TSTOP_USER: the final time, in seconds.
#
#  Output:
#
#    real K2, K3: rate parameters
#
#    real SIGMA2, nitrogen oxide source term.
#
#    real T0: the initial time, in seconds.
#
#    real Y0[4]: the initial condition.
#
#    real TSTOP: the final time, in seconds.
#
  import numpy as np

  if not hasattr ( ozone2_parameters, "k2_default" ):
    ozone2_parameters.k2_default = 1.0E+5

  if not hasattr ( ozone2_parameters, "k3_default" ):
    ozone2_parameters.k3_default = 1.0E-16

  if not hasattr ( ozone2_parameters, "sigma2_default" ):
    ozone2_parameters.sigma2_default = 1.0E+6

  if not hasattr ( ozone2_parameters, "t0_default" ):
    ozone2_parameters.t0_default = 14400.0

  if not hasattr ( ozone2_parameters, "y0_default" ):
    ozone2_parameters.y0_default = np.array ( [ 0.0, 1.3E+10, 5.0E+11, 8.0E+11 ] )

  if not hasattr ( ozone2_parameters, "tstop_default" ):
    ozone2_parameters.tstop_default = 504000.0
#
#  Update defaults if input was supplied.
#
  if ( k2_user is not None ):
    ozone2_parameters.k2_default = k2_user

  if ( k3_user is not None ):
    ozone2_parameters.k3_default = k3_user

  if ( sigma2_user is not None ):
    ozone2_parameters.sigma2_default = sigma2_user

  if ( t0_user is not None ):
    ozone2_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    ozone2_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    ozone2_parameters.tstop_default = tstop_user
#
#  Return values.
#
  k2 = ozone2_parameters.k2_default
  k3 = ozone2_parameters.k3_default
  sigma2 = ozone2_parameters.sigma2_default
  t0 = ozone2_parameters.t0_default
  y0 = ozone2_parameters.y0_default
  tstop = ozone2_parameters.tstop_default

  return k2, k3, sigma2, t0, y0, tstop

def ozone2_solve_ivp ( ):

#*****************************************************************************80
#
## ozone2_solve_ivp uses solve_ivp() to solve ozone2_ode().
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
  print ( 'ozone2_solve_ivp():' )
  print ( '  Use solve_ivp() to solve ozone2_ode().' )

  k2, k3, sigma2, t0, y0, tstop = ozone2_parameters ( )

  f = ozone2_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )
#
#  This problem is stiff.  The "Radau" option solves it quickly.
#
  sol = solve_ivp ( f, tspan, y0, method = 'Radau', t_eval = t )

  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y1  --->' )
  plt.title ( 'ozone2_ode() solve_ivp y1' )
  filename = 'ozone2_solve_ivp_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, sol.y[1], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y2  --->' )
  plt.title ( 'ozone2_ode() solve_ivp y2' )
  filename = 'ozone2_solve_ivp_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, sol.y[2], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y3  --->' )
  plt.title ( 'ozone2_ode() solve_ivp y3' )
  filename = 'ozone2_solve_ivp_y3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, sol.y[3], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y4  --->' )
  plt.title ( 'ozone2_ode() solve_ivp y4' )
  filename = 'ozone2_solve_ivp_y4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = ozone2_conserved ( sol.y )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h[0],h[0]] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  h  --->' )
  plt.title ( 'ozone2_ode() solve_ivp conservation' )
  filename = 'ozone2_solve_ivp_conservation.png'
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
  ozone2_ode_test ( )
  timestamp ( )

