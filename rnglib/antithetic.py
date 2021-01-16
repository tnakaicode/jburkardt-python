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

from rnglib.cglib import cgn_get


def antithetic_set(value):

    # *****************************************************************************80
    #
    # ANTITHETIC_SET sets the antithetic value for a given generator.
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
    #  Parameters:
    #
    #    Input, bool VALUE, is TRUE if the current generator is to be antithetic.
    #

    i = +1
    value = antithetic_memory(i, value)


def antithetic_get():

    # *****************************************************************************80
    #
    # ANTITHETIC_GET queries the antithetic value for a given generator.
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
    #  Parameters:
    #
    #    Output, bool VALUE, is TRUE if generator G is antithetic.
    #

    i = -1
    value = []
    value = antithetic_memory(i, value)

    return value


def antithetic_memory(i, value):

    # *****************************************************************************80
    #
    # ANTITHETIC_MEMORY stores the antithetic value for all generators.
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
    #  Parameters:
    #
    #    Input, integer I, the desired action.
    #    -1, get a value.
    #    0, initialize all values.
    #    1, set a value.
    #
    #    Input/output, bool VALUE.  For I = -1, VALUE is an output
    #    quantity, for I = +1, VALUE is an input quantity.
    #

    g_max = 32

    if (i < 0):
        g = cgn_get()
        value = antithetic_memory.a_save[g - 1]
    elif (i == 0):
        antithetic_memory.a_save = []
        for i in range(1, g_max + 1):
            antithetic_memory.a_save.append(False)
        value = False
    elif (0 < i):
        g = cgn_get()
        antithetic_memory.a_save[g - 1] = value

    return value


antithetic_memory.a_save = [
    False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False]
