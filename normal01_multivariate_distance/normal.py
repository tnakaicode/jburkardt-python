#! /usr/bin/env python3
#


def c8_normal_01(seed):

    # *****************************************************************************80
    #
    # C8_NORMAL_01 returns a unit normally distributed complex number.
    #
    #  Discussion:
    #
    #    The value has mean 0 and standard deviation 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, complex C, a sample of the PDF.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #
    import numpy as np

    v1, seed = r8_uniform_01(seed)
    v2, seed = r8_uniform_01(seed)

    x = np.sqrt(- 2.0 * np.log(v1)) * np.cos(2.0 * np.pi * v2)
    y = np.sqrt(- 2.0 * np.log(v1)) * np.sin(2.0 * np.pi * v2)

    c = x + y * 1j

    return c, seed


def c8_normal_01_test():

    # *****************************************************************************80
    #
    # C8_NORMAL_01_TEST tests C8_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    seed = 123456789

    print('')
    print('C8_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8_NORMAL_01 computes pseudonormal complex values.')

    print('')
    print('  The initial seed is %d' % (seed))
    print('')

    for i in range(1, 11):
        [c, seed] = c8_normal_01(seed)
        print('  %6d  ( %f, %f )' % (i, c.real, c.imag))
#
#  Terminate.
#
    print('')
    print('C8_NORMAL_01_TEST:')
    print('  Normal end of execution.')
    return


def i4_normal_ab(mu, sigma, seed):

    # *****************************************************************************80
    #
    # I4_NORMAL_AB returns a scaled pseudonormal I4.
    #
    #  Discussion:
    #
    #    The normal probability distribution function (PDF) is sampled,
    #    with mean MU and standard deviation SIGMA.
    #
    #    The result is rounded to the nearest integer.
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
    #    Input, real MU, the mean of the PDF.
    #
    #    Input, real SIGMA, the standard deviation of the PDF.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer VALUE, a normally distributed
    #    random value.
    #
    #    Output, integer SEED, an updated seed for the random
    #    number generator.
    #
    import numpy as np

    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)
    value = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)
    value = int(mu + sigma * value)

    return value, seed


def i4_normal_ab_test():

    # *****************************************************************************80
    #
    # I4_NORMAL_AB_TEST tests I4_NORMAL_AB.
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
    import platform

    print('')
    print('I4_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_NORMAL_AB computes integer pseudonormal values with')
    print('  mean MU and standard deviation SIGMA.')

    mu = 10.0
    sigma = 2.0
    seed = 123456789

    print('')
    print('  MU = %g' % (mu))
    print('  SIGMA = %g' % (sigma))
    print('  SEED = %d' % (seed))
    print('')
    for i in range(0, 10):
        r, seed = i4_normal_ab(mu, sigma, seed)
        print('  %2d  %12d' % (i, r))
#
#  Terminate.
#
    print('')
    print('I4_NORMAL_AB_TEST')
    print('  Normal end of execution.')
    return


def normal_test():

    # *****************************************************************************80
    #
    # NORMAL_TEST tests the NORMAL library.
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
    import platform

    print('')
    print('NORMAL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the NORMAL library.')
#
#  Utilities:
#
    r8_uniform_01_test()
    r8mat_print_test()
    r8mat_print_some_test()
    r8vec_print_test()
    r8vec_uniform_01_test()
    timestamp_test()
#
#  Libraries:
#
    c8_normal_01_test()
    i4_normal_ab_test()
    r8_normal_01_test()
    r8_normal_ab_test()
    r8mat_normal_01_test()
    r8mat_normal_ab_test()
    r8vec_normal_01_test()
    r8vec_normal_ab_test()
#
#  Terminate.
#
    print('')
    print('NORMAL_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_normal_01(m, n, seed):

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_01 returns a unit pseudonormal R8MAT.
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
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np

    x = np.zeros((m, n))

    for i in range(0, m):
        for j in range(0, n):
            x[i, j], seed = r8_normal_01(seed)

    return x, seed


def r8mat_normal_01_test():

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_01_TEST tests R8MAT_NORMAL_01.
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
    import numpy as np
    import platform

    m = 5
    n = 4
    seed = 123456789

    print('')
    print('R8MAT_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_NORMAL_01 returns a matrix of Normal 01 values')
    print('')
    print('  SEED = %d' % (seed))

    r, seed = r8mat_normal_01(m, n, seed)

    r8mat_print(m, n, r, '  Matrix:')
#
#  Terminate.
#
    print('')
    print('R8MAT_NORMAL_01_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_normal_ab(m, n, mu, sigma, seed):

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_AB returns a scaled pseudonormal R8MAT.
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
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, real MU, SIGMA, the mean and standard deviation.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np

    x = np.zeros((m, n))

    for i in range(0, m):
        for j in range(0, n):
            xi, seed = r8_normal_01(seed)
            x[i, j] = mu + sigma * xi

    return x, seed


def r8mat_normal_ab_test():

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_AB_TEST tests R8MAT_NORMAL_AB.
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
    import numpy as np
    import platform

    print('')
    print('R8MAT_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_NORMAL_AB returns a matrix of Normal AB values')

    m = 5
    n = 4
    mu = 100.0
    sigma = 5.0
    seed = 123456789

    print('')
    print('  Mean = %g' % (mu))
    print('  Standard deviation = %g' % (sigma))
    print('  SEED = %d' % (seed))

    r, seed = r8mat_normal_ab(m, n, mu, sigma, seed)

    r8mat_print(m, n, r, '  Matrix:')
#
#  Terminate.
#
    print('')
    print('R8MAT_NORMAL_AB_TEST:')
    print('  Normal end of execution.')
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


def r8_normal_ab(a, b, seed):

    # *****************************************************************************80
    #
    # R8_NORMAL_AB returns a scaled pseudonormal R8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the mean of the normal PDF.
    #
    #    Input, real B, the standard deviation of the normal PDF.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    x, seed = r8_normal_01(seed)
    x = a + b * x

    return x, seed


def r8_normal_ab_test():

    # *****************************************************************************80
    #
    # R8_NORMAL_AB_TEST tests R8_NORMAL_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    x_mean = 100.0
    x_std = 10.0
    seed = 123456789
    test_num = 20

    print('')
    print('R8_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_NORMAL_AB generates normally distributed values')
    print('  with given mean and standard deviation.')
    print('  Using initial random number seed = %d' % (seed))
    print('  MEAN = %g' % (x_mean))
    print('  STD = %g' % (x_std))
    print('')

    for test in range(0, test_num):

        x, seed = r8_normal_ab(x_mean, x_std, seed)
        print('  %g' % (x))
#
#  Terminate.
#
    print('')
    print('R8_NORMAL_AB_TEST')
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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('R8VEC_NORMAL_01_TEST:')
    print('  Normal end of execution.')
    return


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
    import numpy as np

    x = np.zeros(n)

    for i in range(0, n):
        xi, seed = r8_normal_01(seed)
        x[i] = mu + sigma * xi

    return x, seed


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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('R8VEC_NORMAL_AB_TEST:')
    print('  Normal end of execution.')
    return


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
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


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


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    normal_test()
    timestamp()
