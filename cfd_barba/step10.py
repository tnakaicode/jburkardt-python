#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP10 examines the 2D Poisson equation.
#
#  Discussion:
#
#    For a moment, recall the Navier-Stokes equations for an incompressible 
#    fluid, letting v represent the velocity vector, and p the pressure:
#
#      dv                      -1
#      -- + ( v dot del ) v =  --- del p + nu del^2 v
#      dt                      rho
#
#      del dot v = 0
#
#    The first equation is the conservation of momentum. 
#    The second equation, the "continuity equation", represents mass 
#    conservation at constant density. 
#
#    But a problem appears: the continuity equation for incompressble flow 
#    does not have a dominant variable and there is no obvious way to couple 
#    the velocity and the pressure.  In contrast, in the case of compressible 
#    flow, mass continuity would provide an evolution equation for the 
#    density rho, which is coupled with an equation of state relating rho and p.
#
#    In incompressible flow, the continuity equation provides a constraint 
#    on the velocity field, so that the pressure field must exert an influence
#    on the velocity field that guarantees that the expansion rate ( del v )
#    vanishes everywhere.
#
#    A way out of this difficulty is to construct a pressure field that 
#    guarantees continuity is satisfied; such a relation can be obtained by 
#    taking the divergence of the momentum equation.  In that process, a 
#    Poisson equation for the pressure shows up!
#
#    Poisson's equation is obtained by including a source term function b(x,y)
#    to the right hand side of Laplace's equation:
#
#      d2 p   d2 p 
#      ---- + ---- = b
#      dx2    dy2
#
#    So, unlike the Laplace equation, there is some nonzero value inside the 
#    field that affects the solution.  Poisson's equation acts to "relax" the 
#    initial sources in the field.
#
#    In discretized form, this looks almost the same as Step 9, except for the 
#    source term:
#
#      p(n,i+1,j) - 2 p(n,i,j) + p(n,i-1,j)   p(n,i,j+1) - 2 p(n,i,j) + p(n,i,j-1)
#      ------------------------------------ + ------------------------------------ = b(i,j)
#                     dx^2                                   dy^2
#
#    As before, we rearrange to obtain an equation for p at point i,j
#
#      p(n,i,j) = ( dy^2 ( p(n,i+1,j) + p(n,i-1,j)
#                 + dx^2 ( p(n,i,j+1) + p(n,i,j-1)
#                 - dx^2 dy^2 b(i,j) )
#                 / 2 / ( dx^2 + dy^2 )
#
#    We will solve this equation by assuming an initial state of p=0
#    everywhere, and applying boundary conditions as follows:
#
#      p = 0 at x = 0 or x = 2 or y = 0 or y = 1.
#
#    The source term b consists of two spikes inside the domain:
#
#      b(i,j) = +100.0 at (i,j)=(nx/4,ny/4)
#      b(i,j) = -100.0 at (i,j)=(3*nx/4,3*ny/4)
#      b(i,j) =    0.0 elsewhere
#
#    The iterations will advance in pseudo-time to relax the initial spikes. 
#    The relaxation under Poisson's equation gets slower and slower as they 
#    progress. Why?
#
#    Let's look at one possible way to write the code for Poisson's equation. 
#    As always, we load our favorite Python libraries.  We also want to make 
#    some lovely plots in 3D.  Let's get our parameters defined and the 
#    initialization out of the way.  What do you notice of the approach below?
#
#  Modified:
#
#    21 May 2016
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
print ( 'STEP10:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 2D Poisson equation.' )


#
#  Problem parameters
#
nx = 50
ny = 50
nt  = 100
xmin = 0.0
xmax = 2.0
ymin = 0.0
ymax = 1.0

dx = ( xmax - xmin ) / ( nx - 1 )
dy = ( ymax - ymin ) / ( ny - 1 )
#
#  Set the x and y coordinate vectors.
#
x  = numpy.linspace ( xmin, xmax, nx )
y  = numpy.linspace ( ymin, ymax, ny )
#
#  Set the initial guess.  Enforce the boundary conditions.
#
p = numpy.zeros ( ( ny, nx ) )
p[0,:] = 0.0
p[ny-1,:] = 0.0
p[:,0] = 0.0
p[:,nx-1] = 0.0
#
#  Set the source term.
#
b = numpy.zeros ( ( ny, nx ) )
b[ny//4,nx//4] = 100.0
b[3*ny//4,3*nx//4] = -100.0
#
#  We are ready to advance the initial guess in pseudo-time. 
#  How is the code below different from the function used in Step 9 to 
#  solve Laplace's equation?
#
for it in range ( nt ):

  pd = p.copy ( )

  p[1:-1,1:-1] = ( dy ** 2 * ( pd[1:-1,2:] + pd[1:-1,:-2] ) \
                 + dx ** 2 * ( pd[2:,1:-1] + pd[:-2,1:-1] ) \
                 - dx ** 2 * dy ** 2 * b[1:-1,1:-1] ) \
                 / ( 2.0 * ( dx ** 2 + dy ** 2 ) )

  p[0,:] = 0.0
  p[ny-1,:] = 0.0
  p[:,0] = 0.0
  p[:,nx-1] = 0.0
#
#  Maybe we could reuse our plotting function from Step 9, don't you think?
#
#  The function plot2d takes three arguments, 
#  * an x-vector, 
#  * a y-vector
#  * our p matrix. 
#
#  Given these three values, it produces a 3D projection plot, 
#  sets the plot limits and gives us a nice viewing angle.
#
def plot2d ( x, y, p ):
  fig = plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
  ax = fig.gca ( projection = '3d' )
  X,Y = numpy.meshgrid ( x, y )
  surf = ax.plot_surface ( X, Y, p[:], rstride = 1, cstride = 1, cmap = cm.coolwarm,
    linewidth = 0, antialiased = False )
  ax.set_xlim ( 0.0, 2.0 )
  ax.set_ylim ( 0.0, 1.0 )
  ax.view_init ( 30, 225 )
#
#  Here's where we call it:
#
plot2d ( x, y, p )
plt.savefig ( 'step10_final' )
print ( '  Saved final solution in file "step10_final.png".' )
#
#  Ah!  The wonders of code reuse!  Now, you probably think: "Well, if I've 
#  written this neat little function that does something so useful, I want 
#  to use it over and over again.  How can I do this without copying and 
#  pasting it each time?  If you are very curious about this, you'll have to 
#  learn about packaging.  But this goes beyond the scope of our CFD lessons. 
#  You'll just have to Google it if you really want to know.
#
#  To learn more about the role of the Poisson equation in CFD, watch Video 
#  Lesson 11 on YouTube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP10:' )
print ( '  Normal end of execution.' )

