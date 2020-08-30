#! /usr/bin/env python3
#


def alogam(x):

    # *****************************************************************************80
    #
    # ALOGAM computes the logarithm of the Gamma function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Malcolm Pike, David Hill,
    #    Algorithm 291:
    #    Logarithm of Gamma Function,
    #    Communications of the ACM,
    #    Volume 9, Number 9, September 1966, page 684.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the Gamma function.
    #    X should be greater than 0.
    #
    #    Output, real VALUE, the logarithm of the Gamma
    #    function of X.
    #
    import numpy as np
    from sys import exit

    if (x <= 0.0):
        print('')
        print('ALOGAM - Fatal error!')
        print('  X <= 0.0')
        exit('ALOGAM - Fatal error!')

    y = x

    if (x < 7.0):

        f = 1.0
        z = y

        while (z < 7.0):
            f = f * z
            z = z + 1.0

        y = z
        f = - np.log(f)

    else:

        f = 0.0

    z = 1.0 / y / y

    value = f + (y - 0.5) * np.log(y) - y \
        + 0.918938533204673 + \
        (((
            - 0.000595238095238 * z
            + 0.000793650793651) * z
            - 0.002777777777778) * z
         + 0.083333333333333) / y

    return value


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


def alogam_test():

    # *****************************************************************************80
    #
    # ALOGAM_TEST tests ALOGAM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ALOGAM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ALOGAM estimates the logarithm of the Gamma function.')
    print('')
    print('      X         Exact Value               '),
    print('Computed                Diff')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = gamma_log_values(n_data)

        if (n_data <= 0):
            break

        fx2 = alogam(x)

        print('  %8.4f  %24.16g  %24.16g  %10.2g' %
              (x, fx, fx2, abs(fx - fx2)))
#
#  Terminate.
#
    print('')
    print('ALOGAM_TEST')
    print('  Normal end of execution.')


def mdbeta(x, p, q):

    # *****************************************************************************80
    #
    # MDBETA evaluates the incomplete beta function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Oliver Ludwig,
    #    Algorithm 179:
    #    Incomplete Beta Ratio,
    #    Communications of the ACM,
    #    Volume 6, Number 6, June 1963, page 314.
    #
    #  Parameters:
    #
    #    Input, real X, the value to which function is to be
    #    integrated.  X must be in the range [0,1] inclusive.
    #
    #    Input, real P, the first parameter.  P must be greater
    #    than 0.0.
    #
    #    Input, real Q, the second parameter.  Q must be greater
    #    than 0.0.
    #
    #    Output, real PROB.  The probability that a random variable
    #    from a Beta distribution having parameters P and Q will be less than
    #    or equal to X.
    #
    #  Local parameters:
    #
    #    Local, real ALEPS, the logarithm of EPS1.
    #
    #    Local, real EPS, the machine precision.
    #
    #    Local, real EPS1, the smallest representable number.
    #
    import numpy as np
    from sys import exit

    aleps = - 179.6016
    eps = 2.2E-16
    eps1 = 1.0E-78
#
#  Check ranges of the arguments.
#
    prob = 0.0
    y = x

    if (x < 0.0):
        print('')
        print('MDBETA - Fatal error!')
        print('  X < 0.0')
        exit('MDBETA - Fatal error!')

    if (1.0 < x):
        print('')
        print('MDBETA - Fatal error!')
        print('  1.0 < X')
        exit('MDBETA - Fatal error!')

    if (p <= 0.0):
        print('')
        print('MDBETA - Fatal error!')
        print('  P <= 0.0')
        exit('MDBETA - Fatal error!')

    if (q <= 0.0):
        print('')
        print('MDBETA - Fatal error!')
        print('  Q <= 0.0')
        exit('MDBETA - Fatal error!')

    if (x <= 0.5):
        interval = 0
    else:
        interval = 1
        temp = p
        p = q
        q = temp
        y = 1.0 - y

    if (x == 0.0 or x == 1.0):

        prob = 0.0

        if (interval != 0):
            prob = 1.0 - prob
            temp = p
            p = q
            q = temp

        return prob

    ib = int(q)
    temp = float(ib)
    ps = q - float(ib)

    if (q == temp):
        ps = 1.0

    dp = p
    dq = q
    px = dp * np.log(y)
    pq = alogam(dp + dq)
    p1 = alogam(dp)
    c = alogam(dq)
    d4 = np.log(dp)
    xb = px + alogam(ps + dp) - alogam(ps) - d4 - p1
#
#  Scaling
#
    ib = int(xb / aleps)
    infsum = 0.0
#
#  First term of a decreasing series will underflow.
#
    if (ib == 0):

        infsum = np.exp(xb)
        cnt = infsum * dp
#
#  CNT will equal exp ( temp ) * ( 1.d0 - ps ) * i * p * y**i / factorial ( i ).
#
        wh = 0.0

        while (True):

            wh = wh + 1.0
            cnt = cnt * (wh - ps) * y / wh
            xb = cnt / (dp + wh)
            infsum = infsum + xb

            if (xb / eps < infsum):
                break

    finsum = 0.0

    if (dq <= 1.0):

        prob = finsum + infsum

        if (interval != 0):
            prob = 1.0 - prob
            temp = p
            p = q
            q = temp

        return prob

    xb = px + dq * np.log(1.0 - y) + pq - p1 - np.log(dq) - c
#
#  Scaling.
#
    ib = int(xb / aleps)

    if (ib < 0):
        ib = 0

    c = 1.0 / (1.0 - y)
    cnt = np.exp(xb - float(ib) * aleps)
    ps = dq
    wh = dq

    while (True):

        wh = wh - 1.0

        if (wh <= 0.0):

            prob = finsum + infsum

            if (interval != 0):
                prob = 1.0 - prob
                temp = p
                p = q
                q = temp

            break

        px = (ps * c) / (dp + wh)

        if (px <= 1.0):

            if (cnt / eps <= finsum or cnt <= eps1 / px):

                prob = finsum + infsum

                if (interval != 0):
                    prob = 1.0 - prob
                    temp = p
                    p = q
                    q = temp

                break

        cnt = cnt * px
#
#  Rescale.
#
        if (1.0 < cnt):
            ib = ib - 1
            cnt = cnt * eps1

        ps = wh

        if (ib == 0):
            finsum = finsum + cnt

    return prob


def beta_inc_values(n_data):

    # *****************************************************************************80
    #
    # BETA_INC_VALUES returns some values of the incomplete Beta function.
    #
    #  Discussion:
    #
    #    The incomplete Beta function may be written
    #
    #      BETA_INC(A,B,X) = Integral (0 to X) T^(A-1) * (1-T)^(B-1) dT
    #                      / Integral (0 to 1) T^(A-1) * (1-T)^(B-1) dT
    #
    #    Thus,
    #
    #      BETA_INC(A,B,0.0) = 0.0;
    #      BETA_INC(A,B,1.0) = 1.0
    #
    #    The incomplete Beta function is also sometimes called the
    #    "modified" Beta function, or the "normalized" Beta function
    #    or the Beta CDF (cumulative density function).
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BETA[X,A,B] / BETA[A,B]
    #
    #    The function can also be evaluated by using the Statistics package:
    #
    #      Needs["Statistics`ContinuousDistributions`"]
    #      dist = BetaDistribution [ a, b ]
    #      CDF [ dist, x ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2015
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
    #    Karl Pearson,
    #    Tables of the Incomplete Beta Function,
    #    Cambridge University Press, 1968.
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
    #    Output, real A, B, the parameters of the function.
    #
    #    Output, real X, the argument of the function.
    #
    #    Output, real F, the value of the function.
    #
    import numpy as np

    n_max = 45

    a_vec = np.array((
        0.5E+00,
        0.5E+00,
        0.5E+00,
        1.0E+00,
        1.0E+00,
        1.0E+00,
        1.0E+00,
        1.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        5.5E+00,
        10.0E+00,
        10.0E+00,
        10.0E+00,
        10.0E+00,
        20.0E+00,
        20.0E+00,
        20.0E+00,
        20.0E+00,
        20.0E+00,
        30.0E+00,
        30.0E+00,
        40.0E+00,
        0.1E+01,
        0.1E+01,
        0.1E+01,
        0.1E+01,
        0.1E+01,
        0.1E+01,
        0.1E+01,
        0.1E+01,
        0.2E+01,
        0.3E+01,
        0.4E+01,
        0.5E+01,
        1.30625,
        1.30625,
        1.30625))

    b_vec = np.array((
        0.5E+00,
        0.5E+00,
        0.5E+00,
        0.5E+00,
        0.5E+00,
        0.5E+00,
        0.5E+00,
        1.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        5.0E+00,
        0.5E+00,
        5.0E+00,
        5.0E+00,
        10.0E+00,
        5.0E+00,
        10.0E+00,
        10.0E+00,
        20.0E+00,
        20.0E+00,
        10.0E+00,
        10.0E+00,
        20.0E+00,
        0.5E+00,
        0.5E+00,
        0.5E+00,
        0.5E+00,
        0.2E+01,
        0.3E+01,
        0.4E+01,
        0.5E+01,
        0.2E+01,
        0.2E+01,
        0.2E+01,
        0.2E+01,
        11.7562,
        11.7562,
        11.7562))

    f_vec = np.array((
        0.6376856085851985E-01,
        0.2048327646991335E+00,
        0.1000000000000000E+01,
        0.0000000000000000E+00,
        0.5012562893380045E-02,
        0.5131670194948620E-01,
        0.2928932188134525E+00,
        0.5000000000000000E+00,
        0.2800000000000000E-01,
        0.1040000000000000E+00,
        0.2160000000000000E+00,
        0.3520000000000000E+00,
        0.5000000000000000E+00,
        0.6480000000000000E+00,
        0.7840000000000000E+00,
        0.8960000000000000E+00,
        0.9720000000000000E+00,
        0.4361908850559777E+00,
        0.1516409096347099E+00,
        0.8978271484375000E-01,
        0.1000000000000000E+01,
        0.5000000000000000E+00,
        0.4598773297575791E+00,
        0.2146816102371739E+00,
        0.9507364826957875E+00,
        0.5000000000000000E+00,
        0.8979413687105918E+00,
        0.2241297491808366E+00,
        0.7586405487192086E+00,
        0.7001783247477069E+00,
        0.5131670194948620E-01,
        0.1055728090000841E+00,
        0.1633399734659245E+00,
        0.2254033307585166E+00,
        0.3600000000000000E+00,
        0.4880000000000000E+00,
        0.5904000000000000E+00,
        0.6723200000000000E+00,
        0.2160000000000000E+00,
        0.8370000000000000E-01,
        0.3078000000000000E-01,
        0.1093500000000000E-01,
        0.918884684620518,
        0.21052977489419,
        0.1824130512500673))

    x_vec = np.array((
        0.01E+00,
        0.10E+00,
        1.00E+00,
        0.00E+00,
        0.01E+00,
        0.10E+00,
        0.50E+00,
        0.50E+00,
        0.10E+00,
        0.20E+00,
        0.30E+00,
        0.40E+00,
        0.50E+00,
        0.60E+00,
        0.70E+00,
        0.80E+00,
        0.90E+00,
        0.50E+00,
        0.90E+00,
        0.50E+00,
        1.00E+00,
        0.50E+00,
        0.80E+00,
        0.60E+00,
        0.80E+00,
        0.50E+00,
        0.60E+00,
        0.70E+00,
        0.80E+00,
        0.70E+00,
        0.10E+00,
        0.20E+00,
        0.30E+00,
        0.40E+00,
        0.20E+00,
        0.20E+00,
        0.20E+00,
        0.20E+00,
        0.30E+00,
        0.30E+00,
        0.30E+00,
        0.30E+00,
        0.225609,
        0.0335568,
        0.0295222))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        a = 0.0
        b = 0.0
        x = 0.0
        f = 0.0
    else:
        a = a_vec[n_data]
        b = b_vec[n_data]
        x = x_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, a, b, x, f


def mdbeta_test():

    # *****************************************************************************80
    #
    # MDBETA_TEST tests MDBETA.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('MDBETA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MDBETA_TEST estimates the modified Beta function.')
    print('')
    print('      X         P         Q         '),
    print('Exact Value               Computed                Diff')
    print('')

    n_data = 0

    while (True):

        n_data, p, q, x, fx = beta_inc_values(n_data)

        if (n_data <= 0):
            break

        fx2 = mdbeta(x, p, q)

        print('  %8.4f  %8.4f  %8.4f  %24.16g  %24.16g  %10.4g'
              % (x, p, q, fx, fx2, abs(fx - fx2)))
#
#  Terminate.
#
    print('')
    print('MDBETA_TEST:')
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


def toms179_test():

    # *****************************************************************************80
    #
    # TOMS179_TEST tests TOMS179.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TOMS179_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test TOMS179.')

    alogam_test()
    mdbeta_test()
#
#  Terminate.
#
    print('')
    print('TOMS179_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    toms179_test()
    timestamp()
