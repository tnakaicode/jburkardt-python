#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import random as rn
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

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print, r8vec_indicator0
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4_choose import i4_choose
from i4lib.i4_uniform_ab import i4_uniform_ab


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
    sum_val = 0.0
    for i in range(1, n + 1):
        sum_val = sum_val + abs(x[i])
    #
    #  Normalize so that the new sum of X will be 1.
    #
    for i in range(1, n + 1):
        x[i] = x[i] / sum_val

    return x


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

    print('')
    print('RANDOM_PERMUTATION_TEST')
    print('  Normal end of execution.')


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

    print('')
    print('WALKER_BUILD_TEST')
    print('  Normal end of execution.')


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
    print('')
    print('WALKER_SAMPLER_TEST')
    print('  Normal end of execution.')


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

    print('')
    print('WALKER_SAMPLE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WALKER_SAMPLE library.')

    walker_build_test()
    walker_sampler_test()
    walker_verify_test()
    zipf_probability_test()

    print('')
    print('WALKER_SAMPLE_TEST:')
    print('  Normal end of execution.')


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
    print('')
    print('WALKER_VERIFY_TEST')
    print('  Normal end of execution.')


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

    print('')
    print('ZIPF_PROBABILITY_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    walker_sample_test()
    timestamp()
