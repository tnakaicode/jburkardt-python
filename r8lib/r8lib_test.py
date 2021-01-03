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


def r8lib_test():

    # *****************************************************************************80
    #
    # r8lib_test tests r8lib.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    from r8lib.r8_abs import r8_abs_test
    from r8lib.r8_acos import r8_acos_test
    from r8lib.r8_acosh import r8_acosh_test
    from r8lib.r8_add import r8_add_test
    from r8lib.r8_agm import r8_agm_test
    from r8lib.r8_aint import r8_aint_test
    from r8lib.r8_asin import r8_asin_test
    from r8lib.r8_asinh import r8_asinh_test
    from r8lib.r8_atan import r8_atan_test
    from r8lib.r8_atanh import r8_atanh_test
    from r8lib.r8_big import r8_big_test
    from r8lib.r8_cas import r8_cas_test
    from r8lib.r8_ceiling import r8_ceiling_test
    from r8lib.r8_choose import r8_choose_test
    from r8lib.r8_chop import r8_chop_test
    from r8lib.r8_cosd import r8_cosd_test
    from r8lib.r8_cotd import r8_cotd_test
    from r8lib.r8_csc import r8_csc_test
    from r8lib.r8_cscd import r8_cscd_test
    from r8lib.r8_cube_root import r8_cube_root_test
    from r8lib.r8_degrees import r8_degrees_test
    from r8lib.r8_diff import r8_diff_test
    from r8lib.r8_digit import r8_digit_test
    from r8lib.r8_divide_i4 import r8_divide_i4_test
    from r8lib.r8_e import r8_e_test
    from r8lib.r8_epsilon import r8_epsilon_test
    from r8lib.r8_epsilon_compute import r8_epsilon_compute_test
    from r8lib.r8_exp import r8_exp_test
    from r8lib.r8_factorial import r8_factorial_test
    from r8lib.r8_factorial_stirling import r8_factorial_stirling_test
    from r8lib.r8_factorial_values import r8_factorial_values_test
    from r8lib.r8_factorial2 import r8_factorial2_test
    from r8lib.r8_factorial2_values import r8_factorial2_values_test
    from r8lib.r8_fall import r8_fall_test
    from r8lib.r8_fall_values import r8_fall_values_test
    from r8lib.r8_floor import r8_floor_test
    from r8lib.r8_fraction import r8_fraction_test
    from r8lib.r8_fractional import r8_fractional_test
    from r8lib.r8_gamma import r8_gamma_test
    from r8lib.r8_gamma_log import r8_gamma_log_test
    from r8lib.r8_gamma_log_int import r8_gamma_log_int_test
    from r8lib.r8_heaviside import r8_heaviside_test
    from r8lib.r8_huge import r8_huge_test
    from r8lib.r8_hypot import r8_hypot_test
    from r8lib.r8_is_in_01 import r8_is_in_01_test
    from r8lib.r8_is_inf import r8_is_inf_test
    from r8lib.r8_is_insignificant import r8_is_insignificant_test
    from r8lib.r8_is_integer import r8_is_integer_test
    from r8lib.r8_is_nan import r8_is_nan_test
    from r8lib.r8_log_10 import r8_log_10_test
    from r8lib.r8_log_2 import r8_log_2_test
    from r8lib.r8_log_b import r8_log_b_test
    from r8lib.r8_mant import r8_mant_test
    from r8lib.r8_max import r8_max_test
    from r8lib.r8_min import r8_min_test
    from r8lib.r8_mod import r8_mod_test
    from r8lib.r8_modp import r8_modp_test
    from r8lib.r8_mop import r8_mop_test
    from r8lib.r8_nint import r8_nint_test
    from r8lib.r8_normal_01 import r8_normal_01_test
    from r8lib.r8_normal_ab import r8_normal_ab_test
    from r8lib.r8_nth_root import r8_nth_root_test
    from r8lib.r8_pi import r8_pi_test
    from r8lib.r8_pi_sqrt import r8_pi_sqrt_test
    from r8lib.r8_power import r8_power_test
    from r8lib.r8_power_fast import r8_power_fast_test
    from r8lib.r8_print import r8_print_test
    from r8lib.r8_radians import r8_radians_test
    from r8lib.r8_relu import r8_relu_test
    from r8lib.r8_rise import r8_rise_test
    from r8lib.r8_rise_values import r8_rise_values_test
    from r8lib.r8_round import r8_round_test
    from r8lib.r8_round2 import r8_round2_test
    from r8lib.r8_roundb import r8_roundb_test
    from r8lib.r8_roundx import r8_roundx_test
    from r8lib.r8_secd import r8_secd_test
    from r8lib.r8_sech import r8_sech_test
    from r8lib.r8_sigmoid import r8_sigmoid_test
    from r8lib.r8_sign import r8_sign_test
    from r8lib.r8_sign_char import r8_sign_char_test
    from r8lib.r8_sign_match import r8_sign_match_test
    from r8lib.r8_sign_match_strict import r8_sign_match_strict_test
    from r8lib.r8_sign_opposite import r8_sign_opposite_test
    from r8lib.r8_sign_opposite_strict import r8_sign_opposite_strict_test
    from r8lib.r8_sign3 import r8_sign3_test
    from r8lib.r8_sincos_sum import r8_sincos_sum_test
    from r8lib.r8_sind import r8_sind_test
    from r8lib.r8_softplus import r8_softplus_test
    from r8lib.r8_sqrt_i4 import r8_sqrt_i4_test
    from r8lib.r8_swap import r8_swap_test
    from r8lib.r8_swap3 import r8_swap3_test
    from r8lib.r8_tand import r8_tand_test
    from r8lib.r8_tiny import r8_tiny_test
    from r8lib.r8_to_dhms import r8_to_dhms_test
    from r8lib.r8_to_i4 import r8_to_i4_test
    from r8lib.r8_to_r8_discrete import r8_to_r8_discrete_test
    from r8lib.r8_uniform_01 import r8_uniform_01_test
    from r8lib.r8_uniform_ab import r8_uniform_ab_test
    from r8lib.r8_unswap3 import r8_unswap3_test
    from r8lib.r8_walsh_1d import r8_walsh_1d_test
    from r8lib.r8_wrap import r8_wrap_test

    from r8lib.r82col_print_part import r82col_print_part_test
    from r8lib.r82row_print_part import r82row_print_part_test
    from r8lib.r82vec_print_part import r82vec_print_part_test
    from r8lib.r83col_print_part import r83col_print_part_test
    from r8lib.r83row_print_part import r83row_print_part_test
    from r8lib.r8block_print import r8block_print_test

    from r8lib.r8mat_add import r8mat_add_test
    from r8lib.r8mat_cholesky_factor import r8mat_cholesky_factor_test
    from r8lib.r8mat_cholesky_factor_upper import r8mat_cholesky_factor_upper_test
    from r8lib.r8mat_cholesky_solve import r8mat_cholesky_solve_test
    from r8lib.r8mat_det_2d import r8mat_det_2d_test
    from r8lib.r8mat_det_3d import r8mat_det_3d_test
    from r8lib.r8mat_det_4d import r8mat_det_4d_test
    from r8lib.r8mat_diag_get_vector import r8mat_diag_get_vector_test
    from r8lib.r8mat_house_axh import r8mat_house_axh_test
    from r8lib.r8mat_house_form import r8mat_house_form_test
    from r8lib.r8mat_identity import r8mat_identity_test
    from r8lib.r8mat_indicator import r8mat_indicator_test
    from r8lib.r8mat_inverse_3d import r8mat_inverse_3d_test
    from r8lib.r8mat_is_binary import r8mat_is_binary_test
    from r8lib.r8mat_l_solve import r8mat_l_solve_test
    from r8lib.r8mat_lt_solve import r8mat_lt_solve_test
    from r8lib.r8mat_mm import r8mat_mm_test
    from r8lib.r8mat_mtm import r8mat_mtm_test
    from r8lib.r8mat_mtv import r8mat_mtv_test
    from r8lib.r8mat_mv import r8mat_mv_test
    from r8lib.r8mat_nint import r8mat_nint_test
    from r8lib.r8mat_nonzeros import r8mat_nonzeros_test
    from r8lib.r8mat_norm_fro import r8mat_norm_fro_test
    from r8lib.r8mat_norm_fro_affine import r8mat_norm_fro_affine_test
    from r8lib.r8mat_norm_l1 import r8mat_norm_l1_test
    from r8lib.r8mat_norm_li import r8mat_norm_li_test
    from r8lib.r8mat_normal_01 import r8mat_normal_01_test
    from r8lib.r8mat_print import r8mat_print_test
    from r8lib.r8mat_print_some import r8mat_print_some_test
    from r8lib.r8mat_product_elementwise import r8mat_product_elementwise_test
    from r8lib.r8mat_ref import r8mat_ref_test
    from r8lib.r8mat_rref import r8mat_rref_test
    from r8lib.r8mat_scale_01 import r8mat_scale_01_test
    from r8lib.r8mat_scale_ab import r8mat_scale_ab_test
    from r8lib.r8mat_solve import r8mat_solve_test
    from r8lib.r8mat_standardize import r8mat_standardize_test
    from r8lib.r8mat_transpose import r8mat_transpose_test
    from r8lib.r8mat_transpose_print import r8mat_transpose_print_test
    from r8lib.r8mat_transpose_print_some import r8mat_transpose_print_some_test
    from r8lib.r8mat_u_inverse import r8mat_u_inverse_test
    from r8lib.r8mat_u_solve import r8mat_u_solve_test
    from r8lib.r8mat_uniform_01 import r8mat_uniform_01_test
    from r8lib.r8mat_uniform_ab import r8mat_uniform_ab_test
    from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec_test
    from r8lib.r8mat_ut_solve import r8mat_ut_solve_test
    from r8lib.r8mat_vand2 import r8mat_vand2_test

    from r8lib.r8rows_to_r8mat import r8rows_to_r8mat_test

    from r8lib.r8vec_amax import r8vec_amax_test
    from r8lib.r8vec_amax_index import r8vec_amax_index_test
    from r8lib.r8vec_amin import r8vec_amin_test
    from r8lib.r8vec_amin_index import r8vec_amin_index_test
    from r8lib.r8vec_asum import r8vec_asum_test
    from r8lib.r8vec_binary_next import r8vec_binary_next_test
    from r8lib.r8vec_bracket import r8vec_bracket_test
    from r8lib.r8vec_bracket5 import r8vec_bracket5_test
    from r8lib.r8vec_cheby_extreme import r8vec_cheby_extreme_test
    from r8lib.r8vec_cheby_zero import r8vec_cheby_zero_test
    from r8lib.r8vec_cheby1space import r8vec_cheby1space_test
    from r8lib.r8vec_concatenate import r8vec_concatenate_test
    from r8lib.r8vec_copy import r8vec_copy_test
    from r8lib.r8vec_correlation import r8vec_correlation_test
    from r8lib.r8vec_covariance import r8vec_covariance_test
    from r8lib.r8vec_diff_norm import r8vec_diff_norm_test
    from r8lib.r8vec_diff_norm_li import r8vec_diff_norm_li_test
    from r8lib.r8vec_direct_product import r8vec_direct_product_test
    from r8lib.r8vec_dot_product import r8vec_dot_product_test
    from r8lib.r8vec_eq import r8vec_eq_test
    from r8lib.r8vec_even import r8vec_even_test
    from r8lib.r8vec_even_select import r8vec_even_select_test
    from r8lib.r8vec_fill import r8vec_fill_test
    from r8lib.r8vec_frac import r8vec_frac_test
    from r8lib.r8vec_house_column import r8vec_house_column_test
    from r8lib.r8vec_identity_row import r8vec_identity_row_test
    from r8lib.r8vec_indicator0 import r8vec_indicator0_test
    from r8lib.r8vec_indicator1 import r8vec_indicator1_test
    from r8lib.r8vec_is_ascending import r8vec_is_ascending_test
    from r8lib.r8vec_is_ascending_strictly import r8vec_is_ascending_strictly_test
    from r8lib.r8vec_is_binary import r8vec_is_binary_test
    from r8lib.r8vec_is_distinct import r8vec_is_distinct_test
    from r8lib.r8vec_is_in_01 import r8vec_is_in_01_test
    from r8lib.r8vec_is_in_ab import r8vec_is_in_ab_test
    from r8lib.r8vec_is_insignificant import r8vec_is_insignificant_test
    from r8lib.r8vec_is_integer import r8vec_is_integer_test
    from r8lib.r8vec_is_negative import r8vec_is_negative_test
    from r8lib.r8vec_is_negative_any import r8vec_is_negative_any_test
    from r8lib.r8vec_is_nonnegative import r8vec_is_nonnegative_test
    from r8lib.r8vec_is_nonpositive import r8vec_is_nonpositive_test
    from r8lib.r8vec_is_nonzero_any import r8vec_is_nonzero_any_test
    from r8lib.r8vec_is_one import r8vec_is_one_test
    from r8lib.r8vec_is_positive import r8vec_is_positive_test
    from r8lib.r8vec_is_zero import r8vec_is_zero_test
    from r8lib.r8vec_linspace import r8vec_linspace_test
    from r8lib.r8vec_linspace2 import r8vec_linspace2_test
    from r8lib.r8vec_max import r8vec_max_test
    from r8lib.r8vec_max_abs_index import r8vec_max_abs_index_test
    from r8lib.r8vec_max_index import r8vec_max_index_test
    from r8lib.r8vec_mean import r8vec_mean_test
    from r8lib.r8vec_mean_geometric import r8vec_mean_geometric_test
    from r8lib.r8vec_mean_running import r8vec_mean_running_test
    from r8lib.r8vec_mean_update import r8vec_mean_update_test
    from r8lib.r8vec_midspace import r8vec_midspace_test
    from r8lib.r8vec_min import r8vec_min_test
    from r8lib.r8vec_mirror_next import r8vec_mirror_next_test
    from r8lib.r8vec_mirror_ab_next import r8vec_mirror_ab_next_test
    from r8lib.r8vec_nint import r8vec_nint_test
    from r8lib.r8vec_norm import r8vec_norm_test
    from r8lib.r8vec_norm_affine import r8vec_norm_affine_test
    from r8lib.r8vec_norm_l0 import r8vec_norm_l0_test
    from r8lib.r8vec_norm_l1 import r8vec_norm_l1_test
    from r8lib.r8vec_norm_l2 import r8vec_norm_l2_test
    from r8lib.r8vec_norm_li import r8vec_norm_li_test
    from r8lib.r8vec_norm_rms import r8vec_norm_rms_test
    from r8lib.r8vec_normal_01 import r8vec_normal_01_test
    from r8lib.r8vec_normal_ab import r8vec_normal_ab_test
    from r8lib.r8vec_normalize_l1 import r8vec_normalize_l1_test
    from r8lib.r8vec_permute import r8vec_permute_test
    from r8lib.r8vec_permute_cyclic import r8vec_permute_cyclic_test
    from r8lib.r8vec_permute_uniform import r8vec_permute_uniform_test
    from r8lib.r8vec_print import r8vec_print_test
    from r8lib.r8vec_print_part import r8vec_print_part_test
    from r8lib.r8vec_print_some import r8vec_print_some_test
    from r8lib.r8vec_product import r8vec_product_test
    from r8lib.r8vec_reverse import r8vec_reverse_test
    from r8lib.r8vec_rotate import r8vec_rotate_test
    from r8lib.r8vec_rsquared import r8vec_rsquared_test
    from r8lib.r8vec_scale_01 import r8vec_scale_01_test
    from r8lib.r8vec_scale_ab import r8vec_scale_ab_test
    from r8lib.r8vec_sign3_running import r8vec_sign3_running_test
    from r8lib.r8vec_smooth import r8vec_smooth_test
    from r8lib.r8vec_softmax import r8vec_softmax_test
    from r8lib.r8vec_sorted_nearest import r8vec_sorted_nearest_test
    from r8lib.r8vec_standardize import r8vec_standardize_test
    from r8lib.r8vec_std import r8vec_std_test
    from r8lib.r8vec_std_sample import r8vec_std_sample_test
    from r8lib.r8vec_std_update import r8vec_std_update_test
    from r8lib.r8vec_step import r8vec_step_test
    from r8lib.r8vec_sum import r8vec_sum_test
    from r8lib.r8vec_sum_running import r8vec_sum_running_test
    from r8lib.r8vec_transpose_print import r8vec_transpose_print_test
    from r8lib.r8vec_uniform_01 import r8vec_uniform_01_test
    from r8lib.r8vec_uniform_ab import r8vec_uniform_ab_test
    from r8lib.r8vec_uniform_unit import r8vec_uniform_unit_test
    from r8lib.r8vec_variance import r8vec_variance_test
    from r8lib.r8vec_variance_circular import r8vec_variance_circular_test
    from r8lib.r8vec_variance_sample import r8vec_variance_sample_test
    from r8lib.r8vec_variance_update import r8vec_variance_update_test

    from r8lib.r8vec2_print import r8vec2_print_test
    from r8lib.r8vec2_print_some import r8vec2_print_some_test

    from r8lib.r8vec3_print import r8vec3_print_test

    from r8lib.r4lib import r4_exp_test, r4_uniform_01_test, r4_uniform_ab_test
    from r8lib.r4lib import r4mat_print_test, r4mat_print_some_test
    from r8lib.r4lib import r4mat_uniform_01_test, r4mat_uniform_ab_test
    from r8lib.r4lib import r4vec_print_test, r4vec_covariance_test
    from r8lib.r4lib import r4vec_uniform_01_test, r4vec_uniform_ab_test

    print('')
    print('r8lib_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test r8lib.')

    r8_abs_test()
    r8_acos_test()
    r8_acosh_test()
    r8_add_test()
    r8_agm_test()
    r8_aint_test()
    r8_asin_test()
    r8_asinh_test()
    r8_atan_test()
    r8_atanh_test()
    r8_big_test()
    r8_cas_test()
    r8_ceiling_test()
    r8_choose_test()
    r8_chop_test()
    r8_cosd_test()
    r8_cotd_test()
    r8_csc_test()
    r8_cscd_test()
    r8_cube_root_test()
    r8_degrees_test()
    r8_diff_test()
    r8_digit_test()
    r8_divide_i4_test()
    r8_e_test()
    r8_epsilon_test()
    r8_epsilon_compute_test()
    r8_exp_test()
    r8_factorial_test()
    r8_factorial_stirling_test()
    r8_factorial_values_test()
    r8_factorial2_test()
    r8_factorial2_values_test()
    r8_fall_test()
    r8_fall_values_test()
    r8_floor_test()
    r8_fraction_test()
    r8_fractional_test()
    r8_gamma_test()
    r8_gamma_log_test()
    r8_heaviside_test()
    r8_huge_test()
    r8_hypot_test()
    r8_is_in_01_test()
    r8_is_inf_test()
    r8_is_insignificant_test()
    r8_is_integer_test()
    r8_is_nan_test()
    r8_log_10_test()
    r8_log_2_test()
    r8_log_b_test()
    r8_mant_test()
    r8_max_test()
    r8_min_test()
    r8_mod_test()
    r8_modp_test()
    r8_mop_test()
    r8_nint_test()
    r8_normal_01_test()
    r8_normal_ab_test()
    r8_nth_root_test()
    r8_pi_test()
    r8_pi_sqrt_test()
    r8_power_test()
    r8_power_fast_test()
    r8_print_test()
    r8_radians_test()
    r8_relu_test()
    r8_rise_test()
    r8_rise_values_test()
    r8_round_test()
    r8_round2_test()
    r8_roundb_test()
    r8_roundx_test()
    r8_secd_test()
    r8_sech_test()
    r8_sigmoid_test()
    r8_sign_test()
    r8_sign_char_test()
    r8_sign_match_test()
    r8_sign_match_strict_test()
    r8_sign_opposite_test()
    r8_sign_opposite_strict_test()
    r8_sign3_test()
    r8_sincos_sum_test()
    r8_sind_test()
    r8_softplus_test()
    r8_sqrt_i4_test()
    r8_swap_test()
    r8_swap3_test()
    r8_tand_test()
    r8_tiny_test()
    r8_to_dhms_test()
    r8_to_i4_test()
    r8_to_r8_discrete_test()
    r8_uniform_01_test()
    r8_uniform_ab_test()
    r8_unswap3_test()
    r8_walsh_1d_test()
    r8_wrap_test()

    r82col_print_part_test()
    r82row_print_part_test()
    r82vec_print_part_test()
    r83col_print_part_test()
    r83row_print_part_test()
    r8block_print_test()

    r8mat_add_test()
    r8mat_cholesky_factor_test()
    r8mat_cholesky_factor_upper_test()
    r8mat_cholesky_solve_test()
    r8mat_det_2d_test()
    r8mat_det_3d_test()
    r8mat_det_4d_test()
    r8mat_diag_get_vector_test()
    r8mat_house_axh_test()
    r8mat_house_form_test()
    r8mat_identity_test()
    r8mat_indicator_test()
    r8mat_inverse_3d_test()
    r8mat_is_binary_test()
    r8mat_l_solve_test()
    r8mat_lt_solve_test()
    r8mat_mm_test()
    r8mat_mtm_test()
    r8mat_mtv_test()
    r8mat_mv_test()
    r8mat_nint_test()
    r8mat_nonzeros_test()
    r8mat_norm_fro_test()
    r8mat_norm_fro_affine_test()
    r8mat_norm_l1_test()
    r8mat_normal_01_test()
    r8mat_print_test()
    r8mat_print_some_test()
    r8mat_product_elementwise_test()
    r8mat_ref_test()
    r8mat_rref_test()
    r8mat_scale_01_test()
    r8mat_scale_ab_test()
    r8mat_solve_test()
    r8mat_standardize_test()
    r8mat_transpose_test()
    r8mat_transpose_print_test()
    r8mat_transpose_print_some_test()
    r8mat_u_inverse_test()
    r8mat_u_solve_test()
    r8mat_uniform_01_test()
    r8mat_uniform_ab_test()
    r8mat_uniform_abvec_test()
    r8mat_ut_solve_test()
    r8mat_vand2_test()

    r8rows_to_r8mat_test()

    r8vec_amax_test()
    r8vec_amax_index_test()
    r8vec_amin_test()
    r8vec_amin_index_test()
    r8vec_asum_test()
    r8vec_binary_next_test()
    r8vec_bracket_test()
    r8vec_bracket5_test()
    r8vec_cheby_extreme_test()
    r8vec_cheby_zero_test()
    r8vec_cheby1space_test()
    r8vec_concatenate_test()
    r8vec_copy_test()
    r8vec_correlation_test()
    r8vec_covariance_test()
    r8vec_diff_norm_test()
    r8vec_diff_norm_li_test()
    r8vec_direct_product_test()
    r8vec_dot_product_test()
    r8vec_eq_test()
    r8vec_even_test()
    r8vec_even_select_test()
    r8vec_fill_test()
    r8vec_frac_test()
    r8vec_house_column_test()
    r8vec_identity_row_test()
    r8vec_indicator0_test()
    r8vec_indicator1_test()
    r8vec_is_ascending_test()
    r8vec_is_ascending_strictly_test()
    r8vec_is_binary_test()
    r8vec_is_distinct_test()
    r8vec_is_in_01_test()
    r8vec_is_in_ab_test()
    r8vec_is_insignificant_test()
    r8vec_is_integer_test()
    r8vec_is_negative_test()
    r8vec_is_negative_any_test()
    r8vec_is_nonnegative_test()
    r8vec_is_nonpositive_test()
    r8vec_is_nonzero_any_test()
    r8vec_is_one_test()
    r8vec_is_positive_test()
    r8vec_is_zero_test()
    r8vec_linspace_test()
    r8vec_linspace2_test()
    r8vec_max_test()
    r8vec_max_abs_index_test()
    r8vec_max_index_test()
    r8vec_mean_test()
    r8vec_mean_geometric_test()
    r8vec_mean_running_test()
    r8vec_mean_update_test()
    r8vec_midspace_test()
    r8vec_min_test()
    r8vec_mirror_next_test()
    r8vec_mirror_ab_next_test()
    r8vec_nint_test()
    r8vec_norm_test()
    r8vec_norm_affine_test()
    r8vec_norm_l0_test()
    r8vec_norm_l1_test()
    r8vec_norm_l2_test()
    r8vec_norm_li_test()
    r8vec_norm_rms_test()
    r8vec_normal_01_test()
    r8vec_normal_ab_test()
    r8vec_normalize_l1_test()
    r8vec_permute_test()
    r8vec_permute_cyclic_test()
    r8vec_permute_uniform_test()
    r8vec_print_test()
    r8vec_print_part_test()
    r8vec_print_some_test()
    r8vec_product_test()
    r8vec_reverse_test()
    r8vec_rotate_test()
    r8vec_rsquared_test()
    r8vec_sign3_running_test()
    r8vec_scale_01_test()
    r8vec_scale_ab_test()
    r8vec_smooth_test()
    r8vec_softmax_test()
    r8vec_sorted_nearest_test()
    r8vec_standardize_test()
    r8vec_std_test()
    r8vec_std_sample_test()
    r8vec_std_update_test()
    r8vec_step_test()
    r8vec_sum_test()
    r8vec_sum_running_test()
    r8vec_transpose_print_test()
    r8vec_uniform_01_test()
    r8vec_uniform_ab_test()
    r8vec_uniform_unit_test()
    r8vec_variance_test()
    r8vec_variance_circular_test()
    r8vec_variance_sample_test()
    r8vec_variance_update_test()

    r8vec2_print_test()
    r8vec2_print_some_test()

    r8vec3_print_test()

    r4_exp_test()
    r4_uniform_01_test()
    r4_uniform_ab_test()

    r4mat_print_test()
    r4mat_print_some_test()
    r4mat_uniform_01_test()
    r4mat_uniform_ab_test()

    r4vec_covariance_test()
    r4vec_print_test()
    r4vec_uniform_01_test()
    r4vec_uniform_ab_test()

    print('')
    print('r8lib_test:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8lib_test()
    timestamp()
