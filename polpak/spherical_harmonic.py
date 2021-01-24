#! /usr/bin/env python
#
def spherical_harmonic(l, m, theta, phi):

    # *****************************************************************************80
    #
    # SPHERICAL_HARMONIC evaluates spherical harmonic functions.
    #
    #  Discussion:
    #
    #    The spherical harmonic function Y(L,M,THETA,PHI)(X) is the
    #    angular part of the solution to Laplace's equation in spherical
    #    coordinates.
    #
    #    Y(L,M,THETA,PHI)(X) is related to the associated Legendre
    #    function as follows:
    #
    #      Y(L,M,THETA,PHI)(X) = FACTOR * P(L,M)(cos(THETA)) * exp ( i * M * PHI )
    #
    #    Here, FACTOR is a normalization factor:
    #
    #      FACTOR = sqrt ( ( 2 * L + 1 ) * ( L - M )! / ( 4 * PI * ( L + M )! ) )
    #
    #    In Mathematica, a spherical harmonic function can be evaluated by
    #
    #      SphericalHarmonicY [ l, m, theta, phi ]
    #
    #    Note that notational tradition in physics requires that THETA
    #    and PHI represent the reverse of what they would normally mean
    #    in mathematical notation; that is, THETA goes up and down, and
    #    PHI goes around.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
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
    #    Eric Weisstein,
    #    CRC Concise Encyclopedia of Mathematics,
    #    CRC Press, 1999.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Wolfram Media / Cambridge University Press, 1999.
    #
    #  Parameters:
    #
    #    Input, integer L, the first index of the spherical harmonic function.
    #    Normally, 0 <= L.
    #
    #    Input, integer M, the second index of the spherical harmonic function.
    #    Normally, -L <= M <= L.
    #
    #    Input, real THETA, the polar angle, for which
    #    0 <= THETA <= PI.
    #
    #    Input, real PHI, the longitudinal angle, for which
    #    0 <= PHI <= 2*PI.
    #
    #    Output, real C(1:L+1), S(1:L+1), the real and imaginary
    #    parts of the functions Y(L,0:L,THETA,PHI).
    #
    import numpy as np
    from legendre_associated_normalized import legendre_associated_normalized

    m_abs = abs(m)

    plm = legendre_associated_normalized(l, m_abs, np.cos(theta))

    c = np.zeros(l + 1)
    s = np.zeros(l + 1)

    for i in range(0, l + 1):
        c[i] = plm[i] * np.cos(float(m) * phi)
        s[i] = plm[i] * np.sin(float(m) * phi)

    if (m < 0):
        for i in range(0, l + 1):
            c[i] = - c[i]
            s[i] = - s[i]

    return c, s


def spherical_harmonic_test():

    # *****************************************************************************80
    #
    # SPHERICAL_HARMONIC_TEST tests SPHERICAL_HARMONIC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from spherical_harmonic_values import spherical_harmonic_values

    print('')
    print('SPHERICAL_HARMONIC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERICAL_HARMONIC evaluats the spherical harmonic function;')
    print('')
    print('      L       M    THETA   PHI   YR   YI')
    print('')

    n_data = 0

    while (True):

        n_data, l, m, theta, phi, yr, yi = spherical_harmonic_values(n_data)

        if (n_data == 0):
            break

        c, s = spherical_harmonic(l, m, theta, phi)

        print('  %6d  %6d  %6f  %6f  %12f  %12f' % (l, m, theta, phi, yr, yi))
        print('                                      %12f  %12f' %
              (c[l], s[l]))
#
#  Terminate.
#
    print('')
    print('SPHERICAL_HARMONIC_TEST')
    print('  Normal end of execution.')
    return


def spherical_harmonic_values(n_data):

    # *****************************************************************************80
    #
    # SPHERICAL_HARMONIC_VALUES returns values of spherical harmonic functions.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      SphericalHarmonicY [ l, m, theta, phi ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 February 2015
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
    #    Eric Weisstein,
    #    CRC Concise Encyclopedia of Mathematics,
    #    CRC Press, 1998.
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
    #    Output, integer L, integer M, real THETA, PHI, the arguments
    #    of the function.
    #
    #    Output, real YR, YI, the real and imaginary parts of
    #    the function.
    #
    import numpy as np

    n_max = 20

    l_vec = np.array((
        0, 1, 2,
        3, 4, 5,
        5, 5, 5,
        5, 4, 4,
        4, 4, 4,
        3, 3, 3,
        3, 3))
    m_vec = np.array((
        0, 0, 1,
        2, 3, 5,
        4, 3, 2,
        1, 2, 2,
        2, 2, 2,
        -1, -1, -1,
        -1, -1))
    phi_vec = np.array((
        0.1047197551196598E+01, 0.1047197551196598E+01, 0.1047197551196598E+01,
        0.1047197551196598E+01, 0.1047197551196598E+01, 0.6283185307179586E+00,
        0.6283185307179586E+00, 0.6283185307179586E+00, 0.6283185307179586E+00,
        0.6283185307179586E+00, 0.7853981633974483E+00, 0.7853981633974483E+00,
        0.7853981633974483E+00, 0.7853981633974483E+00, 0.7853981633974483E+00,
        0.4487989505128276E+00, 0.8975979010256552E+00, 0.1346396851538483E+01,
        0.1795195802051310E+01, 0.2243994752564138E+01))
    theta_vec = np.array((
        0.5235987755982989E+00, 0.5235987755982989E+00, 0.5235987755982989E+00,
        0.5235987755982989E+00, 0.5235987755982989E+00, 0.2617993877991494E+00,
        0.2617993877991494E+00, 0.2617993877991494E+00, 0.2617993877991494E+00,
        0.2617993877991494E+00, 0.6283185307179586E+00, 0.1884955592153876E+01,
        0.3141592653589793E+01, 0.4398229715025711E+01, 0.5654866776461628E+01,
        0.3926990816987242E+00, 0.3926990816987242E+00, 0.3926990816987242E+00,
        0.3926990816987242E+00, 0.3926990816987242E+00))
    yi_vec = np.array((
        0.0000000000000000E+00, 0.0000000000000000E+00, -0.2897056515173922E+00,
        0.1916222768312404E+00, 0.0000000000000000E+00, 0.0000000000000000E+00,
        0.3739289485283311E-02, -0.4219517552320796E-01, 0.1876264225575173E+00,
        -0.3029973424491321E+00, 0.4139385503112256E+00, -0.1003229830187463E+00,
        0.0000000000000000E+00, -0.1003229830187463E+00, 0.4139385503112256E+00,
        -0.1753512375142586E+00, -0.3159720118970196E+00, -0.3940106541811563E+00,
        -0.3940106541811563E+00, -0.3159720118970196E+00))
    yr_vec = np.array((
        0.2820947917738781E+00, 0.4231421876608172E+00, -0.1672616358893223E+00,
        -0.1106331731112457E+00, 0.1354974113737760E+00, 0.5390423109043568E-03,
        -0.5146690442951909E-02, 0.1371004361349490E-01, 0.6096352022265540E-01,
        -0.4170400640977983E+00, 0.0000000000000000E+00, 0.0000000000000000E+00,
        0.0000000000000000E+00, 0.0000000000000000E+00, 0.0000000000000000E+00,
        0.3641205966137958E+00, 0.2519792711195075E+00, 0.8993036065704300E-01,
        -0.8993036065704300E-01, -0.2519792711195075E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        l = 0
        m = 0
        theta = 0.0
        phi = 0.0
        yr = 0.0
        yi = 0.0
    else:
        l = l_vec[n_data]
        m = m_vec[n_data]
        theta = theta_vec[n_data]
        phi = phi_vec[n_data]
        yr = yr_vec[n_data]
        yi = yi_vec[n_data]
        n_data = n_data + 1

    return n_data, l, m, theta, phi, yr, yi


def spherical_harmonic_values_test():

    # *****************************************************************************80
    #
    # SPHERICAL_HARMONIC_VALUES_TEST demonstrates the use of SPHERICAL_HARMONIC_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SPHERICAL_HARMONIC_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERICAL_HARMONIC_VALUES stores values of the SPHERICAL_HARMONIC function.')
    print('')
    print('   L   M    THETA   PHI               YR                YI')
    print('')

    n_data = 0

    while (True):

        n_data, l, m, theta, phi, yr, yi = spherical_harmonic_values(n_data)

        if (n_data == 0):
            break

        print('  %2d  %2d  %8f  %8f  %24.16f  %24.16f' %
              (l, m, theta, phi, yr, yi))
#
#  Terminate.
#
    print('')
    print('SPHERICAL_HARMONIC_VALUES_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    spherical_harmonic_test()
    spherical_harmonic_values_test()
    timestamp()
