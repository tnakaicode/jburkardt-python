#! /usr/bin/env python3
#


def disk_sample(center, r, n, seed):

    # *****************************************************************************80
    #
    # DISK_SAMPLE uniformly samples the unit disk.
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
    #    Input, real CENTER(2), the center of the disk.
    #
    #    Input, real R, the radius of the disk.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(2,N), the points.
    #
    import numpy as np
    from r8_uniform_01 import r8_uniform_01
    from r8vec_normal_01 import r8vec_normal_01

    x = np.zeros([2, n])

    for j in range(0, n):
        #
        #  Fill a vector with normally distributed values.
        #
        v, seed = r8vec_normal_01(2, seed)
#
#  Compute the length of the vector.
#
        norm = np.sqrt(v[0] ** 2 + v[1] ** 2)
#
#  Normalize the vector.
#
        v[0] = v[0] / norm
        v[1] = v[1] / norm
#
#  Now compute a value to map the point ON the disk INTO the disk.
#
        r2, seed = r8_uniform_01(seed)

        x[0, j] = center[0] + r * np.sqrt(r2) * v[0]
        x[1, j] = center[1] + r * np.sqrt(r2) * v[1]

    return x, seed


def disk_sample_test(center, r):

    # *****************************************************************************80
    #
    # DISK_SAMPLE_TEST tests DISK_SAMPLE.
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
    #    Input, real CENTER(2), the center of the disk.
    #
    #    Input, real R, the radius of the disk.
    #
    import platform
    import numpy as np
    from disk_area import disk_area
    from disk01_monomial_integral import disk01_monomial_integral
    from monomial_value import monomial_value

    print('')
    print('DISK_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use DISK_SAMPLE to estimate integrals in the disk')
    print('  with center (%g,%g) and radius %g'
          % (center[0], center[1], r))

    e_test = np.array([
        [0, 0],
        [2, 0],
        [0, 2],
        [4, 0],
        [2, 2],
        [0, 4],
        [6, 0]])

    seed = 123456789

    print('')
    print('         N        1              X^2             Y^2             X^4             X^2Y^2           Y^4             X^6')
    print('')

    n = 1

    while (n <= 65536):

        x, seed = disk_sample(center, r, n, seed)

        print('  %8d' % (n), end='')

        for i in range(0, 7):

            e = e_test[i, :]

            value = monomial_value(2, n, e, x)

            result = disk_area(center, r) * np.sum(value[:]) / n
            print('  %14.6g' % (result), end='')

        print('')

        n = 2 * n

    if (
            center[0] == 0.0 and
            center[1] == 0.0 and
            r == 1.0):
        print('')
        print('     Exact', end='')
        for i in range(0, 7):
            e = e_test[i, :]
            result = disk01_monomial_integral(e)
            print('  %14.6g' % (result), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('DISK01_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    import numpy as np
    timestamp()
    center = np.array([1.0, 2.0])
    r = 3.0
    disk_sample_test(center, r)
    timestamp()
