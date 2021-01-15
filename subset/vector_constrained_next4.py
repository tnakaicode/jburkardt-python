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

from i4lib.i4vec_transpose_print import i4vec_transpose_print


def vector_constrained_next4(n, alpha, x_min, x_max, x, q, more):

    # *****************************************************************************80
    #
    # VECTOR_CONSTRAINED_NEXT4 returns the "next" constrained vector.
    #
    #  Discussion:
    #
    #    This routine is similar to VECTOR_CONSTRAINED_NEXT2 and
    #    VECTOR_CONSTRAINED_NEXT3.
    #
    #    We consider all vectors X of dimension N whose components
    #    satisfy X_MIN(1:N) <= X(1:N) <= X_MAX(1:N).
    #
    #    We are only interested in the subset of these vectors which
    #    satisfy the following constraint:
    #
    #      sum ( 1 <= I <= N ) ALPHA(I) * X(I) <= Q
    #
    #    This routine returns, one at a time, and in right-to-left
    #    lexicographic order, exactly those vectors which satisfy
    #    the constraint.
    #
    #  Example:
    #
    #    N = 3
    #    ALPHA    4.0  3.0  5.0
    #    Q       20.0
    #    X_MIN:   1   1   1
    #    X_MAX:   5   6   4
    #
    #    #  X(1)  X(2)  X(3)     Total
    #
    #    1    1     1     1       12.0
    #    2    2     1     1       20.0
    #    3    1     2     1       15.0
    #    4    2     2     1       19.0
    #    5    1     3     1       18.0
    #    6    1     1     2       17.0
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components in the vector.
    #
    #    Input, real ALPHA(N), the coefficient vector.
    #
    #    Input, integer X_MIN(N), X_MAX(N), the minimum and maximum
    #    values allowed in each component.
    #
    #    Input, integer X(N).  On first call (with MORE = FALSE),
    #    the input value of X is not important.  On subsequent calls, the
    #    input value of X should be the output value from the previous call.
    #
    #    Input, real Q, the limit on the sum.
    #
    #    Input, logical MORE.  On input, if the user has set MORE
    #    FALSE, the user is requesting the initiation of a new sequence
    #    of values.  If MORE is TRUE, then the user is requesting "more"
    #    values in the current sequence.
    #
    #    Output, integer X(N).  On output, (with MORE = TRUE), the value of
    #    X will be the "next" vector in the reverse lexicographical list of
    #    vectors that satisfy the condition.  However, on output with
    #    MORE = FALSE, the vector X is meaningless, because there are no
    #    more vectors in the list.
    #
    #    Output, logical MORE.  On output, if MORE is TRUE,
    #    then another value was found and returned in X, but if MORE is
    #    FALSE, then there are no more values in the sequence, and X is
    #    NOT the next value.
    #
    if (not more):

        for i in range(0, n):
            x[i] = x_min[i]

        total = 0.0
        for i in range(0, n):
            total = total + alpha[i] * x[i]

        if (q < total):
            more = False
        else:
            more = True

        return x, more

    else:

        j = 0

        while (True):

            if (x[j] < x_max[j]):

                x[j] = x[j] + 1

                total = 0.0
                for i in range(0, n):
                    total = total + alpha[i] * x[i]

                if (total <= q):
                    break

            x[j] = x_min[j]

            j = j + 1

            if (n - 1 < j):
                more = False
                break

    return x, more


def vector_constrained_next4_test():

    # *****************************************************************************80
    #
    # VECTOR_CONSTRAINED_NEXT4_TEST tests VECTOR_CONSTRAINED_NEXT4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n_max = 3

    alpha = np.array([4.0, 3.0, 5.0])
    x_max = np.array([2, 6, 4])
    x_min = np.array([1, 0, 1])

    print('')
    print('VECTOR_CONSTRAINED_NEXT4_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  VECTOR_CONSTRAINED_NEXT4:')
    print('  Consider vectors:')
    print('    X_MIN(1:N) <= X(1:N) <= X_MAX(1:N),')
    print('  Set')
    print('    TOTAL = sum ( ALPHA(1:N) * X(1:N) )')
    print('  Accept only vectors for which:')
    print('    TOTAL <= Q')

    for n in range(2, n_max + 1):

        x = np.zeros(n)
        q = 20.0
        more = False

        print('')
        print('  ALPHA:', end='')
        for i in range(0, n):
            print('  %14f' % (alpha[i]), end='')
        print('')
        print('  Q:    %14f' % (q))

        i4vec_transpose_print(n, x_min, '  XMIN:')
        i4vec_transpose_print(n, x_max, '  XMAX:')

        print('')

        j = 0

        while (True):

            x, more = vector_constrained_next4(
                n, alpha, x_min, x_max, x, q, more)

            if (not more):
                break

            total = 0.0
            for i in range(0, n):
                total = total + alpha[i] * x[i]
            j = j + 1
            print('  %8d  %14f' % (j, total), end='')
            for i in range(0, n):
                print('  %8d' % (x[i]), end='')
            print('')
#
#  Terminate.
#
    print('')
    print('VECTOR_CONSTRAINED_NEXT4_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    vector_constrained_next4_test()
    timestamp()
