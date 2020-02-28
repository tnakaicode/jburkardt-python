#! /usr/bin/env python3
#
#*****************************************************************************80
#
##  STEP02 examines 1-D Nonlinear Convection
#
#  Discussion:
#
#    This script continues the presentation of the 12 steps to Navier-Stokes, 
#    the practical module taught in the interactive CFD class of Professor 
#    Lorena Barba.  You should have completed Step 1 before continuing, having 
#    written your own Python script or notebook and having experimented with 
#    varying the parameters of the discretization and observing what happens.
#
#
#    Now we're going to implement non-linear convection by extending the methods 
#    used in step 1. The 1D linear convection equation is:
#      du/dt + c du/dx = 0  [1D Linear Convection Equation]
#    but now we replace the constant c by u, getting a nonlinear equation:
#      du/dt + u du/dx = 0  [1D Linear Convection Equation]
#
#    We're going to use the same discretization as in Step 1: forward 
#    difference in time and backward difference in space.  Here is the 
#    discretized equation:
#
#      u(i,n+1) - u(i,n)          u(i,n) - u(i-1,n)
#      ----------------- - u(i,n) ----------------- = 0  [Discrete Nonlinear Convection]
#              dt                        dx
#
#    Solving for the only unknown term, u(i,n), yields:
#
#      u(i,n+1) = u(i,n) - u(i,n) dt/dx ( u(i,n) - u(i-1,n) )  [Discrete Nonlinear Convection]
#
#    As before, the Python code starts by loading the necessary libraries. 
#    Then, we declare some variables that determine the discretization in space 
#    and time.  You should experiment by changing these parameters to see what 
#    happens.  Then, we create the initial condition u0 by initializing the 
#    array for the solution using the initial condition:
#      u0(x) = 2 if 0.5 <= x <= 1
#            = 1 otherwise.
#
#  Modified:
#
#    15 May 2016
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

print ( '' )
print ( 'STEP02:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  The 1D nonlinear convection equation.' )
#
#  Define variables:
#  NX is the number of equally spaced nodes or points in [0,2];
#  DX is the spacing between nodes;
#  NT is the number of time steps to calculate;
#  DT is the time step size;
#  
nx = 41
dx = 2.0 / ( nx - 1 )
nt = 20
dt = 0.025

x = numpy.linspace ( 0.0, 2.0, nx )
#
#  Set the initial condition as a step function.
#
u = numpy.ones ( nx )
u[10:21] = 2.0
#
#  Take NT time steps.

for n in range ( nt ):
  un = u.copy ( )
  for i in range ( 1, nx ):
    u[i] = un[i] - un[i] * dt / dx * ( un[i] - un[i-1] ) 
#
#  Plot the solution at the final time.
#
plt.plot ( x, u )
plt.savefig ( 'step02_final' )
print ( '  Saved final solution in file "step02_final.png".' )
#
#  What do you observe about the changes in the shape of the solution?
#
#  What happens when you change the numerical parameters?
#
#  For a careful walk-through of the discretization of the convection equation 
#  with finite differences and all steps from 1 to 4, watch Video Lesson 4 
#  by Professor Barba on YouTube.
#
#  Terminate.
#
print ( '' )
print ( 'STEP02:' )
print ( '  Normal end of execution.' )

