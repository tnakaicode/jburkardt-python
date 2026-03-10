#! /usr/bin/env python3
#
epsilon = 1.0

def ill_bvp_test ( ):

#*****************************************************************************80
#
## iill_bvp_test() uses solve_bvp() to solve the ill conditioned BVP.
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

  global epsilon

  print ( '' )
  print ( 'ill_bvp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Use solve_bvp() to solve the ill conditioned BVP:' )
  print ( '  epsilon y" - xy'' + y = 0' )
  print ( '  -1 <= x <= 1' )
  print ( '  y(-1) = 2, y(1) = 1' )

  for epsilon in [ 1.0, 0.1, 0.02, 0.01 ]:

    a = -1.0
    b =  1.0

    n_mesh = 5
    x_mesh = np.linspace ( a, b, n_mesh )
    y_mesh = np.zeros ( [ 2, n_mesh ] )

    sol = solve_bvp ( ill_bvp_fun, ill_bvp_bc, x_mesh, y_mesh )
#
#  Evaluate the solution at plot points.
#
    n_plot = 101
    x_plot = np.linspace ( a, b, n_plot )
    y_plot = sol.sol ( x_plot )[0]
#
#  Plot.
#
    plt.clf ( )
    plt.plot ( x_plot, y_plot, 'r-', linewidth = 2 )
    plt.xlabel ( '<--- X --->' )
    plt.ylabel ( '<--- Y(X) --->' )
    plt.title ( 'Ill conditioned BVP, epsilon = ' + str ( epsilon ) )
    plt.grid ( True )
#
#  Make the aspect ratio ( Y/X ) = 1/3, so we get a long low plot.
#
    axes = plt.gca ( )
    axes.set_aspect ( 1.0 / 3.0 )
    filename = 'ill_bvp_' + str ( epsilon ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.show ( block = False )
    plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ill_bvp_test():' )
  print ( '  Normal end of execution.' )

  return

def ill_bvp_fun ( x, y ):

#*****************************************************************************80
#
## ill_bvp_fun() evaluates the right hand side of the ill-conditioned BVP.
#
#  Discussion:
#
#    We assume that the differential equation has been rewritten as a
#    system of first order equations of the form
#
#      dydx = f(x,y)
#
#    u' = v
#    v' = ( x * v - u ) / epsilon
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

  global epsilon

  dydx = np.array ( [ y[1], ( x * y[1] - y[0] ) / epsilon ] )

  return dydx

def ill_bvp_bc ( ya, yb ):

#*****************************************************************************80
#
## ill_bvp_bc() evaluates boundary conditions for the ill-conditioned BVP.
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

  bc = np.array ( [ ya[0] - 2.0, yb[0] - 1.0 ] ) 

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
  ill_bvp_test ( )
  timestamp ( )

