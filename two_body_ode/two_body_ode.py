#! /usr/bin/env python3
#
def initial_orbit ( ):

#*****************************************************************************80
#
## initial_orbit() simulates initial orbit of a small body around a large one.
#
#  Discussion:
#
#    Given two massive bodies subject to gravity, it is possible to write down
#    differential equations describing their motion.  These equations are
#    simpler to formulate in the frame of reference in which the center of 
#    mass of the two bodies does not move.  If one body is much more massive 
#    than the other, then our calculations in this new frame are essentially
#    the same as in the original geometry.  This is the case when one body
#    is the sun, and another a planet.  
#
#    This simulation would need to be modified if we wanted to consider
#    the behavior of two bodies of comparable mass, and expected to see
#    them both moving, or, even in the sun-planet case, if we wanted to
#    allow the sun to have a velocity while we stayed in a fixed frame
#    of reference.
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'initial_orbit():' )
  print ( '  This simulation follows a small body for two orbits' )
  print ( '  around a relatively massive body - such as Mercury around' )
  print ( '  the sun.' )
  print ( '  Kepler''s equations for a two body system are used.' )
  print ( '  Note that the orbit is NOT an ellipse.  But that''s OK,' )
  print ( '  because the planet is far from its equilibrium orbit.' )
#
#  Get the parameters, but reset TSTOP.
#
  t0, y0, tstop = two_body_parameters ( )
  tstop = 2.0 * 3.895
# t0, y0, tstop = two_body_parameters ( t0, y0, tstop )

  f = two_body_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 33 )
  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot the solution.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[2], 'b-' )
  plt.plot ( sol.y[0], sol.y[2], 'b.', markersize = 20 )
  plt.plot ( 0.0, 0.0, 'r.', markersize = 40 )
  plt.grid ( True )
  plt.title ( 'Two complete orbits' )
  plt.axis ( 'equal' )
  filename = 'initial_orbit.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def orbital_decay ( ):

#*****************************************************************************80
#
## orbital_decay() simulates the decay of an orbit to an equilibrium.
#
#  Discussion:
#
#    Given two massive bodies subject to gravity, it is possible to write down
#    differential equations describing their motion.  These equations are
#    simpler to formulate in the frame of reference in which the center of 
#    mass of the two bodies does not move.  If one body is much more massive 
#    than the other, then our calculations in this new frame are essentially
#    the same as in the original geometry.  This is the case when one body
#    is the sun, and another a planet.  
#
#    By giving an arbitrary initial condition for the system, we are likely
#    to have a planet whose orbit is not the classical ellipse we would
#    expect.  However, if we follow the orbit over time, we will see it
#    gradually decay to an ellipse.
#
#    This simulation would need to be modified if we wanted to consider
#    the behavior of two bodies of com-parable mass, and expected to see
#    them both moving, or, even in the sun-planet case, if we wanted to
#    allow the sun to have a velocity while we stayed in a fixed frame
#    of reference.
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'orbital_decay():' )
  print ( '  This simulation follows a small body for 20 orbits' )
  print ( '  around a relatively massive body - such as Mercury around' )
  print ( '  the sun.' )
  print ( '  Kepler''s equations for a two body system are used.' )
  print ( '  Initially, the orbit is NOT an ellipse, but as time passes,' )
  print ( '  the orbit decays into an elliptical shape.' )
#
#  Get the parameters, but reset TSTOP.
#
  t0, y0, tstop = two_body_parameters ( )
  tstop = 20.0 * 3.895
# t0, y0, tstop = two_body_parameters ( t0, y0, tstop )

  f = two_body_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 2001 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot the result.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[2], 'b-' )
  plt.plot ( 0.0, 0.0, 'r.', markersize = 40 )
  plt.grid ( True )
  plt.title ( 'Almost elliptical after 20 orbits' )
  plt.axis ( 'equal' )
  filename = 'orbital_decay'
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

def two_body_deriv ( t, u ):

#*****************************************************************************80
#
## two_body_deriv() evaluates the right hand side of two_body_ode().
#
#  Discussion:
#
#    two_body_ode() describes the positions in a plane of two gravitating 
#    bodies, one much more massive than the other.
#      
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2020
#
#  Input:
#
#    real T, the current time.
#
#    real U(4), the current state.
#
#  Output:
#
#    real UP(4), the derivative of the current state.
#
  import numpy as np

  r3 = ( u[0]**2 + u[2]**2 ) ** 1.5

  up = np.array ( [  
      u[1],       \
     -u[0] / r3,  \
      u[3],       \
     -u[2] / r3 ] )

  return up

def two_body_ode_test ( ):

#*****************************************************************************80
#
## two_body_ode_test() tests two_body_ode().
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
  print ( 'two_body_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test two_body_ode().' )

  t0, y0, tstop = two_body_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  initial_orbit ( )
  orbital_decay ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'two_body_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def two_body_parameters ( ):

#*****************************************************************************80
#
## two_body_parameters() returns the parameters of two_body_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  t0 = 0.0
  y0 = np.array ( [ 1.0, 0.0, 0.0, 0.8 ] )
  tstop = 2.0 * 3.895

  return t0, y0, tstop

if ( __name__ == '__main__' ):
  timestamp ( )
  two_body_ode_test ( )
  timestamp ( )

