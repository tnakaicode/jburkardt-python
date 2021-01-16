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

from rnglib.cglib import cg_set, cgn_set, cgn_get
from rnglib.iglib import ig_set, ig_get
from rnglib.lglib import lg_set, lg_get
from rnglib.multmod import multmod
from rnglib.antithetic import antithetic_set


def initialize():

    # *****************************************************************************80
    #
    # INITIALIZE initializes the random number generator library.
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
    #    None
    #

    g_max = 32

    #
    #  Remember that we have called INITIALIZE().
    #
    initialized_set()

    #
    #  Initialize all generators to have FALSE antithetic value.
    #
    value = False
    for g in range(1, g_max + 1):
        cgn_set(g)
        antithetic_set(value)

    #
    #  Set the initial seeds.
    #
    ig1 = 1234567890
    ig2 = 123456789
    set_initial_seed(ig1, ig2)

    #
    #  Initialize the current generator index to 1.
    #
    g = 1
    cgn_set(g)

    print('')
    print('INITIALIZE:')
    print('  The RNGLIB package has been initialized.')


def initialized_get():

    # *****************************************************************************80
    #
    # INITIALIZED_GET gets the INITIALIZED value.
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
    #    Output, bool INITIALIZED, is true if the package has been initialized.
    #

    i = -1
    initialized = []
    initialized = initialized_memory(i, initialized)

    return initialized


def initialized_memory(i, initialized):

    # *****************************************************************************80
    #
    # INITIALIZED_MEMORY stores the INITIALIZED value.
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
    #    Input/output, bool INITIALIZED.  For I = -1, an output quantity,
    #    if I = +1, an input quantity, and if I = 0 the value is ignored.
    #
    if (i < 0):
        initialized = initialized_memory.initialized_save
    elif (i == 0):
        initialized_memory.initialized_save = False
        initialized = False
    elif (0 < i):
        initialized_memory.initialized_save = initialized

    return initialized


def initialized_set():

    # *****************************************************************************80
    #
    # INITIALIZED_SET sets the INITIALIZED value to true.
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
    #    None.
    #

    i = +1
    initialized = True
    initialized = initialized_memory(i, initialized)


def set_initial_seed(ig1, ig2):

    # *****************************************************************************80
    #
    # SET_INITIAL_SEED resets the initial seed and state for all generators.
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
    #    Input, integer IG1, IG2, the initial seed values
    #    for the first generator.
    #    1 <= IG1 < 2147483563
    #    1 <= IG2 < 2147483399
    #

    a1_vw = 2082007225
    a2_vw = 784306273
    g_max = 32
    m1 = 2147483563
    m2 = 2147483399

    if (ig1 < 1 or m1 <= ig1):
        print('')
        print('SET_INITIAL_SEED - Fatal error!')
        print('  Input parameter IG1 out of bounds.')
        exit('SET_INITIAL_SEED - Fatal error!')

    if (ig2 < 1 or m2 <= ig2):
        print('')
        print('SET_INITIAL_SEED - Fatal error!')
        print('  Input parameter IG2 out of bounds.')
        exit('SET_INITIAL_SEED - Fatal error!')

    #
    #  Because INITIALIZE calls SET_INITIAL_SEED, it's not easy to correct
    #  the error that arises if SET_INITIAL_SEED is called before INITIALIZE.
    #  So don't bother trying.
    #
    if (not initialized_get()):
        print('')
        print('SET_INITIAL_SEED - Fatal error!')
        print('  The RNGLIB package has not been initialized.')
        exit('SET_INITIAL_SEED - Fatal error!')

    #
    #  Set the initial seed, then initialize the first generator.
    #
    g = 1
    cgn_set(g)
    ig_set(g, ig1, ig2)

    t = 0
    init_generator(t)

    #
    #  Now do similar operations for the other generators.
    #
    for g in range(2, g_max + 1):
        cgn_set(g)
        ig1 = multmod(a1_vw, ig1, m1)
        ig2 = multmod(a2_vw, ig2, m2)
        ig_set(g, ig1, ig2)
        init_generator(t)

    #
    #  Now choose the first generator.
    #
    g = 1
    cgn_set(g)


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


initialized_memory.initialized_save = False
