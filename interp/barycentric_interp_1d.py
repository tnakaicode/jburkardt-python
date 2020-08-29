#! /usr/bin/env python3
#


def lagcheby1_interp_1d(nd, xd, yd, ni, xi):

    # *****************************************************************************80
    #
    # LAGCHEBY1_INTERP_1D evaluates the Lagrange Chebyshev 1 interpolant.
    #
    #  Discussion:
    #
    #    The weight vector WD computed below is only valid if the data points
    #    XD are, as expected, the Chebyshev Type 1 points for [-1,+1], or a linearly
    #    mapped version for [A,B].  The XD values may be computed by:
    #
    #      xd = r8vec_cheby1space ( nd, a, b )
    #
    #    for instance.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Jean-Paul Berrut, Lloyd Trefethen,
    #    Barycentric Lagrange Interpolation,
    #    SIAM Review,
    #    Volume 46, Number 3, September 2004, pages 501-517.
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #    ND must be at least 1.
    #
    #    Input, real XD(ND), the data points.
    #
    #    Input, real YD(ND), the data values.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI), the interpolation points.
    #
    #    Output, real YI(NI), the interpolated values.
    #
    import numpy as np

    wd = np.zeros(nd)
    s = + 1.0
    for j in range(0, nd):
        wd[j] = s * np.sin((2 * j + 1) * np.pi / float(2 * nd))
        s = - s

    numer = np.zeros(ni)
    denom = np.zeros(ni)
    exact = np.zeros(ni, dtype=np.int32)

    for j in range(0, nd):
        t = np.zeros(ni)
        k1 = np.where(xi == xd[j])
        k2 = np.where(xi != xd[j])
        t[k2] = wd[j] / (xi[k2] - xd[j])
        numer = numer + t * yd[j]
        denom = denom + t
        exact[k1] = j + 1

    yi = np.divide(numer, denom)

    j = np.nonzero(exact)
    yi[j] = yd[exact[j] - 1]

    return yi


def lagcheby1_interp_1d_test(prob, nd):

    # *****************************************************************************80
    #
    # LAGCHEBY1_INTERP_1D_TEST tests LAGCHEBY1_INTERP_1D.
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
    #  Parameters:
    #
    #    Input, integer PROB, the problem index.
    #
    #    Input, integer ND, the number of data points to use.
    #
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('LAGCHEBY1_INTERP_1D_TEST:')
    print('  LAGCHEBY1_INTERP_1D uses Chebyshev Type 1 spacing for data points.')
    print('  Interpolate data from TEST_INTERP_1D problem #%d.' % (prob))
    print('  Number of data points = %d' % (nd))
#
#  Define the data.
#
    a = 0.0
    b = +1.0
    xd = r8vec_cheby1space(nd, a, b)
    yd = p00_f(prob, nd, xd)

    r8vec2_print_some(nd, xd, yd, 10, '  Data array:')
#
#  #1:  Does the interpolant match the function at the interpolation points?
#
    ni = nd
    xi = xd
    yi = lagcheby1_interp_1d(nd, xd, yd, ni, xi)

    int_error = np.linalg.norm(yi - yd) / float(ni)

    print('')
    print('  Averaged L2 interpolation error = %g' % (int_error))
#
#  #2: Plot the data.
#
    ni = 500
    xi = np.linspace(a, b, ni)
    yi = lagcheby1_interp_1d(nd, xd, yd, ni, xi)

    plt.plot(xd, yd, 'b.', markersize=30)
    plt.plot(xi, yi, 'r-', linewidth=3, color='r')
    plt.grid(True)
    plt.xlabel('<---X--->')
    plt.ylabel('<---Y--->')
    title_string = 'Barycentric Lagrange Chebyshev1 Interpolant for %d nodes' % (
        nd)
    plt.title(title_string)
    filename = 'p%02d_lagcheby1_%02d.png' % (prob, nd)
    plt.savefig(filename)
    print('  Created plot file "%s".' % (filename))
    # plt.show()
    plt.clf()

    return


def lagcheby2_interp_1d(nd, xd, yd, ni, xi):

    # *****************************************************************************80
    #
    # LAGCHEBY2_INTERP_1D evaluates the Lagrange Chebyshev 2 interpolant.
    #
    #  Discussion:
    #
    #    The weight vector WD computed below is only valid if the data points
    #    XD are, as expected, the Chebyshev Type 2 points for [-1,+1], or a linearly
    #    mapped version for [A,B].  The XD values may be computed by:
    #
    #      xd = r8vec_cheby2space ( nd, a, b )
    #
    #    for instance.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Jean-Paul Berrut, Lloyd Trefethen,
    #    Barycentric Lagrange Interpolation,
    #    SIAM Review,
    #    Volume 46, Number 3, September 2004, pages 501-517.
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #    ND must be at least 1.
    #
    #    Input, real XD(ND,1), the data points.
    #
    #    Input, real YD(ND,1), the data values.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI,1), the interpolation points.
    #
    #    Output, real YI(NI,1), the interpolated values.
    #
    import numpy as np

    wd = np.ones(nd)
    wd[0] = 0.5
    wd[nd - 1] = 0.5
    for j in range(1, nd, 2):
        wd[j] = - wd[j]

    numer = np.zeros(ni)
    denom = np.zeros(ni)
    exact = np.zeros(ni, dtype=np.int32)

    for j in range(0, nd):
        t = np.zeros(ni)
        k1 = np.where(xi == xd[j])
        k2 = np.where(xi != xd[j])
        t[k2] = wd[j] / (xi[k2] - xd[j])
        numer = numer + t * yd[j]
        denom = denom + t
        exact[k1] = j + 1

    yi = np.divide(numer, denom)

    j = np.nonzero(exact)
    yi[j] = yd[exact[j] - 1]

    return yi


def lagcheby2_interp_1d_test(prob, nd):

    # *****************************************************************************80
    #
    # LAGCHEBY2_INTERP_1D_TEST tests LAGCHEBY2_INTERP_1D.
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
    #  Parameters:
    #
    #    Input, integer PROB, the problem index.
    #
    #    Input, integer ND, the number of data points to use.
    #
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('LAGCHEBY2_INTERP_1D_TEST:')
    print('  LAGCHEBY2_INTERP_1D uses Chebyshev Type 2 spacing for data points.')
    print('  Interpolate data from TEST_INTERP_1D problem #%d.' % (prob))
    print('  Number of data points = %d' % (nd))
#
#  Define the data.
#
    a = 0.0
    b = +1.0
    xd = r8vec_cheby2space(nd, a, b)
    yd = p00_f(prob, nd, xd)

    r8vec2_print_some(nd, xd, yd, 10, '  Data array:')
#
#  #1:  Does the interpolant match the function at the interpolation points?
#
    ni = nd
    xi = xd
    yi = lagcheby2_interp_1d(nd, xd, yd, ni, xi)

    int_error = np.linalg.norm(yi - yd) / float(ni)

    print('')
    print('  Averaged L2 interpolation error = %g' % (int_error))
#
#  #2: Plot the data.
#
    ni = 500
    xi = np.linspace(a, b, ni)
    yi = lagcheby2_interp_1d(nd, xd, yd, ni, xi)

    plt.plot(xd, yd, 'b.', markersize=30)
    plt.plot(xi, yi, 'r-', linewidth=3)
    plt.grid(True)
    plt.xlabel('<---X--->')
    plt.ylabel('<---Y--->')
    title_string = 'Barycentric Lagrange Chebyshev2 Interpolant for %d nodes' % (
        nd)
    plt.title(title_string)
    filename = 'p%02d_lagcheby2_%02d.png' % (prob, nd)
    plt.savefig(filename)
    print('  Created plot file "%s".' % (filename))
    # plt.show()
    plt.clf()

    return


def lageven_interp_1d(nd, xd, yd, ni, xi):

    # *****************************************************************************80
    #
    # LAGEVEN_INTERP_1D evaluates the Lagrange evenly-spaced interpolant.
    #
    #  Discussion:
    #
    #    The weight vector WD computed below is only valid if the data points
    #    XD are, as expected, evenly spaced in an interval [A,B] with
    #    spacing (B-A)/N.  The XD values might be computed by:
    #
    #      xd(i) = ( ( 2 * nd - 2 * i + 1 ) * a
    #              + (          2 * i - 1 ) * b )
    #              / ( 2 * nd             )
    #
    #    for instance.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 August 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Jean-Paul Berrut, Lloyd Trefethen,
    #    Barycentric Lagrange Interpolation,
    #    SIAM Review,
    #    Volume 46, Number 3, September 2004, pages 501-517.
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #    ND must be at least 1.
    #
    #    Input, real XD(ND), the data points.
    #
    #    Input, real YD(ND), the data values.
    #
    #    Input, integer NI, the number of interpolation points.
    #
    #    Input, real XI(NI), the interpolation points.
    #
    #    Output, real YI(NI), the interpolated values.
    #
    import numpy as np
    from scipy.special import binom

    wd = np.zeros(nd)
    sgn = -1.0
    for j in range(0, nd):
        wd[j] = sgn * binom(nd, j + 1)
        sgn = - sgn

    numer = np.zeros(ni)
    denom = np.zeros(ni)
    exact = np.zeros(ni, dtype=np.int32)

    for j in range(0, nd):
        t = np.zeros(ni)
        k1 = np.where(xi == xd[j])
        k2 = np.where(xi != xd[j])
        t[k2] = wd[j] / (xi[k2] - xd[j])
        numer = numer + t * yd[j]
        denom = denom + t
        exact[k1] = j + 1

    yi = np.divide(numer, denom)

    j = np.nonzero(exact)
    yi[j] = yd[exact[j] - 1]

    return yi


def lageven_interp_1d_test(prob, nd):

    # *****************************************************************************80
    #
    # LAGEVEN_INTERP_1D_TEST tests LAGEVEN_INTERP_1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 August 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer PROB, the problem index.
    #
    #    Input, integer ND, the number of data points to use.
    #
    import matplotlib.pyplot as plt
    import numpy as np

    print('')
    print('LAGEVEN_INTERP_1D_TEST:')
    print('  LAGEVEN_INTERP_1D uses even spacing for data points.')
    print('  Interpolate data from TEST_INTERP_1D problem #%d.' % (prob))
    print('  Number of data points = %d' % (nd))
#
#  Define the data.
#
    a = 0.0
    b = +1.0
    xd = r8vec_midspace(nd, a, b)
    yd = p00_f(prob, nd, xd)

    r8vec2_print_some(nd, xd, yd, 10, '  Data array:')
#
#  #1:  Does the interpolant match the function at the interpolation points?
#
    ni = nd
    xi = xd
    yi = lageven_interp_1d(nd, xd, yd, ni, xi)

    int_error = np.linalg.norm(yi - yd) / float(ni)

    print('')
    print('  Averaged L2 interpolation error = %g' % (int_error))
#
#  #2: Plot the data.
#
    ni = 500
    xi = np.linspace(a, b, ni)
    yi = lageven_interp_1d(nd, xd, yd, ni, xi)

    plt.plot(xd, yd, 'b.', markersize=30)
    plt.plot(xi, yi, 'r-', linewidth=3)
    plt.grid(True)
    plt.xlabel('<---X--->')
    plt.ylabel('<---Y--->')
    title_string = 'Barycentric Lagrange Even Interpolant for %d nodes' % (nd)
    plt.title(title_string)
    filename = 'p%02d_lageven_%02d.png' % (prob, nd)
    plt.savefig(filename)
    print('  Created plot file "%s".' % (filename))
    # plt.show()
    plt.clf()

    return


def r8vec_cheby1space(n, a, b):

    # *****************************************************************************80
    #
    # R8VEC_CHEBY1SPACE creates a vector of Type 1 Chebyshev spaced values in [A,B].
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the first and last entries.
    #
    #    Output, real X(N), a vector of Type 1 Chebyshev spaced data.
    #
    import numpy as np

    x = np.zeros(n)

    if (n == 1):
        x[0] = (a + b) / 2.0
    else:
        for i in range(0, n):

            theta = float(n - i - 1) * np.pi / float(n - 1)

            c = np.cos(theta)

            if ((n % 2) == 1):
                if (2 * i + 1 == n):
                    c = 0.0

            x[i] = ((1.0 - c) * a
                    + (1.0 + c) * b) \
                / 2.0

    return x


def r8vec_cheby1space_test():

    # *****************************************************************************80
    #
    # R8VEC_CHEBY1SPACE_TEST tests R8VEC_CHEBY1SPACE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_CHEBY1SPACE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_CHEBY1SPACE returns Type 1 Chebyshev values in [A,B].')

    n = 5
    x_lo = 10.0
    x_hi = 20.0
    x = r8vec_cheby1space(n, x_lo, x_hi)

    r8vec_print(n, x, '  The vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_CHEBY1SPACE_TEST')
    print('  Normal end of execution.')
    return


def r8vec_cheby2space(n, a, b):

    # *****************************************************************************80
    #
    # R8VEC_CHEBY2SPACE creates a vector of Type 2  Chebyshev values in [A,B].
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the first and last entries.
    #
    #    Output, real X(N), a vector of Type 2 Chebyshev spaced data.
    #
    import numpy as np

    x = np.zeros(n)

    for i in range(0, n):

        theta = float(n - i) * np.pi / float(n + 1)

        c = np.cos(theta)

        x[i] = ((1.0 - c) * a
                + (1.0 + c) * b) \
            / 2.0

    return x


def r8vec_cheby2space_test():

    # *****************************************************************************80
    #
    # R8VEC_CHEBY2SPACE_TEST tests R8VEC_CHEBY2SPACE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_CHEBY2SPACE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_CHEBY2SPACE returns Type 2 Chebyshev values in [A,B].')

    n = 9
    x_lo = 10.0
    x_hi = 20.0

    print('  Generate %d points in [%g,%g]' % (n, x_lo, x_hi))

    x = r8vec_cheby2space(n, x_lo, x_hi)

    r8vec_print(n, x, '  The vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_CHEBY2SPACE_TEST')
    print('  Normal end of execution.')
    return


def r8vec_midspace(n, a, b):

    # *****************************************************************************80
    #
    # R8VEC_MIDSPACE creates a vector of linearly spaced values.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #    This function divides the interval [a,b] into n subintervals, and then
    #    returns the midpoints of those subintervals.
    #
    #  Example:
    #
    #    N = 5, A = 10, B = 20
    #    X = [ 11, 13, 15, 17, 19 ]
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
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the endpoints of the interval.
    #
    #    Output, real X(N), a vector of linearly spaced data.
    #
    import numpy as np

    if (n == 1):
        x = (a + b) / 2.0
    else:
        a2 = a + (b - a) / 2.0 / float(n)
        b2 = b - (b - a) / 2.0 / float(n)
        x = np.linspace(a2, b2, n)

    return x


def r8vec_midspace_test():

    # *****************************************************************************80
    #
    # R8VEC_MIDSPACE_TEST tests R8VEC_MIDSPACE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_MIDSPACE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MIDSPACE returns the midpoints of N intervals in [A,B].')

    n = 5
    x_lo = 10.0
    x_hi = 20.0
    x = r8vec_midspace(n, x_lo, x_hi)

    r8vec_print(n, x, '  The midspace vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_MIDSPACE_TEST')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8vec2_print_some(n, x1, x2, max_print, title):

    # *****************************************************************************80
    #
    # R8VEC2_PRINT_SOME prints "some" of an R8VEC2.
    #
    #  Discussion:
    #
    #    An R8VEC2 is two R8VEC's.
    #
    #    An R8VEC is a vector of R8 values.
    #
    #    The user specifies MAX_PRINT, the maximum number of lines to print.
    #
    #    If N, the size of the vectors, is no more than MAX_PRINT, then
    #    the entire vectors are printed, one entry of each per line.
    #
    #    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
    #    followed by a line of periods suggesting an omission,
    #    and the last entry.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries of the vectors.
    #
    #    Input, real X1(N), X2(N), the vector to be printed.
    #
    #    Input, integer MAX_PRINT, the maximum number of lines to print.
    #
    #    Input, string TITLE, a title.
    #
    if (max_print <= 0):
        return

    if (n <= 0):
        return

    print('')
    print(title)
    print('')

    if (n <= max_print):

        for i in range(0, n):
            print('%6d: %14g  %14g' % (i, x1[i], x2[i]))

    elif (3 <= max_print):

        for i in range(0, max_print - 2):
            print('%6d: %14g  %14g' % (i, x1[i], x2[i]))
        print('......  ..............  ..............')
        i = n - 1
        print('%6d: %14g  %14g' % (i, x1[i], x2[i]))

    else:

        for i in range(0, max_print - 1):
            print('%6d: %14g  %14g' % (i, x1[i], x2[i]))
        i = max_print - 1
        print('%6d: %14g  %14g  ...more entries...' % (i, x1[i], x2[i]))

    return


def r8vec2_print_some_test():

    # *****************************************************************************80
    #
    # R8VEC2_PRINT_SOME_TEST tests R8VEC2_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 100
    a = np.zeros(n)
    b = np.zeros(n)

    for i in range(0, n):
        x = float(i + 1)
        a[i] = x * x
        b[i] = np.sqrt(x)

    print('')
    print('R8VEC2_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC2_PRINT_SOME prints some of a pair of R8VEC\'s.')

    r8vec2_print_some(n, a, b, 10, '  Square and square root:')
#
#  Terminate.
#
    print('')
    print('R8VEC2_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


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


def barycentric_interp_1d_test():

    # *****************************************************************************80
    #
    # BARYCENTRIC_INTERP_1D_TEST tests the BARYCENTRIC_INTERP_1D library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('BARYCENTRIC_INTERP_1D_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the BARYCENTRIC_INTERP_1D library.')
    print('  The R8LIB library is needed.')
    print('  These test needs the TEST_INTERP_1D library.')

    # 
    # prob_num = 8
    # p00 - p08
    # 
    prob_num = p00_prob_num()
    for prob in range(1, prob_num + 1):
        for nd in [4, 8, 16, 32, 64, 1000]:
            lagcheby1_interp_1d_test(prob, nd)
            lagcheby2_interp_1d_test(prob, nd)
            lageven_interp_1d_test(prob, nd)

    print('')
    print('BARYCENTRIC_INTERP_1D_TEST:')
    print('  Normal end of execution.')
    return


def p00_f(prob, n, x):

    # *****************************************************************************80
    #
    # P00_F evaluates the function for any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer PROB, the number of the desired test problem.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    from sys import exit

    if (prob == 1):
        value = p01_f(n, x)
    elif (prob == 2):
        value = p02_f(n, x)
    elif (prob == 3):
        value = p03_f(n, x)
    elif (prob == 4):
        value = p04_f(n, x)
    elif (prob == 5):
        value = p05_f(n, x)
    elif (prob == 6):
        value = p06_f(n, x)
    elif (prob == 7):
        value = p07_f(n, x)
    elif (prob == 8):
        value = p08_f(n, x)
    else:
        print('')
        print('P00_F - Fatal error!')
        print('  Illegal problem number = %d' % (prob))
        exit('P00_F - Fatal error!')

    return value


def p01_f(n, x):

    # *****************************************************************************80
    #
    # P01_F evaluates the function for problem p01.
    #
    #  Discussion:
    #
    #    Step function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = 2.0 * np.ones(n)

    i = (x <= 1.0 / 3.0)
    j = (4.0 / 5.0 <= x)

    value[i] = -1.0
    value[j] = +1.0

    return value


def p02_f(n, x):

    # *****************************************************************************80
    #
    # P02_F evaluates the function for problem p02.
    #
    #  Discussion:
    #
    #    Nondifferentiable function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = np.zeros(n)

    i = (x <= 1.0 / 3.0)
    j = (1.0 / 3.0 < x)

    value[i] = 1.0 - 3.0 * x[i]
    value[j] = 6.0 * x[j] - 2.0

    return value


def p03_f(n, x):

    # *****************************************************************************80
    #
    # P03_F evaluates the function for problem p03.
    #
    #  Discussion:
    #
    #    Step function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = x * (10.0 * x - 1.0) * (5.0 * x - 2.0) * (5.0 * x - 2.0) \
        * (4 * x - 3.4) * (x - 1.0)

    return value


def p04_f(n, x):

    # *****************************************************************************80
    #
    # P04_F evaluates the function for problem p04.
    #
    #  Discussion:
    #
    #    Step function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = np.arctan(40.0 * x - 15.0)

    return value


def p05_f(n, x):

    # *****************************************************************************80
    #
    # P05_F evaluates the function for problem p05.
    #
    #  Discussion:
    #
    #    Step function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = np.cos(7.0 * x) \
        + 5.0 * np.cos(11.2 * x) \
        - 2.0 * np.cos(14.0 * x) \
        + 5.0 * np.cos(31.5 * x) \
        + 7.0 * np.cos(63.0 * x)

    return value


def p06_f(n, x):

    # *****************************************************************************80
    #
    # P06_F evaluates the function for problem p06.
    #
    #  Discussion:
    #
    #    f(x) = exp ( - (4 * x - 1)^2 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Alan Genz,
    #    A Package for Testing Multiple Integration Subroutines,
    #    in Numerical Integration: Recent Developments, Software
    #    and Applications,
    #    edited by Patrick Keast and Graeme Fairweather,
    #    D Reidel, 1987, pages 337-340,
    #    LC: QA299.3.N38.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = np.exp(- (4.0 * x - 1.0) ** 2)

    return value


def p07_f(n, x):

    # *****************************************************************************80
    #
    # P07_F evaluates the function for problem p07.
    #
    #  Discussion:
    #
    #    f(x) = exp ( 4 * x ) if x <= 1/2
    #           0                  otherwise
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Alan Genz,
    #    A Package for Testing Multiple Integration Subroutines,
    #    in Numerical Integration: Recent Developments, Software
    #    and Applications,
    #    edited by Patrick Keast and Graeme Fairweather,
    #    D Reidel, 1987, pages 337-340,
    #    LC: QA299.3.N38.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = np.zeros(n)

    i = (x < 0.5)

    value[i] = np.exp(4.0 * x[i])

    return value


def p08_f(n, x):

    # *****************************************************************************80
    #
    # P08_F evaluates the function for problem p08.
    #
    #  Discussion:
    #
    #    This is a famous example, due to Runge.  If equally spaced
    #    abscissas are used, the sequence of interpolating polynomials Pn(X)
    #    diverges, in the sense that the max norm of the difference
    #    between Pn(X) and F(X) becomes arbitrarily large as N increases.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), the evaluation points.
    #
    #    Output, real VALUE(N), the function values.
    #
    import numpy as np

    value = 1.0 / ((10.0 * (x - 0.5)) ** 2 + 1.0)

    return value


def p00_f_test():

    # *****************************************************************************80
    #
    # P00_F_TEST tests P00_F.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('P00_F_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_F evaluates any function at N points X.')

    prob_num = p00_prob_num()

    n = 11
    a = 0.0
    b = 1.0
    x = np.linspace(a, b, n)

    print('')

    for prob in range(1, prob_num + 1):

        y = p00_f(prob, n, x)
        title = 'X, Y for problem ' + str(prob)
        r8vec2_print(n, x, y, title)
#
#  Terminate.
#
    print('')
    print('P00_F_TEST:')
    print('  Normal end of execution.')
    return


def p00_plot(prob):

    # *****************************************************************************80
    #
    # P00_PLOT plots the data for any of the tests.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer PROB, the problem index.
    #
    #    Output, string FILENAME, the name of the plot filename.
    #
    import matplotlib.pyplot as plt
    import numpy as np

    prob_num = p00_prob_num

    if (prob < 1 or prob_num < prob):
        print('')
        print('P00_PLOT - Fatal error!')
        print('  Values of PROB must be between 1 and %d.' % (prob_num))
        exit('P00_PLOT - Fatal error!')

    xmin = 0.0
    xmax = 1.0
    n = 501

    x = np.linspace(xmin, xmax, n)
    y = p00_f(prob, n, x)
    t = p00_title(prob)
#
#  PYLAB commands.
#
    plt.plot(x, y, linewidth=2.0)
    plt.title(t)
    plt.grid(True)
    plt.xlabel('<---X--->')
    plt.ylabel('<---Y--->')

    filename = 'p0' + str(prob) + '_plot.png'

    plt.savefig(filename)
    # plt.show()
    plt.clf()

    return filename


def p00_plot_test():

    # *****************************************************************************80
    #
    # P00_PLOT_TEST tests P00_PLOT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('P00_PLOT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_PLOT plots any test problem.')

    num = p00_prob_num()

    print('')
    print('  TEST_INTERP_1D includes %d test problems.' % (num))

    print('')
    for prob in range(1, num + 1):
        filename = p00_plot(prob)
        print('  #%d  "%s"' % (prob, filename))
#
#  Terminate.
#
    print('')
    print('P00_PLOT_TEST:')
    print('  Normal end of execution.')
    return


def p00_prob_num():

    # *****************************************************************************80
    #
    # P00_PROB_NUM returns the number of problems.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer VALUE, the number of problems.
    #
    value = 8

    return value


def p00_prob_num_test():

    # *****************************************************************************80
    #
    # P00_PROB_NUM_TEST tests P00_PROB_NUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('P00_PROB_NUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_PROB_NUM returns the number of test problems.')

    num = p00_prob_num()

    print('')
    print('  TEST_INTERP_1D includes %d test problems.' % (num))
#
#  Terminate.
#
    print('')
    print('P00_PROB_NUM_TEST:')
    print('  Normal end of execution.')
    return


def p00_title(prob):

    # *****************************************************************************80
    #
    # P00_TITLE returns the title of any problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer PROB, the number of the desired test problem.
    #
    #    Output, string TITLE, the title of the problem.
    #
    from sys import exit

    if (prob == 1):
        title = p01_title()
    elif (prob == 2):
        title = p02_title()
    elif (prob == 3):
        title = p03_title()
    elif (prob == 4):
        title = p04_title()
    elif (prob == 5):
        title = p05_title()
    elif (prob == 6):
        title = p06_title()
    elif (prob == 7):
        title = p07_title()
    elif (prob == 8):
        title = p08_title()
    else:
        print('')
        print('P00_TITLE - Fatal error!')
        print('  Illegal problem number = %d' % (prob))
        exit('P00_TITLE - Fatal error!')

    return title


def p01_title():

    # *****************************************************************************80
    #
    # P01_TITLE returns the title of problem p01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = steps -1/2/1 at [0,1/3], [1/3,4/5], [4/5,1].'

    return title


def p02_title():

    # *****************************************************************************80
    #
    # P02_TITLE returns the title of problem p02.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = (1-3x), x < 1/3 (6x-2) if 1/3 < x'

    return title


def p03_title():

    # *****************************************************************************80
    #
    # P03_TITLE returns the title of problem p03.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = x (10*x-1) (5x-2) (5x-2) (4x-3.4) (x-1)'

    return title


def p04_title():

    # *****************************************************************************80
    #
    # P04_TITLE returns the title of problem p04.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = atan ( 40 * x - 15 )'

    return title


def p05_title():

    # *****************************************************************************80
    #
    # P05_TITLE returns the title of problem p05.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = cos(7*x)+5*cos(11.2*x)-2*cos(14*x)+5*cos(31.5*x)+7*cos(63*x).'

    return title


def p06_title():

    # *****************************************************************************80
    #
    # P06_TITLE returns the title of problem p06.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = exp ( - ( 4*x-1 )^2 )'

    return title


def p07_title():

    # *****************************************************************************80
    #
    # P07_TITLE returns the title of problem p07.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = exp ( 2 x ) if x < 0.5, 0 otherwise'

    return title


def p08_title():

    # *****************************************************************************80
    #
    # P08_TITLE returns the title of problem p08.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, string TITLE, the title of the problem.
    #
    title = 'f(x) = 1 / ( 1 + ( 10 * (x-1/2) )^2 )'

    return title


def p00_title_test():

    # *****************************************************************************80
    #
    # P00_TITLE_TEST tests P00_TITLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('P00_TITLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  P00_TITLE returns the title of any test problems.')

    num = p00_prob_num()

    print('')
    print('  TEST_INTERP_1D includes %d test problems.' % (num))

    print('')
    for prob in range(1, num + 1):
        title = p00_title(prob)
        print('  #%d  "%s"' % (prob, title))
#
#  Terminate.
#
    print('')
    print('P00_TITLE_TEST:')
    print('  Normal end of execution.')
    return


def r8vec2_print(n, a1, a2, title):

    # *****************************************************************************80
    #
    # R8VEC2_PRINT prints an R8VEC2.
    #
    #  Discussion:
    #
    #    An R8VEC2 is a dataset consisting of N pairs of real values, stored
    #    as two separate vectors A1 and A2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, real A1(N), A2(N), the vectors to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('  %6d:   %12g  %12g' % (i, a1[i], a2[i]))

    return


def r8vec2_print_test():

    # *****************************************************************************80
    #
    # R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC2_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC2_PRINT prints a pair of R8VEC\'s.')

    n = 6
    v = np.array([0.0, 0.20, 0.40, 0.60, 0.80, 1.0], dtype=np.float64)
    w = np.array([0.0, 0.04, 0.16, 0.36, 0.64, 1.0], dtype=np.float64)
    r8vec2_print(n, v, w, '  Print a pair of R8VEC\'s:')
#
#  Terminate.
#
    print('')
    print('R8VEC2_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def test_interp_1d_test():

    # *****************************************************************************80
    #
    # TEST_INTERP_1D_TEST tests the TEST_INTERP_1D library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TEST_INTERP_1D_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the TEST_INTERP_1D library.')

    p00_prob_num_test()
    p00_title_test()
    p00_f_test()
    p00_plot_test()
#
#  Terminate.
#
    print('')
    print('TEST_INTERP_1D_TEST:')
    print('  Normal end of execution.')
    return


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


if (__name__ == '__main__'):
    timestamp()
    barycentric_interp_1d_test()
    timestamp()
