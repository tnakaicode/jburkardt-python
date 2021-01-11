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

from exactness.chebyshev1_exactness import chebyshev1_exactness_test
from exactness.chebyshev1_integral import chebyshev1_integral_test
from exactness.chebyshev2_exactness import chebyshev2_exactness_test
from exactness.chebyshev2_integral import chebyshev2_integral_test
from exactness.chebyshev3_exactness import chebyshev3_exactness_test
from exactness.clenshaw_curtis_exactness import clenshaw_curtis_exactness_test
from exactness.fejer1_exactness import fejer1_exactness_test
from exactness.fejer2_exactness import fejer2_exactness_test
from exactness.gegenbauer_exactness import gegenbauer_exactness_test
from exactness.gegenbauer_integral import gegenbauer_integral_test
from exactness.hermite_1_exactness import hermite_1_exactness_test
from exactness.hermite_exactness import hermite_exactness_test
from exactness.hermite_integral import hermite_integral_test
from exactness.laguerre_1_exactness import laguerre_1_exactness_test
from exactness.laguerre_exactness import laguerre_exactness_test
from exactness.laguerre_integral import laguerre_integral_test
from exactness.legendre_exactness import legendre_exactness_test
from exactness.legendre_integral import legendre_integral_test


def exactness_test():

    # *****************************************************************************80
    #
    # EXACTNESS_TEST tests EXACTNESS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('EXACTNESS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the EXACTNESS library.')

    chebyshev1_exactness_test()
    chebyshev1_integral_test()
    chebyshev2_exactness_test()
    chebyshev2_integral_test()
    chebyshev3_exactness_test()
    clenshaw_curtis_exactness_test()
    fejer1_exactness_test()
    fejer2_exactness_test()
    gegenbauer_exactness_test()
    gegenbauer_integral_test()
    hermite_1_exactness_test()
    hermite_exactness_test()
    hermite_integral_test()
    laguerre_1_exactness_test()
    laguerre_exactness_test()
    laguerre_integral_test()
    legendre_exactness_test()
    legendre_integral_test()

    print('')
    print('EXACTNESS_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    exactness_test()
    timestamp()
