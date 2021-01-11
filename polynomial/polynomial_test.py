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

from i4lib.i4_choose import i4_choose_test
from i4lib.i4_fall import i4_fall_test
from i4lib.i4_uniform_ab import i4_uniform_ab_test
from i4lib.i4vec_concatenate import i4vec_concatenate_test
from i4lib.i4vec_permute import i4vec_permute_test
from i4lib.i4vec_print import i4vec_print_test
from i4lib.i4vec_sort_heap_index_a import i4vec_sort_heap_index_a_test
from i4lib.i4vec_sum import i4vec_sum_test
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab_test
from r8lib.r8vec_concatenate import r8vec_concatenate_test
from r8lib.r8vec_permute import r8vec_permute_test
from r8lib.r8vec_print import r8vec_print_test
from polynomial.mono_next_grlex import mono_next_grlex_test, mono_total_next_grlex_test
from polynomial.mono_rank_grlex import mono_rank_grlex_test, mono_unrank_grlex_test
from polynomial.mono_upto_enum import mono_upto_enum_test
from polynomial.mono_value import mono_value_test
from polynomial.perm0_uniform import perm0_uniform_test
from polynomial.polynomial_add import polynomial_add_test
from polynomial.polynomial_axpy import polynomial_axpy_test
from polynomial.polynomial_compress import polynomial_compress_test
from polynomial.polynomial_dif import polynomial_dif_test
from polynomial.polynomial_mul import polynomial_mul_test
from polynomial.polynomial_print import polynomial_print_test
from polynomial.polynomial_scale import polynomial_scale_test
from polynomial.polynomial_sort import polynomial_sort_test
from polynomial.polynomial_value import polynomial_value_test


def polynomial_test():

    # *****************************************************************************80
    #
    # POLYNOMIAL_TEST tests the POLYNOMIAL library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYNOMIAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the POLYNOMIAL library.')

    perm0_uniform_test()

    mono_upto_enum_test()
    mono_next_grlex_test()
    mono_rank_grlex_test()
    mono_total_next_grlex_test()
    mono_unrank_grlex_test()
    mono_value_test()

    polynomial_add_test()
    polynomial_axpy_test()
    polynomial_compress_test()
    polynomial_dif_test()
    polynomial_mul_test()
    polynomial_print_test()
    polynomial_scale_test()
    polynomial_sort_test()
    polynomial_value_test()

    print('')
    print('POLYNOMIAL_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polynomial_test()
    timestamp()
