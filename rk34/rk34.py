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
#    04 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = y[0]
  f = y[1]

  drdt =   2.0 * r - 0.001 * r * f
  dfdt = -10.0 * f + 0.002 * r * f

  value = np.array ( [ drdt, dfdt ] )

  return value

def predator_rk3 ( ):

#*****************************************************************************80
#
## predator_rk3() calls rk3() with specific values of n, a, b, and y0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2022
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
  
  t, y = rk3 ( f, tspan, y0, n )

  dt = ( tspan[1] - tspan[0] ) / n

  plt.clf ( )
  plt.plot ( t, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  label = 'Predator rk3 solution with dt = ' + str ( dt )
  plt.title ( label )
  filename = 'predator_rk3_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Prey(T) -->' )
  plt.ylabel ( '<-- Predators(T) -->' )
  label = 'Predator rk3 solution with dt = ' + str ( dt )
  plt.title ( label )
  filename = 'predator_rk3_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def predator_rk4 ( ):

#*****************************************************************************80
#
## predator_rk4() calls rk4() with specific values of n, a, b, and y0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2022
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
  
  t, y = rk4 ( f, tspan, y0, n )

  dt = ( tspan[1] - tspan[0] ) / n

  plt.clf ( )
  plt.plot ( t, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  label = 'Predator rk4 solution with dt = ' + str ( dt )
  plt.title ( label )
  filename = 'predator_rk4_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Prey(T) -->' )
  plt.ylabel ( '<-- Predators(T) -->' )
  label = 'Predator rk4 solution with dt = ' + str ( dt )
  plt.title ( label )
  filename = 'predator_rk4_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return
  
def rk34 ( yprime, tspan, y0, n ):

#*****************************************************************************80
#
## rk34() uses explicit Runge-Kutta schemes of order 3 and 4.
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
#    04 January 2022
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
#    real e(n+1,m): an estimate for the additional error at each step.
#
  import numpy as np

  m = len ( y0 )
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  e = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / n

  t[0] = tspan[0]
  y[0,:] = y0.copy ( )

  a = np.array ( [ \
    [        0.0,           0.0,          0.0,        0.0 ], \
    [        0.25,          0.0,          0.0,        0.0 ], \
    [    4.0/81.0,    32.0/81.0,          0.0,        0.0 ], \
    [   57.0/98.0, -432.0/343.0, 1053.0/686.0,        0.0 ], \
    [     1.0/6.0,          0.0,    27.0/52.0, 49.0/156.0 ] ] )

  b3 = np.array ( [    1.0/6.0, 0.0,   27.0/52.0,   49.0/156.0 ] )
  b4 = np.array ( [ 43.0/288.0, 0.0, 243.0/416.0, 343.0/1872.0, 1.0/12.0 ] )
  c = np.array ( [ 0.0, 0.25, 4.0/9.0, 6.0/7.0, 1.0 ] )

  for i in range ( 0, n ):

    k1 = dt * ( yprime ( t[i] + c[0] * dt, y[i,:] ) )
    k2 = dt * ( yprime ( t[i] + c[1] * dt, y[i,:] + a[1,0] * k1 ) )
    k3 = dt * ( yprime ( t[i] + c[2] * dt, y[i,:] + a[2,0] * k1 \
      + a[2,1] * k2 ) )
    k4 = dt * ( yprime ( t[i] + c[3] * dt, y[i,:] + a[3,0] * k1 \
      + a[3,1] * k2 + a[3,2] * k3 ) )
    k5 = dt * ( yprime ( t[i] + c[3] * dt, y[i,:] + a[4,0] * k1 \
      + a[4,1] * k2 + a[4,2] * k3 + a[4,3] * k4 ) )

    y3 = y[i,:] + b3[0] * k1 + b3[1] * k2 + b3[2] * k3 + b3[3] * k4
    y4 = y[i,:] + b4[0] * k1 + b4[1] * k2 + b4[2] * k3 + b4[3] * k4 + b4[4] * k5

    t[i+1] = t[i] + dt
    y[i+1,:] = y4.copy ( )
    e[i+1,:] = y4 - y3

  return t, y, e 

def rk34_test ( ):

#*****************************************************************************80
#
## rk34_test() tests rk34().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rk34_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rk34().' )

  predator_rk3 ( )
  predator_rk4 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rk34_test():' )
  print ( '  Normal end of execution.' )

  return

def rk3 ( yprime, tspan, y0, n ):

#*****************************************************************************80
#
## rk3() uses an explicit Runge-Kutta scheme of order 3.
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
#    04 January 2022
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
  y[0,:] = y0.copy ( )

  for i in range ( 0, n ):

    k1 = dt * yprime ( t[i],            y[i,:] )
    k2 = dt * yprime ( t[i] + dt,       y[i,:] + k1 )
    k3 = dt * yprime ( t[i] + 0.5 * dt, y[i,:] + 0.25 * k1 + 0.25 * k2 )

    y3 = y[i,:] + ( k1 + k2 + 4.0 * k3 ) / 6.0

    t[i+1] = t[i] + dt
    y[i+1,:] = y3.copy ( )

  return t, y

def rk4 ( yprime, tspan, y0, n ):

#*****************************************************************************80
#
## rk4() uses an explicit Runge-Kutta scheme of order 4.
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
#    04 January 2022
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
  y[0,:] = y0.copy ( )

  a = np.array ( [ \
      [       0.0,          0.0,          0.0,        0.0 ], \
      [      0.25,          0.0,          0.0,        0.0 ], \
      [  4.0/81.0,    32.0/81.0,          0.0,        0.0 ], \
      [ 57.0/98.0, -432.0/343.0, 1053.0/686.0,        0.0 ], \
      [   1.0/6.0,          0.0,    27.0/52.0, 49.0/156.0 ] ] )

  b = np.array ( [ 43.0/288.0, 0.0, 243.0/416.0, 343.0/1872.0, 1.0/12.0 ] )
  c = np.array ( [ 0.0, 0.25, 4.0/9.0, 6.0/7.0, 1.0 ] )
 
  for i in range ( 0, n ):

    k1 = dt * yprime ( t[i] + c[0] * dt, y[i,:] )
    k2 = dt * yprime ( t[i] + c[1] * dt, y[i,:] + a[1,0] * k1 )
    k3 = dt * yprime ( t[i] + c[2] * dt, y[i,:] + a[2,0] * k1 \
      + a[2,1] * k2 )
    k4 = dt * yprime ( t[i] + c[3] * dt, y[i,:] + a[3,0] * k1 \
      + a[3,1] * k2 + a[3,2] * k3 )
    k5 = dt * yprime ( t[i] + c[3] * dt, y[i,:] + a[4,0] * k1 \
      + a[4,1] * k2 + a[4,2] * k3 + a[4,3] * k4 )

    y4 = y[i,:] + b[0] * k1 + b[1] * k2 + b[2] * k3 + b[3] * k4 + b[4] * k5

    t[i+1] = t[i] + dt
    y[i+1,:] = y4.copy ( )

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
  rk34_test ( )
  timestamp ( )

