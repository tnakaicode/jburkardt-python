#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d, plot3d

def gamma_log_values(n_data):

    # *****************************************************************************80
    #
    # GAMMA_LOG_VALUES returns some values of the Log Gamma function.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Log[Gamma[x]]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz and Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    US Department of Commerce, 1964.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Wolfram Media / Cambridge University Press, 1999.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real X, the argument of the function.
    #
    #    Output, real FX, the value of the function.
    #
    import numpy as np

    n_max = 20

    fx_vec = np.array((
        0.1524063822430784E+01,
        0.7966778177017837E+00,
        0.3982338580692348E+00,
        0.1520596783998375E+00,
        0.0000000000000000E+00,
        -0.4987244125983972E-01,
        -0.8537409000331584E-01,
        -0.1081748095078604E+00,
        -0.1196129141723712E+00,
        -0.1207822376352452E+00,
        -0.1125917656967557E+00,
        -0.9580769740706586E-01,
        -0.7108387291437216E-01,
        -0.3898427592308333E-01,
        0.00000000000000000E+00,
        0.69314718055994530E+00,
        0.17917594692280550E+01,
        0.12801827480081469E+02,
        0.39339884187199494E+02,
        0.71257038967168009E+02))

    x_vec = np.array((
        0.20E+00,
        0.40E+00,
        0.60E+00,
        0.80E+00,
        1.00E+00,
        1.10E+00,
        1.20E+00,
        1.30E+00,
        1.40E+00,
        1.50E+00,
        1.60E+00,
        1.70E+00,
        1.80E+00,
        1.90E+00,
        2.00E+00,
        3.00E+00,
        4.00E+00,
        10.00E+00,
        20.00E+00,
        30.00E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        x = 0.0
        fx = 0.0
    else:
        x = x_vec[n_data]
        fx = fx_vec[n_data]
        n_data = n_data + 1

    return n_data, x, fx


def gamma_log_values_test():

    # *****************************************************************************80
    #
    # GAMMA_LOG_VALUE_TEST demonstrates the use of GAMMA_LOG_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 February 2009
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('GAMMA_LOG_VALUES:')
    print('  Python version: %s' % (platform.python_version()))
    print('  GAMMA_LOG_VALUES stores values of')
    print('  the logarithm of the Gamma function.')
    print('')
    print('      X            GAMMA_LOG(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = gamma_log_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16f' % (x, fx))
#
#  Terminate.
#
    print('')
    print('GAMMA_LOG_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_PRINT prints an I4VEC.
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
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i4vec_print_test():

    # *****************************************************************************80
    #
    # I4VEC_PRINT_TEST tests I4VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_PRINT prints an I4VEC.')

    n = 4
    v = np.array([91, 92, 93, 94], dtype=np.int32)
    i4vec_print(n, v, '  Here is an I4VEC:')
#
#  Terminate.
#
    print('')
    print('I4VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT prints an I4VEC "transposed".
    #
    #  Example:
    #
    #    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:
    #
    #       1    2    3    4    5
    #       6    7    8    9   10
    #      11
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < len(title)):
        print('')
        print(title)

    if (0 < n):
        for i in range(0, n):
            print('%8d' % (a[i])),
            if ((i + 1) % 10 == 0 or i == n - 1):
                print('')
    else:
        print('  (empty vector)')

    return


def i4vec_transpose_print_test():

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT_TEST tests I4VEC_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_TRANSPOSE_PRINT prints an I4VEC')
    print('  with 5 entries to a row, and an optional title.')

    n = 12
    a = np.zeros(n, dtype=np.int32)

    for i in range(0, n):
        a[i] = i + 1

    i4vec_transpose_print(n, a, '  My array:  ')
#
#  Terminate.
#
    print('')
    print('I4VEC_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C(N), the randomly chosen integer vector.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4VEC_UNIFORM_AB - Fatal error!')

    a = int(a)
    b = int(b)

    c = np.zeros(n, dtype=np.int32)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        seed = (seed % i4_huge)

        if (seed < 0):
            seed = seed + i4_huge

        r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
        r = (1.0 - r) * (min(a, b) - 0.5) \
            + r * (max(a, b) + 0.5)

        value = round(r)

        value = max(value, min(a, b))
        value = min(value, max(a, b))

        c[i] = value

    return c, seed


def i4vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 20
    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    v, seed = i4vec_uniform_ab(n, a, b, seed)

    i4vec_print(n, v, '  The random vector:')
#
#  Terminate.
#
    print('')
    print('I4VEC_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


def monomial_value(n, m, e, x):

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE evaluates a monomial.
    #
    #  Discussion:
    #
    #    This routine evaluates a monomial of the form
    #
    #      product ( 1 <= i <= m ) x(i)^e(i)
    #
    #    The combination 0.0^0, if encountered, is treated as 1.0.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, integer E(M), the exponents.
    #
    #    Input, real X(N,M), the point coordinates.
    #
    #    Output, real V(N), the monomial values.
    #
    import numpy as np

    v = np.ones(n)

    for i in range(0, m):
        if (0 != e[i]):
            for j in range(0, n):
                v[j] = v[j] * x[j, i] ** e[i]

    return v


def monomial_value_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_TEST tests MONOMIAL_VALUE on sets of data in various dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use monomial_value() to evaluate some monomials')
    print('  in dimensions 1 through 3.')

    e_min = -3
    e_max = 6
    n = 5
    seed = 123456789
    x_min = -2.0
    x_max = +10.0

    for m in range(1, 4):

        print('')
        print('  Spatial dimension M =  %d' % (m))

        e, seed = i4vec_uniform_ab(m, e_min, e_max, seed)
        i4vec_transpose_print(m, e, '  Exponents:')
        x, seed = r8mat_uniform_ab(n, m, x_min, x_max, seed)
#
#  To make checking easier, make the X values integers.
#
        for i in range(0, n):
            for j in range(0, m):
                x[i, j] = round(x[i, j])

        v = monomial_value(n, m, e, x)

        print('')
        print('   V(X)         '),
        for i in range(0, m):
            print('      X(%d)' % (i)),
        print('')
        print('')
        for j in range(0, n):
            print('%14.6g  ' % (v[j])),
            for i in range(0, m):
                print('%10.4f' % (x[j, i])),
            print('')
#
#  Terminate.
#
    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Normal end of execution.')
    return


def polygon_area(n, v):

    # *****************************************************************************80
    #
    # POLYGON_AREA computes the area of a polygon.
    #
    #  Discussion:
    #
    #    AREA = 1/2 * abs ( sum ( 1 <= I <= N ) X(I) * ( Y(I+1) - Y(I-1) ) )
    #    where Y(0) should be replaced by Y(N), and Y(N+1) by Y(1).
    #
    #    If the vertices are given in counterclockwise order, the area
    #    will be positive.  If the vertices are given in clockwise order,
    #    the area will be negative.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #
    #    Input, real V(N,2), the vertices.
    #
    #    Output, real AREA, the area of the polygon.
    #
    area = 0.0

    for i in range(0, n):

        if (i == 0):
            im1 = n - 1
        else:
            im1 = i - 1

        if (i == n - 1):
            ip1 = 0
        else:
            ip1 = i + 1

        area = area + v[i, 0] * (v[ip1, 1] - v[im1, 1])

    area = 0.5 * area

    return area


def polygon_area_test():

    # *****************************************************************************80
    #
    # POLYGON_AREA_TEST tests POLYGON_AREA.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    test_num = 2
    area_exact_test = np.array([2.0, 6.0])
    n_test = np.array([4, 8])

    print('')
    print('POLYGON_AREA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_AREA computes the area of a polygon.')

    for test in range(0, test_num):

        n = n_test[test]
        area_exact = area_exact_test[test]

        if (test == 0):

            v = np.array([
                [1.0, 0.0],
                [2.0, 1.0],
                [1.0, 2.0],
                [0.0, 1.0]])

        elif (test == 1):

            v = np.array([
                [0.0, 0.0],
                [3.0, 0.0],
                [3.0, 3.0],
                [2.0, 3.0],
                [2.0, 1.0],
                [1.0, 1.0],
                [1.0, 2.0],
                [0.0, 2.0]])

        print('')
        print('  Number of polygonal vertices = %d' % (n))

        r8mat_print(n, 2, v, '  The polygon vertices:')

        area = polygon_area(n, v)

        print('')
        print('  Exact area is        %g' % (area_exact))
        print('  The computed area is %g' % (area))
#
#  Terminate.
#
    print('')
    print('POLYGON_AREA_TEST')
    print('  Normal end of execution.')
    return


def polygon_monomial_integral(nv, v, e):

    # *****************************************************************************80
    #
    # POLYGON_MONOMIAL_INTEGRAL integrates a monomial over a polygon.
    #
    #  Discussion:
    #
    #    Nu(P,Q) = Integral ( x, y in polygon ) x^p y^q dx dy
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Carsten Steger,
    #    On the calculation of arbitrary moments of polygons,
    #    Technical Report FGBV-96-05,
    #    Forschungsgruppe Bildverstehen, Informatik IX,
    #    Technische Universitaet Muenchen, October 1996.
    #
    #  Parameters:
    #
    #    Input, integer NV, the number of vertices of the polygon.
    #
    #    Input, real V(NV,2), the vertex coordinates.
    #
    #    Input, integer E(2), the exponents of the monomial.
    #
    #    Output, real NU_PQ, the unnormalized moment Nu(P,Q).
    #
    p = e[0]
    q = e[1]

    nu_pq = 0.0

    xj = v[nv - 1, 0]
    yj = v[nv - 1, 1]

    for i in range(0, nv):

        xi = v[i, 0]
        yi = v[i, 1]

        s_pq = 0.0

        for k in range(0, p + 1):
            for l in range(0, q + 1):
                s_pq = s_pq \
                    + r8_choose(k + l, l) * r8_choose(p + q - k - l, q - l) \
                    * xi ** k * xj ** (p - k) \
                    * yi ** l * yj ** (q - l)

        nu_pq = nu_pq + (xj * yi - xi * yj) * s_pq

        xj = xi
        yj = yi

    nu_pq = nu_pq / float(p + q + 2) / float(p + q + 1) \
        / r8_choose(p + q, p)

    return nu_pq


def polygon_monomial_integral_test():

    # *****************************************************************************80
    #
    # POLYGON_MONOMIAL_INTEGRAL_TEST tests POLYNOMIAL_MONOMIAL_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nv = 3

    v = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0]])

    print('')
    print('POLYGON_MONOMIAL_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_MONOMIAL_INTEGRAL evaluates the integral of a monomial')
    print('  x^p y^q over the interior of a polygon in 2D.')

    r8mat_print(nv, 2, v, '  Polygon vertices:')

    print('')
    print('   P   Q       Integral')
    print('')

    e = np.zeros(2, dtype=np.int32)

    for pq in range(0, 5):
        for p in range(0, pq + 1):
            q = pq - p
            e[0] = p
            e[1] = q

            result = polygon_monomial_integral(nv, v, e)
            print('  %2d  %2d  %14.6g' % (p, q, result))
#
#  Terminate.
#
    print('')
    print('POLYGON_MONOMIAL_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


def polygon_monte_carlo_test():

    # *****************************************************************************80
    #
    # POLYGON_MONTE_CARLO_TEST estimates integrals over a polygon in 2D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nv = 4

    v = np.array([
        [-0.5, -0.5],
        [1.0, -1.0],
        [1.0, 1.0],
        [-1.0, 1.0]])
    
    e_name = ["X", "Y"]
    e_test = np.array([
        [0, 0],
        [2, 0],
        [0, 2],
        [4, 0],
        [2, 2],
        [0, 4],
        [6, 0]])

    print('')
    print('POLYGON_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use POLYGON_SAMPLE to estimate integrals')
    print('  over the interior of a polygon in 2D.')

    obj = plot2d()
    obj.create_tempdir(-1)
    seed = 123456789

    print('')
    txt = " \tN"
    for e in e_test:
        txt += "\t"
        for idx, vname in enumerate(e_name):
            txt += "{}^{:d}".format(vname, e[idx])
    print(txt)
    print('')

    n = 1
    while (n <= 65536):
        x, seed = polygon_sample(nv, v, n, seed)
        print('  %8d' % (n), end='')
        for e in e_test:
            value = monomial_value(n, 2, e, x)
            result = polygon_area(nv, v) * np.sum(value[0:n]) / float(n)
            print('\t%14.6g' % (result), end='')
        print('')

        obj.axs.scatter(x[:, 0], x[:, 1], s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial()
        plt.close()
        obj.new_fig()

        n = 2 * n

    print('     Exact'),
    for e in e_test:
        result = polygon_monomial_integral(nv, v, e)
        print('  %14.6g' % (result)),
    print('')

    print('')
    print('POLYGON_MONTE_CARLO_TEST')
    print('  Normal end of execution.')
    return


def polygon_sample(nv, v, n, seed):

    # *****************************************************************************80
    #
    # POLYGON_SAMPLE uniformly samples a polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NV, the number of vertices.
    #
    #    Input, real V(NV,2), the vertices of the polygon, listed in
    #    counterclockwise order.
    #
    #    Input, integer N, the number of points to create.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real S(2,N), the points.
    #
    import numpy as np
    from polygon_triangulate import polygon_triangulate
#
#  Triangulate the polygon.
#
    x = np.zeros(nv)
    y = np.zeros(nv)
    for j in range(0, nv):
        x[j] = v[j, 0]
        y[j] = v[j, 1]

    triangles = polygon_triangulate(nv, x, y)
#
#  Determine the areas of each triangle.
#
    area_triangle = np.zeros(nv - 2)

    area_polygon = 0.0
    for i in range(0, nv - 2):
        area_triangle[i] = triangle_area(
            v[triangles[i, 0], 0], v[triangles[i, 0], 1],
            v[triangles[i, 1], 0], v[triangles[i, 1], 1],
            v[triangles[i, 2], 0], v[triangles[i, 2], 1])
        area_polygon = area_polygon + area_triangle[i]
#
#  Normalize the areas.
#
    area_relative = np.zeros(nv - 1)

    for i in range(0, nv - 2):
        area_relative[i] = area_triangle[i] / area_polygon
#
#  Replace each area by the sum of itself and all previous ones.
#
    area_cumulative = np.zeros(nv - 2)

    area_cumulative[0] = area_relative[0]
    for i in range(1, nv - 2):
        area_cumulative[i] = area_relative[i] + area_cumulative[i - 1]

    s = np.zeros([n, 2])

    for j in range(0, n):
        #
        #  Choose triangle I at random, based on areas.
        #
        area_percent, seed = r8_uniform_01(seed)

        for k in range(0, nv - 2):

            i = k

            if (area_percent <= area_cumulative[k]):
                break
#
#  Now choose a point at random in triangle I.
#
        r, seed = r8vec_uniform_01(2, seed)

        if (1.0 < r[0] + r[1]):
            r[0] = 1.0 - r[0]
            r[1] = 1.0 - r[1]

        s[j, 0] = (1.0 - r[0] - r[1]) * v[triangles[i, 0], 0] \
            + r[0] * v[triangles[i, 1], 0] \
            + r[1] * v[triangles[i, 2], 0]

        s[j, 1] = (1.0 - r[0] - r[1]) * v[triangles[i, 0], 1] \
            + r[0] * v[triangles[i, 1], 1] \
            + r[1] * v[triangles[i, 2], 1]

    return s, seed


def polygon_sample_test():

    # *****************************************************************************80
    #
    # POLYGON_SAMPLE_TEST tests POLYGON_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 20
    nv = 6
    v = np.array([
        [0.0, 0.0],
        [2.0, 0.0],
        [2.0, 1.0],
        [1.0, 1.0],
        [1.0, 2.0],
        [0.0, 1.0]])

    print('')
    print('POLYGON_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_SAMPLE samples a polygon.')

    seed = 123456789

    x, seed = polygon_sample(nv, v, n, seed)

    r8mat_print(n, 2, x, '  Sample points:')
#
#  Terminate.
#
    print('')
    print('POLYGON_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def r8_choose(n, k):

    # *****************************************************************************80
    #
    # R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
    #
    #  Discussion:
    #
    #    The value is calculated in such a way as to avoid overflow and
    #    roundoff.  The calculation is done in R8 arithmetic.
    #
    #    The formula used is:
    #
    #      C(N,K) = N! / ( K! * (N-K)! )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, K, are the values of N and K.
    #
    #    Output, real VALUE, the number of combinations of N
    #    things taken K at a time.
    #
    import numpy as np

    if (n < 0):

        value = 0.0

    elif (k == 0):

        value = 1.0

    elif (k == 1):

        value = float(n)

    elif (1 < k and k < n - 1):

        facn = r8_gamma_log(float(n + 1))
        fack = r8_gamma_log(float(k + 1))
        facnmk = r8_gamma_log(float(n - k + 1))

        value = round(np.exp(facn - fack - facnmk))

    elif (k == n - 1):

        value = float(n)

    elif (k == n):

        value = 1.0

    else:

        value = 0.0

    return value


def r8_choose_test():

    # *****************************************************************************80
    #
    # R8_CHOOSE_TEST tests R8_CHOOSE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_CHOOSE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_CHOOSE evaluates C(N,K).')
    print('')
    print('         N         K       CNK')

    for n in range(0, 6):
        print('')
        for k in range(0, n + 1):
            cnk = r8_choose(n, k)
            print('  %8d  %8d  %14.6g' % (n, k, cnk))
#
#  Terminate.
#
    print('')
    print('R8_CHOOSE_TEST')
    print('  Normal end of execution.')
    return


def r8_gamma_log(x):

    # *****************************************************************************80
    #
    # R8_GAMMA_LOG evaluates the logarithm of the gamma function.
    #
    #  Discussion:
    #
    #    This routine calculates the LOG(GAMMA) function for a positive real
    #    argument X.  Computation is based on an algorithm outlined in
    #    references 1 and 2.  The program uses rational functions that
    #    theoretically approximate LOG(GAMMA) to at least 18 significant
    #    decimal digits.  The approximation for X > 12 is from reference
    #    3, while approximations for X < 12.0 are similar to those in
    #    reference 1, but are unpublished.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2014
    #
    #  Author:
    #
    #    Original FORTRAN77 version by William Cody, Laura Stoltz.
    #    PYTHON version by John Burkardt.
    #
    #  Reference:
    #
    #    William Cody, Kenneth Hillstrom,
    #    Chebyshev Approximations for the Natural Logarithm of the
    #    Gamma Function,
    #    Mathematics of Computation,
    #    Volume 21, Number 98, April 1967, pages 198-203.
    #
    #    Kenneth Hillstrom,
    #    ANL/AMD Program ANLC366S, DGAMMA/DLGAMA,
    #    May 1969.
    #
    #    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
    #    Charles Mesztenyi, John Rice, Henry Thatcher,
    #    Christoph Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968,
    #    LC: QA297.C64.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the function.
    #
    #    Output, real R8_GAMMA_LOG, the value of the function.
    #
    import numpy as np

    c = np.array([
        -1.910444077728E-03,
        8.4171387781295E-04,
        -5.952379913043012E-04,
        7.93650793500350248E-04,
        -2.777777777777681622553E-03,
        8.333333333333333331554247E-02,
        5.7083835261E-03])
    d1 = -5.772156649015328605195174E-01
    d2 = 4.227843350984671393993777E-01
    d4 = 1.791759469228055000094023E+00
    frtbig = 2.25E+76
    p1 = np.array([
        4.945235359296727046734888E+00,
        2.018112620856775083915565E+02,
        2.290838373831346393026739E+03,
        1.131967205903380828685045E+04,
        2.855724635671635335736389E+04,
        3.848496228443793359990269E+04,
        2.637748787624195437963534E+04,
        7.225813979700288197698961E+03])
    p2 = np.array([
        4.974607845568932035012064E+00,
        5.424138599891070494101986E+02,
        1.550693864978364947665077E+04,
        1.847932904445632425417223E+05,
        1.088204769468828767498470E+06,
        3.338152967987029735917223E+06,
        5.106661678927352456275255E+06,
        3.074109054850539556250927E+06])
    p4 = np.array([
        1.474502166059939948905062E+04,
        2.426813369486704502836312E+06,
        1.214755574045093227939592E+08,
        2.663432449630976949898078E+09,
        2.940378956634553899906876E+10,
        1.702665737765398868392998E+11,
        4.926125793377430887588120E+11,
        5.606251856223951465078242E+11])
    q1 = np.array([
        6.748212550303777196073036E+01,
        1.113332393857199323513008E+03,
        7.738757056935398733233834E+03,
        2.763987074403340708898585E+04,
        5.499310206226157329794414E+04,
        6.161122180066002127833352E+04,
        3.635127591501940507276287E+04,
        8.785536302431013170870835E+03])
    q2 = np.array([
        1.830328399370592604055942E+02,
        7.765049321445005871323047E+03,
        1.331903827966074194402448E+05,
        1.136705821321969608938755E+06,
        5.267964117437946917577538E+06,
        1.346701454311101692290052E+07,
        1.782736530353274213975932E+07,
        9.533095591844353613395747E+06])
    q4 = np.array([
        2.690530175870899333379843E+03,
        6.393885654300092398984238E+05,
        4.135599930241388052042842E+07,
        1.120872109616147941376570E+09,
        1.488613728678813811542398E+10,
        1.016803586272438228077304E+11,
        3.417476345507377132798597E+11,
        4.463158187419713286462081E+11])
    r8_epsilon = 2.220446049250313E-016
    sqrtpi = 0.9189385332046727417803297
    xbig = 2.55E+305
    xinf = 1.79E+308

    y = x

    if (0.0 < y and y <= xbig):

        if (y <= r8_epsilon):

            res = - np.log(y)
#
#  EPS < X <= 1.5.
#
        elif (y <= 1.5):

            if (y < 0.6796875):
                corr = - np.log(y)
                xm1 = y
            else:
                corr = 0.0
                xm1 = (y - 0.5) - 0.5

            if (y <= 0.5 or 0.6796875 <= y):

                xden = 1.0
                xnum = 0.0
                for i in range(0, 8):
                    xnum = xnum * xm1 + p1[i]
                    xden = xden * xm1 + q1[i]

                res = corr + (xm1 * (d1 + xm1 * (xnum / xden)))

            else:

                xm2 = (y - 0.5) - 0.5
                xden = 1.0
                xnum = 0.0
                for i in range(0, 8):
                    xnum = xnum * xm2 + p2[i]
                    xden = xden * xm2 + q2[i]

                res = corr + xm2 * (d2 + xm2 * (xnum / xden))
#
#  1.5 < X <= 4.0.
#
        elif (y <= 4.0):

            xm2 = y - 2.0
            xden = 1.0
            xnum = 0.0
            for i in range(0, 8):
                xnum = xnum * xm2 + p2[i]
                xden = xden * xm2 + q2[i]

            res = xm2 * (d2 + xm2 * (xnum / xden))
#
#  4.0 < X <= 12.0.
#
        elif (y <= 12.0):

            xm4 = y - 4.0
            xden = -1.0
            xnum = 0.0
            for i in range(0, 8):
                xnum = xnum * xm4 + p4[i]
                xden = xden * xm4 + q4[i]

            res = d4 + xm4 * (xnum / xden)
#
#  Evaluate for 12 <= argument.
#
        else:

            res = 0.0

            if (y <= frtbig):

                res = c[6]
                ysq = y * y

                for i in range(0, 6):
                    res = res / ysq + c[i]

            res = res / y
            corr = np.log(y)
            res = res + sqrtpi - 0.5 * corr
            res = res + y * (corr - 1.0)
#
#  Return for bad arguments.
#
    else:

        res = xinf

    return res


def r8_gamma_log_test():

    # *****************************************************************************80
    #
    # R8_GAMMA_LOG_TEST tests R8_GAMMA_LOG.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_GAMMA_LOG_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_GAMMA_LOG evaluates the logarithm of the Gamma function.')
    print('')
    print('      X            GAMMA_LOG(X)    R8_GAMMA_LOG(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx1 = gamma_log_values(n_data)

        if (n_data == 0):
            break

        fx2 = r8_gamma_log(x)

        print('  %12g  %24.16g  %24.16g' % (x, fx1, fx2))
#
#  Terminate.
#
    print('')
    print('R8_GAMMA_LOG_TEST')
    print('  Normal end of execution.')
    return


def r8_uniform_01(seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_01 returns a unit pseudorandom R8.
    #
    #  Discussion:
    #
    #    This routine implements the recursion
    #
    #      seed = 16807 * seed mod ( 2^31 - 1 )
    #      r8_uniform_01 = seed / ( 2^31 - 1 )
    #
    #    The integer arithmetic never requires more than 32 bits,
    #    including a sign bit.
    #
    #    If the initial seed is 12345, then the first three computations are
    #
    #      Input     Output      R8_UNIFORM_01
    #      SEED      SEED
    #
    #         12345   207482415  0.096616
    #     207482415  1790989824  0.833995
    #    1790989824  2035175616  0.947702
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 March 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R, a random value between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_01 - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10

    return r, seed


def r8_uniform_01_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_01 produces a sequence of random values.')

    seed = 123456789

    print('')
    print('  Using random seed %d' % (seed))

    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')
    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))

    print('')
    print('  Verify that the sequence can be restarted.')
    print('  Set the seed back to its original value, and see that')
    print('  we generate the same sequence.')

    seed = 123456789
    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')

    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))
#
#  Terminate.
#
    print('')
    print('R8_UNIFORM_01_TEST')
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


def r8mat_print_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_TEST tests R8MAT_PRINT.
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
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT prints an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print(m, n, v, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
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
        print('  Col: '),

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j)),

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i)),

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j])),

            print('')

    return


def r8mat_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT_SOME prints some of an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_transpose_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
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
    r8mat_transpose_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_transpose_print_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT prints an R8MAT.')

    m = 4
    n = 3
    v = np.array([
        [11.0, 12.0, 13.0],
        [21.0, 22.0, 23.0],
        [31.0, 32.0, 33.0],
        [41.0, 42.0, 43.0]], dtype=np.float64)
    r8mat_transpose_print(m, n, v, '  Here is an R8MAT, transposed:')
#
#  Terminate.
#
    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_transpose_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
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

    for i2lo in range(max(ilo, 0), min(ihi, m - 1), incx):

        i2hi = i2lo + incx - 1
        i2hi = min(i2hi, m - 1)
        i2hi = min(i2hi, ihi)

        print('')
        print('  Row: '),

        for i in range(i2lo, i2hi + 1):
            print('%7d       ' % (i)),

        print('')
        print('  Col')

        j2lo = max(jlo, 0)
        j2hi = min(jhi, n - 1)

        for j in range(j2lo, j2hi + 1):

            print('%7d :' % (j)),

            for i in range(i2lo, i2hi + 1):
                print('%12g  ' % (a[i, j])),

            print('')

    return


def r8mat_transpose_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_TRANSPOSE_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_transpose_print_some(
        m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:')
#
#  Terminate.
#
    print('')
    print('R8MAT_TRANSPOSE_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_uniform_ab(m, n, a, b, seed):

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
    #
    #  Discussion:
    #
    #    An R8MAT is an array of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, real A, B, the range of the pseudorandom values.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.
    #
    #    Output, real R(M,N), an array of random values between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    import numpy
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8MAT_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8MAT_UNIFORM_AB - Fatal error!')

    r = numpy.zeros([m, n])

    for j in range(0, n):
        for i in range(0, m):

            k = (seed // 127773)

            seed = 16807 * (seed - k * 127773) - k * 2836

            seed = (seed % i4_huge)

            if (seed < 0):
                seed = seed + i4_huge

            r[i, j] = a + (b - a) * seed * 4.656612875E-10

    return r, seed


def r8mat_uniform_ab_test():

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_AB_TEST tests R8MAT_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    m = 5
    n = 4
    a = -1.0
    b = +5.0
    seed = 123456789

    print('')
    print('R8MAT_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_UNIFORM_AB computes a random R8MAT.')
    print('')
    print('  %g <= X <= %g' % (a, b))
    print('  Initial seed is %d' % (seed))

    v, seed = r8mat_uniform_ab(m, n, a, b, seed)

    r8mat_print(m, n, v, '  Random R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_UNIFORM_AB_TEST:')
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


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = np.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


def r8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
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

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_01 computes a random R8VEC.')
    print('')
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_01(n, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_TEST:')
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


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


def triangle_area(xa, ya, xb, yb, xc, yc):

    # *****************************************************************************80
    #
    # TRIANGLE_AREA computes the signed area of a triangle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real XA, YA, XB, YB, XC, YC, the vertices.
    #
    #    Output, real AREA, the signed area of the triangle.
    #
    area = 0.5 * ((xb - xa) * (yc - ya)
                  - (xc - xa) * (yb - ya))

    return area


def triangle_area_test():

    # *****************************************************************************80
    #
    # TRIANGLE_AREA_TEST tests TRIANGLE_AREA.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    xa = 0.0
    ya = 1.0
    xb = 0.0
    yb = 0.0
    xc = 1.0
    yc = 0.0

    print('')
    print('TRIANGLE_AREA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANGLE_AREA computes the area of a triangle.')

    print('')
    print('  (XA,YA) = (%g,%g)' % (xa, ya))
    print('  (XB,YB) = (%g,%g)' % (xb, yb))
    print('  (XC,YC) = (%g,%g)' % (xc, yc))

    area = triangle_area(xa, ya, xb, yb, xc, yc)

    print('')
    print('  Triangle area is %g' % (area))
#
#  Terminate.
#
    print('')
    print('TRIANGLE_AREA_TEST')
    print('  Normal end of execution.')
    return


def polygon_monte_carlo_tests():

    # *****************************************************************************80
    #
    # POLYGON_MONTE_CARLO_TESTS tests the POLYGON_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('POLYGON_MONTE_CARLO_TESTS')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the POLYGON_MONTE_CARLO library.')

    polygon_area_test()
    polygon_monomial_integral_test()
    polygon_monte_carlo_test()
    polygon_sample_test()

    print('')
    print('POLYGON_MONTE_CARLO_TESTS:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    polygon_monte_carlo_tests()
    timestamp()
