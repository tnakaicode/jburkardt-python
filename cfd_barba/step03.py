#! /usr/bin/env python3
#
# *****************************************************************************80
#
# STEP03 examines 1-D Diffusion.
#
#  Discussion:
#
#    The diffusion equation in one spatial dimension is:
#
#      du/dt = nu d2 u/dx2  [Diffusion Equation]
#
#    where nu is a physical quantity called the viscosity.
#
#    Unlike the linear and nonlinear convection equations that we considered
#    earlier, this equation involves a second-order derivative.  In order
#    to apply the finite difference method, we first need to learn how to
#    treat this term in the equation.
#
#    The second derivative can be represented geometrically as the line tangent
#    to the curve represented by the first derivative.  We will discretize
#    the second-order derivative with a Central Difference scheme: a
#    combination of Forward Difference and Backward Difference of the
#    first derivative.  Consider the Taylor expansion of u(i+1) and u(i-1)
#    around u(i):
#
#      u(i+1) = u(i) + dx du/dx + dx^2 d2udx2 + dx^3 d3udx3 + O(dx^4)  (Forward)
#      u(i-1) = u(i) - dx du/dx + dx^2 d2udx2 - dx^3 d3udx3 + O(dx^4)  (Backward)
#
#    where du/dx, d2udx2 and d3udx3 are the first, second and third derivatives
#    of u(x), evaluated at x(i), and O(dx^4) represents a remainder term which
#    is small like dx^4.
#
#    If we add the Forward and Backward expansions, you see that the terms
#    involving du/dx and d3udx3 exactly cancel out.  By subtracting 2 u(i)
#    from both sides and dividing by dx^2, we get the following:
#
#      u(i+1) - 2 u(i) + u(i-1)
#      ------------------------ = d2udx2 + O(dx^2)  (Exact Formula)
#               dx^2
#
#    Thus, the quantity on the left hand side is a reasonable approximation
#    to the second derivative, with an error that is small like dx^2.
#    To convert the diffusion equation into a discrete system, we will
#    replace the second derivative by our approximation, which is called
#    the second difference approximation:
#
#      u(i+1) - 2 u(i) + u(i-1)
#      ------------------------  [Second difference approximation to d2udx2]
#               dx^2
#
#    We can now write the discretized version of the diffusion equation in 1D:
#
#      u(i,n+1) - u(i,n)         u(i+1,n) - 2 u(i,n) + u(i-1,n)
#      ----------------- =  nu * ------------------------------
#              dt                          dx^2
#
#      [Discretized Diffusion Equation]
#
#    As before, we notice that once we have an initial condition, the only
#    unknown is u(i,n+1), so we re-arrange the equation to solving for this
#    unknown:
#
#      u(i,n+1) =  u(i,n) + nu * dt/dx^2 ( u(i+1,n) - 2 u(i,n) + u(i-1,n) )
#
#      [Discretized Diffusion Equation (rearranged)]
#
#    This discrete equation allows us to write a program to advance a solution
#    in time, starting from a given initial condition.
#
#    For our example, we'll continue to use a step function as the
#    initial condition.
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

print('')
print('STEP03:')
print('  Python version: %s' % (platform.python_version()))
print('  The 1D diffusion equation.')

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
matplotlib.use('Agg')
#
#  Now we import pyplot for graphics, and give it an abbreviated name.
#
import matplotlib.pyplot as plt
#
#  Define variables:
#  NU is the viscosity.
#  SIGMA is a computational variable we'll have to explain later.
#  It controls the size of the timestep.
#  NX is the number of equally spaced nodes or points in [0,2];
#  DX is the spacing between nodes;
#  NT is the number of time steps to calculate;
#  DT is the time step size;
#
nu = 0.3
sigma = 0.2
nx = 41
dx = 2.0 / (nx - 1)
nt = 20
dt = sigma * dx ** 2
#
#  Set the equally-spaced node locations.
#
x = numpy.linspace(0.0, 2.0, nx)
#
#  Set the initial condition as a step function.
#
u = numpy.ones(nx)
u[10:21] = 2.0
#
#  Carry out NT time steps.
#
for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx ** 2 * \
            (un[i + 1] - 2.0 * un[i] + un[i - 1])
#
#  Plot the solution at the final time.
#
plt.plot(x, u)
plt.savefig('img/step03_final')
print('  Saved final solution in file "step03_final.png".')
#
#  1) What do you notice immediately that is different about the final
#     solution of the diffusion equation, as compare to the final solution
#     of the linear or nonlinear convection equations?
#
#  For a careful walk-through of the discretization of the diffusion equation
#  with finite differences, watch Video Lesson 4 by Professor Barba on YouTube.
#
#  Terminate.
#
print('')
print('STEP03:')
print('  Normal end of execution.')

