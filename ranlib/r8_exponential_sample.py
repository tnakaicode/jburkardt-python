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

from rnglib.r8_uni_01 import r8_uni_01


def r8_exponential_sample(lam):

    # *****************************************************************************80
    #
    # R8_EXPONENTIAL_SAMPLE samples the exponential PDF.
    #
    #  Discussion:
    #
    #    Note that the parameter LAM is a multiplier.  In some formulations,
    #    it is used as a divisor instead.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real LAM, the parameter of the PDF.
    #
    #    Output, real VALUE, a sample of the PDF.
    #

    r = r8_uni_01()

    value = - np.log(r) * lam

    return value


def r8_exponential_sample_test():

    # *****************************************************************************80
    #
    # R8_EXPONENTIAL_TEST tests R8_EXPONENTIAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    test_num = 20

    print('')
    print('R8_EXPONENTIAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_EXPONENTIAL samples the exponential distribution.')
    print('')

    lam = 0.5

    for test in range(0, test_num):

        x = r8_exponential_sample(lam)
        print('  %f' % (x))
#
#  Terminate.
#
    print('')
    print('R8_EXPONENTIAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8_exponential_sample_test()
    timestamp()
