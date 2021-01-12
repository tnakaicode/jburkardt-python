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

from i4lib.i4vec_indicator0 import i4vec_indicator0
from i4lib.i4vec_indicator1 import i4vec_indicator1
from i4lib.i4vec_transpose_print import i4vec_transpose_print


def comb_next(n, k, a, done):

    # *****************************************************************************80
    #
    # COMB_NEXT computes combinations of K things out of N.
    #
    #  Discussion:
    #
    #    The combinations are computed one at a time, in lexicographical order.
    #
    #    10 April 1009: Thanks to "edA-qa mort-ora-y" for supplying a
    #    correction to this code.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Charles Mifsud,
    #    Combination in Lexicographic Order,
    #    ACM algorithm 154,
    #    Communications of the ACM,
    #    March 1963.
    #
    #  Parameters:
    #
    #    Input, integer N, the total number of things.
    #
    #    Input, integer K, the number of things in each combination.
    #
    #    Input, integer A(K), the output value of A on the previous call.
    #    This value is not needed on a startup call.
    #
    #    Input, logical DONE, should be set to TRUE (1) on the first call,
    #    and thereafter set to the output value of DONE on the previous call.
    #
    #    Output, integer(K), the next combination.
    #
    #    Output, logical DONE, is FALSE (0) if the routine can be called
    #    again for more combinations, and TRUE (1) if there are no more.
    #

    if (done):

        if (0 < k):
            a = i4vec_indicator1(k)
            done = False

    else:

        done = True
        km1 = k - 1

        if (a[km1] < n):

            a[km1] = a[km1] + 1
            done = False

        else:

            for i in range(k, 1, -1):

                if (a[i - 2] < n - k + i - 1):

                    a[i - 2] = a[i - 2] + 1

                    for j in range(i, k + 1):
                        a[j - 1] = a[i - 2] + j - (i - 1)
                    done = False

                    break

    return a, done


def comb_next_test():

    # *****************************************************************************80
    #
    # COMB_NEXT_TEST tests COMB_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 5

    print('')
    print('COMB_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  COMB_NEXT produces combinations.')
    print('  We are selecting from a set of size %d' % (n))

    for k in range(1, n + 1):

        print('')
        print('  Combinations of size %d:' % (k))
        print('')

        a = np.zeros(k)
        done = True

        while (True):

            a, done = comb_next(n, k, a, done)

            if (done):
                break

            i4vec_transpose_print(k, a, '')
#
#  Terminate.
#
    print('')
    print('COMB_NEXT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    comb_next_test()
    timestamp()
