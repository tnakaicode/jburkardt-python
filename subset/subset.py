#! /usr/bin/env python3
#
def subset_test ( ):

#*****************************************************************************80
#
## SUBSET_TEST tests SUBSET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  from agm_values                     import agm_values_test
  from asm_enum                       import asm_enum_test
  from asm_triangle                   import asm_triangle_test
  from bell                           import bell_test
  from bell_values                    import bell_values_test
  from catalan                        import catalan_test
  from catalan_row_next               import catalan_row_next_test
  from catalan_values                 import catalan_values_test
  from cfrac_to_rat                   import cfrac_to_rat_test
  from cfrac_to_rfrac                 import cfrac_to_rfrac_test
  from ch_to_digit                    import ch_to_digit_test
  from change_greedy                  import change_greedy_test
  from change_next                    import change_next_test
  from chinese_check                  import chinese_check_test
  from chinese_to_i4                  import chinese_to_i4_test
  from comb_next                      import comb_next_test
  from comb_row_next                  import comb_row_next_test
  from comb_unrank                    import comb_unrank_test
  from comp_enum                      import comp_enum_test
  from comp_next                      import comp_next_test
  from comp_next_grlex                import comp_next_grlex_test
  from comp_random_grlex              import comp_random_grlex_test
  from comp_rank_grlex                import comp_rank_grlex_test
  from comp_to_ksub                   import comp_to_ksub_test
  from comp_unrank_grlex              import comp_unrank_grlex_test
  from compnz_enum                    import compnz_enum_test
  from compnz_next                    import compnz_next_test
  from compnz_to_ksub                 import compnz_to_ksub_test
  from compnz_random                  import compnz_random_test
  from congruence                     import congruence_test
  from count_pose_random              import count_pose_random_test
  from debruijn                       import debruijn_test
  from dec_add                        import dec_add_test
  from dec_div                        import dec_div_test
  from dec_mul                        import dec_mul_test
  from dec_round                      import dec_round_test
  from dec_to_r8                      import dec_to_r8_test
  from dec_to_rat                     import dec_to_rat_test
  from dec_to_s                       import dec_to_s_test
  from dec_width                      import dec_width_test
  from derange_enum                   import derange_enum_test
  from derange_enum2                  import derange_enum2_test
  from derange_enum3                  import derange_enum3_test
  from derange0_back_next             import derange0_back_next_test
  from derange0_check                 import derange0_check_test
  from derange0_weed_next             import derange0_weed_next_test
  from digit_to_ch                    import digit_to_ch_test
  from digraph_arc_euler              import digraph_arc_euler_test
  from digraph_arc_print              import digraph_arc_print_test
  from diophantine                    import diophantine_test
  from diophantine_solution_minimize  import diophantine_solution_minimize_test
  from dvec_add                       import dvec_add_test
  from dvec_complementx               import dvec_complementx_test
  from dvec_mul                       import dvec_mul_test
  from dvec_print                     import dvec_print_test
  from dvec_sub                       import dvec_sub_test
  from dvec_to_i4                     import dvec_to_i4_test
  from equiv_print                    import equiv_print_test
  from equiv_print2                   import equiv_print2_test
  from equiv0_next                    import equiv0_next_test
  from equiv0_random                  import equiv0_random_test
  from equiv1_next                    import equiv1_next_test
  from equiv1_next2                   import equiv1_next2_test
  from euler_row                      import euler_row_test
  from frobenius_number_order2        import frobenius_number_order2_test
  from frobenius_number_order2_values import frobenius_number_order2_values_test
  from gamma_values                   import gamma_values_test
  from gamma_log_values               import gamma_log_values_test
  from gray_next                      import gray_next_test
  from gray_rank2                     import gray_rank2_test
  from gray_unrank2                   import gray_unrank2_test
  from i4_bclr                        import i4_bclr_test
  from i4_bset                        import i4_bset_test
  from i4_btest                       import i4_btest_test
  from i4_choose                      import i4_choose_test
  from i4_factor                      import i4_factor_test
  from i4_factorial                   import i4_factorial_test
  from i4_factorial_values            import i4_factorial_values_test
  from i4_fall                        import i4_fall_test
  from i4_gcd                         import i4_gcd_test
  from i4_huge                        import i4_huge_test
  from i4_log_10                      import i4_log_10_test
  from i4_modp                        import i4_modp_test
  from i4_moebius                     import i4_moebius_test
  from i4_partition_conj              import i4_partition_conj_test
  from i4_partition_count             import i4_partition_count_test
  from i4_partition_count2            import i4_partition_count2_test
  from i4_partition_count_values      import i4_partition_count_values_test
  from i4_partition_next              import i4_partition_next_test
  from i4_partition_next2             import i4_partition_next2_test
  from i4_partition_print             import i4_partition_print_test
  from i4_partition_random            import i4_partition_random_test
  from i4_partitions_next             import i4_partitions_next_test
  from i4_rise                        import i4_rise_test
  from i4_sign                        import i4_sign_test
  from i4_sqrt                        import i4_sqrt_test
  from i4_sqrt_cf                     import i4_sqrt_cf_test
  from i4_to_chinese                  import i4_to_chinese_test
  from i4_to_dvec                     import i4_to_dvec_test
  from i4_to_i4poly                   import i4_to_i4poly_test
  from i4_to_van_der_corput           import i4_to_van_der_corput_test
  from i4_uniform_ab                  import i4_uniform_ab_test
  from i4mat_mm                       import i4mat_mm_test
  from i4mat_perm0                    import i4mat_perm0_test
  from i4mat_2perm0                   import i4mat_2perm0_test
  from i4mat_print                    import i4mat_print_test
  from i4mat_print_some               import i4mat_print_some_test
  from i4mat_u1_inverse               import i4mat_u1_inverse_test
  from i4poly                         import i4poly_test
  from i4poly_add                     import i4poly_add_test
  from i4poly_cyclo                   import i4poly_cyclo_test
  from i4poly_degree                  import i4poly_degree_test
  from i4poly_dif                     import i4poly_dif_test
  from i4poly_div                     import i4poly_div_test
  from i4poly_mul                     import i4poly_mul_test
  from i4poly_print                   import i4poly_print_test
  from i4poly_to_i4                   import i4poly_to_i4_test
  from i4vec_ascends                  import i4vec_ascends_test
  from i4vec_backtrack                import i4vec_backtrack_test
  from i4vec_decrement                import i4vec_decrement_test
  from i4vec_descends                 import i4vec_descends_test
  from i4vec_frac                     import i4vec_frac_test
  from i4vec_index                    import i4vec_index_test
  from i4vec_indicator0               import i4vec_indicator0_test
  from i4vec_indicator1               import i4vec_indicator1_test
  from i4vec_max_index_last           import i4vec_max_index_last_test
  from i4vec_pairwise_prime           import i4vec_pairwise_prime_test
  from i4vec_print                    import i4vec_print_test
  from i4vec_product                  import i4vec_product_test
  from i4vec_reverse                  import i4vec_reverse_test
  from i4vec_sort_bubble_a            import i4vec_sort_bubble_a_test
  from i4vec_sort_heap_index_d        import i4vec_sort_heap_index_d_test
  from i4vec_sum                      import i4vec_sum_test
  from i4vec_transpose_print          import i4vec_transpose_print_test
  from i4vec_uniform_ab               import i4vec_uniform_ab_test
  from index_box_next_2d              import index_box_next_2d_test
  from index_box_next_3d              import index_box_next_3d_test
  from index_box2_next_2d             import index_box2_next_2d_test
  from index_box2_next_3d             import index_box2_next_3d_test
  from index_next0                    import index_next0_test
  from index_next1                    import index_next1_test
  from index_next2                    import index_next2_test
  from index_rank0                    import index_rank0_test
  from index_rank1                    import index_rank1_test
  from index_rank2                    import index_rank2_test
  from index_unrank0                  import index_unrank0_test
  from index_unrank1                  import index_unrank1_test
  from index_unrank2                  import index_unrank2_test
  from inverse_mod_n                  import inverse_mod_n_test
  from inversion_to_perm0             import inversion_to_perm0_test
  from involute_enum                  import involute_enum_test
  from jfrac_to_rfrac                 import jfrac_to_rfrac_test
  from josephus                       import josephus_test
  from ksub_next                      import ksub_next_test
  from ksub_next2                     import ksub_next2_test
  from ksub_next3                     import ksub_next3_test
  from ksub_next4                     import ksub_next4_test
  from ksub_random                    import ksub_random_test
  from ksub_random2                   import ksub_random2_test
  from ksub_random3                   import ksub_random3_test
  from ksub_random4                   import ksub_random4_test
  from ksub_random5                   import ksub_random5_test
  from ksub_rank                      import ksub_rank_test
  from ksub_to_comp                   import ksub_to_comp_test
  from ksub_to_compnz                 import ksub_to_compnz_test
  from ksub_unrank                    import ksub_unrank_test
  from l4vec_next                     import l4vec_next_test
  from moebius_values                 import moebius_values_test
  from monomial_count                 import monomial_count_test
  from monomial_counts                import monomial_counts_test
  from morse_thue                     import morse_thue_test
  from multinomial_coef1              import multinomial_coef1_test
  from multinomial_coef2              import multinomial_coef2_test
  from multiperm_enum                 import multiperm_enum_test
  from multiperm_next                 import multiperm_next_test
  from nim_sum                        import nim_sum_test
  from padovan                        import padovan_test
  from pell_basic                     import pell_basic_test
  from pell_next                      import pell_next_test
  from pent_enum                      import pent_enum_test
  from perm_ascend                    import perm_ascend_test
  from perm_fixed_enum                import perm_fixed_enum_test
  from perm0_break_count              import perm0_break_count_test
  from perm0_check                    import perm0_check_test
  from perm0_cycle                    import perm0_cycle_test
  from perm0_distance                 import perm0_distance_test
  from perm0_free                     import perm0_free_test
  from perm0_inverse                  import perm0_inverse_test
  from perm0_inverse2                 import perm0_inverse2_test
  from perm0_inverse3                 import perm0_inverse3_test
  from perm0_lex_next                 import perm0_lex_next_test
  from perm0_mul                      import perm0_mul_test
  from perm0_next                     import perm0_next_test
  from perm0_next3                    import perm0_next3_test
  from perm0_print                    import perm0_print_test
  from perm0_random                   import perm0_random_test
  from perm0_random2                  import perm0_random2_test
  from perm0_rank                     import perm0_rank_test
  from perm0_sign                     import perm0_sign_test
  from perm0_to_equiv                 import perm0_to_equiv_test
  from perm0_to_inversion             import perm0_to_inversion_test
  from perm0_to_ytb                   import perm0_to_ytb_test
  from perm0_unrank                   import perm0_unrank_test
  from perm1_canon_to_cycle           import perm1_canon_to_cycle_test
  from perm1_check                    import perm1_check_test
  from perm1_cycle_to_canon           import perm1_cycle_to_canon_test
  from perm1_cycle_to_index           import perm1_cycle_to_index_test
  from perm1_index_to_cycle           import perm1_index_to_cycle_test
  from perm1_print                    import perm1_print_test
  from perrin                         import perrin_test
  from pord_check                     import pord_check_test
  from power_mod                      import power_mod_test
  from power_series1                  import power_series1_test
  from power_series2                  import power_series2_test
  from power_series3                  import power_series3_test
  from power_series4                  import power_series4_test
  from prime                          import prime_test
  from pythag_triple_next             import pythag_triple_next_test
  from r8_agm                         import r8_agm_test
  from r8_choose                      import r8_choose_test
  from r8_fall                        import r8_fall_test
  from r8_fall_values                 import r8_fall_values_test
  from r8_gamma                       import r8_gamma_test
  from r8_rise                        import r8_rise_test
  from r8_rise_values                 import r8_rise_values_test
  from r8_to_cfrac                    import r8_to_cfrac_test
  from r8_to_dec                      import r8_to_dec_test
  from r8_to_rat                      import r8_to_rat_test
  from r8_uniform_01                  import r8_uniform_01_test
  from r8_uniform_ab                  import r8_uniform_ab_test
  from r8mat_det                      import r8mat_det_test
  from r8mat_perm0                    import r8mat_perm0_test
  from r8mat_2perm0                   import r8mat_2perm0_test
  from r8mat_permanent                import r8mat_permanent_test
  from r8mat_print                    import r8mat_print_test
  from r8mat_print_some               import r8mat_print_some_test
  from r8poly                         import r8poly_test
  from r8poly_f2p                     import r8poly_f2p_test
  from r8poly_fval                    import r8poly_fval_test
  from r8poly_n2p                     import r8poly_n2p_test
  from r8poly_nval                    import r8poly_nval_test
  from r8poly_nx                      import r8poly_nx_test
  from r8poly_p2f                     import r8poly_p2f_test
  from r8poly_p2n                     import r8poly_p2n_test
  from r8poly_p2t                     import r8poly_p2t_test
  from r8poly_print                   import r8poly_print_test
  from r8poly_pval                    import r8poly_pval_test
  from r8poly_t2p                     import r8poly_t2p_test
  from r8vec_backtrack                import r8vec_backtrack_test
  from r8vec_frac                     import r8vec_frac_test
  from r8vec_indicator1               import r8vec_indicator1_test
  from r8vec_mirror_next              import r8vec_mirror_next_test
  from r8vec_print                    import r8vec_print_test
  from r8vec_uniform_01               import r8vec_uniform_01_test
  from r8vec_uniform_ab               import r8vec_uniform_ab_test
  from rat_add                        import rat_add_test
  from rat_div                        import rat_div_test
  from rat_farey                      import rat_farey_test
  from rat_farey2                     import rat_farey2_test
  from rat_mul                        import rat_mul_test
  from rat_normalize                  import rat_normalize_test
  from rat_to_cfrac                   import rat_to_cfrac_test
  from rat_to_dec                     import rat_to_dec_test
  from rat_to_r8                      import rat_to_r8_test
  from rat_to_s                       import rat_to_s_test
  from rat_width                      import rat_width_test
  from regro_next                     import regro_next_test
  from rfrac_to_cfrac                 import rfrac_to_cfrac_test
  from rfrac_to_jfrac                 import rfrac_to_jfrac_test
  from schroeder                      import schroeder_test
  from subcomp_next                   import subcomp_next_test
  from sort_heap_external             import sort_heap_external_test
  from subcompnz_next                 import subcompnz_next_test
  from subcompnz2_next                import subcompnz2_next_test
  from subset_by_size_next            import subset_by_size_next_test
  from subset_gray_next               import subset_gray_next_test
  from subset_gray_rank               import subset_gray_rank_test
  from subset_gray_unrank             import subset_gray_unrank_test
  from subset_lex_next                import subset_lex_next_test
  from subset_random                  import subset_random_test
  from subtriangle_next               import subtriangle_next_test
  from thue_binary_next               import thue_binary_next_test
  from thue_ternary_next              import thue_ternary_next_test
  from timestamp                      import timestamp_test
  from triang                         import triang_test
  from tuple_next                     import tuple_next_test
  from tuple_next2                    import tuple_next2_test
  from tuple_next_fast                import tuple_next_fast_test
  from tuple_next_ge                  import tuple_next_ge_test
  from ubvec_add                      import ubvec_add_test
  from ubvec_print                    import ubvec_print_test
  from ubvec_to_ui4                   import ubvec_to_ui4_test
  from ubvec_xor                      import ubvec_xor_test
  from ui4_to_ubvec                   import ui4_to_ubvec_test
  from vec_colex_next                 import vec_colex_next_test
  from vec_colex_next2                import vec_colex_next2_test
  from vec_colex_next3                import vec_colex_next3_test
  from vec_gray_next                  import vec_gray_next_test
  from vec_gray_rank                  import vec_gray_rank_test
  from vec_gray_unrank                import vec_gray_unrank_test
  from vec_lex_next                   import vec_lex_next_test
  from vec_random                     import vec_random_test
  from vector_constrained_next        import vector_constrained_next_test
  from vector_constrained_next2       import vector_constrained_next2_test
  from vector_constrained_next3       import vector_constrained_next3_test
  from vector_constrained_next4       import vector_constrained_next4_test
  from vector_constrained_next5       import vector_constrained_next5_test
  from vector_constrained_next6       import vector_constrained_next6_test
  from vector_constrained_next7       import vector_constrained_next7_test
  from vector_next                    import vector_next_test
  from ytb_enum                       import ytb_enum_test
  from ytb_next                       import ytb_next_test
  from ytb_print                      import ytb_print_test
  from ytb_random                     import ytb_random_test

  print ( '' )
  print ( 'SUBSET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SUBSET library.' )

  agm_values_test ( )
  asm_enum_test ( )
  asm_triangle_test ( )

  bell_test ( )
  bell_values_test ( )

  catalan_test ( )
  catalan_row_next_test ( )
  catalan_values_test ( )

  cfrac_to_rat_test ( )
  cfrac_to_rfrac_test ( )

  ch_to_digit_test ( )

  change_greedy_test ( )
  change_next_test ( )

  chinese_check_test ( )
  chinese_to_i4_test ( )

  comb_next_test ( )
  comb_row_next_test ( )
  comb_unrank_test ( )

  comp_enum_test ( )
  comp_next_test ( )
  comp_next_grlex_test ( )
  comp_random_grlex_test ( )
  comp_rank_grlex_test ( )
  comp_to_ksub_test ( )
  comp_unrank_grlex_test ( )

  compnz_enum_test ( )
  compnz_next_test ( )
  compnz_random_test ( )
  compnz_to_ksub_test ( )

  congruence_test ( )

  count_pose_random_test ( )

  debruijn_test ( )

  dec_add_test ( )
  dec_div_test ( )
  dec_mul_test ( )
  dec_round_test ( )
  dec_to_r8_test ( )
  dec_to_rat_test ( )
  dec_to_s_test ( )
  dec_width_test ( )

  derange_enum_test ( )
  derange_enum2_test ( )
  derange_enum3_test ( )

  derange0_back_next_test ( )
  derange0_check_test ( )
  derange0_weed_next_test ( )

  digit_to_ch_test ( )

  digraph_arc_euler_test ( )
  digraph_arc_print_test ( )

  diophantine_test ( )
  diophantine_solution_minimize_test ( )

  dvec_add_test ( )
  dvec_complementx_test ( )
  dvec_mul_test ( )
  dvec_print_test ( )
  dvec_sub_test ( )
  dvec_to_i4_test ( )

  equiv_print_test ( )
  equiv_print2_test ( )

  equiv0_next_test ( )
  equiv0_random_test ( )

  equiv1_next_test ( )
  equiv1_next2_test ( )

  euler_row_test ( )

  frobenius_number_order2_test ( )
  frobenius_number_order2_values_test ( )

  gamma_values_test ( )
  gamma_log_values_test ( )

  gray_next_test ( )
  gray_rank2_test ( )
  gray_unrank2_test ( )

  i4_bclr_test ( )
  i4_bset_test ( )
  i4_btest_test ( )
  i4_choose_test ( )
  i4_factor_test ( )
  i4_factorial_test ( )
  i4_factorial_values_test ( )
  i4_fall_test ( )
  i4_gcd_test ( )
  i4_huge_test ( )
  i4_log_10_test ( )
  i4_modp_test ( )
  i4_moebius_test ( )
  i4_partition_conj_test ( )
  i4_partition_count_test ( )
  i4_partition_count2_test ( )
  i4_partition_count_values_test ( )
  i4_partition_next_test ( )
  i4_partition_next2_test ( )
  i4_partition_print_test ( )
  i4_partition_random_test ( )
  i4_partitions_next_test ( )
  i4_rise_test ( )
  i4_sign_test ( )
  i4_sqrt_test ( )
  i4_sqrt_cf_test ( )
  i4_to_chinese_test ( )
  i4_to_dvec_test ( )
  i4_to_i4poly_test ( )
  i4_to_van_der_corput_test ( )
  i4_uniform_ab_test ( )

  i4mat_mm_test ( )
  i4mat_2perm0_test ( )
  i4mat_perm0_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4mat_u1_inverse_test ( )

  i4poly_test ( )
  i4poly_add_test ( )
  i4poly_cyclo_test ( )
  i4poly_degree_test ( )
  i4poly_dif_test ( )
  i4poly_div_test ( )
  i4poly_mul_test ( )
  i4poly_print_test ( )
  i4poly_to_i4_test ( )

  i4vec_ascends_test ( )
  i4vec_backtrack_test ( )
  i4vec_decrement_test ( )
  i4vec_descends_test ( )
  i4vec_frac_test ( )
  i4vec_index_test ( )
  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_max_index_last_test ( )
  i4vec_pairwise_prime_test ( )
  i4vec_print_test ( )
  i4vec_product_test ( )
  i4vec_reverse_test ( )
  i4vec_sort_bubble_a_test ( )
  i4vec_sort_heap_index_d_test ( )
  i4vec_sum_test ( )
  i4vec_transpose_print_test ( )
  i4vec_uniform_ab_test ( )

  index_box_next_2d_test ( )
  index_box_next_3d_test ( )
  index_box2_next_2d_test ( )
  index_box2_next_3d_test ( )

  index_next0_test ( )
  index_next1_test ( )
  index_next2_test ( )
  index_rank0_test ( )
  index_rank1_test ( )
  index_rank2_test ( )
  index_unrank0_test ( )
  index_unrank1_test ( )
  index_unrank2_test ( )

  inverse_mod_n_test ( )

  inversion_to_perm0_test ( )

  involute_enum_test ( )

  jfrac_to_rfrac_test ( )

  josephus_test ( )

  ksub_next_test ( )
  ksub_next2_test ( )
  ksub_next3_test ( )
  ksub_next4_test ( )
  ksub_random_test ( )
  ksub_random2_test ( )
  ksub_random3_test ( )
  ksub_random4_test ( )
  ksub_random5_test ( )
  ksub_rank_test ( )
  ksub_to_comp_test ( )
  ksub_to_compnz_test ( )
  ksub_unrank_test ( )

  l4vec_next_test ( )

  moebius_values_test ( )

  monomial_count_test ( )
  monomial_counts_test ( )

  morse_thue_test ( )

  multinomial_coef1_test ( )
  multinomial_coef2_test ( )

  multiperm_enum_test ( )
  multiperm_next_test ( )

  nim_sum_test ( )

  padovan_test ( )

  pell_basic_test ( )
  pell_next_test ( )

  pent_enum_test ( )

  perm_ascend_test ( )
  perm_fixed_enum_test ( )

  perm0_break_count_test ( )
  perm0_check_test ( )
  perm0_cycle_test ( )
  perm0_distance_test ( )
  perm0_free_test ( )
  perm0_inverse_test ( )
  perm0_inverse2_test ( )
  perm0_inverse3_test ( )
  perm0_lex_next_test ( )
  perm0_mul_test ( )
  perm0_next_test ( )
  perm0_next3_test ( )
  perm0_print_test ( )
  perm0_random_test ( )
  perm0_random2_test ( )
  perm0_rank_test ( )
  perm0_sign_test ( )
  perm0_to_equiv_test ( )
  perm0_to_inversion_test ( )
  perm0_to_ytb_test ( )
  perm0_unrank_test ( )

  perm1_canon_to_cycle_test ( )
  perm1_check_test ( )
  perm1_cycle_to_canon_test ( )
  perm1_cycle_to_index_test ( )
  perm1_index_to_cycle_test ( )
  perm1_print_test ( )

  perrin_test ( )

  pord_check_test ( )

  power_mod_test ( )

  power_series1_test ( )
  power_series2_test ( )
  power_series3_test ( )
  power_series4_test ( )

  prime_test ( )

  pythag_triple_next_test ( )

  r8_agm_test ( )
  r8_choose_test ( )
  r8_fall_test ( )
  r8_fall_values_test ( )
  r8_gamma_test ( )
  r8_rise_test ( )
  r8_rise_values_test ( )
  r8_to_cfrac_test ( )
  r8_to_dec_test ( )
  r8_to_rat_test ( )
  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )

  r8mat_det_test ( )
  r8mat_2perm0_test ( )
  r8mat_perm0_test ( )
  r8mat_permanent_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )

  r8poly_test ( )
  r8poly_f2p_test ( )
  r8poly_fval_test ( )
  r8poly_n2p_test ( )
  r8poly_nval_test ( )
  r8poly_nx_test ( )
  r8poly_p2f_test ( )
  r8poly_p2n_test ( )
  r8poly_p2t_test ( )
  r8poly_print_test ( )
  r8poly_pval_test ( )
  r8poly_t2p_test ( )

  r8vec_backtrack_test ( )
  r8vec_frac_test ( )
  r8vec_indicator1_test ( )
  r8vec_mirror_next_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )

  rat_add_test ( )
  rat_div_test ( )
  rat_farey_test ( )
  rat_farey2_test ( )
  rat_mul_test ( )
  rat_normalize_test ( )
  rat_to_cfrac_test ( )
  rat_to_dec_test ( )
  rat_to_r8_test ( )
  rat_to_s_test ( )
  rat_width_test ( )

  regro_next_test ( )

  rfrac_to_cfrac_test ( )
  rfrac_to_jfrac_test ( )

  schroeder_test ( )

  sort_heap_external_test ( )

  subcomp_next_test ( )

  subcompnz_next_test ( )
  subcompnz2_next_test ( )

  subset_by_size_next_test ( )
  subset_gray_next_test ( )
  subset_gray_rank_test ( )
  subset_gray_unrank_test ( )
  subset_lex_next_test ( )
  subset_random_test ( )

  subtriangle_next_test ( )

  thue_binary_next_test ( )
  thue_ternary_next_test ( )

  tuple_next_test ( )
  tuple_next2_test ( )
  tuple_next_fast_test ( )
  tuple_next_ge_test ( )

  timestamp_test ( )

  triang_test ( )

  tuple_next_test ( )
  tuple_next2_test ( )

  ubvec_add_test ( )
  ubvec_print_test ( )
  ubvec_to_ui4_test ( )
  ubvec_xor_test ( )

  ui4_to_ubvec_test ( )

  vec_colex_next_test ( )
  vec_colex_next2_test ( )
  vec_colex_next3_test ( )

  vec_gray_next_test ( )
  vec_gray_rank_test ( )
  vec_gray_unrank_test ( )

  vec_lex_next_test ( )

  vec_random_test ( )

  vector_constrained_next_test ( )
  vector_constrained_next2_test ( )
  vector_constrained_next3_test ( )
  vector_constrained_next4_test ( )
  vector_constrained_next5_test ( )
  vector_constrained_next6_test ( )
  vector_constrained_next7_test ( )
  vector_next_test ( )

  ytb_enum_test ( )
  ytb_next_test ( )
  ytb_print_test ( )
  ytb_random_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_test ( )
  timestamp ( )

