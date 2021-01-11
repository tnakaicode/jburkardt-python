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

from i4lib.i4_choose import i4_choose
from i4lib.i4_fall import i4_fall
from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_concatenate import i4vec_concatenate
from i4lib.i4vec_permute import i4vec_permute
from i4lib.i4vec_print import i4vec_print
from i4lib.i4vec_sort_heap_index_a import i4vec_sort_heap_index_a
from i4lib.i4vec_sum import i4vec_sum
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from r8lib.r8vec_concatenate import r8vec_concatenate
from r8lib.r8vec_permute import r8vec_permute
from r8lib.r8vec_print import r8vec_print


def mono_upto_enum(m, n):

    # *****************************************************************************80
    #
    # MONO_UPTO_ENUM enumerates monomials in M dimensions of degree up to N.
    #
    #  Discussion:
    #
    #    For M = 2, we have the following values:
    #
    #    N  VALUE
    #
    #    0    1
    #    1    3
    #    2    6
    #    3   10
    #    4   15
    #    5   21
    #
    #    In particular, VALUE(2,3) = 10 because we have the 10 monomials:
    #
    #      1, x, y, x^2, xy, y^2, x^3, x^2y, xy^2, y^3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int M, the spatial dimension.
    #
    #    Input, int N, the maximum degree.
    #
    #    Output, int VALUE, the number of monomials in
    #    M variables, of total degree N or less.
    #

    value = i4_choose(n + m, n)

    return value


def mono_upto_enum_test():

    # *****************************************************************************80
    #
    # MONO_UPTO_ENUM_TEST tests MONO_UPTO_ENUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('MONO_UPTO_ENUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_UPTO_ENUM can enumerate the number of monomials')
    print('  in M variables, of total degree between 0 and N.')

    print('')
    print('    N:'),
    for n in range(0, 9):
        print('  %4d' % (n)),
    print('')
    print('   M +---------------------------------------------------------------')
    for m in range(1, 9):
        print('  %2d |' % (m)),
        for n in range(0, 9):
            v = mono_upto_enum(m, n)
            print(' %5d' % (v)),
        print('')
    print('')
    print('MONO_UPTO_ENUM_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    mono_upto_enum_test()
    timestamp()
