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
from subset.perm0_print import perm0_print
from subset.perm0_check import perm0_check


def perm0_to_inversion(n, p):

    # *****************************************************************************80
    #
    # PERM0_TO_INVERSION: permutation (0,...,N-1) to inversion sequence.
    #
    #  Discussion:
    #
    #    For a given permutation P acting on objects 0 through N-1, the inversion
    #    sequence INS is defined as:
    #
    #      INS(1) = 0
    #      INS(I) = number of values J < I for which P(I) < P(J).
    #
    #  Example:
    #
    #    Input:
    #
    #      ( 2, 4, 0, 3, 1 )
    #
    #    Output:
    #
    #      ( 0, 0, 2, 1, 3 )
    #
    #    The original permutation can be recovered from the inversion sequence.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 June 2004
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Dennis Stanton and Dennis White,
    #    Constructive Combinatorics,
    #    Springer Verlag, New York, 1986.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects being permuted.
    #
    #    Input, integer P(N), the permutation, in standard index form.
    #    The I-th item has been mapped to P(I).
    #
    #    Output, integer INS(N), the inversion sequence of the permutation.
    #

    check = perm0_check(n, p)

    if (not check):
        print('')
        print('PERM0_TO_INVERSION - Fatal error!')
        print('  The input array does not represent')
        print('  a proper permutation.')
        error('PERM0_TO_INVERSION - Fatal error!')

    ins = np.zeros(n, dtype=np.int32)

    for i in range(0, n):
        for j in range(0, i):
            if (p[i] < p[j]):
                ins[i] = ins[i] + 1

    return ins


def perm0_to_inversion_test():

    # *****************************************************************************80
    #
    # % PERM0_TO_INVERSION_TEST tests PERM0_TO_INVERSION.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 5

    print('')
    print('PERM0_TO_INVERSION_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM0_TO_INVERSION: permutation (0,...,N-1) => inversion.')

    perm = np.array([2, 4, 0, 3, 1])
    perm0_print(n, perm, '  Permutation:')

    ins = perm0_to_inversion(n, perm)
    i4vec_print(n, ins, '  Inversion:')

    perm2 = inversion_to_perm0(n, ins)
    perm0_print(n, perm2, '  Recovered permutation:')
#
#  Terminate.
#
    print('')
    print('PERM0_TO_INVERSION_TEST:')
    print('  Normal end of execution.')
    return


def inversion_to_perm0(n, ins):

    # *****************************************************************************80
    #
    # INVERSION_TO_PERM0: inversion sequence to permutation of (0,...,N-1).
    #
    #  Discussion:
    #
    #    For a given permutation P acting on objects 0 through N-1, the
    #    inversion sequence INS is defined as:
    #
    #      INS(1) = 0
    #      INS(I) = number of values J < I for which P(I) < P(J).
    #
    #  Example:
    #
    #    Input:
    #
    #      ( 0, 0, 2, 1, 3 )
    #
    #    Output:
    #
    #      ( 2, 4, 0, 3, 1 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Dennis Stanton, Dennis White,
    #    Constructive Combinatorics,
    #    Springer Verlag, New York, 1986.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects being permuted.
    #
    #    Input, integer INS(N), the inversion sequence of a permutation.
    #    It must be the case that 0 <= INS(I) < I for I = 1 to N.
    #
    #    Output, integer P(N), the permutation.
    #

    p = i4vec_indicator0(n)

    for i in range(n, 1, -1):

        itemp = p[i - 1 - ins[i - 1]]

        for j in range(i - ins[i - 1], i):
            p[j - 1] = p[j]

        p[i - 1] = itemp

    return p


def inversion_to_perm0_test():

    # *****************************************************************************80
    #
    # INVERSION_TO_PERM0_TEST tests INVERSION_TO_PERM0.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 5

    print('')
    print('INVERSION_TO_PERM0_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  INVERSION_TO_PERM0: inversion => permutation (0,...,N-1).')

    perm = np.array([2, 4, 0, 3, 1])
    i4vec_print(n, perm, '  Permutation:')

    ins = perm0_to_inversion(n, perm)
    i4vec_print(n, ins, '  Inversion:')

    perm2 = inversion_to_perm0(n, ins)
    i4vec_print(n, perm2, '  Recovered permutation:')
#
#  Terminate.
#
    print('')
    print('INVERSION_TO_PERM0_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    perm0_to_inversion_test()
    timestamp()
