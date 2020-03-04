#! /usr/bin/env python3
#


def cfft2d1(s, m, m1, n, x, w):

    # *****************************************************************************80
    #
    # CFFT2D1 performs complex radix 2 FFT's on the first dimension.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np
#
#  If S = 0 then initialize only.
#
    m2 = (m // 2)

    if (s == 0):
        for i in range(0, m2):
            t = 2.0 * np.pi * float(i) / float(m)
            w[i] = np.cos(t) + 1j * np.sin(t)
        return x, w
#
#  Perform forward or backward FFT's according to IS = 1 or -1.
#
    ip = np.zeros([2, m], dtype=np.int32)

    for i in range(0, m):
        ip[0, i] = i + 1

    l = 1
    i1 = 1

    while (True):

        i2 = 3 - i1

        for j in range(l, m2 + 1, l):

            cx = w[j - l]
            if (s < 0):
                cx = cx.conjugate()

            for i in range(j - l + 1, j + 1):
                ii = ip[i1 - 1, i - 1]
                ip[i2 - 1, i + j - l - 1] = ii
                im = ip[i1 - 1, i + m2 - 1]
                ip[i2 - 1, i + j - 1] = im
                for k in range(1, n + 1):
                    ct = x[ii - 1, k - 1] - x[im - 1, k - 1]
                    x[ii - 1, k - 1] = x[ii - 1, k - 1] + x[im - 1, k - 1]
                    x[im - 1, k - 1] = ct * cx

        l = 2 * l
        i1 = i2

        if (m2 < l):
            break

    for i in range(1, m + 1):
        ii = ip[i1 - 1, i - 1]
        if (i < ii):
            for k in range(1, n + 1):
                ct = x[i - 1, k - 1]
                x[i - 1, k - 1] = x[ii - 1, k - 1]
                x[ii - 1, k - 1] = ct

    return x, w


def cfft2d2(s, m, m1, n, x, w):

    # *****************************************************************************80
    #
    # CFFT2D2 performs complex radix 2 FFT's on the second dimension.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np
#
#  If S = 0, then initialize only.
#
    n2 = (n // 2)

    if (s == 0):
        for i in range(0, n2):
            t = 2.0 * np.pi * float(i) / float(n)
            w[i] = np.cos(t) + 1j * np.sin(t)
        return x, w
#
#  Perform forward or backward FFT's according to IS = 1 or -1.
#
    ip = np.zeros([2, n], dtype=np.int32)

    for i in range(1, n + 1):
        ip[0, i - 1] = i

    l = 1
    i1 = 1

    while (True):

        i2 = 3 - i1

        for j in range(l, n2 + 1, l):

            cx = w[j - l]
            if (s < 0):
                cx = cx.conjugate()

            for i in range(j - l + 1, j + 1):
                ii = ip[i1 - 1, i - 1]
                ip[i2 - 1, i + j - l - 1] = ii
                im = ip[i1 - 1, i + n2 - 1]
                ip[i2 - 1, i + j - 1] = im
                for k in range(1, m + 1):
                    ct = x[k - 1, ii - 1] - x[k - 1, im - 1]
                    x[k - 1, ii - 1] = x[k - 1, ii - 1] + x[k - 1, im - 1]
                    x[k - 1, im - 1] = ct * cx

        l = 2 * l
        i1 = i2

        if (n2 < l):
            break

    for i in range(1, n + 1):
        ii = ip[i1 - 1, i - 1]
        if (i < ii):
            for k in range(1, m + 1):
                ct = x[k - 1, i - 1]
                x[k - 1, i - 1] = x[k - 1, ii - 1]
                x[k - 1, ii - 1] = ct

    return x, w


def cfft2d_test():

    # *****************************************************************************80
    #
    # CFFT2D_TEST tests CFFT2D1 and CFFTD2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np
    import sys
    from time import clock

    m = 128
    m1 = 128
    n = 256

    it = 100
    ans = 0.894799941219277
    rmn = 1.0 / float(m * n)
#
#  Random initialization.
#
    f7 = 78125.0
    t30 = 1073741824.0
    t2 = f7 / t30

    x = np.zeros([m1, n], dtype=np.complex128)

    for j in range(0, n):
        for i in range(0, m):
            t1 = ((f7 * t2) % 1.0)
            t2 = ((f7 * t1) % 1.0)
            x[i, j] = t1 + 1j * t2

    w1 = np.zeros(m, dtype=np.complex128)
    x, w1 = cfft2d1(0, m, m1, n, x, w1)
    w2 = np.zeros(n, dtype=np.complex128)
    x, w2 = cfft2d2(0, m, m1, n, x, w2)
#
#  Timing.
#

    for k in range(0, 5):
        sys.stdout.write("\r {:d} / {:d}".format(k, it))
        sys.stdout.flush()

        x = rmn * x
        x, w1 = cfft2d1(1, m, m1, n, x, w1)
        x, w2 = cfft2d2(1, m, m1, n, x, w2)
        x, w2 = cfft2d2(-1, m, m1, n, x, w2)
        x, w1 = cfft2d1(-1, m, m1, n, x, w1)

#
#  Results.
#
    value = x[18, 18]
    er = abs((value.real - ans) / ans)
    fp = it * m * n * (2.0 + 10.0 * np.log(float(m * n)) / np.log(2.0))
    #rt = 1.0E-06 * fp / tm
#
#  Terminate.
#
    return er, fp


if (__name__ == '__main__'):
    import platform
    from timestamp import timestamp
    timestamp()
    er, fp = cfft2d_test()
    print('')
    print('CFFT2D:')
    print('  Python version: %s' % (platform.python_version()))
    print('')
    print(' Program        Error          FP Ops        Seconds     MFLOPS')
    print('')
    print(' CFFT2D   %13.4e  %13.4e' % (er, fp))
    print('')
    print('CFFT2D:')
    print('  Normal end of execution.')
    timestamp()
