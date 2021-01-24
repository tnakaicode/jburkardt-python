#! /usr/bin/env python
#
def bessel_i0_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_I0_VALUES returns some values of the I0 Bessel function.
    #
    #  Discussion:
    #
    #    The modified Bessel functions In(Z) and Kn(Z) are solutions of
    #    the differential equation
    #
    #      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
    #
    #    The modified Bessel function I0(Z) corresponds to N = 0.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselI[0,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 December 2014
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
        0.1000000000000000E+01,
        0.1010025027795146E+01,
        0.1040401782229341E+01,
        0.1092045364317340E+01,
        0.1166514922869803E+01,
        0.1266065877752008E+01,
        0.1393725584134064E+01,
        0.1553395099731217E+01,
        0.1749980639738909E+01,
        0.1989559356618051E+01,
        0.2279585302336067E+01,
        0.3289839144050123E+01,
        0.4880792585865024E+01,
        0.7378203432225480E+01,
        0.1130192195213633E+02,
        0.1748117185560928E+02,
        0.2723987182360445E+02,
        0.6723440697647798E+02,
        0.4275641157218048E+03,
        0.2815716628466254E+04))

    x_vec = np.array((
        0.00E+00,
        0.20E+00,
        0.40E+00,
        0.60E+00,
        0.80E+00,
        0.10E+01,
        0.12E+01,
        0.14E+01,
        0.16E+01,
        0.18E+01,
        0.20E+01,
        0.25E+01,
        0.30E+01,
        0.35E+01,
        0.40E+01,
        0.45E+01,
        0.50E+01,
        0.60E+01,
        0.80E+01,
        0.10E+02))

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


def bessel_i0_values_test():

    # *****************************************************************************80
    #
    # BESSEL_I0_VALUES_TEST demonstrates the use of BESSEL_I0_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('BESSEL_I0_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BESSEL_I0_VALUES stores values of the Bessel I function. of order 0.')
    print('')
    print('      X           I(0,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_i0_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_I0_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_i1_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_I1_VALUES returns some values of the I1 Bessel function.
    #
    #  Discussion:
    #
    #    The modified Bessel functions In(Z) and Kn(Z) are solutions of
    #    the differential equation
    #
    #      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselI[1,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
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
        0.0000000000000000E+00,
        0.1005008340281251E+00,
        0.2040267557335706E+00,
        0.3137040256049221E+00,
        0.4328648026206398E+00,
        0.5651591039924850E+00,
        0.7146779415526431E+00,
        0.8860919814143274E+00,
        0.1084810635129880E+01,
        0.1317167230391899E+01,
        0.1590636854637329E+01,
        0.2516716245288698E+01,
        0.3953370217402609E+01,
        0.6205834922258365E+01,
        0.9759465153704450E+01,
        0.1538922275373592E+02,
        0.2433564214245053E+02,
        0.6134193677764024E+02,
        0.3998731367825601E+03,
        0.2670988303701255E+04))

    x_vec = np.array((
        0.00E+00,
        0.20E+00,
        0.40E+00,
        0.60E+00,
        0.80E+00,
        0.10E+01,
        0.12E+01,
        0.14E+01,
        0.16E+01,
        0.18E+01,
        0.20E+01,
        0.25E+01,
        0.30E+01,
        0.35E+01,
        0.40E+01,
        0.45E+01,
        0.50E+01,
        0.60E+01,
        0.80E+01,
        0.10E+02))

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


def bessel_i1_values_test():

    # *****************************************************************************80
    #
    # BESSEL_I1_VALUES_TEST demonstrates the use of BESSEL_I1_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('BESSEL_I1_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BESSEL_I1_VALUES stores values of the Bessel I function. of order 1.')
    print('')
    print('      X           I(1,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_i1_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_I1_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_j0_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_J0_VALUES returns some values of the J0 Bessel function.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselJ[0,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 September 2004
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
    n_max = 21

    fx_vec = [
    ]

    x_vec = [
    ]
    import numpy as np

    n_max = 21

    fx_vec = np.array((
        -0.1775967713143383E+00,
        -0.3971498098638474E+00,
        -0.2600519549019334E+00,
        0.2238907791412357E+00,
        0.7651976865579666E+00,
        0.1000000000000000E+01,
        0.7651976865579666E+00,
        0.2238907791412357E+00,
        -0.2600519549019334E+00,
        -0.3971498098638474E+00,
        -0.1775967713143383E+00,
        0.1506452572509969E+00,
        0.3000792705195556E+00,
        0.1716508071375539E+00,
        -0.9033361118287613E-01,
        -0.2459357644513483E+00,
        -0.1711903004071961E+00,
        0.4768931079683354E-01,
        0.2069261023770678E+00,
        0.1710734761104587E+00,
        -0.1422447282678077E-01))

    x_vec = np.array((
        -5.0E+00,
        -4.0E+00,
        -3.0E+00,
        -2.0E+00,
        -1.0E+00,
        0.0E+00,
        1.0E+00,
        2.0E+00,
        3.0E+00,
        4.0E+00,
        5.0E+00,
        6.0E+00,
        7.0E+00,
        8.0E+00,
        9.0E+00,
        10.0E+00,
        11.0E+00,
        12.0E+00,
        13.0E+00,
        14.0E+00,
        15.0E+00))

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


def bessel_j0_values_test():

    # *****************************************************************************80
    #
    # BESSEL_J0_VALUES_TEST demonstrates the use of BESSEL_J0_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_J0_VALUES_TEST:')
    print('  BESSEL_J0_VALUES stores values of the Bessel J function. of order 0.')
    print('')
    print('      X           J(0,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_j0_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_J0_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_j1_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_J1_VALUES returns some values of the J1 Bessel function.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselJ[1,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
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

    n_max = 21

    fx_vec = np.array((
        0.3275791375914652E+00,
        0.6604332802354914E-01,
        -0.3390589585259365E+00,
        -0.5767248077568734E+00,
        -0.4400505857449335E+00,
        0.0000000000000000E+00,
        0.4400505857449335E+00,
        0.5767248077568734E+00,
        0.3390589585259365E+00,
        -0.6604332802354914E-01,
        -0.3275791375914652E+00,
        -0.2766838581275656E+00,
        -0.4682823482345833E-02,
        0.2346363468539146E+00,
        0.2453117865733253E+00,
        0.4347274616886144E-01,
        -0.1767852989567215E+00,
        -0.2234471044906276E+00,
        -0.7031805212177837E-01,
        0.1333751546987933E+00,
        0.2051040386135228E+00))

    x_vec = np.array((
        -5.0E+00,
        -4.0E+00,
        -3.0E+00,
        -2.0E+00,
        -1.0E+00,
        0.0E+00,
        1.0E+00,
        2.0E+00,
        3.0E+00,
        4.0E+00,
        5.0E+00,
        6.0E+00,
        7.0E+00,
        8.0E+00,
        9.0E+00,
        10.0E+00,
        11.0E+00,
        12.0E+00,
        13.0E+00,
        14.0E+00,
        15.0E+00))

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


def bessel_j1_values_test():

    # *****************************************************************************80
    #
    # BESSEL_J1_VALUES_TEST demonstrates the use of BESSEL_J1_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_J1_VALUES_TEST:')
    print('  BESSEL_J1_VALUES stores values of the Bessel J function. of order 1.')
    print('')
    print('      X           J(1,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_j1_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_J1_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_k0_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_K0_VALUES returns some values of the K0 Bessel function.
    #
    #  Discussion:
    #
    #    The modified Bessel functions In(Z) and Kn(Z) are solutions of
    #    the differential equation
    #
    #      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
    #
    #    The modified Bessel function K0(Z) corresponds to N = 0.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselK[0,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 December 2014
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
        0.2427069024702017E+01,
        0.1752703855528146E+01,
        0.1114529134524434E+01,
        0.7775220919047293E+00,
        0.5653471052658957E+00,
        0.4210244382407083E+00,
        0.3185082202865936E+00,
        0.2436550611815419E+00,
        0.1879547519693323E+00,
        0.1459314004898280E+00,
        0.1138938727495334E+00,
        0.6234755320036619E-01,
        0.3473950438627925E-01,
        0.1959889717036849E-01,
        0.1115967608585302E-01,
        0.6399857243233975E-02,
        0.3691098334042594E-02,
        0.1243994328013123E-02,
        0.1464707052228154E-03,
        0.1778006231616765E-04))

    x_vec = np.array((
        0.1E+00,
        0.2E+00,
        0.4E+00,
        0.6E+00,
        0.8E+00,
        1.0E+00,
        1.2E+00,
        1.4E+00,
        1.6E+00,
        1.8E+00,
        2.0E+00,
        2.5E+00,
        3.0E+00,
        3.5E+00,
        4.0E+00,
        4.5E+00,
        5.0E+00,
        6.0E+00,
        8.0E+00,
        10.0E+00))

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


def bessel_k0_values_test():

    # *****************************************************************************80
    #
    # BESSEL_K0_VALUES_TEST demonstrates the use of BESSEL_K0_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_K0_VALUES_TEST:')
    print('  BESSEL_K0_VALUES stores values of the Bessel K function. of order 0.')
    print('')
    print('      X           K(0,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_k0_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_K0_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_k1_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_K1_VALUES returns some values of the K1 Bessel function.
    #
    #  Discussion:
    #
    #    The modified Bessel functions In(Z) and Kn(Z) are solutions of
    #    the differential equation
    #
    #      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
    #
    #    The modified Bessel function K1(Z) corresponds to N = 1.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselK[1,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 December 2014
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
        0.9853844780870606E+01,
        0.4775972543220472E+01,
        0.2184354424732687E+01,
        0.1302834939763502E+01,
        0.8617816344721803E+00,
        0.6019072301972346E+00,
        0.4345923910607150E+00,
        0.3208359022298758E+00,
        0.2406339113576119E+00,
        0.1826230998017470E+00,
        0.1398658818165224E+00,
        0.7389081634774706E-01,
        0.4015643112819418E-01,
        0.2223939292592383E-01,
        0.1248349888726843E-01,
        0.7078094908968090E-02,
        0.4044613445452164E-02,
        0.1343919717735509E-02,
        0.1553692118050011E-03,
        0.1864877345382558E-04))

    x_vec = np.array((
        0.1E+00,
        0.2E+00,
        0.4E+00,
        0.6E+00,
        0.8E+00,
        1.0E+00,
        1.2E+00,
        1.4E+00,
        1.6E+00,
        1.8E+00,
        2.0E+00,
        2.5E+00,
        3.0E+00,
        3.5E+00,
        4.0E+00,
        4.5E+00,
        5.0E+00,
        6.0E+00,
        8.0E+00,
        10.0E+00))

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


def bessel_k1_values_test():

    # *****************************************************************************80
    #
    # BESSEL_K1_VALUES_TEST demonstrates the use of BESSEL_K1_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_K1_VALUES_TEST:')
    print('  BESSEL_K1_VALUES stores values of the Bessel K function. of order 1.')
    print('')
    print('      X           K(1,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_k1_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_K1_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_kx_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_KX_VALUES returns some values of the Kx Bessel function.
    #
    #  Discussion:
    #
    #    This set of data considers the less common case in which the
    #    index of the Bessel function Kn is actually not an integer.
    #    We may suggest this case by occasionally replacing the symbol
    #    "Kn" by "Kx".
    #
    #    The modified Bessel functions In(Z) and Kn(Z) are solutions of
    #    the differential equation
    #
    #      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselK[n,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz, Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    National Bureau of Standards, 1964,
    #    ISBN: 0-486-61272-4,
    #    LC: QA47.A34.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Cambridge University Press, 1999,
    #    ISBN: 0-521-64314-7,
    #    LC: QA76.95.W65.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real NU, the order of the function.
    #
    #    Output, real X, the argument of the function.
    #
    #    Output, real FX, the value of the function.
    #
    import numpy as np

    n_max = 28

    fx_vec = np.array((
        2.294489339798475E+00,
        0.4610685044478946E+00,
        0.1199377719680614E+00,
        0.06506594315400999E+00,
        0.03602598513176459E+00,
        0.003776613374642883E+00,
        0.00001799347809370518E+00,
        5.776373974707445E-10,
        0.9221370088957891E+00,
        0.1799066579520922E+00,
        0.004531936049571459E+00,
        0.00001979282590307570E+00,
        3.486992497366216E-23,
        3.227479531135262E+00,
        0.3897977588961997E+00,
        0.006495775004385758E+00,
        0.00002393132586462789E+00,
        3.627839645299048E-23,
        0.7311451879202114E+00,
        0.1567475478393932E+00,
        0.004257389528177461E+00,
        0.00001915541065869563E+00,
        3.463337593569306E-23,
        4.731184839919541E+00,
        0.4976876225514758E+00,
        0.007300864610941163E+00,
        0.00002546421294106458E+00,
        3.675275677913656E-23))

    nu_vec = np.array((
        0.50E+00,
        0.50E+00,
        0.50E+00,
        0.50E+00,
        0.50E+00,
        0.50E+00,
        0.50E+00,
        0.50E+00,
        1.50E+00,
        1.50E+00,
        1.50E+00,
        1.50E+00,
        1.50E+00,
        2.50E+00,
        2.50E+00,
        2.50E+00,
        2.50E+00,
        2.50E+00,
        1.25E+00,
        1.25E+00,
        1.25E+00,
        1.25E+00,
        1.25E+00,
        2.75E+00,
        2.75E+00,
        2.75E+00,
        2.75E+00,
        2.75E+00))

    x_vec = np.array((
        0.2E+00,
        1.0E+00,
        2.0E+00,
        2.5E+00,
        3.0E+00,
        5.0E+00,
        10.0E+00,
        20.0E+00,
        1.0E+00,
        2.0E+00,
        5.0E+00,
        10.0E+00,
        50.0E+00,
        1.0E+00,
        2.0E+00,
        5.0E+00,
        10.0E+00,
        50.0E+00,
        1.0E+00,
        2.0E+00,
        5.0E+00,
        10.0E+00,
        50.0E+00,
        1.0E+00,
        2.0E+00,
        5.0E+00,
        10.0E+00,
        50.0E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        nu = 0
        x = 0.0
        fx = 0.0
    else:
        nu = nu_vec[n_data]
        x = x_vec[n_data]
        fx = fx_vec[n_data]
        n_data = n_data + 1

    return n_data, nu, x, fx


def bessel_kx_values_test():

    # *****************************************************************************80
    #
    # BESSEL_KX_VALUES_TEST demonstrates the use of BESSEL_KX_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_KX_VALUES_TEST:')
    print('  BESSEL_KX_VALUES stores values of the Bessel K function. of real order NU.')
    print('')
    print('      NU          X           K(NU,X)')
    print('')

    n_data = 0

    while (True):

        n_data, nu, x, fx = bessel_kx_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %12f  %24.16g' % (nu, x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_KX_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_y0_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_Y0_VALUES returns some values of the Y0 Bessel function.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselY[0,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 December 2014
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

    n_max = 16

    fx_vec = np.array((
        -0.1534238651350367E+01,
        0.8825696421567696E-01,
        0.5103756726497451E+00,
        0.3768500100127904E+00,
        -0.1694073932506499E-01,
        -0.3085176252490338E+00,
        -0.2881946839815792E+00,
        -0.2594974396720926E-01,
        0.2235214893875662E+00,
        0.2499366982850247E+00,
        0.5567116728359939E-01,
        -0.1688473238920795E+00,
        -0.2252373126343614E+00,
        -0.7820786452787591E-01,
        0.1271925685821837E+00,
        0.2054642960389183E+00))

    x_vec = np.array((
        0.1E+00,
        1.0E+00,
        2.0E+00,
        3.0E+00,
        4.0E+00,
        5.0E+00,
        6.0E+00,
        7.0E+00,
        8.0E+00,
        9.0E+00,
        10.0E+00,
        11.0E+00,
        12.0E+00,
        13.0E+00,
        14.0E+00,
        15.0E+00))

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


def bessel_y0_values_test():

    # *****************************************************************************80
    #
    # BESSEL_Y0_VALUES_TEST demonstrates the use of BESSEL_Y0_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_Y0_VALUES_TEST:')
    print('  BESSEL_Y0_VALUES stores values of the Bessel Y function. of order 0.')
    print('')
    print('      X           Y(0,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_y0_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_Y0_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bessel_y1_values(n_data):

    # *****************************************************************************80
    #
    # BESSEL_Y1_VALUES returns some values of the Y1 Bessel function.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      BesselY[1,x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 December 2014
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

    n_max = 16

    fx_vec = np.array((
        -0.6458951094702027E+01,
        -0.7812128213002887E+00,
        -0.1070324315409375E+00,
        0.3246744247918000E+00,
        0.3979257105571000E+00,
        0.1478631433912268E+00,
        -0.1750103443003983E+00,
        -0.3026672370241849E+00,
        -0.1580604617312475E+00,
        0.1043145751967159E+00,
        0.2490154242069539E+00,
        0.1637055374149429E+00,
        -0.5709921826089652E-01,
        -0.2100814084206935E+00,
        -0.1666448418561723E+00,
        0.2107362803687351E-01))

    x_vec = np.array((
        0.1E+00,
        1.0E+00,
        2.0E+00,
        3.0E+00,
        4.0E+00,
        5.0E+00,
        6.0E+00,
        7.0E+00,
        8.0E+00,
        9.0E+00,
        10.0E+00,
        11.0E+00,
        12.0E+00,
        13.0E+00,
        14.0E+00,
        15.0E+00))

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


def bessel_y1_values_test():

    # *****************************************************************************80
    #
    # BESSEL_Y1_VALUES_TEST demonstrates the use of BESSEL_Y1_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BESSEL_Y1_VALUES_TEST:')
    print('  BESSEL_Y1_VALUES stores values of the Bessel Y function. of order 1.')
    print('')
    print('      X           Y(1,X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = bessel_y1_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16g' % (x, fx))
#
#  Terminate.
#
    print('')
    print('BESSEL_Y1_VALUES_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    bessel_i0_values_test()
    bessel_i1_values_test()
    bessel_j0_values_test()
    bessel_j1_values_test()
    bessel_k0_values_test()
    bessel_k1_values_test()
    bessel_kx_values_test()
    bessel_y0_values_test()
    bessel_y1_values_test()
    timestamp()
