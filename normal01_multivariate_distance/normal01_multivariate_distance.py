#! /usr/bin/env python3
#


def normal01_multivariate_distance_compare(m, n):

    # *****************************************************************************80
    #
    # normal01_multivariate_distance_compare compares multivariate normal distance PDFs.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of samples to use.
    #
    from scipy.stats import chi2
    import matplotlib.pyplot as plt
    import numpy as np

    t = np.zeros(n)
    for i in range(0, n):
        p = np.random.randn(m)
        q = np.random.randn(m)
        t[i] = np.linalg.norm(p - q)

    plt.hist(t**2, rwidth=0.95, bins=20, density=True)
    x = np.linspace(0, 0.5 * m**2, 101)
    y = 0.5 * chi2.pdf(0.5 * x, m)

    plt.plot(x, y, 'r-')
    plt.grid(True)
    plt.xlabel('<-- Distance -->')
    plt.ylabel('<-- Relative frequency -->')
    label = (
        'Compare observed and theoretical PDF for %d-dimensional normal01 samples' % (m))
    plt.title(label)
    filename = 'normal01_multivariate_distance_compare.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def normal01_multivariate_distance_histogram(m, n):

    # *****************************************************************************80
    #
    # normal01_multivariate_distance_histogram histograms normal distances.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of samples to use.
    #
    import matplotlib.pyplot as plt
    import numpy as np

    t = np.zeros(n)
    for i in range(0, n):
        p = np.random.randn(m)
        q = np.random.randn(m)
        t[i] = np.linalg.norm(p - q)

    plt.hist(t**2, rwidth=0.95, bins=20, density=True)
    plt.grid(True)
    plt.xlabel('<-- Distance -->')
    plt.ylabel('<-- Frequency -->')
    label = ('Distance between random %d-dimensional normal01 samples' % (m))
    plt.title(label)
    filename = 'normal01_multivariate_distance_histogram.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def normal01_multivariate_distance_pdf(m):

    # *****************************************************************************80
    #
    # normal01_multivariate_distance_pdf plots a multivariate normal distance PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of samples to use.
    #
    from scipy.stats import chi2
    import matplotlib.pyplot as plt
    import numpy as np

    n = 101
    x = np.linspace(0, 0.5 * m**2, 101)
    y = 0.5 * chi2.pdf(0.5 * x, m)

    plt.plot(x, y, 'r-')
    plt.grid(True)
    plt.xlabel('<-- Distance -->')
    plt.ylabel('<-- Frequency -->')
    label = ('Theoretical PDF for %d-dimensional normal01 samples' % (m))
    plt.title(label)
    filename = 'normal01_multivariate_distance_pdf.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def normal01_multivariate_distance_stats(m, n):

    # *****************************************************************************80
    #
    # normal01_multivariate_distance_stats estimates normal01 statistics.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of sample points to use.
    #
    #    Output, real MU, VAR, the estimated mean and variance of the distance
    #    between two random samples of the multivariate normal distribution.
    #
    import numpy as np

    t = np.zeros(n)
    for i in range(0, n):
        p = np.random.randn(m)
        q = np.random.randn(m)
        t[i] = np.linalg.norm(p - q)

    mu = np.sum(t) / n
    if (1 < n):
        var = np.sum((t - mu)**2) / (n - 1)
    else:
        var = 0.0

    return mu, var


def normal01_multivariate_distance_test():

    # *****************************************************************************80
    #
    # normal01_multivariate_distance_test tests normal01_multivariate_distance.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform

    print('')
    print('normal01_multivariate_distance_test:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test normal01_multivariate_distance.')

    randn_test()

    m = 10
    n = 10000
    mu, var = normal01_multivariate_distance_stats(m, n)
    print('')
    print('  Using N = %d sample points,' % (n))
    print('  Estimated mean distance = %g' % (mu))
    print('  Estimated variance      = %g' % (var))

    m = 10
    n = 10000
    normal01_multivariate_distance_histogram(m, n)

    m = 10
    normal01_multivariate_distance_pdf(m)

    m = 10
    n = 10000
    normal01_multivariate_distance_compare(m, n)

    m_max = 50
    x = np.zeros(m_max)
    y = np.zeros(m_max)
    n = 1000

    for m in range(0, m_max):
        mu, var = normal01_multivariate_distance_stats(m, n)
        x[m] = m
        y[m] = mu

    plt.plot(x, y, 'bo', Linewidth=3)
    plt.plot(x, np.sqrt(2.0 * x), 'r-', Linewidth=3)
    plt.xlabel('<-- Spatial dimension -->')
    plt.ylabel('<-- Average distance -->')
    plt.title('Average distance between multivariate normal01 samples')
    plt.grid(True)
    filename = 'normal01_multivariate_distance_plot.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()
#
#  Terminate.
#
    print('')
    print('normal01_multivariate_distance_test:')
    print('  Normal end of execution.')

    return


def r8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT prints an R8MAT.
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
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    r8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME prints out a portion of an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, real A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def randn_test():

    # *****************************************************************************80
    #
    # randn_test tests randn.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('randn_test')
    print('  randn samples a multivariate unit normal value.')

    m = 10
    n = 5
    r = np.random.randn(m, n)

    label = ('%d samples of %d-dimensional unit normal vectors' % (n, m))
    r8mat_print(m, n, r, label)

    return


def timestamp():

    # *****************************************************************************80
    #
    # timestamp prints the date as a timestamp.
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
    normal01_multivariate_distance_test()
    timestamp()
