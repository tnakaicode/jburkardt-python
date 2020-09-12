#! /usr/bin/env python
#
def monomial_value_1d(n, e, x):

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_1D evaluates a monomial in 1D.
    #
    #  Discussion:
    #
    #    This routine evaluates a monomial of the form
    #
    #      x^e
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, integer E, the exponent.
    #
    #    Input, real X(N), the point coordinates.
    #
    #    Output, real VALUE(N), the value of the monomial.
    #
    import numpy as np

    value = np.zeros(n)

    for i in range(0, n):
        value[i] = x[i] ** e

    return value


def monomial_value_1d_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_1D_TEST tests MONOMIAL_VALUE_1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from r8vec_uniform_ab import r8vec_uniform_ab

    print('')
    print('MONOMIAL_VALUE_1D_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONOMIAL_VALUE_1D evaluates a monomial of a 1D argument.')
    print('')
    print('      X^(-1)       X^(0)       X^(1)       X^(2)       X^(5)')
    print('')

    n = 5
    x_min = -2.0
    x_max = +10.0
    seed = 123456789

    x, seed = r8vec_uniform_ab(n, x_min, x_max, seed)

    e = -1
    vm1 = monomial_value_1d(n, e, x)
    e = 0
    v0 = monomial_value_1d(n, e, x)
    e = 1
    v1 = monomial_value_1d(n, e, x)
    e = 2
    v2 = monomial_value_1d(n, e, x)
    e = 5
    v5 = monomial_value_1d(n, e, x)

    for j in range(0, n):
        print('  %10g  %10g  %10g  %10g  %10g'
              % (vm1[j], v0[j], v1[j], v2[j], v5[j]))
#
#  Terminate.
#
    print('')
    print('MONOMIAL_VALUE_1D_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    monomial_value_1d_test()
    timestamp()
