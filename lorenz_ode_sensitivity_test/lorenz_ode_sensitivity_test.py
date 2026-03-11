#! /usr/bin/env python3
#
def lorenz_ode_sensitivity_test ( ):

#*****************************************************************************80
#
## lorenz_ode_sensitivity_test() shows sensivitity of Lorenz ODE solutions.
#
#  Discussion:
#
#    This program demonstrates that small changes in the initial 
#    condition for the Lorenz equations can result in enormous changes
#    in the subsequent solution trajectories.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2020
#
#  Author:
#
#    Original Python version by John Cook.
#    This version by John Burkardt.
#
#  Reference:
#
#    John Cook,
#    A different view of the Lorenz system,
#    https://www.johndcook.com/blog/
#    26 January 2020.
#    
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'lorenz_ode_sensitivity_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Demonstrate sensitive dependence on initial data for the Lorenz system.' )
  print ( '  This program is based on the work of John D Cook.' )

  a = 0.0
  b = 40.0
  t = np.linspace ( a, b, 4000 )

  sol1 = solve_ivp ( lorenz_deriv, [a, b], [1,1,1], t_eval = t ) 
  sol2 = solve_ivp ( lorenz_deriv, [a, b], [1,1,1.00001], t_eval = t )
#
#  Plot phase portrait (x1,z1).
#
  plt.plot ( sol1.y[0], sol1.y[2] )
  plt.xlabel ( "$x$" )
  plt.ylabel ( "$z$" )
  filename = "lorenz_ode_sensitivity_test_x1z1.png"
  print ( '  Graphics saved as "', filename, '".' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot evolution (t,x1) and error evolution (t,x1-x2).
#
  plt.subplot ( 211 )
  plt.plot ( sol1.t, sol1.y[0] )
  plt.grid ( True )
  plt.xlabel ("$t$" )
  plt.ylabel ("$x_1(t)$" )

  plt.subplot ( 212 )
  plt.plot ( sol1.t, sol1.y[0] - sol2.y[0] )
  plt.grid ( True )
  plt.xlabel ( "$t$" )
  plt.ylabel ( "$x_1(t) - x_2(t)$" )
  filename = "lorenz_ode_sensitivity_test_xdif.png"
  print ( '  Graphics saved as "', filename, '".' )
  plt.savefig ( filename ) 
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lorenz_ode_sensitivity_test:' )
  print ( '  Normal end of execution.' )
  return

def lorenz_deriv ( t, xyz ):

#*****************************************************************************80
#
## lorenz_deriv() evaluates the Lorenz ODE right hand side.
#
#  Discussion:
#
#    The values of parameters sigma, rho and beta correspond to those used by
#    Lorenz in his original report.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the current time.
#
#    real XYZ[3]: the current values of X, Y, Z.
#
#  Output:
#
#    real DXYZDT[3]: the current values of X', Y', Z'.
#
  x, y, z = xyz

  sigma = 10.0
  rho = 28.0
  beta = 8.0 / 3.0

  dxyzdt = [ \
    sigma * ( y - x ), \
    x * ( rho - z ) - y, \
    x * y - beta * z ]

  return dxyzdt

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
#    06 April 2013
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
  lorenz_ode_sensitivity_test ( )
  timestamp ( )

