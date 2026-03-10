#! /usr/bin/env python3
#
def b1g3_test ( ):

#*****************************************************************************80
#
## b1g3_test() tests b1g3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'big3_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test b1g3().' )

  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 200
  predator_prey_b1g3 ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 1.0 ] )
  y0 = np.array ( [ 0.0 ] )
  n = 27
  stiff_b1g3 ( tspan, y0, n )

  tspan = np.array ( [ 0.0, 2.0 ] )
  y0 = np.array ( [ humps_exact ( tspan[0] ) ] )
  n = 50
  humps_b1g3 ( tspan, y0, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'b1g3_test():' )
  print ( '  Normal end of execution.' )

  return

def b1g3 ( f, tspan, y0, n ):

#*****************************************************************************80
#
## b1g3() uses B1G3 + fsolve() to solve an ODE.
#
#  Discussion:
#
#    The first step is taken using the implicit midpoint method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2025
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

  m = len ( y0 )
  t = np.linspace ( tspan[0], tspan[1], n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / n

  for i in range ( 0, n + 1 ):
#
#  Initial condition:
#
    if ( i == 0 ):

      y[i,:] = y0[:]
#
#  Midpoint method for first step.
#
    elif ( i == 1 ):

      t1 = t[i-1]
      y1 = y[i-1,:]

      t2 = t1 + 0.5 * dt 
      y2 = y1 + 0.5 * dt * f ( t1, y1 )

      y2 = fsolve ( midpoint_residual, y2, args = ( f, t1, y1, t2 ) )

      y[i,:] = 2.0 * y2 - y[i-1,:]
#
#  B1G3 step after we have at least two previous estimates.
#
    else:

      t1 = t[i-2]
      y1 = y[i-2,:]
      t2 = t[i-1]
      y2 = y[i-1,:]
      t3 = t[i]
      y3 = y2 + dt * f ( t2, y2 )

      y3 = fsolve ( b1g3_residual, y3, args = ( f, dt, t1, t2, t3, y1, y2 ) )

      y[i,:] = y3

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
  value = yh - yo - ( th - to ) * f ( th, yh )

  return value

def b1g3_residual ( y3, f, dt, t1, t2, t3, y1, y2 ):

#*****************************************************************************80
#
## b1g3_residual() evaluates the B1G3 residual.
#
#  Discussion:
#
#    Given solution data (T1,Y1), (T2,Y2) and estimated (T3,Y3),
#    where T2=T1+DT, T3=T2+DT.
#
#    We are seeking a value Y3 defined by the implicit equation:
#
#      A3 Y3 + A2 Y2 + A1 Y1 = 2 * DT * F ( TM, YM )
#
#    where TM is determined, and YM is to be solved for:
#
#      2 A3 TM = A3 (1+B) T3 - A2 * (1-B) T2 - A1 (1-B) T1
#      2 A3 YM = A3 (1+B) Y3 - A2 * (1-B) Y2 - A1 (1-B) Y1
#
#    with
#
#      A3 =   1/2 + 1/sqrt(3)       
#      A2 =       - 2/sqrt(3)
#      A1 = - 1/2 + 1/sqrt(3)
#      B =          1/sqrt(3)
#
#    which guarantees that:

#      A3+A2+A1=0 
#    and
#      A3 (1+B) - A2 * (1-B) - A1 (1-B) = 2 A3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real y3: the solution at new (estimated) time.
#
#    function handle f: evaluates the right hand side of the ODE.  
#
#    real dt: the time step size
#
#    real t1, t2, t3: the times
#
#    real y1, y2: the solution at old and current times.
#
#  Output:
#
#    real value: the residual.
#
  import numpy as np

  a3 =   0.5 + 1.0 / np.sqrt ( 3.0 )
  a2 =       - 2.0 / np.sqrt ( 3.0 )
  a1 = - 0.5 + 1.0 / np.sqrt ( 3.0 )
  b  =         1.0 / np.sqrt ( 3.0 )

  tm = 0.5 * ( a3 * (1+b) * t3 - a2 * (1-b) * t2 - a1 * (1-b) * t1 ) / a3
  ym = 0.5 * ( a3 * (1+b) * y3 - a2 * (1-b) * y2 - a1 * (1-b) * y1 ) / a3

  value = a3 * y3 + a2 * y2 + a1 * y1 - 2.0 * dt * f ( tm, ym )

  return value

def humps_b1g3 ( tspan, y0, n ):

#*****************************************************************************80
#
## humps_b1g3() solves the humps ODE using b1g3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2025
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
  print ( 'humps_b1g3():' )
  print ( '  Solve the humps ODE using b1g3().' )

  t, y = b1g3 ( humps_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = humps_exact ( t2 )

  plt.plot ( t, y, 'b-', linewidth = 2 )
  plt.plot ( t2, y2, 'r.', markersize = 10 )

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
  plt.title ( 'humps ODE solved by b1g3()' )

  filename = 'b1g3_humps.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def humps_deriv ( t, y ):

#*****************************************************************************80
#
## humps_deriv() evaluates the derivative of the humps function.
#
#  Discussion:
#
#    y = 1.0 / ( ( t - 0.3 )^2 + 0.01 ) \
#      + 1.0 / ( ( t - 0.9 )^2 + 0.04 ) \
#      - 6.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t[:], y[:]: the arguments.
#
#  Output:
#
#    real dydt[:]: the value of the derivative at t.
#
  dydt = - 2.0 * ( t - 0.3 ) / ( ( t - 0.3 )**2 + 0.01 )**2 \
         - 2.0 * ( t - 0.9 ) / ( ( t - 0.9 )**2 + 0.04 )**2

  return dydt

def humps_exact ( t ):

#*****************************************************************************80
#
## humps_exact() evaluates the solution of humps_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  y = 1.0 / ( ( t - 0.3 )**2 + 0.01 ) \
    + 1.0 / ( ( t - 0.9 )**2 + 0.04 ) \
    - 6.0

  return y

def predator_prey_b1g3 ( tspan, y0, n ):

#*****************************************************************************80
#
## predator_prey_b1g3(): solve using b1g3().
#
#  Discussion:
#
#    The physical system under consideration is a pair of animal populations.
#
#    The PREY reproduce rapidly for each animal alive at the beginning of the
#    year, two more will be born by the end of the year.  The prey do not have
#    a natural death rate instead, they only die by being eaten by the predator.
#    Every prey animal has 1 chance in 1000 of being eaten in a given year by
#    a given predator.
#
#    The PREDATORS only die of starvation, but this happens very quickly.
#    If unfed, a predator will tend to starve in about 1/10 of a year.
#    On the other hand, the predator reproduction rate is dependent on
#    eating prey, and the chances of this depend on the number of available prey.
#
#    The resulting differential equations can be written:
#
#      PREY(0) = 5000         
#      PRED(0) =  100
#
#      d PREY / dT =    2 * PREY(T) - 0.001 * PREY(T) * PRED(T)
#      d PRED / dT = - 10 * PRED(T) + 0.002 * PREY(T) * PRED(T)
#
#    Here, the initial values (5000,100) are a somewhat arbitrary starting point.
#
#    The pair of ordinary differential equations that result have an interesting
#    behavior.  For certain choices of the interaction coefficients (such as
#    those given here), the populations of predator and prey will tend to 
#    a periodic oscillation.  The two populations will be out of phase the number
#    of prey will rise, then after a delay, the predators will rise as the prey
#    begins to fall, causing the predator population to crash again.
#
#    There is a conserved quantity, which here would be:
#      E(r,f) = 0.002 r + 0.001 f - 10 ln(r) - 2 ln(f)
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2025
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
#    real TSPAN = [ T0, TMAX ], the initial and final times.
#    A reasonable value might be [ 0, 5 ].
#
#    real Y0 = [ PREY, PRED ], the initial number of prey and predators.
#    A reasonable value might be [ 5000, 100 ].
#
#    integer N: the number of time steps.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_b1g3():' )
  print ( '  A pair of ordinary differential equations for a population' )
  print ( '  of predators and prey are solved using b1g3(),' )
  print ( '  solving the implicit function using fsolve().' )
  print ( '' )
  print ( '  The exact solution shows periodic behavior, with a fixed' )
  print ( '  period and amplitude.' )

  t, y = b1g3 ( predator_prey_deriv, tspan, y0, n )
#
#  Plot the solution.
#
  plt.plot ( y[:,0], y[:,1], 'b-', linewidth = 2 )
  plt.plot ( y[0,0], y[0,1], 'go', markersize = 10 )
  plt.plot ( y[-1,0], y[-1,1], 'ro', markersize = 10 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator prey ODE solved by b1g3()' )
  plt.legend ( [ 'Computed', 'Initial Condition', 'Last Solution' ] )
  filename = 'b1g3_predator_prey.png'
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
#    29 April 2021
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
#    real DYDT[2], the right hand side of the ODE.
#
  import numpy as np

  r = y[0]
  f = y[1]

  drdt =    2.0 * r - 0.001 * r * f
  dfdt = - 10.0 * f + 0.002 * r * f

  dydt = np.array ( [ drdt, dfdt ] )

  return dydt

def stiff_b1g3 ( tspan, y0, n ):

#*****************************************************************************80
#
## stiff_b1g3() uses b1g3 on the stiff ODE.
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
#    06 November 2025
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
  print ( 'stiff_b1g3()' )
  print ( '  Use b1g3() to solve the stiff ODE.' )

  t1, y1 = b1g3 ( stiff_deriv, tspan, y0, n )

  t2 = np.linspace ( tspan[0], tspan[1], 101 )
  y2 = stiff_exact ( t2 )

  plt.plot ( t1, y1, 'ro-', linewidth = 3 )
  plt.plot ( t2, y2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stiff ode with b1g3()' )
  plt.legend ( [ 'Computed', 'Exact' ] )
  filename = 'b1g3_stiff.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
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
  b1g3_test ( )
  timestamp ( )


