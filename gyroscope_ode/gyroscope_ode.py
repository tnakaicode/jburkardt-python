#! /usr/bin/env python3
#
def gyroscope_deriv ( t, y ):

#*****************************************************************************80
#
## gyroscope_deriv() returns the right hand side of gyroscope_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Forest Ray Moulton,
#    "The Damped Gyroscope",
#    Differential Equations,
#    Dover, 1958.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(6), the current state values.
#
#  Output:
#
#    real DYDT(6), the time derivatives of the current state values.
#
  import numpy as np

  A1, A2, A3, m, t0, y0, tstop = gyroscope_parameters ( )

  psi    = y[0]
  theta  = y[1]
  phi    = y[2]
  omega1 = y[3]
  omega2 = y[4]
  omega3 = y[5]

  M1 = - m * A1 * np.sin ( theta ) * np.cos ( phi )
  M2 =   m * A2 * np.sin ( theta ) * np.sin ( phi )
  M3 = 0.0;

  dpsidt = ( omega1 * np.sin ( phi ) + omega2 * np.cos ( phi ) ) / np.sin ( theta )
  dthetadt = omega1 * np.cos ( phi ) - omega2 * np.sin ( phi )
  dphidt = omega3 - np.cos ( theta ) * dpsidt

  domega1dt = ( ( A2 - A3 ) * omega2 * omega3 + M1 ) / A1
  domega2dt = ( ( A3 - A1 ) * omega3 * omega1 + M2 ) / A2
  domega3dt = ( ( A1 - A2 ) * omega1 * omega2 + M3 ) / A3

  dydt = np.array ( [ dpsidt, dthetadt, dphidt, domega1dt, domega2dt, domega3dt ] )

  return dydt

def gyroscope_ode_test ( ):

#*****************************************************************************80
#
## gyroscope_ode_test() solves gyroscope_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gyroscope_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve gyroscope_ode().' )

  A1, A2, A3, m, t0, y0, tstop = gyroscope_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    A1    = ', A1 )
  print ( '    A2    = ', A2 )
  print ( '    A3    = ', A3 )
  print ( '    m     = ', m )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  gyroscope_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gyroscope_ode_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def gyroscope_parameters ( A1_user = None, A2_user = None, A3_user = None, \
  m_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## gyroscope_parameters() returns parameters for gyroscope_ode().
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
#    20 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Forest Ray Moulton,
#    "The Damped Gyroscope",
#    Differential Equations,
#    Dover, 1958.
#
#  Input:
#
#    real A1_USER, A2_USER, A3_USER: the moments of inertia about axes 1, 2, 3.
#
#    real M_USER: the magnitude of the exterior force.
#
#    real T0_USER: the initial time, in seconds
#
#    real Y0_USER(6): the initial values.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A1, A2, A3: the moments of inertia about axes 1, 2, 3.
#
#    real M: the magnitude of the exterior force.
#
#    real T0: the initial time, in seconds
#
#    real Y0(6): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np

  if not hasattr ( gyroscope_parameters, "A1_default" ):
    gyroscope_parameters.A1_default = 1.0

  if not hasattr ( gyroscope_parameters, "A2_default" ):
    gyroscope_parameters.A2_default = 1.0

  if not hasattr ( gyroscope_parameters, "A3_default" ):
    gyroscope_parameters.A3_default = 3.0

  if not hasattr ( gyroscope_parameters, "m_default" ):
    gyroscope_parameters.m_default = 1.0

  if not hasattr ( gyroscope_parameters, "t0_default" ):
    gyroscope_parameters.t0_default = 0.0

  if not hasattr ( gyroscope_parameters, "y0_default" ):
    gyroscope_parameters.y0_default = \
      np.array ( [ 0.25, 0.4, 0.1, 1.0, 2.0, 3.0 ] )

  if not hasattr ( gyroscope_parameters, "tstop_default" ):
    gyroscope_parameters.tstop_default = 5.0
#
#  Update defaults if input was supplied.
#
  if ( A1_user is not None ):
    gyroscope_parameters.A1_default = A1_user

  if ( A2_user is not None ):
    gyroscope_parameters.A2_default = A2_user 

  if ( A3_user is not None ):
    gyroscope_parameters.A3_default = A3_user

  if ( m_user is not None ):
    gyroscope_parameters.m_default = m_user

  if ( t0_user is not None ):
    gyroscope_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    gyroscope_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    gyroscope_parameters.tstop_default = tstop_user
#
#  Return values.
#
  A1 = gyroscope_parameters.A1_default
  A2 = gyroscope_parameters.A2_default
  A3 = gyroscope_parameters.A3_default
  m = gyroscope_parameters.m_default
  t0 = gyroscope_parameters.t0_default
  y0 = gyroscope_parameters.y0_default
  tstop = gyroscope_parameters.tstop_default
  
  return A1, A2, A3, m, t0, y0, tstop

def gyroscope_solve_ivp ( ):

#*****************************************************************************80
#
## gyroscope_solve_ivp() solves gyroscope_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib as mpl
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gyroscope_solve_ivp():' )
  print ( '  Solve gyroscope_ode() using solve_ivp().' )
#
#  Enable TeX symbols.
#
  plt.rcParams['text.usetex'] = True

  A1, A2, A3, m, t0, y0, tstop = gyroscope_parameters ( )

  f = gyroscope_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Adjust psi, theta, phi.
#
  sol.y[0] = ( sol.y[0] + np.pi ) % ( 2.0 * np.pi ) - np.pi
  sol.y[1] = ( sol.y[1] + np.pi ) % ( 2.0 * np.pi ) - np.pi
  sol.y[2] = ( sol.y[2] + np.pi ) % ( 2.0 * np.pi ) - np.pi
#
#  Plot psi, theta, phi.
#
  plt.clf ( )
  plt.plot ( t, ( sol.y[0] ), linewidth = 2 )
  plt.plot ( t, ( sol.y[1] ), linewidth = 2 )
  plt.plot ( t, ( sol.y[2] ), linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- radians -->' )
  plt.title ( 'gyroscope_ode(): solve_ivp, $\Psi(t)$, $\Theta(t)$, $\Phi(t)$' )
  plt.legend ( [ '$\Psi$', '$\Theta$', '$\Phi$' ] );
  filename = 'gyroscope_solve_ivp_angles.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot omega1, omega2, omega3.
#
  plt.clf ( )
  plt.plot ( t, sol.y[3], linewidth = 2 )
  plt.plot ( t, sol.y[4], linewidth = 2 )
  plt.plot ( t, sol.y[5], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- rotation speed -->' )
  plt.title ( 'gyroscope_ode(): solve_ivp, rotation' )
  plt.legend ( [ '$\omega_1$', '$\omega_2$', '$\omega_3$' ] );
  filename = 'gyroscope_solve_ivp_rotation.png'
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
  gyroscope_ode_test ( )
  timestamp ( )

