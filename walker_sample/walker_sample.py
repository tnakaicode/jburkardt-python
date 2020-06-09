#! /usr/bin/env python3
#


def i4_choose(n, k):

    # *****************************************************************************80
    #
    # I4_CHOOSE computes the binomial coefficient C(N,K) as an I4.
    #
    #  Discussion:
    #
    #    The value is calculated in such a way as to avoid overflow and
    #    roundoff.  The calculation is done in integer arithmetic.
    #
    #    The formula used is:
    #
    #      C(N,K) = N! / ( K! * (N-K)! )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    ML Wolfson, HV Wright,
    #    Algorithm 160:
    #    Combinatorial of M Things Taken N at a Time,
    #    Communications of the ACM,
    #    Volume 6, Number 4, April 1963, page 161.
    #
    #  Parameters:
    #
    #    Input, integer N, K, are the values of N and K.
    #
    #    Output, integer VALUE, the number of combinations of N
    #    things taken K at a time.
    #
    mn = min(k, n - k)
    mx = max(k, n - k)

    if (mn < 0):

        value = 0

    elif (mn == 0):

        value = 1

    else:

        value = mx + 1

        for i in range(2, mn + 1):
            value = (value * (mx + i)) / i

    return value


def i4_choose_test():

    # *****************************************************************************80
    #
    # I4_CHOOSE_TEST tests I4_CHOOSE.
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

    print('')
    print('I4_CHOOSE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_CHOOSE evaluates C(N,K).')
    print('')
    print('       N       K     CNK')

    for n in range(0, 5):
        print('')
        for k in range(0, n + 1):
            cnk = i4_choose(n, k)

            print('  %6d  %6d  %6d' % (n, k, cnk))
#
#  Terminate.
#
    print('')
    print('I4_CHOOSE_TEST:')
    print('  Normal end of execution.')
    return


def i4_uniform_ab(a, b, seed):

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB returns a scaled pseudorandom I4.
    #
    #  Discussion:
    #
    #    The pseudorandom number will be scaled to be uniformly distributed
    #    between A and B.
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
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C, the randomly chosen integer.
    #
    #    Output, integer SEED, the updated seed.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4_UNIFORM_AB - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    a = round(a)
    b = round(b)

    r = (1.0 - r) * (min(a, b) - 0.5) \
        + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round(r)

    value = max(value, min(a, b))
    value = min(value, max(a, b))
    value = int(value)

    return value, seed


def i4_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
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

    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    for i in range(1, 21):
        j, seed = i4_uniform_ab(a, b, seed)
        print('  %8d  %8d' % (i, j))
#
#  Terminate.
#
    print('')
    print('I4_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


def normalize(n, x):

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    NORMALIZE scales a vector X so its entries sum to 1.
    #
    #  Modified:
    #
    #    19 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    This Python version by John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, indicates the size of X.
    #
    #    Input/output, double X[N+2], the vector to be normalized.
    #    Entries X[1] through X[N] will sum to 1 on output.
    #

    #
    #  Sum X.
    #
    sum = 0.0
    for i in range(1, n + 1):
        sum = sum + abs(x[i])
#
#  Normalize so that the new sum of X will be 1.
#
    for i in range(1, n + 1):
        x[i] = x[i] / sum

    return x


def normalize_test():

    # *****************************************************************************80
    #
    # NORMALIZE_TEST tests NORMALIZE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NORMALIZE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NORMALIZE normalizes entries 1 through N of a vector')
    print('  of length N+2.')

    n = 5
    seed = 123456789
    x, seed = r8vec_uniform_01(n + 2, seed)
    r8vec_print(n + 2, x, '  Initial X:')

    x_norm = 0.0
    for i in range(1, n + 1):
        x_norm = x_norm + abs(x[i])
    print('')
    print('  Initial L1 norm of X(1:%d) = %10.6g' % (n, x_norm))

    x = normalize(n, x)

    r8vec_print(n + 2, x, '  Normalized X:')

    x_norm = 0.0
    for i in range(1, n + 1):
        x_norm = x_norm + abs(x[i])
    print('')
    print('  Final L1 norm of X(1:%d) = %10.6g' % (n, x_norm))
#
#  Terminate.
#
    print('')
    print('NORMALIZE_TEST')
    print('  Normal end of execution.')
    return


def r8vec_indicator0(n):

    # *****************************************************************************80
    #
    # R8VEC_INDICATOR0 sets an R8VEC to the indicator vector (0,1,2,...).
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
    #    27 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of elements of the vector.
    #
    #    Output, real A(N), the indicator array.
    #
    import numpy

    a = numpy.zeros(n)

    for i in range(0, n):
        a[i] = i

    return a


def r8vec_indicator0_test():

    # *****************************************************************************80
    #
    # R8VEC_INDICATOR0_TEST tests R8VEC_INDICATOR0.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_INDICATOR0_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_INDICATOR0 returns an indicator matrix.')

    n = 10
    a = r8vec_indicator0(n)

    r8vec_print(n, a, '  The indicator0 vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_INDICATOR0_TEST')
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


def random_permutation(n, x, seed):

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    RANDOM_PERMUTATION applies a random permutation to an array.
    #
    #  Modified:
    #
    #    19 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    Python version by John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, indicates the size of X.
    #
    #    Input/output, double X[N+2].  On output, entries X[1] through
    #    X[N] have been randomly permuted.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    for i in range(1, n + 1):

        j, seed = i4_uniform_ab(i, n, seed)

        t = x[i]
        x[i] = x[j]
        x[j] = t

    return x


def random_permutation_test():

    # *****************************************************************************80
    #
    # RANDOM_PERMUTATION_TEST tests RANDOM_PERMUTATION.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('RANDOM_PERMUTATION_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RANDOM_PERMUTATION randomly permutes entries 1 through N of')
    print('  a vector X[0:N+1].')

    n = 5
    x = r8vec_indicator0(n + 2)
    seed = 123456789
    r8vec_print(n + 2, x, '  Initial X:')
    x = random_permutation(n, x, seed)
    r8vec_print(n + 2, x, '  Permuted X:')
#
#  Terminate.
#
    print('')
    print('RANDOM_PERMUTATION_TEST')
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


def walker_build(n, x):

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    WALKER_BUILD sets up the data for a Walker sampler.
    #
    #  Discussion:
    #
    #    From the probability vector X, this function creates the Y and A
    #    vectors used by the Walker sampler.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Warren Smith,
    #    How to sample from a probability distribution,
    #    April 18, 2002.
    #
    #  Parameters:
    #
    #    Input, unsigned int N, indicates the size of X.
    #
    #    Input, double X[N+2], contains in X[1] through X[N] the
    #    probabilities of outcomes 1 through N.
    #
    #    Output, double Y[N+2], the Walker threshold vector.
    #
    #    Output, unsigned int A[N+2], the Walker index vector.
    #
    import numpy as np
#
#  Initialize A.
#
    a = np.zeros(n + 2, dtype=np.int32)
    for i in range(0, n + 2):
        a[i] = i
#
#  Initialize B to the "stay here" value, and set sentinel values at the ends.
#
    b = np.zeros(n + 2, dtype=np.int32)

    for i in range(0, n + 2):
        b[i] = a[i]
#
#  Copy X into Y.
#  Scale the probability vector and set sentinel values at the ends.
#
    y = np.zeros(n + 2, dtype=np.float64)

    y[0] = 0.0
    for i in range(1, n + 1):
        y[i] = x[i] * float(n)
    y[n + 1] = 2.0

    i = 0
    j = n + 1

    while (True):
        #
        #  Find i so Y[B[i]] needs more.
        #
        while (True):
            i = i + 1
            if (1.0 <= y[b[i]]):
                break
#
#  Find j so Y[B[j]] wants less.
#
        while (True):
            j = j - 1
            if (y[b[j]] < 1.0):
                break

        if (j <= i):
            break
#
#  Swap B[i] and B[j].
#
        k = b[i]
        b[i] = b[j]
        b[j] = k

    i = j
    j = j + 1

    while (0 < i):
        #
        #  Find J such that Y[B[j]] needs more.
        #
        while (y[b[j]] <= 1.0):
            j = j + 1
#
#  Meanwhile, Y[B[i]] wants less.
#
        if (n < j):
            break
#
#  B[i] will donate to B[j] to fix up.
#
        y[b[j]] = y[b[j]] - (1.0 - y[b[i]])
        a[b[i]] = b[j]
#
#  Y[B[j]] now wants less so readjust ordering.
#
        if (y[b[j]] < 1.0):
            k = b[i]
            b[i] = b[j]
            b[j] = k
            j = j + 1
        else:
            i = i - 1

    return y, a


def walker_build_test():

    # *****************************************************************************80
    #
    # WALKER_BUILD_TEST tests WALKER_BUILD.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('WALKER_BUILD_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  WALKER_BUILD builds the Walker sampler data vectors Y and A,')
    print('  given a probability vector X.')

    n = 5
    x = np.zeros(n + 2, dtype=np.float64)
    for i in range(1, n + 1):
        x[i] = float(i4_choose(n - 1, i - 1)) / float(2 ** (n - 1))
    r8vec_print(n + 2, x, '  Binomial PDF (ignore first and last entries):')

    y, a = walker_build(n, x)
    print('')
    print('   I    A[I]    Y[i] (ignore first and last entries)')
    print('')
    for i in range(0, n + 2):
        print('  %2d  %2d  %10.4g' % (i, a[i], y[i]))
#
#  Terminate.
#
    print('')
    print('WALKER_BUILD_TEST')
    print('  Normal end of execution.')
    return


def walker_sampler(n, y, a):

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    WALKER_SAMPLER returns a random sample i=1..N with prob X[i].
    #
    #  Discussion:
    #
    #    Implementation of algorithm for sampling from a discrete
    #    probability N-vector X[1], X[2], ..., X[N].  (N>=1.)
    #    Runs on O(1) worst case time per sample,
    #    and uses one integer and one double N-element array for storage.
    #    Preprocessing consumes O(N) time and temporarily uses one
    #    additional integer array (B[0..N+1]) for bookkeeping.
    #    X[0] and X[N+1] are also used as sentinels in the Build() algorithm.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Warren Smith,
    #    How to sample from a probability distribution,
    #    April 18, 2002.
    #
    #  Parameters:
    #
    #    Input, unsigned int N, indicates the size of the probability vector X.
    #
    #    Input, double Y[N+2], the Walker threshold vector.
    #
    #    Input, unsigned int A[N+2], the Walker index vector.
    #
    #    Output, unsigned int WALKER_SAMPLER, a sample value between 1 and N,
    #    selected according to the probability vector X.
    #
    import numpy as np
    import random as rn
#
#  Let i = random uniform integer from {1,2,...N}
#
    i = 1 + int(np.fix(float(n) * rn.random()))

    r = rn.random()

    if (y[i] < r):
        i = a[i]

    return i


def walker_sampler_test():

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    WALKER_SAMPLER_TEST tests WALKER_SAMPLER.
    #
    #  Discussion:
    #
    #    A Zipf-type probability vector is used.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    Python version by John Burkardt.
    #
    #  Parameters:
    #
    #    Input, unsigned int SEED, a seed for the random number generator.
    #
    #    Input, unsigned int N, indicates the size of the probability vector X.
    #
    #    Input, double P, the value of the Zipf parameter
    #    1 <= P.
    #
    import numpy as np
    import platform
    import random as rn

    seed = 123456789
    n = 10
    p = 2.0

    print('')
    print('WALKER_SAMPLER_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  WALKER_SAMPLER creates Walker sample vectors Y and A')
    print('  for efficient sampling of a discrete probability vector.')
    print('  Test the Walker sampler with a Zipf-type probability.')
#
#  Initialize the random number generator.
#
    print('  Use seed = %d as input to random.seed ( seed ):' % (seed))

    rn.seed(seed)
#
#  Generate a standard Zipf probability vector for cases 1 - N,
#  with parameter P.
#
    x = zipf_probability(n, p)

    print('')
    print('  Zipf probabilities')
    print('  for N = %d' % (n))
    print('  and parameter P = %g' % (p))
    print('')
    print('     I     X[I]')
    print('')
    for i in range(1, n + 1):
        print('  %4d  %16g' % (i, x[i]))
#
#  For better testing, randomly scramble the probabilities.
#
    x = random_permutation(n, x, seed)

    print('')
    print('  Randomly permuted X:')
    print('')
    print('     I     X[I]')
    print('')
    for i in range(1, n + 1):
        print('  %4d  %16g' % (i, x[i]))
#
#  Build the Walker sampler.
#
    y, a = walker_build(n, x)

    print('')
    print('  Built the sampler')
    print('  i Y[i] A[i]:')
    print('')

    for i in range(0, n + 2):
        print('  %3d  %16g  %4d' % (i, y[i], a[i]))
#
#  Prepare to count the frequency of each outcome.
#
    count = np.zeros(n + 2, dtype=np.int32)
#
#  Call the sampler many times.
#
    for i in range(0, 100000):
        j = walker_sampler(n, y, a)
        count[j] = count[j] + 1
#
#  Compare normalized sample frequencies to the original probabilities in X.
#
    v = 0.0
    print('')
    print('  100000 samples:')
    print('  prob   #samples:')
    print('')

    for i in range(1, n + 1):
        print('  %16g  %6d' % (x[i], count[i]))
        expval = x[i] * 100000
        t = expval - count[i]
        v = v + t * t / expval

    v = v / (float)(n)

    print('')
    print('  sumvar = %g, (should be about 1)' % (v))
#
#  Terminate.
#
    print('')
    print('WALKER_SAMPLER_TEST')
    print('  Normal end of execution.')
    return


def walker_sample_test():

    # *****************************************************************************80
    #
    #  Purpose:
    #
    #    WALKER_SAMPLE_TEST tests WALKER_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('WALKER_SAMPLE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WALKER_SAMPLE library.')

    i4_choose_test()
    i4_uniform_ab_test()
    normalize_test()
    r8vec_indicator0_test()
    r8vec_print_test()
    r8vec_uniform_01_test()
    random_permutation_test()
    walker_build_test()
    walker_sampler_test()
    walker_verify_test()
    zipf_probability_test()
#
#  Terminate.
#
    print('')
    print('WALKER_SAMPLE_TEST:')
    print('  Normal end of execution.')
    return


def walker_verify(n, x, y, a):

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    WALKER_VERIFY verifies a Walker Sampler structure.
    #
    #  Discussion:
    #
    #    This test applies the sampling algorithms to a Zipfian distribution.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    Python version by John Burkardt.
    #
    #  Parameters:
    #
    #    Input, unsigned int N, indicates the size of X.
    #
    #    Input, double X[N+2], contains in X[1] through X[N] the
    #    probabilities of outcomes 1 through N.
    #
    #    Input, double Y[N+2], the Walker threshold vector.
    #
    #    Input, unsigned int A[N+2], the Walker index vector.
    #
    import numpy as np

    z = np.zeros(n + 2, dtype=np.float64)
#
#  Reverse the scaling.
#
    for i in range(0, n + 2):
        z[i] = y[i] / float(n)
#
#  Add back the adjustments.
#
    for i in range(1, n + 1):
        z[a[i]] = z[a[i]] + (1.0 - y[i]) / float(n)
#
#  Check for discrepancies between Z and X.
#
    v = 0.0
    for i in range(1, n + 1):
        v = v + abs(z[i] - x[i])

    return v


def walker_verify_test():

    # *****************************************************************************80
    #
    # WALKER_VERIFY_TEST tests WALKER_VERIFY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('WALKER_VERIFY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  WALKER_VERIFY verifies the Walker sampler data vectors Y and A,')
    print('  for a given probability vector X.')

    n = 9
    x = np.zeros(n + 2, dtype=np.float64)
    for i in range(1, n + 1):
        x[i] = np.log(1.0 + 1.0 / float(i)) / np.log(float(n + 1))
    r8vec_print(n + 2, x, '  Benford PDF (ignore first and last entries):')

    y, a = walker_build(n, x)

    print('')
    print('   I    A[I]    Y[i] (ignore first and last entries)')
    print('')
    for i in range(0, n + 2):
        print('  %2d  %2d  %10.4g' % (i, a[i], y[i]))

    v = walker_verify(n, x, y, a)

    print('')
    print('  The verification sum = %g' % (v))
    print('  It should be very close to zero.')
#
#  Terminate.
#
    print('')
    print('WALKER_VERIFY_TEST')
    print('  Normal end of execution.')
    return


def zipf_probability(n, p):

    # ****************************************************************************80
    #
    #  Purpose:
    #
    #    ZIPF_PROBABILITY sets up a Zipf probability vector.
    #
    #  Modified:
    #
    #    19 February 2016
    #
    #  Author:
    #
    #    Original C version by Warren Smith.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    George Zipf,
    #    The Psychobiology of Language,
    #    1935.
    #
    #  Parameters:
    #
    #    Input, unsigned int N, indicates the size of X.
    #
    #    Input, double P, the Zipf parameter.
    #    1.0 < P.
    #
    #    Output, double X[N+2], contains in X[1] through X[N] the
    #    probabilities of outcomes 1 through N.
    #
    import numpy as np

    x = np.zeros(n + 2)

    for i in range(1, n + 1):
        x[i] = i ** (- p)

    x = normalize(n, x)

    return x


def zipf_probability_test():

    # *****************************************************************************80
    #
    # ZIPF_PROBABILITY_TEST tests ZIPF_PROBABILITY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ZIPF_PROBABILITY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ZIPF_PROBABILITY sets up a probablity vector X of N+2 elements')
    print('  containing in X[1:N] the probabilities of outcomes 1 through N')
    print('  in a Zipf distribution with parameter P.')

    n = 5
    p = 1.0
    x = zipf_probability(n, p)
    r8vec_print(n + 2, x, '  X for N = 5, P = 1.0')

    n = 5
    p = 2.0
    x = zipf_probability(n, p)
    r8vec_print(n + 2, x, '  X for N = 5, P = 2.0')

    n = 10
    p = 2.0
    x = zipf_probability(n, p)
    r8vec_print(n + 2, x, '  X for N = 10, P = 2.0')
#
#  Terminate.
#
    print('')
    print('ZIPF_PROBABILITY_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    walker_sample_test()
    timestamp()
