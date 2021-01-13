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

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4vec_sum import i4vec_sum
from r8lib.r8_gamma import r8_gamma


def multinomial_coef1(nfactor, factor):

    # *****************************************************************************80
    #
    # MULTINOMIAL_COEF1 computes a multinomial coefficient.
    #
    #  Discussion:
    #
    #    The multinomial coefficient is a generalization of the binomial
    #    coefficient.  It may be interpreted as the number of combinations of
    #    N objects, where FACTOR(1) objects are indistinguishable of type 1,
    #    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
    #    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
    #
    #    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
    #
    #    The log of the gamma function is used, to avoid overflow.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NFACTOR, the number of factors.
    #
    #    Input, integer FACTOR(NFACTOR), contains the factors.
    #    0 <= FACTOR(I)
    #
    #    Output, integer NCOMB, the value of the multinomial coefficient.
    #

    # from math import lgamma

    #
    #  Each factor must be nonnegative.
    #
    for i in range(0, nfactor):

        if (factor[i] < 0):
            print('')
            print('MULTINOMIAL_COEF1 - Fatal error!')
            print('  Factor %d = %d' % (i, factor[i]))
            print('  But this value must be nonnegative.')
            exit('MULTINOMIAL_COEF1 - Fatal error!')
#
#  The factors sum to N.
#
    n = i4vec_sum(nfactor, factor)

    arg = float(n + 1)
#
#  Our obsolete version of Python doesn't have LGAMMA yet!
#
    facn = np.log(r8_gamma(arg))
# facn = lgamma ( arg )

    for i in range(0, nfactor):

        arg = float(factor[i] + 1)
        fack = np.log(r8_gamma(arg))
#   fack = lgamma ( arg )
        facn = facn - fack

    ncomb = int(round(np.exp(facn)))

    return ncomb


def multinomial_coef1_test():

    # *****************************************************************************80
    #
    # MULTINOMIAL_COEF1_TEST tests MULTINOMIAL_COEF1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2003
    #
    #  Author:
    #
    #    John Burkardt
    #

    maxfactor = 5

    print('')
    print('MULTINOMIAL_COEF1_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MULTINOMIAL_COEF1 computes multinomial')
    print('  coefficients using the Gamma function')

    print('')
    print('  Line 10 of the BINOMIAL table:')
    print('')

    n = 10
    nfactor = 2
    factor = np.zeros(nfactor, dtype=np.int32)

    for i in range(0, n + 1):

        factor[0] = i
        factor[1] = n - i

        ncomb = multinomial_coef1(nfactor, factor)

        print('  %2d  %2d   %3d' % (factor[0], factor[1], ncomb))

    print('')
    print('  Level 5 of the TRINOMIAL coefficients:')

    n = 5
    nfactor = 3
    factor = np.zeros(nfactor, dtype=np.int32)

    for i in range(0, n + 1):

        factor[0] = i

        print('')

        for j in range(0, n - factor[0] + 1):

            factor[1] = j
            factor[2] = n - factor[0] - factor[1]

            ncomb = multinomial_coef1(nfactor, factor)

            print('  %2d  %2d  %2d   %3d' %
                  (factor[0], factor[1], factor[2], ncomb))
#
#  Terminate.
#
    print('')
    print('MULTINOMIAL_COEF1_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    multinomial_coef1_test()
    timestamp()
