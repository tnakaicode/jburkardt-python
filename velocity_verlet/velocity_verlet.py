#! /usr/bin/env python3
#
def oscillator_conserved ( y ):

#*****************************************************************************80
#
## oscillator_conserved() defines a conserved quantity of oscillator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Uri Ascher, Sebastian Reich,
#    The midpoint scheme and variants for hamiltonian systems:
#    advantages and disadvantages,
#    SIAM Journal on Scientific Computing,
#    Volume 21, Number 3, pages 1045-1065, 1999.
#
#  Input:
#
#    real Y(2): the current solution variables.
#
#  Output:
#
#    real H: the hamiltonian.
#
  alpha, beta, epsilon, t0, y0, tstop = oscillator_parameters ( )

  p = y[:,0]
  q = y[:,1]

  h = ( p / epsilon )**2 + ( q**2 )

  return h

def oscillator_deriv ( t, y ):

#*****************************************************************************80
#
## oscillator_deriv() defines the right hand side of oscillator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Uri Ascher, Sebastian Reich,
#    The midpoint scheme and variants for hamiltonian systems:
#    advantages and disadvantages,
#    SIAM Journal on Scientific Computing,
#    Volume 21, Number 3, pages 1045-1065, 1999.
#
#  Input:
#
#    real T: the current time.
#
#    real Y(2): the current solution variables.
#
#  Output:
#
#    real DYDT(2): the derivative.
#
  import numpy as np

  alpha, beta, epsilon, t0, y0, tstop = oscillator_parameters ( )

  p = y[0]
  q = y[1]

  dpdt = q
  dqdt = - p / epsilon**2

  dydt = np.array ( [ dpdt, dqdt ] )

  return dydt

def oscillator_exact ( t ):

#*****************************************************************************80
#
## oscillator_exact() defines the exact solution of oscillator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Uri Ascher, Sebastian Reich,
#    The midpoint scheme and variants for hamiltonian systems:
#    advantages and disadvantages,
#    SIAM Journal on Scientific Computing,
#    Volume 21, Number 3, pages 1045-1065, 1999.
#
#  Input:
#
#    real T: the current time.
#
#  Output:
#
#    real Y(2): the exact solution at time T.
#
  import numpy as np

  alpha, beta, epsilon, t0, y0, tstop = oscillator_parameters ( )

  p = alpha * epsilon * np.sin ( ( t - t0 ) / epsilon ) \
    + beta  * epsilon * np.cos ( ( t - t0 ) / epsilon )

  q = alpha * np.cos ( ( t - t0 ) / epsilon ) \
    - beta  * np.sin ( ( t - t0 ) / epsilon )

  y = np.array ( [ p, q ] )

  return y

def oscillator_velocity_verlet ( n ):

#*****************************************************************************80
#
## oscillator_velocity_verlet() solves oscillator_ode() using velocity_verlet.
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
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'oscillator_velocity_verlet():' )
  print ( '  Solve oscillator_ode().' )

  alpha, beta, epsilon, t0, y0, tstop = oscillator_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha =   ', alpha )
  print ( '    beta =    ', beta )
  print ( '    epsilon = ', epsilon )
  print ( '    t0 =      ', t0 )
  print ( '    y0 =      ', y0 )
  print ( '    tstop =   ', tstop )

  f = oscillator_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  t, y = velocity_verlet ( f, tspan, y0, n )

  print ( '' )
  print ( '  Number of equal steps taken was ', n )
#
#  Solution plot.
#
  plt.plot ( t, y[:,0], 'g', linewidth = 2 )
  plt.plot ( t, y[:,1], 'r', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'p(t), q(t)' )
  plt.title ( 'oscillator_ode() Time Plot' )
  plt.legend ( ( 'p(t)', 'q(t)' ) )
  filename = 'oscillator_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plane plot.
#
  plt.plot ( y[:,0], y[:,1], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- p(t) --->' )
  plt.ylabel ( '<--- q(t) --->' )
  plt.axis ( 'equal' )
  plt.title ( 'oscillator_ode() Phase Plot' )
  filename = 'oscillator_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Conservation plot.
#
  h = oscillator_conserved ( y )

  plt.plot ( t, h, linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- h(t) --->' )
  plt.title ( 'oscillator_ode() conservation' )
  filename = 'oscillator_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def oscillator_parameters ( ):

#*****************************************************************************80
#
## oscillator_parameters() returns parameters for oscillator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real ALPHA: the initial value of Y'
#
#    real BETA: the initial value of Y/EPSILON
#
#    real EPSILON: the period / ( 2*pi).
#
#    real T0: the initial time.
#
#    real Y0(2): the initial value.
#
#    real TSTOP: the final time.
#
  import numpy as np

  alpha = 0.0
  beta = 1.0
  epsilon = 0.1
  t0 = 0.0
  y0 = np.array ( [ beta * epsilon, alpha ] )
  tstop = 2.0 * np.pi

  return alpha, beta, epsilon, t0, y0, tstop

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

def velocity_verlet ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## velocity_verlet() solves an ODE using the Velocity Verlet method.
#
#  Discussion:
#
#    A fixed stepsize is used.
#
#    There should be just two variables:
#    U is the position
#    V is the velocity.
#
#    The ODE should have the form:
#
#    U' = V
#    V' = F(T,U)
#
#    Or, as a second order system:
#
#    u'' = f(t,u)
#
#    where f does NOT depend on u'.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle dydt: evaluates the right hand side of the ODE.
#
#    real tspan(2): the initial and final times.
#
#    real y0(2): the initial position and velocity.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t(n+1), y(n+1,2): the times, positions, and velocities.
#
  import numpy as np

  t0 = tspan[0]
  tstop = tspan[1]

  dt = ( tstop - t0 ) / float ( n )

  t = np.linspace ( t0, tstop, n + 1 )
  p = np.zeros ( n + 1 )
  v = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, 2 ] )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = y0[0]
      uvdot = dydt ( t[i], np.array ( [ p[i], v[i] ] ) )
      dv = 0.5 * dt * uvdot[1]
      v[i] = y0[1]
    else:
      w = v[i-1] + dv
      p[i] = p[i-1] + dt * w
      uvdot = dydt ( t[i], np.array ( [ p[i], v[i] ] ) )
      dv = 0.5 * dt * uvdot[1]
      v[i] = w + dv

    y[i,0] = p[i]
    y[i,1] = v[i]

  return t, y

def velocity_verlet_test ( ):

#*****************************************************************************80
#
## velocity_verlet_test() tests velocity_verlet().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'velocity_verlet_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test velocity_verlet().' )

  n = 50
  oscillator_velocity_verlet ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'velocity_verlet_test():' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  velocity_verlet_test ( )
  timestamp ( )

