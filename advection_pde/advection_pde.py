#! /usr/bin/env python3
#
def advection_pde_test ( ):

#*****************************************************************************80
#
## advection_pde_test() solves the advection PDE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'advection_pde_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve the advection PDE.' )
#
#  Get the parameters.
#
  c, t0, tstop, xmin, xmax = advection_parameters ( )

  print ( '' )
  print ( '  Parameter values():' )
  print ( '    c     = ', c )
  print ( '    t0    = ', t0 )
  print ( '    tstop = ', tstop )
  print ( '    xmin  = ', xmin )
  print ( '    xmax  = ', xmax )

  advection_pde_ftcs ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'advection_pde_test():' )
  print ( '  Normal end of execution.' )

  return

def advection_pde_ftcs ( ):

#*****************************************************************************80
#
## advection_pde_ftcs() solves the advection PDE using the FTCS method.
#
#  Discussion:
#
#    The FTCS method (Forward Time, Center Space) is unstable for the 
#    advection problem.
#
#    Given a smooth initial condition, successive FTCS approximations will
#    exhibit erroneous oscillations of increasing magnitude.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2026
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
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'advection_pde_ftcs():' )
  print ( '  Solve the constant-velocity advection PDE in 1D,' )
  print ( '    du/dt + c du/dx = 0' )
  print ( '  over the interval:' )
  print ( '    0.0 <= x <= 1.0' )
  print ( '  with periodic boundary conditions:' )
  print ( '    u(0) = u(1)' )
  print ( '  and advection velocity' )
  print ( '    c = constant' )
  print ( '  and initial condition' )
  print ( '    u(0,x) = (10x-6)^2 (8-10x)^2 for 0.6 <= x <= 0.8' )
  print ( '           = 0 elsewhere.' )
  print ( '  and NX equally spaced nodes in X,' )
  print ( '  and NT equally spaced points in T,' )
  print ( '  using the FTCS method:' )
  print ( '    FT: Forward Time  : du/dt = (u(t+dt,x)-u(t,x))/dt' )
  print ( '    CS: Centered Space: du/dx = (u(t,x+dx)-u(t,x-dx))/2/dx' )
#
#  Get the parameters.
#
  c, t0, tstop, xmin, xmax = advection_parameters ( )

  nx = 101
  dx = ( xmax - xmin ) / ( nx - 1 )
  x = np.linspace ( xmin, xmax, nx )

  nt = 8001
  dt = ( tstop - t0 ) / ( nt - 1 )
  t = np.linspace ( t0, tstop, nt )

  h = np.zeros ( nt )

  print ( '' )
  print ( '  Number of nodes NX = ', nx )
  print ( '  Number of time steps NT = ', nt )
#
#  Setting up im1, i, ip1 allows us to define the centered spatial difference
#  with the periodic boundary condition.
#
  I = np.arange ( nx )
  Im1 = np.roll ( I, 1 )
  Ip1 = np.roll ( I, -1 )
#
#  Compute the solution at each time.
#
  for j in range ( 0, nt ):
#
#  Apply the initial condition to get solution at initial time.
#
    if ( j == 0 ):
      u = advection_initial ( x )
      umax = np.max ( u ) * np.ones ( nx )
      umin = np.min ( u ) * np.ones ( nx )
#
#  At later times, rearrange
#
#    u(x(i),t(j)) - u(x(i),t(j-1))       u(x(i+1),t(j-1)) - u(x(i-1),t(j-1))
#    ----------------------------- + c * ----------------------------------- = 0
#                dt                                    2 dx
#
#  to get
#
#    u(x(i),t(j)) = u(x(i),t(j-1)) - c * dt / ( 2 dx ) * ( u(x(i+1),t(j-1)) - u(x(i-1),t(j-1)) )
#
    else:
      u[I] = u[I] - c * dt / dx / 2.0 * ( u[Ip1] - u[Im1] )

    h[j] = advection_conserved ( x, u )
#
#  Display the solution.
#
    plt.clf ( )
    plt.plot ( x, umin, 'r--', \
           x, umax, 'r--', \
           x, u, 'b-', \
           linewidth = 3 )

    plt.grid ( True )
    plt.xlabel ( '<--- x --->' )
    plt.ylabel ( '<--- u(x,t) --->' )
    plt.axis ( [ 0.0, 1.0, -2.0, +2.0 ] )
    title_string = ( 'Advection PDE FTCS: Time = %g' % ( t[j] ) )
    plt.title ( title_string )

    if ( j == 0 ):
      filename = 'advection_pde_ftcs_initial.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( j == nt - 1 ):
      filename = 'advection_pde_ftcs_final.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
#
#  Plot the conservation quantity.
#
  plt.clf ( )
  plt.plot ( t, h, 'r-',  linewidth = 3 )
  plt.plot ( [ t0, tstop ], [ h[0], h[0] ], 'k:',  linewidth = 3 )
  plt.plot ( [ t0, tstop ], [ 0.0, 0.0 ], 'k--',  linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- t --->' )
  plt.ylabel ( '<--- h(t) --->' )
  plt.legend ( [ 'H computed', 'H initial', 'X axis' ], loc = 'lower center' )
  plt.title ( 'advection pde FTCS: conservation' )
  filename = 'advection_pde_ftcs_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def advection_conserved ( x, u ):

#*****************************************************************************80
#
## advection_conserved() evaluates the conserved quantity for advection PDE.
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
#    17 March 2026
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
#    real H, the value of the conserved quantity.
#
  import numpy as np

  nx = len ( x )
  dx = ( np.max ( x ) - np.min ( x ) ) / ( nx - 1 )
  h = np.sum ( u ) * dx

  return h

def advection_initial ( x ):

#*****************************************************************************80
#
## advection_initial() sets the initial condition for the model advection PDE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2026
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
#    U(NX), the initial condition for the solution.
#
  import numpy as np

  u = np.zeros_like ( x )
#
#  I am pretty sure this idiotic way of imposing two conditions
#  is not the best!
#
  k = np.logical_and ( 0.6 <= x, x <= 0.8 )
  u[k] = ( 10.0 * x[k] - 6.0 )**2 * ( 8.0 - 10.0 * x[k] )**2

  return u

def advection_parameters ( c_user = None, t0_user = None, tstop_user = None, \
  xmin_user = None, xmax_user = None ):

#*****************************************************************************80
#
## advection_parameters() returns the parameters of the advection PDE.
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
#    17 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C_USER: the advection velocity.
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
#    real C: the advection velocity.
#
#    real T0: the initial time.
#
#    real TSTOP: the final time.
#
#    real XMIN: the minimum X value.
#
#    real XMAX: the maximum X value.
#
  if not hasattr ( advection_parameters, "c_default" ):
    advection_parameters.c_default = 5.0

  if not hasattr ( advection_parameters, "t0_default" ):
    advection_parameters.t0_default = 0.0

  if not hasattr ( advection_parameters, "tstop_default" ):
    advection_parameters.tstop_default = 0.08

  if not hasattr ( advection_parameters, "xmin_default" ):
    advection_parameters.xmin_default = 0.0

  if not hasattr ( advection_parameters, "xmax_default" ):
    advection_parameters.xmax_default = 1.0
#
#  Update defaults if input was supplied.
#
  if ( c_user is not None ):
    advection_parameters.c_default = c_user

  if ( t0_user is not None ):
    advection_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    advection_parameters.tstop_default = tstop_user

  if ( xmin_user is not None ):
    advection_parameters.xmin_default = xmin_user

  if ( xmax_user is not None ):
    advection_parameters.xmax_default = xmax_user
#
#  Return values.
#
  c = advection_parameters.c_default
  t0 = advection_parameters.t0_default
  tstop = advection_parameters.tstop_default
  xmin = advection_parameters.xmin_default
  xmax = advection_parameters.xmax_default

  return c, t0, tstop, xmin, xmax 

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
  advection_pde_test ( )
  timestamp ( )

