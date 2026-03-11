#! /usr/bin/env python3
#
def r8lib_test ( ):

#*****************************************************************************80
#
## r8lib_test() tests r8lib().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform
  import scipy

  print ( '' )
  print ( 'r8lib_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + scipy.version.version )
  print ( '  Test r8lib().' )

  rng = default_rng ( )

  agm_values_test ( )

  gamma_values_test ( )
  gamma_log_values_test ( )

  i4_log_10_test ( )
  i4_modp_test ( )
  i4_sign_test ( )
  i4_uniform_ab_test ( rng )
  i4_wrap_test ( )

  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_print_test ( )
  i4vec_transpose_print_test ( )
  i4vec_uniform_ab_test ( rng )

  ksub_next4_test ( )

  perm0_check_test ( )
  perm0_uniform_test ( rng )

  perm1_check_test ( )
  perm1_uniform_test ( rng )

  r8_abs_test ( rng )
  r8_acos_test ( )
  r8_acosh_test ( )
  r8_add_test ( rng )
  r8_agm_test ( )
  r8_aint_test ( rng )
  r8_asin_test ( )
  r8_asinh_test ( )
  r8_atan_test ( )
  r8_atanh_test ( )
  r8_big_test ( )
  r8_cas_test ( )
  r8_ceiling_test ( )
  r8_choose_test ( )
  r8_chop_test ( )
  r8_cosd_test ( )
  r8_cotd_test ( )
  r8_csc_test ( )
  r8_cscd_test ( )
  r8_cube_root_test ( rng )
  r8_degrees_test ( )
  r8_diff_test ( )
  r8_digit_test ( )
  r8_divide_i4_test ( )
  r8_e_test ( )
  r8_epsilon_test ( )
  r8_epsilon_compute_test ( )
  r8_exp_test ( )
  r8_factorial_test ( )
  r8_factorial_stirling_test ( )
  r8_factorial_values_test ( )
  r8_factorial2_test ( )
  r8_factorial2_values_test ( )
  r8_fall_test ( )
  r8_fall_values_test ( )
  r8_floor_test ( rng )
  r8_fraction_test ( rng )
  r8_fractional_test ( rng )
  r8_gamma_test ( )
  r8_gamma_log_test ( )
  r8_heaviside_test ( )
  r8_huge_test ( )
  r8_hypot_test ( )
  r8_is_in_01_test ( rng )
  r8_is_inf_test ( )
  r8_is_insignificant_test ( )
  r8_is_integer_test ( )
  r8_is_nan_test ( )
  r8_log_10_test ( )
  r8_log_2_test ( )
  r8_log_b_test ( )
  r8_mant_test ( )
  r8_max_test ( rng )
  r8_min_test ( rng )
  r8_mod_test ( rng )
  r8_modp_test ( rng )
  r8_mop_test ( rng )
  r8_nint_test ( rng )
  r8_normal_01_test ( rng )
  r8_normal_ab_test ( rng )
  r8_nth_root_test ( )
  r8_pi_test ( )
  r8_pi_sqrt_test ( )
  r8_power_test ( )
  r8_power_fast_test ( )
  r8_print_test ( )
  r8_radians_test ( )
  r8_relu_test ( )
  r8_rise_test ( )
  r8_rise_values_test ( )
  r8_round_test ( rng )
  r8_round2_test ( )
  r8_roundb_test ( )
  r8_roundx_test ( rng )
  r8_secd_test ( )
  r8_sech_test ( )
  r8_sigmoid_test ( )
  r8_sign_test ( )
  r8_sign_char_test ( rng )
  r8_sign_match_test ( rng )
  r8_sign_match_strict_test ( rng )
  r8_sign_opposite_test ( rng )
  r8_sign_opposite_strict_test ( rng )
  r8_sign3_test ( )
  r8_sincos_sum_test ( rng )
  r8_sind_test ( )
  r8_softplus_test ( )
  r8_sqrt_i4_test ( rng )
  r8_swap_test ( )
  r8_swap3_test ( )
  r8_tand_test ( )
  r8_tiny_test ( )
  r8_to_dhms_test ( rng )
  r8_to_i4_test ( )
  r8_to_r8_discrete_test ( rng )
  r8_uniform_01_test ( rng )
  r8_uniform_ab_test ( rng )
  r8_unswap3_test ( )
  r8_walsh_1d_test ( )
  r8_wrap_test ( rng )

  r82col_print_part_test ( )

  r82row_print_part_test ( )

  r82vec_print_part_test ( )

  r83col_print_part_test ( )

  r83row_print_part_test ( )

  r8block_print_test ( )

  r8col_flip_test ( rng )

  r8mat_add_test ( )
  r8mat_cholesky_factor_test ( )
  r8mat_cholesky_factor_upper_test ( )
  r8mat_cholesky_solve_test ( )
  r8mat_column_append_test ( )
  r8mat_det_2d_test ( )
  r8mat_det_3d_test ( )
  r8mat_det_4d_test ( )
  r8mat_diag_get_vector_test ( rng )
  r8mat_house_axh_test ( rng )
  r8mat_house_form_test ( )
  r8mat_identity_test ( )
  r8mat_indicator_test ( )
  r8mat_inverse_3d_test ( )
  r8mat_is_binary_test ( )
  r8mat_l_solve_test ( )
  r8mat_l1_inverse_test ( )
  r8mat_lt_solve_test ( )
  r8mat_mm_test ( )
  r8mat_mtm_test ( )
  r8mat_mtv_test ( )
  r8mat_mv_test ( )
  r8mat_nint_test ( rng )
  r8mat_nonzeros_test ( )
  r8mat_norm_fro_test ( )
  r8mat_norm_fro_affine_test ( rng )
  r8mat_norm_l1_test ( rng )
  r8mat_norm_rms_test ( )
  r8mat_normal_01_test ( rng )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_product_elementwise_test ( )
  r8mat_ref_test ( )
  r8mat_rref_test ( )
  r8mat_rref_solve_binary_test ( )
  r8mat_rref_solve_binary_nz_test ( )
  r8mat_scale_01_test ( rng )
  r8mat_scale_ab_test ( rng )
  r8mat_solve_test ( )
  r8mat_standardize_test ( rng )
  r8mat_transpose_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
  r8mat_u_inverse_test ( )
  r8mat_u_solve_test ( )
  r8mat_uniform_01_test ( rng )
  r8mat_uniform_ab_test ( rng )
  r8mat_uniform_abvec_test ( rng )
  r8mat_ut_solve_test ( )
  r8mat_vand2_test ( )

  r8rows_to_r8mat_test ( )

  r8vec_amax_test ( rng )
  r8vec_amax_index_test ( rng )
  r8vec_amin_test ( rng )
  r8vec_amin_index_test ( rng )
  r8vec_asum_test ( rng )
  r8vec_binary_next_test ( )
  r8vec_bracket_test ( rng )
  r8vec_bracket5_test ( )
  r8vec_cheby_extreme_test ( )
  r8vec_cheby_zero_test ( )
  r8vec_cheby1space_test ( )
  r8vec_concatenate_test ( )
  r8vec_copy_test ( )
  r8vec_correlation_test ( )
  r8vec_covariance_test ( rng )
  r8vec_diff_norm_test ( )
  r8vec_diff_norm_li_test ( rng )
  r8vec_direct_product_test ( )
  r8vec_direct_product2_test ( )
  r8vec_dot_product_test ( rng )
  r8vec_eq_test ( )
  r8vec_even_test ( )
  r8vec_even_select_test ( )
  r8vec_fill_test ( )
  r8vec_frac_test ( rng )
  r8vec_house_column_test ( rng )
  r8vec_identity_row_test ( )
  r8vec_indicator0_test ( )
  r8vec_indicator1_test ( )
  r8vec_is_ascending_test ( )
  r8vec_is_ascending_strictly_test ( )
  r8vec_is_binary_test ( )
  r8vec_is_distinct_test ( )
  r8vec_is_in_01_test ( )
  r8vec_is_in_ab_test ( )
  r8vec_is_insignificant_test ( )
  r8vec_is_integer_test ( )
  r8vec_is_negative_test ( )
  r8vec_is_negative_any_test ( )
  r8vec_is_nonnegative_test ( )
  r8vec_is_nonpositive_test ( )
  r8vec_is_nonzero_any_test ( )
  r8vec_is_one_test ( )
  r8vec_is_positive_test ( )
  r8vec_is_zero_test ( )
  r8vec_linspace_test ( )
  r8vec_linspace2_test ( )
  r8vec_max_test ( rng )
  r8vec_max_abs_index_test ( rng )
  r8vec_max_index_test ( rng )
  r8vec_mean_test ( rng )
  r8vec_mean_geometric_test ( rng )
  r8vec_mean_running_test ( rng )
  r8vec_mean_update_test ( rng )
  r8vec_midspace_test ( )
  r8vec_min_test ( rng )
  r8vec_mirror_next_test ( )
  r8vec_mirror_ab_next_test ( )
  r8vec_nint_test ( rng )
  r8vec_norm_test ( rng )
  r8vec_norm_affine_test ( rng )
  r8vec_norm_l0_test ( rng )
  r8vec_norm_l1_test ( rng )
  r8vec_norm_l2_test ( rng )
  r8vec_norm_li_test ( rng )
  r8vec_norm_rms_test ( )
  r8vec_normal_01_test ( rng )
  r8vec_normal_ab_test ( rng )
  r8vec_normalize_l1_test ( rng )
  r8vec_permute_test ( )
  r8vec_permute_cyclic_test ( )
  r8vec_permute_uniform_test ( rng )
  r8vec_print_test ( )
  r8vec_print_part_test ( )
  r8vec_print_some_test ( )
  r8vec_product_test ( rng )
  r8vec_reverse_test ( )
  r8vec_rotate_test ( )
  r8vec_rsquared_test ( )
  r8vec_scale_01_test ( rng )
  r8vec_scale_ab_test ( rng )
  r8vec_shift_circular_test ( )
  r8vec_sign3_running_test ( rng )
  r8vec_smooth_test ( )
  r8vec_softmax_test ( rng )
  r8vec_sorted_nearest_test ( rng )
  r8vec_standardize_test ( rng )
  r8vec_std_test ( rng )
  r8vec_std_sample_test ( rng )
  r8vec_std_sample_update_test ( rng )
  r8vec_std_update_test ( rng )
  r8vec_std_updates_test ( rng )
  r8vec_step_test ( )
  r8vec_sum_test ( rng )
  r8vec_sum_running_test ( rng )
  r8vec_transpose_print_test ( )
  r8vec_uniform_01_test ( rng )
  r8vec_uniform_ab_test ( rng )
  r8vec_uniform_unit_test ( rng )
  r8vec_variance_test ( rng )
  r8vec_variance_circular_test ( rng )
  r8vec_variance_sample_test ( rng )
  r8vec_variance_sample_update_test ( rng )
  r8vec_variance_update_test ( rng )

  r8vec2_print_test ( )
  r8vec2_print_some_test ( )

  r8vec3_print_test ( )

  sort_heap_external_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8lib_test():' )
  print ( '  Normal end of execution.' )
  return

def agm_values ( n_data ):

#*****************************************************************************80
#
## agm_values() returns some values of the AGM.
#
#  Discussion:
#
#    The AGM is defined for nonnegative A and B.
#
#    The AGM of numbers A and B is defined by setting
#
#      A(0) = A,
#      B(0) = B
#
#      A(N+1) = ( A(N) + B(N) ) / 2
#      B(N+1) = sqrt ( A(N) * B(N) )
#
#    The two sequences both converge to AGM(A,B).
#
#    In Mathematica, the AGM can be evaluated by
#
#      ArithmeticGeometricMean [ a, b ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, the arguments of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  a_vec = np.array ( ( \
     22.0, \
     83.0, \
     42.0, \
     26.0, \
      4.0, \
      6.0, \
     40.0, \
     80.0, \
     90.0, \
      9.0, \
     53.0, \
      1.0, \
      1.0, \
      1.0, \
      1.5 ) )
  b_vec = np.array ( ( \
     96.0, \
     56.0, \
      7.0, \
     11.0, \
     63.0, \
     45.0, \
     75.0, \
      0.0, \
     35.0, \
      1.0, \
     53.0, \
      2.0, \
      4.0, \
      8.0, \
      8.0 ) )
  fx_vec = np.array ( ( \
     52.274641198704240049, \
     68.836530059858524345, \
     20.659301196734009322, \
     17.696854873743648823, \
     23.867049721753300163, \
     20.717015982805991662, \
     56.127842255616681863, \
      0.000000000000000000, \
     59.269565081229636528, \
     3.9362355036495554780, \
     53.000000000000000000, \
     1.4567910310469068692, \
     2.2430285802876025701, \
     3.6157561775973627487, \
     4.0816924080221632670 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    fx = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, fx

def agm_values_test ( ):

#*****************************************************************************80
#
## agm_values_test() tests agm_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2008
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'agm_values_test():' )
  print ( '  agm_values() stores values of' )
  print ( '  the arithmetic geometric mean function.' )
  print ( '' )
  print ( '      A           B         AGM(A,B)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx = agm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( a, b, fx ) )

  return

def gamma_log_values ( n_data ):

#*****************************************************************************80
#
## gamma_log_values() returns some values of the Log Gamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[Gamma[x]]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.1524063822430784E+01, \
      0.7966778177017837E+00, \
      0.3982338580692348E+00, \
      0.1520596783998375E+00, \
      0.0000000000000000E+00, \
     -0.4987244125983972E-01, \
     -0.8537409000331584E-01, \
     -0.1081748095078604E+00, \
     -0.1196129141723712E+00, \
     -0.1207822376352452E+00, \
     -0.1125917656967557E+00, \
     -0.9580769740706586E-01, \
     -0.7108387291437216E-01, \
     -0.3898427592308333E-01, \
     0.00000000000000000E+00, \
     0.69314718055994530E+00, \
     0.17917594692280550E+01, \
     0.12801827480081469E+02, \
     0.39339884187199494E+02, \
     0.71257038967168009E+02 ) )

  x_vec = np.array ( ( \
      0.20E+00, \
      0.40E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def gamma_log_values_test ( ):

#*****************************************************************************80
#
## gamma_log_values_test() tests gamma_log_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gamma_log_values():' )
  print ( '  gamma_log_values() stores values of' )
  print ( '  the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            gamma_log(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def gamma_values ( n_data ):

#*****************************************************************************80
#
## gamma_values() returns some values of the Gamma function.
#
#  Discussion:
#
#    The Gamma function is defined as:
#
#      Gamma(Z) = Integral ( 0 <= T < Infinity) T^(Z-1) exp(-T) dT
#
#    It satisfies the recursion:
#
#      Gamma(X+1) = X * Gamma(X)
#
#    Gamma is undefined for nonpositive integral X.
#    Gamma(0.5) = sqrt(PI)
#    For N a positive integer, Gamma(N+1) = N!, the standard factorial.
#
#    In Mathematica, the function can be evaluated by:
#
#      Gamma[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     -0.3544907701811032E+01, \
     -0.1005871979644108E+03, \
      0.9943258511915060E+02, \
      0.9513507698668732E+01, \
      0.4590843711998803E+01, \
      0.2218159543757688E+01, \
      0.1772453850905516E+01, \
      0.1489192248812817E+01, \
      0.1164229713725303E+01, \
      0.1000000000000000E+01, \
      0.9513507698668732E+00, \
      0.9181687423997606E+00, \
      0.8974706963062772E+00, \
      0.8872638175030753E+00, \
      0.8862269254527580E+00, \
      0.8935153492876903E+00, \
      0.9086387328532904E+00, \
      0.9313837709802427E+00, \
      0.9617658319073874E+00, \
      0.1000000000000000E+01, \
      0.2000000000000000E+01, \
      0.6000000000000000E+01, \
      0.3628800000000000E+06, \
      0.1216451004088320E+18, \
      0.8841761993739702E+31 ) )

  x_vec = np.array ( ( \
     -0.50E+00, \
     -0.01E+00, \
      0.01E+00, \
      0.10E+00, \
      0.20E+00, \
      0.40E+00, \
      0.50E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def gamma_values_test ( ):

#*****************************************************************************80
#
## gamma_values_test() tests gamma_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gamma_values_test():' )
  print ( '  gamma_values() stores values of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10() returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = np.abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test() tests i4_log_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test():' )
  print ( '  i4_log_10(): whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print() prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## i4mat_print_test() tests i4mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_print_test():' )
  print ( '  Test i4mat_print, which prints an I4MAT.' )

  m = 5
  n = 6
  a = np.array ( ( \
    ( 11, 12, 13, 14, 15, 16 ), \
    ( 21, 22, 23, 24, 25, 26 ), \
    ( 31, 32, 33, 34, 35, 36 ), \
    ( 41, 42, 43, 44, 45, 46 ), \
    ( 51, 52, 53, 54, 55, 56 ) ) )
  title = '  A 5 x 6 integer matrix:'
  i4mat_print ( m, n, a, title )

  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some() prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 10

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_print_some_test() tests i4mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_print_some_test():' )
  print ( '  i4mat_print_some() prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = int )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )

  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = i4_modp ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, i4_modp(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  i4_modp    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is divided by J.
#
  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'i4_modp_test():' )
  print ( '  i4_modp() factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  return

def i4_sign ( i ):

#*****************************************************************************80
#
## i4_sign() returns the sign of an integer.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose sign is desired.
#
#  Output:
#
#    integer VALUE, the sign of I.
#
  if ( i < 0 ):
    value = -1
  else:
    value = +1

  return value

def i4_sign_test ( ):

#*****************************************************************************80
#
## i4_sign_test() tests i4_sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  i4_vec = np.array ( ( -10, -7, 0, 5, 9 ) )

  print ( '' )
  print ( 'i4_sign_test():' )
  print ( '  i4_sign() returns the sign of an I4.' )
  print ( '' )
  print ( '    I4  i4_sign(I4)' )
  print ( '' )

  for test in range ( 0, test_num ):
    i4 = i4_vec[test]
    s = i4_sign ( i4 )
    print ( '  %4d  %11d' % ( i4, s ) )

  return

def i4_uniform_ab ( a, b, rng ):

#*****************************************************************************80
#
## i4_uniform_ab() returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer C, the randomly chosen integer.
#
  value = rng.integers ( low = a, high = b, endpoint = True )

  return value

def i4_uniform_ab_test ( rng ):

#*****************************************************************************80
#
## i4_uniform_ab_test() tests i4_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  a = -100
  b = 200

  print ( '' )
  print ( 'i4_uniform_ab_test():' )
  print ( '  i4_uniform_ab() computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j = i4_uniform_ab ( a, b, rng )
    print ( '  %8d  %8d' % ( i, j ) )

  return

def i4vec_indicator0 ( n ):

#*****************************************************************************80
#
## i4vec_indicator0() sets an I4VEC to the indicator vector ( 0, 1, 2, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    integer A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n, dtype = int )

  for i in range ( 0, n ):
    a[i] = i

  return a

def i4vec_indicator0_test ( ):

#*****************************************************************************80
#
## i4vec_indicator0_test() tests i4vec_indicator0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4vec_indicator0_test():' )
  print ( '  i4vec_indicator0() returns an indicator vector.' )

  n = 10
  a = i4vec_indicator0 ( n )
  i4vec_print ( n, a, '  The indicator0 vector:' )

  return

def i4vec_indicator1 ( n ):

#*****************************************************************************80
#
## i4vec_indicator1() sets an I4VEC to the indicator vector ( 1, 2, 3, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    integer A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n, dtype = int )

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def i4vec_indicator1_test ( ):

#*****************************************************************************80
#
## i4vec_indicator1_test() tests i4vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4vec_indicator1_test():' )
  print ( '  i4vec_indicator1() returns an indicator vector.' )

  n = 10
  a = i4vec_indicator1 ( n )
  i4vec_print ( n, a, '  The indicator1 vector:' )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = int )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  return

def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_transpose_print() prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( title, end = '' )

  if ( 0 < n ):
    for i in range ( 0, n ):
      print ( ' %d' % ( a[i] ), end = '' )
      if ( ( i + 1 ) % 20 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '(empty vector)' )

  return

def i4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## i4vec_transpose_print_test() tests i4vec_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_transpose_print_test():' )
  print ( '  i4vec_transpose_print() prints an I4VEC' )
  print ( '  with 5 entries to a row, and an optional title.' )

  n = 12
  a = np.zeros ( n, dtype = int )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  print ( '' )
  i4vec_transpose_print ( n, a, '  My array:  ' )

  return

def i4vec_uniform_ab ( n, a, b, rng ):

#*****************************************************************************80
#
## i4vec_uniform_ab() returns a scaled pseudorandom I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer C(N), the randomly chosen integer vector.
#
  c = rng.integers ( low = a, high = b, size = n, endpoint = True )

  return c

def i4vec_uniform_ab_test ( rng ):

#*****************************************************************************80
#
## i4vec_uniform_ab_test() tests i4vec_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 20
  a = -100
  b = 200

  print ( '' )
  print ( 'i4vec_uniform_ab_test():' )
  print ( '  i4vec_uniform_ab() computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '' )

  v = i4vec_uniform_ab ( n, a, b, rng )

  i4vec_print ( n, v, '  The random vector:' )

  return

def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test():' )
  print ( '  i4_wrap() forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  i4_wrap(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )

  return

def ksub_next4 ( n, k, a, done ):

#*****************************************************************************80
#
## ksub_next4() generates the subsets of size K from a set of size N, one at a time.
#
#  Discussion:
#
#    The subsets are generated one at a time.
#
#    The routine should be used by setting DONE to TRUE, and then calling
#    repeatedly.  Each call returns with DONE equal to FALSE, the array
#    A contains information defining a new subset.  When DONE returns
#    equal to TRUE, there are no more subsets.
#
#    There are ( N*(N-1)*...*(N+K-1)) / ( K*(K-1)*...*2*1) such subsets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2018
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the size of the entire set.
#
#    integer K, the size of the desired subset.  K must be
#    between 0 and N.
#
#    integer A(K), is not needed on the first call, with DONE = TRUE.
#    On subsequent calls, it should be the output value of A from the
#    previous call.
#
#    logical DONE, should be TRUE on the first call, to force initialization,
#    and then FALSE on subsequent calls.
#
#  Output:
#
#    integer A(K), as long as DONE is returned FALSE, A 
#    is the next K subset.
#
#    bool DONE, is TRUE if the routine is returning the
#    next K subset, and FALSE if there are no more subsets to return.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_next4 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    raise Exception ( 'ksub_next4 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_next4 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    raise Exception ( 'ksub_next4 - Fatal error!' )
#
#  First call:
#
  if ( done ):

    a = np.zeros ( n, dtype = int )

    for i in range ( 0, n ):
      a[i] = i + 1

    done = False
#
#  Empty set returned on previous call.
#
  elif ( 0 == n or 0 == k ):

    done = True
#
#  Next call.
#
  elif ( a[0] < n - k + 1 ):

    jsave = k

    for j in range ( 1, k ):

      if ( a[j-1] + 1 < a[j] ):
        jsave = j
        break

    for j in range ( 0, jsave - 1 ):
      a[j] = j + 1
    a[jsave-1] = a[jsave-1] + 1
    done = False

  else:

    done = True

  return a, done

def ksub_next4_test ( ):

#*****************************************************************************80
#
## ksub_next4_test() tests ksub_next4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_next4_test():' )
  print ( '  ksub_next4() generates K subsets of an N set.' )
  print ( '  N = %d' % ( n ) )
  print ( '  K = %d' % ( k ) )
  print ( '' )
  print ( 'Rank    Subset' )
  print ( '' )

  a = np.zeros ( k )
  done = True
  rank = 0
 
  while ( True ):
 
    a, done = ksub_next4 ( n, k, a, done )
 
    if ( done ):
      break

    rank = rank + 1
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

  return

def perm0_check ( n, p ):

#*****************************************************************************80
#
## perm0_check() checks a permutation of (0,...,N-1).
#
#  Discussion:
#
#    The routine verifies that each of the integers from 0 to
#    to N-1 occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    integer P(N), the array to check.
#
#  Output:
#
#    bool CHECK:
#    True if P is a legal permutation of (0,...,N-1).
#    False if P is not a legal permutation of (0,...,N-1).
#
  check = True

  for value in range ( 0, n ):

    check = False

    for location in range ( 0, n ):
      if ( p[location] == value ):
        check = True
        break

    if ( not check ):
      print ( '' )
      print ( 'perm0_check - Warning!' )
      print ( '  Permutation is missing the value %d.' % ( value ) )
      break

  return check

def perm0_check_test ( ):

#*****************************************************************************80
#
## perm0_check_test() tests perm0_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 0, 2, 1, 3, 2 ] )

  print ( '' )
  print ( 'perm0_check_test():' )
  print ( '  perm0_check() checks a permutation of 0,...,N-1.' )

  i4vec_transpose_print ( n, p1, '  Permutation 1:' )
  check = perm0_check ( n, p1 )

  i4vec_transpose_print ( n, p2, '  Permutation 2:' )
  check = perm0_check ( n, p2 )

  i4vec_transpose_print ( n, p3, '  Permutation 3:' )
  check = perm0_check ( n, p3 )

  return

def perm0_uniform ( n, rng ):

#*****************************************************************************80
#
## perm0_uniform() selects a random permutation of 0,...,N-1.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation of 0, ..., N-1.
#
  import numpy as np

  p = np.zeros ( n, dtype = int )

  for i in range ( 0, n ):
    p[i] = i

  for i in range ( 0, n - 1 ):
    j = rng.integers ( low = i, high = n - 1, endpoint = True )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def perm0_uniform_test ( rng ):

#*****************************************************************************80
#
## perm0_uniform_test() tests perm0_uniform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'perm0_uniform_test():' )
  print ( '  perm0_uniform() randomly selects a permutation of 0,...,N-1.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm0_uniform ( n, rng )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%4d' % ( p[i] ), end = '' )
    print ( '' )

  return

def perm1_check ( n, p ):

#*****************************************************************************80
#
## perm1_check() checks a 1-based permutation.
#
#  Discussion:
#
#    The routine verifies that each of the integers from 1 to
#    to N occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    integer P(N), the array to check.
#
#  Output:
#
#    bool CHECK:
#    True if P is a legal permutation of (1,...,N).
#    False if P is not a legal permutation of (1,...,N).
#
  check = True

  for value in range ( 1, n + 1 ):

    check = False

    for location in range ( 0, n ):
      if ( p[location] == value ):
        check = True
        break

    if ( not check ):
      print ( '' )
      print ( 'perm1_check - Warning!' )
      print ( '  Permutation is missing the value %d.' % ( value ) )
      break

  return check

def perm1_check_test ( ):

#*****************************************************************************80
#
## perm1_check_test() tests perm1_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 0, 2, 1, 3, 2 ] )

  print ( '' )
  print ( 'perm1_check_test():' )
  print ( '  perm1_check() checks a permutation of 1,...,N.' )

  i4vec_transpose_print ( n, p1, '  Permutation 1:' )
  check = perm1_check ( n, p1 )

  i4vec_transpose_print ( n, p2, '  Permutation 2:' )
  check = perm1_check ( n, p2 )

  i4vec_transpose_print ( n, p3, '  Permutation 3:' )
  check = perm1_check ( n, p3 )

  return

def perm1_uniform ( n, rng ):

#*****************************************************************************80
#
## perm1_uniform() selects a random permutation of 1, ..., N.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation of the digits 1 through N.
#
  import numpy as np

  p = np.zeros ( n, dtype = int )

  for i in range ( 0, n ):
    p[i] = i + 1

  for i in range ( 0, n - 1 ):
    j = rng.integers ( low = i, high = n - 1, endpoint = True )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def perm1_uniform_test ( rng ):

#*****************************************************************************80
#
## perm1_uniform_test() tests perm1_uniform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'perm1_uniform_test():' )
  print ( '  perm1_uniform() randomly selects a permutation of 1, ..., N.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm1_uniform ( n, rng )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%4d' % ( p[i] ), end = '' )
    print ( '' )

  return

def pyramid_square_num ( n ):

#*****************************************************************************80
#
## pyramid_square_num() returns the N-th pyramidal square number.
#
#  Discussion:
#
#    The N-th pyramidal square number PS(N) is formed by the sum of the first
#    N squares S:
#
#      S(I) = I^2
#
#      PS(N) = sum ( 1 <= I <= N ) S(I)
#
#    By convention, PS(0) = 0.
#
#    The formula is:
#
#      PS(N) = ( N * ( N + 1 ) * ( 2*N+1 ) ) / 6
#
#    Note that geometrically, this pyramid will have a square base.
#
#  Example:
#
#    0    0
#    1    1
#    2    5
#    3   14
#    4   30
#    5   55
#    6   91
#    7  140
#    8  204
#    9  285
#   10  385
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer  N, the index.
#    0 <= N.
#
#  Output:
#
#    integer VALUE, the N-th pyramid square number.
#
  value = ( n * ( n + 1 ) * ( 2 * n + 1 ) ) / 6

  return value

def pyramid_square_num_test ( ):

#*****************************************************************************80
#
## pyramid_square_num_test() tests pyramid_square_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pyramid_square_num_test():' )
  print ( '  pyramid_square_num computes the pyramidal square numbers.' )
  print ( '' )
 
  for n in range ( 1, 11 ):
    print ( '  %2d  %6d' % ( n, pyramid_square_num ( n ) ) )

  return

def r82col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r82col_print_part() prints "part" of an R82COL.
#
#  Discussion:
#
#    An R82COL is an (N,2) array of R8's.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2001
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N,2), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )
        print ( '  ....  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  ...more entries...' % ( i, a[i,0], a[i,1] ) )

  return

def r82col_print_part_test ( ):

#*****************************************************************************80
#
## r82col_print_part_test() tests r82col_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r82col_print_part_test():' )
  print ( '  r82col_print_part() prints an R82COL.' )

  n = 10

  v = np.array ( [ \
    [  11,  12 ], \
    [  21,  22 ], \
    [  31,  32 ], \
    [  41,  42 ], \
    [  51,  52 ], \
    [  61,  62 ], \
    [  71,  72 ], \
    [  81,  82 ], \
    [  91,  92 ], \
    [ 101, 102 ] ] )

  max_print = 2
  r82col_print_part ( n, v, max_print, '  Output with MAX_print = 2' )

  max_print = 5
  r82col_print_part ( n, v, max_print, '  Output with MAX_print = 5' )

  max_print = 25
  r82col_print_part ( n, v, max_print, '  Output with MAX_print = 25' )

  return

def r82row_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r82row_print_part() prints "part" of an R82ROW.
#
#  Discussion:
#
#    An R82ROW is a (2,N) array of R8's.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(2,N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g' % ( i, a[0,i], a[1,i] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g' % ( i, a[0,i], a[1,i] ) )
        print ( '  ....  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g' % ( i, a[0,i], a[1,i] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g' % ( i, a[0,i], a[1,i] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  ...more entries...' % ( i, a[0,i], a[1,i] ) )

  return

def r82row_print_part_test ( ):

#*****************************************************************************80
#
## r82row_print_part_test() tests r82row_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r82row_print_part_test():' )
  print ( '  r82row_print_part prints part of an R82ROW,' )
  print ( '  a real array of 2 rows.' )

  n = 10

  v = np.array ( [ \
    [  11,  12, 13, 14, 15, 16, 17, 18, 19, 20 ], \
    [  21,  22, 23, 24, 25, 26, 27, 28, 29, 30 ] ] )

  max_print = 2
  r82row_print_part ( n, v, max_print, '  Output with MAX_print = 2' )

  max_print = 5
  r82row_print_part ( n, v, max_print, '  Output with MAX_print = 5' )

  max_print = 25
  r82row_print_part ( n, v, max_print, '  Output with MAX_print = 25' )

  return

def r82vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r82vec_print_part() prints "part" of an R82VEC.
#
#  Discussion:
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2001
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(2,N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )
        print ( '  ....  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )
        i = max_print - 1
        print ( '  %4d  %14f  %14f  ...more entries...' % ( i, a[0,i], a[1,i] ) )

  return

def r82vec_print_part_test ( ):

#*****************************************************************************80
#
## r82vec_print_part_test() tests r82vec_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r82vec_print_part_test():' )
  print ( '  r82vec_print_part() prints an R8VEC.' )

  n = 10

  v = np.array ( [ \
    [  11,  12, 13, 14, 15, 16, 17, 18, 19, 20 ], \
    [  21,  22, 23, 24, 25, 26, 27, 28, 29, 30 ] ] )

  max_print = 2
  r82vec_print_part ( n, v, max_print, '  Output with MAX_print = 2' )

  max_print = 5
  r82vec_print_part ( n, v, max_print, '  Output with MAX_print = 5' )

  max_print = 25
  r82vec_print_part ( n, v, max_print, '  Output with MAX_print = 25' )

  return

def r83col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r83col_print_part() prints "part" of an R83COL.
#
#  Discussion:
#
#    An R83COL is a (3,N) array of R8's.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N,3), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        print ( '  ....  ..............  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  %14g  ...more entries...' \
          % ( i, a[i,0], a[i,1], a[i,2] ) )

  return

def r83col_print_part_test ( ):

#*****************************************************************************80
#
## r83col_print_part_test() tests r83col_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r83col_print_part_test():' )
  print ( '  r83col_print_part() prints part of an R83COL.' )

  n = 10

  v = np.array ( [ \
    [  11,  12,  13 ], \
    [  21,  22,  23 ], \
    [  31,  32,  33 ], \
    [  41,  42,  43 ], \
    [  51,  52,  53 ], \
    [  61,  62,  63 ], \
    [  71,  72,  73 ], \
    [  81,  82,  83 ], \
    [  91,  92,  93 ], \
    [ 101, 102, 103 ] ] )

  max_print = 2
  r83col_print_part ( n, v, max_print, '  Output with MAX_print = 2' )

  max_print = 5
  r83col_print_part ( n, v, max_print, '  Output with MAX_print = 5' )

  max_print = 25
  r83col_print_part ( n, v, max_print, '  Output with MAX_print = 25' )

  return

def r83row_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r83row_print_part() prints "part" of an R83ROW.
#
#  Discussion:
#
#    An R83ROW is a (3,N) array of R8's.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(3,N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[0,i], a[1,i], a[2,i] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[0,i], a[1,i], a[2,i] ) )
        print ( '  ....  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g  %14g' % ( i, a[0,i], a[1,i], a[2,i] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[0,i], a[1,i], a[2,i] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  %14g  ...more entries...' \
          % ( i, a[0,i], a[1,i], a[2,i] ) )

  return

def r83row_print_part_test ( ):

#*****************************************************************************80
#
## r83row_print_part_test() tests r83row_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r83row_print_part_test():' )
  print ( '  r83row_print_part() prints part of an R83ROW,' )
  print ( '  a real array of 3 rows.' )

  n = 10

  v = np.array ( [ \
    [  11,  12, 13, 14, 15, 16, 17, 18, 19, 20 ], \
    [  21,  22, 23, 24, 25, 26, 27, 28, 29, 30 ], \
    [  31,  32, 33, 34, 35, 36, 37, 38, 39, 40 ] ] )

  max_print = 2
  r83row_print_part ( n, v, max_print, '  Output with MAX_print = 2' )

  max_print = 5
  r83row_print_part ( n, v, max_print, '  Output with MAX_print = 5' )

  max_print = 25
  r83row_print_part ( n, v, max_print, '  Output with MAX_print = 25' )

  return

def r8_abs ( x ):

#*****************************************************************************80
#
## r8_abs() returns the absolute value of an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose absolute value is desired.
#
#  Output:
#
#    real VALUE, the absolute value of X.
#
  if ( 0.0 <= x ):
    value = + x
  else:
    value = - x

  return value

def r8_abs_test ( rng ):

#*****************************************************************************80
#
## r8_abs_test() tests r8_abs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  r8_lo = -5.0
  r8_hi = +5.0
  test_num = 10

  print ( '' )
  print ( 'r8_abs_test():' )
  print ( '  r8_abs() returns the absolute value of an R8.' )
  print ( '' )
  print ( '      X         r8_abs(X)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_uniform_ab ( r8_lo, r8_hi, rng )
    r8_absolute = r8_abs ( r8 )
    print ( '  %10.6f  %10.6f' % ( r8, r8_absolute ) )

  return

def r8_acosh ( x ):

#*****************************************************************************80
#
## r8_acosh() evaluates the arc-hyperbolic cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the arc-hyperbolic cosine of X.
#
  import numpy as np

  if ( x < 1.0 ):
    print ( '' )
    print ( 'r8_acosh - Fatal error!' )
    print ( '  X < 1.0' )
    raise Exception ( 'r8_acosh - Fatal error!' )

  r8_tiny = 1.0E-30
  xmax = 1.0 / np.sqrt ( r8_tiny )

  if ( x < xmax ):
    value = np.log ( x + np.sqrt ( x * x - 1.0 ) )
  else:
    dln2 = 0.69314718055994530941723212145818
    value = dln2 + np.log ( x )

  return value

def r8_acosh_test ( ):

#*****************************************************************************80
#
## r8_acosh_test() tests r8_acosh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_acosh_test():' )
  print ( '  r8_acosh() computes the arc-hyperbolic-cosine of an angle.' )
  print ( '' )
  print ( '       X            A=r8_ACOSH(X)    COSH(A)' )
  print ( '' )

  for test in range ( 0, 9 ):

    x = 1.0 + ( test ) / 2.0
    a = r8_acosh ( x )
    x2 = np.cosh ( a )

    print ( '  %14.6g  %14.6g  %14.6g' % ( x, a, x2 ) )

  return

def r8_acos ( c ):

#*****************************************************************************80
#
## r8_acos() computes the arc cosine function, with argument truncation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
#
#  Input:
#
#    real C, the argument.
#
#  Output:
#
#    real VALUE, the arc-cosine of C.
#
  import numpy as np

  c2 = max ( c,  - 1.0 )
  c2 = min ( c2, +1.0 )
  
  value = np.arccos ( c2 )

  return value

def r8_acos_test ( ):

#*****************************************************************************80
#
## r8_acos_test() tests r8_acos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r8_acos_test():' )
  print ( '  r8_acos computes the arc-cosine of an angle.' )
  print ( '' )
  print ( '       C            r8_ACOS(C)        ACOS(C)' )
  print ( '' )

  for test in range ( -1, 14 ):

    c = float ( test - 6 ) / 6.0

    if ( -1.0 <= c and c <= 1.0 ):
      print ( '  %14.6g  %14.6g  %14.6g' % ( c, r8_acos ( c ), np.arccos ( c ) ) )
    else:
      print ( '  %14.6g  %14.6g' % ( c, r8_acos ( c ) ) )

  return

def r8_add ( x, y ):

#*****************************************************************************80
#
## r8_add() adds two R8's.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the numbers to be added.
#
#  Output:
#
#    real VALUE, the sum of X and Y.
#
  value = x + y

  return value

def r8_add_test ( rng ):

#*****************************************************************************80
#
## r8_add_test() tests r8_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_add_test():' )
  print ( '  r8_add adds two R8\'s.'  )
  print ( '' )
  print ( '       R1             R2              R3              R4' )
  print ( '                                      R1+R2     r8_ADD(R1,R2)' )
  print ( '' )

  r8_lo = - 500.0
  r8_hi = + 500.0

  for test in range ( 0, 5 ):

    r1 = r8_uniform_ab ( r8_lo, r8_hi, rng )
    r2 = r8_uniform_ab ( r8_lo, r8_hi, rng )
    r3 = r1 + r2
    r4 = r8_add ( r1, r2 )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( r1, r2, r3, r4 ) )

  return

def r8_agm ( a, b ):

#*****************************************************************************80
#
## r8_agm() computes the arithmetic-geometric mean of A and B.
#
#  Discussion:
#
#    The AGM is defined for nonnegative A and B.
#
#    The AGM of numbers A and B is defined by setting
#
#      A(0) = A,
#      B(0) = B
#
#      A(N+1) = ( A(N) + B(N) ) / 2
#      B(N+1) = sqrt ( A(N) * B(N) )
#
#    The two sequences both converge to AGM(A,B).
#
#    In Mathematica, the AGM can be evaluated by
#
#      ArithmeticGeometricMean [ a, b ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    real A, B, the arguments whose AGM is to be computed.
#    0 <= A, 0 <= B.
#
#  Output:
#
#    real VALUE, the arithmetic-geometric mean of A and B.
#
  import numpy as np

  it_max = 1000

  if ( a < 0.0 ):
    print ( '' )
    print ( 'r8_AGM - Fatal error!' )
    print ( '  Argument A < 0.' )
    raise Exception ( 'r8_AGM - Fatal error!' )

  if ( b < 0.0 ):
    print ( '' )
    print ( 'r8_AGM - Fatal error!' )
    print ( '  Argument B < 0.' )
    raise Exception ( 'r8_AGM - Fatal error!' )

  if ( a == 0.0 or b == 0.0 ):
    value = 0.0
    return value

  if ( a == b ):
    value = a
    return value

  it = 0
  tol = 100.0 * r8_epsilon ( )

  a1 = a
  b1 = b

  while ( True ):

    it = it + 1

    a2 = ( a1 + b1 ) / 2.0
    b2 = np.sqrt ( a1 * b1 )

    if ( abs ( a2 - b2 ) <= tol * ( a2 + b2 ) ):
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'r8_AGM - Warning!' )
      print ( '  No convergence.' )
      break

    a1 = a2
    b1 = b2

  value = a2

  return value

def r8_agm_test ( ):

#*****************************************************************************80
#
## r8_agm_test() tests r8_agm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_agm_test():' )
  print ( '  r8_agm() computes the arithmetic geometric mean.' )
  print ( '' )
  print ( '             X              Y              AGM           AGM' )
  print ( '                                           Exact         Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, fx1 = agm_values ( n_data )

    if ( n_data == 0 ):
      break
 
    fx2 = r8_agm ( x, y )

    print ( '  %14.6f  %14.6f  %24.16g  %24.16g' % ( x, y, fx1, fx2 ) )

  return

def r8_aint ( x ):

#****************************************************************************80
#
## r8_aint() truncates an R8 argument to an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the truncated version of X.
#
  if ( x < 0.0 ):
    value = - int ( abs ( x ) )
  else:
    value =   int ( abs ( x ) )

  return value

def r8_aint_test ( rng ):

#*****************************************************************************80
#
## r8_aint_test() tests r8_aint().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_aint_test():' )
  print ( '  r8_aint truncates a real number to its integer part.' )
  print ( '' )
  print ( '        X           r8_AINT(X)' )
  print ( '' )

  for test in range ( 1, 11 ):
    x = r8_uniform_ab ( -10.0, +10.0, rng )
    x2 = r8_aint ( x )
    print ( '  %12f  %12f' % ( x, x2 ) )

  return

def r8_asinh ( x ):

#*****************************************************************************80
#
## r8_asinh() returns the inverse hyperbolic sine of a number.
#
#  Definition:
#
#    The assertion that:
#
#      Y = ASINH2(X)
#
#    implies that
#
#      X = SINH(Y) = 0.5 * ( EXP(Y) - EXP(-Y) ).
#
#  Discussion:
#
#    Since a library function ASINH may be available on some systems,
#    this routine is named ASINH2 to avoid name conflicts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose inverse hyperbolic sine is desired.
#
#  Output:
#
#    real VALUE, the inverse hyperbolic sine of X.
#
  import numpy as np

  value = np.log ( x + np.sqrt ( x * x + 1.0 ) )

  return value

def r8_asinh_test ( ):

#*****************************************************************************80
#
## r8_asinh_test() tests r8_asinh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_asinh_test():' )
  print ( '  r8_asinh() computes the inverse hyperbolic sine.' )
  print ( '' )
  print ( '        x           r8_asinh(x)   sinh(r8_sinh(x))' )
  print ( '' )

  for i in range ( 0, 10 ):
    x = 1.0 + i / 5.0
    a = r8_asinh ( x )
    x2 = np.sinh ( a )
    print ( '  %12f  %12f  %12f' % ( x, a, x2 ) )

  return

def r8_asin ( s ):

#*****************************************************************************80
#
## r8_asin() computes the arc sine function, with argument truncation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    This version by John Burkardt.
#
#  Input:
#
#    real S, the argument.
#
#  Output:
#
#    real VALUE, the arc-sine of S.
#
  import numpy as np
 
  s2 = max ( s,  - 1.0 )
  s2 = min ( s2, +1.0 )
  
  value = np.arcsin ( s2 )

  return value

def r8_asin_test ( ):

#*****************************************************************************80
#
## r8_asin_test() tests r8_asin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_asin_test():' )
  print ( '  r8_asin computes the arc-sine of an angle.' )
  print ( '' )
  print ( '       S            r8_ASIN(S)        ARCSIN(S)' )
  print ( '' )

  for test in range ( -1, 14 ):

    s = float ( test - 6 ) / 6.0

    if ( -1.0 <= s and s <= 1.0 ):
      print ( '  %14.6g  %14.6g  %14.6g' % ( s, r8_asin ( s ), np.arcsin ( s ) ) )
    else:
      print ( '  %14.6g  %14.6g' % ( s, r8_asin ( s ) ) )

  return

def r8_atanh ( x ):

#*****************************************************************************80
#
## r8_atanh() returns the inverse hyperbolic tangent of a number.
#
#  Discussion:
#
#    Y = r8_ATANH ( X )
#
#    implies that
#
#    X = TANH(Y) = ( EXP(Y) - EXP(-Y) ) / ( EXP(Y) + EXP(-Y) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose inverse hyperbolic
#    tangent is desired.  The absolute value of X should be less than
#    or equal to 1.
#
#  Output:
#
#    real VALUE, the inverse hyperbolic tangent of X.
#
  import numpy as np

  if ( 1.0 <= abs ( x ) ):
    print ( '' )
    print ( 'r8_atanh - Fatal error!' )
    print ( '  ABS(X) must be < 1.' )
    print ( '  Your input is X = %f' % ( x ) )
    raise Exception ( 'r8_ATANH - Fatal error!' )

  value = 0.5 * np.log ( ( 1.0 + x ) / ( 1.0 - x ) )

  return value

def r8_atanh_test ( ):

#*****************************************************************************80
#
## r8_atanh_test() tests r8_atanh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_atanh_test():' )
  print ( '  r8_atanh computes the inverse hyperbolic tangent.' )
  print ( '' )
  print ( '        X           r8_ATANH(X)   TANH(r8_TANH(X))' )
  print ( '' )

  for i in range ( -2, 10 ):
    x = i / 10.0
    a = r8_atanh ( x )
    x2 = np.tanh ( a )
    print ( '  %12f  %12f  %12f' % ( x, a, x2 ) )

  return

def r8_atan ( y, x ):

#*****************************************************************************80
#
## r8_atan() computes the inverse tangent of the ratio Y / X.
#
#  Discussion:
#
#    r8_ATAN returns an angle whose tangent is ( Y / X ), a job which
#    the built in functions ATAN and ATAN2 already do.
#
#    However:
#
#    * r8_ATAN always returns a positive angle, between 0 and 2 PI,
#      while ATAN and ATAN2 return angles in the interval [-PI/2,+PI/2]
#      and [-PI,+PI] respectively;
#
#    * r8_ATAN accounts for the signs of X and Y, (as does ATAN2).  The ATAN
#     function by contrast always returns an angle in the first or fourth
#     quadrants.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 October 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y, X, two quantities which represent the tangent of
#    an angle.  If Y is not zero, then the tangent is (Y/X).
#
#  Output:
#
#    real VALUE, an angle between 0 and 2 * PI, whose tangent is
#    (Y/X), and which lies in the appropriate quadrant so that the signs
#    of its cosine and sine match those of X and Y.
#
  import numpy as np
#
#  Special cases:
#
  if ( x == 0.0 ):

    if ( 0.0 < y ):
      value = np.pi / 2.0
    elif ( y < 0.0 ):
      value = 3.0 * np.pi / 2.0
    elif ( y == 0.0 ):
      value = 0.0

  elif ( y == 0.0 ):

    if ( 0.0 < x ):
      value = 0.0
    elif ( x < 0.0 ):
      value = np.pi
#
#  We assume that ATAN2 is correct when both arguments are positive.
#
  else:

    abs_y = abs ( y )
    abs_x = abs ( x )

    theta_0 = np.arctan2 ( abs_y, abs_x )

    if ( 0.0 < x and 0.0 < y ):
      value = theta_0
    elif ( x < 0.0 and 0.0 < y ):
      value = np.pi - theta_0
    elif ( x < 0.0 and y < 0.0 ):
      value = np.pi + theta_0
    elif ( 0.0 < x and y < 0.0 ):
      value = 2.0 * np.pi - theta_0

  return value

def r8_atan_test ( ):

#*****************************************************************************80
#
## r8_atan_test() tests r8_atan().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 8

  xtest = np.array ( [ 1.0, 1.0, 0.0, -1.0, -1.0, -1.0,  0.0,  1.0 ] )
  ytest = np.array ( [ 0.0, 1.0, 1.0,  1.0,  0.0, -1.0, -1.0, -1.0 ] )

  print ( '' )
  print ( 'r8_atan_test():' )
  print ( '  r8_atan computes the arc-tangent given Y and X;' )
  print ( '  ATAN2 is the system version of this routine.' )
  print ( '' )
  print ( '  X     Y     ATAN2(Y,X)   r8_ATAN(Y,X)' )
  print ( '' )

  for i in range ( 0, ntest ):
    x = xtest[i]
    y = ytest[i]
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, np.arctan2 ( y, x ), r8_atan ( y, x ) ) )

  return

def r8_big ( ):

#*****************************************************************************80
#
## r8_big() returns a "big" real number.
#
#  Discussion:
#
#    The value returned by this function is NOT required to be the
#    maximum representable R8.
#    We simply want a "very large" but non-infinite number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, a huge number.
#
  value = 1.0E+30

  return value

def r8_big_test ( ):

#*****************************************************************************80
#
## r8_big_test() tests r8_big().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_big_test():' )
  print ( '  r8_big() returns a "big" R8;' )
  print ( '' )
  print ( '    r8_big =  %g' % ( r8_big ( ) ) )

  return

def r8block_print ( l, m, n, a, title ):

#*****************************************************************************80
#
## r8block_print() prints an R8BLOCK
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L, M, N, the dimensions of the block.
#
#    real A(L,M,N), the array to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( '%s' % ( title ) )

  for k in range ( 0, n ):

    print ( '' )
    print ( '  K = %d' % ( k ) )

    for jlo in range ( 0, m, 5 ):
      jhi = min ( jlo + 5, m )
      print ( '' )
      print ( '      ', end = '' )
      for j in range ( jlo, jhi ):
        print ( '       %7d' % ( j ), end = '' )
      print ( '' )
      print ( '' )
      for i in range ( 0, l ):
        print ( '%5d:' % ( i ), end = '' )
        for j in range ( jlo, jhi ):
          print ( '  %12g' % ( a[i,j,k] ), end = '' )
        print ( '' )

  return

def r8block_print_test ( ):

#*****************************************************************************80
#
## r8block_print_test() tests r8block_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  l = 4
  m = 3
  n = 2

  x = np.array ( [ \
        [  [  1.0,   2.0 ], [  1.0,  2.0 ], [  1.0,   2.0 ] ], \
        [  [  2.0,   4.0 ], [  4.0,  8.0 ], [  8.0,  16.0 ] ], \
        [  [  3.0,   6.0 ], [  9.0, 18.0 ], [ 27.0,  54.0 ] ], \
        [  [  4.0,   8.0 ], [ 16.0, 32.0 ], [ 64.0, 128.0 ] ] ] )

  print ( '' )
  print ( 'r8block_print_test():' )
  print ( '  r8block_print() prints an R8BLOCK.' )

  r8block_print ( l, m, n, x, '  The 3D array:' )

  return

def r8_cas ( x ):

#*****************************************************************************80
#
## r8_cas() returns the "casine" of a number.
#
#  Definition:
#
#    The "casine", used in the discrete Hartley transform, is abbreviated
#    CAS(X), and defined by:
#
#      CAS(X) = cos ( X ) + sin( X )
#             = sqrt ( 2 ) * sin ( X + pi/4 )
#             = sqrt ( 2 ) * cos ( X - pi/4 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose casine is desired.
#
#  Output:
#
#    real VALUE, the casine of X, which will be between
#    plus or minus the square root of 2.
#
  import numpy as np

  value = np.cos ( x ) + np.sin ( x )

  return value

def r8_cas_test ( ):

#*****************************************************************************80
#
## r8_cas_test() tests r8_cas().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 12

  print ( '' )
  print ( 'r8_cas_test():' )
  print ( '  r8_cas() evaluates the casine of a number.' )
  print ( '' )
  print ( '	X	   r8_cas ( X )' )
  print ( '' )
  for test in range ( 0, test_num + 1 ):
    x = np.pi * float ( test ) / float ( test_num )
    print ( '  %14f  %14f' % ( x, r8_cas ( x ) ) )

  return

def r8_ceiling ( x ):

#*****************************************************************************80
#
## r8_ceiling() rounds an R8 up to the nearest integral R8.
#
#  Example:
#
#    X         Value
#
#   -1.1      -1.0
#   -1.0      -1.0
#   -0.9       0.0
#   -0.1       0.0
#    0.0       0.0
#    0.1       1.0
#    0.9       1.0
#    1.0       1.0
#    1.1       2.0
#    2.9       3.0
#    3.0       3.0
#    3.14159   4.0
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number to be rounded up.
#
#  Output:
#
#    real VALUE, the rounded value of X.
#
  import numpy as np

  value = np.ceil ( x )

  return value

def r8_ceiling_test ( ):

#*****************************************************************************80
#
## r8_ceiling_test() tests r8_ceiling().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_ceiling_test():' )
  print ( '  r8_ceiling() rounds a value up.' )
  print ( '' )
  print ( '       X       r8_ceiling(X)' )
  print ( '' )

  for i in range ( -6, 7 ):
    rval = float ( i ) / 5.0
    ival = r8_ceiling ( rval )
    print ( '  %14f  %8d' % ( rval, ival ) )

  return

def r8_choose ( n, k ):

#*****************************************************************************80
#
## r8_choose() computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, K, are the values of N and K.
#
#  Output:
#
#    real VALUE, the number of combinations of N things taken K at a time.
#
  import numpy as np
  from scipy.special import gammaln

  if ( n < 0 ):

    value = 0.0

  elif ( k == 0 ):

    value = 1.0

  elif ( k == 1 ):

    value = float ( n )

  elif ( 1 < k and k < n - 1 ):

    facn = gammaln ( float ( n + 1 ) )
    fack = gammaln ( float ( k + 1 ) )
    facnmk = gammaln ( float ( n - k + 1 ) )

    value = round ( np.exp ( facn - fack - facnmk ) )

  elif ( k == n - 1 ):

    value = float ( n )

  elif ( k == n ):

    value = 1.0

  else:

    value = 0.0

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## r8_choose_test() tests r8_choose().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_choose_test():' )
  print ( '  r8_choose() evaluates C(N,K).' )
  print ( '' )
  print ( '         N         K       CNK' )
 
  for n in range ( 0, 6 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print ( '  %8d  %8d  %14.6g' % ( n, k, cnk ) )

  return

def r8_chop ( place, x ):

#*****************************************************************************80
#
## r8_chop() chops an R8 to a given number of binary places.
#
#  Example:
#
#    3.875 = 2 + 1 + 1/2 + 1/4 + 1/8.
#
#    The following values would be returned for the 'chopped' value of
#    3.875:
#
#    PLACE  Value
#
#       1      2
#       2      3     = 2 + 1
#       3      3.5   = 2 + 1 + 1/2
#       4      3.75  = 2 + 1 + 1/2 + 1/4
#       5+     3.875 = 2 + 1 + 1/2 + 1/4 + 1/8
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PLACE, the number of binary places to preserve.
#    PLACE = 0 means return the integer part of X.
#    PLACE = 1 means return the value of X, correct to 1/2.
#    PLACE = 2 means return the value of X, correct to 1/4.
#    PLACE = -1 means return the value of X, correct to 2.
#
#    real X, the number to be chopped.
#
#  Output:
#
#    real VALUE, the chopped number.
#
  s = r8_sign ( x )
  x = abs ( x )
  temp = int ( r8_log_2 ( x ) )
  fac = 2.0 ** ( temp - place + 1 )
  value = s * ( int ( x / fac ) ) * fac

  return value

def r8_chop_test ( ):

#*****************************************************************************80
#
## r8_chop_test() tests r8_chop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_chop_test():' )
  print ( '  r8_chop() chops an R8 to IPLACE places' )
  print ( '' )
  print ( ' PLACE           X         r8_chop' )
  print ( '' )

  x = np.pi

  for place in range ( 0, 33 ):
    print ( '  %4d  %24.16g  %24.16g' % ( place, x, r8_chop ( place, x )  ) )

  return

def r8col_flip ( m, n, a ):

#*****************************************************************************80
#
## r8col_flip() flips the entries in each column of an R8COL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real B(M,N), the flipped array.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[i,j] = a[m-1-i,j]

  return b

def r8col_flip_test ( rng ):

#*****************************************************************************80
#
## r8col_flip_test() tests r8col_flip().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8col_flip_test():' )
  print ( '  r8col_flip() flips the columns of an R8COL.' )

  m = 5
  n = 4
  a = rng.random ( size = [ m, n ] )

  r8mat_print ( m, n, a, '  Matrix A:' )

  b = r8col_flip ( m, n, a )

  r8mat_print ( m, n, b, '  Matrix after column flipping:' )

  return

def r8col_normalize_li ( m, n, a ):

#*****************************************************************************80
#
## r8col_normalize_li() normalizes an R8COL with the column infinity norm.
#
#  Discussion:
#
#    Each column is scaled so that the entry of maximum norm has the value 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real B(M,N), the normalize array.
#
  import numpy as np

  b = a.copy ( )

  for j in range ( 0, n ):

    c = a[0,j]
    for i in range ( 1, m ):
      if ( abs ( c ) < abs ( a[i,j] ) ):
        c = a[i,j]

    if ( c != 0.0 ):
      b[0:m,j] = b[0:m,j] / c

  return b

def r8col_normalize_li_test ( rng ):

#*****************************************************************************80
#
## r8col_normalize_li_test() tests r8col_normalize_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8col_normalize_li_test():' )
  print ( '  r8col_normalize_li() normalizes an array A, dividing each' )
  print ( '  column by its maximum element.' )

  m = 5
  n = 4
  a = rng.random ( size = [ m, n ] )

  r8mat_print ( m, n, a, '  Matrix A:' )

  b = r8col_normalize_li ( m, n, a )

  r8mat_print ( m, n, b, '  Matrix after column LI normalization:' )

  return

def r8col_swap ( m, n, a, j1, j2 ):

#*****************************************************************************80
#
## r8col_swap() swaps two columns of an R8COL.
#
#  Example:
#
#    Input:
#
#      M = 3, N = 4, I = 2, J = 4
#
#      A = (
#        1  2  3  4
#        5  6  7  8
#        9 10 11 12 )
#
#    Output:
#
#      A = (
#        1  4  3  2
#        5  8  7  6
#        9 12 11 10 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M,N), an array of N columns of length M.
#
#    integer J1, J2, the columns to be swapped.
#
#  Output:
#
#    real A(M,N), the array, with columns swapped.
#
  if ( j1 < 0 or n <= j1 or j2 < 0 or n <= j2 ):
    print ( '' )
    print ( 'r8col_swap - Fatal error!' )
    print ( '  J1 or J2 is out of bounds.' )
    print ( '  J1 =   %d' % ( j1 ) )
    print ( '  J2 =   %d' % ( j2 ) )
    print ( '  N =    %d' % ( n ) )
    raise Exception ( 'r8col_swap - Fatal error!' )

  if ( j1 == j2 ):
    return

  for i in range ( 0, m ):
    t       = a[i,j1]
    a[i,j1] = a[i,j2]
    a[i,j2] = t

  return a

def r8col_swap_test ( ):

#*****************************************************************************80
#
## r8col_swap_test() tests r8col_swap();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_swap_test():' )
  print ( '  r8col_swap() swaps two columns of an R8COL.' )

  a = r8mat_indicator ( m, n )

  r8mat_print ( m, n, a, '  The array:' )

  icol1 = 0
  icol2 = 2

  print ( '' )
  print ( '  Swap columns %d and %d' % ( icol1, icol2 ) )

  a = r8col_swap ( m, n, a, icol1, icol2 )

  r8mat_print ( m, n, a, '  The updated matrix:' )

  return

def r8col_uniform_abvec ( m, n, a, b, rng ):

#*****************************************************************************80
#
## r8col_uniform_abvec() returns a random matrix with row ranges.
#
#  Discussion:
#
#    An R8COL is an array of R8 values, regarded as a set of column vectors.
#
#    The user specifies a minimum and maximum value for each row.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in
#    the array.
#
#    real A(M), B(M), the lower and upper limits.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R(M,N), the array of pseudorandom values.
#
  import numpy as np

  r = rng.random ( size = [ m, n ] )

  for i in range ( 0, m ):
    r[i,0:n] = a[i] + ( b[i] - a[i] ) * r[i,0:n]

  return r

def r8col_uniform_abvec_test ( rng ):

#*****************************************************************************80
#
## r8col_uniform_abvec_test() tests r8col_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0, 17.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1, 20.0 ) )

  print ( '' )
  print ( 'r8col_uniform_abvec_test():' )
  print ( '  r8col_uniform_abvec() computes a random scaled R8COL.' )
  print ( '' )
  print ( '   Col         Min         Max' )
  print ( '' )

  for i in range ( 0, m ):
    print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

  v = r8col_uniform_abvec ( m, n, a, b, rng )

  r8mat_print ( m, n, v, '  Random R8COL:' )

  return

def r8_cosd ( degrees ):

#*****************************************************************************80
#
## r8_cosd() returns the cosine of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DEGREES, the angle in degrees.
#
#  Output:
#
#    real VALUE, the cosine of the angle.
#
  import numpy as np

  radians = np.pi * ( degrees / 180.0 )

  value = np.cos ( radians )

  return value

def r8_cosd_test ( ):

#*****************************************************************************80
#
## r8_cosd_test() tests r8_cosd().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_cosd_test():' )
  print ( '  r8_cosd() computes the cosine of an angle' )
  print ( '  given in degrees.' )
  print ( '' )
  print ( '  ANGLE    r8_cosd(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    print ( '  %8.2f  %14.6g' % ( angle, r8_cosd ( angle ) ) )

  return

def r8_cotd ( degrees ):

#*****************************************************************************80
#
## r8_cotd() returns the cotangent of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DEGREES, the angle in degrees.
#
#  Output:
#
#    real VALUE, the cotangent of the angle.
#
  import numpy as np

  radians = np.pi * ( degrees / 180.0 )

  value = np.cos ( radians ) / np.sin ( radians )

  return value

def r8_cotd_test ( ):

#*****************************************************************************80
#
## r8_cotd_test() tests r8_cotd().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_cotd_test():' )
  print ( '  r8_cotd() computes the cotangent of an angle' )
  print ( '  given in degrees.' )
  print ( '' )
  print ( '  ANGLE    r8_cotd(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( i % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_cotd ( angle ) ) )

  return

def r8_cscd ( degrees ):

#*****************************************************************************80
#
## r8_cscd() returns the cosecant of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DEGREES, the angle in degrees.
#
#  Output:
#
#    real VALUE, the cosecant of the angle.
#
  import numpy as np

  radians = np.pi * ( degrees / 180.0 )

  value = 1.0 / np.sin ( radians )

  return value

def r8_cscd_test ( ):

#*****************************************************************************80
#
## r8_cscd_test() tests r8_cscd().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_cscd_test():' )
  print ( '  r8_cscd() computes the cosecant of an angle' )
  print ( '  given in degrees.' )
  print ( '' )
  print ( '  ANGLE    r8_cscd(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( i % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_cscd ( angle ) ) )

  return

def r8_csc ( theta ):

#*****************************************************************************80
#
## r8_csc() returns the cosecant of X.
#
#  Discussion:
#
#    r8_csc ( THETA ) = 1.0 / SIN ( THETA )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real THETA, the angle, in radians, whose cosecant is desired.
#    It must be the case that SIN ( THETA ) is not zero.
#
#  Output:
#
#    real VALUE, the cosecant of THETA.
#
  import numpy as np

  value = np.sin ( theta )

  if ( value == 0.0 ):
    print ( '' )
    print ( 'r8_csc - Fatal error!' )
    print ( '  Cosecant undefined for THETA = %g' % ( theta ) )
    raise Exception ( 'r8_csc - Fatal error!' )

  value = 1.0 / value

  return value

def r8_csc_test ( ):

#*****************************************************************************80
#
## r8_csc_test() tests r8_csc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_csc_test():' )
  print ( '  r8_csc() computes the cosecant of an angle.' )
  print ( '' )
  print ( '  ANGLE    r8_csc(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    r = angle / 2.0 / np.pi
    if ( ( i % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_csc ( r ) ) )

  return

def r8_cube_root ( x ):

#*****************************************************************************80
#
## r8_cube_root() returns the cube root of an R8.
#
#  Discussion:
#
#    This routine is designed to avoid the possible problems that can occur
#    when formulas like 0.0^(1/3) or (-1.0)^(1/3) are to be evaluated.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose cube root is desired.
#
#  Output:
#
#    real VALUE, the cube root of X.
#
  if ( 0.0 < x ):
    value = x ** ( 1.0 / 3.0 )
  elif ( x == 0.0 ):
    value = 0.0;
  else:
    value = - ( abs ( x ) ) ** ( 1.0 / 3.0 )

  return value

def r8_cube_root_test ( rng ):

#*****************************************************************************80
#
## r8_cube_root_test() tests r8_cube_root().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_cube_root_test():' )
  print ( '  r8_cube_root() computes the cube root of an R8.' )
  print ( '' )
  print ( '       X               Y               Y^3' )
  print ( '' )

  a = -10.0
  b = +10.0

  for i in range ( 0, 10 ):
    x1 = r8_uniform_ab ( a, b, rng )
    y = r8_cube_root ( x1 )
    x2 = y ** 3
    print ( '  %14.6g  %14.6g  %14.6g' % ( x1, y, x2 ) )

  return

def r8_degrees ( radians ):

#*****************************************************************************80
#
## r8_degrees() converts an angle from radian to degree measure.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real RADIANS, the angle measurement in radians.
#
#  Output:
#
#    real VALUE, the angle measurement in degrees.
#
  import numpy as np

  value = radians * 180.0 / np.pi

  return value

def r8_degrees_test ( ):

#*****************************************************************************80
#
## r8_degrees_test() tests r8_degrees().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 12

  print ( '' )
  print ( 'r8_degrees_test():' )
  print ( '  r8_degrees() converts an angle from radians to degrees..' )
  print ( '' )
  print ( '	 Radians         Degrees' )
  print ( '' )

  for test in range ( 0, 13 ):
    r = np.pi * test / 12
    d = r8_degrees ( r )
    print ( '  %14f  %14f' % ( r, d ) )

  return

def r8_diff ( x, y, n ):

#*****************************************************************************80
#
## r8_diff() computes (X-Y) to a specified accuracy.
#
#  Discussion:
#
#    The user controls how many binary digits of accuracy
#    are to be used.
#
#    N determines the accuracy of the value of the result.  If N = 10,
#    for example, only 11 binary places will be used in the arithmetic.
#    In general, only N+1 binary places will be used.
#
#    N may be zero.  However, a negative value of N should
#    not be used, since this will cause both X and Y to look like 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the two values whose difference is desired.
#
#    integer N, the number of binary digits to use.
#
#  Output:
#
#    real VALUE, the value of X-Y.
#
  if ( x == y ):
    value = 0.0
    return value

  pow2 = 2.0 ** n
#
#  Compute the magnitude of X and Y, and take the larger of the
#  two.  At least one of the two values is not zero!
#
  size = max ( abs ( x ), abs ( y ) )
#
#  Make normalized copies of X and Y.  One of the two values will
#  actually be equal to 1.
#
  x = x / size
  y = y / size
#
#  Here's where rounding comes in.  We know that the larger of the
#  the two values equals 1.  We multiply both values by 2^N,
#  where N+1 is the number of binary digits of accuracy we want
#  to use, truncate the values, and divide back by 2^N.
#
  x = ( int ( x * pow2 + 0.5 * r8_sign ( x ) ) ) / pow2
  y = ( int ( y * pow2 + 0.5 * r8_sign ( y ) ) ) / pow2
#
#  Take the difference now.
#
  value = x - y
#
#  Undo the scaling.
#
  value = value * size

  return value

def r8_diff_test ( ):

#*****************************************************************************80
#
## r8_diff_test() tests r8_diff().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 15

  y_test = np.array ( [ \
    0.0625, 0.125, 0.25, 0.50,  0.874, \
    0.876,  0.90,  0.95, 0.99,  1.0, \
    1.01,   1.05,  1.10, 3.0,  10.0 ] )

  ndig = 3
  x = 1.0

  print ( '' )
  print ( 'r8_diff_test():' )
  print ( '  r8_diff() computes a difference X-Y to a given' )
  print ( '  number of binary places.' )
  print ( '' )
  print ( '  For this test, we use %d binary places.' % ( ndig ) )
  print ( '' )
  print ( '       X       Y       X-Y    r8_diff(X,Y)' )
  print ( '' )

  for test in range ( 0, test_num ):
    y = y_test[test]
    print ( '  %10f  %10f  %10f  %10f' % ( x, y, x - y, r8_diff ( x, y, ndig ) ) )

  return

def r8_digit ( x, idigit ):

#*****************************************************************************80
#
## r8_digit() returns a particular decimal digit of an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose NDIG-th decimal digit
#    is desired.  If X is zero, all digits will be returned as 0.
#
#    integer IDIGIT, the position of the desired decimal digit.
#    A value of 1 means the leading digit, a value of 2 the second digit
#    and so on.
#
#  Output:
#
#    integer DIGIT, the value of the IDIGIT-th decimal digit of X.
#
  if ( x == 0.0 ):
    digit = 0
    return digit

  if ( idigit <= 0 ):
    digit = 0
    return digit
#
#  Force X to lie between 1 and 10.
#
  x = abs ( x )

  while ( x < 1.0 ):
    x = x * 10.0

  while ( 10.0 <= x ):
    x = x / 10.0

  for i in range ( 0, idigit ):
    ival = int ( x )
    x = ( x - ival ) * 10.0

  digit = ival

  return digit

def r8_digit_test ( ):

#*****************************************************************************80
#
## r8_digit_test() tests r8_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  maxdig = 20

  r8_pi = 3.141592653589793
  x = r8_pi

  print ( '' )
  print ( 'r8_digit_test():' )
  print ( '  r8_digit() extracts decimal digits.' )
  print ( '' )
  print ( '  Here, we get digits of %g' % ( x ) )
  print ( '' )

  print ( '' )
  
  for idigit in range ( -1, maxdig + 1 ):
    print ( '%3d' % ( idigit ), end = '' )
  print ( '' )

  print ( '' )

  for idigit in range ( -2, maxdig + 1 ):
    digit = r8_digit ( x, idigit )
    print ( '%3d' % ( idigit ), end = '' )
  print ( '' )

  return

def r8_divide_i4 ( i, j ):

#*****************************************************************************80
#
## r8_divide_i4() returns an I4 fraction as an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the numerator and denominator.
#
#  Output:
#
#    real VALUE, the value of (I/J).
#
  value = float ( i ) / float ( j )

  return value

def r8_divide_i4_test ( ):

#*****************************************************************************80
#
## r8_divide_i4_test() tests r8_divide_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 12

  print ( '' )
  print ( 'r8_divide_i4_test():' )
  print ( '  r8_divide_i4() computes an integer ratio as a real number.' )
  print ( '' )
  print ( '     I     J    I/J  I//J  r8_divide_i4(I,J)' )
  print ( '' )
  for i in range ( - 3, 8 ):
    for j in range ( -2, 5 ):
      if ( j != 0 ):
        k = i / j
        l = i // j
        m = r8_divide_i4 ( i, j )
        print ( '  %4d  %4d  %4d  %4d  %g' % ( i, j, k, l, m ) )

  return

def r8_epsilon_compute ( ):

#*****************************************************************************80
#
## r8_epsilon_compute() returns the R8 roundoff unit.
#
#  Discussion:
#
#    The roundoff unit is a number R which is a power of 2 with the 
#    property that, to the precision of the computer's arithmetic,
#      1 < 1 + R
#    but 
#      1 = ( 1 + R / 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the roundoff unit.
#
  one = 1.0
  value = one
  temp = value / 2.0
  test = one + temp

  while ( one < test ):
    value = temp
    temp = value / 2.0
    test = one + temp

  return value

def r8_epsilon_compute_test ( ):

#*****************************************************************************80
#
## r8_epsilon_compute_test() tests r8_epsilon_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2012
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_epsilon_compute_test():' )
  print ( '  r8_epsilon_compute() computes the R8 roundoff unit.' )
  print ( '' )

  r = r8_epsilon_compute ( )
  print ( '  R = r8_epsilon_compute() = %e' % ( r ) )

  s = ( 1.0 + r ) - 1.0
  print ( '  ( 1 + R ) - 1            = %e' % ( s ) )

  s = ( 1.0 + ( r / 2.0 ) ) - 1.0
  print ( '  ( 1 + (R/2) ) - 1        = %e' % ( s ) )

  return

def r8_epsilon ( ):

#*****************************************************************************80
#
## r8_epsilon() returns the R8 roundoff unit.
#
#  Discussion:
#
#    The roundoff unit is a number R which is a power of 2 with the 
#    property that, to the precision of the computer's arithmetic,
#      1 < 1 + R
#    but 
#      1 = ( 1 + R / 2 )
#
#    In Python, you can get this value more directly by
#
#      import sys
#      eps = sys.float_info.epsilon
#
#    or:
#
#      np.finfo(float).eps
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the roundoff unit.
#
  value = 2.220446049250313E-016

  return value

def r8_epsilon_test ( ):

#*****************************************************************************80
#
## r8_epsilon_test() tests r8_epsilon().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2012
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_epsilon_test():' )
  print ( '  r8_epsilon() produces the R8 roundoff unit.' )
  print ( '' )

  r = r8_epsilon ( )
  print ( '  R = r8_epsilon()         = %e' % ( r ) )

  s = ( 1.0 + r ) - 1.0
  print ( '  ( 1 + R ) - 1            = %e' % ( s ) )

  s = ( 1.0 + ( r / 2.0 ) ) - 1.0
  print ( '  ( 1 + (R/2) ) - 1        = %e' % ( s ) )

  return

def r8_e ( ):

#*****************************************************************************80
#
## r8_e() returns the base of the natural logarithm system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the base of the natural logarithm system.
#
  value = 2.718281828459045235360287

  return value

def r8_e_test ( ):

#*****************************************************************************80
#
## r8_e_test() tests r8_e().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_e_test():' )
  print ( '  r8_e() returns the value of E.' )
  print ( '  Compare E to (1+1/n)^n' )
  value1 = r8_e ( )
  print ( '  r8_e = %g' % ( value1 ) )
  print ( '' )
  print ( '        N     Estimate      Error' )
  print ( '' )

  n = 1
  for i in range ( 0, 21 ):
    value2 = ( float ( n + 1 ) / float ( n ) ) ** n
    print ( '  %8d  %14.6g  %14.6g' % ( n, value2, abs ( value1 - value2 ) ) )
    n = n * 2

  return

def r8_exp ( x ):

#*****************************************************************************80
#
## r8_exp() computes the exponential function, avoiding overflow and underflow.
#
#  Discussion:
#
#    For arguments of very large magnitude, the evaluation of the
#    exponential function can cause computational problems.  Some languages
#    and compilers may return an infinite value or a "Not-a-Number".  
#    An alternative, when dealing with a wide range of inputs, is simply
#    to truncate the calculation for arguments whose magnitude is too large.
#    Whether this is the right or convenient approach depends on the problem
#    you are dealing with, and whether or not you really need accurate
#    results for large magnitude inputs, or you just want your code to
#    stop crashing.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the exponential function.
#
#  Output:
#
#    real VALUE, the value of exp ( X ).
#
  import numpy as np

  huge = np.finfo(float).max
  r8_log_max = +69.0776
  r8_log_min = -69.0776

  if ( x <= r8_log_min ):
    value = 0.0
  elif ( x < r8_log_max ):
    value = np.exp ( x )
  else:
    value = huge

  return value

def r8_exp_test ( ):

#*****************************************************************************80
#
## r8_exp_test() tests r8_exp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_exp_test():' )
  print ( '  r8_exp() returns the exponential of a real number.' )
  print ( '' )
  print ( '        X           r8_exp(X)' )
  print ( '' )

  for i in range ( -80, +90, 10 ):
    x = float ( i )
    print ( '  %12g  %12g' % ( x, r8_exp ( x ) ) )

  return

def r8_factorial2 ( n ):

#*****************************************************************************80
#
## r8_factorial2() computes the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the double factorial function.
#    If N is less than 1, VALUE is returned as 1.
#
#  Output:
#
#    real VALUE, the value of the double factorial of N.
#
  value = 1;

  if ( n < 1 ):
    return value

  while ( 1 < n ):
    value = value * n
    n = n - 2

  return value

def r8_factorial2_test ( ):

#*****************************************************************************80
#
## r8_factorial2_test() tests r8_factorial2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_factorial2_test():' )
  print ( '  r8_factorial2() evaluates the double factorial function.' )
  print ( '' )
  print ( '      N                     Exact                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial2 ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )

  return

def r8_factorial2_values ( n_data ):

#*****************************************************************************80
#
## r8_factorial2_values() returns values of the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#    In Mathematica, the function can be evaluated by:
#
#      n!!
#
#  Example:
#
#     N    N!!
#
#     0     1
#     1     1
#     2     2
#     3     3
#     4     8
#     5    15
#     6    48
#     7   105
#     8   384
#     9   945
#    10  3840
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, page 16.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    real F, the value of the function.
# 
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( 
          1.0, \
          1.0, \
          2.0, \
          3.0, \
          8.0, \
         15.0, \
         48.0, \
        105.0, \
        384.0, \
        945.0, \
       3840.0, \
      10395.0, \
      46080.0, \
     135135.0, \
     645120.0, \
    2027025.0 ) )

  n_vec = np.array ( ( 
    0, \
     1,  2,  3,  4,  5, \
     6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    f = 0.0
  else:
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, f

def r8_factorial2_values_test ( ):

#*****************************************************************************80
#
## r8_factorial2_values_test() tests r8_factorial2_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_factorial2_values_test():' )
  print ( '  r8_factorial2_values() returns values of the double factorial function.' )
  print ( '' )
  print ( '     N        N!!' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %14.6g' % ( n, f ) )

  return

def r8_factorial ( n ):

#*****************************************************************************80
#
## r8_factorial() returns N factorial.
#
#  Discussion:
#
#    factorial ( N ) = Product ( 1 <= I <= N ) I
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the function.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the factorial of N.
#
  if ( n < 0 ):
    print ( '' )
    print ( 'r8_factorial - Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'r8_factorial - Fatal error!' )

  value = 1.0

  for i in range ( 2, n + 1 ):
    value = value * i

  return value

def r8_factorial_test ( ):

#*****************************************************************************80
#
## r8_factorial_test() tests r8_factorial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_factorial_test():' )
  print ( '  r8_factorial() evaluates the factorial function.' )
  print ( '' )
  print ( '      N                     Exact                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )

  return

def r8_factorial_stirling ( n ):

#*****************************************************************************80
#
## r8_factorial_stirling() computes Stirling's approximation to N!.
#
#  Discussion:
#
#    N! = Product ( 1 <= I <= N ) I
#
#    Stirling ( N ) = sqrt ( 2 * PI * N ) * ( N / E )^N * E^(1/(12*N) )
#
#    This routine returns the raw approximation for all nonnegative
#    values of N.  If N is less than 0, the value is returned as 0,
#    and if N is 0, the value of 1 is returned.  In all other cases,
#    Stirling's formula is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the function.
#
#  Output:
#
#    real VALUE, an approximation to N!.
#
  import numpy as np

  r8_e = 2.71828182845904523

  if ( n < 0 ):

    value = 0.0

  elif ( n == 0 ):

    value = 1.0

  else:

    value = np.sqrt ( 2.0 * np.pi * n ) * ( n / r8_e ) ** n \
      * np.exp ( 1.0 / ( 12 * n ) )

  return value

def r8_factorial_stirling_test ( ):

#*****************************************************************************80
#
## r8_factorial_stirling_test() tests r8_factorial_stirling().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_factorial_stirling_test():' )
  print ( '  r8_factorial_stirling() computes Stirling\'s' )
  print ( '  approximate factorial function' )
  print ( '' )
  print ( '  N      Factorial    Factorial' )
  print ( '         Stirling' )
  print ( '' )

  f2 = 1.0
  for i in range ( 1, 21 ):
    f1 = r8_factorial_stirling ( i )
    f2 = f2 * i
    print ( '  %6d  %14g  %14g' % ( i, f1, f2 ) )

  return

def r8_factorial_values ( n_data ):

#*****************************************************************************80
#
## r8_factorial_values() returns values of the real factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) J
#
#    Although the factorial is an integer valued function, it quickly
#    becomes too large for an integer to hold.  This routine still accepts
#    an integer as the input argument, but returns the function value
#    as a real number.
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    real FN, the value of the function.
#
  import numpy as np

  n_max = 25

  fn_vec = np.array ( [ \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.6000000000000000E+01, \
     0.2400000000000000E+02, \
     0.1200000000000000E+03, \
     0.7200000000000000E+03, \
     0.5040000000000000E+04, \
     0.4032000000000000E+05, \
     0.3628800000000000E+06, \
     0.3628800000000000E+07, \
     0.3991680000000000E+08, \
     0.4790016000000000E+09, \
     0.6227020800000000E+10, \
     0.8717829120000000E+11, \
     0.1307674368000000E+13, \
     0.2092278988800000E+14, \
     0.3556874280960000E+15, \
     0.6402373705728000E+16, \
     0.1216451004088320E+18, \
     0.2432902008176640E+19, \
     0.1551121004333099E+26, \
     0.3041409320171338E+65, \
     0.9332621544394415E+158, \
     0.5713383956445855E+263 ] )

  n_vec = np.array ( [ \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def r8_factorial_values_test ( ):

#*****************************************************************************80
#
## r8_factorial_values_test() tests r8_factorial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_factorial_values_test():' )
  print ( '  r8_factorial_values() returns values of the real factorial function.' )
  print ( '' )
  print ( '          N          r8_factorial(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %14.6g' % ( n, fn ) )

  return

def r8_fall ( x, n ):

#*****************************************************************************80
#
## r8_fall() computes the falling factorial function [X]_N.
#
#  Discussion:
#
#    Note that the number of "injections" or 1-to-1 mappings from
#    a set of N elements to a set of M elements is [M]_N.
#
#    The number of permutations of N objects out of M is [M]_N.
#
#    Moreover, the Stirling numbers of the first kind can be used
#    to convert a falling factorial into a polynomial, as follows:
#
#      [X]_N = S^0_N + S^1_N * X + S^2_N * X^2 + ... + S^N_N X^N.
#
#  Formula:
#
#    [X]_N = X * ( X - 1 ) * ( X - 2 ) * ... * ( X - N + 1 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the falling factorial function.
#
#    integer N, the order of the falling factorial function.
#    If N = 0, FALL = 1, if N = 1, FALL = X.  Note that if N is
#    negative, a "rising" factorial will be computed.
#
#  Output:
#
#    real VALUE, the value of the falling factorial function.
#
  value = 1.0

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg - 1.0

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg + 1.0

  return value

def r8_fall_test ( ):

#*****************************************************************************80
#
## r8_fall_test() tests r8_fall().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_fall_test():' )
  print ( '  r8_fall() evaluates the falling factorial Fall(X,N).' )
  print ( '' )
  print ( '      X        N                     Exact                  Computed' )

  n_data = 0

  while ( True ):

    n_data, x, n, f1 = r8_fall_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_fall ( x, n )

    print ( '  %8.4g  %4d  %24.16g  %24.16g' % ( x, n, f1, f2 ) )

  return

def r8_fall_values ( n_data ):

#*****************************************************************************80
#
## r8_fall_values() returns values of the falling factorial function.
#
#  Discussion:
#
#    The definition of the falling factorial function is
#
#      (m)_n = (m)! / (m-n)!
#            = ( m ) * ( m - 1 ) * ( m - 2 ) \ * ( m - n + 1 )
#            = Gamma ( m + 1 ) / Gamma ( m - n + 1 )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      FactorialPower[m,n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, integer N, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( [ 
       120.0000000000000,  \
        163.1601562500000, \
        216.5625000000000, \
        281.6601562500000, \
        360.0000000000000, \
        1.000000000000000, \
        7.500000000000000, \
        48.75000000000000, \
        268.1250000000000, \
        1206.562500000000, \
        4222.968750000000, \
        10557.42187500000, \
        15836.13281250000, \
        7918.066406250000, \
        -3959.03320312500 ] )

  n_vec = np.array ( [ 
        4, \
        4, \
        4, \
        4, \
        4, \
        0, \
        1, \
        2, \
        3, \
        4, \
        5, \
        6, \
        7, \
        8, \
        9  ] )

  x_vec = np.array ( [ 
        5.00, \
        5.25, \
        5.50, \
        5.75, \
        6.00, \
        7.50, \
        7.50, \
        7.50, \
        7.50, \
        7.50, \
        7.50, \
        7.50, \
        7.50, \
        7.50, \
        7.50 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    n = 0
    f = 0.0
  else:
    x = x_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, n, f

def r8_fall_values_test ( ):

#*****************************************************************************80
#
## r8_fall_values_test() tests r8_fall_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_fall_values_test():' )
  print ( '  r8_fall_values() returns values of the falling factorial.' )
  print ( '' )
  print ( '          X         N          r8_fall(X,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, n, f = r8_fall_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8.4f  %8d  %24.16g' % ( x, n, f ) )

  return

def r8_floor ( x ):

#*****************************************************************************80
#
## r8_floor() rounds an R8 down to the nearest integral R8.
#
#  Example:
#
#    X         Value
#
#   -1.1      -2.0
#   -1.0      -1.0
#   -0.9      -1.0
#   -0.1      -1.0
#    0.0       0.0
#    0.1       0.0
#    0.9       0.0
#    1.0       1.0
#    1.1       1.0
#    2.9       2.0
#    3.0       3.0
#    3.14159   3.0
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number to be rounded down.
#
#  Output:
#
#    real VALUE, the rounded value of X.
#
  import numpy as np

  value = np.floor ( x )

  return value

def r8_floor_test ( rng ):

#*****************************************************************************80
#
## r8_floor_test() tests r8_floor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_floor_test():' )
  print ( '  r8_floor() returns the "floor" of a real number.' )
  print ( '' )
  print ( '        X           r8_floor(X)' )
  print ( '' )

  for test in range ( 1, 11 ):
    x = r8_uniform_ab ( -10.0, +10.0, rng )
    x2 = r8_floor ( x )
    print ( '  %12f  %12f' % ( x, x2 ) )

  return

def r8_fractional ( x ):

#*****************************************************************************80
#
## r8_fractional() returns the fractional part of an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the fractional part of X.
#
  value = abs ( x ) - int ( abs ( x ) )

  return value

def r8_fractional_test ( rng ):

#*****************************************************************************80
#
## r8_fractional_test() tests r8_fractional().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  r8_hi = 5.0
  r8_lo = -3.0
  test_num = 10

  print ( '' )
  print ( 'r8_fractional_test():' )
  print ( '  r8_fractional() returns the fractional part of an R8.' )
  print ( '' )
  print ( '       X       r8_fractional(X)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_uniform_ab ( r8_lo, r8_hi, rng )
    fractional = r8_fractional ( r8 )
    print ( '  %10f  %10f' % ( r8, fractional ) )

  return

def r8_fraction ( i, j ):

#*****************************************************************************80
#
## r8_fraction() uses real arithmetic on an integer ratio.
#
#  Discussion:
#
#    Given integer variables I and J, both FORTRAN and C will evaluate 
#    an expression such as "I/J" using what is called "integer division",
#    with the result being an integer.  It is often convenient to express
#    the parts of a fraction as integers but expect the result to be computed
#    using real arithmetic.  This function carries out that operation.
#
#  Example:
#
#       I     J   I/J  r8_fraction
#
#       1     2     0  0.5
#       7     4     1  1.75
#       8     4     2  2.00
#       9     4     2  2.25
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the arguments.
#
#  Output:
#
#    real VALUE, the value of the ratio.
#
  value = float ( i ) / float ( j )

  return value

def r8_fraction_test ( rng ):

#*****************************************************************************80
#
## r8_fraction_test() tests r8_fraction().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_fraction_test():' )
  print ( '  r8_fraction() computes a ratio of integers using real arithmetic.' )

  print ( '' )
  print ( '       I       J     I/J  r8_fraction(I,J)' )
  print ( '' )

  for i in range ( 0, 10 ):

    i1 = rng.integers ( low = 1, high = 20, endpoint = True )
    i2 = rng.integers ( low = 1, high = 20, endpoint = True )
    print ( '  %6d  %6d  %6d  %g' % ( i1, i2, i1 / i2, r8_fraction ( i1, i2 ) ) )
 
  return

def r8_gamma_log_int ( n ):

#*****************************************************************************80
#
## r8_gamma_log_int() computes the logarithm of Gamma of an integer N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the logarithm of the Gamma function.
#    0 < N.
#
#  Output:
#
#    real VALUE, the logarithm of the Gamma function of N.
#
  from scipy.special import gammaln

  if ( n <= 0 ):
    print ( '' )
    print ( 'r8_gamma_log_int - Fatal error!' )
    print ( '  Illegal input value of N = %d' % ( n ) )
    print ( '  But N must be strictly positive.' )
    raise Exception ( 'r8_gamma_log_int - Fatal error!' )

  value = gammaln ( float ( n ) )

  return value

def r8_gamma_log_int_test ( ):

#*****************************************************************************80
#
## r8_gamma_log_int_test() tests r8_gamma_log_int().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_gamma_log_int_test():' )
  print ( '  r8_gamma_log_int() evaluates the logarithm of the' )
  print ( '  gamma function for integer argument.' )

  print ( '' )
  print ( '       I    r8_gamma_log_int(I)' )
  print ( '' )

  for i in range ( 1, 21 ):
    g = r8_gamma_log_int ( i )
    print ( '  %6d  %14g' % ( i, g ) )

  return

def r8_gamma_log ( x ):

#*****************************************************************************80
#
## r8_gamma_log() evaluates the logarithm of the gamma function.
#
#  Discussion:
#
#    This routine calculates the LOG(GAMMA) function for a positive real
#    argument X.  Computation is based on an algorithm outlined in
#    references 1 and 2.  The program uses rational functions that
#    theoretically approximate LOG(GAMMA) to at least 18 significant
#    decimal digits.  The approximation for X > 12 is from reference
#    3, while approximations for X < 12.0 are similar to those in
#    reference 1, but are unpublished.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Cody, Kenneth Hillstrom,
#    Chebyshev Approximations for the Natural Logarithm of the
#    Gamma Function,
#    Mathematics of Computation,
#    Volume 21, Number 98, April 1967, pages 198-203.
#
#    Kenneth Hillstrom,
#    ANL/AMD Program ANLC366S, DGAMMA/DLGAMA,
#    May 1969.
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
#    Charles Mesztenyi, John Rice, Henry Thatcher,
#    Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968,
#    LC: QA297.C64.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

  c = np.array ( [ \
    -1.910444077728E-03, \
     8.4171387781295E-04, \
    -5.952379913043012E-04, \
     7.93650793500350248E-04, \
    -2.777777777777681622553E-03, \
     8.333333333333333331554247E-02, \
     5.7083835261E-03 ] )
  d1 = -5.772156649015328605195174E-01
  d2 = 4.227843350984671393993777E-01
  d4 = 1.791759469228055000094023E+00
  frtbig = 2.25E+76
  p1 = np.array ( [ \
    4.945235359296727046734888E+00, \
    2.018112620856775083915565E+02, \
    2.290838373831346393026739E+03, \
    1.131967205903380828685045E+04, \
    2.855724635671635335736389E+04, \
    3.848496228443793359990269E+04, \
    2.637748787624195437963534E+04, \
    7.225813979700288197698961E+03 ] )
  p2 = np.array ( [ \
    4.974607845568932035012064E+00, \
    5.424138599891070494101986E+02, \
    1.550693864978364947665077E+04, \
    1.847932904445632425417223E+05, \
    1.088204769468828767498470E+06, \
    3.338152967987029735917223E+06, \
    5.106661678927352456275255E+06, \
    3.074109054850539556250927E+06 ] )
  p4 = np.array ( [ \
    1.474502166059939948905062E+04, \
    2.426813369486704502836312E+06, \
    1.214755574045093227939592E+08, \
    2.663432449630976949898078E+09, \
    2.940378956634553899906876E+10, \
    1.702665737765398868392998E+11, \
    4.926125793377430887588120E+11, \
    5.606251856223951465078242E+11 ] )
  q1 = np.array ( [ \
    6.748212550303777196073036E+01, \
    1.113332393857199323513008E+03, \
    7.738757056935398733233834E+03, \
    2.763987074403340708898585E+04, \
    5.499310206226157329794414E+04, \
    6.161122180066002127833352E+04, \
    3.635127591501940507276287E+04, \
    8.785536302431013170870835E+03 ] )
  q2 = np.array ( [ \
    1.830328399370592604055942E+02, \
    7.765049321445005871323047E+03, \
    1.331903827966074194402448E+05, \
    1.136705821321969608938755E+06, \
    5.267964117437946917577538E+06, \
    1.346701454311101692290052E+07, \
    1.782736530353274213975932E+07, \
    9.533095591844353613395747E+06 ] )
  q4 = np.array ( [ \
    2.690530175870899333379843E+03, \
    6.393885654300092398984238E+05, \
    4.135599930241388052042842E+07, \
    1.120872109616147941376570E+09, \
    1.488613728678813811542398E+10, \
    1.016803586272438228077304E+11, \
    3.417476345507377132798597E+11, \
    4.463158187419713286462081E+11 ] )
  epsilon = np.finfo(float).eps
  sqrtpi = 0.9189385332046727417803297
  xbig = 2.55E+305
  xinf = 1.79E+308

  y = x

  if ( 0.0 < y and y <= xbig ):

    if ( y <= epsilon ):

      res = - np.log ( y )
#
#  EPS < X <= 1.5.
#
    elif ( y <= 1.5 ):

      if ( y < 0.6796875 ):
        corr = - np.log ( y );
        xm1 = y;
      else:
        corr = 0.0;
        xm1 = ( y - 0.5 ) - 0.5;

      if ( y <= 0.5 or 0.6796875 <= y ):

        xden = 1.0;
        xnum = 0.0;
        for i in range ( 0, 8 ):
          xnum = xnum * xm1 + p1[i]
          xden = xden * xm1 + q1[i]

        res = corr + ( xm1 * ( d1 + xm1 * ( xnum / xden ) ) )

      else:

        xm2 = ( y - 0.5 ) - 0.5
        xden = 1.0
        xnum = 0.0
        for i in range ( 0, 8 ):
          xnum = xnum * xm2 + p2[i]
          xden = xden * xm2 + q2[i]

        res = corr + xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  1.5 < X <= 4.0.
#
    elif ( y <= 4.0 ):

      xm2 = y - 2.0
      xden = 1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm2 + p2[i]
        xden = xden * xm2 + q2[i]

      res = xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  4.0 < X <= 12.0.
#
    elif ( y <= 12.0 ):

      xm4 = y - 4.0
      xden = -1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm4 + p4[i]
        xden = xden * xm4 + q4[i]

      res = d4 + xm4 * ( xnum / xden )
#
#  Evaluate for 12 <= argument.
#
    else:

      res = 0.0

      if ( y <= frtbig ):

        res = c[6]
        ysq = y * y

        for i in range ( 0, 6 ):
          res = res / ysq + c[i]

      res = res / y
      corr = np.log ( y )
      res = res + sqrtpi - 0.5 * corr
      res = res + y * ( corr - 1.0 )
#
#  Return for bad arguments.
#
  else:

    res = xinf

  return res

def r8_gamma_log_test ( ):

#*****************************************************************************80
#
## r8_gamma_log_test() tests r8_gamma_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_gamma_log_test():' )
  print ( '  r8_gamma_log() evaluates the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            gamma_log(X)    r8_gamma_log(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma_log ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8_gamma ( x ):

#*****************************************************************************80
#
## r8_gamma() evaluates Gamma(X) for a real argument.
#
#  Discussion:
#
#    This routine calculates the gamma function for a real argument X.
#
#    Computation is based on an algorithm outlined in reference 1.
#    The program uses rational functions that approximate the gamma
#    function to at least 20 significant decimal digits.  Coefficients
#    for the approximation over the interval (1,2) are unpublished.
#    Those for the approximation for 12 <= X are from reference 2.
#
#    PYTHON provides a GAMMA function, which is likely to be faster, and more
#    accurate.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Cody,
#    An Overview of Software Development for Special Functions,
#    in Numerical Analysis Dundee, 1975,
#    edited by GA Watson,
#    Lecture Notes in Mathematics 506,
#    Springer, 1976.
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
#    Charles Mesztenyi, John Rice, Henry Thatcher,
#    Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968,
#    LC: QA297.C64.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
#
#  Coefficients for minimax approximation over (12, INF).
#
  c = np.array ( [
   -1.910444077728E-03, \
    8.4171387781295E-04, \
   -5.952379913043012E-04, \
    7.93650793500350248E-04, \
   -2.777777777777681622553E-03, \
    8.333333333333333331554247E-02, \
    5.7083835261E-03 ] )
#
#  Mathematical constants
#
  sqrtpi = 0.9189385332046727417803297
#
#  Machine dependent parameters
#
  xbig = 171.624
  xminin = 2.23E-308
  eps = 2.22E-16
  xinf = 1.79E+308
#
#  Numerator and denominator coefficients for rational minimax
#  approximation over (1,2).
#
  p = np.array ( [ \
   -1.71618513886549492533811E+00, \
    2.47656508055759199108314E+01, \
   -3.79804256470945635097577E+02, \
    6.29331155312818442661052E+02, \
    8.66966202790413211295064E+02, \
   -3.14512729688483675254357E+04, \
   -3.61444134186911729807069E+04, \
    6.64561438202405440627855E+04 ] )

  q = np.array ( [ \
   -3.08402300119738975254353E+01, \
    3.15350626979604161529144E+02, \
   -1.01515636749021914166146E+03, \
   -3.10777167157231109440444E+03, \
    2.25381184209801510330112E+04, \
    4.75584627752788110767815E+03, \
   -1.34659959864969306392456E+05, \
   -1.15132259675553483497211E+05 ] )

  parity = 0
  fact = 1.0
  n = 0
  y = x
#
#  Argument is negative.
#
  if ( y <= 0.0 ):

    y = - x
    y1 = np.floor ( y )
    res = y - y1

    if ( res != 0.0 ):

      if ( y1 != np.floor ( y1 * 0.5 ) * 2.0 ):
        parity = 1

      fact = - np.pi / np.sin ( np.pi * res )
      y = y + 1.0

    else:

      res = xinf
      value = res
      return value
#
#  Argument is positive.
#
  if ( y < eps ):
#
#  Argument < EPS.
#
    if ( xminin <= y ):
      res = 1.0 / y
    else:
      res = xinf

    value = res
    return value

  elif ( y < 12.0 ):

    y1 = y
#
#  0.0 < argument < 1.0.
#
    if ( y < 1.0 ):

      z = y
      y = y + 1.0
#
#  1.0 < argument < 12.0.
#  Reduce argument if necessary.
#
    else:

      n = int ( np.floor ( y ) - 1 )
      y = y - n
      z = y - 1.0
#
#  Evaluate approximation for 1.0 < argument < 2.0.
#
    xnum = 0.0
    xden = 1.0
    for i in range ( 0, 8 ):
      xnum = ( xnum + p[i] ) * z
      xden = xden * z + q[i]

    res = xnum / xden + 1.0
#
#  Adjust result for case  0.0 < argument < 1.0.
#
    if ( y1 < y ):

      res = res / y1
#
#  Adjust result for case 2.0 < argument < 12.0.
#
    elif ( y < y1 ):

      for i in range ( 0, n ):
        res = res * y
        y = y + 1.0

  else:
#
#  Evaluate for 12.0 <= argument.
#
    if ( y <= xbig ):

      ysq = y * y
      sum = c[6]
      for i in range ( 0, 6 ):
        sum = sum / ysq + c[i]
      sum = sum / y - y + sqrtpi
      sum = sum + ( y - 0.5 ) * np.log ( y )
      res = np.exp ( sum )

    else:

      res = xinf
      value = res
      return value
#
#  Final adjustments and return.
#
  if ( parity ):
    res = - res

  if ( fact != 1.0 ):
    res = fact / res

  value = res

  return value

def r8_gamma_test ( ):

#*****************************************************************************80
#
## r8_gamma_test() tests r8_gamma().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_gamma_test():' )
  print ( '  r8_gamma() evaluates the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA(X)      r8_gamma(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8_heaviside ( x ):

#*****************************************************************************80
#
## r8_heaviside() evaluates the Heaviside function.
#
#  Discussion:
#
#    The Heaviside function is 0 for x < 0, 1 for x > 0, and 1/2 for x = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  if ( x < 0.0 ):
    value = 0.0
  elif ( x == 0.0 ):
    value = 0.5
  else:
    value = 1.0
  
  return value

def r8_heaviside_test ( ):

#*****************************************************************************80
#
## r8_heaviside_test() tests r8_heaviside().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_heaviside_test():' )
  print ( '  r8_heaviside() evaluates the Heaviside step function.' )
  print ( '' )
  print ( '             x  heaviside(x)' )
  print ( '' )

  for i in range ( -5, +6 ):
    x = float ( i ) / 5.0
    y = r8_heaviside ( x )
    
    print ( '  %12g  %12g' % ( x, y ) )

  return

def r8_huge ( ):

#*****************************************************************************80
#
## r8_huge() returns a "huge" real number.
#
#  Discussion:
#
#    The value returned by this function is intended to be the largest
#    representable real value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, a huge number.
#
  value = 1.79769313486231571E+308

  return value

def r8_huge_test ( ):

#*****************************************************************************80
#
## r8_huge_test() tests r8_huge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_huge_test():' )
  print ( '  r8_huge() returns a "huge" R8;' )
  print ( '' )
  print ( '    r8_huge = %g' % ( r8_huge ( ) ) )

  return

def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## r8_hyper_2f1() evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#    The F77 original version of this routine is copyrighted by
#    Shanjie Zhang and Jianming Jin.  However, they give permission to
#    incorporate this routine into a user program provided that the copyright
#    is acknowledged.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Input:
#
#    real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
  from scipy.special import gamma

  el = 0.5772156649015329

  l0 = ( c == int ( c ) ) and ( c < 0.0 )
  l1 = ( 1.0 - x < 1.0E-15 ) and ( c - a - b <= 0.0 )
  l2 = ( a == int ( a ) ) and ( a < 0.0 )
  l3 = ( b == int ( b ) ) and ( b < 0.0 )
  l4 = ( c - a == int ( c - a ) ) and ( c - a <= 0.0 )
  l5 = ( c - b == int ( c - b ) ) and ( c - b <= 0.0 )

  if ( l0 ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )

  if ( l1 ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  1 = X < 0, C - A - B <= 0.' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  X = %f' % ( x ) )

  if ( 0.95 < x ):
    eps = 1.0E-08
  else:
    eps = 1.0E-15

  if ( x == 0.0 or a == 0.0 or b == 0.0 ):

    value = 1.0
    return value

  elif ( 1.0 - x == eps and 0.0 < c - a - b ):

    gc = gamma ( c )
    gcab = gamma ( c - a - b )
    gca = gamma ( c - a )
    gcb = gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = gamma ( c )
    g2 = gamma ( 1.0 + a / 2.0 - b )
    g3 = gamma ( 0.5 + 0.5 * a )
    value = g0 * g1 / ( g2 * g3 )
    return value

  elif ( l2 or l3 ):

    if ( l2 ):
      nm = int ( abs ( a ) )

    if ( l3 ):
      nm = int ( abs ( b ) )

    value = 1.0
    r = 1.0

    for k in range ( 1, nm + 1 ):
      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r

    return value

  elif ( l4 or l5 ):

    if ( l4 ):
      nm = int ( abs ( c - a ) )
 
    if ( l5 ):
      nm = int ( abs ( c - b ) )

    value = 1.0
    r  = 1.0
    for k in range ( 1, nm + 1 ):
      r = r * ( c - a + float ( k ) - 1.0 ) * ( c - b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r
    value = ( 1.0 - x ) ** ( c - a - b ) * hf
    return value

  aa = a
  bb = b
  x1 = x

  if ( x < 0.0 ):
    x = x / ( x - 1.0 )
    if ( a < c and b < a and 0.0 < b ):
      a = bb
      b = aa
    b = c - b

  if ( 0.75 <= x ):

    gm = 0.0

    if ( abs ( c - a - b - int ( c - a - b ) ) < 1.0E-15 ):

      m = int ( c - a - b )
      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gam = gamma ( a + float ( m ) )
      gbm = gamma ( b + float ( m ) )

      pa = r8_psi ( a )
      pb = r8_psi ( b )

      if ( m != 0 ):
        gm = 1.0

      for j in range ( 1, abs ( m ) ):
        gm = gm * float ( j )

      rm = 1.0
      for j in range ( 1, abs ( m ) + 1 ):
        rm = rm * float ( j )
 
      f0 = 1.0
      r0 = 1.0
      r1 = 1.0
      sp0 = 0.0
      sp = 0.0

      if ( 0 <= m ):

        c0 = gm * gc / ( gam * gbm )
        c1 = - gc * ( x - 1.0 ) ** m / ( ga * gb * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0
 
        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / ( a + float ( k ) - 1.0 ) \
            + 1.0 / ( b + float ( k ) - 1.0 ) - 1.0 / float ( k )

        f1 = pa + pb + sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + ( 1.0 - a ) \
              / ( float ( j + k ) * ( a + float ( j + k ) - 1.0 ) ) \
              + 1.0 / ( b + float ( j + k ) - 1.0 )

          rp = pa + pb + 2.0 * el + sp + sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + m + float ( k ) - 1.0 ) * ( b + m + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break
 
          hw = f1

        value = f0 * c0 + f1 * c1

      elif ( m < 0 ):

        m = - m
        c0 = gm * gc / ( ga * gb * ( 1.0 - x ) ** m )
        c1 = - ( - 1 ) ** m * gc / ( gam * gbm * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a - float ( m ) + float ( k ) - 1.0 ) \
            * ( b - float ( m ) + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0

        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / float ( k )

        f1 = pa + pb - sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) \
            / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + 1.0 / float ( j + k )

          rp = pa + pb + 2.0 * el + sp - sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break

          hw = f1

        value = f0 * c0 + f1 * c1

    else:

      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gca = gamma ( c - a )
      gcb = gamma ( c - b )
      gcab = gamma ( c - a - b )
      gabc = gamma ( a + b - c )
      c0 = gc * gcab / ( gca * gcb )
      c1 = gc * gabc / ( ga * gb ) * ( 1.0 - x ) ** ( c - a - b )
      value = 0.0
      hw = value
      r0 = c0
      r1 = c1

      for k in range ( 1, 251 ):

        r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( a + b - c + float ( k ) ) ) * ( 1.0 - x )

        r1 = r1 * ( c - a + float ( k ) - 1.0 ) \
          * ( c - b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( c - a - b + float ( k ) ) ) * ( 1.0 - x )

        value = value + r0 + r1

        if ( abs ( value - hw ) < abs ( value ) * eps ):
          break

        hw = value

      value = value + c0 + c1

  else:

    a0 = 1.0

    if ( a < c and c < 2.0 * a and b < c and c < 2.0 * b ):

      a0 = ( 1.0 - x ) ** ( c - a - b )
      a = c - a
      b = c - b

    value = 1.0
    hw = value
    r = 1.0

    for k in range ( 1, 251 ):

      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( k * ( c + float ( k ) - 1.0 ) ) * x

      value = value + r

      if ( abs ( value - hw ) <= abs ( value ) * eps ):
        break

      hw = value

    value = a0 * value

  if ( x1 < 0.0 ):
    x = x1
    c0 = 1.0 / ( 1.0 - x ) ** aa
    value = c0 * value

  if ( 120 < k ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Warning!' )
    print ( '  A large number of iterations were needed.' )
    print ( '  The accuracy of the results should be checked.' )

  return value

def r8_hyper_2f1_test ( ):

#*****************************************************************************80
#
## r8_hyper_2f1_test() tests r8_hyper_2f1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_hyper_2f1_test():' )
  print ( '  r8_hyper_2f1() evaluates the hypergeometric 2F1 function.' )
  print ( '' )
  print ( '      A       B       C       X       2F1                       2F1                     DIFF' )
  print ( '                                     ' )
  print ( '(tabulated)               (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, a, b, c, x, fx1 ] = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_hyper_2f1 ( a, b, c, x )
 
    diff = abs ( fx1 - fx2 )
    print ( '  %6g  %6g  %6g  %6g  %24g  %24g  %10g' \
      % ( a, b, c, x, fx1, fx2, diff ) )

  return

def r8_hypot ( x, y ):

#*****************************************************************************80
#
## r8_hypot() returns the value of sqrt ( X^2 + Y^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the arguments.
#
#  Output:
#
#    real VALUE, the value of sqrt ( X^2 + Y^2 ).
#
  import numpy as np

  if ( abs ( x ) < abs ( y ) ):
    a = abs ( y )
    b = abs ( x )
  else:
    a = abs ( x )
    b = abs ( y )
#
#  A contains the larger value.
#
  if ( a == 0.0 ):
    value = 0.0
  else:
    value = a * np.sqrt ( 1.0 + ( b / a ) ** 2 )

  return value

def r8_hypot_test ( ):

#*****************************************************************************80
#
## r8_hypot_test() tests r8_hypot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_hypot_test():' )
  print ( '  r8_hypot() returns an accurate value for sqrt(A^2+B^2).' )
  print ( '' )
  print ( '             A          B          r8_hypot      sqrt(A^2+B^2)' )
  print ( '' )

  b = 2.0

  for i in range ( 0, 20 ):
    a = 1.0
    b = b / 2.0
    c = r8_hypot ( a, b )
    d = np.sqrt ( a ** 2 + b ** 2 )
    
    print ( '  %12g  %12g  %24.16g  %24.16g' % ( a, b, c, d ) )

  return

def r8_is_in_01 ( x ):

#*****************************************************************************80
#
## r8_is_in_01() is TRUE if the value is in the range [0,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the value.
#
#  Output:
#
#    bool VALUE, is TRUE if 0 <= X <= 1.
#
  value = ( 0.0 <= x and x <= 1.0 )

  return value

def r8_is_in_01_test ( rng ):

#*****************************************************************************80
#
## r8_is_in_01_test() tests r8_is_in_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_is_in_01_test():' )
  print ( '  r8_is_in_01() reports whether an R8 is in [0,1].' )
  print ( '' )
  print ( '      R8    r8_is_in_01?' )
  print ( '' )

  for i in range ( 0, 10 ):
    r8 = r8_uniform_ab ( -1.0, 2.0, rng )
    check = r8_is_in_01 ( r8 )
    print ( '  %8.2f  %s' % ( r8, check ) )

  return

def r8_is_inf ( r ):

#*****************************************************************************80
#
## r8_is_inf() determines if an R8 represents an infinite value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the number to be checked.
#
#  Output:
#
#    bool VALUE, is TRUE if R is an infinite value.
#
  value = ( r == - float ( 'inf' ) or r == float ( 'inf' ) )

  return value

def r8_is_inf_test ( ):

#*****************************************************************************80
#
## r8_is_inf_test() tests r8_is_inf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_is_inf_test():' )
  print ( '  r8_is_inf() reports whether an R8 is infinite.' )
  print ( '' )
  print ( '  These tests are wasted, since all the arithmetic' )
  print ( '  operations return run time errors.' )
  print ( '' )

  r8 = 1.0
  print ( '  r8_is_inf(1.0) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 1.0/0.0 causes a run time error!' )
  else:
    r1 = 1.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  r8_is_inf(1.0/0.0) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 0.0/0.0 causes a run time error!' )
  else:
    r1 = 0.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  r8_is_inf(0.0/0.0) = %s' % ( r8_is_inf ( r8 ) ) )
  
  r1 = 0.0
  r2 = 0.0
  r8 = r1 ** r2
  print ( '  r8_is_inf(0^0) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, arccos(-2.0) causes a run time error!' )
  else:
    r1 = -2.0
    r8 = np.arccos ( r1 )
    print ( '  r8_is_inf(acos(-2)) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, exp(1000) causes a run time overflow warning!' )
  else:
    r1 = 1000.0
    r8 = np.exp ( r1 )
    print ( '  r8_is_inf(exp(1000)) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, log(0) causes a run time error!' )
  else:
    r1 = 0.0
    r8 = np.log ( r1 )
    print ( '  r8_is_inf(log(0)) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, sqrt(-1) causes a run time error!' )
  else:
    r1 = -1.0
    r8 = np.sqrt ( r1 )
    print ( '  r8_is_inf(sqrt(-1)) = %s' % ( r8_is_inf ( r8 ) ) )

  return

def r8_is_insignificant ( r, s ):

#*****************************************************************************80
#
## r8_is_insignificant() determines if an R8 is insignificant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the number to be compared against.
#
#    real S, the number to be compared.
#
#  Output:
#
#    bool VALUE, is TRUE if S is insignificant compared to R.
#
  import numpy as np

  value = True
  epsilon = np.finfo(float).eps

  t = r + s
  tol = epsilon * np.abs ( r )

  if ( tol < np.abs ( r - t ) ):
    value = False
  
  return value

def r8_is_insignificant_test ( ):

#*****************************************************************************80
#
## r8_is_insignificant_test() tests r8_is_insignificant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_is_insignificant_test():' )
  print ( '  r8_is_insignificant ( R, S ) is TRUE is S is insignificant' )
  print ( '  compared to R.' )

  epsilon = np.finfo(float).eps
  huge = np.finfo(float).max
  r8_tiny = 1.0E-30

  print ( '' )
  print ( '               R               S  Insignificant?' )
  print ( '' )

  r = r8_tiny
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = epsilon
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = 1.0
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = huge
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  print ( '' )

  r = r8_tiny
  s = epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = epsilon
  s = epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = 1.0
  s = epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = huge
  s = epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  print ( '' )

  r = r8_tiny
  s = 1.0
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = epsilon
  s = 1.0
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = 1.0
  s = 1.0
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = huge
  s = 1.0
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  print ( '' )

  r = r8_tiny
  s = huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = epsilon
  s = huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = 1.0
  s = huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = huge / 2.0
  s = huge / 2.0
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  return

def r8_is_integer ( r ):

#*****************************************************************************80
#
## r8_is_integer() determines if an R8 represents an integer value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the number to be checked.
#
#  Output:
#
#    bool VALUE, is TRUE if R is an integer value.
#
  import numpy as np

  value = ( r == np.round ( r ) )

  return value

def r8_is_integer_test ( ):

#*****************************************************************************80
#
## r8_is_integer_test() tests r8_is_integer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_is_integer_test():' )
  print ( '  r8_is_integer() reports whether an R8 stores an integer value.' )
  print ( '' )

  for i in range ( - 8, 16 ):
    r = float ( i ) / 7.0
    v = r8_is_integer ( r )
    print ( '  %8.4f  %s' % ( r, v ) )

  return

def r8_is_nan ( r ):

#*****************************************************************************80
#
## r8_is_nan() determines if an R8 represents a NaN value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the number to be checked.
#
#  Output:
#
#    bool VALUE, is TRUE if R is a NaN
#
  value = ( r != r )

  return value

def r8_is_nan_test ( ):

#*****************************************************************************80
#
## r8_is_nan_test() tests r8_is_nan().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_is_nan_test():' )
  print ( '  r8_is_nan() reports whether an R8 is a NaN.' )
  print ( '' )
  print ( '  These tests are wasted, since all the arithmetic' )
  print ( '  operations return run time errors.' )
  print ( '' )

  r8 = 1.0
  print ( '  r8_is_nan(1.0) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 1.0/0.0 just sets a run time error.' )
  else:
    r1 = 1.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  r8_is_nan(1.0/0.0) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 0.0/0.0 just sets a run time error.' )
  else:
    r1 = 0.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  r8_is_nan(0.0/0.0) = %d' % ( r8_is_nan ( r8 ) ) )

  r1 = 0.0
  r2 = 0.0
  r8 = r1 ** r2
  print ( '  r8_is_nan(0^0) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, arccos(-2.0) just sets a run time warning.' )
  else:
    r1 = -2.0
    r8 = np.arccos ( r1 )
    print ( '  r8_is_nan(acos(-2)) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, exp(1000) just sets a run time warning.' )
  else:
    r1 = 1000.0
    r8 = np.exp ( r1 )
    print ( '  r8_is_nan(exp(1000)) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, log(0.0) just sets a run time warning.' )
  else:
    r1 = 0.0
    r8 = np.log ( r1 )
    print ( '  r8_is_nan(log(0)) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, sqrt(-1.0) just sets a run time warning.' )
  else:
    r1 = -1.0
    r8 = np.sqrt ( r1 )
    print ( '  r8_is_nan(sqrt(-1)) = %d' % ( r8_is_nan ( r8 ) ) )

  return

def r8_log_10 ( x ):

#*****************************************************************************80
#
## r8_log_10() returns the logarithm base 10 of |X|.
#
#  Discussion:
#
#    value = Log10 ( |X| )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose base 2 logarithm is desired.
#    X should not be 0.
#
#  Output:
#
#    real VALUE, the logarithm base 10 of the absolute
#    value of X.  It should be true that |X| = 10^r8_log_10.
#
  import numpy as np

  if ( x == 0.0 ):
    value = - np.inf
  else:
    value = np.log ( abs ( x ) ) / np.log ( 10.0 )

  return value

def r8_log_10_test ( ):

#*****************************************************************************80
#
## r8_log_10_test() tests r8_log_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 18

  x_test = np.array ( [ \
    0.0,  1.0,  2.0,   3.0,  9.0, \
   10.0, 11.0, 99.0, 101.0, -1.0, \
   -2.0, -3.0, -9.0,   0.5,  0.33, \
    0.25, 0.20, 0.01 ] )

  print ( '' )
  print ( 'r8_log_10_test():' )
  print ( '  r8_log_10() computes the logarithm base 10.' )
  print ( '' )
  print ( '      X      r8_log_10' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test]
    print ( '  %12f  %12f' % ( x, r8_log_10 ( x ) ) )

  return

def r8_log_2 ( x ):

#*****************************************************************************80
#
## r8_log_2() returns the logarithm base 2 of |X|.
#
#  Discussion:
#
#    r8_log_2 ( X ) = Log ( |X| ) / Log ( 2.0 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose base 2 logarithm is desired.
#    X should not be 0.
#
#  Output:
#
#    real VALUE, the logarithm base 2 of the absolute
#    value of X.  It should be true that |X| = 2^r8_log_2.
#
  import numpy as np

  if ( x == 0 ):
    value = float ( '-inf' )
  else:
    value = np.log ( abs ( x ) ) / np.log ( 2.0 )

  return value

def r8_log_2_test ( ):

#*****************************************************************************80
#
## r8_log_2_test() tests r8_log_2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 18

  x_test = np.array ( [ \
    0.0,  1.0,  2.0,   3.0,  9.0, \
   10.0, 11.0, 99.0, 101.0, -1.0, \
   -2.0, -3.0, -9.0,   0.5,  0.33, \
    0.25, 0.20, 0.01 ] )

  print ( '' )
  print ( 'r8_log_2_test():' )
  print ( '  r8_log_2() computes the logarithm base 2.' )
  print ( '' )
  print ( '      X      r8_log_2' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test]
    print ( '  %12f  %12f' % ( x, r8_log_2 ( x ) ) )

  return

def r8_log_b ( x, b ):

#*****************************************************************************80
#
## r8_log_b() returns the logarithm base B of |X|.
#
#  Discussion:
#
#    value = log ( |X| ) / log ( |B| )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 October 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose base B logarithm is desired.
#    X should not be 0.
#
#    real B, the base, which should not be 0, 1 or -1.
#
#  Output:
#
#    real VALUE, the logarithm base B of the absolute
#    value of X.  It should be true that |X| = |B|^D_log_b.
#
  import numpy as np

  value = np.log ( abs ( x ) ) / np.log ( abs ( b ) )

  return value

def r8_log_b_test ( ):

#*****************************************************************************80
#
## r8_log_b_test() tests r8_log_b().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 10

  b_test = np.array ( [ \
    2.0, 3.0, 4.0, 5.0, 6.0, \
    7.0, 8.0, 16.0, 32.0, 256.0 ] )

  x = 16.0

  print ( '' )
  print ( 'r8_log_b_test():' )
  print ( '  r8_log_b() computes the logarithm base B.' )
  print ( '' )
  print ( '        X             B             r8_log_b' )
  print ( '' )

  for test in range ( 0, test_num ):

    b = b_test[test]

    print ( '  %12f  %12f  %12f' % ( x, b, r8_log_b ( x, b ) ) )

  return

def r8_mant ( x ):

#*****************************************************************************80
#
## r8_mant() computes the "mantissa" or "fraction part" of X.
#
#  Formula:
#
#    X = S * R * 2^L
#
#    S is +1 or -1,
#    R is a real value between 1.0 and 2.0,
#    L is an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number to be decomposed.
#
#  Output:
#
#    integer S, the "sign" of the number.
#    S will be -1 if X is less than 0, and +1 if X is greater
#    than or equal to zero.
#
#    real R, the mantissa of X.  R will be greater
#    than or equal to 1, and strictly less than 2.  The one
#    exception occurs if X is zero, in which case R will also
#    be zero.
#
#    integer L, the integer part of the logarithm (base 2) of X.
#

#
#  Determine the sign.
#
  if ( x < 0.0 ):
    s = -1
  else:
    s = 1
#
#  Set R to the absolute value of X, and L to zero.
#  Then force R to lie between 1 and 2.
#
  if ( x < 0.0 ):
    r = -x
  else:
    r = x

  l = 0
#
#  Time to bail out if X is zero.
#
  if ( x == 0.0 ):
    return s, r, l

  while ( 2.0 <= r ):
    r = r / 2.0
    l = l + 1

  while ( r < 1.0 ):
    r = r * 2.0
    l = l - 1

  return s, r, l

def r8_mant_test ( ):

#*****************************************************************************80
#
## r8_mant_test() tests r8_mant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  x = -314.159

  print ( '' )
  print ( 'r8_mant_test():' )
  print ( '  r8_mant() decomposes a value.' )
  print ( '' )
  print ( '  Number to be decomposed:' )
  print ( '  %g' % ( x ) )

  s, r, l = r8_mant ( x )

  print ( '' )
  print ( '  r8_mant: X = %d * %f * 2^ %d' % ( s, r, l ) )

  return

def r8mat_add ( m, n, alpha, a, beta, b ):

#*****************************************************************************80
#
## r8mat_add() computes C = alpha * A + beta * B for R8MAT's.
#
#  Discussion:
#
#    An R8MAT is an array of R8 values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real ALPHA, the multiplier for A.
#
#    real A(M,N), the first matrix.
#
#    real BETA, the multiplier for A.
#
#    real B(M,N), the second matrix.
#
#  Output:
#
#    real C(M,N), the sum of alpha*A+beta*B.
#
  import numpy as np

  c = np.zeros ( [ m, n ] )

  c = alpha * a + beta * b

# for i in range ( 0, m ):
#   for j in range ( 0, n ):
#     c[i.j] = alpha * a[i.j] + beta * b[i.j]

  return c

def r8mat_add_test ( ):

#*****************************************************************************80
#
## r8mat_add_test() tests r8mat_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 4
  n = 4

  print ( '' )
  print ( 'r8mat_add_test():' )
  print ( '  r8mat_add() computes C = alpha * A + beta * B for R8MATs.' )

  alpha = 3.0

  a = r8mat_indicator ( m, n )

  beta = 0.5

  b = r8mat_indicator ( n, m )
  b = r8mat_transpose ( n, m, b )

  c = r8mat_add ( m, n, alpha, a, beta, b )

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )

  print ( '' )
  print ( '  ALPHA = %g, BETA = %g' % ( alpha, beta ) )

  r8mat_print ( m, n, c, '  C = alpha * A + beta * B:' )

  return

def r8mat_cholesky_factor ( n, a ):

#*****************************************************************************80
#
## r8mat_cholesky_factor() computes the Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric positive semidefinite.
#
#    For a positive semidefinite symmetric matrix A, the Cholesky factorization
#    is a lower triangular matrix L such that:
#
#      A = L * L'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real C(N,N), the N by N lower triangular Cholesky factor.
#
#    boolean FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[0:j,j] = 0.0

    for i in range ( j, n ):

      sum2 = c[j,i]
      for k in range ( 0, j ):
        sum2 = sum2 - c[j,k] * c[i,k]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[i,j] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[i,j] = sum2 / c[j,j]
        else:
          c[i,j] = 0.0

  return c, flag

def r8mat_cholesky_factor_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_test() tests r8mat_cholesky_factor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_factor_test():' )
  print ( '  r8mat_cholesky_factor() determines the' )
  print ( '  lower triangular Cholesky factorization' )
  print ( '  of a symmetric positive definite matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )

  return

def r8mat_cholesky_factor_upper ( n, a ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_upper(): upper Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric positive semidefinite.
#
#    For a symmetric positive semidefinite matrix A, the upper Cholesky 
#    factorization is an upper triangular matrix R such that:
#
#      A = R' * R
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real C(N,N), the N by N upper triangular Cholesky factor.
#
#    bool FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[j,0:j] = 0.0

    for i in range ( j, n ):

      sum2 = c[i,j]
      for k in range ( 0, j ):
        sum2 = sum2 - c[k,j] * c[k,i]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[j,i] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[j,i] = sum2 / c[j,j]
        else:
          c[j,i] = 0.0

  return c, flag

def r8mat_cholesky_factor_upper_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_upper_test() tests r8mat_cholesky_factor_upper().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_factor_upper_test():' )
  print ( '  r8mat_cholesky_factor_upper() determines the' )
  print ( '  upper triangular Cholesky factorization' )
  print ( '  of a positive definite symmetric matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  r, flag = r8mat_cholesky_factor_upper ( n, a )
  r8mat_print ( n, n, r, '  Cholesky factor R:' )
  d = np.dot ( r.transpose ( ), r )
  r8mat_print ( n, n, d, '  Product R\' * R:' )

  return

def r8mat_cholesky_solve ( n, l, b ):

#*****************************************************************************80
#
## r8mat_cholesky_solve() solves a Cholesky factored linear system A * x = b.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real L(N,N), the N by N Cholesky factor of the
#    system matrix A.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#

#
#  Solve L * y = b.
#
  x = r8mat_l_solve ( n, l, b )
#
#  Solve L' * x = y.
#
  x = r8mat_lt_solve ( n, l, x )

  return x

def r8mat_cholesky_solve_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_solve_test() tests r8mat_cholesky_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_solve_test():' )
  print ( '  r8mat_cholesky_solve() solves a linear system' )
  print ( '  using the lower triangular Cholesky factorization,' )
  print ( '  for a positive definite symmetric matrix.' )
  
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )
#
#  Solve a linear system.
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
  r8vec_print ( n, b, '  Right hand side b:' )
  x = r8mat_cholesky_solve ( n, l, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  return

def r8mat_column_append ( x, y ):

#*****************************************************************************80
#
## r8mat_column_append() appends a vector as a final column of an R8MAT.
#
#  Discussion:
#
#    This operation is SO EASY in MATLAB and so unbelievably awkward
#    and tricky in Python.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x[m,n]: the array.
#
#    real y[m]: the vector to be appended.
#
#  Output:
#
#    real x[m,n+1]: the updated array.
#
  import numpy as np

  m = x.shape[0]
  n = x.shape[1]
#
#  If Y is a vector, make it a matrix.
#
  ndimy = y.ndim
  if ( ndimy == 1 ):
    y = np.array ( [ y ] )

  my = y.shape[0]
  ny = y.shape[1]
#
#  If Y is a 1-row matrix, transpose it.
#
  if ( my == 1 ):
    y = np.reshape ( y, [ m, 1 ] )

  x = np.append ( x, y, 1 )

  return x

def r8mat_column_append_test ( ):

#*****************************************************************************80
#
## r8mat_column_append_test() tests r8mat_column_append().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_column_append_test():' )
  print ( '  r8mat_column_append() appends a column to a 2D array.' )

  x = np.array ( [ \
    [ 11, 12 ], \
    [ 21, 22 ], \
    [ 31, 32 ] ] )
  m = x.shape[0]
  n = x.shape[1]

  r8mat_print ( m, n, x, '  The original array x:' )
#
#  Y1 is a vector.
#
  y1 = np.array ( [ 13, 23, 33 ] )
  ny = y1.shape[0]
  r8vec_print ( ny, y1, '  The vector y1 to be added:' )

  x = r8mat_column_append ( x, y1 )
  m = x.shape[0]
  n = x.shape[1]
  r8mat_print ( m, n, x, '  The array + y1' )
#
#  Y2 is a 1-column matrix.
#
  y2 = np.array ( [ [ 14 ], [ 24 ], [ 34 ] ] )
  ny = y2.shape[0]
  r8vec_print ( ny, y2[:,0], '  The vector y2 to be added:' )

  x = r8mat_column_append ( x, y2 )
  m = x.shape[0]
  n = x.shape[1]
  r8mat_print ( m, n, x, '  The array + y1 + y2' )
#
#  Y3 is a 1-row matrix.
#
  y3 = np.array ( [ [ 14, 24, 34 ] ] )
  ny = y2.shape[0]
  r8vec_print ( ny, y2[:,0], '  The vector y2 to be added:' )

  x = r8mat_column_append ( x, y2 )
  m = x.shape[0]
  n = x.shape[1]
  r8mat_print ( m, n, x, '  The array + y1 + y2' )

  return

def r8mat_det_2d ( a ):

#*****************************************************************************80
#
## r8mat_det_2d() computes the determinant of a 2 by 2 matrix.
#
#  Discussion:
#
#    The determinant is the area spanned by the vectors making up the rows
#    or columns of the matrix.
#
#    value = A(1,1) * A(2,2) - A(1,2) * A(2,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2,2), the matrix whose determinant is desired.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = a[0,0] * a[1,1] - a[0,1] * a[1,0]

  return det

def r8mat_det_2d_test ( ):

#*****************************************************************************80
#
## r8mat_det_2d_test() tests r8mat_det_2d();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 2

  x = np.array ( [ 1.0, 10.0 ] )

  print ( '' )
  print ( 'r8mat_det_2d_test():' )
  print ( '  r8mat_det_2d(): determinant of a 2 by 2 matrix;' )

  a = r8mat_vand2 ( n, n, x )
 
  r8mat_print ( n, n, a, '  Matrix:' );

  det = r8mat_det_2d ( a )

  print ( '' )
  print ( '  r8mat_det_2d computes determinant: ', det )
#
#  Special formula for the determinant of a Vandermonde matrix:
#
  det = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      det = det * ( x[i] - x[j] )

  print ( '  Exact determinant is ', det )

  return

def r8mat_det_3d ( a ):

#*****************************************************************************80
#
## r8mat_det_3d() computes the determinant of a 3 by 3 matrix.
#
#  Discussion:
#
#    The determinant is the volume of the shape spanned by the vectors
#    making up the rows or columns of the matrix.
#
#    det = a11 * a22 * a33 - a11 * a23 * a32
#        + a12 * a23 * a31 - a12 * a21 * a33
#        + a13 * a21 * a32 - a13 * a22 * a31
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real a[3,3), the matrix whose determinant is desired.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det  =   a[0,0] * ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) \
         + a[0,1] * ( a[1,2] * a[2,0] - a[1,0] * a[2,2] ) \
         + a[0,2] * ( a[1,0] * a[2,1] - a[1,1] * a[2,0] )

  return det

def r8mat_det_3d_test ( ):

#*****************************************************************************80
#
## r8mat_det_3d_test() tests r8mat_det_3d();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  x = np.array ( [ 1.0, 10.0, 4.0 ] )

  print ( '' )
  print ( 'r8mat_det_3d_test():' )
  print ( '  r8mat_det_3d(): determinant of a 3 by 3 matrix' )

  a = r8mat_vand2 ( n, n, x )
  det = r8mat_det_3d ( a )

  r8mat_print ( n, n, a, '  Matrix:' )

  print ( '' )
  print ( '  r8mat_det_3d computes determinant: %g' % ( det ) )
#
#  Special formula for the determinant of a Vandermonde matrix:
#
  det = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      det = det * ( x[i] - x[j] )

  print ( '  Exact determinant is %g' % ( det ) )

  return

def r8mat_det_4d ( a ):

#*****************************************************************************80
#
## r8mat_det_4d() computes the determinant of a 4 by 4 matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(4,4), the matrix whose determinant is desired.
#
#  Output:
#
#    real VALUE, the determinant of the matrix.
#
  value = \
      a[0,0] * ( \
        a[1,1] * ( a[2,2] * a[3,3] - a[2,3] * a[3,2] ) \
      - a[1,2] * ( a[2,1] * a[3,3] - a[2,3] * a[3,1] ) \
      + a[1,3] * ( a[2,1] * a[3,2] - a[2,2] * a[3,1] ) ) \
    - a[0,1] * ( \
        a[1,0] * ( a[2,2] * a[3,3] - a[2,3] * a[3,2] ) \
      - a[1,2] * ( a[2,0] * a[3,3] - a[2,3] * a[3,0] ) \
      + a[1,3] * ( a[2,0] * a[3,2] - a[2,2] * a[3,0] ) ) \
    + a[0,2] * ( \
        a[1,0] * ( a[2,1] * a[3,3] - a[2,3] * a[3,1] ) \
      - a[1,1] * ( a[2,0] * a[3,3] - a[2,3] * a[3,0] ) \
      + a[1,3] * ( a[2,0] * a[3,1] - a[2,1] * a[3,0] ) ) \
    - a[0,3] * ( \
        a[1,0] * ( a[2,1] * a[3,2] - a[2,2] * a[3,1] ) \
      - a[1,1] * ( a[2,0] * a[3,2] - a[2,2] * a[3,0] ) \
      + a[1,2] * ( a[2,0] * a[3,1] - a[2,1] * a[3,0] ) )

  return value

def r8mat_det_4d_test ( ):

#*****************************************************************************80
#
## r8mat_det_4d_test() tests r8mat_det_4d()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  x = np.array ( [ 1.0, 10.0, 4.0, 2.0 ] )

  print ( '' )
  print ( 'r8mat_det_4d_test():' )
  print ( '  r8mat_det_4d() determinant of a 4 by 4 matrix' )

  a = r8mat_vand2 ( n, n, x )
  det = r8mat_det_4d ( a )

  r8mat_print ( n, n, a, '  Matrix:' )

  print ( '' )
  print ( '  r8mat_det_4d computes determinant: %g' % ( det ) )
#
#  Special formula for the determinant of a Vandermonde matrix:
#
  det = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      det = det * ( x[i] - x[j] )

  print ( '  Exact determinant is %g' % ( det ) )

  return

def r8mat_diag_get_vector ( n, a ):

#*****************************************************************************80
#
## r8mat_diag_get_vector() returns the diagonal of an R8MAT in a vector.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of
#    the matrix.
#
#    real A(N,N), the N by N matrix.
#
#  Output:
#
#    real V(N), the diagonal entries
#    of the matrix.
#
  import numpy as np

  v = np.zeros ( n )

  for i in range ( 0, n ):
    v[i] = a[i,i]
 
  return v

def r8mat_diag_get_vector_test ( rng ):

#*****************************************************************************80
#
## r8mat_diag_get_vector_test() tests r8mat_diag_get_vector().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#

  m = 5
  n = m

  print ( '' )
  print ( 'r8mat_diag_get_vector_test():' )
  print ( '  r8mat_diag_get_vector() retrieves the diagonal from an R8MAT.' )

  a = r8mat_uniform_01 ( m, n, rng )

  r8mat_print ( m, n, a, '  Random R8MAT:' )

  v = r8mat_diag_get_vector ( n, a )
  r8vec_print ( n, v, '  Diagonal vector:' )

  return

def r8mat_diff_frobenius ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_diff_frobenius(): Frobenius norm of the difference of two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), B(M,N), the matrices for which we
#    are to compute the Frobenius norm of the difference.
#
#  Output:
#
#    real DIF, the Frobenius norm of A-B.
#
  import numpy as np

  diff = np.sqrt ( np.sum ( np.sum ( ( a[0:m,0:n] - b[0:m,0:n] ) ** 2 ) ) )

  return diff

def r8mat_diff_frobenius_test ( ):

#*****************************************************************************80
#
## r8mat_diff_frobenius_test() tests r8mat_diff_frobenius().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_diff_frobenius_test():' )
  print ( '  r8mat_diff_frobenius() computes the Frobenius norm of' )
  print ( '  the difference of two R8MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], \
    [ 21.0, 22.0, 23.0 ] ] )

  b = np.array ( [ \
    [ 10.0, 13.0, 12.0 ], \
    [ 23.0, 21.0, 24.0 ] ] )

  c = a - b

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A-B:' )

  diff = r8mat_diff_frobenius ( m, n, a, b )

  print ( '' )
  print ( '  Frobenius norm ||A-B|| = %g' % ( diff ) )

  return

def r8mat_expand_linear2 ( m, n, a, m2, n2 ):

#*****************************************************************************80
#
## r8mat_expand_linear2() expands an R8MAT by linear interpolation.
#
#  Discussion:
#
#    In this version of the routine, the expansion is indicated
#    by specifying the dimensions of the expanded array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in A.
#
#    real A(M,N), a "small" M by N array.
#
#    integer M2, N2, the number of rows and columns in A2.
#
#  Output:
#
#    real A2(M2,N2), the expanded array, which
#    contains an interpolated version of the data in A.
#
  import numpy as np

  a2 = np.zeros ( [ m2, n2 ] )

  for i in range ( 1, m2 + 1 ):

    if ( m2 == 1 ):
      r = 0.5
    else:
      r = ( i - 1 ) / ( m2 - 1 )

    i1 = 1 + floor ( r * ( m - 1 ) )
    i2 = i1 + 1

    if ( m < i2 ):
      i1 = m - 1
      i2 = m

    r1 = ( i1 - 1 ) / ( m - 1 )
    r2 = ( i2 - 1 ) / ( m - 1 )

    for j in range ( 1, n2 + 1 ):

      if ( n2 == 1 ):
        s = 0.5
      else:
        s = ( j - 1 ) / ( n2 - 1 )
 
      j1 = 1 + floor ( s * ( n - 1 ) )
      j2 = j1 + 1

      if ( n < j2 ):
        j1 = n - 1
        j2 = n

      s1 = ( j1 - 1 ) / ( n - 1 )
      s2 = ( j2 - 1 ) / ( n - 1 )

      a2[i-1,j-1] = \
        ( ( r2 - r ) * ( s2 - s ) * a(i1,j1) \
        + ( r - r1 ) * ( s2 - s ) * a(i2,j1) \
        + ( r2 - r ) * ( s - s1 ) * a(i1,j2) \
        + ( r - r1 ) * ( s - s1 ) * a(i2,j2) ) \
        / ( ( r2 - r1 ) * ( s2 - s1 ) )

  return a2

def r8mat_house_axh ( n, a, v ):

#*****************************************************************************80
#
## r8mat_house_axh() computes A*H where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real A(N,N), the matrix to be postmultiplied.
#
#    real V(N), a vector defining a Householder matrix.
#
#  Output:
#
#    real AH(N,N), the product A*H.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ah = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ah[i,j] = a[i,j]
      for k in range ( 0, n ):
        ah[i,j] = ah[i,j] - 2.0 * a[i,k] * v[k] * v[j] / vtv
            
  return ah

def r8mat_house_axh_test ( rng ):

#*****************************************************************************80
#
## r8mat_house_axh_test() tests r8mat_house_axh().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8mat_house_axh_test():' )
  print ( '  r8mat_house_axh() multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0

  a = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, rng )

  r8mat_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A packs column 3 of A.
#
  k = 3
  km1 = k - 1
  a_col = np.zeros ( n )
  for i in range ( 0, n ):
    a_col[i] = a[i,km1]

  v = r8vec_house_column ( n, a_col, km1 )

  r8vec_print ( n, v, '  Compact vector V so column 3 of H*A is packed:' )

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8mat_house_axh ( n, a, v )

  r8mat_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = r8mat_mm ( n, n, n, a, h )

  r8mat_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = r8mat_mm ( n, n, n, h, a )

  r8mat_print ( n, n, ha, '  H*A should pack column 3:' )

  return

def r8mat_house_form ( n, v ):

#*****************************************************************************80
#
## r8mat_house_form() constructs a Householder matrix from its compact form.
#
#  Discussion:
#
#    H(v) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real V(N,1), the vector defining the Householder matrix.
#
#  Output:
#
#    real H(N,N), the Householder matrix.
#
  import numpy as np

  v_dot_v = 0.0
  for i in range ( 0, n ):
    v_dot_v = v_dot_v + v[i] * v[i]

  c = - 2.0 / v_dot_v

  h = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    h[j,j] = 1.0
    for i in range ( 0, n ):
      h[i,j] = h[i,j] + c * v[i] * v[j]
            
  return h

def r8mat_house_form_test ( ):

#*****************************************************************************80
#
## r8mat_house_form_test() tests r8mat_house_form().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  v = np.array ( ( 0.0, 0.0, 1.0, 2.0, 3.0 ) )

  print ( '' )
  print ( 'r8mat_house_form_test():' )
  print ( '  r8mat_house_form() forms a Householder' )
  print ( '  matrix from its compact form.' )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )
 
  r8mat_print ( n, n, h, '  Householder matrix H:' )

  return

def r8mat_house_hxa ( n, a, v ):

#*****************************************************************************80
#
## r8mat_house_hxa() computes H*A where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real A(N,N), the matrix to be postmultiplied.
#
#    real V(N), a vector defining a Householder matrix.
#
#  Output:
#
#    real HA(N,N), the product H*A.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ha = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ha[i,j] = a[i,j]
      for k in range ( 0, n ):
        ha[i,j] = ha[i,j] - 2.0 * v[i] * v[k] * a[k,j] / vtv
            
  return ha

def r8mat_house_hxa_test ( rng ):

#*****************************************************************************80
#
## r8mat_house_hxa_test() tests r8mat_house_hxa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8mat_house_hxa_test():' )
  print ( '  r8mat_house_hxa() multiplies a compact Householder matrix H' )
  print ( '  times a matrix A.' )

  r8_lo = -5.0
  r8_hi = +5.0

  a = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, rng )

  r8mat_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A' packs column 3 of A'.
#
  k = 3
  a_row = np.zeros ( n )
  for j in range ( 0, n ):
    a_row[j] = a[k,j]

  v = r8vec_house_column ( n, a_row, k )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute H*A.
#
  ha = r8mat_house_hxa ( n, a, v )

  r8mat_print ( n, n, ha, '  Indirect product H*A:' )
#
#  Compare with a direct calculation.
#
  ha = r8mat_mm ( n, n, n, h, a )

  r8mat_print ( n, n, ha, '  Direct product H*A:' )

  return

def r8mat_identity ( n ):

#*****************************************************************************80
#
## r8mat_identity() sets up an NxN identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ), dtype = float )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def r8mat_identity_test ( ):

#*****************************************************************************80
#
## r8mat_identity_test() tests r8mat_identity().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
# 
  print ( '' )
  print ( 'r8mat_identity_test():' )
  print ( '  r8mat_identity() creates an identity matrix.' )

  m = 5
  n = m
  a = r8mat_identity ( n )
  r8mat_print ( m, n, a, '  The identity matrix:' )

  return

def r8mat_indicator ( m, n ):

#*****************************************************************************80
#
## r8mat_indicator() sets up an indicator R8MAT.
#
#  Discussion:
#
#    The value of each entry suggests its location, as in:
#
#      11  12  13  14
#      21  22  23  24
#      31  32  33  34
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real TABLE(M,N), the indicator table.
#
  import numpy as np

  table = np.zeros ( ( m, n ), dtype = float )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      table[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return table

def r8mat_indicator_test ( ):

#*****************************************************************************80
#
## r8mat_indicator_test() tests r8mat_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8mat_indicator_test():' )
  print ( '  r8mat_indicator() creates an "indicator" R8MAT.' )

  m = 5
  n = 4
  a = r8mat_indicator ( m, n )
  r8mat_print ( m, n, a, '  The indicator matrix:' )

  return

def r8mat_inverse_3d ( a ):

#*****************************************************************************80
#
## r8mat_inverse_3d() inverts a 3 by 3 R8MAT using Cramer's rule.
#
#  Discussion:
#
#    If DET is zero, then A is singular, and does not have an
#    inverse.  In that case, B is simply set to zero, and a
#    message is printed.
#
#    If DET is nonzero, then its value is roughly an estimate
#    of how nonsingular the matrix A is.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(3,3), the matrix to be inverted.
#
#  Output:
#
#    real B(3,3), the inverse of the matrix.
#
#    real DET, the determinant of the matrix.
#
  import numpy as np
#
#  Compute the determinant of A
#
  det =   a[0,0] * ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) \
        + a[0,1] * ( a[1,2] * a[2,0] - a[1,0] * a[2,2] ) \
        + a[0,2] * ( a[1,0] * a[2,1] - a[1,1] * a[2,0] )
#
#  If the determinant is zero, bail out.
#
  if ( det == 0.0 ):
    b = np.zeros ( [ 3, 3 ] )
    return b, det
#
#  Compute the entries of the inverse matrix using an explicit
#  formula.
#
  b = np.zeros ( [ 3, 3 ] )

  b[0,0] = + ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) / det
  b[0,1] = - ( a[0,1] * a[2,2] - a[0,2] * a[2,1] ) / det
  b[0,2] = + ( a[0,1] * a[1,2] - a[0,2] * a[1,1] ) / det

  b[1,0] = - ( a[1,0] * a[2,2] - a[1,2] * a[2,0] ) / det
  b[1,1] = + ( a[0,0] * a[2,2] - a[0,2] * a[2,0] ) / det
  b[1,2] = - ( a[0,0] * a[1,2] - a[0,2] * a[1,0] ) / det

  b[2,0] = + ( a[1,0] * a[2,1] - a[1,1] * a[2,0] ) / det
  b[2,1] = - ( a[0,0] * a[2,1] - a[0,1] * a[2,0] ) / det
  b[2,2] = + ( a[0,0] * a[1,1] - a[0,1] * a[1,0] ) / det

  return b, det

def r8mat_inverse_3d_test ( ):

#*****************************************************************************80
#
## r8mat_inverse_3d_test() tests r8mat_inverse_3d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
#
#  Each ROW of this definion is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  print ( '' )
  print ( 'r8mat_inverse_3d_test():' )
  print ( '  r8mat_inverse_3d inverts a 3 by 3 matrix.' )

  r8mat_print ( n, n, a, '  Matrix A to be inverted:' )
#
#  Compute the inverse matrix.
#
  b, det = r8mat_inverse_3d ( a )
 
  if ( det == 0.0 ):
    print ( '' )
    print ( '  The input matrix was singular, no inverse' )
    print ( '  could be computed.' )
    return

  r8mat_print ( n, n, b, '  Inverse matrix B:' )

  c = np.dot ( a, b )

  r8mat_print ( n, n, c, '  Product C = A * B:' )

  return

def r8mat_is_binary ( m, n, x ):

#*****************************************************************************80
#
## r8mat_is_binary() is true if an R8MAT only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimension of the array.
#
#    real X(M,N), the array to be checked.
#
#  Output:
#
#    bool VALUE, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      if ( x[i,j] != 0.0 and x[i,j] != 1.0 ):
        value = False
        break

  return value

def r8mat_is_binary_test ( ):

#*****************************************************************************80
#
## r8mat_is_binary_test() tests r8mat_is_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_is_binary_test():' )
  print ( '  r8mat_is_binary() is TRUE if an R8MAT only contains' )
  print ( '  0 or 1 entries.' )

  m = 2
  n = 3

  x = np.array ( [ \
    [ 0.0, 1.0, 0.0 ], \
    [ 1.0, 0.0, 1.0 ] ] )
  r8mat_print ( m, n, x, '  X:' )
  if ( r8mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ \
    [ 1.0, 1.0, 1.0 ], \
    [ 1.0, 1.0, 1.0 ] ] )
  r8mat_print ( m, n, x, '  X:' )
  if ( r8mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ \
    [ 0.0, 1.0, 0.0 ], \
    [ 1.0, 2.0, 1.0 ] ] )
  r8mat_print ( m, n, x, '  X:' )
  if ( r8mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  return

def r8mat_is_identity ( n, a ):

#*****************************************************************************80
#
## r8mat_is_identity() determines if a matrix is the identity.
#
#  Discussion:
#
#    The routine returns the Frobenius norm of A - I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real ERROR_frobenius, the Frobenius norm
#    of the difference matrix A - I, which would be exactly zero
#    if A were the identity matrix.
#
  import numpy as np

  error_frobenius = 0.0

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        error_frobenius = error_frobenius + ( a[i,j] - 1.0 ) ** 2
      else:
        error_frobenius = error_frobenius + a[i,j] ** 2

  error_frobenius = np.sqrt ( error_frobenius );

  return error_frobenius

def r8mat_is_identity_test ( ):

#*****************************************************************************80
#
## r8mat_is_identity_test() tests r8mat_is_identity().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_is_identity_test():' )
  print ( '  r8mat_is_identity() reports the Frobenius norm difference' )
  print ( '  between a given matrix A and the identity matrix.' )

  n = 4
  a = np.zeros ( [ n, n ] )
  r8mat_print ( n, n, a, '  Zero matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
  r8mat_print ( n, n, a, '  Identity matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = a[i,j] + float ( i * j ) / 1000
  r8mat_print ( n, n, a, '  Almost identity matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  return

def r8mat_is_insignificant ( m, n, r, s ):

#*****************************************************************************80
#
## r8mat_is_insignificant() determines if an R8MAT is relatively insignificant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimension of the matrices.
#
#    real R(M,N), the vector to be compared against.
#
#    real S(M,N), the vector to be compared.
#
#  Output:
#
#    bool VALUE, is true if S is insignificant
#    relative to R.
#
  eps = 2.220446049250313E-016

  value = True

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      t = r[i,j] + s[i,j]
      tol = eps * abs ( r[i,j] )

      if ( tol < abs ( r[i,j] - t ) ):
        value = False
        break
  
  return value

def r8mat_is_significant ( m, n, r, s ):

#*****************************************************************************80
#
## r8mat_is_significant() determines if an R8MAT is relatively significant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 217
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimension of the matrices.
#
#    real R(M,N), the vector to be compared against.
#
#    real S(M,N), the vector to be compared.
#
#  Output:
#
#    bool VALUE, is true if S is significant
#    relative to R.
#
  eps = 2.220446049250313E-016

  value = False

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      t = r[i,j] + s[i,j]
      tol = eps * abs ( r[i,j] )

      if ( tol < abs ( r[i,j] - t ) ):
        value = True
        break
  
  return value

def r8mat_l1_inverse ( A ):

#*****************************************************************************80
#
## r8mat_l1_inverse() inverts a unit lower triangular R8MAT.
#
#  Discussion:
#
#    A unit lower triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's above the main diagonal.
#
#    The inverse of a unit lower triangular matrix is also
#    a unit lower triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    real A(N,N), the unit lower triangular matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np

  n = np.size ( A, 0 )
  
  B = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i < j ):
        B[i,j] = 0.0
      elif ( j == i ):
        B[i,j] = 1.0
      else:
        B[i,j] = - np.sum ( A[i,0:i] * B[0:i,j] )

  return B

def r8mat_l1_inverse_test ( ):

#*****************************************************************************80
#
## r8mat_l1_inverse_test() tests r8mat_l1_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
#
#  Each row of this definition is a COLUMN of the matrix.
#
  A = np.array ( [ \
    [  1.0, 0.0, 0.0, 0.0, 0.0, 0.0 ], \
    [  2.0, 1.0, 0.0, 0.0, 0.0, 0.0 ], \
    [  0.0, 0.0, 1.0, 0.0, 0.0, 0.0 ], \
    [  5.0, 0.0, 3.0, 1.0, 0.0, 0.0 ], \
    [  0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ], \
    [ 75.0, 0.0, 0.0, 6.0, 4.0, 1.0 ] ] )

  print ( '' )
  print ( 'r8mat_l1_inverse_test():' )
  print ( '  r8mat_l1_inverse() inverts a unit lower triangular matrix.' )

  r8mat_print ( n, n, A, '  Matrix A to be inverted:' )
 
  B = r8mat_l1_inverse ( A )
 
  r8mat_print ( n, n, B, '  Inverse matrix B:' )
 
  C = np.matmul ( A, B )

  r8mat_print ( n, n, C, '  Product C = A * B:' )

  return

def r8mat_l_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_l_solve() solves a lower triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of
#    the matrix A.
#
#    real A(N,N), the N by N lower triangular matrix.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  x = np.zeros ( n )
#
#  Solve L * x = b.
#
  for i in range ( 0, n ):
    x[i] = b[i]
    for j in range ( 0, i ):
      x[i] = x[i] - a[i,j] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_l_solve_test ( ):

#*****************************************************************************80
#
## r8mat_l_solve_test() tests r8mat_l_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  a = np.array ( [ \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 2.0,  3.0,  0.0,  0.0 ], \
    [ 4.0,  5.0,  6.0,  0.0 ], \
    [ 7.0,  8.0,  9.0, 10.0 ] ] )

  b = np.array ( [ 1.0, 8.0, 32.0, 90.0 ] )

  print ( '' )
  print ( 'r8mat_l_solve_test():' )
  print ( '  r8mat_l_solve() solves a lower triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_l_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = r8vec_norm ( n, r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )

  return

def r8mat_lt_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_lt_solve() solves a transposed lower triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#    Given the lower triangular matrix A, the linear system to be solved is:
#
#      A' * x = b
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns
#    of the matrix.
#
#    real A(N,N), the N by N lower triangular matrix.
#
#    real B(N,1), the right hand side of the linear system.
#
#  Output:
#
#    real X(N,1), the solution of the linear system.
#
  import numpy as np
#
#  Solve U' * x = b.
#
  x = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    x[i] = b[i]
    for j in range ( i + 1, n ):
      x[i] = x[i] - a[j,i] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_lt_solve_test ( ):

#*****************************************************************************80
#
## r8mat_lt_solve_test() tests r8mat_lt_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  a = np.array ( [ \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 2.0,  3.0,  0.0,  0.0 ], \
    [ 4.0,  5.0,  6.0,  0.0 ], \
    [ 7.0,  8.0,  9.0, 10.0 ] ] )

  b = np.array ( [ 45.0, 53.0, 54.0, 40.0 ] )

  print ( '' )
  print ( 'r8mat_lt_solve_test():' )
  print ( '  r8mat_lt_solve() solves a transposed lower triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_lt_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( np.transpose ( a ), x ) - b

  rnorm = r8vec_norm ( n, r )

  print ( '' )
  print ( '  Norm of A\'*x-b = %g' % ( rnorm ) )

  return

def r8mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8mat_mm() multiplies two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8mat_mm_test ( ):

#*****************************************************************************80
#
## r8mat_mm_test() tests r8mat_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8mat_mm_test():' )
  print ( '  r8mat_mm() computes a matrix-matrix product C = A * B;' )

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8mat_mm ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B:' )

  return

def r8mat_mmt ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8mat_mmt() multiplies an R8MAT times a transposed R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N1,N2), B(N3,N2), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A * B'.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[j,k]

  return c

def r8mat_mmt_test ( ):

#*****************************************************************************80
#
## r8mat_mmt_test() tests r8mat_mmt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8mat_mmt_test():' )
  print ( '  r8mat_mmt() computes a matrix-matrix product C = A * B\';' )

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.copy ( a )

  c = r8mat_mmt ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n3, n2, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B\':' )

  return

def r8mat_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8mat_mtm() computes A' * B for two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A' * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8mat_mtm_test ( ):

#*****************************************************************************80
#
## r8mat_mtm_test() tests r8mat_mtm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8mat_mtm_test():' )
  print ( '  r8mat_mtm() computes a matrix-matrix product C = A\' * B;' )

  a = np.zeros ( ( n2, n1 ) )

  for i in range ( 0, n2 ): 
    for j in range ( 0, n1 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = a

  c = r8mat_mtm ( n1, n2, n3, a, b )

  r8mat_print ( n2, n1, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A\'*B:' )

  return

def r8mat_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8mat_mtv() multiplies a tranposed matrix times a vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the M by N matrix.
#
#    real X(M), the vector to be multiplied by A'.
#
#  Output:
#
#    real Y(N), the product A'*X.
#
  import numpy as np

  y = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      y[j] = y[j] + x[i] * a[i,j]

  return y

def r8mat_mtv_test ( ):

#*****************************************************************************80
#
## r8mat_mtv_test() tests r8mat_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 2

  a = np.array \
  ( \
    ( ( 1.0, 1.0 ), \
    ( 2.0, 1.0 ), \
    ( 3.0, 1.0 ), \
    ( 4.0, 1.0 ) ) \
  )
 
  x = np.array ( ( 1.0, 2.0, 3.0, 4.0 ) )

  print ( '' )
  print ( 'r8mat_mtv_test():' )
  print ( '  r8mat_mtv() computes a matrix-vector product b = A\' * x;' )

  b = r8mat_mtv ( m, n, a, x )

  r8mat_print ( m, n, a, '  A:' )
  r8vec_print ( m, x, '  X:' )
  r8vec_print ( n, b, '  B = A\'*X:' )

  return

def r8mat_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8mat_mv() multiplies a matrix times a vector.
#
#  Discussion:
#
#    In FORTRAN90, this operation can be more efficiently carried
#    out by the command
#
#      Y(1:M) = MATMUL ( A(1:M,1:N), X(1:N) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the M by N matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real Y(M), the product A*X.
#
  import numpy as np

  y = np.zeros ( m )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      y[i] = y[i] + a[i,j] * x[j]

  return y

def r8mat_mv_test ( ):

#*****************************************************************************80
#
## r8mat_mv_test() tests r8mat_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 2

  a = np.array \
  ( \
    ( ( 1.0, 1.0 ), \
    ( 2.0, 1.0 ), \
    ( 3.0, 1.0 ), \
    ( 4.0, 1.0 ) ) \
  )
 
  x = np.array ( ( 1.0, 2.0 ) )

  print ( '' )
  print ( 'r8mat_mv_test():' )
  print ( '  r8mat_mv() computes a matrix-vector product b = A * x;' )

  b = r8mat_mv ( m, n, a, x )

  r8mat_print ( m, n, a, '  A:' )
  r8vec_print ( n, x, '  X:' )
  r8vec_print ( m, b, '  B = A*X:' )

  return

def r8mat_nint ( m, n, a ):

#*****************************************************************************80
#
## r8mat_nint() rounds the entries of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real A(M,N), the matrix to be rounded.
#
#  Output:
#
#    real A(M,N), the rounded matrix.
#
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  return a

def r8mat_nint_test ( rng ):

#*****************************************************************************80
#
## r8mat_nint_test() tests r8mat_nint().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8mat_nint_test():' )
  print ( '  r8mat_nint() rounds an R8MAT.' )

  x1 = -5.0
  x2 = +5.0

  a = r8mat_uniform_ab ( m, n, x1, x2, rng )
  r8mat_print ( m, n, a, '  Matrix A:' )
  a = r8mat_nint ( m, n, a )
  r8mat_print ( m, n, a, '  Rounded matrix A:' )

  return

def r8mat_nonzeros ( m, n, a ):

#*****************************************************************************80
#
## r8mat_nonzeros() returns the number of nonzeros in an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    integer VALUE, the number of nonzeros.
#
  value = 0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( a[i,j] != 0.0 ):
        value = value + 1

  return value

def r8mat_nonzeros_test ( ):

#*****************************************************************************80
#
## r8mat_nonzeros_test() tests r8mat_nonzeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4
  a = np.zeros ( ( m, n ) )

  print ( '' )
  print ( 'r8mat_nonzeros_test():' )
  print ( '  r8mat_nonzeros() counts nonzeros in an R8MAT.' )

  c1 = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( ( i % 2 ) == 0 and ( j % 2 ) == 0 ):
        a[i,j] = 1.0
        c1 = c1 + 1
      else:
        a[i,j] = 0.0

  r8mat_print ( m, n, a, '  Matrix A:' )

  c2 = r8mat_nonzeros ( m, n, a )

  print ( '' )
  print ( '  Expected nonzeros = %d' % ( c1 ) )
  print ( '  Computed nonzeros = %d' % ( c2 ) )

  return

def r8mat_normal_01 ( m, n, rng ):

#*****************************************************************************80
#
## r8mat_normal_01() returns a unit pseudonormal R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(M,N), the pseudorandom values.
#
  import numpy as np

  x = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      x[i,j] = r8_normal_01 ( rng )

  return x

def r8mat_normal_01_test ( rng ):

#*****************************************************************************80
#
## r8mat_normal_01_test() tests r8mat_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  m = 5
  n = 4

  print ( '' )
  print ( 'r8mat_normal_01_test():' )
  print ( '  r8mat_normal_01() returns a matrix of Normal 01 values' )
  print ( '' )

  r = r8mat_normal_01 ( m, n, rng )

  r8mat_print ( m, n, r, '  Matrix:' )

  return

def r8mat_normal_ab ( m, n, mu, sigma ):

#*****************************************************************************80
#
## r8mat_normal_ab() returns a scaled pseudonormal R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real MU, SIGMA, the mean and standard deviation.
#
#  Output:
#
#    real X(M,N), the pseudorandom values.
#
  import numpy as np

  x = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      xi = r8_normal_01 ( )
      x[i,j] = mu + sigma * xi

  return x

def r8mat_normal_ab_test ( ):

#*****************************************************************************80
#
## r8mat_normal_ab_test() tests r8mat_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_normal_ab_test():' )
  print ( '  r8mat_normal_ab() returns a matrix of Normal AB values' )

  m = 5
  n = 4
  mu = 100.0
  sigma = 5.0

  print ( '' )
  print ( '  Mean = %g' % ( mu ) )
  print ( '  Standard deviation = %g' % ( sigma ) )

  r = r8mat_normal_ab ( m, n, mu, sigma )

  r8mat_print ( m, n, r, '  Matrix:' )

  return

def r8mat_norm_fro_affine ( m, n, a1, a2 ):

#*****************************************************************************80
#
## r8mat_norm_fro_affine() returns the Frobenius norm of an R8MAT difference.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    real A1(M,N), A2(M,N), the matrices for whose difference 
#    the Frobenius norm is desired.
#
#  Output:
#
#    real VALUE, the Frobenius norm of A1 - A2.
#
  import numpy as np
 
  value = np.sqrt ( sum ( sum ( ( a1 - a2 ) ** 2 ) ) )

  return value

def r8mat_norm_fro_affine_test ( rng ):

#*****************************************************************************80
#
## r8mat_norm_fro_affine_test() tests r8mat_norm_fro_affine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4
  a = r8mat_uniform_01 ( m, n, rng )
  b = r8mat_uniform_01 ( m, n, rng )

  print ( '' )
  print ( 'r8mat_norm_fro_affine_test():' )
  print ( '  r8mat_norm_fro_affine() computes the Frobenius norm' )
  print ( '  of the difference of two R8MAT\'s;' )

  t1 = 0.0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      t1 = t1 + ( a[i,j] - b[i,j] ) ** 2

  t1 = np.sqrt ( t1 );

  t2 = r8mat_norm_fro_affine ( m, n, a, b );

  print ( '' )
  print ( '  Expected norm = %g' % ( t1 ) )
  print ( '  Computed norm = %g' % ( t2 ) )

  return

def r8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## r8mat_norm_fro() returns the Frobenius norm of an R8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix whose Frobenius
#    norm is desired.
#
#  Output:
#
#    real VALUE, the Frobenius norm of A.
#
  import numpy as np
 
  value = np.sqrt ( sum ( sum ( a ** 2 ) ) )

  return value

def r8mat_norm_fro_test ( ):

#*****************************************************************************80
#
## r8mat_norm_fro_test() tests r8mat_norm_fro().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4

  a = np.zeros ( ( m, n ) )

  k = 0
  t1 = 0.0

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k
      t1 = t1 + k * k

  t1 = np.sqrt ( t1 )

  print ( '' )
  print ( 'r8mat_norm_fro_test():' )
  print ( '  r8mat_norm_fro() computes the Frobenius norm of an R8MAT;' )

  t2 = r8mat_norm_fro ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ( '' )
  print ( '  Expected Frobenius norm = %g' % ( t1 ) )
  print ( '  Computed Frobenius norm = %g' % ( t2 ) )

  return

def r8mat_norm_l1 ( m, n, a ):

#*****************************************************************************80
#
## r8mat_norm_l1() returns the matrix L1 norm of an R8MAT.
#
#  Discussion:
#
#    The matrix L1 norm is defined as:
#
#      value = max ( 1 <= J <= N ) sum ( 1 <= I <= M ) abs ( A(I,J) ).
#
#    The matrix L1 norm is derived from the vector L1 norm, and
#    satisifies:
#
#      vec_norm_l1 ( A * x ) <= mat_norm_l1 ( A ) * vec_norm_l1 ( x ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  value = 0.0

  for j in range ( 0, n ):
    row_sum = 0.0
    for i in range ( 0, m ):
      row_sum = row_sum + abs ( a[i,j] )
    value = max ( value, row_sum )

  return value

def r8mat_norm_l1_test ( rng ):

#*****************************************************************************80
#
## r8mat_norm_l1_test() tests r8mat_norm_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = 4
  x1 = -5.0
  x2 = +5.0

  a = r8mat_uniform_ab ( m, n, x1, x2, rng )
  
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  print ( '' )
  print ( 'r8mat_norm_l1_test():' )
  print ( '  r8mat_norm_l1() computes the L1 norm of an R8MAT;' )

  t = r8mat_norm_l1 ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ( '' )
  print ( '  Computed L1 norm = %g' % ( t ) )

  return

def r8mat_norm_li ( m, n, a ):

#*****************************************************************************80
#
## r8mat_norm_li() returns the matrix Loo norm of an R8MAT.
#
#  Discussion:
#
#    The matrix L-infinity norm is defined as:
#
#      value =  max ( 1 <= I <= M ) sum ( 1 <= J <= N ) abs ( A(I,J) ).
#
#    The matrix L-infinity norm is derived from the vector L-infinity norm,
#    and satisifies:
#
#      vec_norm_li ( A * x ) <= mat_norm_li ( A ) * vec_norm_li ( x ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  value = 0.0

  for i in range ( 0, m ):
    col_sum = 0.0
    for j in range ( 0, n ):
      col_sum = col_sum + abs ( a[i,j] )
    value = max ( value, col_sum )

  return value

def r8mat_norm_li_test ( rng ):

#*****************************************************************************80
#
## r8mat_norm_li_test() tests r8mat_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#

  m = 5
  n = 4
  x1 = -5.0
  x2 = +5.0

  a = r8mat_uniform_ab ( m, n, x1, x2, rng )
  
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  print ( '' )
  print ( 'r8mat_norm_li_test():' )
  print ( '  r8mat_norm_li() computes the Loo norm of an R8MAT;' )

  t = r8mat_norm_li ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )

  print ( '' )
  print ( '  Computed Loo norm = %g' % ( t ) )

  return

def r8mat_norm_rms ( A ):

#*****************************************************************************80
#
## r8mat_norm_rms() returns the Root-Mean-Square (RMS) norm of an R8MAT.
#
#  Discussion:
#
#    The RMS norm is defined as
#
#      value = sqrt ( ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 ) / N / M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the RMS norm of A.
#
  import numpy as np
 
  m, n = A.shape
  value = np.sqrt ( ( sum ( sum ( A ** 2 ) ) ) / m / n )

  return value

def r8mat_norm_rms_test ( ):

#*****************************************************************************80
#
## r8mat_norm_rms_test() tests r8mat_norm_rms().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4

  A = np.zeros ( ( m, n ) )

  k = 0
  t1 = 0.0

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      A[i,j] = k
      t1 = t1 + k * k

  t1 = np.sqrt ( t1 / m / n ) 

  print ( '' )
  print ( 'r8mat_norm_rms_test():' )
  print ( '  r8mat_norm_rms() computes the RMS norm of an R8MAT;' )

  t2 = r8mat_norm_rms ( A )

  r8mat_print ( m, n, A, '  A:' )
  print ( '' )
  print ( '  Expected RMS norm = ', t1 )
  print ( '  Computed RMS norm = ', t2 )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## r8mat_print_test() tests r8mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_print_test():' )
  print ( '  r8mat_print() prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )

  return

def r8mat_print_python3 ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print_python3() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some_python3 ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_python3_test ( ):

#*****************************************************************************80
#
## r8mat_print_python3_test() tests r8mat_print_python3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_print_python3_test():' )
  print ( '  r8mat_print_python3() prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_print_python3 ( m, n, v, '  Here is an R8MAT:' )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_print_some_test() tests r8mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_print_some_test():' )
  print ( '  r8mat_print_some() prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )

  return

def r8mat_print_some_python3 ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some_python3() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_print_some_python3_test() tests r8mat_print_some_python3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_print_some_python3_test():' )
  print ( '  r8mat_print_some_python3() prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_print_some_python3 ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )

  return

def r8mat_product_elementwise ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_product_elementwise() returns the elementwise produce to two R8MAT's.
#
#  Example:
#
#    A = [ 1, 2, 3;    B = [ 1, 3, 5;    product = 86
#          4, 5, 6 ]         2, 4, 6 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    real A(M,N), B(M,N), the two matrices.
#
#  Output:
#
#    real VALUE, the elementwise product of A and B.
#
  value = 0.0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      value = value + a[i,j] * b[i,j]

  return value

def r8mat_product_elementwise_test ( ):

#*****************************************************************************80
#
## r8mat_product_elementwise_test() tests r8mat_product_elementwise().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_product_elementwise_test():' )
  print ( '  r8mat_product_elementwise() computes the elementwise' )
  print ( '  product of two R8MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ] ] )

  b = np.array ( [ \
    [ 1.0, 3.0, 5.0 ], \
    [ 2.0, 4.0, 6.0 ] ])

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )

  t = r8mat_product_elementwise ( m, n, a, b )
 
  print ( '' );
  print ( '  Elementwise product = %g' % ( t ) )

  return

def r8mat_ref ( m, n, a ):

#*****************************************************************************80
#
## r8mat_ref() computes the row echelon form of a matrix.
#
#  Discussion:
#
#    A matrix is in row echelon form if:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#  Example:
#
#    Input matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#    -2.0 -6.0  0.0 -2.0 -8.0  3.0  1.0
#     3.0  9.0  0.0  0.0  6.0  6.0  2.0
#    -1.0 -3.0  0.0  1.0  0.0  9.0  3.0
#
#    Output matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#     0.0  0.0  0.0  1.0  2.0  4.5  1.5
#     0.0  0.0  0.0  0.0  0.0  1.0  0.3
#     0.0  0.0  0.0  0.0  0.0  0.0  0.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Cullen,
#    An Introduction to Numerical Linear Algebra,
#    PWS Publishing Company, 1994,
#    ISBN: 978-0534936903,
#    LC: QA185.D37.C85.
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix A.
#
#    real A(M,N), the matrix to be analyzed.
#
#  Output:
#
#    real A(M,N), the REF form of the matrix.
#
#    real DET, the pseudo-determinant.
#
  det = 1.0
  asum = 0.0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      asum = asum + abs ( a[i,j] )
  tol = r8_epsilon ( ) * asum
  lead = 0

  for r in range ( 0, m ):

    if ( n <= lead ):
      break
#
#  Seek I, the first nonzero entry in A[R:M,LEAD]
#
    i = r

    while ( a[i,lead] == 0.0 ):

      i = i + 1
#
#  If A[R:M,LEAD] is all 0, return to row R, and increment column LEAD.
#
      if ( m <= i ):
        i = r
        lead = lead + 1
#
#  If LEAD was the last column, set LEAD to -1 and break.
#
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break
#
#  Swap rows I and R.
#
    temp     = a[i,0:n]
    a[i,0:n] = a[r,0:n]
    a[r,0:n] = temp
#
#  Update pseudo-determinant.
#
    det = det * a[r,lead]
#
#  Normalize the row so A[R,LEAD] = 1.
#
    a[r,0:n] = a[r,0:n] / a[r,lead]
#
#  Use row R to zero out lower entries in column LEAD.
#
    for i in range ( r + 1, m ):
      a[i,0:n] = a[i,0:n] - a[i,lead] * a[r,0:n]
#
#  Prepare to handle next column.
#
    lead = lead + 1

  return a, det

def r8mat_ref_test ( ):

#*****************************************************************************80
#
## r8mat_ref_test() tests r8mat_ref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array( [ \
    [  1.0,  3.0,  0.0,  2.0,  6.0,  3.0,  1.0 ], \
    [ -2.0, -6.0,  0.0, -2.0, -8.0,  3.0,  1.0 ], \
    [  3.0,  9.0,  0.0,  0.0,  6.0,  6.0,  2.0 ], \
    [ -1.0, -3.0,  0.0,  1.0,  0.0,  9.0,  3.0 ] ] )

  print ( '' )
  print ( 'r8mat_ref_test():' )
  print ( '  r8mat_ref() computes the row echelon form of a matrix.' )

  r8mat_print ( m, n, a, '  Input A:' )

  a, det = r8mat_ref ( m, n, a )

  print ( '' )
  print ( '  Pseudo-determinat = ', det )

  r8mat_print ( m, n, a, '  REF form:' )

  return

def r8mat_rref ( m, n, a ):

#*****************************************************************************80
#
## r8mat_rref() computes the reduced row echelon form of a matrix.
#
#  Discussion:
#
#    A matrix is in row echelon form if:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Example:
#
#    Input matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#    -2.0 -6.0  0.0 -2.0 -8.0  3.0  1.0
#     3.0  9.0  0.0  0.0  6.0  6.0  2.0
#    -1.0 -3.0  0.0  1.0  0.0  9.0  3.0
#
#    Output matrix:
#
#     1.0  3.0  0.0  0.0  2.0  0.0  0.0
#     0.0  0.0  0.0  1.0  2.0  0.0  0.0
#     0.0  0.0  0.0  0.0  0.0  1.0  0.3
#     0.0  0.0  0.0  0.0  0.0  0.0  0.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Cullen,
#    An Introduction to Numerical Linear Algebra,
#    PWS Publishing Company, 1994,
#    ISBN: 978-0534936903,
#    LC: QA185.D37.C85.
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix A.
#
#    real A(M,N), the matrix to be analyzed. 
#
#  Output:
#
#    real  A(M,N), the RREF form of the matrix.
#
#    real DET, the pseudo-determinant.
#
  import numpy as np

  det = 1.0
  asum = 0.0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      asum = asum + abs ( a[i,j] )
  tol = asum * np.finfo(float).eps
  lead = 0

  for r in range ( 0, m ):

    if ( n <= lead ):
      break

    i = r

    while ( abs ( a[i,lead] ) <= tol ):

      i = i + 1

      if ( m <= i ):
        i = r
        lead = lead + 1
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break

    for j in range ( 0, n ):
      t      = a[i,j]
      a[i,j] = a[r,j]
      a[r,j] = t

    det = det * a[r,lead]
    a[r,0:n] = a[r,0:n] / a[r,lead]

    for i in range ( 0, m ):
      if ( i != r ):
        a[i,0:n] = a[i,0:n] - a[i,lead] * a[r,0:n]

    lead = lead + 1

  return a, det

def r8mat_rref_test ( ):

#*****************************************************************************80
#
## r8mat_rref_test() tests r8mat_rref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array( [ \
    [  1.0,  3.0,  0.0,  2.0,  6.0,  3.0,  1.0 ], \
    [ -2.0, -6.0,  0.0, -2.0, -8.0,  3.0,  1.0 ], \
    [  3.0,  9.0,  0.0,  0.0,  6.0,  6.0,  2.0 ], \
    [ -1.0, -3.0,  0.0,  1.0,  0.0,  9.0,  3.0 ] ] )

  print ( '' )
  print ( 'r8mat_rref_test():' )
  print ( '  r8mat_rref() computes the reduced row echelon form of a matrix.' )

  r8mat_print ( m, n, a, '  Input A:' )

  a, det = r8mat_rref ( m, n, a )

  print ( '' )
  print ( '  Pseudo-determinant = ', det )

  r8mat_print ( m, n, a, '  RREF form:' )

  return

def r8mat_rref_solve_binary_nz ( m, n, nz, a, b ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary_nz() seeks binary solutions of an RREF system.
#
#  Discussion:
#
#    Any acceptable binary solution must have exactly NZ nonzero entries.
#
#    An MxN linear system Ax = b is considered, in which only binary
#    solutions are allowed that is, each entry of x is either 0 or 1.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to row-reduced echelon form.  Therefore, the matrix A satisfies:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the rows and columns of the RREF matrix A.
#
#    integer NZ, the number of nonzeros required in any binary solution.
#
#    real A(M,N), the RREF matrix to be analyzed. 
#
#    real B(M), the RREF right hand side.
#
#  Output:
#
#    integer X_NUM, the number of binary solutions.
#    Note that there may be no binary solutions at all.
#
#    real X(N,X_NUM), the solutions.
#
  import numpy as np

  verbose = True
#
#  Remove the zero rows of A.
#
  while ( 0 < m ):
    if ( np.sum ( abs ( a[m-1,0:n] ) ) == 0.0 ):
      a = np.delete ( a, m-1, axis = 0 )
      m = m - 1
    else:
      break
#
#  Number of dimensions of freedom is n - m.
#
  klog = n - m

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  System has', klog, 'degrees of freedom.' )
#
#  Determine the indeterminate variables.
#  Insert corresponding data in A and B.
#
  freedom = np.zeros ( 0, dtype = int )

  if ( 0 < klog ):

    for j in range ( 0, n ):
      if ( j+1 <= m ):
        if ( a[j,j] != 1 ):
          r = r8vec_identity_row ( n, j )
          a = np.insert ( a, j, r, axis = 0 )
          b = np.insert ( b, j, 0, axis = 0 )
          freedom = np.append ( freedom, j )
          m = m + 1
      else:
        r = r8vec_identity_row ( n, j )
        a = np.append ( a, r, axis = 0 )
        b = np.append ( b, 0 )
        freedom = np.append ( freedom, j )
        m = m + 1
#
#  For debugging, print augmented system.
#
  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Augmented Row-Reduced Echelon Form system matrix A and right hand side B:' )
    print ( '  Columns associated with a free variable are headed with a "*"' )
    print ( '' )

    label = n * ':'
    label = list ( label )
    for k in range ( 0, klog ):
      j = freedom[k]
      label[j] = '*'

    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( ' ', label[j], end = '' )
    print ( '' )

    for i in range ( 0, m ):
      print ( '  ', end = '' )
      for j in range ( 0, n ):
        print ( '%2d' % ( a[i,j] ), end = '' )
      print ( '  %2d' % ( b[i] ) )
#
#  Initialize to "empty" a list of binary soutions.
#
#  There are KLOG degrees of freedom, each of which could be set to 1.
#  There must be NZ variables set to 1.
#  Consider setting NZ2 degrees of freedom to 1, where NZ2 is between 0
#  and the minimum of NZ and KLOG.
#
#  Choose every possible selection of NZ2 degrees of freedom, and solve
#  the system.
#
#  If the resulting solution is binary, then add it to the list.
#
  x_num = 0
  x = np.zeros ( [ n, 0 ], dtype = float )
  b_num = 0

  nz2_max = min ( nz, klog )

  for nz2 in range ( 0, nz2_max + 1 ):

    done = True
    free_sub = np.zeros ( nz2_max )

    while ( True ):

      free_sub, done = ksub_next4 ( klog, nz2, free_sub, done )

      if ( done ):
        break

      b2 = np.copy ( b )
      b2[freedom[free_sub[0:nz2]-1]] = 1
      b_num = b_num + 1

      y = r8mat_u_solve ( n, a, b2 )

      if ( r8vec_is_binary ( n, y ) ):
        y = np.reshape ( y, ( n, 1 ) )
        x = np.append ( x, y, axis = 1 )
        x_num = x_num + 1

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Tried', b_num, 'right hands sides, found', x_num, 'solutions.' )

  return x_num, x

def r8mat_rref_solve_binary_nz_test ( ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary_nz_test() tests r8mat_rref_solve_binary_nz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_rref_solve_binary_nz_test():' )
  print ( '  r8mat_rref_solve_binary_nz() seeks binary solutions of' )
  print ( '  a Reduced Row Echelon Form linear system A*x=b' )
  print ( '  which have exactly NZ nonzeros.' )

  m = 9
  n = 10

  a = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 1, 0,-1, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 1, 0, 0, 0, 1, 0,-1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 1, 1 ], \
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ], \
    [ 0, 0, 0, 0, 0, 1,-1, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 1, 0,-1 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ] )

  r8mat_print ( m, n, a, '  The RREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  r8vec_print ( m, b, '  The RREF right hand side b:' )

  nz = 4
  print ( '' )
  print ( '  Only consider binary solutions with exactly', nz, 'nonzeros.' )

  x_num, x = r8mat_rref_solve_binary_nz ( m, n, nz, a, b )

  r8mat_print ( n, x_num, x, '  Binary solution vectors x:' )

  return

def r8mat_rref_solve_binary ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary() seeks binary solutions of an RREF system.
#
#  Discussion:
#
#    An MxN linear system Ax = b is considered, in which only binary
#    solutions are allowed that is, each entry of x is either 0 or 1.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to row-reduced echelon form.  Therefore, the matrix A satisfies:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the rows and columns of the RREF matrix A.
#
#    real A(M,N), the RREF matrix to be analyzed. 
#
#    real B(M), the RREF right hand side.
#
#  Output:
#
#    integer X_NUM, the number of binary solutions.
#    Note that there may be no binary solutions at all.
#
#    real X(N,X_NUM), the solutions.
#
  import numpy as np
#
#  Remove the zero rows of A.
#
  while ( 0 < m ):
    if ( np.sum ( abs ( a[m-1,0:n] ) ) == 0.0 ):
      a = np.delete ( a, m-1, axis = 0 )
      m = m - 1
    else:
      break
#
#  Number of dimensions of freedom is n - m.
#
  klog = n - m
#
#  Determine the indeterminate variables.
#  Insert corresponding data in A and B.
#
  freedom = np.zeros ( 0, dtype = int )

  if ( 0 < klog ):

    for j in range ( 0, n ):
      if ( j+1 <= m ):
        if ( a[j,j] != 1 ):
          r = r8vec_identity_row ( n, j )
          a = np.insert ( a, j, r, axis = 0 )
          b = np.insert ( b, j, 0, axis = 0 )
          freedom = np.append ( freedom, j )
          m = m + 1
      else:
        r = r8vec_identity_row ( n, j )
        a = np.append ( a, r, axis = 0 )
        b = np.append ( b, 0 )
        freedom = np.append ( freedom, j )
        m = m + 1
#
#  The indeterminate variables have a simple equation 
#    x(i) = b(i) = 0 or 1
#  Set up and solve every variation of this system.
#  If a solution is binary, accept it.
#
  x_num = 0
  x = np.zeros ( [ n, 0 ], dtype = float )

  binary = np.zeros ( klog )

  while ( True ):

    b2 = b
    for k in range ( 0, klog ):
      i = freedom[k]
      b2[i] = binary[k]

    y = r8mat_u_solve ( n, a, b2 )

    if ( r8vec_is_binary ( n, y ) ):
      y = np.reshape ( y, ( n, 1 ) )
      x = np.append ( x, y, axis = 1 )
      x_num = x_num + 1

    binary = r8vec_binary_next ( klog, binary )

    if ( np.sum ( binary ) == 0 ):
      break

  return x_num, x

def r8mat_rref_solve_binary_test ( ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary_test() tests r8mat_rref_solve_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_rref_solve_binary_test():' )
  print ( '  r8mat_rref_solve_binary() seeks binary solutions of' )
  print ( '  a Reduced Row Echelon Form linear system A*x=b.' )

  m = 9
  n = 10

  a = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 1, 0,-1, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 1, 0, 0, 0, 1, 0,-1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 1, 1 ], \
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ], \
    [ 0, 0, 0, 0, 0, 1,-1, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 1, 0,-1 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ] )

  r8mat_print ( m, n, a, '  The RREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  r8vec_print ( m, b, '  The RREF right hand side b:' )

  x_num, x = r8mat_rref_solve_binary ( m, n, a, b )

  r8mat_print ( n, x_num, x, '  Binary solution vectors x:' )

  return

def r8mat_scale_01 ( m, n, x ):

#*****************************************************************************80
#
## r8mat_scale_01() scales the columns of an R8MAT to [0,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of entries in the vector.
#
#    real X(M,N), the array to be scaled.
#
#  Output:
#
#    real XS(M,N), the scaled array.
#
  import numpy as np

  xmin = np.ndarray.min ( x, axis = 0 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xs = np.zeros ( [ m, n ] )
  for j in range ( 0, n ):
    if ( 0.0 < xmax[j] - xmin[j] ):
      xs[0:m,j] = ( x[0:m,j] - xmin[j] ) / ( xmax[j] - xmin[j] )
    else:
      xs[0:m,j] = 0.5

  return xs

def r8mat_scale_01_test ( rng ):

#*****************************************************************************80
#
## r8mat_scale_01_test() tests r8mat_scale_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_scale_01_test():' )
  print ( '  r8mat_scale_01() shifts and scales the columns of an R8MAT' )
  print ( '  so they each have min 0 and max 1' )

  m = 5
  n = 3
  a = -5.0
  b = 15.0

  x = r8mat_uniform_ab ( m, n, a, b, rng )
 
  r8mat_print ( m, n, x, '  Array X:' )
  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xmin = np.ndarray.min ( x, axis = 0 )
  print ( '' )
  r8vec_transpose_print ( n, mu, '  mean(X):' )
  r8vec_transpose_print ( n, sigma, '  std(X):' )
  r8vec_transpose_print ( n, xmax, '  max(X):' )
  r8vec_transpose_print ( n, xmin, '  min(X):' )

  xs = r8mat_scale_01 ( m, n, x )

  r8mat_print ( m, n, xs, '  Array XS:' )
  mu = np.mean ( xs, axis = 0 )
  sigma = np.std ( xs, axis = 0 )
  xmax = np.ndarray.max ( xs, axis = 0 )
  xmin = np.ndarray.min ( xs, axis = 0 )
  print ( '' )
  r8vec_transpose_print ( n, mu, '  mean(XS):' )
  r8vec_transpose_print ( n, sigma, '  std(XS):' )
  r8vec_transpose_print ( n, xmax, '  max(XS):' )
  r8vec_transpose_print ( n, xmin, '  min(XS):' )

  return

def r8mat_scale_ab ( m, n, x, a, b ):

#*****************************************************************************80
#
## r8mat_scale_ab() scales the columns of an R8MAT to [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of entries in the vector.
#
#    real X(M,N), the array to be scaled.
#
#    real A, B, the new minimum and maximum.
#
#  Output:
#
#    real XS(M,N), the scaled array.
#
  import numpy as np

  xmin = np.ndarray.min ( x, axis = 0 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xs = np.zeros ( [ m, n ] )
  for j in range ( 0, n ):
    if ( 0.0 < xmax[j] - xmin[j] ):
      xs[0:m,j] = a + ( b - a ) * ( x[0:m,j] - xmin[j] ) / ( xmax[j] - xmin[j] )
    else:
      xs[0:m,j] = ( a + b ) / 2.0

  return xs

def r8mat_scale_ab_test ( rng ):

#*****************************************************************************80
#
## r8mat_scale_ab_test() tests r8mat_scale_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  print ( '' )
  print ( 'r8mat_scale_ab_test():' )
  print ( '  r8mat_scale_ab() shifts and scales the columns of an R8MAT' )
  print ( '  so they each have min A and max B' )

  m = 5
  n = 3
  a = -5.0
  b = 15.0

  x = r8mat_uniform_ab ( m, n, a, b, rng )
 
  r8mat_print ( m, n, x, '  Array X:' )
  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xmin = np.ndarray.min ( x, axis = 0 )
  print ( '' )
  r8vec_transpose_print ( n, mu, '  mean(X):' )
  r8vec_transpose_print ( n, sigma, '  std(X):' )
  r8vec_transpose_print ( n, xmax, '  max(X):' )
  r8vec_transpose_print ( n, xmin, '  min(X):' )

  a = -1.0
  b = +1.0
  print ( '' )
  print ( '  Scaling data to [%g,%g]' % ( a, b ) )

  xs = r8mat_scale_ab ( m, n, x, a, b )

  r8mat_print ( m, n, xs, '  Array XS:' )
  mu = np.mean ( xs, axis = 0 )
  sigma = np.std ( xs, axis = 0 )
  xmax = np.ndarray.max ( xs, axis = 0 )
  xmin = np.ndarray.min ( xs, axis = 0 )
  print ( '' )
  r8vec_transpose_print ( n, mu, '  mean(XS):' )
  r8vec_transpose_print ( n, sigma, '  std(XS):' )
  r8vec_transpose_print ( n, xmax, '  max(XS):' )
  r8vec_transpose_print ( n, xmin, '  min(XS):' )

  return

def r8mat_solve ( n, nrhs, a ):

#*****************************************************************************80
#
## r8mat_solve() uses Gauss-Jordan elimination to solve an N by N linear system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NRHS, the number of right hand sides.  NRHS
#    must be at least 0.
#
#    real A(N,N+NRHS), contains in rows and
#    columns 1 to N the coefficient matrix, and in columns N+1 through
#    N+NRHS, the right hand sides.
#
#  Output:
#
#    real A(N,N+NRHS), the coefficient matrix
#    area has been destroyed, while the right hand sides have
#    been overwritten with the corresponding solutions.
#
#    integer INFO, singularity flag.
#    0, the matrix was not singular, the solutions were computed;
#    J, factorization failed on step J, and the solutions could not
#    be computed.
#
  info = 0

  for j in range ( 0, n ):
#
#  Choose a pivot row IPIVOT.
#
    ipivot = j
    apivot = a[j,j]

    for i in range ( j + 1, n ):
      if ( abs ( apivot ) < abs ( a[i,j] ) ):
        apivot = a[i,j]
        ipivot = i

    if ( apivot == 0.0 ):
      info = j
      return a, info
#
#  Interchange.
#
    for k in range ( 0, n + nrhs ):
      temp        = a[ipivot,k]
      a[ipivot,k] = a[j,k]
      a[j,k]      = temp
#
#  A(J,J) becomes 1.
#
    a[j,j] = 1.0
    for k in range ( j + 1, n + nrhs ):
      a[j,k] = a[j,k] / apivot;
#
#  A(I,J) becomes 0.
#
    for i in range ( 0, n ):

      if ( i != j ):

        factor = a[i,j]
        a[i,j] = 0.0
        for k in range ( j + 1, n + nrhs ):
          a[i,k] = a[i,k] - factor * a[j,k]

  return a, info

def r8mat_solve_test ( ):

#*****************************************************************************80
#
## r8mat_solve_test() tests r8mat_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  n = 3
  rhs_num = 2
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0, 14.0,  7.0 ], \
    [ 4.0, 5.0, 6.0, 32.0, 16.0 ], \
    [ 7.0, 8.0, 0.0, 23.0,  7.0 ] ] )

  print ( '' )
  print ( 'r8mat_solve_test():' )
  print ( '  r8mat_solve() solves linear systems.' )
#
#  Print out the matrix to be inverted.
#
  r8mat_print ( n, n + rhs_num, a, '  The linear system:' )
#
#  Solve the systems.
#
  a, info = r8mat_solve ( n, rhs_num, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( '  The input matrix was singular.' )
    print ( '  The solutions could not be computed.' )
    return

  r8mat_print ( n, n + rhs_num, a, '  Factored matrix and solutions:' )

  return

def r8mat_standardize ( m, n, x ):

#*****************************************************************************80
#
## r8mat_standardize() standardizes an R8MAT.
#
#  Discussion:
#
#    Each column of the output array has 0 mean and unit standard deviation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimensions of the array.
#
#    real X(M,N), the array to be standardized.
#
#  Output:
#
#    real XS(M,N), the standardized array.
#
  import numpy as np

  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0, ddof = 1 )
  xs = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    if ( sigma[j] != 0.0 ):
      xs[:,j] = ( xs[:,j] - mu[j] ) / sigma[j]

  return xs

def r8mat_standardize_test ( rng ):

#*****************************************************************************80
#
## r8mat_standardize_test() tests r8mat_standardize().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_standardize_test():' )
  print ( '  r8mat_standardize() shifts and scales an R8MAT so that' )
  print ( '  each column has zero mean and unit standard deviation.' )

  m = 10
  n = 3
  a = -5.0
  b = 15.0

  x = r8mat_uniform_ab ( m, n, a, b, rng )
 
  r8mat_print ( m, n, x, '  Vector X:' )
  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0, ddof = 1 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xmin = np.ndarray.min ( x, axis = 0 )
  print ( '' )
  print ( '  mean(X) = %g  %g  %g' % ( mu[0], mu[1], mu[2] ) )
  print ( '  std(X)  = %g  %g  %g' % ( sigma[0], sigma[1], sigma[2] ) )
  print ( '  max(X)  = %g  %g  %g' % ( xmax[0], xmax[1], xmax[2] ) )
  print ( '  min(X)  = %g  %g  %g' % ( xmin[0], xmin[1], xmin[2] ) )

  xs = r8mat_standardize ( m, n, x )

  r8mat_print ( m, n, xs, '  Vector XS:' )
  mu = np.mean ( xs, axis = 0 )
  sigma = np.std ( xs, axis = 0, ddof = 1 )
  xmax = np.ndarray.max ( xs, axis = 0 )
  xmin = np.ndarray.min ( xs, axis = 0 )
  print ( '' )
  print ( '  mean(X) = %g  %g  %g' % ( mu[0], mu[1], mu[2] ) )
  print ( '  std(X)  = %g  %g  %g' % ( sigma[0], sigma[1], sigma[2] ) )
  print ( '  max(X)  = %g  %g  %g' % ( xmax[0], xmax[1], xmax[2] ) )
  print ( '  min(X)  = %g  %g  %g' % ( xmin[0], xmin[1], xmin[2] ) )

  return

def r8mat_sub ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_sub() computes the difference of two matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrices.
#
#    real A(M,N), B(M,N), the matrices.
#
#  Output:
#
#    real C(M,N), the difference C = A - B.
#
  import numpy as np

  c = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m):
      c[i,j] = a[i,j] - b[i,j]

  return c

def r8mat_sub_test ( ):

#*****************************************************************************80
#
## r8mat_sub_test() tests r8mat_sub().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 4

  print ( '' )
  print ( 'r8mat_sub_test():' )
  print ( '  r8mat_sub() computes C = A - B;' )

  a = r8mat_indicator ( m, n )

  b = r8mat_transpose ( m, n, a )

  c = r8mat_sub ( m, n, a, b )

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A - B:' )

  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = float )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_transpose_print_some_test():' )
  print ( '  r8mat_transpose_print_some() prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  return

def r8mat_transpose ( m, n, a ):

#*****************************************************************************80
#
## r8mat_transpose() transposes an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real A(M,N), the matrix to be transposed.
#
#  Output:
#
#    real AT(N,M), the transposed matrix.
#
  import numpy as np

  at = np.zeros ( ( n, m ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      at[j,i] = a[i,j]

  return at

def r8mat_transpose_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_test() tests r8mat_transpose().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8mat_transpose_test():' )
  print ( '  r8mat_transpose() transposes an R8MAT.' )

  a = r8mat_indicator ( m, n )
  r8mat_print ( m, n, a, '  Matrix A:' )

  at = r8mat_transpose ( m, n, a )
  r8mat_print ( n, m, at, '  Transposed matrix At:' )

  return

def r8mat_u1_inverse ( A ):

#*****************************************************************************80
#
## r8mat_u1_inverse() inverts a unit upper triangular R8MAT.
#
#  Discussion:
#
#    A unit upper triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's below the main diagonal.
#
#    The inverse of a unit upper triangular matrix is also
#    a unit upper triangular matrix.
#
#    This routine can invert a matrix in place, that is, with no extra
#    storage.  If the matrix is stored in A, then the call
#
#      call r8mat_u1_inverse ( n, a, a )
#
#    will result in A being overwritten by its inverse.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    real A(N,N), the unit upper triangular matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np

  n = np.size ( A, 0 )

  B = np.zeros ( [ n, n ] )

  for j in range ( n - 1, -1, -1 ):

    for i in range ( n - 1, -1, -1 ):

      if ( j < i ):
        B[i,j] = 0.0
      elif ( i == j ):
        B[i,j] = 1.0
      else:
        B[i,j] = - np.sum ( A[i,i+1:j+1] * B[i+1:j+1,j] )


  return B

def r8mat_u1_inverse_test ( ):

#*****************************************************************************80
#
## r8mat_u1_inverse_test() tests r8mat_u1_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
#
#  Each row of this definition is a COLUMN of the matrix.
#
  A = np.array ( [ \
    [ 1.0, 2.0, 0.0, 5.0, 0.0, 75.0 ], \
    [ 0.0, 1.0, 0.0, 0.0, 0.0,  0.0 ], \
    [ 0.0, 0.0, 1.0, 3.0, 0.0,  0.0 ], \
    [ 0.0, 0.0, 0.0, 1.0, 0.0,  6.0 ], \
    [ 0.0, 0.0, 0.0, 0.0, 1.0,  4.0 ], \
    [ 0.0, 0.0, 0.0, 0.0, 0.0,  1.0 ] ] )

  print ( '' )
  print ( 'r8mat_u1_inverse_test():' )
  print ( '  r8mat_u1_inverse() inverts a unit upper triangular matrix.' )

  r8mat_print ( n, n, A, '  Input matrix A' )
 
  B = r8mat_u1_inverse ( A )
 
  r8mat_print ( n, n, B, '  Inverse matrix B:' )

  C = np.matmul ( A, B )

  r8mat_print ( n, n, C, '  Product C = A * B:' )

  return

def r8mat_u_inverse ( n, a ):

#*****************************************************************************80
#
## r8mat_u_inverse() inverts an upper triangular R8MAT.
#
#  Discussion:
#
#    An upper triangular matrix is a matrix whose only nonzero entries
#    occur on or above the diagonal.
#
#    The inverse of an upper triangular matrix is an upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2017
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, number of rows and columns in the matrix.
#
#    real A(N,N), the upper triangular matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for j in range ( n - 1, -1, -1 ):
    for i in range ( n - 1, -1, -1 ):

      if ( i == j ):
        b[i,j] = 1.0 / a[i,j]
      elif ( i < j ):
        b[i,j] = - np.dot ( a[i,i+1:n],  b[i+1:n,j] ) / a[i,i]

  return b

def r8mat_u_inverse_test ( ):

#*****************************************************************************80
#
## r8mat_u_inverse_test() tests r8mat_u_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  a = np.array ( [ \
    [ 1.0, 2.0, 4.0,  7.0 ], \
    [ 0.0, 3.0, 5.0,  8.0 ], \
    [ 0.0, 0.0, 6.0,  9.0 ], \
    [ 0.0, 0.0, 0.0, 10.0 ] ] )

  print ( '' )
  print ( 'r8mat_u_inverse_test():' )
  print ( '  r8mat_u_inverse() inverts an upper triangular matrix.' )

  r8mat_print ( n, n, a, '  Input matrix A' )
 
  b = r8mat_u_inverse ( n, a )
 
  r8mat_print ( n, n, b, '  Inverse matrix B:' )
 
  c = np.dot ( a, b )

  r8mat_print ( n, n, c, '  Product C = A * B:' )

  return

def r8mat_uniform_01 ( m, n, rng ):

#*****************************************************************************80
#
## r8mat_uniform_01() returns a unit pseudorandom R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
  r = rng.random ( size = [ m, n ] )

  return r

def r8mat_uniform_01_test ( rng ):

#*****************************************************************************80
#
## r8mat_uniform_01_test() tests r8mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4

  print ( '' )
  print ( 'r8mat_uniform_01_test():' )
  print ( '  r8mat_uniform_01() computes a random R8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
 
  v = r8mat_uniform_01 ( m, n, rng )

  r8mat_print ( m, n, v, '  Random R8MAT:' )

  return

def r8mat_uniform_ab ( m, n, a, b, rng ):

#*****************************************************************************80
#
## r8mat_uniform_ab() returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A, B, the range of the pseudorandom values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
  import numpy as np

  r = a + ( b - a ) * rng.random ( size = [ m, n ] )

  return r

def r8mat_uniform_ab_test ( rng ):

#*****************************************************************************80
#
## r8mat_uniform_ab_test() tests r8mat_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4
  a = -1.0
  b = +5.0

  print ( '' )
  print ( 'r8mat_uniform_ab_test():' )
  print ( '  r8mat_uniform_ab() computes a random R8MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )

  v = r8mat_uniform_ab ( m, n, a, b, rng )

  r8mat_print ( m, n, v, '  Random R8MAT:' )

  return

def r8mat_uniform_abvec ( m, n, a, b, rng ):

#*****************************************************************************80
#
## r8mat_uniform_abvec() returns a random matrix with row ranges.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M), B(M), the range of the pseudorandom values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
  import numpy as np

  r = rng.random ( size = [ m, n ] )

  for i in range ( 0, m ):
    r[i,0:n] = a[i] + ( b[i] - a[i] ) * r[i,0:n]

  return r

def r8mat_uniform_abvec_test ( rng ):

#*****************************************************************************80
#
## r8mat_uniform_abvec_test() tests r8mat_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4
  a = np.array ( [  2.0, 0.0, -1.0, 100.0, 0.1 ] )
  b = np.array ( [ 10.0, 1.0,  0.0, 110.0, 0.2 ] )

  print ( '' )
  print ( 'r8mat_uniform_abvec_test():' )
  print ( '  r8mat_uniform_abvec() computes a random R8MAT.' )

  r8vec2_print ( a, b, '  Lower and upper row limits:' )

  v = r8mat_uniform_abvec ( m, n, a, b, rng )

  r8mat_print ( m, n, v, '  Random R8MAT:' )

  return

def r8mat_u_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_u_solve() solves an upper triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#    real A(N,N), the N by N upper triangular matrix.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np
#
#  Solve U * x = b.
#
  x = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    x[i] = b[i]
    for j in range ( i + 1, n ):
      x[i] = x[i] - a[i,j] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_u_solve_test ( ):

#*****************************************************************************80
#
## r8mat_u_solve_test() tests r8mat_u_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  a = np.array ( [ \
    [ 1.0,  2.0,  4.0,  7.0 ], \
    [ 0.0,  3.0,  5.0,  8.0 ], \
    [ 0.0,  0.0,  6.0,  9.0 ], \
    [ 0.0,  0.0,  0.0, 10.0 ] ] )

  b = np.array ( [ 45.0, 53.0, 54.0, 40.0 ] )

  print ( '' )
  print ( 'r8mat_u_solve_test():' )
  print ( '  r8mat_u_solve() solves an upper triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_u_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = r8vec_norm ( n, r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )

  return

def r8mat_ut_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_ut_solve() solves a transposed upper triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#    Given the upper triangular matrix A, the linear system to be solved is:
#
#      A' * x = b
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns
#    of the matrix.
#
#    real A(N,N), the N by N upper triangular matrix.
#
#    real B(N,1), the right hand side of the linear system.
#
#  Output:
#
#    real X(N,1), the solution of the linear system.
#
  import numpy as np
#
#  Solve U' * x = b.
#
  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
    for j in range ( 0, i ):
      x[i] = x[i] - a[j,i] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_ut_solve_test ( ):

#*****************************************************************************80
#
## r8mat_ut_solve_test() tests r8mat_ut_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  a = np.array ( [ \
    [ 1.0,  2.0,  4.0,  7.0 ], \
    [ 0.0,  3.0,  5.0,  8.0 ], \
    [ 0.0,  0.0,  6.0,  9.0 ], \
    [ 0.0,  0.0,  0.0, 10.0 ] ] )

  b = np.array ( [ 1.0, 8.0, 32.0, 90.0 ] )

  print ( '' )
  print ( 'r8mat_ut_solve_test():' )
  print ( '  r8mat_ut_solve() solves a transposed upper triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_ut_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( np.transpose ( a ), x ) - b

  rnorm = r8vec_norm ( n, r )

  print ( '' )
  print ( '  Norm of A\'*x-b = %g' % ( rnorm ) )

  return

def r8mat_vand2 ( m, n, x ):

#*****************************************************************************80
#
## r8mat_vand2() returns the N by N row Vandermonde matrix A.
#
#  Discussion:
#
#    The row Vandermonde matrix returned by this routine reads "across"
#    rather than down.  In particular, each row begins with a 1, followed by
#    some value X, followed by successive powers of X.
#
#  Formula:
#
#    A(I,J) = X(I)^(J-1)
#
#  Properties:
#
#    A is nonsingular if, and only if, the X values are distinct.
#
#    The determinant of A is
#
#      det(A) = product ( 2 <= I <= N ) (
#        product ( 1 <= J <= I-1 ) ( ( X(I) - X(J) ) ) ).
#
#    The matrix A is generally ill-conditioned.
#
#  Example:
#
#    N = 5, X = (2, 3, 4, 5, 6)
#
#    1 2  4   8   16
#    1 3  9  27   81
#    1 4 16  64  256
#    1 5 25 125  625
#    1 6 36 216 1296
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix desired.
#
#    real X(M), the values that define A.
#
#  Output:
#
#    real A(M,N), the M by N row Vandermonde matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  
  for i in range ( 0, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = a[i,j-1] * x[i]

  return a

def r8mat_vand2_test ( ):

#*****************************************************************************80
#
## r8mat_vand2_test() tests r8mat_vand2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8mat_vand2_test():' )
  print ( '  r8mat_vand2() returns a row Vandermonde matrix.' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The factor vector X:' )

  a = r8mat_vand2 ( m, n, x )
  r8mat_print ( m, n, a, '  The row Vandermonde matrix:' )

  return

def r8_max ( a, b ):

#*****************************************************************************80
#
## r8_max() returns the maximum of two R8's.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, values to compare.
#
#  Output:
#
#    real VALUE, the maximum of A and B.
#
  if ( a < b ):
    value = b
  else:
    value = a

  return value

def r8_max_test ( rng ):

#*****************************************************************************80
#
## r8_max_test() tests r8_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_max_test():' )
  print ( '  r8_max() computes the maximum of two R8\'s.' )

  r8_lo = - 10.0
  r8_hi = + 10.0

  print ( '' )
  print ( '     A         B         C=r8_max(A,B)' )
  print ( '' )
  for i in range ( 0, 10 ):
    a = r8_uniform_ab ( r8_lo, r8_hi, rng )
    b = r8_uniform_ab ( r8_lo, r8_hi, rng )
    c = r8_max ( a, b )
    print ( '  %8g  %8g  %8g' % ( a, b, c ) )

  return

def r8_min ( a, b ):

#*****************************************************************************80
#
## r8_min() returns the minimum of two R8's.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, values to compare.
#
#  Output:
#
#    real VALUE, the minimum of A and B.
#
  if ( a < b ):
    value = a
  else:
    value = b

  return value

def r8_min_test ( rng ):

#*****************************************************************************80
#
## r8_min_test() tests r8_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_min_test():' )
  print ( '  r8_min() computes the minimum of two R8\'s.' )

  r8_lo = - 10.0
  r8_hi = + 10.0

  print ( '' )
  print ( '     A         B         C=r8_min(A,B)' )
  print ( '' )
  for i in range ( 0, 10 ):
    a = r8_uniform_ab ( r8_lo, r8_hi, rng )
    b = r8_uniform_ab ( r8_lo, r8_hi, rng )
    c = r8_min ( a, b )
    print ( '  %8g  %8g  %8g' % ( a, b, c ) )

  return

def r8_modp ( x, y ):

#*****************************************************************************80
#
## r8_modp() returns the nonnegative remainder of real division.
#
#  Discussion:
#
#    If
#      REM = r8_modp ( X, Y )
#      RMULT = ( X - REM ) / Y
#    then
#      X = Y * RMULT + REM
#    where REM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360.0) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, r8_modp(A,360.0) is between 0 and 360, always.
#
#  Example:
#
#        I         J     MOD r8_modp  r8_modp Factorization
#
#      107        50       7       7    107 =  2 *  50 + 7
#      107       -50       7       7    107 = -2 * -50 + 7
#     -107        50      -7      43   -107 = -3 *  50 + 43
#     -107       -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number to be divided.
#
#    real Y, the number that divides X.
#
#  Output:
#
#    real VALUE, the nonnegative remainder when X is divided by Y.
#
  import numpy as np

  if ( y == 0.0 ):
    print ( '' )
    print ( 'r8_modp - Fatal error!' )
    print ( '  r8_modp ( X, Y ) called with Y = %f' % ( y ) )
    raise Exception ( 'r8_modp - Fatal error!' )

  value = ( x % y )

  if ( value < 0.0 ):
    value = value + np.abs ( y )

  return value

def r8_modp_test ( rng ):

#*****************************************************************************80
#
## r8_modp_test() tests r8_modp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np
 
  test_num = 10

  print ( '' )
  print ( 'r8_modp_test():' )
  print ( '  r8_modp() returns the remainder after division.' )
  print ( '  Unlike the MATLAB MOD, r8_modp ( X, Y ) is positive.' )
  print ( '' )
  print ( '      X       Y      MOD(X,Y)  r8_modp(X,Y)' )
  print ( '' )

  x_lo = -10.0
  x_hi = +10.0

  for test in range ( 0, test_num ):

    x = x_lo + ( x_hi - x_lo ) * rng.random ( )
    y = x_lo + ( x_hi - x_lo ) * rng.random ( )

    z1 = ( x % y )
    z2 = r8_modp ( x, y )

    print ( '  %12f  %12f  %12f  %12f' % ( x, y, z1, z2 ) )

  return

def r8_mod ( x, y ):

#*****************************************************************************80
#
## r8_mod() returns the remainder of R8 division.
#
#  Formula:
#
#    If
#      REM = r8_mod ( X, Y )
#      RMULT = ( X - REM ) / Y
#    then
#      X = Y * RMULT + REM
#    where REM has the same sign as X, and abs ( REM ) < Y.
#
#  Example:
#
#        X         Y     r8_mod  r8_mod Factorization
#
#      107        50       7      107 =  2 *  50 + 7
#      107       -50       7      107 = -2 * -50 + 7
#     -107        50      -7     -107 = -2 *  50 - 7
#     -107       -50      -7     -107 =  2 * -50 - 7
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number to be divided.
#
#    real Y, the number that divides X.
#
#  Output:
#
#    real VALUE, the remainder when X is divided by Y.
#
  if ( y == 0.0 ):
    print ( '' )
    print ( 'r8_mod - Fatal error!' )
    print ( '  r8_mod ( X, Y ) called with Y = 0.' )
    raise Exception ( 'r8_mod - Fatal error!' )

  value = x - int ( x / y ) * y

  if ( x < 0.0 and 0.0 < value ):
    value = value - abs ( y )
  elif ( 0.0 < x and value < 0.0 ):
    value = value + abs ( y )

  return value

def r8_mod_test ( rng ):

#*****************************************************************************80
#
## r8_mod_test() tests r8_mod().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  test_num = 10

  print ( '' )
  print ( 'r8_mod_test():' )
  print ( '  r8_mod() returns the remainder after division.' )
  print ( '' )
  print ( '        X             Y             (X%Y)    r8_mod(X,Y)' )
  print ( '' )

  x_lo = -10.0
  x_hi = +10.0

  for test in range ( 0, test_num ):

    x = r8_uniform_ab ( x_lo, x_hi, rng )
    y = r8_uniform_ab ( x_lo, x_hi, rng )

    z1 = x % y
    z2 = r8_mod ( x, y )

    print ( '  %12f  %12f  %12f  %12f' % ( x, y, z1, z2 ) )

  return

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real r8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( rng ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_mop_test():' )
  print ( '  r8_mop() evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_MOP(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = 100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

  return

def r8_nint ( x ):

#*****************************************************************************80
#
## r8_nint() returns the nearest integer to an R8.
#
#  Example:
#
#        X        r8_nint
#
#      1.3         1
#      1.4         1
#      1.5         1 or 2
#      1.6         2
#      0.0         0
#     -0.7        -1
#     -1.1        -1
#     -1.6        -2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the value.
#
#  Output:
#
#    integer VALUE, the nearest integer to X.
#
  if ( x < 0.0 ):
    s = -1
  else:
    s = 1

  value = s * round ( abs ( x ) + 0.5 )

  return value

def r8_nint_test ( rng ):

#*****************************************************************************80
#
## r8_nint_test() tests r8_nint().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  test_num = 10

  print ( '' )
  print ( 'r8_nint_test():' )
  print ( '  r8_nint() produces the nearest integer.' )
  print ( '' )
  print ( '      X      r8_nint(X)' )
  print ( '' )

  b = -10.0
  c = +10.0

  for test  in range ( 0, test_num ):
    x = r8_uniform_ab ( b, c, rng )
    print ( '  %10f  %6d' % ( x, r8_nint ( x ) ) )

  return

def r8_normal_01 ( rng ):

#*****************************************************************************80
#
## r8_normal_01() samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X, a sample of the standard normal PDF.
#
  import numpy as np

  r1 = rng.random ( )
  r2 = rng.random ( )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return x

def r8_normal_01_test ( rng ):

#*****************************************************************************80
#
## r8_normal_01_test() tests r8_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  test_num = 20

  print ( '' )
  print ( 'r8_normal_01_test():' )
  print ( '  r8_normal_01() generates normally distributed random values.' )
  print ( '' )

  for test in range ( 0, test_num ):

    x = r8_normal_01 ( rng )
    print ( '  %f' % ( x ) )

  return

def r8_normal_ab ( a, b, rng ):

#*****************************************************************************80
#
## r8_normal_ab() returns a scaled pseudonormal R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the mean of the normal PDF.
#
#    real B, the standard deviation of the normal PDF.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X, a sample of the standard normal PDF.
#
  x = r8_normal_01 ( rng )
  x = a + b * x

  return x

def r8_normal_ab_test ( rng ):

#*****************************************************************************80
#
## r8_normal_ab_test() tests r8_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  x_mean = 100.0
  x_std = 10.0
  test_num = 20

  print ( '' )
  print ( 'r8_normal_ab_test():' )
  print ( '  r8_normal_ab() generates normally distributed values' )
  print ( '  with given mean and standard deviation.' )
  print ( '  MEAN = %g' % ( x_mean ) )
  print ( '  STD = %g' % ( x_std ) )
  print ( '' )

  for test in range ( 0, test_num ):

    x = r8_normal_ab ( x_mean, x_std, rng )
    print ( '  %g' % ( x ) )

  return

def r8_nth_root ( x, n ):

#*****************************************************************************80
#
## r8_nth_root() returns the nth-root of an R8.
#
#  Discussion:
#
#    The nth root of X is x^(1/n)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose Nth root is desired.
#
#    integer N, the index of the root.
#
#  Output:
#
#    real VALUE, the Nth root of X.
#
  import numpy as np
#
#  Potential Error 1: 0^0
#  But we will use it as 1.
#
  if ( x == 0.0 and n == 0 ):

    value = 1.0
#
#  Error 2: 0^(negative power)
#
  elif ( x == 0.0 and n < 0 ):

    value = np.inf
#
#  Error 3: (negative)^(even strictly positive root)
#
  elif ( x < 0.0 and ( n % 2 ) == 0 and 0 < n ):

    value = np.nan
#
#  X^0 = 1
#
  elif ( n == 0 ):

    value = 1.0
#
#  X^1 = X
#
  elif ( n == 1 ):

    value = x
#
#  X^(-1) = 1/X
#
  elif ( n == -1 ):

    value = 1.0 / x

  else:
  
    e = 1.0 / abs ( n )

    if ( 0.0 < x ):
      value = x ** e
    elif ( x == 0.0 ):
      value = 0.0
    else:
      value = - ( - x ) ** e

    if ( n < 0 ):
      value = 1.0 / value

  return value

def r8_nth_root_test ( ):

#*****************************************************************************80
#
## r8_nth_root_test() tests r8_nth_root().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_nth_root_test():' )
  print ( '  r8_nth_root() computes the nth root of an R8.' )
  print ( '' )
  print ( '         X        -3        -2        -1         0         1         2         3' )
  print ( '' )

  for i in range ( -3, 4 ):

    x = float ( i )
    print ( '  %8.4g' % ( x ), end = '' )

    for n in range ( -3, 4 ):
      y = r8_nth_root ( x, n )
      print ( '  %8.4g' % ( y ), end = '' )

    print ( '' )

  return

def r8_pi ( ):

#*****************************************************************************80
#
## r8_pi returns the value of pi as an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the value of pi.
#
  value = 3.141592653589793

  return value

def r8_pi_test ( ):

#*****************************************************************************80
#
## r8_pi_test() tests r8_pi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_pi_test():' )
  print ( '  r8_pi() returns the value of PI.' )
  print ( '' )
  v1 = r8_pi ( )
  print ( '  r8_pi       =       %24.16f' % ( v1 ) )
  v2 = 4.0 * np.arctan ( 1.0 )
  print ( '  4 * Atan(1) = %24.16f' % ( v2 ) )
  v3 = np.pi
  print ( '  np.pi       =       %24.16f' % ( v3 ) )

  return

def r8_pi_sqrt ( ):

#*****************************************************************************80
#
## r8_pi_sqrt() returns the square root of pi as an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the square root of pi.
#
  value = 1.7724538509055160273

  return value

def r8_pi_sqrt_test ( ):

#*****************************************************************************80
#
## r8_pi_sqrt_test() tests r8_pi_sqrt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_pi_sqrt_test():' )
  print ( '  r8_pi_sqrt() returns the square root of PI.' )
  print ( '' )
  print ( '  r8_pi_sqrt           = %24.16f' % ( r8_pi_sqrt ( ) ) )
  print ( '  sqrt ( 4 * Atan(1) ) = %24.16f' % ( np.sqrt ( 4.0 * np.arctan ( 1.0 ) ) ) )
  print ( '  sqrt ( NP.PI )       = %24.16f' % ( np.sqrt ( np.pi ) ) )
  print ( '' )
  print ( '  NP.PI                = %24.16f' % ( np.pi ) )
  print ( '  r8_pi_sqrt ** 2      = %24.16f' % ( r8_pi_sqrt ( ) ** 2 ) )

  return

def r8_power_fast ( r, p ):

#*****************************************************************************80
#
## r8_power_fast() computes the P-th power of R.
#
#  Discussion:
#
#    Obviously, R^P can be computed using P-1 multiplications.
#
#    However, R^P can also be computed using at most 2*LOG2(P) multiplications.
#    To do the calculation this way, let N = LOG2(P).
#    Compute A, A^2, A^4, ..., A^N by N-1 successive squarings.
#    Start the value of R^P at A, and each time that there is a 1 in
#    the binary expansion of P, multiply by the current result of the squarings.
#
#    This algorithm is not optimal.  For small exponents, and for special
#    cases, the result can be computed even more quickly.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the base.
#
#    integer P, the power, which may be negative.
#
#  Output:
#
#    real RP, the value of R^P.
#
#    integer MULTS, the number of multiplications and divisions.
#
  mults = 0
#
#  Force P to be an integer.
#
  p = int ( p )
#
#  Special bases.
#
  if ( r == 1.0 ):
    rp = 1.0
    return rp, mults

  if ( r == -1.0 ):

    if ( ( p % 2 ) == 1 ):
      rp = -1.0
    else:
      rp = 1.0

    return rp, mults

  if ( r == 0.0 ):

    if ( p <= 0 ):
      print ( '' )
      print ( 'r8_power_fast - Fatal error!' )
      print ( '  Base is zero, and exponent is negative.' )
      raise Exception ( 'r8_power_fast - Fatal error!' );

    rp = 0.0
    return rp, mults
#
#  Special powers.
#
  if ( p == -1 ):
    rp = 1.0 / r
    mults = mults + 1
    return rp, mults
  elif ( p == 0 ):
    rp = 1.0
    return rp, mults
  elif ( p == 1 ):
    rp = r
    return rp, mults
#
#  Some work to do.
#
  p_mag = abs ( p )
  p_sign = i4_sign ( p )

  rp = 1.0
  r2 = r

  while ( 0 < p_mag ):

    if ( ( p_mag % 2 ) == 1 ):
      rp = rp * r2
      mults = mults + 1

    p_mag = ( p_mag // 2 )
    r2 = r2 * r2
    mults = mults + 1

  if ( p_sign == -1 ):
    rp = 1.0 / rp
    mults = mults + 1

  return rp, mults

def r8_power_fast_test ( ):

#*****************************************************************************80
#
## r8_power_fast_test() tests r8_power_fast().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_power_fast_test():' )
  print ( '  r8_power_fast() computes R^P, economizing on' )
  print ( '  multiplications.' )
  print ( '' )
  print ( '      R          P       R^P        Mults' )
  print ( '' )

  for i in range ( -10, 41 ):

    r = 2.0
    p = i
    rp, mults = r8_power_fast ( r, p )
    print ( '  %12f  %5d  %12f  %5d' % ( r, p, rp, mults ) )

  return

def r8_power ( r, p ):

#*****************************************************************************80
#
## r8_power() computes the P-th power of R.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the base.
#
#    integer P, the power, which may be negative.
#
#  Output:
#
#    real VALUE, the value of R^P.
#
  mults = 0
#
#  Force P to be an integer.
#
  p = int ( p )
#
#  Special case.  R^0 = 1.
#
  if ( p == 0 ):
    value = 1.0
#
#  Special case.  Positive powers of 0 are 0.
#  For negative powers, we go ahead and compute it, hoping software will complain.
#
  elif ( r == 0.0 ):
    if ( 0 < p ):
      value = 0.0
    else:
      value = r ** p
  elif ( 1 <= p ):
    value = r ** p
  else:
    value = r ** p

  return value

def r8_power_test ( ):

#*****************************************************************************80
#
## r8_power_test() tests r8_power().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_power_test():' )
  print ( '  r8_power() computes R^P.' )
  print ( '' )
  print ( '      R          P       r8_power' )
  print ( '' )

  for i in range ( -5, 6 ):

    r = 2.0
    p = i
    value = r8_power ( r, p )
    print ( '  %14f  %5d  %14f' % ( r, p, value ) )

  return

def r8_print ( r, title ):

#*****************************************************************************80
#
## r8_print() prints an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the value to be printed.
#
#    string TITLE, a title.
#
  print ( '%s  %g' % ( title, r ) )

  return

def r8_print_test ( ):

#*****************************************************************************80
#
## r8_print_test() tests r8_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 October 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_print_test():' )
  print ( '  r8_print() prints an R8 with a label.' )
  print ( '' )
  r8_print ( np.pi, '  The value np.pi:' )
  r8_print ( 1.0, '  The value 1.0:' )
  r8_print ( -123456789, '  The value -123456789:' )
  r8_print ( 1.23456789, '  The value 1.23456789:' )

  return

def r8_radians ( degrees ):

#*****************************************************************************80
#
## r8_radians() converts an angle from degree to radian measure.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real RADIANS, the angle measurement in degrees.
#
#  Output:
#
#    real VALUE, the angle measurement in radians.
#
  import numpy as np

  value = degrees * np.pi / 180.0

  return value

def r8_radians_test ( ):

#*****************************************************************************80
#
## r8_radians_test() tests r8_radians().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 12

  print ( '' )
  print ( 'r8_radians_test():' )
  print ( '  r8_radians() converts an angle from degrees to radians.' )
  print ( '' )
  print ( '	 Degrees         Radians' )
  print ( '' )
  for test in range ( 0, 13 ):
    d = 180.0 * test / 12.0
    r = r8_radians ( d )
    print ( '  %14f  %14f' % ( d, r ) )

  return

def r8_relu ( x ):

#*****************************************************************************80
#
## r8_relu() evaluates the ReLU function of an R8.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#    The ReLU function is max(x,0.0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  if ( x <= 0.0 ):
    value = 0.0
  else:
    value = x

  return value

def r8_relu_test ( ):

#*****************************************************************************80
#
## r8_relu_test() tests r8_relu().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_relu_test():' )
  print ( '  r8_relu() evaluates the ReLU function of an R8.' )
  print ( '  This is max(x,0).' )
  print ( '' )
  print ( '      X             r8_relu(X)' )
  print ( '' )

  x_test = np.array ( [ \
    -500.0,   -50.0,    -5.0,    -4.0,     -3.0, \
      -2.0,    -1.0,    -0.5,    -0.05,    -0.005, \
      -0.0005,  0.0,     0.0005,  0.005,    0.05, \
       0.5,     1.0,     2.0,     3.0,      4.0, \
       5.0,    50.0,   500.0,  5000.0,  50000.0 ] )

  for i in range ( 0, 25 ):
    x = x_test[i]
    value = r8_relu ( x )
    print ( '  %10.6g  %10.6g' % ( x, value ) )

  return

def r8_rise ( x, n ):

#*****************************************************************************80
#
## r8_rise() computes the rising factorial function [X]^N.
#
#  Discussion:
#
#    [X]^N = X * ( X + 1 ) * ( X + 2 ) * ... * ( X + N - 1 ).
#
#    Note that the number of ways of arranging N objects in M ordered
#    boxes is [M]^N.  (Here, the ordering of the objects in each box matters).
#    Thus, 2 objects in 2 boxes have the following 6 possible arrangements:
#
#      -|12, 1|2, 12|-, -|21, 2|1, 21|-.
#
#    Moreover, the number of non-decreasing maps from a set of
#    N to a set of M ordered elements is [M]^N / N!.  Thus the set of
#    nondecreasing maps from (1,2,3) to (a,b,c,d) is the 20 elements:
#
#      aaa, abb, acc, add, aab, abc, acd, aac, abd, aad
#      bbb, bcc, bdd, bbc, bcd, bbd, ccc, cdd, ccd, ddd.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the rising factorial function.
#
#    integer N, the order of the rising factorial function.
#    If N = 0, RISE = 1, if N = 1, RISE = X.  Note that if N is
#    negative, a "falling" factorial will be computed.
#
#  Output:
#
#    real VALUE, the value of the rising factorial function.
#
  value = 1.0

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg + 1.0

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg - 1.0

  return value

def r8_rise_test ( ):

#*****************************************************************************80
#
## r8_rise_test() tests r8_rise().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_rise_test():' )
  print ( '  r8_rise() evaluates the rising factorial Rise(X,N).' )
  print ( '' )
  print ( '      X        N                     Exact                  Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, n, f1 = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_rise ( x, n )

    print ( '  %8.4g  %4d  %24.16g  %24.16g' % ( x, n, f1, f2 ) )

  return

def r8_rise_values ( n_data ):

#*****************************************************************************80
#
## r8_rise_values() returns values of the rising factorial function.
#
#  Discussion:
#
#    The rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) \ * ( m - 1 + n )
#            = Gamma ( m + n ) / Gamma ( m )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      Pochhammer[m,n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, integer N, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( [ 
       1680.000000000000, \
       1962.597656250000, \
       2279.062500000000, \
       2631.972656250000, \
       3024.000000000000, \
       1.000000000000000, \
       7.500000000000000, \
       63.75000000000000, \
       605.6250000000000, \
       6359.062500000000, \
       73129.21875000000, \
       914115.2343750000, \
       1.234055566406250E+07, \
       1.789380571289063E+08, \
       2.773539885498047E+09 ] )

  n_vec = np.array ( [ 
       4, \
       4, \
       4, \
       4, \
       4, \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9 ] )

  x_vec = np.array ( [ 
       5.00, \
       5.25, \
       5.50, \
       5.75, \
       6.00, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    n = 0
    f = 0.0
  else:
    x = x_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, n, f

def r8_rise_values_test ( ):

#*****************************************************************************80
#
## r8_rise_values_test() tests r8_rise_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_rise_values_test():' )
  print ( '  r8_rise_values() returns values of the rising factorial.' )
  print ( '' )
  print ( '          X         N          r8_rise(X,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, n, f = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8.4f  %8d  %24.16g' % ( x, n, f ) )

  return

def r8_round2 ( nplace, x ):

#*****************************************************************************80
#
## r8_round2() rounds a number to a specified number of binary digits.
#
#  Discussion:
#
#    Assume that the input quantity X has the form
#
#      X = S * J * 2^L
#
#    where S is plus or minus 1, L is an integer, and J is a binary
#    mantissa which is either exactly zero, or greater than or equal
#    to 0.5 and less than 1.0.
#
#    Then on return, XROUND will satisfy
#
#      XROUND = S * K * 2^L
#
#    where S and L are unchanged, and K is a binary mantissa which
#    agrees with J in the first NPLACE binary digits and is zero
#    thereafter.
#
#    If NPLACE is 0, XROUND will always be zero.
#
#    If NPLACE is 1, the mantissa of XROUND will be 0 or 0.5.
#
#    If NPLACE is 2, the mantissa of XROUND will be 0, 0.25, 0.50,
#    or 0.75.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPLACE, the number of binary digits to
#    preserve.  NPLACE should be 0 or positive.
#
#    real X, the number to be decomposed.
#
#  Output:
#
#    real XROUND, the rounded value of X.
#
  xround = 0.0
#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    return xround

  if ( nplace <= 0 ):
    return xround
#
#  2: Determine the sign S.
#
  if ( 0.0 < x ):
    s = 1
    xtemp = x
  else:
    s = -1
    xtemp = -x
#
#  3: Force XTEMP to lie between 1 and 2, and compute the
#  logarithm L.
#
  l = 0

  while ( 2.0 <= xtemp ):
    xtemp = xtemp / 2.0
    l = l + 1

  while ( xtemp < 1.0 ):
    xtemp = xtemp * 2.0
    l = l - 1
#
#  4: Strip out the digits of the mantissa as XMANT, and decrease L.
#
  xmant = 0.0
  iplace = 0

  while ( True ):

    xmant = 2.0 * xmant

    if ( 1.0 <= xtemp ):
      xmant = xmant + 1.0
      xtemp = xtemp - 1.0

    iplace = iplace + 1

    if ( xtemp == 0.0 or nplace <= iplace ):
      xround = s * xmant * 2.0 ** l
      break

    l = l - 1
    xtemp = xtemp * 2.0

  return xround

def r8_round2_test ( ):

#*****************************************************************************80
#
## r8_round2_test() tests r8_round2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  x = np.pi

  print ( '' )
  print ( 'r8_round2_test():' )
  print ( '  r8_round2() rounds a number to a' )
  print ( '  specified number of base 2 digits.' )
  print ( '' )
  print ( '  Test effect on PI.' )
  print ( '  X = %f' % ( x ) )
  print ( '' )
  print ( '  NPLACE  XROUND' )
  print ( '' )

  for i in range ( 0, 21 ):
    nplace = i
    xround = r8_round2 ( nplace, x )
    print ( '  %8d  %f' % ( i, xround ) )

  return

def r8_roundb ( ibase, nplace, x ):

#*****************************************************************************80
#
## r8_roundb() rounds a number to a given number of digits in a given base.
#
#  Discussion:
#
#    The code does not seem to do a good job of rounding when
#    the base is negative!
#
#    Assume that the input quantity X has the form
#
#      X = S * J * IBASE^L
#
#    where S is plus or minus 1, L is an integer, and J is a
#    mantissa base IBASE which is either exactly zero, or greater
#    than or equal to (1/IBASE) and less than 1.0.
#
#    Then on return, XROUND will satisfy
#
#      XROUND = S * K * IBASE^L
#
#    where S and L are unchanged, and K is a mantissa base IBASE
#    which agrees with J in the first NPLACE digits and is zero
#    thereafter.
#
#    Note that because of rounding, for most bases, most numbers
#    with a fractional quantities cannot be stored exactly in the
#    computer, and hence will have trailing "bogus" digits.
#
#    If NPLACE is 0, XROUND will always be zero.
#
#    If NPLACE is 1, the mantissa of XROUND will be 0,
#    1/IBASE, 2/IBASE, ..., (IBASE-1)/IBASE.
#
#    If NPLACE is 2, the mantissa of XROUND will be 0,
#    IBASE/IBASE^2, (IBASE+1)/IBASE^2, ...,
#    IBASE^2-2/IBASE^2, IBASE^2-1/IBASE^2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IBASE, the base of the arithmetic.
#    IBASE must not be zero.  Theoretically, IBASE may be negative.
#
#    integer NPLACE, the number of digits base IBASE to
#    preserve.  NPLACE should be 0 or positive.
#
#    real X, the number to be decomposed.
#
#  Output:
#
#    real XROUND, the rounded value of X.
#
  xround = 0.0
#
#  0: Error checks.
#
  if ( ibase == 0 ):
    print ( '' )
    print ( 'r8_roundb - Fatal error!' )
    print ( '  The base IBASE cannot be zero.' )
    raise Exception ( 'r8_roundb - Fatal error!' )
#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    return xround

  if ( nplace <= 0 ):
    return xround
#
#  2: Determine the sign IS.
#
  if ( 0.0 < x ):
    s = 1
    xtemp = x
  else:
    s = -1
    xtemp = -x
#
#  3: Force XTEMP to lie between 1 and ABS(IBASE), and compute the
#  logarithm L.
#
  l = 0

  while ( abs ( ibase ) <= abs ( xtemp ) ):

    xtemp = xtemp / ibase

    if ( xtemp < 0.0 ):
      s = - s
      xtemp = -xtemp

    l = l + 1

  while ( abs ( xtemp ) < 1.0 ):

    xtemp = xtemp * ibase

    if ( xtemp < 0.0 ):
      s = - s
      xtemp = -xtemp

    l = l - 1
#
#  4: Now strip out the digits of the mantissa as XMANT, and
#  decrease L.
#
  xmant = 0.0
  iplace = 0
  js = s

  while ( True ):

    xmant = ibase * xmant

    if ( xmant < 0.0 ):
      js = - js
      xmant = -xmant

    if ( 1.0 <= xtemp ):
      xmant = xmant + int ( xtemp )
      xtemp = xtemp - int ( xtemp )

    iplace = iplace + 1

    if ( xtemp == 0.0 or nplace <= iplace ):
      xround = js * xmant * ibase ** l
      break

    l = l - 1
    xtemp = xtemp * ibase

    if ( xtemp < 0.0 ):
      s = -s
      xtemp = -xtemp

  return xround

def r8_roundb_test ( ):

#*****************************************************************************80
#
## r8_roundb_test() tests r8_roundb().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  base = 3
  x = np.pi

  print ( '' )
  print ( 'r8_roundb_test():' )
  print ( '  r8_roundb() rounds a number to a' )
  print ( '  specified number of base BASE digits.' )
  print ( '' )
  print ( '  Here, we will use BASE = %d' % ( base ) )
  print ( '' )
  print ( '  Test effect on PI:' )
  print ( '  X = %f' % ( x ) )
  print ( '' )
  print ( '  NPLACE  XROUND' )
  print ( '' )

  for i in range ( 0, 21 ):
    nplace = i
    xround = r8_roundb ( base, nplace, x )
    print ( '  %8d  %f' % ( i, xround ) )

  print ( '' )
  print ( '  Try with a negative base:' )
  x = 121.0
  base = -3
  nplace = 3
  print ( '' )
  print ( '  Input quantity is X = %f' % ( x ) )
  print ( '  to be rounded in base %d' % ( base ) )

  for nplace in range ( 1, 6 ):

    xround = r8_roundb ( base, nplace, x )

    print ( '' )
    print ( '  Output value to %d places is %f' % ( nplace, xround ) )

  return

def r8_round_i4 ( x ):

#*****************************************************************************80
#
## r8_round_i4() rounds an R8 to the nearest integral value, returning an I4.
#
#  Discussion:
#
#    In MATLAB, it is essentially true that there is little difference between
#    this function and r8_round, because we store our integers in what amounts
#    to a real variable.
#
#  Example:
#
#        X        r8_round_i4
#
#      1.3         1
#      1.4         1
#      1.5         1 or 2
#      1.6         2
#      0.0         0
#     -0.7        -1
#     -1.1        -1
#     -1.6        -2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the value.
#
#  Output:
#
#    integer VALUE, the rounded value.
#
  if ( x < 0.0 ):
    value = - int ( - x + 0.5 )
  else:
    value =   int ( + x + 0.5 )

  return value

def r8_round ( x ):

#*****************************************************************************80
#
## r8_round() sets an R8 to the nearest integral value.
#
#  Example:
#
#        X        r8_round
#
#      1.3         1.0
#      1.4         1.0
#      1.5         1.0 or 2.0
#      1.6         2.0
#      0.0         0.0
#     -0.7        -1.0
#     -1.1        -1.0
#     -1.6        -2.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the value.
#
#  Output:
#
#    real VALUE, the rounded value.
#
  if ( x < 0.0 ):
    value = - int ( - x + 0.5 )
  else:
    value =   int ( + x + 0.5 )

  return value

def r8_round_test ( rng ):

#*****************************************************************************80
#
## r8_round_test() tests r8_round().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_round_test():' )
  print ( '  r8_round() rounds a real number to a real number with integer value.' )
  print ( '' )
  print ( '  X     XROUND' )
  print ( '' )
  s = + 1.0

  for i in range ( 0, 10 ):

    x = rng.random ( )
    x = s * 100.0 * x
    xround = r8_round ( x )
    print ( ' %f  %f' % ( x, xround ) )
    s = - s

  return

def r8_roundx ( nplace, x ):

#*****************************************************************************80
#
## r8_roundx() rounds an R8.
#
#  Discussion:
#
#    Assume that the input quantity X has the form
#
#      X = S * J * 10^L
#
#    where S is plus or minus 1, L is an integer, and J is a decimal
#    mantissa which is either exactly zero, or greater than or equal
#    to 0.1 and less than 1.0.
#
#    Then on return, XROUND will satisfy
#
#      XROUND = S * K * 10^L
#
#    where S and L are unchanged, and K is a decimal mantissa which
#    agrees with J in the first NPLACE decimal digits and is zero
#    thereafter.
#
#    Note that because of rounding, most decimal fraction quantities
#    cannot be stored exactly in the computer, and hence will have
#    trailing "bogus" digits.
#
#    If NPLACE is 0, XROUND will always be zero.
#
#    If NPLACE is 1, the mantissa of XROUND will be 0, 0.1,
#    0.2, ..., or 0.9.
#
#    If NPLACE is 2, the mantissa of XROUND will be 0, 0.01, 0.02,
#    0.03, ..., 0.98, 0.99.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPLACE, the number of decimal digits to
#    preserve.  NPLACE should be 0 or positive.
#
#    real X, the number to be decomposed.
#
#  Output:
#
#    real XROUND, the rounded value of X.
#
  xround = 0.0
#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    return xround

  if ( nplace <= 0 ):
    return xround
#
#  2: Determine the sign S.
#
  if ( 0.0 < x ):
    s = 1
    xtemp = x
  else:
    s = -1
    xtemp = -x
#
#  3: Force XTEMP to lie between 1 and 10, and compute the
#  logarithm L.
#
  l = 0

  while ( 10.0 <= x ):
    xtemp = xtemp / 10.0
    l = l + 1

  while ( xtemp < 1.0 ):
    xtemp = xtemp * 10.0
    l = l - 1
#
#  4: Now strip out the digits of the mantissa as XMANT, and
#  decrease L.
#
  xmant = 0.0
  iplace = 0

  while ( True ):

    xmant = 10.0 * xmant

    if ( 1.0 <= xtemp ):
      xmant = xmant + int ( xtemp )
      xtemp = xtemp - int ( xtemp )

    iplace = iplace + 1

    if ( xtemp == 0.0 or nplace <= iplace ):
      xround = s * xmant * 10.0 ** l
      break

    l = l - 1
    xtemp = xtemp * 10.0

  return xround

def r8_roundx_test ( rng ):

#*****************************************************************************80
#
## r8_roundx_test() tests r8_roundx().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  x = np.pi

  print ( '' )
  print ( 'r8_roundx_test():' )
  print ( '  r8_roundx() rounds a number to a' )
  print ( '  specified number of decimal digits.' )
  print ( '' )
  print ( '  Test effect on PI:' )
  print ( '  X = %f' % ( x ) )
  print ( '' )
  print ( '  NPLACE  XROUND' )
  print ( '' )

  for i in range ( 0, 11 ):
    nplace = i
    xround = r8_roundx ( nplace, x )
    print ( '  %6d  %f' % ( i, xround ) )

  print ( '' )
  print ( '  Test effect on random values:' )
  print ( '' )
  print ( '  NPLACE  X     XROUND' )
  print ( '' )

  for i in range ( 1, 6 ):

    x = rng.random ( )

    print ( '' )

    for i in range ( 0, 6 ):
      nplace = 2 * i
      xround = r8_roundx ( nplace, x )
      print ( '  %6d  %f  %f' % ( nplace, x, xround ) )

  return

def r8row_max ( m, n, x ):

#*****************************************************************************80
#
## r8row_max() returns the maximums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M,N), the R8ROW.
#
#  Output:
#
#    real XMAX(M), the maximums of the rows of X.
#
  import numpy as np

  xmax = np.zeros ( m )

  for i in range ( 0, m ):
    xmax[i] = x[i,0]
    for j in range ( 1, n ):
      xmax[i] = max ( xmax[i], x[i,j] )

  return xmax

def r8row_max_test ( ):

#*****************************************************************************80
#
## r8row_max_test() tests r8row_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_max_test():' )
  print ( '  r8row_max() computes maximums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  amax = r8row_max ( m, n, a )

  r8vec_print ( m, amax, '  Row maximums:' )

  return

def r8row_mean ( m, n, a ):

#*****************************************************************************80
#
## r8row_mean() returns the means of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the R8ROW
#
#  Output:
#
#    real ROW_mean(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def r8row_mean_test ( ):

#*****************************************************************************80
#
## r8row_mean_test() tests r8row_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_mean_test():' )
  print ( '  r8row_mean() computes row means of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  means = r8row_mean ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )

  return

def r8row_min ( m, n, x ):

#*****************************************************************************80
#
## r8row_min() returns the minimums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M,N), the R8ROW.
#
#  Output:
#
#    real XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def r8row_min_test ( ):

#*****************************************************************************80
#
## r8row_min_test() tests r8row_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_min_test():' )
  print ( '  r8row_min() computes minimums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  amin = r8row_min ( m, n, a )

  r8vec_print ( m, amin, '  Row minimums:' )

  return

def r8rows_to_r8mat ( m, n, r8rows ):

#*****************************************************************************80
#
## r8rows_to_r8mat() converts a row-major vector to an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, in column major order.
#
#    I am frustrated that the FORTRAN standard for initializing an array
#    forces me to enter a table of data by columns, so that I have to
#    transpose the information, which is confusing to me and any reader.
#
#    This function allows me to declare a vector of the right type and length,
#    fill it with data that I can display row-wise, and then have the
#    data copied into a column-major doubly-indexed array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real R8ROWS(M*N), the data. stored rowwise
#    in a vector.
#
#  Output:
#
#    real R8MAT(M,N), a copy of the data, stored
#    columnwise in an array.
#
  import numpy as np

  k = 0
  r8mat = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      r8mat[i,j] = r8rows[k]
      k = k + 1

  return r8mat

def r8rows_to_r8mat_test ( ):

#*****************************************************************************80
#
## r8rows_to_r8mat_test() tests r8rows_to_r8mat().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4
  r8rows = np.array ( [ \
    11.0, 12.0, 13.0, 14.0, \
    21.0, 22.0, 23.0, 24.0, \
    31.0, 32.0, 33.0, 34.0 ] )

  print ( '' )
  print ( 'r8rows_to_r8mat_test():' )
  print ( '  r8rows_to_r8mat() allows an R8MAT to be initialized' )
  print ( '  by data stored ROW-WISE in a vector.' )

  r8vec_print ( m * n, r8rows, '  The data vector:' )

  r8mat = r8rows_to_r8mat ( m, n, r8rows )

  r8mat_print ( m, n, r8mat, '  The data copied into an array:' )

  return

def r8row_uniform_abvec ( m, n, a, b, rng ):

#*****************************************************************************80
#
## r8row_uniform_abvec() returns a random matrix with column ranges.
#
#  Discussion:
#
#    An R8ROW is an array of R8 values, regarded as a set of row vectors.
#
#    The user specifies a minimum and maximum value for each column.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in
#    the array.
#
#    real A(N), B(N), the lower and upper limits.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R(M,N), the array of pseudorandom values.
#
  import numpy as np

  r = rng.random ( size = [ m, n ] )

  for j in range ( 0, n ):
    r[0:m,j] = a[j] + ( b[j] - a[j] ) * r[0:m,j]

  return r

def r8row_uniform_abvec_test ( rng ):

#*****************************************************************************80
#
## r8row_uniform_abvec_test() tests r8row_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 5
  n = 4
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1 ) )

  print ( '' )
  print ( 'r8row_uniform_abvec_test():' )
  print ( '  r8row_uniform_abvec() computes a random scaled R8ROW.' )
  print ( '' )
  print ( '   Col         Min         Max' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

  v = r8row_uniform_abvec ( m, n, a, b, rng )

  r8mat_print ( m, n, v, '  Random R8ROW:' )

  return

def r8row_variance ( m, n, x ):

#*****************************************************************************80
#
## r8row_variance() returns the variances of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real X(M,N), the R8ROW whose row means are desired.
#
#  Output:
#
#    real VARIANCE(M), the variances of the rows of X.
#
  import numpy as np

  variance = np.zeros ( m )

  for i in range ( 0, m ):

    mean = 0.0
    for j in range ( 0, n ):
      mean = mean + x[i,j]
    mean = mean / float ( n )

    for j in range ( 0, n ):
      variance[i] = variance[i] + ( x[i,j] - mean ) ** 2

    if ( 1 < n ):
      variance[i] = variance[i] / float ( n - 1 )
    else:
      variance[i] = 0.0 

  return variance

def r8row_variance_test ( ):

#*****************************************************************************80
#
## r8row_variance_test() tests r8row_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8row_variance_test():' )
  print ( '  r8row_variance() computes variances of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  variance = r8row_variance ( m, n, a )

  r8vec_print ( m, variance, '  The row variances:' )

  return

def r8_secd ( degrees ):

#*****************************************************************************80
#
## r8_secd() returns the secant of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DEGREES, the angle in degrees.
#
#  Output:
#
#    real VALUE, the secant of the angle.
#
  import numpy as np

  radians = np.pi * ( degrees / 180.0 )

  value = 1.0 / np.cos ( radians )

  return value

def r8_secd_test ( ):

#*****************************************************************************80
#
## r8_secd_test() tests r8_secd().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_secd_test():' )
  print ( '  r8_secd() computes the secant of an angle' )
  print ( '  given in degrees.' )
  print ( '' )
  print ( '  ANGLE    r8_secd(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( ( i + 90 ) % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_secd ( angle ) ) )

  return

def r8_sech ( x ):

#*****************************************************************************80
#
## r8_sech() evaluates the hyperbolic secant, while avoiding COSH overflow.
#
#  Discussion:
#
#    Oddly enough, the numpy library does not include the sech() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

  log_huge = 80.0

  if ( log_huge < abs ( x ) ):
    value = 0.0
  else:
    value = 1.0 / np.cosh ( x )

  return value

def r8_sech_test ( ):

#*****************************************************************************80
#
## r8_sech_test() tests r8_sech().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_sech_test():' )
  print ( '  r8_sech() computes the hyperbolic secant.' )
  print ( '' )
  print ( '  X    r8_sech(X)' )
  print ( '' )
 
  for i in range ( -10, 11 ):
    x = float ( i ) / 10.0
    fx = r8_sech ( x )
    print ( '  %10.4g  %14.6g' % ( x, fx ) )

  return

def r8_sigmoid ( l, b, m, x ):

#*****************************************************************************80
#
## r8_sigmoid() evaluates the sigmoid or logistic function.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#    The sigmoid function is useful for classification problems in
#    machine learning.  Its value is always between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real l, the maximum value of the function.  This is often 1.
#
#    real b, the cutoff value, where the function equals l/2.
#    This is often 0.
#
#    real m, the slope, which determines the steepness of the curve
#    and the width of the uncertainty interval.  This is often 1.
#
#    real x, the argument.
#
#  Output:
#
#    real value, the value.
#
  import numpy as np

  value = l / ( 1.0 + np.exp ( - m * ( x - b ) ) )

  return value

def r8_sigmoid_test ( ):

#*****************************************************************************80
#
## r8_sigmoid_test() tests r8_sigmoid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_sigmoid_test():' )
  print ( '  r8_sigmoid() evaluates the sigmoid function of R8.' )
  print ( '' )
  print ( '      X         r8_SIGMOID(L,B,M,X)' )
  print ( '' )

  x_test = np.array ( [ -4.0, -2.0, -1.0, -0.5, -0.25, 0.0, 0.25, 0.50, 1.0, 2.0, 4.0 ] )

  l = 1.0
  b = 0.0
  m = 1.0

  for i in range ( 0, 11 ):
    x = x_test[i]
    value = r8_sigmoid ( l, b, m, x )
    print ( '  %10.6g  %10.6g' % ( x, value ) )

  return

def r8_sign3 ( x ):

#*****************************************************************************80
#
## r8_sign3() returns the three-way sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive, 0 if zero, and -1 otherwise.
#
#    It would be better to use the numpy function sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  elif ( x == 0.0 ):
    value = 0.0;
  else:
    value = +1.0
 
  return value

def r8_sign3_test ( ):

#*****************************************************************************80
#
## r8_sign3_test() tests r8_sign3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign3_test():' )
  print ( '  r8_sign3() returns the three-way sign of an R8.' )
  print ( '' )
  print ( '    R8  r8_sign3(R8)' )
  print ( '' )

  for test in range ( 0, 5 ):
    r8 = r8_test[test]
    s = r8_sign3 ( r8 )
    print ( '  %8g  %8g' % ( r8, s ) )

  return

def r8_sign_char ( r8 ):

#*****************************************************************************80
#
## r8_sign_char() returns the sign of an R8 as a character.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R8, the value whose sign is of interest.
#
#  Output:
#
#    character C, is '-', '0', or '+'.

  if ( r8 < 0.0 ):
    c = '-'
  elif ( r8 == 0.0 ):
    c = '0'
  else:
    c = '+'

  return c

def r8_sign_char_test ( rng ):

#*****************************************************************************80
#
## r8_sign_char_test() tests r8_sign_char().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_sign_char_test():' )
  print ( '  r8_sign_char() returns the sign of an R8 as a character.' )
  print ( '' )
  print ( '      R8      r8_sign_CHAR(R8)' )
  print ( '' )

  for test in range ( 0, 10 ):
    r8 = r8_uniform_ab ( -5.0, +5.0, rng )
    s = r8_sign_char ( r8 )
    print ( '  %10f    %s' % ( r8, s ) )

  return

def r8_sign_match ( r1, r2 ):

#*****************************************************************************80
#
## r8_sign_match() is TRUE if two R8's are of the same sign.
#
#  Discussion:
#
#    This test could be coded numerically as
#
#      if ( 0 <= r1 * r2 ) then ...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R1, R2, the values to check.
#
#  Output:
#
#    bool VALUE, is TRUE if ( R1 <= 0 and R2 <= 0 )
#    or ( 0 <= R1 and 0 <= R2 ).
#
  value = ( r1 <= 0.0 and r2 <= 0.0 ) or ( 0.0 <= r1 and 0.0 <= r2 );

  return value

def r8_sign_match_test ( rng ):

#*****************************************************************************80
#
## r8_sign_match_test() tests r8_sign_match().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_sign_match_test():' )
  print ( '  r8_sign_match() is TRUE if two R8\'s have matching signs.' )
  print ( '' )
  print ( '        R1        R2        Match(R1,R2)?' )
  print ( '' )

  for test in range ( 0, 21 ):

    if ( ( test % 4 ) == 0 ):
      r1 = 0.0
    else:
      r1 = r8_uniform_ab ( -10.0, +10.0, rng )

    if ( ( test % 10 ) == 0 ):
      r2 = 0.0
    else:
      r2 = r8_uniform_ab ( -10.0, +10.0, rng )

    s = r8_sign_match ( r1, r2 )
    print ( '  %8.4f  %8.4f  %s' % ( r1, r2, s ) )

  return

def r8_sign_match_strict ( r1, r2 ):

#*****************************************************************************80
#
## r8_sign_match_strict() is TRUE if two R8's are of the same strict sign.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R1, R2, the values to check.
#
#  Output:
#
#    bool VALUE, is TRUE if the signs match.
#
  value = ( r1 <  0.0 and r2 <  0.0 ) or \
          ( r1 == 0.0 and r2 == 0.0 ) or \
          ( 0.0 <  r1 and 0.0 <  r2 )

  return value

def r8_sign_match_strict_test ( rng ):

#*****************************************************************************80
#
## r8_sign_match_strict_test() tests r8_sign_match_strict().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
# 
  print ( '' )
  print ( 'r8_sign_match_strict_test():' )
  print ( '  r8_sign_match_strict() is TRUE if two R8\'s have matching signs.' )
  print ( '' )
  print ( '        R1        R2        MatchStrict(R1,R2)?' )
  print ( '' )

  for test in range ( 0, 21 ):

    if ( ( test % 4 ) == 0 ):
      r1 = 0.0
    else:
      r1 = r8_uniform_ab ( -10.0, +10.0, rng )

    if ( ( test % 10 ) == 0 ):
      r2 = 0.0
    else:
      r2 = r8_uniform_ab ( -10.0, +10.0, rng )

    s = r8_sign_match_strict ( r1, r2 )
    print ( '  %8.4f  %8.4f  %s' % ( r1, r2, s ) )

  return

def r8_sign_opposite ( r1, r2 ):

#*****************************************************************************80
#
## r8_sign_opposite() is TRUE if two R8's are not of the same sign.
#
#  Discussion:
#
#    This test could be coded numerically as
#
#      if ( r1 * r2 <= 0.0 ) then ...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R1, R2, the values to check.
#
#  Output:
#
#    bool VALUE, is TRUE if ( R1 <= 0 and 0 <= R2 )
#    or ( R2 <= 0 and 0 <= R1 ).
#
  value = ( r1 <= 0.0 and 0.0 <= r2 ) or ( r2 <= 0.0 and 0.0 <= r1 )

  return value

def r8_sign_opposite_test ( rng ):

#*****************************************************************************80
#
## r8_sign_opposite_test() tests r8_sign_opposite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_sign_opposite_test():' )
  print ( '  r8_sign_opposite() is TRUE if two R8\'s have opposite signs.' )
  print ( '' )
  print ( '        R1        R2        Opposite(R1,R2)?' )
  print ( '' )

  for test in range ( 0, 21 ):

    if ( ( test % 4 ) == 0 ):
      r1 = 0.0
    else:
      r1 = r8_uniform_ab ( -10.0, +10.0, rng )

    if ( ( test % 10 ) == 0 ):
      r2 = 0.0
    else:
      r2 = r8_uniform_ab ( -10.0, +10.0, rng )
    s = r8_sign_opposite ( r1, r2 )
    print ( '  %8.4f  %8.4f  %s' % ( r1, r2, s ) )

  return

def r8_sign_opposite_strict ( r1, r2 ):

#*****************************************************************************80
#
## r8_sign_opposite_strict() is TRUE if two R8's are strictly of opposite sign.
#
#  Discussion:
#
#    This test could be coded numerically as
#
#      if ( r1 * r2 < 0.0 ) then ...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R1, R2, the values to check.
#
#  Output:
#
#    bool VALUE, is TRUE if ( R1 < 0 and 0 < R2 )
#    or ( R2 < 0 and 0 < R1 ).
#
  value = ( r1 < 0.0 and 0.0 < r2 ) or ( r2 < 0.0 and 0.0 < r1 );

  return value

def r8_sign_opposite_strict_test ( rng ):

#*****************************************************************************80
#
## r8_sign_opposite_strict_test() tests r8_sign_opposite_strict().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_sign_opposite_strict_test():' )
  print ( '  r8_sign_opposite_strict() is TRUE if two R8\'s have opposite signs.' )
  print ( '' )
  print ( '        R1        R2        OppositeStrict(R1,R2)?' )
  print ( '' )

  for test in range ( 0, 21 ):

    if ( ( test % 4 ) == 0 ):
      r1 = 0.0
    else:
      r1 = r8_uniform_ab ( -10.0, +10.0, rng )

    if ( ( test % 10 ) == 0 ):
      r2 = 0.0
    else:
      r2 = r8_uniform_ab ( -10.0, +10.0, rng )

    s = r8_sign_opposite_strict ( r1, r2 )
    print ( '  %8.4f  %8.4f  %s' % ( r1, r2, s ) )

  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#    It might be better to use the numpy function sign(), except that
#    np.sign(0) returns 0, whereas r8_sign(0) returns 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign_test():' )
  print ( '  r8_sign() returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )

  return

def r8_sincos_sum ( a, b ):

#*****************************************************************************80
#
## r8_sincos_sum() simplifies a*sin(cx)+b*cos(cx).
#
#  Discussion:
#
#    The expression
#      a * sin ( c * x ) + b * cos ( c * x )
#    can be rewritten as
#      d * sin ( c * x + e )
#    or
#      d * cos ( c * x + f ) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the coefficients in the linear combination.
#
#  Output:
#
#    real D, E, F, the new coefficient, and the shift for
#    sine or for cosine.
#
  import numpy as np

  d = np.sqrt ( a * a + b * b )
  e = np.arctan2 ( b, a )
  f = np.arctan2 ( b, a ) - np.pi / 2.0
  if ( f < - np.pi ):
    f = f + 2.0 * np.pi

  return d, e, f
  
def r8_sincos_sum_test ( rng ):

#*****************************************************************************80
#
## r8_sincos_sum_test() tests r8_sincos_sum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_sincos_sum_test():' )
  print ( '  r8_sincos_sum() simplifies a linear sine and cosine sum' )

  a = r8_uniform_ab ( -5.0, +5.0, rng )
  b = r8_uniform_ab ( -5.0, +5.0, rng )
  c = r8_uniform_ab ( -5.0, +5.0, rng )

  d, e, f = r8_sincos_sum ( a, b )

  print ( '' )
  print ( '    %g * sin ( %g * x ) + %g * cos ( %g * x )' % ( a, c, b, c ) )
  print ( '  = %g * sin ( %g * x + %g )' % ( d, c, e ) )
  print ( '  = %g * cos ( %g * x + %g )' % ( d, c, f ) )

  x = np.linspace ( 0.0, np.pi, 11 )
  y1 = a * np.sin ( c * x ) + b * np.cos ( c * x )
  y2 = d * np.sin ( c * x + e )
  y3 = d * np.cos ( c * x + f )

  print ( '' )
  print ( '   I      X              form 1        form 2        form 3' )
  print ( '' )

  for i in range ( 0, 11 ):
    print ( '  %2d  %10f  %12.6g  %12.6g  %12.6g' % ( i, x[i], y1[i], y2[i], y3[i] ) )

  return

def r8_sind ( degrees ):

#*****************************************************************************80
#
## r8_sind() returns the sine of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DEGREES, the angle in degrees.
#
#  Output:
#
#    real VALUE, the sine of the angle.
#
  import numpy as np

  radians = np.pi * ( degrees / 180.0 )

  value = np.sin ( radians )

  return value

def r8_sind_test ( ):

#*****************************************************************************80
#
## r8_sind_test() tests r8_sind().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_sind_test():' )
  print ( '  r8_sind() computes the sine of an angle given in degrees.' )
  print ( '' )
  print ( '  ANGLE    r8_sind(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    print ( '  %8.2f  %14.6g' % ( angle, r8_sind ( angle ) ) )

  return

def r8_softplus ( x ):

#*****************************************************************************80
#
## r8_softplus() evaluates the softplus function of an R8.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#    The softplus function is a smoothed (differentiable) version of max(x,0.0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  if ( x <= -36.841 ):
    value = 0.0
  elif ( +36.841 <= x ):
    value = x
  else:
    value = np.log ( 1.0 + np.exp ( x ) )

  return value

def r8_softplus_test ( ):

#*****************************************************************************80
#
## r8_softplus_test() tests r8_softplus().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_softplus_test():' )
  print ( '  r8_softplus() evaluates the softplus function of an R8.' )
  print ( '  This is a smoothed version of max(x,0).' )
  print ( '' )
  print ( '      X         r8_softplus(X)' )
  print ( '' )

  x_test = np.array ( [ \
    -500.0,   -50.0,    -5.0,    -4.0,     -3.0, \
      -2.0,    -1.0,    -0.5,    -0.05,    -0.005, \
      -0.0005,  0.0,     0.0005,  0.005,    0.05, \
       0.5,     1.0,     2.0,     3.0,      4.0, \
       5.0,    50.0,   500.0,  5000.0,  50000.0 ] )

  for i in range ( 0, 25 ):
    x = x_test[i]
    value = r8_softplus ( x )
    print ( '  %10.6g  %10.6g' % ( x, value ) )

  return

def r8_sqrt_i4 ( i ):

#*****************************************************************************80
#
## r8_sqrt_i4() returns the square root of an I4 as an R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose square root is desired.
#
#  Output:
#
#    real VALUE, the value of sqrt(I).
#
  import numpy as np

  value = np.sqrt ( float ( i ) )

  return value

def r8_sqrt_i4_test ( rng ):

#*****************************************************************************80
#
## r8_sqrt_i4_test() tests r8_sqrt_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_sqrt_i4_test():' )
  print ( '  r8_sqrt_i4() returns the square root of an I4 as an R8.' )
  print ( '' )
  print ( '      I4      r8_sqrt_i4(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = 0, high = 1000000, endpoint = True )
    r8 = r8_sqrt_i4 ( i4 )
    print ( '  %10d  %10g' % ( i4, r8 ) )

  return

def r8_swap3 ( x, y, z ):

#*****************************************************************************80
#
## r8_swap3() swaps three R8's.
#
#  Example:
#
#    Input:
#
#      X = 1, Y = 2, Z = 3
#
#    Output:
#
#      X = 2, Y = 3, Z = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, Z, three values to be swapped.
#
#  Output:
#
#    real X, Y, Z, three values to be swapped.
#
  w = x
  x = y
  y = z
  z = w

  return x, y, z

def r8_swap3_test ( ):

#*****************************************************************************80
#
## r8_swap3_test() tests r8_swap3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_swap3_test():' )
  print ( '  r8_swap3() swaps three reals.' )

  x = 1.0
  y = 3.14159
  z = 1952.0

  print ( '' )
  print ( '  Before  %g  %g  %g' % ( x, y, z ) )
  print ( '' )

  for i in range ( 0, 3 ):
    x, y, z = r8_swap3 ( x, y, z )
    print ( '  Swap %d:  %g  %g  %g' % ( i, x, y, z ) )

  return

def r8_swap ( x, y ):

#*****************************************************************************80
#
## r8_swap() swaps two R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, two values to interchange.
#
#  Output:
#
#    real X, Y, the interchanged values.
#
  z = y
  y = x
  x = z

  return x, y

def r8_swap_test ( ):

#*****************************************************************************80
#
## r8_swap_test() tests r8_swap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_swap_test():' )
  print ( '  r8_swap() swaps two reals.' )

  x = 1.0
  y = 3.14159

  print ( '' )
  print ( '  Before swapping:' )
  print ( '' )
  print ( '    X = %f' % ( x ) )
  print ( '    Y = %f' % ( y ) )

  x, y = r8_swap ( x, y )

  print ( '' )
  print ( '  After swapping:' )
  print ( '' )
  print ( '    X = %f' % ( x ) )
  print ( '    Y = %f' % ( y ) )

  return

def r8_tand ( degrees ):

#*****************************************************************************80
#
## r8_tand() returns the tangent of an angle given in degrees.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real DEGREES, the angle in degrees.
#
#  Output:
#
#    real VALUE, the tangent of the angle.
#
  import numpy as np

  radians = np.pi * ( degrees / 180.0 )

  value = np.sin ( radians ) / np.cos ( radians )

  return value

def r8_tand_test ( ):

#*****************************************************************************80
#
## r8_tand_test() tests r8_tand().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_tand_test():' )
  print ( '  r8_tand() computes the tangent of an angle in degrees.' )
  print ( '' )
  print ( '  ANGLE    r8_tand(ANGLE)' )
  print ( '' )
 
  for i in range ( 0, 375, 15 ):
    angle = float ( i )
    if ( ( ( i + 90 ) % 180 ) == 0 ):
      print ( '  %8.2f    Undefined' % ( angle ) )
    else:
      print ( '  %8.2f  %14.6g' % ( angle, r8_tand ( angle ) ) )

  return

def r8_tiny ( ):

#*****************************************************************************80
#
## r8_tiny() returns the smallest positive R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, a "tiny" value.
#
  value = 1.0E-30

  return value

def r8_tiny_test ( ):

#*****************************************************************************80
#
## r8_tiny_test() tests r8_tiny().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_tiny_test():' )
  print ( '  r8_tiny() returns a "tiny" R8;' )
  print ( '' )
  print ( '    r8_tiny = %g' % ( r8_tiny ( ) ) )

  return

def r8_to_dhms ( r ):

#*****************************************************************************80
#
## r8_to_dhms() converts decimal days into days, hours, minutes, seconds.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, a decimal number representing a time 
#    period measured in days.
#
#  Output:
#
#    integer D, integer H, integer M, real S, the equivalent number of 
#    days, hours, minutes and seconds.
#
  r_sign = r8_sign ( r )
  r = abs ( r )

  d = int ( r )

  r = r - d
  r = 24.0 * r
  h = int ( r )

  r = r - h
  r = 60.0 * r
  m = int ( r )

  r = r - m
  s = 60.0 * r

  d = r_sign * d
  h = r_sign * h
  m = r_sign * m
  s = r_sign * s

  return d, h, m, s

def r8_to_dhms_test ( rng ):

#*****************************************************************************80
#
## r8_to_dhms_test() tests r8_to_dhms().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_to_dhms_test():' )
  print ( '  r8_to_dhms() converts a real day measure into days, hours, minutes, seconds.' )
  print ( '' )
  print ( '         X         D     H     M         S' )
  print ( '' )

  for i in range ( 1, 11 ):
    x = r8_uniform_ab ( - 2.0, +10.0, rng )
    d, h, m, s = r8_to_dhms ( x )
    print ( '  %12g  %4d  %4d  %4d  %12g' % ( x, d, h, m, s ) )

  return

def r8_to_i4 ( xmin, xmax, x, ixmin, ixmax ):

#*****************************************************************************80
#
## r8_to_i4() maps X in [XMIN, XMAX] to integer IX in [IXMIN, IXMAX].
#
#  Discussion:
#
#    IX := IXMIN + ( IXMAX - IXMIN ) * ( X - XMIN ) / ( XMAX - XMIN )
#    IX := min ( IX, max ( IXMIN, IXMAX ) )
#    IX := max ( IX, min ( IXMIN, IXMAX ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XMIN, XMAX, the range.  XMAX and
#    XMIN must not be equal.  It is not necessary that XMIN be less than XMAX.
#
#    real X, the number to be converted.
#
#    integer IXMIN, IXMAX, the allowed range of the output
#    variable.  IXMAX corresponds to XMAX, and IXMIN to XMIN.
#    It is not necessary that IXMIN be less than IXMAX.
#
#  Output:
#
#    integer IX, the value in the range [IXMIN,IXMAX] that
#    corresponds to X.
#
  if ( xmax == xmin ):
    print ( '' )
    print ( 'r8_to_i4 - Fatal error!' )
    print ( '  XMAX = XMIN, making a zero divisor.' )
    print ( '  XMAX = %g' % ( xmax ) )
    print ( '  XMIN = %g' % ( xmin )  )
    raise Exception ( 'r8_to_i4 - Fatal error!' )

  temp = ( ( xmax - x        ) * ixmin   \
         + (        x - xmin ) * ixmax ) \
         / ( xmax     - xmin )

  if ( 0.0 <= temp ):
    temp = temp + 0.5
  else:
    temp = temp - 0.5

  ix = int ( temp )

  return ix

def r8_to_i4_test ( ):

#*****************************************************************************80
#
## r8_to_i4_test() tests r8_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_to_i4_test():' )
  print ( '  r8_to_i4() finds an integer IX in [IXMIN,IXMAX]' )
  print ( '  corresponding to X in [XMIN,XMAX].' )

  xmin = 2.5
  x = 3.5
  xmax = 5.5

  ixmin = 10
  ixmax = 40

  ix = r8_to_i4 ( xmin, xmax, x, ixmin, ixmax )

  print ( '' )
  print ( '   XMIN = %12f,  X = %12f,  XMAX = %12f' % (  xmin,  x,  xmax ) )
  print ( '  IXMIN = %12d, IX = %12d, IXMAX = %12d' % ( ixmin, ix, ixmax ) )

  return

def r8_to_r8_discrete ( r, rmin, rmax, nr ):

#*****************************************************************************80
#
## r8_to_r8_discrete() maps R to RD in [RMIN, RMAX] with NR possible values.
#
#  Discussion:
#
#    if ( R < RMIN ) then
#      RD = RMIN
#    else if ( RMAX < R ) then
#      RD = RMAX
#    else
#      T = nint ( ( NR - 1 ) * ( R - RMIN ) / ( RMAX - RMIN ) )
#      RD = RMIN + T * ( RMAX - RMIN ) / real ( NR - 1 )
#
#    In the special case where NR = 1, when
#
#      RD = 0.5 * ( RMAX + RMIN )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the number to be converted.
#
#    real RMAX, RMIN, the maximum and minimum
#    values for RD.
#
#    integer NR, the number of allowed values for XD.
#    NR should be at least 1.
#
#  Output:
#
#    real RD, the corresponding discrete value.
#

#
#  Check for errors.
#
  if ( nr < 1 ):
    print ( '' )
    print ( 'r8_to_r8_discrete - Fatal error!' )
    print ( '  NR = %d' % ( nr ) )
    print ( '  but NR must be at least 1.' )
    raise Exception ( 'r8_to_r8_discrete - Fatal error!' )

  if ( nr == 1 ):
    rd = 0.5 * ( rmin + rmax )
    return rd

  if ( rmax == rmin ):
    rd = rmax
    return rd

  f = round ( nr * ( rmax - r ) / ( rmax - rmin ) )
  f = max ( f, 0 )
  f = min ( f, nr )

  rd = ( (      f ) * rmin   \
       + ( nr - f ) * rmax ) \
       / ( nr     )


  return rd

def r8_to_r8_discrete_test ( rng ):

#*****************************************************************************80
#
## r8_to_r8_discrete_test() tests r8_to_r8_discrete().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  ndx = 19
  rhi = 10.0
  rlo = 1.0
  test_num = 15

  print ( '' )
  print ( 'r8_to_r8_discrete_test():' )
  print ( '  r8_to_r8_discrete() maps numbers to a discrete set' )
  print ( '  of equally spaced numbers in an interval.' )
  print ( '' )
  print ( '  Number of discrete values = %d' % ( ndx ) )
  print ( '  Real interval: [%f, %f]' % ( rlo, rhi ) )
  print ( '' )
  print ( '       R        RD' )
  print ( '' )

  rlo2 = rlo - 2.0
  rhi2 = rhi + 2.0

  for test in range ( 0, test_num ):
    r = r8_uniform_ab ( rlo2, rhi2, rng )
    rd = r8_to_r8_discrete ( r, rlo, rhi, ndx )
    print ( '  %14f  %14f' % ( r, rd ) )

  return

def r8_uniform_01 ( rng ):

#*****************************************************************************80
#
## r8_uniform_01() returns a unit pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    real R, a random value between 0 and 1.
#
  r = rng.random ( )

  return r

def r8_uniform_01_test ( rng ):

#*****************************************************************************80
#
## r8_uniform_01_test() tests r8_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8_uniform_01_test():' )
  print ( '  r8_uniform_01() produces a sequence of random values.' )

  print ( '' )
  for i in range ( 0, 10 ):
    x = r8_uniform_01 ( rng )
    print ( '  %14f' % ( x ) )

  return

def r8_uniform_ab ( a, b, rng ):

#*****************************************************************************80
#
## r8_uniform_ab() returns a scaled pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    real A, B, the minimum and maximum values.
#
#  Output:
#
#    real R, the randomly chosen value.
#
  r = a + ( b - a ) * rng.random ( )

  return r

def r8_uniform_ab_test ( rng ):

#*****************************************************************************80
#
## r8_uniform_ab_test() tests r8_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'r8_uniform_ab_test():' )
  print ( '  r8_uniform_ab() returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_uniform_ab ( a, b, rng )
    print ( '  %f' % ( r ) )

  return

def r8_unswap3 ( x, y, z ):

#*****************************************************************************80
#
## r8_unswap3() unswaps three R8's.
#
#  Example:
#
#    Input:
#
#      X = 2, Y = 3, Z = 1
#
#    Output:
#
#      X = 1, Y = 2, Z = 3
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, Z, three values to be swapped.
#
#  Output:
#
#    real X, Y, Z, the swapped values.
#
  w = z
  z = y
  y = x
  x = w

  return x, y, z

def r8_unswap3_test ( ):

#*****************************************************************************80
#
## r8_unswap3_test() tests r8_unswap3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_unswap3_test():' )
  print ( '  r8_unswap3() unswaps three reals.' )

  x = 1.0
  y = 3.14159
  z = 1952.0

  print ( '' )
  print ( '  Data :    %g  %g  %g' % ( x, y, z ) )
  x, y, z = r8_swap3 ( x, y, z )

  print ( '  Swap :    %g  %g  %g' % ( x, y, z ) )

  x, y, z = r8_unswap3 ( x, y, z )
  print ( '  Unswap :  %g  %g  %g' % ( x, y, z ) )

  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## r8poly_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of the polynomial.
#
#    real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( r8vec_is_zero ( m + 1, a ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) = ', end = '' ),
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False
      else:
        print ( '         ', end = '' ),

      if ( 2 <= i ):
        print ( '  %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '  %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '  %c %g' % ( plus_minus, mag ) )

  return

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_print_test' )
  print ( '  r8poly_print() prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#    In Python, use:
#
#      print ( title )
#      print ( np.c_ [ a1, a2 ] )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = float )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = float )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
## r8vec2_print_some() prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_print, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vectors.
#
#    real X1(N), X2(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

  return

def r8vec2_print_some_test ( ):

#*****************************************************************************80
#
## r8vec2_print_some_test() tests r8vec2_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 100
  a = np.zeros ( n )
  b = np.zeros ( n )

  for i in range ( 0, n ):
    x = float ( i + 1 )
    a[i] = x * x
    b[i] = np.sqrt ( x )

  print ( '' )
  print ( 'r8vec2_print_some_test():' )
  print ( '  r8vec2_print_some() prints some of a pair of R8VEC\'s.' )

  r8vec2_print_some ( n, a, b, 10, '  Square and square root:' )

  return

def r8vec3_print ( n, a1, a2, a3, title ):

#*****************************************************************************80
#
## r8vec3_print() prints an R8VEC3.
#
#  Discussion:
#
#    An R8VEC3 is a dataset consisting of 3 vectors of N real values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), A3(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g  %12g' % ( i, a1[i], a2[i], a3[i] ) )

  return

def r8vec3_print_test ( ):

#*****************************************************************************80
#
## r8vec3_print_test() tests r8vec3_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec3_print_test():' )
  print ( '  r8vec3_print() prints an R8VEC.' )

  n = 6

  t = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = float )
  u = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = float )
  v = np.array ( [ 0.0, 0.24, 0.56, 0.96, 1.44, 2.0 ], dtype = float )

  r8vec3_print ( n, t, u, v, '  X, X^2, X+X^2\'s:' )

  return

def r8vec_amax_index ( n, a ):

#*****************************************************************************80
#
## r8vec_amax_index() returns the index of the maximum absolute value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    integer VALUE_index, the (0-based) index of the maximum absolute value 
#    in the vector.
#
  import numpy as np

  value_max = - np.inf
  value_index = -1

  for i in range ( 0, n ):
    if ( value_max < abs ( a[i] ) ):
      value_max = abs ( a[i] )
      value_index = i

  return value_index

def r8vec_amax_index_test ( rng ):

#*****************************************************************************80
#
## r8vec_amax_index_test() tests r8vec_amax_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_amax_index_test():' )
  print ( '  r8vec_amax_index() computes the index of the entry of' )
  print ( '  maximum absolute value in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value_index = r8vec_amax_index ( n, a )
  value_max = a[value_index]

  print ( '' )
  print ( '  AMAX = A[%d] = %g' % ( value_index, value_max ) )

  return

def r8vec_amax ( n, a ):

#*****************************************************************************80
#
## r8vec_amax() returns the maximum absolute value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the maximum absolute value in the vector.
#
  value = 0.0
  for i in range ( 0, n ):
    if ( value < abs ( a[i] ) ):
      value = abs ( a[i] )

  return value

def r8vec_amax_test ( rng ):

#*****************************************************************************80
#
## r8vec_amax_test() tests r8vec_amax().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_amax_test():' )
  print ( '  r8vec_amax() computes the maximum absolute value entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_amax ( n, a )
  print ( '' )
  print ( '  Max Abs = %g' % ( value ) )

  return

def r8vec_amin_index ( n, a ):

#*****************************************************************************80
#
## r8vec_amin_index() returns the index of the minimum absolute value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    integer VALUE_index, the (0-based) index of the minimum absolute 
#    value in the vector.
#
  import numpy as np

  value_min = np.inf
  value_index = -1

  for i in range ( 0, n ):
    if ( abs ( a[i] ) < value_min ):
      value_min = abs ( a[i] )
      value_index = i

  return value_index

def r8vec_amin_index_test ( rng ):

#*****************************************************************************80
#
## r8vec_amin_index_test() tests r8vec_amin_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_amin_index_test():' )
  print ( '  r8vec_amin_index() computes the index of the entry of' )
  print ( '  minimum absolute value in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value_index = r8vec_amin_index ( n, a )
  value_min = a[value_index]

  print ( '' )
  print ( '  AMIN = A[%d] = %g' % ( value_index, value_min ) )

  return

def r8vec_amin ( n, a ):

#*****************************************************************************80
#
## r8vec_amin() returns the minimum absolute value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the minimum absolute value in the vector.
#
  import numpy as np

  huge = np.finfo(float).max

  value = huge
  for i in range ( 0, n ):
    if ( abs ( a[i] ) < value ):
      value = abs ( a[i] )

  return value

def r8vec_amin_test ( rng ):

#*****************************************************************************80
#
## r8vec_amin_test() tests r8vec_amin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_amin_test():' )
  print ( '  r8vec_amin() computes the minimum absolute entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = a_lo + ( a_hi - a_lo ) * rng.random ( size = n )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_amin ( n, a )
  print ( '' )
  print ( '  Min Abs = %g' % ( value ) )

  return

def r8vec_asum ( n, a ):

#*****************************************************************************80
#
## r8vec_asum() sums the absolute values of the entries of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the sum of the absolute values of the entries.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + abs ( a[i] )

  return value

def r8vec_asum_test ( rng ):

#*****************************************************************************80
#
## r8vec_asum_test() tests r8vec_asum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_asum_test():' )
  print ( '  r8vec_asum() sums the absolute values of the entries in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_asum ( n, a )

  print ( '' )
  print ( '  Sum of absolute values of entries = %g' % ( value ) )

  return

def r8vec_binary_next ( n, bvec ):

#*****************************************************************************80
#
## r8vec_binary_next() generates the next binary vector.
#
#  Discussion:
#
#    The vectors have the order
#
#      (0,0,...,0),
#      (0,0,...,1),
#      ...
#      (1,1,...,1)
#
#    and the "next" vector after (1,1,...,1) is (0,0,...,0).  That is,
#    we allow wrap around.
#
#  Example:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  0 1 1
#    0 1 1  =>  1 0 0
#    1 0 0  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real BVEC(N), the vector whose successor is desired.
#
#  Output:
#
#    real BVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( bvec[i] == 0.0 ):
      bvec[i] = 1.0
      break

    bvec[i] = 0.0

  return bvec

def r8vec_binary_next_test ( ):

#*****************************************************************************80
#
## r8vec_binary_next_test() tests r8vec_binary_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'r8vec_binary_next_test():' )
  print ( '  r8vec_binary_next() generates the next binary vector.' )
  print ( '' )
 
  bvec = np.zeros ( n, dtype = float )

  while ( True ):

    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%d' % ( bvec[i] ), end = '' )
    print ( '' )

    if ( all ( bvec[0:n] == 1.0 ) ):
      break

    bvec = r8vec_binary_next ( n, bvec )

  return

def r8vec_bracket5 ( nd, xd, xi ):

#*****************************************************************************80
#
## r8vec_bracket5() brackets data between successive entries of a sorted R8VEC.
#
#  Discussion:
#
#    We assume XD is sorted.
#
#    If XI is contained in the interval [XD(1),XD(N)], then the returned 
#    value B indicates that XI is contained in [ XD(B), XD(B+1) ].
#
#    If XI is not contained in the interval [XD(1),XD(N)], then B = -1.
#
#    This code implements a version of binary search which is perhaps more
#    understandable than the usual ones.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data values.
#
#    real XD(N), the sorted data.
#
#    real XD, the query value.
#
#  Output:
#
#    integer B, the bracket information.
#
  import numpy as np

  if ( xi < xd[0] or xd[nd-1] < xi ):

    b = -1

  else:

    l = 0
    r = nd - 1

    while ( l + 1 < r ):
      m = int ( ( l + r ) / 2 )
      if ( xi < xd[m] ):
        r = m
      else:
        l = m

    b = l

  return b

def r8vec_bracket5_test ( ):

#*****************************************************************************80
#
## r8vec_bracket5_test() tests r8vec_bracket5().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  test_num = 6;

  xtest = np.array ( [ -10.0, 1.0, 4.5, 5.0, 10.0, 12.0 ] )

  print ( '' )
  print ( 'r8vec_bracket5_test():' )
  print ( '  r8vec_bracket5 finds a pair of entries in a' )
  print ( '  sorted R8VEC which bracket a value.' )

  x = r8vec_indicator1 ( n )
  x[5] = x[4]

  r8vec_print ( n, x, '  Sorted array:' )

  print ( '' )
  print ( '        LEFT                   RIGHT' )
  print ( '      X(LEFT)       XVAL     X(RIGHT)' )

  for test in range ( 0, test_num ):

    xval = xtest[test]
    left = r8vec_bracket5 ( n, x, xval )

    print ( '' )
    if ( left == -1 ):
      print ( '  %10d' % ( left ) )
      print ( '              %10.4f  (Not bracketed!)' % ( xval ) )
    else:
      right = left + 1
      print ( '  %10d              %10d' % ( left, right ) )
      print ( '  %10.4f  %10.4f  %10.4f' % ( x[left], xval, x[right] ) )

  return

def r8vec_bracket ( n, x, xval ):

#*****************************************************************************80
#
## r8vec_bracket() searches a sorted array for successive brackets of a value.
#
#  Discussion:
#
#    A naive algorithm is used.
#
#    If the values in the vector are thought of as defining intervals
#    on the real line, then this routine searches for the interval
#    nearest to or containing the given value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, length of input array.
#
#    real X(N), an array that has been sorted into ascending order.
#
#    real XVAL, a value to be bracketed.
#
#  Output:
#
#    integer LEFT, RIGHT, the results of the search.
#    Either:
#      XVAL < X(1), when LEFT = 1, RIGHT = 2
#      XVAL > X(N), when LEFT = N-1, RIGHT = N
#    or
#      X(LEFT) <= XVAL <= X(RIGHT).
#
  for i in range ( 1, n - 1 ):

    if ( xval < x[i] ):
      left = i - 1
      right = i
      return left, right

  left = n - 2
  right = n - 1

  return left, right

def r8vec_bracket_test ( rng ):

#*****************************************************************************80
#
## r8vec_bracket_test() tests r8vec_bracket().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 11

  print ( '' )
  print ( 'r8vec_bracket_test():' )
  print ( '  r8vec_bracket() finds, for a given value R,' )
  print ( '  the nearest interval [low,high] in a sorted R8VEC' )
  print ( '  that "brackets" the value.' )

  s = np.linspace ( 0.0, 10.0, n );
  r8vec_print ( n, s, '  Sorted R8VEC:' )

  print ( '' )
  for i in range ( 0, 15 ):
    r = r8_uniform_ab ( -1.0, 11.0, rng )
    [ low, high ] = r8vec_bracket ( n, s, r )
    print ( '  R = %g is bracketed by ( S[%d] = %g, S[%d] = %g' \
      % ( r, low, s[low], high, s[high] ) )

  return

def r8vec_cheby1space ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby1space() creates a vector of Type 1 Chebyshev values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Type 1 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_cheby1space_test ( ):

#*****************************************************************************80
#
## r8vec_cheby1space_test() tests r8vec_cheby1space().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_cheby1space_test():' )
  print ( '  r8vec_cheby1space() returns Type 1 Chebyshev values in [A,B].' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_cheby1space ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )

  return

def r8vec_cheby2space ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby2space() creates a vector of Type 2 Chebyshev values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Type 2 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):

    theta = float ( n - i ) * np.pi / float ( n + 1 )

    c = np.cos ( theta )

    x[i] = ( ( 1.0 - c ) * a  \
           + ( 1.0 + c ) * b ) \
           /   2.0
 
  return x

def r8vec_cheby2space_test ( ):

#*****************************************************************************80
#
## r8vec_cheby2space_test() tests r8vec_cheby2space().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_cheby2space_test():' )
  print ( '  r8vec_cheby2space() returns Type 2 Chebyshev values in [A,B].' )

  n = 9
  x_lo = 10.0
  x_hi = 20.0

  print ( '  Generate %d points in [%g,%g]' % ( n, x_lo, x_hi ) )

  x = r8vec_cheby2space ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )

  return

def r8vec_cheby_extreme ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby_extreme() creates Chebyshev Extreme values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_cheby_extreme_test ( ):

#*****************************************************************************80
#
## r8vec_cheby_extreme_test() tests r8vec_cheby_extreme().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_cheby_extreme_test():' )
  print ( '  r8vec_cheby_extreme() returns Chebyshev Extreme values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_cheby_extreme ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )

  return

def r8vec_cheby_zero ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby_zero() creates Chebyshev Zero values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( 2 * ( n - i ) - 1 ) * np.pi / float ( 2 *  n )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_cheby_zero_test ( ):

#*****************************************************************************80
#
## r8vec_cheby_zero_test() tests r8vec_cheby_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_cheby_zero_test():' )
  print ( '  r8vec_cheby_zero() returns Chebyshev Zero values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_cheby_zero ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )

  return

def r8vec_concatenate ( n1, a1, n2, a2 ):

#*****************************************************************************80
#
## r8vec_concatenate() concatenates two R8VEC's.
#
#  Discussion:
#
#    An R8VEC is a vector of R8 values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, the number of entries in the first vector.
#
#    real A1(N1), the first vector.
#
#    integer N2, the number of entries in the second vector.
#
#    real A2(N2), the second vector.
#
#  Output:
#
#    real A3(N1+N2), the concatenation of A1 and A2.
#
  import numpy as np

  a3 = np.concatenate ( ( a1, a2 ), axis = 0 )

  return a3

def r8vec_concatenate_test ( ):

#*****************************************************************************80
#
## r8vec_concatenate_test() tests r8vec_concatenate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 5
  n2 = 3
  n3 = n1 + n2

  a1 = np.array ( [ 91.1, 31.2, 71.3, 51.4, 31.5 ] )
  a2 = np.array ( [ 42.6, 22.7, 12.8 ] )

  print ( '' )
  print ( 'r8vec_concatenate_test():' )
  print ( '  r8vec_concatenate() concatenates two R8VECs' )

  r8vec_print ( n1, a1, '  Array 1:' )
  r8vec_print ( n2, a2, '  Array 2:' )
  a3 = r8vec_concatenate ( n1, a1, n2, a2 )
  r8vec_print ( n3, a3, '  Array 3 = Array 1 + Array 2:' )

  return

def r8vec_copy ( n1, a1 ):

#*****************************************************************************80
#
## r8vec_copy() copies an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8 values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, the number of entries in the vector.
#
#    real A1(N1), the vector.
#
#  Output:
#
#    real A2(N1), a copy of A2.
#
  import numpy as np

  a2 = np.zeros ( n1, dtype = float )
  for i in range ( 0, n1 ):
    a2[i] = a1[i]

  return a2

def r8vec_copy_test ( ):

#*****************************************************************************80
#
## r8vec_copy_test() tests r8vec_copy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 5

  a1 = np.array ( [ 91.1, 31.2, 71.3, 51.4, 31.5 ] )
 
  print ( '' )
  print ( 'r8vec_copy_test():' )
  print ( '  r8vec_copy() copies an R8VEC.' )

  r8vec_print ( n1, a1, '  Array 1:' );
  a2 = r8vec_copy ( n1, a1 );
  r8vec_print ( n1, a2, '  Array 2:' );

  return

def r8vec_correlation ( n, x, y ):

#*****************************************************************************80
#
## r8vec_correlation() returns the correlation of two R8VEC's.
#
#  Discussion:
#
#    The correlation coefficient is also known as Pearson's r coefficient.
#
#    It must be the case that -1 <= r <= +1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the dimension of the vectors.
#
#    real x(n), y(n): the vectors.
#
#  Output:
#
#    real r: the correlation coefficient.
#
  import numpy as np

  x_mean = np.mean ( x )
  x_std = np.std ( x, ddof = 1 )

  y_mean = np.mean ( y )
  y_std = np.std ( y, ddof = 1 )

  if ( n <= 1 ):
    r = 0.0
  else:
    r = np.dot ( ( x - x_mean ), ( y - y_mean ) ) / x_std / y_std / ( n - 1 )

  return r

def r8vec_correlation_test ( ):

#*****************************************************************************80
#
## r8vec_correlation_test() tests r8vec_correlation().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 August 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '\n' )
  print ( 'r8vec_correlation_test():' )
  print ( '  r8vec_correlation computes the correlation of two R8VEC\'s.' )

  n = 6
  v1 = np.array ( [ 43, 21, 25, 42, 57, 59 ] )
  r8vec_print ( n, v1, '  Vector V1:' )
  v2 = np.array ( [ 99, 65, 79, 75, 87, 81 ] )
  r8vec_print ( n, v2, '  Vector V2:' )

  value = r8vec_correlation ( n, v1, v2 )
  print ( '' )
  print ( '  V1 V2 Correlation coefficient r = ', value )

  return

def r8vec_covariance ( n, x, y ):

#*****************************************************************************80
#
## r8vec_covariance() computes the covariance of two vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the dimension of the two vectors.
#
#    real X(N), Y(N), the two vectors.
#
#  Output:
#
#    real VALUE, the covariance of the two vectors.
#
  import numpy as np

  x_average = np.mean ( x[0:n] )
  y_average = np.mean ( y[0:n] )
  
  value = 0.0
  for i in range ( 0, n ):
    value = value + ( x[i] - x_average ) * ( y[i] - y_average )

  value = value / float ( n - 1 )

  return value

def r8vec_covariance_test ( rng ):

#*****************************************************************************80
#
## r8vec_covariance_test() tests r8vec_covariance().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_covariance_test():' )
  print ( '  r8vec_covariance() computes the covariance of two R8VECs.' )

  n = 2

  v1 = np.array ( [ 1.0, 0.0 ] )
  print ( '' )
  print ( '  Vector V1:', end = '' )
  for i in range ( 0, n ):
    print ( '%g' % ( v1[i] ), end = '' )
  print ( '' )

  for i in range ( 0, 12 ):
    angle = float ( 2 * i ) * np.pi / 12.0
    r = rng.random ( )
    v2 = r * np.array ( [ np.cos(angle), np.sin(angle) ] )
    print ( '' )
    print ( '  Vector V2:', end = '' )
    for i in range ( 0, n ):
      print ( '%g' % ( v2[i] ), end = '' )
    print ( '' )
    value = r8vec_covariance ( n, v1, v2 )
    print ( '  Covariance(V1,V2) = %g' % ( value ) )

  return

def r8vec_diff_norm_li ( n, a, b ):

#*****************************************************************************80
#
## r8vec_diff_norm_li() returns the L-infinity norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L-infinity norm is defined as:
#
#      value = max ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), B(N), the vectors.
#
#  Output:
#
#    real VALUE, the L-infinity norm of A - B.
#
  value = 0.0
  for i in range ( 0, n ):
    value = max ( value, abs ( a[i] - b[i] ) )

  return value

def r8vec_diff_norm_li_test ( rng ):

#*****************************************************************************80
#
## r8vec_diff_norm_li_test() tests r8vec_diff_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_diff_norm_li_test():' )
  print ( '  r8vec_diff_norm_li(): L-infinity norm of the difference' )
  print ( '  of two R8VEC\'s.' )
 
  n = 5
  r8_lo = -10.0
  r8_hi = +10.0

  v1 = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )
  v2 = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, v1, '  Vector V1:' )
  r8vec_print ( n, v2, '  Vector V2:' )

  diff = r8vec_diff_norm_li ( n, v1, v2 )

  print ( '' )
  print ( '  L-Infinity norm of V1-V2: %g' % ( diff ) )

  return

def r8vec_diff_norm ( n, a, b ):

#*****************************************************************************80
#
## r8vec_diff_norm() returns the L2 norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), B(N), the vectors.
#
#  Output:
#
#    real VALUE, the L2 norm of A - B.
#
  import numpy as np

  value = np.sqrt ( np.sum ( ( a[0:n] - b[0:n] ) ** 2 ) )

  return value

def r8vec_diff_norm_test ( ):

#*****************************************************************************80
#
## r8vec_diff_norm_test() tests r8vec_diff_norm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_diff_norm_test():' )
  print ( '  r8vec_diff_norm(): L2 norm of the difference of two R8VECs.' )

  n = 6
  v = np.array ( [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ], dtype = float )
  w = np.array ( [ 1.0, 2.0, 3.0, 5.0, 5.0, 6.0 ], dtype = float )
  
  print ( '' )
  print ( '  I    V[I]  W[I]' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '%2d  %f  %f' % ( i, v[i], w[i] ) )

  d = r8vec_diff_norm ( n, v, w )

  print ( '' )
  print ( '  L2 norm of vector difference ||V-W|| is %g' % ( d ) )

  return

def r8vec_direct_product ( factor_index, factor_order, \
  factor_value, factor_num, point_num, x, contig, rep, skip ):

#*****************************************************************************80
#
## r8vec_direct_product() creates a direct product of R8VEC's.
#
#  Discussion:
#
#    To explain what is going on here, suppose we had to construct
#    a multidimensional quadrature rule as the product of K rules
#    for 1D quadrature.
#
#    The product rule will be represented as a list of points and weights.
#
#    The J-th item in the product rule will be associated with
#      item J1 of 1D rule 1,
#      item J2 of 1D rule 2, 
#      ..., 
#      item JK of 1D rule K.
#
#    In particular, 
#      X(J) = ( X(1,J1), X(2,J2), ..., X(K,JK))
#    and
#      W(J) = W(1,J1) * W(2,J2) * ... * W(K,JK)
#
#    So we can construct the quadrature rule if we can properly
#    distribute the information in the 1D quadrature rules.
#
#    This routine carries out that task.
#
#    Another way to do this would be to compute, one by one, the
#    set of all possible indices (J1,J2,...,JK), and then index
#    the appropriate information.  An advantage of the method shown
#    here is that you can process the K-th set of information and
#    then discard it.
#
#  Example:
#
#    Rule 1: 
#      Order = 4
#      X(1:4) = ( 1, 2, 3, 4 )
#
#    Rule 2:
#      Order = 3
#      X(1:3) = ( 10, 20, 30 )
#
#    Rule 3:
#      Order = 2
#      X(1:2) = ( 100, 200 )
#
#    Product Rule:
#      Order = 24
#      X(1:24) = 
#        ( 1, 10, 100 )
#        ( 2, 10, 100 )
#        ( 3, 10, 100 )
#        ( 4, 10, 100 )
#        ( 1, 20, 100 )
#        ( 2, 20, 100 )
#        ( 3, 20, 100 )
#        ( 4, 20, 100 )
#        ( 1, 30, 100 )
#        ( 2, 30, 100 )
#        ( 3, 30, 100 )
#        ( 4, 30, 100 )
#        ( 1, 10, 200 )
#        ( 2, 10, 200 )
#        ( 3, 10, 200 )
#        ( 4, 10, 200 )
#        ( 1, 20, 200 )
#        ( 2, 20, 200 )
#        ( 3, 20, 200 )
#        ( 4, 20, 200 )
#        ( 1, 30, 200 )
#        ( 2, 30, 200 )
#        ( 3, 30, 200 )
#        ( 4, 30, 200 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer FACTOR_index, the index of the factor being processed.
#    The first factor processed must be factor 1#
#
#    integer FACTOR_ORDER, the order of the factor.
#
#    real FACTOR_VALUE(FACTOR_ORDER), the factor values
#    for factor FACTOR_index.
#
#    integer FACTOR_NUM, the number of factors.
#
#    integer POINT_NUM, the number of elements in the direct product.
#
#    real X(FACTOR_NUM,POINT_NUM), the elements of the
#    direct product.  
#
#    integer CONTIG, the number of consecutive values to set.
#    The user should not set or alter this value.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#    The user should not set or alter this value.
#
#    integer REP, the number of blocks of values to set.
#    The user should not set or alter this value.
#
#  Output:
#
#    real X(FACTOR_NUM,POINT_NUM), the updated elements of the
#    direct product.  
#
#    integer CONTIG, the number of consecutive values to set.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#
#    integer REP, the number of blocks of values to set.
#
#  Local:
#
#    integer START, the first location of a block of values to set.
#
  import numpy as np

  if ( factor_index == 0 ):
    contig = 1
    skip = 1
    rep = point_num

  rep = ( rep // factor_order )
  skip = skip * factor_order

  for j in range ( 0, factor_order ):

    start = j * contig

    for k in range ( 0, rep ):
      for l in range ( start, start + contig ):
        x[factor_index,l] = factor_value[j]
      start = start + skip

  contig = contig * factor_order

  return x, contig, rep, skip

def r8vec_direct_product_test ( ):

#*****************************************************************************80
#
## r8vec_direct_product_test() tests r8vec_direct_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  factor_num = 3
  point_num = 24

  print ( '' )
  print ( 'r8vec_direct_product_test():' )
  print ( '  r8vec_direct_product() forms the entries of a' )
  print ( '  direct product of a given number of R8VEC factors.' )

  x = np.zeros ( ( factor_num, point_num ) )
  contig = 0
  skip = 0
  rep = 0

  for factor_index in range ( 0, factor_num ):

    if ( factor_index == 0 ):
      factor_order = 4
      factor_value = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
    elif ( factor_index == 1 ):
      factor_order = 3
      factor_value = np.array ( [ 50.0, 60.0, 70.0 ] )
    elif ( factor_index == 2 ):
      factor_order = 2
      factor_value = np.array ( [ 800.0, 900.0 ] )
  
    x, contig, rep, skip = r8vec_direct_product ( factor_index, factor_order, \
      factor_value, factor_num, point_num, x, contig, rep, skip );

  r8mat_transpose_print ( factor_num, point_num, x, '  Matrix (transposed)' )

  return

def r8vec_direct_product2 ( factor_index, factor_order, \
  factor_value, factor_num, point_num, w, contig2, rep2, skip2 ):

#*****************************************************************************80
#
## r8vec_direct_product2() creates a direct product of R8VEC's.
#
#  Discussion:
#
#    To explain what is going on here, suppose we had to construct
#    a multidimensional quadrature rule as the product of K rules
#    for 1D quadrature.
#
#    The product rule will be represented as a list of points and weights.
#
#    The J-th item in the product rule will be associated with
#      item J1 of 1D rule 1,
#      item J2 of 1D rule 2, 
#      ..., 
#      item JK of 1D rule K.
#
#    In particular, 
#      X(J) = ( X(1,J1), X(2,J2), ..., X(K,JK))
#    and
#      W(J) = W(1,J1) * W(2,J2) * ... * W(K,JK)
#
#    So we can construct the quadrature rule if we can properly
#    distribute the information in the 1D quadrature rules.
#
#    This routine carries out that task for the weights W.
#
#    Another way to do this would be to compute, one by one, the
#    set of all possible indices (J1,J2,...,JK), and then index
#    the appropriate information.  An advantage of the method shown
#    here is that you can process the K-th set of information and
#    then discard it.
#
#  Example:
#
#    Rule 1: 
#      Order = 4
#      W(1:4) = ( 2, 3, 5, 7 )
#
#    Rule 2:
#      Order = 3
#      W(1:3) = ( 11, 13, 17 )
#
#    Rule 3:
#      Order = 2
#      W(1:2) = ( 19, 23 )
#
#    Product Rule:
#      Order = 24
#      W(1:24) =
#        ( 2 * 11 * 19 )
#        ( 3 * 11 * 19 )
#        ( 4 * 11 * 19 )
#        ( 7 * 11 * 19 )
#        ( 2 * 13 * 19 )
#        ( 3 * 13 * 19 )
#        ( 5 * 13 * 19 )
#        ( 7 * 13 * 19 )
#        ( 2 * 17 * 19 )
#        ( 3 * 17 * 19 )
#        ( 5 * 17 * 19 )
#        ( 7 * 17 * 19 )
#        ( 2 * 11 * 23 )
#        ( 3 * 11 * 23 )
#        ( 5 * 11 * 23 )
#        ( 7 * 11 * 23 )
#        ( 2 * 13 * 23 )
#        ( 3 * 13 * 23 )
#        ( 5 * 13 * 23 )
#        ( 7 * 13 * 23 )
#        ( 2 * 17 * 23 )
#        ( 3 * 17 * 23 )
#        ( 5 * 17 * 23 )
#        ( 7 * 17 * 23 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer FACTOR_INDEX, the index of the factor being processed.
#    The first factor processed must be factor 0.
#
#    integer FACTOR_ORDER, the order of the factor.
#
#    real FACTOR_VALUE(FACTOR_ORDER), the factor values for
#    factor FACTOR_INDEX.
#
#    integer FACTOR_NUM, the number of factors.
#
#    integer POINT_NUM, the number of elements in the direct product.
#
#    real W(POINT_NUM), the elements of the
#    direct product.
#
#    integer CONTIG2, the number of consecutive values to set.
#    The user should not set or alter this value.
#
#    integer REP2, the number of blocks of values to set.
#    The user should not set or alter this value.
#
#    integer SKIP2, the distance from the current value of START
#    to the next location of a block of values to set.
#    The user should not set or alter this value.
#
#  Output:
#
#    real W(POINT_NUM), the elements of the
#    direct product, updated by the latest factor.
#
#    integer CONTIG2, the number of consecutive values to set.
#
#    integer REP2, the number of blocks of values to set.
#
#    integer SKIP2, the distance from the current value of START
#    to the next location of a block of values to set.
#
#  Local:
#
#    integer START, the first location of a block of values to set.
#
  import numpy as np

  if ( factor_index == 0 ):
    contig2 = 1
    skip2 = 1
    rep2 = point_num
    w = np.ones ( point_num )

  rep2 = rep2 // factor_order
  skip2 = skip2 * factor_order

  for j in range ( 0, factor_order ):

    start = j * contig2

    for k in range ( 0, rep2 ):
      w[start:start+contig2] = w[start:start+contig2] * factor_value[j]
      start = start + skip2

  contig2 = contig2 * factor_order

  return w, contig2, rep2, skip2

def r8vec_direct_product2_test ( ):

#*****************************************************************************80
#
## r8vec_direct_product2_test() tests r8vec_direct_product2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  factor_num = 3
  point_num = 24

  print ( '' )
  print ( 'r8vec_direct_product2_test():' )
  print ( '  r8vec_direct_product2() forms the entries of a' )
  print ( '  direct product of a given number of R8VEC factors.' )

  w = np.zeros ( point_num )
  contig2 = 0
  skip2 = 0
  rep2 = 0

  for factor_index in range ( 0, factor_num ):

    if ( factor_index == 0 ):
      factor_order = 4
      factor_value = np.array ( [ 2.0, 3.0, 5.0, 7.0 ] )
    elif ( factor_index == 1 ):
      factor_order = 3
      factor_value = np.array ( [ 11.0, 13.0, 17.0 ] )
    elif ( factor_index == 2 ):
      factor_order = 2
      factor_value = np.array ( [ 19.0, 23.0 ] )
  
    w, contig2, rep2, skip2 = r8vec_direct_product2 ( factor_index, factor_order, \
      factor_value, factor_num, point_num, w, contig2, rep2, skip2 );

  print ( '' )
  print ( '  Direct product W:' )
  pprint.pprint ( w )

  return

def r8vec_dot_product ( n, v1, v2 ):

#*****************************************************************************80
#
## r8vec_dot_product() finds the dot product of a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real V1(N), V2(N), the vectors.
#
#  Output:
#
#    real VALUE, the dot product.
#

  value = 0.0
  for i in range ( 0, n ):
    value = value + v1[i] * v2[i]

  return value

def r8vec_dot_product_test ( rng ):

#*****************************************************************************80
#
## r8vec_dot_product_test() tests r8vec_dot_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_dot_product_test():' )
  print ( '  r8vec_dot_product() computes the dot product of two R8VEC\'s.' )

  n = 10
  v1 = rng.random ( size = n )
  v2 = rng.random ( size = n )
  r8vec2_print ( v1, v2, '  V1 and V2:' )

  value = r8vec_dot_product ( n, v1, v2 )

  print ( '' )
  print ( '  V1 dot V2 = %g' % ( value ) )

  return

def r8vec_eq ( n, a, b ):

#*****************************************************************************80
#
## r8vec_eq() is TRUE if two R8VEC's are equal.
#
#  Example:
#
#    A = ( 9, 7, 7, 3, 2, 1, -8 )
#    B = ( 9, 7, 6, 3, 2, 1, -8 )
#    r8vec_eq = FALSE
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the arrays.
#
#    real A(N), B(N), the arrays to be compared.
#
#  Output:
#
#    bool VALUE, is TRUE if the arrays are equal.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( a[i] != b[i] ):
      value = False
      break

  return value

def r8vec_eq_test ( ):

#*****************************************************************************80
#
## r8vec_eq_test() tests r8vec_eq().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  test_num = 4

  a_test = np.array ( [ \
    [ 1.1, 3.2, 2.3, 4.4 ], \
    [ 2.1, 2.2, 2.3, 2.4 ], \
    [ 1.1, 2.2, 2.3, 4.4 ], \
    [ 1.1, 2.2, 3.3, 4.4 ] ], dtype = float )

  b_test = np.array ( [ \
    [ 1.1, 3.2, 2.3, 4.4 ], \
    [ 2.1, 2.2, 1.3, 2.4 ], \
    [ 4.1, 1.2, 1.3, 3.4 ], \
    [ 1.1, 2.2, 3.3, 4.4 ] ], dtype = float )

  print ( '' )
  print ( 'r8vec_eq_test():' )
  print ( '  r8vec_eq() is TRUE if two R8VECs are equal.' )

  for i in range ( 0, test_num ):

    a = a_test[i,0:n].copy ( )
    b = b_test[i,0:n].copy ( )

    r8vec2_print ( a, b, '  Vectors A and B:' )

    value = r8vec_eq ( n, a, b )

    print ( '  r8vec_eq(A,B) = %s' % ( value ) )

  return

def r8vec_even ( n, alo, ahi ):

#*****************************************************************************80
#
## r8vec_even() returns N real values, evenly spaced between ALO and AHI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values.
#
#    real ALO, AHI, the low and high values.
#
#  Output:
#
#    real A(N), N evenly spaced values.
#    Normally, A(1) = ALO and A(N) = AHI.
#    However, if N = 1, then A(1) = 0.5*(ALO+AHI).
#
  import numpy as np

  a = np.zeros ( n )

  if ( n == 1 ):

    a[0] = 0.5 * ( alo + ahi )

  else:

    for i in range ( 0, n ):
      a[i] = ( ( n - 1 - i ) * alo + i * ahi ) / float ( n - 1 )

  return a

def r8vec_even_test ( ):

#*****************************************************************************80
#
## r8vec_even_test() tests r8vec_even().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  n = 10
  xlo = 0.0
  xhi = 99.0
 
  print ( '' )
  print ( 'r8vec_even_test():' )
  print ( '  r8vec_even computes N evenly spaced values' )
  print ( '  between XLO and XHI.' )
  print ( '' )
  print ( '  XLO = %f' % ( xlo ) )
  print ( '  XHI = %f' % ( xhi ) )
  print ( '  while N = %d' % ( n ) )
 
  x = r8vec_even ( n, xlo, xhi )
 
  r8vec_print ( n, x, '  Resulting array:' )

  return

def r8vec_even_select ( n, xlo, xhi, ival ):

#*****************************************************************************80
#
## r8vec_even_select() returns the I-th of N evenly spaced values in [ XLO, XHI ].
#
#  Discussion:
#
#    XVAL = ( (N-IVAL) * XLO + (IVAL-1) * XHI ) / dble ( N - 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values.
#
#    real XLO, XHI, the low and high values.
#
#    integer IVAL, the index of the desired point.
#    IVAL is normally between 1 and N, but may be any
#    integer value.
#
#  Output:
#
#    real XVAL, the IVAL-th of N evenly spaced values
#    between XLO and XHI.
#    Unless N = 1, X(1) = XLO and X(N) = XHI.
#    If N = 1, then X(1) = 0.5*(XLO+XHI).
#
  if ( n == 1 ):

    xval = 0.5 * ( xlo + xhi )

  else:

    xval = ( float ( n - ival     ) * xlo   \
           + float (     ival - 1 ) * xhi ) \
           / float ( n        - 1 )

  return xval

def r8vec_even_select_test ( ):

#*****************************************************************************80
#
## r8vec_even_select_test() tests r8vec_even_select().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  n = 10
  xlo = 0.0
  xhi = 99.0
 
  print ( '' )
  print ( 'r8vec_even_select_test():' )
  print ( '  r8vec_even_select returns the I-th of N evenly spaced values' )
  print ( '  between XLO and XHI.' )
  print ( '' )
  print ( '  XLO = %f' % ( xlo ) )
  print ( '  XHI = %f' % ( xhi ) )
  print ( '  while N = %d' % ( n ) )
  print ( '' )
 
  for i in range ( 2, n + 1, 3 ):
    xi = r8vec_even_select ( n, xlo, xhi, i )
    print ( '  X(%d) = %g' % ( i, xi ) )

  return

def r8vec_expand_linear ( n, x, fat ):

#*****************************************************************************80
#
## r8vec_expand_linear() linearly interpolates new data into a vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of input data values.
#
#    real X(N), the original data.
#
#    integer FAT, the number of data values to interpolate
#    between each pair of original data values.
#
#  Output:
#
#    real XFAT((N-1)*(FAT+1)+1), the "fattened" data.
#
  import numpy as np

  xfat = np.zeros ( ( n - 1 ) * ( fat + 1 ) + 1 )

  k = 0

  for i in range ( 1, n ):

    xfat[k] = x[i-1]
    k = k + 1

    for j in range ( 1, fat + 1 ):
      xfat[k] = ( ( fat - j + 1 ) * x[i-1] \
                + (       j     ) * x[i] ) \
                / ( fat     + 1 )
      k = k + 1

  xfat[k] = x[n-1]
  k = k + 1

  return xfat

def r8vec_expand_linear2 ( n, x, before, fat, after ):

#*****************************************************************************80
#
## r8vec_expand_linear2() linearly interpolates new data into an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    This routine starts with a vector of data.
#
#    The intent is to "fatten" the data, that is, to insert more points
#    between successive values of the original data.
#
#    There will also be extra points placed BEFORE the first original
#    value and AFTER that last original value.
#
#    The "fattened" data is equally spaced between the original points.
#
#    The BEFORE data uses the spacing of the first original interval,
#    and the AFTER data uses the spacing of the last original interval.
#
#  Example:
#
#    N = 3
#    BEFORE = 3
#    FAT = 2
#    AFTER = 1
#
#    X    = (/                   0.0,           6.0,             7.0       /)
#    XFAT = (/ -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 6.33, 6.66, 7.0, 7.66 /)
#            3 "BEFORE's"        Old  2 "FATS"  Old    2 "FATS"  Old  1 "AFTER"
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of input data values.
#    N must be at least 2.
#
#    real X(N), the original data.
#
#    integer BEFORE, the number of "before" values.
#
#    integer FAT, the number of data values to interpolate
#    between each pair of original data values.
#
#    integer AFTER, the number of "after" values.
#
#  Output:
#
#    real XFAT(BEFORE+(N-1)*(FAT+1)+1+AFTER), the "fattened" data.
#
  import numpy as np

  xfat = np.zeros ( before+(n-1)*(fat+1)+1+after )

  k = 0
#
#  Points BEFORE.
#
  for j in range ( 1 - before + fat, fat + 1 ):

    xfat[k] = ( ( fat - j + 1 ) * ( x[0] - ( x[1] - x[0] ) ) \
              + (       j     ) *   x[0]          ) \
              / ( fat     + 1 )
    k = k + 1
#
#  Original points and FAT points.
#
  for i in range ( 1, n ):

    xfat[k] = x[i-1]
    k = k + 1

    for j in range ( 1, fat + 1 ):
      xfat[k] = ( ( fat - j + 1 ) * x[i-1] \
                + (       j     ) * x[i] ) \
                / ( fat     + 1 )
      k = k + 1

  xfat[k] = x[n-1]
  k = k + 1
#
#  Points AFTER.
#
  for j in range ( 1, after + 1 ):
    xfat[k] = ( ( fat - j + 1 ) *   x[n-1] \
              + (       j     ) * ( x[n-1] + ( x[n-1] - x[n-2] ) ) ) \
              / ( fat     + 1 )
    k = k + 1

  return xfat

def r8vec_fill ( n, value ):

#*****************************************************************************80
#
## r8vec_fill() sets all entries of an array to a given value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    real VALUE, the value.
#
#  Output:
#
#    real X(N), the array.
#
  import numpy as np

  x = value * np.ones ( n )

  return x

def r8vec_fill_test ( ):

#*****************************************************************************80
#
## r8vec_fill_test() tests r8vec_fill().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10
  ahi = 10.0
  alo = 0.0

  print ( '' )
  print ( 'r8vec_fill_test():' )
  print ( '  r8vec_fill() sets all entries of an array to a given value.' )

  n = 5
  value = 1.2
  x = r8vec_fill ( n, value )
  r8vec_print ( n, x, '  x=r8vec_fill(5,1.2):' )

  n = 3
  value = -123.456
  x = r8vec_fill ( n, value )
  r8vec_print ( n, x, '  x=r8vec_fill(3,123.456):' )

  return

def r8vec_frac ( n, a, k ):

#*****************************************************************************80
#
## r8vec_frac() searches for the K-th smallest entry in an R8VEC.
#
#  Discussion:
#
#    Hoare's algorithm is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    real A(N), the array to search.
#
#    integer K, the fractile to be sought.  If K = 1, the minimum
#    entry is sought.  If K = N, the maximum is sought.  Other values
#    of K search for the entry which is K-th in size.  K must be at
#    least 1, and no greater than N.
#
#  Output:
#
#    real FRAC, the value of the K-th fractile of A.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'r8vec_frac - Fatal error!' )
    print ( '  Illegal nonpositive value of N = %d' % ( n ) )
    raise Exception ( 'r8vec_frac - Fatal error!' )

  if ( k <= 0 ):
    print ( '' )
    print ( 'r8vec_frac - Fatal error!' )
    print ( '  Illegal nonpositive value of K = %d' % ( k ) )
    raise Exception ( 'r8vec_frac - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'r8vec_frac - Fatal error!' )
    print ( '  Illegal N < K, K = %d' % ( k ) )
    raise Exception ( 'r8vec_frac - Fatal error!' )

  left = 1
  iryt = n

  while ( True ):

    if ( iryt <= left ):
      frac = a[k-1]
      break

    x = a[k-1]
    i = left
    j = iryt

    while ( True ):

      if ( j < i ):
        if ( j < k ):
          left = i
        if ( k < i ):
          iryt = j
        break;
#
#  Find I so that X <= A(I)
#
      while ( a[i-1] < x ):
        i = i + 1
#
#  Find J so that A(J) <= X
#
      while ( x < a[j-1] ):
        j = j - 1

      if ( i <= j ):

        temp   = a[i-1]
        a[i-1] = a[j-1]
        a[j-1] = temp

        i = i + 1
        j = j - 1

  return frac

def r8vec_frac_test ( rng ):

#*****************************************************************************80
#
## r8vec_frac_test() tests r8vec_frac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10
  ahi = 10.0
  alo = 0.0

  print ( '' )
  print ( 'r8vec_frac_test():' )
  print ( '  r8vec_frac(): K-th smallest real vector entry;' )

  a = r8vec_uniform_ab ( n, alo, ahi, rng )

  r8vec_print ( n, a, '  The real array to search: ' )

  print ( '' )
  print ( 'Frac   r8vec_frac' )
  print ( '' )

  for k in range ( 1, n + 1 ):

    afrac = r8vec_frac ( n, a, k )
    print ( '  %2d  %6f' % ( k, afrac ) )

  return

def r8vec_house_column ( n, a_vec, k ):

#*****************************************************************************80
#
## r8vec_house_column() defines a Householder premultiplier that "packs" a column.
#
#  Discussion:
#
#    The routine returns a vector V that defines a Householder
#    premultiplier matrix H(V) that zeros out the subdiagonal entries of
#    column K of the matrix A.
#
#       H(V) = I - 2 * v * v'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix A.
#
#    real A_VEC(N), a row or column of the matrix A.
#
#    integer K, the "special" entry in A_VEC.
#    The Householder matrix will zero out the entries after this.
#
#  Output:
#
#    real V(N), a vector of unit L2 norm which defines an
#    orthogonal Householder premultiplier matrix H with the property
#    that the K-th column of H*A is zero below the diagonal.
#
  import numpy as np

  v = np.zeros ( n )

  if ( k < 0 or n - 1 <= k ):
    return v

  s = 0.0
  for i in range ( k, n ):
    s = s + a_vec[i] ** 2
  s = np.sqrt ( s )

  if ( s == 0.0 ):
    return v

  if ( a_vec[k] < 0.0 ):
    v[k] = a_vec[k] - abs ( s )
  else:
    v[k] = a_vec[k] + abs ( s )

  for i in range ( k + 1, n ):
    v[i] = a_vec[i]

  s = 0.0
  for i in range ( k, n ):
    s = s + v[i] ** 2
  s = np.sqrt ( s )

  for i in range ( k, n ):
    v[i] = v[i] / s

  return v

def r8vec_house_column_test ( rng ):

#*****************************************************************************80
#
## r8vec_house_column_test() tests r8vec_house_column().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_house_column_test():' )
  print ( '  r8vec_house_column() returns the compact form of' )
  print ( '  a Householder matrix that "packs" a column' )
  print ( '  of a matrix.' )
#
#  Get a random matrix.
#
  n = 4
  r8_lo = 0.0
  r8_hi = 5.0

  a = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, rng )

  r8mat_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ( '' )
    print ( '  Working on column K = %d' % ( k ) )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8mat_house_form ( n, v )

    r8mat_print ( n, n, h, '  Householder matrix H:' )

    ha = r8mat_mm ( n, n, n, h, a )

    r8mat_print ( n, n, ha, '  Product H*A:' )
#
#  If we set A := HA, then we can successively convert A to upper
#  triangular form.
#
    a = ha

  return

def r8vec_identity_row ( n, i ):

#*****************************************************************************80
#
## r8vec_identity_row() returns a row of the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer I, the index of the entry to be set to 1.
#    0-based indexing is used.
#
#  Output:
#
#    real A[1,N], the vector.
#
  import numpy as np

  a = np.zeros ( [ 1, n ] );

  if ( 0 <= i and i < n ):
    a[0,i] = 1.0

  return a

def r8vec_identity_row_test ( ):

#*****************************************************************************80
#
## r8vec_identity_row_test() tests r8vec_identity_row().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8vec_identity_row_test():' )
  print ( '  r8vec_identity_row() returns a row of the identity matrix.' )
  print ( '' )

  n = 5
  for i in range ( -1, 6 ):
    a = r8vec_identity_row ( n, i )
    print ( '%2d: ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( ' %d' % ( a[0,j] ), end = '' )
    print ( '' )

  return

def r8vec_indicator0 ( n ):

#*****************************************************************************80
#
## r8vec_indicator0() sets an R8VEC to the indicator vector (0,1,2,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i

  return a

def r8vec_indicator0_test ( ):

#*****************************************************************************80
#
## r8vec_indicator0_test() tests r8vec_indicator0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r8vec_indicator0_test():' )
  print ( '  r8vec_indicator0() returns an indicator matrix.' )

  n = 10
  a = r8vec_indicator0 ( n )

  r8vec_print ( n, a, '  The indicator0 vector:' )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_is_ascending ( n, x ):

#*****************************************************************************80
#
## r8vec_is_ascending() determines if an R8VEC is (weakly) ascending.
#
#  Example:
#
#    X = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.5, 9.8 )
#
#    value = true
#
#    The sequence is not required to be strictly ascending.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the array.
#
#    real X(N), the array to be examined.
#
#  Output:
#
#    bool VALUE, is true if the entries of X ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i+1] < x[i] ):
      value = False
      break

  return value

def r8vec_is_ascending_test ( ):

#*****************************************************************************80
#
## r8vec_is_ascending_test() tests r8vec_is_ascending().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_ascending_test():' )
  print ( '  r8vec_is_ascending() is TRUE if the entries of an R8VEC' )
  print ( '  are ascending.' )

  n = 4

  x = np.array ( [ 1.0, 2.0, 0.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending ( n, x ) ):
    print ( '  X is ascending.' )
  else:
    print ( '  X is NOT ascending.' )

  x = np.array ( [ 1.0, 2.0, 2.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending ( n, x ) ):
    print ( '  X is ascending.' )
  else:
    print ( '  X is NOT ascending.' )

  x = np.array ( [ 1.0, 2.0, 4.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending ( n, x ) ):
    print ( '  X is ascending.' )
  else:
    print ( '  X is NOT ascending.' )

  return

def r8vec_is_ascending_strictly ( n, x ):

#*****************************************************************************80
#
## r8vec_is_ascending_strictly() determines if an R8VEC is strictly ascending.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    Notice the effect of entry number 6 in the following results:
#
#      X = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.4, 9.8 )
#      Y = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.5, 9.8 )
#      Z = ( -8.1, 1.3, 2.2, 3.4, 7.5, 7.6, 9.8 )
#
#      r8vec_is_ascending_strictly ( X ) = false
#      r8vec_is_ascending_strictly ( Y ) = false
#      r8vec_is_ascending_strictly ( Z ) = true
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the array.
#
#    real X(N), the array to be examined.
#
#  Output:
#
#    bool VALUE, is true if the
#    entries of X strictly ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i+1] <= x[i] ):
      value = False
      break

  return value

def r8vec_is_ascending_strictly_test ( ):

#*****************************************************************************80
#
## r8vec_is_ascending_strictly_test() tests r8vec_is_ascending_strictly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_ascending_strictly_test():' )
  print ( '  r8vec_is_ascending_strictly() is TRUE if the entries of an R8VEC' )
  print ( '  are strictly ascending.' )

  n = 4

  x = np.array ( [ 1.0, 2.0, 0.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending_strictly ( n, x ) ):
    print ( '  X is strictly ascending.' )
  else:
    print ( '  X is NOT strictly ascending.' )

  x = np.array ( [ 1.0, 2.0, 2.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending_strictly ( n, x ) ):
    print ( '  X is strictly ascending.' )
  else:
    print ( '  X is NOT strictly ascending.' )

  x = np.array ( [ 1.0, 2.0, 4.0, 9.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_ascending_strictly ( n, x ) ):
    print ( '  X is strictly ascending.' )
  else:
    print ( '  X is NOT strictly ascending.' )

  return

def r8vec_is_binary ( n, x ):

#*****************************************************************************80
#
## r8vec_is_binary() is true if an R8VEC only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    real VALUE, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, n ):

    if ( x[i] != 0.0 and x[i] != 1.0 ):
      value = False
      break

  return value

def r8vec_is_binary_test ( ):

#*****************************************************************************80
#
## r8vec_is_binary_test() tests r8vec_is_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_binary_test():' )
  print ( '  r8vec_is_binary() is TRUE if an R8VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0.0, 2.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  return

def r8vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## r8vec_is_distinct() is true if the entries in an R8VEC are distinct.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be checked.
#
#  Output:
#
#    bool VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

def r8vec_is_distinct_test ( ):

#*****************************************************************************80
#
## r8vec_is_distinct_test() tests r8vec_is_distinct().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_distinct_test():' )
  print ( '  r8vec_is_distinct() computes the maximum entry in an R8VEC.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 3.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 2.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  return

def r8vec_is_in_01 ( n, x ):

#*****************************************************************************80
#
## r8vec_is_in_01() is true if all entries are in [0,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    real VALUE, is true if all entries are in [0,1].
#
  import numpy as np

  value = ( np.all ( 0.0 <= x[0:n] ) and np.all ( x[0:n] <= 1.0 ) )

  return value

def r8vec_is_in_01_test ( ):

#*****************************************************************************80
#
## r8vec_is_in_01_test() tests r8vec_is_in_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_in_01_test():' )
  print ( '  r8vec_is_in_01() is TRUE if an R8VEC only contains' )
  print ( '  entries in [0,1].' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_01 ( n, x ) ):
    print ( '  All entries are in [0,1].' )
  else:
    print ( '  At least one entry is NOT in [0,1].' )

  x = np.array ( [ 0.5, 0.1, 0.9 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_01 ( n, x ) ):
    print ( '  All entries are in [0,1].' )
  else:
    print ( '  At least one entry is NOT in [0,1].' )

  x = np.array ( [ -0.5, 0.5, 0.4 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_01 ( n, x ) ):
    print ( '  All entries are in [0,1].' )
  else:
    print ( '  At least one entry is NOT in [0,1].' )

  return

def r8vec_is_in_ab ( n, x, a, b ):

#*****************************************************************************80
#
## r8vec_is_in_ab() is true if all entries are in [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#    real A, B, the limits, with A <= B.
#
#  Output:
#
#    bool VALUE, is true if all entries are in [A,B].
#
  import numpy as np

  value = ( np.all ( a <= x[0:n] ) and np.all ( x[0:n] <= b ) )

  return value

def r8vec_is_in_ab_test ( ):

#*****************************************************************************80
#
## r8vec_is_in_ab_test() tests r8vec_is_in_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_in_ab_test():' )
  print ( '  r8vec_is_in_ab() is TRUE if an R8VEC only contains' )
  print ( '  entries in [A,B].' )

  n = 3
  a = 0.5
  b = 2.0

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_ab ( n, x, a, b ) ):
    print ( '  All entries are in [%f,%f].' % ( a, b ) )
  else:
    print ( '  At least one entry is NOT in [%f,%f].' % ( a, b ) )

  x = np.array ( [ 0.5, 1.1, 0.9 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_ab ( n, x, a, b ) ):
    print ( '  All entries are in [%f,%f].' % ( a, b ) )
  else:
    print ( '  At least one entry is NOT in [%f,%f].' % ( a, b ) )

  x = np.array ( [ -0.5, 0.5, 0.4 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_ab ( n, x, a, b ) ):
    print ( '  All entries are in [%f,%f].' % ( a, b ) )
  else:
    print ( '  At least one entry is NOT in [%f,%f].' % ( a, b ) )

  return

def r8vec_is_insignificant ( n, r, s ):

#*****************************************************************************80
#
## r8vec_is_insignificant() determines if an R8VEC is relatively insignificant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real R(N), the vector to be compared against.
#
#    real S(N), the vector to be compared.
#
#  Output:
#
#    bool VALUE, is true if S is insignificant
#    relative to R.
#
  eps = 2.220446049250313E-016

  value = True

  for i in range ( 0, n ):
    t = r[i] + s[i]
    tol = eps * abs ( r[i] )

    if ( tol < abs ( r[i] - t ) ):
      value = False
      break
  
  return value

def r8vec_is_insignificant_test ( ):

#*****************************************************************************80
#
## r8vec_is_insignificant_test() tests r8vec_is_insignificant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_insignificant_test():' )
  print ( '  r8vec_is_insignificant() is TRUE if an R8VEC only contains' )
  print ( '  negative entries.' )

  eps = 2.220446049250313E-016

  n = 3

  x = np.array ( [ 1.0, 2.0, 100.0 ] )
  y = 100000.0 * eps * np.array ( [ 1.0, 2.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  r8vec_transpose_print ( n, y, '  Y:' )
  if ( r8vec_is_insignificant ( n, x, y ) ):
    print ( '  Y is insignificant compared to X.' )
  else:
    print ( '  Y is NOT insignificant compared to X.' )

  x = np.array ( [ 1.0, 2.0, 100.0 ] )
  y = 10.0 * eps * np.array ( [ 1.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  r8vec_transpose_print ( n, y, '  Y:' )
  if ( r8vec_is_insignificant ( n, x, y ) ):
    print ( '  Y is insignificant compared to X.' )
  else:
    print ( '  Y is NOT insignificant compared to X.' )

  x = np.array ( [ 1.0, 2.0, 100.0 ] )
  y = 0.0001 * eps * np.array ( [ 1.0, 2.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  r8vec_transpose_print ( n, y, '  Y:' )
  if ( r8vec_is_insignificant ( n, x, y ) ):
    print ( '  Y is insignificant compared to X.' )
  else:
    print ( '  Y is NOT insignificant compared to X.' )

  return

def r8vec_is_integer ( n, x ):

#*****************************************************************************80
#
## r8vec_is_integer() is true if every entry is an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if all entries are integers.
#
  import numpy as np

  value = np.all ( x[0:n] == np.round ( x[0:n] ) )

  return value

def r8vec_is_integer_test ( ):

#*****************************************************************************80
#
## r8vec_is_integer_test() tests r8vec_is_integer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_integer_test():' )
  print ( '  r8vec_is_integer() is TRUE if an R8VEC contains' )
  print ( '  only integer entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  x = np.array ( [ 1.0, 2.5, 3.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  return

def r8vec_is_negative_any ( n, x ):

#*****************************************************************************80
#
## r8vec_is_negative_any() is true if an R8VEC contains any negative entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if any entry is negative.
#
  import numpy as np

  value = np.any ( x[0:n] < 0.0 )

  return value

def r8vec_is_negative_any_test ( ):

#*****************************************************************************80
#
## r8vec_is_negative_any_test() tests r8vec_is_negative_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_negative_any_test():' )
  print ( '  r8vec_is_negative_any() is TRUE if an R8VEC contains' )
  print ( '  any negative entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative_any ( n, x ) ):
    print ( '  X contains at least one negative entry.' )
  else:
    print ( '  X does NOT contain any negative entries.' )

  x = np.array ( [ -1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative_any ( n, x ) ):
    print ( '  X contains at least one negative entry.' )
  else:
    print ( '  X does NOT contain any negative entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative_any ( n, x ) ):
    print ( '  X contains at least one negative entry.' )
  else:
    print ( '  X does NOT contain any negative entries.' )

  return

def r8vec_is_negative ( n, x ):

#*****************************************************************************80
#
## r8vec_is_negative() is true if an R8VEC only contains negative entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if X only contains
#    negative entries.
#
  import numpy as np

  value = np.all ( x[0:n] < 0.0 )

  return value

def r8vec_is_negative_test ( ):

#*****************************************************************************80
#
## r8vec_is_negative_test() tests r8vec_is_negative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_negative_test():' )
  print ( '  r8vec_is_negative() is TRUE if an R8VEC only contains' )
  print ( '  negative entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative ( n, x ) ):
    print ( '  X contains only negative entries.' )
  else:
    print ( '  X does NOT contain only negative entries.' )

  x = np.array ( [ -1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative ( n, x ) ):
    print ( '  X contains only negative entries.' )
  else:
    print ( '  X does NOT contain only negative entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_negative ( n, x ) ):
    print ( '  X contains only negative entries.' )
  else:
    print ( '  X does NOT contain only negative entries.' )

  return

def r8vec_is_nonnegative ( n, x ):

#*****************************************************************************80
#
## r8vec_is_nonnegative() is true if an R8VEC only contains nonnegative entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if X only contains
#    nonnegative entries.
#
  import numpy as np

  value = np.all ( 0.0 <= x[0:n] )

  return value

def r8vec_is_nonnegative_test ( ):

#*****************************************************************************80
#
## r8vec_is_nonnegative_test() tests r8vec_is_nonnegative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_nonnegative_test():' )
  print ( '  r8vec_is_nonnegative() is TRUE if an R8VEC only contains' )
  print ( '  nonnegative entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonnegative ( n, x ) ):
    print ( '  X contains only nonnegative entries.' )
  else:
    print ( '  X does NOT contain only nonnegative entries.' )

  x = np.array ( [ -1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonnegative ( n, x ) ):
    print ( '  X contains only nonnegative entries.' )
  else:
    print ( '  X does NOT contain only nonnegative entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonnegative ( n, x ) ):
    print ( '  X contains only nonnegative entries.' )
  else:
    print ( '  X does NOT contain only nonnegative entries.' )

  return

def r8vec_is_nonpositive ( n, x ):

#*****************************************************************************80
#
## r8vec_is_nonpositive() is true if an R8VEC only contains nonpositive entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if X only contains
#    nonpositive entries.
#
  import numpy as np

  value = np.all ( x[0:n] <= 0.0 )

  return value

def r8vec_is_nonpositive_test ( ):

#*****************************************************************************80
#
## r8vec_is_nonpositive_test() tests r8vec_is_nonpositive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r8vec_is_nonpositive_test():' )
  print ( '  r8vec_is_nonpositive() is TRUE if an R8VEC only contains' )
  print ( '  nonpositive entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonpositive ( n, x ) ):
    print ( '  X contains only nonpositive entries.' )
  else:
    print ( '  X does NOT contain only nonpositive entries.' )

  x = np.array ( [ -2.0, -1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonpositive ( n, x ) ):
    print ( '  X contains only nonpositive entries.' )
  else:
    print ( '  X does NOT contain only nonpositive entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonpositive ( n, x ) ):
    print ( '  X contains only nonpositive entries.' )
  else:
    print ( '  X does NOT contain only nonpositive entries.' )

  return

def r8vec_is_nonzero_any ( n, x ):

#*****************************************************************************80
#
## r8vec_is_nonzero_any() is true if any entry is nonzero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if X only contains
#    nonzero entries.
#
  import numpy as np

  value = np.any ( x[0:n] != 0.0 )

  return value

def r8vec_is_nonzero_any_test ( ):

#*****************************************************************************80
#
## r8vec_is_nonzero_any_test() tests r8vec_is_nonzero_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r8vec_is_nonzero_any_test():' )
  print ( '  r8vec_is_nonzero_any() is TRUE if an R8VEC contains' )
  print ( '  any nonzero entry.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonzero_any ( n, x ) ):
    print ( '  X contains at least one nonzero entry.' )
  else:
    print ( '  X contains NO nonzero entries.' )

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonzero_any ( n, x ) ):
    print ( '  X contains at least one nonzero entry.' )
  else:
    print ( '  X contains NO nonzero entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_nonzero_any ( n, x ) ):
    print ( '  X contains at least one nonzero entry.' )
  else:
    print ( '  X contains NO nonzero entries.' )

  return

def r8vec_is_one ( n, x ):

#*****************************************************************************80
#
## r8vec_is_one() is true if every entry is one.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if all entries are one.
#
  import numpy as np

  value = np.all ( x[0:n] == 1.0 )

  return value

def r8vec_is_one_test ( ):

#*****************************************************************************80
#
## r8vec_is_one_test() tests r8vec_is_one().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_one_test():' )
  print ( '  r8vec_is_one() is TRUE if an R8VEC contains' )
  print ( '  only one entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_one ( n, x ) ):
    print ( '  X contains only one entries.' )
  else:
    print ( '  X contains at least one nonone entry.' )

  x = np.array ( [ 1.0, 1.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_one ( n, x ) ):
    print ( '  X contains only one entries.' )
  else:
    print ( '  X contains at least one nonone entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_one ( n, x ) ):
    print ( '  X contains only one entries.' )
  else:
    print ( '  X contains at least one nonone entry.' )

  return

def r8vec_is_positive ( n, x ):

#*****************************************************************************80
#
## r8vec_is_positive() is true if an R8VEC only contains  strictly positive entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if X only contains
#    strictly positive entries.
#
  import numpy as np

  value = np.all ( 0.0 < x[0:n] )

  return value

def r8vec_is_positive_test ( ):

#*****************************************************************************80
#
## r8vec_is_positive_test() tests r8vec_is_positive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_positive_test():' )
  print ( '  r8vec_is_positive() is TRUE if an R8VEC only contains' )
  print ( '  strictly positive entries.' )

  n = 3

  x = np.array ( [ 1.0, 2.0, 3.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_positive ( n, x ) ):
    print ( '  X contains only positive entries.' )
  else:
    print ( '  X does NOT contain only positive entries.' )

  x = np.array ( [ 2.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_positive ( n, x ) ):
    print ( '  X contains only positive entries.' )
  else:
    print ( '  X does NOT contain only positive entries.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_positive ( n, x ) ):
    print ( '  X contains only positive entries.' )
  else:
    print ( '  X does NOT contain only positive entries.' )

  return

def r8vec_is_zero ( n, x ):

#*****************************************************************************80
#
## r8vec_is_zero() is true if every entry is zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if all entries are zero.
#
  import numpy as np

  value = np.all ( x[0:n] == 0.0 )

  return value

def r8vec_is_zero_test ( ):

#*****************************************************************************80
#
## r8vec_is_zero_test() tests r8vec_is_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_zero_test():' )
  print ( '  r8vec_is_zero() is TRUE if an R8VEC contains' )
  print ( '  only zero entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  return

def r8vec_linspace2 ( n, a, b ):

#*****************************************************************************80
#
## r8vec_linspace2() creates a vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    5 points evenly spaced between 0 and 12 will yield 2, 4, 6, 8, 10.
#
#    In other words, the interval is divided into N+1 even subintervals,
#    and the endpoints of internal intervals are used as the points.
#
#    numpy's linspace() does something non-mathematical when n=1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( float ( n - i     ) * a \
           + float (     i + 1 ) * b ) \
           / float ( n     + 1 )
 
  return x

def r8vec_linspace2_test ( ):

#*****************************************************************************80
#
## r8vec_linspace2_test() tests r8vec_linspace2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_linspace2_test():' )
  print ( '  r8vec_linspace2() returns evenly spaced values between A and B' )
  print ( '  omitting the endpoints.' )

  n = 4
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace2 ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace2 vector:' )

  return

def r8vec_linspace ( n, a, b ):

#*****************************************************************************80
#
## r8vec_linspace() creates a column vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    While MATLAB has the built in command 
#
#      x = linspace ( a, b, n )
#
#    that command has the distinct disadvantage of returning a ROW vector.
#
#    4 points evenly spaced between 0 and 12 will yield 0, 4, 8, 12.
#
#    In other words, the interval is divided into N-1 even subintervals,
#    and the endpoints of intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):
     x[i] = ( ( n - 1 - i ) * a \
            + (         i ) * b ) \
            / ( n - 1     )
 
  return x

def r8vec_linspace_test ( ):

#*****************************************************************************80
#
## r8vec_linspace_test() tests r8vec_linspace().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_linspace_test():' )
  print ( '  r8vec_linspace() returns evenly spaced values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace vector:' )

  return

def r8vec_max_abs_index ( n, a ):

#*****************************************************************************80
#
## r8vec_max_abs_index(): index of entry of maximum absolute value in an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    real A(N), the array.
#
#  Output:
#
#    integer MAX_abs_index, the index of the entry of maximum
#    absolute value.
#
  if ( n <= 0 ):

    max_abs_index = -1

  else:

    max_abs_index = 0

    for i in range ( 1, n ):
      if ( abs ( a[max_abs_index] ) < abs ( a[i] ) ):
        max_abs_index = i

  return max_abs_index

def r8vec_max_abs_index_test ( rng ):

#*****************************************************************************80
#
## r8vec_max_abs_index_test() tests r8vec_max_abs_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10
 
  print ( '' )
  print ( 'r8vec_max_abs_index_test():' )
  print ( '  r8vec_max_abs_index(): index of entry of maximum absolute value' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )
 
  r8vec_print ( n, a, '  Input vector:' )

  ival = r8vec_max_abs_index ( n, a )

  print ( '' )
  print ( '  Maximum index: %d' % ( ival ) )

  return

def r8vec_max_index ( n, a ):

#*****************************************************************************80
#
## r8vec_max_index() returns the index of the maximum value in an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    real A(N), the array.
#
#  Output:
#
#    integer MAX_index, the index of the largest entry.
#
  if ( n <= 0 ):

    max_index = -1

  else:

    max_index = 0

    for i in range ( 1, n ):
      if ( a[max_index] < a[i] ):
        max_index = i

  return max_index

def r8vec_max_index_test ( rng ):

#*****************************************************************************80
#
## r8vec_max_index_test() tests r8vec_max_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10
 
  print ( '' )
  print ( 'r8vec_max_index_test():' )
  print ( '  r8vec_max_index(): index of maximum entry' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )
 
  r8vec_print ( n, a, '  Input vector:' )

  ival = r8vec_max_index ( n, a )

  print ( '' )
  print ( '  Maximum index: %d' % ( ival ) )

  return

def r8vec_max ( n, a ):

#*****************************************************************************80
#
## r8vec_max() returns the maximum value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the maximum value in the vector.
#
  import numpy as np

  huge = np.finfo(float).max

  value = - huge
  for i in range ( 0, n ):
    if ( value < a[i] ):
      value = a[i]

  return value

def r8vec_max_test ( rng ):

#*****************************************************************************80
#
## r8vec_max_test() tests r8vec_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_max_test():' )
  print ( '  r8vec_max() computes the maximum entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = a_lo + ( a_hi - a_lo ) * rng.random ( size = n )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_max ( n, a )
  print ( '' )
  print ( '  Max = %g' % ( value ) )

  return

def r8vec_mean_geometric ( n, a ):

#*****************************************************************************80
#
## r8vec_mean_geometric() returns the geometric mean of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#    All entries should be nonnegative.
#
#  Output:
#
#    real VALUE, the geometric mean of the vector.
#
  import numpy as np

  value = np.exp ( np.sum ( np.log ( a[0:n] ) ) / float ( n ) );

  return value

def r8vec_mean_geometric_test ( rng ):

#*****************************************************************************80
#
## r8vec_mean_geometric_test() tests r8vec_mean_geometric().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_mean_geometric_test():' )
  print ( '  r8vec_mean_geometric() computes the geometric mean of an R8VEC.' )

  n = 10
  r8_lo = 0.0
  r8_hi = 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_mean_geometric ( n, a )
  print ( '' )
  print ( '  Geometric mean = %g' % ( value ) )

  return

def r8vec_mean ( n, a ):

#*****************************************************************************80
#
## r8vec_mean() returns the mean of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the mean of the vector.
#
  import numpy as np

  value = np.sum ( a ) / float ( n )

  return value

def r8vec_mean_test ( rng ):

#*****************************************************************************80
#
## r8vec_mean_test() tests r8vec_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_mean_test():' )
  print ( '  r8vec_mean() computes the mean of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_mean ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )

  return

def r8vec_mean_running ( n, v ):

#*****************************************************************************80
#
## r8vec_mean_running() computes the running mean of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items.
#
#    real V(N), the data.
#
#  Output:
#
#    real A(N+1), the running means.  A(I) is the average value
#    of the first I-1 values in V.
#
  import numpy as np

  a = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    a[i] = a[i-1] + v[i-1]
#
#  Average.
#
  for i in range ( 1, n + 1 ):
    a[i] = a[i] / float ( i )

  return a

def r8vec_mean_running_test ( rng ):

#*****************************************************************************80
#
## r8vec_mean_running_test() tests r8vec_mean_running().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_mean_running_test():' )
  print ( '  r8vec_mean_running() returns the running means of an R8VEC.' )

  n = 10
  a = -5.0
  b = +10.0

  r = r8vec_uniform_ab ( n, a, b, rng )

  r8vec_print ( n, r, '  Random R8VEC:' )

  s = r8vec_mean_running ( n, r )

  r8vec_print ( n + 1, s, '  Running means:' )

  return

def r8vec_mean_update ( nm1, mean_nm1, xn ):

#*****************************************************************************80
#
## r8vec_mean_update() updates the mean of an R8VEC with one new value.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NM1, the number of entries in the old vector.
#
#    real MEAN_NM1, the mean of the old vector.
#
#    real XN, the new N-th entry of the vector.
#
#  Output:
#
#    integer N, the number of entries in the new vector.
#
#    real MEAN_N, the mean of the new vector.
#
  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n

  return n, mean_n

def r8vec_mean_update_test ( rng ):

#*****************************************************************************80
#
## r8vec_mean_update_test() tests r8vec_mean_update().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_mean_update_test():' )
  print ( '  r8vec_mean_update() updates the mean of a vector' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R               MEAN         MEAN_update' )
  print ( '' )

  n_max = 10
  a = np.zeros ( n_max )
  mean_n = 0.0

  for i in range ( 1, n_max ):

    r = rng.random ( )
    a[i-1] = r
    mean = r8vec_mean ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    n, mean_n = r8vec_mean_update ( nm1, mean_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, mean, mean_n ) )

  return

def r8vec_midspace ( n, a, b ):

#*****************************************************************************80
#
## r8vec_midspace() creates a vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    This function divides the interval [a,b] into n subintervals, and then
#    returns the midpoints of those subintervals.
#
#  Example:
#
#    N = 5, A = 10, B = 20
#    X = [ 11, 13, 15, 17, 19 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the endpoints of the interval.
#
#  Output:
#
#    real X(N), a vector of linearly spaced data.
#
  import numpy as np
  
  if ( n == 1 ):
    x = ( a + b ) / 2.0
  else:
    a2 = a + ( b - a ) / 2.0 / float ( n )
    b2 = b - ( b - a ) / 2.0 / float ( n )
    x = np.linspace ( a2, b2, n )

  return x

def r8vec_midspace_test ( ):

#*****************************************************************************80
#
## r8vec_midspace_test() tests r8vec_midspace().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_midspace_test():' )
  print ( '  r8vec_midspace() returns the midpoints of N intervals in [A,B].' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_midspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The midspace vector:' )

  return

def r8vec_min ( n, a ):

#*****************************************************************************80
#
## r8vec_min() returns the minimum value in an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the minimum value in the vector.
#
  import numpy as np

  huge = np.finfo(float).max

  value = huge
  for i in range ( 0, n ):
    if ( a[i] < value ):
      value = a[i]

  return value

def r8vec_min_test ( rng ):

#*****************************************************************************80
#
## r8vec_min_test() tests r8vec_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_min_test():' )
  print ( '  r8vec_min() computes the minimum entry in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = a_lo + ( a_hi - a_lo ) * rng.random ( size = n )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_min ( n, a )
  print ( '' )
  print ( '  Min = %g' % ( value ) )

  return

def r8vec_mirror_ab_next ( m, a, b, x, done ):

#*****************************************************************************80
#
## r8vec_mirror_ab_next() steps through "mirrored" versions of vector X.
#
#  Discussion:
#
#    X is an M component vector contained in a rectangle described by A and B,
#    that is, for each index I, we have
#      A(I) <= X(I) <= B(I).
#
#    "Mirrored" versions of the vector X have one or more components
#    reflected about the A or B limit.  
#
#    As long as each component of X is strictly between the limits A and B,
#    this means there will be 3^M possible versions of the vector.
#
#    If one component of X is equal to one limit or the other, this 
#    suppresses mirroring across that limit.  If one component of
#    X, A and B are equal, then no mirroring is done at all in that component.
# 
#  Example:
#
#      A = 0, 0, 0
#      X = 1, 1, 1
#      B = 2, 2, 2
#      results in the following sequence of 3x3x3 values:
#
#      0  0  0
#      0  0  1
#      0  0  2
#      0  1  0
#      0  1  1
#      .......
#      2  1  1
#      2  1  2
#      2  2  0
#      2  2  1
#      2  2  2
#
#    A = 0 1 0
#    X = 1 1 1
#    B = 2 2 2
#    results in the following sequence of 3x2x3 values:
#
#      0 1 0
#      0 1 1
#      0 1 2
#      0 2 0
#      0 2 1
#      0 2 2
#      1 1 0
#      1 1 1
#      1 1 2
#      1 2 0
#      1 2 1
#      1 2 2
#      2 1 0
#      2 1 1
#      2 1 2
#      2 2 0
#      2 2 1
#      2 2 2
#
#    A = 0 1 0
#    X = 1 1 1
#    B = 2 1 2
#    results in the following sequence of 3x1x3 values:
#
#      0 1 0
#      0 1 1
#      0 1 2
#      1 1 0
#      1 1 1
#      1 1 2
#      2 1 0
#      2 1 1
#      2 1 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of entries in the vector.
#
#    real A(M), B(M), the lower and upper limits.
#
#    real X(M), a vector being manipulated.
#
#    bool DONE.  On first call, DONE should be TRUE, and
#    A(I) <= X(I) <= B(I) for each index I. 
#
#  Output:
#
#    real X(M), the mirrored vector.
#
#    bool DONE.  On output, if DONE is TRUE,
#    then the returned value is the last entry in the sequence.
#

#
#  First call:
#
  if ( done ):
#
#  Ensure all A(I) <= X(I) <= B(I).
#
    for i in range ( 0, m ):

      if ( x[i] < a[i] ):
        print ( '' )
        print ( 'r8vec_mirror_ab_next - Fatal error!' )
        print ( '  Not every A(I) <= X(I).' )
        raise Exception ( 'r8vec_mirror_ab_next - Fatal error!' )

      if ( b[i] < x[i] ):
        print ( '' )
        print ( 'r8vec_mirror_ab_next - Fatal error!' )
        print ( '  Not every X(I) <= B(I).' )
        raise Exception ( 'r8vec_mirror_ab_next - Fatal error!' )
#
#  Set first element of sequence.
#
    x[0:m] = 2.0 * a[0:m] - x[0:m]
#
#  Unless A = B, our sequence is not done.
#
    done = True
    for i in range ( 0, m ):
      if ( a[i] != b[i] ):
        done = False
        break
#
#  Subsequent calls.
#
  else:
#
#  Initialize index to last.
#  loop
#    if index < 1, set DONE = true and return.
#    if the index-th value is below B, increment it and return
#    otherwise reset index-th value to A.
#    decrement the index.
#
    i = m - 1

    while ( 0 <= i ):

      if ( x[i] < a[i] ):
        x[i] = 2.0 * a[i] - x[i]
        return x, done
      elif ( x[i] < b[i] ):
        x[i] = 2.0 * b[i] - x[i]
        return x, done
      else:
        x[i] = x[i] - 2.0 * ( b[i] - a[i] )

      i = i - 1

    done = True

  return x, done

def r8vec_mirror_ab_next_test ( ):

#*****************************************************************************80
#
## r8vec_mirror_ab_next_test() tests r8vec_mirror_ab_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3

  print ( '' )
  print ( 'r8vec_mirror_ab_next_test():' )
  print ( '  r8vec_mirror_ab_next() generates all versions of' )
  print ( '  of a real vector X mirrored by A and B.' )

  a = np.array ( [ -0.5, -0.5, -0.5 ] )
  x = np.array ( [  0.0,  0.0,  0.0 ] )
  b = np.array ( [  0.5,  0.5,  0.5 ] )

  print ( '' )
  print ( '  Case 1: 3x3x3 possibilities:'  )
  print ( '' )

  r8vec_transpose_print ( m, a, '   A:' )
  r8vec_transpose_print ( m, x, '   X:' )
  r8vec_transpose_print ( m, b, '   B:' )

  print ( '' )

  i = 0
  done = True

  while ( True ):

    x, done = r8vec_mirror_ab_next ( m, a, b, x, done )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

    i = i + 1
    s = str ( i )

    r8vec_transpose_print ( m, x, s )

  a = np.array ( [ -0.5, -0.5, -0.5 ] )
  x = np.array ( [  0.0,  0.5,  0.0 ] )
  b = np.array ( [  0.5,  0.5,  0.5 ] )

  print ( '' )
  print ( '  Case 2: 3x2x3 possibilities:'  )
  print ( '' )

  r8vec_transpose_print ( m, a, '   A:' )
  r8vec_transpose_print ( m, x, '   X:' )
  r8vec_transpose_print ( m, b, '   B:' )

  print ( '' )

  i = 0
  done = True

  while ( True ):

    x, done = r8vec_mirror_ab_next ( m, a, b, x, done )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

    i = i + 1
    s = str ( i )

    r8vec_transpose_print ( m, x, s )

  a = np.array ( [  0.0, -0.5, -0.5 ] )
  x = np.array ( [  0.0,  0.0,  0.0 ] )
  b = np.array ( [  0.0,  0.5,  0.5 ] )

  print ( '' )
  print ( '  Case 3: 1x3x3 possibilities:'  )
  print ( '' )

  r8vec_transpose_print ( m, a, '   A:' )
  r8vec_transpose_print ( m, x, '   X:' )
  r8vec_transpose_print ( m, b, '   B:' )

  print ( '' )

  i = 0
  done = True

  while ( True ):

    x, done = r8vec_mirror_ab_next ( m, a, b, x, done )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

    i = i + 1
    s = str ( i )

    r8vec_transpose_print ( m, x, s )

  return

def r8vec_mirror_next ( n, a ):

#*****************************************************************************80
#
## r8vec_mirror_next() steps through all sign variations of an R8VEC.
#
#  Discussion:
#
#    In normal use, the user would set every element of A to be positive.
#    The routine will take the input value of A, and output a copy in
#    which the signs of one or more entries have been changed.  Repeatedly
#    calling the routine with the output from the previous call will generate
#    every distinct "variation" of A; that is, all possible sign variations.
#
#    When the output variable DONE is TRUE (or equal to 1), then the
#    output value of A is the last in the series.
#
#    Note that A may have some zero values.  The routine will essentially
#    ignore such entries; more exactly, it will not stupidly assume that -0
#    is a proper "variation" of 0!
#
#    Also, it is possible to call this routine with the signs of A set
#    in any way you like.  The routine will operate properly, but it
#    will nonethess terminate when it reaches the value of A in which
#    every nonzero entry has negative sign.
#
#    More efficient algorithms using the Gray code seem to require internal
#    memory in the routine,
#    or the passing back and forth of a "memory array", or the use of
#    global variables, or unnatural demands on the user.  This form of
#    the routine is about as clean as I can make it.
#
#  Example:
#
#      Input         Output
#    ---------    --------------
#    A            A         DONE
#    ---------    --------  ----
#     1  2  3     -1  2  3  false
#    -1  2  3      1 -2  3  false
#     1 -2  3     -1 -2  3  false
#    -1 -2  3      1  2 -3  false
#     1  2 -3     -1  2 -3  false
#    -1  2 -3      1 -2 -3  false
#     1 -2 -3     -1 -2 -3  false
#    -1 -2 -3      1  2  3  true
#
#     1  0  3     -1  0  3  false
#    -1  0  3      1  0 -3  false
#     1  0 -3     -1  0 -3  false
#    -1  0 -3      1  0  3  true
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), a vector of real numbers.
#
#  Output:
#
#    real A(N), some signs have been changed.
#
#    bool DONE, is TRUE if the input vector A was the last element
#    in the series (every entry was nonpositive); the output vector is reset 
#    so that all entries are nonnegative, but presumably the ride is over!
#

#
#  Seek the first strictly positive entry of A.
#
  positive = 0
  for i in range ( 0, n ):
    if ( 0.0 < a[i] ):
      positive = i + 1
      break
#
#  If there is no strictly positive entry of A, there is no successor.
#
  if ( positive == 0 ):
    for i in range ( 0, n ):
      a[i] = - a[i]
    done = True
  else:
    for i in range ( 0, positive ):
      a[i] = - a[i]
    done = False

  return a, done

def r8vec_mirror_next_test ( ):

#*****************************************************************************80
#
## r8vec_mirror_next_test() tests r8vec_mirror_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'r8vec_mirror_next_test():' )
  print ( '  r8vec_mirror_next() generates all sign variations' )
  print ( '  of a real vector.' )
  print ( '' )

  a = np.array ( [ 1.0, 2.0, 3.0 ] )

  k = 0

  while ( True ):

    print ( '  %2d' % ( k ), end = '' )
    for i in range ( 0, n ):
      print ( '  %6g' % ( a[i] ), end = '' )
    print ( '' )

    a, done = r8vec_mirror_next ( n, a )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

  a = np.array ( [ 1.0, 0.0, 3.0 ] )

  print ( '' )
  
  while ( True ):

    print ( '  %2d' % ( k ), end = '' )
    for i in range ( 0, n ):
      print ( '  %6g' % ( a[i] ), end = '' )
    print ( '' )

    a, done = r8vec_mirror_next ( n, a )

    if ( done ):
      print ( '' )
      print ( '  Done.' )
      break

  return

def r8vec_nint ( n, a ):

#*****************************************************************************80
#
## r8vec_nint() rounds entries of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be rounded.
#
#  Output:
#
#    real A(N), the rounded vector.
#
  for i in range ( 0, n ):
    a[i] = round ( a[i] )

  return a

def r8vec_nint_test ( rng ):

#*****************************************************************************80
#
## r8vec_nint_test() tests r8vec_nint().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_nint_test():' )
  print ( '  r8vec_nint() rounds an R8VEC.' )

  n = 5
  x1 = -5.0
  x2 = +5.0
  a = r8vec_uniform_ab ( n, x1, x2, rng )
  r8vec_print ( n, a, '  Vector A:' )
  a = r8vec_nint ( n, a )
  r8vec_print ( n, a, '  Rounded vector A:' )

  return

def r8vec_norm_affine ( n, v0, v1 ):

#*****************************************************************************80
#
## r8vec_norm_affine() returns the affine norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The affine vector L2 norm is defined as:
#
#      r8vec_norm_affine(V0,V1) 
#        = sqrt ( sum ( 1 <= I <= N ) ( V1(I) - V0(I) )^2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the vector dimnension.
#
#    real V0(N), the base vector.
#
#    real V1(N), the vector.
#
#  Output:
#
#    real VALUE, the affine L2 norm.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ): 
    value = value + ( v0[i] - v1[i] ) ** 2
  value =  np.sqrt ( value )

  return value

def r8vec_norm_affine_test ( rng ):

#*****************************************************************************80
#
## r8vec_norm_affine_test() tests r8vec_norm_affine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8vec_norm_affine_test():' )
  print ( '  r8vec_norm_affine() computes the L2 norm of' )
  print ( '  the difference of two R8VECs.' )

  x = rng.random ( size = n )
  y = rng.random ( size = n )
  z = np.zeros ( n )
  for i in range ( 0, n ):
    z[i] = x[i] - y[i]

  print ( '' )
  print ( '  r8vec_norm_affine(X,Y) = %g' % ( r8vec_norm_affine ( n, x, y ) ) )
  print ( '  r8vec_norm (X-Y):        %g' % ( r8vec_norm ( n, z ) ) )

  return

def r8vec_normal_01 ( n, rng ):

#*****************************************************************************80
#
## r8vec_normal_01() returns a unit pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = r8_normal_01 ( rng )

  return x

def r8vec_normal_01_test ( rng ):

#*****************************************************************************80
#
## r8vec_normal_01_test() tests r8vec_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8vec_normal_01_test():' )
  print ( '  r8vec_normal_01() returns a vector of Normal 01 values' )
  print ( '' )

  r = r8vec_normal_01 ( n, rng )

  r8vec_print ( n, r, '  Vector:' )

  return

def r8vec_normal_ab ( n, mu, sigma, rng ):

#*****************************************************************************80
#
## r8vec_normal_ab() returns a scaled pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real MU, the average value of the PDF.
#
#    real SIGMA, the standard deviation of the PDF.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    xi = r8_normal_01 ( rng )
    x[i] = mu + sigma * xi

  return x

def r8vec_normal_ab_test ( rng ):

#*****************************************************************************80
#
## r8vec_normal_ab_test() tests r8vec_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_normal_ab_test():' )
  print ( '  r8vec_normal_ab() returns a vector of Normal AB values' )

  n = 10
  mu = 15.0
  sigma = 0.25

  print ( '' )
  print ( '  Mean = %g' % ( mu ) )
  print ( '  Standard deviation = %g' % ( sigma ) )

  r = r8vec_normal_ab ( n, mu, sigma, rng )

  r8vec_print ( n, r, '  Vector:' )

  return

def r8vec_normalize_l1 ( n, a ):

#*****************************************************************************80
#
## r8vec_normalize_l1() normalizes an R8VEC to have unit sum.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be normalized.
#
#  Output:
#
#    real A(N), the entries of A should have unit sum.  However, 
#    if the input vector has zero sum, the routine halts.
#
  import numpy as np

  a_sum = np.sum ( np.abs ( a ) )

  if ( a_sum == 0.0 ):
    print ( '' )
    print ( 'r8vec_normalize_l1 - Fatal error!' )
    print ( '  The vector entries sum to 0.' )
    raise Exception ( 'r8vec_normalize_l1 - Fatal error!' )

  a = a / a_sum

  return a

def r8vec_normalize_l1_test ( rng ):

#*****************************************************************************80
#
## r8vec_normalize_l1_test() tests r8vec_normalize_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8vec_normalize_l1_test():' )
  print ( '  r8vec_normalize_l1() normalizes an R8VEC in the L1 norm.' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  a = r8_lo + ( r8_hi - r8_lo ) * rng.random ( size = n )
 
  r8vec_print ( n, a, '  Input vector:' )

  a = r8vec_normalize_l1 ( n, a )

  r8vec_print ( n, a, '  After calling r8vec_normalize_l1:' )

  return

def r8vec_norm_l0 ( n, a ):

#*****************************************************************************80
#
## r8vec_norm_l0() returns the l0 "norm" of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The l0 "norm" simply counts the number of nonzero entries in the vector.
#    It is not a true norm, but has some similarities to one.  It is useful
#    in the study of compressive sensing.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the value of the norm.
#
  value = 0.0
  for i in range ( 0, n ):
    if ( a[i] != 0.0 ):
      value = value + 1.0

  return value

def r8vec_norm_l0_test ( rng ):

#*****************************************************************************80
#
## r8vec_norm_l0_test() tests r8vec_norm_l0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_norm_l0_test():' )
  print ( '  r8vec_norm_l0() computes the L0 "norm" of an R8VEC.' )

  n = 10
  a_lo = - 2.0
  a_hi = + 2.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )
  a = r8vec_nint ( n, a )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_l0 ( n, a )

  print ( '' )
  print ( '  L0 norm = %g' % ( value ) )

  return

def r8vec_norm_l1 ( n, a ):

#*****************************************************************************80
#
## r8vec_norm_l1() returns the L1 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L1 norm is defined as:
#
#      value = sum ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), the vector whose L1 norm is desired.
#
#  Output:
#
#    real VALUE, the L1 norm of A.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + abs ( a[i] )

  return value

def r8vec_norm_l1_test ( rng ):

#*****************************************************************************80
#
## r8vec_norm_l1_test() tests r8vec_norm_l1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'r8vec_norm_l1_test():' )
  print ( '  r8vec_norm_l1() computes the L1 norm of an R8VEC.' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )
 
  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_l1 ( n, a )

  print ( '' )
  print ( '  L1 norm = %g' % ( value ) )

  return

def r8vec_norm_l2 ( n, a ):

#*****************************************************************************80
#
## r8vec_norm_l2() returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), the vector whose L2 norm is desired.
#
#  Output:
#
#    real VALUE, the L2 norm of A.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = np.sqrt ( value )

  return value

def r8vec_norm_l2_test ( rng ):

#*****************************************************************************80
#
## r8vec_norm_l2_test() tests r8vec_norm_l2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_norm_l2_test():' )
  print ( '  r8vec_norm_l2() computes the L2 norm of an R8VEC.' )

  n = 10
  a_lo = - n
  a_hi = + n
  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm_l2 ( n, a )

  print ( '' )
  print ( '  L2 norm = %g' % ( a_norm ) )

  return

def r8vec_norm_li ( n, a ):

#*****************************************************************************80
#
## r8vec_norm_li() returns the loo norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the value of the norm.
#
  value = 0.0
  for i in range ( 0, n ):
    if ( value < abs ( a[i] ) ):
      value = abs ( a[i] )

  return value

def r8vec_norm_li_test ( rng ):

#*****************************************************************************80
#
## r8vec_norm_li_test() tests r8vec_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_norm_li_test():' )
  print ( '  r8vec_norm_li() computes the Loo norm of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_li ( n, a )

  print ( '' )
  print ( '  Loo norm = %g' % ( value ) )

  return

def r8vec_norm ( n, a ):

#*****************************************************************************80
#
## r8vec_norm() returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), the vector whose L2 norm is desired.
#
#  Output:
#
#    real VALUE, the L2 norm of A.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = np.sqrt ( value )

  return value

def r8vec_norm_test ( rng ):

#*****************************************************************************80
#
## r8vec_norm_test() tests r8vec_norm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_norm_test():' )
  print ( '  r8vec_norm() computes the L2 norm of an R8VEC.' )

  n = 10
  a = rng.random ( size = n )
  r8vec_print ( n, a, '  Input vector:' )

  a_norm = r8vec_norm ( n, a )
  print ( '' )
  print ( '  L2 norm = %g' % ( a_norm ) )

  return

def r8vec_norm_rms ( a ):

#*****************************************************************************80
#
## r8vec_norm_rms() returns the RMS norm of an R8VEC.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = sqrt ( 1/N * sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N), the vector whose norm is desired.
#
#  Output:
#
#    real VALUE, the RMS norm of A.
#
  import numpy as np

  value = np.sqrt ( (a**2).mean() )

  return value

def r8vec_norm_rms_test ( ):

#*****************************************************************************80
#
## r8vec_norm_rms_test() tests r8vec_norm_rms().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r8vec_norm_rms_test():' )
  print ( '  r8vec_norm_rms() computes the RMS norm of an R8VEC.' )

  n = 9
  a = np.linspace ( -6.0, 10.0, n ) 
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm_rms ( a )

  print ( '' )
  print ( '  RMS norm = %g' % ( a_norm ) )

  return

def r8vec_permute_cyclic ( n, k, a ):

#*****************************************************************************80
#
## r8vec_permute_cyclic() performs a cyclic permutation of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    For 0 <= K < N, this function cyclically permutes the input vector
#    to have the form
#
#     ( A(K+1), A(K+2), ..., A(N), A(1), ..., A(K) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects.
#
#    integer K, the increment used.
#
#    real A(N), the array to be permuted.
#
#  Output:
#
#    real B(N), the permuted array.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    ipk = i4_wrap ( i + k, 0, n - 1 )
    b[i] = a[ipk];

  return b

def r8vec_permute_cyclic_test ( ):

#*****************************************************************************80
#
## r8vec_permute_cyclic_test() tests r8vec_permute_cyclic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_permute_cyclic_test():' )
  print ( '  r8vec_permute_cyclic() performa a cyclic permutation' )
  print ( '  of K positions on an R8VEC.' )

  k = 4
  print ( '' )
  print ( '  K = %d' % ( k ) )

  n = 10
  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  Original array X:' )

  x = r8vec_permute_cyclic ( n, k, x )

  r8vec_print ( n, x, '  Array after permutation:' )

  return

def r8vec_permute ( n, p, a ):

#*****************************************************************************80
#
## r8vec_permute() permutes an R8VEC in place.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    This routine permutes an array of real "objects", but the same
#    logic can be used to permute an array of objects of any arithmetic
#    type, or an array of objects.  The only temporary
#    storage required is enough to store a single object.  The number
#    of data movements made is N + the number of cycles of order 2 or more,
#    which is never more than N + N/2.
#
#  Example:
#
#    Input:
#
#      N = 5
#      P = (   1,   3,   4,   0,   2 )
#      A = ( 1.0, 2.0, 3.0, 4.0, 5.0 )
#
#    Output:
#
#      A    = ( 2.0, 4.0, 5.0, 1.0, 3.0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects.
#
#    integer P[N], the permutation.  P(I) = J means
#    that the I-th element of the output array should be the J-th
#    element of the input array.
#
#    real A[N], the array to be permuted.
#
#  Output:
#
#    real A[N], the permuted array.
#
  check = perm0_check ( n, p );

  if ( not check ):
    print ( '' )
    print ( 'r8vec_permute - Fatal error!' )
    print ( '  perm0_check rejects the permutation.' )
    raise Exception ( 'r8vec_permute - Fatal error!' )
#
#  In order for the sign negation trick to work, we need to assume that the
#  entries of P are strictly positive.  Presumably, the lowest number is 0.
#  So temporarily add 1 to each entry to force positivity.
#
  for i in range ( 0, n ):
    p[i] = p[i] + 1
#
#  Search for the next element of the permutation that has not been used.
#
  for istart in range ( 1, n + 1 ):
    if ( p[istart-1] < 0 ):
      continue
    elif ( p[istart-1] == istart ):
      p[istart-1] = - p[istart-1]
    else:
      a_temp = a[istart-1];
      iget = istart;
#
#  Copy the new value into the vacated entry.
#
      while ( True ):
        iput = iget
        iget = p[iget-1]

        p[iput-1] = - p[iput-1]

        if ( iget < 1 or n < iget ):
          print ( '' )
          print ( 'r8vec_permute - Fatal error!' )
          print ( '  Entry IPUT = %d has' % ( iput ) )
          print ( '  an illegal value IGET = %d.' % (iget ) )
          raise Exception ( 'r8vec_permute - Fatal error!' )

        if ( iget == istart ):
          a[iput-1] = a_temp
          break

        a[iput-1] = a[iget-1]
#
#  Restore the signs of the entries.
#
  for i in range ( 0, n ):
    p[i] = - p[i]
#
#  Restore the entries.
#
  for i in range ( 0, n ):
    p[i] = p[i] - 1

  return a

def r8vec_permute_test ( ):

#*****************************************************************************80
#
## r8vec_permute_test() tests r8vec_permute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8vec_permute_test():' )
  print ( '  r8vec_permute() permutes an R8VEC.' )

  x = np.array ( [ 1.1, 2.2, 3.3, 4.4, 5.5 ], dtype = float )
  p = np.array ( [ 1, 3, 4, 0, 2 ], dtype = int )

  r8vec_print ( n, x, '  Original array X[]:' )

  i4vec_print ( n, p, '  Permutation vector P[]:' )

  x = r8vec_permute ( n, p, x )

  r8vec_print ( n, x, '  Permuted array X[P[*]]:' )

  return

def r8vec_permute_uniform ( n, a, rng ):

#*****************************************************************************80
#
## r8vec_permute_uniform() randomly permutes an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects.
#
#    real A(N), the array to be permuted.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(N), the permuted array.
#
  p = perm0_uniform ( n, rng )

  a = r8vec_permute ( n, p, a )

  return a

def r8vec_permute_uniform_test ( rng ):

#*****************************************************************************80
#
## r8vec_permute_uniform_test() tests r8vec_permute_uniform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 12

  print ( '' )
  print ( 'r8vec_permute_uniform_test():' )
  print ( '  r8vec_permute_uniform() randomly reorders an R8VEC.' )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = 101 + i

  r8vec_print ( n, a, '  A, before rearrangement:' )

  a = r8vec_permute_uniform ( n, a, rng )

  r8vec_print ( n, a, '  A, after rearrangement:' )

  return

def r8vec_print_part ( n, a, i_lo, i_hi, title ):

#*****************************************************************************80
#
## r8vec_print_part() prints "part" of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8 values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines to print.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )

  for i in range ( max ( 0, i_lo ), min ( n, i_hi + 1 ) ):
    print ( '  %8d: %12g' % ( i, a[i] ) )

  return

def r8vec_print_part_test ( ):

#*****************************************************************************80
#
## r8vec_print_part_test() tests r8vec_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8vec_print_part_test():' )
  print ( '  r8vec_print_part() prints part of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  r8vec_print_part ( n, a, 10, 20, '  Lines 10:20 of the vector:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests r8vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_print_test():' )
  print ( '  Test r8vec_print(), which prints an R8VEC.' )
#
#  Use r8vec_print:
#
  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = float )
  label = '  Use r8vec_print():'
  r8vec_print ( n, v, label )
#
#  Use Python print() for data.
#
  print ( '' )
  print ( '  Use python print():' )
  print ( '' )
  print ( v )

  return

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## r8vec_print_some() prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec_print_some_test ( ):

#*****************************************************************************80
#
## r8vec_print_some_test() tests r8vec_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8vec_print_some_test():' )
  print ( '  r8vec_print_some() prints some of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  max_print = 10

  r8vec_print_some ( n, a, max_print, '  No more than 10 lines of this vector:' )

  return

def r8vec_product ( n, a ):

#*****************************************************************************80
#
## r8vec_product() computes the product of the entries of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the product of the entries.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * a[i]

  return value

def r8vec_product_test ( rng ):

#*****************************************************************************80
#
## r8vec_product_test() tests r8vec_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_product_test():' )
  print ( '  r8vec_product() computes the product of the entries in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_product ( n, a )

  print ( '' )
  print ( '  Product of entries = %g' % ( value ) )

  return

def r8vec_reverse ( n, a1 ):

#*****************************************************************************80
#
## r8vec_reverse() reverses the elements of an R8VEC.
#
#  Example:
#
#    Input:
#
#      N = 5, A = ( 11.0, 12.0, 13.0, 14.0, 15.0 ).
#
#    Output:
#
#      A = ( 15.0, 14.0, 13.0, 12.0, 11.0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    real A1(N), the array to be reversed.
#
#  Output:
#
#    real A2(N), the reversed array.
#
  import numpy as np

  a2 = np.zeros ( n )
  for i in range ( 0, n ):
    a2[i] = a1[n-1-i]

  return a2

def r8vec_reverse_test ( ):

#*****************************************************************************80
#
## r8vec_reverse_test() tests r8vec_reverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8vec_reverse_test():' )
  print ( '  r8vec_reverse() reverses an R8VEC.' )
 
  a1 = np.zeros ( n )
  for i in range ( 0, n ):
    a1[i] = float ( i + 1 )
 
  r8vec_print ( n, a1, '  Original array:' )

  a2 = r8vec_reverse ( n, a1 )

  r8vec_print ( n, a2, '  Reversed array:' )

  return

def r8vec_rotate ( n, a, m ):

#*****************************************************************************80
#
## r8vec_rotate() "rotates" the entries of an R8VEC in place.
#
#  Discussion:
#
#    This routine rotates an array of real "objects", but the same
#    logic can be used to permute an array of objects of any arithmetic
#    type, or an array of objects.  The only temporary
#    storage required is enough to store a single object.  The number
#    of data movements made is N + the number of cycles of order 2 or more,
#    which is never more than N + N/2.
#
#  Example:
#
#    Input:
#
#      N = 5, M = 2
#      A    = ( 1.0, 2.0, 3.0, 4.0, 5.0 )
#
#    Output:
#
#      A    = ( 4.0, 5.0, 1.0, 2.0, 3.0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects.
#
#    integer M, the number of positions to the right that
#    each element should be moved.  Elements that shift pass position
#    N "wrap around" to the beginning of the array.
#
#    real A(N), the array to be rotated.
#
#  Output:
#
#    real A(N), the rotated array.
#

#
#  Force M to be positive, between 0 and N-1.
#
  m = i4_modp ( m, n )

  if ( m == 0 ):
    return a

  istart = 0
  nset = 0

  while ( True ):

    istart = istart + 1

    if ( n < istart ):
      break

    temp = a[istart-1]
    iget = istart
#
#  Copy the new value into the vacated entry.
#
    while ( True ):

      iput = iget

      iget = iget - m
      if ( iget < 1 ):
        iget = iget + n

      if ( iget == istart ):
        break

      a[iput-1] = a[iget-1]
      nset = nset + 1

    a[iput-1] = temp
    nset = nset + 1

    if ( n <= nset ):
      break

  return a

def r8vec_rotate_test ( ):

#*****************************************************************************80
#
## r8vec_rotate_test() tests r8vec_rotate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  a = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  m = 2

  print ( '' )
  print ( 'r8vec_rotate_test():' )
  print ( '  r8vec_rotate() rotates an R8VEC in place.' )
  print ( '' )
  print ( '  Rotate entries %d places to the right' % ( m ) )

  r8vec_print ( n, a, '  Original array:' )

  a = r8vec_rotate ( n, a, m )

  r8vec_print ( n, a, '  Rotated array:' )

  return

def r8vec_rsquared_adjusted ( n, y_data, y_model, degree ):

#*****************************************************************************80
#
## r8vec_rsquared_adjusted() computes the adjusted R^2 goodness of fit measurement.
#
#  Discussion:
#
#    We suppose a set of N data values Y_DATA are known, and that a
#    formula or model has generated a corresponding set of Y_modEL values.
#
#    R^2 measures the extent to which the variation in Y_DATA is captured
#    by the model data Y_modEL.  
#
#    The adjusted value of R^2 accounts for the use of a polynomial model
#    of degree higher than 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values.
#
#    real Y_DATA(N), Y_modEL(N), the data and model values.
#
#    integer DEGREE, the polynomial degree of the model.
#
#  Output:
#
#    real VALUE, the adjusted R^2 value.
#
  import numpy as np

  y_average = np.sum ( y_data[0:n] ) / n

  top = np.sum ( ( y_data[0:n] - y_model[0:n] ) ** 2 )
  bot = np.sum ( ( y_data[0:n] - y_average ) ** 2 )

  value = 1.0 - ( top / bot ) * float ( n - 1 ) / float ( n - degree - 1 )
 
  return value

def r8vec_rsquared_adjusted_test ( ):

#*****************************************************************************80
#
## r8vec_rsquared_adjusted_test() tests r8vec_rsquared_adjusted().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_rsquared_adjusted_test():' )
  print ( '  r8vec_rsquared_adjusted() computes the adjusted R^2 goodness-of-fit statistic.' )

  n = 11

  y_model = np.array ( [ \
     0.00,  9.00, 16.00, 21.00, 24.00, \
    25.00, 24.00, 21.00, 16.00,  9.00,  \
     0.00 ] )
  y_data = np.array ( [ \
     0.00,  9.58, 16.76, 21.52, 24.38, \
    24.97, 22.90, 20.45, 12.40,  7.65, \
    -3.82 ] )

  r8vec2_print ( y_data, y_model, "  Data and model:" )

  rsquared = r8vec_rsquared_adjusted ( n, y_data, y_model, degree )
  print ( '' )
  print ( '  Computed R^2, adjusted for degree = %d, is %g' % ( degree, rsquared ) )

  return

def r8vec_rsquared ( n, y_data, y_model ):

#*****************************************************************************80
#
## r8vec_rsquared() computes the R^2 goodness of fit measurement.
#
#  Discussion:
#
#    We suppose a set of N data values Y_DATA are known, and that a
#    formula or model has generated a corresponding set of Y_modEL values.
#
#    R^2 measures the extent to which the variation in Y_DATA is captured
#    by the model data Y_modEL.  If the model is linear, then a value
#    of R^2=1 is optimal, and R^2=0 is the worst possible.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values.
#
#    real Y_DATA(N), Y_modEL(N), the data and model values.
#
#  Output:
#
#    real VALUE, the R^2 value.
#
  import numpy as np

  y_average = np.sum ( y_data[0:n] ) / n

  top = np.sum ( ( y_data[0:n] - y_model[0:n] ) ** 2 )
  bot = np.sum ( ( y_data[0:n] - y_average ) ** 2 )

  value = 1.0 - top / bot

  return value

def r8vec_rsquared_test ( ):

#*****************************************************************************80
#
## r8vec_rsquared_test() tests r8vec_rsquared().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 January 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_rsquared_test():' )
  print ( '  r8vec_rsquared() computes the R^2 goodness-of-fit statistic.' )

  n = 11

  y_model = np.array ( [ \
     0.00,  9.00, 16.00, 21.00, 24.00, \
    25.00, 24.00, 21.00, 16.00,  9.00,  \
     0.00 ] )
  y_data = np.array ( [ \
     0.00,  9.58, 16.76, 21.52, 24.38, \
    24.97, 22.90, 20.45, 12.40,  7.65, \
    -3.82 ] )

  r8vec2_print ( y_data, y_model, "  Data and model:" )

  rsquared = r8vec_rsquared ( n, y_data, y_model )
  print ( '' )
  print ( '  Computed R^2 is %g' % ( rsquared ) )

  return

def r8vec_scale_01 ( n, x ):

#*****************************************************************************80
#
## r8vec_scale_01() scales an R8VEC to [0,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real X(N), the vector to be scaled.
#
#  Output:
#
#    real XS(N), the scaled vector.
#
  import numpy as np

  xs = x.copy ( )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  if ( 0.0 < xmax - xmin ):
    xs = ( xs - xmin ) / ( xmax - xmin )
  else:
    xs = 0.5

  return xs

def r8vec_scale_01_test ( rng ):

#*****************************************************************************80
#
## r8vec_scale_01_test() tests r8vec_scale_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_scale_01_test():' )
  print ( '  r8vec_scale_01() shifts and scales an R8VEC so that' )
  print ( '  it has min 0 and max 1' )

  n = 10
  a = -5.0
  b = 15.0

  x = r8vec_uniform_ab ( n, a, b, rng )
 
  r8vec_print ( n, x, '  Vector X:' )
  mu = np.mean ( x )
  sigma = np.std ( x )
  xmin = np.ndarray.min ( x )
  xmax = np.ndarray.max ( x )
  print ( '' )
  print ( '  mean(X) = %g' % ( mu ) )
  print ( '  std(X)  = %g' % ( sigma ) )
  print ( '  max(X)  = %g' % ( xmax ) )
  print ( '  min(X)  = %g' % ( xmin ) )

  xs = r8vec_scale_01 ( n, x )

  r8vec_print ( n, xs, '  Vector XS:' )
  mu = np.mean ( xs )
  sigma = np.std ( xs )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  print ( '' )
  print ( '  mean(XS) = %g' % ( mu ) )
  print ( '  std(XS)  = %g' % ( sigma ) )
  print ( '  max(XS)  = %g' % ( xmax ) )
  print ( '  min(XS)  = %g' % ( xmin ) )

  return

def r8vec_scale_ab ( n, x, a, b ):

#*****************************************************************************80
#
## r8vec_scale_ab() scales an R8VEC to [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real X(N), the vector to be scaled.
#
#    real A, B, the new limits.
#
#  Output:
#
#    real XS(N), the scaled vector.
#
  import numpy as np

  xs = x.copy ( )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  if ( 0.0 < xmax - xmin ):
    xs = a + ( b - a ) * ( xs - xmin ) / ( xmax - xmin )
  else:
    xs = ( a + b ) / 2.0

  return xs

def r8vec_scale_ab_test ( rng ):

#*****************************************************************************80
#
## r8vec_scale_ab_test() tests r8vec_scale_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_scale_ab_test():' )
  print ( '  r8vec_scale_ab() shifts and scales an R8VEC so that' )
  print ( '  it has min A and max B' )

  n = 10
  a = -5.0
  b = 15.0

  x = r8vec_uniform_ab ( n, a, b, rng )
 
  r8vec_print ( n, x, '  Vector X:' )
  mu = np.mean ( x )
  sigma = np.std ( x )
  xmin = np.ndarray.min ( x )
  xmax = np.ndarray.max ( x )
  print ( '' )
  print ( '  mean(X) = %g' % ( mu ) )
  print ( '  std(X)  = %g' % ( sigma ) )
  print ( '  max(X)  = %g' % ( xmax ) )
  print ( '  min(X)  = %g' % ( xmin ) )

  a = -1.0
  b = +1.0
  print ( '' )
  print ( '  Rescale to [%g,%g]' % ( a, b ) )

  xs = r8vec_scale_ab ( n, x, a, b )

  r8vec_print ( n, xs, '  Vector XS:' )
  mu = np.mean ( xs )
  sigma = np.std ( xs )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  print ( '' )
  print ( '  mean(XS) = %g' % ( mu ) )
  print ( '  std(XS)  = %g' % ( sigma ) )
  print ( '  max(XS)  = %g' % ( xmax ) )
  print ( '  min(XS)  = %g' % ( xmin ) )

  return

def r8vec_shift_circular ( n, x, k ):

#*****************************************************************************80
#
## r8vec_shift_circular() performs a circular shift on an R8VEC.
#
#  Discussion:
#
#    The numpy function np.roll(x,k) should be preferred.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vector entries.
#
#    real X(N), the vector to be shifted.
#
#    integer K, the amount by which each entry is to
#    be shifted.  K should be nonnegative.
#
#  Output:
#
#    real X(N), the shifted vector.
#
  import numpy as np

  x = np.roll ( x, k )

  return x

def r8vec_shift_circular_test ( ):

#*****************************************************************************80
#
## r8vec_shift_circular_test() tests r8vec_shift_circular().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8vec_shift_circular_test():' )
  print ( '  r8vec_shift_circular() circularly shifts a vector by K positions.' )

  n = 10
  a = r8vec_indicator1 ( n )
  r8vec_print ( n, a, '  The vector:' )

  k = 3
  print ( '' )
  print ( '  Using a circular shift of K = ', k )

  a2 = r8vec_shift_circular ( n, a, k )
  r8vec_print ( n, a2, '  Shifted vector:' )

  return

def r8vec_sign3_running ( n, v ):

#*****************************************************************************80
#
## r8vec_sign3_running() computes the running threeway sign of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items.
#
#    real V(N), the data.
#
#  Output:
#
#    real S(N+1), the running threeway sign.  S(I) is:
#    -1 if the sum of the first I-1 values in V is negative
#     0, if zero
#    +1, if positive.
#
  import numpy as np

  s = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    s[i] = s[i-1] + v[i-1]

  for i in range ( 0, n + 1 ):
    if ( s[i] < 0.0 ):
      s[i] = -1.0
    elif ( s[i] == 0.0 ):
      s[i] = 0.0
    else:
      s[i] = +1.0

  return s

def r8vec_sign3_running_test ( rng ):

#*****************************************************************************80
#
## r8vec_sign3_running_test() tests r8vec_sign3_running().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_sign3_running_test():' )
  print ( '  r8vec_sign3_running() returns the running sign3 of an R8VEC.' )

  n = 10
  a = -5.0
  b = +10.0

  r = r8vec_uniform_ab ( n, a, b, rng )

  r8vec_print ( n, r, '  Random R8VEC:' )

  s = r8vec_sign3_running ( n, r )

  r8vec_print ( n + 1, s, '  Running sign3:' )

  return

def r8vec_smooth ( n, x, s ):

#*****************************************************************************80
#
## r8vec_smooth() smooths an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    Except for the beginning and ending entries, the vector values
#    are replaced by averages of 2*S+1 neighbors.
#
#  Example:
#
#    S = 2
#
#    Z(1)   =                     X(1)
#    Z(2)   = (          X(1)   + X(2)   + X(3) ) / 3
#    Z(3)   = ( X(1)   + X(2)   + X(3)   + X(4)   + X(5) ) / 5
#    Z(4)   = ( X(2)   + X(3)   + X(4)   + X(5)   + X(6) ) / 5
#    ...
#    Z(N-2) = ( X(N-4) + X(N-3) + X(N-2) + X(N-1) + X(N) ) / 5
#    Z(N-1) =          ( X(N-2) + X(N-1) + X(N) ) / 3
#    Z(N) =                       X(N)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of X.
#
#    real X(N), the vector to be smoothed.
#
#  Output:
#
#    real Z(N), the smoothed vector.
#
  import numpy as np

  z = np.zeros ( n )

  for j in range ( 1, s + 1 ):
    z[j-1] = np.sum ( x[0:2*j-1] ) / ( 2 * j - 1 )

  for j in range ( s + 1, n - s + 1 ):
    z[j-1] = np.sum ( x[j-s-1:j+s] ) / ( 2 * s + 1 )

  for j in range ( s, 0, -1 ):
    z[n-j] = np.sum ( x[n-(2*j-1):n] ) / ( 2 * j - 1 )

  return z

def r8vec_smooth_test ( ):

#*****************************************************************************80
#
## r8vec_smooth_test() tests r8vec_smooth().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_smooth_test():' )
  print ( '  r8vec_smooth smooths an R8VEC.' )

  n = 10
  x = np.linspace ( 1, n, n )
  r8vec_print ( n, x, '  The vector X:' )
  s = 2
  z = r8vec_smooth ( n, x, s )
  label = ( '  Vector X using smoothing S = %d' % ( s ) )
  r8vec_print ( n, z, label )

  n = 10
  x = np.linspace ( 1, n, n )
  x = x ** 2
  r8vec_print ( n, x, '  The vector X:' )
  s = 1
  z = r8vec_smooth ( n, x, s )
  label = ( '  Vector X using smoothing S = %d' % ( s ) )
  r8vec_print ( n, z, label )

  return

def r8vec_softmax ( n, x ):

#*****************************************************************************80
#
## r8vec_softmax() evaluates the SOFTMAX function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the vector.
#
#    real X(N), the vector.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  index = np.argmax ( x )
  bottom = np.sum ( np.exp ( x[0:n] - x[index] ) )
  value = np.exp ( x[0:n] - x[index] ) / bottom

  return value

def r8vec_softmax_test ( rng ):

#*****************************************************************************80
#
## r8vec_softmax_test() tests r8vec_softmax().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#

  print ( '' )
  print ( 'r8vec_softmax_test():' )
  print ( '  r8vec_softmax() evaluates the softmax function.' )

  n = 10

  x = r8vec_normal_ab ( n, -3.0, +3.0, rng )

  sx = r8vec_softmax ( n, x )

  r8vec2_print ( x, sx, '  X, Softmax(X):' )

  return

def r8vec_sorted_nearest ( n, a, value ):

#*****************************************************************************80
#
## r8vec_sorted_nearest() returns the nearest element in a sorted R8VEC.
#
#  Discussion:
#
#    A correction was made in the ascending case, where previous if the
#    "mid" value was exactly encountered, no index value was returned.
#    30 June 2025.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    real A(N), a sorted vector.
#
#    real VALUE, the value whose nearest vector entry is sought.
#
#  Output:
#
#    integer INDEX, the index of the nearest
#    entry in the vector.
#
  import numpy as np

  if ( n < 1 ):
    index = -1
    return index

  if ( n == 1 ):
    index = 0
    return index

  if ( a[0] < a[n-1] ):

    if ( value < a[0] ):
      index = 0
      return index
    elif ( a[n-1] < value ):
      index = n - 1
      return index
#
#  Seek an interval containing the value.
#
    lo = 0
    hi = n - 1

    while ( lo < hi - 1 ):

      mid = int ( np.floor ( ( lo + hi ) / 2 ) )

      if ( value == a[mid] ):
        index = mid
        return index
      elif ( value < a[mid] ):
        hi = mid
      else:
        lo = mid
#
#  Take the nearest.
#
    if ( abs ( value - a[lo] ) < abs ( value - a[hi] ) ):
      index = lo
    else:
      index = hi

    return index
#
#  A descending sorted vector A.
#
  else:

    if ( value < a[n-1] ):
      index = n - 1
      return index
    elif ( a[0] < value ):
      index = 0
      return index
#
#  Seek an interval containing the value.
#
    lo = n - 1
    hi = 0

    while ( lo < hi - 1 ):

      mid = np.floor ( ( lo + hi ) / 2 )

      if ( value == a[mid] ):
        index = mid
        return index
      elif ( value < a[mid] ):
        hi = mid
      else:
        lo = mid
#
#  Take the nearest.
#
    if ( abs ( value - a[lo] ) < abs ( value - a[hi] ) ):
      index = lo
    else:
      index = hi

    return index

  return index

def r8vec_sorted_nearest_test ( rng ):

#*****************************************************************************80
#
## r8vec_sorted_nearest_test() tests r8vec_sorted_nearest().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 11

  print ( '' )
  print ( 'r8vec_sorted_nearest_test():' )
  print ( '  r8vec_sorted_nearest() finds, for a given value R,' )
  print ( '  the nearest element in a sorted R8VEC.' )

  s = np.linspace ( 0.0, 10.0, n );
  r8vec_print ( n, s, '  Sorted R8VEC:' )

  print ( '' )
  for i in range ( 0, 15 ):
    r = r8_uniform_ab ( -1.0, 11.0, rng )
    index = r8vec_sorted_nearest ( n, s, r )
    print ( '  R = %g is nearest S[%d] = %g' % ( r, index, s[index] ) )

  return

def r8vec_standardize ( n, x ):

#*****************************************************************************80
#
## r8vec_standardize() standarizes an R8VEC.
#
#  Discussion:
#
#    The output vector will have 0 mean and unit standard deviation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real X(N), the vector to be standardized.
#
#  Output:
#
#    real XS(N), the standardized vector.
#
  import numpy as np

  mu = np.mean ( x )
  sigma = np.std ( x, ddof = 1 )
  
  if ( sigma != 0.0 ):
    xs = ( x - mu ) / sigma
  else:
    xs = np.zeros ( n )

  return xs

def r8vec_standardize_test ( rng ):

#*****************************************************************************80
#
## r8vec_standardize_test() tests r8vec_standardize().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_standardize_test():' )
  print ( '  r8vec_standardize() shifts and scales an R8VEC so that' )
  print ( '  it has zero mean and unit standard deviation.' )

  n = 10
  a = -5.0
  b = 15.0

  x = r8vec_uniform_ab ( n, a, b, rng )
 
  r8vec_print ( n, x, '  Vector X:' )
  mu = np.mean ( x )
  sigma = np.std ( x, ddof = 1 )
  xmax = np.ndarray.max ( x )
  xmin = np.ndarray.min ( x )
  print ( '' )
  print ( '  mean(X) = %g' % ( mu ) )
  print ( '  std(X)  = %g' % ( sigma ) )
  print ( '  max(X)  = %g' % ( xmax ) )
  print ( '  min(X)  = %g' % ( xmin ) )

  xs = r8vec_standardize ( n, x )

  r8vec_print ( n, xs, '  Vector XS:' )
  mu = np.mean ( xs )
  sigma = np.std ( xs, ddof = 1 )
  xmax = np.ndarray.max ( xs )
  xmin = np.ndarray.min ( xs )
  print ( '' )
  print ( '  mean(XS) = %g' % ( mu ) )
  print ( '  std(XS)  = %g' % ( sigma ) )
  print ( '  max(XS)  = %g' % ( xmax ) )
  print ( '  min(XS)  = %g' % ( xmin ) )

  return

def r8vec_std ( n, a ):

#*****************************************************************************80
#
## r8vec_std() returns the standard deviation of an R8VEC.
#
#  Discussion:
#
#    The standard deviation of a vector X of length N is defined as
#
#      mean ( X(1:n) ) = sum ( X(1:n) ) / n
#
#      std ( X(1:n) ) = sqrt ( sum ( ( X(1:n) - mean )^2 ) / n )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the standard deviation of the vector.
#
  import numpy as np

  if ( n < 2 ):

    value = 0.0

  else:

    mean = np.sum ( a[0:n] ) / n

    std = np.sum ( ( a[0:n] - mean ) ** 2 )

    value = np.sqrt ( std / n )

  return value

def r8vec_std_test ( rng ):

#*****************************************************************************80
#
## r8vec_std_test() tests r8vec_std().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_std_test()' )
  print ( '  r8vec_std() computes the standard deviation of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_std ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )

  return

def r8vec_std_sample ( n, a ):

#*****************************************************************************80
#
## r8vec_std_sample() returns the sample standard deviation of an R8VEC.
#
#  Discussion:
#
#    The standard deviation of a vector X of length N is defined as
#
#      mean ( X(1:n) ) = sum ( X(1:n) ) / n
#
#      std ( X(1:n) ) = sqrt ( sum ( ( X(1:n) - mean )^2 ) / ( n - 1 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the sample standard deviation of the vector.
#
  import numpy as np

  if ( n < 2 ):

    value = 0.0

  else:

    mean = np.sum ( a[0:n] ) / n

    std = np.sum ( ( a[0:n] - mean ) ** 2 )

    value = np.sqrt ( std / ( n - 1 ) )

  return value

def r8vec_std_sample_test ( rng ):

#*****************************************************************************80
#
## r8vec_std_sample_test() tests r8vec_std_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_std_sample_test():' )
  print ( '  r8vec_std_sample() computes the sample standard deviation of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_std_sample ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )

  return

def r8vec_std_sample_update ( nm1, mean_nm1, std_nm1, xn ):

#*****************************************************************************80
#
## r8vec_std_sample_update() updates sample standard deviation with one new value.
#
#  Discussion:
#
#   On first call:
#     nm1 = 0
#     mean_nm1 = 0.0
#     std_nm1 = 0.0
#     xn = first value to be handled.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Accurately computing running variance,
#    https://www.johndcook.com/blog/standard_deviation/
#
#  Input:
#
#    integer NM1, the number of entries in the old vector.
#
#    real MEAN_NM1, the mean of the old vector.
#
#    real STD_NM1, the sample standard deviation of the old vector.
#
#    real XN, the new N-th entry of the vector.
#
#  Output:
#
#    integer N, the number of entries in the new vector.
#
#    real MEAN_N, the mean of the new vector.
#
#    real STD_N, the sample standard deviation of the new vector.
#
  import numpy as np

  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
    std_n = 0.0
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n
    std_n = np.sqrt ( ( std_nm1 * std_nm1 * ( nm1 - 1 ) \
      + ( xn - mean_nm1 ) * ( xn - mean_n ) ) / ( n - 1 ) )

  return n, mean_n, std_n

def r8vec_std_sample_update_test ( rng ):

#*****************************************************************************80
#
## r8vec_std_sample_update_test() tests r8vec_std_sample_update().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_std_sample_update_test():' )
  print ( '  r8vec_std_sample_update() updates sample standard deviation' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R                STD          STD_update' )
  print ( '' )

  n_max = 10

  a = np.zeros ( n_max )
  mean_n = 0.0
  std_n = 0.0

  for i in range ( 1, n_max ):

    r = rng.random ( )
    a[i-1] = r
    std = r8vec_std_sample ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    std_nm1 = std_n
    n, mean_n, std_n = r8vec_std_sample_update ( nm1, mean_nm1, std_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, std, std_n ) )

  return

def r8vec_std_update ( nm1, mean_nm1, std_nm1, xn ):

#*****************************************************************************80
#
## r8vec_std_update() updates the standard deviation with one new value.
#
#  Discussion:
#
#   On first call:
#     nm1 = 0
#     mean_nm1 = 0.0
#     std_nm1 = 0.0
#     xn = first value to be handled.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Accurately computing running variance,
#    https://www.johndcook.com/blog/standard_deviation/
#
#  Input:
#
#    integer NM1, the number of entries in the old vector.
#
#    real MEAN_NM1, the mean of the old vector.
#
#    real STD_NM1, the standard deviation of the old vector.
#
#    real XN, the new N-th entry of the vector.
#
#  Output:
#
#    integer N, the number of entries in the new vector.
#
#    real MEAN_N, the mean of the new vector.
#
#    real STD_N, the standard deviation of the new vector.
#
  import numpy as np

  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
    std_n = 0.0
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n
    std_n = np.sqrt ( ( std_nm1 * std_nm1 * nm1 \
      + ( xn - mean_nm1 ) * ( xn - mean_n ) ) / n )

  return n, mean_n, std_n

def r8vec_std_update_test ( rng ):

#*****************************************************************************80
#
## r8vec_std_update_test() tests r8vec_std_update().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_std_update_test():' )
  print ( '  r8vec_std_update() updates the standard deviation of a vector' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R                STD          STD_update' )
  print ( '' )

  n_max = 10

  a = np.zeros ( n_max )
  mean_n = 0.0
  std_n = 0.0

  for i in range ( 1, n_max ):

    r = rng.random ( )
    a[i-1] = r
    std = r8vec_std ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    std_nm1 = std_n
    n, mean_n, std_n = r8vec_std_update ( nm1, mean_nm1, std_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, std, std_n ) )

  return

def r8vec_std_updates ( n1, mean1, std1, n2,  mean2, std2 ):

#*****************************************************************************80
#
## r8vec_std_updates() computes the standard deviation of two combined vectors.
#
#  Discussion:
#
#    Vectors 1 and 2 have size, mean, and standard deviations computed.
#    This function computes the corresponding size, mean and standard deviation
#    for the vector formed by combining the two vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, the number of entries in vector 1.
#
#    real MEAN1, the mean of vector 1.
#
#    real STD1, the standard deviation of vector 1.
#
#    integer N2, the number of entries in vector 2.
#
#    real MEAN2, the mean of vector 2.
#
#    real STD2, the standard deviation of vector 2.
#
#  Output:
#
#    integer N12, the number of entries in the combined vector.
#
#    real MEAN12, the mean of the combined vector.
#
#    real STD12, the standard deviation of the combined vector.
#
  import numpy as np

  n12 = n1 + n2

  mean12 = ( n1 * mean1 + n2 * mean2 ) / ( n1 + n2 )

  ta = ( ( n1 - 1 ) * std1**2 + ( n2 - 1 ) * std2**2 ) / ( n1 + n2 - 1 )
  tb = n1 * n2 * ( mean1 - mean2 )**2 / ( n1 + n2 ) / ( n1 + n2 - 1 )
  v12 = ta + tb
  std12 = np.sqrt ( v12 )

  return n12, mean12, std12

def r8vec_std_updates_test ( rng ):

#*****************************************************************************80
#
## r8vec_std_updates_test() tests r8vec_std_updates().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_std_updates_test():' )
  print ( '  r8vec_std_updates() computes the standard deviation of' )
  print ( '    V12 = V1 + V2' )
  print ( '  where V1 and V2 are vectors whose length, mean and' )
  print ( '  standard deviation are given.' )

  n1 = 5
  v1 = rng.standard_normal ( size = n1 )
# v1 = np.array ( [ 1, 2, 3, 4, 5 ] )
  mean1 = np.mean ( v1 )
  std1 = np.std ( v1, ddof = 1 )

  n2 = 7
  v2 = rng.standard_normal ( size = n2 )
# v2 = np.array ( [ 6, 7, 8, 9, 10, 11, 12 ] )
  mean2 = np.mean ( v2 )
  std2 = np.std ( v2, ddof = 1 )

  n12, mean12, std12 = r8vec_std_updates ( n1, mean1, std1, n2, mean2, std2 )

  print ( '' )
  print (  n1, mean1, std1 )
  print (  n2, mean2, std2 )
  print (  n12, mean12, std12 )

  v12 = np.concatenate ( ( v1, v2 ) )
  n12 = n1 + n2
  mean12 = np.mean ( v12 )
  std12 = np.std ( v12, ddof = 1 )
  print ( '' )
  print ( '  Recompute directly from V12:' )
  print (  n12, mean12, std12 )

  return

def r8vec_step ( x0, n, x ):

#*****************************************************************************80
#
## r8vec_step() evaluates a unit step function.
#
#  Discussion:
#
#    F(X) = 0 if X < X0
#           1 if     X0 <= X
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X0, the location of the jump.
#
#    integer N, the number of argument values.
#
#  Output:
#
#    real X(N), the arguments.
#
#    real FX(N), the function values.
#
  import numpy

  fx = numpy.zeros ( n );

  for i in range ( 0, n ):
    if ( x[i] < x0 ):
      fx[i] = 0.0
    else:
      fx[i] = 1.0

  return fx

def r8vec_step_test ( ):

#*****************************************************************************80
#
## r8vec_step_test() tests r8vec_step().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_step_test():' )
  print ( '  r8vec_step() evaluates a step function.' )
  print ( '' )
  print ( '        X0         X           STEP(X0,X)' )
  print ( '' )

  x0 = 0.31
  n = 21

  x = np.linspace ( 0.0, 1.0, n )
  v = r8vec_step ( x0, n, x )

  r8vec2_print ( x, v, '  Step function with X0 = 0.31' )

  return

def r8vec_sum ( n, a ):

#*****************************************************************************80
#
## r8vec_sum() sums the entries of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the sum of the entries.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i]

  return value

def r8vec_sum_test ( rng ):

#*****************************************************************************80
#
## r8vec_sum_test() tests r8vec_sum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_sum_test():' )
  print ( '  r8vec_sum() sums the entries in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = r8vec_uniform_ab ( n, a_lo, a_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_sum ( n, a )

  print ( '' )
  print ( '  Sum of entries = %g' % ( value ) )

  return

def r8vec_sum_running ( n, v ):

#*****************************************************************************80
#
## r8vec_sum_running() computes the running sum of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items.
#
#    real V(N), the data.
#
#  Output:
#
#    real S(N+1), the running sum.  S(I) is the sum
#    of the first I-1 values in V.
#
  import numpy as np

  s = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    s[i] = s[i-1] + v[i-1]

  return s

def r8vec_sum_running_test ( rng ):

#*****************************************************************************80
#
## r8vec_sum_running_test() tests r8vec_sum_running().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_sum_running_test():' )
  print ( '  r8vec_sum_running() returns the running sums of an R8VEC.' )

  n = 10
  a = -5.0
  b = +10.0

  r = r8vec_uniform_ab ( n, a, b, rng )

  r8vec_print ( n, r, '  Random R8VEC:' )

  s = r8vec_sum_running ( n, r )

  r8vec_print ( n + 1, s, '  Running sums:' )

  return

def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_transpose_print() prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## r8vec_transpose_print_test() tests r8vec_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 11

  print ( '' )
  print ( 'r8vec_transpose_print_test():' )
  print ( '  r8vec_transpose_print() prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x = np.array ( [ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 ] )

  r8vec_transpose_print ( n, x, '  The vector X:' )

  return

def r8vec_uniform_01 ( n, rng ):

#*****************************************************************************80
#
## r8vec_uniform_01() returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  x = rng.random ( size = n )

  return x

def r8vec_uniform_01_test ( rng ):

#*****************************************************************************80
#
## r8vec_uniform_01_test() tests r8vec_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r8vec_uniform_01_test():' )
  print ( '  r8vec_uniform_01() computes a random R8VEC.' )
  print ( '' )

  v = r8vec_uniform_01 ( n, rng )

  r8vec_print ( n, v, '  Random R8VEC:' )

  return

def r8vec_uniform_ab ( n, a, b, rng ):

#*****************************************************************************80
#
## r8vec_uniform_ab() returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the range of the pseudorandom values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  x = a + ( b - a ) * rng.random ( size = n )

  return x

def r8vec_uniform_ab_test ( rng ):

#*****************************************************************************80
#
## r8vec_uniform_ab_test() tests r8vec_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 10
  a = -1.0
  b = +5.0

  print ( '' )
  print ( 'r8vec_uniform_ab_test():' )
  print ( '  r8vec_uniform_ab() computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
 
  v = r8vec_uniform_ab ( n, a, b, rng )

  r8vec_print ( n, v, '  Random R8VEC:' )

  return

def r8vec_uniform_abvec ( n, a, b, rng ):

#*****************************************************************************80
#
## r8vec_uniform_ab() returns a random vector with a range for each entry.
#
#  Discussion:
#
#    Dimension I ranges from A(I) to B(I).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), B(N), the range of the pseudorandom values.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  import numpy as np

  x = rng.random ( size = n )
  x = a + ( b - a ) * x

  return x

def r8vec_uniform_abvec_test ( rng ):

#*****************************************************************************80
#
## r8vec_uniform_abvec_test() tests r8vec_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 5
  a = np.array ( (  0.0, 0.20, 10.0, 52.0, -1.0 ) )
  b = np.array ( ( +1.0, 0.25, 20.0, 54.0, +1.0 ) )
 
  print ( '' )
  print ( 'r8vec_uniform_abvec_test():' )
  print ( '  r8vec_uniform_abvec() computes a random R8VEC.' )

  v = r8vec_uniform_abvec ( n, a, b, rng )

  print ( '' )
  print ( '   I         A         X         B' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10g  %10g  %10g' % ( i, a[i], v[i], b[i] ) )
  print ( '' )

  return

def r8vec_uniform_unit ( m, rng ):

#*****************************************************************************80
#
## r8vec_uniform_unit() generates a random unit vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the space.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real W(M), a random direction vector,
#    with unit norm.
#

#
#  Get values from a standard normal distribution.
#
  w = r8vec_normal_01 ( m, rng )
#
#  Compute the length of the vector.
#
  norm = r8vec_norm ( m, w )
#
#  Normalize the vector.
#
  for i in range ( 0, m ):
    w[i] = w[i] / norm

  return w

def r8vec_uniform_unit_test ( rng ):

#*****************************************************************************80
#
## r8vec_uniform_unit_test() tests r8vec_uniform_unit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5

  print ( '' )
  print ( 'r8vec_uniform_unit_test():' )
  print ( '  r8vec_uniform_unit() returns a random R8VEC' )
  print ( '  on the surface of the unit M sphere.' )
  print ( '' )

  for j in range ( 0, 5 ):

    x = r8vec_uniform_unit ( m, rng )

    r8vec_print ( m, x, '  Vector:' )

  return

def r8vec_variance_circular ( n, x ):

#*****************************************************************************80
#
## r8vec_variance_circular() returns the circular variance of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real X(N), the vector whose variance is desired.
#
#  Output:
#
#    real VALUE, the circular variance of the vector entries.
#
  import numpy as np

  mean = 0.0
  for i in range ( 0, n ):
    mean = mean + x[i]
  mean = mean / float ( n )

  c = 0.0
  s = 0.0
  for i in range ( 0, n ):
    c = c + np.cos ( x[i] - mean )
    s = s + np.sin ( x[i] - mean )

  value = s * s + c * c

  value = np.sqrt ( value ) / float ( n )

  value = 1.0 - value

  return value

def r8vec_variance_circular_test ( rng ):

#*****************************************************************************80
#
## r8vec_variance_circular_test() tests r8vec_variance_circular().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_variance_circular_test():' )
  print ( '  r8vec_variance_circular() computes the circular variance of an R8VEC.' )

  n = 10
  a = - np.pi
  b = + np.pi
  x = r8vec_uniform_ab ( n, a, b, rng )

  r8vec_print ( n, x, '  Uniform Vector in [-PI,+PI]:' )
  variance_circular = r8vec_variance_circular ( n, x )

  print ( '' )
  print ( '  Circular variance: %g' % ( variance_circular ) )

  n = 10
  a = 0.0
  b = 1.0

  x = r8vec_normal_ab ( n, a, b, rng )

  r8vec_print ( n, x, '  Normal vector, mean 0, variance 1' )

  variance_circular = r8vec_variance_circular ( n, x )

  print ( '' )
  print ( '  Circular variance: %g' % ( variance_circular ) )

  return

def r8vec_variance ( n, a ):

#*****************************************************************************80
#
## r8vec_variance() returns the variance of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the variance of the vector.
#
  import numpy as np

  if ( n < 2 ):

    value = 0.0

  else:

    mean = np.sum ( a[0:n] ) / n

    value = np.sum ( ( a[0:n] - mean ) ** 2 ) / ( n )

  return value

def r8vec_variance_test ( rng ):

#*****************************************************************************80
#
## r8vec_variance_test() tests r8vec_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_variance_test():' )
  print ( '  r8vec_variance() computes the variance of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_variance ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )

  return

def r8vec_variance_sample ( n, a ):

#*****************************************************************************80
#
## r8vec_variance_sample() returns the sample variance of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the variance of the vector.
#
  import numpy as np
  if ( n < 2 ):

    value = 0.0

  else:

    mean = np.sum ( a[0:n] ) / n

    value = np.sum ( ( a[0:n] - mean ) ** 2 ) / ( n - 1 )

  return value

def r8vec_variance_sample_test ( rng ):

#*****************************************************************************80
#
## r8vec_variance_sample_test() tests r8vec_variance_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vec_variance_sample_test():' )
  print ( '  r8vec_variance_sample() computes the sample variance of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0

  a = r8vec_uniform_ab ( n, r8_lo, r8_hi, rng )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_variance_sample ( n, a )
  print ( '' )
  print ( '  Sample variance = %g' % ( value ) )

  return

def r8vec_variance_sample_update ( nm1, mean_nm1, variance_nm1, xn ):

#*****************************************************************************80
#
## r8vec_variance_sample_update() updates the sample variance with one new value.
#
#  Discussion:
#
#    On first call:
#      nm1 = 0
#      mean_nm1 = 0.0
#      variance_nm1 = 0.0
#      xn = first value to be handled.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Accurately computing running variance,
#    https://www.johndcook.com/blog/standard_deviation/
#
#  Input:
#
#    integer NM1, the number of entries in the old vector.
#
#    real MEAN_NM1, the mean of the old vector.
#
#    real VARIANCE_NM1, the variance of the old vector.
#
#    real XN, the new N-th entry of the vector.
#
#  Output:
#
#    integer N, the number of entries in the new vector.
#
#    real MEAN_N, the mean of the new vector.
#
#    real VARIANCE_N, the variance of the new vector.
#
  import numpy as np

  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
    variance_n = 0.0
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n
    variance_n = ( variance_nm1 * ( nm1 - 1 ) + ( xn - mean_nm1 ) * ( xn - mean_n ) ) / ( n - 1 )

  return n, mean_n, variance_n

def r8vec_variance_sample_update_test ( rng ):

#*****************************************************************************80
#
## r8vec_variance_sample_update_test() tests r8vec_variance_sample_update().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_variance_sample_update_test():' )
  print ( '  r8vec_variance_sample_update() updates the sample variance of a vector' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R                VARIANCE          VARIANCE_update' )
  print ( '' )

  n_max = 10

  a = np.zeros ( n_max )
  mean_n = 0.0
  variance_n = 0.0

  for i in range ( 1, n_max ):

    r = rng.random ( )
    a[i-1] = r
    variance = r8vec_variance_sample ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    variance_nm1 = variance_n
    n, mean_n, variance_n = r8vec_variance_sample_update ( nm1, mean_nm1, \
      variance_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, variance, variance_n ) )

  return

def r8vec_variance_update ( nm1, mean_nm1, variance_nm1, xn ):

#*****************************************************************************80
#
## r8vec_variance_update() updates the variance with one new value.
#
#  Discussion:
#
#   On first call:
#     nm1 = 0
#     mean_nm1 = 0.0
#     variance_nm1 = 0.0
#     xn = first value to be handled.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Accurately computing running variance,
#    https://www.johndcook.com/blog/standard_deviation/
#
#  Input:
#
#    integer NM1, the number of entries in the old vector.
#
#    real MEAN_NM1, the mean of the old vector.
#
#    real VARIANCE_NM1, the variance of the old vector.
#
#    real XN, the new N-th entry of the vector.
#
#  Output:
#
#    integer N, the number of entries in the new vector.
#
#    real MEAN_N, the mean of the new vector.
#
#    real VARIANCE_N, the variance of the new vector.
#
  import numpy as np

  if ( nm1 <= 0 ):
    n = 1
    mean_n = xn
    variance_n = 0.0
  else:
    n = nm1 + 1
    mean_n = mean_nm1 + ( xn - mean_nm1 ) / n
    variance_n = ( variance_nm1 * nm1 + ( xn - mean_nm1 ) * ( xn - mean_n ) ) / n

  return n, mean_n, variance_n

def r8vec_variance_update_test ( rng ):

#*****************************************************************************80
#
## r8vec_variance_update_test() tests r8vec_variance_update().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_variance_update_test():' )
  print ( '  r8vec_variance_update() updates the variance of a vector' )
  print ( '  when one more element is added.' )
  print ( '' )
  print ( '   N      R                VARIANCE          VARIANCE_update' )
  print ( '' )

  n_max = 10

  a = np.zeros ( n_max )
  mean_n = 0.0
  variance_n = 0.0

  for i in range ( 1, n_max ):

    r = rng.random ( )
    a[i-1] = r
    variance = r8vec_variance ( i, a )

    nm1 = i - 1
    mean_nm1 = mean_n
    variance_nm1 = variance_n
    n, mean_n, variance_n = r8vec_variance_update ( nm1, mean_nm1, \
      variance_nm1, r )

    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( i, r, variance, variance_n ) )

  return

def r8_walsh_1d ( x, digit ):

#*****************************************************************************80
#
## r8_walsh_1d() evaluates the Walsh function.
#
#  Discussion:
#
#    Consider the binary representation of X, and number the digits
#    in descending order, from leading to lowest, with the units digit
#    being numbered 0.
#
#    The Walsh function W(J)(X) is equal to the J-th binary digit of X.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the Walsh function.
#
#    integer DIGIT, the index of the Walsh function.
#
#  Output:
#
#    real VALUE, the value of the Walsh function.
#

#
#  Hide the effect of the sign of X.
#
  x = abs ( x )
#
#  If DIGIT is positive, divide by 2 DIGIT times.
#  If DIGIT is negative, multiply by 2 (-DIGIT) times.
#
  x = x / 2.0 ** digit
#
#  Make it an integer.
#  Because it's positive, and we're using INT, we don't change the
#  units digit.
#
  n = int ( x )
#
#  Is the units digit odd or even?
#
  if ( ( n % 2 ) == 0 ):
    value = 0.0
  else:
    value = 1.0

  return value

def r8_walsh_1d_test ( ):

#*****************************************************************************80
#
## r8_walsh_1d_test() tests r8_walsh_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_walsh_1d_test():' )
  print ( '  r8_walsh_1d() evaluates 1D Walsh functions:' )
  print ( '' )
  print ( '  X  W(+2) W(+1) W(0) W(-1) W(-2) W(-3)' )
  print ( '' )

  for i in range ( 0, 33 ):

    x = i / 4.0

    wp2 = r8_walsh_1d ( x,  2 )
    wp1 = r8_walsh_1d ( x,  1 )
    w0  = r8_walsh_1d ( x,  0 )
    wm1 = r8_walsh_1d ( x, -1 )
    wm2 = r8_walsh_1d ( x, -2 )
    wm3 = r8_walsh_1d ( x, -3 )

    print ( '  %10f  %4f  %4f  %4f  %4f  %4f  %4f' \
      % ( x, wp2, wp1, w0, wm1, wm2, wm3 ) )

  return

def r8_wrap ( r, lo, hi ):

#*****************************************************************************80
#
## r8_wrap() forces an R8 to lie between given limits by wrapping.
#
#  Discussion:
#
#    An R8 is a real value.
#
#  Example:
#
#    LO = 4.0, HI = 8.0
#
#     R  Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, a value.
#
#    real LO, HI, the desired bounds.
#
#  Output:
#
#    real R, a "wrapped" version of the value.
#
  r = lo + ( ( r - lo ) % ( hi - lo ) )

  return r

def r8_wrap_test ( rng ):

#*****************************************************************************80
#
## r8_wrap_test() tests r8_wrap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  a = - 2.0
  b = 12.0
  rhi = 6.5
  rlo = 3.0
  test_num = 20

  print ( '' )
  print ( 'r8_wrap_test():' )
  print ( '  r8_wrap "wraps" an R8 to lie within an interval:' )
  print ( '' )
  print ( '  Wrapping interval is %f, %f' % ( rlo, rhi ) )
  print ( '' )
  print ( '      R      r8_wrap ( R )' )
  print ( '' )

  for test in range ( 0, test_num ):

    r = a + ( b - a ) * rng.random ( )
    r2 = r8_wrap ( r, rlo, rhi )
    print ( '  %14g  %14g' % ( r, r2 ) )

  return

def roots_to_r8poly ( n, x ):

#*****************************************************************************80
#
## roots_to_r8poly() converts polynomial roots to polynomial coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of roots specified.
#
#    real X(N), the roots.
#
#  Output:
#
#    real C(1:N+1), the coefficients of the polynomial.
#
  import numpy as np
#
#  Initialize C to (0, 0, ..., 0, 1).
#  Essentially, we are setting up a divided difference table.
#
  c = np.zeros ( n + 1 )
  c[n] = 1.0
#
#  Convert to standard polynomial form by shifting the abscissas
#  of the divided difference table to 0.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 1, n + 2 - j ):
      c[n-i] = c[n-i] - x[n+1-i-j] * c[n-i+1]

  return c

def roots_to_r8poly_test ( ):

#*****************************************************************************80
#
## roots_to_r8poly_test() tests roots_to_r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  n = 5

  x = np.array ( [ \
   [  1.0 ], \
   [ -4.0 ], \
   [  3.0 ], \
   [  0.0 ], \
   [  3.0 ] ] );

  print ( '' )
  print ( 'roots_to_r8poly_test():' )
  print ( '  roots_to_r8poly() is given N real roots,' )
  print ( '  and constructs the coefficient vector' )
  print ( '  of the corresponding polynomial.' )

  r8vec_print ( n, x, '  N real roots:' )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( n, c, '  The polynomial:' )

  return

def sort_heap_external ( n, indx,isgn, i1, j1, k0, k1, n1 ):

#*****************************************************************************80
#
## sort_heap_external() externally sorts a list of items into ascending order.
#
#  Discussion:
#
#    The actual list of data is not passed to the routine.  Hence this
#    routine may be used to sort integers, reals, numbers, names,
#    dates, shoe sizes, and so on.  After each call, the routine asks
#    the user to compare or interchange two items, until a special
#    return value signals that the sorting is completed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf.
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of items to be sorted.
#
#    integer INDX, the main communication signal.
#    The user must set INDX to 0 before the first call.
#    Thereafter, the user should set the input value of INDX
#    to the output value from the previous call.
#
#    integer ISGN, results of comparison of elements I and J.
#    (Used only when the previous call returned INDX less than 0).
#    ISGN <= 0 means I is less than or equal to J
#    0 <= ISGN means I is greater than or equal to J.
#
#    integer I1, J1, K0, K1, N1, variables that
#    are used for bookkeeping.  The user should declare them, and pass the
#    output values from one call as input values on the next call.  The user
#    should not change these variables.
#
#  Output:
#
#    integer INDX, the main communication signal.
#    If INDX is
#
#      greater than 0, the user should:
#      * interchange items I and J
#      * call again.
#
#      less than 0, the user should:
#      * compare items I and J
#      * set ISGN = -1 if I < J, ISGN = +1 if J < I
#      * call again.
#
#      equal to 0, the sorting is done.
#
#    integer I, J, the indices of two items.
#    On return with INDX positive, elements I and J should be interchanged.
#    On return with INDX negative, elements I and J should be compared, and
#    the result reported in ISGN on the next call.
#
#    integer I1, J1, K0, K1, N1, variables that
#    are used for bookkeeping. 
#

#
#  INDX = 0: This is the first call.
#
  if ( indx == 0 ):
      
    k0 = ( n // 2 )
    k1 = ( n // 2 )
    n1 = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
  elif ( indx < 0 ):

    if ( indx == -2 ):

      if ( isgn < 0 ):
        i1 = i1 + 1

      j1 = k1
      k1 = i1
      indx = -1
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( 0 < isgn ):
      indx = 2
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( k0 <= 1 ):

      if ( n1 == 1 ):
        i1 = 0
        j1 = 0
        indx = 0
      else:
        i1 = n1
        n1 = n1 - 1
        j1 = 1
        indx = 1

      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    k0 = k0 - 1
    k1 = k0
#
#  0 < INDX, the user was asked to make an interchange.
#
  elif ( indx == 1 ):

    k1 = k0

  while ( True ):

    i1 = 2 * k1

    if ( i1 == n1 ):
      j1 = k1
      k1 = i1
      indx = -1
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1
    elif ( i1 < n1 ):
      j1 = i1 + 1
      indx = -2
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( k0 <= 1 ):
      break

    k0 = k0 - 1
    k1 = k0

  if ( n1 == 1 ):
    i1 = 0
    j1 = 0
    indx = 0
    i = i1 - 1
    j = j1 - 1
  else:
    i1 = n1
    n1 = n1 - 1
    j1 = 1
    indx = 1
    i = i1 - 1
    j = j1 - 1

  return indx, i, j, i1, j1, k0, k1, n1

def sort_heap_external_test ( rng ):

#*****************************************************************************80
#
## sort_heap_external_test() tests sort_heap_external().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 20

  print ( '' )
  print ( 'sort_heap_external_test():' )
  print ( '  sort_heap_external() sorts objects externally.' )

  a = rng.integers ( low = 1, high = n, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array:' )

  indx = 0
  isgn = 0
  i1 = 0
  j1 = 0
  k0 = 0
  k1 = 0
  n1 = 0

  while ( True ):

    indx, i, j, i1, j1, k0, k1, n1 = sort_heap_external ( n, indx, \
      isgn, i1, j1, k0, k1, n1 )

    if ( indx < 0 ):
      isgn = 1
      if ( a[i] <= a[j] ):
        isgn = -1
    elif ( 0 < indx ):
      t    = a[i]
      a[i] = a[j]
      a[j] = t
    else:
      break

  i4vec_print ( n, a, '  Sorted array:' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def timestamp_test ( ):

#*****************************************************************************80
#
## timestamp_test() tests timestamp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'timestamp_test():' )
  print ( '  timestamp() prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  r8lib_test ( )
  timestamp ( )

