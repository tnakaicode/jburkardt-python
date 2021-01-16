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

from rnglib.cglib import cg_set, cgn_get
from rnglib.lglib import lg_get, lg_set
from rnglib.iglib import ig_get
from rnglib.initialize import initialize, initialized_get
from rnglib.multmod import multmod


def init_generator(t):

    # *****************************************************************************80
    #
    # INIT_GENERATOR sets the current generator to initial, last or new seed.
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
    #    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Pierre LEcuyer, Serge Cote,
    #    Implementing a Random Number Package with Splitting Facilities,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 1, March 1991, pages 98-111.
    #
    #  Parameters:
    #
    #    Input, integer T, the seed type:
    #    0, use the seed chosen at initialization time.
    #    1, use the last seed.
    #    2, use a new seed set 2^30 values away.
    #

    a1_w = 1033780774
    a2_w = 1494757890
    m1 = 2147483563
    m2 = 2147483399
#
#  Check whether the package must be initialized.
#
    if (not initialized_get()):
        print('')
        print('INIT_GENERATOR - Note:')
        print('  Initializing RNGLIB package.')
        initialize()
#
#  Get the current generator index.
#
    g = cgn_get()
#
#  0: Restore the initial seed.
#
    if (t == 0):

        ig1, ig2 = ig_get(g)
        lg1 = ig1
        lg2 = ig2
        lg_set(g, lg1, lg2)
#
#  1: Restore the last seed.
#
    elif (t == 1):

        lg1, lg2 = lg_get(g)
#
#  Advance to a new seed.
#
    elif (t == 2):

        lg1, lg2 = lg_get(g)
        lg1 = multmod(a1_w, lg1, m1)
        lg2 = multmod(a2_w, lg2, m2)
        lg_set(g, lg1, lg2)

    else:

        print('')
        print('INIT_GENERATOR - Fatal error!')
        print('  Input parameter T out of bounds.')
        exit('INIT_GENERATOR - Fatal error!')
#
#  Store the new seed.
#
    cg1 = lg1
    cg2 = lg2
    cg_set(g, cg1, cg2)

    return
