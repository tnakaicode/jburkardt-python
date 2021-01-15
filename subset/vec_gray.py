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


def vec_gray_next(n, base, a, done, active, dir):

    # *****************************************************************************80
    #
    # VEC_GRAY_NEXT computes the elements of a product space.
    #
    #  Discussion:
    #
    #    The elements are produced one at a time.
    #
    #    This routine handles the case where the number of degrees of freedom may
    #    differ from one component to the next.
    #
    #    A method similar to the Gray code is used, so that successive
    #    elements returned by this routine differ by only a single element.
    #
    #    A previous version of this routine used internal static memory.
    #
    #  Example:
    #
    #    N = 2, BASE = ( 2, 3 ), DONE = TRUE
    #
    #     A    DONE  CHANGE
    #    ---  -----  ------
    #    0 0  FALSE    1
    #    0 1  FALSE    2
    #    0 2  FALSE    2
    #    1 2  FALSE    1
    #    1 1  FALSE    2
    #    1 0  FALSE    2
    #    1 0   TRUE   -1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Dennis Stanton, Dennis White,
    #    Constructive Combinatorics,
    #    Springer, 1986,
    #    ISBN: 0387963472,
    #    LC: QA164.S79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components.
    #
    #    Input, integer BASE(N), contains the number of degrees of
    #    freedom of each component.  The output values of A will
    #    satisfy 0 <= A(I) < BASE(I).
    #
    #    Input/output, integer A(N).  On the first call, the input value
    #    of A doesn't matter.  Thereafter, it should be the same as
    #    its output value from the previous call. On output, A contains
    #    the next vector.
    #
    #    Input/output, logical DONE.  On the first call, the user must
    #    set DONE to TRUE.  Thereafter, DONE should be set to the output
    #    value of DONE on the previous call.  If the output value is FALSE,
    #    then the program has computed another entry in A.  If the output
    #    value of DONE is TRUE, then there are no more entries.
    #
    #    Input/output, integer ACTIVE(N), DIR(N), work arrays needed by the
    #    function.  The user should create them before the first call, but
    #    thereafter should not change their values, passing in the output values
    #    of the previous call for the next call.
    #
    #    Output, integer CHANGE, is set to the index of the element whose
    #    value was changed.  On return from the first call, CHANGE
    #    is 0, even though all the elements have been "changed".  On
    #    return with DONE equal to TRUE, CHANGE is -1.
    #

    #
    #  The user is calling for the first time.
    #
    if (done):

        done = False
        for i in range(0, n):
            a[i] = 0
            dir[i] = 1
            active[i] = 1

        for i in range(0, n):

            if (base[i] < 1):
                print('')
                print('VEC_GRAY_NEXT - Warning!')
                print('  For index I = %d' % (i))
                print('  the nonpositive value of BASE(I) = %d' % (base[i]))
                print('  which was reset to 1!')
                base[i] = 1
                active[i] = 0
            elif (base[i] == 1):
                active[i] = 0

        change = 0

    #
    #  Find the maximum active index.
    #
    else:

        change = -1

        for i in range(0, n):
            if (active[i] != 0):
                change = i

        #
        #  If there are NO active indices, we have generated all vectors.
        #
        if (change == -1):

            done = True

        else:
            #
            #  Increment the element with maximum active index.
            #
            a[change] = a[change] + dir[change]

            #
            #  If we attained a minimum or maximum value, reverse the direction
            #  vector, and deactivate the index.
            #
            if (a[change] == 0 or a[change] == base[change] - 1):
                dir[change] = - dir[change]
                active[change] = 0

            #
            #  Activate all subsequent indices.
            #
            for i in range(change + 1, n):
                if (1 < base[i]):
                    active[i] = 1

    return a, done, active, dir, change


def vec_gray_next_test():

    # *****************************************************************************80
    #
    # VEC_GRAY_NEXT_TEST tests VEC_GRAY_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4
    base = np.array([2, 2, 1, 4])
    number = np.prod(base)

    print('')
    print('VEC_GRAY_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VEC_GRAY_NEXT generates product space elements.')
    print('')
    print('  The number of components is %d' % (n))
    print('  The number of elements is %d' % (number))
    print('  Each component has its own number of degrees of')
    print('  freedom.')
    print('')
    print('  Rank Change     ', end='')
    for i in range(0, n):
        print('  %4d' % (base[i]), end='')
    print('')
    print('')

    rank = 0
    a = np.zeros(n)
    done = True
    active = np.zeros(n)
    dir = np.zeros(n)

    while (True):

        rank = rank + 1

        a, done, active, dir, change = vec_gray_next(
            n, base, a, done, active, dir)

        if (done):
            break

        print('  %4d  %4d      ' % (rank, change), end='')
        for i in range(0, n):
            print('  %4d' % (a[i]), end='')
        print('')
    print('')
    print('VEC_GRAY_NEXT_TEST:')
    print('  Normal end of execution.')
    return


def vec_gray_rank(n, base, a):

    # *****************************************************************************80
    #
    # VEC_GRAY_RANK computes the rank of a product space element.
    #
    #  Discussion:
    #
    #    The rank applies only to the elements as produced by the routine
    #    VEC_GRAY_NEXT.
    #
    #  Example:
    #
    #    N = 2, BASE = (/ 2, 3 /), A = ( 1, 2 ),
    #
    #    RANK = 4.
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
    #  Reference:
    #
    #    Dennis Stanton, Dennis White,
    #    Constructive Combinatorics,
    #    Springer, 1986,
    #    ISBN: 0387963472,
    #    LC: QA164.S79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components.
    #
    #    Input, integer BASE(N), contains the number of degrees of
    #    freedom of each component.  The output values of A will
    #    satisfy 0 <= A(I) < BASE(I).
    #
    #    Input, integer A(N), the product space element, with the
    #    property that 0 <= A(I) < BASE(I) for each entry I.
    #
    #    Output, integer RANK, the rank, or order, of the element in
    #    the list of all elements.  The rank count begins at 1.
    #
    rank = 0

    for i in range(0, n):

        if ((rank % 2) == 1):
            c = base[i] - a[i] - 1
        else:
            c = a[i]

        rank = base[i] * rank + c

    rank = rank + 1

    return rank


def vec_gray_rank_test():

    # *****************************************************************************80
    #
    # VEC_GRAY_RANK_TEST tests VEC_GRAY_RANK.
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

    n = 4
    base = np.array([2, 2, 1, 4])
    ne = np.prod(base)

    print('')
    print('VEC_GRAY_RANK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VEC_GRAY_RANK ranks product space elements.')
    print('')
    print('  The number of components is %d' % (n))
    print('  The number of elements is %d' % (ne))
    print('  Each component has its own number of degrees of')
    print('  freedom.')

    a = np.zeros(n)
    for i in range(0, n):
        a[i] = base[i] // 2

    rank = vec_gray_rank(n, base, a)

    print('')
    print('  VEC_GRAY_RANK reports the element')
    print('')
    for i in range(0, n):
        print('  %d' % (a[i]), end='')
    print('')
    print('')
    print('  has rank %d' % (rank))
    print('')
    print('VEC_GRAY_RANK_TEST:')
    print('  Normal end of execution.')
    return


def vec_gray_unrank(n, base, rank):

    # *****************************************************************************80
    #
    # VEC_GRAY_UNRANK computes the product space element of a given rank.
    #
    #  Discussion:
    #
    #    The rank applies only to the elements as produced by the routine
    #    VEC_GRAY_NEXT.
    #
    #  Examples:
    #
    #    N = 2, BASE = ( 2, 3 ), RANK = 4.
    #
    #    A = ( 1, 2 ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Dennis Stanton, Dennis White,
    #    Constructive Combinatorics,
    #    Springer, 1986,
    #    ISBN: 0387963472,
    #    LC: QA164.S79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components.
    #
    #    Input, integer BASE(N), contains the number of degrees of
    #    freedom of each component.  The output values of A will
    #    satisfy 0 <= A(I) < BASE(I).
    #
    #    Input, integer RANK, the desired rank, or order, of the element in
    #    the list of all elements.  The rank count begins at 1 and extends
    #    to MAXRANK = Product ( 1 <= I <= N ) BASE(I).
    #
    #    Output, integer A(N), the product space element of the given rank.
    #

    a = np.zeros(n, dtype=np.int32)

    s = rank - 1

    for i in range(n - 1, -1, -1):

        a[i] = (s % base[i])
        s = (s // base[i])

        if ((s % 2) == 1):
            a[i] = base[i] - a[i] - 1

    return a


def vec_gray_unrank_test():

    # *****************************************************************************80
    #
    # VEC_GRAY_UNRANK_TEST tests VEC_GRAY_UNRANK.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4
    base = np.array([2, 2, 1, 4])
    number = np.prod(base)

    print('')
    print('VEC_GRAY_UNRANK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VEC_GRAY_UNRANK unranks product space elements.')
    print('')
    print('  The number of components is %d' % (n))
    print('  The number of elements is %d' % (number))
    print('  Each component has its own number of degrees of')
    print('  freedom.')

    rank = 7
    a = vec_gray_unrank(n, base, rank)

    print('')
    print('  VEC_GRAY_UNRANK reports the element of rank %d:' % (rank))
    print('')
    for i in range(0, n):
        print('  %d' % (a[i]), end='')
    print('')
    print('')
    print('VEC_GRAY_UNRANK_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    vec_gray_next_test()
    timestamp()
