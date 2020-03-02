#! /usr/bin/env python3
#
# *****************************************************************************80
#
# STEP12 examines the 2D Navier-Stokes equations for channel flow.
#
#  Discussion:
#
#    Did you make it this far?  This is the last step!  How long did it take
#    you to write your own Navier-Stokes solver in Python following this
#    interactive module?
#
#    One difference between this final step and Step 11 is that we are going #
#    to add a source term to the u-momentum equation, to mimic the effect of a
#    pressure-driven channel flow.  Here are our modified Navier-Stokes
#    equations:
#
#      du     du     du   - 1 dp      ( d2 u   d2 u )
#      -- + u -- + v -- = --- -- + nu ( ---- + ---- ) + F(x,y)
#      dt     dx     dy   rho dx      ( dx2    dy2  )
#
#
#      dv     dv     dv   - 1 dp      ( d2 v   d2 v )
#      -- + u -- + v -- = --- -- + nu ( ---- + ---- )
#      dt     dx     dy   rho dy      ( dx2    dy2  )
#
#      d2 p   d2 p         ( du du     du dv   dv dv )
#      ---- + ---- = - rho ( -- -- + 2 -- -- + -- -- )
#      dx2    dy2          ( dx dx     dy dx   dy dy )
#
#    With patience and care, we write the discretized form of the equations.
#    It is highly recommended that you write these in your own hand, mentally
#    following each term as you write it.
#
#    The u-momentum equation:
#
#      u(n+1,i,j) - u(n,i,j)
#      ---------------------
#                dt
#
#                 u(n,i,j) - u(n,i-1,j)            u(n,i,j) - u(n,i,j-1)
#      + u(n,i,j) --------------------- + v(n,i,j) ---------------------
#                         dx                               dy
#
#         -1 p(n,i+1,j) - p(n,i-1,j)
#      = --- -----------------------
#        rho          2 dx
#
#           ( u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j)   u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1) )
#      + nu ( ------------------------------------ + ------------------------------------ )
#           (            dx^2                                   dy^2                      )
#
#      + f(i,j)
#
#    The v-momentum equation:
#
#      v(n+1,i,j) - v(n,i,j)
#      ---------------------
#                dt
#
#                 v(n,i,j) - v(n,i-1,j)            v(n,i,j) - v(n,i,j-1)
#      + u(n,i,j) --------------------- + v(n,i,j) ---------------------
#                         dx                               dy
#
#         -1 p(n,i+1,j) - p(n,i-1,j)
#      = --- -----------------------
#        rho          2 dy
#
#           ( v(n,i+1,j) - 2 v(n,i,j) + v(n,i-1,j)   v(n,i,j+1) - 2 v(n,i,j) + v(n,i,j-1) )
#      + nu ( ------------------------------------ + ------------------------------------ )
#           (            dx^2                                   dy^2                      )
#
#
#    And the pressure equation:
#
#      p(n,i+1,j) - 2 p(n,i,j) + p(n,i-1,j)   p(n,i,j+1) - 2 p(n,i,j) + p(n,i,j-1)
#      ------------------------------------ + ------------------------------------
#                       dx^2                                 dy^2
#
#            (  1 ( u(n,i+1,j) - u(n,i-1,j)   v(n,i,j+1) - v(n,i,j-1) )
#      = rho ( -- ------------------------- + ----------------------- )
#            ( dt            2 dx                      2 dy           )
#
#        u(n,i+1,j) - u(n,i-1,j)  u(n,i+1,j) - u(n,i-1,j)
#      - -----------------------  -----------------------
#               2 dx                     2 dx
#
#          u(n,i,j+1) - u(n,i,j-1)  v(n,i+1,j) - v(n,i-1,j)
#      - 2 -----------------------  -----------------------
#                   2 dy                    2 dx
#
#        v(n,i,j+1) - v(n,i,j-1)  v(n,i,j+1) - v(n,i,j-1)
#      - -----------------------  -----------------------
#               2 dy                     2 dy
#
#
#    As always, we re-arrange these equations to the form we need in the code
#    to make the iterations proceed.
#
#    The momentum equation in the u direction:
#
#      u(n+1,i,j) = u(n,i,j)
#        - u(n,i,j) dt/dx ( u(n,i,j) - u(n,i-1,j)
#        - v(n,i,j) dt/dy ( u(n,i,j) - u(n,i,j-1)
#        - dt / ( 2 rho dx ) ( p(n,i+1,j) - p(n,i-1,j) )
#        + nu dt/dx^2 ( u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j) )
#        + nu dt/dy^2 ( u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1) )
#        + dt * f(i,j)
#
#    The momentum equation in the v direction:
#
#      v(n+1,i,j) = v(n,i,j)
#        - u(n,i,j) dt/dx ( v(n,i,j) - v(n,i-1,j)
#        - v(n,i,j) dt/dy ( v(n,i,j) - v(n,i,j-1)
#        - dt / ( 2 rho dy ) ( p(n,i,j+1) - p(n,i,j-1) )
#        + nu dt/dx^2 ( v(n,i+1,j) - 2 v(n,i,j) + v(n,i-1,j) )
#        + nu dt/dy^2 ( v(n,i,j+1) - 2 v(n,i,j) + v(n,i,j-1) )
#
#    And for the pressure equation, we isolate the term p(n,i,j)
#    to iterate in pseudo-time:
#
#                 ( p(n,i+1,j) + p(n,i-1,j) ) dy^2 + ( p(n,i,j+1) + p(n,i,j-1) ) dx^2
#      p(n,i,j) = -------------------------------------------------------------------
#                                            2 ( dx^2 + dy^2 )
#
#             rho dx^2 dy^2
#        - -----------------
#          2 ( dx^2 + dy^2 )
#
#          [  1 ( u(n,i+1,j) - u(n,i-1,j)   v(n,i,j+1) - v(n,i,j-1) )
#        * [ -- ( ----------------------- + ----------------------- )
#          [ dt (          2 dx                      2 dy           )
#
#          - u(n,i+1,j) - u(n,i-1,j)  u(n,i+1,j) - u(n,i-1,j)
#            -----------------------  -----------------------
#                     2 dx                     2 dx
#
#              u(n,i,j+1) - u(n,i,j-1)  v(n,i+1,j) - v(n,i-1,j)
#          - 2 -----------------------  -----------------------
#                       2 dy                    2 dx
#
#            v(n,i,j+1) - v(n,i,j-1)  v(n,i,j+1) - v(n,i,j-1) ]
#          - -----------------------  ----------------------- ]
#                     2 dy                     2 dy           ]
#
#    The initial condition is u, v, p = 0 everywhere.
#
#    The boundary conditions are:
#
#    u, v, p are periodic at x = 0 and 2
#    u, v = 0 at y = 0 and 2
#    dpdy = 0 at y = 0 and 2
#    F(x,y) = 1 everywhere.
#
#  Modified:
#
#    26 May 2016
#
#  Author:
#
#    Lorena Barba
#
import numpy
import platform

print('')
print('STEP12:')
print('  Python version: %s' % (platform.python_version()))
print('  The 2D Navier-Stokes equations for channel flow.')
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
#  In step 11, we isolated a portion of our transposed equation to make it
#  easier to parse and we're going to do the same thing here.  One thing to
#  note is that we have periodic boundary conditions throughout this grid,
#  so we need to explicitly calculate the values at the leading and trailing
#  edge of our u vector.
#


def buildUpB(rho, dt, dx, dy, u, v):

    b = numpy.zeros_like(u)

    b[1:-1, 1:-1] = rho * (1.0 / dt *
                           ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx)
                            + (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))
                           - ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx)) ** 2
                           - 2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy)
                                  * (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx))
                           - ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) ** 2)
#
#  Periodic BC Pressure at x = 2
#
    b[1:-1, -1] = rho * (1.0 / dt *
                         ((u[1:-1, 0] - u[1:-1, -2]) / (2 * dx)
                          + (v[2:, -1] - v[0:-2, -1]) / (2 * dy))
                         - ((u[1:-1, 0] - u[1:-1, -2]) / (2 * dx)) ** 2
                         - 2 * ((u[2:, -1] - u[0:-2, -1]) / (2 * dy)
                                * (v[1:-1, 0] - v[1:-1, -2]) / (2 * dx))
                         - ((v[2:, -1] - v[0:-2, -1]) / (2 * dy)) ** 2)
#
#  Periodic BC Pressure at x = 0
#
    b[1:-1, 0] = rho * (1.0 / dt *
                        ((u[1:-1, 1] - u[1:-1, -1]) / (2 * dx)
                         + (v[2:, 0] - v[0:-2, 0]) / (2 * dy))
                        - ((u[1:-1, 1] - u[1:-1, -1]) / (2 * dx)) ** 2
                        - 2 * ((u[2:, 0] - u[0:-2, 0]) / (2 * dy) *
                               (v[1:-1, 1] - v[1:-1, -1]) / (2 * dx))
                        - ((v[2:, 0] - v[0:-2, 0]) / (2 * dy)) ** 2)

    return b
#
#  We'll also define a Pressure Poisson iterative function, again like we did
#  in Step 11.  Once more, note that we have to include the periodic boundary
#  conditions at the leading and trailing edge.  We also have to specify the
#  boundary conditions at the top and bottom of our grid.
#


def presPoissPeriodic(p, dx, dy):

    pn = numpy.empty_like(p)

    for q in range(nit):

        pn = p.copy()
        p[1:-1, 1:-1] = \
            ((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy ** 2
             + (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) \
            / (2 * (dx ** 2 + dy ** 2)) \
            - dx ** 2 * dy ** 2 / (2 * (dx ** 2 + dy ** 2)) * b[1:-1, 1:-1]
#
#  Periodic BC Pressure at x = 2
#
        p[1:-1, -1] = \
            ((pn[1:-1, 0] + pn[1:-1, -2]) * dy ** 2
             + (pn[2:, -1] + pn[0:-2, -1]) * dx ** 2) \
            / (2 * (dx ** 2 + dy ** 2)) \
            - dx ** 2 * dy ** 2 / (2 * (dx ** 2 + dy ** 2)) * b[1:-1, -1]
#
#  Periodic BC Pressure at x = 0
#
        p[1:-1, 0] = \
            ((pn[1:-1, 1] + pn[1:-1, -1]) * dy ** 2
             + (pn[2:, 0] + pn[0:-2, 0]) * dx ** 2) \
            / (2 * (dx ** 2 + dy ** 2)) \
            - dx ** 2 * dy ** 2 / (2 * (dx ** 2 + dy ** 2)) * b[1:-1, 0]
#
#  Wall boundary conditions, pressure
#
        p[-1, :] = p[-2, :]
        p[0, :] = p[1, :]

    return p


#
#  Now we have our familiar list of variables and initial conditions to declare before we start.
#
#  Problem variables.
#
nx = 41
ny = 41
nt = 10
nit = 50
rho = 1.0
nu = 0.1
F = 1.0
dt = 0.01

dx = 2.0 / (nx - 1)
dy = 2.0 / (ny - 1)

x = numpy.linspace(0.0, 2.0, nx)
y = numpy.linspace(0.0, 2.0, ny)
X, Y = numpy.meshgrid(x, y)
#
#  Initial conditions
#
u = numpy.zeros((ny, nx))
v = numpy.zeros((ny, nx))
p = numpy.ones((ny, nx))
#
#  For the meat of our computation, we're going to reach back to a trick
#  we used in Step 9 for Laplace's Equation.  We're interested in what our
#  grid will look like once we've reached a near-steady state.  We can either
#  specify a number of timesteps nt and increment it until we're satisfied
#  with the results, or we can tell our code to run until the difference
#  between two consecutive iterations is very small.
#
#  We also have to manage 8 separate boundary conditions for each iteration.
#  The code below writes each of them out explicitly. If you're interested
#  in a challenge, you can try to write a function which can handle some or
#  all of these boundary conditions. If you're interested in tackling that,
#  you should probably read up on Python dictionaries.
#
udiff = 1.0
stepcount = 0

while udiff > 0.001:

    un = u.copy()
    vn = v.copy()

    b = buildUpB(rho, dt, dx, dy, u, v)
    p = presPoissPeriodic(p, dx, dy)

    u[1:-1, 1:-1] = un[1:-1, 1:-1] \
        - un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) \
        - vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) \
        - dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2]) \
        + nu * (dt / dx ** 2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2])
                + dt / dy ** 2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])) \
        + F * dt

    v[1:-1, 1:-1] = vn[1:-1, 1:-1] \
        - un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) \
        - vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) \
        - dt / (2 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1]) \
        + nu * (dt / dx ** 2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2])
                + dt / dy ** 2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1]))
#
#  Periodic BC u at x = 2
#
    u[1:-1, -1] = un[1:-1, -1] \
        - un[1:-1, -1] * dt / dx * (un[1:-1, -1] - un[1:-1, -2]) \
        - vn[1:-1, -1] * dt / dy * (un[1:-1, -1] - un[0:-2, -1]) \
        - dt / (2 * rho * dx) * (p[1:-1, 0] - p[1:-1, -2]) \
        + nu * (dt / dx ** 2 * (un[1:-1, 0] - 2 * un[1:-1, -1] + un[1:-1, -2])
                + dt / dy ** 2 * (un[2:, -1] - 2 * un[1:-1, -1] + un[0:-2, -1])) \
        + F * dt
#
#  Periodic BC u at x = 0
#
    u[1:-1, 0] = un[1:-1, 0] \
        - un[1:-1, 0] * dt / dx * (un[1:-1, 0] - un[1:-1, -1]) \
        - vn[1:-1, 0] * dt / dy * (un[1:-1, 0] - un[0:-2, 0]) \
        - dt / (2 * rho * dx) * (p[1:-1, 1] - p[1:-1, -1]) \
        + nu * (dt / dx ** 2 * (un[1:-1, 1] - 2 * un[1:-1, 0] + un[1:-1, -1])
                + dt / dy ** 2 * (un[2:, 0] - 2 * un[1:-1, 0] + un[0:-2, 0])) \
        + F * dt
#
#  Periodic BC v at x = 2
#
    v[1:-1, -1] = vn[1:-1, -1] \
        - un[1:-1, -1] * dt / dx * (vn[1:-1, -1] - vn[1:-1, -2]) \
        - vn[1:-1, -1] * dt / dy * (vn[1:-1, -1] - vn[0:-2, -1]) \
        - dt / (2 * rho * dy) * (p[2:, -1] - p[0:-2, -1]) \
        + nu * (dt / dx ** 2 * (vn[1:-1, 0] - 2 * vn[1:-1, -1] + vn[1:-1, -2])
                + dt / dy ** 2 * (vn[2:, -1] - 2 * vn[1:-1, -1] + vn[0:-2, -1]))
#
#  Periodic BC v at x = 0
#
    v[1:-1, 0] = vn[1:-1, 0] \
        - un[1:-1, 0] * dt / dx * (vn[1:-1, 0] - vn[1:-1, -1]) \
        - vn[1:-1, 0] * dt / dy * (vn[1:-1, 0] - vn[0:-2, 0]) \
        - dt / (2 * rho * dy) * (p[2:, 0] - p[0:-2, 0]) \
        + nu * (dt / dx ** 2 * (vn[1:-1, 1] - 2 * vn[1:-1, 0] + vn[1:-1, -1])
                + dt / dy ** 2 * (vn[2:, 0] - 2 * vn[1:-1, 0] + vn[0:-2, 0]))
#
#  Wall BC: u,v = 0 at y = 0,2
#
    u[0, :] = 0.0
    u[-1, :] = 0.0
    v[0, :] = 0.0
    v[-1, :] = 0.0
#
#  The original calculation of UDIFF was wrong.
#
    udiff = numpy.sum(abs(u - un)) / numpy.sum(abs(u))
    stepcount = stepcount + 1
#
#  You can see that we've also included a variable stepcount to see how
#  many iterations our loop went through before our stop condition was met.
#
print('  Number of steps taken was %d' % (stepcount))
print('  Final UDIFF = %g' % (udiff))
#
#  If you want to see how the number of iterations increases as our udiff
#  condition gets smaller and smaller, try defining a function to perform
#  the while loop written above that takes an input udiff and outputs the
#  number of iterations that the function runs.
#
#  For now, let's look at our results. We've used the quiver function to
#  look at the cavity flow results and it works well for channel flow, too.
#
fig = plt.figure(figsize=(11, 7), dpi=100)
plt.quiver(X[::3, ::3], Y[::3, ::3], u[::3, ::3], v[::3, ::3])
#
#  Save the plot in a file.
#
plt.savefig('step12_trimmed')
print('  Saved solution in file "step12_trimmed.png".')
#
#  The structures in the quiver command that look like [::3, ::3] are useful
#  when dealing with large amounts of data that you want to visualize.
#  The one used above tells matplotlib to only plot every 3rd data point.
#  If we leave it out, you can see that the results can appear a little crowded.
#
fig = plt.figure(figsize=(11, 7), dpi=100)
plt.quiver(X, Y, u, v)
plt.savefig('step12_all')
print('  Saved solution in file "step12_all.png".')
#
#  What is the meaning of the F term?
#
#  Step 12 is an exercise demonstrating the problem of flow in a channel or
#  pipe. If you recall from your fluid mechanics class, a specified pressure
#  gradient is what drives Poiseuille flow.
#
#  Recall the x-momentum equation:
#    dudt + u del u = = dpdx + nu * ( d2u/dx2 + d2u/dy2 )
#
#  What we actually do in Step 12 is split the pressure into steady and
#  unsteady components p=P+p'. The applied steady pressure gradient is
#  the constant -dPdx=F (interpreted as a source term), and the unsteady
#  component is dp'/dx. So the pressure that we solve for in Step 12
#  is actually p', which for a steady flow is in fact equal to zero everywhere.
#
#  Why did we do this?
#
#  Note that we use periodic boundary conditions for this flow. For a flow
#  with a constant pressure gradient, the value of pressure on the left edge
#  of the domain must be different from the pressure at the right edge.
#  So we cannot apply periodic boundary conditions on the pressure directly.
#  It is easier to fix the gradient and then solve for the perturbations
#  in pressure.
#
#  Shouldn't we always expect a uniform/constant p' then?
#
#  That's true only in the case of steady laminar flows. At high Reynolds
#  numbers, flows in channels can become turbulent, and we will see unsteady
#  fluctuations in the pressure, which will result in non-zero values for p'.
#
#  In step 12, note that the pressure field itself is not constant, but it's
#  the pressure perturbation field that is. The pressure field varies linearly
#  along the channel with slope equal to the pressure gradient.  Also, for
#  incompressible flows, the absolute value of the pressure is inconsequential.
#
#  The interactive module 12 steps to Navier-Stokes is one of several
#  components of the Computational Fluid Dynamics class taught by Professor
#  Lorena Barba in Boston University between 2009 and 2013.
#
#  Terminate.
#
print('')
print('STEP12:')
print('  Normal end of execution.')
