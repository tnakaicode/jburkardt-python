#! /usr/bin/env python3
#
def leapfrog ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## leapfrog() solves an ODE using the leapfrog method.
#
#  Discussion:
#
#    There are two crucial assumptions:
#
#    1) The number of variables is 2.
#    2) Written as a first order system, the ODE has the form
#       u' = v
#       v' = f(t,u)   NO DEPENDENCE ON V
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2020
#
#  Author:
#
#    Original Python version by John D Cook;
#    This version by John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Leapfrog integrator,
#    https://www.johndcook.com/blog/2020/07/13/leapfrog-integrator/
#    13 July 2020.
#
#  Input:
#
#    function dydt: evaluates the right hand side of the ODE.
#
#    real tspan[2]: contains the initial and final times.
#
#    real y0[2]: the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t[n+1], y[n+1,2]: the times and solution values.
#
  import numpy as np

  t0 = tspan[0]
  tstop = tspan[1]
  dt = ( tstop - t0 ) / n

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, 2 ] )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      t[0]   = t0
      y[0,0] = y0[0]
      y[0,1] = y0[1]
      anew   = dydt ( t, y[i,:] )
    else:
      t[i]   = t[i-1] + dt
      aold   = anew
      y[i,0] = y[i-1,0] + dt * ( y[i-1,1] + 0.5 * dt * aold[1] )
      anew   = dydt ( t, y[i,:] )
      y[i,1] = y[i-1,1] + 0.5 * dt * ( aold[1] + anew[1] )
  
  return t, y

def leapfrog_test ( ):

#*****************************************************************************80
#
## leapfrog_test() tests leapfrog().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'leapfrog_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test leapfrog().' )

  n = 80
  shm_leapfrog ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'leapfrog_test():' )
  print ( '  Normal end of execution.' )
  return

def shm_deriv ( t, y ):

#*****************************************************************************80
#
## shm_deriv() evaluates the right hand side of shm_ode().
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

  dydt = np.zeros ( 2 )

  dydt[0] =   y[1]
  dydt[1] = - y[0]

  return dydt

def shm_exact ( t ):

#*****************************************************************************80
#
## shm_exact() evaluates the exact solution of shm_ode().
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
#  Input:
#
#    real T(:): the evaluation times.
#
#  Output:
#
#    real Y(:,2): the exact solution values.
#
  import numpy as np

  n = len ( t )

  y = np.zeros ( [ n, 2 ] )

  y[:,0] = np.sin ( t )
  y[:,1] = np.cos ( t )

  return y

def shm_leapfrog ( n ):

#*****************************************************************************80
#
## shm_leapfrog() uses leapfrog() to solve shm_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2020
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

  print ( '' )
  print ( 'shm_leapfrog():' )
  print ( '  Use leapfrog() to solve shm_ode().' )
#
#  Get parameters.
#
  t0, y0, tstop = shm_parameters ( )

  dydt = shm_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = leapfrog ( dydt, tspan, y0, n )

  print ( '' )
  print ( '  Number of equal steps is', n )

  ye = shm_exact ( t )

  plt.plot ( t, y[:,0], 'ro', linewidth = 2 )
  plt.plot ( t, ye[:,0], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y1(T) --->' )
  plt.title ( 'shm leapfrog: Y1(t)' )
  plt.legend ( [ 'Leapfrog', 'Exact' ] )
  filename = 'shm_leapfrog_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, y[:,1], 'ro', linewidth = 2 )
  plt.plot ( t, ye[:,1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y2(T) --->' )
  plt.title ( 'shm leapfrog: Y2(t)' )
  plt.legend ( [ 'Leapfrog', 'Exact' ] )
  filename = 'shm_leapfrog_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Y1(T) --->' )
  plt.ylabel ( '<--- Y2(T) --->' )
  plt.title ( 'shm leapfrog: Phase' )
  filename = 'shm_leapfrog_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = 0.5 * ( y[:,0]**2 + y[:,1]**2 )

  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H(T) --->' )
  plt.title ( 'shm leapfrog: conservation' )
  filename = 'shm_leapfrog_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def shm_parameters ( ):

#*****************************************************************************80
#
## shm_parameters() returns parameters for shm_ode().
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
#  Output:
#
#    real T0: the initial time.
#
#    real Y0: the initial value.
#
#    real TSTOP: the final time.
#
  import numpy as np

  t0 = 0.0;
  y0 = np.array ( [ 0.0, 1.0 ] )
  tstop = 5 * 2.0 * np.pi

  return t0, y0, tstop

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
  leapfrog_test ( )
  timestamp ( )

