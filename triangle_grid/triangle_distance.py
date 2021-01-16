#! /usr/bin/env python3
#


def hstar(indx, t, a, b, c, alpha, h):

    # *****************************************************************************80
    #
    # hstar evaluates the H-star functions #1 through #4.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    The distribution function of the distance between two random points
    #    in a right-angled triangle,
    #    arXiv:1208.6228v2 17 September 2012.
    #
    #  Parameters:
    #
    #    Input, integer INDX, the index of the function.
    #
    #    Input, real T, the arguments.
    #
    #    Input, real A, B, the length of the two legs of the triangle.  A <= B.
    #
    #    Input, real C, the length of the hypotenuse.
    #
    #    Input, real ALPHA, the angle BAC, in radians.
    #
    #    Input, real H, the value of A * cos ( ALPHA ).
    #
    #    Output, real VALUE, the value of the function.
    #
    if (indx == 1):
        value = theta(1, a, b, alpha) * t**2 / 8.0
    elif (indx == 2):
        value = theta(2, a, b, alpha) * t**2 / 8.0 \
            + theta(3, a, b, alpha) * lstar(1, t, h) \
            + c * lstar(2, t, h)
    elif (indx == 3):
        value = a * t + theta(4, a, b, alpha) * t**2 / 2.0 \
            + 0.5 * theta(3, a, b, alpha) * lstar(1, t, h) \
            + 0.5 * c * lstar(2, t, h) \
            + 0.5 * (b / a) * lstar(1, t, a) \
            + 0.5 * b * lstar(2, t, a)
    elif (indx == 4):
        value = theta(5, a, b, alpha) * t \
            + theta(6, a, b, alpha) * t**2 / 8.0 \
            + 0.5 * (b / a) * lstar(1, t, a) \
            + 0.5 * b * lstar(2, t, a) \
            + 0.5 * (a / b) * lstar(1, t, b) \
            + 0.5 * a * lstar(2, t, b)
    else:
        print('')
        print('hstar - Fatal error!')
        print('  Called with INDX = %d, but only values 1:4 are legal.' % (indx))
        return None

    return value


def jstar(d, a, b, c, alpha, h):

    # *****************************************************************************80
    #
    # jstar evaluates the J-star function.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    The distribution function of the distance between two random points
    #    in a right-angled triangle,
    #    arXiv:1208.6228v2 17 September 2012.
    #
    #  Parameters:
    #
    #    Input, real D(*), the distance between two points in the triangle.
    #
    #    Input, real A, B, the length of the two legs of the triangle.  A <= B.
    #
    #    Input, real C, the length of the hypotenuse.
    #
    #    Input, real ALPHA, the angle BAC, in radians.
    #
    #    Input, real H, the value of A * cos ( ALPHA ).
    #
    #    Output, real VALUE(*), the value of J*(D).
    #
    import numpy as np

    n = d.size
    value = np.zeros(n)

    i1 = np.where((0.0 <= d) & (d < h))
    i2 = np.where((h <= d) & (d < a))
    i3 = np.where((a <= d) & (d < b))
    i4 = np.where((b <= d) & (d <= c))

    value[i1] = jstars(1, 0.0, d[i1], a, b, c, alpha, h)

    value[i2] = jstars(1, 0.0, h, a, b, c, alpha, h) \
        + jstars(2, h, d[i2], a, b, c, alpha, h)

    value[i3] = jstars(1, 0.0, h, a, b, c, alpha, h) \
        + jstars(2, h, a, a, b, c, alpha, h) \
        + jstars(3, a, d[i3], a, b, c, alpha, h)

    value[i4] = jstars(1, 0.0, h, a, b, c, alpha, h) \
        + jstars(2, h, a, a, b, c, alpha, h) \
        + jstars(3, a, b, a, b, c, alpha, h) \
        + jstars(4, b, d[i4], a, b, c, alpha, h)

    return value


def jstars(indx, s, t, a, b, c, alpha, h):

    # *****************************************************************************80
    #
    # jstars evaluates the J-star functions #1 through #4.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    The distribution function of the distance between two random points
    #    in a right-angled triangle,
    #    arXiv:1208.6228v2 17 September 2012.
    #
    #  Parameters:
    #
    #    Input, integer INDX, the index of the function.
    #
    #    Input, real S, T, the arguments.
    #
    #    Input, real A, B, the length of the two legs of the triangle.  A <= B.
    #
    #    Input, real C, the length of the hypotenuse.
    #
    #    Input, real ALPHA, the angle BAC, in radians.
    #
    #    Input, real H, the value of A * cos ( ALPHA ).
    #
    #    Output, real VALUE, the value of the function.
    #
    value = hstar(indx, t, a, b, c, alpha, h) \
        - hstar(indx, s, a, b, c, alpha, h)

    return value


def lstar(indx, t, a):

    # *****************************************************************************80
    #
    # lstar evaluates the L-star functions #1 through #2.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    The distribution function of the distance between two random points
    #    in a right-angled triangle,
    #    arXiv:1208.6228v2 17 September 2012.
    #
    #  Parameters:
    #
    #    Input, integer INDX, the index of the function.
    #
    #    Input, real T, A, the arguments.
    #
    #    Output, real VALUE, the value of the function.
    #
    import numpy as np

    if (indx == 1):
        value = 0.5 * (a * np.sqrt(t**2 - a**2) + t**2 * np.arcsin(a / t))
    elif (indx == 2):
        value = np.sqrt(t**2 - a**2) + a * np.arcsin(a / t)
    else:
        print('')
        print('lstar - Fatal error!')
        print('  Called with INDX = %d, but only values 1:2 are legal.' % (indx))
        return None

    return value


def theta(indx, a, b, alpha):

    # *****************************************************************************80
    #
    # theta evaluates the theta auxilliary functions.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    The distribution function of the distance between two random points
    #    in a right-angled triangle,
    #    arXiv:1208.6228v2 17 September 2012.
    #
    #  Parameters:
    #
    #    Input, integer INDX, the index of the desired theta function.
    #    1 <= INDX <= 6.
    #
    #    Input, real A, B, the length of the two legs of the triangle.  A <= B.
    #
    #    Input, real ALPHA, the angle BAC, in radians.
    #
    import numpy as np

    if (indx == 1):
        value = (a / b) * (2.0 * alpha + np.pi) + \
            (2.0 * b / a) * (np.pi - alpha) + 6.0
    elif (indx == 2):
        value = (a / b) * (2.0 * alpha - np.pi) - (2.0 * b / a) * alpha + 6.0
    elif (indx == 3):
        value = (a / b) + (b / a)
    elif (indx == 4):
        value = 1.0 - (b / a) * alpha
    elif (indx == 5):
        value = a + b
    elif (indx == 6):
        value = (a / b) * (2.0 * alpha - np.pi) - (2.0 * b / a) * alpha + 2.0
    else:
        print('')
        print('theta - Fatal error!')
        print('  Called with INDX = %d, but only values 1:6 are legal.' % (indx))
        return None

    return value


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


def triangle_distance_stats(v, n):

    # *****************************************************************************80
    #
    # triangle estimates distance statistics for a given triangle.
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
    #    Input, real V(3,2), the vertices of the triangle.
    #
    #    Input, integer N, the number of sample points to use.
    #
    #    Output, real MU, VAR, the estimated mean and variance of the
    #    distance between two random points in the triangle.
    #
    import numpy as np

    p = triangle_sample(v, n)
    q = triangle_sample(v, n)

    t = (p - q)**2
    t = np.sum(t, 1)
    t = np.sqrt(t)
    mu = np.sum(t) / n

    if (1 < n):
        var = np.sum((t - mu)**2) / (n - 1)
    else:
        var = 0.0

    return mu, var


def triangle_distance_stats_test():

    # *****************************************************************************80
    #
    # triangle_distance_stats_test tests triangle_distance_stats.
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

    n = 10000

    print('')
    print('triangle_distance_stats_test')
    print('  Test triangle_distance_stats')
    print('')
    print('  Number of sample points N = %d' % (n))
#
#  Equilateral triangle with side 1.
#
    v = np.array([
        [0.00, 0.00],
        [1.00, 0.00],
        [0.500, np.sqrt(3.0) / 2.0]
    ])

    triangle_print(v, '  Equilateral triangle vertices:')

    mu, var = triangle_distance_stats(v, n)
    mu_exact = 0.2 + 3.0 * np.log(3.0) / 20.0
    print('')
    print('  Estimated mu  = %g' % (mu))
    print('  Exact mu      = %g' % (mu_exact))
    print('  Estimated var = %g' % (var))
#
#  Unit right triangle.
#
    v = np.array([
        [0.00, 0.00],
        [1.00, 0.00],
        [0.00, 1.00]
    ])
    triangle_print(v, '  Unit right triangle vertices:')

    mu, var = triangle_distance_stats(v, n)
    mu_exact = (2.0 + 4.0 * np.sqrt(2.0)
                + (4.0 + np.sqrt(2.0)) * np.arcsinh(1.0)) / 30.0
    print('')
    print('  Estimated mu  = %g' % (mu))
    print('  Exact mu      = %g' % (mu_exact))
    print('  Estimated var = %g' % (var))
#
#  345 right triangle.
#
    v = np.array([
        [0.00, 0.00],
        [3.00, 0.00],
        [0.00, 4.00]
    ])
    triangle_print(v, '  345 right triangle Vertices:')

    mu, var = triangle_distance_stats(v, n)

    print('')
    print('  Estimated mu  = %g' % (mu))
    print('  Estimated var = %g' % (var))
#
#  scalene triangle.
#
    v = np.array([
        [0.75, 0.90],
        [0.00, 0.20],
        [0.95, 0.65]
    ])

    triangle_print(v, '  scalene triangle Vertices:')

    mu, var = triangle_distance_stats(v, n)

    print('')
    print('  Estimated mu  = %g' % (mu))
    print('  Estimated var = %g' % (var))

    return


def triangle_distance_test():

    # *****************************************************************************80
    #
    # triangle_distance_test tests triangle_distance.
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
    import platform

    print('')
    print('triangle_distance_test:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test triangle_distance.')

    triangle_distance_histogram_test()

    triangle_distance_stats_test()

    triangle_equilateral_distance_pdf_test()

    triangle_right_distance_pdf_test()

    triangle_right_error_test()

    triangle_sample_test()

    triangle_sides_test()
#
#  Terminate.
#
    print('')
    print('triangle_distance_test:')
    print('  Normal end of execution.')

    return


def triangle_distance_histogram(v, n, filename):

    # *****************************************************************************80
    #
    # triangle_distance_histogram histograms distance statistics for a given triangle.
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
    #    Input, real V(3,2), the vertices of the triangle.
    #
    #    Input, integer N, the number of samples to use.
    #
    #    Input, string FILENAME, the name of the file to be created.
    #
    import matplotlib.pyplot as plt
    import numpy as np

    p = triangle_sample(v, n)
    q = triangle_sample(v, n)

    t = (p - q) ** 2
    t = np.sum(t, 1)
    t = np.sqrt(t)
    t_max = np.max(t)

    plt.hist(t, bins=20, rwidth=0.95, density=True)
    plt.grid(True)
    plt.xlabel('<-- Distance -->')
    plt.ylabel('<-- Frequency -->')
    plt.title('Distance between a pair of random points in a triangle')
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def triangle_distance_histogram_test():

    # *****************************************************************************80
    #
    # triangle_distance_histogram_test tests triangle_distance_histogram.
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

    n = 10000

    print('')
    print('triangle_distance_histogram_test')
    print('  Test triangle_distance_histogram.')
    print('')
    print('  Number of sample points N = %d' % (n))
#
#  Equilateral triangle with side 1.
#
    v = np.array([
        [0.00, 0.00],
        [1.00, 0.00],
        [0.500, np.sqrt(3.0) / 2.0]
    ])

    triangle_print(v, '  Equilateral triangle vertices:')

    filename = 'triangle_distance_histogram_equilateral.png'
    triangle_distance_histogram(v, n, filename)
#
#  Unit right triangle.
#
    v = np.array([
        [0.00, 0.00],
        [1.00, 0.00],
        [0.00, 1.00]
    ])

    triangle_print(v, '  Unit right triangle vertices:')

    filename = 'triangle_distance_histogram_right011.png'
    triangle_distance_histogram(v, n, filename)
#
#  345 right triangle.
#
    v = np.array([
        [0.00, 0.00],
        [3.00, 0.00],
        [0.00, 4.00]
    ])

    triangle_print(v, '  345 right triangle Vertices:')

    filename = 'triangle_distance_histogram_right345.png'
    triangle_distance_histogram(v, n, filename)
#
#  scalene triangle.
#
    v = np.array([
        [0.75, 0.90],
        [0.00, 0.20],
        [0.95, 0.65]
    ])

    triangle_print(v, '  scalene triangle Vertices:')

    filename = 'triangle_distance_histogram_scalene.png'
    triangle_distance_histogram(v, n, filename)

    return


def triangle_equilateral_distance_pdf(d):

    # *****************************************************************************80
    #
    # triangle_equilateral_distance_pdf: PDF for equilateral triangle distance..
    #
    #  Discussion:
    #
    #    This calculation is for an equilateral triangle with side 1.
    #    PDF(D) is zero if D is less than 0 or greater than 1.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    Random chords and point distances in regular polygons,
    #    Acta Mathematica Universitatis Comenianae,
    #    Volume LXXXII, Number 1, pages 1-18, 2014.
    #
    #  Parameters:
    #
    #    Input, real D, the distance.
    #
    #    Output, real PDF, the probability density function for that distance.
    #
    import numpy as np
#
#  s is the length of a side.
#
    s = 1.0
#
#  r is the radius of the circumscribed circle.
#
    r = s / np.sqrt(3.0)

    u = 3.0 * np.sqrt(3.0) * r
    A = (3.0 / 4.0) * np.sqrt(3.0) * r**2

    n = 101
    d = np.linspace(0.0, s, n)

    phi = np.zeros(n)

    i1 = np.where((0.0 < d) & (d <= 1.5 * r))
    phi[i1] = (3.0 * np.sqrt(3.0) + 2.0 * np.pi) * d[i1]**2 / (36.0 * r)

    i2 = np.where((1.5 * r < d) & (d <= s))
    phi[i2] = (1.5 * (d[i2] * np.sqrt(1.0 - (1.5 * r / d[i2])**2) - 0.5 * np.pi * r)
               + (1.0 / 4.0 / np.sqrt(3.0) - np.pi / 9.0) * d[i2]**2 / r
               + (1.5 * r + d[i2]**2 / 3.0 / r) * np.arcsin(1.5 * r / d[i2]))

    pdf = 2.0 * d / A * (np.pi + (u / A) * (phi - d))

    return pdf


def triangle_equilateral_distance_pdf_test():

    # *****************************************************************************80
    #
    # triangle_equilateral_distance_pdf_test tests triangle_equilateral_distance_pdf.
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

    print('')
    print('triangle_equilateral_distance_pdf_test')
    print('  Test triangle_equilateral_distance_pdf,')
    print('  probability density function for the distance D between')
    print('  between a pair of random points in an equilateral triangle.')

    v = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.500, np.sqrt(3) / 2.0]
    ])
    triangle_print(v, '  Triangle vertices:')
    a, b, c = triangle_sides(v)
    d = np.linspace(0.0, c, 101)
    pdf = triangle_equilateral_distance_pdf(d)

    plt.plot(d, pdf, 'r-', linewidth=2)
    plt.grid(True)
    plt.xlabel('<-- X = Distance -->')
    plt.ylabel('<-- Y = PDF(X) -->')
    plt.title('PDF for distance between random points in equilateral triangle')
    filename = 'triangle_equilateral_distance_pdf.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    n = 10000
    p = triangle_sample(v, n)
    q = triangle_sample(v, n)
    t = (p - q) ** 2
    t = np.sum(t, 1)
    t = np.sqrt(t)
    t_max = np.max(t)
    plt.hist(t, bins=20, rwidth=0.95, density=True)

    plt.plot(d, pdf, 'r-', linewidth=2)

    plt.grid(True)
    plt.xlabel('<-- X = Distance -->')
    plt.ylabel('<-- Y = PDF(X) -->')
    plt.title('PDF and histogram for pairwise distance in equilateral triangle')
    filename = 'triangle_equilateral_distance_compare.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def triangle_print(v, label):

    # *****************************************************************************80
    #
    # triangle_print prints a triangle.
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
    #    Input, real V(3,2), the X and Y coordinates of the vertices.
    #
    #    Input, string LABEL, a title for the triangle.
    #
    if (0 < len(label)):
        print('')
        print(label)

    print('')
    for i in range(0, 3):
        print('  ( %g, %g )' % (v[i, 0], v[i, 1]))

    return


def triangle_right_distance_pdf(v, d):

    # *****************************************************************************80
    #
    # triangle_right_distance_pdf: PDF for the right triangle distance problem.
    #
    #  Discussion:
    #
    #    This calculation is for a right triangle with vertices given in V.
    #
    #    The triangle will be mapped to
    #
    #       A
    #       |\
    #     b |  \ c
    #       |    \
    #       C-----B
    #          a
    #
    #    The PDF is 0 if D is less than 0, or greater than c.
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
    #  Reference:
    #
    #    Uwe Baesel,
    #    The distribution function of the distance between two random points
    #    in a right-angled triangle,
    #    arXiv:1208.6228v2 17 September 2012.
    #
    #  Parameters:
    #
    #    Input, real V(3,2), the vertices of the right triangle.
    #
    #    Input, real D, the distance.
    #
    #    Output, real PDF, the probability density function for that distance.
    #
    import numpy as np
#
#  1: Check that the triangle is close enough to a right triangle.
#
    eps = 2.220446049250313E-016

    tol = 100.0 * np.sqrt(eps) * np.max(v**2)

    err = triangle_right_error(v)

    if (tol < err):
        print('')
        print('triangle_right_distance_pdf - Fatal error!')
        print('  Input triangle rightness error = %g' % (err))
        return None
#
#  2: Compute the triangle side lengths a <= b <= c.
#
    a, b, c = triangle_sides(v)

    alpha = np.arctan2(a, b)
    perimeter = a + b + c
    area = 0.5 * a * b
    h = a * np.cos(alpha)
#
#  3: Evaluate the PDF formula.
#
    pdf = (2.0 * d / area) \
        * (np.pi + (jstar(d, a, b, c, alpha, h) - perimeter * d) / area)

    return pdf


def triangle_right_distance_pdf_test():

    # *****************************************************************************80
    #
    # triangle_right_distance_pdf_test tests triangle_right_distance_pdf.
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

    print('')
    print('triangle_right_distance_pdf_test')
    print('  Test triangle_right_distance_pdf,')
    print('  probability density function for the distance D between')
    print('  a pair of random points in a right triangle.')

    v = np.array([
        [0.0, 0.0],
        [5.0, 0.0],
        [0.0, 12.0]
    ])
    triangle_print(v, '  Triangle vertices:')
    a, b, c = triangle_sides(v)
    d = np.linspace(0.0, c, 101)
    pdf = triangle_right_distance_pdf(v, d)

    plt.plot(d, pdf, 'r-', linewidth=3)
    plt.grid(True)
    plt.xlabel('<-- X = Distance -->')
    plt.ylabel('<-- Y = PDF(X) -->')
    plt.title('PDF for distance between random points in a right triangle')
    filename = 'triangle_right_distance_pdf.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    n = 10000
    p = triangle_sample(v, n)
    q = triangle_sample(v, n)
    t = (p - q) ** 2
    t = np.sum(t, 1)
    t = np.sqrt(t)
    t_max = np.max(t)
    plt.hist(t, bins=20, rwidth=0.95, density=True)
    plt.plot(d, pdf, 'r-', linewidth=2)
    plt.grid(True)
    plt.xlabel('<-- X = Distance -->')
    plt.ylabel('<-- Y = PDF(X) -->')
    plt.title('PDF and histogram for pairwise distance in equilateral triangle')
    filename = 'triangle_right_distance_compare.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def triangle_right_error(v):

    # *****************************************************************************80
    #
    # triangle_right_error reports how close a triangle is to being right.
    #
    #  Discussion:
    #
    #    err = a^2 + b^2 - c^2.
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
    #    Input, real V(3,2), the vertices of the triangle.
    #
    #    Output, real ERR, the value of a^2+b^2-c^2.
    #
    import numpy as np
#
#  Get the side lengths.
#
    t = np.zeros(3)
    t[0] = np.linalg.norm(v[0, :] - v[1, :])
    t[1] = np.linalg.norm(v[1, :] - v[2, :])
    t[2] = np.linalg.norm(v[2, :] - v[0, :])
#
#  Sort the side lengths.
#
    t = np.sort(t)
#
#  Set c to the longest side.
#
    a = t[0]
    b = t[1]
    c = t[2]
#
#  Make the test.
#
    err = a**2 + b**2 - c**2

    return err


def triangle_right_error_test():

    # *****************************************************************************80
    #
    # triangle_right_error_test tests triangle_right_error.
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
    print('triangle_right_error_test')
    print('  Test triangle_right_error,')
    print('  which reports right triangle error a^2+b^2-c^2')

    v = np.array([
        [0.0, 0.0],
        [3.0, 0.0],
        [0.0, 4.0]
    ])
    triangle_print(v, '  Triangle #1:')
    err = triangle_right_error(v)
    print('  Right triangle error is %g' % (err))

    v = np.array([
        [4.0, 0.0],
        [0.0, 0.0],
        [0.0, 3.0]
    ])
    triangle_print(v, '  Triangle #2:')
    err = triangle_right_error(v)
    print('  Right triangle error is %g' % (err))

    v = np.array([
        [0.1, 0.0],
        [3.0, 0.2],
        [0.3, 4.0]
    ])
    triangle_print(v, '  Triangle #3:')
    err = triangle_right_error(v)
    print('  Right triangle error is %g' % (err))

    v = np.random.rand(3, 2)
    triangle_print(v, '  Triangle #4:')
    err = triangle_right_error(v)
    print('  Right triangle error is %g' % (err))

    return


def triangle_sample(v, n):

    # *****************************************************************************80
    #
    # triangle_sample uniformly samples a triangle.
    #
    #  Discussion:
    #
    #    The triangle is defined by three vertices.  This routine
    #    uses Turk's rule #2.
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
    #  Reference:
    #
    #    Greg Turk,
    #    Generating Random Points in a Triangle,
    #    in Graphics Gems,
    #    edited by Andrew Glassner,
    #    AP Professional, 1990, pages 24-28.
    #
    #  Parameters:
    #
    #    Input, real V(3,2), the X and Y coordinates of the vertices.
    #
    #    Input, integer N, the number of points desired.
    #
    #    Output, real X(N,2), the points.
    #
    import numpy as np

    s = np.random.rand(n, 2)
    i = np.where(1.0 < s[:, 0] + s[:, 1])
    s[i, :] = 1.0 - s[i, :]

    r = np.zeros([n, 3])
    r[:, 0] = s[:, 0]
    r[:, 1] = s[:, 1]
    r[:, 2] = 1.0 - r[:, 0] - r[:, 1]

    x = np.matmul(r, v)

    return x


def triangle_sample_test():

    # *****************************************************************************80
    #
    # triangle_sample_test tests triangle_sample.
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

    print('')
    print('triangle_sample_test')
    print('  Test triangle_sample, which uniformly samples a triangle.')

    n = 2500

    v = np.array([
        [0.75, 0.90],
        [0.00, 0.20],
        [0.95, 0.65]
    ])

    print('')
    print('  Number of points N = %d' % (n))

    print('')
    print('  Vertices:')
    print('  V1 = %12f  %12f' % (v[0, 0], v[0, 1]))
    print('  V2 = %12f  %12f' % (v[1, 0], v[1, 1]))
    print('  V3 = %12f  %12f' % (v[2, 0], v[2, 1]))

    x = triangle_sample(v, n)

    v2 = np.zeros([4, 2])
    v2[0:3, 0:2] = v[0:3, 0:2]
    v2[3, 0:2] = v[0, 0:2]

    plt.plot(v2[:, 0], v2[:, 1], 'k-', linewidth=3)
    plt.plot(x[:, 0], x[:, 1], 'b.', markersize=3)
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel('<-- X -->')
    plt.ylabel('<-- Y -->')
    plt.title('Uniform points by triangle_sample()')
    filename = 'triangle_sample_test.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
    plt.show(block=False)
    plt.clf()

    return


def triangle_sides(v):

    # *****************************************************************************80
    #
    # triangle_sides computes the side lengths of a triangle.
    #
    #  Discussion:
    #
    #    The side lengths are calculated, and ordered so that a <= b <= c.
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
    #    Input, real V(3,2), the vertices of the triangle.
    #
    #    Output, real A, B, C, the triangle side lengths.
    #    with A <= B <= C.
    #
    import numpy as np
#
#  Compute the lengths.
#
    t = np.zeros(3)
    t[0] = np.linalg.norm(v[0, :] - v[1, :])
    t[1] = np.linalg.norm(v[1, :] - v[2, :])
    t[2] = np.linalg.norm(v[2, :] - v[0, :])
#
#  Sort them.
#
    t = np.sort(t)
#
#  A <= B <= C.
#
    a = t[0]
    b = t[1]
    c = t[2]

    return a, b, c


def triangle_sides_test():

    # *****************************************************************************80
    #
    # triangle_sides_test tests triangle_sides.
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
    print('triangle_sides_test')
    print('  Test triangle_sides,')
    print('  which reports the lengths of the sides of a triangle.')

    v = np.array([
        [0.0, 0.0],
        [3.0, 0.0],
        [0.0, 4.0]
    ])

    triangle_print(v, '  Triangle #1:')
    a, b, c = triangle_sides(v)
    print('  a = %g, b = %g, c = %g' % (a, b, c))

    v = np.array([
        [4.0, 0.0],
        [0.0, 0.0],
        [0.0, 3.0]
    ])

    triangle_print(v, '  Triangle #2:')
    a, b, c = triangle_sides(v)
    print('  a = %g, b = %g, c = %g' % (a, b, c))

    v = np.array([
        [0.1, 0.0],
        [3.0, 0.2],
        [0.3, 4.0]
    ])

    triangle_print(v, '  Triangle #3:')
    a, b, c = triangle_sides(v)
    print('  a = %g, b = %g, c = %g' % (a, b, c))

    v = np.random.rand(3, 2)
    triangle_print(v, '  Triangle #4:')
    a, b, c = triangle_sides(v)
    print('  a = %g, b = %g, c = %g' % (a, b, c))

    return


if (__name__ == '__main__'):
    timestamp()
    triangle_distance_test()
    timestamp()
