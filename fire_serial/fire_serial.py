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

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from i4lib.i4_uniform_ab import i4_uniform_ab
from r8lib.r8vec_print import r8vec_print, r8vec_print_some, r8vec_transpose_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose import r8vec_transpose_print
from r8lib.r8mat_transpose import r8mat_transpose_print, r8mat_transpose_print_some
from r8lib.r8 import r8_uniform_01

UNBURNT = 0
SMOLDERING = 1
BURNING = 2
BURNT = 3


def fire_serial(forest_size, prob_spread):

    # *****************************************************************************80
    #
    # FIRE_SERIAL simulates a fire in a rectangular forest of trees.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the number of trees in a horizontal
    #    or vertical line.
    #
    #    Input, real PROB_SPREAD, the probability that a burning tree will
    #    ignite a neighboring tree.
    #
    import platform

    print('')
    print('FIRE_SERIAL')
    print('  Python version: %s' % (platform.python_version()))
    print('  A probabilistic simulation of a forest fire.')
    print('  The forest is a square grid with %d trees on a side.' % (forest_size))
    print('  The probability of tree-to-tree spread is %g' % (prob_spread))
#
#  Initialize the random number generator.
#
    seed = 123456789
    print('  The random number generator is seeded by %d' % (seed))
#
#  Initialize the values in the forest.
#
    forest = forest_initialize(forest_size)
#
#  Choose a tree at random where the fire will start.
#
    i_ignite, seed = i4_uniform_ab(0, forest_size - 1, seed)
    j_ignite, seed = i4_uniform_ab(0, forest_size - 1, seed)
    tree_ignite(forest_size, forest, i_ignite, j_ignite)

    print('')
    print('  Fire starts at tree[%d,%d]' % (i_ignite, j_ignite))
#
#  Let time run until nothing is burning any more.
#
    while (forest_is_burning(forest_size, forest)):
        seed = forest_burns(forest_size, forest, seed, prob_spread)
#
#  Display the final forest state.
#
    forest_print(forest_size, forest, i_ignite, j_ignite)
#
#  Report the percentage of forest burned.
#
    percent = get_percent_burned(forest_size, forest)

    print('')
    print('  Percentage of forest burned = %g' % (percent))
#
#  Terminate.
#
    print('')
    print('FIRE_SERIAL:')
    print('  Normal end of execution.')
    return


def fire_spreads(seed, prob_spread):

    # *****************************************************************************80
    #
    # FIRE_SPREADS determines whether the fire spreads.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random
    #    number generator.
    #
    #    Input, real PROB_SPREAD, the probability of spreading.
    #
    #    Output, logical FIRE_SPREADS, is TRUE if the fire spreads.
    #
    #    Output, integer SEED, a seed for the random
    #    number generator.
    #
    u, seed = r8_uniform_01(seed)

    if (u < prob_spread):
        value = True
    else:
        value = False

    return value, seed


def forest_burns(forest_size, forest, seed, prob_spread):

    # *****************************************************************************80
    #
    # FOREST_BURNS models a single time step of the burning forest.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #    Input/output, integer FOREST(FOREST_SIZE,FOREST_SIZE), an
    #    array with an entry for each tree in the forest.
    #
    #    Input, integer SEED, a seed for the random
    #    number generator.
    #
    #    Input, real PROB_SPREAD, the probability that the fire will
    #    spread from a burning tree to an unburnt one.
    #
    #    Output, integer SEED, a seed for the random
    #    number generator.
    #

    #
    #  Burning trees burn down;
    #  Smoldering trees ignite;
    #
    for j in range(0, forest_size):
        for i in range(0, forest_size):
            if (forest[i, j] == BURNING):
                forest[i, j] = BURNT
            elif (forest[i, j] == SMOLDERING):
                forest[i, j] = BURNING
#
#  Unburnt trees might catch fire.
#
    for j in range(0, forest_size):
        for i in range(0, forest_size):

            if (forest[i, j] == BURNING):
                #
                #  North.
                #
                if (0 < i):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i - 1, j] == UNBURNT):
                        forest[i - 1, j] = SMOLDERING
#
#  South.
#
                if (i < forest_size - 1):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i + 1, j] == UNBURNT):
                        forest[i + 1, j] = SMOLDERING
#
#  West.
#
                if (0 < j):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i, j - 1] == UNBURNT):
                        forest[i, j - 1] = SMOLDERING
#
#  East.
#
                if (j < forest_size - 1):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i, j + 1] == UNBURNT):
                        forest[i, j + 1] = SMOLDERING

    return seed


def forest_initialize(forest_size):

    # *****************************************************************************80
    #
    # FOREST_INITIALIZE initializes the forest values.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #    Output, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    import numpy as np

    forest = UNBURNT * np.zeros([forest_size, forest_size])

    return forest


def forest_is_burning(forest_size, forest):

    # *****************************************************************************80
    #
    # FOREST_IS_BURNING reports whether any trees in the forest are burning.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #    Input, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Output, logical FOREST_IS_BURNING, is TRUE if any tree in the forest
    #    is in the SMOLDERING or BURNING state.
    #
    value = False

    for j in range(0, forest_size):
        for i in range(0, forest_size):
            if (forest[i, j] == SMOLDERING or forest[i, j] == BURNING):
                value = True
                return value

    return value


def forest_print(forest_size, forest, i_ignite, j_ignite):

    # *****************************************************************************80
    #
    # FOREST_PRINT prints the state of the trees in the forest.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ( kind = 4 ) FOREST_SIZE, the linear dimension of the forest.
    #
    #    Input, integer ( kind = 4 ) FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Input, integer ( kind = 4 ) I_IGNITE, J_IGNITE, the location of the start
    #    of the fire.
    #
    import sys as sys

    print('')
    print('  Map of fire damage.')
    print('  Fire started at "*".')
    print('  Burned trees are indicated by "."')
    print('  Unburned trees are indicated by "X".')
    print('')

    for i in range(0, forest_size):
        sys.stdout.write('  ')
        for j in range(0, forest_size):
            if (i == i_ignite and j == j_ignite):
                sys.stdout.write('*')
            elif (forest[i, j] == BURNT):
                sys.stdout.write('.')
            else:
                sys.stdout.write('X')
        print('')

    return


def get_percent_burned(forest_size, forest):

    # *****************************************************************************80
    #
    # GET_PERCENT_BURNED computes the percentage of the forest that burned.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #   Input, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Output, real PERCENT, the percentage of the forest
    #    that burned.
    #
    total = 0
    for j in range(0, forest_size):
        for i in range(0, forest_size):
            if (forest[i, j] == BURNT):
                total = total + 1

    percent = float(total) / float(forest_size) / float(forest_size)

    return percent


def tree_ignite(forest_size, forest, i_ignite, j_ignite):

    # *****************************************************************************80
    #
    # TREE_IGNITE sets a given tree to the SMOLDERING state.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of
    #    the forest.
    #
    #    Input, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Input, integer I_IGNITE, J_IGNITE, the coordinates of the
    #    tree which is to be set to SMOLDERING.
    #
    forest[i_ignite, j_ignite] = SMOLDERING


if (__name__ == '__main__'):
    timestamp()
    forest_size = 20
    prob_spread = 0.5
    fire_serial(forest_size, prob_spread)
    timestamp()
