#! /usr/bin/env python3
#
def fd1d_poisson_test ( ):

#*****************************************************************************80
#
## fd1d_poisson_test() tests fd1d_poisson()
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
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'fd1d_poisson_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  fd1d_poisson() is a Poisson equation solver' )
  print ( '  for an interval.' )

  xmin = 0.0
  xmax = 5.0
  print ( '' )
  print ( '  The equations are:' )
  print ( '    -y" = -(2x+5)*exp(x).' )
  print ( '    y(', xmin, ') = ', g(xmin) )
  print ( '    y(', xmax, ') = ', g(xmax) )
  print ( '  over the interval [', xmin, ',', xmax, ']' )

  nx = 21
  print ( '' )
  print ( '  Using grid of n = ', nx, ' points.' )

  x = np.linspace ( xmin, xmax, nx )
  hx = ( xmax - xmin ) / ( nx - 1 )

  u = fd1d_poisson ( nx, x, hx, f, g )
#
#  Compute the RMS error.
#
  err = 0.0
  for i in range ( 0, nx ):
    err = err + ( u[i] - exact ( x[i] ) )**2
  err = np.sqrt ( err / nx )

  print ( '  The RMS error was ', err )
#
#  Plot the computed and exact solutions.
#
  nx2 = 101
  x2 = np.linspace ( xmin, xmax, nx2 )
  u2 = g ( x2 )

  plt.clf ( )
  plt.plot ( x, u, 'ro-', linewidth = 3 )
  plt.plot ( x2, u2, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- Y -->' )
  plt.title ( 'Computed (red) and exact (blue) solutions' )
  filename = 'fd1d_poisson_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fd1d_poisson_test():' )
  print ( '  Normal end of execution.' )

  return

def fd1d_poisson ( nx, x, hx, f, g ):

#*****************************************************************************80
#
## fd1d_poisson() solves a Poisson equation in an interval.
#
#  Discussion:
#
#    This program uses the finite difference method to estimate the solution
#    to a Poisson problem over an interval:
#
#      - Del U = f(x) in Omega
#            U = g(x) on dOmega
#
#    The user specifies 
#      the number of grid points (nx), 
#      the spatial extent (xmin,xmax), 
#      the functions f(x), g(x).
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
#    integer NX, the number of grid points.
#
#    real X(NX), the spatial coordinates.
#
#    real HX: the spacing.
#
#    function handle F, the name of the function which evaluates
#    the right hand side of the Poisson equation.
#
#    function handle G, the name of the function which evaluates
#    the Dirichlet boundary conditions.
#
#  Output:
#
#    real U(NX), a table of solution values.
#
  import numpy as np
#
#  Set the system matrix A and right hand side rhs.
#
  A = np.zeros ( [ nx, nx ] )
  rhs = np.zeros ( nx )

  eqn = 0
  for i in range ( 0, nx ):

    if ( i + 1 == 1 or i + 1 == nx ):
      A[eqn,eqn] = 1.0
      rhs[eqn] = g ( x[i] )
    else:
      A[eqn,eqn] = 2.0 / hx / hx
      A[eqn,eqn-1]  = - 1.0 / hx / hx
      A[eqn,eqn+1]  = - 1.0 / hx / hx
      rhs[eqn] = f ( x[i] )
    eqn = eqn + 1
#
#  Solve for u, the solution vector.
#
  u = np.linalg.solve ( A, rhs )

  return u

def f ( x ):

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
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value of F(X).
#
  import numpy as np

  value = - ( 2.0 * x + 5.0 ) * np.exp ( x )

  return value

def g ( x ):

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
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value of G(X).
#
  value = exact ( x )

  return value

def exact ( x ):

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
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the exact solution at x.
#
  import numpy as np

  value = ( 2.0 * x + 1.0 ) * np.exp ( x )

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
  fd1d_poisson_test ( )
  timestamp ( )

