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

from i4lib.i4_choose import i4_choose
from i4lib.i4vec_print import i4vec_print, i4vec_print_test
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.i4vec_transpose import i4vec_transpose_print, i4vec_transpose_print_test
from r8lib.r8vec_transpose import r8vec_transpose_print, r8vec_transpose_print_test
from r8lib.r8mat_transpose import r8mat_transpose_print, r8mat_transpose_print_some


def tableau_check(n, tab):

    # *****************************************************************************80
    #
    # TABLEAU_CHECK checks a 2 by N tableau.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Donald Kreher, Douglas Simpson,
    #    Combinatorial Algorithms,
    #    CRC Press, 1998,
    #    ISBN: 0-8493-3988-X,
    #    LC: QA164.K73.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of columns in the tableau.
    #    N must be positive.
    #
    #    Input, integer TAB(2,N), a 2 by N tableau.
    #
    #    Output, integer CHECK.
    #    1, the data is legal.
    #    0, the data is not legal.
    #
    check = True

    if (n < 1):
        check = False
        return check
#
#  The entries must be between 1 and 2*N.
#
    for i in range(0, 2):
        for j in range(0, n):
            if (tab[i, j] < 1 or 2 * n < tab[i, j]):
                check = False
                return check
#
#  The entries must be increasing to the right.
#
    for i in range(0, 2):
        for j in range(1, n):
            if (tab[i, j] <= tab[i, j - 1]):
                check = False
                return check
#
#  The entries must be increasing down.
#
    for j in range(0, n):
        if (tab[1, j] <= tab[0, j]):
            check = False
            return check

    return check


def tableau_check_test():

    # *****************************************************************************80
    #
    # TABLEAU_CHECK_TEST tests TABLEAU_CHECK.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('TABLEAU_CHECK TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TABLEAU_CHECK checks a 2xN tableau.')
    print('')
    print('  Check?')
    print('')

    for test in range(1, 6):

        if (test == 1):
            n = 0
            t = np.array([
                [],
                []])
        elif (test == 2):
            n = 4
            t = np.array([
                [1, 2, 3, 4],
                [2, 4, 7, 9]])
        elif (test == 3):
            n = 4
            t = np.array([
                [1, 3, 5, 3],
                [2, 4, 5, 3]])
        elif (test == 4):
            n = 4
            t = np.array([
                [1, 3, 4, 5],
                [2, 4, 5, 3]])
        elif (test == 5):
            n = 4
            t = np.array([
                [1, 3, 6, 7],
                [3, 4, 7, 8]])

        print('')
        check = tableau_check(n, t)
        print('      Check = %2d' % (check))
        i4mat_print(2, n, t, '  Tableau:')
#
#  Terminate.
#
    print('')
    print('TABLEAU_CHECK_TEST:')
    print('  Normal end of execution.')
    return


def tableau_enum(n):

    # *****************************************************************************80
    #
    # TABLEAU_ENUM enumerates tableaus on N nodes.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of nodes in each tree.
    #    N must normally be at least 3, but for this routine,
    #    any value of N is allowed.
    #
    #    Output, integer BALUE, the number of 2 by N standard tableaus.
    #

    value = i4_choose(2 * n, n) / (n + 1)

    return value


def tableau_enum_test():

    # *****************************************************************************80
    #
    # TABLEAU_ENUM_TEST tests TABLEAU_ENUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('TABLEAU_ENUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TABLEAU_ENUM enumerates tableaus on N nodes.')
    print('')
    print('   N           #')
    print('')

    for n in range(0, 11):
        tableau_num = tableau_enum(n)
        print('  %2d  %10d' % (n, tableau_num))
#
#  Terminate.
#
    print('')
    print('TABLEAU_ENUM_TEST:')
    print('  Normal end of execution.')
    return


def tableau_to_bal_seq(n, tab):

    # *****************************************************************************80
    #
    # % TABLEAU_TO_BAL_SEQ converts a 2 by N tableau to a balanced sequence.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Donald Kreher, Douglas Simpson,
    #    Combinatorial Algorithms,
    #    CRC Press, 1998,
    #    ISBN: 0-8493-3988-X,
    #    LC: QA164.K73.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of 0's (and 1's) in the sequence.
    #    N must be positive.
    #
    #    Input, integer TAB(2,N), a 2 by N tableau.
    #
    #    Output, integer T(2*N), a balanced sequence.
    #

    check = tableau_check(n, tab)

    if (not check):
        print('')
        print('TABLEAU_TO_BAL_SEQ - Fatal error!')
        print('  The input array is illegal.')
        print('TABLEAU_TO_BAL_SEQ - Fatal error!')

    t = np.zeros(2 * n)

    for i in range(0, 2):
        for j in range(0, n):
            t[tab[i, j] - 1] = i

    return t


def tableau_to_bal_seq_test():

    # *****************************************************************************80
    #
    # TABLEAU_TO_BAL_SEQ_TEST tests TABLEAU_TO_BAL_SEQ.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4

    print('')
    print('TABLEAU_TO_BAL_SEQ_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TABLEAU_TO_BAL_SEQ converts a tableau')
    print('  to a balanced sequence.')

    tab = np.array([
        [1, 2, 5, 6],
        [3, 4, 7, 8]])

    i4mat_print(2, n, tab, '  Tableau:')

    t = tableau_to_bal_seq(n, tab)

    i4vec_transpose_print(2 * n, t, '  Balanced sequence:')
#
#  Terminate.
#
    print('')
    print('TABLEAU_TO_BAL_SEQ_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    tableau_check_test()
    tableau_enum_test()
    tableau_to_bal_seq_test()
    timestamp()
