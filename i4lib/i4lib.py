#! /usr/bin/env python3
#
def i4lib_test ( ):

#*****************************************************************************80
#
## I4LIB_TEST tests the I4LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  from gamma_log_values           import gamma_log_values_test

  from i4_abs                     import i4_abs_test
  from i4_and                     import i4_and_test
  from i4_bclr                    import i4_bclr_test
  from i4_bit_hi1                 import i4_bit_hi1_test
  from i4_bit_lo0                 import i4_bit_lo0_test
  from i4_bit_lo1                 import i4_bit_lo1_test
  from i4_bit_reverse             import i4_bit_reverse_test
  from i4_bset                    import i4_bset_test
  from i4_btest                   import i4_btest_test
  from i4_ceiling                 import i4_ceiling_test
  from i4_characteristic          import i4_characteristic_test
  from i4_choose                  import i4_choose_test
  from i4_choose_check            import i4_choose_check_test
  from i4_choose_log              import i4_choose_log_test
  from i4_div_rounded             import i4_div_rounded_test
  from i4_division                import i4_division_test
  from i4_divp                    import i4_divp_test
  from i4_factorial               import i4_factorial_test
  from i4_factorial_log           import i4_factorial_log_test
  from i4_factorial2              import i4_factorial2_test
  from i4_fall                    import i4_fall_test
  from i4_floor                   import i4_floor_test
  from i4_gcd                     import i4_gcd_test
  from i4_gcdb                    import i4_gcdb_test
  from i4_huge                    import i4_huge_test
  from i4_huge_normalizer         import i4_huge_normalizer_test
  from i4_is_even                 import i4_is_even_test
  from i4_is_odd                  import i4_is_odd_test
  from i4_is_power_of_2           import i4_is_power_of_2_test
  from i4_is_power_of_10          import i4_is_power_of_10_test
  from i4_is_prime                import i4_is_prime_test
  from i4_lcm                     import i4_lcm_test
  from i4_lcm_12n                 import i4_lcm_12n_test
  from i4_log_10                  import i4_log_10_test
  from i4_log_2                   import i4_log_2_test
  from i4_log_i4                  import i4_log_i4_test
  from i4_log_r8                  import i4_log_r8_test
  from i4_mant                    import i4_mant_test
  from i4_max                     import i4_max_test
  from i4_min                     import i4_min_test
  from i4_mod_inv                 import i4_mod_inv
  from i4_moddiv                  import i4_moddiv_test
  from i4_modp                    import i4_modp_test
  from i4_mop                     import i4_mop_test
  from i4_not                     import i4_not_test
  from i4_or                      import i4_or_test
  from i4_power                   import i4_power_test
  from i4_rise                    import i4_rise_test
  from i4_sign                    import i4_sign_test
  from i4_sign3                   import i4_sign3_test
  from i4_swap                    import i4_swap_test
  from i4_swap3                   import i4_swap3_test
  from i4_to_angle                import i4_to_angle_test
  from i4_to_halton               import i4_to_halton_test
  from i4_to_isbn                 import i4_to_isbn_test
  from i4_to_l4                   import i4_to_l4_test
  from i4_to_pascal               import i4_to_pascal_test
  from i4_to_pascal_degree        import i4_to_pascal_degree_test
  from i4_to_triangle_lower       import i4_to_triangle_lower_test
  from i4_to_triangle_upper       import i4_to_triangle_upper_test
  from i4_uniform_ab              import i4_uniform_ab_test
  from i4_unswap3                 import i4_unswap3_test
  from i4_walsh_1d                import i4_walsh_1d_test
  from i4_width                   import i4_width_test
  from i4_wrap                    import i4_wrap_test
  from i4_xor                     import i4_xor_test

  from i4mat_flip_cols            import i4mat_flip_cols_test
  from i4mat_flip_rows            import i4mat_flip_rows_test
  from i4mat_indicator            import i4mat_indicator_test
  from i4mat_is_binary            import i4mat_is_binary_test
  from i4mat_is_integer           import i4mat_is_integer_test
  from i4mat_max                  import i4mat_max_test
  from i4mat_min                  import i4mat_min_test
  from i4mat_mm                   import i4mat_mm_test
  from i4mat_print                import i4mat_print_test
  from i4mat_print_some           import i4mat_print_some_test
  from i4mat_product_elementwise  import i4mat_product_elementwise_test
  from i4mat_rank                 import i4mat_rank_test
  from i4mat_ref                  import i4mat_ref_test
  from i4mat_row_reduce           import i4mat_row_reduce_test
  from i4mat_row_swap             import i4mat_row_swap_test
  from i4mat_rref                 import i4mat_rref_test
  from i4mat_rref_solve_binary    import i4mat_rref_solve_binary_test
  from i4mat_rref_solve_binary_nz import i4mat_rref_solve_binary_nz_test
  from i4mat_sum                  import i4mat_sum_test
  from i4mat_transpose            import i4mat_transpose_test
  from i4mat_transpose_print      import i4mat_transpose_print_test
  from i4mat_transpose_print_some import i4mat_transpose_print_some_test
  from i4mat_u_solve              import i4mat_u_solve_test
  from i4mat_u1_inverse           import i4mat_u1_inverse_test
  from i4mat_uniform_ab           import i4mat_uniform_ab_test
  from i4mat_width                import i4mat_width_test

  from i4row_max                  import i4row_max_test
  from i4row_mean                 import i4row_mean_test
  from i4row_min                  import i4row_min_test
  from i4row_variance             import i4row_variance_test

  from i4rows_to_i4mat            import i4rows_to_i4mat_test

  from i4vec_add                  import i4vec_add_test
  from i4vec_amax                 import i4vec_amax_test
  from i4vec_amin                 import i4vec_amin_test
  from i4vec_binary_next          import i4vec_binary_next_test
  from i4vec_choose               import i4vec_choose_test
  from i4vec_concatenate          import i4vec_concatenate_test
  from i4vec_copy                 import i4vec_copy_test
  from i4vec_cum                  import i4vec_cum_test
  from i4vec_cum0                 import i4vec_cum0_test
  from i4vec_decrement            import i4vec_decrement_test
  from i4vec_dot_product          import i4vec_dot_product_test
  from i4vec_frac                 import i4vec_frac_test
  from i4vec_heap_d               import i4vec_heap_d_test
  from i4vec_identity_row         import i4vec_identity_row_test
  from i4vec_increment            import i4vec_increment_test
  from i4vec_index                import i4vec_index_test
  from i4vec_indicator0           import i4vec_indicator0_test
  from i4vec_indicator1           import i4vec_indicator1_test
  from i4vec_is_ascending         import i4vec_is_ascending_test
  from i4vec_is_binary            import i4vec_is_binary_test
  from i4vec_is_descending        import i4vec_is_descending_test
  from i4vec_is_distinct          import i4vec_is_distinct_test
  from i4vec_is_equal             import i4vec_is_equal_test
  from i4vec_is_even_all          import i4vec_is_even_all_test
  from i4vec_is_even_any          import i4vec_is_even_any_test
  from i4vec_is_lt_any            import i4vec_is_lt_any_test
  from i4vec_is_negative_any      import i4vec_is_negative_any_test
  from i4vec_is_nonpositive_all   import i4vec_is_nonpositive_all_test
  from i4vec_is_nonzero_any       import i4vec_is_nonzero_any_test
  from i4vec_is_odd_all           import i4vec_is_odd_all_test
  from i4vec_is_odd_any           import i4vec_is_odd_any_test
  from i4vec_is_one               import i4vec_is_one_test
  from i4vec_is_pairwise_prime    import i4vec_is_pairwise_prime_test
  from i4vec_is_zero              import i4vec_is_zero_test
  from i4vec_max                  import i4vec_max_test
  from i4vec_max_index_last       import i4vec_max_index_last_test
  from i4vec_max_last             import i4vec_max_last_test
  from i4vec_mean                 import i4vec_mean_test
  from i4vec_mean_i4              import i4vec_mean_i4_test
  from i4vec_min                  import i4vec_min_test
  from i4vec_permute              import i4vec_permute_test
  from i4vec_permute_uniform      import i4vec_permute_uniform_test
  from i4vec_print                import i4vec_print_test
  from i4vec_print_mask           import i4vec_print_mask_test
  from i4vec_product              import i4vec_product_test
  from i4vec_red                  import i4vec_red_test
  from i4vec_reverse              import i4vec_reverse_test
  from i4vec_run_count            import i4vec_run_count_test
  from i4vec_search_binary_a      import i4vec_search_binary_a_test
  from i4vec_search_binary_d      import i4vec_search_binary_d_test
  from i4vec_sort_bubble_a        import i4vec_sort_bubble_a_test
  from i4vec_sort_heap_a          import i4vec_sort_heap_a_test
  from i4vec_sort_heap_index_a    import i4vec_sort_heap_index_a_test
  from i4vec_sort_heap_index_d    import i4vec_sort_heap_index_d_test
  from i4vec_sort_insert_a        import i4vec_sort_insert_a_test
  from i4vec_sort_insert_d        import i4vec_sort_insert_d_test
  from i4vec_sorted_unique        import i4vec_sorted_unique_test
  from i4vec_sorted_unique_count  import i4vec_sorted_unique_count_test
  from i4vec_sum                  import i4vec_sum_test
  from i4vec_sum_vec              import i4vec_sum_vec_test
  from i4vec_transpose_print      import i4vec_transpose_print_test
  from i4vec_uniform_ab           import i4vec_uniform_ab_test
  from i4vec_unique_count         import i4vec_unique_count_test
  from i4vec_variance             import i4vec_variance_test
  from i4vec_width                import i4vec_width_test

  from i4vec2_print               import i4vec2_print_test

  from ksub_next4                 import ksub_next4_test

  from l4_to_i4                   import l4_to_i4_test

  from pascal_to_i4               import pascal_to_i4_test

  from perm0_check                import perm0_check_test
  from perm0_uniform              import perm0_uniform_test

  from perm1_check                import perm1_check_test
  from perm1_uniform              import perm1_uniform_test

  from permutation_symbol         import permutation_symbol_test

  from prime                      import prime_test

  from r8_gamma_log               import r8_gamma_log_test
  from r8_uniform_ab              import r8_uniform_ab_test

  from r8vec_print                import r8vec_print_test

  from timestamp                  import timestamp_test

  from triangle_lower_to_i4       import triangle_lower_to_i4_test
  from triangle_upper_to_i4       import triangle_upper_to_i4_test

  print ( '' )
  print ( 'I4LIB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the I4LIB library.' )

  gamma_log_values_test ( )

  i4_abs_test ( )
  i4_and_test ( )
  i4_bclr_test ( )
  i4_bit_hi1_test ( )
  i4_bit_lo0_test ( )
  i4_bit_lo1_test ( )
  i4_bit_reverse_test ( )
  i4_bset_test ( )
  i4_btest_test ( )
  i4_ceiling_test ( )
  i4_characteristic_test ( )
  i4_choose_test ( )
  i4_choose_check_test ( )
  i4_choose_log_test ( )
  i4_div_rounded_test ( )
  i4_division_test ( )
  i4_divp_test ( )
  i4_factorial_test ( )
  i4_factorial_log_test ( )
  i4_factorial2_test ( )
  i4_fall_test ( )
  i4_floor_test ( )
  i4_gcd_test ( )
  i4_gcdb_test ( )
  i4_huge_test ( )
  i4_huge_normalizer_test ( )
  i4_is_even_test ( )
  i4_is_odd_test ( )
  i4_is_power_of_2_test ( )
  i4_is_power_of_10_test ( )
  i4_is_prime_test ( )
  i4_lcm_test ( )
  i4_lcm_12n_test ( )
  i4_log_10_test ( )
  i4_log_2_test ( )
  i4_log_i4_test ( )
  i4_log_r8_test ( )
  i4_mant_test ( )
  i4_max_test ( )
  i4_min_test ( )
  i4_moddiv_test ( )
  i4_modp_test ( )
  i4_mop_test ( )
  i4_not_test ( )
  i4_or_test ( )
  i4_power_test ( )
  i4_rise_test ( )
  i4_sign_test ( )
  i4_sign3_test ( )
  i4_swap_test ( )
  i4_swap3_test ( )
  i4_to_angle_test ( )
  i4_to_halton_test ( )
  i4_to_isbn_test ( )
  i4_to_l4_test ( )
  i4_to_pascal_test ( )
  i4_to_pascal_degree_test ( )
  i4_to_triangle_lower_test ( )
  i4_to_triangle_upper_test ( )
  i4_uniform_ab_test ( )
  i4_unswap3_test ( )
  i4_walsh_1d_test ( )
  i4_width_test ( )
  i4_wrap_test ( )
  i4_xor_test ( )

  i4mat_flip_cols_test ( )
  i4mat_flip_rows_test ( )
  i4mat_indicator_test ( )
  i4mat_is_binary_test ( )
  i4mat_is_integer_test ( )
  i4mat_max_test ( )
  i4mat_min_test ( )
  i4mat_mm_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4mat_product_elementwise_test ( )
  i4mat_rank_test ( )
  i4mat_ref_test ( )
  i4mat_row_reduce_test ( )
  i4mat_row_swap_test ( )
  i4mat_rref_test ( )
  i4mat_rref_solve_binary_test ( )
  i4mat_rref_solve_binary_nz_test ( )
  i4mat_sum_test ( )
  i4mat_transpose_test ( )
  i4mat_transpose_print_test ( )
  i4mat_transpose_print_some_test ( )
  i4mat_u_solve_test ( )
  i4mat_u1_inverse_test ( )
  i4mat_uniform_ab_test ( )
  i4mat_width_test ( )

  i4row_max_test ( )
  i4row_mean_test ( )
  i4row_min_test ( )
  i4row_variance_test ( )

  i4rows_to_i4mat_test ( )

  i4vec_add_test ( )
  i4vec_amax_test ( )
  i4vec_amin_test ( )
  i4vec_binary_next_test ( )
  i4vec_concatenate_test ( )
  i4vec_copy_test ( )
  i4vec_cum_test ( )
  i4vec_cum0_test ( )
  i4vec_decrement_test ( )
  i4vec_dot_product_test ( )
  i4vec_frac_test ( )
  i4vec_heap_d_test ( )
  i4vec_identity_row_test ( )
  i4vec_increment_test ( )
  i4vec_index_test ( )
  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_is_ascending_test ( )
  i4vec_is_binary_test ( )
  i4vec_is_descending_test ( )
  i4vec_is_distinct_test ( )
  i4vec_is_equal_test ( )
  i4vec_is_even_all_test ( )
  i4vec_is_even_any_test ( )
  i4vec_is_lt_any_test ( )
  i4vec_is_negative_any_test ( )
  i4vec_is_nonpositive_all_test ( )
  i4vec_is_nonzero_any_test ( )
  i4vec_is_odd_all_test ( )
  i4vec_is_odd_any_test ( )
  i4vec_is_one_test ( )
  i4vec_is_pairwise_prime_test ( )
  i4vec_is_zero_test ( )
  i4vec_max_test ( )
  i4vec_max_index_last_test ( )
  i4vec_max_last_test ( )
  i4vec_mean_test ( )
  i4vec_mean_i4_test ( )
  i4vec_min_test ( )
  i4vec_permute_test ( )
  i4vec_permute_uniform_test ( )
  i4vec_print_test ( )
  i4vec_print_mask_test ( )
  i4vec_product_test ( )
  i4vec_red_test ( )
  i4vec_reverse_test ( )
  i4vec_run_count_test ( )
  i4vec_search_binary_a_test ( )
  i4vec_sort_bubble_a_test ( )
  i4vec_sort_heap_a_test ( )
  i4vec_sort_heap_index_a_test ( )
  i4vec_sort_heap_index_d_test ( )
  i4vec_sort_insert_a_test ( )
  i4vec_sort_insert_d_test ( )
  i4vec_sorted_unique_test ( )
  i4vec_sorted_unique_count_test ( )
  i4vec_sum_test ( )
  i4vec_transpose_print_test ( )
  i4vec_uniform_ab_test ( )
  i4vec_unique_count_test ( )
  i4vec_variance_test ( )
  i4vec_width_test ( )

  i4vec2_print_test ( )

  ksub_next4_test ( )

  l4_to_i4_test ( )

  pascal_to_i4_test ( ) 

  perm0_check_test ( )
  perm0_uniform_test ( )

  perm1_check_test ( )
  perm1_uniform_test ( )

  permutation_symbol_test ( )

  prime_test ( )

  r8_gamma_log_test ( )
  r8_uniform_ab_test ( )

  r8vec_print_test ( )

  timestamp_test ( )

  triangle_lower_to_i4_test ( )
  triangle_upper_to_i4_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4LIB_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4lib_test ( )
  timestamp ( )

