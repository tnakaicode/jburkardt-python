#! /usr/bin/env python3
#
def gray_scott_pde_test ( ):

#*****************************************************************************80
#
## gray_scott_pde_test() solves the 2D Gray-Scott reaction-diffusion equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'gray_scott_pde_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Solve the 2D Gray-Scott reaction-diffusion PDE' )

  nx = 251
  ny = 251
  nt = 150001

  d1, d2, gamma, kappa, t0, tstop, xmin, xmax, ymin, ymax = gray_scott_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    U diffusion d1  =', d1 )
  print ( '    V diffusion d2  =', d2 )
  print ( '    Flow rate gamma =', gamma )
  print ( '    Kill rate kappa =', kappa )
  print ( '    t0              =', t0 )
  print ( '    tstop           =', tstop )
  print ( '    xmin            =', xmin )
  print ( '    xmax            =', xmax )
  print ( '    ymin            =', ymin )
  print ( '    ymax            =', ymax )

  gray_scott_pde ( nx, ny, nt )
#
#  Terminate.
#
  print ( '' )
  print ( 'gray_scott_pde_test()' )
  print ( '  Normal end of execution.' )

  return

def gray_scott_parameters ( d1_user = None, d2_user = None, \
  gamma_user = None, kappa_user = None, t0_user = None, tstop_user = None, \
  xmin_user = None, xmax_user = None, ymin_user = None, ymax_user = None ):

#*****************************************************************************80
#
## gray_scott_parameters() returns the parameters of the Gray Scott ODE.
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
#    17 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real D1_USER: the U diffusion coefficient.
#
#    real D2_USER: the V diffusion coefficient.
#
#    real GAMMA_USER: the flow rate.
#
#    real KAPPA_USER: the kill rate.
#
#    real T0_USER: the initial time.
#
#    real TSTOP_USER: the final time.
#
#    real XMIN_USER: the minimum X value.
#
#    real XMAX_USER: the maximum X value.
#
#    real YMIN_USER: the minimum Y value.
#
#    real YMAX_USER: the maximum Y value.
#
#  Output:
#
#    real D1: the U diffusion coefficient.
#
#    real D2: the V diffusion coefficient.
#
#    real GAMMA: the flow rate.
#
#    real KAPPA: the kill rate.
#
#    real T0: the initial time.
#
#    real TSTOP: the final time.
#
#    real XMIN: the minimum X value.
#
#    real XMAX: the maximum X value.
#
#    real YMIN: the minimum Y value.
#
#    real YMAX: the maximum Y value.
#

#
#  Initialize defaults.
#
  if not hasattr ( gray_scott_parameters, "d1_default" ):
    gray_scott_parameters.d1_default = 8.0E-05

  if not hasattr ( gray_scott_parameters, "d2_default" ):
    gray_scott_parameters.d2_default = 4.0E-05

  if not hasattr ( gray_scott_parameters, "gamma_default" ):
    gray_scott_parameters.gamma_default = 0.024

  if not hasattr ( gray_scott_parameters, "kappa_default" ):
    gray_scott_parameters.kappa_default = 0.06

  if not hasattr ( gray_scott_parameters, "t0_default" ):
    gray_scott_parameters.t0_default = 0.0

  if not hasattr ( gray_scott_parameters, "tstop_default" ):
    gray_scott_parameters.tstop_default = 1500.0

  if not hasattr ( gray_scott_parameters, "xmin_default" ):
    gray_scott_parameters.xmin_default = 0.0

  if not hasattr ( gray_scott_parameters, "xmax_default" ):
    gray_scott_parameters.xmax_default = 2.5

  if not hasattr ( gray_scott_parameters, "ymin_default" ):
    gray_scott_parameters.ymin_default = 0.0

  if not hasattr ( gray_scott_parameters, "ymax_default" ):
    gray_scott_parameters.ymax_default = 2.5
#
#  Update defaults if input was supplied.
#
  if ( d1_user is not None ):
    gray_scott_parameters.d1_default = d1_user

  if ( d2_user is not None ):
    gray_scott_parameters.d2_default = d2_user

  if ( gamma_user is not None ):
    gray_scott_parameters.gamma_default = gamma_user

  if ( kappa_user is not None ):
    gray_scott_parameters.kappa_default = kappa_user

  if ( t0_user is not None ):
    gray_scott_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    gray_scott_parameters.tstop_default = tstop_user

  if ( xmin_user is not None ):
    gray_scott_parameters.xmin_default = xmin_user

  if ( xmax_user is not None ):
    gray_scott_parameters.xmax_default = xmax_user

  if ( ymin_user is not None ):
    gray_scott_parameters.ymin_default = ymin_user

  if ( ymax_user is not None ):
    gray_scott_parameters.ymax_default = ymax_user
#
#  Return values.
#
  d1 = gray_scott_parameters.d1_default
  d2 = gray_scott_parameters.d2_default
  gamma = gray_scott_parameters.gamma_default
  kappa = gray_scott_parameters.kappa_default
  t0 = gray_scott_parameters.t0_default
  tstop = gray_scott_parameters.tstop_default
  xmin = gray_scott_parameters.xmin_default
  xmax = gray_scott_parameters.xmax_default
  ymin = gray_scott_parameters.ymin_default
  ymax = gray_scott_parameters.ymax_default
  
  return d1, d2, gamma, kappa, t0, tstop, xmin, xmax, ymin, ymax

def gray_scott_pde ( nx, ny, nt ):

#*****************************************************************************80
#
## gray_scott_pde() solves the Gray-Scott PDE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    integer NX, NY, the number of nodes in the X and Y directions.
#
#    integer NT, the number of time steps.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gray_scott_pde():' )
  print ( '  Solve the Gray-Scott diffusion-reaction PDE' )

  d1, d2, gamma, kappa, t0, tstop, xmin, xmax, ymin, ymax = gray_scott_parameters ( )

  x = np.linspace ( xmin, xmax, nx )
  dx = ( xmax - xmin ) / ( nx - 1 )

  print ( '' )
  print ( '  Number of X nodes = ', nx )
  print ( '  dx = ', dx )

  y = np.linspace ( ymin, ymax, ny )
  dy = ( ymax - ymin ) / ( ny - 1 )

  print ( '' )
  print ( '  Number of Y nodes = ', ny )
  print ( '  dy = ', dy )

  X, Y = np.meshgrid ( x, y )

  t = np.linspace ( t0, tstop, nt )
  dt = ( tstop - t0 ) / ( nt - 1 )

  print ( '' )
  print ( '  Number of T values = ', nt )
  print ( '  dt = ', dt )
#
#  Begin the time loop.
#
  for it in range ( 0, nt ):
#
#  On first step, use the initial condition.
#
    if ( it == 0 ):

      V = 0.25 * ( np.sin ( 4.0 * np.pi * X ) )**2 \
               * ( np.sin ( 4.0 * np.pi * Y ) )**2

      V = V * ( 1.0 <= X ) * ( X <= 1.5 ) * ( 1.0 <= Y ) * ( Y <= 1.5 )

      U = np.ones ( [ nx, ny ] ) - 2.0 * V
#
#  On subsequent steps, use the Euler method to update the data.
#
    else:

      delU = laplacian9_torus ( U, dx, dy )
      delV = laplacian9_torus ( V, dx, dy )

      dUdt = d1 * delU - U * V**2 + gamma * ( 1.0 - U )
      dVdt = d2 * delV + U * V**2 - ( gamma + kappa ) * V

      U = U + dt * dUdt
      V = V + dt * dVdt
#
#  Display the data at certain steps.
#
    if ( ( it % 100 ) == 0 ):
      plt.clf ( )
      plt.imshow ( U )
      label = 'Gray-Scott PDE, U, time = ' + str ( t[it] )
      plt.title ( label )
      plt.axis ( 'equal' )
      plt.axis ( 'off' )
#
#  Save images at times matching the textbook results.
#
    if ( it == 0 ):
      filename = 'gray_scott_u0000.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( it == 10000 ):
      filename = 'gray_scott_u0100.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( it == 20000 ):
      filename = 'gray_scott_u0200.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( it == 50000 ):
      filename = 'gray_scott_u0500.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( it == 100000 ):
      filename = 'gray_scott_u1000.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( it == 150000 ):
      filename = 'gray_scott_u1500.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )

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
#    17 February 2025
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
  gray_scott_pde_test ( )
  timestamp ( )

