#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc


class Brownian(plot2d):

    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #

    def __init__(self):
        plot2d.__init__(self)

        k = 40
        m = 2
        n = 1001
        d = 10.0
        t = 1.0
        pnt = self.brownian_motion_simulation(m, n, d, t)
        dsq = self.brownian_displacement_simulation(k, n, m, d, t)
        self.brownian_motion_display(m, n, pnt)
        self.brownian_displacement_display(k, n, m, d, t, dsq)

    def brownian_motion_simulation(self, m=2, n=1001, d=10.0, t=1.0):
        #
        #  BROWNIAN_MOTION_SIMULATION simulates Brownian motion.
        #
        #  Discussion:
        #
        #    Thanks to Feifei Xu for pointing out a missing factor of 2 in the
        #    stepsize calculation, 08 March 2016.
        #
        #    Thanks to Joerg Peter Pfannmoeller for pointing out a missing factor
        #    of M in the stepsize calculation, 23 April 2018.
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #    Input, integer N, the number of time steps to take, plus 1.
        #    Input, real D, the diffusion coefficient.
        #    Input, real T, the total time.
        #    Output, real X(M,N), the initial position at time 0.0, and
        #    the N-1 successive locations of the particle.
        #

        #  Set the time step.
        dt = t / float(n - 1)

        #  Compute the individual steps.
        x = np.zeros([m, n])
        for j in range(1, n):
            #  S is the stepsize
            s = np.sqrt(2.0 * m * d * dt) * np.random.randn(1)

            #  Direction is random.
            if (m == 1):
                dx = s * np.ones(1)
            else:
                dx = np.random.randn(m)
                norm_dx = np.sqrt(np.sum(dx ** 2))
                for i in range(0, m):
                    dx[i] = s * dx[i] / norm_dx

            #  Each position is the sum of the previous steps.
            x[0:m, j] = x[0:m, j - 1] + dx[0:m]

        return x

    def brownian_displacement_simulation(self, k=20, n=1001, m=2, d=10.0, t=1.0):
        #
        # BROWNIAN_DISPLACEMENT_SIMULATION simulates Brownian displacement.
        #
        #  Discussion:
        #
        #    Thanks to Feifei Xu for pointing out a missing factor of 2 in the
        #    stepsize calculation, 08 March 2016.
        #
        #    This function computes the square of the distance of the Brownian
        #    particle from the starting point, repeating this calculation
        #    several times.
        #
        #  Parameters:
        #
        #    Input, integer K, the number of repetitions.
        #    Input, integer N, the number of time steps to take, plus 1.
        #    Input, integer M, the spatial dimension.  Typically, this is 2.
        #    Input, real D, the diffusion coefficient.
        #       This might be 10.0.
        #       Computationally, this is simply a scale factor between time and space.
        #    Input, real T, the total time, which defaults to 1.0.
        #    Output, real DSQ(K,N), the displacements over time for each repetition.
        #    DSQ(:,1) is 0.0, because we include the displacement at the initial time.
        #

        dsq = np.zeros([k, n])
        for i in range(0, k):
            pnt = self.brownian_motion_simulation(m, n, d, t)
            dsq[i, 0:n] = np.sum(pnt[0:m, 0:n] ** 2, 0)

        return dsq

    def brownian_motion_display(self, m, n, x):
        #
        # BROWNIAN_MOTION_DISPLAY displays successive Brownian motion positions.
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #       M should be 1, 2 or 3.
        #    Input, integer N, the number of time steps.
        #    Input, real X(M,N), the particle positions.
        #
        
        self.new_2Dfig(aspect="auto")

        if (m == 1):
            filename = 'motion_' + str(m) + 'd.png'
            y = np.linspace(0, n - 1, n) / float(n - 1)
            self.axs.plot(x[0, :], y[:], 'b', linewidth=2)
            self.axs.plot(x[0, 0], y[0], 'g.', markersize=35)
            self.axs.plot(x[0, n - 1], y[n - 1], 'r.', markersize=35)
            self.axs.set_xlabel('<--X-->')
            self.axs.set_ylabel('<--Time-->')
            self.axs.set_title('Brownian motion simulation in 1D')
            self.SavePng(filename)
            
        elif (m == 2):
            filename = 'motion_' + str(m) + 'd.png'
            self.axs.plot(x[0, :], x[1, :], 'b', LineWidth=2)
            self.axs.plot(x[0, 0], x[1, 0], 'g.', markersize=35)
            self.axs.plot(x[0, n - 1], x[1, n - 1], 'r.', markersize=35)
            self.axs.set_xlabel('<--X-->')
            self.axs.set_ylabel('<--Y-->')
            self.axs.set_title('Brownian motion simulation in 2D')
            self.SavePng(filename)

        elif (m == 3):
            filename = 'motion_' + str(m) + 'd.png'
            self.new_3Dfig()
            self.axs.plot(x[0, :], x[1, :], x[2, :], 'b', linewidth=2)
            self.axs.scatter(x[0, 0], x[1, 0], x[2, 0], c='g', marker='o', s=100)
            self.axs.scatter(x[0, n - 1], x[1, n - 1],
                       x[2, n - 1], c='r', marker='o', s=100)
            self.axs.set_title('Brownian motion simulation in 3D')
            self.SavePng(filename)

        else:

            print('')
            print('BROWNIAN_MOTION_DISPLAY - Fatal error!')
            print('  Cannot display data except for M = 1, 2, 3.')
            exit('BROWNIAN_MOTION_DISPLAY - Fatal error!')

        print('')
        print('  Plot saved as "%s".' % (filename))

    def brownian_displacement_display(self, k, n, m, d, t, dsq):
        #
        # BROWNIAN_DISPLACEMENT_DISPLAY displays average Brownian motion displacement.
        #
        #  Discussion:
        #
        #    Thanks to Feifei Xu for pointing out a missing factor of 2 in the
        #    displacement calculation.
        #
        #  Parameters:
        #
        #    Input, integer K, the number of repetitions.
        #    Input, integer N, the number of time steps.
        #    Input, integer M, the spatial dimension.
        #    Input, real D, the diffusion coefficient.
        #    Input, real T, the total time.
        #    Input, real DSQ(K,N), the displacements over time for each repetition.
        #
        
        self.new_2Dfig(aspect="auto")

        #  Get the T values.
        tvec = np.linspace(0, t, n)

        #  Select 5 random trajectories for display.
        for s in range(0, 5):
            i = int(k * np.random.rand(1))
            self.axs.plot(tvec, dsq[i, :], 'b-')

        #  Display the average displacement.
        dsq_ave = np.sum(dsq, 0) / float(k)
        self.axs.plot(tvec, dsq_ave, 'r-', linewidth=2)

        #  Display the ideal displacment.
        dsq_ideal = 2.0 * m * d * tvec
        self.axs.plot(tvec, dsq_ideal, 'k-', linewidth=3)

        self.axs.set_xlabel('<--T-->')
        self.axs.set_ylabel('<--D^2-->')
        self.axs.set_title('Squared displacement (Red), Predicted (Black), Samples (Blue)')

        filename = 'displacement_' + str(m) + '.png'
        self.SavePng(filename)

        print('')
        print('  Plot saved as "%s".' % (filename))


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #

    t = time.time()
    print(time.ctime(t))


if (__name__ == '__main__'):
    timestamp()
    obj = Brownian()
    timestamp()
