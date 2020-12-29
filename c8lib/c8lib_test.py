#! /usr/bin/env python
#

import numpy as np
import matplotlib.pyplot as plt
import math
import platform
import time
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from c8lib.c8_abs import c8_abs_test
from c8lib.c8_acos import c8_acos_test
from c8lib.c8_acosh import c8_acosh_test
from c8lib.c8_add import c8_add_test
from c8lib.c8_arg import c8_arg_test
from c8lib.c8_asin import c8_asin_test
from c8lib.c8_asinh import c8_asinh_test
from c8lib.c8_atan import c8_atan_test
from c8lib.c8_atanh import c8_atanh_test
from c8lib.c8_conj import c8_conj_test
from c8lib.c8_cos import c8_cos_test
from c8lib.c8_cosh import c8_cosh_test
from c8lib.c8_cube_root import c8_cube_root_test
from c8lib.c8_div import c8_div_test
from c8lib.c8_div_r8 import c8_div_r8_test
from c8lib.c8_exp import c8_exp_test
from c8lib.c8_i import c8_i_test
from c8lib.c8_imag import c8_imag_test
from c8lib.c8_inv import c8_inv_test
from c8lib.c8_le_l1 import c8_le_l1_test
from c8lib.c8_le_l2 import c8_le_l2_test
from c8lib.c8_le_li import c8_le_li_test
from c8lib.c8_log import c8_log_test
from c8lib.c8_mag import c8_mag_test
from c8lib.c8_mul import c8_mul_test
from c8lib.c8_nint import c8_nint_test
from c8lib.c8_norm_l1 import c8_norm_l1_test
from c8lib.c8_norm_l2 import c8_norm_l2_test
from c8lib.c8_norm_li import c8_norm_li_test
from c8lib.c8_normal_01 import c8_normal_01_test
from c8lib.c8_one import c8_one_test
from c8lib.c8_print import c8_print_test
from c8lib.c8_real import c8_real_test
from c8lib.c8_sin import c8_sin_test
from c8lib.c8_sinh import c8_sinh_test
from c8lib.c8_sqrt import c8_sqrt_test
from c8lib.c8_tan import c8_tan_test
from c8lib.c8_tanh import c8_tanh_test
from c8lib.c8_to_cartesian import c8_to_cartesian_test
from c8lib.c8_to_polar import c8_to_polar_test
from c8lib.c8_uniform_01 import c8_uniform_01_test
from c8lib.c8_zero import c8_zero_test
from c8lib.c8mat_identity import c8mat_identity_test
from c8lib.c8mat_indicator import c8mat_indicator_test
from c8lib.c8mat_norm_fro import c8mat_norm_fro_test
from c8lib.c8mat_norm_l1 import c8mat_norm_l1_test
from c8lib.c8mat_norm_li import c8mat_norm_li_test
from c8lib.c8mat_print import c8mat_print_test
from c8lib.c8mat_print_some import c8mat_print_some_test
from c8lib.c8mat_uniform_01 import c8mat_uniform_01_test
from c8lib.c8vec_indicator import c8vec_indicator_test
from c8lib.c8vec_nint import c8vec_nint_test
from c8lib.c8vec_norm_l1 import c8vec_norm_l1_test
from c8lib.c8vec_norm_l2 import c8vec_norm_l2_test
from c8lib.c8vec_norm_li import c8vec_norm_li_test
from c8lib.c8vec_print import c8vec_print_test
from c8lib.c8vec_print_part import c8vec_print_part_test
from c8lib.c8vec_sort_a_l1 import c8vec_sort_a_l1_test
from c8lib.c8vec_sort_a_l2 import c8vec_sort_a_l2_test
from c8lib.c8vec_sort_a_li import c8vec_sort_a_li_test
from c8lib.c8vec_spiral import c8vec_spiral_test
from c8lib.c8vec_uniform_01 import c8vec_uniform_01_test
from c8lib.c8vec_unity import c8vec_unity_test
from c8lib.cartesian_to_c8 import cartesian_to_c8_test
from c8lib.polar_to_c8 import polar_to_c8_test
from c8lib.r8_atan import r8_atan_test
from c8lib.r8_uniform_01 import r8_uniform_01_test


def c8lib_test():

    # *****************************************************************************80
    #
    # C8LIB_TEST tests the C8LIB library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('C8LIB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the C8LIB library.')


    cartesian_to_c8_test()

    polar_to_c8_test()

    r8_atan_test()
    r8_uniform_01_test()

    print('')
    print('C8LIB_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    c8lib_test()
    timestamp()
