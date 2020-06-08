#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP04 examines the 1-D Burgers equation.
#
#  Discussion:
#
#    You can read about the Burgers Equation on its Wikipedia page.
#
#    In 1D, the Burgers equation looks like this:
#
#      du/dt + u du/dx = nu * d2u/dx2  [The Burgers Equation]
#
#    As you can see, it is a combination of non-linear convection (the
#    u * du/dx term) and diffusion (the nu * d2u/dx2 term). 
#    It is surprising how much you can learn from this neat little equation,
#    which is a simplified relative of the Navier-Stokes equations we will
#    be considering later!
#
#    We can discretize the equation by using the methods we've already 
#    detailed in Steps 1 to 3. Using forward difference for time, backward
#    difference for space and our second-order method for the second 
#    derivatives yields:
#
#      u(i,n+1) - u(i,n)          u(i,n) - u(i-1,n)      u(i+1,n) - 2 u(i,n) + u(i-1,n)
#      ----------------- + u(i,n) ----------------- = nu ------------------------------
#              dt                        dx                           dx^2
#
#      [The discrete Burgers Equation]
#
#    As before, once we have an initial condition, the only unknown is u(i,n+1).
#
#    By rearranging the equation so that the unknown u(i,n+1) is alone on the
#    left hand side, we now have a formula that will allow us to step forward
#    in time as follows:
#
#      u(i,n+1) = u(i,n) - dt/dx * ( u(i,n) - u(i-1,n) 
#               + nu dt/dx^2 ( u(i+1,n) - 2 u(i,n) + u(i-1,n) )
#
#      [The discrete Burgers Equation rewritten for computation]
#
#    To examine some interesting properties of the Burgers equation, it is 
#    helpful to use different initial and boundary conditions than we've 
#    been using for previous steps.
#
#    First, we define the helper function phi(x,t) by:
#      phi(x,t) = exp ( - ( x - 4 t        )^2 / ( 4 * nu * ( t + 1 ) ) 
#               + exp ( - ( x - 4 t - 2 pi )^2 / ( 4 * nu * ( t + 1 ) )
#
#    Then our initial condition for this problem is going to be:
#      u0(x) = - 2 ( nu / phi(x,0) ) d phi/dx + 4
#
#    Our boundary conditions will be:
#      u(0,t) = u(2*pi,t)
#
#    This is called a periodic boundary condition.  Pay attention!  This will 
#    cause you a bit of headache if you don't work with it properly.
#
#    With these initial and boundary conditions, the Burgers equation has 
#    an exact solution, given by:
#
#      u(x,t) = - 2 ( nu / phi(x,t) ) d phi/dx + 4
#
#    The initial condition we're using can be a bit of a pain to evaluate by 
#    hand. The derivative d phi/dx isn't too terribly difficult, but it would 
#    be easy to drop a sign or forget a factor of x somewhere, so we're going 
#    to use SymPy to help us out.
#
#    SymPy is the symbolic math library for Python.  It has a lot of the same 
#    symbolic math functionality as Mathematica, with the added benefit that 
#    we can easily translate its results back into our Python calculations,
#    as though we had patiently computed the derivative and typed in the
#    formula ourselves.
#
#  Modified:
#
#    17 May 2016
#
#  Author:
#
#    Lorena Barba
#
import numpy
import matplotlib
#
#  We aren't issuing commands interactively.  So we want the graphics to
#  go to a png file, not to the screen.  To do this, we have to request
#  the noninteractive graphics backend called 'Agg'.
#
matplotlib.use ( 'Agg' )
import matplotlib.pyplot as plt
import platform
import sympy
from sympy import init_printing

init_printing ( use_latex = True )

print ( '' )
print ( 'STEP04:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 1D Burgers equation.' )
#
#  Start by setting up symbolic variables for the three variables in our 
#  initial condition.
#
x, nu, t = sympy.symbols('x nu t')
#
#  Type out the full equation for phi.
#
phi = sympy.exp ( - ( x - 4 * t                ) ** 2 / ( 4 * nu * ( t + 1 ) ) ) \
    + sympy.exp ( - ( x - 4 * t - 2 * numpy.pi ) ** 2 / ( 4 * nu * ( t + 1 ) ) )
#
#  Ask SymPy to repeat what we just said, but pretty.
#
phi
#
#  Now we can ask SymPy to evaluate our partial derivative d phi/dx:
#
phiprime = phi.diff ( x )
#
#  And we can ask SymPy to print the formula.
#
phiprime
#
#  To see the unrendered (ugly) version, just use the Python print command.
#
print ( phiprime )
#
#  Now that we have the Pythonic version of our derivative phiprime, we can 
#  write out the full initial condition and then translate it into a 
#  usable Python expression. 
#
u = -2*nu*(phiprime/phi)+4
print ( u )
# 
#  To convert the symbolic expression into Python code, we import lambdify.
#
from sympy.utilities.lambdify import lambdify
#
#  To lambdify the expression, we tell lambdify 
#  * the name of the Python function to create;
#  * the variables which are input to the function;
#  * the SymPy formula which the function is to evaluate.
#
ufunc = lambdify ( ( t, x, nu ), u )
#
#  ufunc is now a Python function.  We can evaluate it by passing
#  in values of t, x, and nu, as in this example:
#
print ( ufunc ( 1.0, 4.0, 3.0 ) )
#
#  Now we can finish setting up the problem. 
#
#  Define some problem variables
#
nx = 101
nt = 100
dx = 2.0 * numpy.pi / ( nx - 1 )
nu = 0.07
dt = dx * nu
#
#  Define our nx equally spaced nodes over [0,2 pi]:
#
x = numpy.linspace ( 0.0, 2.0 * numpy.pi, nx )
#
#  We define out initial condition using our lambdify-ed function ufunc.
#
t = 0.0
u = numpy.asarray ( [ ufunc ( t, xi, nu ) for xi in x ] )
#
#  Let's see what the result is:
#
u
#
#  Plot the initial condition.
#
plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
plt.plot ( x, u, marker = 'o', lw = 2 )
plt.xlim ( [ 0, 2*numpy.pi ] )
plt.ylim ( [ 0, 10 ] );
#
#  Save a copy of the plot in a file.
#
plt.savefig ( 'img/step04_initial' )
print ( '  Saved initial solution in file "step04_final.png".' )
#
#  This is definitely not the step function we've been dealing with until now. 
#  We call it a "saw-tooth function". 
#  Let's proceed forward and see what happens.
#
#  Periodic Boundary Conditions
#
#  One of the big differences between Step 4 and the previous lessons is the 
#  use of periodic boundary conditions. 
#
#  If you experiment with Steps 1 and 2 and make the simulation run longer,
#  by increasing nt, you will notice that the wave will keep moving to the 
#  right until it no longer even shows up in the plot.
#
#  But with periodic boundary conditions, if a wave travels to the right-hand 
#  side of the frame, then it will reappear on the left hand side of the
#  frame, as though the region wraps around.
#
#  Recall the discretization that we worked out earlier:
#
#    u(i,n+1) = u(i,n) - dt/dx * ( u(i,n) - u(i-1,n) 
#             + nu dt/dx^2 ( u(i+1,n) - 2 u(i,n) + u(i-1,n) )
#
#  What should u(i+1,n) mean when i is already at the end of the frame?
#  Think about this for a minute before proceeding.
#
for n in range ( nt ):
  un = u.copy ( )

  u[0] = un[0] - un[0] * dt/dx * ( un[0] - un[nx-1] ) \
    + nu * dt / dx ** 2 * ( un[1] - 2 * un[0] + un[nx-1] )

  for i in range ( 1, nx - 1 ):
    u[i] = un[i] - un[i] * dt / dx * ( un[i] - un[i-1] ) \
      + nu * dt / dx ** 2 * ( un[i+1] - 2 * un[i] + un[i-1] )

  u[nx-1] = un[nx-1] - un[nx-1] * dt / dx * ( un[nx-1] - un[nx-2] ) \
    + nu * dt / dx ** 2 * ( un[0] - 2 * un[nx-1] + un[nx-2] )
#
#  Evaluate the exact solution at time nt * dt, at each node.
#
u_analytical = numpy.asarray ( [ ufunc ( nt * dt, xi, nu ) for xi in x ] )
#
#  Plot exact and computed solutions together for comparison.
#
plt.figure ( figsize = ( 11, 7 ), dpi = 100 )
plt.plot ( x, u, marker = 'o', lw = 2, label = 'Computational' )
plt.plot ( x, u_analytical, label = 'Analytical' )
plt.xlim ( [ 0.0, 2 * numpy.pi ] )
plt.ylim ( [ 0, 10 ] )
plt.legend ( );
#
#  Save a copy of the plot.
#
plt.savefig ( 'img/step04_final' )
print ( '  Saved final solution in file "step04_final.png".' )
#
#  What next?
#
#  The subsequent steps, from 5 to 12, will be in two dimensions. 
#
#  We will find that it is easy to extend the 1D finite-difference formulas 
#  to partial derivatives in 2D or 3D. 
#  Just apply the definition - a partial derivative with respect to x is 
#  the variation in the x direction while keeping y constant.
#
#  Before moving on to Step 5, make sure you have completed your own code 
#  for steps 1 through 4 and you have experimented with the parameters 
#  and thought about what is happening. 
#
#  Also, we recommend that you take a slight break to learn about 
#  array operations with NumPy, because arrays will become more prominent
#  as we move to the 2D problems.
#
#  Terminate.
#
print ( '' )
print ( 'STEP04:' )
print ( '  Normal end of execution.' )


