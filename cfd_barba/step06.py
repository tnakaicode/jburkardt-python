#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP06 examines the 2D nonlinear convection equation.
#
#  Discussion:
#
#    Now we solve the 2D nonlinear convection equation, represented by the 
#    pair of coupled partial differential equations:
#
#      du     du     du
#      -- + u -- + v -- = 0
#      dt     dx     dy
#
#      dv     dv     dv
#      -- + u -- + v -- = 0
#      dt     dx     dy
#
#    Discretizing these equations using the methods we've applied previously yields:
#
#      u(n+1,i,j) - u(n,i,j)
#      --------------------- ...
#                 dt
#
#                  u(n,i,j) - u(n,i-1,j)            u(n,i,j) - u(n,i,j-1)
#      + u(n,i,j) --------------------- + v(n,i,j) --------------------- = 0
#                           dx                               dy
#
#      v(n+1,i,j) - v(n,i,j)
#      --------------------- ...
#                 dt
#
#                 v(n,i,j) - v(n,i-1,j)            v(n,i,j) - v(n,i,j-1)
#      + u(n,i,j) --------------------- + v(n,i,j) --------------------- = 0
#                     dx                               dy
#
#    We rearrange both equations to solve for u(n+1,i,j) and v(n+1,i,j).
#
#      u(n+1,i,j) = u(n,i,j) - u(n,i,j) dt/dx (u(n,i,j)-u(n,i-1,j)) 
#                            - v(n,i,j) dt/dy (u(n,i,j)-u(n,i,j-1))
#
#      v(n+1,i,j) = v(n,i,j) - u(n,i,j) dt/dx (v(n,i,j)-v(n,i-1,j)) 
#                            - v(n,i,j) dt/dy (v(n,i,j)-v(n,i,j-1))
#
#    The initial conditions are the same as those we used for 1D convection, 
#    applied in both the x and y directions.
#
#      u, v = 2, if (x,y) is in [0.5,1]x[0.5,1]
#           = 1, everywhere else
#
#    The boundary conditions hold u and v equal to 1 along the boundaries
#    of the grid .
#
#      u=1, v=1 for {x=0,2y=0,2
#
#  Modified:
#
#    18 May 2016
#
#  Author:
#
#    Lorena Barba
#
import platform
#
#  Load the matplotlib library, for graphics.
#
import matplotlib
#
#  We aren't issuing commands interactively.  So we want the graphics to
#  go to a png file, not to the screen.  To do this, we have to request
#  the noninteractive graphics backend called 'Agg'.
#
matplotlib.use ( 'Agg' )
#
#  cm = "colormap" for changing the 3d plot color palette
#
from matplotlib import cm
#
#  Now we import pyplot for graphics, and give it an abbreviated name.
#
import matplotlib.pyplot as plt
#
#  Import a library needed for 3D plots.
#
from mpl_toolkits.mplot3d import Axes3D

print ( '' )
print ( 'STEP06:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 2D nonlinear convection equation.' )

import numpy
#
#  Problem variables
#
nx = 101
ny = 101
nt = 80
dx = 2.0 / ( nx - 1 )
dy = 2.0 / ( ny - 1 )
sigma = 0.2
dt = sigma * dx
#
#  Create x, y vectors.
#
x = numpy.linspace ( 0.0, 2.0, nx )
y = numpy.linspace ( 0.0, 2.0, ny )
#
#  Create X, Y tables for plotting.
#
X, Y = numpy.meshgrid ( x, y )
#
#  Initial conditions.
#
u = numpy.ones ( ( ny, nx ) )
u[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
v = numpy.ones ( ( ny, nx ) )
v[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
#
#  Plot the initial conditions for U and V.
#
fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
ax.plot_surface ( X, Y, u, cmap = cm.coolwarm )
plt.savefig ( 'img/step06_initial_u' )
print ( '  Saved initial solution in file "step06_initial_u.png".' )

fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
ax.plot_surface ( X, Y, v, cmap = cm.coolwarm );
plt.savefig ( 'img/step06_initial_v' )
print ( '  Saved initial solution in file "step06_initial_v.png".' )
#
#  Carry out time steps.
#
for n in range ( nt + 1 ):
  un = u.copy ( )
  vn = v.copy ( )

  u[1:,1:] = un[1:,1:] - un[1:,1:] * dt / dx * ( un[1:,1:] - un[1:,:-1] ) \
                       - vn[1:,1:] * dt / dy * ( un[1:,1:] - un[:-1,1:] )
 
  v[1:,1:] = vn[1:,1:] - un[1:,1:] * dt / dx * ( vn[1:,1:] - vn[1:,:-1] ) \
                       - vn[1:,1:] * dt / dy * ( vn[1:,1:] - vn[:-1,1:] )
    
  u[0,:] = 1.0
  u[-1,:] = 1.0
  u[:,0] = 1.0
  u[:,-1] = 1.0
    
  v[0,:] = 1.0
  v[-1,:] = 1.0
  v[:,0] = 1.0
  v[:,-1] = 1.0
#
#  Plot the final solutions for U and V.
#
fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
ax.plot_surface ( X, Y, u, cmap = cm.coolwarm );
plt.savefig ( 'img/step06_final_u' )
print ( '  Saved final solution in file "step06_final_u.png".' )

fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
ax.plot_surface ( X, Y, v, cmap = cm.coolwarm );
plt.savefig ( 'img/step06_final_v' )
print ( '  Saved final solution in file "step06_final_v.png".' )
#
#  Video lesson 6 walks you through the details for Steps 5 to 8.
#
#  Terminate.
#
print ( '' )
print ( 'STEP06:' )
print ( '  Normal end of execution.' )
