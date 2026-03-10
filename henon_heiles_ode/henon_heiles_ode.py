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

def henon_heiles_choose_xp ( e, lam, x, y, yp ):

#*****************************************************************************80
#
## henon_heiles_choose_xp(): consistent initial condition for henon_heiles_ode().
#
#  Discussion:
#
#    It must be the case that 0 <= 2e-yp^2-x^2-y^2-2x^2y+2y^3/3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michel Henon, Carl Heiles,
#    The applicability of the third integral of motion: 
#    Some numerical experiments,
#    The Astronomical Journal,
#    Volume 69, pages 73-79, 1964.
#
#  Input:
#
#    real E: proposed initial energy.
#
#    real LAM: a parameter.
#
#    real X, Y, YP: proposed initial values for three coordinates.
#
#  Output:
#
#    real XP: a value which gives a consistent initial condition.
#
  import numpy as np

  xpsq = 2.0 * e - yp**2 - x**2 - y**2 \
    - 2.0 * lam * ( x**2 * y - y**3 / 3.0 )

  if ( xpsq < 0.0 ):
    print ( 'henon_heiles_choose_xp(): Fatal error!' )
    print ( '  2e-yp^2-x^2-y^2-2x^2y+2y^3/3 < 0' )
    raise Exception ( 'henon_heiles_choose_xp(): Fatal error!' )

  xp = np.sqrt ( xpsq )

  return xp

def henon_heiles_conserved ( w ):

#*****************************************************************************80
#
## henon_heiles_conserved() evaluates conserved quantities for henon_heiles_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michel Henon, Carl Heiles,
#    The applicability of the third integral of motion: 
#    Some numerical experiments,
#    The Astronomical Journal,
#    Volume 69, pages 73-79, 1964.
#
#  Input:
#
#    real W(N,4): the current coordinates.
#
#  Output:
#
#    real H(N): the conserved quantities.
#
  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  x =  w[:,0]
  xp = w[:,1]
  y =  w[:,2]
  yp = w[:,3]

  h = 0.5 * ( xp**2 + yp**2 ) + 0.5 * ( x**2 + y**2 ) \
    + lam * ( x**2 * y - y**3 / 3.0 )

  return h

def henon_heiles_deriv ( t, w ):

#*****************************************************************************80
#
## henon_heiles_deriv() evaluates the derivative of henon_heiles_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michel Henon, Carl Heiles,
#    The applicability of the third integral of motion: 
#    Some numerical experiments,
#    The Astronomical Journal,
#    Volume 69, pages 73-79, 1964.
#
#  Input:
#
#    real T, W(4): the arguments of the derivative.
#
#  Output:
#
#    real DWDT(4): the value of the derivative.
#
  import numpy as np

  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  x =  w[0]
  xp = w[1]
  y =  w[2]
  yp = w[3]

  dxdt = xp
  dxpdt = - x - 2.0 * lam * x * y
  dydt = yp
  dypdt = - y - lam * ( x**2 - y**2 )

  dwdt = np.array ( [ dxdt, dxpdt, dydt, dypdt ] )

  return dwdt

def henon_heiles_euler ( n ):

#*****************************************************************************80
#
## henon_heiles_euler() uses euler() to solve henon_heiles_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'henon_heiles_euler():' )
  print ( '  Use euler() to solve henon_heiles_ode().' )

  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, w = euler ( henon_heiles_deriv, tspan, w0, n )
#
#  Make plots.
#
  plt.plot ( t, w[:,0], 'r-', linewidth = 2 )
  plt.plot ( t, w[:,1], 'g-', linewidth = 2 )
  plt.plot ( t, w[:,2], 'b-', linewidth = 2 )
  plt.plot ( t, w[:,3], 'm-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  p,q  --->' )
  plt.title ( 'henon_heiles_ode(): euler, Time Plot' )
  plt.legend ( ( 'X', 'X\'', 'Y', 'Y\'' ) )
  filename = 'henon_heiles_euler_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( w[:,0], w[:,2] )
  plt.grid ( True )
  plt.xlabel ( '<---  q1  --->' )
  plt.ylabel ( '<---  q2  --->' )
  plt.title ( 'henon_heiles_ode(): euler Orbit' )
  filename = 'henon_heiles_euler_orbit.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = henon_heiles_conserved ( w )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( [ tspan[0], tspan[1] ], [0.0, 0.0 ], 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H(T) -->' )
  plt.title ( 'henon_heiles_ode(): euler, H(T) conservation' )
  filename = 'henon_heiles_euler_conserved.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def henon_heiles_ode_test ( ):

#*****************************************************************************80
#
## henon_heiles_ode_test() solves henon_heiles_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'henon_heiles_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve henon_heiles_ode().' )

  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    e     = ', e )
  print ( '    lam   = ', lam )
  print ( '    t0    = ', t0 )
  print ( '    w0    = ', w0 )
  print ( '    tstop = ', tstop )

  n = 10000
  henon_heiles_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'henon_heiles_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def henon_heiles_parameters ( e_user = None, lam_user = None, \
  t0_user = None, w0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## henon_heiles_parameters() returns parameters for henon_heiles_ode().
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
#    01 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real E_USER: the initial energy.
#
#    real LAM_USER: a parameter.
#
#    real T0_USER: the initial time.
#
#    real W0_USER[4]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real E: the initial energy.
#
#    real LAM: a parameter.
#
#    real T0: the initial time.
#
#    real W0[4]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( henon_heiles_parameters, "e_default" ):
    henon_heiles_parameters.e_default = 0.05

  if not hasattr ( henon_heiles_parameters, "lam_default" ):
    henon_heiles_parameters.lam_default = 1.0

  if not hasattr ( henon_heiles_parameters, "t0_default" ):
    henon_heiles_parameters.t0_default = 0.0

  if not hasattr ( henon_heiles_parameters, "w0_default" ):
    e = henon_heiles_parameters.e_default
    lam = henon_heiles_parameters.lam_default
    x = 0.0
    y = 0.0
    yp = 0.0
    xp = henon_heiles_choose_xp ( e, lam, x, y, yp )
    w0 = np.array ( [ x, xp, y, yp ] )
    henon_heiles_parameters.w0_default = w0

  if not hasattr ( henon_heiles_parameters, "tstop_default" ):
    henon_heiles_parameters.tstop_default = 30.0
#
#  Update defaults if input was supplied.
#
  if ( e_user is not None ):
    henon_heiles_parameters.e_default = e_user

  if ( lam_user is not None ):
    henon_heiles_parameters.lam_default = lam_user

  if ( t0_user is not None ):
    henon_heiles_parameters.t0_default = t0_user

  if ( w0_user is not None ):
    henon_heiles_parameters.w0_default = w0_user

  if ( tstop_user is not None ):
    henon_heiles_parameters.tstop_default = tstop_user
#
#  Return values.
#
  e = henon_heiles_parameters.e_default
  lam = henon_heiles_parameters.lam_default
  t0 = henon_heiles_parameters.t0_default
  w0 = henon_heiles_parameters.w0_default
  tstop = henon_heiles_parameters.tstop_default
  
  return e, lam, t0, w0, tstop

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
  henon_heiles_ode_test ( )
  timestamp ( )

