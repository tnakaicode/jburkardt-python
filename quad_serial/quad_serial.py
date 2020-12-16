#! /usr/bin/env python3
#
import numpy as np
import platform
import time


def quad_serial():

    # *****************************************************************************80
    #
    # QUAD_SERIAL estimates an integral using a quadrature rule.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 October 2011
    #
    #  Author:
    #
    #    John Burkardt
    #

    a = 0.0
    b = 10.0
    n = 10000000
    exact = 0.49936338107645674464

    print('')
    print('QUAD_SERIAL:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Estimate the integral of f(x) from A to B.')
    print('  f(x) = 50 / ( pi * ( 2500 * x * x + 1 ) ).')
    print('')
    print('  A        = %g' % (a))
    print('  B        = %g' % (b))
    print('  N        = %d' % (n))
    print('  Exact    = %g' % (exact))

    wtime = time.time()

    total = 0.0

    for i in range(n):
        x = (float(n - i - 1) * a + float(i) * b) / float(n - 1)
        total = total + f(x)

    wtime = time.time() - wtime

    total = (b - a) * total / float(n)
    error = abs(total - exact)

    print('')
    print('  Estimate = %g' % (total))
    print('  Error    = %g' % (error))
    print('  Time     = %g' % (wtime))
    print('')
    print('QUAD_SERIAL:')
    print('  Normal end of execution.')
    return


def f(x):

    # *****************************************************************************80
    #
    # F evaluates the function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #

    value = 50.0 / (np.pi * (2500.0 * x * x + 1.0))

    return value


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
    quad_serial()
    timestamp()
