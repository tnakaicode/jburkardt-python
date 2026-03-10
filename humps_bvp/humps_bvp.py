#! /usr/bin/env python3
#
def humps_bvp_test ( ):

#*****************************************************************************80
#
## humps_bvp_test() tests humps_bvp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'humps_bvp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve humps_ode().' )

  for n in [ 21, 41 ]:
    humps_bvp_solve ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'humps_bvp_test():' )
  print ( '  Normal end of execution.' )

  return

def humps_bvp_solve ( n ):

#*****************************************************************************80
#
## humps_bvp_solve() solves the humps BVP using n nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of nodes to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
#
#  Get the parameters.
#
  x0, y0, x1 = humps_parameters ( )
  y1 = humps_fun ( x1 )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 = ', x0 )
  print ( '    y0 = ', y0 )
  print ( '    t1 = ', x1 )
  print ( '    y1 = ', y1 )

#
#  Set the nodes.
#
  x = np.linspace ( x0, x1, n )
#
#  Evaluate the right hand side of y'' = f(x,y)
#
  rhs = humps_deriv2 ( x )
  rhs[0] = humps_fun ( x0 )
  rhs[n-1] = humps_fun ( x1 )
#
#  Evaluate the second difference matrix.
#
  A = dif2_matrix ( n )
  dx = ( x1 - x0 ) / ( n - 1 )
  A = - A / dx**2
  A[0,0] = 1.0
  A[0,1] = 0.0
  A[n-1,n-2] = 0.0
  A[n-1,n-1] = 1.0
#
#  Solve for y.
#
  y = np.linalg.solve ( A, rhs )

  x2 = np.linspace ( x0, x1, 101 )
  y2 = humps_fun ( x2 )

  plt.plot ( x,  y, 'ro-', linewidth = 3, label = 'Computed' )
  plt.plot ( x2, y2, 'b-', linewidth = 3, label = 'Exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- x -->' )
  plt.ylabel ( '<-- y(x) -->' )
  plt.legend ( )
  plt.title ( 'humps BVP, n = ' + str ( n ) )
  filename = 'humps_bvp_' + str ( n ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'humps_bvp_test():' )
  print ( '  Normal end of execution.' )

  return

def dif2_matrix ( n ):

#*****************************************************************************80
#
## dif2_matrix() returns the second difference matrix.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
#
#  Rectangular Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.18,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 45, 
#    LC: QA263.G68.
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Example A8,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 1.
#
#    Joan Westlake,
#    Test Matrix A15,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    if ( 0 < i and i - 1 < n ):
      A[i,i-1] = -1.0

    if ( i < n ):
      A[i,i] = 2.0

    if ( i + 1 < n ):
      A[i,i+1] = -1.0

  return A

def humps_deriv2 ( x ):

#*****************************************************************************80
#
## humps_deriv2() evaluates the second derivative of the humps function.
#
#  Discussion:
#
#    y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
#      + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
#      - 6.0
#
#    ypp = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 )**2 + 0.01 )**2 \
#          - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 )**2 + 0.04 )**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the arguments.
#
#  Output:
#
#    real ypp(): the value of the second derivative at x.
#
  u1 = - 2.0 * ( x - 0.3 )
  v1 = ( ( x - 0.3 )**2 + 0.01 )**2
  u2 = - 2.0 * ( x - 0.9 )
  v2 = ( ( x - 0.9 )**2 + 0.04 )**2

  u1p = - 2.0
  v1p = 2.0 * ( ( x - 0.3 )**2 + 0.01 ) * 2.0 * ( x - 0.3 ) 
  u2p = - 2.0
  v2p = 2.0 * ( ( x - 0.9 )**2 + 0.04 ) * 2.0 * ( x - 0.9 )

  ypp = ( u1p * v1 - u1 * v1p ) / v1**2 \
      + ( u2p * v2 - u2 * v2p ) / v2**2

  return ypp

def humps_fun ( x ):

#*****************************************************************************80
#
## humps_fun() evaluates the humps function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
    + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
    - 6.0

  return y

def humps_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## humps_parameters() returns parameters for humps_ode().
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( humps_parameters, "t0_default" ):
    humps_parameters.t0_default = 0.0

  if not hasattr ( humps_parameters, "y0_default" ):
    humps_parameters.y0_default = humps_fun ( humps_parameters.t0_default )

  if not hasattr ( humps_parameters, "tstop_default" ):
    humps_parameters.tstop_default = 2.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    humps_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    humps_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    humps_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = humps_parameters.t0_default
  y0 = humps_parameters.y0_default
  tstop = humps_parameters.tstop_default
  
  return t0, y0, tstop

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
  humps_bvp_test ( )
  timestamp ( )

