#! /usr/bin/env python3
#
def fd2d_convergence_test ( ):

#*****************************************************************************80
#
## fd2d_convergence_test() does a convergence study
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Hall, Thomas Porsching,
#    Numerical Analysis of Partial Differential Equations, page 258,
#    Prentice-Hall, 1990,
#    ISBN: 013626557X,
#    LC: QA374.H29.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'fd2d_convergence_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  fd2d_poisson() solves a Poisson problem on a' )
  print ( '  sequence of meshes of mesh size h.  Compute RMS error E.' )
  print ( '  Plot log(h) versus log(E).' )

  xmin = 0.0
  xmax = 1.0
  ymin = 0.0
  ymax = 1.0

  print ( '' )
  print ( '  i           h(i)     e(i)                rate(i)' )
  print ( '' )

  n = 6

  r = np.zeros ( n )
  h = np.zeros ( n )
  e = np.zeros ( n )

  for k in range ( 0, n ):

    nx = 2**(k+2) + 1
    ny = nx
    U, X, Y = fd2d_poisson ( nx, ny, xmin, xmax, ymin, ymax, f, g )

    err = 0.0
    for j in range ( 0, ny ):
      for i in range ( 0, nx ):
        err = err + ( U[i,j] - exact ( X[i,j], Y[i,j] ) )**2
    err = np.sqrt ( err / nx / ny )

    h[k] = 1.0 / ( nx - 1 )
    e[k] = err

    if ( k == 0 ):
      r[k] = np.NaN
      print ( '%2d  %14.6g  %14.6g  %14.6g' % ( k, h[k], e[k], r[k] ) )
    else:
      r[k] = np.log ( e[k-1] / e[k] ) \
           / np.log ( h[k-1] / h[k] )
      print ( '%2d  %14.6g  %14.6g  %14.6g' % ( k, h[k], e[k], r[k] ) )
#
#  Plot the computed and exact solutions.
#
  x = np.log ( h )
  y = np.log ( e )

  plt.clf ( )
  plt.plot ( x, y, 'r-o', linewidth = 3 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<-- log(h) -->' )
  plt.ylabel ( '<-- log(RMS error) -->' )
  plt.title ( 'Convergence rate' )
  filename = 'fd2d_convergence_test.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fd2d_convergence_test():' )
  print ( '  Normal end of execution.' )

  return

def f ( x, y ):

#*****************************************************************************80
#
## f() evaluates the right hand side of the Poisson equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the arguments.
#
#  Output:
#
#    real VALUE, the value of F(X,Y).
#
  import numpy as np

  value = - 2.0 - ( x**2 + y**2 ) * np.exp ( x * y )

  return value

def g ( x, y ):

#*****************************************************************************80
#
## g() evaluates the boundary conditions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the arguments.
#
#  Output:
#
#    real VALUE, the value of G(X,Y).
#
  value = exact ( x, y )

  return value

def exact ( x, y ):

#*****************************************************************************80
#
## exact() evaluates the exact solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the arguments.
#
#  Output:
#
#    real VALUE, the value of the exact solution at (X,Y).
#
  import numpy as np

  value = ( x - 2.0 )**2 + np.exp ( x * y )

  return value

def fd2d_poisson ( nx, ny, xmin, xmax, ymin, ymax, f, g ):

#*****************************************************************************80
#
## fd2d_poisson() is a simple program to solve a Poisson equation in a rectangle.
#
#  Discussion:
#
#    This program uses the finite difference method to estimate the solution
#    to a Poisson problem on a rectangle:
#
#      - Del U = f(x,y) in Omega
#            U = g(x,y) on dOmega
#
#    The user specifies the number of grid points (nx,ny), the spatial
#    extent (xmin,xmax,ymin,ymax), and the functions f(x,y), g(x,y).
#
#    No attempt is made to efficiently construct the matrix, or to store
#    it sparsely.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NX, NY, the number of grid points in the X and Y directions.
#
#    real XMIN, XMAX, YMIN, YMAX, the X and Y endpoints.
#
#    function handle F, the name of the MATLAB function which evaluates
#    the right hand side of the Poisson equation.
#
#    function handle G, the name of the MATLAB function which evaluates
#    the Dirichlet boundary conditions.
#
#  Output:
#
#    real U(NY,NX), a table of solution values.
#
#    real X(NY,NX), Y(NY,NX), tables of the X and Y coordinates of the points.
#
  import numpy as np
#
#  Compute the X and Y spacings.
#
  hx = ( xmax - xmin ) / ( nx - 1 )
  hy = ( ymax - ymin ) / ( ny - 1 )
#
#  Compute the X and Y coordinate vectors.
#
  x = np.linspace ( xmin, xmax, nx )
  y = np.linspace ( ymin, ymax, ny )
#
#  Set the system matrix A and right hand side rhs.
#
  A = np.zeros ( [ nx * ny, nx * ny ] )
  rhs = np.zeros ( nx * ny )

  eqn = 0
  for j in range ( 0, ny ):
    for i in range ( 0, nx ):

      if ( i == 0 or i == nx- 1 or j == 0 or j == ny - 1 ):
        A[eqn,eqn] = 1.0
        rhs[eqn] = g ( x[i], y[j] )
      else:
        A[eqn,eqn-nx] = - 1.0 / hy**2
        A[eqn,eqn-1]  = - 1.0 / hx**2
        A[eqn,eqn]    =   2.0 / hx**2 + 2.0 / hy**2
        A[eqn,eqn+1]  = - 1.0 / hx**2
        A[eqn,eqn+nx] = - 1.0 / hy**2
        rhs[eqn]      = f ( x[i], y[j] )

      eqn = eqn + 1
#
#  Solve for u, the solution vector.
#
  U = np.linalg.solve ( A, rhs )
#
#  Return matrices U, X, Y.
#
  U.shape = ( nx, ny )
  X, Y = np.meshgrid ( x, y )

  return U, X, Y

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
  fd2d_convergence_test ( )
  timestamp ( )

