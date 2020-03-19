import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from rnd_uniform.uniform import r8vec_uniform_01
from base import plot2d


def annulus_sample(pc, r1, r2, n, seed):

    # *****************************************************************************80
    #
    # ANNULUS_SAMPLE samples a circular annulus.
    #
    #  Discussion:
    #
    #    A circular annulus with center PC, inner radius R1 and
    #    outer radius R2, is the set of points P so that
    #
    #      R1^2 <= (P(1)-PC(1))^2 + (P(2)-PC(2))^2 <= R2^2
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Peter Shirley,
    #    Nonuniform Random Point Sets Via Warping,
    #    Graphics Gems, Volume III,
    #    edited by David Kirk,
    #    AP Professional, 1992,
    #    ISBN: 0122861663,
    #    LC: T385.G6973.
    #
    #  Parameters:
    #
    #    Input, real PC(2), the center.
    #
    #    Input, real R1, R2, the inner and outer radii.
    #    0.0 <= R1 <= R2.
    #
    #    Input, integer N, the number of points to generate.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real P(2,N), sample points.
    #
    import numpy as np
    from sys import exit

    if (r1 < 0.0):
        print('')
        print('ANNULUS_SAMPLE - Fatal error!')
        print('  Inner radius R1 < 0.0.')
        exit('ANNULUS_SAMPLE - Fatal error!')

    if (r2 < r1):
        print('')
        print('ANNULUS_SAMPLE - Fatal error!')
        print('  Outer radius R1 < R1 = inner radius.')
        exit('ANNULUS_SAMPLE - Fatal error!')

    u, seed = r8vec_uniform_01(n, seed)

    theta = u[:] * 2.0 * np.pi

    v, seed = r8vec_uniform_01(n, seed)

    r = np.sqrt((1.0 - v[:]) * r1 * r1
                + v[:] * r2 * r2)

    p = np.zeros([2, n])

    p[0, :] = pc[0] + r[:] * np.cos(theta[:])
    p[1, :] = pc[1] + r[:] * np.sin(theta[:])

    return p, seed


class MonteCarlo (plot2d):

    def __init__(self, aspect='equal'):
        plot2d.__init__(self, aspect=aspect)


if (__name__ == '__main__'):
    obj = MonteCarlo()
