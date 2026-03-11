#! /usr/bin/env python3
#
def poisson_2d_test ( ):

#*****************************************************************************80
#
## poisson_2d_test() tests poisson_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'poisson_2d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test poisson_2d().' )
#
#  Problem 1.
#
  nx = 11
  ny = 11
  poisson_2d ( nx, ny, rhs1, u_exact1, uxxyy_exact1 )
#
#  Terminate.
#
  print ( '' )
  print ( 'poisson_2d_test():' )
  print ( '  Normal end of execution.' )

  return

def poisson_2d ( nx, ny, rhs, u_exact, uxxyy_exact ):

#*****************************************************************************80
#
## poisson_2d() computes a solution to the Poisson equation on a rectangle.
#
#  Discussion:
#
#    This program runs serially.  Its output is used as a benchmark for
#    comparison with similar programs run in a parallel environment.
#
#    The Poisson equation
#
#      - DEL^2 U(x,y) = F(x,y)
#
#    is solved on the unit square [0,1] x [0,1] using a grid of NX by
#    NX evenly spaced points.  The first and last points in each direction
#    are boundary points.
#
#    The boundary conditions and F are set so that the exact solution is
#
#      U(x,y) = sin ( pi * x * y )
#
#    so that
#
#      - DEL^2 U(x,y) = pi^2 * ( x^2 + y^2 ) * sin ( pi * x * y )
#
#    The Jacobi iteration is repeatedly applied until convergence is detected.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NX, NY, the number of nodes in the X and Y directions.
#
#    f = rhs ( x, y ): evaluates the right hand side function.
#
#    u = u_exact ( x, y ): evaluates the exact solution.
#
#    uxxyy = uxxyy_exact ( x, y ): evaluates the exact uxxyy.
#
#  Local:
#
#    real DX, DY, the X and Y spacing.
#
#    integer IT_MAX: the maximum number of Jacobi iterations allowed.
#
#    real TOLERANCE: convergence is declared if successive iterates differ
#    by less than this value in norm.
#
  import numpy as np

  a = 0.0
  b = 1.0
  c = 0.0
  d = 1.0
  dx = ( b - a ) / ( nx - 1 )
  dy = ( d - c ) / ( ny - 1 )
  it_max = 1000
  tolerance = 0.000001

  print ( '' )
  print ( 'poisson_2d():' )
  print ( '  A program for solving the Poisson equation:' )
  print ( '    -DEL^2 U = F(X,Y)' )
  print ( '  on the rectangle 0 <= X <= 1, 0 <= Y <= 1.' )
  print ( '' )
  print ( '  F(X,Y) = pi^2 * ( x^2 + y^2 ) * sin ( pi * x * y )' )
  print ( '' )
  print ( '  The number of X grid points is ', nx )
  print ( '  The number of Y grid points is ', ny )
  print ( '  The X grid spacing is ', dx )
  print ( '  The Y grid spacing is ', dy )
#
#  Set the right hand side.
#
  f = rhs ( nx, ny )
  fnorm = np.linalg.norm ( f, 'fro' ) / nx / ny
  print ( '  RMS of F = ', fnorm )
#
#  Set the initial solution estimate.
#  We are "allowed" to pick up the boundary conditions exactly.
#
  unew = np.zeros ( [ nx, ny ] )

  unew[0,     0:ny] = f[0,     0:ny]
  unew[  nx-1,0:ny] = f[  nx-1,0:ny]
  unew[0:nx,  0]    = f[0:nx,  0]
  unew[0:nx,  ny-1] = f[0:nx,  ny-1]

  unew_norm = np.linalg.norm ( unew, 'fro' ) / nx / ny
#
#  Set up the exact solution.
#
  x = np.linspace ( a, b, nx )
  y = np.linspace ( c, d, ny )
  X, Y = np.meshgrid ( x, y )
  uexact = u_exact ( X, Y )
  unorm = np.linalg.norm ( uexact, 'fro' ) / nx / ny
  print ( '  RMS of exact solution U = ', unorm )
#
#  Do the iteration.
#
  print ( '' )
  print ( 'Step    |Unew|     |Unew-U|     |Unew-Exact|' )
  print ( '' )

  error = np.linalg.norm ( unew - uexact, 'fro' ) / nx / ny
  print ( '%4d  %12g                %12g' % ( 0, unew_norm, error ) )

  for it in range ( 1, it_max + 1 ):

    u = unew.copy()
#
#  Perform one Jacobi sweep.
#
    unew = jacobi ( nx, ny, dx, dy, f, u )
#
#  Check for convergence.
#
    u_norm = unew_norm
    unew_norm = np.linalg.norm ( unew, 'fro' ) / nx / ny
    diff = np.linalg.norm ( unew - u, 'fro' ) / nx / ny
    error = np.linalg.norm ( unew - uexact, 'fro' ) / nx / ny

    print ( '%3d  %12g  %12g  %12g' % ( it, unew_norm, diff, error ) )

    if ( diff <= tolerance ):
      print ( '  The iteration has converged.' )
      return

  print ( '  The iteration has NOT converged.' )

  return

def jacobi ( nx, ny, dx, dy, f, u ):

#*****************************************************************************80
#
## jacobi() carries out one step of the Jacobi iteration.
#
#  Discussion:
#
#    Assuming DX = DY, we can approximate
#
#      - ( d/dx d/dx + d/dy d/dy ) U(X,Y) 
#
#    by
#
#      ( U(i-1,j) + U(i+1,j) + U(i,j-1) + U(i,j+1) - 4*U(i,j) ) / dx / dy
#
#    The discretization employed below will not be correct in the general
#    case where DX and DY are not equal.  It's only a little more complicated
#    to allow DX and DY to be different, but we're not going to worry about 
#    that right now.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NX, NY, the X and Y grid dimensions.
#
#    real DX, DY, the spacing between grid points.
#
#    real F(NX,NY), the right hand side data.
#
#    real U(NX,NY), the previous solution estimate.
#
#  Output:
#
#    real UNEW(NX,NY), the updated solution estimate.
#

#
#  The boundary values are stored in F.  Copy them.
#
  unew = f.copy()
#
#  The interior values are set by a Jacobi iteration.
#
  unew[1:nx-1,1:ny-1] = 0.25 * ( \
      u[0:nx-2,1:ny-1] \
    + u[1:nx-1,2:ny] \
    + u[1:nx-1,0:ny-2] \
    + u[2:nx,  1:ny-1] \
    + f[1:nx-1,1:ny-1] * dx * dy )

  return unew

def rhs1 ( nx, ny ):

#*****************************************************************************80
#
## rhs1() initializes the right hand side "vector" for problem 1.
#
#  Discussion:
#
#    It is convenient for us to set up RHS as a 2D array.  However, each
#    entry of RHS is really the right hand side of a linear system of the
#    form
#
#      A * U = F
#
#    In cases where U(I,J) is a boundary value, then the equation is simply
#
#      U(I,J) = F(i,j)
#
#    and F(I,J) holds the boundary data.
#
#    Otherwise, the equation has the form
#
#      (1/DX^2) * ( U(I+1,J)+U(I-1,J)+U(I,J-1)+U(I,J+1)-4*U(I,J) ) = F(I,J)
#
#    where DX is the spacing and F(I,J) is the value at X(I), Y(J) of
#
#      pi^2 * ( x^2 + y^2 ) * sin ( pi * x * y )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    103 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NX, NY, the X and Y grid dimensions.
#
#  Output:
#
#    real F(NX,NY), the right hand side data.
#
  import numpy as np

  f = np.zeros ( [ nx, ny ] )

  for j in range ( 0, ny ):
    y = j / ( ny - 1 )
    for i in range ( 0, nx ):
      x = i / ( nx - 1 )
#
#  The "boundary" entries of F store the boundary values of the solution.
#
      if ( i == 0 or i == nx - 1 or j == 0 or j == ny - 1 ):
        f[i,j] = u_exact1 ( x, y )
#
#  The "interior" entries of F store the right hand sides of the Poisson equation.
#
      else:
        f[i,j] = - uxxyy_exact1 ( x, y )

  return f

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

def u_exact1 ( x, y ):

#*****************************************************************************80
#
## uexact1() evaluates the exact solution for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the coordinates of a point.
#
#  Output:
#
#    real U, the value of the exact solution at (X,Y).
#
  import numpy as np

  u = np.sin ( np.pi * x * y )

  return u

def uxxyy_exact1 ( x, y ):

#*****************************************************************************80
#
## uxxyy_exact1() evaluates exact ( d/dx d/dx + d/dy d/dy ) for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the coordinates of a point.
#
#  Output:
#
#    real UXXYY, the value of ( d/dx d/dx + d/dy d/dy ) of the
#    exact solution at (X,Y).
#
  import numpy as np

  uxxyy = - np.pi * np.pi * ( x * x + y * y ) * np.sin ( np.pi * x * y )

  return uxxyy

if ( __name__ == '__main__' ):
  timestamp ( )
  poisson_2d_test ( )
  timestamp ( )

 
