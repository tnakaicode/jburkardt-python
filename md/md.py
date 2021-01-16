#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from r8lib.r8mat_uniform_ab import r8mat_uniform_ab

obj = plot2d()


def md(d_num=3, p_num=10, step_num=2, dt=0.1):

    # *****************************************************************************80
    #
    # MD is the main program for the molecular dynamics simulation.
    #
    #  Discussion:
    #
    #    MD implements a simple molecular dynamics simulation.
    #
    #    The velocity Verlet time integration scheme is used.
    #
    #    The particles interact with a central pair potential.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer D_NUM, the spatial dimension.
    #    A value of 2 or 3 is usual.
    #    The default value is 3.
    #
    #    Input, integer P_NUM, the number of particles.
    #    A value of 1000 or 2000 is small but "reasonable".
    #    The default value is 500.
    #
    #    Input, integer STEP_NUM, the number of time steps.
    #    A value of 500 is a small but reasonable value.
    #    The default value is 500.
    #
    #    Input, real DT, the time step.
    #    A value of 0.1 is large; the system will begin to move quickly but the
    #    results will be less accurate.
    #    A value of 0.0001 is small, but the results will be more accurate.
    #    The default value is 0.1.
    #

    mass = 1.0
    #
    #  Report to the user.
    #
    print('')
    print('MD')
    print('  Python version: %s' % (platform.python_version()))
    print('  A molecular dynamics program.')
    print('')
    print('  D_NUM, the spatial dimension, is %d' % (d_num))
    print('  P_NUM, the number of particles in the simulation is %d.' % (p_num))
    print('  STEP_NUM, the number of time steps, is %d.' % (step_num))
    print('  DT, the time step size, is %g seconds.' % (dt))

    print('')
    print('  At each step, we report the potential and kinetic energies.')
    print('  The sum of these energies should be a constant.')
    print('  As an accuracy check, we also print the relative error')
    print('  in the total energy.')
    print('')
    print('      Step      Potential       Kinetic        (P+K-E0)/E0')
    print('                Energy P        Energy K       Relative Energy Error')
    print('')

    step_print_index = 0
    step_print_num = 10
    step_print = 0
    data = []
    for step in range(0, step_num + 1):

        if (step == 0):
            pos, vel, acc = initialize(p_num, d_num)
        else:
            pos, vel, acc = update(
                p_num, d_num, pos, vel, force, acc, mass, dt)

        force, potential, kinetic = compute(p_num, d_num, pos, vel, mass)

        if (step == 0):
            e0 = potential + kinetic

        rel = (potential + kinetic - e0) / e0
        if (step == step_print):
            print('  %8d  %14f  %14f  %14g' % (step, potential, kinetic, rel))
            step_print_index = step_print_index + 1
            step_print = (step_print_index * step_num) // step_print_num
        data.append(np.array([step, potential, kinetic, rel]))
    data = np.array(data)

    obj.new_2Dfig()
    obj.axs.plot(data[:, 0], data[:, 1])
    obj.SavePng(obj.rootname + "_potential.png")

    obj.new_2Dfig()
    obj.axs.plot(data[:, 0], data[:, 2])
    obj.SavePng(obj.rootname + "_kinetic.png")

    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(data[:, 0], data[:, 3])
    obj.SavePng(obj.rootname + "_rel.png")


def compute(p_num, d_num, pos, vel, mass):

    # *****************************************************************************80
    #
    # COMPUTE computes the forces and energies.
    #
    #  Discussion:
    #
    #    The potential function V(X) is a harmonic well which smoothly
    #    saturates to a maximum value at PI/2:
    #
    #      v(x) = ( sin ( min ( x, PI/2 ) ) )^2
    #
    #    The derivative of the potential is:
    #
    #      dv(x) = 2.0 * sin ( min ( x, PI/2 ) ) * cos ( min ( x, PI/2 ) )
    #            = sin ( 2.0 * min ( x, PI/2 ) )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer P_NUM, the number of particles.
    #
    #    Input, integer D_NUM, the number of spatial dimensions.
    #
    #    Input, real POS(D_NUM,P_NUM), the positions.
    #
    #    Input, real VEL(D_NUM,P_NUM), the velocities.
    #
    #    Input, real MASS, the mass of each particle.
    #
    #    Output, real FORCE(D_NUM,P_NUM), the forces.
    #
    #    Output, real POTENTIAL, the total potential energy.
    #
    #    Output, real KINETIC, the total kinetic energy.
    #

    force = np.zeros([d_num, p_num])
    rij = np.zeros(d_num)

    potential = 0.0

    for i in range(0, p_num):
        #
        #  Compute the potential energy and forces.
        #
        for j in range(0, p_num):

            if (i != j):
                #
                #  Compute RIJ, the displacement vector.
                #
                for k in range(0, d_num):
                    rij[k] = pos[k, i] - pos[k, j]
                #
                #  Compute D and D2, a distance and a truncated distance.
                #
                d = 0.0
                for k in range(0, d_num):
                    d = d + rij[k] ** 2
                d = np.sqrt(d)
                d2 = min(d, np.pi / 2.0)
                #
                #  Attribute half of the total potential energy to particle J.
                #
                potential = potential + 0.5 * np.sin(d2) * np.sin(d2)
                #
                #  Add particle J's contribution to the force on particle I.
                #
                for k in range(0, d_num):
                    force[k, i] = force[k, i] - rij[k] * np.sin(2.0 * d2) / d
    #
    #  Compute the kinetic energy.
    #
    kinetic = 0.0
    for k in range(0, d_num):
        for j in range(0, p_num):
            kinetic = kinetic + vel[k, j] ** 2

    kinetic = 0.5 * mass * kinetic

    return force, potential, kinetic


def initialize(p_num, d_num):

    # *****************************************************************************80
    #
    # INITIALIZE initializes the positions, velocities, and accelerations.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer P_NUM, the number of particles.
    #
    #    Input, integer D_NUM, the number of spatial dimensions.
    #
    #    Output, real POS(D_NUM,P_NUM), the positions.
    #
    #    Output, real VEL(D_NUM,P_NUM), the velocities.
    #
    #    Output, real ACC(D_NUM,P_NUM), the accelerations.
    #

    #
    #  Positions.
    #
    seed = 123456789
    pos, seed = r8mat_uniform_ab(d_num, p_num, 0.0, 10.0, seed)
    #
    #  Velocities.
    #
    vel = np.zeros([d_num, p_num])
    #
    #  Accelerations.
    #
    acc = np.zeros([d_num, p_num])

    return pos, vel, acc


def update(p_num, d_num, pos, vel, f, acc, mass, dt):

    # *****************************************************************************80
    #
    # UPDATE updates positions, velocities and accelerations.
    #
    #  Discussion:
    #
    #    The time integration is fully parallelizable.
    #
    #    A velocity Verlet algorithm is used for the updating.
    #
    #    x(t+dt) = x(t) + v(t) * dt + 0.5 * a(t) * dt * dt
    #    v(t+dt) = v(t) + 0.5 * ( a(t) + a(t+dt) ) * dt
    #    a(t+dt) = f(t) / m
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer P_NUM, the number of particles.
    #
    #    Input, integer D_NUM, the number of spatial dimensions.
    #
    #    Input, real POS(D_NUM,P_NUM), the positions.
    #
    #    Input, real VEL(D_NUM,P_NUM), the velocities.
    #
    #    Input, real F(D_NUM,P_NUM), the forces.
    #
    #    Input, real ACC(D_NUM,P_NUM), the accelerations.
    #
    #    Input, real MASS, the mass of each particle.
    #
    #    Input, real DT, the time step.
    #
    #    Output, real POS(D_NUM,P_NUM), the updated positions.
    #
    #    Output, real VEL(D_NUM,P_NUM), the updated velocities.
    #
    #    Output, real ACC(D_NUM,P_NUM), the updated accelerations.
    #
    rmass = 1.0 / mass
    #
    #  Update positions.
    #
    for i in range(0, d_num):
        for j in range(0, p_num):
            pos[i, j] = pos[i, j] + vel[i, j] * dt + 0.5 * acc[i, j] * dt * dt
    #
    #  Update velocities.
    #
    for i in range(0, d_num):
        for j in range(0, p_num):
            vel[i, j] = vel[i, j] + 0.5 * dt * (f[i, j] * rmass + acc[i, j])
    #
    #  Update accelerations.
    #
    for i in range(0, d_num):
        for j in range(0, p_num):
            acc[i, j] = f[i, j] * rmass

    return pos, vel, acc


def md_test():

    # *****************************************************************************80
    #
    # MD_TEST tests MD.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #

    print('')
    print('MD_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the MD molecular dynamics program.')

    d_num = 3
    p_num = 100
    step_num = 50
    dt = 0.1
    md(d_num, p_num, step_num, dt)

    print('')
    print('MD_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    md_test()
    timestamp()
