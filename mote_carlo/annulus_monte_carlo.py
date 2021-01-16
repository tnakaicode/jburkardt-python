#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d
obj = plot2d()


def annulus_sample_test(center, r1, r2):

    # *****************************************************************************80
    #
    # ANNULUS_SAMPLE_TEST uses ANNULUS_SAMPLE to estimate integrals.
    #
    #  Discussion:
    #
    #    If CENTER=(0,0) and R1 = 0 and R2 = 1, then we can compare exact values.
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

    e_test = np.array([
        [0, 0],
        [2, 0],
        [0, 2],
        [4, 0],
        [2, 2],
        [0, 4],
        [3, 2],
        [6, 0]])

    print('')
    print('ANNULUS_SAMPLE_TEST')
    print('  ANNULUS_SAMPLE can sample an annulus uniformly.')
    print('  Use it to estimate integrals in the annulus')
    print('  centered at (%g,%g) with R1 = %g, R2 = %g'
          % (center[0], center[1], r1, r2))

    obj.create_tempdir(-1)
    seed = 123456789

    print('')
    txt = "\tN"
    for e in e_test:
        txt += "\t\tX^{:d} Y^{:d}".format(*e)
    print(txt)
    print('')

    n = 2**10
    data = []
    while (n <= 2**16):
        x, seed = annulus_sample(center, r1, r2, n, seed)
        dat = [n]
        print(' %8d' % (n), end='')
        for e in e_test:
            value = monomial_value(2, n, e, x)
            result = annulus_area(center, r1, r2) * np.sum(value[:]) / n
            print('\t%14.6g' % (result), end='')
            dat.append(result)

            obj.new_2Dfig()
            obj.contourf_tri(*x, value)
            obj.axs.scatter(*x, s=1.0, color="c")
            obj.axs.set_title("n={:d}".format(n))
            obj.axs.set_xlim(-r2 * 1.25 + center[0], r2 * 1.25 + center[0])
            obj.axs.set_ylim(-r2 * 1.25 + center[1], r2 * 1.25 + center[1])
            obj.SavePng_Serial()
            plt.close()

        data.append(np.array(dat))
        print('')

        obj.new_2Dfig()
        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.axs.set_xlim(-r2 * 1.25 + center[0], r2 * 1.25 + center[0])
        obj.axs.set_ylim(-r2 * 1.25 + center[1], r2 * 1.25 + center[1])
        obj.SavePng_Serial()
        plt.close()

        n = 2 * n

    data = np.array(data)
    obj.new_fig(aspect="auto")
    for i, e in enumerate(e_test):
        obj.axs.plot(data[:, 0], data[:, i])
        obj.axs.set_title(r"$x^{:d} y^{:d}$".format(*e))
        obj.SavePng_Serial()
        plt.close()
        obj.new_fig(aspect="auto")

    if (
            center[0] == 0.0 and
            center[1] == 0.0 and
            r1 == 0.0 and
            r2 == 1.0):
        print('')
        print('     Exact', end='')
        for i in range(0, 7):
            e = e_test[i, :]
            result = disk01_monomial_integral(e)
            print('  %14.6g' % (result), end='')
        print('')

    return


def annulus_area(center, r1, r2):

    # *****************************************************************************80
    #
    # ANNULUS_AREA computes the area of a circular annulus in 2D.
    #
    #  Discussion:
    #
    #    A circular annulus with center (XC,YC), inner radius R1 and
    #    outer radius R2, is the set of points (X,Y) so that
    #
    #      R1^2 <= (X-XC)^2 + (Y-YC)^2 <= R2^2
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
    #  Parameters:
    #
    #    Input, real CENTER(2), the coordinates of the center.
    #    This data is actually not necessary for area calculations.
    #
    #    Input, real R1, R2, the inner and outer radii of the annulus.
    #    0.0 <= R1 <= R2.
    #
    #    Output, real AREA, the area of the annulus.
    #
    import numpy as np
    from sys import exit

    if (r1 < 0.0):
        print('')
        print('ANNULUS_AREA - Fatal error!')
        print('  Inner radius R1 < 0.0.')
        exit('ANNULUS_AREA - Fatal error!')

    if (r2 < r1):
        print('')
        print('ANNULUS_AREA - Fatal error!')
        print('  Outer radius R1 < R1 = inner radius.')
        exit('ANNULUS_AREA - Fatal error!')

    area = np.pi * (r2 + r1) * (r2 - r1)

    return area


def annulus_area_test():

    # *****************************************************************************80
    #
    # ANNULUS_AREA_TEST test ANNULUS_AREA.
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
    import numpy as np

    print('')
    print('ANNULUS_AREA_TEST')
    print('  ANNULUS_AREA computes the area of an annulus with')
    print('  center = (CX,CY), inner radius R1 and outer radius R2.')

    seed = 123456789

    print('')
    print('  (   CX        CY     )    R1         R2         Area')
    print('')

    center = np.zeros(2)

    for i in range(0, 10):
        data, seed = r8vec_uniform_01(4, seed)
        center[0] = 10.0 * data[0] - 5.0
        center[1] = 10.0 * data[1] - 5.0
        r1 = data[2]
        r2 = r1 + data[3]
        area = annulus_area(center, r1, r2)
        print('  (%9.6f,%9.6f)  %9.6f  %9.6f  %9.6f'
              % (center[0], center[1], r1, r2, area))
    #
    #  Terminate.
    #
    print('')
    print('ANNULUS_AREA_TEST')
    print('  Normal end of execution.')
    return


def annulus_monte_carlo_test():

    # *****************************************************************************80
    #
    # ANNULUS_MONTE_CARLO_TEST tests ANNULUS_MONTE_CARLO.
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
    import numpy as np
    import platform

    print('')
    print('ANNULUS_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the ANNULUS_MONTE_CARLO library.')

    center = np.array([0.0, 0.0])
    r1 = 0.0
    r2 = 1.0
    annulus_sample_test(center, r1, r2)

    center = np.array([0.0, 0.0])
    r1 = 1.5
    r2 = 2.5
    annulus_sample_test(center, r1, r2)

    center = np.array([1.0, 0.0])
    r1 = 0.0
    r2 = 1.0
    annulus_sample_test(center, r1, r2)
    #
    #  Terminate.
    #
    print('')
    print('ANNULUS_MONTE_CARLO_TEST')
    print('  Normal end of execution.')
    return


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



def disk01_monomial_integral(e):

    # *****************************************************************************80
    #
    # DISK01_MONOMIAL_INTEGRAL returns monomial integrals in the unit disk.
    #
    #  Discussion:
    #
    #    The integration region is
    #
    #      X^2 + Y^2 <= 1.
    #
    #    The monomial is F(X,Y) = X^E(1) * Y^E(2).
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
    #  Parameters:
    #
    #    Input, integer E(2), the exponents of X and Y in the
    #    monomial.  Each exponent must be nonnegative.
    #
    #    Output, real INTEGRAL, the integral.
    #
    from scipy.special import gamma
    from sys import exit

    r = 1.0

    if (e[0] < 0 or e[1] < 0):
        print('')
        print('DISK01_MONOMIAL_INTEGRAL - Fatal error!')
        print('  All exponents must be nonnegative.')
        exit('DISK01_MONOMIAL_INTEGRAL - Fatal error!')

    if (((e[0] % 2) == 1) or ((e[1] % 2) == 1)):

        integral = 0.0

    else:

        integral = 2.0

        for i in range(0, 2):
            arg = 0.5 * float(e[i] + 1)
            integral = integral * gamma(arg)

        arg = 0.5 * float(e[0] + e[1] + 2)
        integral = integral / gamma(arg)
    #
    #  The surface integral is now adjusted to give the volume integral.
    #
    s = e[0] + e[1] + 2

    integral = integral * r ** s / float(s)

    return integral


def monomial_value(m, n, e, x):

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE evaluates a monomial.
    #
    #  Discussion:
    #
    #    This routine evaluates a monomial of the form
    #
    #      product ( 1 <= i <= m ) x(i)^e(i)
    #
    #    The combination 0.0^0, if encountered, is treated as 1.0.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, integer E(M), the exponents.
    #
    #    Input, real X(M,N), the point coordinates.
    #
    #    Output, real V(N), the monomial values.
    #
    import numpy as np

    v = np.ones(n)

    for i in range(0, m):
        if (0 != e[i]):
            for j in range(0, n):
                v[j] = v[j] * x[i, j] ** e[i]

    return v


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = np.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


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
    import time

    t = time.time()
    print(time.ctime(t))

    return None


if (__name__ == '__main__'):
    timestamp()
    annulus_monte_carlo_test()
    timestamp()
