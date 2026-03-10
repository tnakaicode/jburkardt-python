#! /usr/bin/env python3
#
def blood_pressure_compliance ( ):

#*****************************************************************************80
#
## blood_pressure_compliance() evaluates the compliance for blood_pressure_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real CA, the compliance.
#
  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )

  ca = q / pulse / ( psys - pdia )

  return ca

def blood_pressure_deriv ( t, y ):

#*****************************************************************************80
#
## blood_pressure_deriv() evaluates the derivative for blood_pressure_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT: the value of the derivative.
#
#  Local:
#
#    real CA: the compliance.
#
#    real RS: the resistance.
#
  import numpy as np

  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )

  T = 1.0 / pulse
  b1 = np.floor ( ( told - t0 ) / T )
  b2 = np.floor ( ( t - t0 )    / T )

  if ( b1 == b2 ):
    ca = blood_pressure_compliance ( )
    rs = blood_pressure_resistance ( )
    dydt = - y / ca / rs
#
#  This assumes b2 = b1 + 1.
#
  else:
    dydt = ( psys - y ) / ( t - told )
#
#  Remember the value of time.
#
  told = t
  blood_pressure_parameters ( pdia, psys, pulse, q, told, t0, y0, tstop )

  return dydt

def blood_pressure_euler ( n ):

#*****************************************************************************80
#
## blood_pressure_euler() uses euler() to solve blood_pressure_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'blood_pressure_euler():' )
  print ( '  Use euler() to solve blood_pressure_ode().' )
  print ( '  Number of equal steps = ', n )
#
#  Get the parameters.
#
  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )
#
#  Estimate the solution.
#
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( blood_pressure_deriv, tspan, y0, n )

  ye = blood_pressure_exact ( t )
#
#  Plot the solution curve.
#
  plt.clf ( )
  plt.plot ( t, y, 'bo', linewidth = 3 )
  plt.plot ( t, ye, 'r-', linewidth = 3 )

  plt.title ( 'blood_pressure_ode():, euler' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X(T) --->' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  plt.show ( block = False )
  filename = 'blood_pressure_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def blood_pressure_exact ( t ):

#*****************************************************************************80
#
## blood_pressure_exact() evaluates the exact solution for blood_pressure_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the times.
#
#  Output:
#
#    real Y(:), the exact solution values.
#
  import numpy as np

  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )

  ca = blood_pressure_compliance ( )
  rs = blood_pressure_resistance ( )
  tpulse = 1.0 / pulse
  tmod = np.mod ( t - t0, tpulse )
  y = psys * np.exp ( - tmod / ca / rs )

  return y

def blood_pressure_exact_test ( ):

#*****************************************************************************80
#
## blood_pressure_exact_test() displays the exact solution of blood_pressure_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'blood_pressure_exact_test():' )
  print ( '  blood_pressure_exact() evaluates the exact solution' )
  print ( '  to blood_pressure_ode()' )
#
#  Get the parameters.
#
  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )
#
#  Evaluate the solution at 501 points.
#
  t = np.linspace ( t0, tstop, 501 )

  ye = blood_pressure_exact ( t )
#
#  Plot the exact solution.
#
  plt.clf ( )
  plt.plot ( t, ye, 'r-', linewidth = 3 )
  plt.title ( 'blood_pressure_ode():, exact' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y(T) --->' )
  plt.show ( block = False )
  filename = 'blood_pressure_exact.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def blood_pressure_ode_test ( ):

#*****************************************************************************80
#
## blood_pressure_ode_test() solves blood_pressure_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'blood_pressure_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  blood_pressure_ode() models pressure variation' )
  print ( '  in the human blood network.' )
#
#  Get parameters.
#
  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    pdia  = ', pdia )
  print ( '    psys  = ', psys )
  print ( '    pulse = ', pulse )
  print ( '    q     = ', q )
  print ( '    told  = ', told )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  ca = blood_pressure_compliance ( )
  rs = blood_pressure_resistance ( )
  print ( '    compliance = ', ca )
  print ( '    resistance = ', rs )

  blood_pressure_exact_test ( )

  n = 100
  blood_pressure_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'blood_pressure_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def blood_pressure_parameters ( pdia_user = None, psys_user = None, \
  pulse_user = None, q_user = None, told_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## blood_pressure_parameters() returns parameters for blood_pressure_ode().
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
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real PDIA_USER: the diastolic blood pressure.
#
#    real PSYS_USER: the systolic blood pressure.
#
#    real PULSE_USER: the number of heart beats per minute.
#
#    real Q_USER: the cardiac output, liters of blood per minute.
#
#    real TOLD_USER: the time at the previous call to blood_pressure_deriv.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition at time T0.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real PULSE: the number of heart beats per minute.
#
#    real Q: the cardiac output, liters of blood per minute.
#
#    real TOLD_USER: the time at the previous call to blood_pressure_deriv.
#
#    real T0: the initial time.
#
#    real Y0: the initial condition at time T0.
#
#    real TSTOP: the final time.
#

#
#  Initialize defaults.
#
  if ( not hasattr ( blood_pressure_parameters, "pdia_default" ) ):
    blood_pressure_parameters.pdia_default = 80.0

  if ( not hasattr ( blood_pressure_parameters, "psys_default" ) ):
    blood_pressure_parameters.psys_default = 120.0

  if ( not hasattr ( blood_pressure_parameters, "pulse_default" ) ):
    blood_pressure_parameters.pulse_default = 70.0

  if ( not hasattr ( blood_pressure_parameters, "q_default" ) ):
    blood_pressure_parameters.q_default = 5.6

  if ( not hasattr ( blood_pressure_parameters, "told_default" ) ):
    blood_pressure_parameters.told_default = 0.0

  if ( not hasattr ( blood_pressure_parameters, "t0_default" ) ):
    blood_pressure_parameters.t0_default = 0.0

  if ( not hasattr ( blood_pressure_parameters, "y0_default" ) ):
    blood_pressure_parameters.y0_default = 120.0

  if ( not hasattr ( blood_pressure_parameters, "tstop_default" ) ):
    blood_pressure_parameters.tstop_default = 4.0 / 70.0
#
#  Update defaults if input was supplied.
#
  if ( pdia_user is not None ):
    blood_pressure_parameters.pdia_default = pdia_user

  if ( psys_user is not None ):
    blood_pressure_parameters.psys_default = psys_user

  if ( pulse_user is not None ):
    blood_pressure_parameters.pulse_default = pulse_user

  if ( q_user is not None ):
    blood_pressure_parameters.q_default = q_user

  if ( told_user is not None ):
    blood_pressure_parameters.told_default = told_user

  if ( t0_user is not None ):
    blood_pressure_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    blood_pressure_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    blood_pressure_parameters.tstop_default = tstop_user
#
#  Return values.
#
  pdia = blood_pressure_parameters.pdia_default
  psys = blood_pressure_parameters.psys_default
  pulse = blood_pressure_parameters.pulse_default
  q = blood_pressure_parameters.q_default
  told = blood_pressure_parameters.told_default
  t0 = blood_pressure_parameters.t0_default
  y0 = blood_pressure_parameters.y0_default
  tstop = blood_pressure_parameters.tstop_default

  return pdia, psys, pulse, q, told, t0, y0, tstop

def blood_pressure_resistance ( ):

#*****************************************************************************80
#
## blood_pressure_resistance() returns the resistance of a blood network.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RS(:), the resistance.
#
  import numpy as np

  pdia, psys, pulse, q, told, t0, y0, tstop = blood_pressure_parameters ( )

  T = 1.0 / pulse
  ca = blood_pressure_compliance ( )
  rs = T / ( ca * ( np.log ( psys ) - np.log ( pdia) ) )

  return rs

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

  m = np.size ( y0 )

  t0 = tspan[0]
  tstop = tspan[1]
  dt = ( tstop - t0 ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = t0
  y[0,:] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( dydt ( t[i], y[i,:] ) )

  return t, y

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
  blood_pressure_ode_test ( )
  timestamp ( )

