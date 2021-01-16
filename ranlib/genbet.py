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

from r4lib.r4lib import r4_exp
from rnglib.r4_uni_01 import r4_uni_01
from rnglib.initialize import initialize, set_initial_seed

from ranlib.phrtsd import phrtsd
from ranlib.genunf import genunf
from ranlib.stats import stats
from ranlib.trstat import trstat


def genbet(aa, bb):

    # *****************************************************************************80
    #
    # GENBET generates a beta random deviate.
    #
    #  Discussion:
    #
    #    This procedure returns a single random deviate from the beta distribution
    #    with parameters A and B.  The density is
    #
    #      x^(a-1) * (1-x)^(b-1) / Beta(a,b) for 0 < x < 1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Barry Brown, James Lovato.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Generating Beta Variates with Nonintegral Shape Parameters,
    #    Communications of the ACM,
    #    Volume 21, Number 4, April 1978, pages 317-322.
    #
    #  Parameters:
    #
    #    Input, real AA, the first parameter of the beta distribution.
    #    0.0 < AA.
    #
    #    Input, real BB, the second parameter of the beta distribution.
    #    0.0 < BB.
    #
    #    Output, real VALUE, a beta random variate.
    #

    if (aa <= 0.0):
        print('')
        print('GENBET - Fatal error!')
        print('  AA <= 0.0')
        exit('GENBET - Fatal error!')

    if (bb <= 0.0):
        print('')
        print('GENBET - Fatal error!')
        print('  BB <= 0.0')
        exit('GENBET - Fatal error!')

    #
    #  Algorithm BB
    #
    if (1.0 < aa and 1.0 < bb):

        a = min(aa, bb)
        b = max(aa, bb)
        alpha = a + b
        beta = np.sqrt((alpha - 2.0) / (2.0 * a * b - alpha))
        gamma = a + 1.0 / beta

        while (True):

            u1 = r4_uni_01()
            u2 = r4_uni_01()
            v = beta * np.log(u1 / (1.0 - u1))
            #
            #  EXP ( V ) replaced by R4_EXP ( V ), to truncate at large magnitude inputs.
            #
            w = a * r4_exp(v)

            z = u1 ** 2 * u2
            r = gamma * v - np.log(4.0)
            s = a + r - w

            if (5.0 * z <= s + 1.0 + np.log(5.0)):
                break

            t = np.log(z)
            if (t <= s):
                break

            if (t <= (r + alpha * np.log(alpha / (b + w)))):
                break

    #
    #  Algorithm BC
    #
    else:

        a = max(aa, bb)
        b = min(aa, bb)
        alpha = a + b
        beta = 1.0 / b
        delta = 1.0 + a - b

        k1 = delta * (1.0 / 72.0 + b / 24.0) / (a / b - 7.0 / 9.0)
        k2 = 0.25 + (0.5 + 0.25 / delta) * b

        while (True):

            u1 = r4_uni_01()
            u2 = r4_uni_01()

            if (u1 < 0.5):

                y = u1 * u2
                z = u1 * y

                if (k1 <= 0.25 * u2 + z - y):
                    continue

            else:

                z = u1 ** 2 * u2

                if (z <= 0.25):

                    v = beta * np.log(u1 / (1.0 - u1))
                    w = a * np.exp(v)

                    if (aa == a):
                        value = w / (b + w)
                    else:
                        value = b / (b + w)

                    return value

                if (k2 < z):
                    continue

            v = beta * np.log(u1 / (1.0 - u1))
            w = a * np.exp(v)

            if (np.log(z) <= alpha * (np.log(alpha / (b + w)) + v) - np.log(4.0)):
                break

    if (aa == a):
        value = w / (b + w)
    else:
        value = b / (b + w)

    return value


def genbet_test(phrase):

    # *****************************************************************************80
    #
    # GENBET_TEST tests GENBET, which generates Beta deviates.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 1000

    print('')
    print('RANLIB_TEST_GENBET')
    print('  GENBET generates Beta deviates.')

    #
    #  Initialize the generators.
    #
    initialize()

    #
    #  Set the seeds based on the phrase.
    #
    seed1, seed2 = phrtsd(phrase)

    #
    #  Initialize all generators.
    #
    set_initial_seed(seed1, seed2)

    #
    #  Select the parameters at random within a given range.
    #
    low = 1.0
    high = 10.0
    a = genunf(low, high)

    low = 1.0
    high = 10.0
    b = genunf(low, high)

    print('')
    print('  N = %d' % (n))
    print('')
    print('  Parameters:')
    print('')
    print('  A = %g' % (a))
    print('  B = %g' % (b))

    #
    #  Generate N samples.
    #
    array = np.zeros(n)
    for i in range(0, n):
        array[i] = genbet(a, b)

    #
    #  Compute statistics on the samples.
    #
    av, var, xmin, xmax = stats(array, n)

    #
    #  Request expected value of statistics for this distribution.
    #
    pdf = 'bet'
    param = np.array([a, b])
    avtr, vartr = trstat(pdf, param)

    print('')
    print('  Sample data range:          %14.6g  %14.6g' % (xmin, xmax))
    print('  Sample mean, variance:      %14.6g  %14.6g' % (av, var))
    print('  Distribution mean, variance %14.6g  %14.6g' % (avtr, vartr))
    print('')
    print('GENBET_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    phrase = 'Randomizer'
    genbet_test(phrase)
    timestamp()
