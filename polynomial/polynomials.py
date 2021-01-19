#! /usr/bin/env python3
#
def polynomials():

    # *****************************************************************************80
    #
    # POLYNOMIALS tests the POLYNOMIALS library.
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
    from butcher import butcher_test
    from camel import camel_test
    from camera import camera_test
    from caprasse import caprasse_test
    from cyclic5 import cyclic5_test
    from cyclic7 import cyclic7_test
    from cyclic8 import cyclic8_test
    from goldstein_price import goldstein_price_test
    from hairer import hairer_test
    from heart import heart_test
    from himmelblau import himmelblau_test
    from hunecke import hunecke_test
    from kearfott import kearfott_test
    from lv3 import lv3_test
    from lv4 import lv4_test
    from magnetism6 import magnetism6_test
    from magnetism7 import magnetism7_test
    from quadratic import quadratic_test
    from rd import rd_test
    from reimer5 import reimer5_test
    from reimer6 import reimer6_test
    from rosenbrock import rosenbrock_test
    from schwefel import schwefel_test
    from smith1 import smith1_test
    from smith2 import smith2_test
    from virasoro import virasoro_test
    from wright import wright_test
    from zakharov import zakharov_test

    print('')
    print('POLYNOMIALS')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the POLYNOMIALS library.')

    butcher_test()
    camel_test()
    camera_test()
    caprasse_test()
    cyclic5_test()
    cyclic7_test()
    cyclic8_test()
    goldstein_price_test()
    hairer_test()
    heart_test()
    himmelblau_test()
    hunecke_test()
    kearfott_test()
    lv3_test()
    lv4_test()
    magnetism6_test()
    magnetism7_test()
    quadratic_test()
    rd_test()
    reimer5_test()
    reimer6_test()
    rosenbrock_test()
    schwefel_test()
    smith1_test()
    smith2_test()
    virasoro_test()
    wright_test()
    zakharov_test()
#
#  Terminate.
#
    print('')
    print('POLYNOMIALS')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    polynomials()
    timestamp()
