#! /usr/bin/env python3
#
def bdf3 ( f, tspan, y0, n ):

#*****************************************************************************80
#
## bdf3() uses backward difference formula 3 + fsolve() to solve an ODE.
#
#  Discussion:
#
#    The first step is taken using a Runge-Kutta method of order 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle f: evaluates the right hand side of the ODE.  
#
#    real tspan(2): the starting and ending times.
#
#    real y0(m): the initial conditions. 
#
#    integer n: the number of steps.
#
#  Output:
#
#    real t(n+1,1), y(n+1,m): the solution estimates.
#
  from scipy.optimize import fsolve
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t = np.linspace ( tspan[0], tspan[1], n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  for i in range ( 0, n + 1 ):
#
#  Initial condition.
#
    if ( i == 0 ):

      y[i,:] = y0.copy ( )
#
#  Use midpoint rule (only order 2)
#
    elif ( i <= 2 ):

      to = t[i-1]
      yo = y[i-1,:]
      th = t[i-1] + 0.5 * dt 
      yh = y[i-1,:] + 0.5 * dt * f ( t[i-1], y[i-1,:] )

      yh = fsolve ( backward_euler_residual, yh, args = ( f, to, yo, th ) )

      y[i,:] = 2.0 * yh - y[i-1,:]

    else:

      t1 = t[i-3]
      y1 = y[i-3,:]
      t2 = t[i-2]
      y2 = y[i-2,:]
      t3 = t[i-1]
      y3 = y[i-1,:]
      t4 = t[i] 
      y4 = y[i-1,:] + dt * f ( t[i-1], y[i-1,:] )

      y4 = fsolve ( bdf3_residual, y4, args = ( f, dt, t4, y1, y2, y3 ) )

      y[i,:] = y4.copy()

  return t, y

def backward_euler_residual ( yp, f, to, yo, tp ):

#*****************************************************************************80
#
## backward_euler_residual() evaluates the backward Euler residual.
#
#  Discussion:
#
#    We are seeking a value YP defined by the implicit equation:
#
#      YP = YO + ( TP - TO ) * F ( TP, YP )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yp: the estimated solution value at the new time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real tp: the new time.
#
#  Output:
#
#    real value: the residual.
#
  value = yp - yo - ( tp - to ) * f ( tp, yp )

  return value

def bdf3_residual ( y4, f, dt, t4, y1, y2, y3 ):

#*****************************************************************************80
#
## bdf3_residual() evaluates the bdf3 residual.
#
#  Discussion:
#
#    We are seeking a value Y3 defined by the implicit equation:
#
#      11 Y4 - 18 Y3 + 9 Y2 - 2 Y1 = 6 * DT * F ( T4, Y4 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real y4: the solution at the new (estimated) times.
#
#    function handle f: evaluates the right hand side of the ODE.  
#
#    real dt: the time step size
#
#    real t4: the new time
#
#    real y1, y2, y3: the solution at old, current times.
#
#  Output:
#
#    real value: the residual.
#
  value = 11.0 * y4 - 18.0 * y3 + 9.0 * y2 - 2.0 * y1 \
    - 6.0 * dt * f ( t4, y4 );

  return value

def bdf3_test ( ):

#*****************************************************************************80
#
## bdf3_test() tests bdf3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import scipy as sp

  print ( '' )
  print ( 'bdf3_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + sp.version.version )
  print ( '  Test bdf3().' )

  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 200
  predator_prey_bdf3 ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 1.0 ] )
  y0 = np.array ( [ 0.0 ] )
  n = 27
  stiff_bdf3 ( tspan, y0, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'bdf3_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def predator_prey_bdf3 ( tspan, y0, n ):

#*****************************************************************************80
#
## predator_prey_bdf3(): solve using bdf3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2025
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
  print ( 'predator_prey_bdf3():' )
  print ( '  A pair of ordinary differential equations for a population' )
  print ( '  of predators and prey are solved using the bdf3,' )
  print ( '  solving the implicit function using fsolve().' )
  print ( '' )
  print ( '  The exact solution shows periodic behavior, with a fixed' )
  print ( '  period and amplitude.' )

  f = predator_prey_deriv
  t, y = bdf3 ( f, tspan, y0, n )
#
#  Plot the solution.
#
  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator prey ODE solved by bdf3()' )
  filename = 'predator_prey_bdf3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def predator_prey_deriv ( t, y ):

#*****************************************************************************80
#
## predator_prey_deriv() evaluates the right hand side of the system.
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
#    real Y[2], the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real DYDT[2], the right hand side of the 2 ODE's.
#
  import numpy as np

  r = y[0]
  f = y[1]

  drdt =    2.0 * r - 0.001 * r * f
  dfdt = - 10.0 * f + 0.002 * r * f

  dydt = np.array ( [ drdt, dfdt ] )

  return dydt

def stiff_bdf3 ( tspan, y0, n ):

#*****************************************************************************80
#
## stiff_bdf3() uses bdf3 on the stiff ODE.
#
#  Discussion:
#
#    fsolve() is used to solve the backward Euler equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real TSPAN(2): the first and last times.
#
#    real Y0: the initial condition.
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stiff_bdf3()' )
  print ( '  Use bdf3() to solve the stiff ODE.' )

  t1, y1 = bdf3 ( stiff_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'ro-', linewidth = 3 )
  plt.plot ( t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff bdf3: time plot' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  filename = 'stiff_bdf3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def stiff_deriv ( t, y ):

#*****************************************************************************80
#
## stiff_deriv() evaluates the right hand side of the stiff equation.
#
#  Discussion:
#
#    y' = 50 * ( cos(t) - y )
#    y(0) = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y: the time and solution value.
#
#  Output:
#
#    real DYDT: the derivative value.
#
  import numpy as np

  dydt = 50.0 * ( np.cos ( t ) - y )

  return dydt

def stiff_exact ( t ):

#*****************************************************************************80
#
## stiff_exact() evaluates the exact solution of the stiff equation.
#
#  Discussion:
#
#    y' = 50 * ( cos(t) - y )
#    y(0) = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2020
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
#    real Y(:): the exact solution values.
#
  import numpy as np

  value = 50.0 * ( np.sin ( t ) + 50.0 * np.cos(t) \
    - 50.0 * np.exp ( - 50.0 * t ) ) / 2501.0

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
  bdf3_test ( )
  timestamp ( )

