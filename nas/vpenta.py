#! /usr/bin/env python3
#


def vpenta(jl, ju, kl, ku, nja, njb, a, b, c, d, e, f):

    # *****************************************************************************80
    #
    # VPENTA inverts 3 pentadiagonal systems simultaneously.
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

    x = np.zeros([nja, njb], dtype=np.float64)
    y = np.zeros([nja, njb], dtype=np.float64)
#
#  Start forward generation process and sweep.
#
    j = jl
    for k in range(kl, ku + 1):
        rld = c[j - 1, k - 1]
        rldi = 1.0 / rld
        f[j - 1, k - 1, 0] = f[j - 1, k - 1, 0] * rldi
        f[j - 1, k - 1, 1] = f[j - 1, k - 1, 1] * rldi
        f[j - 1, k - 1, 2] = f[j - 1, k - 1, 2] * rldi
        x[j - 1, k - 1] = d[j - 1, k - 1] * rldi
        y[j - 1, k - 1] = e[j - 1, k - 1] * rldi

    j = jl + 1
    for k in range(kl, ku + 1):
        rld1 = b[j - 1, k - 1]
        rld = c[j - 1, k - 1] - rld1 * x[j - 2, k - 1]
        rldi = 1.0 / rld
        f[j - 1, k - 1, 0] = (f[j - 1, k - 1, 0] -
                              rld1 * f[j - 2, k - 1, 0]) * rldi
        f[j - 1, k - 1, 1] = (f[j - 1, k - 1, 1] -
                              rld1 * f[j - 2, k - 1, 1]) * rldi
        f[j - 1, k - 1, 2] = (f[j - 1, k - 1, 2] -
                              rld1 * f[j - 2, k - 1, 2]) * rldi
        x[j - 1, k - 1] = (d[j - 1, k - 1] - rld1 * y[j - 2, k - 1]) * rldi
        y[j - 1, k - 1] = e[j - 1, k - 1] * rldi

    for j in range(jl + 2, ju - 1):
        for k in range(kl, ku + 1):
            rld2 = a[j - 1, k - 1]
            rld1 = b[j - 1, k - 1] - rld2 * x[j - 3, k - 1]
            rld = c[j - 1, k - 1] - \
                (rld2 * y[j - 3, k - 1] + rld1 * x[j - 2, k - 1])
            rldi = 1.0 / rld
            f[j - 1, k - 1, 0] = (f[j - 1, k - 1, 0] - rld2 *
                                  f[j - 3, k - 1, 0] - rld1 * f[j - 2, k - 1, 0]) * rldi
            f[j - 1, k - 1, 1] = (f[j - 1, k - 1, 1] - rld2 *
                                  f[j - 3, k - 1, 1] - rld1 * f[j - 2, k - 1, 1]) * rldi
            f[j - 1, k - 1, 2] = (f[j - 1, k - 1, 2] - rld2 *
                                  f[j - 3, k - 1, 2] - rld1 * f[j - 2, k - 1, 2]) * rldi
            x[j - 1, k - 1] = (d[j - 1, k - 1] - rld1 * y[j - 2, k - 1]) * rldi
            y[j - 1, k - 1] = e[j - 1, k - 1] * rldi

    j = ju - 1
    for k in range(kl, ku + 1):
        rld2 = a[j - 1, k - 1]
        rld1 = b[j - 1, k - 1] - rld2 * x[j - 3, k - 1]
        rld = c[j - 1, k - 1] - \
            (rld2 * y[j - 3, k - 1] + rld1 * x[j - 2, k - 1])
        rldi = 1.0 / rld
        f[j - 1, k - 1, 0] = (f[j - 1, k - 1, 0] - rld2 *
                              f[j - 3, k - 1, 0] - rld1 * f[j - 2, k - 1, 0]) * rldi
        f[j - 1, k - 1, 1] = (f[j - 1, k - 1, 1] - rld2 *
                              f[j - 3, k - 1, 1] - rld1 * f[j - 2, k - 1, 1]) * rldi
        f[j - 1, k - 1, 2] = (f[j - 1, k - 1, 2] - rld2 *
                              f[j - 3, k - 1, 2] - rld1 * f[j - 2, k - 1, 2]) * rldi
        x[j - 1, k - 1] = (d[j - 1, k - 1] - rld1 * y[j - 2, k - 1]) * rldi

    j = ju
    for k in range(kl, ku + 1):
        rld2 = a[j - 1, k - 1]
        rld1 = b[j - 1, k - 1] - rld2 * x[j - 3, k - 1]
        rld = c[j - 1, k - 1] - \
            (rld2 * y[j - 3, k - 1] + rld1 * x[j - 2, k - 1])
        rldi = 1.0 / rld
        f[j - 1, k - 1, 0] = (f[j - 1, k - 1, 0] - rld2 *
                              f[j - 3, k - 1, 0] - rld1 * f[j - 2, k - 1, 0]) * rldi
        f[j - 1, k - 1, 1] = (f[j - 1, k - 1, 1] - rld2 *
                              f[j - 3, k - 1, 1] - rld1 * f[j - 2, k - 1, 1]) * rldi
        f[j - 1, k - 1, 2] = (f[j - 1, k - 1, 2] - rld2 *
                              f[j - 3, k - 1, 2] - rld1 * f[j - 2, k - 1, 2]) * rldi
#
#  Back sweep solution.
#
    for k in range(kl, ku + 1):
        f[ju - 1, k - 1, 0] = f[ju - 1, k - 1, 0]
        f[ju - 1, k - 1, 1] = f[ju - 1, k - 1, 1]
        f[ju - 1, k - 1, 2] = f[ju - 1, k - 1, 2]
        f[ju - 2, k - 1, 0] = f[ju - 2, k - 1, 0] - \
            x[ju - 2, k - 1] * f[ju - 1, k - 1, 0]
        f[ju - 2, k - 1, 1] = f[ju - 2, k - 1, 1] - \
            x[ju - 2, k - 1] * f[ju - 1, k - 1, 1]
        f[ju - 2, k - 1, 2] = f[ju - 2, k - 1, 2] - \
            x[ju - 2, k - 1] * f[ju - 1, k - 1, 2]

    for j in range(2, ju - jl + 1):
        jx = ju - j
        for k in range(kl, ku + 1):
            f[jx - 1, k - 1, 0] = f[jx - 1, k - 1, 0] - x[jx - 1, k - 1] * \
                f[jx, k - 1, 0] - y[jx - 1, k - 1] * f[jx + 1, k - 1, 0]
            f[jx - 1, k - 1, 1] = f[jx - 1, k - 1, 1] - x[jx - 1, k - 1] * \
                f[jx, k - 1, 1] - y[jx - 1, k - 1] * f[jx + 1, k - 1, 1]
            f[jx - 1, k - 1, 2] = f[jx - 1, k - 1, 2] - x[jx - 1, k - 1] * \
                f[jx, k - 1, 2] - y[jx - 1, k - 1] * f[jx + 1, k - 1, 2]

    return f


def vpenta_test():

    # *****************************************************************************80
    #
    # VPENTA_TEST tests VPENTA.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2015
    #
    #  Author:
    #
    #    Original FORTRAN77 version by David Bailey.
    #    Python version by John Burkardt.
    #
    import numpy as np
    from time import clock

    jl = 1
    ju = 128
    kl = 1
    ku = 128
    nja = 128
    njb = 128

    it = 400
    ans = -0.354649411858726
    lf = nja * njb * 3
#
#  Random initialization.
#
    f7 = 78125.0
    t30 = 1073741824.0
    t = f7 / t30

    a = np.zeros([nja, njb], dtype=np.float64)
    b = np.zeros([nja, njb], dtype=np.float64)
    c = np.zeros([nja, njb], dtype=np.float64)
    d = np.zeros([nja, njb], dtype=np.float64)
    e = np.zeros([nja, njb], dtype=np.float64)
    fx = np.zeros([nja, njb, 3], dtype=np.float64)

    for j in range(kl, ku + 1):
        for i in range(jl, ju + 1):
            t = ((f7 * t) % 1.0)
            a[i - 1, j - 1] = t
            t = ((f7 * t) % 1.0)
            b[i - 1, j - 1] = t
            t = ((f7 * t) % 1.0)
            c[i - 1, j - 1] = t
            t = ((f7 * t) % 1.0)
            d[i - 1, j - 1] = t
            t = ((f7 * t) % 1.0)
            e[i - 1, j - 1] = t
            for k in range(1, 4):
                t = ((f7 * t) % 1.0)
                fx[i - 1, j - 1, k - 1] = t

    f = np.zeros([nja, njb, 3], dtype=np.float64)
#
#  Timing.
#
    tm = clock()

    for iter in range(0, it):

        for j in range(kl, ku + 1):
            for i in range(jl, ju + 1):
                for k in range(1, 4):
                    f[i - 1, j - 1, k - 1] = fx[i - 1, j - 1, k - 1]

        f = vpenta(jl, ju, kl, ku, nja, njb, a, b, c, d, e, f)

    tm = clock() - tm
#
#  Results.
#
    er = abs((f[18, 18, 0] - ans) / ans)
    fp = it * ku * (40 * ku - 53)
    rt = 1.0E-06 * fp / tm
#
#  Terminate.
#
    return er, fp, tm, rt


if (__name__ == '__main__'):
    import platform
    from timestamp import timestamp
    timestamp()
    er, fp, tm, rt = vpenta_test()
    print('')
    print('VPENTA:')
    print('  Python version: %s' % (platform.python_version()))
    print('')
    print(' Program        Error          FP Ops        Seconds     MFLOPS')
    print('')
    print(' VPENTA   %13.4e  %13.4e  %10.4e  %10.2e' % (er, fp, tm, rt))
    print('')
    print('VPENTA:')
    print('  Normal end of execution.')
    timestamp()
