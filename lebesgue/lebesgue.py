#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import platform
import time


def chebyshev1(n):

    # *****************************************************************************80
    #
    # CHEBYSHEV1 returns the Type 1 Chebyshev points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #
    x = np.zeros(n)
    for i in range(0, n):
        x[i] = np.cos(float(2 * i + 1) * np.pi / float(2 * n))

    return x


def chebyshev2(n):

    # *****************************************************************************80
    #
    # CHEBYSHEV2 returns the Type 2 Chebyshev points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    x = np.zeros(n)

    if (1 < n):
        for i in range(0, n):
            x[i] = np.cos(float(n - 1 - i) * np.pi / float(n - 1))

    return x


def chebyshev3(n):

    # *****************************************************************************80
    #
    # CHEBYSHEV3 returns the Type 3 Chebyshev points.
    #
    #  Discussion:
    #
    #    Note that this point set is NOT symmetric in [-1,+1].
    #    It is sometimes augmented by the value -1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    angle = np.zeros(n)

    for i in range(0, n):
        angle[i] = (2 * n - 2 * i - 1) * np.pi / float(2 * n + 1)

    x = np.cos(angle)

    return x


def chebyshev4(n):

    # *****************************************************************************80
    #
    # CHEBYSHEV4 returns the Type 4 Chebyshev points.
    #
    #  Discussion:
    #
    #    Note that this point set is NOT symmetric in [-1,+1].
    #    It is sometimes augmented by the value +1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    angle = np.zeros(n)

    for i in range(0, n):
        angle[i] = float(2 * (n - i)) * np.pi / float(2 * n + 1)

    x = np.cos(angle)

    return x


def equidistant1(n):

    # *****************************************************************************80
    #
    # EQUIDISTANT1 returns the Type 1 Equidistant points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    x = np.zeros(n)

    for i in range(0, n):
        x[i] = float(1 - n + 2 * i) / float(n + 1)

    return x


def equidistant2(n):

    # *****************************************************************************80
    #
    # EQUIDISTANT2 returns the Type 2 Equidistant points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    x = np.zeros(n)

    if (1 < n):
        for i in range(0, n):
            x[i] = float(1 - n + 2 * i) / float(n - 1)

    return x


def equidistant3(n):

    # *****************************************************************************80
    #
    # EQUIDISTANT3 returns the Type 3 Equidistant points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    x = np.zeros(n)

    for i in range(0, n):
        x[i] = float(1 - n + 2 * i) / float(n)

    return x


def fejer1(n):

    # *****************************************************************************80
    #
    # FEJER1 returns the Type 1 Fejer points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    theta = np.zeros(n)

    for i in range(0, n):
        theta[i] = float(2 * n - 1 - 2 * i) * np.pi / float(2 * n)

    x = np.cos(theta)

    return x


def fejer2(n):

    # *****************************************************************************80
    #
    # FEJER2 returns the Type 2 Fejer points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(N), the points.
    #

    theta = np.zeros(n)

    for i in range(0, n):
        theta[i] = float(n - i) * np.pi / float(n + 1)

    x = np.cos(theta)

    return x


def lagrange_value(data_num, t_data, interp_num, t_interp):

    # *****************************************************************************80
    #
    # LAGRANGE_VALUE evaluates the Lagrange polynomials.
    #
    #  Discussion:
    #
    #    Given DATA_NUM distinct abscissas, T_DATA(1:DATA_NUM),
    #    the I-th Lagrange polynomial L(I)(T) is defined as the polynomial of
    #    degree DATA_NUM - 1 which is 1 at T_DATA(I) and 0 at the DATA_NUM - 1
    #    other abscissas.
    #
    #    A formal representation is:
    #
    #      L(I)(T) = Product ( 1 <= J <= DATA_NUM, I /= J )
    #       ( T - T(J) ) / ( T(I) - T(J) )
    #
    #    This routine accepts a set of INTERP_NUM values at which all the Lagrange
    #    polynomials should be evaluated.
    #
    #    Given data values P_DATA at each of the abscissas, the value of the
    #    Lagrange interpolating polynomial at each of the interpolation points
    #    is then simple to compute by matrix multiplication:
    #
    #      P_INTERP(1:INTERP_NUM) =
    #        P_DATA(1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
    #
    #    or, in the case where P is multidimensional:
    #      P_INTERP(1:M,1:INTERP_NUM) =
    #        P_DATA(1:M,1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2007
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer DATA_NUM, the number of data points.
    #    DATA_NUM must be at least 1.
    #
    #    Input, real T_DATA(DATA_NUM), the data points.
    #
    #    Input, integer INTERP_NUM, the number of
    #    interpolation points.
    #
    #    Input, real T_INTERP(INTERP_NUM), the
    #    interpolation points.
    #
    #    Output, real L_INTERP(DATA_NUM,INTERP_NUM), the values
    #    of the Lagrange polynomials at the interpolation points.
    #
    #
    #  Evaluate the polynomial.
    #
    l_interp = np.ones([data_num, interp_num])

    for i in range(0, data_num):

        for j in range(0, data_num):

            if (j != i):

                for k in range(0, interp_num):

                    l_interp[i, k] = l_interp[i, k] \
                        * (t_interp[k] - t_data[j]) / (t_data[i] - t_data[j])

    return l_interp


def lebesgue_chebyshev1_test():

    # *****************************************************************************80
    #
    # LEBESGUE_CHEBYSHEV1_TEST looks at Chebyshev1 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_CHEBYSHEV1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Chebyshev1 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 21
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = chebyshev1(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Chebyshev1 Lebesgue constants:')

    l2 = np.zeros(n)
    for n in range(1, n_max + 1):
        l2[n - 1] = l[n - 1] / np.log(n + 1)

    r8vec_print(n_max, l2, '  Chebyshev1 Lebesgue constants/log(N+1):')
#
#  Examine one case more closely.
#
    n = 11
    x = chebyshev1(n)
    r8vec_print(n, x, '  Chebyshev1 points for N = 11')

    label = 'Chebyshev1 points for N = 11'
    filename = 'chebyshev1.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_CHEBYSHEV1_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_chebyshev2_test():

    # *****************************************************************************80
    #
    # LEBESGUE_CHEBYSHEV2_TEST looks at Chebyshev2 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_CHEBYSHEV2_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Chebyshev2 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = chebyshev2(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Chebyshev2 Lebesgue constants for N = 1 to 11:')

    l2 = np.zeros(n)
    for n in range(1, n_max + 1):
        l2[n - 1] = l[n - 1] / np.log(n + 1)

    r8vec_print(n_max, l2, '  Chebyshev2 Lebesgue constants/log(N+1):')
#
#  Examine one case more closely.
#
    n = 11
    x = chebyshev2(n)
    r8vec_print(n, x, '  Chebyshev2 points for N = 11')

    label = 'Chebyshev2 points for N = 11'
    filename = 'chebyshev2.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_CHEBYSHEV2_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_chebyshev3_test():

    # *****************************************************************************80
    #
    # LEBESGUE_CHEBYSHEV3_TEST looks at Chebyshev3 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_CHEBYSHEV3_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Chebyshev3 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = chebyshev3(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Chebyshev3 Lebesgue constants for N = 1 to 11:')

    l2 = np.zeros(n)
    for n in range(1, n_max + 1):
        l2[n - 1] = l[n - 1] / np.log(n + 1)

    r8vec_print(n_max, l2, '  Chebyshev3 Lebesgue constants/log(N+1):')
#
#  Examine one case more closely.
#
    n = 11
    x = chebyshev3(n)
    r8vec_print(n, x, '  Chebyshev3 points for N = 11')

    label = 'Chebyshev3 points for N = 11'
    filename = 'chebyshev3.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_CHEBYSHEV3_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_chebyshev4_test():

    # *****************************************************************************80
    #
    # LEBESGUE_CHEBYSHEV4_TEST looks at Chebyshev4 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_CHEBYSHEV4_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Chebyshev4 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = chebyshev4(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Chebyshev4 Lebesgue constants for N = 1 to 11:')

    l2 = np.zeros(n)
    for n in range(1, n_max + 1):
        l2[n - 1] = l[n - 1] / np.log(n + 1)

    r8vec_print(n_max, l2, '  Chebyshev4 Lebesgue constants/log(N+1):')
#
#  Examine one case more closely.
#
    n = 11
    x = chebyshev4(n)
    r8vec_print(n, x, '  Chebyshev4 points for N = 11')

    label = 'Chebyshev4 points for N = 11'
    filename = 'chebyshev4.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_CHEBYSHEV4_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_constant(n, x, nfun, xfun):

    # *****************************************************************************80
    #
    # LEBESGUE_CONSTANT estimates the Lebesgue constant for a set of points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Jean-Paul Berrut, Lloyd Trefethen,
    #    Barycentric Lagrange Interpolation,
    #    SIAM Review,
    #    Volume 46, Number 3, September 2004, pages 501-517.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of interpolation points.
    #
    #    Input, real X(N), the interpolation points.
    #
    #    Input, integer NFUN, the number of evaluation points.
    #
    #    Input, real XFUN(CONSTANT), the evaluation points.
    #
    #    Output, real LMAX, an estimate of the Lebesgue constant for the points.
    #

    lfun = lebesgue_function(n, x, nfun, xfun)

    lmax = np.max(lfun)

    return lmax


def lebesgue_equidistant1_test():

    # *****************************************************************************80
    #
    # LEBESGUE_EQUIDISTANT1_TEST looks at Equidistant1 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_EQUIDISTANT1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Equidistant1 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = equidistant1(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Equidistant1 Lebesgue constants for N = 1 to 11:')
#
#  Examine one case more closely.
#
    n = 11
    x = equidistant1(n)
    r8vec_print(n, x, '  Equidistant1 points for N = 11')

    label = 'Equidistant1 points for N = 11'
    filename = 'equidistant1.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_EQUIDISTANT1_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_equidistant2_test():

    # *****************************************************************************80
    #
    # LEBESGUE_EQUIDISTANT2_TEST looks at Equidistant2 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_EQUIDISTANT2_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Equidistant2 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = equidistant2(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Equidistant2 Lebesgue constants for N = 1 to 11:')
#
#  Examine one case more closely.
#
    n = 11
    x = equidistant2(n)
    r8vec_print(n, x, '  Equidistant2 points for N = 11')

    label = 'Equidistant2 points for N = 11'
    filename = 'equidistant2.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_EQUIDISTANT2_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_equidistant3_test():

    # *****************************************************************************80
    #
    # LEBESGUE_EQUIDISTANT3_TEST looks at Equidistant3 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_EQUIDISTANT3_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Equidistant3 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = equidistant3(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Equidistant3 Lebesgue constants for N = 1 to 11:')
#
#  Examine one case more closely.
#
    n = 11
    x = equidistant3(n)
    r8vec_print(n, x, '  Equidistant3 points for N = 11')

    label = 'Equidistant3 points for N = 11'
    filename = 'equidistant3.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_EQUIDISTANT3_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_fejer1_test():

    # *****************************************************************************80
    #
    # LEBESGUE_FEJER1_TEST looks at Fejer 1 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_FEJER1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Fejer1 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = fejer1(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Fejer1 Lebesgue constants for N = 1 to 11:')
#
#  Examine one case more closely.
#
    n = 11
    x = fejer1(n)
    r8vec_print(n, x, '  Fejer1 points for N = 11')

    label = 'Fejer1 points for N = 11'
    filename = 'fejer1.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_FEJER1_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_fejer2_test():

    # *****************************************************************************80
    #
    # LEBESGUE_FEJER2_TEST looks at Fejer2 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LEBESGUE_FEJER2_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Analyze Fejer2 points.')

    nfun = 501
    xfun = r8vec_linspace(nfun, -1.0, +1.0)

    n_max = 11
    l = np.zeros(n_max)
    for n in range(1, n_max + 1):
        x = fejer2(n)
        l[n - 1] = lebesgue_constant(n, x, nfun, xfun)

    r8vec_print(n_max, l, '  Fejer2 Lebesgue constants for N = 1 to 11:')
#
#  Examine one case more closely.
#
    n = 11
    x = fejer2(n)
    r8vec_print(n, x, '  Fejer2 points for N = 11')

    label = 'Fejer2 points for N = 11'
    filename = 'fejer2.png'
    lebesgue_plot(n, x, nfun, xfun, label, filename)
    print('')
    print('  Plot file saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('LEBESGUE_FEJER2_TEST')
    print('  Normal end of execution.')
    return


def lebesgue_function(n, x, nfun, xfun):

    # *****************************************************************************80
    #
    # LEBESGUE_FUNCTION evaluates the Lebesgue function for a set of points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Jean-Paul Berrut, Lloyd Trefethen,
    #    Barycentric Lagrange Interpolation,
    #    SIAM Review,
    #    Volume 46, Number 3, September 2004, pages 501-517.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of interpolation points.
    #
    #    Input, real X(N), the interpolation points.
    #
    #    Input, integer NFUN, the number of evaluation points.
    #
    #    Input, real XFUN(NFUN), the evaluation points.
    #
    #    Output, real LFUN(NFUN), the Lebesgue function evaluated at XFUN.
    #
    #
    #  Handle special case.
    #
    if (n == 1):

        lfun = np.ones(nfun)

    else:

        llfun = lagrange_value(n, x, nfun, xfun)

        lfun = np.zeros(nfun)

        for j in range(0, nfun):
            t = 0.0
            for i in range(0, n):
                t = t + abs(llfun[i, j])
            lfun[j] = t

    return lfun


def lebesgue_plot(n, x, nfun, xfun, label, filename):

    # *****************************************************************************80
    #
    # LEBESGUE_PLOT plots the Lebesgue function for a set of points.
    #
    #  Discussion:
    #
    #    The interpolation interval is assumed to be [min(XFUN), max(XFUN)].
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Parameters:
    #
    #    Jean-Paul Berrut, Lloyd Trefethen,
    #    Barycentric Lagrange Interpolation,
    #    SIAM Review,
    #    Volume 46, Number 3, September 2004, pages 501-517.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of interpolation points.
    #
    #    Input, real X(N), the interpolation points.
    #
    #    Input, integer NFUN, the number of evaluation points.
    #
    #    Input, real XFUN(NFUN), the evaluation points.
    #
    #    Input, string LABEL, a title for the plot.
    #
    #    Input, string FILENAME, a filename in which to save the plot.
    #

    lfun = lebesgue_function(n, x, nfun, xfun)

    plt.plot(xfun, lfun, linewidth=2)

    ymax = np.ceil(np.max(lfun)) + 1

    xmin = np.min(xfun)
    xmax = np.max(xfun)

    plt.axis([xmin, xmax, 0.0, ymax])
    plt.grid(True)
    plt.xlabel('<--- X --->')
    plt.ylabel('<--- Lebesgue(X) --->')
    plt.title(label)

    plt.savefig(filename)


def r8vec_linspace(n, a, b):

    # *****************************************************************************80
    #
    # R8VEC_LINSPACE creates a column vector of linearly spaced values.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #    While MATLAB has the built in command
    #
    #      x = linspace ( a, b, n )
    #
    #    that command has the distinct disadvantage of returning a ROW vector.
    #
    #    4 points evenly spaced between 0 and 12 will yield 0, 4, 8, 12.
    #
    #    In other words, the interval is divided into N-1 even subintervals,
    #    and the endpoints of intervals are used as the points.
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
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the first and last entries.
    #
    #    Output, real X(N), a vector of linearly spaced data.
    #

    x = np.zeros(n)

    if (n == 1):
        x[0] = (a + b) / 2.0
    else:
        for i in range(0, n):
            x[i] = ((n - 1 - i) * a
                    + (i) * b) \
                / (n - 1)

    return x


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

    t = time.time()
    print(time.ctime(t))

    return None


if (__name__ == '__main__'):
    timestamp()
    lebesgue_chebyshev1_test()
    lebesgue_chebyshev2_test()
    lebesgue_chebyshev3_test()
    lebesgue_chebyshev4_test()
    lebesgue_equidistant1_test()
    lebesgue_equidistant2_test()
    lebesgue_equidistant3_test()
    lebesgue_fejer1_test()
    lebesgue_fejer2_test()
    timestamp()
