#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import math
import platform
import time
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def bivariate_normal_cdf_values(n_data):

    # *****************************************************************************80
    #
    # BIVARIATE_NORMAL_CDF_VALUES returns some values of the bivariate normal CDF.
    #
    #  Discussion:
    #
    #    FXY is the probability that two variables A and B, which are
    #    related by a bivariate normal distribution with correlation R,
    #    respectively satisfy A <= X and B <= Y.
    #
    #    Mathematica can evaluate the bivariate normal CDF via the commands:
    #
    #      <<MultivariateStatistics`
    #      cdf = CDF[MultinormalDistribution[{0,0}{{1,r},{r,1}}],{x,y}]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    National Bureau of Standards,
    #    Tables of the Bivariate Normal Distribution and Related Functions,
    #    NBS, Applied Mathematics Series, Number 50, 1959.
    #
    #  Parameters:
    #
    #    Input, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.
    #
    #    Output, integer N_DATA, the routine increments the input value of N_DATA
    #    by 1, and returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real X, Y, the parameters of the function.
    #
    #    Output, real R, the correlation value.
    #
    #    Output, real F, the value of the function.
    #
    import numpy as np

    n_max = 41

    f_vec = np.array((
        0.02260327218569867,
        0.1548729518584100,
        0.4687428083352184,
        0.7452035868929476,
        0.8318608306874188,
        0.8410314261134202,
        0.1377019384919464,
        0.1621749501739030,
        0.1827411243233119,
        0.2010067421506235,
        0.2177751155265290,
        0.2335088436446962,
        0.2485057781834286,
        0.2629747825154868,
        0.2770729823404738,
        0.2909261168683812,
        0.3046406378726738,
        0.3183113449213638,
        0.3320262544108028,
        0.3458686754647614,
        0.3599150462310668,
        0.3742210899871168,
        0.3887706405282320,
        0.4032765198361344,
        0.4162100291953678,
        0.6508271498838664,
        0.8318608306874188,
        0.0000000000000000,
        0.1666666666539970,
        0.2500000000000000,
        0.3333333333328906,
        0.5000000000000000,
        0.7452035868929476,
        0.1548729518584100,
        0.1548729518584100,
        0.06251409470431653,
        0.7452035868929476,
        0.1548729518584100,
        0.1548729518584100,
        0.06251409470431653,
        0.6337020457912916))

    r_vec = np.array((
        0.500, 0.500, 0.500, 0.500, 0.500,
        0.500, -0.900, -0.800, -0.700, -0.600,
        -0.500, -0.400, -0.300, -0.200, -0.100,
        0.000, 0.100, 0.200, 0.300, 0.400,
        0.500, 0.600, 0.700, 0.800, 0.900,
        0.673, 0.500, -1.000, -0.500, 0.000,
        0.500, 1.000, 0.500, 0.500, 0.500,
        0.500, 0.500, 0.500, 0.500, 0.500,
        0.500))

    x_vec = np.array((
        -2.0, -1.0, 0.0, 1.0, 2.0,
        3.0, -0.2, -0.2, -0.2, -0.2,
        -0.2, -0.2, -0.2, -0.2, -0.2,
        -0.2, -0.2, -0.2, -0.2, -0.2,
        -0.2, -0.2, -0.2, -0.2, -0.2,
        1.0, 2.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 1.0, -1.0,
        -1.0, 1.0, 1.0, -1.0, -1.0,
        0.7071067811865475))

    y_vec = np.array((
        1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 0.5, 0.5, 0.5, 0.5,
        0.5, 0.5, 0.5, 0.5, 0.5,
        0.5, 0.5, 0.5, 0.5, 0.5,
        0.5, 0.5, 0.5, 0.5, 0.5,
        0.5, 1.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 1.0, -1.0, 1.0,
        -1.0, 1.0, -1.0, 1.0, -1.0,
        0.7071067811865475))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        x = 0.0
        y = 0.0
        r = 0.0
        f = 0.0
    else:
        x = x_vec[n_data]
        y = y_vec[n_data]
        r = r_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, x, y, r, f


def bivariate_normal_cdf_values_test():

    # *****************************************************************************80
    #
    # BIVARIATE_NORMAL_CDF_VALUES_TEST tests BIVARIATE_NORMAL_CDF_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BIVARIATE_NORMAL_CDF_VALUES_TEST:')
    print('  BIVARIATE_NORMAL_CDF_VALUES stores values of the bivariate normal CDF.')
    print('')
    print('      X         Y         R        BIVARIATE_NORMAL_CDF(X,Y,R)')
    print('')

    n_data = 0

    while (True):

        n_data, x, y, r, f = bivariate_normal_cdf_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %12f  %12f  %24.16g' % (x, y, r, f))
#
#  Terminate.
#
    print('')
    print('BIVARIATE_NORMAL_CDF_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def bivnor(ah, ak, r):

    # *****************************************************************************80
    #
    # BIVNOR computes the bivariate normal CDF.
    #
    #  Discussion:
    #
    #    BIVNOR computes the probability for two normal variates X and Y
    #    whose correlation is R, that AH <= X and AK <= Y.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Thomas Donnelly.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Thomas Donnelly,
    #    Algorithm 462: Bivariate Normal Distribution,
    #    Communications of the ACM,
    #    October 1973, Volume 16, Number 10, page 638.
    #
    #  Parameters:
    #
    #    Input, real AH, AK, the lower limits of integration.
    #
    #    Input, real R, the correlation between X and Y.
    #
    #    Output, real VALUE, the bivariate normal CDF.
    #
    #  Local Parameters:
    #
    #    Local, integer IDIG, the number of significant digits
    #    to the right of the decimal point desired in the answer.
    #
    import numpy as np
    from sys import exit

    idig = 15
    b = 0.0

    gh = gauss(- ah) / 2.0
    gk = gauss(- ak) / 2.0

    if (r == 0.0):
        b = 4.00 * gh * gk
        b = max(b, 0.0)
        b = min(b, 1.0)
        value = b
        return value

    rr = (1.0 + r) * (1.0 - r)

    if (rr < 0.0):
        print('')
        print('BIVNOR - Fatal error!')
        print('  1 < |R|.')
        exit('BIVNOR - Fatal error!')

    if (rr == 0.0):

        if (r < 0.0):

            if (ah + ak < 0.0):
                b = 2.0 * (gh + gk) - 1.0

        else:

            if (ah - ak < 0.0):
                b = 2.0 * gk
            else:
                b = 2.0 * gh

        b = max(b, 0.0)
        b = min(b, 1.0)
        value = b
        return value

    sqr = np.sqrt(rr)

    if (idig == 15):
        con = 2.0 * np.pi * 1.0E-15 / 2.0
    else:
        con = np.pi
        for i in range(0, idig):
            con = con / 10.0
#
#  (0,0)
#
    if (ah == 0.0 and ak == 0.0):
        b = 0.25 + 0.5 * np.arcsin(r) / np.pi
        b = max(b, 0.0)
        b = min(b, 1.0)
        value = b
        return value
#
#  (0,nonzero)
#
    if (ah == 0.0 and ak != 0.0):

        b = gk
        wh = - ak
        wk = (ah / ak - r) / sqr
        gw = 2.0 * gk
        iss = 1
#
#  (nonzero,0)
#
    elif (ah != 0.0 and ak == 0.0):

        b = gh
        wh = - ah
        wk = (ak / ah - r) / sqr
        gw = 2.0 * gh
        iss = - 1
#
#  (nonzero,nonzero)
#
    elif (ah != 0.0 and ak != 0.0):

        b = gh + gk
        if (ah * ak < 0.0):
            b = b - 0.5
        wh = - ah
        wk = (ak / ah - r) / sqr
        gw = 2.0 * gh
        iss = -1

    while (True):

        sgn = - 1.0
        t = 0.0

        if (wk != 0.0):

            if (abs(wk) == 1.0):

                t = wk * gw * (1.0 - gw) / 2.0
                b = b + sgn * t

            else:

                if (1.0 < abs(wk)):

                    sgn = - sgn
                    wh = wh * wk
                    g2 = gauss(wh)
                    wk = 1.0 / wk

                    if (wk < 0.0):
                        b = b + 0.5

                    b = b - (gw + g2) / 2.0 + gw * g2

                h2 = wh * wh
                a2 = wk * wk
                h4 = h2 / 2.0
                ex = np.exp(- h4)
                w2 = h4 * ex
                ap = 1.0
                s2 = ap - ex
                sp = ap
                s1 = 0.0
                sn = s1
                conex = abs(con / wk)

                while (True):

                    cn = ap * s2 / (sn + sp)
                    s1 = s1 + cn

                    if (abs(cn) <= conex):
                        break

                    sn = sp
                    sp = sp + 1.0
                    s2 = s2 - w2
                    w2 = w2 * h4 / sp
                    ap = - ap * a2

                t = 0.5 * (np.arctan(wk) - wk * s1) / np.pi
                b = b + sgn * t

        if (0 <= iss):
            break

        if (ak == 0.0):
            break

        wh = - ak
        wk = (ah / ak - r) / sqr
        gw = 2.0 * gk
        iss = 1

    b = max(b, 0.0)
    b = min(b, 1.0)
    value = b

    return value


def bivnor_test():

    # *****************************************************************************80
    #
    # BIVNOR_TEST demonstrates the use of BIVNOR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('BIVNOR_TEST:')
    print('  BIVNOR computes the bivariate normal probability.')
    print('  Compare to tabulated values.')
    print('')
    print('      X             Y             R             P                         P                       DIFF')
    print('                                               (Tabulated)               (BIVNOR)')
    print('')

    n_data = 0

    while (True):

        n_data, x, y, r, fxy1 = bivariate_normal_cdf_values(n_data)

        if (n_data == 0):
            break

        fxy2 = bivnor(- x, - y, r)

        print('  %12.8f  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' %
              (x, y, r, fxy1, fxy2, abs(fxy1 - fxy2)))
#
#  Terminate.
#
    print('')
    print('BIVNOR_TEST:')
    print('  Normal end of execution.')
    return


def gauss(t):

    # *****************************************************************************80
    #
    # GAUSS is a univariate lower normal tail area.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Thomas Donnelly,
    #    Algorithm 462: Bivariate Normal Distribution,
    #    Communications of the ACM,
    #    October 1973, Volume 16, Number 10, page 638.
    #
    #  Parameters:
    #
    #    Input, real T, the evaluation point.
    #
    #    Output, real VALUE, the area of the lower tail of the normal PDF
    #    from -oo to T.
    #
    import numpy as np
    import scipy
    from scipy import special

    value = (1.0 + scipy.special.erf(t / np.sqrt(2.0))) / 2.0

    return value


def normal_01_cdf_values(n_data):

    # *****************************************************************************80
    #
    # NORMAL_01_CDF_VALUES returns some values of the Normal 01 CDF.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Needs["Statistics`ContinuousDistributions`"]
    #      dist = NormalDistribution [ 0, 1 ]
    #      CDF [ dist, x ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2015
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
    #    Output, real F, the value of the function.
    #
    import numpy as np

    n_max = 17

    f_vec = np.array((
        0.5000000000000000E+00,
        0.5398278372770290E+00,
        0.5792597094391030E+00,
        0.6179114221889526E+00,
        0.6554217416103242E+00,
        0.6914624612740131E+00,
        0.7257468822499270E+00,
        0.7580363477769270E+00,
        0.7881446014166033E+00,
        0.8159398746532405E+00,
        0.8413447460685429E+00,
        0.9331927987311419E+00,
        0.9772498680518208E+00,
        0.9937903346742239E+00,
        0.9986501019683699E+00,
        0.9997673709209645E+00,
        0.9999683287581669E+00))

    x_vec = np.array((
        0.0000000000000000E+00,
        0.1000000000000000E+00,
        0.2000000000000000E+00,
        0.3000000000000000E+00,
        0.4000000000000000E+00,
        0.5000000000000000E+00,
        0.6000000000000000E+00,
        0.7000000000000000E+00,
        0.8000000000000000E+00,
        0.9000000000000000E+00,
        0.1000000000000000E+01,
        0.1500000000000000E+01,
        0.2000000000000000E+01,
        0.2500000000000000E+01,
        0.3000000000000000E+01,
        0.3500000000000000E+01,
        0.4000000000000000E+01))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        x = 0.0
        f = 0.0
    else:
        x = x_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, x, f


def normal_01_cdf_values_test():

    # *****************************************************************************80
    #
    # NORMAL_01_CDF_VALUES_TEST demonstrates the use of NORMAL_01_CDF_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NORMAL_01_CDF_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  NORMAL_01_CDF_VALUES stores values of the unit normal CDF.')
    print('')
    print('      X         NORMAL_01_CDF(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, f = normal_01_cdf_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16f' % (x, f))
#
#  Terminate.
#
    print('')
    print('NORMAL_01_CDF_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def owen_values(n_data):

    # *****************************************************************************80
    #
    # OWEN_VALUES returns some values of Owen's T function.
    #
    #  Discussion:
    #
    #    Owen's T function is useful for computation of the bivariate normal
    #    distribution and the distribution of a skewed normal distribution.
    #
    #    Although it was originally formulated in terms of the bivariate
    #    normal function, the function can be defined more directly as
    #
    #      T(H,A) = 1 / ( 2 * pi ) *
    #        Integral ( 0 <= X <= A ) e^(H^2*(1+X^2)/2) / (1+X^2) dX
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      fx = 1/(2*Pi) * Integrate [ E^(-h^2*(1+x^2)/2)/(1+x^2), {x,0,a} ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Mike Patefield, David Tandy,
    #    Fast and Accurate Calculation of Owen's T Function,
    #    Journal of Statistical Software,
    #    Volume 5, Number 5, 2000, pages 1-25.
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
    #    Output, real H, a parameter.
    #
    #    Output, real A, the upper limit of the integral.
    #
    #    Output, real T, the value of the function.
    #
    import numpy as np

    n_max = 28

    a_vec = np.array((
        0.2500000000000000E+00,
        0.4375000000000000E+00,
        0.9687500000000000E+00,
        0.0625000000000000E+00,
        0.5000000000000000E+00,
        0.9999975000000000E+00,
        0.5000000000000000E+00,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.3000000000000000E+01,
        0.5000000000000000E+00,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.3000000000000000E+01,
        0.5000000000000000E+00,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.3000000000000000E+01,
        0.5000000000000000E+00,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.3000000000000000E+01,
        0.5000000000000000E+00,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.3000000000000000E+01,
        0.1000000000000000E+02,
        0.1000000000000000E+03))

    h_vec = np.array((
        0.0625000000000000E+00,
        6.5000000000000000E+00,
        7.0000000000000000E+00,
        4.7812500000000000E+00,
        2.0000000000000000E+00,
        1.0000000000000000E+00,
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.5000000000000000E+00,
        0.5000000000000000E+00,
        0.5000000000000000E+00,
        0.5000000000000000E+00,
        0.2500000000000000E+00,
        0.2500000000000000E+00,
        0.2500000000000000E+00,
        0.2500000000000000E+00,
        0.1250000000000000E+00,
        0.1250000000000000E+00,
        0.1250000000000000E+00,
        0.1250000000000000E+00,
        0.7812500000000000E-02,
        0.7812500000000000E-02,
        0.7812500000000000E-02,
        0.7812500000000000E-02,
        0.7812500000000000E-02,
        0.7812500000000000E-02))

    t_vec = np.array((
        3.8911930234701366E-02,
        2.0005773048508315E-11,
        6.3990627193898685E-13,
        1.0632974804687463E-07,
        8.6250779855215071E-03,
        6.6741808978228592E-02,
        0.4306469112078537E-01,
        0.6674188216570097E-01,
        0.7846818699308410E-01,
        0.7929950474887259E-01,
        0.6448860284750376E-01,
        0.1066710629614485E+00,
        0.1415806036539784E+00,
        0.1510840430760184E+00,
        0.7134663382271778E-01,
        0.1201285306350883E+00,
        0.1666128410939293E+00,
        0.1847501847929859E+00,
        0.7317273327500385E-01,
        0.1237630544953746E+00,
        0.1737438887583106E+00,
        0.1951190307092811E+00,
        0.7378938035365546E-01,
        0.1249951430754052E+00,
        0.1761984774738108E+00,
        0.1987772386442824E+00,
        0.2340886964802671E+00,
        0.2479460829231492E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        t = 0.0
        h = 0.0
        a = 0.0
    else:
        t = t_vec[n_data]
        h = h_vec[n_data]
        a = a_vec[n_data]
        n_data = n_data + 1

    return n_data, h, a, t


def owen_values_test():

    # *****************************************************************************80
    #
    # OWEN_VALUES_TEST demonstrates the use of OWEN_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('OWEN_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  OWEN_VALUES stores values of the OWEN function.')
    print('')
    print('      H         A          T')
    print('')

    n_data = 0

    while (True):

        n_data, h, a, t = owen_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %12f  %12f' % (h, a, t))
#
#  Terminate.
#
    print('')
    print('OWEN_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def q(h, ah):

    # *****************************************************************************80
    #
    # Q computes (1/2) * p(H<Z) - T(H,AH).
    #
    #  Discussion:
    #
    #    The routine computes Q = (1/2) * P( H < Z ) - T ( H, AH ).
    #
    #    The result for Q is non-negative.
    #
    #    Warning : Q is computed as the difference between two terms;
    #    When the two terms are of similar value this may produce
    #    error in Q.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Mike Patefield, David Tandy.
    #    MATLAB version by John Burkardt.
    #
    #  Reference:
    #
    #    Mike Patefield, David Tandy,
    #    Fast and Accurate Calculation of Owen's T Function,
    #    Journal of Statistical Software,
    #    Volume 5, Number 5, 2000, pages 1-25.
    #
    #  Parameters:
    #
    #    Input, real H, the lower limit for Z.
    #    0 < H.
    #
    #    Input, real AH, one of the arguments for the T function.
    #
    #    Output, real Q, the desired quantity.
    #
    rroot2 = 0.70710678118654752440

    if (1.0 < ah):
        ahh = ah * h
        value = tfun(ahh, 1.0 / ah, h) - znorm2(ahh) * znorm1(h)
    else:
        value = 0.5 * znorm2(h) - t(h, ah)

    return value


def t(h, a):

    # *****************************************************************************80
    #
    # T computes Owen's T function for arbitrary H and A.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Mike Patefield, David Tandy.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Mike Patefield, David Tandy,
    #    Fast and Accurate Calculation of Owen's T Function,
    #    Journal of Statistical Software,
    #    Volume 5, Number 5, 2000, pages 1-25.
    #
    #  Parameters:
    #
    #    Input, real H, A, the arguments.
    #
    #    Output, real VALUE, the value of Owen's T function.
    #
    cut = 0.67
    rroot2 = 0.70710678118654752440

    absh = abs(h)
    absa = abs(a)
    ah = absa * absh

    if (absa <= 1.0):

        value = tfun(absh, absa, ah)

    elif (absh <= cut):

        value = 0.25 - znorm1(absh) * znorm1(ah) - tfun(ah, 1.0 / absa, absh)

    else:

        normh = znorm2(absh)
        normah = znorm2(ah)
        value = 0.5 * (normh + normah) - normh * \
            normah - tfun(ah, 1.0 / absa, absh)

    if (a < 0.0):
        value = - value

    return value


def t_test():

    # *****************************************************************************80
    #
    # T_TEST demonstrates the use of T.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('T_TEST:')
    print('  T evaluates Owen''s T function.')
    print('  Compare to tabulated values.')
    print('')
    print('          H            A        T                         T')
    print('                                (Tabulated)               (T)                     DIFF')
    print('')

    n_data = 0

    while (True):

        n_data, h, a, t1 = owen_values(n_data)

        if (n_data == 0):
            break

        t2 = t(h, a)

        print('  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' %
              (h, a, t1, t2, abs(t1 - t2)))

    return


def tfun(h, a, ah):

    # *****************************************************************************80
    #
    # TFUN computes Owen's T function for a restricted range of parameters.
    #
    #  Discussion:
    #
    #    This routine computes Owen's T-function of H and A.
    #
    #    Originally called "TF", this function was renamed "TFUN" to avoid
    #    a conflict with a built in MATLAB routine.
    #
    #    Thanks to Benjamin Sobotta for pointing out a missing factor of
    #    0.5 that occurred where ZNORM1 was used, 15 December 2011.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Mike Patefield, David Tandy.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Mike Patefield, David Tandy,
    #    Fast and Accurate Calculation of Owen's T Function,
    #    Journal of Statistical Software,
    #    Volume 5, Number 5, 2000, pages 1-25.
    #
    #  Parameters:
    #
    #    Input, real H, the H argument of the function.
    #    0 <= H.
    #
    #    Input, real A, the A argument of the function.
    #    0 <= A <= 1.
    #
    #    Input, real AH, the value of A*H.
    #
    #    Output, real VALUE, the value of Owen's T function.
    #
    import numpy as np

    arange = np.array([
        0.025,
        0.09,
        0.15,
        0.36,
        0.5,
        0.9,
        0.99999])

    c2 = np.array([
        0.99999999999999987510,
        -0.99999999999988796462,
        0.99999999998290743652,
        -0.99999999896282500134,
        0.99999996660459362918,
        -0.99999933986272476760,
        0.99999125611136965852,
        -0.99991777624463387686,
        0.99942835555870132569,
        -0.99697311720723000295,
        0.98751448037275303682,
        -0.95915857980572882813,
        0.89246305511006708555,
        -0.76893425990463999675,
        0.58893528468484693250,
        -0.38380345160440256652,
        0.20317601701045299653,
        -0.82813631607004984866E-01,
        0.24167984735759576523E-01,
        -0.44676566663971825242E-02,
        0.39141169402373836468E-03])

    hrange = np.array([
        0.02,
        0.06,
        0.09,
        0.125,
        0.26,
        0.4,
        0.6,
        1.6,
        1.7,
        2.33,
        2.4,
        3.36,
        3.4,
        4.8])

    meth = np.array([
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        3,
        4,
        4,
        4,
        4,
        5,
        6])

    ord = np.array([
        2,
        3,
        4,
        5,
        7,
        10,
        12,
        18,
        10,
        20,
        30,
        20,
        4,
        7,
        8,
        20,
        13,
        0])

    pts = np.array([
        0.35082039676451715489E-02,
        0.31279042338030753740E-01,
        0.85266826283219451090E-01,
        0.16245071730812277011,
        0.25851196049125434828,
        0.36807553840697533536,
        0.48501092905604697475,
        0.60277514152618576821,
        0.71477884217753226516,
        0.81475510988760098605,
        0.89711029755948965867,
        0.95723808085944261843,
        0.99178832974629703586])

    rroot2 = 0.70710678118654752440
    rrtpi = 0.39894228040143267794
    rtwopi = 0.15915494309189533577

    select = np.array([
        [1, 1, 2, 13, 13, 13, 13, 13, 13, 13, 13, 16, 16, 16, 9],
        [1, 2, 2, 3, 3, 5, 5, 14, 14, 15, 15, 16, 16, 16, 9],
        [2, 2, 3, 3, 3, 5, 5, 15, 15, 15, 15, 16, 16, 16, 10],
        [2, 2, 3, 5, 5, 5, 5, 7, 7, 16, 16, 16, 16, 16, 10],
        [2, 3, 3, 5, 5, 6, 6, 8, 8, 17, 17, 17, 12, 12, 11],
        [2, 3, 5, 5, 5, 6, 6, 8, 8, 17, 17, 17, 12, 12, 12],
        [2, 3, 4, 4, 6, 6, 8, 8, 17, 17, 17, 17, 17, 12, 12],
        [2, 3, 4, 4, 6, 6, 18, 18, 18, 18, 17, 17, 17, 12, 12]])

    wts = np.array([
        0.18831438115323502887E-01,
        0.18567086243977649478E-01,
        0.18042093461223385584E-01,
        0.17263829606398753364E-01,
        0.16243219975989856730E-01,
        0.14994592034116704829E-01,
        0.13535474469662088392E-01,
        0.11886351605820165233E-01,
        0.10070377242777431897E-01,
        0.81130545742299586629E-02,
        0.60419009528470238773E-02,
        0.38862217010742057883E-02,
        0.16793031084546090448E-02])
#
#  Determine appropriate method from t1...t6
#
    ihint = 15
    for i in range(0, 14):
        if (h <= hrange[i]):
            ihint = i + 1
            break

    iaint = 8
    for i in range(0, 7):
        if (a <= arange[i]):
            iaint = i + 1
            break

    icode = select[iaint - 1, ihint - 1]
    m = ord[icode - 1]
#
#  t1(h, a, m)  m = 2, 3, 4, 5, 7, 10, 12 or 18
#  jj = 2j - 1  gj = exp(-h*h/2) * (-h*h/2)**j / j!
#  aj = a**(2j-1) / (2*pi)
#
    if (meth[icode - 1] == 1):

        hs = - 0.5 * h * h
        dhs = np.exp(hs)
        ass = a * a
        j = 1
        jj = 1
        aj = rtwopi * a
        value = rtwopi * np.arctan(a)
        dj = dhs - 1.0
        gj = hs * dhs

        while (True):

            value = value + dj * aj / float(jj)

            if (m <= j):
                return value

            j = j + 1
            jj = jj + 2
            aj = aj * ass
            dj = gj - dj
            gj = gj * hs / float(j)
#
#  t2(h, a, m)  m = 10, 20 or 30
#  z = (-1)^(i-1) * zi  ii = 2i - 1
#  vi = (-1)^(i-1) * a^(2i-1) * exp[-(a*h)^2/2] / sqrt(2*pi)
#
    elif (meth[icode - 1] == 2):

        maxii = m + m + 1
        ii = 1
        value = 0.0
        hs = h * h
        ass = - a * a
        vi = rrtpi * a * np.exp(- 0.5 * ah * ah)
        z = znorm1(ah) / h
        y = 1.0 / hs

        while (True):

            value = value + z

            if (maxii <= ii):
                value = value * rrtpi * np.exp(- 0.5 * hs)
                return value

            z = y * (vi - ii * z)
            vi = ass * vi
            ii = ii + 2
#
#  t3(h, a, m)  m = 20
#  ii = 2i - 1
#  vi = a**(2i-1) * exp[-(a*h)**2/2] / sqrt(2*pi)
#
    elif (meth[icode - 1] == 3):

        i = 1
        ii = 1
        value = 0.0
        hs = h * h
        ass = a * a
        vi = rrtpi * a * np.exp(- 0.5 * ah * ah)
        zi = znorm1(ah) / h
        y = 1.0 / hs

        while (True):

            value = value + zi * c2[i - 1]

            if (m < i):
                value = value * rrtpi * np.exp(- 0.5 * hs)
                return value

            zi = y * (ii * zi - vi)
            vi = ass * vi
            i = i + 1
            ii = ii + 2
#
#  t4(h, a, m)  m = 4, 7, 8 or 20  ii = 2i + 1
#  ai = a * exp[-h*h*(1+a*a)/2] * (-a*a)^i / (2*pi)
#
    elif (meth[icode - 1] == 4):

        maxii = m + m + 1
        ii = 1
        hs = h * h
        ass = - a * a
        value = 0.0
        ai = rtwopi * a * np.exp(- 0.5 * hs * (1.0 - ass))
        yi = 1.0

        while (True):

            value = value + ai * yi

            if (maxii <= ii):
                return value

            ii = ii + 2
            yi = (1.0 - hs * yi) / float(ii)
            ai = ai * ass
#
#  t5(h, a, m)  m = 13
#  2m - point gaussian quadrature
#
    elif (meth[icode - 1] == 5):

        value = 0.0
        ass = a * a
        hs = - 0.5 * h * h
        for i in range(0, m):
            r = 1.0 + ass * pts[i]
            value = value + wts[i] * np.exp(hs * r) / r
        value = a * value
#
#  t6(h, a)  approximation for a near 1, (a<=1)
#
    elif (meth[icode - 1] == 6):

        normh = znorm2(h)
        value = 0.5 * normh * (1.0 - normh)
        y = 1.0 - a
        r = np.arctan(y / (1.0 + a))

        if (r != 0.0):
            value = value - rtwopi * r * np.exp(- 0.5 * y * h * h / r)

    return value


def znorm1(z):

    # *****************************************************************************80
    #
    # ZNORM1 evaluates the normal CDF from 0 to Z.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real Z, the upper limit.
    #
    #    Output, real VALUE, the probability that a standard
    #    normal variable will lie between -oo and Z.
    #
    import numpy as np
    from scipy import special

    value = 0.5 * special.erf(z / np.sqrt(2.0))

    return value


def znorm1_test():

    # *****************************************************************************80
    #
    # ZNORM1_TEST demonstrates the use of ZNORM1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('ZNORM1_TEST:')
    print('  ZNORM1 computes the normal CDF starting at 0.')
    print('  Compare to tabulated values.')
    print('')
    print('          X           P                         P                       DIFF')
    print('                     (Tabulated)               (ZNORM1)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx1 = normal_01_cdf_values(n_data)

        if (n_data == 0):
            break

        fx1 = fx1 - 0.5

        fx2 = znorm1(x)

        print('  %12.8f  %24.16e  %24.16e  %10.4e' %
              (x, fx1, fx2, abs(fx1 - fx2)))

    return


def znorm2(z):

    # *****************************************************************************80
    #
    # ZNORM2 evaluates the normal CDF from Z to +oo.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real Z, the lower limit.
    #
    #    Output, real VALUE, the probability that a standard
    #    normal variable will lie between Z and +oo.
    #
    import numpy as np
    from scipy import special

    value = 0.5 * special.erfc(z / np.sqrt(2.0))

    return value


def znorm2_test():

    # *****************************************************************************80
    #
    # ZNORM2_TEST demonstrates the use of ZNORM2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('ZNORM2_TEST:')
    print('  ZNORM2 computes the normal CDF starting at 0.')
    print('  Compare to tabulated values.')
    print('')
    print('          X           P                         P                       DIFF')
    print('                     (Tabulated)               (ZNORM2)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx1 = normal_01_cdf_values(n_data)

        if (n_data == 0):
            break

        fx1 = 1.0 - fx1

        fx2 = znorm2(x)

        print('  %12.8f  %24.16e  %24.16e  %10.4e' %
              (x, fx1, fx2, abs(fx1 - fx2)))

    return


def owen_test():

    # *****************************************************************************80
    #
    # owen_TEST tests the owen library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 July 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('owen_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the owen library.')

    bivnor_test()
    t_test()
    znorm1_test()
    znorm2_test()

    print('')
    print('owen_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    owen_test()
    timestamp()
