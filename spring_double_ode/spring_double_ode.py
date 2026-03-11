#! /usr/bin/env python3
#
def spring_double_deriv ( t, y ):

#*****************************************************************************80
#
## spring_double deriv() returns the right hand side of spring_double_ode().
#
#  Discussion:
#
#    Spring #1 is suspended from a fixed support, has mass m1 and 
#    spring constant k1.
#
#    Spring #2 is suspended from spring #1, has mass m2 and spring
#    constant k2.
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
#    A stiffening spring,
#    https://www.johndcook.com/blog/2021/03/04/a-stiffening-spring/
#
#    K E Clark, S Hill,
#    The Effects of a Stiffening Spring,
#    College Mathematics Journal,
#    Volume 30, Number 5, November 1999, pages 379-382.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(4), the current state values.
#
#  Output:
#
#    real dydt(4), the time derivatives of the current state values.
#
  import numpy as np

  m1, m2, k1, k2, t0, y0, tstop = spring_double_parameters ( )

  u1 = y[0]
  v1 = y[1]
  u2 = y[2]
  v2 = y[3]

  du1dt = v1
  dv1dt = ( - k1 * u1 + k2 * ( u2 - u1 ) ) / m1
  du2dt = v2
  dv2dt = (           - k2 * ( u2 - u1 ) ) / m2

  dydt = np.array ( [ du1dt, dv1dt, du2dt, dv2dt ] )

  return dydt

def spring_double_solve_ivp ( ):

#*****************************************************************************80
#
## spring_double_solve_ivp() solves spring_double_ode() using solve_ivp().
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
  print ( 'spring_double_solve_ivp():' )
  print ( '  Use solve_ivp() to solve spring_double_ode().' )

  m1, m2, k1, k2, t0, y0, tstop = spring_double_parameters ( )

  f = spring_double_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot displacements.
#
  plt.plot ( t, sol.y[0], 'r-', linewidth = 2 )
  plt.plot ( t, sol.y[2], 'b-', linewidth = 2 )
  plt.plot ( t, sol.y[2]-sol.y[0], 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Displacements -->' )
  plt.title ( 'spring_double_ode(): solve_ivp' )
  plt.legend ( ( 'u1', 'u2', 'u2-u1' ) )
  filename = 'spring_double_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def spring_double_ode_test ( ):

#*****************************************************************************80
#
## spring_double_ode_test() solves spring_double_ode().
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
  print ( 'spring_double_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve spring_double_ode().' )

  m1, m2, k1, k2, t0, y0, tstop = spring_double_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    mass #1      = ', m1 )
  print ( '    mass #2      = ', m2 )
  print ( '    stiffness #1 = ', k1 )
  print ( '    stiffness #2 = ', k2 )
  print ( '    t0           = ', t0 )
  print ( '    y0           = ', y0 )
  print ( '    tstop        = ', tstop )

  spring_double_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'spring_double_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def spring_double_parameters ( m1_user = None, m2_user = None, \
  k1_user = None, k2_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## spring_double_parameters() returns parameters for spring_double_ode().
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
#    real M1_USER, M2_USER: the masses
#
#    real K1_USER, K2_USER: the spring constants.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real M1, M2: the masses
#
#    real K1, K2: the spring constants.
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( spring_double_parameters, "m1_default" ):
    spring_double_parameters.m1_default = 3.0

  if not hasattr ( spring_double_parameters, "m2_default" ):
    spring_double_parameters.m2_default = 5.0

  if not hasattr ( spring_double_parameters, "k1_default" ):
    spring_double_parameters.k1_default = 1.0

  if not hasattr ( spring_double_parameters, "k2_default" ):
    spring_double_parameters.k2_default = 10.0

  if not hasattr ( spring_double_parameters, "t0_default" ):
    spring_double_parameters.t0_default = 0.0

  if not hasattr ( spring_double_parameters, "y0_default" ):
    u10 = 0.0
    v10 = 1.0
    u20 = 0.0
    v20 = 0.0
    spring_double_parameters.y0_default = np.array ( [ u10, v10, u20, v20 ] )

  if not hasattr ( spring_double_parameters, "tstop_default" ):
    spring_double_parameters.tstop_default = 50.0
#
#  Update defaults if input was supplied.
#
  if ( m1_user is not None ):
    spring_double_parameters.m1_default = m1_user

  if ( m2_user is not None ):
    spring_double_parameters.m2_default = m2_user

  if ( k1_user is not None ):
    spring_double_parameters.k1_default = k1_user

  if ( k2_user is not None ):
    spring_double_parameters.k2_default = k2_user

  if ( t0_user is not None ):
    spring_double_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    spring_double_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    spring_double_parameters.tstop_default = tstop_user
#
#  Return values.
#
  m1 = spring_double_parameters.m1_default
  m2 = spring_double_parameters.m2_default
  k1 = spring_double_parameters.k1_default
  k2 = spring_double_parameters.k2_default
  t0 = spring_double_parameters.t0_default
  y0 = spring_double_parameters.y0_default
  tstop = spring_double_parameters.tstop_default
  
  return m1, m2, k1, k2, t0, y0, tstop

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
  spring_double_ode_test ( )
  timestamp ( )

