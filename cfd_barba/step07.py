#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP07 examines the 2D diffusion equation.
#
#  Discussion:
#
#    You see where this is going?  We'll do 2D diffusion now, and next we 
#    will be able to combine steps 6 and 7 to solve the 2D Burgers equation. 
#    So make sure your previous steps work well before continuing.
#
#    The 2D diffusion equation for the scalar function u(x,y) is:
#
#      du      ( d2 u + d2 u )
#      -- = nu ( ----   ---- )
#      dt      ( dx2    dy2  )
#
#    Recall that we came up with a method for discretizing second order 
#    derivatives in Step 3, when investigating 1D diffusion.  We are going to 
#    use the same scheme here, with our forward difference in time and 
#    two second-order derivatives:
#
#      u(n+1,i,j) - u(n,i,j)        u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j)
#      --------------------- = nu * ------------------------------------
#                 dt                                dx^2
#
#                                   u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1)
#                            + nu * ------------------------------------
#                                                   dy^2
#
#    Once again, we reorganize the discretized equation and solve for u(n+1,i,j):
#
#      u(n+1,i,j) = u(n,i,j) + nu*dt/dx^2 * ( u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j) )
#                            + nu*dt/dy^2 * ( u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1) )
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    Lorena Barba
#
import numpy
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
import platform

print ( '' )
print ( 'STEP07:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 2D diffusion equation.' )
#
#  Problem variables.
#
nx = 31
ny = 31
nt = 17
nu = 0.05
dx = 2.0 / ( nx - 1 )
dy = 2.0 / ( ny - 1 )
sigma = 0.25
dt = sigma * dx * dy / nu
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
#  Set the initial condition.
#
u = numpy.ones ( ( ny, nx ) )
u[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
#
#  Plot the initial condition.
#
fig = plt.figure ( )
ax = fig.gca ( projection = '3d' )
surf = ax.plot_surface ( X, Y, u, rstride = 1, cstride = 1, cmap = cm.coolwarm, \
  linewidth = 0, antialiased = False )
ax.set_xlim ( 0.0, 2.0 )
ax.set_ylim ( 0.0, 2.0 )
ax.set_zlim ( 1.0, 2.5 );
plt.savefig ( 'step07_initial' )
print ( '  Saved initial solution in file "step07_initial.png".' )

def diffuse ( nt ):
#
## DIFFUSE is a separate function which runs the diffusion problem for NT steps.
#
#  Set the initial condition.
#
  u = numpy.ones ( ( ny, nx ) )
  u[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
    
  for n in range ( nt + 1 ): 
    un = u.copy ( )
    u[1:-1,1:-1] = un[1:-1,1:-1] \
      + nu * dt / dx ** 2 * ( un[1:-1,2:] - 2.0 * un[1:-1,1:-1] + un[1:-1,0:-2] ) \
      + nu * dt / dy ** 2 * ( un[2:,1:-1] - 2.0 * un[1:-1,1:-1] + un[0:-2,1:-1] )
    u[0,:] = 1.0
    u[-1,:] = 1.0
    u[:,0] = 1.0
    u[:,-1] = 1.0

  fig = plt.figure ( )
  ax = fig.gca ( projection = '3d' )
  surf = ax.plot_surface ( X, Y, u[:], rstride = 1, cstride = 1, cmap = cm.coolwarm, \
    linewidth = 0, antialiased = True )
  ax.set_xlim ( 0.0, 2.0 )
  ax.set_ylim ( 0.0, 2.0 )
  ax.set_zlim ( 1.0, 2.5 )

  filename = 'step07_{}.png'.format ( nt )
  plt.savefig ( filename )
  print ( '  Saved initial solution in file "%s".' % ( filename ) )
#
#  Solve the diffusion problem for a variety of time steps.
#
diffuse ( 10 )

diffuse ( 14 )

diffuse ( 50 )
#
#  Video lesson 6 walks you through the details for Steps 5 to 8 on YouTube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP07:' )
print ( '  Normal end of execution.' )

