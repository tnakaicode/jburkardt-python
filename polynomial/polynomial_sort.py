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
from polynomial.polynomial_print import polynomial_print
from polynomial.polynomial_compress import polynomial_compress


def polynomial_sort(o, c, e):

    # *****************************************************************************80
    #
    # POLYNOMIAL_SORT sorts the information in a polynomial.
    #
    #  Discussion:
    #
    #    The coefficients C and exponents E are rearranged so that
    #    the elements of E are in ascending order.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer O, the "order" of the polynomial.
    #
    #    Input, real C[O], the coefficients of the scaled polynomial.
    #
    #    Input, integer E[O], the indices of the exponents of
    #    the scaled polynomial.
    #
    #    Output, real C[O], the coefficients of the sorted polynomial.
    #
    #    Output, integer E[O], the indices of the exponents of
    #    the sorted polynomial.
    #

    indx = i4vec_sort_heap_index_a(o, e)

    e = i4vec_permute(o, indx, e)
    c = r8vec_permute(o, indx, c)

    return c, e


def polynomial_sort_test():

    # *****************************************************************************80
    #
    # POLYNOMIAL_SORT_TEST tests POLYNOMIAL_SORT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    o = 6
    c = np.array([0.0, 9.0, -5.0, - 13.0, 7.0, 11.0], dtype=np.float64)
    e = np.array([12, 4, 2, 33, 1, 5], dtype=np.int32)

    print('')
    print('POLYNOMIAL_SORT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYNOMIAL_SORT sorts a polynomial by exponent index.')

    print('')
    title = '  Unsorted polynomial:'
    polynomial_print(m, o, c, e, title)

    c, e = polynomial_sort(o, c, e)

    print('')
    title = '  Sorted polynomial:'
    polynomial_print(m, o, c, e, title)

    print('')
    print('POLYNOMIAL_SORT_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polynomial_sort_test()
    timestamp()
