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

from i4lib.i4_sign import i4_sign
from i4lib.i4vec_indicator0 import i4vec_indicator0
from subset.perm0_print import perm0_print
from subset.perm0_check import perm0_check


def perm0_next(n, p, more, even):

    # *****************************************************************************80
    #
    # PERM0_NEXT computes permutations of (0,...,N-1), one at a time.
    #
    #  Discussion:
    #
    #    The routine is initialized by calling with MORE = TRUE, in which case
    #    it returns the identity permutation.
    #
    #    If the routine is called with MORE = FALSE, then the successor of the
    #    input permutation is computed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Albert Nijenhuis, Herbert Wilf,
    #    Combinatorial Algorithms,
    #    Academic Press, 1978, second edition,
    #    ISBN 0-12-519260-6.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects being permuted.
    #
    #    Input, integer P(N), the output value of P from the previous call.
    #    However, on an initialization call, with MORE = FALSE, the value of P
    #    is not needed.
    #
    #    Input, logical MORE, should be FALSE on the first call, to force
    #    initialization.  Thereafter, it should be TRUE, to request the next
    #    permutation in the sequence.
    #
    #    Input, logical EVEN, is the output value of EVEN from the previous call.
    #    However, on an initialization call, with MORE = FALSE, the value of EVEN
    #    is not needed.
    #
    #    Output, integer P(N), the next permutation.
    #
    #    Output, logical MORE, indicates that there are more permutations
    #    that may be generated.
    #
    #    Output, logical EVEN, is TRUE if the output permutation is even,
    #    that is, involves an even number of transpositions.
    #

    if (n == 1):
        p[0] = 0
        more = False
        even = True
        return p, more, even

    if (not more):

        p = i4vec_indicator0(n)
        more = True
        even = True

        if (p[n - 1] != 0 or p[0] != 1 + (n % 2)):
            return p, more, even

        for i in range(0, n - 3):
            if (p[i + 1] != p[i] + 1):
                return p, more, even

        more = False

    else:

        if (even):

            ia = p[0] + 1
            p[0] = p[1]
            p[1] = ia - 1
            even = False

            if (p[n - 1] != 0 or p[0] != 1 + (n % 2)):
                return p, more, even

            for i in range(0, n - 3):
                if (p[i + 1] != p[i] + 1):
                    return p, more, even

            more = False
            return p, more, even

        else:

            more = False

            s = 0

            for i1 in range(1, n):

                ia = p[i1] + 1
                i = i1 - 1
                id = 0

                for j in range(0, i + 1):
                    if (ia < p[j] + 1):
                        id = id + 1

                s = id + s

                if (id != (i + 1) * (s % 2)):
                    more = True
                    break

            if (not more):
                p[0] = -1
                return p, more, even

        m = ((s + 1) % 2) * (n + 1)

        for j in range(0, i + 1):

            if (i4_sign(p[j] + 1 - ia) != i4_sign(p[j] + 1 - m)):
                m = p[j] + 1
                l = j

        p[l] = ia - 1
        p[i1] = m - 1
        even = True

    return p, more, even


def perm0_next_test():

    # *****************************************************************************80
    #
    # PERM0_NEXT_TEST tests PERM0_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4

    print('')
    print('PERM0_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM0_NEXT generates permutations.')
    print('')

    more = False
    p = np.zeros(n, dtype=np.int32)
    even = False

    while (True):

        p, more, even = perm0_next(n, p, more, even)

        perm0_print(n, p, '')

        if (not more):
            break
#
#  Terminate.
#
    print('')
    print('PERM0_NEXT_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    perm0_next_test()
    timestamp()
