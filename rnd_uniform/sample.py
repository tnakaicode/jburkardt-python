#
#    Licensing:
#
#    This code is distributed under the GNU LGPL license.
#

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from rnd_uniform.uniform import r8vec_uniform_01, r8mat_uniform_01, r8_uniform_01


def triangle01_sample(n, seed):

    #
    # TRIANGLE01_SAMPLE samples the interior of the unit triangle in 2D.
    #
    #  Reference:
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Krieger, 1992,
    #    ISBN: 0894647644,
    #    LC: QA298.R79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real XY(2,N), the points.
    #
    m = 2

    xy = np.zeros([m, n])
    for j in range(0, n):
        e, seed = r8vec_uniform_01(m + 1, seed)
        e = - np.log(e)
        d = np.sum(e)
        xy[0:2, j] = e[0:2] / d

    return xy, seed


def cube01_sample(n, seed):

    #
    # CUBE01_SAMPLE samples points in the unit cube in 3D.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(3,N), the points.
    #
    m = 3

    x, seed = r8mat_uniform_01(m, n, seed)

    return x, seed


def ball01_sample(n, seed):

    #
    # BALL01_SAMPLE uniformly samples the unit ball.
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Random Variate Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998, pages 168.
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Krieger, 1992,
    #    ISBN: 0894647644,
    #    LC: QA298.R79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(3,N), the points.
    #

    x = np.random.normal(0.0, 1.0, [3, n])
    for j in range(0, n):
        norm = np.sqrt(x[0, j] ** 2 + x[1, j] ** 2 + x[2, j] ** 2)
        for i in range(0, 3):
            x[i, j] = x[i, j] / norm

    for j in range(0, n):
        r = np.random.random()
        x[:, j] = x[:, j] * r ** (1.0 / 3.0)

    return x, seed


def annulus_sample(pc, r1, r2, n, seed):

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
    v, seed = r8vec_uniform_01(n, seed)

    theta = u * 2.0 * np.pi
    r = np.sqrt((1.0 - v) * r1**2 + v * r2**2)
    p = np.zeros([2, n])

    p[0, :] = pc[0] + r * np.cos(theta)
    p[1, :] = pc[1] + r * np.sin(theta)

    return p, seed


def circle01_sample_ergodic(n, angle):

    #
    # CIRCLE01_SAMPLE_ERGODIC samples points on the circumference of the unit circle in 2D.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, real ANGLE, an angle between 0 and 2 PI.
    #
    #    Output, real X(2,N), the points.
    #

    r = 1.0
    c = np.zeros(2)

    golden_ratio = (1.0 + np.sqrt(5.0)) / 2.0

    golden_angle = 2.0 * np.pi / golden_ratio ** 2

    x = np.zeros([2, n])

    for j in range(0, n):
        x[0, j] = c[0] + r * np.cos(angle)
        x[1, j] = c[1] + r * np.sin(angle)
        angle = np.mod(angle + golden_angle, 2.0 * np.pi)

    return x, angle


def circle01_sample_random(n, seed):

    #
    # CIRCLE01_SAMPLE_RANDOM samples points on the circumference of the unit circle in 2D.
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Random Variate Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998, pages 168.
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Krieger, 1992,
    #    ISBN: 0894647644,
    #    LC: QA298.R79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(2,N), the points.
    #

    r = 1.0
    c = np.zeros(2)

    theta, seed = r8vec_uniform_01(n, seed)

    x = np.zeros([2, n])

    for j in range(0, n):
        x[0, j] = c[0] + r * np.cos(2.0 * np.pi * theta[j])
        x[1, j] = c[1] + r * np.sin(2.0 * np.pi * theta[j])

    return x, seed


def hypercube01_sample(m, n, seed):

    # *****************************************************************************80
    #
    # HYPERCUBE01_SAMPLE samples points in the unit hypercube in M dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(M,N), the points.
    #
    x, seed = r8mat_uniform_01(m, n, seed)

    return x, seed
