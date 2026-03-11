#! /usr/bin/env python3
#
def spring_conserved ( y ):

#*****************************************************************************80
#
## spring_conserved() returns a conserved quantity for spring_ode().
#
#  Discussion:
#
#    This conserved quantity can be regarded as the total energy of
#    the system.  Actually, if damping is present, the energy will 
#    not be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(:,2): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  u = y[0]
  v = y[1]

  m, b, k, t0, y0, tstop = spring_parameters ( )

  h = 0.5 * k * u**2 + 0.5 * m * v**2

  return h

def spring_deriv ( t, y ):

#*****************************************************************************80
#
## spring_deriv() returns the right hand side of spring_ode().
#
#  Discussion:
#
#    Y1 is the displacement
#    Y2 is the velocity
#
#    M is the mass.
#    B is the damping.
#    K is the spring stiffness.
#
#    The second order ODE:
#
#      m * x'' + b * x' + k * x = 0
#
#    is transformed into a pair of first order ODE's
#    using the variables:
#
#      y(1) = x,
#      y(2) = x'
#
#    so that
#
#      y'(1) = y(2)
#      y'(2) = - ( k / m ) y(1) - ( b / m ) y(2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
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

  m, b, k, t0, y0, tstop = spring_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - ( k / m ) * u - ( b / m ) * v

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def spring_exact ( t ):

#*****************************************************************************80
#
## spring_exact() returns the exact solution for spring_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the current time.
#
#  Output:
#
#    real Y(2): the exact solution.
#
  import numpy as np

  m, b, k, t0, y0, tstop = spring_parameters ( )

  u0 = y0[0]
  v0 = y0[1]

  r = np.sqrt ( ( 4.0 * m * k - b**2 ) ) / 2.0 / m
  c1 = u0
  c2 = ( v0 + k * u0 / 2.0 / m ) / r

  u = c1 * np.exp ( - b * ( t - t0 ) / 2.0 / m ) * np.cos ( r * ( t - t0 ) ) \
    + c2 * np.exp ( - b * ( t - t0 ) / 2.0 / m ) * np.sin ( r * ( t - t0 ) )

  v = c1 * ( - b / 2.0 / m ) * np.exp ( - b * ( t - t0 ) / 2.0 / m ) \
                             * np.cos ( r * ( t - t0 ) ) \
    - c1 * r                 * np.exp ( - b * ( t - t0 ) / 2.0 / m ) \
                             * np.sin ( r * ( t - t0 ) ) \
    + c2 * ( - b / 2.0 / m ) * np.exp ( - b * ( t - t0 ) / 2.0 / m ) \
                             * np.sin ( r * ( t - t0 ) ) \
    + c2 * r                 * np.exp ( - b * ( t - t0 ) / 2.0 / m ) \
                             * np.cos ( r * ( t - t0 ) )

  y = np.array ( [ u, v ] )

  return y

def spring_solve_ivp ( ):

#*****************************************************************************80
#
## spring_solve_ivp() uses solve_ivp() to solve spring_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'spring_solve_ivp():' )
  print ( '  Use solve_ivp() to solve spring_ode().' )

  m, b, k, t0, y0, tstop = spring_parameters ( )

  f = spring_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  ye = spring_exact ( t )
#
#  Plot y1
#
  plt.plot ( t, sol.y[0], 'ro', linewidth = 2 )
  plt.plot ( t, ye[0], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Displacement -->' )
  plt.title ( 'spring_ode(): solve_ivp, displacement' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'spring_solve_ivp_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
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
  plt.ylabel ( '<-- Velocity -->' )
  plt.title ( 'spring_ode(): solve_ivp, velocity' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'spring_solve_ivp_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot phase.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], 'ro', linewidth = 2 )
  plt.plot ( ye[0], ye[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Displacement -->' )
  plt.ylabel ( '<-- Velocity -->' )
  plt.title ( 'spring_ode(): solve_ivp, phase' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'spring_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = spring_conserved ( sol.y )

  plt.clf ( )
  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'spring_ode(): solve_ivp, energy' )
  filename = 'spring_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def spring_ode_test ( ):

#*****************************************************************************80
#
## spring_ode_test() solves spring_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'spring_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve spring_ode().' )

  m, b, k, t0, y0, tstop = spring_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    mass      = ', m )
  print ( '    damping   = ', b )
  print ( '    stiffness = ', k )
  print ( '    t0        = ', t0 )
  print ( '    u0        = ', y0[0] )
  print ( '    v0        = ', y0[1] )
  print ( '    tstop     = ', tstop )

  spring_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'spring_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def spring_parameters ( m_user = None, b_user = None, k_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## spring_parameters() returns parameters for spring_ode().
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
#    02 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real M_USER: the mass
#
#    real B_USER: the damping coefficient
#
#    real K_USER: the spring stiffness.
#
#    real T0_USER: the initial time, in seconds
#
#    real Y0_USER(2): the initial values.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real M: the mass
#
#    real B: the damping coefficient
#
#    real K: the spring stiffness.
#
#    real T0: the initial time, in seconds
#
#    real Y0(2): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize the defaults.
#
  if not hasattr ( spring_parameters, "m_default" ):
    spring_parameters.m_default = 5.0

  if not hasattr ( spring_parameters, "b_default" ):
    spring_parameters.b_default = 2.0

  if not hasattr ( spring_parameters, "k_default" ):
    spring_parameters.k_default = 3.0

  if not hasattr ( spring_parameters, "t0_default" ):
    spring_parameters.t0_default = 0.0

  if not hasattr ( spring_parameters, "y0_default" ):
    spring_parameters.y0_default = np.array ( [ 0.0, 1.0 ] )

  if not hasattr ( spring_parameters, "tstop_default" ):
    spring_parameters.tstop_default = 25.0
#
#  Update defaults if input was supplied.
#
  if ( m_user is not None ):
    spring_parameters.m_default = m_user

  if ( b_user is not None ):
    spring_parameters.b_default = b_user

  if ( k_user is not None ):
    spring_parameters.k_default = k_user

  if ( t0_user is not None ):
    spring_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    spring_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    spring_parameters.tstop_default = tstop_user
#
#  Return values.
#
  m = spring_parameters.m_default
  b = spring_parameters.b_default
  k = spring_parameters.k_default
  t0 = spring_parameters.t0_default
  y0 = spring_parameters.y0_default
  tstop = spring_parameters.tstop_default
  
  return m, b, k, t0, y0, tstop

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
  spring_ode_test ( )
  timestamp ( )

