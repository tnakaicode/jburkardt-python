#! /usr/bin/env python3
#
def sawtooth_deriv ( t, y ):

#*****************************************************************************80
#
## sawtooth_deriv() returns the right hand side of sawtooth_ode().
#
#  Discussion:
#
#    y1' = y2
#    y2' = -y1 + sawtooth(omega*t)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Driving vibrations with sawtooth waves,
#    https://www.johndcook.com/blog/2020/09/19/sawtooth-waves/
#    
#  Input:
#
#    real T, the current time.
#
#    real Y(2), the current state values.
#
#  Output:
#
#    real dydt(2), the time derivatives of the current state values.
#
  import numpy as np

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - u + sawtooth_driver ( t )

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def sawtooth_driver ( t ):

#*****************************************************************************80
#
## sawtooth_driver() returns the driving term for sawtooth_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
# 
#  Input:
#
#    real T, the current time.
#
#  Output:
#
#    real F, the value of the driver function.
#
  import numpy as np

  omega, t0, y0, tstop = sawtooth_parameters ( )

  f = ( t + omega * np.pi ) % ( 2.0 * omega * np.pi ) - omega * np.pi

  return f

def sawtooth_driver_test ( ):

#*****************************************************************************80
#
## sawtooth_driver_test() tests sawtooth_driver().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sawtooth_driver_test()' )
  print ( '  Plot the right hand side of sawtooth_ode().' )

  omega, t0, y0, tstop = sawtooth_parameters ( )

  n = 129
  t = np.linspace ( -2.0 * np.pi, +2.0 * np.pi, n )
  f = sawtooth_driver ( t )

  plt.plot ( t, f, 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- F(T,\omega) --->' )
  s = ( 'F(T,omega) for the sawtooth ODE, omega = %g' % ( omega ) )
  plt.title ( s )

  filename = 'sawtooth_driver_' + str ( omega ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def sawtooth_solve_ivp ( ):

#*****************************************************************************80
#
## sawtooth_solve_ivp() solves sawtooth_ode() with solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sawtooth_solve_ivp():' )
  print ( '  Solve sawtooth_ode() using solve_ivp().' )

  omega, t0, y0, tstop = sawtooth_parameters ( )

  f = sawtooth_deriv
  tspan = np.array ( [ t0, tstop ] )

  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.plot ( t, sol.y[1], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(1), Y(2) -->' )
  plt.title ( 'sawtooth_ode() using solve_ivp()' )
  plt.legend ( ( 'Y1(t)', 'Y2(t)' ) )
  filename = 'sawtooth_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def sawtooth_ode_test ( ):

#*****************************************************************************80
#
## sawtooth_ode_test() solves sawtooth_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sawtooth_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve sawtooth_ode().' )

  omega, t0, y0, tstop = sawtooth_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    omega = ', omega )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  sawtooth_solve_ivp ( )

  omega = 0.5
  omega, t0, y0, tstop = sawtooth_parameters ( omega, t0, y0, tstop )
  sawtooth_driver_test ( )

  omega = 1.0
  omega, t0, y0, tstop = sawtooth_parameters ( omega, t0, y0, tstop )
  sawtooth_driver_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sawtooth_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def sawtooth_parameters ( omega_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## sawtooth_parameters() returns parameters for sawtooth_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real OMEGA_USER: the sawtooth frequency;
#
#    real T0_USER: the initial time, in seconds;
#
#    real Y0_USER(2): the initial values.
#
#    real TSTOP_USER: the final time, in seconds.
#
#  Output:
#
#    real OMEGA: the sawtooth frequency
#
#    real T0: the initial time, in seconds
#
#    real Y0(2): the initial values.
#
#    real TSTOP: the final time, in seconds.
#
  import numpy as np

  if not hasattr ( sawtooth_parameters, "omega_default" ):
    sawtooth_parameters.omega_default = 1.0

  if not hasattr ( sawtooth_parameters, "t0_default" ):
    sawtooth_parameters.t0_default = 0.0

  if not hasattr ( sawtooth_parameters, "y0_default" ):
    sawtooth_parameters.y0_default = np.array ( [ 1.0, 1.0 ] )

  if not hasattr ( sawtooth_parameters, "tstop_default" ):
    sawtooth_parameters.tstop_default = 20.0
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( omega_user is not None ):
    sawtooth_parameters.omega_default = omega_user

  if ( t0_user is not None ):
    sawtooth_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    sawtooth_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    sawtooth_parameters.tstop_default = tstop_user
#
#  Return the current default values.
#
  omega = sawtooth_parameters.omega_default
  t0 = sawtooth_parameters.t0_default
  y0 = sawtooth_parameters.y0_default
  tstop = sawtooth_parameters.tstop_default

  return omega, t0, y0, tstop

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
  sawtooth_ode_test ( )
  timestamp ( )

