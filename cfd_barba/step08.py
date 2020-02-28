#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP08 examines the 2D Burgers equation.
#
#  Discussion:
#
#    This will be a milestone!  We now get to the Burgers equation.  We 
#    can learn so much more from this equation.  It plays a very important 
#    role in fluid mechanics, because it contains the full convective 
#    nonlinearity of the flow equations, and at the same time there are 
#    many known analytical solutions.
#
#    An interesting feature is that the Burgers equation can generate 
#    discontinuous solutions from an initial condition that is smooth, 
#    that is, it can develop sharp transitions that are called shocks.
#    We want to see this in two dimensions now!
#
#    Here is our coupled set of PDEs:
#
#      du     du     du      ( d2 u + d2 u )
#      -- + u -- + v -- = nu ( ----   ---- )
#      dt     dx     dy      ( dx2    dy2  )
#
#      dv     dv     dv      ( d2 v + d2 v )
#      -- + u -- + v -- = nu ( ----   ---- )
#      dt     dx     dy      ( dx2    dy2  )
#
#    We know how to discretize each term: we've already done it before
#    in the nonlinear convection and the diffusion equations.
#
#      u(n+1,i,j) - u(n,i,j)
#      --------------------- ...
#                 dt
#
#                  u(n,i,j) - u(n,i-1,j)            u(n,i,j) - u(n,i,j-1)
#      + u(n,i,j) --------------------- + v(n,i,j) --------------------- ...
#                           dx                               dy
#
#             u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j)
#      = nu * ------------------------------------  ...
#                           dx^2
#
#             u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1)
#      + nu * ------------------------------------
#                           dy^2
#
#      v(n+1,i,j) - v(n,i,j)
#      --------------------- ...
#                 dt
#
#                 v(n,i,j) - v(n,i-1,j)            v(n,i,j) - v(n,i,j-1)
#      + u(n,i,j) --------------------- + v(n,i,j) --------------------- ...
#                     dx                               dy
#
#             v(n,i+1,j) - 2 v(n,i,j) + v(n,i-1,j)
#      = nu * ------------------------------------  ...
#                           dx^2
#
#             v(n,i,j+1) - 2 v(n,i,j) + v(n,i,j-1)
#      + nu * ------------------------------------
#                           dy^2
#
#    We rearrange these equations for the two unknown components u and v
#    at the next time step:
#
#      u(n+1,i,j) = u(n,i,j) - u(n,i,j) dt/dx (u(n,i,j)-u(n,i-1,j)) 
#                            - v(n,i,j) dt/dy (u(n,i,j)-u(n,i,j-1))
#                            + nu*dt/dx^2 * ( u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j) )
#                            + nu*dt/dy^2 * ( u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1) )
#
#      v(n+1,i,j) = v(n,i,j) - u(n,i,j) dt/dx (v(n,i,j)-v(n,i-1,j)) 
#                            - v(n,i,j) dt/dy (v(n,i,j)-v(n,i,j-1))
#                            + nu*dt/dx^2 * ( v(n,i+1,j) - 2 v(n,i,j) + v(n,i-1,j) )
#                            + nu*dt/dy^2 * ( v(n,i,j+1) - 2 v(n,i,j) + v(n,i,j-1) )
#
#  Modified:
#
#    20 May 2016
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
print ( 'STEP08:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 2D Burgers equation.' )
#
#  Problem variables.
#
nx = 41
ny = 41
nt = 120
dx = 2.0 / ( nx - 1 )
dy = 2.0 / ( ny - 1 )
sigma = 0.0009
nu = 0.01
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
#  Initial conditions.
#
u = numpy.ones ( ( ny, nx ) )
u[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
v = numpy.ones ( ( ny, nx ) )
v[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
#
#  Plot the initial conditions together.
#
fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
wire1 = ax.plot_wireframe ( X, Y, u[:], cmap = cm.coolwarm )
wire2 = ax.plot_wireframe ( X, Y, v[:], cmap = cm.coolwarm )
plt.savefig ( 'step08_initial' )
print ( '  Saved initial solution in file "step08_initial.png".' )
#
#  Time steps.
#
for n in range ( nt + 1 ):
  un = u.copy ( )
  vn = v.copy ( )

  u[1:-1,1:-1] = un[1:-1,1:-1] \
    - dt / dx * un[1:-1,1:-1] * ( un[1:-1,1:-1] - un[1:-1,0:-2] ) \
    - dt / dy * vn[1:-1,1:-1] * ( un[1:-1,1:-1] - un[0:-2,1:-1] ) \
    + nu * dt / dx ** 2 * ( un[1:-1,2:] - 2 * un[1:-1,1:-1] + un[1:-1,0:-2] ) \
    + nu * dt / dy ** 2 * ( un[2:,1:-1] - 2 * un[1:-1,1:-1] + un[0:-2,1:-1] )
    
  v[1:-1,1:-1] = vn[1:-1,1:-1] \
    - dt / dx * un[1:-1,1:-1] * ( vn[1:-1,1:-1] - vn[1:-1,0:-2] ) \
    - dt / dy * vn[1:-1,1:-1] * ( vn[1:-1,1:-1] - vn[0:-2,1:-1] ) \
    + nu * dt / dx ** 2 * ( vn[1:-1,2:] - 2 * vn[1:-1,1:-1] + vn[1:-1,0:-2] ) \
    + nu * dt / dy ** 2 * ( vn[2:,1:-1] - 2 * vn[1:-1,1:-1] + vn[0:-2,1:-1] )

  u[0,:] = 1.0
  u[-1,:] = 1.0
  u[:,0] = 1.0
  u[:,-1] = 1.0
    
  v[0,:] = 1.0
  v[-1,:] = 1.0
  v[:,0] = 1.0
  v[:,-1] = 1.0
#
#  Plot the final solution.
#
fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
wire1 = ax.plot_wireframe ( X, Y, u )
wire2 = ax.plot_wireframe ( X, Y, v )
plt.savefig ( 'step08_final' )
print ( '  Saved final solution in file "step08_final.png".' )
#
#  Video lesson 6 walks you through the details for Steps 5 to 8 on YouTube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP08:' )
print ( '  Normal end of execution.' )

