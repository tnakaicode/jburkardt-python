#! /usr/bin/env python3
#
def pendulum_double_conserved ( x ):

#*****************************************************************************80
#
## pendulum_double_conserved(): conserved quantity for pendulum_double_ode().
#
#  Discussion:
#
#    This quantity is the total energy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(4): theta1, dtheta1/dt, theta2, dtheta2/dt.
#
#  Output:
#
#    real E: the energy.
#
  import numpy as np

  g, m1, m2, l1, l2, t0, y0, tstop = pendulum_double_parameters ( )

  e = 0.5 * ( m1 + m2 ) * l1**2 * x[1]**2 \
    + 0.5 * m2 * l2**2 * x[3]**2 \
    + m2 * l1 * l2 * x[1] * x[3] * np.cos ( x[0] - x[2] ) \
    - ( m1 + m2 ) * g * l1 * np.cos ( x[0] ) \
    - m2 * g * l2 * np.cos ( x[2] )

  return e

def pendulum_double_deriv ( t, x ):

#*****************************************************************************80
#
## pendulum_double_deriv(): right hand side of pendulum_double_ode().
#
#  Discussion:
#
#    In the double pendulum problem, a rod of length l1 is fixed at
#    one end (0,0), and forms an angle theta1 with the downward vertical,
#    so that its endpoint is at (x1,y1) = (l1*cos(theta1),l1*sin(theta1)).
#    A weight of mass m1 is attached to this end of the first rod.
#
#    A second rod, of length l2 is also attached to this end of the
#    first rod.  It forms an angle theta2 with the downward vertical.
#    A weight of mass m2 is attached to the free end of the second rod.
#    The position of this weight is 
#    (x2,y2) = (x1,y1) + (l2*cos(theta2),l2*sin(theta2)).
#
#    Gravity has a force coefficient of G.
#
#    The unknowns are the angles and their time derivatives.
#    We store the unknowns in a vector X:
#
#      x(1) =   theta(1)
#      x(2) = d theta(1) dt
#      x(3) =   theta(2)
#      x(4) = d theta(2) dt
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the current time.
#
#    real X(4): the current solution.
#
#  Output:
#
#    real DXDT(4): the right hand side of the ODE.
#
#  Local:
#
#    real G: the gravitational force coefficient.
#
#    real M1, M2: the masses of pendulums 1 and 2.
#
#    real L1, L2: the lengths of pendulums 1 and 2.
#
  import numpy as np

  g, m1, m2, l1, l2, t0, y0, tstop = pendulum_double_parameters ( )

  dxdt = np.zeros(4)

  dxdt[0] = x[1]

  dxdt[1] = - \
  ( \
    (\
      g * ( 2.0 * m1 + m2 ) * np.sin ( x[0] ) + \
      m2 * \
      ( \
        g * np.sin ( x[0] - 2.0 * x[2] ) + 2.0 * \
        ( \
          l2 * x[3]**2 + l1 * x[1]**2 * np.cos ( x[0] - x[2] ) \
        ) \
        * np.sin ( x[0] - x[2] ) \
      ) \
    ) \
    / \
    ( \
     2.0 * l1 * ( m1 + m2 - m2 * ( np.cos ( x[0] - x[2] ) )**2 ) \
    ) \
  )

  dxdt[2] = x[3]

  dxdt[3] = \
  ( \
    ( \
      ( m1 + m2 ) * ( l1 * x[1]**2 + g * np.cos ( x[0] ) ) \
      + l2 * m2 * x[3]**2 * np.cos ( x[0] - x[2] ) \
    ) * \
    np.sin ( x[0] - x[2] ) \
  ) \
  / \
  ( \
    l2 * ( m1 + m2 - m2 * ( np.cos ( x[0] - x[2] ) )**2 ) \
  )

  return dxdt

def pendulum_double_ode_test ( ):

#*****************************************************************************80
#
## pendulum_double_ode_test() tests pendulum_double_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pendulum_double_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pendulum_double_ode().' )

  g, m1, m2, l1, l2, t0, y0, tstop = pendulum_double_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    g =     ', g )
  print ( '    m1 =    ', m1 )
  print ( '    m2 =    ', m2 )
  print ( '    l1 =    ', l1 )
  print ( '    l2 =    ', l2 )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  pendulum_double_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pendulum_double_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def pendulum_double_solve_ivp ( ):

#*****************************************************************************80
#
## pendulum_double_solve_ivp() applies solve_ivp() to pendulum_double_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  g, m1, m2, l1, l2, t0, y0, tstop = pendulum_double_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( pendulum_double_deriv, tspan, y0, t_eval = t )

  x1 =   l1 * np.sin ( sol.y[0] )
  y1 = - l1 * np.cos ( sol.y[0] )

  x2 = x1 + l2 * np.sin ( sol.y[2] )
  y2 = y1 - l2 * np.cos ( sol.y[2] )
#
#  Solution plot.
#
  plt.figure ( 0 )
  plt.plot ( t, x1, 'g', \
             t, y1, 'r', \
             linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'x1(t), y1(t)' )
  plt.legend ( ( 'x1(t)', 'y1(t)' ) )
  plt.title ( 'pendulum_double_ode(): (x1,y1)' )
  filename = 'pendulum_double_x1y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.figure ( 1 )
  plt.plot ( t, x2, 'g', \
             t, y2, 'r', \
             linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'x2(t), y2(t)' )
  plt.legend ( ( 'x2(t)', 'y2(t)' ) )
  plt.title ( 'pendulum_double_ode(): (x2,y2)' )
  filename = 'pendulum_double_x2y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plane plot.
#
  plt.figure ( 2 )
  plt.plot ( x1, y1, 'r-', linewidth = 3 )
  plt.plot ( x2, y2, 'b-', linewidth = 1 )
  plt.grid ( True )
  plt.xlabel ( '<--- x(t) --->' )
  plt.ylabel ( '<--- y(t) --->' )
  plt.legend ( ( '(x1,y1)', '(x2,y2)' ) )
  plt.axis ( 'equal' )
  plt.title ( 'pendulum_double_ode(): phase' )
  filename = 'pendulum_double_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Energy plot.
#
  plt.figure ( 3 )
  e = pendulum_double_conserved ( sol.y )
  plt.plot ( t, e, 'r-', linewidth = 3 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- energy --->' )
  plt.title ( 'pendulum_double_ode(): energy' )
  filename = 'pendulum_double_energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def pendulum_double_parameters ( g_user = None, m1_user = None, \
  m2_user = None, l1_user = None, l2_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## pendulum_double_parameters() returns parameters for pendulum_double_ode().
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
#    03 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real G_USER: the gravitational force coefficient.
#
#    real M1_USER: the mass of pendulum 1.
#
#    real M2_USER: the mass of pendulum 2.
#
#    real L1_USER: the length of pendulum 1.
#
#    real L2_USER: the length of pendulum 2.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real G: the gravitational force coefficient.
#
#    real M1: the mass of pendulum 1.
#
#    real M2: the mass of pendulum 2.
#
#    real L1: the length of pendulum 1.
#
#    real L2: the length of pendulum 2.
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
  if not hasattr ( pendulum_double_parameters, "g_default" ):
    pendulum_double_parameters.g_default = 9.81

  if not hasattr ( pendulum_double_parameters, "m1_default" ):
    pendulum_double_parameters.m1_default = 1.0

  if not hasattr ( pendulum_double_parameters, "m2_default" ):
    pendulum_double_parameters.m2_default = 1.0

  if not hasattr ( pendulum_double_parameters, "l1_default" ):
    pendulum_double_parameters.l1_default = 2.0

  if not hasattr ( pendulum_double_parameters, "l2_default" ):
    pendulum_double_parameters.l2_default = 1.0

  if not hasattr ( pendulum_double_parameters, "t0_default" ):
    pendulum_double_parameters.t0_default = 0.0

  if not hasattr ( pendulum_double_parameters, "y0_default" ):
    pendulum_double_parameters.y0_default = np.array ( [ 0.25, 0.0, 0.0, 0.0 ] )

  if not hasattr ( pendulum_double_parameters, "tstop_default" ):
    pendulum_double_parameters.tstop_default = 50.0
#
#  Update defaults if input was supplied.
#
  if ( g_user is not None ):
    pendulum_double_parameters.g_default = g_user

  if ( m1_user is not None ):
    pendulum_double_parameters.m1_default = m1_user

  if ( m2_user is not None ):
    pendulum_double_parameters.m2_default = m2_user

  if ( l1_user is not None ):
    pendulum_double_parameters.l1_default = l1_user

  if ( l2_user is not None ):
    pendulum_double_parameters.l2_default = l2_user

  if ( t0_user is not None ):
    pendulum_double_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    pendulum_double_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    pendulum_double_parameters.tstop_default = tstop_user
#
#  Return values.
#
  g = pendulum_double_parameters.g_default
  m1 = pendulum_double_parameters.m1_default
  m2 = pendulum_double_parameters.m2_default
  l1 = pendulum_double_parameters.l1_default
  l2 = pendulum_double_parameters.l2_default
  t0 = pendulum_double_parameters.t0_default
  y0 = pendulum_double_parameters.y0_default
  tstop = pendulum_double_parameters.tstop_default
  
  return g, m1, m2, l1, l2, t0, y0, tstop

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
  pendulum_double_ode_test ( )
  timestamp ( )

