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


def polyomino_enumerate_chiral(n_data):

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_CHIRAL counts chiral polyominoes (allowing holes).
    #
    #  Discussion:
    #
    #    Polyominoes are connected planar shapes formed by adjoining unit squares.
    #
    #    The number of unit squares in a polyomino is its order.
    #
    #    If we ignore reflections and rotations when comparing polyominoes,
    #    then we are considering the class of "chiral" polyominoes.  In that case,
    #    for instance, there are just 18 chiral polyominoes of order 5.
    #
    #    As the order increases, the number of polyominoes grows very rapidly.
    #    The list offered here goes no further than order 28, but the later
    #    numbers in the list are too large to represent as 32 byte integers.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Solomon Golomb,
    #    Polyominoes: Puzzles, Patterns, Problems, and Packings,
    #    Princeton University Press, 1996,
    #    ISBN: 9780691024448
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, integer ORDER, the order of a polyomino.
    #
    #    Output, integer NUMBER, the number of chiral polyominos of this order.
    #
    import numpy as np

    n_max = 31

    order_vec = np.array([
        0,
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30])

    number_vec = np.array([
        1,
        1, 1, 2, 7, 18,
        60, 196, 704, 2500, 9189,
        33896, 126759, 476270, 1802312, 6849777,
        26152418, 100203194, 385221143, 1485200848, 5741256764,
        22245940545, 86383382827, 336093325058, 1309998125640, 5114451441106,
        19998172734786, 78306011677182, 307022182222506, 1205243866707468, 4736694001644862])

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        order = 0
        number = 0
    else:
        order = order_vec[n_data]
        number = number_vec[n_data]
        n_data = n_data + 1

    return n_data, order, number


def polyomino_enumerate_chiral_test():

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_CHIRAL_TEST tests POLYOMINO_ENUMERATE_CHIRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('POLYOMINO_ENUMERATE_CHIRAL_TEST:')
    print('  POLYOMINO_ENUMERATE_CHIRAL returns counts of')
    print('  the number of chiral polyominoes.')
    print('')
    print('     Order     Number')
    print('')

    n_data = 0

    while (True):

        n_data, order, number = polyomino_enumerate_chiral(n_data)

        if (n_data == 0):
            break

        print('  %d  %d' % (order, number))
#
#  Terminate.
#
    print('')
    print('POLYOMINO_ENUMERATE_CHIRAL_TEST:')
    print('  Normal end of execution.')
    return


def polyomino_enumerate_fixed(n_data):

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_FIXED counts fixed polyominoes (allowing holes).
    #
    #  Discussion:
    #
    #    Polyominoes are connected planar shapes formed by adjoining unit squares.
    #
    #    The number of unit squares in a polyomino is its order.
    #
    #    If we do not ignore reflections and rotations when comparing polyominoes,
    #    then we are considering the class of "fixed" polyominoes.  In that case,
    #    for instance, there are 65 fixed polyominoes of order 5.
    #
    #    As the order increases, the number of polyominoes grows very rapidly.
    #    The list offered here goes no further than order 28, but the later
    #    numbers in the list are too large to represent as 32 byte integers.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Solomon Golomb,
    #    Polyominoes: Puzzles, Patterns, Problems, and Packings,
    #    Princeton University Press, 1996,
    #    ISBN: 9780691024448
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, integer ORDER, the order of a polyomino.
    #
    #    Output, integer NUMBER, the number of fixed polyominos of this order.
    #
    import numpy as np

    n_max = 29

    order_vec = np.array([
        0,
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28])

    number_vec = np.array([
        1,
        1, 2, 6, 19, 63,
        216, 760, 2725, 9910, 36446,
        135268, 505861, 1903890, 7204874, 27394666,
        104592937, 400795844, 1540820542, 5940738676, 22964779660,
        88983512783, 345532572678, 1344372335524, 5239988770268, 20457802016011,
        79992676367108, 313224032098244, 1228088671826973])

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        order = 0
        number = 0
    else:
        order = order_vec[n_data]
        number = number_vec[n_data]
        n_data = n_data + 1

    return n_data, order, number


def polyomino_enumerate_fixed_test():

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_FIXED_TEST tests POLYOMINO_ENUMERATE_FIXED.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('POLYOMINO_ENUMERATEv_FIXED_TEST:')
    print('  POLYOMINO_ENUMERATE_FIXED returns counts of')
    print('  the number of fixed polyominoes.')
    print('')
    print('     Order     Number')
    print('')

    n_data = 0

    while (True):

        n_data, order, number = polyomino_enumerate_fixed(n_data)

        if (n_data == 0):
            break

        print('  %d  %d' % (order, number))
#
#  Terminate.
#
    print('')
    print('POLYOMINO_ENUMERATE_FIXED_TEST:')
    print('  Normal end of execution.')
    return


def polyomino_enumerate_free(n_data):

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_FREE counts free polyominoes (allowing holes).
    #
    #  Discussion:
    #
    #    Polyominoes are connected planar shapes formed by adjoining unit squares.
    #
    #    The number of unit squares in a polyomino is its order.
    #
    #    If we ignore reflections and rotations when comparing polyominoes,
    #    then we are considering the class of "free" polyominoes.  In that case,
    #    for instance, there are just 12 free polyominoes of order 5, the
    #    so called "pentominoes".
    #
    #    As the order increases, the number of polyominoes grows very rapidly.
    #    The list offered here goes no further than order 28, but the later
    #    numbers in the list are too large to represent as 32 byte integers.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Solomon Golomb,
    #    Polyominoes: Puzzles, Patterns, Problems, and Packings,
    #    Princeton University Press, 1996,
    #    ISBN: 9780691024448
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, integer ORDER, the order of a polyomino.
    #
    #    Output, integer NUMBER, the number of free polyominos of this order.
    #
    import numpy as np

    n_max = 29

    order_vec = np.array([
        0,
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28])

    number_vec = np.array([
        1,
        1, 1, 2, 5, 12,
        35, 108, 369, 1285, 4655,
        17073, 63600, 238591, 901971, 3426576,
        13079255, 50107909, 192622052, 742624232, 2870671950,
        11123060678, 43191857688, 168047007728, 654999700403, 2557227044764,
        9999088822075, 39153010938487, 153511100594603])

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        order = 0
        number = 0
    else:
        order = order_vec[n_data]
        number = number_vec[n_data]
        n_data = n_data + 1

    return n_data, order, number


def polyomino_enumerate_free_test():

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_FREE_TEST tests POLYOMINO_ENUMERATE_FREE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('POLYOMINO_ENUMERATE_FREE_TEST:')
    print('  POLYOMINO_ENUMERATE_FREE returns counts of')
    print('  the number of free polyominoes.')
    print('')
    print('     Order     Number')
    print('')

    n_data = 0

    while (True):

        n_data, order, number = polyomino_enumerate_free(n_data)

        if (n_data == 0):
            break

        print('  %d  %d' % (order, number))
#
#  Terminate.
#
    print('')
    print('POLYOMINO_ENUMERATE_FREE_TEST:')
    print('  Normal end of execution.')
    return


def polyomino_enumerate_test():

    # *****************************************************************************80
    #
    # POLYOMINO_ENUMERATE_TEST tests the POLYOMINO_ENUMERATE library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('POLYOMINO_ENUMERATE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYOMINO_ENUMERATE counts various kinds of polyominoes.')

    polyomino_enumerate_chiral_test()
    polyomino_enumerate_fixed_test()
    polyomino_enumerate_free_test()

    print('')
    print('POLYOMINO_ENUMERATE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polyomino_enumerate_test()
    timestamp()
