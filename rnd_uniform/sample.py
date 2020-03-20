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
from rnd_uniform.uniform import r8vec_uniform_01, r8mat_uniform_01, r8_uniform_01, r8_normal_01, r8po_fa, r8po_sl, uniform_in_sphere01_map
from rnd_uniform.triangle import polygon_triangulate, triangle_area


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


def polygon_sample(v, n, seed):

    #
    # POLYGON_SAMPLE uniformly samples a polygon.
    #
    #  Parameters:
    #
    #    Input, integer NV, the number of vertices.
    #
    #    Input, real V(NV,2), the vertices of the polygon, listed in
    #    counterclockwise order.
    #
    #    Input, integer N, the number of points to create.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real S(2,N), the points.
    #
    #
    #  Triangulate the polygon.
    #

    nv, m = v.shape
    x = np.zeros(nv)
    y = np.zeros(nv)
    for j in range(0, nv):
        x[j] = v[j, 0]
        y[j] = v[j, 1]

    #
    #  Determine the areas of each triangle.
    #
    triangles = polygon_triangulate(nv, x, y)
    area_triangle = np.zeros(nv - 2)
    area_polygon = 0.0
    for i in range(0, nv - 2):
        area_triangle[i] = triangle_area(
            v[triangles[i, 0], 0], v[triangles[i, 0], 1],
            v[triangles[i, 1], 0], v[triangles[i, 1], 1],
            v[triangles[i, 2], 0], v[triangles[i, 2], 1])
        area_polygon = area_polygon + area_triangle[i]

    #
    #  Normalize the areas.
    #
    area_relative = np.zeros(nv - 1)
    for i in range(0, nv - 2):
        area_relative[i] = area_triangle[i] / area_polygon

    #
    #  Replace each area by the sum of itself and all previous ones.
    #
    area_cumulative = np.zeros(nv - 2)
    area_cumulative[0] = area_relative[0]
    for i in range(1, nv - 2):
        area_cumulative[i] = area_relative[i] + area_cumulative[i - 1]

    s = np.zeros([2, n])
    for j in range(0, n):
        #
        #  Choose triangle I at random, based on areas.
        #
        area_percent, seed = r8_uniform_01(seed)
        for k in range(0, nv - 2):
            i = k
            if (area_percent <= area_cumulative[k]):
                break

        #
        #  Now choose a point at random in triangle I.
        #
        r, seed = r8vec_uniform_01(2, seed)
        if (1.0 < r[0] + r[1]):
            r[0] = 1.0 - r[0]
            r[1] = 1.0 - r[1]

        s[0, j] = (1.0 - r[0] - r[1]) * v[triangles[i, 0], 0] \
            + r[0] * v[triangles[i, 1], 0] \
            + r[1] * v[triangles[i, 2], 0]

        s[1, j] = (1.0 - r[0] - r[1]) * v[triangles[i, 0], 1] \
            + r[0] * v[triangles[i, 1], 1] \
            + r[1] * v[triangles[i, 2], 1]

    return s, seed


def ellipsoid_sample(m, n, a, v, r, seed):

    #
    # ELLIPSOID_SAMPLE samples points uniformly from an ellipsoid.
    #
    #  Discussion:
    #
    #    The points X in the ellipsoid are described by a M by M
    #    positive definite symmetric matrix A, a "center" V, and
    #    a "radius" R, such that
    #
    #      (X-V)' * A * (X-V) <= R * R
    #
    #    The algorithm computes the Cholesky factorization of A:
    #
    #      A = U' * U.
    #
    #    A set of uniformly random points Y is generated, satisfying:
    #
    #      Y' * Y <= R * R.
    #
    #    The appropriate points in the ellipsoid are found by solving
    #
    #      U * X = Y
    #      X = X + V
    #
    #    Thanks to Dr Karl-Heinz Keil for pointing out that the original
    #    coding was actually correct only if A was replaced by its inverse.
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
    #    Input, integer M, the dimension of the space.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real A(M,M), the matrix that describes
    #    the ellipsoid.
    #
    #    Input, real V(M), the "center" of the ellipsoid.
    #
    #    Input, real R, the "radius" of the ellipsoid.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(M,N), the points.
    #
    import numpy as np
    #
    #  Get the Cholesky factor U.
    #
    u = r8po_fa(m, a)
    #
    #  Get the points Y that satisfy Y' * Y <= 1.
    #
    y, seed = uniform_in_sphere01_map(m, n, seed)
    #
    #  Get the points Y that satisfy Y' * Y <= R * R.
    #
    y = r * y
    #
    #  Solve U * X = Y.
    #
    x = np.zeros([m, n])
    sol = np.zeros(m)
    rhs = np.zeros(m)

    for j in range(0, n):
        rhs[0:m] = y[0:m, j]
        sol = r8po_sl(m, u, rhs)
        x[0:m, j] = sol[0:m]
        #
        #  X = X + V.
        #
    for i in range(0, m):
        x[i, 0:n] = x[i, 0:n] + v[i]

    return x, seed
