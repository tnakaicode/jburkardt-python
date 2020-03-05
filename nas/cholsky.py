#! /usr/bin/env python3
#


def cholsky(ida, nmat, m, n, a, nrhs, idb, b):

    # *****************************************************************************80
    #
    # CHOLSKY carries out Cholesky decomposition and back substitution.
    #
    #  Discussion:
    #
    #    The Cholesky decomposition is performed on a set of input matrices
    #    which are provided as a single three-dimensional array.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np

    epss = np.zeros(nmat + 1)

    eps = 1.0E-13
#
#  Cholesky decomposition.
#
    for j in range(0, n + 1):

        i0 = max(-m, -j)
#
#  Off diagonal elements.
#
        for i in range(i0, 0):
            for jj in range(i0 - i, 0):
                for l in range(0, nmat + 1):
                    a[l, i + m, j] = a[l, i + m, j] - \
                        a[l, jj + m, i + j] * a[l, i + jj + m, j]
            for l in range(0, nmat + 1):
                a[l, i + m, j] = a[l, i + m, j] * a[l, 0 + m, i + j]
#
#  Store inverse of diagonal elements.
#
        for l in range(0, nmat + 1):
            epss[l] = eps * a[l, 0 + m, j]

        for jj in range(i0, 0):
            for l in range(0, nmat + 1):
                a[l, 0 + m, j] = a[l, 0 + m, j] - a[l, jj + m, j] ** 2

        for l in range(0, nmat + 1):
            a[l, 0 + m, j] = 1.0 / np.sqrt(abs(epss[l] + a[l, 0 + m, j]))
#
#  Solution.
#
    for i in range(0, nrhs + 1):

        for k in range(0, n + 1):

            for l in range(0, nmat + 1):
                b[i, l, k] = b[i, l, k] * a[l, 0 + m, k]

            for jj in range(1, min(m, n - k) + 1):
                for l in range(0, nmat + 1):
                    b[i, l, k + jj] = b[i, l, k + jj] - \
                        a[l, -jj + m, k + jj] * b[i, l, k]

        for k in range(n, -1, -1):

            for l in range(0, nmat + 1):
                b[i, l, k] = b[i, l, k] * a[l, 0 + m, k]

            for jj in range(1, min(m, k) + 1):
                for l in range(0, nmat + 1):
                    b[i, l, k - jj] = b[i, l, k - jj] - \
                        a[l, -jj + m, k] * b[i, l, k]

    return b


def cholsky_test():

    # *****************************************************************************80
    #
    # CHOLSKY_TEST is the test program for CHOLSKY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np
    from time import clock

    ida = 250
    m = 4
    n = 40
    nmat = 250
    nrhs = 3

    it = 200
    it = 1
    ans = 5177.88531774562
    la = (ida + 1) * (m + 1) * (n + 1)
    lb = (nrhs + 1) * (nmat + 1) * (n + 1)
#
#  Random initialization.
#
    f7 = 78125.0
    t30 = 1073741824.0
    t = f7 / t30

    ax = np.zeros([ida + 1, m + 1, n + 1])

    for k in range(0, n + 1):
        for j in range(0, m + 1):
            for i in range(0, ida + 1):
                t = ((f7 * t) % 1.0)
                ax[i, j, k] = t

    bx = np.zeros([nrhs + 1, nmat + 1, n + 1])

    for k in range(0, n + 1):
        for j in range(0, nmat + 1):
            for i in range(0, nrhs + 1):
                t = ((f7 * t) % 1.0)
                bx[i, j, k] = t
#
#  Timing.
#
    tm = clock()

    for j in range(0, it):
        a = ax
        b = bx
        b = cholsky(ida, nmat, m, n, a, nrhs, ida, b)

    tm = clock() - tm
#
#  Results.
#
    er = abs((b[1, 19, 19] - ans) / ans)
    fp = it * (nmat + 1) * 440
    rt = 1.0E-06 * fp / tm

    print(' CHOLSKY  %13.4e  %13.4e  %10.4e  %10.2e' % (er, fp, tm, rt))
#
#  Terminate.
#
    return er, fp, tm, rt


if (__name__ == '__main__'):
    import platform
    from timestamp import timestamp
    timestamp()
    er, fp, tm, rt = cholsky_test()
    print('')
    print('CHOLSKY:')
    print('  Python version: %s' % (platform.python_version()))
    print('')
    print(' Program          Error         FP Ops     Seconds      MFLOPS')
    print('')
    print('')
    print('CHOLSKY:')
    print('  Normal end of execution.')
    timestamp()
