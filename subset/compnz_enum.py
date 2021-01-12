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

from i4lib.i4_choose import i4_choose


def compnz_enum(n, k):

    # *****************************************************************************80
    #
    # COMPNZ_ENUM returns the number of nonzero compositions of the N into K parts.
    #
    #  Discussion:
    #
    #    A composition of the integer N into K nonzero parts is an ordered sequence
    #    of K positive integers which sum to N.  The compositions (1,2,1)
    #    and (1,1,2) are considered to be distinct.
    #
    #    The 10 compositions of 6 into three nonzero parts are:
    #
    #      4 1 1,  3 2 1,  3 1 2,  2 3 1,  2 2 2,  2 1 3,
    #      1 4 1,  1 3 2,  1 2 3,  1 1 4.
    #
    #    The formula for the number of compositions of N into K nonzero
    #    parts is
    #
    #      Number = ( N - 1 )! / ( ( N - K )! * ( K - 1 )! )
    #
    #    (Describe the composition using N-K '1's and K-1 dividing lines '|'.
    #    The number of distinct permutations of these symbols is the number
    #    of compositions into nonzero parts.  This is equal to the number of
    #    permutations of  N-1 things, with N-K identical of one kind
    #    and K-1 identical of another.)
    #
    #    Thus, for the above example, we have:
    #
    #      Number = ( 6 - 1 )! / ( ( 6 - 3 )! * ( 3 - 1 )! ) = 10
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Albert Nijenhuis, Herbert Wilf,
    #    Combinatorial Algorithms for Computers and Calculators,
    #    Second Edition,
    #    Academic Press, 1978,
    #    ISBN: 0-12-519260-6,
    #    LC: QA164.N54.
    #
    #  Parameters:
    #
    #    Input, integer N, the integer whose compositions are desired.
    #
    #    Input, integer K, the number of parts in the composition.
    #
    #    Output, integer VALUE, the number of compositions of N into
    #    K nonzero parts.
    #

    value = i4_choose(n - 1, n - k)

    return value


def compnz_enum_test():

    # *****************************************************************************80
    #
    # COMPNZ_ENUM_TEST tests COMPNZ_ENUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    n_max = 7

    print('')
    print('COMPNZ_ENUM_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  COMPNZ_ENUM returns the number of nonzero compositions')
    print('  of N into K parts.')
    print('')
    print('   N\K ', end='')
    for k in range(0, n_max + 1):
        print('  %4d' % (k), end='')
    print('')
    print('')
    for n in range(0, n_max + 1):
        print('  %2d:  ' % (n), end='')
        for k in range(0, n + 1):
            value = compnz_enum(n, k)
            print('  %4d' % (value), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('COMPNZ_ENUM_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    compnz_enum_test()
    timestamp()
