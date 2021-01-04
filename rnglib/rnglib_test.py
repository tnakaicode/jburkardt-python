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
from rnglib.initialize import initialize
from rnglib.rnglib_test03 import rnglib_test03
from rnglib.rnglib_test04 import rnglib_test04


def rnglib_test():

    # *****************************************************************************80
    #
    # RNGLIB_TEST tests the RNGLIB library.
    #
    #  Discussion:
    #
    #    RNGLIB_TEST calls sample problems for the RNGLIB library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 May 2013
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RNGLIB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the RNGLIB library.')

    #
    #  Initialize RNGLIB.
    #
    initialize()

    rnglib_test03()
    rnglib_test04()

    print('')
    print('RNGLIB_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    rnglib_test()
    timestamp()
