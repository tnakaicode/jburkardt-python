#! /usr/bin/env python3
#
def bvp_fd ( n ):

#*****************************************************************************80
#
## bvp_fd() uses the finite difference method for a boundary value problem.
#
#  Discussion:
#
#    Demonstrate how the solution of a lineary boundary value problem (BVP)
#    can be approximated using the finite difference method.
#
#    Choose n nodes in the interval [a,b].
#
#    Define n x n linear system.
#
#    First and last equations enforce boundary conditions.
#    Equations 2 through n-1 are discretized versions of the differential
#    equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of nodes to use in the interval.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  The BVP is specified over [a,b]:
#
  a = 0.0
  b = 0.5
#
#  The side conditions are y(a) = ya, y(b) = yb.
#
  ya = 1.0
  yb = 2.0 * np.exp ( 0.5 )
#
#  Set the nodes.
#
  x = np.linspace ( a, b, n )
  dx = ( b - a ) / float ( n - 1 )
#
#  Allocate the matrix and right hand side.
#
  A = np.zeros ( [ n, n ] )
  rhs = np.zeros ( n )
#
#  First equation.
#
  A[0,0] = 1.0
  rhs[0] = ya
#
#  Internal equations:
#  y" - y = 4 exp(x)
#
  for i in range ( 1, n - 1 ):
    A[i,i-1] =  1.0 / dx**2 
    A[i,i  ] = -2.0 / dx**2 - 1.0
    A[i,i+1] =  1.0 / dx**2
    rhs[i] = 4.0 * np.exp ( x[i] )
#
#  Last equation.
#
  A[n-1,n-1] = 1.0
  rhs[n-1] = yb
#
#  Solve for y.
#
  y = np.linalg.solve ( A, rhs )

  y_exact = ( 2.0 * x + 1.0 ) * np.exp ( x )
#
#  Now plot the solution.
#
  plt.clf ( )
  plt.plot ( x, y_exact, 'b-', linewidth = 2 )
  plt.plot ( x, y, 'ro', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y(X) --->' )
  plt.title ( 'Solution of y"=y+4e^x, y(0)=1, y(1/2)=2 sqrt(x).' )
  plt.legend ( [ 'exact', 'FD solution' ] )
  filename = 'bvp_fd_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def bvp_fd_test ( ):

#*****************************************************************************80
#
## bvp_fd_test() tests bvp_fd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bvp_fd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  bvp_fd() is a simple example of the finite difference method,' )
  print ( '  in which a boundary value problem (BVP) is solved' )
  print ( '  by choosing a grid of n points, setting up a linear system' )
  print ( '  which enforces boundary conditions, and uses discretized' )
  print ( '  versions of derivatives at each point.' )
#
#  Request a solution with a given number of nodes.
#
  n = 11
  bvp_fd ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'bvp_fd_test():' )
  print ( '  Normal end of execution.' )

  return

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
  bvp_fd_test ( )
  timestamp ( )

