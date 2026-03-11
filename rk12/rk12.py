#! /usr/bin/env python3
#
def predator_deriv ( t, y ):

#*****************************************************************************80
#
## predator_deriv() returns the right hand side of the predator test problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  drdt =   2.0 * y[0] - 0.001 * y[0] * y[1]
  dfdt = -10.0 * y[1] + 0.002 * y[0] * y[1]

  dydt = np.array ( [ drdt, dfdt ] )

  return dydt

def predator_rk12 ( ):

#*****************************************************************************80
#
## predator_rk12() calls rk12() with specific values of n, a, b, and y0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  f = predator_deriv
  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 1000

  t, y, e = rk12 ( f, tspan, y0, n )

  dt = ( tspan[1] - tspan[0] ) / n

  plt.clf ( )
  plt.plot ( t, e[:,0], 'g', linewidth = 3 )
  plt.plot ( t, e[:,1], 'r', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Error(T) -->' )
  label = ( 'Error with dt = %g' % ( dt ) )
  plt.title ( label )
  plt.legend ( [ 'Prey error', 'Predator error' ] )
  filename = 'error_rk12_time.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.plot ( e[:,0], e[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Prey Error(T) -->' )
  plt.ylabel ( '<-- Predator Error(T) -->' )
  label = ( 'Predator/prey error with dt = %g' % ( dt ) )
  plt.title ( label )
  filename = 'error_rk12_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def predator_rk1 ( ):

#*****************************************************************************80
#
## predator_rk1() calls rk1() with specific values of n, a, b, and y0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  f = predator_deriv
  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 1000
  
  t, y = rk1 ( f, tspan, y0, n )

  dt = ( tspan[1] - tspan[0] ) / n

  plt.clf ( )
  plt.plot ( t, y[:,0], 'g', linewidth = 3 )
  plt.plot ( t, y[:,1], 'r', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  label =  ( 'Predator/Prey RK1 solution with dt = %g' % ( dt ) )
  plt.title ( label )
  plt.legend ( [ 'Prey', 'Predator' ] )
  filename = 'predator_rk1_time.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Prey(T) -->' )
  plt.ylabel ( '<-- Predators(T) -->' )
  label = ( 'Predator/Prey RK1 solution phase with dt = %g' % ( dt ) )
  plt.title ( label )
  filename = 'predator_rk1_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def predator_rk2 ( ):

#*****************************************************************************80
#
## predator_rk2() calls rk2() with specific values of n, a, b, and y0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  f = predator_deriv
  tspan = np.array ( [ 0.0, 5.0 ] )
  y0 = np.array ( [ 5000, 100 ] )
  n = 1000

  t, y = rk2 ( f, tspan, y0, n )

  dt = ( tspan[1] - tspan[0] ) / n

  plt.clf ( )
  plt.plot ( t, y[:,0], 'g', linewidth = 3 )
  plt.plot ( t, y[:,1], 'r', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  label = ( 'predator/prey rk2 solution with dt = %g' % ( dt ) )
  plt.title ( label )
  plt.legend ( [ 'Prey', 'Predator' ] )
  filename = 'predator_rk2_time.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Prey(T) -->' )
  plt.ylabel ( '<-- Predator(T) -->' )
  label = ( 'Predator/Prey rk2 phase with dt = %g' % ( dt ) )
  plt.title ( label )
  filename = 'predator_rk2_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def rk12 ( yprime, tspan, y0, n ):

#*****************************************************************************80
#
## rk12() uses explicit Runge-Kutta schemes of order 1 and 2.
#
#  Discussion:
#
#    This function uses an explicit Runge-Kutta method of order 2 to
#    approximate the solution of a differential equation of the form:
#      y' = yprime(t,y)
#      y(tspan(1)) = y0
#    and estimates the approximation error by comparing the solution
#    obtained from a Runge-Kutta method of order 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle yprime: defines the derivative function of the form
#      value = yprime ( t, y )
#
#    real tspan(2): contains the initial and final times.
#
#    real y0(m): contains the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t(n+1): the times.
#
#    real y(n+1,m): the estimated solution values.
#
#    real e(n+1,m): an estimate for the error made at each step.
#
  import numpy as np

  m = len ( y0 )
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  e = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / n

  t[0] = tspan[0]
  y[0,:] = y0[:]
  e[0,:] = 0.0
 
  for i in range ( 0, n ):
    k1 = dt * yprime ( t[i],      y[i,:] )
    yt = y[i,:] + np.transpose ( k1 )
    k2 = dt * yprime ( t[i] + dt, y[i,:] + np.transpose ( k1 ) )
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + 0.5 * np.transpose ( k1 ) + 0.5 * np.transpose ( k2 )
    e[i+1,:] = y[i+1,:] - yt

  return t, y, e 

def rk12_test ( ):

#*****************************************************************************80
#
## rk12_test() tests rk12().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rk12_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rk12().' )

  predator_rk1 ( )
  predator_rk2 ( )
  predator_rk12 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rk12_test():' )
  print ( '  Normal end of execution.' )

  return

def rk1 ( yprime, tspan, y0, n ):

#*****************************************************************************80
#
## rk1() uses an explicit Runge-Kutta scheme of order 1.
#
#  Discussion:
#
#    This function approximates the solution of a differential
#    equation of the form:
#      y' = yprime(t,y)
#      y(tspan(1)) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle yprime: defines the derivative function of the form
#      value = yprime ( t, y )
#
#    real tspan(2): contains the initial and final times.
#
#    real y0(m): contains the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t(n+1): the times.
#
#    real y(n+1,m): the estimated solution values.
#
  import numpy as np

  m = len ( y0 )
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / n

  t[0] = tspan[0]
  y[0,:] = y0[:]
 
  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    k1 = dt * yprime ( t[i], y[i,:] )
    y[i+1,:] = y[i,:] + np.transpose ( k1 )

  return t, y

def rk2 ( yprime, tspan, y0, n ):

#*****************************************************************************80
#
## rk2() uses an explicit Runge-Kutta scheme of order 2.
#
#  Discussion:
#
#    This function approximates the solution of a differential
#    equation of the form:
#      y' = yprime(t,y)
#      y(tspan(1)) = y0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function handle yprime: defines the derivative function of the form
#      value = yprime ( t, y )
#
#    real tspan(2): contains the initial and final times.
#
#    real y0(m): contains the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t(n+1): the times.
#
#    real y(n+1,m): the estimated solution values.
#
  import numpy as np

  m = len ( y0 )
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / n

  t[0] = tspan[0]
  y[0,:] = y0[:]
 
  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    k1 = dt * yprime ( t[i],      y[i,:]      )
    k2 = dt * yprime ( t[i] + dt, y[i,:] + np.transpose ( k1 ) )
    y[i+1,:] = y[i,:] + 0.5 * np.transpose ( k1 ) + 0.5 * np.transpose ( k2 )

  return t, y

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
  rk12_test ( )
  timestamp ( )

