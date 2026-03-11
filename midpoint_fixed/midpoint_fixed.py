#! /usr/bin/env python3
#
def midpoint_fixed ( f, tspan, y0, n ):

#*****************************************************************************80
#
## midpoint_fixed() uses a midpoint + fixed point to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2021
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
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  it_max = 10
  theta = 0.5

  t[0] = tspan[0];
  y[0,:] = y0

  for i in range ( 0, n ):

    xm = t[i] + theta * dt
    ym = y[i,:]

    for j in range ( 0, it_max ):
      ym = y[i,:] + theta * dt * f ( xm, ym )

    t[i+1] = t[i] + dt
    y[i+1,:] = (       1.0 / theta ) * ym \
             + ( 1.0 - 1.0 / theta ) * y[i,:]

  return t, y

def midpoint_fixed_test ( ):

#*****************************************************************************80
#
## midpoint_fixed_test() tests midpoint_fixed().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'midpoint_fixed_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test midpoint_fixed() for solving an ODE.' )

  tspan = np.array ( [ 0.0, 2.0 ] )
  y0 = 5.1765
  n = 100
  midpoint_fixed_humps_test ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 10.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 100
  midpoint_fixed_predator_prey_test ( tspan, y0, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'midpoint_fixed_test():' )
  print ( '  Normal end of execution.' )
  return

def midpoint_fixed_humps_test ( tspan, y0, n ):

#*****************************************************************************80
#
## midpoint_fixed_humps_test() solves humps_ode() using midpoint_fixed().
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
#    real tspan[2]: the time span
#
#    real y0[2]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'midpoint_fixed_humps_test():' )
  print ( '  Solve the humps_ode() using midpoint_fixed().' )

  t, y = midpoint_fixed ( humps_deriv, tspan, y0, n )

  plt.plot ( t, y, 'r-', linewidth = 2 )

  a = tspan[0]
  b = tspan[1]
  if ( a <= 0.0 and 0.0 <= b ):
    plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y(T) --->' )
  plt.title ( 'humps_ode() solved by midpoint_fixed()' )

  filename = 'midpoint_fixed_humps.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def midpoint_fixed_predator_prey_test ( tspan, y0, n ):

#*****************************************************************************80
#
## midpoint_fixed_predator_prey_test() solves predator_prey_ode() using midpoint_fixed().
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
#    real tspan[2]: the time span
#
#    real y0[2]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'midpoint_fixed_predator_prey_test():' )
  print ( '  Solve the predator_prey_ode() using midpoint_fixed().' )

  t, y = midpoint_fixed ( predator_prey_deriv, tspan, y0, n )


  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator prey ode solved by midpoint_fixed()' )

  filename = 'midpoint_fixed_predator_prey.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def humps_deriv ( x, y ):

#*****************************************************************************80
#
## humps_deriv() evaluates the derivative of humps_ode().
#
#  Discussion:
#
#    y = 1.0 ./ ( ( x - 0.3 )**2 + 0.01 ) \
#      + 1.0 ./ ( ( x - 0.9 )**2 + 0.04 ) \
#      - 6.0
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
#    real x[:], y[:]: the arguments.
#
#  Output:
#
#    real yp[:]: the value of the derivative at x.
#
  yp = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 )**2 + 0.01 )**2 \
       - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 )**2 + 0.04 )**2

  return yp

def predator_prey_deriv ( t, rf ):

#*****************************************************************************80
#
## predator_prey_deriv() evaluates the right hand side of predator_prey_ode().
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
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Input:
#
#    real T, the current time.
#
#    real RF[2], the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real DRFDT[2], the right hand side of the 2 ODE's.
#
  import numpy as np

  r = rf[0]
  f = rf[1]

  drdt =    2.0 * r - 0.001 * r * f
  dfdt = - 10.0 * f + 0.002 * r * f

  drfdt = np.array ( [ drdt, dfdt ] )

  return drfdt

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
  midpoint_fixed_test ( )
  timestamp ( )
 
