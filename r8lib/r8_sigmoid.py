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


def r8_sigmoid(l, b, m, x):

    # *****************************************************************************80
    #
    # r8_sigmoid evaluates the sigmoid or logistic function.
    #
    #  Discussion:
    #
    #    An R8 is a double precision real value.
    #
    #    The sigmoid function is useful for classification problems in
    #    machine learning.  Its value is always between 0 and 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 October 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real l, the maximum value of the function.  This is often 1.
    #
    #    real b, the cutoff value, where the function equals l/2.
    #    This is often 0.
    #
    #    real m, the slope, which determines the steepness of the curve
    #    and the width of the uncertainty interval.  This is often 1.
    #
    #    real x, the argument.
    #
    #  Output:
    #
    #    real value, the value.
    #

    value = l / (1.0 + np.exp(- m * (x - b)))

    return value


def r8_sigmoid_test():

    # *****************************************************************************80
    #
    # r8_sigmoid_test tests r8_sigmoid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 October 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('r8_sigmoid_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  r8_sigmoid evaluates the sigmoid function of R8.')
    print('')
    print('      X         R8_SIGMOID(L,B,M,X)')
    print('')

    n = 21
    x_test = np.linspace(-10, 10, n)
    l = 1.0
    b = 0.0
    m = 1.0

    for i in range(n):
        x = x_test[i]
        value = r8_sigmoid(l, b, m, x)
        print('  %10.6g  %10.6g' % (x, value))

    print('')
    obj = plot2d(aspect="auto")
    obj.axs.plot(x_test, r8_sigmoid(l, b, m, x_test))
    obj.SavePng()

    print('')
    print('r8_sigmoid_test')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8_sigmoid_test()
    timestamp()
