#! /usr/bin/env python3
#
def wave_pde_test ( ):

#*****************************************************************************80
#
## wave_pde_test() solves a 1D wave equation with periodic boundary conditions.
#
#  Discussion:
#
#    d^2 u / dt^2 = c * d^2 u / dx^2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 April 2025
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'wave_pde():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Solve the wave equation in one space and time dimension.' )
  print ( '  Use periodic boundary conditions, and a sinusoidal solution.' )
#
#  Compute solution on time/space grid.
#
  c = 1.0

  nx = 25
  xmin = 0.0
  xmax = 2.0 * np.pi
  x = np.linspace ( xmin, xmax, nx )
  dx = ( xmax - xmin ) / ( nx - 1 )

  nt = 101
  tmin = 0.0
  tmax = 2.0 * np.pi
  t = np.linspace ( tmin, tmax, nt )
  dt = ( tmax - tmin ) / ( nt - 1 )

  print ( '  CFL = c * dt**2 / dx**2 = ', c * dt**2 / dx**2 )

  U = np.zeros ( [ nt, nx ] )
  
  for i in range ( 0, nt ):

    if ( i == 0 ):
      U[0,:] = np.sin ( x ) * np.cos ( c * t[0] )
    elif ( i == 1 ):
      dudt = np.sin(x) * c * np.sin ( c * t[0] )
      U[1,:] = U[0,:] + dt * dudt
    else:
#
#  The first and last equations are at the same periodic point.
#
#          0     1  2 ...  nx-2  nx-1
# nx-2   nx-1                      0    1
#
      U[i,0] = 2.0 * U[i-1,0] - U[i-2,0] \
          + c * dt**2 / dx**2 \
          * ( U[i-1,nx-2] - 2.0 * U[i-1,0] + U[i-1,1] )

      U[i,1:nx-1] = 2.0 * U[i-1,1:nx-1] - U[i-2,1:nx-1] \
          + c * dt**2 / dx**2 \
          * ( U[i-1,0:nx-2] - 2.0 * U[i-1,1:nx-1] + U[i-1,2:nx] )

      U[i,nx-1] = 2.0 * U[i-1,nx-1] - U[i-2,nx-1] \
          + c * dt**2 / dx**2 \
          * ( U[i-1,nx-2] - 2.0 * U[i-1,nx-1] + U[i-1,1] ) 
#
#  Make a sequence of frames for a later animation.
#
  for i in range ( 0, nt ):

    plt.clf ( )
    plt.xlim ( xmin, xmax )
    plt.ylim ( -1.0, 1.0 )
    plt.plot ( x, U[i,:], 'b-', linewidth = 2 )
    plt.grid ( True )
    plt.xlabel ( '<--- X --->' )
    plt.ylabel ( '<--- U(T,X) --->' )
    plt.title ( 'Wave equation, t = ' + str ( t[i] ) )
    filename = 'wave_pde_' + str ( i ).zfill(3) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Make a surface plot.
#
  X, T = np.meshgrid ( x, t )

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( X, T, U, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Wave equation, periodic', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- T --->', fontsize = 16 )
  ax.set_zlabel ( '<--- U(T,X) --->', fontsize = 16 )
  filename = 'wave_pde.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

if ( __name__ == "__main__" ):
  wave_pde_test ( )

