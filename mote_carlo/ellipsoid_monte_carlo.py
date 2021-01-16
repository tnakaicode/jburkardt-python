#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d, plot3d
obj = plot3d()


def ellipsoid_monte_carlo_test01():

    # *****************************************************************************80
    #
    # ELLIPSOID_MONTE_CARLO_TEST01 uses ELLIPSOID_SAMPLE on a 2D ellipse centered at (0,0).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 2

    a = np.array([
        [9.0, 1.0],
        [1.0, 4.0]])

    e_test = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [2, 0],
        [1, 1],
        [0, 2],
        [3, 0]])

    r = 2.0
    v = np.array([0.0, 0.0])

    print('')
    print('ELLIPSOID_MONTE_CARLO_TEST01')
    print('  Use ELLIPSOID_SAMPLE to estimate integrals')
    print('  in a 2D ellipse x'' * A * x <= r^2.')

    print('')
    print('  Ellipsoid radius R = %g' % (r))
    r8vec_print(m, v, '  Ellipsoid center V:')
    r8mat_print(m, m, a, '  Ellipsoid matrix A:')

    volume = ellipsoid_volume(m, a, v, r)
    print('')
    print('  Ellipsoid volume = %g' % (volume))
    print('')
    print('         N        1              X               Y               X^2               XY             Y^2             X^3')
    print('')

    obj.create_tempdir(-1)

    seed = 123456789
    n = 2**5
    while (n <= 2**14):
        x, seed = ellipsoid_sample(m, n, a, v, r, seed)
        print('  %8d' % (n), end='')
        for j in range(0, 7):
            e = e_test[j]
            value = monomial_value(m, n, e, x)
            result = volume * np.sum(value[0:n]) / float(n)
            print('  %14.6g' % (result), end='')
        print('')

        obj.new_2Dfig()
        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial()
        plt.close()

        n = 2 * n
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_MONTE_CARLO_TEST01')
    print('  Normal end of execution.')
    return


def ellipsoid_monte_carlo_test02():

    # *****************************************************************************80
    #
    # ELLIPSOID_MONTE_CARLO_TEST02 uses ELLIPSOID_SAMPLE on a 2D ellipse centered at (2,3).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 2

    a = np.array([
        [9.0, 1.0],
        [1.0, 4.0]])

    e_test = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [2, 0],
        [1, 1],
        [0, 2],
        [3, 0]])

    r = 0.5

    v = np.array([2.0, 3.0])

    print('')
    print('ELLIPSOID_MONTE_CARLO_TEST02')
    print('  Use ELLIPSOID_SAMPLE to estimate integrals')
    print('  in a 2D ellipse (x-v)'' * A * (x-v) <= r^2.')

    print('')
    print('  Ellipsoid radius R = %g' % (r))
    r8vec_print(m, v, '  Ellipsoid center V:')
    r8mat_print(m, m, a, '  Ellipsoid matrix A:')

    volume = ellipsoid_volume(m, a, v, r)
    print('')
    print('  Ellipsoid volume = %g' % (volume))

    seed = 123456789

    print('')
    print('         N        1              X               Y               X^2               XY             Y^2             X^3')
    print('')

    n = 1
    while (n <= 65536):
        x, seed = ellipsoid_sample(m, n, a, v, r, seed)
        print('  %8d' % (n), end='')
        for j in range(0, 7):
            e = e_test[j]
            value = monomial_value(m, n, e, x)
            result = volume * np.sum(value[0:n]) / float(n)
            print('  %14.6g' % (result), end='')
        print('')

        obj.new_2Dfig()
        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial()
        plt.close()

        n = 2 * n
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_MONTE_CARLO_TEST02')
    print('  Normal end of execution.')
    return


def ellipsoid_monte_carlo_test03():

    # *****************************************************************************80
    #
    # ELLIPSOID_MONTE_CARLO_TEST03 uses ELLIPSOID_SAMPLE on a 3D ellipse centered at (1,2,3).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 3

    a = np.array([
        [9.0, 6.0, 3.0],
        [6.0, 5.0, 4.0],
        [3.0, 4.0, 9.0]])

    e_test = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 2],
        [0, 0, 3]])

    r = 0.5

    v = np.array([1.0, 2.0, 3.0])

    print('')
    print('ELLIPSOID_MONTE_CARLO_TEST03')
    print('  Use ELLIPSOID_SAMPLE to estimate integrals')
    print('  in a 3D ellipse (x-v)'' * A * (x-v) <= r^2.')

    print('')
    print('  Ellipsoid radius R = %g' % (r))
    r8vec_print(m, v, '  Ellipsoid center V:')
    r8mat_print(m, m, a, '  Ellipsoid matrix A:')

    volume = ellipsoid_volume(m, a, v, r)
    print('')
    print('  Ellipsoid volume = %g' % (volume))
    print('')
    print('         N        1              X               Y                Z                X^2            YZ              Z^3')
    print('')

    obj.create_tempdir(-1)
    seed = 123456789
    n = 2**5
    while (n <= 2**15):
        x, seed = ellipsoid_sample(m, n, a, v, r, seed)
        print('  %8d' % (n))
        for j in range(0, 7):
            e = e_test[j]
            value = monomial_value(m, n, e, x)
            result = volume * np.sum(value[0:n]) / float(n)
            print('  %14.6g' % (result), end='')
        print('')

        obj.new_3Dfig()
        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.set_axes_equal()
        obj.SavePng_Serial()
        plt.close()

        n = 2 * n
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_MONTE_CARLO_TEST03')
    print('  Normal end of execution.')
    return


def ellipsoid_sample(m, n, a, v, r, seed):

    # *****************************************************************************80
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
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 August 2014
    #
    #  Author:
    #
    #    John Burkardt
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


def ellipsoid_volume(m, a, v, r):

    # *****************************************************************************80
    #
    # ELLIPSOID_VOLUME returns the volume of an ellipsoid.
    #
    #  Discussion:
    #
    #    The points X in the ellipsoid are described by an M by M
    #    positive definite symmetric matrix A, an M-dimensional point V,
    #    and a "radius" R, such that
    #      (X-V)' * A * (X-V) <= R * R
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, real A(M,M), the matrix that describes
    #    the ellipsoid.  A must be symmetric and positive definite.
    #
    #    Input, real V(M), the "center" of the ellipse.
    #    The value of V is not actually needed by this function.
    #
    #    Input, real R, the "radius" of the ellipse.
    #
    #    Output, real VOLUME, the volume of the ellipsoid.
    #
    u = r8po_fa(m, a)

    sqrt_det = 1.0
    for i in range(0, m):
        sqrt_det = sqrt_det * u[i, i]

    volume = r ** m * hypersphere_unit_volume(m) / sqrt_det

    return volume


def hypersphere_unit_volume(m):

    # *****************************************************************************80
    #
    # HYPERSPHERE_UNIT_VOLUME: volume of a unit hypersphere in M dimensions.
    #
    #  Discussion:
    #
    #    The unit sphere in ND satisfies:
    #
    #      sum ( 1 <= I <= M ) X(I) * X(I) = 1
    #
    #    Results for the first few values of M are:
    #
    #     M  Volume
    #
    #     1    2
    #     2    1        * PI
    #     3  ( 4 /   3) * PI
    #     4  ( 1 /   2) * PI^2
    #     5  ( 8 /  15) * PI^2
    #     6  ( 1 /   6) * PI^3
    #     7  (16 / 105) * PI^3
    #     8  ( 1 /  24) * PI^4
    #     9  (32 / 945) * PI^4
    #    10  ( 1 / 120) * PI^5
    #
    #    For the unit sphere, Volume(M) = 2 * PI * Volume(M-2) / M
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 February 2005
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Output, real VOLUME, the volume of the sphere.
    #
    import numpy as np

    if ((m % 2) == 0):
        m2 = m // 2
        volume = np.pi ** m2
        for i in range(1, m2 + 1):
            volume = volume / float(i)
    else:
        m2 = (m - 1) // 2
        volume = np.pi ** m2 * 2.0 ** m
        for i in range(m2 + 1, 2 * m2 + 2):
            volume = volume / float(i)

    return volume


def i4vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_PRINT prints an I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i4vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT prints an I4VEC "transposed".
    #
    #  Example:
    #
    #    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:
    #
    #       1    2    3    4    5
    #       6    7    8    9   10
    #      11
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < len(title)):
        print('')
        print(title)

    if (0 < n):
        for i in range(0, n):
            print('%8d' % (a[i]), end='')
            if ((i + 1) % 10 == 0 or i == n - 1):
                print('')
    else:
        print('  (empty vector)')

    return


def i4vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
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
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C(N), the randomly chosen integer vector.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4VEC_UNIFORM_AB - Fatal error!')

    a = round(a)
    b = round(b)

    c = np.zeros(n, dtype=np.int32)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        seed = (seed % i4_huge)

        if (seed < 0):
            seed = seed + i4_huge

        r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
        r = (1.0 - r) * (min(a, b) - 0.5) \
            + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
        value = round(r)

        value = max(value, min(a, b))
        value = min(value, max(a, b))

        c[i] = value

    return c, seed


def i4vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 20
    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    v, seed = i4vec_uniform_ab(n, a, b, seed)

    i4vec_print(n, v, '  The random vector:')
#
#  Terminate.
#
    print('')
    print('I4VEC_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


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


def monomial_value_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_TEST tests MONOMIAL_VALUE on sets of data in various dimensions.
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
    import platform

    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use monomial_value() to evaluate some monomials')
    print('  in dimensions 1 through 3.')

    e_min = -3
    e_max = 6
    n = 5
    seed = 123456789
    x_min = -2.0
    x_max = +10.0

    for m in range(1, 4):

        print('')
        print('  Spatial dimension M =  %d' % (m))

        e, seed = i4vec_uniform_ab(m, e_min, e_max, seed)
        i4vec_transpose_print(m, e, '  Exponents:')
        x, seed = r8mat_uniform_ab(m, n, x_min, x_max, seed)
#
#  To make checking easier, make the X values integers.
#
        for i in range(0, m):
            for j in range(0, n):
                x[i, j] = round(x[i, j])

        v = monomial_value(m, n, e, x)

        print('')
        print('   V(X)         ', end='')
        for i in range(0, m):
            print('      X(%d)' % (i), end='')
        print('')
        print('')
        for j in range(0, n):
            print('%14.6g  ' % (v[j]), end='')
            for i in range(0, m):
                print('%10.4f' % (x[i, j]), end='')
            print('')
#
#  Terminate.
#
    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Normal end of execution.')
    return


def r8_normal_01(seed):

    # *****************************************************************************80
    #
    # R8_NORMAL_01 samples the standard normal probability distribution.
    #
    #  Discussion:
    #
    #    The standard normal probability distribution function (PDF) has
    #    mean 0 and standard deviation 1.
    #
    #    The Box-Muller method is used.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np

    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)

    x = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)

    return x, seed


def r8_normal_01_test():

    # *****************************************************************************80
    #
    # R8_NORMAL_01_TEST tests R8_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    seed = 123456789
    test_num = 20

    print('')
    print('R8_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_NORMAL_01 generates normally distributed')
    print('  random values.')
    print('  Using initial random number seed = %d' % (seed))
    print('')

    for test in range(0, test_num):

        x, seed = r8_normal_01(seed)
        print('  %f' % (x))
#
#  Terminate.
#
    print('')
    print('R8_NORMAL_01_TEST')
    print('  Normal end of execution.')
    return


def r8_uniform_01(seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_01 returns a unit pseudorandom R8.
    #
    #  Discussion:
    #
    #    This routine implements the recursion
    #
    #      seed = 16807 * seed mod ( 2^31 - 1 )
    #      r8_uniform_01 = seed / ( 2^31 - 1 )
    #
    #    The integer arithmetic never requires more than 32 bits,
    #    including a sign bit.
    #
    #    If the initial seed is 12345, then the first three computations are
    #
    #      Input     Output      R8_UNIFORM_01
    #      SEED      SEED
    #
    #         12345   207482415  0.096616
    #     207482415  1790989824  0.833995
    #    1790989824  2035175616  0.947702
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 March 2013
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
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R, a random value between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_01 - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10

    return r, seed


def r8_uniform_01_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_01 produces a sequence of random values.')

    seed = 123456789

    print('')
    print('  Using random seed %d' % (seed))

    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')
    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))

    print('')
    print('  Verify that the sequence can be restarted.')
    print('  Set the seed back to its original value, and see that')
    print('  we generate the same sequence.')

    seed = 123456789
    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')

    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))
#
#  Terminate.
#
    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Normal end of execution.')
    return


def r83col_print_part(n, a, max_print, title):

    # *****************************************************************************80
    #
    # R83COL_PRINT_PART prints "part" of an R83COL.
    #
    #  Discussion:
    #
    #    An R83COL is a (3,N) array of R8's.
    #
    #    The user specifies MAX_PRINT, the maximum number of lines to print.
    #
    #    If N, the size of the vector, is no more than MAX_PRINT, then
    #    the entire vector is printed, one entry per line.
    #
    #    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
    #    followed by a line of periods suggesting an omission,
    #    and the last entry.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries of the vector.
    #
    #    Input, real A(N,3), the vector to be printed.
    #
    #    Input, integer MAX_PRINT, the maximum number of lines
    #    to print.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < max_print):

        if (0 < n):

            if (0 < len(title)):
                print('')
                print(title)

            print('')

            if (n <= max_print):

                for i in range(0, n):
                    print('  %4d  %14g  %14g  %14g' %
                          (i, a[i, 0], a[i, 1], a[i, 2]))

            elif (3 <= max_print):

                for i in range(0, max_print - 2):
                    print('  %4d  %14g  %14g  %14g' %
                          (i, a[i, 0], a[i, 1], a[i, 2]))
                print('  ....  ..............  ..............  ..............')
                i = n - 1
                print('  %4d  %14g  %14g  %14g' %
                      (i, a[i, 0], a[i, 1], a[i, 2]))

            else:

                for i in range(0, max_print - 1):
                    print('  %4d  %14g  %14g  %14g' %
                          (i, a[i, 0], a[i, 1], a[i, 2]))
                i = max_print - 1
                print('  %4d  %14g  %14g  %14g  ...more entries...'
                      % (i, a[i, 0], a[i, 1], a[i, 2]))

    return


def r8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT prints an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    r8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_print_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_TEST tests R8MAT_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT prints an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print(m, n, v, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME prints out a portion of an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, real A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def r8mat_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT_SOME prints some of an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_transpose_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    r8mat_transpose_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_transpose_print_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT prints an R8MAT.')

    m = 4
    n = 3
    v = np.array([
        [11.0, 12.0, 13.0],
        [21.0, 22.0, 23.0],
        [31.0, 32.0, 33.0],
        [41.0, 42.0, 43.0]], dtype=np.float64)
    r8mat_transpose_print(m, n, v, '  Here is an R8MAT, transposed:')
#
#  Terminate.
#
    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_transpose_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, real A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for i2lo in range(max(ilo, 0), min(ihi, m - 1), incx):

        i2hi = i2lo + incx - 1
        i2hi = min(i2hi, m - 1)
        i2hi = min(i2hi, ihi)

        print('')
        print('  Row: ', end='')

        for i in range(i2lo, i2hi + 1):
            print('%7d       ' % (i), end='')

        print('')
        print('  Col')

        j2lo = max(jlo, 0)
        j2hi = min(jhi, n - 1)

        for j in range(j2lo, j2hi + 1):

            print('%7d :' % (j), end='')

            for i in range(i2lo, i2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def r8mat_uniform_ab(m, n, a, b, seed):

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
    #
    #  Discussion:
    #
    #    An R8MAT is an array of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 April 2013
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
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, real A, B, the range of the pseudorandom values.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.
    #
    #    Output, real R(M,N), an array of random values between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    import numpy
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8MAT_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8MAT_UNIFORM_AB - Fatal error!')

    r = numpy.zeros([m, n])

    for j in range(0, n):
        for i in range(0, m):

            k = (seed // 127773)

            seed = 16807 * (seed - k * 127773) - k * 2836

            seed = (seed % i4_huge)

            if (seed < 0):
                seed = seed + i4_huge

            r[i, j] = a + (b - a) * seed * 4.656612875E-10

    return r, seed


def r8po_fa(n, a):

    # *****************************************************************************80
    #
    # R8PO_FA factors a R8PO matrix.
    #
    #  Discussion:
    #
    #    The R8PO storage format is appropriate for a symmetric positive definite
    #    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
    #    upper triangular matrix, so it will be in R8GE storage format.)
    #
    #    Only the diagonal and upper triangle of the square array are used.
    #    This same storage scheme is used when the matrix is factored by
    #    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
    #    is set to zero.
    #
    #    The positive definite symmetric matrix A has a Cholesky factorization
    #    of the form:
    #
    #      A = R' * R
    #
    #    where R is an upper triangular matrix with positive elements on
    #    its diagonal.  This routine overwrites the matrix A with its
    #    factor R.
    #
    #    This function failed miserably when I wrote "r = a", because of a
    #    disastrously misconceived feature of Python, which does not copy
    #    one matrix to another, but makes them both point to the same object.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 August 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Bunch, Moler, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the matrix in R8PO storage.
    #
    #    Output, real R(N,N), the Cholesky factor R in R8GE storage.
    #
    #    Output, integer INFO, error flag.
    #    0, normal return.
    #    K, error condition.  The principal minor of order K is not
    #    positive definite, and the factorization was not completed.
    #
    import numpy as np
    from sys import exit

    r = np.zeros([n, n])

    for i in range(0, n):
        for j in range(i, n):
            r[i, j] = a[i, j]

    for j in range(0, n):

        for k in range(0, j):
            t = 0.0
            for i in range(0, k):
                t = t + r[i, k] * r[i, j]
            r[k, j] = (r[k, j] - t) / r[k, k]

        t = 0.0
        for i in range(0, j):
            t = t + r[i, j] ** 2

        s = r[j, j] - t

        if (s <= 0.0):
            print('')
            print('R8PO_FA - Fatal error!')
            print('  Factorization fails on column %d.' % (j))
            exit('R8PO_FA - Fatal error!')

        r[j, j] = np.sqrt(s)
#
#  Since the Cholesky factor is stored in R8GE format, be sure to
#  zero out the lower triangle.
#
    for i in range(0, n):
        for j in range(0, i):
            r[i, j] = 0.0

    return r


def r8po_sl(n, r, b):

    # *****************************************************************************80
    #
    # R8PO_SL solves a R8PO system factored by R8PO_FA.
    #
    #  Discussion:
    #
    #    The R8PO storage format is appropriate for a symmetric positive definite
    #    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
    #    upper triangular matrix, so it will be in R8GE storage format.)
    #
    #    Only the diagonal and upper triangle of the square array are used.
    #    This same storage scheme is used when the matrix is factored by
    #    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
    #    is set to zero.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Bunch, Moler, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real R(N,N), the Cholesky factor, in R8GE storage,
    #    returned by R8PO_FA.
    #
    #    Input, real B(N), the right hand side.
    #
    #    Output, real X(N), the solution vector.
    #
    import numpy as np

    x = np.zeros(n)

    for i in range(0, n):
        x[i] = b[i]
#
#  Solve R' * y = b.
#
    for k in range(0, n):
        t = 0.0
        for i in range(0, k):
            t = t + x[i] * r[i, k]
        x[k] = (x[k] - t) / r[k, k]
#
#  Solve R * x = y.
#
    for k in range(n - 1, -1, -1):
        x[k] = x[k] / r[k, k]
        for i in range(0, k):
            x[i] = x[i] - r[i, k] * x[k]

    return x


def r8vec_normal_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
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

    x = np.zeros(n)

    for i in range(0, n):
        x[i], seed = r8_normal_01(seed)

    return x, seed


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


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


def uniform_in_sphere01_map(m, n, seed):

    # *****************************************************************************80
    #
    # UNIFORM_IN_SPHERE01_MAP maps uniform points in the unit M-dimensional sphere.
    #
    #  Discussion:
    #
    #    The sphere has center 0 and radius 1.
    #
    #    We first generate a point ON the sphere, and then distribute it
    #    IN the sphere.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
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
    #    Wiley, 1986, page 232.
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the points.
    #
    import numpy as np

    exponent = 1.0 / float(m)

    x = np.zeros([m, n])

    for j in range(0, n):
        #
        #  Fill a vector with normally distributed values.
        #
        v, seed = r8vec_normal_01(m, seed)
        #
        #  Compute the length of the vector.
        #
        norm = np.linalg.norm(v)
        #
        #  Normalize the vector.
        #
        v[0:m] = v[0:m] / norm
        #
        #  Now compute a value to map the point ON the sphere INTO the sphere.
        #
        r, seed = r8_uniform_01(seed)

        x[0:m, j] = r ** exponent * v[0:m]

    return x, seed


def ellipsoid_monte_carlo_tests():

    # *****************************************************************************80
    #
    # ELLIPSOID_MONTE_CARLO_TESTS tests the ELLIPSOID_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ELLIPSOID_MONTE_CARLO_TESTS')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the ELLIPSOID_MONTE_CARLO library.')

    ellipsoid_monte_carlo_test01()
    ellipsoid_monte_carlo_test02()
    ellipsoid_monte_carlo_test03()

    print('')
    print('ELLIPSOID_MONTE_CARLO_TESTS')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    ellipsoid_monte_carlo_tests()
    timestamp()
