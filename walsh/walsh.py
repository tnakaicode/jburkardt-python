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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4_log_2 import i4_log_2
from r8lib.r8_uniform_ab import r8vec_uniform_01


def ffwt(n, x):

    # *****************************************************************************80
    #
    # FFWT performs an in-place fast Walsh transform.
    #
    #  Discussion:
    #
    #    This routine performs a fast Walsh transform on an input series X
    #    leaving the transformed results in X.
    #    X is dimensioned N, which must be a power of 2.
    #    The results of this Walsh transform are in sequency order.
    #
    #    The output sequence could be normalized by dividing by N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    Original MATLAB version by Ken Beauchamp
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Ken Beauchamp,
    #    Walsh functions and their applications,
    #    Academic Press, 1975,
    #    ISBN: 0-12-084050-2,
    #    LC: QA404.5.B33.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items in X.
    #    N must be a power of 2.
    #
    #    Input, real X(N), the data to be transformed.
    #
    #    Output, real X(N), the transformed data.
    #

    m = i4_log_2(n)

    two_power = np.zeros(m, dtype=np.int32)
    two_power[m - 1] = 1
    for i in range(m - 2, -1, -1):
        two_power[i] = 2 * two_power[i + 1]

    nz = 1
    for l in range(0, m):

        nzi = 2 * nz
        nzn = int(n / nzi)
        nz2 = int(nz / 2)
        if (nz2 == 0):
            nz2 = 1

        for i in range(0, nzn):

            js = i * nzi - 1
            z = 1.0

            for ii in range(0, 2):

                for j in range(0, nz2):
                    js = js + 1
                    j2 = js + nz
                    hold = x[js] + z * x[j2]
                    z = - z
                    x[j2] = x[js] + z * x[j2]
                    x[js] = hold
                    z = - z

                if (l == 0):
                    break

                z = - 1.0

        nz = nz * 2

    #
    #  Bit reversal section.
    #
    nw = 0

    for k in range(1, n + 1):
        #
        #  Choose correct index and switch elements if not already switched.
        #
        if (k < nw + 1):
            hold = x[nw]
            x[nw] = x[k - 1]
            x[k - 1] = hold

        #
        #  Bump up series by 1.
        #
        for i in range(1, m + 1):

            ii = i
            if (nw < two_power[i - 1]):
                break

            mw = int(nw / two_power[i - 1])
            mw1 = int(mw / 2)
            if (mw <= 2 * mw1):
                break

            nw = nw - two_power[i - 1]

        nw = nw + two_power[ii - 1]

    return x


def ffwt_test():

    # *****************************************************************************80
    #
    # FFWT_TEST tests FFWT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 16

    print('')
    print('FFWT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FFWT computes a fast Walsh transform.')

    for j in range(1, 3):

        if (j == 1):
            seed = 123456789
            w, seed = r8vec_uniform_01(n, seed)
        else:
            w = np.linspace(1, n, n)

        x = w.copy()
        w = ffwt(n, w)

        y = w.copy()
        for i in range(0, n):
            y[i] = y[i] / float(n)

        w = ffwt(n, w)

        z = w.copy()
        for i in range(0, n):
            z[i] = z[i] / float(n)

        print('')
        print('     I        X(I)   Y=FFWT(X)/N  Z=FFWT(Y)/N')
        print('')
        for i in range(0, n):
            print('  %4d  %10f  %10f  %10f' % (i, x[i], y[i], z[i]))


def fwt(n, x):

    # *****************************************************************************80
    #
    # FWT performs a fast Walsh transform.
    #
    #  Discussion:
    #
    #    This routine performs a fast Walsh transform on an input series X
    #    leaving the transformed results in X.
    #    X is dimensioned N, which must be a power of 2.
    #    The results of this Walsh transform are in sequency order.
    #
    #    The output sequence could be normalized by dividing by N.
    #
    #    Note that the program text in the reference included the line
    #      y(jd) = abs ( x(j) - x(j2) )
    #    which has been corrected to:
    #      y(jd) = x(j) - x(j2)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    Original MATLAB version by Ken Beauchamp
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Ken Beauchamp,
    #    Walsh functions and their applications,
    #    Academic Press, 1975,
    #    ISBN: 0-12-084050-2,
    #    LC: QA404.5.B33.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items in X.
    #    N must be a power of 2.
    #
    #    Input, real X(N), the data to be transformed.
    #
    #    Output, real X(N), the transformed data.
    #

    y = np.zeros(n)
    n2 = int(n / 2)

    m = i4_log_2(n)
    nz = 1

    for l in range(0, m):

        ny = 0
        nzi = 2 * nz
        nzn = int(n / nzi)

        for i in range(0, nzn):

            nx = ny + 1
            ny = ny + nz
            js = i * nzi
            jd = js + nzi + 1

            for j in range(nx, ny + 1):
                js = js + 1
                j2 = j + n2
                y[js - 1] = x[j - 1] + x[j2 - 1]
                jd = jd - 1
                y[jd - 1] = x[j - 1] - x[j2 - 1]

        x = y.copy()

        nz = nz * 2

    return x


def fwt_test():

    # *****************************************************************************80
    #
    # FWT_TEST tests FWT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 16

    print('')
    print('FWT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FWT computes a fast Walsh transform.')

    for j in range(1, 3):

        if (j == 1):
            seed = 123456789
            w, seed = r8vec_uniform_01(n, seed)
        else:
            w = np.linspace(1, n, n)

        x = w.copy()

        w = fwt(n, w)

        y = w.copy()
        for i in range(0, n):
            y[i] = y[i] / float(n)

        w = fwt(n, w)

        z = w.copy()
        for i in range(0, n):
            z[i] = z[i] / float(n)

        print('')
        print('     I        X(I)    Y=FWT(X)/N   Z=FWT(Y)/N')
        print('')
        for i in range(0, n):
            print('  %4d  %10f  %10f  %10f' % (i, x[i], y[i], z[i]))


def haar(n, x):

    # *****************************************************************************80
    #
    # HAAR performs a Haar transform.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    Original MATLAB version by Ken Beauchamp
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Ken Beauchamp,
    #    Walsh functions and their applications,
    #    Academic Press, 1975,
    #    ISBN: 0-12-084050-2,
    #    LC: QA404.5.B33.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items in X.
    #    N must be a power of 2.
    #
    #    Input, real X(N), the data to be transformed.
    #
    #    Output, real X(N), the transformed data.
    #

    k = i4_log_2(n)
    l2 = 2 ** k

    for i in range(0, k):

        l2 = l2 // 2

        y = np.zeros(2 * l2)
        for j in range(0, 2 * l2):
            y[j] = x[j]

        for j in range(1, l2 + 1):
            l3 = l2 + j
            jj = 2 * j - 1
            x[j - 1] = y[jj - 1] + y[jj]
            x[l3 - 1] = y[jj - 1] - y[jj]

    return x


def haar_test():

    # *****************************************************************************80
    #
    # HAAR_TEST tests HAAR, HAARIN and HNORM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 16

    print('')
    print('HAAR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HAAR computes a Haar transform.')
    print('  HNORM normalizes the transformed data.')
    print('  HAARIN computes an inverse Haar transform.')

    for j in range(1, 3):

        if (j == 1):
            seed = 123456789
            w, seed = r8vec_uniform_01(n, seed)
        else:
            w = np.linspace(1, n, n)

        x = w.copy()
        w = haar(n, w)

        y = w.copy()
        w = hnorm(n, w)

        z = w.copy()
        w = haarin(n, w)

        print('')
        print('     I        X(I)    Y=HAAR(X)  Z=HNORM(Y)  W=HAARIN(Z)')
        print('')
        for i in range(0, n):
            print('  %4d  %10f  %10f  %10f  %10f' %
                  (i, x[i], y[i], z[i], w[i]))


def haarin(n, x):

    # *****************************************************************************80
    #
    # HAARIN inverts a Haar transform.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    Original MATLAB version by Ken Beauchamp
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Ken Beauchamp,
    #    Walsh functions and their applications,
    #    Academic Press, 1975,
    #    ISBN: 0-12-084050-2,
    #    LC: QA404.5.B33.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items in X.
    #    N must be a power of 2.
    #
    #    Input, real X(N), the data to be transformed.
    #
    #    Output, real X(N), the transformed data.
    #

    k = i4_log_2(n)
    l = 1

    for i in range(0, k):

        y = np.zeros(2 * l)
        for j in range(0, 2 * l):
            y[j] = x[j]

        for j in range(1, l + 1):
            lj = l + j
            jj = 2 * j
            jj1 = jj - 1
            x[jj - 1] = y[j - 1] - y[lj - 1]
            x[jj1 - 1] = y[j - 1] + y[lj - 1]

        l = l * 2

    return x


def hnorm(n, x):

    # *****************************************************************************80
    #
    # HNORM computes normalization factors for a forward or inverse Haar transform.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    Ken Beauchamp
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Ken Beauchamp,
    #    Walsh functions and their applications,
    #    Academic Press, 1975,
    #    ISBN: 0-12-084050-2,
    #    LC: QA404.5.B33.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items in X.
    #    N must be a power of 2.
    #
    #    Input, real X(N), the data to be normalized.
    #
    #    Output, real X(N), the normalized data.
    #
    k = i4_log_2(n)

    x[0] = x[0] / 2.0 ** k

    if (1 <= k):
        x[1] = x[1] / 2.0 ** k

    for ii in range(2, k + 1):

        i = ii - 1
        wlk = 1.0 / 2.0 ** (k - i)
        jmin = 2 ** i + 1
        jmax = 2 ** ii

        for j in range(jmin, jmax + 1):
            x[j - 1] = x[j - 1] * wlk

    return x


def walsh(n, x):

    # *****************************************************************************80
    #
    # WALSH performs a fast Walsh transform.
    #
    #  Discussion:
    #
    #    This routine performs a fast Wash transform on an input series X
    #    leaving the transformed results in X.  The array Y is working space.
    #    X and Y are dimensioned N, which must be a power of 2.
    #    The results of this Walsh transform are in sequency order.
    #
    #    The output sequence could be normalized by dividing by N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    Original MATLAB version by Ken Beauchamp
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Ken Beauchamp,
    #    Walsh functions and their applications,
    #    Academic Press, 1975,
    #    ISBN: 0-12-084050-2,
    #    LC: QA404.5.B33.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items in X.
    #    N must be a power of 2.
    #
    #    Input, real X(N), the data to be transformed.
    #
    #    Output, real X(N), the transformed data.
    #

    y = np.zeros(n)
    n2 = int(n / 2)

    m = i4_log_2(n)
    z = - 1.0

    for j in range(1, m + 1):

        n1 = 2 ** (m - j + 1)
        j1 = 2 ** (j - 1)

        for l in range(1, j1 + 1):

            iss = (l - 1) * n1 + 1
            i1 = 0
            w = z

            for i in range(iss, iss + n1, 2):
                a = x[i - 1]
                x[iss + i1 - 1] = a + x[i]
                i1 = i1 + 1
                y[i1 - 1] = (x[i] - a) * w
                w = w * z

            n2 = int(n1 / 2)

            for k in range(0, n2):
                x[n2 + iss + k - 1] = y[k]

    return x


def walsh_test():

    # *****************************************************************************80
    #
    # WALSH_TEST tests WALSH.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 16

    print('')
    print('WALSH_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  WALSH computes a fast Walsh transform.')

    for j in range(1, 3):

        if (j == 1):
            seed = 123456789
            w, seed = r8vec_uniform_01(n, seed)
        else:
            w = np.linspace(1, n, n)

        x = w.copy()

        w = walsh(n, w)

        y = w.copy()
        for i in range(0, n):
            y[i] = y[i] / float(n)

        w = walsh(n, w)

        z = w.copy()
        for i in range(0, n):
            z[i] = z[i] / float(n)

        print('')
        print('     I        X(I)    Y=FWT(X)/N   Z=FWT(Y)/N')
        print('')
        for i in range(0, n):
            print('  %4d  %10f  %10f  %10f' % (i, x[i], y[i], z[i]))

    return


def walsh_tests():

    # *****************************************************************************80
    #
    # WALSH_TESTS tests the WALSH library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('WALSH_TESTS')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WALSH library.')

    ffwt_test()
    fwt_test()
    haar_test()
    walsh_test()

    print('')
    print('WALSH_TESTS')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    walsh_tests()
    timestamp()
