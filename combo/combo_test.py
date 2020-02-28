#! /usr/bin/env python3
#
def combo_test ( ):

#*****************************************************************************80
#
## COMBO_TEST tests the COMBO library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  from backtrack                 import backtrack_test

  from bal_seq_check             import bal_seq_check_test
  from bal_seq_enum              import bal_seq_enum_test
  from bal_seq_rank              import bal_seq_rank_test
  from bal_seq_successor         import bal_seq_successor_test
  from bal_seq_to_tableau        import bal_seq_to_tableau_test
  from bal_seq_unrank            import bal_seq_unrank_test

  from bell_numbers              import bell_numbers_test
  from bell_values               import bell_values_test

  from cycle_check               import cycle_check_test
  from cycle_to_perm             import cycle_to_perm_test

  from dist_enum                 import dist_enum_test
  from dist_next                 import dist_next_test

  from edge_check                import edge_check_test
  from edge_degree               import edge_degree_test
  from edge_enum                 import edge_enum_test

  from gamma_log_values          import gamma_log_values_test

  from gray_code_check           import gray_code_check_test
  from gray_code_enum            import gray_code_enum_test
  from gray_code_rank            import gray_code_rank_test
  from gray_code_successor       import gray_code_successor_test
  from gray_code_unrank          import gray_code_unrank_test

  from i4_choose                 import i4_choose_test
  from i4_factorial              import i4_factorial_test
  from i4_factorial_values       import i4_factorial_values_test
  from i4_fall                   import i4_fall_test
  from i4_fall_values            import i4_fall_values_test
  from i4_huge                   import i4_huge_test
  from i4_uniform_ab             import i4_uniform_ab_test

  from i4mat_print               import i4mat_print_test
  from i4mat_print_some          import i4mat_print_some_test

  from i4vec_backtrack           import i4vec_backtrack_test
  from i4vec_dot_product         import i4vec_dot_product_test
  from i4vec_indicator1          import i4vec_indicator1_test
  from i4vec_part1               import i4vec_part1_test
  from i4vec_part2               import i4vec_part2_test
  from i4vec_print               import i4vec_print_test
  from i4vec_reverse             import i4vec_reverse_test
  from i4vec_search_binary_a     import i4vec_search_binary_a_test
  from i4vec_search_binary_d     import i4vec_search_binary_d_test
  from i4vec_sort_insert_a       import i4vec_sort_insert_a_test
  from i4vec_sort_insert_d       import i4vec_sort_insert_d_test
  from i4vec_uniform_ab          import i4vec_uniform_ab_test

  from knapsack_01               import knapsack_01_test
  from knapsack_rational         import knapsack_rational_test
  from knapsack_reorder          import knapsack_reorder_test

  from ksubset_colex_check       import ksubset_colex_check_test
  from ksubset_colex_rank        import ksubset_colex_rank_test
  from ksubset_colex_successor   import ksubset_colex_successor_test
  from ksubset_colex_unrank      import ksubset_colex_unrank_test
  from ksubset_enum              import ksubset_enum_test
  from ksubset_lex_check         import ksubset_lex_check_test
  from ksubset_lex_rank          import ksubset_lex_rank_test
  from ksubset_lex_successor     import ksubset_lex_successor_test
  from ksubset_lex_unrank        import ksubset_lex_unrank_test
  from ksubset_revdoor_rank      import ksubset_revdoor_rank_test
  from ksubset_revdoor_successor import ksubset_revdoor_successor_test
  from ksubset_revdoor_unrank    import ksubset_revdoor_unrank_test

  from marriage                  import marriage_test

  from mountain                  import mountain_test

  from npart_enum                import npart_enum_test
  from npart_rsf_lex_random      import npart_rsf_lex_random_test
  from npart_rsf_lex_rank        import npart_rsf_lex_rank_test
  from npart_rsf_lex_successor   import npart_rsf_lex_successor_test
  from npart_rsf_lex_unrank      import npart_rsf_lex_unrank_test
  from npart_sf_lex_successor    import npart_sf_lex_successor_test
  from npart_table               import npart_table_test

  from part_enum                 import part_enum_test
  from part_rsf_check            import part_rsf_check_test
  from part_sf_check             import part_sf_check_test
  from part_sf_conjugate         import part_sf_conjugate_test
  from part_sf_majorize          import part_sf_majorize_test
  from part_successor            import part_successor_test
  from part_table                import part_table_test

  from partn_enum                import partn_enum_test
  from partn_sf_check            import partn_sf_check_test
  from partn_successor           import partn_successor_test

  from partition_greedy          import partition_greedy_test

  from perm_check                import perm_check_test
  from perm_enum                 import perm_enum_test
  from perm_inv                  import perm_inv_test
  from perm_lex_rank             import perm_lex_rank_test
  from perm_lex_successor        import perm_lex_successor_test
  from perm_lex_unrank           import perm_lex_unrank_test
  from perm_mul                  import perm_mul_test
  from perm_parity               import perm_parity_test
  from perm_print                import perm_print_test
  from perm_random               import perm_random_test
  from perm_tj_rank              import perm_tj_rank_test
  from perm_tj_successor         import perm_tj_successor_test
  from perm_tj_unrank            import perm_tj_unrank_test
  from perm_to_cycle             import perm_to_cycle_test

  from pruefer_check             import pruefer_check_test
  from pruefer_enum              import pruefer_enum_test
  from pruefer_rank              import pruefer_rank_test
  from pruefer_successor         import pruefer_successor_test
  from pruefer_to_tree           import pruefer_to_tree_test
  from pruefer_unrank            import pruefer_unrank_test

  from queens                    import queens_test

  from r8_choose                 import r8_choose_test
  from r8_gamma_log              import r8_gamma_log_test

  from r8vec_backtrack           import r8vec_backtrack_test

  from rgf_check                 import rgf_check_test
  from rgf_enum                  import rgf_enum_test
  from rgf_rank                  import rgf_rank_test
  from rgf_successor             import rgf_successor_test
  from rgf_to_setpart            import rgf_to_setpart_test
  from rgf_unrank                import rgf_unrank_test

  from rgf_g_table               import rgf_g_table_test

  from setpart_check             import setpart_check_test
  from setpart_enum              import setpart_enum_test
  from setpart_to_rgf            import setpart_to_rgf_test

  from stirling_numbers1         import stirling_numbers1_test
  from stirling_numbers2         import stirling_numbers2_test

  from subset_check              import subset_check_test
  from subset_colex_rank         import subset_colex_rank_test
  from subset_colex_successor    import subset_colex_successor_test
  from subset_colex_unrank       import subset_colex_unrank_test
  from subset_complement         import subset_complement_test
  from subset_distance           import subset_distance_test
  from subset_enum               import subset_enum_test
  from subset_intersect          import subset_intersect_test
  from subset_lex_rank           import subset_lex_rank_test
  from subset_lex_successor      import subset_lex_successor_test
  from subset_lex_unrank         import subset_lex_unrank_test
  from subset_random             import subset_random_test
  from subset_union              import subset_union_test
  from subset_weight             import subset_weight_test
  from subset_xor                import subset_xor_test

  from subsetsum_swap            import subsetsum_swap_test

  from tableau_check             import tableau_check_test
  from tableau_enum              import tableau_enum_test
  from tableau_to_bal_seq        import tableau_to_bal_seq_test

  from tree_check                import tree_check_test
  from tree_enum                 import tree_enum_test
  from tree_rank                 import tree_rank_test
  from tree_successor            import tree_successor_test
  from tree_to_pruefer           import tree_to_pruefer_test
  from tree_unrank               import tree_unrank_test

  print ( '' )
  print ( 'COMBO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the COMBO library.' )

  backtrack_test ( )

  bal_seq_check_test ( )
  bal_seq_enum_test ( )
  bal_seq_rank_test ( )
  bal_seq_successor_test ( )
  bal_seq_to_tableau_test ( )
  bal_seq_unrank_test ( )

  bell_numbers_test ( )
  bell_values_test ( )

  cycle_check_test ( )
  cycle_to_perm_test ( )

  dist_enum_test ( )
  dist_next_test ( )

  edge_check_test ( )
  edge_degree_test ( )
  edge_enum_test ( )

  gamma_log_values_test ( )

  gray_code_check_test ( )
  gray_code_enum_test ( )
  gray_code_rank_test ( )
  gray_code_successor_test ( )
  gray_code_unrank_test ( )

  i4_choose_test ( )
  i4_factorial_test ( )
  i4_factorial_values_test ( )
  i4_fall_test ( )
  i4_fall_values_test ( )
  i4_huge_test ( )
  i4_uniform_ab_test ( )

  i4mat_print_test ( );
  i4mat_print_some_test ( )

  i4vec_backtrack_test ( )
  i4vec_dot_product_test ( )
  i4vec_indicator1_test ( )
  i4vec_part1_test ( )
  i4vec_part2_test ( )
  i4vec_print_test ( )
  i4vec_reverse_test ( )
  i4vec_search_binary_a_test ( )
  i4vec_search_binary_d_test ( )
  i4vec_sort_insert_a_test ( )
  i4vec_sort_insert_d_test ( )
  i4vec_uniform_ab_test ( )

  knapsack_01_test ( )
  knapsack_rational_test ( )
  knapsack_reorder_test ( )

  ksubset_colex_check_test ( )
  ksubset_colex_rank_test ( )
  ksubset_colex_successor_test ( )
  ksubset_colex_unrank_test ( )
  ksubset_enum_test ( )
  ksubset_lex_check_test ( )
  ksubset_lex_rank_test ( )
  ksubset_lex_successor_test ( )
  ksubset_lex_unrank_test ( )
  ksubset_revdoor_rank_test ( )
  ksubset_revdoor_successor_test ( )
  ksubset_revdoor_unrank_test ( )

  marriage_test ( )

  mountain_test ( )

  npart_enum_test ( )
  npart_rsf_lex_random_test ( )
  npart_rsf_lex_rank_test ( )
  npart_rsf_lex_successor_test ( )
  npart_rsf_lex_unrank_test ( )
  npart_sf_lex_successor_test ( )
  npart_table_test ( )

  part_enum_test ( )
  part_rsf_check_test ( )
  part_sf_check_test ( )
  part_sf_conjugate_test ( )
  part_sf_majorize_test ( )
  part_successor_test ( )
  part_table_test ( )

  partn_enum_test ( )
  partn_sf_check_test ( )
  partn_successor_test ( )

  partition_greedy_test ( )

  perm_check_test ( )
  perm_enum_test ( )
  perm_inv_test ( )
  perm_lex_rank_test ( )
  perm_lex_successor_test ( )
  perm_lex_unrank_test ( )
  perm_mul_test ( )
  perm_parity_test ( )
  perm_print_test ( )
  perm_random_test ( )
  perm_tj_rank_test ( )
  perm_tj_successor_test ( )
  perm_tj_unrank_test ( )
  perm_to_cycle_test ( )

  pruefer_check_test ( )
  pruefer_enum_test ( )
  pruefer_rank_test ( )
  pruefer_successor_test ( )
  pruefer_to_tree_test ( )
  pruefer_unrank_test ( )

  queens_test ( )

  r8_choose_test ( )
  r8_gamma_log_test ( )

  r8vec_backtrack_test ( )

  rgf_check_test ( )
  rgf_enum_test ( )
  rgf_rank_test ( )
  rgf_successor_test ( )
  rgf_to_setpart_test ( )
  rgf_unrank_test ( )

  rgf_g_table_test ( )

  setpart_check_test ( )
  setpart_enum_test ( )
  setpart_to_rgf_test ( )

  stirling_numbers1_test ( )
  stirling_numbers2_test ( )

  subset_check_test ( )
  subset_colex_rank_test ( )
  subset_colex_successor_test ( )
  subset_colex_unrank_test ( )
  subset_complement_test ( )
  subset_distance_test ( )
  subset_enum_test ( )
  subset_intersect_test ( )
  subset_lex_rank_test ( )
  subset_lex_successor_test ( )
  subset_lex_unrank_test ( )
  subset_random_test ( )
  subset_union_test ( )
  subset_weight_test ( )
  subset_xor_test ( )

  subsetsum_swap_test ( )

  tableau_check_test ( )
  tableau_enum_test ( )
  tableau_to_bal_seq_test ( )

  tree_check_test ( )
  tree_enum_test ( )
  tree_rank_test ( )
  tree_successor_test ( )
  tree_to_pruefer_test ( )
  tree_unrank_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMBO_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  combo_test ( )
  timestamp ( )
 
