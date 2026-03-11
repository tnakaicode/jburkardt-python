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

  p = y[0]
  q = y[1]

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

def oscillator_ode_test ( ):

#*****************************************************************************80
#
## oscillator_ode_test() tests oscillator_ode().
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
  print ( 'oscillator_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
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

  oscillator_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'oscillator_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def oscillator_solve_ivp ( ):

#*****************************************************************************80
#
## oscillator_solve_ivp() applies solve_ivp() to oscillator_ode().
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

  alpha, beta, epsilon, t0, y0, tstop = oscillator_parameters ( )

  f = oscillator_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Solution plot.
#
  plt.plot ( t, sol.y[0,:], 'g', \
             t, sol.y[1,:], 'r', \
             linewidth = 2 )
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
  plt.plot ( sol.y[0,:], sol.y[1,:], linewidth = 2 )
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
  h = oscillator_conserved ( sol.y )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  oscillator_ode_test ( )
  timestamp ( )

