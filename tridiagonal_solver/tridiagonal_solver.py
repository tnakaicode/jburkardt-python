#! /usr/bin/env python3
#
def tridiagonal_mv ( a, b, c, x ):

#*****************************************************************************80
#
## tridiagonal_mv() multiplies a tridiagonal matrix times a vector.
#
#  Discussion:
#
#    There are M rows in the matrix, but at most three nonzero entries.
#    The subdiagonal is stored in A, the diagonal in B, the superdiagonal in C.
#
#    | b(1)    c(1)    ....  ....    ....    ....   |
#    | a(2)    b(2)    c(2)  ....    ....    ....   |
#    | ....    a(3)    b(3)  c(3)    ....    ....   |
#    | ....    ....    ....  ......  ....    ....   |
#    | ....    ....    ....  a(n-1)  b(n-1)  c(n-1) |
#    | ....    ....    ....  ......  a(n)    b(n)   |
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
#
#  Input:
#
#    real A(N), B(N), C(N), the matrix entries.
#    A(1) and C(N) are not used.
#
#    real X(N,:), the vector to be multiplied.
#
#  Output:
#
#    real RHS(N,:), the product.
#
  import numpy as np

  if ( x.ndim == 1 ):
    x = np.atleast_2d ( x )
    x = x.T

  m, n = x.shape

  rhs = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    rhs[0:m,j]   =                b[0:m]   * x[0:m,j]
    rhs[1:m,j]   = rhs[1:m,j]   + a[1:m]   * x[0:m-1,j]
    rhs[0:m-1,j] = rhs[0:m-1,j] + c[0:m-1] * x[1:m,j] 

  return rhs

def tridiagonal_solver ( a, b, c, d ):

#*****************************************************************************80
#
## tridiagonal_solver() solves a tridiagonal linear system.
#
#  Discussion:
#
#    There are N equations in a tridiagonal system.
#
#    Equation 1 is:
#                      b(1) * x(1) + c(1) * x(2)   = d(1)
#    Equation i, for 1 < i < n, is:
#      a(i) * x(i-1) + b(i) * x(i) + c(i) * x(i+1) = d(i)
#    Equation N is:
#      a(n) * x(n-1) + b(n) * x(n)                 = d(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
#
#  Input:
#
#    real A(N), B(N), C(N), the matrix entries.
#    A(1) and C(N) are not used.
#
#    real D(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution.
#
  import numpy as np

# if ( d.ndim == 1 ):
#   d = np.atleast_2d ( d )
#   d = d.T

# m, n = d.shape
  m = len ( d )

  for i in range ( 1, m ):
    s = a[i] / b[i-1]
    b[i] = b[i] - s * c[i-1]
    d[i] = d[i] - s * d[i-1]

  x = d.copy()

  for i in range ( m - 1, -1, -1 ):

    if ( b[i] == 0.0 ):
      print ( '' )
      print ( 'tridiagonal_solver(): Fatal error!' )
      print ( '  b(', i, ') = 0' )
      raise Exception ( 'tridiagonal_solver(): Fatal error!' )

    if ( i == m - 1 ):
      x[i] = x[i] / b[i]
    else:
      x[i] = ( x[i] - c[i] * x[i+1] ) / b[i]

  return x

def tridiagonal_solver_test ( ):

#*****************************************************************************80
#
## tridiagonal_solver_test() tests tridiagonal_solver().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'tridiagonal_solver_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  tridiagonal_solver() solves a tridiagonal linear system.' )

  rng = default_rng ( )

  tridiagonal_solver_test1 ( rng )
  tridiagonal_solver_test2 ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'tridiagonal_solver_test():' )
  print ( '  Normal end of execution.' )

  return

def tridiagonal_solver_test1 ( rng ):

#*****************************************************************************80
#
## tridiagonal_solver_test1() tests tridiagonal_solver on a single system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'tridiagonal_solver_test1():' )
  print ( '  tridiagonal_solver() solves A*x = b where' )
  print ( '  A is a tridiagonal matrix.' )

  m = 5
  g = np.linspace ( 1, m - 1, m - 1 )
  print ( '' )
  print ( '  Matrix order M =', m )
#
#  Set the matrix.
#
  a, b, c = spline_matrix ( g )
#
#  Set the desired solution.
#
  x1 = rng.permutation ( m )
#
#  Compute the corresponding right hand side.
#
  rhs = tridiagonal_mv ( a, b, c, x1 )
#
#  Solve the system.
#
  x2 = tridiagonal_solver ( a, b, c, rhs )
  x2 = x2[:,0]

  print ( '' )
  print ( '  Exact and computed solutions:' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  %d  %g  %g' % ( i, x1[i], x2[i] ) )

  return

def spline_matrix ( g ):

#*****************************************************************************80
#
## spline_matrix sets the entries of a tridiagonal spline matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = len ( g ) + 1

  a = np.zeros ( n )
  b = np.zeros ( n )
  c = np.zeros ( n )

  a[1:n] = g[0:n-1]

  b[0] = 2.0 * g[0]
  b[1:n-1] = 2.0 * ( g[0:n-2] + g[1:n-1] )
  b[n-1] = 2.0 * g[n-2]

  c[0:n-1] = g[0:n-1]

  return a, b, c

def tridiagonal_solver_test2 ( rng ):

#*****************************************************************************80
#
## tridiagonal_solver_test2 tests tridiagonal_solver on 2 systems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'tridiagonal_solver_test2()' )
  print ( '  tridiagonal_solver() solves A*x = b where' )
  print ( '  A is a tridiagonal matrix.' )
  print ( '  Solve two linear systems at once.' )

  m = 5
  n = 2
  print ( '' )
  print ( '  Matrix order M = ', m )
  print ( '  Number of right hand sides N = ', n )
#
#  Set the matrix.
#
  a = - np.ones ( m )
  a[0] = 0.0
  b = 2.0 * np.ones ( m )
  c = - np.ones ( m )
  c[m-1] = 0.0
#
#  Set the desired solution.
#
  y = np.linspace ( 1, m, m )

  x1 = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    p = rng.permutation ( m )
    x1[:,j] = y[p]
#
#  Compute the corresponding right hand side.
#
  rhs = tridiagonal_mv ( a, b, c, x1 )
#
#  Solve the system.
#
  x2 = tridiagonal_solver ( a, b, c, rhs )

  for j in range ( 0, n ):
    print ( '' )
    print ( '  Solution of linear system ', j )
    print ( '' )
    for i in range ( 0, m ):
      print ( '  %d  %g  %g' % ( i, x1[i,j], x2[i,j] ) )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  tridiagonal_solver_test ( )
  timestamp ( )

