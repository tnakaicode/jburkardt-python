#! /usr/bin/env python3
#
def three_body_deriv ( t, y ):

#*****************************************************************************80
#
## three_body_deriv() returns the right hand side of three_body_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2020
#
#  Author:
#
#    Original MATLAB version by Dominik Gruntz, Joerg Waldvogel.
#    This version by John Burkardt.
#
#  Reference:
#
#    Dominik Gruntz, Joerg Waldvogel,
#    Orbits in the Planar Three-Body Problem,
#    Walter Gander, Jiri Hrebicek, editors,
#    Solving Problems in Scientific Computing using Maple and Matlab,
#    Springer, 1997,
#    ISBN: 3-540-61793-0,
#    LC: Q183.9.G36.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(12), the current solution.
#
#  Output:
#
#    real YDOT(12), the derivatives of the current solution.
#
  import numpy as np

  m0, m1, m2, t0, y0, tstop = three_body_parameters ( )

  x0 = y[0:2]
  x1 = y[4:6]
  x2 = y[8:10]

  d0 = ( x2 - x1 ) / np.linalg.norm ( x2 - x1 )**3
  d1 = ( x0 - x2 ) / np.linalg.norm ( x0 - x2 )**3
  d2 = ( x1 - x0 ) / np.linalg.norm ( x1 - x0 )**3

  ydot = np.zeros ( 12 )

  ydot[0:2] = y[2:4]
  ydot[2:4] = m1 * d2 - m2 * d1
  ydot[4:6] = y[6:8]
  ydot[6:8] = m2 * d0 - m0 * d2
  ydot[8:10] = y[10:12]
  ydot[10:12] = m0 * d1 - m1 * d0

  return ydot

def three_body_ode_test ( ):

#*****************************************************************************80
#
## three_body_ode_test() tests three_body_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'three_body_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test three_body_ode().' )

  m0, m1, m2, t0, y0, tstop = three_body_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    m0 =    ', m0 )
  print ( '    m1 =    ', m1 )
  print ( '    m2 =    ', m2 )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  three_body_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'three_body_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def three_body_parameters ( m0_user = None, m1_user = None, \
  m2_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## three_body_parameters() returns parameters for three_body_ode().
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
#    real M0_USER, M1_USER, M2_USER: the masses of the three bodies.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real M0, M1, M2: the masses of the three bodies.
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
  if not hasattr ( three_body_parameters, "m0_default" ):
    three_body_parameters.m0_default = 5.0

  if not hasattr ( three_body_parameters, "m1_default" ):
    three_body_parameters.m1_default = 3.0

  if not hasattr ( three_body_parameters, "m2_default" ):
    three_body_parameters.m2_default = 4.0

  if not hasattr ( three_body_parameters, "t0_default" ):
    three_body_parameters.t0_default = 0.0

  if not hasattr ( three_body_parameters, "y0_default" ):
    three_body_parameters.y0_default = np.array ( [ \
     1.0, -1.0,  0.0,  0.0, \
     1.0,  3.0,  0.0,  0.0, \
    -2.0, -1.0,  0.0,  0.0 ] )

  if not hasattr ( three_body_parameters, "tstop_default" ):
    three_body_parameters.tstop_default = 63.0
#
#  Update defaults if input was supplied.
#
  if ( m0_user is not None ):
    three_body_parameters.m0_default = m0_user

  if ( m1_user is not None ):
    three_body_parameters.m1_default = m1_user

  if ( m2_user is not None ):
    three_body_parameters.m2_default = m2_user

  if ( t0_user is not None ):
    three_body_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    three_body_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    three_body_parameters.tstop_default = tstop_user
#
#  Return values.
#
  m0 = three_body_parameters.m0_default
  m1 = three_body_parameters.m1_default
  m2 = three_body_parameters.m2_default
  t0 = three_body_parameters.t0_default
  y0 = three_body_parameters.y0_default
  tstop = three_body_parameters.tstop_default
  
  return m0, m1, m2, t0, y0, tstop

def three_body_solve_ivp ( ):

#*****************************************************************************80
#
## three_body_solve_ivp() uses solve_ivp() on three_body_ode()..
#
#  Discussion:
#
#    Three bodies, regarded as point masses, are constrained to lie in a plane.
#    The masses of each body are given, as are the positions and velocities
#    at a starting time T = 0.  The bodies move in accordance with the
#    gravitational force between them.
#
#    The force exerted on the 0-th body by the 1st body can be written:
#
#      F = - m0 m1 ( p0 - p1 ) / |p0 - p1|^3
#
#    assuming that units have been normalized to that the gravitational
#    coefficient is 1.  Newton's laws of motion can be written:
#
#      m0 p0'' = - m0 m1 ( p0 - p1 ) / |p0 - p1|^3 
#                - m0 m2 ( p0 - p2 ) / |p0 - p2|^3
#
#      m1 p1'' = - m1 m0 ( p1 - p0 ) / |p1 - p0|^3 
#                - m1 m2 ( p1 - p2 ) / |p1 - p2|^3
#
#      m2 p2'' = - m2 m0 ( p2 - p0 ) / |p2 - p0|^3 
#                - m2 m1 ( p2 - p1 ) / |p2 - p1|^3
#
#    Letting
#
#      y1 = p0(x)
#      y2 = p0(y)
#      y3 = p0'(x)
#      y4 = p0'(y)
#
#    and using similar definitions for p1 and p2, the 3 second order vector 
#    equations can be rewritten as 12 first order equations.  In particular,
#    the first four are:
#
#      y1' = y3
#      y2' = y4
#      y3' = - m1 ( y1 - y5  ) / |(y1,y2) - (y5,y6) |^3 
#            - m2 ( y1 - y9  ) / |(y1,y2) - (y9,y10)|^3
#      y4' = - m1 ( y2 - y6  ) / |(y1,y2) - (y5,y6) |^3 
#            - m2 ( y2 - y10 ) / |(y1,y2) - (y9,y10)|^3
#
#    and so on.
#
#    This first order system can be integrated by a standard ODE solver.
#
#    Note that when any two bodies come close together, the solution changes
#    very rapidly, and very small steps must be taken by the ODE solver.
#    For this system, the first near collision occurs around T=15.8299, and
#    the results produced by MATLAB's ode45 will not be very accurate after
#    that point.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dominik Gruntz, Joerg Waldvogel,
#    Orbits in the Planar Three-Body Problem,
#    Walter Gander, Jiri Hrebicek, editors,
#    Solving Problems in Scientific Computing using Maple and Matlab,
#    Springer, 1997,
#    ISBN: 3-540-61793-0,
#    LC: Q183.9.G36.
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'three_body_solve_ivp():' )
  print ( '  Use solve_ivp() to solve three_body_ode().' )
#
#  Get parameters.
#
  m0, m1, m2, t0, y0, tstop = three_body_parameters ( )
#
#  Set the time range.
#
  f = three_body_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 501 )
#
#  Integrate the ODE.
#
  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Display the results.
#
  i10 = np.argmin ( np.abs ( t - 10.0 ) )
  plt.plot ( \
    sol.y[0,0:i10], sol.y[1,0:i10], 'b.', \
    sol.y[4,0:i10], sol.y[5,0:i10], 'r.', \
    sol.y[8,0:i10], sol.y[9,0:i10], 'g.' )
  plt.title ( 'three_body_ode(): 0 <= T <= 10' )
  filename = 'three_body_1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  i20 = np.argmin ( np.abs ( t - 20.0 ) )
  plt.plot ( \
    sol.y[0,i10:i20], sol.y[1,i10:i20], 'b.', \
    sol.y[4,i10:i20], sol.y[5,i10:i20], 'r.', \
    sol.y[8,i10:i20], sol.y[9,i10:i20], 'g.' )
  plt.title ( 'three_body_ode(): 10 <= T <= 20' )
  filename = 'three_body_2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  i50 = np.argmin ( np.abs ( t - 50.0 ) )
  i63 = len ( t )
  plt.plot ( \
    sol.y[0,i50:], sol.y[1,i50:i63], 'b.', \
    sol.y[4,i50:i63], sol.y[5,i50:i63], 'r.', \
    sol.y[8,i50:i63], sol.y[9,i50:i63], 'g.' )
  plt.title ( 'three_body_ode(): 50 <= T <= 63' )
  filename = 'three_body_3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( \
    sol.y[0,:], sol.y[1,:], 'b.', \
    sol.y[4,:], sol.y[5,:], 'r.', \
    sol.y[8,:], sol.y[9,:], 'g.' )
  plt.title ( 'three_body_ode(): 0 <= T <= 63' )
  filename = 'three_body_4.png'
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
  three_body_ode_test ( )
  timestamp ( )

