#! /usr/bin/env python
#
import numpy as np
import platform
from hermite_poly_phys_values import hermite_poly_phys_values
from timestamp import timestamp


def hermite_poly_phys(n, x):

    # *****************************************************************************80
    #
    # HERMITE_POLY_PHYS evaluates the Hermite polynomials at X.
    #
    #  Differential equation:
    #
    #    Y'' - 2 X Y' + 2 N Y = 0
    #
    #  First terms:
    #
    #      1
    #      2 X
    #      4 X^2     -  2
    #      8 X^3     - 12 X
    #     16 X^4     - 48 X^2     + 12
    #     32 X^5    - 160 X^3    + 120 X
    #     64 X^6    - 480 X^4    + 720 X^2    - 120
    #    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
    #    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
    #    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
    #   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
    #
    #  Recursion:
    #
    #    H(0,X) = 1,
    #    H(1,X) = 2*X,
    #    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
    #
    #  Norm:
    #
    #    Integral ( -oo < X < oo ) exp ( - X^2 ) * H(N,X)^2 dX
    #    = sqrt ( pi ) * 2^N * N!
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2004
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
    #  Parameters:
    #
    #    Input, integer N, the highest order polynomial to compute.
    #    Note that polynomials 0 through N will be computed.
    #
    #    Input, real X, the point at which the polynomials are to be evaluated.
    #
    #    Output, real CX[0:N], the values of the first N+1 Hermite
    #    polynomials at the point X.
    #

    cx = np.zeros(n + 1)

    cx[0] = 1.0

    if (0 < n):

        cx[1] = 2.0 * x

        for i in range(2, n + 1):
            cx[i] = 2.0 * x * cx[i - 1] - 2.0 * (i - 1) * cx[i - 2]

    return cx


def hermite_poly_phys_test():

    # *****************************************************************************80
    #
    # HERMITE_POLY_PHYS_TEST tests HERMITE_POLY_PHYS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('HERMITE_POLY_PHYS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HERMITE_POLY_PHYS computes the Hermite physicist polynomials;')
    print('')
    print('       N      X        Exact F       H(N)(X)')
    print('')

    n_data = 0

    while (True):

        n_data, n, x, fx = hermite_poly_phys_values(n_data)

        if (n_data == 0):
            break

        fx2 = hermite_poly_phys(n, x)

        print('  %2d  %12f  %14g  %14g' % (n, x, fx, fx2[n]))
#
#  Terminate.
#
    print('')
    print('HERMITE_POLY_PHYS_TEST')
    print('  Normal end of execution.')
    return


def hermite_poly_phys_values(n_data):

    # *****************************************************************************80
    #
    # HERMITE_POLY_PHYS_VALUES returns some values of the physicist's Hermite polynomial.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      HermiteH[n,x]
    #
    #  Differential equation:
    #
    #    Y'' - 2 X Y' + 2 N Y = 0
    #
    #  First terms:
    #
    #      1
    #      2 X
    #      4 X^2     -  2
    #      8 X^3     - 12 X
    #     16 X^4     - 48 X^2     + 12
    #     32 X^5    - 160 X^3    + 120 X
    #     64 X^6    - 480 X^4    + 720 X^2    - 120
    #    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
    #    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
    #    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
    #   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
    #
    #  Recursion:
    #
    #    H(0,X) = 1,
    #    H(1,X) = 2*X,
    #    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
    #
    #  Norm:
    #
    #    Integral ( -oo < X < +oo ) exp ( - X^2 ) * H(N,X)^2 dX
    #    = sqrt ( PI ) * 2^N * N!
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2015
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
    #    Output, integer N, the order of the polynomial.
    #
    #    Output, real X, the point where the polynomial is evaluated.
    #
    #    Output, real FX, the value of the function.
    #
    import numpy as np

    n_max = 18

    f_vec = np.array((
        0.1000000000000000E+01,
        0.1000000000000000E+02,
        0.9800000000000000E+02,
        0.9400000000000000E+03,
        0.8812000000000000E+04,
        0.8060000000000000E+05,
        0.7178800000000000E+06,
        0.6211600000000000E+07,
        0.5206568000000000E+08,
        0.4212712000000000E+09,
        0.3275529760000000E+10,
        0.2432987360000000E+11,
        0.1712370812800000E+12,
        0.0000000000000000E+00,
        0.4100000000000000E+02,
        -0.8000000000000000E+01,
        0.3816000000000000E+04,
        0.3041200000000000E+07))

    n_vec = np.array((
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,
        9, 10, 11,
        12, 5, 5,
        5, 5, 5))

    x_vec = np.array((
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        5.0E+00,
        0.0E+00,
        0.5E+00,
        1.0E+00,
        3.0E+00,
        1.0E+01))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        n = 0
        x = 0.0
        f = 0.0
    else:
        n = n_vec[n_data]
        x = x_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, n, x, f


def hermite_poly_phys_values_test():

    # *****************************************************************************80
    #
    # HERMITE_POLY_PHYS_VALUES_TEST demonstrates the use of HERMITE_POLY_PHYS_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('HERMITE_POLY_PHYS_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  HERMITE_POLY_PHYS_VALUES stores values of the Hermite physicist polynomials.')
    print('')
    print('      N            X            FX')
    print('')

    n_data = 0

    while (True):

        n_data, n, x, fx = hermite_poly_phys_values(n_data)

        if (n_data == 0):
            break

        print('  %6d  %12f  %24.16g' % (n, x, fx))
#
#  Terminate.
#
    print('')
    print('HERMITE_POLY_PHYS_VALUES_TEST:')
    print('  Normal end of execution.')


def hermite_poly_phys_coef(n):

    # *****************************************************************************80
    #
    # HERMITE_POLY_PHYS_COEF: coefficients of the physicist's Hermite polynomial H(n,x).
    #
    #  First terms:
    #
    #    N/K     0     1      2      3       4     5      6    7      8    9   10
    #
    #     0      1
    #     1      0     2
    #     2     -2     0      4
    #     3      0   -12      0      8
    #     4     12     0    -48      0      16
    #     5      0   120      0   -160       0    32
    #     6   -120     0    720      0    -480     0     64
    #     7      0 -1680      0   3360       0 -1344      0   128
    #     8   1680     0 -13440      0   13440     0  -3584     0    256
    #     9      0 30240      0 -80640       0 48384      0 -9216      0 512
    #    10 -30240     0 302400      0 -403200     0 161280     0 -23040   0 1024
    #
    #  Recursion:
    #
    #    H(0,X) = 1,
    #    H(1,X) = 2*X,
    #    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 February 2015
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
    #  Parameters:
    #
    #    Input, integer N, the highest order polynomial to compute.
    #    Note that polynomials 0 through N will be computed.
    #
    #    Output, real C(1:N+1,1:N+1), the coefficients of the Hermite
    #    polynomials.
    #
    import numpy as np

    c = np.zeros((n + 1, n + 1))

    c[0, 0] = 1.0

    if (0 < n):

        c[1, 1] = 2.0

        for i in range(1, n):
            c[i + 1, 0] = -2.0 * float(i) * c[i - 1, 0]
            for j in range(1, i):
                c[i + 1, j] = 2.0 * c[i, j - 1] - 2.0 * float(i) * c[i - 1, j]
            c[i + 1, i] = 2.0 * c[i, i - 1]
            c[i + 1, i + 1] = 2.0 * c[i, i]

    return c


def hermite_poly_phys_coef_test():

    # *****************************************************************************80
    #
    # HERMITE_POLY_PHYS_COEF_TEST tests HERMITE_POLY_PHYS_COEF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 5

    print('')
    print('HERMITE_POLY_PHYS_COEF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HERMITE_POLY_PHYS_COEF determines the Hermite')
    print('  physicist\'s polynomial coefficients.')

    c = hermite_poly_phys_coef(n)

    for i in range(0, n + 1):
        print('')
        print('  H(%d)' % (i))
        print('')
        for j in range(i, -1, -1):
            if (j == 0):
                print('    %f' % (c[i, j]))
            elif (j == 1):
                print('    %f * x' % (c[i, j]))
            else:
                print('    %f * x^%d' % (c[i, j], j))
#
#  Terminate.
#
    print('')
    print('HERMITE_POLY_PHYS_COEF_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    hermite_poly_phys_test()
    hermite_poly_phys_coef_test()
    hermite_poly_phys_values_test()
    timestamp()
