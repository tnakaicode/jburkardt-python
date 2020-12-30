#! /usr/bin/env python3
#

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


def cosine_transform_data(n, d):

    # *****************************************************************************80
    #
    # COSINE_TRANSFORM_DATA does a cosine transform on a vector of data.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data points.
    #
    #    Input, real D(N), the vector of data.
    #
    #    Output, real C(N), the cosine transform coefficients.
    #

    c = np.zeros(n)

    for i in range(0, n):
        for j in range(0, n):
            angle = np.pi * float(2 * j + 1) * float(i) / 2.0 / float(n)
            c[i] = c[i] + d[j] * np.cos(angle)

        c[i] = c[i] * np.sqrt(2.0 / float(n))

    return c


def cosine_transform_inverse(n, c):

    # *****************************************************************************80
    #
    # COSINE_TRANSFORM_INVERSE does an inverse cosine transform.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data points.
    #
    #    Input, real C(N), the cosine transform coefficients.
    #
    #    Output, real D(N), the vector of data.
    #

    d = np.zeros(n)

    for i in range(0, n):
        d[i] = c[0] / 2.0
        for j in range(1, n):
            d[i] = d[i] + np.cos(np.pi * float(2 * i + 1)
                                 * float(j) / 2.0 / float(n)) * c[j]
        d[i] = d[i] * np.sqrt(2.0 / float(n))

    return d


def cosine_transform_data_test():

    # *****************************************************************************80
    #
    # COSINE_TRANSFORM_DATA_TEST carries out a DCT and its inverse.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('COSINE_TRANSFORM_DATA_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  COSINE_TRANSFORM_DATA does a cosine transform of data')
    print('  defined by a vector.')
    print('')
    print('  Apply the transform, then its inverse.')
    print('  Let R be a random N vector.')
    print('  Let S be the transform of D.')
    print('  Let T be the transform of E.')
    print('  Then R and T will be equal.')

    seed = 123456789
    r, seed = r8vec_uniform_01(n, seed)
    s = cosine_transform_data(n, r)
    t = cosine_transform_inverse(n, s)

    print('')
    print('     I      R(I)        S(I)        T(I)')
    print('')

    for i in range(0, n):
        print('  %4d  %10f  %10f  %10f' % (i, r[i], s[i], t[i]))

    print('')
    print('COSINE_TRANSFORM_DATA_TEST')
    print('  Normal end of execution.')


def cosine_transform_test():

    # *****************************************************************************80
    #
    # COSINE_TRANSFORM_TEST tests the COSINE_TRANSFORM library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('COSINE_TRANSFORM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the COSINE_TRANSFORM library.')

    cosine_transform_data_test()

    print('')
    print('COSINE_TRANSFORM_TEST:')
    print('  Normal end of execution.')


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

    return


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


if (__name__ == '__main__'):
    timestamp()
    cosine_transform_test()
    timestamp()
