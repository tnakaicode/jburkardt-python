#! /usr/bin/env python3
#
def fd1d_heat_steady_test ( ):

#*****************************************************************************80
#
## fd1d_heat_steady_test() tests fd1d_heat_steady().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'fd1d_heat_steady_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test fd1d_heat_steady().' )
  print ( '' )
  print ( '  Finite difference solution of ' )
  print ( '  the steady 1D heat equation' )
  print ( '    - d/dx ( k(x) dUdx ) = F(x)' )
  print ( '  for space interval A <= X <= B with boundary conditions' )
  print ( '    U(A) = UA' )
  print ( '    U(B) = UB' )
  print ( '  A second order difference approximation is used.' )

  test1 ( )
  test2 ( )
  test3 ( )
  test4 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fd1d_heat_steady_test():' )
  print ( '  Normal end of execution.' )

  return

def fd1d_heat_steady ( n, a, b, ua, ub, k, f ):

#*****************************************************************************80
#
## fd1d_heat_steady() solves the steady 1D heat equation.
#
#  Discussion:
#
#    This program seeks a solution of the steady heat equation:
#
#      - d/dx ( K(X) dUdx ) = F(X)
#
#    over the interval [A,B] with boundary conditions
#
#      U(A) = UA,
#      U(B) = UB.
#
#    The code uses the finite difference method to approximate the
#    second derivative in space.  This results in a sparse linear system.
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
#    integer N, the number of grid points.
#
#    real A, B, the interval endpoints.
#
#    real UA, UB, the values prescribed for U at the endpoints.
#
#    function K(X), evaluates the thermal conductance at the N
#    points X.  Set K(X) = 1 if you don't care about this coefficient.
#
#    function F(X), evaluates the heat source term at the N
#    points X.  Set F(X) = 0 if you don't want any heat sources.
#
#  Output:
#
#    real X(N), the grid points.
#
#    real U(N), the approximation to the solution at the grid points.
#
  import numpy as np
#
#  Set the X values.
#
  dx = ( b - a ) / ( n - 1 )
  x = np.linspace ( a, b, n )
#
#  Set up the matrix.
#
  A = np.zeros ( [ n, n ] )
  rhs = np.zeros ( n )

  A[0,0] = 1.0
  rhs[0] = ua

  for i in range ( 1, n - 1 ):
    A[i,i-1] = - k(x[i]-0.5*dx)                    / dx / dx
    A[i,i] =   ( k(x[i]-0.5*dx) + k(x[i]+0.5*dx) ) / dx / dx
    A[i,i+1] =                  - k(x[i]+0.5*dx)   / dx / dx
    rhs[i] = f(x[i])

  A[n-1,n-1] = 1.0
  rhs[n-1] = ub
#
#  Solve the linear system.
#
  u = np.linalg.solve ( A, rhs )

  return x, u

def test1 ( ):

#*****************************************************************************80
#
## test1() is the main program for problem 1.
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'test1():' )
  print ( '  Test fd1d_heat_steady().' )
  print ( '  Simple linear solution.' )

  n = 11

  a = 0.0
  b = 1.0

  ua = 0.0
  ub = 1.0

  x, u = fd1d_heat_steady ( n, a, b, ua, ub, k1, f1 )

  plt.clf ( )
  plt.plot ( x, u, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'Problem 1: Uniform K(X)' )
  plt.xlabel ( 'A <= X <= B' )
  plt.ylabel ( 'Temperature' )
  filename = 'test1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def k1 ( x ):

#*****************************************************************************80
#
## k1() evaluates the heat transfer coefficient K(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of K(X).
#
  value = 1.0

  return value

def f1 ( x ):

#*****************************************************************************80
#
## f1() evaluates the right hand side function F(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of F(X).
#
  value = 0.0

  return value

def test2 ( ):

#*****************************************************************************80
#
## test2() is the main program for problem 2.
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'test2():' )
  print ( '  Test fd1d_heat_steady().' )
  print ( '  Low K, high K, moderate K.' )

  n = 11

  a = 0.0
  b = 1.0

  ua = 0.0
  ub = 1.0

  x, u = fd1d_heat_steady ( n, a, b, ua, ub, k2, f2 )

  plt.clf ( )
  plt.plot ( x, u, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'Problem 2: low K, high K, moderate K' )
  plt.xlabel ( 'X' )
  plt.ylabel ( 'Temperature' )
  filename = 'test2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def k2 ( x ):

#*****************************************************************************80
#
## k2() evaluates the heat transfer coefficient K(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of K(X).
#
  if ( x < 0.50 ):
    value = 0.25
  elif ( x < 0.75 ):
    value = 4.0
  else:
    value = 1.0

  return value

def f2 ( x ):

#*****************************************************************************80
#
## f2() evaluates the right hand side function F(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of F(X).
#
  value = 0.0

  return value

def test3 ( ):

#*****************************************************************************80
#
## test3() is the main program for problem 3.
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'test3():' )
  print ( '  Test fd1d_heat_steady().' )
  print ( '  An interior heat source.' )

  n = 21

  a = 0.0
  b = 1.0

  ua =   0.0
  ub = 100.0

  x, u = fd1d_heat_steady ( n, a, b, ua, ub, k3, f3 )

  plt.clf ( )
  plt.plot ( x, u, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'Problem 3: Interior source term' )
  plt.xlabel ( 'X' )
  plt.ylabel ( 'Temperature' )
  filename = 'test3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def k3 ( x ):

#*****************************************************************************80
#
## k3() evaluates the heat transfer coefficient K(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of K(X).
#
  value = 1.0

  return value

def f3 ( x ):

#*****************************************************************************80
#
## f3() evaluates the right hand side function F(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of F(X).
#
  if ( x < 0.15 ):
    value = 0.0
  elif ( x < 0.45 ):
    value = 200.0
  else:
    value = 0.0

  return value

def test4 ( ):

#*****************************************************************************80
#
## test4() is the main program for problem 4.
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'test4():' )
  print ( '  Test fd1d_heat_steady().' )
  print ( '  A heat source and a heat sink.' )

  n = 21

  a = 0.0
  b = 1.0

  ua = 0.0
  ub = 0.0

  x, u = fd1d_heat_steady ( n, a, b, ua, ub, k4, f4 )

  plt.clf ( )
  plt.plot ( x, u, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'Problem 4: a heat source and a heat sink' )
  plt.xlabel ( 'X' )
  plt.ylabel ( 'Temperature' )
  filename = 'test4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def k4 ( x ):

#*****************************************************************************80
#
## k4() evaluates the heat transfer coefficient K(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of K(X).
#
  value = 1.0

  return value

def f4 ( x ):

#*****************************************************************************80
#
## f4() evaluates the right hand side function F(X).
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
#    real X, the position.
#
#  Output:
#
#    real VALUE, the value of F(X).
#
  if ( x < 0.15 ):
    value = 0.0
  elif ( x < 0.35 ):
    value = 1.0
  elif ( x < 0.75 ):
    value = 0.0
  elif ( x < 0.85 ):
    value = -2.0
  else:
    value = 0.0

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
  fd1d_heat_steady_test ( )
  timestamp ( )

