#! /usr/bin/env python3
#
def fisher_pde_ftcs ( ):

#*****************************************************************************80
#
## fisher_pde_ftcs() solves the KPP Fisher equation using FTCS().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import os
  import platform
#
#  Set the X values.
#
  nx = 51
  xmin = 0.0
  xmax = 1.0
  x = np.linspace ( xmin, xmax, nx )
  dx = ( xmax - xmin ) / ( nx - 1 )
#
#  Set the T values.
#
  nt = 801
  tmin = 0.0
  tmax = 0.05
  t = np.linspace ( tmin, tmax, nt )
  dt = ( tmax - tmin ) / ( nt - 1 )
#
#  Indexes to approximate uxx:
#
  I = np.arange ( 0, nx )
  Im1 = np.roll ( I, +1 )
  Ip1 = np.roll ( I, -1 )

  print ( '' )
  print ( 'fisher_pde_ftcs():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve the KPP Fisher PDE using ftcs()' )
  print ( '    du/dt = uxx + u * ( 1 - u )' )
  print ( '  over the spatial interval:' )
  print ( '    ', xmin, ' <= x <= ', xmax )
  print ( '  and time interval' )
  print ( '     ', tmin, ' <= t <= ', tmax )
  print ( '  with boundary conditions:' )
  print ( '    u(', xmin, ') = ( cos(100*t(j)) + 1.5 ) / 2.5 (Dirichlet)' )
  print ( '    u\'(', xmax, ') = 0.0 (Neumann)' )
  print ( '  and initial condition' )
  print ( '    u(0,x) = ( cos ( 15.0 * x ) + 1.5 ) / 2.5.' )
  print ( '  Create a sequence of graphic figures.' )
  print ( '  Save each one to a png file.' )
  print ( '  Use "convert()" to create a gif animation.' )

  print ( '  Space steps = ', nx )
  print ( '  Space interval is [',xmin,',',xmax,']' )
  print ( '  Space increment is ', dx )
  print ( '' )
  print ( '  Time steps = ', nt )
  print ( '  Time interval is [',tmin,',',tmax,']' )
  print ( '  Time increment is ', dt )
#
#  Set the initial condition.
#
  frame = 0

  for j in range ( 0, nt ):

    if ( j == 0 ):
      u = ( np.cos ( 15.0 * x ) + 1.5 ) / 2.5
    else:
      dudxx = ( u[Ip1] - 2.0 * u[I] + u[Im1] ) / dx**2
      dudt = dudxx + u * ( 1.0 - u )
      u = u + dt * dudt
#
#  Enforce the Dirichlet condition on the left.
#
    u[0] = ( np.cos ( 100.0 * t[j] ) + 1.5 ) / 2.5
#
#  Enforce the Neumann condition on the right.
#
    u[nx-1] = u[nx-2]
#
#  Display the current solution.
#
    plt.clf ( )
    plt.plot ( x, u, 'b-', linewidth = 2 )
    plt.plot ( [ xmin, xmax ], [ 0.0, 0.0 ], 'k-', linewidth = 2 ) 
    plt.axis ( [ xmin, xmax, 0.0, 1.0 ] )
    plt.grid ( True )
    label = ( 'u(t,x), fisher pde ftcs, step = %d, t=%.3f' % ( j, t[j] ) )
    plt.title ( label )
    plt.xlabel ( '<--- X --->' )
    plt.ylabel ( '<--- U(T,X) --->' )

    if ( ( j % 25 ) == 0 ):
      filename = ( '%05d_frame.png' % ( frame ) )
      plt.savefig ( filename )
      frame = frame + 1

    if ( j == 0 ):
      filename = 'fisher_pde_ftcs_initial.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( j == nt - 1 ):
      filename = 'fisher_pde_ftcs_final.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
#
#  Use Imagemagick "convert()" to merge png images into an animation file.
#
  os.system ( "convert -delay 10 -loop 0 *.png fisher_pde_ftcs.gif" )
  print ( '  Animation created as "fisher_pde_ftcs.gif"' )
  os.system ( "rm *_frame.png" )
  print ( '  Removed frame files.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fisher_pde_ftcs():' )
  print ( '  Normal end of execution.' )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  fisher_pde_ftcs ( )
  timestamp ( )

