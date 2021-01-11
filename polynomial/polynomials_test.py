#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from r8lib.r8mat_print import r8mat_print
from r8lib.r8mat_print_some import r8mat_print_some
from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec
from r8lib.r8vec2_print import r8vec2_print
from polynomial.butcher import butcher_test
from polynomial.camel import camel_test
from polynomial.camera import camera_test
from polynomial.caprasse import caprasse_test
from polynomial.cyclic5 import cyclic5_test
from polynomial.cyclic7 import cyclic7_test
from polynomial.cyclic8 import cyclic8_test
from polynomial.goldstein_price import goldstein_price_test
from polynomial.hairer import hairer_test
from polynomial.heart import heart_test
from polynomial.himmelblau import himmelblau_test
from polynomial.hunecke import hunecke_test
from polynomial.kearfott import kearfott_test
from polynomial.lv3 import lv3_test
from polynomial.lv4 import lv4_test
from polynomial.magnetism6 import magnetism6_test
from polynomial.magnetism7 import magnetism7_test
from polynomial.quadratic import quadratic_test
from polynomial.rd import rd_test
from polynomial.reimer5 import reimer5_test
from polynomial.reimer6 import reimer6_test
from polynomial.rosenbrock import rosenbrock_test
from polynomial.schwefel import schwefel_test
from polynomial.smith1 import smith1_test
from polynomial.smith2 import smith2_test
from polynomial.virasoro import virasoro_test
from polynomial.wright import wright_test
from polynomial.zakharov import zakharov_test


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

    print('')
    print('POLYNOMIALS')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polynomials()
    timestamp()
