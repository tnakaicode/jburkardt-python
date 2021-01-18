#! /usr/bin/env python
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
from r8lib.r8 import r8_normal_01


def r8vec_normal_ab(n, mu, sigma, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_AB returns a scaled pseudonormal R8VEC.
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
    #    Input, real MU, the average value of the PDF.
    #
    #    Input, real SIGMA, the standard deviation of the PDF.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x = np.zeros(n)

    for i in range(0, n):
        xi, seed = r8_normal_01(seed)
        x[i] = mu + sigma * xi

    return x, seed


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

    x = np.zeros(n)

    for i in range(0, n):
        x[i], seed = r8_normal_01(seed)

    return x, seed


def r8vec_dot_product(n, v1, v2):

    # *****************************************************************************80
    #
    # R8VEC_DOT_PRODUCT finds the dot product of a pair of R8VEC's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real V1(N), V2(N), the vectors.
    #
    #    Output, real VALUE, the dot product.
    #

    value = 0.0
    for i in range(0, n):
        value = value + v1[i] * v2[i]

    return value


def r8vec_mean(n, a):

    # *****************************************************************************80
    #
    # R8VEC_MEAN returns the mean of an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the mean of the vector.
    #

    value = np.sum(a) / float(n)

    return value


def r8vec_circular_variance(n, x):

    # *****************************************************************************80
    #
    # R8VEC_CIRCULAR_VARIANCE returns the circular variance of an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real X(N), the vector whose variance is desired.
    #
    #    Output, real VALUE, the circular variance of the vector entries.
    #

    mean = 0.0
    for i in range(0, n):
        mean = mean + x[i]
    mean = mean / float(n)

    c = 0.0
    s = 0.0
    for i in range(0, n):
        c = c + np.cos(x[i] - mean)
        s = s + np.sin(x[i] - mean)

    value = s * s + c * c

    value = np.sqrt(value) / float(n)

    value = 1.0 - value

    return value


def r8vec_mean(n, a):

    # *****************************************************************************80
    #
    # R8VEC_MEAN returns the mean of an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the mean of the vector.
    #

    value = np.sum(a) / float(n)

    return value


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


def r8vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_TRANSPOSE_PRINT prints an R8VEC "transposed".
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Example:
    #
    #    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:   1.0    2.1    3.2    4.3    5.4
    #                 6.5    7.6    8.7    9.8   10.9
    #                11.0
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    title_length = len(title)

    for ilo in range(0, n, 5):

        if (ilo == 0):
            print(title),
        else:
            blanks = ''
            for i in range(0, title_length):
                blanks = blanks + ' '
            print(blanks),

        print('  '),

        ihi = min(ilo + 5 - 1, n - 1)

        for i in range(ilo, ihi + 1):
            print('  %12g' % (a[i])),
        print('')


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


def r8vec2_print(n, a1, a2, title):

    # *****************************************************************************80
    #
    # R8VEC2_PRINT prints an R8VEC2.
    #
    #  Discussion:
    #
    #    An R8VEC2 is a dataset consisting of N pairs of real values, stored
    #    as two separate vectors A1 and A2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, real A1(N), A2(N), the vectors to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('  %6d:   %12g  %12g' % (i, a1[i], a2[i]))


def r8vec_sum(n, a):

    # *****************************************************************************80
    #
    # R8VEC_SUM sums the entries of an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the sum of the entries.
    #
    value = 0.0
    for i in range(0, n):
        value = value + a[i]

    return value


def r8vec_min(n, a):

    # *****************************************************************************80
    #
    # R8VEC_MIN returns the minimum value in an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the minimum value in the vector.
    #
    r8_huge = 1.79769313486231571E+308

    value = r8_huge
    for i in range(0, n):
        if (a[i] < value):
            value = a[i]

    return value


def r8vec_max(n, a):

    # *****************************************************************************80
    #
    # R8VEC_MAX returns the maximum value in an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the maximum value in the vector.
    #
    r8_huge = 1.79769313486231571E+308

    value = - r8_huge
    for i in range(0, n):
        if (value < a[i]):
            value = a[i]

    return value


def r8vec_norm(n, a):

    # *****************************************************************************80
    #
    # R8VEC_NORM returns the L2 norm of an R8VEC.
    #
    #  Discussion:
    #
    #    The vector L2 norm is defined as:
    #
    #      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in A.
    #
    #    Input, real A(N), the vector whose L2 norm is desired.
    #
    #    Output, real VALUE, the L2 norm of A.
    #

    value = 0.0
    for i in range(0, n):
        value = value + a[i] * a[i]
    value = np.sqrt(value)

    return value


def r8vec_variance(n, a):

    # *****************************************************************************80
    #
    # R8VEC_VARIANCE returns the variance of an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the variance of the vector.
    #
    #
    #  DDOF = 1 requests normalization by N-1 rather than N.
    #
    value = np.var(a, ddof=1)

    return value


def r8vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
    #
    #  Discussion:
    #
    #    Each dimension ranges from A to B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Springer Verlag, pages 201-202, 1983.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, pages 362-376, 1986.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, pages 136-143, 1969.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the range of the pseudorandom values.
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
        print('R8VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_AB - Fatal error!')

    x = np.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = a + (b - a) * seed * 4.656612875E-10

    return x, seed


def r8vec_variance_test():

    # *****************************************************************************80
    #
    # R8VEC_VARIANCE_TEST tests R8VEC_VARIANCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_VARIANCE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_VARIANCE computes the variance of an R8VEC.')

    n = 10
    r8_lo = - 5.0
    r8_hi = + 5.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_variance(n, a)
    print('')
    print('  Value = %g' % (value))
    print('')
    print('R8VEC_VARIANCE_TEST:')
    print('  Normal end of execution.')


def r8vec_transpose_print_test():

    # *****************************************************************************80
    #
    # R8VEC_TRANSPOSE_PRINT_TEST tests R8VEC_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 12
    seed = 123456789

    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_TRANSPOSE_PRINT prints an R8VEC "tranposed",')
    print('  that is, placing multiple entries on a line.')

    x, seed = r8vec_uniform_01(n, seed)

    r8vec_transpose_print(n, x, '  The vector X:')

    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Normal end of execution.')


def r8vec_sum_test():

    # *****************************************************************************80
    #
    # R8VEC_SUM_TEST tests R8VEC_SUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_SUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_SUM sums the entries in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_sum(n, a)

    print('')
    print('  Sum of entries = %g' % (value))
    print('')
    print('R8VEC_SUM_TEST:')
    print('  Normal end of execution.')


def r8vec_norm_test():

    # *****************************************************************************80
    #
    # R8VEC_NORM_TEST tests R8VEC_NORM.
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

    print('')
    print('R8VEC_NORM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORM computes the L2 norm of an R8VEC.')

    n = 10
    seed = 123456789
    a, seed = r8vec_uniform_01(n, seed)
    r8vec_print(n, a, '  Input vector:')
    a_norm = r8vec_norm(n, a)

    print('')
    print('  L2 norm = %g' % (a_norm))
    print('')
    print('R8VEC_NORM_TEST:')
    print('  Normal end of execution.')


def r8vec_max_test():

    # *****************************************************************************80
    #
    # R8VEC_MAX_TEST tests R8VEC_MAX.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_MAX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MAX computes the maximum entry in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_max(n, a)
    print('')
    print('  Max = %g' % (value))
    print('')
    print('R8VEC_MAX_TEST:')
    print('  Normal end of execution.')


def r8vec_min_test():

    # *****************************************************************************80
    #
    # R8VEC_MIN_TEST tests R8VEC_MIN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_MIN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MIN computes the minimum entry in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_min(n, a)
    print('')
    print('  Min = %g' % (value))
    print('')
    print('R8VEC_MIN_TEST:')
    print('  Normal end of execution.')


def r8vec_normal_01_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01_TEST tests R8VEC_NORMAL_01.
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

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_01 returns a vector of Normal 01 values')
    print('')
    print('  SEED = %d' % (seed))

    r, seed = r8vec_normal_01(n, seed)

    r8vec_print(n, r, '  Vector:')

    print('')
    print('R8VEC_NORMAL_01_TEST:')
    print('  Normal end of execution.')


def r8vec_normal_ab_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_AB_TEST tests R8VEC_NORMAL_AB.
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

    print('')
    print('R8VEC_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_AB returns a vector of Normal AB values')

    n = 10
    mu = 15.0
    sigma = 0.25
    seed = 123456789

    print('')
    print('  Mean = %g' % (mu))
    print('  Standard deviation = %g' % (sigma))
    print('  SEED = %d' % (seed))

    r, seed = r8vec_normal_ab(n, mu, sigma, seed)

    r8vec_print(n, r, '  Vector:')

    print('')
    print('R8VEC_NORMAL_AB_TEST:')
    print('  Normal end of execution.')


def r8vec_circular_variance_test():

    # *****************************************************************************80
    #
    # R8VEC_CIRCULAR_VARIANCE_TEST tests R8VEC_CIRCULAR_VARIANCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_CIRCULAR_VARIANCE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_CIRCULAR_VARIANCE computes the circular variance of an R8VEC.')

    n = 10
    a = - np.pi
    b = + np.pi
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, a, b, seed)

    r8vec_print(n, x, '  Uniform Vector in [-PI,+PI]:')
    circular_variance = r8vec_circular_variance(n, x)

    print('')
    print('  Circular variance: %g' % (circular_variance))

    n = 10
    a = 0.0
    b = 1.0
    seed = 123456789
    x, seed = r8vec_normal_ab(n, a, b, seed)

    r8vec_print(n, x, '  Normal vector, mean 0, variance 1')

    circular_variance = r8vec_circular_variance(n, x)

    print('')
    print('  Circular variance: %g' % (circular_variance))
    print('')
    print('R8VEC_CIRCULAR_VARIANCE_TEST')
    print('  Normal end of execution.')


def r8vec_mean_test():

    # *****************************************************************************80
    #
    # R8VEC_MEAN_TEST tests R8VEC_MEAN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_MEAN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MEAN computes the mean of an R8VEC.')

    n = 10
    r8_lo = - 5.0
    r8_hi = + 5.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_mean(n, a)
    print('')
    print('  Value = %g' % (value))
    print('')
    print('R8VEC_MEAN_TEST:')
    print('  Normal end of execution.')


def r8vec_dot_product_test():

    # *****************************************************************************80
    #
    # R8VEC_DOT_PRODUCT_TEST tests R8VEC_DOT_PRODUCT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_DOT_PRODUCT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_DOT_PRODUCT computes the dot product of two R8VEC\'s.')

    n = 10
    seed = 123456789
    v1, seed = r8vec_uniform_01(n, seed)
    v2, seed = r8vec_uniform_01(n, seed)
    r8vec2_print(n, v1, v2, '  V1 and V2:')

    value = r8vec_dot_product(n, v1, v2)

    print('')
    print('  V1 dot V2 = %g' % (value))
    print('')
    print('R8VEC_DOT_PRODUCT_TEST:')
    print('  Normal end of execution.')


def r8vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10
    a = -1.0
    b = +5.0
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_AB computes a random R8VEC.')
    print('')
    print('  %g <= X <= %g' % (a, b))
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_ab(n, a, b, seed)

    r8vec_print(n, v, '  Random R8VEC:')

    print('')
    print('R8VEC_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')

    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')


def r8vec2_print_test():

    # *****************************************************************************80
    #
    # R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC2_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC2_PRINT prints a pair of R8VEC\'s.')

    n = 6
    v = np.array([0.0, 0.20, 0.40, 0.60, 0.80, 1.0], dtype=np.float64)
    w = np.array([0.0, 0.04, 0.16, 0.36, 0.64, 1.0], dtype=np.float64)
    r8vec2_print(n, v, w, '  Print a pair of R8VEC\'s:')

    print('')
    print('R8VEC2_PRINT_TEST:')
    print('  Normal end of execution.')


def r8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_01 computes a random R8VEC.')
    print('')
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_01(n, seed)

    r8vec_print(n, v, '  Random R8VEC:')

    print('')
    print('R8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')


def r8vec_mean_test():

    # *****************************************************************************80
    #
    # R8VEC_MEAN_TEST tests R8VEC_MEAN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_MEAN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MEAN computes the mean of an R8VEC.')

    n = 10
    r8_lo = - 5.0
    r8_hi = + 5.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_mean(n, a)
    print('')
    print('  Value = %g' % (value))
    print('')
    print('R8VEC_MEAN_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
