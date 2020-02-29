#! /usr/bin/env python3
#


def camel_b(m):

    # *****************************************************************************80
    #
    # CAMEL_B returns the bounds in the camel problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Sashwati Ray, PSV Nataraj,
    #    An efficient algorithm for range computation of polynomials using the
    #    Bernstein form,
    #    Journal of Global Optimization,
    #    Volume 45, 2009, pages 403-426.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Output, integer L(M), U(M), the lower and upper bounds.
    #
    import numpy as np

    l = np.array([-3.0, -3.0])
    u = np.array([+3.0, +3.0])

    return l, u


def camel_f(m, n, x):

    # *****************************************************************************80
    #
    # CAMEL_F returns the function in the camel problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Sashwati Ray, PSV Nataraj,
    #    An efficient algorithm for range computation of polynomials using the
    #    Bernstein form,
    #    Journal of Global Optimization,
    #    Volume 45, 2009, pages 403-426.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(M,N), the points.
    #
    #    Output, integer VALUE(N), the value of the function at X.
    #
    value = (
        4.0 * x[0, 0:n] ** 2
        - 2.1 * x[0, 0:n] ** 4
        + 1.0 / 3.0 * x[0, 0:n] ** 6
        + x[0, 0:n] * x[1, 0:n]
        - 4.0 * x[1, 0:n] ** 2
        + 4.0 * x[1, 0:n] ** 4)

    return value


def camel_m():

    # *****************************************************************************80
    #
    # CAMEL_M returns the number of variables in the camel problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Sashwati Ray, PSV Nataraj,
    #    An efficient algorithm for range computation of polynomials using the
    #    Bernstein form,
    #    Journal of Global Optimization,
    #    Volume 45, 2009, pages 403-426.
    #
    #  Parameters:
    #
    #    Output, integer M, the number of variables.
    #
    m = 2

    return m


def camel_test():

    # *****************************************************************************80
    #
    # CAMEL_TEST uses sampling to estimate the range of the CAMEL polynomial.
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
    #    26 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from r8mat_uniform_abvec import r8mat_uniform_abvec

    print('')
    print('CAMEL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = camel_m()
    l, u = camel_b(m)
    print('  camel: [ -1.031628453489616, ? ]:')

    seed = 123456789
    n = 8

    for n_log_2 in range(4, 15):

        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = camel_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))
#
#  Terminate.
#
    print('')
    print('CAMEL_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    camel_test()
    timestamp()
