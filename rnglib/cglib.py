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


def cg_get(g):

    # *****************************************************************************80
    #
    # CG_GET queries the CG values for a given generator.
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
    #    Input, integer G, the index of the generator.
    #    1 <= G <= 32.
    #
    #    Output, integer CG1, CG2, the CG values for generator G.
    #

    i = -1
    cg1 = []
    cg2 = []
    cg1, cg2 = cg_memory(i, g, cg1, cg2)

    return cg1, cg2


def cg_set(g, cg1, cg2):

    # *****************************************************************************80
    #
    # CG_SET sets the CG values for a given generator.
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
    #    Input, integer G, the index of the generator.
    #    1 <= G <= 32.
    #
    #    Input, integer CG1, CG2, the CG values for generator G.
    #

    i = +1
    cg1, cg2 = cg_memory(i, g, cg1, cg2)

    return


def cg_memory(i, g, cg1, cg2):

    # *****************************************************************************80
    #
    # CG_MEMORY stores the CG values for all generators.
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
    #    Input, integer G, for I = -1 or +1, the index of
    #    the generator, with 1 <= G <= 32.
    #
    #    Input/output, integer CG1, CG2.  For I = -1,
    #    these are output, for I = +1, these are input, for I = 0,
    #    these arguments are ignored.  When used, the arguments are
    #    old or new values of the CG parameter for generator G.
    #

    g_max = 32

    if (g < 1 or g_max < g):
        print('')
        print('CG_MEMORY - Fatal error!')
        print('  Input generator index G is out of bounds.')
        exit('CG_MEMORY - Fatal error!')

    if (i < 0):
        cg1 = cg_memory.cg1_save[g - 1]
        cg2 = cg_memory.cg2_save[g - 1]
    elif (i == 0):
        for i in range(1, g_max + 1):
            cg_memory.cg1_save[i - 1] = 0
            cg_memory.cg2_save[i - 1] = 0
        cg1 = 0
        cg2 = 0
    elif (0 < i):
        cg_memory.cg1_save[g - 1] = cg1
        cg_memory.cg2_save[g - 1] = cg2

    return cg1, cg2


def cgn_get():

    # *****************************************************************************80
    #
    # CGN_GET gets the current generator index.
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
    #    Output, integer G, the current generator index.
    #

    i = -1
    g = []
    g = cgn_memory(i, g)

    return g


def cgn_set(g):

    # *****************************************************************************80
    #
    # CGN_SET sets the current generator index.
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
    #    Input, integer G, the current generator index.
    #    1 <= G <= 32.
    #

    i = +1
    g = cgn_memory(i, g)


def cgn_memory(i, g):

    # *****************************************************************************80
    #
    # CGN_MEMORY stores the current generator index.
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
    #    -1, get the value.
    #    0, initialize the value.
    #    1, set the value.
    #
    #    Input/output, integer G.  For I = -1 or 0, an output quantity.
    #    For I = +1, an input quantity.
    #

    g_max = 32

    if (i < 0):
        g = cgn_memory.g_save

    elif (i == 0):
        cgn_memory.g_save = 1
        g = cgn_memory.g_save

    elif (0 < i):

        if (g < 1 or g_max < g):
            print('')
            print('CGN_MEMORY - Fatal error!')
            print('  Input generator index G is out of bounds.')
            exit('CGN_MEMORY - Fatal error!')

        cgn_memory.g_save = g

    return g


cg_memory.cg1_save = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cg_memory.cg2_save = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
