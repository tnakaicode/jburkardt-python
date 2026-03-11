#! /usr/bin/env python3
#
def midpoint ( f, tspan, y0, n ):

#*****************************************************************************80
#
## midpoint() uses the implicit midpoint method to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real tspan[2]: the starting and ending times.
#
#    real y0[m]: the initial conditions. 
#
#    integer n: the number of steps.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the solution estimates.
#
  from scipy.optimize import fsolve
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  t[0] = tspan[0];
  y[0,:] = y0

  for i in range ( 0, n ):

    to = t[i]
    yo = y[i,:]

    th = to + 0.5 * dt
    yh = yo + 0.5 * dt * f ( to, yo )
    yh = fsolve ( midpoint_residual, yh, args = ( f, to, yo, th ) )

    tp = to + dt
    yp = 2.0 * yh - yo

    t[i+1]   = tp
    y[i+1,:] = yp

  return t, y

def midpoint_residual ( yh, f, to, yo, th ):

#*****************************************************************************80
#
## midpoint_residual() evaluates the midpoint residual.
#
#  Discussion:
#
#    We are seeking a value YH defined by the implicit equation:
#
#      YH = YO + ( TH - TO ) * F ( TH, YH )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yh: the estimated solution value at the midpoint time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real th: the midpoint time.
#
#  Output:
#
#    real value: the midpoint residual.
#
  value = yh - yo - ( th - to ) * f ( th, yh );

  return value

def polar_deriv ( t, z ):

#*****************************************************************************80
#
## polar_deriv() evaluates the right hand side of polar_ode().
#
#  Discussion:
#
#    The variable Z(t) is complex, and has the formula:
#
#    theta = t
#    r = 1 - sin(theta) * cos(3*theta)
#    z = r * exp ( i * theta )
#    dzdt = ( drdt + i * r ) * exp ( i * theta ) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, complex Z: the time and solution value.
#
#  Output:
#
#    complex DZDT: the derivative value.
#
  import numpy as np

  theta = t
  r = 1.0 - np.sin ( theta ) * np.cos ( 3.0 * theta )
  drdt = -       np.cos ( theta ) * np.cos ( 3.0 * theta ) \
         + 3.0 * np.sin ( theta ) * np.sin ( 3.0 * theta )

  dzdt = complex ( drdt, r ) * np.exp ( complex ( 0.0, theta ) )

  return dzdt

def polar_exact ( t ):

#*****************************************************************************80
#
## polar_exact() evaluates the exact solution of polar_ode().
#
#  Discussion:
#
#    The variable Z(t) is complex, and has the formula:
#
#    theta = t
#    r = 1 - sin(theta) * cos(3*theta)
#    z = r * exp ( i * theta )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2021
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
#    complex Z(:): the exact solution values.
#
  import numpy as np

  r = 1.0 - np.sin ( t ) * np.cos ( 3.0 * t )
  z = r * np.exp ( t * 1j )

  return z

def polar_solve_ivp ( ):

#*****************************************************************************80
#
## polar_solve_ivp() uses solve_ivp() on polar_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'polar_solve_ivp():' )
  print ( '  Solve polar_ode() using solve_ivp().' )

  t0, z0, tstop = polar_parameters ( )

  f = polar_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, z0, t_eval = t )
#
#  For incomprehensible reasons, z1 is returned as a 1 by 101 array.
#  We have to flatten it to a 101 vector in order to plot it.
#
  z1 = sol.y
  z1 = z1.flatten()

  z2 = polar_exact ( t )
#
#  Polar plot.
#
  plt.plot ( z1.real, z1.imag, 'ro', linewidth = 3 )
  plt.plot ( z2.real, z2.imag, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- R(z) -->' )
  plt.ylabel ( '<-- I(z) -->' )
  plt.title ( 'polar_ode(): solve_ivp, phase' )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = 'polar_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Time plot.
#
  plt.plot ( t, z1.real, 'ro', linewidth = 3 )
  plt.plot ( t, z1.imag, 'mo', linewidth = 3 )
  plt.plot ( t, z2.real, 'b-', linewidth = 3 )
  plt.plot ( t, z2.imag, 'c-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- z(t) -->' )
  plt.title ( 'polar_ode(): solve_ivp, time' )
  plt.legend ( ( 'R(approx)', 'I(approx)', 'R(exact)', 'I(exact)' ) )
  filename = 'polar_solve_ivp_time.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Compare solution values at solve_ivp's nodes.
#
  z2 = polar_exact ( t )
  e = rms ( z1 - z2 )
  print ( '  RMS error norm = ', e )
  print ( '  L2 error norm = ', np.linalg.norm ( z1 - z2 ) )

  return

def polar_ode_test ( ):

#*****************************************************************************80
#
## polar_ode_test() tests polar_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polar_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve polar_ode(), an ordinary differential equation (ODE)' )
  print ( '  involving a complex variable, whose solution is best ' )
  print ( '  viewed in a polar coordinate plot.' )

  t0, z0, tstop = polar_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    z0    = ', z0 )
  print ( '    tstop = ', tstop )

  polar_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polar_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def polar_parameters ( t0_user = None, z0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## polar_parameters() returns the parameters of polar_ode().
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
#    06 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time.
#
#    complex Z0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    complex Z0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  if not hasattr ( polar_parameters, "t0_default" ):
    polar_parameters.t0_default = 0.0

  if not hasattr ( polar_parameters, "z0_default" ):
    polar_parameters.z0_default = np.array ( [ complex ( 1.0, 0.0 ) ] )

  if not hasattr ( polar_parameters, "tstop_default" ):
    polar_parameters.tstop_default = 6.0 * np.pi
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( t0_user is not None ):
    polar_parameters.t0_default = t0_user

  if ( z0_user is not None ):
    polar_parameters.z0_default = z0_user

  if ( tstop_user is not None ):
    polar_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = polar_parameters.t0_default
  z0 = polar_parameters.z0_default
  tstop = polar_parameters.tstop_default
  
  return t0, z0, tstop

def rms ( x ):

#*****************************************************************************80
#
## rms() returns the RMS norm of an R8VEC.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) |A(I)|^2 / N ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the vector.
#
#  Output:
#
#    real VALUE, the RMS norm.
#
  import numpy as np

  value = np.sqrt ( np.mean ( ( abs ( x ) )**2 ) )

  return value

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
  polar_ode_test ( )
  timestamp ( )

