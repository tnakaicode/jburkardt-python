#! /usr/bin/env python3
#
def diffusion_pde_test ( ):

#*****************************************************************************80
#
## diffusion_pde_test() solves the diffusion PDE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'diffusion_pde_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve a diffusion PDE using the FTCS difference method.' )

  diffusion_pde_ftcs ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusion_pde_test():' )
  print ( '  Normal end of execution.' )

  return

def diffusion_conserved ( x, u ):

#*****************************************************************************80
#
## diffusion_conserved() evaluates the conserved quantity for diffusion PDE.
#
#  Discussion:
#
#    The integral of U over the region should be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(NX), the coordinates of the nodes.
#
#    real U(NX), the current solution.
#
#  Output:
#
#    real H: the value of the conserved quantity.
#
  import numpy as np

  nx = x.size
  dx = ( np.max ( x ) - np.min ( x ) ) / ( nx - 1 )
  h = np.sum ( u ) * dx

  return h

def diffusion_deriv ( t, u, x ):

#*****************************************************************************80
#
## diffusion_deriv() returns the right hand side of the diffusion ODE.
#
#  Discussion:
#
#    This version of the equation has the form:
#
#      du/dt = nu * uxx
#
#    Zero Neumann boundary conditions are assumed, and so we
#    set dudt(1) = dudt(2) and dudt(nx) = dudt(nx-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Costica Morosanu, Silvio Paval,
#    On the numerical approximation of a nonlinear reaction-diffusion
#    equation with non-homogeneous Neumann boundary conditions.  Case 1D,
#    ROMAI Journal,
#    Volume 15, Number 2, pages 43-60, 2019.
#
#    Jian Zhang, Qiang Du,
#    Numerical studies of discrete approximations to the Allen-Cahn
#    equation in the sharp interface limit,
#    SIAM Journal on Scientific Computing,
#    Volume 31, Number 4, pages 3042-3063, 2009.
#
#  Input:
#
#    real T, the current time.
#
#    real U(*): the current state values.
#
#    real X(*): the node coordinates.
#
#  Output:
#
#    real DUDT(*), the time derivatives of the current state values.
#
  mu, t0, tstop, xmin, xmax = diffusion_parameters ( )

  uxx = laplacian_interval ( u, x )

  dudt = mu * uxx
#
#  Apply periodic boundary conditions.
#
  dudt[0] = dudt[1]
  dudt[-1] = dudt[-2]

  return dudt

def diffusion_initial ( x ):

#*****************************************************************************80
#
## diffusion_initial() sets the initial condition for the diffusion PDE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(NX), the coordinates of the nodes.
#
#  Output:
#
#    real U(NX), the initial condition for the solution.
#
  import numpy as np

  u = np.zeros_like ( x )
  k = np.nonzero ( ( 0.6 <= x ) & ( x <= 0.8 ) )
  u[k] = ( 10.0 * x[k] - 6.0 )**2 * ( 8.0 - 10.0 * x[k] )**2

  return u

def diffusion_parameters ( mu_user = None, t0_user = None, tstop_user = None, \
  xmin_user = None, xmax_user = None ):

#*****************************************************************************80
#
## diffusion_parameters() returns the parameters of the diffusion PDE.
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
#    05 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU_USER: the diffusion coefficient.
#
#    real T0_USER: the initial time.
#
#    real TSTOP_USER: the final time.
#
#    real XMIN_USER: the minimum X value.
#
#    real XMAX_USER: the maximum X value.
#
#  Output:
#
#    real MU: the diffusion coefficient.
#
#    real T0: the initial time.
#
#    real TSTOP: the final time.
#
#    real XMIN: the minimum X value.
#
#    real XMAX: the maximum X value.
#

#
#  Initialize defaults.
#
  if not hasattr ( diffusion_parameters, "mu_default" ):
    diffusion_parameters.mu_default = 0.5

  if not hasattr ( diffusion_parameters, "t0_default" ):
    diffusion_parameters.t0_default = 0.0

  if not hasattr ( diffusion_parameters, "tstop_default" ):
    diffusion_parameters.tstop_default = 0.03

  if not hasattr ( diffusion_parameters, "xmin_default" ):
    diffusion_parameters.xmin_default = 0.0

  if not hasattr ( diffusion_parameters, "xmax_default" ):
    diffusion_parameters.xmax_default = 1.0
#
#  Update defaults if input was supplied.
#
  if ( mu_user is not None ):
    diffusion_parameters.mu_default = mu_user

  if ( t0_user is not None ):
    diffusion_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    diffusion_parameters.tstop_default = tstop_user

  if ( xmin_user is not None ):
    diffusion_parameters.xmin_default = xmin_user

  if ( xmax_user is not None ):
    diffusion_parameters.xmax_default = xmax_user
#
#  Return values.
#
  mu = diffusion_parameters.mu_default
  t0 = diffusion_parameters.t0_default
  tstop = diffusion_parameters.tstop_default
  xmin = diffusion_parameters.xmin_default
  xmax = diffusion_parameters.xmax_default

  return mu, t0, tstop, xmin, xmax

def diffusion_pde_ftcs ( ):

#*****************************************************************************80
#
## diffusion_pde_ftcs() solves the diffusion PDE using the FTCS method.
#
#  Discussion:
#
#    The FTCS method (Forward Time, Center Space) is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent diffusion-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'diffusion_pde_ftcs():' )
  print ( '  Solve the diffusion PDE in 1D,' )
  print ( '    du/dt - mu d2u/dx2 = 0' )
  print ( '  over the interval:' )
  print ( '    0.0 <= x <= 1.0' )
  print ( '  with periodic boundary conditions:' )
  print ( '    u(0.0) = u(1.0)' )
  print ( '  and diffusion coefficient' )
  print ( '    mu = constant' )
  print ( '  and initial condition' )
  print ( '    u(0,x) = (10x-6)^2 (8-10x)^2 for 0.6 <= x <= 0.8' )
  print ( '           = 0 elsewhere.' )
  print ( '  and NX equally spaced nodes in X,' )
  print ( '  and NT equally spaced points in T,' )
  print ( '  using the FTCS method:' )
  print ( '    FT: Forward Time  : du/dt = (u(t+dt,x)-u(t,x))/dt' )
  print ( '    CS: Centered Space: d2u/dx2 = (u(t,x+dx)-2u(t,x)+u(t,x-dx))/dx^2' )

  mu, t0, tstop, xmin, xmax = diffusion_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    mu    = ', mu )
  print ( '    t0    = ', t0 )
  print ( '    tstop = ', tstop )
  print ( '    xmin  = ', xmin )
  print ( '    xmax  = ', xmax )

  nx = 101
  dx = ( xmax - xmin ) / ( nx - 1 )
  x = np.linspace ( xmin, xmax, nx )

  nt = 601
  dt = ( tstop - t0 ) / ( nt - 1 )
  t = np.linspace ( t0, tstop, nt )

  h = np.zeros ( nt )

  cfl = mu * dt / dx**2

  print ( '' )
  print ( '  Number of nodes NX = ', nx )
  print ( '  Number of time steps NT = ', nt )
  print ( '  CFL coefficient ( must be < 0.5 ) = ', cfl )
#
#  Setting up im1, i, ip1 allows us to define the centered spatial difference
#  with the periodic boundary condition.
#
#  im1 = [ nx-1, 0, 1, 2, ..., nx-2 ]
#  i   = [       0, 1, 2, ..., nx-2, nx-1 ]
#  ip1 = [          1, 2, ..., nx-2, nx-1, 0 ]
#
  im1 = np.arange ( 0, nx - 1 )
  im1 = np.insert ( im1, 0, nx-1 )
  
  i   = np.arange ( 0, nx )

  ip1 = np.arange ( 1, nx )
  ip1 = np.append ( ip1, 0 )
#
#  Compute the solution at time steps 0, 1, ..., NT-1.
#
  for j in range ( 0, nt ):
#
#  Apply the initial condition to get solution at initial time.
#
    if ( j == 0 ):

      u = diffusion_initial ( x )
      umax = np.max ( u ) * np.ones ( nx )
      umin = np.min ( u ) * np.ones ( nx )
#
#  At later times, rearrange
#
#    u(x(i),t(j)) - u(x(i),t(j-1))        u(x(i+1),t(j-1)) - 2u(x(i),t(j-1)) + u(x(i-1),t(j-1))
#    ----------------------------- - mu * ----------------------------------------------------- = 0
#                dt                                               dx^2
#
#  to get
#
#    u(x(i),t(j)) = u(x(i),t(j-1)) ...
#      + mu * dt / ( 2 dx^2 ) * ( u(x(i+1),t(j-1)) - 2 u(x(i),t(j-1) + u(x(i-1),t(j-1)) )
#
    else:
      u[i] = u[i] + mu * dt / dx**2 * ( u[ip1] - 2 * u[i] + u[im1] )

    h[j] = diffusion_conserved ( x, u )
#
#  Display the solution.
#
    plt.clf ( )
    plt.plot ( x, umin, 'r-', linewidth = 3 )
    plt.plot ( x, umax, 'r-', linewidth = 3 )
    plt.plot ( x, u,    'b-', linewidth = 3 )

    plt.grid ( True )
    plt.xlabel ( '<--- x --->' )
    plt.ylabel ( '<--- u(x,t) --->' )
    title_string = 'diffusion PDE FTCS, Time = ' + str ( t[j] )
    plt.title ( title_string )

    if ( j == 0 ):
      filename = 'diffusion_pde_ftcs_initial.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( j == nt - 1 ):
      filename = 'diffusion_pde_ftcs_final.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
#
#  Plot the conservation quantity.
#
  plt.clf ( )
  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( [ t0, tstop ], [ h[0], h[0] ], 'k:', linewidth = 3 )
  plt.plot ( [ t0, tstop ], [ 0.0, 0.0 ], 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- h(t) --->' )
  plt.legend ( [ 'H computed', 'H initial', 'X axis' ] )
  plt.title ( 'diffusion PDE ftcs: conservation' )
  filename = 'diffusion_pde_ftcs_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def laplacian_interval ( u, x ):

#*****************************************************************************80
#
## laplacian_interval() approximates the laplacian on an interval.
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
#  Modified:
#
#    30 June 2020
#
#  Input:
#
#    real u(nx): the values of a function on an equally spaced grid of points.
#
#    real x(nx): the node coordinates.
#
#  Output:
#
#    real uxx(nx): the estimate for the laplacian.
#
  import numpy as np

  nx = len ( u )

  uxl = ( u[1:nx-1] - u[0:nx-2] ) / ( x[1:nx-1] - x[0:nx-2] )
  uxr = ( u[2:nx]   - u[1:nx-1] ) / ( x[2:nx]   - x[1:nx-1] )

  uxx = 2.0 * ( uxr[0:nx-2] - uxl[0:nx-2] ) / ( x[2:nx] - x[0:nx-2] )
#
#  Pad the result with initial and final 0.
#
  uxx = np.insert ( uxx, 0, 0.0 )
  uxx = np.insert ( uxx, nx-1, 0.0 )

  return uxx

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
  diffusion_pde_test ( )
  timestamp ( )

