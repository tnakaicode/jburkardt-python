#! /usr/bin/env python3
#


def c8_log_values(n_data):

    # *****************************************************************************80
    #
    # C8_LOG_VALUES returns values of the complex logarithm function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 January 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    David Collens,
    #    Algorithm 243: Logarithm of a Complex Number,
    #    Communications of the Association for Computing Machinery,
    #    Volume 7, Number 11, November 1964, page 660.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, complex X, the argument of the function.
    #
    #    Output, complex CAI, the value of the function.
    #
    import numpy as np

    n_max = 12

    fz_vec = np.array([
        1.039720770839918 - 2.356194490192345j,
        0.804718956217050 + 2.677945044588987j,
        0.346573590279973 - 2.356194490192345j,
        0.000000000000000 + 3.141592653589793j,
        0.693147180559945 - 1.570796326794897j,
        0.000000000000000 - 1.570796326794897j,
        0.000000000000000 + 1.570796326794897j,
        0.693147180559945 + 1.570796326794897j,
        0.346573590279973 - 0.785398163397448j,
        0.000000000000000 + 0.000000000000000j,
        1.039720770839918 - 0.785398163397448j,
        0.804718956217050 + 0.463647609000806j])

    z_vec = np.array([
        -2.0 - 2.0j,
        -2.0 + 1.0j,
        -1.0 - 1.0j,
        -1.0 + 0.0j,
        0.0 - 2.0j,
        0.0 - 1.0j,
        0.0 + 1.0j,
        0.0 + 2.0j,
        1.0 - 1.0j,
        1.0 + 0.0j,
        2.0 - 2.0j,
        2.0 + 1.0j])

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        z = 0.0 + 0.0j
        fz = 0.0 + 0.0j
    else:
        z = z_vec[n_data]
        fz = fz_vec[n_data]
        n_data = n_data + 1

    return n_data, z, fz


def c8_log_values_test():

    # *****************************************************************************80
    #
    # C8_LOG_VALUES_TEST tests C8_LOG_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 January 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8_LOG_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  C8_LOG_VALUES stores values of')
    print('  the complex logarithm function.')
    print('')
    print('        Z.real        Z.imag          FZ.real                FZ.imag')
    print('')

    n_data = 0

    while (True):

        n_data, z, fz = c8_log_values(n_data)

        if (n_data == 0):
            break

        print('  %12g  %12g  %24.16g  %24.16g'
              % (z.real, z.imag, fz.real, fz.imag))
#
#  Terminate.
#
    print('')
    print('C8_LOG_VALUES_TEST:')
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


def toms243(z):

    # *****************************************************************************80
    #
    # TOMS243 computes the natural logarithm for complex values.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 January 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    David Collens,
    #    Algorithm 243: Logarithm of a Complex Number,
    #    Communications of the Association for Computing Machinery,
    #    Volume 7, Number 11, November 1964, page 660.
    #
    #  Parameters:
    #
    #    Input, complex Z, the argument of the function.
    #
    #    Output, complex VALUE, the value of the function.
    #
    import numpy as np

    a = z.real
    b = z.imag

    if (a == 0.0 and b == 0.0):
        c = np.nan()
        d = np.nan()
    else:
        e = a / 2.0
        f = b / 2.0
        if (abs(e) < 0.5 and abs(f) < 0.5):
            c = abs(2.0 * a) + abs(2.0 * b)
            d = 8.0 * (a / c) * a + 8.0 * (b / c) * b
            c = 0.5 * (np.log(c) + np.log(d)) - np.log(np.sqrt(8.0))
        else:
            c = abs(e / 2.0) + abs(f / 2.0)
            d = 0.5 * (e / c) * e + 0.5 * (f / c) * f
            c = 0.5 * (np.log(c) + np.log(d)) + np.log(np.sqrt(8.0))

        if ((a != 0.0) and abs(f) <= abs(e)):
            if (np.sign(a) != -1.0):
                d = np.arctan(b / a)
            elif (np.sign(b) != -1.0):
                d = np.arctan(b / a) + np.pi
            else:
                d = np.arctan(b / a) - np.pi
        else:
            d = - np.arctan(a / b) + np.pi / 2.0 * np.sign(b)

    value = np.complex128(c + d * 1j)

    return value


def toms243_test():

    # *****************************************************************************80
    #
    # TOMS243_TEST tests the TOMS243 library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 January 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TOMS243_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TOMS243 evaluates the complex logarithm function.')
    print('')
    print('        Z.real        Z.imag                   Exact')
    print('                                             Computed')
    print('')

    n_data = 0

    while (True):

        n_data, z, fz1 = c8_log_values(n_data)

        if (n_data == 0):
            break

        print('  %12g  %12g  %24.16g  %24.16g'
              % (z.real, z.imag, fz1.real, fz1.imag))

        fz2 = toms243(z)

        print('                              %24.16g  %24.16g'
              % (fz2.real, fz2.imag))
#
#  Terminate.
#
    print('')
    print('TOMS243_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    toms243_test()
    timestamp()
