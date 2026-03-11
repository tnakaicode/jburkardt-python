#! /usr/bin/env python3
#
def spiral_pde_test ( ):

#*****************************************************************************80
#
## spiral_pde_test() tests spiral_pde().
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
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'spiral_pde_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  spiral_pde() solves a reaction-diffusion' )
  print ( '  partial differential equation with spiral solution.' )
#
#  Set N, the number of spatial nodes in each direction.
#
  n = 401
#
#  Set the X values.
#
  nx = n
  xmin = 0.0
  xmax = 80.0
  dx = ( xmax - xmin ) / ( nx - 1 )
  x = np.linspace ( xmin, xmax, n )
#
#  Set the Y values.
#
  ny = n
  ymin = 0.0
  ymax = 80.0
  dy = ( ymax - ymin ) / ( ny - 1 )
  y = np.linspace ( ymin, ymax, n )
#
#  Set the X, Y grid.
#
  X, Y = np.meshgrid ( x, y )
#
#  Set the T values.
#
  nt = 5001
  tmin = 0.0
  tmax = 5.0
  dt = ( tmax - tmin ) / ( nt - 1 )
  t = np.linspace ( tmin, tmax, nt )
#
#  Report discretization values.
#
  print ( '' )
  print ( '  discretization values:' )
  print ( '' )
  print ( '    nx = ', nx )
  print ( '    xmin = ', xmin )
  print ( '    xmax = ', xmax )
  print ( '    dx = ', dx )
  print ( '    ny = ', ny )
  print ( '    ymin = ', ymin )
  print ( '    ymax = ', ymax )
  print ( '    dy = ', dy )
  print ( '    nt = ', nx )
  print ( '    tmin = ', tmin )
  print ( '    tmax = ', tmax )
  print ( '    dt = ', dy )
#
#  Set problem parameters alpha, beta, delta, epsilon.
#
  alpha, beta, delta, epsilon = spiral_parameters ( )
#
#  Report parameter values.
#
  print ( '' )
  print ( '  parameters:' )
  print ( '' )
  print ( '    alpha = ', alpha )
  print ( '    beta = ', beta )
  print ( '    delta = ', delta )
  print ( '    epsilon = ', epsilon )

  for k in range ( 0, nt ):
#
#  Set initial condition for U and V.
#
    if ( k == 0 ):

      U, V = spiral_initial_condition ( X, Y )
#
#  Use the Forward Euler method to take a time step.
#
    else:

      dUdt, dVdt = spiral_deriv ( t, U, V, dx, dy )
      U = U + dt * dUdt
      V = V + dt * dVdt
#
#  Apply zero Neumann boundary conditions.
#
      U[:,0]  = U[:,1]
      U[:,-1] = U[:,-2]
      U[0,:]  = U[1,:]
      U[-1,:] = U[-2,:]

      V[:,0]  = V[:,1]
      V[:,-1] = V[:,-2]
      V[0,:]  = V[1,:]
      V[-1,:] = V[-2,:]
#
#  Plot once every 25 time steps.
#
    if ( ( k % 25 ) == 0 ):

      f, ax = plt.subplots ( 1, 2 )

      label = ( 'Spiral PDE, step = %d, time = %f' % ( k, t[k] ) )
      f.suptitle ( label )

      ax[0].contourf ( X, Y, U )
      ax[0].axis ( 'off' )
      ax[0].axis ( 'equal' )
      ax[0].set_title ( 'U(x,y)' )
      ax[0].set_xticks ( [] )
      ax[0].set_yticks ( [] )

      ax[1].contourf ( X, Y, V )
      ax[1].axis ( 'equal' )
      ax[1].axis ( 'off' )
      ax[1].set_title ( 'V(x,y)' )
      ax[1].set_xticks ( [] )
      ax[1].set_yticks ( [] )

      if ( ( k % 500 ) == 0 ):
        filename = ( 'spiral_%04d.png' % ( k ) )
        plt.savefig ( filename )
        print ( '  Graphics saved as "' + filename + '"' )

      plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'spiral_pde_test():' )
  print ( '  Normal end of execution.' )

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

def spiral_deriv ( t, U, V, dx, dy ):

#*****************************************************************************80
#
## spiral_deriv(): right hand side of spiral reaction-diffusion PDE.
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
#    real T: the current time.
#
#    real U(NX,NY), V(NX,NY): the current solution.
#
#    real DX, DY: the X and Y spacings.
#
#  Output:
#
#    real DUDT, DVDT(NX,NY), the right hand sides of the ODE at each node.
#

#
#  Get parameters:
#
  alpha, beta, delta, epsilon = spiral_parameters ( )
#
#  Compute the laplacians of U and V using a 9 point stencil.
#
  del2U = laplacian9_torus ( U, dx, dy )
  del2V = laplacian9_torus ( V, dx, dy )
#
#  Take an explicit Euler time step for U and V.
#
  dUdt = del2U + ( 1.0 / epsilon ) * U * ( 1.0 - U ) \
    * ( U - ( V + beta ) / alpha )
  dVdt = delta * del2V + U - V

  return dUdt, dVdt

def spiral_initial_condition ( X, Y ):

#*****************************************************************************80
#
## spiral_initial_condition(): initial values for spiral reaction-diffusion PDE.
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
#    real X(nr,nc), Y(nr,nc): the node coordinates.
#
#  Output:
#
#    real U(nr,nc), V(nr,nc): the node velocities.
#
  alpha, beta, delta, epsilon = spiral_parameters ( )

  U0 = ( 40.0 <= X )

  V0 = 0.5 * alpha * ( 40.0 <= Y )

  return U0, V0

def spiral_parameters ( ):

#*****************************************************************************80
#
## spiral_parameters() returns parameters for the spiral reaction-diffusion PDE.
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
#  Output:
#
#    real alpha, beta, delta, epsilon: PDE parameters.
#
  alpha =   0.25
  beta =    0.001
  delta =   0.00001
  epsilon = 0.002

  return alpha, beta, delta, epsilon

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
  spiral_pde_test ( )
  timestamp ( )

