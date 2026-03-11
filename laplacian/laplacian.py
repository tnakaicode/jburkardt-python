#! /usr/bin/env python3
#
def laplacian_test ( ):

#*****************************************************************************80
#
## laplacian_test() tests laplacian().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'laplacian_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test laplacian().' )

  laplacian3_interval_test ( )
  laplacian3_interval_uneven_test ( )
  laplacian5_plane_test ( )
  laplacian5_torus_test ( )
  laplacian9_torus_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'laplacian_test():' )
  print ( '  Normal end of execution.' )

  return

def laplacian3_circle ( up, dx ):

#*****************************************************************************80
#
## laplacian3_circle() approximates the laplacian on a periodic 1D domain.
#
#  Discussion:
#
#    If the domain is represented by nx equally spaced points, it is
#    assumed that only the data for the first nxp=nx-1 points is supplied.
#    In other words, the last entry of up() is at the node just BEFORE
#    the node where the periodic condition takes effect.
#
#    This is the standard laplacian estimate on a uniform grid, 
#    except that, by periodicity, and suppressing the last node, we have
#    the east neighbor of node 1 is the last node, and
#    the west neighbor of the last node is node 1.
#
#    This function offers four equivalent ways of computing the Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2020
#
#  Input:
#
#    real up(nxp): the values of a function on an equally spaced grid
#    of points in a periodic domain.
#
#    real dx: the spacing between any two consecutive nodes.
#
#  Output:
#
#    real lp(nxp): the estimate for the laplacian.
#
  import numpy as np

  nxp = up.shape[0]
  lp = np.zeros ( nxp )

  I =   np.arange ( 0, nxp )
  Im1 = np.roll ( I, 1 )
  Ip1 = np.rool ( I, -1 )

  lp = ( up[Ip1] - 2.0 * up[I] + up[Im1] ) / dx**2

  return lp

def laplacian3_interval ( u, dx ):

#*****************************************************************************80
#
## laplacian3_interval() approximates the laplacian on a 1D interval.
#
#  Discussion:
#
#    The domain is represented by nx equally spaced points.
#
#    The laplacian is computed for the interior points, but a value
#    of 0 is returned for the first and last points.
#
#    It is up to the user to decide whether to reset l(1) and l(nx)
#    to nonzero values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Input:
#
#    real u(nx): the values of a function on an equally spaced grid of points.
#
#    real dx: the spacing between any two consecutive nodes.
#
#  Output:
#
#    real l(nx): the estimate for the laplacian.
#
  import numpy as np

  nx = u.shape[0]
  l = np.zeros ( nx )
  l[1:nx-1] = ( u[2:nx] - 2.0 * u[1:nx-1] + u[0:nx-2] ) / dx**2

  return l

def laplacian3_interval_test ( ):

#*****************************************************************************80
#
## laplacian3_interval_test() tests laplacian3_interval().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laplacian3_interval_test():' )
  print ( '  laplacian3_interval() approximates the Laplacian operator' )
  print ( '  applied to a function on an interval.' )
  print ( '' )

  for p in [ 1, 2, 4 ]:

    nx = 5 * p
    xmin = 0.0
    xmax = 2.0 * np.pi
    x = np.linspace ( xmin, xmax, nx )
    dx = ( xmax - xmin ) / ( nx - 1 )

    A = np.sin ( x )
#
#  A2 is the exact value of the Laplacian.
#
    A2 = - np.sin ( x )
#
#  L is our estimate.
#
    L = laplacian3_interval ( A, dx )
#
#  Ignore error at first and last nodes.
#
    e = r8vec_norm_rms ( L[1:nx-1] - A2[1:nx-1] )
    print ( '  DX = %g, RMS error = %g' % ( dx, e ) )

  return

def laplacian3_interval_uneven ( u, x ):

#*****************************************************************************80
#
## laplacian3_interval_uneven() approximates the laplacian on a 1D interval.
#
#  Discussion:
#
#    The domain is represented by nx unequally spaced points.
#
#    The laplacian is computed for the interior points, but a value
#    of 0 is returned for the first and last points.
#
#    It is up to the user to decide whether to reset l(1) and l(nx)
#    to nonzero values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 September 2024
#
#  Input:
#
#    real u(nx): the values of a function on a grid of points.
#
#    real x(nx): the coordinates of each point.
#
#  Output:
#
#    real l(nx): the estimate for the laplacian.
#
  import numpy as np

  nx = u.shape[0]

  l = np.zeros ( nx )

  for i in range ( 1, nx - 1 ):

    dxl = x[i]   - x[i-1]
    dxr = x[i+1] - x[i]

    alpha =  2.0 *   dxr         / dxl / ( dxl + dxr ) / dxr
    beta = - 2.0 * ( dxr + dxl ) / dxl / ( dxl + dxr ) / dxr
    gamma =  2.0 *         dxl   / dxl / ( dxl + dxr ) / dxr

    l[i] = alpha * u[i-1] + beta * u[i] + gamma * u[i+1]

  return l

def laplacian3_interval_uneven_test ( ):

#*****************************************************************************80
#
## laplacian3_interval_uneven_test() tests laplacian3_interval_uneven().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laplacian3_interval_uneven_test():' )
  print ( '  laplacian3_interval_uneven() approximates the Laplacian' )
  print ( '  operator applied to a function on an unevenly spaced grid.' )

  for test in [ 1, 2 ]:

    if ( test == 1 ):
      print ( '' )
      print ( '  Use EVEN spacing:' )
      print ( '' )
    else:
      print ( '' )
      print ( '  Use UNEVEN spacing:' )
      print ( '' )

    for p in [ 1, 2, 4, 8 ]:

      nx = 5 * p
      xmin = 0.0
      xmax = 2.0 * np.pi
      if ( test == 1 ):
        x = np.linspace ( xmin, xmax, nx )
      else:
        x = r8vec_cheby1space ( nx, xmin, xmax )

      dxmax = np.max ( x[1:nx] - x[0:nx-1] )

      A = np.sin ( x )
#
#  A2 is the exact value of the Laplacian.
#
      A2 = - np.sin ( x )
#
#  L is our estimate.
#
      L = laplacian3_interval_uneven ( A, x )
#
#  Ignore error at first and last nodes.
#
      e = r8vec_norm_rms ( L[1:nx-1] - A2[1:nx-1] )
      print ( '  DXMAX = %g, RMS error = %g' % ( dxmax, e ) )

  return

def laplacian5_plane ( u, dx, dy ):

#*****************************************************************************80
#
## laplacian5_plane() approximates the laplacian on a plane grid.
#
#  Discussion:
#
#    The domain is represented by a grid of nx * ny points.
#    There is constant spacing dx and dy in the x and y directions respectifely.
#
#    The laplacian is computed for the interior points, but a value
#    of 0 is returned for points on the boundary.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2024
#
#  Input:
#
#    real u(nx,ny): the function values at grid points.
#
#    real dx, dy: the spacing in the x and y directions.
#
#  Output:
#
#    real l(nx,ny): the estimate for the laplacian.
#
  import numpy as np

  nx, ny = u.shape

  uxx = np.zeros ( [ nx, ny ] )
  uyy = np.zeros ( [ nx, ny ] )

  uxx[1:nx-1,:] = ( u[2:nx,:] - 2.0 * u[1:nx-1,:] + u[0:nx-2,:] ) / dx**2
  uyy[:,1:ny-1] = ( u[:,2:ny] - 2.0 * u[:,1:ny-1] + u[:,0:ny-2] ) / dy**2

  l = uxx + uyy

  return l

def laplacian5_plane_test ( ):

#*****************************************************************************80
#
## laplacian5_plane_test() tests laplacian5_plane().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laplacian5_plane_test():' )
  print ( '  laplacian5_plane() approximates the Laplacian operator' )
  print ( '  applied to a function on a 2D plane.' )
  print ( '' )

  for p in [ 1, 2, 4 ]:

    nx = 5 * p
    xmin = 0.0
    xmax = 2.0 * np.pi
    x = np.linspace ( xmin, xmax, nx )
    dx = ( xmax - xmin ) / ( nx - 1 )

    ny = 5 * p
    ymin = - np.pi
    ymax = + np.pi
    y = np.linspace ( ymin, ymax, ny )
    dy = ( ymax - ymin ) / ( ny - 1 )

    X, Y = np.meshgrid ( x, y )

    A = np.sin ( X ) * np.sin ( Y )
#
#  A2 is the exact value of the Laplacian.
#
    A2 = - 2.0 * np.sin ( X ) * np.sin ( Y )
#
#  L is our estimate.
#
    L = laplacian5_plane ( A, dx, dy )

    e = r8mat_norm_rms ( L - A2 )
    print ( '  DX = %g, DY = %g, RMS error = %g' % ( dx,dy, e ) )

  return

def laplacian5_torus ( A, dx, dy ):

#*****************************************************************************80
#
## laplacian5_torus() uses a 5 point Laplacian stencil on a torus.
#
#  Discussion:
#
#    1) Assumes the region is a rectangular torus
#    2) Assumes the mesh is uniform in both X and Y directions.
#    3) Assumes the spacing is dx in both directions.
#
#    The computation is done using for loops.  It could be speeded up
#    by using vectorized MATLAB statements.
#
#    Because of the periodic boundary conditions, the first and last rows
#    and columns are identified, that is, equivalent.  Therefore, when
#    computing indices im1, ip1, jm1, jp1, we have to skip over the last
#    row or column.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(NXP,NYP): function values, sampled on a regular grid.
#
#    real DX, DY: the grid spacing in the X and Y directions.
#
#  Output:
#
#    real L(NXP,NYP): the values of the Laplacian, as estimated by the
#    5 point periodic stencil.
#
  import numpy as np

  nxp, nyp = A.shape
  L = np.zeros ( [ nxp, nyp ] )

  for j in range ( 0, nyp ):

    if ( j == nyp - 2 ):
      jp1 = 0
    elif ( j == nyp - 1 ):
      jp1 = 1
    else:
      jp1 = j + 1

    if ( j == 0 ):
      jm1 = nyp - 2
    else:
      jm1 = j - 1
 
    for i in range ( 0, nxp ):

      if ( i == nxp - 2 ):
        ip1 = 0
      elif ( i == nxp - 1 ):
        ip1 = 1
      else:
        ip1 = i + 1

      if ( i == 0 ):
        im1 = nxp - 2
      else:
        im1 = i - 1

      L[i,j] = ( A[ip1,j] - 2.0 * A[i,j] + A[im1,j] ) / dx**2 \
             + ( A[i,jp1] - 2.0 * A[i,j] + A[i,jm1] ) / dy**2

  return L

def laplacian5_torus_test ( ):

#*****************************************************************************80
#
## laplacian5_torus_test() tests laplacian5_torus().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laplacian5_torus_test():' )
  print ( '  laplacian5_torus() approximates the Laplacian operator' )
  print ( '  applied to a function on a 2D torus.' )
  print ( '' )

  for p in [ 1, 2, 4 ]:

    nx = 5 * p
    xmin = 0.0
    xmax = 2.0 * np.pi
    x = np.linspace ( xmin, xmax, nx )
    dx = ( xmax - xmin ) / ( nx - 1 )

    ny = 5 * p
    ymin = - np.pi
    ymax = + np.pi
    y = np.linspace ( ymin, ymax, ny )
    dy = ( ymax - ymin ) / ( ny - 1 )

    X, Y = np.meshgrid ( x, y )

    A = np.sin ( X ) * np.sin ( Y )
#
#  A2 is the exact value of the Laplacian.
#
    A2 = - 2.0 * np.sin ( X ) * np.sin ( Y )
#
#  L is our estimate.
#
    L = laplacian5_torus ( A, dx, dy )

    e = r8mat_norm_rms ( L - A2 )
    print ( '  DX = %g, DY = %g, RMS error = %g' % ( dx,dy, e ) )

  return

def laplacian9_torus ( A, dx, dy ):

#*****************************************************************************80
#
## laplacian9_torus() uses a 9 point Laplacian stencil on a 2D torus.
#
#  Discussion:
#
#    1) Assumes the region is a rectangular torus
#    2) Assumes the mesh is uniform in both X and Y directions.
#    3) Assumes the spacing is dx in both directions.
#
#    Because of the periodic boundary conditions, the first and last rows
#    and columns are identified, that is, equivalent.  Therefore, when
#    computing indices im1, ip1, jm1, jp1, we have to skip over the last
#    row or column.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(NXP,NYP): function values, sampled on a regular 2D grid.
#
#    real DX, DY: the grid spacing in the X and Y directions.
#
#  Output:
#
#    real L(NXP,NYP): the values of the Laplacian, as estimated by the
#    9 point periodic stencil.
#
  import numpy as np

  nxp, nyp = A.shape
  L = np.zeros ( [ nxp, nyp ] )

  for j in range ( 0, nyp ):

    if ( j == nyp - 2 ):
      jp1 = 0
    elif ( j == nyp - 1 ):
      jp1 = 1
    else:
      jp1 = j + 1

    if ( j == 0 ):
      jm1 = nyp - 2
    else:
      jm1 = j - 1
 
    for i in range ( 0, nxp ):

      if ( i == nxp - 2 ):
        ip1 = 0
      elif ( i == nxp - 1 ):
        ip1 = 1
      else:
        ip1 = i + 1

      if ( i == 0 ):
        im1 = nxp - 2
      else:
        im1 = i - 1

      L[i,j] = \
        ( 1.0 * A[im1,jm1] +  4.0 * A[im1,j] + 1.0 * A[im1,jp1] \
        + 4.0 * A[i,  jm1] - 20.0 * A[i,j]   + 4.0 * A[i,  jp1] \
        + 1.0 * A[ip1,jm1] +  4.0 * A[ip1,j] + 1.0 * A[ip1,jp1] ) \
        / 6.0 / dx**2

  return L

def laplacian9_torus_test ( ):

#*****************************************************************************80
#
## laplacian9_torus_test() tests laplacian9_torus().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laplacian9_torus_test():' )
  print ( '  laplacian9_torus() approximates the Laplacian operator' )
  print ( '  applied to a function on a 2D torus.' )
  print ( '' )

  for p in [ 1, 2, 4 ]:

    nx = 5 * p
    xmin = 0.0
    xmax = 2.0 * np.pi
    x = np.linspace ( xmin, xmax, nx )
    dx = ( xmax - xmin ) / ( nx - 1 )

    ny = 5 * p
    ymin = - np.pi
    ymax = + np.pi
    y = np.linspace ( ymin, ymax, ny )
    dy = ( ymax - ymin ) / ( ny - 1 )

    X, Y = np.meshgrid ( x, y )

    A = np.sin ( X ) * np.sin ( Y )
#
#  A2 is the exact value of the Laplacian.
#
    A2 = - 2.0 * np.sin ( X ) * np.sin ( Y )
#
#  L is our estimate.
#
    L = laplacian9_torus ( A, dx, dy )

    e = r8mat_norm_rms ( L - A2 )
    print ( '  DX = %g, DY = %g, RMS error = %g' % ( dx,dy, e ) )

  return

def r8mat_norm_rms ( A ):

#*****************************************************************************80
#
## r8mat_norm_rms() returns the Root-Mean-Square (RMS) norm of an R8MAT.
#
#  Discussion:
#
#    The RMS norm is defined as
#
#      value = sqrt ( ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 ) / N / M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the RMS norm of A.
#
  import numpy as np
 
  m, n = A.shape
  value = np.sqrt ( ( sum ( sum ( A ** 2 ) ) ) / m / n )

  return value

def r8vec_cheby1space ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby1space() creates a vector of Type 1 Chebyshev values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Type 1 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_norm_rms ( a ):

#*****************************************************************************80
#
## r8vec_norm_rms() returns the RMS norm of an R8VEC.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = sqrt ( 1/N * sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N), the vector whose norm is desired.
#
#  Output:
#
#    real VALUE, the RMS norm of A.
#
  import numpy as np

  value = np.sqrt ( (a**2).mean() )

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
  laplacian_test ( )
  timestamp ( )

