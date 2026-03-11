#! /usr/bin/env python3
#
def solve_bvp_test ( ):

#*****************************************************************************80
#
## solve_bvp_test() uses solve_bvp() to solve Bratu's problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2022
#
#  Author:
#
#    John Burkardt.
#
  from scipy.integrate import solve_bvp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'solve_bvp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Use solve_bvp() to solve Bratu''s problem:' )
  print ( '  y" + k e^y = 0' )
  print ( '  0 <= x <= 1' )
  print ( '  y''(0) = 0, y''(1) = 0' )

  a = 0.0
  b = 1.0

  n_mesh = 5
  x_mesh = np.linspace ( a, b, n_mesh )
  ya_mesh = np.zeros ( [ 2, n_mesh ] )
  yb_mesh = np.zeros ( [ 2, n_mesh ] )
  yb_mesh[0] = 3.0

  sol_a = solve_bvp ( bratu_fun, bratu_bc, x_mesh, ya_mesh )
  sol_b = solve_bvp ( bratu_fun, bratu_bc, x_mesh, yb_mesh )
#
#  Use DEVAL to evaluate the solution.
#
  n_plot = 101
  x_plot = np.linspace ( a, b, n_plot )
  ya_plot = sol_a.sol ( x_plot )[0]
  yb_plot = sol_b.sol ( x_plot )[0]
#
#  Display a plot of Y and Y'.
#
  plt.clf ( )
  plt.plot ( x_plot, ya_plot, 'r-', linewidth = 2 )
  plt.plot ( x_plot, yb_plot, 'b-', linewidth = 2 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y(X) --->' )
  plt.title ( 'Bratu''s BVP solved by solve_bvp()' )
  plt.grid ( True )
  filename = 'solve_bvp_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'solve_bvp_test():' )
  print ( '  Normal end of execution.' )

  return

def bratu_fun ( x, y ):

#*****************************************************************************80
#
## bratu_fun() evaluates the right hand side of Bratu's BVP.
#
#  Discussion:
#
#    We assume that the differential equation has been rewritten as a
#    system of first order equations of the form
#
#      dydx = f(x,y)
#
#    u' = v
#    v' = - exp ( u )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the ODE is to be evaluated.
#
#    real Y(*), the value of the solution at X.
#
#    real LAMBDA, the estimated eigenvalue.
#
#  Output:
#
#    real DYDX(M), the value of the right hand side given X and Y.
#
  import numpy as np

  dydx = np.array ( [ y[1], - np.exp ( y[0] ) ] )

  return dydx

def bratu_bc ( ya, yb ):

#*****************************************************************************80
#
## bratu_bc() evaluates the boundary conditions for the Bratu BVP.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real YA(M), YB(M), the solution value at the left and right endpoints.
#
#  Output:
#
#    real BC(2), the value of the boundary conditions.
#
  import numpy as np

  bc = np.array ( [ ya[0], yb[0] ] ) 

  return bc

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
  solve_bvp_test ( )
  timestamp ( )

