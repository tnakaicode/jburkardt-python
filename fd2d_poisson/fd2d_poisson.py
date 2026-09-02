#! /usr/bin/env python3
#
def fd2d_poisson_test ( ):

#*****************************************************************************80
#
## fd2d_poisson_test() tests fd2d_poisson()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2026
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'fd2d_poisson_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  fd2d_poisson() is a simple Poisson equation solver' )
  print ( '  for a rectangular region.' )

  nx = 21
  ny = 41

  xmin = 0.0
  xmax = 1.0
  ymin = 1.0
  ymax = 3.0
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

  U, X, Y = fd2d_poisson ( nx, ny, x, y, hx, hy, f, g )
#
#  Compute the RMS error.
#
  err = 0.0
  for i in range ( 0, ny ):
    for j in range ( 0, nx ):
      err = err + ( U[i,j] - exact ( x[j], y[i] ) )**2

  err = np.sqrt ( err / nx / ny )

  print ( '' )
  print ( '  Using a ', nx, ' by ', ny, ' grid' )
  print ( '  The RMS error was ', err )
#
#  Plot the computed and exact solutions.
#
  plt.clf ( )
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( X, Y, U, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Computed solution surface', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  filename = 'poisson_computed_surface.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  U2 = exact ( X, Y )
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( X, Y, U2, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Exact solution surface', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  filename = 'poisson_exact_surface.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  levels = 15
  plt.contourf ( X, Y, U, levels, cmap = cm.coolwarm )
  plt.title ( 'Computed solution contours' )
  filename = 'poisson_computed_contours.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fd2d_poisson_test():' )
  print ( '  Normal end of execution.' )

  return

def fd2d_poisson ( nx, ny, x, y, hx, hy, f, g ):

#*****************************************************************************80
#
## fd2d_poisson() solves a Poisson equation in a rectangle.
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
#    08 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NX, NY, the number of grid points in the X and Y directions.
#
#    real X[NX], Y[NY], the coordinates.
#
#    real HX, HY: the mesh spacings.
#
#    function F, the name of the function which evaluates
#    the right hand side of the Poisson equation.
#
#    function G, the name of the function which evaluates
#    the Dirichlet boundary conditions.
#
#  Output:
#
#    real U(NY,NX), solution values.
#
#    real X(NY,NX), Y(NY,NX), the X and Y coordinates of the points.
#
  import numpy as np
#
#  Set the system matrix A and right hand side rhs.
#
  A = np.zeros ( [ nx * ny, nx * ny ] )
  rhs = np.zeros ( nx * ny )

  eqn = 0
  for j in range ( 0, ny ):
    for i in range ( 0, nx ):

      if ( i + 1 == 1 or i + 1 == nx or j + 1 == 1 or j + 1 == ny ):
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
  u = np.linalg.solve ( A, rhs )
#
#  Return matrices U, X, Y.
#
  U = np.reshape ( u, [ ny, nx ] )
  Y, X = np.meshgrid ( y, x, indexing = 'ij' )

  return U, X, Y

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
#    08 May 2026
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

  value = np.pi * np.pi * ( x * x + y * y ) * np.sin ( np.pi * x * y )

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
#    08 May 2026
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
#    08 May 2026
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

  value = np.sin ( np.pi * x * y )

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
  fd2d_poisson_test ( )
  timestamp ( )

