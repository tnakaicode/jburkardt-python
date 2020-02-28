#! /usr/bin/env python3
#
def lorenz_sensitivity_test ( ):

#*****************************************************************************80
#
## lorenz_sensitivity_test shows sensivitity of solutions to the Lorenz system.
#
#  Discussion:
#
#    This program demonstrates that small changes in the initial 
#    condition for the Lorenz equations can result in enormous changes
#    in the subsequent solution trajectories.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 January 2020
#
#  Author:
#
#    John Cook.
#    Some modifications by John Burkardt.
#
#  Reference:
#
#    John Cook,
#    A different view of the Lorenz system,
#    https://www.johndcook.com/blog/
#    26 January 2020.
#    
  from scipy import linspace
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import platform

  print ( '' )
  print ( 'lorenz_sensitivity_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Demonstrate sensitive dependence on initial data for the Lorenz system.' )
  print ( '  This program is based on the work of John D Cook.' )

  a = 0.0
  b = 40.0
  t = linspace ( a, b, 4000 )

  sol1 = solve_ivp ( lorenz_ode, [a, b], [1,1,1], t_eval = t ) 
  sol2 = solve_ivp ( lorenz_ode, [a, b], [1,1,1.00001], t_eval = t )
#
#  Plot phase portrait (x1,z1).
#
  plt.plot ( sol1.y[0], sol1.y[2] )
  plt.xlabel ( "$x$" )
  plt.ylabel ( "$z$" )
  plt.show ( block = False )
  filename = "lorenz_sensitivity_test_x1z1.png"
  print ( '  Graphics saved as "', filename, '".' )
  plt.savefig ( filename )
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
  plt.show ( block = False )

  filename = "lorenz_sensitivity_test_xdif.png"
  print ( '  Graphics saved as "', filename, '".' )
  plt.savefig ( filename ) 
#
#  Terminate.
#
  print ( '' )
  print ( 'lorenz_sensitivity_test:' )
  print ( '  Normal end of execution.' )
  return

def lorenz_ode ( t, xyz ):

#*****************************************************************************80
#
## lorenz_ode evaluates the Lorenz ODE right hand side.
#
#  Discussion:
#
#    The values of parameters sigma, rho and beta correspond to those used by
#    Lorenz in his original report.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
#    real VALUE[3]: the current values of X', Y', Z'.
#
  x, y, z = xyz

  sigma = 10.0
  rho = 28.0
  beta = 8.0 / 3.0

  value = [ \
    sigma * ( y - x ), \
    x * ( rho - z ) - y, \
    x * y - beta * z ]

  return value

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  lorenz_sensitivity_test ( )
  timestamp ( )

