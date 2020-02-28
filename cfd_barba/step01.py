#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP01 examines 1-D Linear Convection
#
#  Discussion:
#
#    This script will lead you through the first step of programming 
#    your own Navier-Stokes solver in Python from the ground up.  We're going to 
#    dive right in.  Don't worry if you don't understand everything that's 
#    happening at first, we'll cover it in detail as we move forward and you 
#    can support your learning with the videos of Prof. Barba's lectures 
#    on YouTube.
#
#    The 1-D Linear Convection equation is the simplest, most basic model that 
#    can be used to learn something about CFD.  It is surprising that this 
#    little equation can teach us so much!  Here it is:
#
#      du/dt + c du/dx = 0  [1D Linear Convection Equation]
#
#    With given initial conditions (understood as a wave), the equation 
#    represents the propagation of that initial wave with speed c, without 
#    change of shape.  Let the initial condition be 
#
#      u(x,0) = u0(x).  [Initial Condition]
#
#    Then the exact solution of the equation is 
#
#      u(x,t) = u0(x-ct)  [Exact Solution]
#
#    We discretize this equation in both space and time, using the Forward 
#    Difference scheme for the time derivative and the Backward Difference 
#    scheme for the space derivative.  Consider discretizing the spatial 
#    coordinate x into points that we index from i=0 to N, and stepping in 
#    discrete time intervals of size dt.
#
#    From the definition of a derivative (and simply removing the limit), 
#    we know that it is approximately true that:
#
#      du/dx = ( u(x+dx) - u(x) ) / dx  [Forward Difference Approximation]
#
#    Our discrete equation, then, is:
#
#      u(i,n+1) - u(i,n)     u(i,n) - u(i-1,n)
#      ----------------- - c ----------------- = 0  [Discrete Convection]
#              dt                  dx
#
#    where n and n+1 are two consecutive steps in time, while i-1 and i
#    are two neighboring points in the discretized x coordinate.  If there
#    are given initial conditions, then the onlhy unknown in this discretization
#    is u(i,n+1).  We can solve for our unknown to get an equation that
#    allows us to advance in time, as follows:
#
#      u(i,n+1) = u(i,n) - c dt/dx ( u(i,n) - u(i-1,n) )  [Discrete Convection]
#
#    Now let's try implementing this in Python.
#
#    We'll start by importing a few libraries to help us out:
#
#    * numpy is a library that provides a bunch of useful matrix operations 
#      akin to MATLAB.
#    * matplotlib is a 2D plotting library that we will use to plot our results.
#
#    Remember: comments in python are denoted by the pound sign
#
#  Modified:
#
#    15 May 2016
#
#  Author:
#
#    Lorena Barba
#
import platform

print ( '' )
print ( 'STEP01:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 1D linear convection equation.' )
#
#  Load the numpy library:
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
#  Now we import pyplot for graphics, and give it an abbreviated name.
#
import matplotlib.pyplot as plt
#
#  Now let's define a few variables; 
#
#  We want to define an evenly spaced grid of points within a spatial domain 
#  that is 2 units of length wide, i.e., x(i) is in (0,2).  We'll define: 
#  * nx, the number of grid points we want;
#  * dx will be the distance between any pair of adjacent grid points.
#  * nt will be the number of time steps we want to take.
#  * dt will be the time step.
#  * c will be the wave speed.
#
nx = 41
dx = 2.0 / ( nx - 1 )
nt = 25
dt = 0.025
c = 1.0
#
#  We can create an array x of nx equally spaced points between 0 and 2
#  by using the numpy function linspace():
#
x = numpy.linspace ( 0.0, 2.0, nx )
#
#  Our initial condition U0 is 2.0 between 0.5 and 1, and 1.0 elsewhere.
#
#  The numpy command ones() can create a list of the right size, full of
#  the value 1.0.
#
u = numpy.ones ( nx )
#
#  The U values that need to be reset to 2 have indices between
#  0.5/dx and 1.0/dx.  We can change all the values of an array
#  between a lower and upper index using the colon notation.
#  In Python, to go from index i to index j, we have to write i:j+1.
#
u[10:21] = 2.0
#
#  Now let's take a look at those initial conditions using a Matplotlib plot. 
#
plt.plot ( x, u )
#
#  Save this plot in a file called 'step01_initial.png'
#
plt.savefig ( 'step01_initial' )
print ( '  Saved initial condition in file "step01_initial.png".' )
#
#  Now it's time to implement the discretization of the convection equation 
#  using a finite-difference scheme.
#
#  For every element of our array u, we need to perform the operation 
#    u(n+1,i) = u(n,i) - c dt / dx ( u(n,i) - u(n,i-1) )
#  Using the python "copy" function, we'll copy the current solution u
#  into a temporary array un, which will allow us to fill up u with the
#  values at the next time step.  
#
#  We will repeat this operation for as many time-steps as we specify 
#  and then we can see how far the wave has convected.
#
#  We may think we have two iterative operations: one in space and 
#  one in time (we'll learn differently later), so we'll start by nesting 
#  one loop inside the other.  
#
#  Note the use of the nifty range() function:
#    range ( nt ) means go from 0 to nt - 1.
#    range ( 1, nx ) means go from 1 to nx - 1.
#
for n in range ( nt ):
  un = u.copy ( )
  for i in range ( 1, nx ):
    u[i] = un[i] - c * dt / dx * ( un[i] - un[i-1] )
#
#  We will learn later that the code as written above is quite inefficient, 
#  and there are better ways to write this, Python-style.
#
#  Now let's try plotting our u array after advancing in time.
#  Because we haven't cleared the plot window, we will see both the
#  initial and final solutions.  
#
#  But actually, that's good, because there is an interesting 
#  comparison to make.
#  
plt.plot ( numpy.linspace ( 0, 2, nx ), u );
#
#  Save this plot in a file called 'step01_final.png'
#
plt.savefig ( 'step01_final' )
print ( '  Saved final solution in file "step01_final.png".' )
#
#  OK! So our function has definitely moved to the right, but its shape 
#  has changed.  
#
#  1) The exact initial condition is a step function.  When we plot our
#     computational initial condition, the jumps up and down are not
#     exactly vertical, but are slightly sloped.  Why?
#
#  2) If you plot the exact solution of the convection equation, its shape
#     stays the same as it moves to the right.  So is there an error in our
#     code?
#
#  3) What happens if you rerun this problem, but change nx from 41 to 81?
#
#  4) Change the statement in the double loop from:
#       for i in range(1,nx):
#     to
#       for i in range(nx):
#     What happens?  Why?
#
#  5) In our discussion, the discrete solution u was a two-dimensional
#     array, with a typical entry being u(i,n).  But in the program, we
#     use a one dimensional vector u, plus a temporary vector un.  Is there
#     an advantage to doing this?
#
#  For a more thorough explanation of the finite-difference method, including 
#  topics like the truncation error, order of convergence and other details, 
#  watch Video Lessons 2 and 3 by Prof. Barba on YouTube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP01:' )
print ( '  Normal end of execution.' )

