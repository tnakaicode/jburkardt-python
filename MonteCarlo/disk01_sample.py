#! /usr/bin/env python3
#


def disk01_sample(n, seed):

    # *****************************************************************************80
    #
    # DISK01_SAMPLE uniformly samples the unit disk.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 January 2014
    #
    #  Author:
    #
    #    John Burkardt
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
        r, seed = r8_uniform_01(seed)
        x[0, j] = np.sqrt(r) * v[0]
        x[1, j] = np.sqrt(r) * v[1]

    return x, seed


def disk01_sample_test():

    # *****************************************************************************80
    #
    # DISK01_SAMPLE_TEST tests DISK01_SAMPLE.
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
    import platform
    from r8mat_transpose_print import r8mat_transpose_print

    print('')
    print('DISK01_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DISK01_SAMPLE samples the unit disk.')

    n = 10
    seed = 123456789

    x, seed = disk01_sample(n, seed)

    r8mat_transpose_print(2, n, x, '  Sample points in the unit disk.')
#
#  Terminate.
#
    print('')
    print('DISK01_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    disk01_sample_test()
    timestamp()
