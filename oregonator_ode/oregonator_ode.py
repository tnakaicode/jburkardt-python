#! /usr/bin/env python3
#
def oregonator_deriv ( t, y ):

#*****************************************************************************80
#
## oregonator_deriv() returns the right hand side of oregonator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Field, Endre Koros, Richard Noyes,
#    Oscillations in Chemical Systems II. Thorough analysis of temporal 
#    oscillations in the Ce-BrO3-malonic acid system,
#    Journal of the American Chemical Society,
#    Volume 94, pages 8649-8664, 1972.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(3), the current state values.
#
#  Output:
#
#    real DYDT(3), the time derivatives of the current state values.
#
  import numpy as np

  eta1, eta2, q, f, t0, y0, tstop = oregonator_parameters ( )

  u = y[0]
  v = y[1]
  w = y[2]

  dudt = (   q * v - u * v + u * ( 1.0 - u ) ) / eta1
  dvdt = ( - q * v - u * v + f * w ) / eta2
  dwdt = u - w

  dydt = np.array ( [ dudt, dvdt, dwdt ] )

  return dydt

def oregonator_ode_test ( ):

#*****************************************************************************80
#
## oregonator_ode_test() solves oregonator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'oregonator_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve oregonator_ode().' )

  eta1, eta2, q, f, t0, y0, tstop = oregonator_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    eta1  = ', eta1 )
  print ( '    eta2  = ', eta2 )
  print ( '    q     = ', q )
  print ( '    f     = ', f )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  oregonator_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'oregonator_ode_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def oregonator_parameters ( eta1_user = None, eta2_user = None, q_user = None, \
  f_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## oregonator_parameters() returns parameters for oregonator_ode().
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
#    10 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ETA1_USER, ETA2_USER, Q_USER, F_USER: scaling parameters.
#
#    real T0_USER: the initial time, in seconds
#
#    real Y0_USER(3): the initial values.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ETA1, ETA2, Q, F: scaling parameters.
#
#    real T0: the initial time, in seconds
#
#    real Y0(3): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np

  if not hasattr ( oregonator_parameters, "eta1_default" ):
    a = 0.06
    b = 0.02
    k5 = 33.6
    kc = 1.0
    oregonator_parameters.eta1_default = kc * b / k5 / a

  if not hasattr ( oregonator_parameters, "eta2_default" ):
    a = 0.06
    b = 0.02
    k2 = 2.4E+06
    k4 = 3.0E+03
    k5 = 33.6
    kc = 1.0
    oregonator_parameters.eta2_default = 2.0 * kc * k4 * b / k2 / k5 / a

  if not hasattr ( oregonator_parameters, "q_default" ):
    k2 = 2.4E+06
    k3 = 1.28
    k4 = 3.0E+03
    k5 = 33.6
    oregonator_parameters.q_default = 2.0 * k3 * k4 / k2 / k5

  if not hasattr ( oregonator_parameters, "f_default" ):
    oregonator_parameters.f_default = 1.0

  if not hasattr ( oregonator_parameters, "t0_default" ):
    oregonator_parameters.t0_default = 0.0

  if not hasattr ( oregonator_parameters, "y0_default" ):
    oregonator_parameters.y0_default = np.array ( [ 1.0, 1.0, 1.0 ] )

  if not hasattr ( oregonator_parameters, "tstop_default" ):
    oregonator_parameters.tstop_default = 25.0
#
#  Update defaults if input was supplied.
#
  if ( eta1_user is not None ):
    oregonator_parameters.eta1_default = eta1_user

  if ( eta2_user is not None ):
    oregonator_parameters.eta2_default = eta2_user 

  if ( q_user is not None ):
    oregonator_parameters.q_default = q_user

  if ( f_user is not None ):
    oregonator_parameters.f_default = f_user

  if ( t0_user is not None ):
    oregonator_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    oregonator_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    oregonator_parameters.tstop_default = tstop_user
#
#  Return values.
#
  eta1 = oregonator_parameters.eta1_default
  eta2 = oregonator_parameters.eta2_default
  q = oregonator_parameters.q_default
  f = oregonator_parameters.f_default
  t0 = oregonator_parameters.t0_default
  y0 = oregonator_parameters.y0_default
  tstop = oregonator_parameters.tstop_default
  
  return eta1, eta2, q, f, t0, y0, tstop

def oregonator_solve_ivp ( ):

#*****************************************************************************80
#
## oregonator_solve_ivp() solves oregonator_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib as mpl
  from mpl_toolkits.mplot3d import Axes3D
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'oregonator_solve_ivp():' )
  print ( '  Solve oregonator_ode() using solve_ivp().' )

  eta1, eta2, q, f, t0, y0, tstop = oregonator_parameters ( )

  f = oregonator_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot x.
#
  plt.plot ( t, np.log10 ( sol.y[0] ), 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- log10(x(t)) -->' )
  plt.title ( 'oregonator_ode(): solve_ivp, log10(x(t))' )
  filename = 'oregonator_solve_ivp_x.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot y.
#
  plt.plot ( t, np.log10 ( sol.y[1] ), 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- log10(y(t)) -->' )
  plt.title ( 'oregonator_ode(): solve_ivp, log10(y(t))' )
  filename = 'oregonator_solve_ivp_y.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot z.
#
  plt.plot ( t, np.log10 ( sol.y[2] ), 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- log10(z(t)) -->' )
  plt.title ( 'oregonator_ode(): solve_ivp, log10(z(t))' )
  filename = 'oregonator_solve_ivp_z.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  3D Plot xyz.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
# ax = fig.gca ( projection = '3d' )
  ax.plot ( np.log10 ( sol.y[0] ), np.log10 ( sol.y[1] ), np.log10 ( sol.y[2] ), \
    'b-', linewidth = 2 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- log10(x(t)) -->' )
  ax.set_ylabel ( '<-- log10(y(t)) -->' )
  ax.set_zlabel ( '<-- log10(z(t)) -->' )
  ax.set_title ( 'oregonator_ode(): solve_ivp, log10(x,y,z)' )
  filename = 'oregonator_solve_ivp_xyz.png'
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
  oregonator_ode_test ( )
  timestamp ( )

