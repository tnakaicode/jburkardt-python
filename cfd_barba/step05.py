#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP05 examines the 2-D linear convection equation.
#
#  Discussion:
#
#    Up to now, all of our work has been in one spatial dimension (Steps 1 to 
#    4). We can learn a lot in just 1D, but let's grow up to flatland: two 
#    dimensions.
#
#    In the following exercises, you will extend the first four steps to 2D. 
#    To extend the 1D finite-difference formulas to partial derivatives in 2D 
#    or 3D, just apply the definition: a partial derivative with respect to x
#    is the variation in the x direction at constant y.
#
#    In 2D space, we can discretize a rectangular region by creating a
#    (uniform) grid is defined by points with coordinates:
#      x(i) = x0 + i dx, 0 <= i < nx
#      y(j) = y0 + j dy, 0 <= j < ny
#    where (x0,y0) is the location of the lower left corner of the region.
#
#    Using this discretization of a region, we may define discretized functions
#    by listing a value at every grid point (i,j).  Thus u(i,j) will be the 
#    value of our discretized function at the point (x(i),y(j)).
#
#    In fact, our solution varies with time.  Therefore, we can imagine
#    discretizing time, using an index n, running 0 <= n <= nt.  If we
#    wish to discuss a discretized solution value, then strictly speaking
#    we should include all three indices when referencing it, perhaps
#    in the order n, i, j, so that we would refer to a typical entry as
#    u(n,i,j).  
#
#    However, in cases where the time variable is not important, we might
#    simply write u(i,j) instead.
#
#    A differential equation in 2D may include (first order) partial derivatives.
#    Such a derivative considers changes in a function of x, y and t that occur
#    when only one variable is changed.  Thus, the corresponding finite 
#    difference approximation to a partial derivative simply compares values
#    of the function along one coordinate ( t, x, or y ), using the 2D
#    Taylor expansion only in that coordinate direction.
#
#    Here, for example, is how a first order partial derivative with respect
#    to x can be approximated by a forward difference in x:
#
#      du                   ( u(n,i+1,j) - u(n,i,j)
#      --(t(n),x(i),y(j)) = ----------------------- + O(dx)
#      dx                                dx
#
#    We could also use a backward or central difference for this approximation.
#    A first order partial derivative with respect to y would be handled by
#    a difference in the j direction.
#
#    The 2D linear convection equation is a generalization of the 1D
#    equation, and is written as
#
#      du     ( du   du )
#      -- + c ( -- + -- ) = 0
#      dt     ( dx   dy )
#
#    For our finite difference approximation, the timestep will be discretized 
#    as a forward difference and both spatial steps will be discretized as 
#    backward differences.
#
#    With the 1D implementation, we used the i subscript to denote movement 
#    in the x spatial direction, as in u(n,i)-u(n,i-1).  Now that we have two 
#    dimensions to account for, we need to add a second subscript, j, which 
#    will correspond to variation in the y spatial direction, along with the
#    n index for time.
#
#    With that in mind, our discretization of the PDE should be relatively
#    straightforward:
#
#      u(n+1,i,j) - u(n,i,j)     ( u(n,i,j) - u(n,i-1,j)   u(n,i,j) - u(n,i,j-1) )
#      --------------------- + c ( --------------------- + --------------------  ) = 0
#                dt              (         dx                      dy            )
#
#    As before, solve for the only unknown:
#
#      u(n+1,i,j) = u(n,i,j) - c dt/dx ( 2 u(n,i,j) - u(n,i-1,j) - u(n,i,j-1) )
#
#    We will solve this equation with the following initial conditions
#    at t = 0.0 (or n = 0):
#
#      u(0.0,x,y) = 2.0 if x and y are both greater than 0.5 and less than 1;
#                   1.0 otherwise
#
#    and boundary conditions, for any t greater than 0:
#      u(t,x,y) = 1.0 for x=0.0 or y=0.0 or x=2.0 or y=2.0
#    which is equivalent to the discrete conditions:
#      u(n,i,j) = 1.0 if i = 0 or i = nx - 1 or j = 0 or j = ny - 1.
#
#  Modified:
#
#    18 May 2016
#
#  Author:
#
#    Lorena Barba
#
import numpy
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
#  Now we import pyplot for graphics, and give it an abbreviated name.
#
import matplotlib.pyplot as plt
#
#  Import a library needed for 3D plots.
#
from mpl_toolkits.mplot3d import Axes3D

print ( '' )
print ( 'STEP05:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 2D linear convection equation.' )
#
#  Define problem variables
#
nx = 81
ny = 81
nt = 100
c = 1.0
dx = 2.0 / ( nx - 1 )
dy = 2.0 / ( ny - 1 )
sigma = 0.2
dt = sigma * dx
#
#  Define 1D vectors of X and Y coordinates.
#
x = numpy.linspace ( 0.0, 2.0, nx )
y = numpy.linspace ( 0.0, 2.0, ny )
#
#  Set the initial conditions.
#
u = numpy.ones ( ( ny, nx ) )
u[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
#
#  Plot the initial condition
#  The "figsize" parameter can be used to control the size of the image.
#
fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )                      
X, Y = numpy.meshgrid ( x, y )                            
surf = ax.plot_surface ( X, Y, u[:] )
#
#  Save a copy of the plot.
#
plt.savefig ( 'step05_initial' )
print ( '  Saved initial solution in file "step05_initial.png".' )
#
#  3D Plotting Notes
#
#  The actual plotting commands are a little more involved than with 
#  simple 2d plots.
#
#  The line 
#    fig = plt.figure ( figsize = ( 11, 7 ), dpi=100)
#  is initializing a figure window. 
#  The figsize and dpi commands are optional and simply specify the size 
#  and resolution of the figure being produced. 
#  You may omit them, but you will still require the command
#    fig = plt.figure ( )
#
#  The line 
#    ax = fig.gca(projection='3d')
#  assigns the label 'ax' to the plot window and specifies that it will 
#  be a 3d projection plot. 
#
#  The X and Y objects are not the 1-D vectors x and y. 
#  In order to use matplotlib's 3D plotting functions, you need to generate 
#  a grid of x, y values of each coordinate in the plotting frame. 
#  This coordinate grid is generated form x and y using the numpy function meshgrid.
#    X, Y = numpy.meshgrid ( x, y )
#
#  The final line uses the command
#    surf = ax.plot_surface(X,Y,u[:])
#  which is similar to the familiar plot command, but takes a grid of X and Y 
#  values for the data point positions.
#

#
#  To evaluate the wave in two dimensions requires the use of several nested 
#  for-loops to cover all of the i's and j's.  Since Python is not a compiled 
#  language there can be noticeable slowdowns in the execution of code with 
#  multiple for-loops. 
#
for n in range ( nt + 1 ):
  un = u.copy ( )
  row, col = u.shape
  for j in range ( 1, row ):
    for i in range ( 1, col ):
      u[j,i] = un[j,i] - c * dt / dx * ( 2.0 * un[j,i] - un[j,i-1] - un[j-1,i] )
      u[0,:] = 1.0
      u[-1,:] = 1.0
      u[:,0] = 1.0
      u[:,-1] = 1.0

fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
surf1 = ax.plot_surface ( X, Y, u[:] )
#
#  Save a copy of the plot.
#
plt.savefig ( 'step05_final1' )
print ( '  Saved final1 solution in file "step05_final1.png".' )
#
#  Instead of the nested for loops above, we can use array operations.
#  Before doing so, we have to restore U to the initial condition:
#
u = numpy.ones ( ( ny, nx ) )
u[(ny-1)//4:(ny-1)//2+1,(nx-1)//4:(nx-1)//2+1] = 2.0
#
#  Carry out the time steps using array operations.
#
for n in range ( nt + 1 ):
  un = u.copy ( )
  u[1:,1:] = un[1:,1:] - c * dt / dx * ( 2.0 * un[1:,1:] - un[1:,:-1] - un[:-1,1:] )
  u[0,:] = 1.0
  u[-1,:] = 1.0
  u[:,0] = 1.0
  u[:,-1] = 1.0

fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
ax = fig.gca ( projection = '3d' )
surf2 = ax.plot_surface ( X, Y, u[:] )
#
#  Save a copy of the plot.
#
plt.savefig ( 'step05_final2' )
print ( '  Saved final2 solution in file "step05_final2.png".' )
#
#  The video lesson that walks you through the details for Step 5, and onwards 
#  to Step 8, is Video Lesson 6 on You Tube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP05:' )
print ( '  Normal end of execution.' )

