#! /usr/bin/env python3
#


def pwl_interp_2d(nxd, nyd, xd, yd, zd, ni, xi, yi):

    # *****************************************************************************80
    #
    # PWL_INTERP_2D: piecewise linear interpolant to data defined on a 2D grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NXD, NYD, the number of X and Y data values.
    #
    #    Input, real XD(NXD), YD(NYD), the sorted X and Y data.
    #
    #    Input, real ZD(NXD,NYD), the Z data.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI), YI(NI), the coordinates of the
    #    interpolation points.
    #
    #    Output, real ZI(NI), the value of the interpolant.
    #
    import numpy as np

    zi = np.zeros(ni)

    for k in range(0, ni):
        #
        #  For interpolation point (xi[k],yi[k]), find data intervals I and J so that:
        #
        #    xd[i] <= xi[k] <= xd[i+1],
        #    yd[j] <= yi[k] <= yd[j+1].
        #
        #  But if the interpolation point is not within a data interval,
        #  assign the dummy interpolant value zi[jk = infinity.
        #
        i = r8vec_bracket5(nxd, xd, xi[k])
        if (i == -1):
            zi[k] = r8_huge()
            continue

        j = r8vec_bracket5(nyd, yd, yi[k])
        if (j == -1):
            zi[k] = r8_huge()
            continue
#
#  The rectangular cell is arbitrarily split into two triangles.
#  The linear interpolation formula depends on which triangle
#  contains the data point.
#
#    (I,J+1)--(I+1,J+1)
#      |\       |
#      | \      |
#      |  \     |
#      |   \    |
#      |    \   |
#      |     \  |
#    (I,J)---(I+1,J)
#
        if (yi[k] < yd[j + 1] + (yd[j] - yd[j + 1]) * (xi[k] - xd[i]) / (xd[i + 1] - xd[i])):

            dxa = xd[i + 1] - xd[i]
            dya = yd[j] - yd[j]

            dxb = xd[i] - xd[i]
            dyb = yd[j + 1] - yd[j]

            dxi = xi[k] - xd[i]
            dyi = yi[k] - yd[j]

            det = dxa * dyb - dya * dxb

            alpha = (dxi * dyb - dyi * dxb) / det
            beta = (dxa * dyi - dya * dxi) / det
            gamma = 1.0 - alpha - beta

            zi[k] = alpha * zd[i + 1, j] + beta * \
                zd[i, j + 1] + gamma * zd[i, j]

        else:

            dxa = xd[i] - xd[i + 1]
            dya = yd[j + 1] - yd[j + 1]

            dxb = xd[i + 1] - xd[i + 1]
            dyb = yd[j] - yd[j + 1]

            dxi = xi[k] - xd[i + 1]
            dyi = yi[k] - yd[j + 1]

            det = dxa * dyb - dya * dxb

            alpha = (dxi * dyb - dyi * dxb) / det
            beta = (dxa * dyi - dya * dxi) / det
            gamma = 1.0 - alpha - beta

            zi[k] = alpha * zd[i, j + 1] + beta * \
                zd[i + 1, j] + gamma * zd[i + 1, j + 1]

    return zi


def r8vec_bracket5(nd, xd, xi):

    # *****************************************************************************80
    #
    # R8VEC_BRACKET5 brackets data between successive entries of a sorted R8VEC.
    #
    #  Discussion:
    #
    #    We assume XD is sorted.
    #
    #    If XI is contained in the interval [XD(1),XD(N)], then the returned
    #    value B indicates that XI is contained in [ XD(B), XD(B+1) ].
    #
    #    If XI is not contained in the interval [XD(1),XD(N)], then B = -1.
    #
    #    This code implements a version of binary search which is perhaps more
    #    understandable than the usual ones.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data values.
    #
    #    Input, real XD(N), the sorted data.
    #
    #    Input, real XD, the query value.
    #
    #    Output, integer B, the bracket information.
    #
    import numpy as np

    if (xi < xd[0] or xd[nd - 1] < xi):

        b = -1

    else:

        l = 0
        r = nd - 1

        while (l + 1 < r):
            m = ((l + r) // 2)
            if (xi < xd[m]):
                r = m
            else:
                l = m

        b = l

    return b


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def pwl_interp_2d_test():

    # *****************************************************************************80
    #
    # PWL_INTERP_2D_TEST tests the PWL_INTERP_2D library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 February 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('PWL_INTERP_2D_TEST:')
    print('  Python version\n')
    print('  Test the PWL_INTERP_2D library.')

    nxd = 5
    xd = np.linspace(-1.0, +1.0, nxd)
    nyd = 5
    yd = np.linspace(-1.0, +1.0, nyd)
    zd = np.zeros([nxd, nyd])
    for i in range(0, nxd):
        for j in range(0, nyd):
            zd[i, j] = xd[i] ** 2 + yd[j] ** 2

    ni = 10
    xi = 2.0 * np.random.rand(ni) - 1.0
    yi = 2.0 * np.random.rand(ni) - 1.0
    zi = pwl_interp_2d(nxd, nyd, xd, yd, zd, ni, xi, yi)

    print('')
    print('   K  XI[K]  YI[K]  ZI[K]  F(XI{K],YI[K])')
    print('')
    for k in range(0, ni):
        t = xi[k] ** 2 + yi[k] ** 2
        print('  %2d  %8.4f  %8.4f  %8.4f  %8.4f' %
              (k, xi[k], yi[k], zi[k], t))
#
#  Terminate.
#
    print('')
    print('PWL_INTERP_2D_TEST:')
    print('  Normal end of execution.')
    print('\n')


if (__name__ == '__main__'):
    timestamp()
    pwl_interp_2d_test()
    timestamp()
