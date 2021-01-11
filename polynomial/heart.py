#! /usr/bin/env python3
#


def heart_b(m):

    # *****************************************************************************80
    #
    # HEART_B returns the bounds in the heart problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Cesar Munoz, Anthony Narkawicz,
    #    Formalization of Bernstein polynomials and applications to global
    #    optimization,
    #    Journal of Automated Reasoning,
    #    Volume 51, Number 2, 2013, pages 151-196.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Output, integer L(M), U(M), the lower and upper bounds.
    #
    import numpy as np

    l = np.array([-0.1, 0.4, -0.7, -0.7, +0.1, -0.1, -0.3, -1.1])
    u = np.array([0.4, +1.0, -0.4, +0.4, +0.2, +0.2, +1.1, -0.3])

    return l, u


def heart_f(m, n, x):

    # *****************************************************************************80
    #
    # HEART_F returns the function in the heart problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Cesar Munoz, Anthony Narkawicz,
    #    Formalization of Bernstein polynomials and applications to global
    #    optimization,
    #    Journal of Automated Reasoning,
    #    Volume 51, Number 2, 2013, pages 151-196.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real x[M,N), the points.
    #
    #    Output, integer VALUE(N), the value of the function at X.
    #
    value = (
        + x[0, 0:n] * x[5, 0:n] ** 3
        - 3.0 * x[0, 0:n] * x[5, 0:n] * x[6, 0:n] ** 2
        + x[2, 0:n] * x[6, 0:n] ** 3
        - 3.0 * x[2, 0:n] * x[6, 0:n] * x[5, 0:n] ** 2
        + x[1, 0:n] * x[4, 0:n] ** 3
        - 3.0 * x[1, 0:n] * x[4, 0:n] * x[7, 0:n] ** 2
        + x[3, 0:n] * x[7, 0:n] ** 3
        - 3.0 * x[3, 0:n] * x[7, 0:n] * x[4, 0:n] ** 2
        + 0.9563453)

    return value


def heart_m():

    # *****************************************************************************80
    #
    # HEART_M returns the number of variables in the heart problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Cesar Munoz, Anthony Narkawicz,
    #    Formalization of Bernstein polynomials and applications to global
    #    optimization,
    #    Journal of Automated Reasoning,
    #    Volume 51, Number 2, 2013, pages 151-196.
    #
    #  Parameters:
    #
    #    Output, integer M, the number of variables.
    #
    m = 8

    return m


def heart_test():

    # *****************************************************************************80
    #
    # HEART_TEST uses sampling to estimate the range of the HEART polynomial.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from r8mat_uniform_abvec import r8mat_uniform_abvec

    print('')
    print('HEART_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = heart_m()
    l, u = heart_b(m)
    print('  heart: [-1.36775, +1.74345327935]')

    seed = 123456789
    n = 8

    for n_log_2 in range(4, 15):

        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = heart_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))
#
#  Terminate.
#
    print('')
    print('HEART_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    heart_test()
    timestamp()
