#! /usr/bin/env python3
#
# *****************************************************************************80
#
# STEP11 examines the 2D Navier-Stokes equations for the driven cavity.
#
#  Discussion:
#
#    The final two steps in this interactive module teaching beginning CFD
#    with Python will both solve the Navier-Stokes equations in two dimensions,
#    but with different boundary conditions.
#
#    Recall the Navier-Stokes equations for an incompressible fluid, letting
#    v represent the velocity vector, and p the pressure:
#
#      dv                      -1
#      -- + ( v dot del ) v =  --- del p + nu del^2 v
#      dt                      rho
#
#      del dot v = 0
#
#    Rewritten as a system of 3 scalar differential equations for (u,v) and p,
#    we have:
#
#      du     du     du   - 1 dp      ( d2 u   d2 u )
#      -- + u -- + v -- = --- -- + nu ( ---- + ---- )
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
#    From the previous steps, we already know how to discretize all these terms.
#    Only the last equation is a little unfamiliar.  But with a little patience,
#    it will not be hard!
#
#    Discretize the u-momentum equation, as follows:
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
#    Similarly for the v-momentum equation:
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
#    Finally, the discretized pressure-Poisson equation can be written thus:
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
#    You should write these equations down on your own notes, by hand,
#    following each term mentally as you write it.
#
#    As before, let's rearrange the equations in the way that the iterations
#    need to proceed in the code. First, the momentum equations for the
#    velocity at the next time step.
#
#    The momentum equation in the u direction:
#
#      u(n+1,i,j) = u(n,i,j)
#        - u(n,i,j) dt/dx ( u(n,i,j) - u(n,i-1,j)
#        - v(n,i,j) dt/dy ( u(n,i,j) - u(n,i,j-1)
#        - dt / ( 2 rho dx ) ( p(n,i+1,j) - p(n,i-1,j) )
#        + nu dt/dx^2 ( u(n,i+1,j) - 2 u(n,i,j) + u(n,i-1,j) )
#        + nu dt/dy^2 ( u(n,i,j+1) - 2 u(n,i,j) + u(n,i,j-1) )
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
#    Now, we rearrange the pressure-Poisson equation:
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
#      u = 1 at y = 2 (the "lid");
#      u = v = 0 on the other boundaries;
#      dpdy = 0 at y = 0;
#      p = 0 at y = 2
#      dpdx = 0 at x = 0 and x = 2
#
#  Modified:
#
#    25 May 2016
#
#  Author:
#
#    Lorena Barba
#
import platform

print('')
print('STEP11:')
print('  Python version: %s' % (platform.python_version()))
print('  The 2D Navier-Stokes equations for the driven cavity.')

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

nx = 41
ny = 41
nt = 500
nit = 50
dx = 2.0 / (nx - 1)
dy = 2.0 / (ny - 1)

rho = 1.0
nu = 0.1
dt = 0.001

x = numpy.linspace(0.0, 2.0, nx)
y = numpy.linspace(0.0, 2.0, ny)
X, Y = numpy.meshgrid(x, y)
#
#  The pressure Poisson equation (PPE) can be hard to write out without typos.
#  The function buildUpB below represents the contents of the
#  square brackets, so that the entirety of the PPE is slightly more manageable.
#


def buildUpB(b, rho, dt, u, v, dx, dy):

    b[1:-1, 1:-1] = rho * (1.0 / dt *
                           ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx)
                            + (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))
                           - ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx)) ** 2
                           - 2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy)
                                  * (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx))
                           - ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) ** 2)

    return b
#
#  The function presPoisson is defined to help segregate the different rounds of
#  calculations.  Note the presence of the pseudo-time variable nit.
#  This sub-iteration in the Poisson calculation helps ensure a divergence-free field.
#


def presPoisson(p, dx, dy, b):

    pn = numpy.empty_like(p)
    pn = p.copy()

    for q in range(nit):

        pn = p.copy()

        p[1:-1, 1:-1] = ((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy ** 2
                         + (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx ** 2) \
            / (2.0 * (dx ** 2 + dy ** 2)) \
            - dx ** 2 * dy ** 2 \
            / (2.0 * (dx ** 2 + dy ** 2)) * b[1:-1, 1:-1]

        p[:, -1] = p[:, -2]
        p[0, :] = p[1, :]
        p[:, 0] = p[:, 1]
        p[-1, :] = 0.0

        return p
#
#  Finally, the rest of the cavity flow equations are wrapped inside
#  the function cavityFlow, allowing us to easily plot the results
#  of the cavity flow solver for different lengths of time.
#


def cavityFlow(nt, u, v, dt, dx, dy, p, rho, nu):

    un = numpy.empty_like(u)
    vn = numpy.empty_like(v)
    b = numpy.zeros((ny, nx))

    for n in range(nt):

        un = u.copy()
        vn = v.copy()

        b = buildUpB(b, rho, dt, u, v, dx, dy)

        p = presPoisson(p, dx, dy, b)

        u[1:-1, 1:-1] = un[1:-1, 1:-1] \
            - un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) \
            - vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) \
            - dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2]) \
            + nu * (dt / dx ** 2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2])
                    + dt / dy ** 2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))

        v[1:-1, 1:-1] = vn[1:-1, 1:-1] \
            - un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) \
            - vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) \
            - dt / (2 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1]) \
            + nu * (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2])
                    + dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1]))

        u[0, :] = 0.0
        u[:, 0] = 0.0
        u[:, -1] = 0.0
        u[-1, :] = 1.0
        v[0, :] = 0.0
        v[-1, :] = 0.0
        v[:, 0] = 0.0
        v[:, -1] = 0.0

    return u, v, p


#
#  Let's start with nt = 100 and see what the solver gives us:
#
u = numpy.zeros((ny, nx))
v = numpy.zeros((ny, nx))
p = numpy.zeros((ny, nx))

nt = 100

u, v, p = cavityFlow(nt, u, v, dt, dx, dy, p, rho, nu)

fig = plt.figure(figsize=(11, 7), dpi=100)
plt.contourf(X, Y, p, alpha=0.5)
plt.colorbar()
plt.contour(X, Y, p)
plt.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2])
plt.xlabel('X')
plt.ylabel('Y')
#
#  Save the plot in a file.
#
plt.savefig('img/step11_100')
print('  Saved solution at 100 timesteps in file "step11_100.png".')
#
#  You can see that two distinct pressure zones are forming,
#  and that the spiral pattern expected from lid-driven cavity flow
#  is beginning to form.
#
#  Experiment with different values of nt to see how long the system takes to stabilize.
#
u = numpy.zeros((ny, nx))
v = numpy.zeros((ny, nx))
p = numpy.zeros((ny, nx))

nt = 700

u, v, p = cavityFlow(nt, u, v, dt, dx, dy, p, rho, nu)

fig = plt.figure(figsize=(11, 7), dpi=100)
plt.contourf(X, Y, p, alpha=0.5)
plt.colorbar()
plt.contour(X, Y, p)
plt.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2])
plt.xlabel('X')
plt.ylabel('Y')

plt.savefig('img/step11_700')
print('  Saved solution at 700 timesteps in file "step11_700.png".')
#
#  The interactive module 12 steps to Navier-Stokes is one of several components
#  of the Computational Fluid Dynamics class taught by Professor Lorena Barba
#  in Boston University between 2009 and 2013.
#
#  For a sample of what the other components of this class are, you can explore
#  the Resources section of the Spring 2013 version of the course's Piazza site.
#
#  Terminate.
#
print('')
print('STEP11:')
print('  Normal end of execution.')
