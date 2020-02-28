#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP09 examines the 2D Laplace equation.
#
#  Discussion:
#
#    In the previous step, we solved the 2D Burgers equation: an important 
#    equation in the study of fluid mechanics because it contains the full 
#    convective nonlinearity of the flow equations.  With that exercise, we 
#    also build the experience to incrementatlly code a Navier-Stokes solver.
#
#    In the next two steps, we will solve the Laplace and then the Poisson 
#    equation. We will then put it all together!
#
#    Here is Laplace's equation in 2D:
#
#      d2 p   d2 p 
#      ---- + ---- = 0
#      dx2    dy2  
#
#    We know how to discretize a second order derivative.  But think about this 
#    for a minute: Laplace's equation has the features typical of diffusion 
#    phenomena.  For this reason, it has to be discretized with central 
#    differences, so that the discretization is consistent with the physics we 
#    want to simulate.
#
#    We will write the discretized equation as:
#
#      p(n,i+1,j) - 2 p(n,i,j) + p(n,i-1,j)   p(n,i,j+1) - 2 p(n,i,j) + p(n,i,j-1)
#      ------------------------------------ + ------------------------------------ = 0
#                     dx^2                                   dy^2
#
#    The original Laplace equation does not have a dependence on time.  Why do
#    we write a typical component of the discretized solution as p(n,i,j),
#    as though this was another time dependent problem?  Since we won't be given
#    an initial condition, we will actually have to simply pick an arbitrary
#    initial guess for the solution, and then carry out an iteration that we
#    hope will converge to the solution.  Thus the index n in p(n,i,j) will
#    not represent time, but the iterative steps that we will take.
#
#    The fact that the Laplace Equation does not have a time dependence 
#    indicates that instead of tracking a wave through time, as in the previous
#    steps, the Laplace equation calculates the equilibrium state of a system 
#    under the supplied boundary conditions.
#
#    If you have taken coursework in Heat Transfer, you will recognize the 
#    Laplace Equation as the steady-state heat equation.  Instead of calculating 
#    where the system will be at some time t, we will iteratively solve for 
#    p(n,i,j) until it meets a condition that we specify.  The system will 
#    reach equilibrium only as the number of iterations tends to infinity,
#    but we can approximate the equilibrium state by iterating until the change 
#    between one iteration and the next is very small.
#
#    Let's rearrange the discretized equation, solving for p(n,i,j):
#
#      p(n,i,j) = ( dy^2 ( p(n,i+1,j) + p(n,i-1,j)
#                 + dx^2 ( p(n,i,j+1) + p(n,i,j-1) )
#                 / 2 / ( dx^2 + dy^2 )
#
#    Using second-order central-difference schemes in both directions is the 
#    most widely applied method for the Laplace operator.  It is also known 
#    as the five-point difference operator, alluding to its stencil.
#
#    We are going to solve Laplace's equation numerically by assuming an 
#    initial state of p = 0 everywhere.  Then we add boundary conditions:
#
#      p = 0 at x = 0;
#      p = y at x = 2;
#      dp/dy = 0 at y = 0 and at y = 2.
#
#    Under these conditions, there is an analytical solution:
#
#      p(x,y) = x / 4 
#        - 4 * sum ( odd n ) sinh ( n pi x ) cos ( n pi y ) / ( n pi )^2 / sinh ( 2 n pi )
#
#    Exercise:
#
#    Write your own code to solve Poisson's equation using loops, in the style 
#    of coding used in our first lessons.  Then, consider the demonstration 
#    of how to write it using functions, as below, and modify your code in 
#    that style.  Can you think of reasons to abandon the old style and adopt 
#    modular coding?
#
#    Other tips:
#
#    * Visualize each step of the iterative process
#    * Think about what the boundary conditions are doing
#    * Think about what the PDE is doing
#
#    Using functions
#
#    Remember the lesson on writing functions with Python?  We will use that 
#    style of code in this exercise.
#
#    We're going to define two functions: 
#    * plot2d will plot our data in a 3D projection plot;
#    * laplace2d repeatedly updates the solution, stopping when the solution
#      is changing very little, as measured by the l1 norm.
#
#  Modified:
#
#    20 May 2016
#
#  Author:
#
#    Lorena Barba
#
import platform

print ( '' )
print ( 'STEP09:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 2D Laplace equation.' )

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
#  The function laplace2d takes five arguments:
#  * p matrix, 
#  * y-vector, 
#  * dx, 
#  * dy,
#  * the value l1norm_target. 
#
#  This last value defines how close the p matrix should be in two consecutive 
#  iterations before the loop breaks and returns the calculated p value.
#
def laplace2d ( p, y, dx, dy, l1norm_target ):
  l1norm = 1.0
# pn = numpy.empty_like ( p )

  while ( l1norm > l1norm_target ):
    pn = p.copy ( )
    p[1:-1,1:-1] = ( dy ** 2 * ( pn[1:-1,2:] + pn[1:-1,0:-2] ) \
                   + dx ** 2 * ( pn[2:,1:-1] + pn[0:-2,1:-1] ) ) \
                   / ( 2.0 * ( dx ** 2 + dy ** 2 ) ) 

    p[:,0] = 0.0
    p[:,-1] = y
    p[0,:] = p[1,:]
    p[-1,:] = p[-2,:]

    l1norm = ( numpy.sum ( numpy.abs ( p[:] ) - numpy.abs ( pn[:] ) ) ) \
             / numpy.sum ( numpy.abs ( pn[:] ) )
     
  return p
#
#  Variable declarations
#
nx = 61
ny = 31
dx = 2.0 / ( nx - 1 )
dy = 1.0 / ( ny - 1 )
#
#  Set the x and y coordinate vectors.
#
x = numpy.linspace ( 0.0, 2.0, nx )
y = numpy.linspace ( 0.0, 1.0, ny )
#
#  Initial condition for p.
#
p = numpy.zeros ( ( ny, nx ) )
p[:,0] = 0.0
p[:,-1] = y
p[0,:] = p[1,:]
p[-1,:] = p[-2,:]
#
#  Now let's try using our plot2D function to look at our initial conditions. 
#
plot2d ( x, y, p )
plt.savefig ( 'step09_initial' )
print ( '  Saved initial solution in file "step09_initial.png".' )
#
#  It worked!  This is the initial state of our problem, where the value of p
#  is zero everywhere except for along x=2 where p=y.  Now let's try to run our 
#  laplace2d function with a specified L1 target of 0.0001
#
p = laplace2d ( p, y, dx, dy, 1e-4 )
#
#  Now try plotting this new value of p with our plot function.
#
plot2d ( x, y, p )
plt.savefig ( 'step09_final' )
print ( '  Saved final solution in file "step09_final.png".' )
#
#  The next step will be to solve Poisson's equation.  Watch Video Lesson 11 on 
#  YouTube to understand why we need Poisson's equation in CFD.
#
#  And for a detailed walk-through of the discretization of Laplace and Poisson 
#  equations (steps 9 and 10), watch Video Lesson 12 on YouTube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP09:' )
print ( '  Normal end of execution.' )

