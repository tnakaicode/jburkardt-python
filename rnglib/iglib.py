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


def ig_get(g):

    # *****************************************************************************80
    #
    # IG_GET queries the IG values for a given generator.
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
    #    Output, integer IG1, IG2, the IG values for generator G.
    #

    i = -1
    ig1 = []
    ig2 = []
    ig1, ig2 = ig_memory(i, g, ig1, ig2)

    return ig1, ig2


def ig_set(g, ig1, ig2):

    # *****************************************************************************80
    #
    # IG_SET sets the IG values for a given generator.
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
    #    Input, integer IG1, IG2, the IG values for generator G.
    #

    i = +1
    ig1, ig2 = ig_memory(i, g, ig1, ig2)


def ig_memory(i, g, ig1, ig2):

    # *****************************************************************************80
    #
    # IG_MEMORY stores the IG values for all generators.
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
    #    Input/output, integer IG1, IG2.  For I = -1,
    #    these are output, for I = +1, these are input, for I = 0,
    #    these arguments are ignored.  When used, the arguments are
    #    old or new values of the IG parameter for generator G.
    #

    g_max = 32

    if (g < 1 or g_max < g):
        print('')
        print('IG_MEMORY - Fatal error!')
        print('  Input generator index G is out of bounds.')
        exit('IG_MEMORY - Fatal error!')

    if (i < 0):
        ig1 = ig_memory.ig1_save[g - 1]
        ig2 = ig_memory.ig2_save[g - 1]
    elif (i == 0):
        for j in range(1, g_max + 1):
            ig_memory.ig1_save[j - 1] = 0
            ig_memory.ig2_save[j - 1] = 0
        ig1 = 0
        ig2 = 0
    elif (0 < i):
        ig_memory.ig1_save[g - 1] = ig1
        ig_memory.ig2_save[g - 1] = ig2

    return ig1, ig2


ig_memory.ig1_save = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ig_memory.ig2_save = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
