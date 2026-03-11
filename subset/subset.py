#! /usr/bin/env python3
#
def subset_test ( ):

#*****************************************************************************80
#
## subset_test() tests subset().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test subset().' )

  rng = default_rng ( )

  agm_values_test ( )
  asm_enum_test ( )
  asm_triangle_test ( )

  bell_test ( )
  bell_values_test ( )

  catalan_number_test ( )
  catalan_numbers_test ( )
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
  comp_random_grlex_test ( rng )
  comp_rank_grlex_test ( rng )
  comp_to_ksub_test ( rng )
  comp_unrank_grlex_test ( )

  compnz_enum_test ( )
  compnz_next_test ( )
  compnz_random_test ( rng )
  compnz_to_ksub_test ( rng )

  congruence_test ( )

  count_pose_random_test ( rng )

  debruijn_test ( )

  dec_add_test ( )
  dec_div_test ( )
  dec_mul_test ( )
  dec_round_test ( )
  dec_to_r8_test ( rng )
  dec_to_rat_test ( rng )
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

  dvec_add_test ( rng )
  dvec_complementx_test ( rng )
  dvec_mul_test ( rng )
  dvec_print_test ( )
  dvec_sub_test ( rng )
  dvec_to_i4_test ( rng )

  equiv_print_test ( rng )
  equiv_print2_test ( rng )

  equiv0_next_test ( )
  equiv0_random_test ( rng )

  equiv1_next_test ( )
  equiv1_next2_test ( )

  euler_row_test ( )

  frobenius_number_order2_test ( )
  frobenius_number_order2_values_test ( )

  gray_next_test ( )
  gray_rank2_test ( )
  gray_unrank2_test ( )

  i4_bclr_test ( )
  i4_bset_test ( )
  i4_btest_test ( )
  i4_choose_test ( )
  i4_factor_test ( )
  i4_fall_test ( )
  i4_gcd_test ( )
  i4_gpf_test ( )
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
  i4_partition_random_test ( rng )
  i4_partitions_next_test ( )
  i4_rise_test ( )
  i4_sign_test ( )
  i4_sqrt_test ( )
  i4_sqrt_cf_test ( )
  i4_to_chinese_test ( )
  i4_to_dvec_test ( rng )
  i4_to_i4poly_test ( )
  i4_to_van_der_corput_test ( )

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
  i4vec_decrement_test ( rng )
  i4vec_descends_test ( )
  i4vec_frac_test ( rng )
  i4vec_index_test ( rng )
  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_max_index_last_test ( rng )
  i4vec_pairwise_prime_test ( )
  i4vec_print_test ( )
  i4vec_product_test ( rng )
  i4vec_reverse_test ( rng )
  i4vec_sort_bubble_a_test ( rng )
  i4vec_sort_heap_index_d_test ( rng )
  i4vec_transpose_print_test ( )

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

  jfrac_to_rfrac_test ( rng )

  josephus_test ( )

  ksub_next_test ( )
  ksub_next2_test ( )
  ksub_next3_test ( )
  ksub_next4_test ( )
  if ( False ):
    ksub_random_test ( rng )
  else:
    print ( "ksub_random_test skipped, ksub_random() is flawed." )
  ksub_random2_test ( rng )
  ksub_random3_test ( rng )
  ksub_random4_test ( rng )
  ksub_random5_test ( rng )
  ksub_rank_test ( )
  ksub_to_comp_test ( rng )
  ksub_to_compnz_test ( rng )
  ksub_unrank_test ( )

  l4vec_next_test ( )

  moebius_values_test ( )

  monomial_count_test ( )
  monomial_counts_test ( )

  morse_thue_test ( )

  multinomial_coef1_test ( )
  multinomial_coef2_test ( )

  multiperm_enum_test ( rng )
  multiperm_next_test ( )

  nim_sum_test ( rng )

  padovan_test ( )

  pell_basic_test ( )
  pell_next_test ( )
  pell_number_test ( )

  pent_enum_test ( )

  perm_ascend_test ( )
  perm_fixed_enum_test ( )

  perm0_break_count_test ( )
  perm0_check_test ( )
  perm0_cycle_test ( )
  perm0_distance_test ( rng )
  perm0_free_test ( )
  perm0_inverse_test ( )
  perm0_inverse2_test ( )
  perm0_inverse3_test ( )
  perm0_lex_next_test ( )
  perm0_mul_test ( rng )
  perm0_next_test ( )
  perm0_next3_test ( )
  perm0_print_test ( )
  perm0_random_test ( rng )
  perm0_random2_test ( rng )
  perm0_rank_test ( )
  perm0_sign_test ( )
  perm0_to_equiv_test ( )
  perm0_to_inversion_test ( )
  perm0_to_ytb_test ( )
  perm0_unrank_test ( )

  perm1_canon_to_cycle_test ( )
  perm1_check_test ( )
  perm1_cycle_max_test ( )
  perm1_cycle_stats_test ( rng )
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

  pythag_triple_ijk_test ( )
  pythag_triple_next_test ( )

  r8_agm_test ( )
  r8_choose_test ( )
  r8_fall_test ( )
  r8_fall_values_test ( )
  r8_rise_test ( )
  r8_rise_values_test ( )
  r8_to_cfrac_test ( )
  r8_to_dec_test ( rng )
  r8_to_rat_test ( rng )

  r8mat_det_test ( )
  r8mat_2perm0_test ( )
  r8mat_perm0_test ( )
  r8mat_permanent_test ( )

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
  r8vec_frac_test ( rng )
  r8vec_indicator1_test ( )
  r8vec_mirror_next_test ( )

  rat_add_test ( )
  rat_div_test ( )
  rat_farey_test ( )
  rat_farey2_test ( )
  rat_mul_test ( )
  rat_normalize_test ( )
  rat_to_cfrac_test ( )
  rat_to_dec_test ( rng )
  rat_to_r8_test ( rng )
  rat_to_s_test ( )
  rat_width_test ( )

  regro_next_test ( )

  rfrac_to_cfrac_test ( )
  rfrac_to_jfrac_test ( rng )

  schroeder_test ( )

  sort_heap_external_test ( rng )

  subcomp_next_test ( )

  subcompnz_next_test ( )
  subcompnz2_next_test ( )

  subset_by_size_next_test ( )
  subset_gray_next_test ( )
  subset_gray_rank_test ( )
  subset_gray_unrank_test ( )
  subset_lex_next_test ( )
  subset_random_test ( rng )

  subtriangle_next_test ( )

  thue_binary_next_test ( )
  thue_ternary_next_test ( )

  tuple_next_test ( )
  tuple_next2_test ( )
  tuple_next_fast_test ( )
  tuple_next_ge_test ( )

  triang_test ( )

  tuple_next_test ( )
  tuple_next2_test ( )

  ubvec_add_test ( rng )
  ubvec_print_test ( )
  ubvec_to_ui4_test ( )
  ubvec_xor_test ( rng )

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
  vector_sumlex_next_test ( )

  ytb_conjugate_test ( )
  ytb_enum_test ( )
  ytb_next_test ( )
  ytb_print_test ( )
  ytb_random_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'subset_test():' )
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    real A, B, the argument ofs the function.
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

def asm_enum ( n ):

#*****************************************************************************80
#
## asm_enum() returns the number of alternating sign matrices of a given order.
#
#  Discussion:
#
#    N     asm_nUM
#
#    0       1
#    1       1
#    2       2
#    3       7
#    4      42
#    5     429
#    6    7436
#    7  218348
#
#    A direct formula is
#
#      asm_num ( N ) = product ( 0 <= I <= N-1 ) ( 3 * I + 1 )! / ( N + I )!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2001
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#
#  Output:
#
#    integer VALUE, the number of alternating sign
#    matrices of order N.
#
  import numpy as np

  value = 0

  if ( n + 1 <= 0 ):
    return value
#
#  Row 1
#
  if ( n + 1 == 1 ):
    value = 1
    return value
#
#  Row 2
#
  if ( n + 1 == 2 ):
    value = 1
    return value

  a = np.zeros ( n + 1 )
  b = np.zeros ( n + 1 )
  c = np.zeros ( n + 1 )

  a[0] = 1
  a[1] = 1
  b[0] = 2
  c[0] = 2
#
#  Row 3 and on.
#
  for nn in range ( 3, n + 1 ):

    b[nn-2] = nn
    for i in range ( nn - 2, 1, -1 ):
      b[i-1] = b[i-1] + b[i-2]

    b[0] = 2

    c[nn-2] = 2
    for i in range ( nn - 2, 1, -1 ):
      c[i-1] = c[i-1] + c[i-2]

    c[0] = nn

    for i in range ( 1, nn - 1 ):
      a[0] = a[0] + a[i]

    for i in range ( 1, nn ):
      a[i] = a[i-1] * c[i-1] // b[i-1]
 
  value = 0
  for i in range ( 0, n ):
    value = value + a[i]

  return value

def asm_enum_test ( ):

#*****************************************************************************80
#
## asm_enum_test() tests asm_enum().
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
  n_max = 7

  print ( '' )
  print ( 'asm_enum_test():' )
  print ( '  asm_enum() returns the number of alternating sign' )
  print ( '  matrices of a given order.' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):
    value = asm_enum ( n )
    print ( '  %2d  %8d' % ( n, value ) )

  return

def asm_triangle ( n ):

#*****************************************************************************80
#
## asm_triangle() returns a row of the alternating sign matrix triangle.
#
#  Discussion:
#
#    The first seven rows of the triangle are as follows:
#
#          1      2      3      4      5      6     7
#
#    0     1
#    1     1      1
#    2     2      3      2
#    3     7     14     14      7
#    4    42    105    135    105     42
#    5   429   1287   2002   2002   1287    429
#    6  7436  26026  47320  56784  47320  26026  7436
#
#    For a given N, the value of A(J) represents entry A(I,J) of
#    the triangular matrix, and gives the number of alternating sign matrices
#    of order N in which the (unique) 1 in row 1 occurs in column J.
#
#    Thus, of alternating sign matrices of order 3, there are
#    2 with a leading 1 in column 1:
#
#      1 0 0  1 0 0
#      0 1 0  0 0 1
#      0 0 1  0 1 0
#
#    3 with a leading 1 in column 2, and
#
#      0 1 0  0 1 0  0 1 0
#      1 0 0  0 0 1  1-1 1
#      0 0 1  1 0 0  0 1 0
#
#    2 with a leading 1 in column 3:
#
#      0 0 1  0 0 1
#      1 0 0  0 1 0
#      0 1 0  1 0 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the desired row.
#
#  Output:
#
#    integer A(N+1), the entries of the row.
#
  import numpy as np

  a = np.zeros ( n + 1 )
  b = np.zeros ( n + 1 )
  c = np.zeros ( n + 1 )
#
#  Row 1
#
  a[0] = 1

  if ( n + 1 == 1 ):
    return a
#
#  Row 2
#
  nn = 2
  b[0] = 2
  c[0] = nn

  a[0] = np.sum ( a )
  for i in range ( 1, nn ):
    a[i] = a[i-1] * c[i-1] / b[i-1]

  if ( n + 1 == 2 ):
    return a
#
#  Row 3 and on.
#
  for nn in range ( 3, n + 2 ):

    b[nn-2] = nn
    for i in range ( nn - 3, 0, -1 ):
      b[i] = b[i] + b[i-1]
    b[0] = 2

    c[nn-2] = 2
    for i in range ( nn - 3, 0, -1 ):
      c[i] = c[i] + c[i-1]
    c[0] = nn

    a[0] = np.sum ( a )
    for i in range ( 1, nn ):
      a[i] = a[i-1] * c[i-1] / b[i-1]

  return a

def asm_triangle_test ( ):

#*****************************************************************************80
#
## asm_triangle_test() tests asm_triangle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2009
#
#  Author:
#
#    John Burkardt
#
  max_n = 7

  print ( '' )
  print ( 'asm_triangle_test():' )
  print ( '  asm_triangle() returns a row of the alternating sign' )
  print ( '  matrix triangle.' )
  print ( '' )

  for n  in range ( 0, max_n + 1 ):
    a = asm_triangle ( n )
    print ( '  %2d' % ( n ), end = '' )
    for i in range ( 0, n + 1 ):
      print ( '  %8d' % ( a[i] ), end = '' )
    print ( '' )

  return

def bell ( n ):

#*****************************************************************************80
#
## bell() returns the Bell numbers from 0 to N.
#
#  Discussion:
#
#    The Bell number B(N) is the number of restricted growth functions
#    on N.
#
#    Note that the Stirling numbers of the second kind, S^m_n, count the
#    number of partitions of N objects into M classes, and so it is
#    true that
#
#      B(N) = S^1_n + S^2_n + ... + S^N_n.
#
#  Definition:
#
#    The Bell number B(N) is defined as the number of partitions (of
#    any size) of a set of N distinguishable objects.
#
#    A partition of a set is a division of the objects of the set into
#    subsets.
#
#  Example:
#
#    There are 15 partitions of a set of 4 objects:
#
#      (1234), (123)(4), (124)(3), (12)(34), (12)(3)(4),
#      (134)(2), (13)(24), (13)(2)(4), (14)(23), (1)(234),
#      (1)(23)(4), (14)(2)(3), (1)(24)(3), (1)(2)(34), (1)(2)(3)(4)
#
#    and so B(4) = 15.
#
#  First values:
#
#     N         B(N)
#     0           1
#     1           1
#     2           2
#     3           5
#     4          15
#     5          52
#     6         203
#     7         877
#     8        4140
#     9       21147
#    10      115975
#
#  Recursion:
#
#    B(I) = sum ( 1 <= J <= I ) Binomial ( I-1, J-1 ) * B(I-J)
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
#    integer N, the number of Bell numbers desired.
#
#  Output:
#
#    integer B(1:N+1), the Bell numbers from 0 to N.
#
  import numpy as np

  b = np.zeros ( n + 1 )

  b[0] = 1

  for i in range ( 1, n + 1 ):
    b[i] = 0
    for j in range ( 1, i + 1 ):
      b[i] = b[i] + i4_choose ( i - 1, j - 1 ) * b[i-j]

  return b

def bell_test ( ):

#*****************************************************************************80
#
## bell_test() tests bell().
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
  print ( '' )
  print ( 'bell_test():' )
  print ( '  bell() computes Bell numbers.' )
  print ( '' )
  print ( '  N  exact C(I)  computed C(I)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = bell ( n )

    print ( '  %4d  %8d  %8d' % ( n, c, c2[n] ) )

  return

def bell_values ( n_data ):

#*****************************************************************************80
#
## bell_values() returns some values of the Bell numbers.
#
#  Discussion:
#
#    The Bell number B(N) is the number of restricted growth functions on N.
#
#    Note that the Stirling numbers of the second kind, S^m_n, count the
#    number of partitions of N objects into M classes, and so it is
#    true that
#
#      B(N) = S^1_n + S^2_n + ... + S^N_n.
#
#    The Bell numbers were named for Eric Temple Bell.
#
#    In Mathematica, the function can be evaluated by
#
#      Sum[StirlingS2[n,m],{m,1,n}]
#
#    The Bell number B(N) is defined as the number of partitions (of
#    any size) of a set of N distinguishable objects.  
#
#    A partition of a set is a division of the objects of the set into 
#    subsets.
#
#  Example:
#
#    There are 15 partitions of a set of 4 objects:
#
#      (1234), 
#      (123) (4), 
#      (124) (3), 
#      (12) (34), 
#      (12) (3) (4), 
#      (134) (2), 
#      (13) (24), 
#      (13) (2) (4), 
#      (14) (23), 
#      (1) (234),
#      (1) (23) (4), 
#      (14) (2) (3), 
#      (1) (24) (3), 
#      (1) (2) (34), 
#      (1) (2) (3) (4).
#
#    and so B(4) = 15.
#
#  First values:
#
#     N         B(N)
#     0           1
#     1           1
#     2           2
#     3           5
#     4          15
#     5          52
#     6         203
#     7         877
#     8        4140
#     9       21147
#    10      115975
#
#  Recursion:
#
#    B(I) = sum ( 1 <= J <=I ) Binomial ( I-1, J-1 ) * B(I-J)
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer N, the order of the Bell number.
#
#    integer C, the value of the Bell number.
#
  import numpy as np

  n_max = 11

  c_vec = np.array ( ( 1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975 ) )

  n_vec = np.array ( ( 0,  1,  2,  3,  4, 5,  6,  7,  8,  9,  10 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def bell_values_test ( ):

#*****************************************************************************80
#
## bell_values_test() tests bell_values().
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
  print ( '' )
  print ( 'bell_values_test():' )
  print ( '  bell_values() returns values of' )
  print ( '  the Bell numbers.' )
  print ( '' )
  print ( '     N        BELL(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %10d' % ( n, c ) )

  return

def catalan_number ( n ):

#*****************************************************************************80
#
## catalan_number() computes the N-th Catalan number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the Catalan number.
#
#  Output:
#
#    integer C: the value of the Catalan number.
#
  import numpy as np

  if ( n < 0 ):
    c = 0
    return c
 
  c = 1
#
#  The extra parentheses ensure that the integer division is
#  done AFTER the integer multiplication.
#
  for i in range ( 1, n + 1 ):
    c = ( c * 2 * ( 2 * i - 1 ) ) // ( i + 1 )

  return c

def catalan_number_test ( ):

#*****************************************************************************80
#
## catalan_number_test() tests catalan_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'catalan_number_test():' )
  print ( '  catalan_number() computes aCatalan number.' )
  print ( '' )
  print ( '  N     C(N)' )
  print ( '' )

  for n in range ( 0, 16 ):

    c = catalan_number ( n )

    print ( '  %4d  %9d' % ( n, c ) )

  return

def catalan_numbers ( n ):

#*****************************************************************************80
#
## catalan_numbers() computes the Catalan numbers, from C(0) to C(N).
#
#  First values:
#
#     C(0)     1
#     C(1)     1
#     C(2)     2
#     C(3)     5
#     C(4)    14
#     C(5)    42
#     C(6)   132
#     C(7)   429
#     C(8)  1430
#     C(9)  4862
#    C(10) 16796
#
#  Formula:
#
#    C(N) = (2*N)! / ( (N+1) * (N!) * (N!) )
#         = 1 / (N+1) * COMB ( 2N, N )
#         = 1 / (2N+1) * COMB ( 2N+1, N+1).
#
#  Recursion:
#
#    C(N) = 2 * (2*N-1) * C(N-1) / (N+1)
#    C(N) = sum ( 1 <= I <= N-1 ) C(I) * C(N-I)
#
#  Discussion:
#
#    The Catalan number C(N) counts:
#
#    1) the number of binary trees on N vertices;
#    2) the number of ordered trees on N+1 vertices;
#    3) the number of full binary trees on 2N+1 vertices;
#    4) the number of well formed sequences of 2N parentheses
#    5) number of ways 2N ballots can be counted, in order,
#       with N positive and N negative, so that the running sum
#       is never negative;
#    6) the number of standard tableaus in a 2 by N rectangular Ferrers diagram;
#    7) the number of monotone functions from [1..N} to [1..N} which
#       satisfy f(i) <= i for all i;
#    8) the number of ways to triangulate a polygon with N+2 vertices.
#
#  Example:
#
#    N = 3
#
#    ()()()
#    ()(())
#    (()())
#    (())()
#    ((()))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Input:
#
#    integer N, the number of Catalan numbers desired.
#
#  Output:
#
#    integer C(1:N+1), the Catalan numbers from C(0) to C(N).
#
  import numpy as np

  c = np.zeros ( n + 1 )

  c[0] = 1
#
#  The extra parentheses ensure that the integer division is
#  done AFTER the integer multiplication.
#
  for i in range ( 1, n + 1 ):
    c[i] = ( c[i-1] * 2 * ( 2 * i - 1 ) ) // ( i + 1 )

  return c

def catalan_numbers_test ( ):

#*****************************************************************************80
#
## catalan_numbers_test() tests catalan_numbers().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'catalan_numbers_test():' )
  print ( '  catalan_numbers() computes Catalan numbers.' )
  print ( '' )
  print ( '  N  exact C(I)  computed C(I)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = catalan_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = catalan_numbers ( n )

    print ( '  %4d  %6d  %6d' % ( n, c, c2[n] ) )

  return

def catalan_row_next ( ido, n, row_old ):

#*****************************************************************************80
#
## catalan_row_next() computes row N of Catalan's triangle.
#
#  Example:
#
#    I\J 0   1   2   3   4   5   6
#
#    0   1
#    1   1   1
#    2   1   2   2
#    3   1   3   5   5
#    4   1   4   9  14  14
#    5   1   5  14  28  42  42
#    6   1   6  20  48  90 132 132
#
#  Recursion:
#
#    C(0,0) = 1
#    C(I,0) = 1
#    C(I,J) = 0 for I < J
#    C(I,J) = C(I,J-1) + C(I-1,J)
#    C(I,I) is the I-th Catalan number.
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
#  Input:
#
#    integer IDO, indicates whether this is a call for
#    the 'next' row of the triangle.
#    IDO = 0, this is a startup call.  Row N is desired, but
#    presumably this is a first call, or row N-1 was not computed
#    on the previous call.
#    IDO = 1, this is not the first call, and row N-1 was computed
#    on the previous call.  In this case, much work can be saved
#    by using the information from the previous values of IROW
#    to build the next values.
#
#    integer N, the index of the row of the triangle desired.  
#
#    integer ROW_OLD(1:N), the row of coefficients.
#    If IDO = 0, then ROW_OLD is not required to be set on input.
#    If IDO = 1, then ROW_OLD must be set on input to the value of
#    row N-1.
#
#  Output:
#
#    integer ROW_nEW(1:N+1), the next row of coefficients.
#
  import numpy as np

  row_new = np.zeros ( n + 1 )

  if ( ido == 0 ):

    row_new[0] = 1
 
    for i in range ( 1, n + 1 ):

      im1 = i - 1
      row_new[0] = 1

      for j in range ( 0, im1 ):
        row_new[j+1] = row_new[j+1] + row_new[j]

      row_new[i] = row_new[i-1]
 
  else:
 
    for i in range ( 0, n ):
      row_new[i] = row_old[i]
    row_new[n] = 0

    row_new[0] = 1

    for j in range ( 0, n - 1 ):
      row_new[j+1] = row_new[j+1] + row_new[j]

    if ( 1 <= n ):
      row_new[n] = row_new[n-1]

  return row_new

def catalan_row_next_test ( ):

#*****************************************************************************80
#
## catalan_row_next_test() tests catalan_row_next().
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

  print ( '' )
  print ( 'catalan_row_next_test():' )
  print ( '  catalan_row_next() computes a row of Catalan\'s triangle.' )
  print ( '' )
  print ( '  First, compute row 7 from scratch.' )

  ido = 0
  i = 7
  c = np.zeros ( 0 )
  c = catalan_row_next ( ido, i, c )

  i4vec_transpose_print ( i + 1, c, '  Row 7:' )

  print ( '' )
  print ( '  Now compute rows one at a time:' )
  print ( '' )

  n = 10
  ido = 0
  c = np.zeros ( 0 )
  
  for i in range ( 0, n + 1 ):
    c = catalan_row_next ( ido, i, c )
    i4vec_transpose_print ( i + 1, c, '' )
    ido = 1

  return

def catalan_values ( n_data ):

#*****************************************************************************80
#
## catalan_values() returns some values of the Catalan numbers.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Binomial[2*n,n] / ( n + 1 )
#
#  First values:
#
#     C(0)     1
#     C(1)     1
#     C(2)     2
#     C(3)     5
#     C(4)    14
#     C(5)    42
#     C(6)   132
#     C(7)   429
#     C(8)  1430
#     C(9)  4862
#    C(10) 16796
#
#  Formula:
#
#    C(N) = (2*N)! / ( (N+1) * (N!) * (N!) ) 
#         = 1 / (N+1) * COMB ( 2N, N )
#         = 1 / (2N+1) * COMB ( 2N+1, N+1).
#
#  Recursion:
#
#    C(N) = 2 * (2*N-1) * C(N-1) / (N+1)
#    C(N) = sum ( 1 <= I <= N-1 ) C(I) * C(N-I)
#
#  Discussion:
#
#    The Catalan number C(N) counts:
#
#    1) the number of binary trees on N vertices;
#    2) the number of ordered trees on N+1 vertices;
#    3) the number of full binary trees on 2N+1 vertices;
#    4) the number of well formed sequences of 2N parentheses;
#    5) the number of ways 2N ballots can be counted, in order,
#       with N positive and N negative, so that the running sum
#       is never negative;
#    6) the number of standard tableaus in a 2 by N rectangular Ferrers diagram;
#    7) the number of monotone functions from [1..N} to [1..N} which 
#       satisfy f(i) <= i for all i;
#    8) the number of ways to triangulate a polygon with N+2 vertices.
#
#  Example:
#
#    N = 3
#
#    ()()()
#    ()(())
#    (()())
#    (())()
#    ((()))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2004
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer N, the order of the Catalan number.
#
#    integer C, the value of the Catalan number.
#
  import numpy as np

  n_max = 11

  c_vec = np.array ( ( 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796 ) )

  n_vec = np.array ( ( 0,  1,  2,  3,  4, 5,  6,  7,  8,  9,  10 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def catalan_values_test ( ):

#*****************************************************************************80
#
## catalan_values_test() tests catalan_values().
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
  print ( 'catalan_values_test():' )
  print ( '  catalan_values() returns values of the Catalan numbers.' )
  print ( '' )
  print ( '     N        C(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = catalan_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, c ) )

  return

def cfrac_to_rat ( n, a ):

#*****************************************************************************80
#
## cfrac_to_rat() converts a monic continued fraction to an ordinary fraction.
#
#  Discussion:
#
#    The routine is given the monic or "simple" continued fraction with
#    integer coefficients:
#
#      A(1) + 1 / ( A(2) + 1 / ( A(3) ... + 1 / A(N) ) )
#
#    and returns the N successive approximants P(I)/Q(I)
#    to the value of the rational number represented by the continued
#    fraction, with the value exactly equal to the final ratio P(N)/Q(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Input:
#
#    integer N, the number of continued fraction coefficients.
#
#    integer A(N), the continued fraction coefficients.
#
#  Output:
#
#    integer P(N), Q(N), the N successive approximations
#    to the value of the continued fraction.
#
  import numpy as np

  p = np.zeros ( n )
  q = np.zeros ( n )

  for i in range ( 0, n ):

    if ( i == 0 ):
      p[i] = a[i] * 1 + 0
      q[i] = a[i] * 0 + 1
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + 1
      q[i] = a[i] * q[i-1] + 0
    else:
      p[i] = a[i] * p[i-1] + p[i-2]
      q[i] = a[i] * q[i-1] + q[i-2]

  return p, q

def cfrac_to_rat_test ( ):

#*****************************************************************************80
#
## cfrac_to_rat_test() tests cfrac_to_rat().
#
#  Discussion:
#
#    Compute the continued fraction form of 4096/15625.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  m = 10

  print ( '' )
  print ( 'cfrac_to_rat_test():' )
  print ( '  cfrac_to_rat() continued fraction => fraction.' )
  print ( '' )

  top = 4096
  bot = 15625

  print ( '  Regular fraction is %6d / %6d' % ( top, bot ) )
 
  n, a = rat_to_cfrac ( top, bot )
 
  i4vec_print ( n, a, '  Continued fraction coefficients:' )

  p, q = cfrac_to_rat ( n, a )
 
  print ( '' )
  print ( '  The continued fraction convergents.' )
  print ( '  The last row contains the value of the continued' )
  print ( '  fraction, written as a common fraction.' )
  print ( '' )
  print ( '  I, P(I), Q(I), P(I)/Q(I)' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %3d  %6d  %6d  %14f' % ( i, p[i], q[i], p[i] / q[i] ) )

  return

def cfrac_to_rfrac ( m, g, h ):

#*****************************************************************************80
#
## cfrac_to_rfrac() converts a polynomial fraction from continued to rational form.
#
#  Discussion:
#
#    The routine accepts a continued polynomial fraction:
#
#      G(1)     / ( H(1) +
#      G(2) * X / ( H(2) +
#      G(3) * X / ( H(3) + ...
#      G(M) * X / ( H(M) )...) ) )
#
#    and returns the equivalent rational polynomial fraction:
#
#      P(1) + P(2) * X + ... + P(L1) * X^(L1)
#      -------------------------------------------------------
#      Q(1) + Q(2) * X + ... + Q(L2) * X^(L2-1)
#
#    where
#
#      L1 = (M+1)/2
#      L2 = (M+2)/2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Input:
#
#    integer M, the number of continued fraction polynomial coefficients.
#
#    real G(M), H(M), the continued polynomial fraction coefficients.
#
#  Output:
#
#    real P((M+1)/2), Q((M+2)/2), the rational polynomial fraction
#    coefficients.
#
  import numpy as np

  phi = ( m + 1 ) // 2
  qhi = ( m + 2 ) // 2

  p = np.zeros ( phi )
  q = np.zeros ( qhi )

  if ( m == 1 ):
    p[0] = g[0]
    q[0] = h[0]
    return p, q

  a = np.zeros ( [ m, qhi ] )
#
#  Solve for P's.
#
  a[0,0] = g[0]
  a[1,0] = g[0] * h[1]

  for i in range ( 3, m + 1 ):
    a[i-1,0] = h[i-1] * a[i-2,0]
    jhi = ( ( i + 1 ) // 2 )
    for j in range ( 2, jhi + 1 ):
      a[i-1,j-1] = h[i-1] * a[i-2,j-1] + g[i-1] * a[i-3,j-2]

  for j in range ( 1, phi + 1 ):
    p[j-1] = a[m-1,j-1]
#
#  Solve for Q's.
#
  a[0,0] = h[0]
  a[1,0] = h[0] * h[1]
  a[1,1] = g[1]

  for i in range ( 3, m + 1 ):
    a[i-1,0] = h[i-1] * a[i-2,0]
    jhi = ( ( i + 2 ) // 2 )
    for j in range ( 2, jhi + 1 ):
      a[i-1,j-1] = h[i-1] * a[i-2,j-1] + g[i-1] * a[i-3,j-2]

  for j in range ( 1, qhi + 1 ):
    q[j-1] = a[m-1,j-1]

  return p, q

def cfrac_to_rfrac_test ( ):

#*****************************************************************************80
#
## cfrac_to_rfrac_test() tests cfrac_to_rfrac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  maxm = 10
  m = 3

  p = np.array ( [ 1.0, 1.0, 2.0 ] )
  q = np.array ( [ 1.0, 3.0, 1.0, 1.0 ] )

  print ( '' )
  print ( 'cfrac_to_rfrac_test():' )
  print ( '  cfrac_to_rfrac(): continued fraction to rational polynomial fraction.' )

  r8vec_print ( m, p, '  Rational polynomial numerator coefficients:' )
  r8vec_print ( m + 1, q, '  Rational polynomial numerator coefficients:' )
 
  h = rfrac_to_cfrac ( m, p, q )
 
  r8vec_print ( 2 * m, h, '  Continued fraction coefficients:' )

  g = np.ones ( 2 * m )

  p2, q2 = cfrac_to_rfrac ( 2 * m, g, h )
 
  r8vec_print ( m, p2, '  Recovered rational polynomial numerator coefficients:' )
  r8vec_print ( m + 1, q2, '  Recovered rational polynomial numerator coefficients:' )

  return

def change_greedy ( total, coin_num, coin_value ):

#*****************************************************************************80
#
## change_greedy() makes change for a given total using the biggest coins first.
#
#  Discussion:
#
#    The algorithm is simply to use as many of the largest coin first,
#    then the next largest, and so on.
#
#    It is assumed that there is always a coin of value 1.  The
#    algorithm will otherwise fail!
#
#  Example:
#
#    Total = 17
#    COIN_nUM = 3
#    COIN_VALUE = (/ 1, 5, 10 /)
#
#
#    #  CHANGE              COIN_VALUE(CHANGE)
#
#    4  3 2 1 1             10 5 1 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TOTAL, the total for which change is to be made.
#
#    integer COIN_nUM, the number of types of coins.
#
#    integer COIN_VALUE(COIN_nUM), the value of each coin.
#    The values should be in ascending order, and if they are not,
#    they will be sorted.
#
#  Output:
#
#    integer change_nUM, the number of coins given in change.
#
#    integer CHANGE(TOTAL), the indices of the coins will be
#    in entries 1 through change_nUM.
#
  import numpy as np

  change_num = 0
  change = np.zeros ( total, dtype = np.int32 )
#
#  Find the largest coin smaller than the total.
#
  j = coin_num

  while ( 0 < j ):
    if ( coin_value[j-1] <= total ):
      break
    j = j - 1

  if ( j <= 0 ):
    return change_num, change
#
#  Subtract the current coin from the total.
#  Once that coin is too big, use the next coin.
#
  total_copy = total

  while ( 0 < total_copy ):

    if ( coin_value[j-1] <= total_copy ):

      total_copy = total_copy - coin_value[j-1]
      change_num = change_num + 1
      change[change_num-1] = j - 1

    else:

      j = j - 1
      if ( j <= 0 ):
        break

  return change_num, change

def change_greedy_test ( ):

#*****************************************************************************80
#
## change_greedy_test() tests change_greedy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  coin_num = 6
  coin_value = np.array ( [ 1, 5, 10, 25, 50, 100 ], dtype = np.int32 )

  print ( '' )
  print ( 'change_greedy_test():' )
  print ( '  change_greedy() makes change using the biggest coins first.' )

  total = 73

  print ( '' )
  print ( '  The total for which change is to be made: %d' % ( total ) )
  print ( '' )
  print ( '  The available coins are:' )
  print ( '' )
  for i in range ( 0, coin_num ):
    print ( '  %6d  %6d' % ( i, coin_value[i] ) )

  change_num, change = change_greedy ( total, coin_num, coin_value )

  print ( '' )
  print ( '  %4d: ' % (change_num ), end = '' )
  for i in range ( 0, change_num ):
    print ( '  %3d' % ( change[i] ), end = '' )
  print ( '' )

  total2 = 0
  for i in range ( 0, change_num ):
    total2 = total2 + coin_value[change[i]]
 
  print ( '  %4d: ' % ( total2 ), end = '' )
  for i in range ( 0, change_num ):
    print ( '  %3d' % ( coin_value[change[i]] ), end = '' )
  print ( '' )

  return

def change_next ( total, coin_num, coin_value, change_num, change, done  ):

#*****************************************************************************80
#
## change_next() computes the next set of change for a given sum.
#
#  Examples:
#
#    Total = 17
#    COIN_nUM = 3
#    COIN_VALUE = (/ 1, 5, 10 /)
#
#
#        #  CHANGE              COIN_VALUE(CHANGE)
#
#    1   4  3 2 1 1             10 5 1 1
#    2   8  3 1 1 1 1 1 1 1     10 1 1 1 1 1 1 1
#    3   5  2 2 2 1 1            5 5 5 1 1
#    4   9  2 2 1 1 1 1 1 1 1    5 5 1 1 1 1 1 1 1
#    5  13  2 1 1 1 1 1 1 1 1 1  5 1 1 1 1 1 1 1 1 1
#           1 1 1                1 1 1
#    6  17  1 1 1 1 1 1 1 1 1 1  1 1 1 1 1 1 1 1 1 1 1
#           1 1 1 1 1 1 1        1 1 1 1 1 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TOTAL, the total for which change is to be made.
#
#    integer COIN_nUM, the number of types of coins.
#
#    integer COIN_VALUE(COIN_nUM), the value of each coin.
#    The values should be in ascending order.
#
#    integer change_nUM, the output value of change_nUM from
#    the previous call.  This value is not needed on a startup call.
#
#    integer CHANGE(change_nUM), the output value of CHANGE from
#    the previous call.  This value is not needed on a startup call.
#
#    bool DONE.  The user sets DONE = TRUE on the
#    first call to tell the routine this is the beginning of a computation.
#    Thereafter, DONE should be set to the output value of DONE from]
#    the previous call.
#
#  Output:
#
#    integer change_nUM, the number of coins given in change
#    for the next set of change.
#
#    integer CHANGE(change_nUM), the indices of the coins
#    used in this set of change.
#
#    bool DONE, is FALSE until the last possible set of change
#    has been made.
#
  if ( done ):
#
#  Make sure the coin values are sorted.
#
    if ( not i4vec_ascends ( coin_num, coin_value ) ):
      print ( '' )
      print ( 'change_next()(): Fatal error!' )
      print ( '  The array COIN_VALUE is not in ascending order.' )
      raise Exception ( 'change_next(): Fatal error!' )
#
#  Start with the greedy change.
#
    change_num, change = change_greedy ( total, coin_num, coin_value )
#
#  In a few cases, like change for 4 cents, we're done after the first call.
#
    if ( change_num == total ):
      done = True
    else:
      done = False

    return change_num, change, done
#
#  Find the last location in the input change which is NOT a penny.
#
  else:

    last = -1

    for i in range ( change_num - 1, -1, -1 ):

      if ( change[i] != 0 ):
        last = i
        break
#
#  If that location is still 0, an error was made.
#
    if ( last == -1 ):
      done = True
      return change_num, change, done
#
#  Sum the entries from that point to the end.
#
    total2 = 0
    for i in range ( last, change_num ):
      total2 = total2 + coin_value[change[i]]
#
#  Make greedy change for the partial sum using coins smaller than that one.
#
    coin_num2 = change[last]

    change_num2, change2 = change_greedy ( total2, coin_num2, coin_value )

    for i in range ( 0, change_num2 ):
      change[last+i] = change2[i]

    change_num = last + change_num2

  return change_num, change, done

def change_next_test ( ):

#*****************************************************************************80
#
## change_next_test() tests change_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  coin_num = 6
  coin_value = np.array ( [ 1, 5, 10, 25, 50, 100 ] )

  print ( '' )
  print ( 'change_next_test():' )
  print ( '  change_next() displays the next possible way to make' )
  print ( '  change for a given total' )

  total = 50

  print ( '' )
  print ( '  The total for which change is to be made: %d' % ( total ) )
  print ( '' )
  print ( '  The available coins are:' )
  print ( '' )
  for i in range ( 0, coin_num ):
    print ( '  %6d' % ( coin_value[i] ) )

  i = 0
  change_num = 0
  change = np.zeros ( 0 )
  done = True

  print ( '' )

  while ( True ):

    change_num, change, done = change_next ( total, coin_num, coin_value, \
      change_num, change, done )

    if ( done or 9 < i ):
      break
 
    i = i + 1
    print ( '  %3d:' % ( i ), end = '' )
    for j in range ( 0, change_num ):
      print ( '  %3d' % ( coin_value[change[j]] ), end = '' )
    print ( '' )

  return

def chinese_check ( n, m ):

#*****************************************************************************80
#
## chinese_check() checks the Chinese remainder moduluses.
#
#  Discussion:
#
#    For a Chinese remainder representation, the moduluses M(I) must
#    be positive and pairwise prime.  Also, in case this is not obvious,
#    no more than one of the moduluses may be 1.
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
#  Input:
#
#    integer N, the number of moduluses.
#
#    integer M(N), the moduluses.  These should be positive
#    and pairwise prime.
#
#  Output:
#
#    integer IERROR, an error flag.
#    0, no error was detected.
#    nonzero, an error was detected.
#

#
#  Do not allow nonpositive entries.
#
  ierror = 0

  for i in range ( 0, n ):
    if ( m[i] <= 0 ):
      ierror = 1
      return ierror
#
#  Allow one entry to be 1, but not two entries.
#
  for i in range ( 0, n ):
    if ( m[i] == 1 ):
      for j in range ( i + 1, n ):
        if ( m[j] == 1 ):
          ierror = 2
          return ierror
#
#  Now check pairwise primeness.
#
  if ( not i4vec_pairwise_prime ( n, m ) ):
    ierror = 3
    return ierror

  return ierror

def chinese_check_test ( ):

#*****************************************************************************80
#
## chinese_check_test() tests chinese_check().
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

  n = 4
  m1 = np.array ( [ 1, 3,  8, 25 ] )
  m2 = np.array ( [ 1, 3, -8, 25 ] )
  m3 = np.array ( [ 1, 3,  1, 25 ] )
  m4 = np.array ( [ 1, 3,  8, 24 ] )

  print ( '' )
  print ( 'chinese_check_test():' )
  print ( '  chinese_check() checks a set of moduluses for use with' )
  print ( '  the Chinese Remainder representation.' )

  i4vec_print ( n, m1, '  Modulus set #1:' )
  ierror = chinese_check ( n, m1 )
  print ( '  IERROR = %d' % ( ierror ) )

  i4vec_print ( n, m2, '  Modulus set #2:' )
  ierror = chinese_check ( n, m2 )
  print ( '  IERROR = %d' % ( ierror ) )

  i4vec_print ( n, m3, '  Modulus set #3:' )
  ierror = chinese_check ( n, m3 )
  print ( '  IERROR = %d' % ( ierror ) )

  i4vec_print ( n, m4, '  Modulus set #4:' )
  ierror = chinese_check ( n, m4 )
  print ( '  IERROR = %d' % ( ierror ) )

  return

def chinese_to_i4 ( n, m, r ):

#*****************************************************************************80
#
## chinese_to_i4() converts a set of Chinese remainders to an equivalent integer.
#
#  Discussion:
#
#    Given a set of N pairwise prime, positive moduluses M(I), and
#    a corresponding set of remainders R(I), this routine finds an
#    integer J such that, for all I,
#
#      J = R(I) mod M(I)
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
#  Input:
#
#    integer N, the number of moduluses.
#
#    integer M(N), the moduluses.  These should be positive
#    and pairwise prime.
#
#    integer R(N), the Chinese remainder representation of the integer.
#
#  Output:
#
#    integer J, the corresponding integer.
#
  import numpy as np

  ierror = chinese_check ( n, m )

  if ( ierror != 0 ):
    print ( '' )
    print ( 'chinese_to_i4()(): Fatal error!' )
    print ( '  The moduluses are not legal.' )
    raise Exception ( 'chinese_to_i4(): Fatal error!' )
#
#  Set BIG_M.
#
  big_m = i4vec_product ( n, m )
#
#  Solve BIG_M / M(I) * B(I) = 1, mod M(I)
#
  b = np.zeros ( n )

  for i in range ( 0, n ):
    a = big_m // m[i]
    c = 1
    b[i], ierror = congruence ( a, m[i], c )
#
#  Set J = sum ( 1 <= I <= N ) ( R(I) * B(I) * BIG_M / M(I) ) mod M
#
  j = 0
  for i in range ( 0, n ):
    j = ( ( j + r[i] * b[i] * ( big_m // m[i] ) ) % big_m )

  return j

def chinese_to_i4_test ( ):

#*****************************************************************************80
#
## chinese_to_i4_test() tests chinese_to_i4().
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

  n = 4
  m = np.array ( [ 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'chinese_to_i4_test():' )
  print ( '  chinese_to_i4() computes an integer with the given' )
  print ( '  Chinese Remainder representation.' )

  i4vec_print ( n, m, '  The moduli:' )

  j = 37

  print ( '' )
  print ( '  The number being analyzed is %d' % ( j ) )

  r = i4_to_chinese ( j, n, m )

  i4vec_print ( n, r, '  The remainders:' )

  j2 = chinese_to_i4 ( n, m, r )

  print ( '' )
  print ( '  The reconstructed number is %d' % ( j2 ) )

  r = i4_to_chinese ( j2, n, m )

  i4vec_print ( n, r, '  The remainders of the reconstructed number:' )

  return

def ch_to_digit ( c ):

#*****************************************************************************80
#
## ch_to_digit() returns the integer value of a base 10 digit.
#
#  Example:
#
#     C   DIGIT
#    ---  -----
#    '0'    0
#    '1'    1
#    ...  ...
#    '9'    9
#    ' '    0
#    'X'   -1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C, the decimal digit, '0' through '9' or blank
#    are legal.
#
#  Output:
#
#    integer DIGIT, the corresponding integer value.  If C was
#    'illegal', then DIGIT is -1.
#
  i0 = ord ( '0' )
  i9 = ord ( '9' )
  ic = ord ( c )

  if ( i0 <= ic and ic <= i9 ):

    digit = ic - i0

  elif ( c == ' ' ):

    digit = 0

  else:

    digit = -1

  return digit

def ch_to_digit_test ( ):

#*****************************************************************************80
#
## ch_to_digit_test() tests ch_to_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ch_to_digit_test():' )
  print ( '  ch_to_digit(): character -> decimal digit' )
  print ( '' )
 
  for i in range ( -2, 12 ):
    c = digit_to_ch ( i )
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )

  return

def comb_next ( n, k, a, done ):

#*****************************************************************************80
#
## comb_next() computes combinations of K things out of N.
#
#  Discussion:
#
#    The combinations are computed one at a time, in lexicographical order.
#
#    10 April 2009: Thanks to "edA-qa mort-ora-y" for supplying a
#    correction to this code.
#
#    25 June 2025: Correction for the case k=0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Mifsud,
#    Combination in Lexicographic Order,
#    ACM algorithm 154,
#    Communications of the ACM,
#    March 1963.
#
#  Input:
#
#    integer N, the total number of things.
#
#    integer K, the number of things in each combination.
#
#    integer A(K), the output value of A on the previous call.
#    This value is not needed on a startup call.
#
#    bool DONE, should be set to TRUE (1) on the first call,
#    and thereafter set to the output value of DONE on the previous call.
#
#  Output:
#
#    integer A(K), the next combination.
#
#    bool DONE, is FALSE (0) if the routine can be called
#    again for more combinations, and TRUE (1) if there are no more.
#
  if ( k < 0 ):
    a = []
    done = True
    return a, done
  
  if ( k == 0 ):
    if ( done ):
      a = []
      done = False
    else:
      done = True
    return a, done

  if ( done ):

    a = i4vec_indicator1 ( k )
    done = False

  else:

    done = True
    km1 = k - 1

    if ( a[km1] < n ):

      a[km1] = a[km1] + 1
      done = False

    else:

      for i in range ( k, 1, -1 ):

        if ( a[i-2] < n-k+i-1 ):

          a[i-2] = a[i-2] + 1

          for j in range (  i, k + 1 ):
            a[j-1] = a[i-2] + j - ( i - 1 )
          done = False

          break

  return a, done

def comb_next_test ( ):

#*****************************************************************************80
#
## comb_next_test() tests comb_next().
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

  n = 5

  print ( '' )
  print ( 'comb_next_test():' )
  print ( '  comb_next() produces combinations.' )
  print ( '  We are selecting from a set of size %d' % ( n ) )

  for k in range ( 1, n + 1 ):

    print ( '' )
    print ( '  Combinations of size %d:' % ( k ) )
    print ( '' )

    a = np.zeros ( k )
    done = True

    while ( True ):

      a, done = comb_next ( n, k, a, done )
 
      if ( done ):
        break

      i4vec_transpose_print ( k, a, '' )

  return

def comb_row_next ( n, row ):

#*****************************************************************************80
#
## comb_row_next() computes the next row of Pascal's triangle.
#
#  Discussion:
#
#    Row N contains the combinatorial coefficients
#
#      C(N,0), C(N,1), C(N,2), ... C(N,N)
#
#  Discussion:
#
#    The sum of the elements of row N is equal to 2^N.
#
#  Formula:
#
#    C(N,K) = N! / ( K! * (N-K)! )
#
#  First terms:
#
#     N K:0  1   2   3   4   5   6   7  8  9 10
#
#     0   1
#     1   1  1
#     2   1  2   1
#     3   1  3   3   1
#     4   1  4   6   4   1
#     5   1  5  10  10   5   1
#     6   1  6  15  20  15   6   1
#     7   1  7  21  35  35  21   7   1
#     8   1  8  28  56  70  56  28   8  1
#     9   1  9  36  84 126 126  84  36  9  1
#    10   1 10  45 120 210 252 210 120 45 10  1
#
#  Recursion:
#
#    C(N,K) = C(N-1,K-1)+C(N-1,K)
#
#  Special values:
#
#    C(N,0) = C(N,N) = 1
#    C(N,1) = C(N,N-1) = N
#    C(N,N-2) = sum ( 1 <= I <= N ) N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the row of the triangle desired.  The triangle
#    begins with row N = 0.
#
#    integer ROW(N), row N-1 of the triangle.
#
#  Output:
#
#    integer ROW2(N+1), row N.
#
  import numpy as np

  row2 = np.zeros ( n + 1 )

  row2[n] = 1
  for i in range ( n - 1, 0, - 1 ):
    row2[i] = row[i] + row[i-1]
  row2[0] = 1

  return row2

def comb_row_next_test ( ):

#*****************************************************************************80
#
## comb_row_next()_test tests comb_row_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  n_max = 10

  print ( '' )
  print ( 'comb_row_next_test():' )
  print ( '  comb_row_next() computes a row of Pascal\'s triangle.' )
  print ( '' )
  
  c = []

  for n in range ( 0, n_max + 1 ):
    c = comb_row_next ( n, c )
    print ( '  %2d' % ( n ), end = '' )
    for j in range ( 0, n + 1 ):
      print ( ' %4d' % ( c[j] ), end = '' )
    print ( '' )

  return

def comb_unrank ( m, n, rank ):

#*****************************************************************************80
#
## comb_unrank() returns the RANK-th combination of N things out of M.
#
#  Discussion:
#
#    Going from a rank to a thing is called "unranking".
#
#    The combinations are ordered lexically.
#
#    Lexical order can be illustrated for the general case of N and M as
#    follows:
#
#    1:       1,     2,     3,     ..., N-2, N-1, N
#    2:       1,     2,     3,     ..., N-2, N-1, N+1
#    3:       1,     2,     3,     ..., N-2, N-1, N+2
#    ...
#    M-N+1:   1,     2,     3,     ..., N-2, N-1, M
#    M-N+2:   1,     2,     3,     ..., N-2, N,   N+1
#    M-N+3:   1,     2,     3,     ..., N-2, N,   N+2
#    ...
#    LAST-2:  M-N,   M-N+1, M-N+3, ..., M-2, M-1, M
#    LAST-1:  M-N,   M-N+2, M-N+3, ..., M-2, M-1, M
#    LAST:    M-N+1, M-N+2, M-N+3, ..., M-2, M-1, M
#
#    There are a total of M!/(N!*(M-N)!) combinations of M
#    things taken N at a time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    B P Buckles, M Lybanon,
#    Algorithm 515,
#    Generation of a Vector from the Lexicographical Index,
#    ACM Transactions on Mathematical Software,
#    Volume 3, Number 2, pages 180-182, June 1977.
#
#  Input:
#
#    integer M, the size of the set.
#
#    integer N, the number of things in the combination.
#    N must be greater than 0, and no greater than M.
#
#    integer RANK, the lexicographical rank of the combination
#    sought.  RANK must be at least 1, and no greater than M!/(N!*(M-N)!).
#
#  Output:
#
#    integer A(N), the combination.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )
#
#  Initialize the lower bound index.
#
  k = 0
#
#  Select elements in ascending order.
#
  for i in range ( 0, n - 1 ):
#
#  Set the lower bound element number for next element value.
#
    a[i] = 0

    if ( 0 < i ):
      a[i] = a[i-1]
#
#  Check each element value.
#
    while ( True ):

      a[i] = a[i] + 1
      j = i4_choose ( m - a[i], n - i - 1 )
      k = k + j

      if ( rank <= k ):
        break

    k = k - j;

  a[n-1] = a[n-2] + rank - k

  return a

def comb_unrank_test ( ):

#*****************************************************************************80
#
## comb_unrank_test() tests comb_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  m = 10
  cnk = i4_choose ( m, n )

  print ( '' )
  print ( 'comb_unrank_test():' )
  print ( '  comb_unrank() returns a combination of N things' )
  print ( '  out of M, given the lexicographic rank.' )
  print ( '' )
  print ( '  The total set size is M = %d' % ( m ) )
  print ( '  The subset size is N =    %d' % ( n ) )
  print ( '  The number of combinations of N out of M is %d' % ( cnk ) )
  print ( '' )
  print ( '   Rank	  Combination' )
  print ( '' )
 
  for rank in range ( 1, 4 ):
    a = comb_unrank ( m, n, rank )
    print ( '  %3d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %5d' % ( a[i] ), end = '' )
    print ( '' )
 
  for rank in range ( 6, 9 ):
    a = comb_unrank ( m, n, rank )
    print ( '  %3d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %5d' % ( a[i] ), end = '' )
    print ( '' )
 
  for rank in range ( 250, 253 ):
    a = comb_unrank ( m, n, rank )
    print ( '  %3d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %5d' % ( a[i] ), end = '' )
    print ( '' )

  return

def comp_enum ( n, k ):

#*****************************************************************************80
#
## comp_enum() returns the number of compositions of the integer N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The 28 compositions of 6 into three parts are:
#
#      6 0 0,  5 1 0,  5 0 1,  4 2 0,  4 1 1,  4 0 2,
#      3 3 0,  3 2 1,  3 1 2,  3 0 3,  2 4 0,  2 3 1,
#      2 2 2,  2 1 3,  2 0 4,  1 5 0,  1 4 1,  1 3 2,
#      1 2 3,  1 1 4,  1 0 5,  0 6 0,  0 5 1,  0 4 2,
#      0 3 3,  0 2 4,  0 1 5,  0 0 6.
#
#    The formula for the number of compositions of N into K parts is
#
#      Number = ( N + K - 1 )! / ( N! * ( K - 1 )! )
#
#    Describe the composition using N '1's and K-1 dividing lines '|'.
#    The number of distinct permutations of these symbols is the number
#    of compositions.  This is equal to the number of permutations of
#    N+K-1 things, with N identical of one kind and K-1 identical of another.
#
#    Thus, for the above example, we have:
#
#      Number = ( 6 + 3 - 1 )! / ( 6! * (3-1)! ) = 28
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the integer whose compositions are desired.
#
#    integer K, the number of parts in the composition.
#
#  Output:
#
#    integer VALUE, the number of compositions of N into K parts.
#
  value = i4_choose ( n + k - 1, n )

  return value

def comp_enum_test ( ):

#*****************************************************************************80
#
## comp_enum_test() tests comp_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'comp_enum_test():' )
  print ( '  comp_enum() counts compositions.' )

  print ( '' )
  for n in range ( 0, 11 ):
    for k in range ( 1, 11 ):
      num = comp_enum ( n, k )
      print ( '  %6d' % ( num ), end = '' )
    print ( '' )

  return

def comp_next_grlex ( kc, xc ):

#*****************************************************************************80
#
## comp_next_grlex() returns the next composition in grlex order.
#
#  Discussion:
#
#    Example:
#
#    KC = 3
#
#    #   XC(1) XC(2) XC(3)  Degree
#      +------------------------
#    1 |  0     0     0        0
#      |
#    2 |  0     0     1        1
#    3 |  0     1     0        1
#    4 |  1     0     0        1
#      |
#    5 |  0     0     2        2
#    6 |  0     1     1        2
#    7 |  0     2     0        2
#    8 |  1     0     1        2
#    9 |  1     1     0        2
#   10 |  2     0     0        2
#      |
#   11 |  0     0     3        3
#   12 |  0     1     2        3
#   13 |  0     2     1        3
#   14 |  0     3     0        3
#   15 |  1     0     2        3
#   16 |  1     1     1        3
#   17 |  1     2     0        3
#   18 |  2     0     1        3
#   19 |  2     1     0        3
#   20 |  3     0     0        3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int KC, the number of parts of the composition.
#    1 <= KC.
#
#    int XC[KC], the current composition.
#    Each entry of XC must be nonnegative.
#
#  Output:
#
#    int XC[KC], the next composition.
#

#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_next_grlex(): Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_next_grlex(): Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ( '' )
      print ( 'comp_next_grlex(): Fatal error!' )
      print ( '  XC[I] < 0' )
      raise Exception ( 'comp_next_grlex(): Fatal error!' )
#
#  Find I, the index of the rightmost nonzero entry of X.
#
  i = 0
  for j in range ( kc, 0, -1 ):
    if ( 0 < xc[j-1] ):
      i = j
      break
#
#  set T = X(I)
#  set XC(I) to zero,
#  increase XC(I-1) by 1,
#  increment XC(KC) by T-1.
#
  if ( i == 0 ):
    xc[kc-1] = 1
    return xc
  elif ( i == 1 ):
    t = xc[0] + 1
    im1 = kc
  elif ( 1 < i ):
    t = xc[i-1]
    im1 = i - 1

  xc[i-1] = 0
  xc[im1-1] = xc[im1-1] + 1
  xc[kc-1] = xc[kc-1] + t - 1

  return xc

def comp_next_grlex_test ( ):

#*****************************************************************************80
#
## comp_next_grlex_test() tests comp_next_grlex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  kc = 3

  print ( '' )
  print ( 'comp_next_grlex_test():' )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  comp_next_grlex() determines the next COMP in' )
  print ( '  graded lexicographic (grlex) order.' )
  
  xc = np.zeros ( kc, dtype = np.int32 )

  print ( '' )
  print ( '  Rank:     NC       COMP' )
  print ( '  ----:     --   ------------' )

  for rank in range ( 1, 72 ):
    if ( rank == 1 ):
      for j in range ( 0, kc ):
        xc[j] = 0
    else:
      xc = comp_next_grlex ( kc, xc )

    nc = np.sum ( xc )

    print ( '   %3d: ' % ( rank ), end = '' )
    print ( '    %2d = ' % ( nc ), end = '' )
    for j in range ( 0, kc - 1 ):
      print ( '%2d + ' % ( xc[j] ), end = '' )
    print ( '%2d' % ( xc[kc-1] ) )
#
#  When XC(1) == NC, we have completed the compositions associated with
#  a particular integer, and are about to advance to the next integer.
#
    if ( xc[0] == nc ):
      print ( '  ----:     --   ------------' )

  return

def comp_next ( n, k, a, more, h, t ):

#*****************************************************************************80
#
## comp_next() computes the compositions of the integer N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The routine computes one composition on each call until there are no more.
#    For instance, one composition of 6 into 3 parts is
#    3+2+1, another would be 6+0+0.
#
#    On the first call to this routine, set MORE = FALSE.  The routine
#    will compute the first element in the sequence of compositions, and
#    return it, as well as setting MORE = TRUE.  If more compositions
#    are desired, call again, and again.  Each time, the routine will
#    return with a new composition.
#
#    However, when the LAST composition in the sequence is computed 
#    and returned, the routine will reset MORE to FALSE, signaling that
#    the end of the sequence has been reached.
#
#    This routine originally used a SAVE statement to maintain the
#    variables H and T.  I have decided that it is safer
#    to pass these variables as arguments, even though the user should
#    never alter them.  This allows this routine to safely shuffle
#    between several ongoing calculations.
#
#    There are 28 compositions of 6 into three parts.  This routine will
#    produce those compositions in the following order:
#
#     I         A
#     -     ---------
#     1     6   0   0
#     2     5   1   0
#     3     4   2   0
#     4     3   3   0
#     5     2   4   0
#     6     1   5   0
#     7     0   6   0
#     8     5   0   1
#     9     4   1   1
#    10     3   2   1
#    11     2   3   1
#    12     1   4   1
#    13     0   5   1
#    14     4   0   2
#    15     3   1   2
#    16     2   2   2
#    17     1   3   2
#    18     0   4   2
#    19     3   0   3
#    20     2   1   3
#    21     1   2   3
#    22     0   3   3
#    23     2   0   4
#    24     1   1   4
#    25     0   2   4
#    26     1   0   5
#    27     0   1   5
#    28     0   0   6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the integer whose compositions are desired.
#
#    integer K, the number of parts in the composition.
#
#    integer A(K), the previous composition.  On the first call,
#    with MORE = FALSE, set A = [].  Thereafter, A should be the 
#    value of A output from the previous call.
#
#    bool MORE.  The input value of MORE on the first
#    call should be FALSE, which tells the program to initialize.
#    On subsequent calls, MORE should be TRUE, or simply the
#    output value of MORE from the previous call.
#
#    integer H, T, two internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the next composition.
#
#    bool MORE, will be TRUE unless the composition 
#    that is being returned is the final one in the sequence.
#
#    integer H, T, the updated values of the two internal 
#    variables.
#
  if ( not more ):

    t = n
    h = 0
    a[0] = n
    for i in range ( 1, k ):
      a[i] = 0

  else:
      
    if ( 1 < t ):
      h = 0

    t = a[h]
    a[h] = 0
    a[0] = t - 1
    a[h+1] = a[h+1] + 1
    h = h + 1

  more = ( a[k-1] != n )

  return a, more, h, t

def comp_next_test ( ):

#*****************************************************************************80
#
## comp_next_test() tests comp_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'comp_next_test():' )
  print ( '  comp_next() generates compositions.' )
  print ( '' )

  n = 6
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0

  print ( '  Seeking all compositions of N = %d' % ( n ) )
  print ( '  using %d parts.' % ( k ) )
  print ( '' )

  while ( True ):

    a, more, h, t = comp_next ( n, k, a, more, h, t )
    
    print ( '  ', end = '' )
    for i in range ( 0, k ):
      print ( '%2d  ' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def compnz_enum ( n, k ):

#*****************************************************************************80
#
## compnz_enum() returns the number of nonzero compositions of the N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K nonzero parts is an ordered sequence
#    of K positive integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The 10 compositions of 6 into three nonzero parts are:
#
#      4 1 1,  3 2 1,  3 1 2,  2 3 1,  2 2 2,  2 1 3,
#      1 4 1,  1 3 2,  1 2 3,  1 1 4.
#
#    The formula for the number of compositions of N into K nonzero
#    parts is
#
#      Number = ( N - 1 )! / ( ( N - K )! * ( K - 1 )! )
#
#    (Describe the composition using N-K '1's and K-1 dividing lines '|'.
#    The number of distinct permutations of these symbols is the number
#    of compositions into nonzero parts.  This is equal to the number of
#    permutations of  N-1 things, with N-K identical of one kind
#    and K-1 identical of another.)
#
#    Thus, for the above example, we have:
#
#      Number = ( 6 - 1 )! / ( ( 6 - 3 )! * ( 3 - 1 )! ) = 10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the integer whose compositions are desired.
#
#    integer K, the number of parts in the composition.
#
#  Output:
#
#    integer VALUE, the number of compositions of N into K nonzero parts.
#
  value = i4_choose ( n - 1, n - k )

  return value

def compnz_enum_test ( ):

#*****************************************************************************80
#
## compnz_enum_test() tests compnz_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  n_max = 7

  print ( '' )
  print ( 'compnz_enum_test():' )
  print ( '  compnz_enum() returns the number of nonzero compositions' )
  print ( '  of N into K parts.' )
  print ( '' )
  print ( '   N\K ', end = '' )
  for k in range ( 0, n_max + 1 ):
    print ( '  %4d' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, n_max + 1 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      value = compnz_enum ( n, k )
      print ( '  %4d' % ( value ), end = '' )
    print ( '' )

  return

def compnz_next ( n, k, a, more, h, t ):

#*****************************************************************************80
#
## compnz_next() computes the compositions of the integer N into K nonzero parts.
#
#  Discussion:
#
#    A composition of the integer N into K nonzero parts is an ordered sequence
#    of K positive integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The routine computes one composition on each call until there are no more.
#    For instance, one composition of 6 into 3 parts is 3+2+1, another would
#    be 4+1+1 but 5+1+0 is not allowed since it includes a zero part.
#
#    On the first call to this routine, set MORE = FALSE.  The routine
#    will compute the first element in the sequence of compositions, and
#    return it, as well as setting MORE = TRUE.  If more compositions
#    are desired, call again, and again.  Each time, the routine will
#    return with a new composition.
#
#    However, when the LAST composition in the sequence is computed
#    and returned, the routine will reset MORE to FALSE, signaling that
#    the end of the sequence has been reached.
#
#  Example:
#
#    The 10 compositions of 6 into three nonzero parts are:
#
#      4 1 1,  3 2 1,  3 1 2,  2 3 1,  2 2 2,  2 1 3,
#      1 4 1,  1 3 2,  1 2 3,  1 1 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis and Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the integer whose compositions are desired.
#
#    integer K, the number of parts in the composition.
#    K must be no greater than N.
#
#    integer A(K), the previous composition.  On the first call,
#    with MORE = FALSE, set A = [].  Thereafter, A should be the 
#    value of A output from the previous call.
#
#    bool MORE.  The input value of MORE on the first
#    call should be FALSE, which tells the program to initialize.
#    On subsequent calls, MORE should be TRUE, or simply the
#    output value of MORE from the previous call.
#
#    integer H, T, internal variables.  The user should set these
#    to 0 before the first call, and on subsequent calls pass in the previous
#    output values.
#
#  Output:
#
#    integer A(K), the next composition.
#
#    bool MORE, will be TRUE unless the composition 
#    that is being returned is the final one in the sequence.
#
#    integer H, T, updated internal variables.
#

#
#  We use the trick of computing ordinary compositions of (N-K)
#  into K parts, and adding 1 to each part.
#
  if ( n < k ):
    more = False
    for i in range ( 0, k ):
      a[i] = -1
    return a, more, h, t

  if ( not more ):

    t = n - k
    h = 0
    a[0] = n - k
    for i in range ( 1, k ):
      a[i] = 0

  else:

    for i in range ( 0, k ):
      a[i] = a[i] - 1

    if ( 1 < t ):
      h = 0

    h = h + 1
    t = a[h-1]
    a[h-1] = 0
    a[0] = t - 1
    a[h] = a[h] + 1

  more = ( a[k-1] != ( n - k ) )

  for i in range ( 0, k ):
    a[i] = a[i] + 1

  return a, more, h, t

def compnz_next_test ( ):

#*****************************************************************************80
#
## compnz_next_test() tests compnz_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'compnz_next_test():' )
  print ( '  compnz_next() generates compositions' )
  print ( '  with nonzero parts.' )
  print ( '' )

  n = 6
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0

  print ( '  Seeking all compositions of N = %d' % ( n ) )
  print ( '  using %d nonzero parts.' % ( k ) )
  print ( '' )

  while ( True ):

    a, more, h, t = compnz_next ( n, k, a, more, h, t )
    
    print ( '  ', end = '' )
    for i in range ( 0, k ):
      print ( '%2d  ' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def compnz_random ( n, k, rng ):

#*****************************************************************************80
#
## compnz_random() selects a random composition of the integer N into K nonzero parts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis and Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the integer to be decomposed.
#
#    integer K, the number of parts in the composition.
#    K must be no greater than N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K), the parts of the composition.
#
  import numpy as np

  a = np.zeros ( k, dtype = np.int32 )

  if ( 1 < n and 1 < k ):
    b = ksub_random2 ( n - 1, k - 1, rng )

  for i in range ( 0, k - 1 ):
    a[i] = b[i]

  a[k-1] = n
  l = 0

  for i in range ( 0, k ):
    m = a[i]
    a[i] = a[i] - l - 1
    l = m

  for i in range ( 0, k ):
    a[i] = a[i] + 1

  return a

def compnz_random_test ( rng ):

#*****************************************************************************80
#
## compnz_random_test() tests compnz_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  k = 5
  n = 10

  print ( '' )
  print ( 'compnz_random_test():' )
  print ( '  compnz_random() generates random compositions' )
  print ( '  using nonzero parts.' )
  print ( '' )
  print ( '  Seeking random compositions of N = ', n )
  print ( '  using ', k, ' nonzero parts.' )
  print ( '' )

  for i in range ( 0, 5 ):
    a = compnz_random ( n, k, rng )
    for j in range ( 0, k ):
      print ( '  %2d' % ( a[j] ), end = '' )
    print ( '' )

  return

def compnz_to_ksub ( nc, kc, ac ):

#*****************************************************************************80
#
## compnz_to_ksub() converts a (nonzero) composition to a K-subset.
#
#  Discussion:
#
#    There is a bijection between K subsets and nonzero compositions.
#
#    Let AC be a nonzero composition of NC into KC parts.
#
#    Then let
#      NS = NC - 1
#      KS = KC - 1
#    and define
#      AS(I) = sum ( AC(1:I) ), for I = 1 : KS.
#      
#    Then AS is a KS subset of the integers 1 through NS.
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
#    integer NC, the composition sum.
#
#    integer KC, the number of parts of the composition.
#
#    integer AC(KC), the parts of the composition.
#
#  Output:
#
#    integer NS, the size of the set.
#
#    integer KS, the size of the subset.
#
#    integer BS(KS), the entries of the K-subset, in increasing order.
#
  import numpy as np

  ns = nc - 1
  ks = kc - 1
  bs = np.zeros ( ks )
  t = 0
  for i in range ( 0, ks ):
    t = t + ac[i]
    bs[i] = t

  return ns, ks, bs

def compnz_to_ksub_test ( rng ):

#*****************************************************************************80
#
## compnz_to_ksub_test() tests compnz_to_ksub().
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
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'compnz_to_ksub_test():' )
  print ( '  compnz_to_ksub() returns the K subset corresponding' )
  print ( '  to a nonzero composition.' )

  nc = 10
  kc = 5

  print ( '' )
  print ( '  The composition sums to %d' % ( nc ) )
  print ( '  and contains %d parts.' % ( kc ) )

  for i in range ( 0, 5 ):

    print ( '' )

    ac = compnz_random ( nc, kc, rng )
   
    print ( '  COMPNZ:', end = '' )
    for j in range ( 0, kc ):
      print ( '  %2d' % ( ac[j] ), end = '' )
    print ( '' )

    ns, ks, bs = compnz_to_ksub ( nc, kc, ac )
    print ( '  KSUB:  ', end = '' )
    for j in range ( 0, ks ):
      print ( '  %2d' % ( bs[j] ), end = '' )
    print ( '' )

  return

def comp_random_grlex ( kc, rank1, rank2, rng ):

#*****************************************************************************80
#
## comp_random_grlex(): random composition with degree less than or equal to NC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int KC, the number of parts in the composition.
#
#    int RANK1, RANK2, the minimum and maximum ranks.
#    1 <= RANK1 <= RANK2.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    int X[KC], the random composition.
#
#    int RANK, the rank of the composition.
#
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_random_grlex(): Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_random_grlex(): Fatal error!' )
#
#  Ensure that 1 <= RANK1.
#
  if ( rank1 < 1 ):
    print ( '' )
    print ( 'comp_random_grlex(): Fatal error!' )
    print ( '  RANK1 < 1' )
    raise Exception ( 'comp_random_grlex(): Fatal error!' )
#
#  Ensure that RANK1 <= RANK2.
#
  if ( rank2 < rank1 ):
    print ( '' )
    print ( 'comp_random_grlex(): Fatal error!' )
    print ( '  RANK2 < RANK1' )
    raise Exception ( 'comp_random_grlex(): Fatal error!' )
#
#  Choose RANK between RANK1 and RANK2.
#
  rank = rng.integers ( low = rank1, high = rank2, endpoint = True )
#
#  Recover the composition of given RANK.
#
  xc = comp_unrank_grlex ( kc, rank )

  return xc, rank

def comp_random_grlex_test ( rng ):

#*****************************************************************************80
#
## comp_random_grlex_test() tests comp_random_grlex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'comp_random_grlex_test():' )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  comp_random_grlex() selects a random COMP in' )
  print ( '  graded lexicographic (grlex) order between indices RANK1 and RANK2.' )
  print ( '' )

  kc = 3
  rank1 = 20
  rank2 = 60

  for test in range ( 0, 5 ):
    xc, rank = comp_random_grlex ( kc, rank1, rank2, rng )
    nc = np.sum ( xc )
    print ( '   %3d: ' % ( rank ), end = '' )
    print ( '    %2d = ' % ( nc ), end = '' )
    for j in range ( 0, kc - 1 ):
      print ( '%2d + ' % ( xc[j] ), end = '' )
    print ( '%2d' % ( xc[kc-1] ) )

  return

def comp_random ( n, k, rng ):

#*****************************************************************************80
#
## comp_random() selects a random composition of the integer N into K parts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2015
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
#    integer N, the integer to be decomposed.
#
#    integer K, the number of parts in the composition.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K), the parts of the composition.
#
  import numpy as np

  b = ksub_random2 ( n + k - 1, k - 1, rng )

  a = np.zeros ( k )
  for i in range ( 0, k - 1 ):
    a[i] = b[i]
  a[k-1] = n + k

  l = 0

  for i in range ( 0, k ):
    m = a[i]
    a[i] = a[i] - l - 1
    l = m

  return a

def comp_random_test ( rng ):

#*****************************************************************************80
#
## comp_random_test() tests comp_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 10
  k = 5

  print ( '' )
  print ( 'comp_random_test():' )
  print ( '  comp_random() generates random compositions.' )
  print ( '  Seeking compositions of %d using %d parts.' % ( n, k ) )
  print ( '' )

  for i in range ( 1, 6 ):
    a = comp_random ( n, k, rng )
    for j in range ( 0, k ):
      print ( '  %2d' % ( a[j] ), end = '' )
    print ( '' )

  return

def comp_rank_grlex ( kc, xc ):

#*****************************************************************************80
#
## comp_rank_grlex() computes the graded lexicographic rank of a composition.
#
#  Discussion:
#
#    The graded lexicographic ordering is used, over all KC-compositions
#    for NC = 0, 1, 2, ...
#
#    For example, if KC = 3, the ranking begins:
#
#    Rank  Sum    1  2  3
#    ----  ---   -- -- --
#       1    0    0  0  0
#
#       2    1    0  0  1
#       3    1    0  1  0
#       4    1    1  0  1
#
#       5    2    0  0  2
#       6    2    0  1  1
#       7    2    0  2  0
#       8    2    1  0  1
#       9    2    1  1  0
#      10    2    2  0  0
#
#      11    3    0  0  3
#      12    3    0  1  2
#      13    3    0  2  1
#      14    3    0  3  0
#      15    3    1  0  2
#      16    3    1  1  1
#      17    3    1  2  0
#      18    3    2  0  1
#      19    3    2  1  0
#      20    3    3  0  0
#
#      21    4    0  0  4
#      ..   ..   .. .. ..
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int KC, the number of parts in the composition.
#    1 <= KC.
#
#    int XC[KC], the composition.
#    For each 1 <= I <= KC, we have 0 <= XC(I).
#
#  Output:
#
#    integer RANK, the rank of the composition.
#
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_rank_grlex(): Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_rank_grlex(): Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ( '' )
      print ( 'comp_rank_grlex(): Fatal error!' )
      print ( '  XC[I] < 0' )
      raise Exception ( 'comp_rank_grlex(): Fatal error!' );
#
#  NC = sum ( XC )
#
  nc = np.sum ( xc )
#
#  Convert to KSUBSET format.
#
  ns = nc + kc - 1
  ks = kc - 1
  xs = np.zeros ( ks, dtype = np.int32 )

  xs[0] = xc[0] + 1
  for i in range ( 2, kc ):
    xs[i-1] = xs[i-2] + xc[i-1] + 1
#
#  Compute the rank.
#
  rank = 1;

  for i in range ( 1, ks + 1 ):
    if ( i == 1 ):
      tim1 = 0
    else:
      tim1 = xs[i-2];

    if ( tim1 + 1 <= xs[i-1] - 1 ):
      for j in range ( tim1 + 1, xs[i-1] ):
        rank = rank + i4_choose ( ns - j, ks - i )

  for n in range ( 0, nc ):
    rank = rank + i4_choose ( n + kc - 1, n )

  return rank

def comp_rank_grlex_test ( rng ):

#*****************************************************************************80
#
## comp_rank_grlex_test() tests comp_rank_grlex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'comp_rank_grlex_test():' )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  comp_rank_grlex() determines the rank of a COMP from' )
  print ( '  its parts.' )
  print ( '' )
  print ( '        Actual  Inferred' )
  print ( '  Test    Rank      Rank' )
  print ( '' )

  kc = 3
  rank1 = 20
  rank2 = 60

  for test in range ( 0, 5 ):
    xc, rank3 = comp_random_grlex ( kc, rank1, rank2, rng )
    rank4 = comp_rank_grlex ( kc, xc )
    print ( '  %4d  %6d  %8d' % ( test, rank3, rank4 ) )

  return

def comp_to_ksub ( nc, kc, ac ):

#*****************************************************************************80
#
## comp_to_ksub() converts a composition to a K-subset.
#
#  Discussion:
#
#    There is a bijection between K subsets and compositions.
#
#    Because we allow a composition to have entries that are 0, we need
#    to implicitly add 1 to each entry before establishing the bijection.
#
#    Let AC be a composition of NC into KC parts.
#
#    Then let
#      NS = NC + KC - 1
#      KS = KC - 1
#    and define
#      AS(I) = sum ( AC(1:I) + 1 ), for I = 1 : KS.
#      
#    Then AS is a KS subset of the integers 1 through NS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NC, the composition sum.
#
#    integer KC, the number of parts of the composition.
#
#    integer AC(KC), the parts of the composition.
#
#  Output:
#
#    integer NS, the size of the set.
#
#    integer KS, the size of the subset.
#
#    integer BS(KS), the entries of the K-subset, in increasing order.
#
  import numpy as np

  ns = nc + kc - 1
  ks = kc - 1
  bs = np.zeros ( ks )
  t = 0
  for i in range ( 0, ks ):
    t = t + ac[i] + 1
    bs[i] = t

  return ns, ks, bs

def comp_to_ksub_test ( rng ):

#*****************************************************************************80
#
## comp_to_ksub_test() tests comp_to_ksub().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'comp_to_ksub_test():' )
  print ( '  comp_to_ksub() returns the K subset corresponding to a composition.' )

  nc = 10
  kc = 5

  for i in range ( 0, 5 ):

    print ( '' )

    ac = comp_random ( nc, kc, rng )
    print ( '  COMP:  ', end = '' )
    for j in range ( 0, kc ):
      print ( '  %2d' % ( ac[j] ), end = '' )
    print ( '' )

    ns, ks, bs = comp_to_ksub ( nc, kc, ac );
    print ( '  KSUB:  ', end = '' )
    for j in range ( 0, ks ):
      print ( '  %2d' % ( bs[j] ), end = '' )
    print ( '' )

  return

def comp_unrank_grlex ( kc, rank ):

#*****************************************************************************80
#
## comp_unrank_grlex() computes the composition of given grlex rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int KC, the number of parts of the composition.
#    1 <= KC.
#
#    int RANK, the rank of the composition.
#    1 <= RANK.
#
#  Output:
#
#    integer XC[KC], the composition XC of the given rank.
#    For each I, 0 <= XC[I] <= NC, and 
#    sum ( 1 <= I <= KC ) XC[I] = NC.
#
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_unrank_grlex(): Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_unrank_grlex(): Fatal error!' )
#
#  Ensure that 1 <= RANK.
#
  if ( rank < 1 ):
    print ( '' )
    print ( 'comp_unrank_grlex(): Fatal error!' )
    print ( '  RANK < 1' )
    raise Exception ( 'comp_unrank_grlex(): Fatal error!' )
#
#  Determine the appropriate value of NC.
#  Do this by adding up the number of compositions of sum 0, 1, 2, 
#  ..., without exceeding RANK.  Moreover, RANK - this sum essentially
#  gives you the rank of the composition within the set of compositions
#  of sum NC.  And that's the number you need in order to do the
#  unranking.
#
  rank1 = 1
  nc = -1

  while ( True ):
    nc = nc + 1
    r = i4_choose ( nc + kc - 1, nc )
    if ( rank < rank1 + r ):
      break
    rank1 = rank1 + r

  rank2 = rank - rank1
#
#  Convert to KSUBSET format.
#  Apology: an unranking algorithm was available for KSUBSETS,
#  but not immediately for compositions.  One day we will come back
#  and simplify all this.
#
  ks = kc - 1
  ns = nc + kc - 1
  xs = np.zeros ( ks, dtype = np.int32 )
  nksub = i4_choose ( ns, ks )

  j = 1

  for i in range ( 1, ks + 1 ):
    r = i4_choose ( ns - j, ks - i )
    while ( r <= rank2 and 0 < r ):
      rank2 = rank2 - r
      j = j + 1
      r = i4_choose ( ns - j, ks - i )
    xs[i-1] = j
    j = j + 1
#
#  Convert from KSUBSET format to COMP format.
#
  xc = np.zeros ( kc, dtype = np.int32 )
  xc[0] = xs[0] - 1
  for i in range ( 2, kc ):
    xc[i-1] = xs[i-1] - xs[i-2] - 1
  xc[kc-1] = ns - xs[ks-1]

  return xc

def comp_unrank_grlex_test ( ):

#*****************************************************************************80
#
## comp_unrank_grlex_test() tests comp_unrank_grlex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  kc = 3

  print ( '' )
  print ( 'comp_unrank_grlex_test():' )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  comp_unrank_grlex() determines the parts' )
  print ( '  of a COMP from its rank.' )
 
  print ( '' )
  print ( '  Rank: ->  NC       COMP    ' )
  print ( '  ----:     --   ------------ ' )

  for rank in range ( 1, 72 ):
    xc = comp_unrank_grlex ( kc, rank )
    nc = np.sum ( xc )
    print ( '   %3d: ' % ( rank ), end = '' )
    print ( '    %2d = ' % ( nc ), end = '' )
    for j in range ( 0, kc - 1 ):
      print ( '%2d + ' % ( xc[j] ), end = '' )
    print ( '%2d' % ( xc[kc-1] ) )
#
#  When XC(1) == NC, we have completed the compositions associated with
#  a particular integer, and are about to advance to the next integer.
#
    if ( xc[0] == nc ):
      print ( '  ----:     --   ------------' )

  return

def congruence ( a, b, c ):

#*****************************************************************************80
#
## congruence() solves a congruence of the form A * X = C ( mod B ).
#
#  Discussion:
#
#    A, B and C are given integers.  The equation is solvable if and only
#    if the greatest common divisor of A and B also divides C.
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
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998, page 446.
#
#  Input:
#
#    integer A, B, C, the coefficients of the Diophantine equation.
#
#  Output:
#
#    integer X, the solution of the Diophantine equation.
#    X will be between 0 and B-1.
#
#    integer IERROR, error flag.
#    0, no error, X was computed.
#    1, A = B = 0, C is nonzero.
#    2, A = 0, B and C nonzero, but C is not a multiple of B.
#    3, A nonzero, B zero, C nonzero, but C is not a multiple of A.
#    4, A, B, C nonzero, but GCD of A and B does not divide C.
#    5, algorithm ran out of internal space.
#
  import numpy as np

  a = np.floor ( a )
  b = np.floor ( b )
  c = np.floor ( c )

  nmax = 100
#
#  Initialize output quantities.
#
  ierror = 0
  x = 0
  y = 0
#
#  Special cases.
#
  if ( a == 0 and b == 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a == 0 and b == 0 and c != 0 ):
    ierror = 1
    x = 0
    return x, ierror
  elif ( a == 0 and b != 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a == 0 and b != 0 and c != 0 ):
    x = 0
    if ( ( c % b ) != 0 ):
      ierror = 2
    return x, ierror
  elif ( a != 0 and b == 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a != 0 and b == 0 and c != 0 ):
    x = ( c // a )
    if ( ( c % a ) != 0 ):
      ierror = 3
    return x, ierror
  elif ( a != 0 and b != 0 and c == 0 ):
#   g = i4_gcd ( a, b )
#   x = np.floor ( b / g )
    x = 0
    return x, ierror
#
#  Now handle the "general" case: A, B and C are nonzero.
#
#  Step 1: Compute the GCD of A and B, which must also divide C.
#
  g = i4_gcd ( a, b )

  if ( ( c % g ) != 0 ):
    ierror = 4
    return x, ierror

  a_copy = ( a // g )
  b_copy = ( b // g )
  c_copy = ( c // g )
#
#  Step 2: Split A and B into sign and magnitude.
#
  a_mag = abs ( a_copy )
  a_sign = i4_sign ( a_copy )
  b_mag = abs ( b_copy )
  b_sign = i4_sign ( b_copy )
#
#  Another special case, A_MAG = 1 or B_MAG = 1.
#
  if ( a_mag == 1 ):
    x = a_sign * c_copy
    return x, ierror
  elif ( b_mag == 1 ):
    x = 0
    return x, ierror
#
#  Step 3: Produce the Euclidean remainder sequence.
#
  q = np.zeros ( nmax )

  if ( b_mag <= a_mag ):
    swap = 0
    q[0] = a_mag
    q[1] = b_mag
  else:
    swap = 1
    q[0] = b_mag
    q[1] = a_mag

  n = 2

  while ( True ):

    q[n] = ( q[n-2] % q[n-1] )

    if ( q[n] == 1 ):
      break

    n = n + 1

    if ( nmax <= n ):
      ierror = 5
      print ( '' )
      print ( 'congruence(): Fatal error!' )
      print ( '  Exceeded number of iterations.' )
      raise Exception ( 'congruence(): Fatal error!' )
#
#  Step 4: Now go backwards to solve X * A_MAG + Y * B_MAG = 1.
#
  y = 0
  for k in range ( n, 0, -1 ):
    x = y
    y = ( 1 - x * q[k-1] ) / q[k]
#
#  Step 5: Undo the swapping.
#
  if ( swap ):
    z = x
    x = y
    y = z
#
#  Step 6: Now apply signs to X and Y so that X * A + Y * B = 1.
#
  x = x * a_sign
#
#  Step 7: Multiply by C, so that X * A + Y * B = C.
#
  x = x * c_copy
#
#  Step 8: Now force 0 <= X < B.
#
  x = ( x % b )
#
#  Step 9: Force positivity.
#
  if ( x < 0 ):
    x = x + b

  return x, ierror

def congruence_test ( ):

#*****************************************************************************80
#
## congruence_test() tests congruence().
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
  import numpy as np

  test_num = 20

  a_test = np.array ( ( \
     1027,  1027,  1027,  1027, -1027, \
    -1027, -1027, -1027,     6,     0, \
        0,     0,     1,     1,     1, \
     1024,     0,     0,     5,     2 ) )
  b_test = np.array ( ( \
      712,   712,  -712,  -712,   712, \
      712,  -712,  -712,     8,     0, \
        1,     1,     0,     0,     1, \
   -15625,     0,     3,     0,     4 ) )
  c_test = np.array ( ( \
        7,    -7,     7,    -7,     7, \
       -7,     7,    -7,    50,     0, \
        0,     1,     0,     1,     0, \
    11529,     1,    11,    19,     7 ) )

  print ( '' )
  print ( 'congruence_test():' )
  print ( '  congruence() solves a congruence equation:' )
  print ( '    A * X = C mod ( B )' )
  print ( '' )
  print ( '   I        A         B         C         X     Mod ( A*X-C,B)' )
  print ( '' )

  for test_i in range ( 0, test_num ):

    a = a_test[test_i]
    b = b_test[test_i]
    c = c_test[test_i]

    x, ierror = congruence ( a, b, c )

    if ( b != 0 ):
      result = i4_modp ( a * x - c, b )
    else:
      result = 0

    print ( '  %2d  %8d  %8d  %8d  %8d  %8d' % ( test_i, a, b, c, x, result ) )

  return

def count_pose_random ( rng ):

#*****************************************************************************80
#
## count_pose_random() poses a problem for the game "The Count is Good"
#
#  Discussion:
#
#    The French television show "The Count is Good" has a game that goes
#    as follows:
#
#      A number is chosen at random between 100 and 999.  This is the GOAL.
#
#      Six numbers are randomly chosen from the set 1, 2, 3, 4, 5, 6, 7, 8,
#      9, 10, 25, 50, 75, 100.  These numbers are the BLOCKS.
#
#      The player must construct a formula, using some or all of the blocks,
#      (but not more than once), and the operations of addition, subtraction,
#      multiplication and division.  Parentheses should be used to remove
#      all ambiguity.  However, it is forbidden to use subtraction in a
#      way that produces a negative result, and all division must come out
#      exactly, with no remainder.
#
#    This routine poses a sample problem from the show.  The point is,
#    to determine how to write a program that can solve such a problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Raymond Seroul,
#    Programming for Mathematicians,
#    Springer Verlag, 2000, page 355-357.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer BLOCKS(6), the six numbers available for the formula.
#
#    integer GOAL, the goal number.
#
  import numpy as np

  stuff = np.array ( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100 ], \
    dtype = np.int32 )

  goal = rng.integers ( low = 100, high = 999, endpoint = True )

  m = 14
  n = 6
  ind = ksub_random2 ( m, n, rng )

  blocks = np.zeros ( 6, dtype = np.int32 )

  for i in range ( 0, 6 ):
    blocks[i] = stuff[ind[i]-1]

  return blocks, goal

def count_pose_random_test ( rng ):

#*****************************************************************************80
#
## count_pose_random_test() tests count_pose_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'count_pose_random_test():' )
  print ( '  count_pose_random() poses a random problem for' )
  print ( '  the game "The Count is Good".' )

  for i in range ( 0, 5 ):

    blocks, goal = count_pose_random ( rng )

    print ( '' )
    print ( '  Problem #%d' % ( i ) )
    print ( '' )
    print ( '    The goal number:' )
    print ( '' )
    print ( '      %d' % ( goal ) )
    print ( '' )
    print ( '    The available numbers are' )
    print ( '' )
    print ( '    ', end = '' )
    for j in range ( 0, 6 ):
      print ( '  %4d' % ( blocks[j] ), end = '' )
    print ( '' )

  return

def debruijn ( m, n ):

#*****************************************************************************80
#
## debruijn() constructs a de Bruijn sequence.
#
#  Discussion:
#
#    Suppose we have an alphabet of M letters, and we are interested in
#    all possible strings of length N.  If M = 2 and N = 3, then we are
#    interested in the M^N strings:
#
#      000
#      001
#      010
#      011
#      100
#      101
#      110
#      111
#
#    Now, instead of making a list like this, we prefer, if possible, to
#    write a string of letters, such that every consecutive sequence of
#    N letters is one of the strings, and every string occurs once, if
#    we allow wraparound.
#
#    For the above example, a suitable sequence would be the 8 characters:
#
#      00011101(00...
#
#    where we have suggested the wraparound feature by repeating the first
#    two characters at the end.
#
#    Such a sequence is called a de Bruijn sequence.  It can easily be
#    constructed by considering a directed graph, whose nodes are all
#    M^(N-1) strings of length N-1.  A node I has a directed edge to
#    node J (labeled with character K) if the string at node J can
#    be constructed by beheading the string at node I and adding character K.
#
#    In this setting, a de Bruijn sequence is simply an Eulerian circuit
#    of the directed graph, with the edge labels being the entries of the
#    sequence.  In general, there are many distinct de Bruijn sequences
#    for the same parameter M and N.  This program will only find one
#    of them.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of letters in the alphabet.
#
#    integer N, the number of letters in a codeword.
#
#  Output:
#
#    integer STRING(M^N), a De Bruijn string.
#
  import numpy as np
#
#  Construct the adjacency information.
#
  nnode = m ** ( n - 1 )
  nedge = m ** n

  iedge = 0

  inode = np.zeros ( nedge, dtype = np.int32 )
  jnode = np.zeros ( nedge, dtype = np.int32 )
  knode = np.zeros ( nedge, dtype = np.int32 )
  jvec = np.zeros ( n - 1, dtype = np.int32 )

  for i in range ( 1, nnode + 1 ):

    ivec = index_unrank0 ( n - 1, m, i )

    for k in range ( 0, m ):

      for l in range ( 0, n - 2 ):
        jvec[l] = ivec[l+1]
      jvec[n-2] = k + 1

      j = index_rank0 ( n - 1, m, jvec )

      inode[iedge] = i
      jnode[iedge] = j
      knode[iedge] = k + 1
      iedge = iedge + 1
#
#  Determine a circuit.
#
  success, trail = digraph_arc_euler ( nnode, nedge, inode, jnode )
#
#  The string is constructed from the labels of the edges in the circuit.
#
  s = ''
  for i in range ( 0, nedge ):
    s = s + digit_to_ch ( knode[trail[i]-1] )

  return s

def debruijn_test ( ):

#*****************************************************************************80
#
## debruijn_test() tests debruijn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  mtest = np.array ( [ 2, 3, 2 ] )
  ntest = np.array ( [ 3, 3, 4 ] )

  print ( '' )
  print ( 'debruijn_test():' )
  print ( '  debruijn() computes a de Bruijn string.' )

  for itest in range ( 0, 3 ):

    m = mtest[itest]
    n = ntest[itest]

    print ( '' )
    print ( '  The alphabet size is M = %d' % ( m ) )
    print ( '  The string length is N = %d' % ( n ) )

    s = debruijn ( m, n )

    print ( '' )
    print ( '    %s' % ( s ) )

  return

def dec_add ( mantissa1, exponent1, mantissa2, exponent2, dec_digit ):

#*****************************************************************************80
#
## dec_add() adds two decimal quantities.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine computes
#
#      MANTISSA * 10^EXPONENT = 
#        MANTISSA1 * 10^EXPONENT1 
#      + MANTISSA2 * 10^EXPONENT2
#
#    while trying to avoid integer overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA1, EXPONENT1, the first number to be added.
#
#    integer MANTISSA2, EXPONENT2, the second number to be added.
#
#    integer dec_digit, the number of decimal digits.
#
#  Output:
#
#    integer MANTISSA, EXPONENT, the sum.
#
  if ( mantissa1 == 0 ):
    mantissa = mantissa2
    exponent = exponent2
    return mantissa, exponent
  elif ( mantissa2 == 0 ):
    mantissa = mantissa1
    exponent = exponent1
    return mantissa, exponent
  elif ( exponent1 == exponent2 ):
    mantissa = mantissa1 + mantissa2
    exponent = exponent1
    [ mantissa, exponent ] = dec_round ( mantissa, exponent, dec_digit )
    return mantissa, exponent
#
#  Line up the exponents.
#
  mantissa3 = mantissa1
  mantissa4 = mantissa2

  if ( exponent1 < exponent2 ):
    mantissa4 = mantissa4 * 10 ** ( exponent2 - exponent1 )
  elif ( exponent2 < exponent1 ):
    mantissa3 = mantissa3 * 10 ** ( exponent1 - exponent2 )
#
#  Add the coefficients.
#
  mantissa = mantissa3 + mantissa4
  exponent = min ( exponent1, exponent2 )
#
#  Clean up the result.
#
  mantissa, exponent = dec_round ( mantissa, exponent, dec_digit )

  return mantissa, exponent

def dec_add_test ( ):

#*****************************************************************************80
#
## dec_add_test() tests dec_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#

  print ( '' )
  print ( 'dec_add_test():' )
  print ( '  dec_add() adds two decimals.' )

  dec_digit = 3

  atop = 128
  abot = -1
  btop = 438
  bbot = -2

  ctop, cbot = dec_add ( atop, abot, btop, bbot, dec_digit )

  print ( '' )
  print ( '  Number of decimal places is %d' % ( dec_digit ) )
  print ( '' )

  string = dec_to_s ( atop, abot )
  print ( '  A = %s' % ( string ) )
  string = dec_to_s ( btop, bbot )
  print ( '  B = %s' % ( string ) )
  string = dec_to_s ( ctop, cbot )
  print ( '  C = %s' % ( string ) )

  return

def dec_div ( mantissa1, exponent1, mantissa2, exponent2, dec_digit ):

#*****************************************************************************80
#
## dec_div() divides two decimal values.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine computes
#
#      MANTISSA * 10^EXPONENT
#      = ( MANTISSA1 * 10^EXPONENT1 ) / ( MANTISSA2 * 10^EXPONENT2 )
#      = ( MANTISSA1 / MANTISSA2 ) * 10^( EXPONENT1 - EXPONENT2 )
#
#    while avoiding integer overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA1, EXPONENT1, the numerator.
#
#    integer MANTISSA2, EXPONENT2, the denominator.
#
#    integer dec_digit, the number of decimal digits.
#
#  Output:
#
#    integer MANTISSA, EXPONENT, the result.
#

#
#  First special case, top fraction is 0.
#
  if ( mantissa1 == 0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent
#
#  First error, bottom of fraction is 0.
#
  if ( mantissa2 == 0 ):
    print ( '' )
    print ( 'dec_div(): Fatal error!' )
    print ( '  Denominator is zero.' )
    raise Exception ( 'dec_div(): Fatal error!' )
#
#  Second special case, result is 1.
#
  if ( mantissa1 == mantissa2 and exponent1 == exponent2 ):
    mantissa = 1
    exponent = 0
    return mantissa, exponent
#
#  Third special case, result is power of 10.
#
  if ( mantissa1 == mantissa2 ):
    mantissa = 1
    exponent = exponent1 - exponent2
    return mantissa, exponent
#
#  Fourth special case: MANTISSA1/MANTISSA2 is exact.
#
  if ( ( mantissa1 // mantissa2 ) * mantissa2 == mantissa1 ):
    mantissa = ( mantissa1 // mantissa2 )
    exponent = exponent1 - exponent2
    return mantissa, exponent
#
#  General case.
#
  dval = float ( mantissa1 ) / float ( mantissa2 )

  mantissa3, exponent3 = r8_to_dec ( dval, dec_digit )

  mantissa = mantissa3
  exponent = exponent3 + exponent1 - exponent2

  return mantissa, exponent

def dec_div_test ( ):

#*****************************************************************************80
#
## dec_div_test() tests dec_div().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'dec_div_test():' )
  print ( '  dec_div() divides two decimals.' )

  dec_digit = 3

  atop = 523
  abot = -1
  btop = 134
  bbot = 2

  ctop, cbot = dec_div ( atop, abot, btop, bbot, dec_digit )

  print ( '' )
  print ( '  Number of decimal places is %d' % ( dec_digit ) )
  print ( '' )

  string = dec_to_s ( atop, abot )
  print ( '  A = %s' % ( string ) )
  string = dec_to_s ( btop, bbot )
  print ( '  B = %s' % ( string ) )
  string = dec_to_s ( ctop, cbot )
  print ( '  C = %s' % ( string ) )

  return

def dec_mul ( mantissa1, exponent1, mantissa2, exponent2, dec_digit ):

#*****************************************************************************80
#
## dec_mul() multiplies two decimals.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine computes
#
#      MANTISSA * 10^EXPONENT 
#      = ( MANTISSA1 * 10^EXPONENT1) * (MANTISSA2 * 10^EXPONENT2)
#      = ( MANTISSA1 * MANTISSA2 ) * 10^( EXPONENT1 + EXPONENT2 )
#
#    while avoiding integer overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA1, EXPONENT1, the first multiplier.
#
#    integer MANTISSA2, EXPONENT2, the second multiplier.
#
#    integer dec_digit, the number of decimal digits.
#
#  Output:
#
#    integer MANTISSA, EXPONENT, the product.
#
  import numpy as np

  i_max = i4_huge ( )
#
#  The result is zero if either MANTISSA1 or MANTISSA2 is zero.
#
  if ( mantissa1 == 0 or mantissa2 == 0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent
#
#  The result is simple if either MANTISSA1 or MANTISSA2 is one.
#
  if ( abs ( mantissa1 ) == 1 or abs ( mantissa2 ) == 1 ):
    mantissa = mantissa1 * mantissa2
    exponent = exponent1 + exponent2
    return mantissa, exponent

  temp = np.log ( abs ( mantissa1 ) ) + np.log ( abs ( mantissa2 ) )

  if ( temp < np.log ( i_max ) ):

    mantissa = mantissa1 * mantissa2
    exponent = exponent1 + exponent2

  else:

    dval = mantissa1 * mantissa2

    mantissa3, exponent3 = r8_to_dec ( dval, dec_digit )

    mantissa = mantissa3
    exponent = exponent3 + ( exponent1 + exponent2 )

  mantissa, exponent = dec_round ( mantissa, exponent, dec_digit )

  return mantissa, exponent

def dec_mul_test ( ):

#*****************************************************************************80
#
## dec_mul_test() tests dec_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'dec_mul_test():' )
  print ( '  dec_mul() multiplies two decimals.' )

  dec_digit = 2

  atop = 14
  abot = -4
  btop = 16
  bbot = 2

  ctop, cbot = dec_mul ( atop, abot, btop, bbot, dec_digit )

  print ( '' )
  print ( '  Number of decimal places is %d' % ( dec_digit ) )
  print ( '' )

  string = dec_to_s ( atop, abot )
  print ( '  A = %s' % ( string ) )
  string = dec_to_s ( btop, bbot )
  print ( '  B = %s' % ( string ) )
  string = dec_to_s ( ctop, cbot )
  print ( '  C = %s' % ( string ) )

  return

def dec_round ( mantissa, exponent, dec_digit ):

#*****************************************************************************80
#
## dec_round() rounds a decimal fraction to a given number of digits.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine takes an arbitrary decimal fraction makes sure that
#    MANTISSA has no more than dec_digit digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA, EXPONENT, the coefficient and exponent
#    of a decimal fraction.
#
#    integer dec_digit, the number of decimal digits.
#
#  Output:
#
#    integer MANTISSA, EXPONENT, the rounded data.
#    MANTISSA has no more than dec_digit decimal digits.
#
  if ( mantissa == 0 ):
    exponent = 0
    return mantissa, exponent

  while ( 10 ** dec_digit <= abs ( mantissa ) ):
    mantissa = int ( round ( mantissa / 10.0 ) )
    exponent = exponent + 1
#
#  Absorb trailing 0's into the exponent.
#
  while ( ( mantissa // 10 ) * 10 == mantissa ):
    mantissa = mantissa // 10
    exponent = exponent + 1

  return mantissa, exponent

def dec_round_test ( ):

#*****************************************************************************80
#
## dec_round_test() tests dec_round().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_test = 7
  d_test = np.array ( [ 1, 2, 3, 4, 2, 3, 4 ] )
  exponent_test = np.array ( [ -1,  -1, -1, -1, 2, 2, 2 ] )
  mantissa_test = np.array ( [ 523, 523, 523, 523, 6340, 6340, 6340 ] )

  print ( '' )
  print ( 'dec_round_test():' )
  print ( '  dec_round() "rounds" a decimal to a number of digits.' )
  print ( '' )
  print ( '           -----Before-------  -----After--------' )
  print ( '  Digits   Mantissa  Exponent  Mantissa  Exponent' )
  print ( '' )

  for i in range ( 0, n_test ):

    dec_digit = d_test[i]

    mantissa = mantissa_test[i]
    exponent = exponent_test[i]

    mantissa, exponent = dec_round ( mantissa, exponent, dec_digit )

    print ( '  %6d  %6d  %6d      %6d  %6d' \
      % ( dec_digit, mantissa_test[i], exponent_test[i], mantissa, exponent ) )

  return

def dec_to_r8 ( mantissa, exponent ):

#*****************************************************************************80
#
## dec_to_r8() converts a decimal to an R8.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA, EXPONENT, the coefficient and exponent
#    of the decimal value.
#
#  Output:
#
#    real R, the equivalent real value.
#
  r = mantissa * ( 10 ** exponent )

  return r

def dec_to_r8_test ( rng ):

#*****************************************************************************80
#
## dec_to_r8_test() tests dec_to_r8().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'dec_to_r8_test():' )
  print ( '  dec_to_r8() converts a decimal to a real number.' )

  dec_digit = 5

  print ( '' )
  print ( '  The number of decimal digits is %d' % ( dec_digit ) )

  r8_lo = -10.0
  r8_hi = +10.0

  print ( '' )
  print ( '     R   =>  A * 10^B  =>  R2' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    a, b = r8_to_dec ( r, dec_digit )
    r2 = dec_to_r8 ( a, b )
    print ( '  %10.6f  %6d  %6d  %10.6f' % ( r, a, b, r2 ) )

  return

def dec_to_rat ( mantissa, exponent ):

#*****************************************************************************80
#
## dec_to_rat() converts a decimal to a rational representation.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    A rational value is represented by TOP / BOT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA, EXPONENT, the decimal number.
#
#  Output:
#
#    integer TOP, BOT, the rational value.
#
  if ( exponent == 0 ):
    top = mantissa
    bot = 1
  elif ( 0 < exponent ):
    top = mantissa * 10 ** exponent
    bot = 1
  else:
    top = mantissa
    bot = 10 ** ( - exponent )
    gcd = i4_gcd ( top, bot )
    top = ( top // gcd )
    bot = ( bot // gcd )

  return top, bot

def dec_to_rat_test ( rng ):

#*****************************************************************************80
#
## dec_to_rat_test() tests dec_to_rat().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'dec_to_rat_test():' )
  print ( '  dec_to_rat() decimal => fraction.' )
  print ( '' )
  print ( '  In this test, choose the top and bottom' )
  print ( '  of a rational at random, and compute the' )
  print ( '  equivalent real number.' )
  print ( '' )
  print ( '  Then convert to decimal, and the equivalent real.' )
  print ( '' )
  print ( '  Then convert back to rational and the equivalent real.' )
  
  for i in range ( 0, 10 ):

    rat_top = rng.integers ( low = -1000, high = 1000, endpoint = True )
    rat_bot = rng.integers ( low = 1, high = 1000, endpoint = True )

    r1 = float ( rat_top ) / float ( rat_bot )
    mantissa, exponent = rat_to_dec ( rat_top, rat_bot )
    r2 = float ( mantissa ) * 10.0 ** exponent
    rat_top2, rat_bot2 = dec_to_rat ( mantissa, exponent )
    r3 = float ( rat_top2 ) / float ( rat_bot2 )

    print ( '' )
    print ( '  %g = %d / %d' % ( r1, rat_top, rat_bot ) )
    print ( '  %g = %d * 10^%d' % ( r2, mantissa, exponent ) )
    print ( '  %g = %d / %d' % ( r1, rat_top2, rat_bot2 ) )

  return

def dec_to_s ( mantissa, exponent ):

#*****************************************************************************80
#
## dec_to_s() returns a string representation of a decimal.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#  Example:
#
#    MANTISSA EXPONENT   S
#    ----     ----       ------
#       0        0       0
#      21        3       21000
#      -3        0       -3
#     147       -2       14.7
#      16       -5       0.00016
#     123      -21       0.0000000000000000012
#      34      -30       0.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA, EXPONENT, integers which represent the decimal.
#
#  Output:
#
#    string S, the representation of the value.
#
  s = ''

  if ( mantissa == 0 ):
    s = '0'
    return s

  if ( mantissa < 0 ):
    s = '-'
    mantissa = abs ( mantissa )
#
#  Mantissas should be normalized so that they do not end in 0!
#
  while ( 10 * ( mantissa // 10 ) == mantissa ):
    mantissa = ( mantissa // 10 )
    exponent = exponent + 1
#
#  How many digits are there in the mantissa?
#
  mantissa_digits = 0
  mantissa_ten = 1

  while ( mantissa_ten <= mantissa ):
    mantissa_ten = mantissa_ten * 10
    mantissa_digits = mantissa_digits + 1
#
#  For a positive exponent, we just print the mantissa,
#  possibly followed by some zeros.
#
  if ( 0 <= exponent ):

    for i in range ( 0, mantissa_digits ):
      mantissa_ten = ( mantissa_ten // 10 )
      d = ( mantissa // mantissa_ten )
      mantissa = mantissa - d * mantissa_ten
      c = digit_to_ch ( d )
      s = s + c

    for i in range ( 0, exponent ):
      s = s + '0'
#
#  A negative mantissa means, 
#  * possibly some digits, or else 0,
#  * a decimal point,
#  * possibly some zeros
#  * the remaining digits.
#
  elif ( exponent < 0 ):

    if ( 0 < mantissa_digits + exponent ):

      for i in range ( 0, mantissa_digits + exponent ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

      s = s + '.'

      ihi = - exponent

      for i in range ( 0, ihi ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

    elif ( 0 == mantissa_digits + exponent ):

      s = s + '0' + '.'

      for i in range ( 0, mantissa_digits ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

    elif ( mantissa_digits + exponent < 0 ):

      s = s + '0' + '.'

      ihi = - ( mantissa_digits + exponent )

      for i in range ( 0, ihi ):
        s = s + '0'

      for i in range ( 0, mantissa_digits ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

  return s

def dec_to_s_test ( ):

#*****************************************************************************80
#
## dec_to_s_test() tests dec_to_s().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'dec_to_s_test():' )
  print ( '  dec_to_s() prints a decimal value.' )
  print ( '' )
  print ( '  Mantissa  Exponent  String' )
  print ( '' )

  mantissa = 523
  exponent = -1
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  mantissa = 134
  exponent = 2
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  mantissa = -134
  exponent = 2
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  mantissa = 0
  exponent = 10
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  for exponent in range ( -8, 4 ):
    mantissa = 123456
    s = dec_to_s ( mantissa, exponent )
    print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  return

def dec_width ( mantissa, exponent ):

#*****************************************************************************80
#
## dec_width() returns the "width" of a decimal number.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The "width" of a decimal number is the number of characters
#    required to print it.
#
#  Example:
#
#    Mantissa  Exponent Width  Representation:
#
#         523      -1       4           5.23
#         134       2       5       13400
#           0      10       1           0
#      123456     -10      12           0.0000123456
#      123456      -3       7         123.456
#      123456       0       6      123456
#      123456       3       9   123456000
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MANTISSA, EXPONENT, the decimal number.
#
#  Output:
#
#    integer WIDTH, the "width" of the decimal number.
#
  width = 1
  ten_pow = 10

  if ( mantissa == 0 ):
    return width
  
  mantissa_abs = abs ( mantissa )

  while ( ten_pow <= mantissa_abs ):
    width = width + 1
    ten_pow = ten_pow * 10

  if ( 0 < exponent ):
    width = width + exponent
  elif ( exponent < 0 ):
    width = max ( width, 1 - exponent )
#
#  An internal decimal point adds one position.
#
    if ( 0 < width ):
      width = width + 1
#
#  A leading "0." adds two positions.
#
    else:
      width = 2 - width

  if ( mantissa < 0 ):
    width = width + 1

  return width

def dec_width_test ( ):

#*****************************************************************************80
#
## dec_width_test() tests dec_width().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'dec_width_test():' )
  print ( '  dec_width() determines the "width" of a decimal.' )
  print ( '' )
  print ( '  Mantissa  Exponent  Width' )
  print ( '' )

  mantissa = 523
  exponent = -1
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  mantissa = 134
  exponent = 2
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  mantissa = -134
  exponent = 2
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  mantissa = 0
  exponent = 10
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  for exponent in range ( -8, 4 ):
    mantissa = 123456
    i = dec_width ( mantissa, exponent )
    print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  return

def derange0_back_next ( n, a, more, indx, k, maxstack, nstack, stacks, ncan ):

#*****************************************************************************80
#
## derange0_back_next() returns the next derangement of N items.
#
#  Discussion:
#
#    A derangement of N objects is a permutation of (0,...,N-1) which leaves 
#    no object unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#    This routine uses backtracking.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items to be deranged.
#
#    integer A(N), the output value of A from the previous call.
#    On first call with MORE = FALSE, the input value of A is not important.
#
#    bool MORE, should be set to FALSE on the first call, to force
#    initialization, and should be TRUE thereafter.
#
#    integer INDX, K, MAXSTACK, NSTACK, STACKS(N*(N+1)/2), NCAN(N),
#    bookkeeping variables which the user must set up, but not alter.
#
#  Output:
#
#    integer A(N), contains the next derangement, if MORE is TRUE.
#
#    bool MORE, is TRUE if another derangement was found, and
#    FALSE if there are no more derangements to return.
#
#    integer INDX, K, MAXSTACK, NSTACK, STACKS(N*(N+1)/2), NCAN(N),
#    bookkeeping variables which the user must set up, but not alter.
#
  if ( not more ):

    if ( n < 2 ):
      more = False
      return a, more, indx, k, maxstack, nstack, stacks, ncan

    indx = 0
    k = 0
    maxstack = ( ( n * ( n + 1 ) ) // 2 )
    nstack = 0
    for i in range ( 0, maxstack ):
      stacks[i] = 0
    for i in range ( 0, n ):
      ncan[i] = 0
    more = True

  while ( True ):

    a, indx, k, nstack, stacks, ncan = i4vec_backtrack ( n, maxstack, \
      a, indx, k, nstack, stacks, ncan )

    if ( indx == 1 ):

      break

    elif ( indx == 2 ):

      nstack, stacks, ncan = derange0_back_candidate ( n, a, k, nstack, \
        stacks, ncan )

    else:

      more = False
      break

  return a, more, indx, k, maxstack, nstack, stacks, ncan

def derange0_back_candidate ( n, a, k, nstack, stacks, ncan ):

#*****************************************************************************80
#
## derange0_back_candidate(): possible K-th entries of a derangement of (1,...,N).
#
#  Discussion:
#
#    A derangement of N objects is a permutation of (0,...,N-1) which leaves 
#    no object unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the derangement.
#
#    integer A(N).  The first K-1 entries of A
#    record the currently set values of the derangement.
#
#    integer K, the entry of the derangement for which candidates
#    are to be found.
#
#    integer NSTACK, the length of the stack.
#
#    integer STACKS((N*(N+1))/2).
#
#    integer NCAN(N), the number of candidates for each level.
#
#  Output:
#
#    integer NSTACK, the length of the output stack.
#
#    integer STACKS((N*(N+1))/2), contains candidates for entry K
#    added to the end of the stack.
#
#    integer NCAN(N), the number of candidates for each level.
#

#
#  Consider all the integers from 1 through N that have not been used yet.
#
  nfree = n - k + 1

  ifree = perm0_free ( k - 1, a, nfree )
#
#  Everything but K is a legitimate candidate for the K-th entry.
#
  ncan[k-1] = 0

  for ican in range ( 0, nfree ):

    if ( ifree[ican] != k - 1 ):
      ncan[k-1] = ncan[k-1] + 1
      stacks[nstack] = ifree[ican]
      nstack = nstack + 1

  return nstack, stacks, ncan

def derange0_back_next_test ( ):

#*****************************************************************************80
#
## derange0_back_next_test() tests derange0_back_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  a = np.zeros ( n )
  more = False
  indx = 0
  k = 0
  maxstack = ( ( n * ( n + 1 ) ) // 2 )
  nstack = 0
  stacks = np.zeros ( maxstack, dtype = np.int32 )
  ncan = np.zeros ( n, dtype = np.int32 )

  print ( '' )
  print ( 'derange0_back_next_test():' )
  print ( '  derange0_back_next() generates derangements' )
  print ( '  using backtracking.' )
  print ( '' )
  print ( '  Here, we seek all derangements of order N = %d' % ( n ) )
  print ( '' )

  rank = 0

  while ( True ):

    a, more, indx, k, maxstack, nstack, stacks, ncan = derange0_back_next ( n, \
    a, more, indx, k, maxstack, nstack, stacks, ncan )

    if ( not more ):
      break

    rank = rank + 1
    print ( '  %2d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

  return

def derange0_check ( n, a ):

#*****************************************************************************80
#
## derange0_check() checks if a vector is a derangement of ( 0, ..., N-1 ).
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer A(N), a permutation.
#
#  Output:
#
#    bool CHECK, is TRUE if A is a derangement, and
#    FALSE otherwise.
#

#
#  Values must be between 0 and N - 1
#
  for i in range ( 0, n ):
    if ( a[i] < 0 or n - 1 < a[i] ):
      check = False
      return check
#
#  Every value must be represented.
#
  for j in range ( 0, n ):
    check = False
    for i in range ( 0, n ):
      if ( a[i] == j ):
        check = True
        break
    if ( not check ):
      return check
#
#  Values must be deranged.
#
  for i in range ( 0, n ):
    if ( a[i] == i ):
      check = False
      return check

  check = True

  return check

def derange0_check_test ( ):

#*****************************************************************************80
#
## derange0_check_test() tests derange0_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  n = 5

  a_test = np.array ( [ \
    [  1, 2, 3, 4, 0 ], \
    [  1, 4, 2, 0, 3 ], \
    [  1, 2, 3, 0, 3 ], \
    [ -1, 2, 3, 4, 0 ], \
    [  0, 3, 8, 1, 2 ] ] )

  a = np.zeros ( n )

  print ( '' )
  print ( 'derange0_check_test():' )
  print ( '  derange0_check() checks whether a vector of N objects' )
  print ( '  represents a derangement of (1,...,N).' )
 
  for i in range ( 0, 5 ):
 
    for j in range ( 0, n ):
      a[j] = a_test[i,j]

    i4vec_transpose_print ( n, a, '  Potential derangement:' )
    check = derange0_check ( n, a )
    print ( '  CHECK = %s' % ( check ) )

  return

def derange0_weed_next ( n, a, more, maxder, numder ):

#*****************************************************************************80
#
## derange0_weed_next() computes derangements of (0,...,N-1), one at a time.
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#    This routine simply generates all permutations, one at a time,
#    and weeds out those that are not derangements.
#
#  Example:
#
#    Here are the derangements when N = 4:
#
#    1032
#    1230
#    1302
#    2031
#    2301
#    2310
#    3012
#    3201
#    3210
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer A(N).  On an initialization call, A is ignored.
#    Otherwise, A should be the output value of A from the previous call.
#
#    bool MORE, is FALSE on an initialization call, and TRUE otherwise.
#
#    integer MAXDER, NUMDER, two variables
#    used by the program for bookkeeping.  The user should declare these
#    variables, and pass the output values from one call to the next,
#    but should not alter them.
#
#  Output:
#
#    integer A(N), if MORE is TRUE, the next derangement.
#    If MORE is FALSE, then A contains no useful information.
#
#    bool MORE is TRUE if the next derangement was output in
#    A, and FALSE if there are no more derangements.
#
#    integer MAXDER, NUMDER, two variables
#    used by the program for bookkeeping.  The user should declare these
#    variables, and pass the output values from one call to the next,
#    but should not alter them.
#

#
#  Initialization on call with MORE = FALSE.
#
  if ( not more ):
    maxder = derange_enum ( n )
    numder = 0
#
#  Watch out for cases where there are no derangements.
#
  if ( maxder == 0 ):
    more = False
    return a, more, maxder, numder
#
#  Get the next permutation.
#
  while ( True ):

    a, more = perm0_lex_next ( n, a, more )
#
#  See if it is a derangment.
#
    deranged = derange0_check ( n, a )

    if ( deranged ):
      break

  numder = numder + 1

  if ( maxder <= numder ):
    more = False

  return a, more, maxder, numder

def derange0_weed_next_test ( ):

#*****************************************************************************80
#
## derange0_weed_next_test() tests derange0_weed_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  a = np.zeros ( n )
  more = 0
  maxder = 0
  numder = 0

  print ( '' )
  print ( 'derange0_weed_next_test():' )
  print ( '  derange0_weed_next() generates derangements' )
  print ( '  by generating ALL permutations, and "weeding out"' )
  print ( '  the ones that are not derangements.' )
  print ( '' )
  print ( '  Here, we seek all derangements of order N = %d' % ( n ) )
  print ( '' )

  rank = 0
 
  while ( True ):

    a, more, maxder, numder = derange0_weed_next ( n, a, more, maxder, numder )

    rank = rank + 1
    print ( '  %2d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def derange_enum2 ( n ):

#*****************************************************************************80
#
## derange_enum2() returns the number of derangements of N objects.
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#  Recursion:
#
#      D(0) = 1
#      D(1) = 0
#      D(2) = 1
#      D(N) = (N-1) * ( D(N-1) + D(N-2) )
#
#    or
#
#      D(0) = 1
#      D(1) = 0
#      D(N) = N * D(N-1) + (-1)^N
#
#  Formula:
#
#    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
#
#    Based on the inclusion/exclusion law.
#
#    D(N) is the number of ways of placing N non-attacking rooks on
#    an N by N chessboard with one diagonal deleted.
#
#    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
#
#    The number of permutations with exactly K items in the right
#    place is COMB(N,K) * D(N-K).
#
#  First values:
#
#     N         D(N)
#     0           1
#     1           0
#     2           1
#     3           2
#     4           9
#     5          44
#     6         265
#     7        1854
#     8       14833
#     9      133496
#    10     1334961
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
#  Input:
#
#    integer N, the number of objects to be permuted.
#
#  Output:
#
#    integer D(0:N), the number of derangements of N objects.
#
  import numpy as np

  d = np.zeros ( n + 1 )

  d[0] = 1
  d[1] = 0

  for i in range ( 2, n + 1 ):
    d[i] = ( i - 1 ) * ( d[i-1] + d[i-2] )

  return d

def derange_enum2_test ( ):

#*****************************************************************************80
#
## derange_enum2_test() tests derange_enum2().
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
  print ( '' )
  print ( 'derange_enum2_test():' )
  print ( '  derange_enum2() counts derangements;' )

  n = 10
  d = derange_enum2 ( n )

  print ( '' )
  print ( '  N    # of derangements' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    print ( '  %8d  %8d' % ( i, d[i] ) )

  return

def derange_enum3 ( n ):

#*****************************************************************************80
#
## derange_enum3() returns the number of derangements of N objects.
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#  Recursion:
#
#      D(0) = 1
#      D(1) = 0
#      D(2) = 1
#      D(N) = (N-1) * ( D(N-1) + D(N-2) )
#
#    or
#
#      D(0) = 1
#      D(1) = 0
#      D(N) = N * D(N-1) + (-1)^N
#
#  Formula:
#
#    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
#
#    Based on the inclusion/exclusion law.
#
#    D(N) is the number of ways of placing N non-attacking rooks on
#    an N by N chessboard with one diagonal deleted.
#
#    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
#
#    The number of permutations with exactly K items in the right
#    place is COMB(N,K) * D(N-K).
#
#  First values:
#
#     N         D(N)
#     0           1
#     1           0
#     2           1
#     3           2
#     4           9
#     5          44
#     6         265
#     7        1854
#     8       14833
#     9      133496
#    10     1334961
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
#    integer N, the number of objects to be permuted.
#
#  Output:
#
#    integer VALUE, the number of derangements of N objects.
#
  import math
  import numpy as np

  if ( n < 0 ):
    value = -1
  elif ( n == 0 ):
    value = 1
  elif ( n == 1 ):
    value = 0
  else:
    e = 2.718281828459045
    r = math.factorial ( n ) / e
    value = int ( r )

  return value

def derange_enum3_test ( ):

#*****************************************************************************80
#
## derange_enum3_test() tests derange_enum3().
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
  print ( '' )
  print ( 'derange_enum3_test():' )
  print ( '  derange_enum3() counts derangements;' )

  n = 10

  print ( '' )
  print ( '  N    # of derangements' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    print ( '  %8d  %8d' % ( i, derange_enum3 ( i ) ) )

  return

def derange_enum ( n ):

#*****************************************************************************80
#
## derange_enum() returns the number of derangements of N objects.
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#  Recursion:
#
#      D(0) = 1
#      D(1) = 0
#      D(2) = 1
#      D(N) = (N-1) * ( D(N-1) + D(N-2) )
#
#    or
#
#      D(0) = 1
#      D(1) = 0
#      D(N) = N * D(N-1) + (-1)^N
#
#  Formula:
#
#    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
#
#    Based on the inclusion/exclusion law.
#
#    D(N) is the number of ways of placing N non-attacking rooks on
#    an N by N chessboard with one diagonal deleted.
#
#    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
#
#    The number of permutations with exactly K items in the right
#    place is COMB(N,K) * D(N-K).
#
#  First values:
#
#     N         D(N)
#     0           1
#     1           0
#     2           1
#     3           2
#     4           9
#     5          44
#     6         265
#     7        1854
#     8       14833
#     9      133496
#    10     1334961
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
#  Input:
#
#    integer N, the number of objects to be permuted.
#
#  Output:
#
#    integer VALUE, the number of derangements of N objects.
#
  if ( n < 0 ):

    dn = -1

  elif ( n == 0 ):

    dn = 1

  elif ( n == 1 ):

    dn = 0

  elif ( n == 2 ):

    dn = 1

  else:

    dnm1 = 0
    dn = 1

    for i in range ( 3, n + 1 ):
      dnm2 = dnm1
      dnm1 = dn
      dn = ( i - 1 ) * ( dnm1 + dnm2 )

  value = dn

  return value

def derange_enum_test ( ):

#*****************************************************************************80
#
## derange_enum_test() tests derange_enum().
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
  n = 10

  print ( '' )
  print ( 'derange_enum_test():' )
  print ( '  derange_enum() counts derangements;' )
  print ( '' )
  print ( '  N    # of derangements' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    print ( '  %8d  %8d' % ( i, derange_enum ( i ) ) )

  return

def digit_to_ch ( digit ):

#*****************************************************************************80
#
## digit_to_ch() returns the character representation of a decimal digit.
#
#  Example:
#
#    DIGIT   C
#    -----  ---
#      0    '0'
#      1    '1'
#    ...    ...
#      9    '9'
#     17    '*'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIGIT, the digit value between 0 and 9.
#
#  Output:
#
#    character C, the corresponding character, or '*' if DIGIT
#    was illegal.
#
  if ( 0 <= digit and digit <= 9 ):
    i0 = ord ( '0' )
    c = chr ( i0 + digit )
  else:
    c = '*'

  return c

def digit_to_ch_test ( ):

#*****************************************************************************80
#
## digit_to_ch_test() tests digit_to_ch().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'digit_to_ch_test():' )
  print ( '  digit_to_ch() converts decimal digit -> character.' )
  print ( '' )
 
  for i in range ( -2, 12 ):
    c = digit_to_ch ( i )
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )

  return

def digraph_arc_euler ( nnode, nedge, inode, jnode ):

#*****************************************************************************80
#
## digraph_arc_euler() returns an Euler circuit in a digraph.
#
#  Description:
#
#    An Euler circuit of a digraph is a path which starts and ends at
#    the same node and uses each directed edge exactly once.  A digraph is
#    eulerian if it has an Euler circuit.  The problem is to decide whether
#    a given digraph is eulerian and to find an Euler circuit if the
#    answer is affirmative.
#
#    A digraph has an Euler circuit if and only if the number of incoming
#    edges is equal to the number of outgoing edges at each node.
#
#    This characterization gives a straightforward procedure to decide whether
#    a digraph is eulerian.  Furthermore, an Euler circuit in an eulerian
#    digraph G of NEDGE edges can be determined by the following method:
#
#      STEP 1: Choose any node U as the starting node, and traverse any edge
#      ( U, V ) incident to node U, and than traverse any unused edge incident
#      to node U.  Repeat this process of traversing unused edges until the
#      starting node U is reached.  Let P be the resulting walk consisting of
#      all used edges.  If all edges of G are in P, than stop.
#
#      STEP 2: Choose any unused edge ( X,  Y) in G such that X is
#      in P and Y is not in P.  Use node X as the starting node and
#      find another walk Q using all unused edges as in step 1.
#
#      STEP 3: Walk P and walk Q share a common node X, they can be merged
#      to form a walk R by starting at any node S of P and to traverse P
#      until node X is reached than, detour and traverse all edges of Q
#      until node X is reached and continue to traverse the edges of P until
#      the starting node S is reached.  Set P = R.
#
#      STEP 4: Repeat steps 2 and 3 until all edges are used.
#
#    The running time of the algorithm is O ( NEDGE ).
#
#    The digraph is assumed to be connected.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hang Tong Lau,
#    Algorithms on Graphs,
#    Tab Books, 1989.
#
#  Input:
#
#    integer NNODE, the number of nodes.
#
#    integer NEDGE, the number of edges.
#
#    integer INODE(NEDGE), JNODE(NEDGE) the I-th edge starts at node
#    INODE(I) and ends at node JNODE(I).
#
#  Output:
#
#    bool SUCCESS, is TRUE if an Euler circuit was found,
#    and FALSE otherwise.
#
#    integer TRAIL(NEDGE).  TRAIL(I) is the edge number of the I-th
#    edge in the Euler circuit.
#
  import numpy as np
#
#  Check if the digraph is eulerian.
#
  trail = np.zeros ( nedge, dtype = np.int32 )
  endnod = np.zeros ( nedge, dtype = np.int32 )

  for i in range ( 1, nedge + 1 ):
    j = inode[i-1]
    trail[j-1] = trail[j-1] + 1
    j = jnode[i-1]
    endnod[j-1] = endnod[j-1] + 1

  for i in range ( 1, nnode + 1 ):
    if ( trail[i-1] != endnod[i-1] ):
      success = False
      return success, trail
#
#  The digraph is eulerian find an Euler circuit.
#
  success = 1
  lensol = 1
  lenstk = 0
#
#  Find the next edge.
#
  stacks = np.zeros ( 2 * nedge, dtype = np.int32 )
  candid = np.zeros ( nedge, dtype = np.int32 )

  while ( True ):

    if ( lensol == 1 ):

      endnod[0] = inode[0]
      stacks[0] = 1
      stacks[1] = 1
      lenstk = 2

    else:

      l = lensol - 1

      if ( lensol != 2 ):
        endnod[l-1] = inode[trail[l-1]-1] + jnode[trail[l-1]-1] - endnod[l-2]

      k = endnod[l-1]

      for i in range ( 1, nedge + 1 ):
        candid[i-1] = ( k == jnode[i-1] )

      for i in range ( 1, l + 1 ):
        candid[trail[i-1]-1] = False

      lens = lenstk

      for i in range ( 1, nedge + 1 ):

        if ( candid[i-1] ):
          lens = lens + 1
          stacks[lens-1] = i

      stacks[lens] = lens - lenstk
      lenstk = lens + 1

    while ( True ):

      istak = stacks[lenstk-1]
      lenstk = lenstk - 1

      if ( istak != 0 ):
        break

      lensol = lensol - 1

      if ( lensol == 0 ):
        trail = i4vec_reverse ( nedge, trail )
        return success, trail

    trail[lensol-1] = stacks[lenstk-1]
    stacks[lenstk-1] = istak - 1

    if ( lensol == nedge ):
      break

    lensol = lensol + 1

  trail = i4vec_reverse ( nedge, trail )

  return success, trail

def digraph_arc_euler_test ( ):

#*****************************************************************************80
#
## digraph_arc_euler_test() calls digraph_arc_euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  nedge = 7
  nnode = 5

  inode = np.array ( [ 2, 1, 2, 1, 3, 5, 4 ], dtype = np.int32 )
  jnode = np.array ( [ 5, 4, 3, 2, 1, 1, 2 ], dtype = np.int32 )

  print ( '' )
  print ( 'digraph_arc_euler_test():' )
  print ( '  digraph_arc_euler() finds an Euler circuit of a digraph.' )

  digraph_arc_print ( nedge, inode, jnode, '  The arc list of the digraph:' )

  success, trail = digraph_arc_euler ( nnode, nedge, inode, jnode )

  if ( success ):

    i4vec_print ( nedge, trail, '  The edge list of the Euler circuit:' )

    print ( '' )
    print ( '  The node list of the Euler circuit:' )
    print ( '' )
    print ( '    I  Edge  Node' )
    print ( '' )

    for i in range ( 1, nedge + 1 ):

      j = trail[i-1]

      if ( i == nedge ):
        jp1 = trail[0]
      else:
        jp1 = trail[i]

      if ( jnode[j-1] == inode[jp1-1] ):
        inn = jnode[j-1]
      else:
        print ( '' )
        print ( 'The circuit has failed!' )
        break

      print ( '  %4d  %4d  %4d' % ( i, j, inn ) )

  else:

    print ( '' )
    print ( '  The digraph is not eulerian.' )
    print ( '' )

  return

def digraph_arc_print ( nedge, inode, jnode, title ):

#*****************************************************************************80
#
## digraph_arc_print() prints out a digraph from an edge list.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NEDGE, the number of edges.
#
#    integer INODE(NEDGE), JNODE(NEDGE), the beginning and end
#    nodes of the edges.
#
#    character TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  print ( '' )

  for i in range ( 0,  nedge ):
    print ( '  %4d    %4d  %4d' % ( i, inode[i], jnode[i] ) )

  return

def digraph_arc_print_test ( ):

#*****************************************************************************80
#
## digraph_arc_print_test() calls digraph_arc_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nedge = 7
  nnode = 5

  inode = np.array ( [ 2, 1, 2, 1, 3, 5, 4 ] )
  jnode = np.array ( [ 5, 4, 3, 2, 1, 1, 2 ] )

  print ( '' )
  print ( 'digraph_arc_print_test():' )
  print ( '  digraph_arc_print() prints a digraph.' )

  digraph_arc_print ( nedge, inode, jnode, '  The arc list of the digraph:' );

  return

def diophantine ( a, b, c ):

#*****************************************************************************80
#
## diophantine() solves a Diophantine equation A * X + B * Y = C.
#
#  Discussion:
#
#    Given integers A, B and C, produce X and Y so that
#
#      A * X + B * Y = C.
#
#    In general, the equation is solvable if and only if the
#    greatest common divisor of A and B also divides C.
#
#    A solution (X,Y) of the Diophantine equation also gives the solution
#    X to the congruence equation:
#
#      A * X = C mod ( B ).
#
#    Generally, if there is one nontrivial solution, there are an infinite
#    number of solutions to a Diophantine problem.
#    If (X0,Y0) is a solution, then so is ( X0+T*B/D, Y0-T*A/D ) where
#    T is any integer, and D is the greatest common divisor of A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998, page 446.
#
#  Input:
#
#    integer A, B, C, the coefficients of the Diophantine equation.
#
#  Output:
#
#    integer X, Y, the solution of the Diophantine equation.
#    Note that the algorithm will attempt to return a solution with
#    smallest Euclidean norm.
#
#    integer IERROR, error flag.
#    0, no error, X and Y were computed.
#    1, A = B = 0, C is nonzero.
#    2, A = 0, B and C nonzero, but C is not a multiple of B.
#    3, A nonzero, B zero, C nonzero, but C is not a multiple of A.
#    4, A, B, C nonzero, but GCD of A and B does not divide C.
#    5, the algorithm ran out of internal space.
#
  import numpy as np

  nmax = 100

  ierror = 0
  x = 0
  y = 0
#
#  Special cases.
#
  if ( a == 0 and b == 0 and c == 0 ):
    x = 0
    y = 0
    return x, y, ierror
  elif ( a == 0 and b == 0 and c != 0 ):
    ierror = 1
    x = 0
    y = 0
    return x, y, ierror
  elif ( a == 0 and b != 0 and c == 0 ):
    x = 0
    y = 0
    return x, y, ierror
  elif ( a == 0 and b != 0 and c != 0 ):
    x = 0
    y = c // b
    if ( ( c % b ) != 0 ):
      ierror = 2
    return x, y, ierror
  elif ( a != 0 and b == 0 and c == 0 ):
    x = 0
    y = 0
    return x, y, ierror
  elif ( a != 0 and b == 0 and c != 0 ):
    x = c / a
    y = 0
    if ( ( c % a ) != 0 ):
      ierror = 3
    return x, y, ierror
  elif ( a != 0 and b != 0 and c == 0 ):
    g = i4_gcd ( a, b )
    x = b // g
    y = - a // g
    return x, y, ierror
#
#  Now handle the "general" case: A, B and C are nonzero.
#
#  Step 1: Compute the GCD of A and B, which must also divide C.
#
  g = i4_gcd ( a, b )

  if ( ( c % g ) != 0 ):
    ierror = 4
    return x, y, ierror

  a_copy = a // g
  b_copy = b // g
  c_copy = c // g
#
#  Step 2: Split A and B into sign and magnitude.
#
  a_mag = abs ( a_copy )
  a_sign = i4_sign ( a_copy )
  b_mag = abs ( b_copy )
  b_sign = i4_sign ( b_copy )
#
#  Another special case, A_MAG = 1 or B_MAG = 1.
#
  if ( a_mag == 1 ):
    x = a_sign * c_copy
    y = 0
    return x, y, ierror
  elif ( b_mag == 1 ):
    x = 0
    y = b_sign * c_copy
    return x, y, ierror
#
#  Step 3: Produce the Euclidean remainder sequence.
#
  q = np.zeros ( nmax, dtype = np.int32 )

  if ( b_mag <= a_mag ):

    swap = False
    q[0] = a_mag
    q[1] = b_mag

  else:

    swap = True
    q[0] = b_mag
    q[1] = a_mag

  n = 2

  while ( True ):

    q[n] = ( q[n-2] % q[n-1] )

    if ( q[n] == 1 ):
      break

    n = n + 1

    if ( nmax <= n ):
      ierror = 5
      print ( '' )
      print ( 'diophantine(): Fatal error!' )
      print ( '  Exceeded number of iterations.' )
      raise Exception ( 'diophantine(): Fatal error!' )
#
#  Step 4: Now go backwards to solve X * A_MAG + Y * B_MAG = 1.
#
  y = 0
  for k in range ( n, 0, -1 ):
    x = y
    y = ( 1 - x * q[k-1] ) // q[k]
#
#  Step 5: Undo the swapping.
#
  if ( swap ):
    z = x
    x = y
    y = z
#
#  Step 6: Now apply signs to X and Y so that X * A + Y * B = 1.
#
  x = x * a_sign
  y = y * b_sign
#
#  Step 7: Multiply by C, so that X * A + Y * B = C.
#
  x = x * c_copy
  y = y * c_copy
#
#  Step 8: Given a solution (X,Y), try to find the solution of
#  minimal magnitude.
#
  x, y = diophantine_solution_minimize ( a_copy, b_copy, x, y )

  return x, y, ierror

def diophantine_test ( ):

#*****************************************************************************80
#
## diophantine_test() tests diophantine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 20

  a_test = np.array ( [ \
     1027,  1027,  1027, 1027, -1027,  -1027, -1027, -1027,    6,   0, \
        0,     0,     1,    1,     1,   1024,     0,     0,    5,   2 ] )
  b_test = np.array ( [ \
       712,   712, -712, -712,   712,    712,  -712,  -712,    8,   0, \
         1,     1,    0,    0,     1, -15625,     0,     3,    0,   4 ] )
  c_test = np.array ( [ \
         7,    -7,    7,   -7,     7,     -7,     7,    -7,   50,   0, \
         0,     1,    0,    1,     0,  11529,     1,    11,   19,   7 ] )

  print ( '' )
  print ( 'diophantine_test():' )
  print ( '  diophantine() solves a Diophantine equation:' )
  print ( '    A * X + B * Y = C' )
  print ( '' )
  print ( '        A         B         C         X     Y     Error' )
  print ( '' )

  for test_i in range ( 0, test_num ):

    a = a_test[test_i]
    b = b_test[test_i]
    c = c_test[test_i]

    x, y, ierror = diophantine ( a, b, c )

    if ( ierror != 0 ):
      print ( '  %8d  %8d  %8d  Error code = %d' % ( a, b, c, ierror ) )
    else:
      error = a * x + b * y - c
      print ( '  %8d  %8d  %8d  %8d  %8d  %8d' % ( a, b, c, x, y, error ) )

  return

def diophantine_solution_minimize ( a, b, x, y ):

#*****************************************************************************80
#
## diophantine_solution_minimize(): minimal solution of a Diophantine equation.
#
#  Discussion:
#
#    Given a solution (X,Y) of a Diophantine equation:
#
#      A * X + B * Y = C.
#
#    then there are an infinite family of solutions of the form
#
#      ( X(i), Y(i) ) = ( X + i * B, Y - i * A )
#
#    An integral solution of minimal Euclidean norm can be found by
#    tentatively moving along the vectors (B,-A) and (-B,A) one step
#    at a time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998, page 446.
#
#  Input:
#
#    integer A, B, the coefficients of the Diophantine equation.
#    A and B are assumed to be relatively prime.
#
#    integer X, Y, on a solution of the Diophantine equation.
#
#  Output:
#
#    integer X, Y, a solution of minimal Euclidean norm.
#

#
#  Compute the minimum for T real, and then look nearby.
#
  t = float ( - b * x + a * y ) / float ( a * a + b * b )

  x = x + int ( round ( t ) ) * b
  y = y - int ( round ( t ) ) * a
#
#  Look nearby.
#
  norm = x * x + y * y

  while ( True ):

    x2 = x + b
    y2 = y - a

    norm2 = x2 * x2 + y2 * y2

    if ( norm <= norm2 ):
      break

    x = x2
    y = y2
    norm = norm2

  while ( True ):

    x2 = x - b
    y2 = y + a

    norm2 = x2 * x2 + y2 * y2

    if ( norm <= norm2 ):
      break

    x = x2
    y = y2
    norm = norm2

  return x, y

def diophantine_solution_minimize_test ( ):

#*****************************************************************************80
#
## diophantine_solution_minimize_test() tests diophantine_solution_minimize().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'diophantine_solution_minimize_test():' )
  print ( '  diophantine_solution_minimize() computes a minimal' )
  print ( '  Euclidean norm solution of a Diophantine equation:' )
  print ( '    A * X + B * Y = C' )

  a = 4096
  b = -15625
  c = 46116
  x = 665499996
  y = 174456828

  r = a * x + b * y - c

  print ( '' )
  print ( '  Coefficients:' )
  print ( '    A = %12d' % ( a ) )
  print ( '    B = %12d' % ( b ) )
  print ( '    C = %12d' % ( c ) )
  print ( '  Solution:' )
  print ( '    X = %12d' % ( x ) )
  print ( '    Y = %12d' % ( y ) )
  print ( '  Residual R = A * X + B * Y - C:' )
  print ( '    R = %12d' % ( r ) )

  x, y = diophantine_solution_minimize ( a, b, x, y )

  r = a * x + b * y - c

  print ( '' )
  print ( '  The minimized solution:' )
  print ( '    X = %12d' % ( x ) )
  print ( '    Y = %12d' % ( y ) )
  print ( '  Residual R = A * X + B * Y - C:' )
  print ( '    R = %12d' % ( r ) )

  x = 15621
  y = 4092

  r = a * x + b * y - c

  print ( '' )
  print ( '  The minimal positive solution:' )
  print ( '    X = %12d' % ( x ) )
  print ( '    Y = %12d' % ( y ) )
  print ( '  Residual R = A * X + B * Y - C:' )
  print ( '    R = %12d' % ( r ) )

  return

def dvec_add ( n, dvec1, dvec2 ):

#*****************************************************************************80
#
## dvec_add() adds two (signed) decimal vectors.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10^(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#    N = 4
#
#      DVEC1     +   DVEC2     =   DVEC3
#
#    ( 0 0 1 7 ) + ( 0 1 0 4 ) = ( 0 0 1 2 1 )
#
#          17    +       104   =         121
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer DVEC1(N), DVEC2(N), the vectors to be added.
#
#  Output:
#
#    integer DVEC3(N), the sum of the two input vectors.
#
  import numpy as np

  base = 10
  overflow = 0

  dvec3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    dvec3[i] = dvec1[i] + dvec2[i]

  for i in range ( 0, n ):
    while ( base <= dvec3[i] ):
      dvec3[i] = dvec3[i] - base
      if ( i < n - 1 ):
        dvec3[i+1] = dvec3[i+1] + 1
      else:
        overflow = 1

  return dvec3

def dvec_add_test ( rng ):

#*****************************************************************************80
#
## dvec_add_test() tests dvec_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  test_num = 10

  print ( '' )
  print ( 'dvec_add_test():' )
  print ( '  dvec_add() adds decimal vectors representing integers' )
  print ( '' )
  print ( '        I        J        K = I + J' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i = rng.integers ( low = -100, high = 100, endpoint = True )
    j = rng.integers ( low = -100, high = 100, endpoint = True )

    print ( '' )

    print ( '  %8d  %8d' % ( i, j ) )

    k = i + j

    print ( '  Directly:           %8d' % ( k ) )

    dvec1 = i4_to_dvec ( i, n )
    dvec2 = i4_to_dvec ( j, n )

    dvec3 = dvec_add ( n, dvec1, dvec2 )
    k = dvec_to_i4 ( n, dvec3 )

    print ( '  dvec_add  %8d' % ( k ) )

  return

def dvec_complementx ( n, dvec1 ):

#*****************************************************************************80
#
## dvec_complementx() computes the ten's complement of a DVEC.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10**(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer DVEC1(N), the vector to be complemented.
#
#  Output:
#
#    integer DVEC2(N), the ten's complemented vector.
#
  import numpy as np

  base = 10

  dvec3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    dvec3[i] = ( base - 1 ) - dvec1[i]

  dvec4 = np.zeros ( n, dtype = np.int32 )
  dvec4[0] = 1

  dvec2 = dvec_add ( n, dvec3, dvec4 )

  return dvec2

def dvec_complementx_test ( rng ):

#*****************************************************************************80
#
## dvec_complementx_test() tests dvec_complementx();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  test_num = 5

  print ( '' )
  print ( 'dvec_complementx_test():' )
  print ( '  dvec_complementx() returns the ten\'s complement' )
  print ( '  of a (signed) decimal vector;' )

  for test in range ( 0, test_num ):
    
    i = rng.integers ( low = -100, high = 100, endpoint = True )

    dvec1 = i4_to_dvec ( i, n )

    dvec2 = dvec_complementx ( n, dvec1 )

    j = dvec_to_i4 ( n, dvec2 )

    print ( '' )
    print ( '  I = %8d' % ( i ) )
    print ( '  J = %8d' % ( j ) )

    dvec_print ( n, dvec1, '' )
    dvec_print ( n, dvec2, '' )

  return

def dvec_mul ( n, dvec1, dvec2 ):

#*****************************************************************************80
#
## dvec_mul() computes the product of two decimal vectors.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10^(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer DVEC1(N), DVEC2(N), the vectors to be multiplied.
#
#  Output:
#
#    integer DVEC3(N), the product of the two input vectors.
#
  import numpy as np

  base = 10
#
#  Record the sign of the product.
#  Make the factors positive.
#
  product_sign = 1

  if ( dvec1[n-1] != 0 ):
    product_sign = - product_sign
    dvec1 = dvec_complementx ( n, dvec1 )

  if ( dvec2[n-1] != 0 ):
    product_sign = - product_sign
    dvec2 = dvec_complementx ( n, dvec2 )

  dvec3 = np.zeros ( n )
#
#  Multiply.
#
  for i in range ( 0, n - 1 ):
    for j in range ( 0, n - 1 - i ):
      dvec3[i+j] = dvec3[i+j] + dvec1[i] * dvec2[j]
#
#  Take care of carries.
#
  for i in range ( 0, n - 1 ):

    carry = ( dvec3[i] // base )
    dvec3[i] = dvec3[i] - carry * base
#
#  Unlike the case of dvec_add, we do NOT allow carries into
#  the N-th position when multiplying.
#
    if ( i < n - 2 ):
      dvec3[i+1] = dvec3[i+1] + carry
#
#  Take care of the sign of the product.
#
  if ( product_sign < 0 ):
    dvec3 = dvec_complementx ( n, dvec3 )

  return dvec3

def dvec_mul_test ( rng ):

#*****************************************************************************80
#
## dvec_mul_test() tests dvec_mul();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  test_num = 10
  test2_num = 2

  print ( '' )
  print ( 'dvec_mul_test():' )
  print ( '  dvec_mul() multiplies decimal vectors' )
  print ( '  representing integers;' )

  for test2 in range ( 0, test2_num ):

    if ( test2 == 0 ):

      n2 = n

    elif ( test2 == 1 ):

      n2 = 6

      print ( '' )
      print ( '  NOW REPEAT THE TEST...' )
      print ( '' )
      print ( '  but use too few digits to represent big products.' )
      print ( '  This corresponds to an "overflow".' )
      print ( '  The result here should get the final decimal' )
      print ( '  digits correctly, though.' )

    print ( '' )
    print ( '        I        J        K = I * J' )

    for test in range ( 0, test_num ):
    
      i = rng.integers ( low = -1000, high = 1000, endpoint = True )
      j = rng.integers ( low = -1000, high = 1000, endpoint = True )

      print ( '' )

      print ( '  %8d  %8d' % ( i, j ) )

      k = i * j

      print ( '  Directly:           %8d' % ( k ) )

      dvec1 = i4_to_dvec ( i, n2 )
      dvec2 = i4_to_dvec ( j, n2 )
      dvec3 = dvec_mul ( n2, dvec1, dvec2 )
      k = dvec_to_i4 ( n2, dvec3 )

      print ( '  dvec_mul            %8d\n' % ( k ) )

  return

def dvec_print ( n, dvec, title ):

#*****************************************************************************80
#
## dvec_print() prints a DVEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real DVEC(N), the vector to be printed.
#
#  Output:
#
#    character TITLE, a title to be printed first.
#    TITLE may be blank.
#
  import sys

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
    print ( '' )

  if ( dvec[n-1] == 9 ):
    sys.stdout.write ( '-' )
  else:
    sys.stdout.write ( '+' )
 
  for i in range ( n - 2, -1, -1 ):
    sys.stdout.write ( str ( dvec[i] ) )
  print ( '' )

  return

def dvec_print_test ( ):

#*****************************************************************************80
#
## dvec_print_test() tests dvec_print();
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  dvec = np.array ( [ \
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \
    3, 4, 1, 7, 7, 5, 5, 0, 0, 9 ] )

  print ( '' )
  print ( 'dvec_print_test():' )
  print ( '  dvec_print() prints a (signed) decimal vector;' )

  n = 20
  dvec_print ( n, dvec, '  The DVEC:' )

  return

def dvec_sub ( n, dvec1, dvec2 ):

#*****************************************************************************80
#
## dvec_sub() subtracts two decimal vectors.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10**(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer DVEC1(N), DVEC2(N), the vectors to be subtracted.
#
#  Output:
#
#    integer DVEC3(N), the value of DVEC1 - DVEC2.
#
  dvec4 = dvec_complementx ( n, dvec2 )

  dvec3 = dvec_add ( n, dvec1, dvec4 )

  return dvec3

def dvec_sub_test ( rng ):

#*****************************************************************************80
#
## dvec_sub_test() tests dvec_sub();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  test_num = 10

  print ( '' )
  print ( 'dvec_sub_test():' )
  print ( '  dvec_sub() subtracts decimal vectors representing integers;' )
  print ( '' )
  print ( '        I        J        L = I - J' )

  for test in range ( 0, test_num ):
    
    i = rng.integers ( low = -100, high = 100, endpoint = True )
    j = rng.integers ( low = -100, high = 100, endpoint = True )

    print ( '' )
    print ( '  %8d  %8d' % ( i, j ) )

    l = i - j

    print ( '  Directly:           %8d' % ( l ) )

    dvec1 = i4_to_dvec ( i, n )
    dvec2 = i4_to_dvec ( j, n )

    dvec4 = dvec_sub ( n, dvec1, dvec2 )
    l = dvec_to_i4 ( n, dvec4 )

    print ( '  dvec_sub  %8d' % ( l ) )

  return

def dvec_to_i4 ( n, dvec ):

#*****************************************************************************80
#
## dvec_to_i4() makes an integer from a (signed) decimal vector.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10**(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer DVEC(N), the decimal representation.
#
#  Output:
#
#    integer VALUE, the integer.
#
  import numpy as np

  base = 10

  i_sign = 1

  if ( dvec[n-1] == base - 1 ):
    i_sign = -1
    dvec = dvec_complementx ( n, dvec )

  value = 0
  for j in range ( n - 2, -1, -1 ):
    value = base * value + dvec[j]

  value = i_sign * value

  return value

def dvec_to_i4_test ( rng ):

#*****************************************************************************80
#
## dvec_to_i4_test() tests dvec_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'dvec_to_i4_test():' )
  print ( '  dvec_to_i4() converts a DVEC to an I4.' )
  print ( '' )
  print ( '        I4 => DVEC => I4' )
  print ( '' )

  i1 = rng.integers ( low = -10000, high = 10000, endpoint = True )

  n = 6
  dvec = i4_to_dvec ( i1, n )

  i2 = dvec_to_i4 ( n, dvec )

  print ( '  %6d  ' % ( i1 ), end = '' )
  for i in range ( n - 1, -1, -1 ):
    print ( '%2d' % ( dvec[i] ), end = '' )
  print ( '  %6d' % ( i2 ) )

  return

def equiv0_next ( n, npart, jarray, iarray, more ):

#*****************************************************************************80
#
## equiv0_next() partitions a set into subsets whose first label is 0.
#
#  Discussion:
#
#    A partition of a set assigns each element to exactly one subset.
#
#    The number of partitions of a set of size N is the Bell number B(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
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
#    integer N, the number of elements in the set to be partitioned.
#
#    integer NPART, the number of subsets in the previous partition.
#
#    integer JARRAY(N), the number of elements in each subset
#    of the previous partition.
#
#    integer IARRAY(N), the subset to which each element belongs
#    in the previous partition.
#
#    bool MORE, is set to FALSE on the first call, and the
#    input values of NPART, JARRAY and IARRAY are not needed.  On subsequent
#    calls, MORE should be TRUE, and NPART, JARRAY, and IARRAY should have the
#    values of the output quantities NPART, JARRAY and IARRAY from
#    the previous call.
#
#  Output:
#
#    integer NPART, the number of subsets in the new partition.
#
#    integer JARRAY(N), the number of elements in each subset
#    of the new partition.
#
#    integer IARRAY(N), the subset to which each element belongs
#    in the new partition.
#
#    bool MORE, is TRUE as long as the new partition returned
#    is not the last one.  When MORE is returned FALSE, all the partitions
#    have been computed and returned.
#
  import numpy as np

  if ( not more ):

    npart = 1
    for i in range ( 0, n ):
      iarray[i] = 0
    jarray[0] = n
    for i in range ( 1, n ):
      jarray[i] = 0

  else:

    m = n

    while ( jarray[iarray[m-1]] == 1 ):
      iarray[m-1] = 0
      m = m - 1

    l = iarray[m-1] + 1
    npart = npart + m - n
    jarray[0] = jarray[0] + n - m

    if ( l == npart ):
      npart = npart + 1
      jarray[npart-1] = 0

    iarray[m-1] = l
    jarray[l-1] = jarray[l-1] - 1
    jarray[l] = jarray[l] + 1

  more = ( npart != n )

  return npart, jarray, iarray, more

def equiv0_next_test ( ):

#*****************************************************************************80
#
## equiv0_next_test() tests equiv0_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  n = 4
  npart = 0
  jarray = np.zeros ( n, dtype = np.int32 )
  a = np.zeros ( n, dtype = np.int32 )
  more = False

  print ( '' )
  print ( 'equiv0_next_test():' )
  print ( '  equiv0_next() generates all partitions of a set.' )
  print ( '' )
  print ( '          ', end = '' )
  for i in range ( 0, n ):
    print ( '  %4d' % ( i ), end = '' )
  print ( '' )
  print ( '' )
 
  rank = 0

  while ( True ):
 
    npart, jarray, a, more = equiv0_next ( n, npart, jarray, a, more )
 
    rank = rank + 1
    print ( '  %2d  %2d: ' % ( rank, npart ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )
 
    if ( not more ):
      break

  return

def equiv0_random ( n, rng ):

#*****************************************************************************80
#
## equiv0_random() randomly partitions a set into subset whose first label is 0.
#
#  Discussion:
#
#    The user does not control the number of parts in the partition.
#
#    The equivalence classes are numbered in no particular order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
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
#    integer N, the number of elements in the set to be partitioned.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer NPART, the number of classes or parts in the 
#    partition.  NPART will be between 1 and N.
#
#    integer A(N), indicates the class to which each element
#    is assigned.
#
  import numpy as np

  b = np.zeros ( n )

  b[0] = 1.0

  for l in range ( 1, n ):

    sum1 = 1.0 / float ( l )
    for k in range ( 1, l ):
      sum1 = ( sum1 + b[k-1] ) / float ( l - k )

    b[l] = ( sum1 + b[l-1] ) / float ( l + 1 )

  a = np.zeros ( n, dtype = np.int32 )

  m = n
  npart = 0

  while ( True ):

    z = rng.random ( )
    z = m * b[m-1] * z
    k = 0
    npart = npart + 1

    while ( 0.0 <= z ):

      a[m-1] = npart
      m = m - 1

      if ( m == 0 ):
        break

      z = z - b[m-1]
      k = k + 1
      z = z * k

    if ( m == 0 ):
      break
#
#  Randomly permute the assignments.
#
  for i in range ( 0, n ):
    j = rng.integers ( low = i, high = n, endpoint = False )
    t    = a[i]
    a[i] = a[j]
    a[j] = t

  return npart, a

def equiv0_random_test ( rng ):

#*****************************************************************************80
#
## equiv0_random_test() tests equiv0_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 4

  print ( '' )
  print ( 'equiv0_random_test():' )
  print ( '  equiv0_random() selects a random set partition.' )
 
  for i in range ( 0, 5 ):
 
    npart, a = equiv0_random ( n, rng )

    equiv_print2 ( n, a, '  The partition:' )

  return

def equiv1_next2 ( n, a, done ):

#*****************************************************************************80
#
## equiv1_next2() computes, one at a time, the partitions of a set.
#
#  Discussion:
#
#    A partition of a set assigns each element to exactly one subset.
#
#    The number of partitions of a set of size N is the Bell number B(N).
#
#    The entries of IARRAY are the partition subset to which each
#    element of the original set belongs.  If there are NPART distinct
#    parts of the partition, then each entry of IARRAY will be a
#    number between 1 and NPART.  Every number from 1 to NPART will
#    occur somewhere in the list.  If the entries of IARRAY are
#    examined in order, then each time a new partition subset occurs,
#    it will be the next unused integer.
#
#    For instance, for N = 4, the program will describe the set
#    where each element is in a separate subset as 1, 2, 3, 4,
#    even though such a partition might also be described as
#    4, 3, 2, 1 or even 1, 5, 8, 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements in the set.
#
#    integer A(N), the previous partition, that is, the output value
#    of A on the previous call.  On the first call, with DONE = TRUE,
#    the value of A is not needed.
#
#    bool DONE, should be set to TRUE for the first call, to set
#    up initialization, and should be FALSE thereafter.
#
#  Output:
#
#    integer A(N), the next partition.
#
#    bool DONE, is TRUE if there are more partitions to generate.
#
  if ( done ):

    done = False
    for i in range ( 0, n ):
      a[i] = 1

  else:
#
#  Find the last element J that can be increased by 1.
#  This is the element that is not equal to its maximum possible value,
#  which is the maximum value of all preceding elements +1.
#
    jmax = a[0]
    imax = 0

    for j in range ( 1, n ):

      if ( jmax < a[j] ):
        jmax = a[j]
      else:
        imax = j
#
#  If no element can be increased by 1, we are done.
#
    if ( imax == 0 ):
      done = True
      return a, done
#
#  Increase the value of the IMAX-th element by 1, set its successors to 1.
#
    done = False
    a[imax] = a[imax] + 1
    for j in range ( imax + 1, n ):
      a[j] = 1

  return a, done

def equiv1_next2_test ( ):

#*****************************************************************************80
#
## equiv1_next2_test() tests equiv1_next2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  a = np.zeros ( n )
  done = True

  print ( '' )
  print ( 'equiv1_next2_test():' )
  print ( '  equiv1_next2() generates all partitions of a set.' )
  print ( '  Here, N = ', n )
  print ( ' ' )
  print ( '      ', end = '' )
  for i in range ( 0, n ):
    print ( '  %4d' % ( i ), end = '' )
  print ( '' )
  print ( '' )
 
  rank = 0

  while ( True ):

    a, done = equiv1_next2 ( n, a, done )

    if ( done ):
      break

    rank = rank + 1
    print ( '  %2d: ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )

  return

def equiv1_next ( n, npart, jarray, iarray, more ):

#*****************************************************************************80
#
## equiv1_next() partitions a set into subsets whose first label is 1.
#
#  Discussion:
#
#    A partition of a set assigns each element to exactly one subset.
#
#    The number of partitions of a set of size N is the Bell number B(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
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
#    integer N, the number of elements in the set to be partitioned.
#
#    integer NPART, the number of subsets in the previous partition.
#
#    integer JARRAY(N), the number of elements in each subset
#    of the previous partition.
#
#    integer IARRAY(N), the subset to which each element belongs
#    in the previous partition.
#
#    bool MORE, is set to FALSE on the first call, and the
#    input values of NPART, JARRAY and IARRAY are not needed.  On subsequent
#    calls, MORE should be TRUE, and NPART, JARRAY, and IARRAY should have the
#    values of the output quantities NPART, JARRAY and IARRAY from
#    the previous call.
#
#  Output:
#
#    integer NPART, the number of subsets in the new partition.
#
#    integer JARRAY(N), the number of elements in each subset
#    of the new partition.
#
#    integer IARRAY(N), the subset to which each element belongs
#    in the new partition.
#
#    bool MORE, is TRUE as long as the new partition returned
#    is not the last one.  When MORE is returned FALSE, all the partitions
#    have been computed and returned.
#
  import numpy as np

  if ( not more ):

    npart = 1
    for i in range ( 0, n ):
      iarray[i] = 1
    jarray[0] = n
    for i in range ( 1, n ):
      jarray[i] = 0

  else:

    m = n

    while ( jarray[iarray[m-1]-1] == 1 ):
      iarray[m-1] = 1
      m = m - 1

    l = iarray[m-1]
    npart = npart + m - n
    jarray[0] = jarray[0] + n - m

    if ( l == npart ):
      npart = npart + 1
      jarray[npart-1] = 0

    iarray[m-1] = l + 1
    jarray[l-1] = jarray[l-1] - 1
    jarray[l+1-1] = jarray[l+1-1] + 1

  more = ( npart != n )

  return npart, jarray, iarray, more

def equiv1_next_test ( ):

#*****************************************************************************80
#
## equiv1_next_test() tests equiv1_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  npart = 0
  jarray = np.zeros ( n, dtype = np.int32 )
  a = np.zeros ( n, dtype = np.int32 )
  more = False

  print ( '' )
  print ( 'equiv1_next_test():' )
  print ( '  equiv1_next() generates all partitions of a set.' )
  print ( '' )
  print ( '          ', end = '' )
  for i in range ( 0, n ):
    print ( '  %4d' % ( i ), end = '' )
  print ( '' )
  print ( '' )
 
  rank = 0

  while ( True ):
 
    npart, jarray, a, more = equiv1_next ( n, npart, jarray, a, more )
 
    rank = rank + 1
    print ( '  %2d  %2d: ' % ( rank, npart ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )
 
    if ( not more ):
      break

  return

def equiv_print2 ( n, s, title ):

#*****************************************************************************80
#
## equiv_print2() prints a partition of a set.
#
#  Discussion:
#
#    The partition is printed using the parenthesis format.
#
#    For example, here are the partitions of a set of 4 elements:
#
#      (1,2,3,4)
#      (1,2,3)(4)
#      (1,2,4)(3)
#      (1,2)(3,4)
#      (1,2)(3)(4)
#      (1,3,4)(2)
#      (1,3)(2,4)
#      (1,3)(2)(4)
#      (1,4)(2,3)
#      (1)(2,3,4)
#      (1)(2,3)(4)
#      (1,4)(2)(3)
#      (1)(2,4)(3)
#      (1)(2)(3,4)
#      (1)(2)(3)(4)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements in the set.
#
#    integer S(N), defines the partition.  
#    Element I belongs to subset S(I).
#
#    string TITLE, a title to be printed first.
#
  import numpy as np

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  print ( '' )
  s_min = np.min ( s )
  s_max = np.max ( s )

  for j in range ( s_min, s_max + 1 ):

    print ( 'subset %d: ('% ( j ), end = '' )
    size = 0
    for i in range ( 0, n ):
      if ( s[i] == j ):
        if ( 0 < size ):
          print ( ',', end = '' )
        print ( '%d' % ( i ), end = '' )
        size = size + 1
    print ( ')' )

  return

def equiv_print2_test ( rng ):

#*****************************************************************************80
#
## equiv_print2_test() tests equiv_print2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 4

  print ( '' )
  print ( 'equiv_print2_test():' )
  print ( '  equiv_print2() prints a set partition.' )
 
  for i in range ( 0, 5 ):
 
    npart, a = equiv0_random ( n, rng )

    equiv_print2 ( n, a, '  The partition:' )

  return

def equiv_print ( n, iarray, title ):

#*****************************************************************************80
#
## equiv_print() prints a partition of a set.
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
#    integer N, number of elements in set to be partitioned.
#
#    integer IARRAY(N), defines the partition or set of equivalence
#    classes.  Element I belongs to subset IARRAY(I).
#
#    string TITLE, a title to be printed first.
#    TITLE may be blank.
#
  import numpy as np

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  print ( '' )
  print ( '   Set  Size' )

  s_min = np.min ( iarray )
  s_max = np.max ( iarray )

  karray = np.zeros ( n )

  for s in range ( s_min, s_max + 1 ):

    k = 0

    for j in range ( 0, n ):

      if ( iarray[j] == s ):
        karray[k] = j;
        k = k + 1

    if ( 0 < k ):
      print ( '  %4d  %4d :: ' % ( s, k ), end = '' )
      for j in range ( 0, k ):
        print ( '%4d' % ( karray[j] ), end = '' )
      print ( '' )

  return

def equiv_print_test ( rng ):

#*****************************************************************************80
#
## equiv_print_test() tests equiv_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
# 
#  Input:
#
#    rng(): the current random number generator.
#
  n = 4

  print ( '' )
  print ( 'equiv_print_test():' )
  print ( '  equiv_print() prints a set partition.' )
 
  for i in range ( 0, 5 ):
 
    npart, a = equiv0_random ( n, rng )

    equiv_print ( n, a, '  The partition:' )

  return

def euler_row ( n ):

#*****************************************************************************80
#
## euler_row() returns the N-th row of Euler's triangle.
#
#  Discussion:
#
#    E(N,K) counts the number of permutations of the N digits that have
#    exactly K "ascents", that is, K places where the Ith digit is
#    less than the (I+1)th digit.
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
#    integer N, the row of Euler's triangle desired.
#
#  Output:
#
#    integer A[0:N], the N-th row of Euler's
#    triangle, A(K+1) contains the value of E(N,K).  Note
#    that A(1) should be 1 and A(N+1) should be 0.
#
  import numpy as np

  a = np.zeros ( n + 1 )

  a[0] = 1

  if ( 0 < n ):
    a[1] = 0
    for irow in range ( 2, n + 1 ):
      a[irow] = 0
      for k in range ( irow - 1, 0, -1 ):
        a[k] = ( k + 1 ) * a[k] + ( irow - k ) * a[k-1]
      a[0] = 1

  return a

def euler_row_test ( ):

#*****************************************************************************80
#
## euler_row_test() tests euler_row().
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
  nmax = 9

  print ( '' )
  print ( 'euler_row_test():' )
  print ( '  euler_row() gets rows of Euler\'s triangle.' )
  print ( '' )

  for n in range ( 0, nmax + 1 ):
    ieuler = euler_row ( n )
    for i in range ( 0, n + 1 ):
      print ( '  %d' % ( ieuler[i] ), end = '' )
    print ( '' )

  return

def frobenius_number_order2 ( c1, c2 ):

#*****************************************************************************80
#
## frobenius_number_order2() returns the Frobenius number for order 2.
#
#  Discussion:
#
#    The Frobenius number of order N is the solution of the Frobenius
#    coin sum problem for N coin denominations.
#
#    The Frobenius coin sum problem assumes the existence of
#    N coin denominations, and asks for the largest value that cannot
#    be formed by any combination of coins of these denominations.
#
#    The coin denominations are assumed to be distinct positive integers.
#
#    For general N, this problem is fairly difficult to handle.
#
#    For N = 2, it is known that:
#
#    * if C1 and C2 are not relatively prime, then
#      there are infinitely large values that cannot be formed.
#
#    * otherwise, the largest value that cannot be formed is
#      C1 * C2 - C1 - C2, and that exactly half the values between
#      1 and C1 * C2 - C1 - C2 + 1 cannot be represented.
#
#    As a simple example, if C1 = 2 and C2 = 7, then the largest
#    unrepresentable value is 5, and there are (5+1)/2 = 3
#    unrepresentable values, namely 1, 3, and 5.
#
#    For a general N, and a set of coin denominations C1, C2, ..., CN,
#    the Frobenius number F(N, C(1:N) ) is defined as the largest value
#    B for which the equation
#
#      C1*X1 + C2*X2 + ... + CN*XN = B
#
#    has no nonnegative integer solution X(1:N).
#
#    In the Mathematica Package "NumberTheory", the Frobenius number
#    can be determined by
#
#    <<NumberTheory`Frobenius`
#    FrobeniusF[ {C1,...,CN} ]
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
#    James Sylvester,
#    Question 7382,
#    Mathematical Questions with their Solutions,
#    Educational Times,
#    Volume 41, page 21, 1884.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer C1, C2, the coin denominations. C1 and C2
#    should be positive and relatively prime.
#
#  Output:
#
#    integer VALUE, the Frobenius number of (C1,C2).
#
  if ( c1 <= 0 ):
    value = i4_huge ( )
  elif ( c2 <= 0 ):
    value = i4_huge ( )
  elif ( i4_gcd ( c1, c2 ) != 1 ):
    value = i4_huge ( )
  else:
    value = c1 * c2 - c1 - c2

  return value

def frobenius_number_order2_test ( ):

#*****************************************************************************80
#
## frobenius_number_order2_test() tests frobenius_number_order2().
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
  print ( '' )
  print ( 'frobenius_number_order2_test():' )
  print ( '  frobenius_number_order2() computes Frobenius numbers of order 2.' )
  print ( '' )
  print ( '        C1        C1   exact F  computed F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, c1, c2, f1 = frobenius_number_order2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = frobenius_number_order2 ( c1, c2 )

    print ( '  %8d  %8d  %8d  %8d' % ( c1, c2, f1, f2 ) )

  return

def frobenius_number_order2_values ( n_data ):

#*****************************************************************************80
#
## frobenius_number_order2_values() returns values of the order 2 Frobenius number.
#
#  Discussion:
#
#    The Frobenius number of order N is the solution of the Frobenius
#    coin sum problem for N coin denominations.
#
#    The Frobenius coin sum problem assumes the existence of
#    N coin denominations, and asks for the largest value that cannot
#    be formed by any combination of coins of these denominations.
#
#    The coin denominations are assumed to be distinct positive integers.
#
#    For general N, this problem is fairly difficult to handle.
#
#    For N = 2, it is known that:
#
#    * if C1 and C2 are not relatively prime, then
#      there are infinitely large values that cannot be formed.
#
#    * otherwise, the largest value that cannot be formed is
#      C1 * C2 - C1 - C2, and that exactly half the values between
#      1 and C1 * C2 - C1 - C2 + 1 cannot be represented.
#
#    As a simple example, if C1 = 2 and C2 = 7, then the largest
#    unrepresentable value is 5, and there are (5+1)/2 = 3
#    unrepresentable values, namely 1, 3, and 5.
#
#    For a general N, and a set of coin denominations C1, C2, ..., CN,
#    the Frobenius number F(N, C(1:N) ) is defined as the largest value
#    B for which the equation
#
#      C1*X1 + C2*X2 + ... + CN*XN = B
#
#    has no nonnegative integer solution X(1:N).
#
#    In Mathematica, the Frobenius number can be determined by
#
#      FrobeniusNumber[ {C1,...,CN} ]
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
#    Gerard Cornuejols, Regina Urbaniak, Robert Weismantel, Laurence Wolsey,
#    Decomposition of Integer Programs and of Generating Sets,
#    in Algorithms - ESA '97,
#    Lecture Notes in Computer Science 1284,
#    edited by Rainer Burkard, G Woeginger,
#    Springer, 1997, pages 92-103,
#    LC: QA76.9.A43.E83.
#
#    Robert Owens,
#    An Algorithm to Solve the Frobenius Problem,
#    Mathematics Magazine,
#    Volume 76, Number 4, October 2003, 264-275.
#
#    James Sylvester,
#    Question 7382,
#    Mathematical Questions with their Solutions,
#    Educational Times,
#    Volume 41, page 21, 1884.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer C1, C2, the arguments of the function.
#
#    integer F, the value of the function.
#
  import numpy as np

  n_max = 6

  c1_vec = np.array ( ( 2,  3,  4,  5,  12,  99 ) )
  c2_vec = np.array ( ( 5,  17,  19,  13,  11,  100 ) )
  f_vec = np.array ( ( 3,  31,  53,  47,  109,  9701 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    c1 = 0
    c2 = 0
    f = 0
  else:
    c1 = c1_vec[n_data]
    c2 = c2_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, c1, c2, f

def frobenius_number_order2_values_test ( ):

#*****************************************************************************80
#
## frobenius_number_order2_values_test() tests frobenius_number_order2_values().
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
  print ( '' )
  print ( 'frobenius_number_order2_values_test():' )
  print ( '  frobenius_number_order2_values() returns values of' )
  print ( '  the Frobenius number of order 2.' )
  print ( '' )
  print ( '         C1        C2          F(C1,C2)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, c1, c2, f = frobenius_number_order2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %8d  %8d' % ( c1, c2, f ) )

  return

def gray_next ( n, change, k, a ):

#*****************************************************************************80
#
## gray_next() generates the next Gray code by switching one item at a time.
#
#  Discussion:
#
#    On the first call only, the user must set CHANGE = -N.
#    This initializes the routine to the Gray code for N zeroes.
#
#    Each time it is called thereafter, it returns in CHANGE the index
#    of the item to be switched in the Gray code.  The sign of CHANGE
#    indicates whether the item is to be added or subtracted (or
#    whether the corresponding bit should become 1 or 0).  When
#    CHANGE is equal to N+1 on all the Gray codes have been
#    generated.
#
#  Example:
#
#    N  CHANGE         Subset in/out   Binary Number
#                      Interpretation  Interpretation
#                       1 2 4 8
#   --  ---------      --------------  --------------
#
#    4   -4 / 0         0 0 0 0         0
#
#        +1             1 0 0 0         1
#          +2           1 1 0 0         3
#        -1             0 1 0 0         2
#            +3         0 1 1 0         6
#        +1             1 1 1 0         7
#          -2           1 0 1 0         5
#        -1             0 0 1 0         4
#              +4       0 0 1 1        12
#        +1             1 0 1 1        13
#          +2           1 1 1 1        15
#        -1             0 1 1 1        14
#            -3         0 1 0 1        10
#        +1             1 1 0 1        11
#          -2           1 0 0 1         9
#        -1             0 0 0 1         8
#              -4       0 0 0 0         0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
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
#    integer N, the order of the total set from which
#    subsets will be drawn.
#
#    integer CHANGE.  This is an input item only
#    on the first call for a particular sequence of Gray codes,
#    at which time it must be set to -N.  This corresponds to
#    all items being excluded, or all bits being 0, in the Gray code.
#
#    integer K, a bookkeeping variable.
#    The user must declare this variable before the first call.
#    The output value from one call should be the input value for the next.
#    The user should not change this variable.
#
#    integer A(N), a bookkeeping variable.
#    The user must declare this variable before the first call.
#    The output value from one call should be the input value for the next.
#    The user should not change this variable.
#
#  Output:
#
#    integer CHANGE, indicates which of the N items must be
#    "changed", and the sign indicates whether the item is to be added
#    or removed (or the bit is to become 1 or 0).  Note that on return from
#    the first call only, CHANGE has the value 0, indicating
#    that the first set is the empty set, or the number 0.
#
#    integer K, a bookkeeping variable.
#
#    integer A(N), a bookkeeping variable.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'gray_next(): Fatal error!' )
    print ( '  Input value of N <= 0.' )
    raise Exception ( 'gray_next(): Fatal error!' )

  if ( change == - n ):
    change = 0
    k = 1
    for i in range ( 0, n ):
      a[i] = 0
    return change, k, a
#
#  First determine WHICH item is to be changed.
#
  if ( ( k % 2 ) == 1 ):

    change = 1

  else:

    for i in range ( 0, n ):
      if ( a[i] == 1 ):
        change = i + 2
        break
#
#  Take care of the terminal case CHANGE = N.
#
  if ( change == n + 1 ):
    change = n
#
#  Now determine HOW the item is to be changed.
#
  if ( a[change-1] == 0 ):
    a[change-1] = 1
  elif ( a[change-1] == 1 ):
    a[change-1] = 0
    change = - change
#
#  Update the counter.
#
  k = k + 1
#
#  If the output CHANGE = -N, then we're done.
#
  if ( change == - n ):
    k = 0

  return change, k, a

def gray_next_test ( ):

#*****************************************************************************80
#
## gray_next_test() tests gray_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gray_next_test():' )
  print ( '  gray_next() returns the index of the single item' )
  print ( '  to be changed in order to get the next Gray code.' )
  print ( '' )
  print ( '   K  Change  Gray Code' )
  print ( '' )

  n = 4
  change = -n
  k = 0
  a = np.zeros ( n )

  g = np.zeros ( n )

  while ( True ):

    change, k, a = gray_next ( n, change, k, a )

    if ( change == -n ):
      break
    elif ( change == 0 ):
      for i in range ( 0, n ):
        g[i] = 0
    else:
      g[abs(change)-1] = 1 - g[abs(change)-1]

    print ( '  %2d  %6d  ' % ( k, change ), end = '' )
    for i in range ( 0, n ):
      print ( '%d' % ( g[i] ), end = '' )
    print ( '' )

  return

def gray_rank2 ( gray ):

#*****************************************************************************80
#
## gray_rank2() ranks a Gray code.
#
#  Discussion:
#
#    In contrast to gray_rank, this routine is entirely arithmetical,
#    and does not require access to bit testing and setting routines.
#
#
#    Given the number GRAY, its ranking is the order in which it would be
#    visited in the Gray code ordering.  The Gray code ordering begins
#
#    Rank  Gray  Gray
#          (Dec) (Bin)
#
#       0     0  0000
#       1     1  0001
#       2     3  0011
#       3     2  0010
#       4     6  0110
#       5     7  0111
#       6     5  0101
#       7     4  0100
#       8    12  0110
#       etc
#
#   This routine is given a Gray code, and has to return the rank.
#
#  Example:
#
#    Gray  Gray  Rank
#    (Dec) (Bin)
#
#     0       0     0
#     1       1     1
#     2      10     3
#     3      11     2
#     4     100     7
#     5     101     6
#     6     110     4
#     7     111     5
#     8    1000    15
#     9    1001    14
#    10    1010    12
#    11    1011    13
#    12    1100     8
#    13    1101     9
#    14    1110    11
#    15    1111    10
#    16   10000    31
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer GRAY, the Gray code to be ranked.
#
#  Output:
#
#    integer RANK, the rank of GRAY, and the integer whose Gray
#    code is GRAY.
#
  if ( gray < 0 ):
    print ( '' )
    print ( 'gray_rank2(): Fatal error!' )
    print ( '  Input value of GRAY < 0.' )
    raise Exception ( 'gray_rank2(): Fatal error!' )

  if ( gray == 0 ):
    rank = 0
    return rank
#
#  Find TWO_K, the largest power of 2 less than or equal to GRAY.
#
  k = 0
  two_k = 1
  while ( 2 * two_k <= gray ):
    two_k = two_k * 2
    k = k + 1

  rank = two_k
  last = 1
  gray = gray - two_k

  while ( 0 < k ):

    two_k = ( two_k // 2 )
    k = k - 1

    next = ( two_k <= gray and gray < two_k * 2 )

    if ( next ):
      gray = gray - two_k

    if ( next != last ):
      rank = rank + two_k
      last = 1
    else:
      last = 0

  return rank

def gray_rank2_test ( ):

#*****************************************************************************80
#
## gray_rank2_test() tests gray_rank2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gray_rank2_test():' )
  print ( '  gray_rank2() ranks a Gray code;' )
  print ( '' )
  print ( '    R  =                         RANK' )
  print ( '    G  =            gray_unrank2(RANK)' )
  print ( '    R2 = gray_rank2(gray_unrank2(RANK))' )
  print ( '' )
  print ( '       R       G       R2' )
  print ( '' )

  for rank in range ( 0, 25 ):
    gray = gray_unrank2 ( rank )
    rank2 = gray_rank2 ( gray )
    print ( '  %6d  %6d  %6d' % ( rank, gray, rank2 ) )

  return

def gray_unrank2 ( rank ):

#*****************************************************************************80
#
## gray_unrank2() unranks a Gray code.
#
#  Discussion:
#
#    In contrast to gray_unrank, this routine is entirely arithmetical,
#    and does not require access to bit testing and setting routines.
#
#    The binary values of the Gray codes of successive integers differ in
#    just one bit.
#
#    The sequence of Gray codes for 0 to (2^N)-1 can be interpreted as a
#    Hamiltonian cycle on a graph of the cube in N dimensions.
#
#  Example:
#
#    Rank  Gray  Gray
#          (Dec) (Bin)
#
#     0     0       0
#     1     1       1
#     2     3      11
#     3     2      10
#     4     6     110
#     5     7     111
#     6     5     101
#     7     4     100
#     8    12    1100
#     9    14    1001
#    10    12    1010
#    11    13    1011
#    12     8    1100
#    13     9    1101
#    14    11    1110
#    15    10    1111
#    16    31   10000
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer RANK, the integer whose Gray code is desired.
#
#  Output:
#
#    integer GRAY, the Gray code of the given rank.
#
  if ( rank <= 0 ):
    gray = 0
    return gray

  k = 0
  two_k = 1
  while ( 2 * two_k <= rank ):
    two_k = two_k * 2
    k = k + 1

  gray = two_k
  rank = rank - two_k
  next = 1

  while ( 0 < k ):

    two_k = ( two_k // 2 )
    k = k - 1

    last = next
    next = ( two_k <= rank and rank <= two_k * 2 )

    if ( next != last ):
      gray = gray + two_k

    if ( next ):
      rank = rank - two_k

  return gray

def gray_unrank2_test ( ):

#*****************************************************************************80
#
## gray_unrank2_test() tests gray_unrank2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gray_unrank2_test():' )
  print ( '  gray_unrank2() unranks a Gray code.' )
  print ( '' )
  print ( '    R  =                         RANK' )
  print ( '    G  =            gray_unrank2(RANK)' )
  print ( '    R2 = gray_rank2(gray_unrank2(RANK))' )
  print ( '' )
  print ( '       R       G       R2' )
  print ( '' )

  for rank in range ( 0, 25 ):
    gray = gray_unrank2 ( rank )
    rank2 = gray_rank2 ( gray )
    print ( '  %6d  %6d  %6d' % ( rank, gray, rank2 ) )

  return

def i4_bclr ( i4, pos ):

#*****************************************************************************80
#
## i4_bclr() returns a copy of an I4 in which the POS-th bit is set to 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 20145
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Input:
#
#    integer I4, the integer to be tested.
#
#    integer POS, the bit position, between 0 and 31.
#
#  Output:
#
#    integer VALUE, a copy of I4, with the POS-th bit set to 0.
#
  i4_huge = 2147483647

  value = i4

  if ( pos < 0 ):
    pass
  elif ( pos < 31 ):

    sub = 1

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )
      sub = sub * 2

    if ( ( j % 2 ) == 1 ):
      value = i4 - sub

  elif ( pos == 31 ):

    if ( i4 < 0 ):
      value = ( i4_huge + i4 ) + 1

  elif ( 31 < pos ):

    value = i4

  return value

def i4_bclr_test ( ):

#*****************************************************************************80
#
## i4_bclr_test() tests i4_bclr().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 2

  i4_test = np.array ( [ 101, -31 ], dtype = np.int32 )

  print ( '' )
  print ( 'i4_bclr_test():' )
  print ( '  i4_bclr() sets a given bit to 0.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     i4_bclr(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bclr ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )

  return

def i4_bset ( i4, pos ):

#*****************************************************************************80
#
## i4_bset() returns a copy of an I4 in which the POS-th bit is set to 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Input:
#
#    integer I4, the integer to be tested.
#
#    integer POS, the bit position, between 0 and 31.
#
#  Output:
#
#    integer VALUE, a copy of I4, but with the POS-th bit set to 1.
#
  i4_huge = 2147483647

  value = i4

  if ( pos < 0 ):

    pass

  elif ( pos < 31 ):

    add = 1

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )
      add = add * 2

    if ( ( j % 2 ) == 0 ):
      value = i4 + add

  elif ( pos == 31 ):

    if ( 0 < i4 ):
      value = - ( i4_huge - i4 ) - 1

  elif ( 31 < pos ):

    value = i4

  return value

def i4_bset_test ( ):

#*****************************************************************************80
#
## i4_bset_test() tests i4_bset().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 2

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'i4_bset_test():' )
  print ( '  i4_bset() sets a given bit to 1.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     i4_bset(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bset ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )

  return

def i4_btest ( i4, pos ):

#*****************************************************************************80
#
## i4_btest() returns TRUE if the POS-th bit of an I4 is 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Input:
#
#    integer I4, the integer to be tested.
#
#    integer POS, the bit position, between 0 and 31.
#
#  Output:
#
#    logical VALUE, is TRUE if the POS-th bit of I4 is 1.
#
  i4_huge = 2147483647

  if ( pos < 0 ):

    print ( '' )
    print ( 'i4_btest(): Fatal error!' )
    print ( '  POS < 0.' )
    raise Exception ( 'i4_btest(): Fatal error!' )

  elif ( pos < 31 ):

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )

    if ( ( j % 2 ) == 0 ):
      value = False
    else:
      value = True

  elif ( pos == 31 ):

    if ( i4 < 0 ):
      value = True
    else:
      value = False

  elif ( 31 < pos ):

    print ( '' )
    print ( 'i4_btest(): Fatal error!' )
    print ( '  31 < POS.' )
    raise Exception ( 'i4_btest(): Fatal error!' )

  return value

def i4_btest_test ( ):

#*****************************************************************************80
#
## i4_btest_test() tests i4_btest().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'i4_btest_test():' )
  print ( '  i4_btest() reports whether a given bit is 0 or 1.' )

  for test in range ( 0, 2 ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Analyze the integer I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     i4_btest(I4,POS)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_btest ( i4, pos )

      print ( '  %12d             %s' % ( pos, j ) )

  return

def i4_choose ( n, k ):

#*****************************************************************************80
#
## i4_choose() computes the binomial coefficient C(N,K) as an I4.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in integer arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#    Instead of i4_choose(), you could use scipy.special.comb ( n, k ),
#    except that that function uses real arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    ML Wolfson, HV Wright,
#    Algorithm 160:
#    Combinatorial of M Things Taken N at a Time,
#    Communications of the ACM,
#    Volume 6, Number 4, April 1963, page 161.
#
#  Input:
#
#    integer N, K, are the values of N and K.
#
#  Output:
#
#    integer VALUE, the number of combinations of N
#    things taken K at a time.
#
  mn = min ( k, n - k )
  mx = max ( k, n - k )

  if ( mn < 0 ):

    value = 0

  elif ( mn == 0 ):

    value = 1

  else:

    value = mx + 1

    for i in range ( 2, mn + 1 ):
      value = ( value * ( mx + i ) ) // i

  return value

def i4_choose_test ( ):

#*****************************************************************************80
#
## i4_choose_test() tests i4_choose().
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
  print ( '' )
  print ( 'i4_choose_test():' )
  print ( '  i4_choose() evaluates C(N,K).' )
  print ( '' )
  print ( '       N       K     CNK' )

  for n in range ( 0, 5 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = i4_choose ( n, k )

      print ( '  %6d  %6d  %6d' % ( n, k, cnk ) )

  return

def i4_factor ( n ):

#*****************************************************************************80
#
## i4_factor() factors an integer into prime factors.
#
#  Discussion:
#
#    N = NLEFT * Product ( 1 <= I <= NFACTOR ) FACTOR(I)^EXPONENT(I).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be factored.  N may be positive,
#    negative, or 0.
#
#  Output:
#
#    integer NFACTOR, the number of prime factors of N discovered
#    by the routine.
#
#    integer FACTOR(NFACTOR), the prime factors of N.
#
#    integer EXPONENT(NFACTOR).  EXPONENT(I) is the power of
#    the FACTOR(I) in the representation of N.
#
#    integer NLEFT, the factor of N that the routine could not
#    divide out.  If NLEFT is 1, then N has been completely factored.
#    Otherwise, NLEFT represents factors of N involving large primes.
#
  import numpy as np

  nfactor = 0

  factor_list = []
  exponent_list = []

  nleft = n

  if ( n == 0 ):
    factor = np.zeros ( 0 )
    exponent = np.zeros ( 0 )
    return nfactor, factor, exponent, nleft

  if ( abs ( n ) == 1 ):
    nfactor = 1
    factor_list.append ( 1 )
    exponent_list.append ( 0 )
    factor = np.ones ( 1 )
    exponent = np.zeros ( 1 )
    return nfactor, factor, exponent, nleft
#
#  Find out how many primes we stored.
#
  maxprime = prime ( -1 )
#
#  Try dividing the remainder by each prime.
#
  for i in range ( 1, maxprime + 1 ):

    p = prime ( i )

    if ( ( abs ( nleft ) ) % p == 0 ):

      nfactor = nfactor + 1
      factor_list.append ( p )
      exponent_list.append ( 0 )

      while ( True ):

        exponent_list[nfactor-1] = exponent_list[nfactor-1] + 1
        nleft = ( nleft // p )

        if ( ( abs ( nleft ) ) % p != 0 ):
          break

      if ( abs ( nleft ) == 1 ):
        break

  factor = np.zeros ( nfactor )
  exponent = np.zeros ( nfactor )
  for i in range ( 0, nfactor ):
    factor[i] = factor_list[i]
    exponent[i] = exponent_list[i]
  return nfactor, factor, exponent, nleft

def i4_factor_test ( ):

#*****************************************************************************80
#
## i4_factor_test() tests i4_factor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_factor_test():' )
  print ( '  i4_factor() factors an integer.' )

  n = 2 * 2 * 17 * 37

  print ( '' )
  print ( '  The integer is %d' % ( n ) )

  nfactor, factor, power, nleft = i4_factor ( n )

  print ( '' )
  print ( '  Prime representation:' )
  print ( '' )
  print ( '  I, FACTOR(I), POWER(I)' )
  print ( '' )
  if ( abs ( nleft ) != 1 ):
    print ( '  %6d  %6d  (UNFACTORED PORTION)' % ( 0, nleft ) )

  for i in range ( 0, nfactor ):
    print ( '  %6d  %6d  %6d' % ( i, factor[i], power[i] ) )

  return

def i4_fall ( x, n ):

#*****************************************************************************80
#
## i4_fall() computes the falling factorial function [X]_n.
#
#  Discussion:
#
#    Note that the number of "injections" or 1-to-1 mappings from
#    a set of N elements to a set of M elements is [M]_n.
#
#    The number of permutations of N objects out of M is [M]_n.
#
#    Moreover, the Stirling numbers of the first kind can be used
#    to convert a falling factorial into a polynomial, as follows:
#
#      [X]_n = S^0_n + S^1_n * X + S^2_n * X^2 + ... + S^N_n X^N.
#
#  Formula:
#
#    [X]_n = X * ( X - 1 ) * ( X - 2 ) * ... * ( X - N + 1 ).
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
#    integer X, the argument of the falling factorial function.
#
#    integer N, the order of the falling factorial function.
#    If N = 0, FALL = 1, if N = 1, FALL = X.  Note that if N is
#    negative, a "rising" factorial will be computed.
#
#  Output:
#
#    integer VALUE, the value of the falling factorial function.
#
  value = 1

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg - 1.0

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg + 1

  return value

def i4_fall_test ( ):

#*****************************************************************************80
#
## i4_fall_test() tests i4_fall().
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
  print ( '' )
  print ( 'i4_fall_test():' )
  print ( '  i4_fall() evaluates the falling factorial Fall(I,N).' )
  print ( '' )
  print ( '         M         N      Exact         i4_fall(M,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = i4_fall_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_fall ( m, n )

    print ( '  %8d  %8d  %12d  %12d' % ( m, n, f1, f2 ) )

  return

def i4_fall_values ( n_data ):

#*****************************************************************************80
#
## i4_fall_values() returns values of the integer falling factorial function.
#
#  Discussion:
#
#    The definition of the falling factorial function is
#
#      (m)_n = (m)! / (m-n)!
#            = ( m ) * ( m - 1 ) * ( m - 2 ) ... * ( m - n + 1 )
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer M, N, the arguments of the function.
#
#    integer FMN, the value of the function.
#
  import numpy as np

  n_max = 15

  fmn_vec = np.array ( [ 
     1, 5, 20, 60, 120, \
     120, 0, 1, 10, 4000, \
     90, 4896, 24, 912576, 0 ] )
  m_vec = np.array ( [ 
    5, 5, 5, 5, 5, \
    5, 5, 50, 10, 4000, \
    10, 18, 4, 98, 1 ] )
  n_vec = np.array ( [ 
    0, 1, 2, 3, 4, \
    5, 6, 0, 1, 1, \
    2, 3, 4, 3, 7 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
    n = 0
    fmn = 0
  else:
    m = m_vec[n_data]
    n = n_vec[n_data]
    fmn = fmn_vec[n_data]
    n_data = n_data + 1

  return n_data, m, n, fmn

def i4_fall_values_test ( ):

#*****************************************************************************80
#
## i4_fall_values_test() tests i4_fall_values().
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
  print ( '' )
  print ( 'i4_fall_values_test():' )
  print ( '  i4_fall_values() returns values of the integer falling factorial.' )
  print ( '' )
  print ( '          M         N          i4_fall(M,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, fmn = i4_fall_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %8d  %8d' % ( m, n, fmn ) )

  return

def i4_gcd ( i, j ):

#*****************************************************************************80
#
## i4_gcd() finds the greatest common divisor of I and J.
#
#  Discussion:
#
#    Only the absolute values of I and J are
#    considered, so that the result is always nonnegative.
#
#    If I or J is 0, i4_gcd is returned as max ( 1, abs ( I ), abs ( J ) ).
#
#    If I and J have no common factor, i4_gcd is returned as 1.
#
#    Otherwise, using the Euclidean algorithm, i4_gcd is the
#    largest common factor of I and J.
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
#  Input:
#
#    integer I, J, two numbers whose greatest common divisor
#    is desired.
#
#  Output:
#
#    integer VALUE, the greatest common divisor of I and J.
#
  value = 1
#
#  Return immediately if either I or J is zero.
#
  if ( i == 0 ):
    value = max ( 1, abs ( j ) )
    return value
  elif ( j == 0 ):
    value = max ( 1, abs ( i ) )
    return value
#
#  Set IP to the larger of I and J, IQ to the smaller.
#  This way, we can alter IP and IQ as we go.
#
  ip = max ( abs ( i ), abs ( j ) )
  iq = min ( abs ( i ), abs ( j ) )
#
#  Carry out the Euclidean algorithm.
#
  while ( True ):

    ir = ( ip % iq )

    if ( ir == 0 ):
      break

    ip = iq
    iq = ir

  value = iq

  return value

def i4_gcd_test ( ):

#*****************************************************************************80
#
## i4_gcd_test() tests i4_gcd().
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
  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ( '' )
  print ( 'i4_gcd_test():' )
  print ( '  i4_gcd() computes the greatest common factor' )
  print ( '' )
  print ( '     I     J   i4_gcd' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_gcd ( i, j )
    print ( '  %6d  %6d  %6d' % ( i, j, k ) )

  return

def i4_gpf ( n ):

#*****************************************************************************80
#
## i4_gpf() finds the greatest prime factor of an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be analyzed.
#
#  Output:
#
#    integer P: the greatest prime factor of N.
#
  nleft = n
#
#  Find out how many primes we stored.
#
  maxprime = prime ( -1 )
#
#  Try dividing the remainder by each prime.
#
  i = 0
  p = 1

  while ( 1 < nleft ):

    i = i + 1
    if ( maxprime < i ):
      print ( '' )
      print ( 'i4_gpf(): Fatal error!' )
      print ( '  Exceeded maximum stored prime number.' )
      raise Exception ( 'i4_gpf(): Fatal error!' )

    p = prime ( i );

    while ( ( nleft % p ) == 0 ):
      nleft = nleft // p

  return p

def i4_gpf_values ( n_data ):

#*****************************************************************************80
#
## i4_gpf_values() returns values of the greatest prime factor function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer n: the arguments of the function.
#
#    integer gpf: the value of the function.
#
  import numpy as np

  n_max = 86

  gpf_vec = np.array ( [ 
     1,  2,  3,  2,  5,  3,  7,  2,  3,  5, \
    11,  3, 13,  7,  5,  2, 17,  3, 19,  5, \
     7, 11, 23,  3,  5, 13,  3,  7, 29,  5, \
    31,  2, 11, 17,  7,  3, 37, 19, 13,  5, \
    41,  7, 43, 11,  5, 23, 47,  3,  7,  5, \
    17, 13, 53,  3, 11,  7, 19, 29, 59,  5, \
    61, 31,  7,  2, 13, 11, 67, 17, 23,  7, \
    71,  3, 73, 37,  5, 19, 11, 13, 79,  5, \
     3, 41, 83,  7, 17, 43 ] )
  n_vec = np.array ( [ 
     1,  2,  3,  4,  5,  6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20, \
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, \
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, \
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, \
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60, \
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, \
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80, \
    81, 82, 83, 84, 85, 86 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    gpf = 0
  else:
    n = n_vec[n_data]
    gpf = gpf_vec[n_data]
    n_data = n_data + 1

  return n_data, n, gpf

def i4_gpf_test ( ):

#*****************************************************************************80
#
## i4_gpf_test() tests i4_gpf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_gpf_test():' )
  print ( '  i4_gpf() returns the greatest prime factor.' )
  print ( '' )
  print ( '          n          gpf(n)     i4_gpf(n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, gpf1 = i4_gpf_values ( n_data )

    if ( n_data == 0 ):
      break

    gpf2 = i4_gpf ( n )

    print ( '  %8d  %8d  %8d' % ( n, gpf1, gpf2 ) )

  return

def i4_huge ( ):

#*****************************************************************************80
#
## i4_huge() returns a "huge" I4.
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
#  Output:
#
#    integer VALUE, a huge integer.
#
  value = 2147483647

  return value;

def i4_huge_test ( ) :

#*****************************************************************************80
#
## i4_huge_test() tests i4_huge().
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
  print ( '' )
  print ( 'i4_huge_test():' )
  print ( '  i4_huge() returns a huge integer.' )
  print ( '' )
  i = i4_huge ( )
  print ( '  i4_huge() = %d' % ( i ) )

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

    i_abs = abs ( i )

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
  print ( '  i4_log_10() computes the whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def i4mat_2perm0 ( m, n, a, p, q ):

#*****************************************************************************80
#
## i4mat_2perm0() uses permutations of (0,...,M-1) and (0,...,N-1) on an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
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
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#
#    integer A(M,N), the matrix to be permuted.
#
#    integer P(M), the row permutation.  P(I) is the new number of row I.
#
#    integer Q(N), the column permutation.  Q(I) is the new number
#    of column I. 
#
#  Output:
#
#    integer A(M,N), the permuted matrix.
#
  sp, ncp, tagp = perm0_cycle ( m, p )

  sq, ncq, tagq = perm0_cycle ( n, q )

  for i in range ( 0, m ):

    i1 = - tagp[i] * p[i]

    if ( 0 < i1 ):

      lc = 0

      while ( True ):

        i1 = tagp[i1] * p[i1]
        lc = lc + 1

        if ( i1 < 0 ):
          break

      i1 = i

      for j in range ( 0, n ):

        if ( tagq[j] < 0 ):

          j2 = j
          k = lc

          while ( True ):

            j1 = j2
            it = a[i1,j1]

            while ( True ):

              i1 = p[i1]
              j1 = q[j1]

              t        = a[i1,j1]
              a[i1,j1] = it
              it       = t

              if ( j1 != j2 ):
                continue

              k = k - 1

              if ( i1 == i ):
                break

            j2 = q[j2]

            if ( k == 0 ):
              break

  return a

def i4mat_2perm0_test ( ):

#*****************************************************************************80
#
## i4mat_2perm0_test() tests i4mat_2perm0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 9
  n = 7

  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ] )
  q = np.array ( [ 2,3,4,5,6,0,1 ] )

  print ( '' )
  print ( 'i4mat_2perm0_test():' )
  print ( '  i4mat_2perm0() reorders an integer matrix in place.' )
  print ( '  Rows and columns use different permutations.' )

  a = np.zeros ( [ m, n ] )
 
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = ( i + 1 ) * 10 + ( j + 1 )
 
  i4mat_print ( m, n, a, '  The input matrix:' )
 
  perm0_print ( m, p, '  The row permutation:' )

  perm0_print ( n, q, '  The column permutation:' )
 
  a = i4mat_2perm0 ( m, n, a, p, q )
 
  i4mat_print ( m, n, a, '  The permuted matrix:' )

  return

def i4mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## i4mat_mm() computes the product of two I4MAT's.
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
#  Input:
#
#    integer N1, N2, N3, matrix dimensions.
#
#    integer A(N1,N2), factor 1.
#
#  Output:
#
#    integer B(N2,N3), factor 2.
#
#    integer C(N1,N3), the product.
#
  import numpy as np

  c = np.zeros ( [ n1, n3 ], dtype = np.int32 )

  for k in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for j in range ( 0, n2 ):
        c[i,k] = c[i,k] + a[i,j] * b[j,k]

  return c

def i4mat_mm_test ( ):

#*****************************************************************************80
#
## i4mat_mm_test() tests i4mat_mm().
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

  n1 = 3
  n2 = 2
  n3 = 4
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [
   [  11,  12 ], \
   [  21,  22 ], \
   [  31,  32 ] ] )

  b = np.array ( [
   [  11,  12, 13, 14 ], \
   [  21,  22, 23, 24 ] ] )

  print ( '' )
  print ( 'i4mat_mm_test():' )
  print ( '  i4mat_mm() multiplies two I4MAT\'s' )

  i4mat_print ( n1, n2, a, '  Matrix A:' )
  i4mat_print ( n2, n3, b, '  Matrix B:' )

  c = i4mat_mm ( n1, n2, n3, a, b )
 
  i4mat_print ( n1, n3, c, '  C = A*B:' )

  return

def i4mat_perm0 ( n, a, p ):

#*****************************************************************************80
#
## i4mat_perm0() applies a permutation of (0,...,N-1) to a square I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
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
#    integer N, the order of the matrix.
#
#    integer A(N,N), the matrix to be permuted.
#
#    integer P(N), the permutation.  P(I) is the new number of row
#    and column I.
#
#  Output:
#
#    integer A(N,N), the permuted matrix.
#
  s, nc, tag = perm0_cycle ( n, p )

  for i in range ( 0, n ):

    i1 = - tag[i] * p[i]

    if ( 0 < i1 ):

      lc = 0

      while ( True ):

        i1 = tag[i1] * p[i1]
        lc = lc + 1

        if ( i1 < 0 ):
          break

      i1 = i

      for j in range ( 0, n ):

        if ( tag[j] < 0 ):

          j2 = j
          k = lc

          while ( True ):

            j1 = j2
            it = a[i1,j1]

            while ( True ):

              i1 = p[i1]
              j1 = p[j1]

              t = a[i1,j1]
              a[i1,j1] = it
              it = t

              if ( j1 != j2 ):
                continue

              k = k - 1

              if ( i1 == i ):
                break

            j2 = p[j2]

            if ( k == 0 ):
              break

  return a

def i4mat_perm0_test ( ):

#*****************************************************************************80
#
## i4mat_perm0_test() test i4mat_perm0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9

  p = np.array ( [ 1, 2, 8, 5, 6, 7, 4, 3, 0 ] )

  print ( '' )
  print ( 'i4mat_perm0_test():' )
  print ( '  i4mat_perm0() reorders an integer matrix in place.' )
  print ( '  The rows and columns use the same permutation.' )

  a = np.zeros ( [ n, n ], dtype = np.int32 )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = ( i + 1 ) * 10 + j + 1

  i4mat_print ( n, n, a, '  The input matrix:' )
 
  perm0_print ( n, p, '  The row and column permutation:' )
 
  a = i4mat_perm0 ( n, a, p )
 
  i4mat_print ( n, n, a, '  The permuted matrix:' )

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
  print ( '  i4mat_print() prints an I4MAT.' )

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
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )

  return

def i4mat_u1_inverse ( n, a ):

#*****************************************************************************80
#
## i4mat_u1_inverse() inverts a unit upper triangular I4MAT.
#
#  Discussion:
#
#    A unit upper triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's below the main diagonal.
#
#    The inverse of an integer unit upper triangular matrix is also
#    an integer unit upper triangular matrix.
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
#    integer A(N,N), the unit upper triangular matrix.
#
#  Output:
#
#    integer B(N,N), the inverse matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ], dtype = np.int32 )

  for j in range ( n - 1, -1, -1 ):

    b[j,j] = 1

    for i in range ( j - 1, -1, -1 ):
      for k in range ( i + 1, j + 1 ):
        b[i,j] = b[i,j] - a[i,k] * b[k,j]

  return b

def i4mat_u1_inverse_test ( ):

#*****************************************************************************80
#
## i4mat_u1_inverse_test() tests i4mat_u1_inverse().
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

  n = 6
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [
   [  1,  2,  0,  5,  0, 75 ], \
   [  0,  1,  0,  0,  0,  0 ], \
   [  0,  0,  1,  3,  0,  0 ], \
   [  0,  0,  0,  1,  0,  6 ], \
   [  0,  0,  0,  0,  1,  4 ], \
   [  0,  0,  0,  0,  0,  1 ] ] )

  print ( '' )
  print ( 'i4mat_u1_inverse_test():' )
  print ( '  i4mat_u1_inverse() inverts a unit upper triangular matrix.' )

  i4mat_print ( n, n, a, '  The original matrix:' )
 
  b = i4mat_u1_inverse ( n, a )
 
  i4mat_print ( n, n, b, '  The inverse matrix:' )

  c = i4mat_mm ( n, n, n, a, b )

  i4mat_print ( n, n, c, '  The product:' )

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
    print ( 'i4_modp(): Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp(): Fatal error!' )

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
  print ( '  Repeat using the % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  return

def i4_moebius ( n ):

#*****************************************************************************80
#
## i4_moebius() returns the value of MU(N), the Moebius function of N.
#
#  Discussion:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1
#              0 if N is divisible by the square of a prime
#              (-1)^K, if N is the product of K distinct primes.
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#    The Moebius function MU(D) is related to Euler's totient 
#    function PHI(N):
#
#      PHI(N) = sum ( D divides N ) MU(D) * ( N / D ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.
#
#  Output:
#
#    integer MU, the value of MU(N).
#    If N is less than or equal to 0, MU will be returned as -2.
#    If there was not enough internal space for factoring, MU
#    is returned as -3.
#
  if ( n <= 0 ):
    mu = -2
    return mu

  if ( n == 1 ):
    mu = 1
    return mu
#
#  Factor N.
#
  nfactor, factor, exponent, nleft =  i4_factor ( n  )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'i4_moebius - Warning!' )
    print ( '  Not enough factorization space.' )
    mu = -3
    return mu

  mu = 1

  for i in range ( 0, nfactor ):

    mu = - mu

    if ( 1 < exponent[i] ):
      mu = 0
      return mu

  return mu

def i4_moebius_test ( ):

#*****************************************************************************80
#
## i4_moebius_test() tests i4_moebius().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_moebius_test():' )
  print ( '  i4_moebius() evaluates the Moebius function:' )
  print ( '' )
  print ( '         N      Exact         i4_moebius(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c1 = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = i4_moebius ( n )

    print ( '  %8d  %12d  %12d' % ( n, c1, c2 ) )

  return

def i4_partition_conj ( n, iarray1, mult1, npart1 ):

#*****************************************************************************80
#
## i4_partition_conj() computes the conjugate of a partition.
#
#  Discussion:
#
#    A partition of an integer N is a set of positive integers which
#    add up to N.  The conjugate of a partition P1 of N is another partition
#    P2 of N obtained in the following way:
#
#      The first element of P2 is the number of parts of P1 greater than
#      or equal to 1.
#
#      The K-th element of P2 is the number of parts of P1 greater than
#      or equal to K.
#
#    Clearly, P2 will have no more than N elements it may be surprising
#    to find that P2 is guaranteed to be a partition of N.  However, if
#    we symbolize the initial partition P1 by rows of X's, then we can
#    see that P2 is simply produced by grouping by columns:
#
#        6 3 2 2 1
#      5 X X X X X
#      4 X X X X
#      2 X X
#      1 X
#      1 X
#      1 X
#
#  Example:
#
#    14 = 5 + 4 + 2 + 1 + 1 + 1
#
#    The conjugate partition is:
#
#    14 = 6 + 3 + 2 + 2 + 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be partitioned.
#
#    integer IARRAY1(NPART1).  IARRAY1 contains the parts of
#    the partition.  The value of N is represented by
#
#      sum ( 1 <= I <= NPART1 ) MULT1(I) * IARRAY1(I).
#
#    integer MULT1(NPART1).  MULT1 counts the multiplicity of
#    the parts of the partition.  MULT1(I) is the multiplicity
#    of the part IARRAY1(I), for I = 1 to NPART1.
#
#    integer NPART1, the number of "parts" in the partition.
#
#  Output:
#
#    integer IARRAY2(N).  IARRAY contains the parts of
#    the conjugate partition in entries 1 through NPART2.
#
#    integer MULT2(N).  MULT2 counts the multiplicity of
#    the parts of the conjugate partition in entries 1 through NPART2.
#
#    integer NPART2, the number of "parts" in the conjugate partition.
#
  import numpy as np

  iarray2 = np.zeros ( n )
  mult2 = np.zeros ( n )
  npart2 = 0

  itest = 0

  while ( True ):

    itest = itest + 1

    itemp = 0

    for i in range ( 0, npart1 ):
      if ( itest <= iarray1[i] ):
        itemp = itemp + mult1[i]

    if ( itemp <= 0 ):
      break

    if ( 0 < npart2 ):
      if ( itemp == iarray2[npart2-1] ):
        mult2[npart2-1] = mult2[npart2-1] + 1
      else:
        npart2 = npart2 + 1
        iarray2[npart2-1] = itemp
        mult2[npart2-1] = 1
    else:
      npart2 = npart2 + 1
      iarray2[npart2-1] = itemp
      mult2[npart2-1] = 1

  return iarray2, mult2, npart2

def i4_partition_conj_test ( ):

#*****************************************************************************80
#
## i4_partition_conj_test() tests i4_partition_conj().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 14
  npart1 = 4

  a1 = np.array ( [ 2, 5, 1, 4 ] )
  mult1 = np.array ( [ 1, 1, 3, 1 ] )

  print ( '' )
  print ( 'i4_partition_conj_test():' )
  print ( '  i4_partition_conj() conjugates an integer partition.' )
  print ( '' )
  print ( '  Original partition:' )
  print ( '' )

  i4_partition_print ( n, npart1, a1, mult1 )

  a2, mult2, npart2 = i4_partition_conj ( n, a1, mult1, npart1 )

  print ( '' )
  print ( '  Conjugate partition:' )
  print ( '' )

  i4_partition_print ( n, npart2, a2, mult2 )

  return

def i4_partition_count2 ( n ):

#*****************************************************************************80
#
## i4_partition_count2() computes the number of partitions of an integer.
#
#  First values:
#
#    N   P
#
#    0   1
#    1   1
#    2   2
#    3   3
#    4   5
#    5   7
#    6  11
#    7  15
#    8  22
#    9  30
#   10  42
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
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
#    integer N, the largest integer to be considered.
#
#  Output:
#
#    integer P[0:N], the partition numbers.
#
  import numpy as np
  
  p = np.zeros ( n + 1 )

  p[0] = 1

  if ( 0 < n ):

    p[1] = 1

    for i in range ( 2, n + 1 ):

      total = 0

      for t in range ( 1, i + 1 ):

        s = 0
        j = i

        while ( True ):

          j = j - t

          if ( 0 < j ):
            s = s + p[j]
          else:
            if ( j == 0 ):
              s = s + 1
            break

        total = total + s * t;

      p[i] = ( total // i )

  return p

def i4_partition_count2_test ( ):

#*****************************************************************************80
#
## i4_partition_count2_test() tests i4_partition_count2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_partition_count2_test():' )
  print ( '  i4_partition_count2() counts partitions of an integer.' )

  n_data = 0

  print ( '' )
  print ( '   N     Exact     Count' )
  print ( '' )

  while ( True ):

    n_data, n, p = i4_partition_count_values ( n_data )

    if ( n_data == 0 ):
      break

    p2 = i4_partition_count2 ( n )
 
    print ( '  %4d  %8d  %8d' % ( n, p, p2[n] ) )

  return

def i4_partition_count ( n ):

#*****************************************************************************80
#
## i4_partition_count() computes the number of partitions of an integer.
#
#  Discussion:
#
#    Partition numbers are difficult to compute.  This routine uses
#    Euler's method, which observes that:
#
#      P(0) = 1
#      P(N) =   P(N-1)  + P(N-2)
#             - P(N-5)  - P(N-7)
#             + P(N-12) + P(N-15)
#             - ...
#
#      where the numbers 1, 2, 5, 7, ... to be subtracted from N in the
#      indices are the successive pentagonal numbers, (with both positive 
#      and negative indices) with the summation stopping when a negative 
#      index is reached.
#
#  First values:
#
#    N   P
#
#    0   1
#    1   1
#    2   2
#    3   3
#    4   5
#    5   7
#    6  11
#    7  15
#    8  22
#    9  30
#   10  42
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Conway and Richard Guy,
#    The Book of Numbers,
#    Springer Verlag, 1996, page 95.
#
#  Input:
#
#    integer N, the index of the highest partition number desired.
#
#  Output:
#
#    integer P[0:N], the partition numbers.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.int32 )

  p[0] = 1

  for i in range ( 1, n + 1 ):

    p[i] = 0

    j = 0
    sgn = 1

    while ( True ):

      j = j + 1
      pj = pent_enum ( j )

      if ( i < pj ):
        break

      p[i] = p[i] + sgn * p[i-pj]
      sgn = -sgn

    j = 0
    sgn = 1

    while ( True ):

      j = j - 1
      pj = pent_enum ( j );

      if ( i < pj ):
        break

      p[i] = p[i] + sgn * p[i-pj]
      sgn = -sgn

  return p

def i4_partition_count_test ( ):

#*****************************************************************************80
#
## i4_partition_count_test() tests i4_partition_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_partition_count_test():' )
  print ( '  i4_partition_count() counts partitions of an integer.' )

  n_data = 0

  print ( '' )
  print ( '   N     Exact     Count' )
  print ( '' )

  while ( True ):

    n_data, n, p = i4_partition_count_values ( n_data )

    if ( n_data == 0 ):
      break

    p2 = i4_partition_count ( n )
 
    print ( '  %4d  %8d  %8d' % ( n, p, p2[n] ) )

  return

def i4_partition_count_values ( n_data ):

#*****************************************************************************80
#
## i4_partition_count_values() returns some values of the integer partition count.
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer
#    as the sum of nonzero positive integers.  The order of the summands
#    does not matter.  The number of partitions of N is symbolized
#    by P(N).  Thus, the number 5 has P(N) = 7, because it has the
#    following partitions:
#
#    5 = 5
#      = 4 + 1
#      = 3 + 2
#      = 3 + 1 + 1
#      = 2 + 2 + 1
#      = 2 + 1 + 1 + 1
#      = 1 + 1 + 1 + 1 + 1
#
#    In Mathematica, the function can be evaluated by
#
#      PartitionsP[n]
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer N, the integer.
#
#    integer C, the number of partitions of the integer.
#
  import numpy as np

  n_max = 21

  c_vec = np.array ( ( \
      1, \
      1,   2,   3,   5,   7,  11,  15,  22,  30,  42, \
     56,  77, 101, 135, 176, 231, 297, 385, 490, 627 ) )

  n_vec = np.array ( ( \
     0,  \
     1,  2,  3,  4,  5,  6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def i4_partition_count_values_test ( ):

#*****************************************************************************80
#
## i4_partition_count_values_test() tests i4_partition_count_values().
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
  print ( '' )
  print ( 'i4_partition_count_values_test():' )
  print ( '  i4_partition_count_values() returns values of ' )
  print ( '  the integer partition count function.' )
  print ( '' )
  print ( '     N         P(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_partition_count_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, fn ) )

  return

def i4_partition_next2 ( n, npart, a, mult, more ):

#*****************************************************************************80
#
## i4_partition_next2() computes the partitions of the integer N one at a time.
#
#  Discussion:
#
#    Unlike compositions, order is not important in a partition.  Thus
#    the sequences 3+2+1 and 1+2+3 represent distinct compositions, but
#    not distinct partitions.  Also 0 is never returned as one of the
#    elements of the partition.
#
#    Initialize the program by calling with MORE = FALSE.  On an initialization
#    call, the input values of A, MULT and NPART are not needed.  Thereafter,
#    they should be set to the output values of A, MULT and NPART from
#    the previous call.
#
#  Example:
#
#    Sample partitions of 6 include:
#
#      6 = 4+1+1 = 3+2+1 = 2+2+2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the integer whose partitions are desired.
#
#    integer NPART, the output value of NPART on the previous call.
#
#    integer A(N), the output value of A on the previous call.
#
#    integer MULT(N), the output value of MULT on the previous call.
#
#    bool MORE, is FALSE on the first call, which causes
#    initialization.  Thereafter, it should be TRUE.
#
#  Output:
#
#    integer NPART, the number of distinct, nonzero parts in the
#    output partition.
#
#    integer A(N).  A(1:NPART) the distinct parts
#    of the partition.
#
#    integer MULT(1:NPART), the multiplicity of the parts.
#
#    bool MORE is TRUE if there are more partitions available.
#
  if ( not more ):
    npart = 1
    a[npart-1] = n
    mult[npart-1] = 1
    more = ( mult[npart-1] != n )
    return npart, a, mult, more

  isum = 1

  if ( a[npart-1] <= 1 ):
    isum = mult[npart-1] + 1
    npart = npart - 1

  iff = a[npart-1] - 1

  if ( mult[npart-1] != 1 ):
    mult[npart-1] = mult[npart-1] - 1
    npart = npart + 1

  a[npart-1] = iff
  mult[npart-1] = 1 + ( isum // iff )
  s = ( isum % iff )

  if ( 0 < s ):
    npart = npart + 1
    a[npart-1] = s
    mult[npart-1] = 1
#
#  There are more partitions, as long as we haven't just computed
#  the last one, which is N copies of 1.
#
  more = ( mult[npart-1] != n )

  return npart, a, mult, more

def i4_partition_next2_test ( ):

#*****************************************************************************80
#
## i4_partition_next2_test() tests i4_partition_next2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 7

  print ( '' )
  print ( 'i4_partition_next2_test():' )
  print ( '  i4_partition_next2() produces partitions of an integer.' )
  print ( '' )

  npart = 0
  a = np.zeros ( n )
  mult = np.zeros ( n )
  more = False

  while ( True ):

    npart, a, mult, more = i4_partition_next2 ( n, npart, a, mult, more )

    i4_partition_print ( n, npart, a, mult )

    if ( not more ):
      break

  return

def i4_partition_next ( n, npart, a, mult, done ):

#*****************************************************************************80
#
## i4_partition_next() generates the partitions of an integer, one at a time.
#
#  Discussion:
#
#    The number of partitions of N is:
#
#      1     1
#      2     2
#      3     3
#      4     5
#      5     7
#      6    11
#      7    15
#      8    22
#      9    30
#     10    42
#     11    56
#     12    77
#     13   101
#     14   135
#     15   176
#     16   231
#     17   297
#     18   385
#     19   490
#     20   627
#     21   792
#     22  1002
#     23  1255
#     24  1575
#     25  1958
#     26  2436
#     27  3010
#     28  3718
#     29  4565
#     30  5604
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
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
#    integer N, the integer to be partitioned.
#
#    integer NPART, the output value of NPART on the previous call.
#
#    integer A(N), the output value of A on the previous call.
#
#    integer MULT(N), the output value of MULT on the previous call.
#
#    bool DONE, is TRUE on the first call, to perform initialization.
#    On an initialization call, the input values of NPART, A and MULT are not
#    needed.
#
#  Output:
#
#    integer NPART, the number of "parts" in the next partition.
#
#    integer A(N), the parts of the nextpartition.  The value N is
#    represented by sum ( 1 <= I <= NPART ) MULT(I) * A(I).
#
#    integer MULT(N), the multiplicities.
#
#    bool DONE, is FALSE if there are more partitions, or TRUE
#    if there are no more.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'i4_partition_next(): Fatal error!' )
    print ( '  N must be positive.' )
    print ( '  The input value of N was %d' % ( n ) )
    raise Exception ( 'i4_partition_next(): Fatal error!' )

  if ( done ):

    a[0] = n
    for i in range ( 1, n ):
      a[i] = 0

    mult[0] = 1
    for i in range ( 1, n ):
      mult[i] = 0

    npart = 1
    done = False

  else:

    if ( 1 < a[npart-1] or 1 < npart ):

      done = False

      if ( a[npart-1] == 1 ):
        s = a[npart-2] + mult[npart-1]
        k = npart - 1
      else:
        s = a[npart-1]
        k = npart

      iw = a[k-1] - 1
      iu = ( s // iw )
      iv = ( s % iw )
      mult[k-1] = mult[k-1] - 1

      if ( mult[k-1] == 0 ):
        k1 = k
      else:
        k1 = k + 1

      mult[k1-1] = iu
      a[k1-1] = iw

      if ( iv == 0 ):
        npart = k1
      else:
        mult[k1] = 1
        a[k1] = iv
        npart = k1 + 1

    else:

      done = True

  return npart, a, mult, done

def i4_partition_next_test ( ):

#*****************************************************************************80
#
## i4_partition_next_test() tests i4_partition_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 7
  npart = 0
  a = np.zeros ( n )
  mult = np.zeros ( n )
  done = True

  print ( '' )
  print ( 'i4_partition_next_test():' )
  print ( '  i4_partition_next() generates partitions of an integer.' )
  print ( '  Here N = %d' % ( n ) )
  print ( '' )

  while ( True ):

    npart, a, mult, done = i4_partition_next ( n, npart, a, mult, done )
 
    if ( done ):
      break 

    i4_partition_print ( n, npart, a, mult )

  return

def i4_partition_print ( n, npart, a, mult ):

#*****************************************************************************80
#
## i4_partition_print() prints a partition of an integer.
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer as
#    the sum of nonzero integers:
#
#      N = A1 + A2 + A3 + ...
#
#    It is standard practice to gather together all the values that 
#    are equal, and replace them in the sum by a single term, multiplied
#    by its "multiplicity":
#
#      N = M1 * A1 + M2 * A2 + ... + M(NPART) * A(NPART)
#    
#    In this representation, every A is a unique positive number, and 
#    no M is zero (or negative).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be partitioned.
#
#    integer NPART, the number of "parts" in the partition.
#
#    integer A(NPART), the parts of the partition.  
#
#    integer MULT(NPART), the multiplicities of the parts.
#
  print ( '  %d =' % ( n ), end = '' )

  for i in range ( 0, npart ):

    if ( i == 0 ):
      print ( '', end = '' )
    else:
      print ( '+', end = '' )

    print ( '%d * %d' % ( mult[i], a[i] ), end = '' )

  print ( '' )

  return

def i4_partition_print_test ( ):

#*****************************************************************************80
#
## i4_partition_print_test() tests i4_partition_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 14
  npart = 4

  a = np.array ( [ 2, 5, 1, 4 ] )
  mult = np.array ( [ 1, 1, 3, 1 ] )

  print ( '' )
  print ( 'i4_partition_print_test():' )
  print ( '  i4_partition_print() prints an integer partition.' )

  print ( '' )
  i4_partition_print ( n, npart, a, mult )

  return

def i4_partition_random ( n, table, rng ):

#*****************************************************************************80
#
## i4_partition_random() selects a random partition of the integer N.
#
#  Discussion:
#
#    Note that some elements of the partition may be 0.  The partition is
#    returned as (MULT(I),I), with NPART nonzero entries in MULT, and
#
#      N = sum ( 1 <= I <= N ) MULT(I) * I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
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
#    integer N, the integer to be partitioned.
#
#    integer TABLE(N), the number of partitions of the integers 1 through N.
#    This table may be computed by i4_partition_count2.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(N), contains in A(1:NPART) the parts of the partition.
#
#    integer MULT(N), contains in MULT(1:NPART) the multiplicity
#    of the parts.
#
#    integer NPART, the number of parts in the partition chosen,
#    that is, the number of integers I with nonzero multiplicity MULT(I).
#
  import numpy as np

  m = n
  npart = 0

  a = np.zeros ( n, dtype = np.int32 )
  mult = np.zeros ( n, dtype = np.int32 )

  while ( 0 < m ):

    z = rng.random ( )
    z = m * table[m-1] * z
    id = 1
    i1 = m
    j = 0

    while ( True ):

      j = j + 1
      i1 = i1 - id

      if ( i1 < 0 ):
        id = id + 1
        i1 = m
        j = 0
        continue

      if ( i1 == 0 ):
        z = z - id
        if ( 0.0 < z ):
          id = id + 1
          i1 = m
          j = 0
          continue
        else:
          break

      if ( 0 < i1 ):
        z = z - id * table[i1-1]
        if ( z <= 0.0 ):
          break

    mult[id-1] = mult[id-1] + j
    npart = npart + j
    m = i1
#
#  Reformulate the partition in the standard form.
#  NPART is the number of distinct parts.
#
  npart = 0

  for i in range ( 1, n + 1 ):
    if ( mult[i-1] != 0 ):
      npart = npart + 1
      a[npart-1] = i
      mult[npart-1] = mult[i-1]

  for i in range ( npart, n ):
    mult[i] = 0

  return a, mult, npart

def i4_partition_random_test ( rng ):

#*****************************************************************************80
#
## i4_partition_random_test() tests i4_partition_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 8

  print ( '' )
  print ( 'i4_partition_random_test():' )
  print ( '  i4_partition_random() generates a random partition.' )
  print ( '' )
#
#  Get the partition table.
#
  table = i4_partition_count2 ( n )

  print ( '' )
  print ( '  The number of partitions of N' )
  print ( '' )
  print ( '     N    Number of partitions' )
  print ( '' )

  for j in range ( 0, n ):
    print ( '  %4d    %6d' % ( j, table[j] ) )

  print ( '' )

  for i in range ( 0, 5 ):

    a, mult, npart = i4_partition_random ( n, table, rng )

    i4_partition_print ( n, npart, a, mult )

  return

def i4_partitions_next ( s, m1 ):

#*****************************************************************************80
#
## i4_partitions_next(): next partition into S parts.
#
#  Discussion:
#
#    This function generates, one at a time, entries from the list of
#    nondecreasing partitions of the integers into S or fewer parts.
#
#    The list is ordered first by the integer that is partitioned
#    (the sum of the entries), and second by decreasing lexical order
#    in the partition vectors.
#
#    The first value returned is the only such partition of 0.
#
#    Next comes the only partition of 1.
#
#    There follow two partitions of 2, and so on.
#
#    Typical use of this function begins with an initialization call,
#    and then repeated calls in which the output from the previous call
#    is used as input to the next call:
#
#    m = [ 0, 0, 0 ]
#
#    while ( condition )
#      m = i4_partitions_next ( s, m )
#    end
#
#  Example:
#
#    S = 3
#
#    P  D    M
#    _  _  _____
#    1  0  0 0 0
#    2  1  1 0 0
#    3  2  2 0 0
#    4  2  1 1 0
#    5  3  3 0 0
#    6  3  2 1 0
#    7  3  1 1 1
#    8  4  4 0 0
#    9  4  3 1 0
#   10  4  2 2 0
#   11  4  2 1 1
#   12  5  5 0 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer S, the number of items in the partition.
#
#    integer M1(S), the current partition.  On first call, this
#    should be a nondecreasing partition.  Thereafter, it should be the
#    output partition from the previous call.
#
#  Output:
#
#    integer M2(S), the next partition.
#
  import numpy as np

  m2 = np.zeros ( s )
  for i in range ( 0, s ):
    m2[i] = m1[i]

  msum = m2[0]

  for i in range ( 1, s ):

    msum = msum + m2[i]

    if ( m2[0] <= m2[i] + 1 ):
      m2[i] = 0
    else:
      m2[0] = msum - i * ( m2[i] + 1 )
      for j in range ( 1, i + 1 ):
        m2[j] = m2[i] + 1
      return m2
#
#  If we failed to find a suitable index I, put
#  the entire sum into M(1), increment by 1, and
#  prepare to partition the next integer.
#
  m2[0] = msum + 1

  return m2

def i4_partitions_next_test ( ):

#*****************************************************************************80
#
## i4_partitions_next_test() tests i4_partitions_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4_partitions_next_test():' )
  print ( '  i4_partitions_next() produces the next' )
  print ( '  nondecreasing partitions of an integer, and' )
  print ( '  if necessary, increments the integer to keep on going.' )
  print ( '' )
  print ( '   I Sum    Partition' )
  print ( '' )

  i = 0
  s = 3
  m = np.array ( [ 0, 0, 0 ] )

  print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ), end = '' )
  for j in range ( 0, s ):
    print ( '  %2d' % ( m[j] ), end = '' )
  print ( '' )

  for i in range ( 0, 15 ):

    m = i4_partitions_next ( s, m )

    print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ), end = '' )
    for j in range ( 0, s ):
      print ( '  %2d' % ( m[j] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  You can start from any legal partition.' )
  print ( '  Here, we restart at ( 2, 1, 0 ).' )
  print ( '' )
  print ( '   I Sum    Partition' )
  print ( '' )

  i = 0
  s = 3
  m = np.array ( [ 2, 1, 0 ] )

  print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ), end = '' )
  for j in range ( 0, s ):
    print ( '  %2d' % ( m[j] ), end = '' )
  print ( '' )

  for i in range ( 0, 15 ):

    m = i4_partitions_next ( s, m )

    print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ), end = '' )
    for j in range ( 0, s ):
      print ( '  %2d' % ( m[j] ), end = '' )
    print ( '' )

  return

def i4poly_add ( na, a, nb, b ):

#*****************************************************************************80
#
## i4poly_add() adds two I4POLY's.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the degree of polynomial A.
#
#    integer A[0:NA], the coefficients of the first
#    polynomial factor.
#
#    integer NB, the degree of polynomial B.
#
#    integer B[0:NB], the coefficients of the
#    second polynomial factor.
#
#  Output:
#
#    integer C[0:max(NA,NB)], the coefficients of A + B.
#
  import numpy as np

  nc = max ( na, nb ) + 1

  c = np.zeros ( nc )

  for i in range ( 0, na + 1 ):
    c[i] = c[i] + a[i]

  for i in range ( 0, nb + 1 ):
    c[i] = c[i] + b[i]

  return c

def i4poly_add_test ( ):

#*****************************************************************************80
#
## i4poly_add_test() tests i4poly_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4poly_add_test():' )
  print ( '  i4poly_add() adds two I4POLY\'s.' )

  na = 5
  a = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  nb = 5
  b = np.array ( [ 1, -2, 7, 8, 0, -5 ] )

  c = i4poly_add ( na, a, nb, b )

  i4poly_print ( na, a, '  Polynomial A:' )

  i4poly_print ( nb, b, '  Polynomial B:' )

  nc = max ( na, nb )

  nc2 = i4poly_degree ( nc, c )

  i4poly_print ( nc2, c, '  Polynomial C = A+B:' )

  return

def i4poly_cyclo ( n ):

#*****************************************************************************80
#
## i4poly_cyclo() computes a cyclotomic polynomial.
#
#  Discussion:
#
#    For 1 <= N, let
#
#      I = SQRT ( - 1 )
#      L = EXP ( 2 * PI * I / N )
#
#    Then the N-th cyclotomic polynomial is defined by
#
#      PHI(NX) = Product ( 1 <= K <= N and GCD(K,N) = 1 ) ( X - L^K )
#
#    We can use the Moebius MU function to write
#
#      PHI(NX) = Product ( mod ( D, N ) = 0 ) ( X^D - 1 )^MU(N/D)
#
#    There is a sort of inversion formula:
#
#      X^N - 1 = Product ( mod ( D, N ) = 0 ) PHI(DX)
#
#  Example:
#
#     N  PHI
#
#     0  1
#     1  X - 1
#     2  X + 1
#     3  X^2 + X + 1
#     4  X^2 + 1
#     5  X^4 + X^3 + X^2 + X + 1
#     6  X^2 - X + 1
#     7  X^6 + X^5 + X^4 + X^3 + X^2 + X + 1
#     8  X^4 + 1
#     9  X^6 + X^3 + 1
#    10  X^4 - X^3 + X^2 - X + 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Raymond Seroul,
#    Programming for Mathematicians,
#    Springer Verlag, 2000, page 269.
#
#  Input:
#
#    integer N, the index of the cyclotomic polynomial desired.
#
#  Output:
#
#    integer PHI(1:N+1), the N-th cyclotomic polynomial.
#
  import numpy as np

  max_poly = 100

  num = np.zeros ( max_poly )
  num[0] = 1
  num_n = 0

  den = np.zeros ( max_poly )
  den[0] = 1
  den_n = 0

  for d in range ( 1, n + 1 ):
#
#  For each divisor D of N, ...
#
    if ( ( n % d ) == 0 ):

      arg = ( n // d )
      mu = i4_moebius ( arg )
#
#  ...multiply the numerator or denominator by (X^D-1).
#
      factor = np.zeros ( d + 1 )

      factor[0] = -1
      for i in range ( 1, d ):
        factor[i] = 0
      factor[d] = 1

      if ( mu == +1 ):

        if ( max_poly < num_n + d ):
          print ( '' )
          print ( 'i4poly_cyclo(): Fatal error!' )
          print ( '  Numerator polynomial degree too high.' )
          raise Exception ( 'i4poly_cyclo(): Fatal error!' )

        num = i4poly_mul ( num_n, num, d, factor )

        num_n = num_n + d

      elif ( mu == -1 ):

        if ( max_poly < den_n + d ):
          print ( '' )
          print ( 'i4poly_cyclo(): Fatal error!' )
          print ( '  Denominator polynomial degree too high.' )
          raise Exception ( 'i4poly_cyclo(): Fatal error!' )

        den = i4poly_mul ( den_n, den, d, factor )

        den_n = den_n + d
#
#  PHI = NUM / DEN
#
  nq, q, nr, rem = i4poly_div ( num_n, num, den_n, den )

  phi = np.zeros ( n + 1 )
  for i in range ( 0, nq + 1 ):
    phi[i] = q[i]

  return phi

def i4poly_cyclo_test ( ):

#*****************************************************************************80
#
## i4poly_cyclo_test() tests i4poly_cyclo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
# 
  print ( '' )
  print ( 'i4poly_cyclo_test():' )
  print ( '  i4poly_cyclo() computes cyclotomic polynomials.' )

  for n in range ( 0, 11 ):

    print ( '' )
    print ( '  N = %d' % ( n ) )

    phi = i4poly_cyclo ( n )

    i4poly_print ( n, phi, '  The cyclotomic polynomial:' )

  return

def i4poly_degree ( na, a ):

#*****************************************************************************80
#
## i4poly_degree() returns the degree of a polynomial.
#
#  Discussion:
#
#    The degree of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#    The degree of a constant polynomial is 0.  The degree of the
#    zero polynomial is debatable, but this routine returns the
#    degree as 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the dimension of A.
#
#    integer A[0:NA], the coefficients of the polynomial.
#
#  Output:
#
#    integer DEGREE, the degree of A.
#
  degree = na

  while ( 0 < degree ):

    if ( a[degree] != 0 ):
      return degree

    degree = degree - 1;

  return degree

def i4poly_degree_test ( ):

#*****************************************************************************80
#
## i4poly_degree_test() tests i4poly_degree().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4poly_degree_test():' )
  print ( '  i4poly_degree() returns the degree of an I4POLY.' )

  n = 10
  a = np.array ( [ 0, 1, 0, 3, 4, 0, 6, 7, 0, 0, 0 ] )

  i4poly_print ( n, a, '  The polynomial:' )

  degree = i4poly_degree ( n, a )

  print ( '' )
  print ( '  The polynomial degree is %d' % ( degree ) )

  return

def i4poly_dif ( na, a, d ):

#*****************************************************************************80
#
## i4poly_dif() differentiates an I4POLY.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the degree of polynomial A.
#
#    integer A[0:NA], the coefficients of a polynomial.
#
#    integer D, the number of times the polynomial
#    is to be differentiated.
#
#  Output:
#
#    integer B[0:NA-D], the coefficients of the
#    differentiated polynomial.
#
  import numpy as np

  if ( na < d ):
    b = np.zeros ( 1 )
    return b

  nb = na - d
  b = np.zeros ( nb + 1 )

  for i in range ( 0, nb + 1 ):
    b[i] = a[i+d] * i4_fall ( i + d, d )

  return b

def i4poly_dif_test ( ):

#*****************************************************************************80
#
## i4poly_dif_test() tests i4poly_dif().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 2

  print ( '' )
  print ( 'i4poly_dif_test():' )
  print ( '  i4poly_dif() computes derivatives of an I4POLY.' )
#
#  1: Differentiate X^3 + 2*X^2 - 5*X - 6 once.
#  2: Differentiate X^4 + 3*X^3 + 2*X^2 - 2  3 times.
#
  for test in range ( 0, 2 ):

    if ( test == 0 ):
      na = 3
      d = 1
      a = np.array ( [ -6, -5, 2, 1 ] )
    elif ( test == 1 ):
      na = 4
      d = 3
      a = np.array ( [ -2, 5, 2, 3, 1 ] )

    i4poly_print ( na, a, '  The polynomial A:' )

    print ( '' )
    print ( '  Differentiate A %d times.' % ( d ) )

    b = i4poly_dif ( na, a, d )
 
    i4poly_print ( na - d, b, '  The derivative, B:' )

  return

def i4poly_div ( na, a, nb, b ):

#*****************************************************************************80
#
## i4poly_div() computes the quotient and remainder of two polynomials.
#
#  Discussion:
#
#    Normally, the quotient and remainder would have rational coefficients.
#    This routine assumes that the special case applies that the quotient
#    and remainder are known beforehand to be integral.
#
#    The polynomials are assumed to be stored in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the dimension of A.
#
#    integer A(1:NA+1), the coefficients of the polynomial to be divided.
#
#    integer NB, the dimension of B.
#
#    integer B(1:NB+1), the coefficients of the divisor polynomial.
#
#  Output:
#
#    integer NQ, the degree of Q.
#    If the divisor polynomial is zero, NQ is returned as -1.
#
#    integer Q(1:NA-NB+1), contains the quotient of A/B.
#    If A and B have full degree, Q should be dimensioned Q(1:NA-NB+1).
#    In any case, Q(1:NA+1) should be enough.
#
#    integer NR, the degree of R.
#    If the divisor polynomial is zero, NR is returned as -1.
#
#    integer R(1:NB), contains the remainder of A/B.
#    If B has full degree, R should be dimensioned R(1:NB).
#    Otherwise, R will actually require less space.
#
  import numpy as np

  na2 = i4poly_degree ( na, a )
  nb2 = i4poly_degree ( nb, b )

  if ( b[nb2] == 0 ):
    nq = -1
    q = np.zeros ( 0 )
    nr = -1
    r = np.zeros ( 0 )
    return nq, q, nr, r

  a2 = np.zeros ( na + 1, dtype = np.int32 )
  for i in range ( 0, na + 1 ):
    a2[i] = a[i]

  nq = na2 - nb2
  q = np.zeros ( nq + 1, dtype = np.int32 )

  for i in range ( nq, -1, -1 ):
    q[i] = a2[i+nb2] // b[nb2]
    a2[i+nb2] = 0
    for j in range ( 0, nb2 ):
      a2[i+j] = a2[i+j] - q[i] * b[j]

  nr = nb2 - 1
  r = np.zeros ( nr + 1, dtype = np.int32 )

  for i in range ( 0, nr + 1 ):
    r[i] = a2[i]

  return nq, q, nr, r

def i4poly_div_test ( ):

#*****************************************************************************80
#
## i4poly_div_test() tests i4poly_div().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 2

  print ( '' )
  print ( 'i4poly_div_test():' )
  print ( '  i4poly_div() computes the quotient and' )
  print ( '  remainder for polynomial division.' )
  print ( '' )
#
#  1: Divide X^3 + 2*X^2 - 5*X - 6  by X-2.  
#     Quotient is 3+4*X+X^2, remainder is 0.
#
#  2: Divide X^4 + 3*X^3 + 2*X^2 - 2  by  X^2 + X - 3.
#     Quotient is X^2 + 2*X + 3, remainder 8*X + 7.
#
  for test in range ( 0, ntest ):

    if ( test == 0 ):
      na = 3
      a = np.array ( [ -6, -5, 2, 1 ] )
      nb = 1
      b = np.array ( [ -2, 1 ] )
    elif ( test == 1 ):
      na = 4
      a = np.array ( [ -2, 5, 2, 3, 1 ] )
      nb = 2
      b = np.array ( [ -3, 1, 1 ] )

    i4poly_print ( na, a, '  The polynomial to be divided, A:' )
    i4poly_print ( nb, b, '  The divisor polynomial, B:' )

    nq, q, nr, r = i4poly_div ( na, a, nb, b )
 
    i4poly_print ( nq, q, '  The quotient polynomial, Q:' )
    i4poly_print ( nr, r, '  The remainder polynomial, R:' )

  return

def i4poly_mul ( na, a, nb, b ):

#*****************************************************************************80
#
## i4poly_mul() computes the product of two integer polynomials A and B.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the dimension of A.
#
#    integer A[0:NA], the coefficients of the first polynomial factor.
#
#    integer NB, the dimension of B.
#
#    integer B[0:NB], the coefficients of the second polynomial factor.
#
#  Output:
#
#    integer C[0:NA+NB], the coefficients of A * B.
#
  import numpy as np

  nc = na + nb

  c = np.zeros ( nc + 1 )

  for i in range ( 0, na + 1 ):
    for j in range ( 0, nb + 1 ):
      c[i+j] = c[i+j] + a[i] * b[j]

  return c

def i4poly_mul_test ( ):

#*****************************************************************************80
#
## i4poly_mul_test() tests i4poly_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 2

  print ( '' )
  print ( 'i4poly_mul_test():' )
  print ( '  i4poly_mul() multiplies two polynomials.' )
#
#  1: Multiply (1+X) times (1-X).  Answer is 1-X^2.
#  2: Multiply (1+2*X+3*X^2) by (1-2*X). Answer is 1 + 0*X - X^2 - 6*X^3
#
  for test in range ( 0, ntest ):

    if ( test == 0 ):
      na = 1
      a = np.array ( [ 1, 1 ] )
      nb = 1
      b = np.array ( [ 1, -1 ] )
    elif ( test == 1 ):
      na = 2
      a = np.array ( [ 1, 2, 3 ] )
      nb = 1
      b = np.array ( [ 1, -2 ] )

    c = i4poly_mul ( na, a, nb, b )

    i4poly_print ( na, a, '  The factor A:' )
    i4poly_print ( nb, b, '  The factor B:' )
    i4poly_print ( na+nb, c, '  The product C = A*B:' )

  return

def i4poly_print ( n, a, title ):

#*****************************************************************************80
#
## i4poly_print() prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    integer A(1:N+1), the polynomial coefficients.
#    A(1) is the constant term and
#    A(N+1) is the coefficient of X**N.
#
#    character TITLE(*), an optional title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  print ( '' )

  n2 = i4poly_degree ( n, a )

  if ( a[n2] < 0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[n2] )

  if ( 2 <= n2 ):
    print ( ' p(x) = %c%d * x^%d' % ( plus_minus, mag, n2 ) )
  elif ( n2 == 1 ):
    print ( ' p(x) = %c%d * x' % ( plus_minus, mag ) )
  elif ( n2 == 0 ):
    print ( ' p(x) = %c%d' % ( plus_minus, mag ) )

  for i in range ( n2 - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0 ):

      if ( 2 <= i ):
        print ( '        %c%d * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '        %c%d * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '        %c%d' % ( plus_minus, mag ) )

  return

def i4poly_print_test ( ):

#*****************************************************************************80
#
## i4poly_print_test() tests i4poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4poly_print_test():' )
  print ( '  i4poly_print() prints an I4POLY.' )

  n = 4
  a = np.array ( [ -2, 5, 2, 3, 1 ] )

  i4poly_print ( n, a, '  The polynomial:' )

  return

def i4poly ( n, a, x0, iopt ):

#*****************************************************************************80
#
## i4poly() performs operations on integer polynomials in power or factorial form.
#
#  Discussion:
#
#    The power sum form of a polynomial is
#
#      P(X) = A1 + A2*X + A3*X^2 + ... + (AN+1)*X^N
#
#    The Taylor expansion at C has the form
#
#      P(X) = A1 + A2*(X-C) + A3*(X-C)^2 + ... + (AN+1)*(X-C)^N
#
#    The factorial form of a polynomial is
#
#      P(X) = A1 + A2*X + A3*(X)*(X-1) + A4*(X)*(X-1)*(X-2)+...
#        + (AN+1)*(X)*(X-1)*...*(X-N+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuism, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of coefficients in the polynomial
#    (in other words, the polynomial degree + 1)
#
#    integer A(N), the coefficients of the polynomial.
#
#    integer X0, for IOPT = -1, 0, or positive, the value of the
#    argument at which the polynomial is to be evaluated, or the
#    Taylor expansion is to be carried out.
#
#    integer IOPT, a flag describing which algorithm is to
#    be carried out:
#
#    -3: Reverse Stirling.  Input the coefficients of the polynomial in
#    factorial form, output them in power sum form.
#
#    -2: Stirling.  Input the coefficients in power sum form, output them
#    in factorial form.
#
#    -1: Evaluate a polynomial which has been input in factorial form.
#
#    0:  Evaluate a polynomial input in power sum form.
#
#    1 or more:  Given the coefficients of a polynomial in
#    power sum form, compute the first IOPT coefficients of
#    the polynomial in Taylor expansion form.
#
#  Output:
#
#    integer A(N), the coefficients of the output polynomial.
#    Depending on the option chosen, these coefficients are the input values,
#    or those of a different form of the polynomial.
#
#    integer VAL, for IOPT = -1 or 0, the value of the
#    polynomial at the point X0.
#
  val = 0

  n1 = min ( n, iopt )
  n1 = max ( 1, n1 )

  if ( iopt < -1 ):
    n1 = n

  delta = ( max ( -iopt, 0 ) % 2 )

  w = -n * delta

  if ( -2 < iopt ):
    w = w + x0

  for m in range ( 1, n1 + 1 ):

    val = 0
    z = w

    for i in range ( m, n + 1 ):
      z = z + delta
      val = a[n+m-i-1] + z * val
      if ( iopt != 0 and iopt != -1 ):
        a[n+m-i-1] = val

    if ( iopt < 0 ):
      w = w + 1

  return a, val

def i4poly_test ( ):

#*****************************************************************************80
#
## i4poly_test() test i4poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6

  print ( '' )
  print ( 'i4poly_test():' )
  print ( '  i4poly() converts between power sum, factorial' )
  print ( '  and Taylor forms, and can evaluate a polynomial' )
  print ( '' )
 
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      iopt = -3
      x0 = 0
    elif ( test == 2 ):
      iopt = -2
      x0 = 0
    elif ( test == 3 ):
      iopt = -1
      x0 = 2
    elif ( test == 4 ):
      iopt = 0
      x0 = 2
    elif ( test == 5 ):
      iopt = 6
      x0 = 2
    elif ( test == 6 ):
      iopt = 6
      x0 = -2

    a = np.array ( [ 0, 0, 0, 0, 0, 1 ] )

    if ( test == 1 ):
      print ( '' )
      print ( '  All calls have input A as follows:' )
      for i in range ( 0, n ):
        print ( '  %2d' % ( a[i] ) )
      print ( '' )
 
    a, val = i4poly ( n, a, x0, iopt )
 
    print ( '' )
    print ( '  Option IOPT = %d' % ( iopt ) )

    if ( -1 <= iopt ):
      print ( '  X0 = %d' % ( x0 ) )

    if ( iopt == -3 or iopt == -2 or 0 < iopt ):
      print ( '  Output array:' )
      for i in range ( 0, n ):
        print ( '  %2d' % ( a[i] ), end = '' )
      print ( '' )

    if ( iopt == -1 or iopt == 0 ):
      print ( '  Value = %d' % ( val ) )

  return

def i4poly_to_i4 ( n, a, x ):

#*****************************************************************************80
#
## i4poly_to_i4() evaluates an integer polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the polynomial.
#
#    integer A[0:N], the polynomial coefficients.
#    A(1) is the constant term and
#    A(N+1) is the coefficient of X^N.
#
#    integer X, the point at which the polynomial is to be evaluated.
#
#  Output:
#
#    integer VALUE, the value of the polynomial.
#
  value = 0

  for i in range ( n, -1, -1 ):
    value = value * x + a[i]

  return value

def i4poly_to_i4_test ( ):

#*****************************************************************************80
#
## i4poly_to_i4_test() tests i4poly_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 9

  base_test = np.array ( [ 2, 2, 2, 3, 4, 5, 6, 23, 24 ] )
  intval_test = np.array ( [ 1, 6, 23, 23, 23, 23, 23, 23, 23 ] )

  print ( '' )
  print ( 'i4poly_to_i4_test():' )
  print ( '  i4poly_to_i4() evaluates an integer polynomial.' )
  print ( '' )
  print ( '       I    BASE  DEGREE  Coefficients' )
  print ( '' )

  degree_max = 10

  for test in range ( 0, test_num ):
    intval = intval_test[test]
    base = base_test[test]
    a, degree = i4_to_i4poly ( intval, base, degree_max )
    print ( '  %6d  %6d  %6d' % ( intval, base, degree ), end = '' )
    for i in range ( degree, -1, -1 ):
      print ( '  %6d' % (a[i] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  Now let i4_to_i4poly() convert I to a polynomial,' )
  print ( '  use i4poly_to_i4*( to evaluate it, and compare.' )
  print ( '' )
  print ( '       I    I2' )
  print ( '' )

  for test in range ( 0, test_num ):
    intval = intval_test[test]
    base = base_test[test]
    a, degree = i4_to_i4poly ( intval, base, degree_max )
    intval2 = i4poly_to_i4 ( degree, a, base )
    print ( '  %6d  %6d' % ( intval, intval2 ) )

  return

def i4_rise ( x, n ):

#*****************************************************************************80
#
## i4_rise() computes the rising factorial function [X]^N.
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
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the rising factorial function.
#
#    integer N, the order of the rising factorial function.
#    If N = 0, RISE = 1, if N = 1, RISE = X.  Note that if N is
#    negative, a "falling" factorial will be computed.
#
#  Output:
#
#    integer VALUE, the value of the rising factorial function.
#
  value = 1

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg + 1

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg - 1

  return value

def i4_rise_test ( ):

#*****************************************************************************80
#
## i4_rise_test() tests i4_rise().
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
  print ( '' )
  print ( 'i4_rise_test():' )
  print ( '  i4_rise() evaluates the rising factorial Fall(I,N).' )
  print ( '' )
  print ( '         M         N      Exact         i4_rise(M,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = i4_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_rise ( m, n )

    print ( '  %8d  %8d  %12d  %12d' % ( m, n, f1, f2 ) )

  return

def i4_rise_values ( n_data ):

#*****************************************************************************80
#
## i4_rise_values() returns values of the integer rising factorial function.
#
#  Discussion:
#
#    The integer rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) ... * ( m - 1 + n )
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer M, N, the arguments of the function.
#
#    integer FMN, the value of the function.
#
  import numpy as np

  n_max = 15

  fmn_vec = np.array ( [ 
     1, 5, 30, 210, 1680, \
     15120, 151200, 1, 10, 4000, \
     110, 6840, 840, 970200, 5040 ] )
  m_vec = np.array ( [ 
    5, 5, 5, 5, 5, \
    5, 5, 50, 10, 4000, \
    10, 18, 4, 98, 1 ] )
  n_vec = np.array ( [ 
     0, 1, 2, 3, 4, \
    5, 6, 0, 1, 1, \
    2, 3, 4, 3, 7 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
    n = 0
    fmn = 0
  else:
    m = m_vec[n_data]
    n = n_vec[n_data]
    fmn = fmn_vec[n_data]
    n_data = n_data + 1

  return n_data, m, n, fmn

def i4_rise_values_test ( ):

#*****************************************************************************80
#
## i4_rise_values_test() tests i4_rise_values.
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
  print ( '' )
  print ( 'i4_rise_values_test():' )
  print ( '  i4_rise_values() returns values of the integer rising factorial.' )
  print ( '' )
  print ( '          M         N          i4_rise(M,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, fmn = i4_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %8d  %8d' % ( m, n, fmn ) )

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

def i4_sqrt_cf ( n, max_term ):

#*****************************************************************************80
#
## i4_sqrt_cf() finds the continued fraction representation of a square root of an integer.
#
#  Discussion:
#
#    The continued fraction representation of the square root of an integer
#    has the form
#
#      [ B0, (B1, B2, B3, ..., BM), ... ]
#
#    where
#
#      B0 = int ( sqrt ( real ( N ) ) )
#      BM = 2 * B0
#      the sequence ( B1, B2, B3, ..., BM ) repeats in the representation.
#      the value M is termed the period of the representation.
#
#  Example:
#
#     N  Period  Continued Fraction
#
#     2       1  [ 1, 2, 2, 2, ... ]
#     3       2  [ 1, 1, 2, 1, 2, 1, 2... ]
#     4       0  [ 2 ]
#     5       1  [ 2, 4, 4, 4, ... ]
#     6       2  [ 2, 2, 4, 2, 4, 2, 4, ... ]
#     7       4  [ 2, 1, 1, 1, 4, 1, 1, 4, 1, 1, 4... ]
#     8       2  [ 2, 1, 4, 1, 4, 1, 4, 1, 4, ... ]
#     9       0  [ 3 ]
#    10       1  [ 3, 6, 6, 6, ... ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#   John Burkardt
#
#  Reference:
#
#    Mark Herkommer,
#    Number Theory, A Programmer's Guide,
#    McGraw Hill, 1999, pages 294-307.
#
#  Input:
#
#    integer N, the number whose continued fraction square root
#    is desired.
#
#    integer MAX_TERM, the maximum number of terms that may
#    be computed.
#
#  Output:
#
#    integer B(1:N_TERM), the continued fraction coefficients.
#
#    integer N_TERM, the number of terms computed  The routine should 
#    stop if it detects that the period has been reached.
#
  import numpy as np

  c = np.zeros ( max_term + 1 )

  n_term = 0

  s, r = i4_sqrt ( n )

  c[0] = s

  if ( 0 < r ):

    p = 0
    q = 1

    while ( True ):

      p = c[n_term+1-1] * q - p
      q = ( ( n - p * p ) // q )

      if ( max_term <= n_term ):
        break

      n_term = n_term + 1
      c[n_term+1-1] = ( ( p + s ) // q )

      if ( q == 1 ):
        break

  b = np.zeros ( n_term+1 )
  for i in range ( 0, n_term + 1 ):
    b[i] = c[i]

  return b, n_term

def i4_sqrt_cf_test ( ):

#*****************************************************************************80
#
## i4_sqrt_cf_test() tests i4_sqrt_cf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  max_term = 100

  print ( '' )
  print ( 'i4_sqrt_cf_test():' )
  print ( '  i4_sqrt_cf() computes the continued fraction form' )
  print ( '  of the square root of an integer.' )
  print ( '' )
  print ( '   N  Period  Whole  Repeating Part' )
  print ( '' )

  for n in range ( 1, 21 ):

    b, n_term = i4_sqrt_cf ( n, max_term )

    print ( '  %3d  %6d  %5d' % ( n, n_term, b[0] ), end = '' )
    for i in range ( 1, n_term + 1 ):

      print ( '  %3d' % ( b[i] ), end = '' )
      
      if ( ( ( i + 1 ) % 10 ) == 0 ):
        print ( '' )
        print ( '               ', end = '' )

    print ( '' )

  return

def i4_sqrt ( n ):

#*****************************************************************************80
#
## i4_sqrt() finds the integer square root of N by solving N = Q^2 + R.
#
#  Discussion:
#
#    The integer square root of N is an integer Q such that
#    Q^2 <= N but N < (Q+1)^2.
#
#    A simpler calculation would be something like
#
#      Q = INT ( SQRT ( REAL ( N ) ) )
#
#    but this calculation has the virtue of using only integer arithmetic.
#
#    To avoid the tedium of worrying about negative arguments, the routine
#    automatically considers the absolute value of the argument.
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
#   John Burkardt
#
#  Reference:
#
#    Mark Herkommer,
#    Number Theory, A Programmer's Guide,
#    McGraw Hill, 1999, pages 294-307.
#
#  Input:
#
#    integer N, the number whose integer square root is desired.
#    Actually, only the absolute value of N is considered.
#
#  Output:
#
#    integer Q, R, the integer square root, and positive remainder,
#    of N.
#
  n_abs = abs ( n )

  q = n_abs

  if ( 0 < n_abs ):

    while ( ( n_abs // q ) < q ):
      q = ( ( q + ( n_abs // q ) ) // 2 )

  r = n_abs - q * q

  return q, r

def i4_sqrt_test ( ):

#*****************************************************************************80
#
## i4_sqrt_test() tests i4_sqrt().
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
  print ( '' )
  print ( 'i4_sqrt_test():' )
  print ( '  i4_sqrt() computes the square root of an I4.' )
  print ( '' )
  print ( '       N  Sqrt(N) Remainder' )
  print ( '' )

  for n in range ( -5, 21 ):
    q, r = i4_sqrt ( n )

    print ( '  %7d  %7d  %7d' % ( n, q, r ) )

  return

def i4_to_chinese ( j, n, m ):

#*****************************************************************************80
#
## i4_to_chinese() converts an integer to its Chinese remainder form.
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
#  Input:
#
#    integer J, the integer to be converted.
#
#    integer N, the number of moduluses.
#
#    integer M(N), the moduluses.  These should be positive
#    and pairwise prime.
#
#  Output:
#
#    integer R(N), the Chinese remainder representation of the integer.
#
  import numpy as np

  ierror = chinese_check ( n, m )

  if ( ierror != 0 ):
    print ( '' )
    print ( 'i4_to_chinese(): Fatal error!' )
    print ( '  The moduluses are not legal.' )
    raise Exception ( 'i4_to_chinese(): Fatal error!' )

  r = np.zeros ( n )

  for i in range ( 0, n ):
    r[i] = i4_modp ( j, m[i] )

  return r

def i4_to_chinese_test ( ):

#*****************************************************************************80
#
## i4_to_chinese_test() tests i4_to_chinese().
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

  n = 4
  m = np.array ( [ 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'i4_to_chinese_test():' )
  print ( '  i4_to_chinese() computes the Chinese Remainder' )
  print ( '  representation of an integer.' )

  i4vec_print ( n, m, '  The moduli:' )

  j = 37

  print ( '' )
  print ( '  The number being analyzed is %d' % ( j ) )

  r = i4_to_chinese ( j, n, m )

  i4vec_print ( n, r, '  The remainders:' )

  j2 = chinese_to_i4 ( n, m, r )

  print ( '' )
  print ( '  The reconstructed number is %d' % ( j2 ) )

  r = i4_to_chinese ( j2, n, m )

  i4vec_print ( n, r, '  The remainders of the reconstructed number are:' )

  return

def i4_to_dvec ( i, n ):

#*****************************************************************************80
#
## i4_to_dvec() makes a signed decimal vector from an integer.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10**(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, an integer to be represented.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    integer DVEC(N), the signed decimal representation.
#
  import numpy as np

  base = 10
  i2 = abs ( i )

  dvec = np.zeros ( n, dtype = np.int32 )

  for j in range ( 0, n - 1 ):
    dvec[j] = ( i2 % base )
    i2 = ( i2 // base )

  dvec[n-1] = 0

  if ( i < 0 ):
    dvec = dvec_complementx ( n, dvec )

  return dvec

def i4_to_dvec_test ( rng ):

#*****************************************************************************80
#
## i4_to_dvec_test() tests i4_to_dvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4_to_dvec_test():' )
  print ( '  i4_to_dvec() converts an I4 to a DVEC.' )
  print ( '' )
  print ( '        I4 => DVEC => I4' )
  print ( '' )

  i1 = rng.integers ( low = -10000, high = 10000, endpoint = True )

  n = 6
  dvec = i4_to_dvec ( i1, n )

  i2 = dvec_to_i4 ( n, dvec )

  print ( '  %6d  ' % ( i1 ), end = '' )
  for i in range ( n - 1, -1, -1 ):
    print ( '%2d' % ( dvec[i] ), end = '' )
  print ( '  %6d' % ( i2 ) )

  return

def i4_to_i4poly ( intval, base, degree_max ):

#*****************************************************************************80
#
## i4_to_i4poly() converts an integer to an integer polynomial in a given base.
#
#  Example:
#
#    INTVAL  BASE  Degree     A (in reverse order!)
#
#         1     2       0     1
#         6     2       2     1  1  0
#        23     2       4     1  0  1  1  1
#        23     3       2     2  1  2
#        23     4       2     1  1  3
#        23     5       1     4  3
#        23     6       1     3  5
#        23    23       1     1  0
#        23    24       0    23
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer INTVAL, an integer to be converted.
#
#    integer BASE, the base, which should be greater than 1.
#
#    integer DEGREE_max, the maximum degree.
#
#  Output:
#
#    integer A[0:DEGREE], contains the coefficients
#    of the polynomial expansion of INTVAL in base BASE.
#
#    integer DEGREE, the degree of the polynomial.
#
  import numpy as np

  a = np.zeros ( degree_max + 1 )

  j = abs ( intval )

  degree = 0

  a[degree] = ( j % base )

  j = j - a[degree]
  j = ( j // base )

  while ( 0 < j ):

    degree = degree + 1

    a[degree] = ( j % base )

    j = j - a[degree]
    j = ( j // base )

  if ( intval < 0 ):
    for i in range ( 0, degree + 1 ):
      a[i] = - a[i]

  return a, degree

def i4_to_i4poly_test ( ):

#*****************************************************************************80
#
## i4_to_i4poly_test() tests i4_to_i4poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 9

  base_test = np.array ( [ 2, 2, 2, 3, 4, 5, 6, 23, 24 ] )
  intval_test = np.array ( [ 1, 6, 23, 23, 23, 23, 23, 23, 23 ] )

  print ( '' )
  print ( 'i4_to_i4poly_test():' )
  print ( '  i4_to_i4poly() converts an integer to a polynomial' )
  print ( '  in a given base' )
  print ( '' )
  print ( '       I    BASE  DEGREE  Coefficients' )
  print ( '' )

  for test in range ( 0, test_num ):
    intval = intval_test[test]
    base = base_test[test]
    degree_max = 9
    a, degree = i4_to_i4poly ( intval, base, degree_max )
    print ( '  %6d  %6d  %6d' % ( intval, base, degree ), end = '' )
    for i in range ( degree, -1, -1 ):
      print ( '  %6d' % ( a[i] ), end = '' )
    print ( '' )

  return

def i4_to_van_der_corput ( key, base ):

#*****************************************************************************80
#
## i4_to_van_der_corput() computes an element of a van der Corput sequence.
#
#  Discussion:
#
#    The van der Corput sequence is often used to generate a "subrandom"
#    sequence of points which have a better covering property
#    than pseudorandom points.
#
#    The van der Corput sequence generates a sequence of points in [0,1]
#    which (theoretically) never repeats.  Except for KEY = 0, the
#    elements of the van der Corput sequence are strictly between 0 and 1.
#
#    The van der Corput sequence writes an integer in a given base B,
#    and then its digits are "reflected" about the decimal point.
#    This maps the numbers from 1 to N into a set of numbers in [0,1],
#    which are especially nicely distributed if N is one less
#    than a power of the base.
#
#    Hammersley suggested generating a set of N nicely distributed
#    points in two dimensions by setting the first component of the
#    Ith point to I/N, and the second to the van der Corput 
#    value of I in base 2.  
#
#    Halton suggested that in many cases, you might not know the number 
#    of points you were generating, so Hammersley's formulation was
#    not ideal.  Instead, he suggested that to generated a nicely
#    distributed sequence of points in M dimensions, you simply
#    choose the first M primes, P(1:M), and then for the J-th component of
#    the I-th point in the sequence, you compute the van der Corput
#    value of I in base P(J).
#
#    Thus, to generate a Halton sequence in a 2 dimensional space,
#    it is typical practice to generate a pair of van der Corput sequences,
#    the first with prime base 2, the second with prime base 3.
#    Similarly, by using the first K primes, a suitable sequence
#    in K-dimensional space can be generated.
#
#    The generation is quite simple.  Given an integer KEY, the expansion
#    of KEY in base BASE is generated.  Then, essentially, the result R
#    is generated by writing a decimal point followed by the digits of
#    the expansion of KEY, in reverse order.  This decimal value is actually
#    still in base BASE, so it must be properly interpreted to generate
#    a usable value.
#
#  Example:
#
#    BASE = 2
#
#    KEY      KEY       van der Corput
#    decimal  binary    binary   decimal
#    -------  ------    ------   -------
#        0  =     0  =>  .0     = 0.0
#        1  =     1  =>  .1     = 0.5
#        2  =    10  =>  .01    = 0.25
#        3  =    11  =>  .11    = 0.75
#        4  =   100  =>  .001   = 0.125
#        5  =   101  =>  .101   = 0.625
#        6  =   110  =>  .011   = 0.375
#        7  =   111  =>  .111   = 0.875
#        8  =  1000  =>  .0001  = 0.0625
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    J H Halton,
#    On the efficiency of certain quasi-random sequences of points
#    in evaluating multi-dimensional integrals,
#    Numerische Mathematik,
#    Volume 2, pages 84-90, 1960.
# 
#    J M Hammersley,
#    Monte Carlo methods for solving multivariable problems,
#    Proceedings of the New York Academy of Science,
#    Volume 86, pages 844-874, 1960.
#
#    J G van der Corput,
#    Verteilungsfunktionen I & II,
#    Nederl. Akad. Wetensch. Proc.,
#    Volume 38, 1935, pages 813-820, pages 1058-1066.
#
#  Input:
#
#    integer KEY, the index of the desired element.
#    KEY should be nonnegative.  Only the integer part of KEY is used.
#    KEY = 0 is allowed, and returns R = 0.
#
#    integer BASE, the van der Corput base, which is typically
#    a prime number.  Only the integer part of BASE is used.
#    BASE must be greater than 1.
#
#  Output:
#
#    real R, the KEY-th element of the van der Corput sequence
#    for base BASE.
#
  r = 0.0
#
#  Ensure that BASE is an integer, and acceptable.
#
  base = int ( base )

  if ( base <= 1 ):
    print ( '' )
    print ( 'i4_to_van_der_corput(): Fatal error!' )
    print ( '  The input base BASE is <= 1!' )
    print ( '  BASE = %d' % ( base ) )
    raise Exception ( 'i4_to_van_der_corput(): Fatal error!' )
#
#  Ensure that KEY is an integer, and acceptable.
#
  key = int ( key )

  if ( key < 0 ):
    print ( '' )
    print ( 'i4_to_van_der_corput(): Fatal error!' )
    print ( '  The input base KEY is < 0!' )
    print ( '  KEY = %d' % ( key ) )
    raise Exception ( 'i4_to_van_der_corput(): Fatal error!' );
#
#  Carry out the computation.
#
  base_inv = 1.0 / float ( base )

  while ( key != 0 ):
    digit = ( key % base )
    r = r + float ( digit ) * base_inv
    base_inv = base_inv / float ( base )
    key = ( key // base )

  return r

def i4_to_van_der_corput_test ( ):

#*****************************************************************************80
#
## i4_to_van_der_corput_test() tests i4_to_van_der_corput().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_prime = 5
  n_test = 10

  print ( '' )
  print ( 'i4_to_van_der_corput_test():' )
  print ( '  i4_to_van_der_corput() computes the elements' )
  print ( '  of a van der Corput sequence.' )
  print ( '  The sequence depends on the prime numbers used' )
  print ( '  as a base.' )
  print ( '' )
  print ( '  Bases:' )
  print ( '' )
  print ( '' )
  for j in range ( 1, n_prime + 1 ):
    print ( '        %6d' % prime ( j ), end = '' )
  print ( '' )
  print ( '' )

  h = np.zeros ( n_prime )

  for i in range ( 0, n_test ):
    for j in range ( 1, n_prime + 1 ):
      jm1 = j - 1
      p = prime ( j )
      h[jm1] = i4_to_van_der_corput ( i, p )

    print ( '  %2d' % ( i ), end = '' )
    for j in range ( 1, n_prime + 1 ):
      jm1 = j - 1
      print ( '  %12f' % ( h[jm1] ), end = '' )
    print ( '' )

  return

def i4vec_ascends ( n, x ):

#*****************************************************************************80
#
## i4vec_ascends() is TRUE if an I4VEC is increasing.
#
#  Example:
#
#    X = ( 9, 7, 7, 3, 2, 1, -8 )
#
#    i4vec_ascends = FALSE
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the array.
#
#    integer X(N), the array to be examined.
#
#  Output:
#
#    bool VALUE, is TRUE if the entries of X ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i] > x[i+1] ):
      value = False
      break

  return value

def i4vec_ascends_test ( ):

#*****************************************************************************80
#
## i4vec_ascends_test() tests i4vec_ascends().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  test_num = 6

  x_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 2, 2 ], \
    [ 1, 2, 2, 4 ], \
    [ 1, 2, 3, 4 ], \
    [ 4, 4, 3, 1 ], \
    [ 9, 7, 3, 0 ] ] )

  print ( '' )
  print ( 'i4vec_ascends_test():' )
  print ( '  i4vec_ascends() determines if an I4VEC ascends.' )

  for i in range ( 0, test_num ):

    x = np.zeros ( n )
    for j in range ( 0, n ):
      x[j] = x_test[i,j]

    i4vec_transpose_print ( n, x, '  Test vector:' )

    value = i4vec_ascends ( n, x )

    print ( '  i4vec_ascends = %s' % ( value ) )

  return

def i4vec_backtrack ( n, maxstack, x, indx, k, nstack, stacks, ncan ):

#*****************************************************************************80
#
## i4vec_backtrack() supervises a backtrack search for a vector.
#
#  Discussion:
#
#    The routine tries to construct a vector one index at a time,
#    using possible candidates as supplied by the user.
#
#    At any time, the partially constructed vector may be discovered to be
#    unsatisfactory, but the routine records information about where the
#    last arbitrary choice was made, so that the search can be
#    carried out efficiently, rather than starting out all over again.
#
#    First, call the routine with INDX = 0 so it can initialize itself.
#
#    Now, on each return from the routine, if INDX is:
#      1, you've just been handed a complete candidate vector
#         Admire it, analyze it, do what you like.
#      2, please determine suitable candidates for position X(K).
#         Return the number of candidates in NCAN(K), adding each
#         candidate to the end of STACKS, and increasing NSTACK.
#      3, you're done.  Stop calling the routine
#
#    At one time, the variable "stacks" was called "stack", but MATLAB
#    now seems to have taken "stack" as a keyword that is no longer
#    acceptable as a variable name.
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
#    integer N, the number of positions to be filled in the vector.
#
#    integer MAXSTACK, the maximum length of the stack.
#
#    integer X(N), the partially filled in candidate vector.
#
#    integer INDX, a communication flag.
#    * 0, to begin a backtracking search.
#    * 2, the requested candidates for position K have been added to
#      STACKS, and NCAN(K) was updated.
#
#    integer K, the index in X that we are trying to fill.
#
#    integer NSTACK, the current length of the stack.
#
#    integer STACKS(MAXSTACK), a list of all current candidates for
#    all positions 1 through K.
#
#    integer NCAN(N), lists the current number of candidates for
#    all positions 1 through K.
#
#  Output:
#
#    integer X(N), the partially filled in candidate vector.
#
#    integer INDX, a communication flag.
#    * 1, a complete output vector has been determined and returned in X(1:N)
#    * 2, candidates are needed for position X(K)
#    * 3, no more possible vectors exist.
#
#    integer K, the index in X that we are trying to fill.
#
#    integer NSTACK, the current length of the stack.
#
#    integer STACKS(MAXSTACK), a list of all current candidates for
#    all positions 1 through K.
#
#    integer NCAN(N), lists the current number of candidates for
#    all positions 1 through K.
#

#
#  If this is the first call, request a candidate for position 1.
#
  if ( indx == 0 ):
    k = 1
    nstack = 0
    indx = 2
    return x, indx, k, nstack, stacks, ncan
#
#  Examine the stack.
#
  while ( True ):
#
#  If there are candidates for position K, take the first available
#  one off the stack, and increment K.
#
#  This may cause K to reach the desired value of N, in which case
#  we need to signal the user that a complete set of candidates
#  is being returned.
#
    if ( 0 < ncan[k-1] ):
      x[k-1] = stacks[nstack-1]
      nstack = nstack - 1

      ncan[k-1] = ncan[k-1] - 1

      if ( k != n ):
        k = k + 1
        indx = 2
      else:
        indx = 1

      break
#
#  If there are no candidates for position K, then decrement K.
#  If K is still positive, repeat the examination of the stack.
#
    else:

      k = k - 1

      if ( k <= 0 ):
        indx = 3
        break

  return x, indx, k, nstack, stacks, ncan

def i4vec_backtrack_test ( ):

#*****************************************************************************80
#
## i4vec_backtrack_test() tests i4vec_backtrack().
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

  print ( '' )
  print ( 'i4vec_backtrack_test():' )
  print ( '  i4vec_backtrack() uses backtracking, seeking a vector X of' )
  print ( '  N values which satisfies some condition.' )

  print ( '' )
  print ( '  In this demonstration, we have 8 integers W(I).' )
  print ( '  We seek all subsets that sum to 53.' )
  print ( '  X(I) is 0 or 1 if the entry is skipped or used.' )
  print ( '' )

  n = 8
  maxstack = 100
  stacks = np.zeros ( maxstack )
  x = np.zeros ( n )
  indx = 0
  k = 1
  nstack = 0
  ncan = np.zeros ( n )

  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ], dtype = np.int32 )
  t = 53

  found_num = 0

  while ( True ):

    x, indx, k, nstack, stacks, ncan = i4vec_backtrack ( n, maxstack, \
    x, indx, k, nstack, stacks, ncan )

    if ( indx == 1 ):

      found_num = found_num + 1
      print ( '  %2d   ' % ( found_num ), end = '' )

      total = 0
      for i in range ( 0, n ):
        if ( x[i] == 1 ):
          total = total + w[i]
      print ( '  %2d:  ' % ( total ), end = '' )

      for i in range ( 0, n ):
        if ( x[i] == 1 ):
          print ( '  %d' % ( w[i] ), end = '' )
      print ( '' )
#
#  Given that we've chose X(1:K-1), what are our choices for X(K)?
#
#    if T < TOTAL, 
#      no choices
#    if T = TOTAL, 
#      X(K) = 0
#    if T > TOTAL and K < N, 
#      X(k) = 0
#      If ( W(K)+TOTAL <= T ) X(K) = 1
#    If T > TOTAL and K = N,
#      If ( W(K) + TOTAL) = T ) X(K) = 1
#
    elif ( indx == 2 ):

      total = 0
      for i in range ( 0, k - 1 ):
        if ( x[i] == 1 ):
          total = total + w[i]

      if ( t < total ):

        ncan[k-1] = 0

      elif ( t == total ):

        ncan[k-1] = ncan[k-1] + 1
        nstack = nstack + 1
        stacks[nstack-1] = 0

      elif ( total < t and k < n ):

        ncan[k-1] = ncan[k-1] + 1
        nstack = nstack + 1
        stacks[nstack-1] = 0

        if ( total + w[k-1] <= t ):
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1

      elif ( total < t and k == n ):

        if ( total + w[k-1] == t ):
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1

    else:

      print ( '' )
      print ( '  Done!' )
      break

  return

def i4vec_decrement ( n, v ):

#*****************************************************************************80
#
## i4vec_decrement() decrements an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the I4VEC.
#
#    integer V[N], the vector to be decremented.
#
#  Output:
#
#    integer V[N], the decremented vector.
#
  v[0:n] = v[0:n] - 1

  return v

def i4vec_decrement_test ( rng ):

#*****************************************************************************80
#
## i4vec_decrement_test() tests i4vec_decrement().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'i4vec_decrement_test():' )
  print ( '  i4vec_decrement() decrements an I4VEC.' )

  v_lo = -5
  v_hi = 10
  v = rng.integers ( low = v_lo, high = v_hi, size = n, endpoint = True )
  i4vec_print ( n, v, '  The I4VEC:' )
  v = i4vec_decrement ( n, v )
  i4vec_print ( n, v, '  The I4VEC after decrementing:' )

  return

def i4vec_descends ( n, x ):

#*****************************************************************************80
#
## i4vec_descends() is TRUE if an integer vector is decreasing.
#
#  Example:
#
#    X = ( 9, 7, 7, 3, 2, 1, -8 )
#
#    i4vec_descends = TRUE
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the array.
#
#    integer X(N), the array to be examined.
#
#  Output:
#
#    bool VALUE, is TRUE if the entries of X descend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i] < x[i+1] ):
      value = False
      break

  return value

def i4vec_descends_test ( ):

#*****************************************************************************80
#
## i4vec_descends_test() tests i4vec_descends().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  test_num = 6

  x_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 2, 2 ], \
    [ 1, 2, 2, 4 ], \
    [ 1, 2, 3, 4 ], \
    [ 4, 4, 3, 1 ], \
    [ 9, 7, 3, 0 ] ] )

  print ( '' )
  print ( 'i4vec_descends_test():' )
  print ( '  i4vec_descends() determines if an I4VEC descends.' )

  for i in range ( 0, test_num ):

    x = np.zeros ( n )
    for j in range ( 0, n ):
      x[j] = x_test[i,j]

    i4vec_transpose_print ( n, x, '  Test vector:' )

    value = i4vec_descends ( n, x )

    print ( '  i4vec_descends = %s' % ( value ) )

  return

def i4vec_frac ( n, a, k ):

#*****************************************************************************80
#
## i4vec_frac() searches for the K-th smallest entry in an N-vector.
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
#    26 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    integer A(N), the array to search.
#
#    integer K, the fractile to be sought.  If K = 1, the minimum
#    entry is sought.  If K = N, the maximum is sought.  Other values
#    of K search for the entry which is K-th in size.  K must be at
#    least 1, and no greater than N.
#
#  Output:
#
#    integer FRAC, the value of the K-th fractile of A.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'i4vec_frac(): Fatal error!' )
    print ( '  Illegal nonpositive value of N = %d' % ( n ) )
    raise Exception ( 'i4vec_frac(): Fatal error!' )

  if ( k <= 0 ):
    print ( '' )
    print ( 'i4vec_frac(): Fatal error!' )
    print ( '  Illegal nonpositive value of K = %d' % ( k ) )
    raise Exception ( 'i4vec_frac(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'i4vec_frac(): Fatal error!' )
    print ( '  Illegal N < K, K = %d' % ( k ) )
    raise Exception ( 'i4vec_frac(): Fatal error!' )

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
        break
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

def i4vec_frac_test ( rng ):

#*****************************************************************************80
#
## i4vec_frac_test() tests i4vec_frac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  b = 1
  c = 2 * n

  print ( '' )
  print ( 'i4vec_frac_test():' )
  print ( '  i4vec_frac(): K-th smallest integer vector entry.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  The array to search:' )

  print ( '' )
  print ( '  Fractile    Value' )
  print ( '' )

  nh = ( n // 3 )

  for k in range ( 1, n + 1, nh ):

    afrac = i4vec_frac ( n, a, k )

    print ( '  %6d  %6d' % ( k, afrac ) )

  return

def i4vec_index ( n, a, aval ):

#*****************************************************************************80
#
## i4vec_index() returns the location of the first occurrence of a given value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector to be searched.
#
#    integer AVAL, the value to be indexed.
#
#  Output:
#
#    integer VALUE, the first location in A which has the
#    value AVAL, or -1 if no such index exists.
#
  value = -1

  for i in range ( 0, n ):
    if ( a[i] == aval ):
      value = i
      break

  return value

def i4vec_index_test ( rng ):

#*****************************************************************************80
#
## i4vec_index_test() tests i4vec_index();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'i4vec_index_test():' )
  print ( '  i4vec_index(): first index of given value;' )

  a = rng.integers ( low = -n, high = n, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  i = ( n // 2 )
  aval = a[i]

  print ( '' )
  j = i4vec_index ( n, a, aval )
  print ( '  Index of first occurrence of %d is %d' % ( aval, j ) )

  aval = aval + 1
  j = i4vec_index ( n, a, aval )
  print ( '  Index of first occurrence of %d is %d' % ( aval, j ) )

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

  a = np.zeros ( n, dtype = np.int32 )

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

  a = np.zeros ( n, dtype = np.int32 )

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

def i4vec_max_index_last ( n, a ):

#*****************************************************************************80
#
## i4vec_max_index() returns the index of the last largest entry in an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of integer values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector to be searched.
#
#  Output:
#
#    integer MAX_index_last, the index of the last largest entry.
#
  if ( n <= 0 ):

    max_index_last = -1

  else:

    amax = a[0]
    max_index_last = 0

    for i in range ( 1, n ):

      if ( amax <= a[i] ):
        amax = a[i]
        max_index_last = i

  return max_index_last

def i4vec_max_index_last_test ( rng ):

#*****************************************************************************80
#
## i4vec_max_index_last_test() tests i4vec_max_index_last().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 15

  print ( '' )
  print ( 'i4vec_max_index_last_test():' )
  print ( '  i4vec_max_index_last(), last maximal index' )

  i4_lo = 0
  i4_hi = + ( n // 4 )

  a = rng.integers ( low = i4_lo, high = i4_hi, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  print ( '' )

  ival = i4vec_max_index_last ( n, a )
  print ( '  Last maximum index: %d' % ( ival ) )

  return

def i4vec_pairwise_prime ( n, a ):

#*****************************************************************************80
#
## i4vec_pairwise_prime() checks whether a vector of integers is pairwise prime.
#
#  Discussion:
#
#    Two positive integers I and J are pairwise prime if they have no common
#    factor greater than 1.
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
#  Input:
#
#    integer N, the number of values to check.
#
#    integer A(N), the vector of integers.
#
#  Output:
#
#    bool VALUE, is TRUE if the vector of integers
#    is pairwise prime.
#
  value = True

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      if ( i4_gcd ( a[i], a[j] ) != 1 ):
        value = False
        break

  return value

def i4vec_pairwise_prime_test ( ):

#*****************************************************************************80
#
## i4vec_pairwise_prime_test() tests i4vec_pairwise_prime().
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

  n = 4
  test_num = 6

  x_test = np.array ( [ \
     [ 1,  3,  2,  4 ], \
     [ 2,  2,  2,  2 ], \
     [ 5,  7, 12, 29 ], \
     [ 1, 13,  1, 11 ], \
     [ 1,  4,  9, 16 ], \
     [ 6, 35, 13, 77 ] ] )

  x = np.zeros ( n )

  print ( '' )
  print ( 'i4vec_pairwise_prime_test():' )
  print ( '  i4vec_pairwise_prime() determines if a vector of' )
  print ( '  integers is pairwise prime.' )
  print ( '' )
  print ( '                          Pairwise' )
  print ( '  Row Vector              Prime?' )
  print ( ''
 )
  for test in range ( 0, test_num ):

    for j in range ( 0, n ):
      x[j] = x_test[test,j]

    value = i4vec_pairwise_prime ( n, x )

    for j in range ( 0, n ):
      print ( '  %3d' % ( x[j] ), end = '' )
    print ( '  %s' % ( value ) )

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
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  return

def i4vec_product ( n, a ):

#*****************************************************************************80
#
## i4vec_product() computes the product of the entries of an I4VEC.
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
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the product of the entries.
#
  value = 1
  for i in range ( 0, n ):
    value = value * a[i]

  return value

def i4vec_product_test ( rng ):

#*****************************************************************************80
#
## i4vec_product_test() tests i4vec_product().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_product_test():' )
  print ( '  i4vec_product() computes the product of the entries in an I4VEC.' )

  n = 10
  i4_lo = - 5
  i4_hi = + 5

  a = rng.integers ( low = i4_lo, high = i4_hi, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  value = i4vec_product ( n, a )
  print ( '' )
  print ( '  Product of entries = %d' % ( value ) )

  return

def i4vec_reverse ( n, a ):

#*****************************************************************************80
#
## i4vec_reverse() reverses the elements of an I4VEC.
#
#  Example:
#
#    Input:
#
#      N = 5,
#      A = ( 11, 12, 13, 14, 15 ).
#
#    Output:
#
#      A = ( 15, 14, 13, 12, 11 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    integer A(N), the array to be reversed.
#
#  Output:
#
#    integer A(N), the reversed array.
#
  for i in range ( 0, n // 2 ):
    j = n - i - 1
    t    = a[i]
    a[i] = a[j]
    a[j] = t

  return a

def i4vec_reverse_test ( rng ):

#*****************************************************************************80
#
## i4vec_reverse_test() tests i4vec_reverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  b = 0
  c = 3 * n

  print ( '' )
  print ( 'i4vec_reverse_test():' )
  print ( '  i4vec_reverse() reverses a list of integers.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Original vector:' )

  a = i4vec_reverse ( n, a )

  i4vec_print ( n, a, '  Reversed:' )

  return

def i4vec_sort_bubble_a ( n, a ):

#*****************************************************************************80
#
## i4vec_sort_bubble_a() ascending sorts an I4VEC using bubble sort.
#
#  Discussion:
#
#    Bubble sort is simple to program, but inefficient.  It should not
#    be used for large arrays.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    integer A(N), an unsorted array.
#
#  Output:
#
#    integer A(N), the array has been sorted.
#
  for i in range ( 0, n - 1 ):
    for j in range ( i + 1, n ):
      if ( a[j] < a[i] ):
        t    = a[i]
        a[i] = a[j]
        a[j] = t

  return a

def i4vec_sort_bubble_a_test ( rng ):

#*****************************************************************************80
#
## i4vec_sort_bubble_a_test() tests i4vec_sort_bubble_a().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 20
  b = 0
  c = 3 * n

  print ( '' )
  print ( 'i4vec_sort_bubble_a_test():' )
  print ( '  i4vec_sort_bubble_a() ascending sorts,' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted:' )

  a = i4vec_sort_bubble_a ( n, a )

  i4vec_print ( n, a, '  Ascending sorted:' )

  return

def i4vec_sort_heap_index_a ( n, a ):

#*****************************************************************************80
#
## i4vec_sort_heap_index_a() does an indexed heap ascending sort of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The sorting is not actually carried out.  Rather an index array is
#    created which defines the sorting.  This array may be used to sort
#    or index the array, or to sort or index related arrays keyed on the
#    original array.
#
#    Once the index array is computed, the sorting can be carried out
#    "implicitly:
#
#      a(indx(*))
#
#    or explicitly, by the call
#
#      i4vec_permute ( n, indx, a )
#
#    after which a(*) is sorted.
#
#    Note that the index vector is 0-based.
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
#    int N, the number of entries in the array.
#
#    int A[N], an array to be index-sorted.
#
#  Output:
#
#    int i4vec_sort_heap_index_a[N], contains the sort index.  The
#    I-th element of the sorted array is A(INDX(I)).
#
  import numpy as np

  indx = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    indx[i] = i

  if ( n == 1 ):
    return indx

  l = n // 2 + 1
  ir = n

  while ( True ):
    if ( 1 < l ):
      l = l - 1
      indxt = indx[l-1]
      aval = a[indxt]
    else:
      indxt = indx[ir-1]
      aval = a[indxt]
      indx[ir-1] = indx[0]
      ir = ir - 1

      if ( ir == 1 ):
        indx[0] = indxt
        break

    i = l
    j = l + l

    while ( j <= ir ):
      if ( j < ir ):
        if ( a[indx[j-1]] < a[indx[j]] ):
          j = j + 1

      if ( aval < a[indx[j-1]] ):
        indx[i-1] = indx[j-1]
        i = j
        j = j + j
      else:
        j = ir + 1
    indx[i-1] = indxt

  return indx

def i4vec_sort_heap_index_a_test ( rng ):

#*****************************************************************************80
#
## i4vec_sort_heap_index_a_test() tests i4vec_sort_heap_index_a().
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
#    rng(): the current random number generator.
#
  import numpy as np

  n = 20

  print ( '' )
  print ( 'i4vec_sort_heap_index_a_test():' )
  print ( '  i4vec_sort_heap_index_a() creates an ascending' )
  print ( '  sort index for an I4VEC.' )

  b = 0
  c = 3 * n

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array A:' )

  indx = i4vec_sort_heap_index_a ( n, a )

  i4vec_print ( n, indx, '  Sort vector INDX:' )

  print ( '' )
  print ( '       I   INDX(I)  A(INDX(I))' )
  print ( '' )
  for i in range ( 0, n ):
     print ( '  %8d  %8d  %8d' % ( i, indx[i], a[indx[i]] ) )

  return

def i4vec_sort_heap_index_d ( n, a ):

#*****************************************************************************80
#
## i4vec_sort_heap_index_d() does an indexed heap descending sort of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The sorting is not actually carried out.  Rather an index array is
#    created which defines the sorting.  This array may be used to sort
#    or index the array, or to sort or index related arrays keyed on the
#    original array.
#
#    Once the index array is computed, the sorting can be carried out
#    "implicitly:
#
#      a(indx(*))
#
#    or explicitly, by the call
#
#      i4vec_permute ( n, indx, a )
#
#    after which a(*) is sorted.
#
#    Note that the index vector is 0-based.
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
#  Input:
#
#    int N, the number of entries in the array.
#
#    int A[N], an array to be index-sorted.
#
#  Output:
#
#    int i4vec_sort_heap_index_d[N], contains the sort index.  The
#    I-th element of the sorted array is A(INDX(I)).
#
  import numpy as np

  indx = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    indx[i] = i

  if ( n == 1 ):
    return indx

  l = n // 2 + 1
  ir = n

  while ( True ):

    if ( 1 < l ):
      l = l - 1
      indxt = indx[l-1]
      aval = a[indxt]
    else:
      indxt = indx[ir-1]
      aval = a[indxt]
      indx[ir-1] = indx[0]
      ir = ir - 1

      if ( ir == 1 ):
        indx[0] = indxt
        break

    i = l
    j = l + l

    while ( j <= ir ):

      if ( j < ir ):
        if ( a[indx[j]] < a[indx[j-1]] ):
          j = j + 1

      if ( a[indx[j-1]] < aval ):
        indx[i-1] = indx[j-1]
        i = j
        j = j + j
      else:
        j = ir + 1

    indx[i-1] = indxt

  return indx

def i4vec_sort_heap_index_d_test ( rng ):

#*****************************************************************************80
#
## i4vec_sort_heap_index_d_test() tests i4vec_sort_heap_index_d().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 20

  print ( '' )
  print ( 'i4vec_sort_heap_index_d_test():' )
  print ( '  i4vec_sort_heap_index_d() creates a descending' )
  print ( '  sort index for an I4VEC.' )

  b = 0
  c = 3 * n

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array A:' )

  indx = i4vec_sort_heap_index_d ( n, a )

  i4vec_print ( n, indx, '  Sort vector INDX:' )

  print ( '' )
  print ( '       I   INDX(I)  A(INDX(I))' )
  print ( '' )
  for i in range ( 0, n ):
     print ( '  %8d  %8d  %8d' % ( i, indx[i], a[indx[i]] ) )

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
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  print ( '' )
  i4vec_transpose_print ( n, a, '  My array:  ' )

  return

def index_box2_next_2d ( n1, n2, ic, jc, i, j, more ):

#*****************************************************************************80
#
## index_box2_next_2d() produces index vectors on the surface of a box in 2D.
#
#  Discussion:
#
#    The box is has center at (IC,JC), and has half-widths N1 and N2.
#    The index vectors are exactly those which are between (IC-N1,JC-N1) and
#    (IC+N1,JC+N2) with the property that at least one of I and J
#    is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the half-widths of the box, that is, the
#    maximum distance allowed between (IC,JC) and (I,J).
#
#    integer IC, JC, the central cell of the box.
#
#    integer I, J, the output value of I and J on the previous call.
#    Input values ignored on first call.
#
#    bool MORE, set this to 0 on the first call, and therafter,
#    set it to its output value on the previous call.
#
#  Output:
#
#    integer I, J, the next index set.
#
#    bool MORE, is FALSE (or 0) if there are no more indices
#    to return, and TRUE otherwise.
#
  if ( not more ):
    more = True
    i = ic - n1
    j = jc - n2
    return i, j, more

  if ( i == ic + n1 and j == jc + n2 ):
    more = False
    return i, j, more
#
#  Increment J.
#
  j = j + 1
#
#  Check J.
#
  if ( jc + n2 < j ):
    j = jc - n2
    i = i + 1
  elif ( j < jc + n2 and ( i == ic - n1 or i == ic + n1 ) ):
    pass
  else:
    j = jc + n2

  return i, j, more

def index_box2_next_2d_test ( ):

#*****************************************************************************80
#
## index_box2_next_2d_test() tests index_box2_next_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  ic = 10
  jc = 20
  n1 = 4
  n2 = 3

  print ( '' )
  print ( 'index_box2_next_2d_test():' )
  print ( '  index_box2_next_2d() produces IJ indices that' )
  print ( '  lie on the surface of a box2 in 2D.' )
  print ( '' )
  print ( '  The box has half-widths:' )
  print ( '  %3d  %3d' % ( n1, n2 ) )
  print ( '' )
  print ( '  and has center cell:' )
  print ( '  %3d  %3d' % ( ic, jc ) )
  print ( '' )
  print ( '   #    I   J' )
  print ( '' )

  i = -1
  j = -1
  more = False
  n = 0

  while ( True ):

    i, j, more = index_box2_next_2d ( n1, n2, ic, jc, i, j, more )

    if ( not more ):
      break

    n = n + 1
    print ( '  %3d  %3d  %3d' % ( n, i, j ) )

  return

def index_box2_next_3d ( n1, n2, n3, ic, jc, kc, i, j, k, more ):

#*****************************************************************************80
#
## index_box2_next_3d() produces index vectors on the surface of a box in 3D.
#
#  Discussion:
#
#    The box has a central cell of (IC,JC,KC), with a half widths of
#    (N1,N2,N3).  The index vectors are exactly those between
#    (IC-N1,JC-N2,KC-N3) and (IC+N1,JC+N2,KC+N3) with the property that
#    at least one of I, J, and K is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the "half widths" of the box, that is, the
#    maximum distances from the central cell allowed for I, J and K.
#
#    integer IC, JC, KC, the central cell of the box.
#
#    integer I, J, K.  On input with MORE = TRUE, the previous index set
#    If MORE is FALSE, the input values of I, J and K are not needed.
#
#    bool MORE, is FALSE on an initialization call.  Thereafter,
#    MORE should be TRUE to request the next index set.
#
#  Output:
#
#    integer I, J, K, the next index set.
#
#    bool MORE, is TRUE until there are no more index sets to return.
#
  if ( not more ):
    more = True
    i = ic - n1
    j = jc - n2
    k = kc - n3
    return i, j, k, more

  if ( i == ic + n1 and j == jc + n2 and k == kc + n3 ):
    more = False
    return i, j, k, more
#
#  Increment K.
#
  k = k + 1
#
#  Check K.
#
  if ( kc + n3 < k ):
    k = kc - n3
    j = j + 1
  elif ( k < kc + n3 and \
    ( i == ic - n1 or i == ic + n1 or j == jc - n2 or j == jc + n2 ) ):
    return i, j, k, more
  else:
    k = kc + n3
    return i, j, k, more
#
#  Check J.
#
  if ( jc + n2 < j ):
    j = jc - n2
    i = i + 1
  elif ( j < jc + n2 and \
    ( i == ic - n1 or i == ic + n1 or k == kc - n3 or k == kc + n3 ) ):
    pass
  else:
    j = jc + n2

  return i, j, k, more

def index_box2_next_3d_test ( ):

#*****************************************************************************80
#
## index_box2_next_3d_test() tests index_box2_next_3d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  ic = 10
  jc = 20
  kc = 30
  n1 = 5
  n2 = 3
  n3 = 4

  print ( '' )
  print ( 'index_box2_next_3d_test():' )
  print ( '  index_box2_next_3d() produces IJK indices that' )
  print ( '  lie on the surface of a box.' )
  print ( '' )
  print ( '  The box has half widths:' )
  print ( '  %3d  %3d  %3d' % ( n1, n2, n3 ) )
  print ( '' )
  print ( '  and central cell:' )
  print ( '  %3d  %3d  %3d' % ( ic, jc, kc ) )
  print ( '' )
  print ( '  We will only print a PORTION of the data!' )
  print ( '' )
  print ( '   #    I   J   K' )
  print ( '' )

  i = -1
  j = -1
  k = -1
  more = False

  n = 0

  while ( True ):

    i, j, k, more = index_box2_next_3d ( n1, n2, n3, ic, jc, kc, i, j, k, more )

    if ( not more ):
      break

    n = n + 1
    print ( '  %3d  %3d  %3d  %3d' % ( n, i, j, k ) )

  return

def index_box_next_2d ( n1, n2, i, j, more ):

#*****************************************************************************80
#
## index_box_next_2d() produces index vectors on the surface of a box in 2D.
#
#  Discussion:
#
#    The index vectors are exactly those which are between (1,1) and
#    (N1,N2) with the property that at least one of I and J
#    is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the "dimensions" of the box, that is, the
#    maximum values allowed for I and J.  The minimum values are
#    assumed to be 1.
#
#    integer I, J, the previous index set.  The values of I and J
#    are not needed on the first call, with MORE set to FALSE.
#
#    bool MORE, is FALSE on the first call, and TRUE therafter.
#
#  Output:
#
#    integer I, J, the next index set.
#
#    bool MORE, is TRUE if the routine can be called again
#    for more index sets.
#
  if ( not more ):
    more = True
    i = 1
    j = 1
    return i, j, more

  if ( i == n1 and j == n2 ):
    more = False
    return i, j, more
#
#  Increment J.
#
  j = j + 1
#
#  Check J.
#
  if ( n2 < j ):
    j = 1
    i = i + 1
  elif ( j < n2 and ( i == 1 or i == n1 ) ):
    pass
  else:
    j = n2

  return i, j, more

def index_box_next_2d_test ( ):

#*****************************************************************************80
#
## index_box_next_2d_test() tests index_box_next_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n1 = 5
  n2 = 3

  print ( '' )
  print ( 'index_box_next_2d_test():' )
  print ( '  index_box_next_2d() produces IJ indices that' )
  print ( '  lie on the surface of a box in 2D.' )
  print ( '' )
  print ( '  The box has logical dimensions:' )
  print ( '  %3d by %3d' % ( n1, n2 ) )
  print ( '' )
  print ( '    #    I    J' )
  print ( '' )

  i = 0
  j = 0
  more = False
  n = 0

  while ( True ):

    i, j, more = index_box_next_2d ( n1, n2, i, j, more )

    if ( not more ):
      break

    n = n + 1
    print ( '  %3d  %3d  %3d' % ( n, i, j ) )

  return

def index_box_next_3d ( n1, n2, n3, i, j, k, more ):

#*****************************************************************************80
#
## index_box_next_3d() produces index vectors on the surface of a box in 3D.
#
#  Discussion:
#
#    The index vectors are exactly those which are between (1,1,1) and
#    (N1,N2,N3) with the property that at least one of I, J, and K
#    is an "extreme" value.
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
#    integer N1, N2, N3, the "dimensions" of the box, that is, the
#    maximum values allowed for I, J and K.  The minimum values are
#    assumed to be 1.
#
#    integer I, J, K, the previous index set.  However, on
#    first call, with MORE = FALSE, the input values of I, J and K are not needed.
#
#    bool MORE, is set to FALSE on the first call, and should be
#    TRUE thereafter.
#
#  Output:
#
#    integer I, J, K, the next index set.
#
#    bool MORE, is TRUE if there are more index sets available.
#
  if ( not more ):
    more = True
    i = 1
    j = 1
    k = 1
    return i, j, k, more

  if ( i == n1 and j == n2 and k == n3 ):
    more = False
    return i, j, k, more
#
#  Increment K.
#
  k = k + 1
#
#  Check K.
#
  if ( n3 < k ):
    k = 1
    j = j + 1
  elif ( k < n3 and ( i == 1 or i == n1 or j == 1 or j == n2 ) ):
    return i, j, k, more
  else:
    k = n3
    return i, j, k, more
#
#  Check J.
#
  if ( n2 < j ):
    j = 1
    i = i + 1
  elif ( j < n2 and ( i == 1 or i == n1 or k == 1 or k == n3 ) ):
    return i, j, k, more
  else:
    j = n2
    return i, j, k, more

  return i, j, k, more

def index_box_next_3d_test ( ):

#*****************************************************************************80
#
## index_box_next_3d_test() tests index_box_next_3d().
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
  n1 = 5
  n2 = 3
  n3 = 4
  i = 0
  j = 0
  k = 0
  more = False

  print ( '' )
  print ( 'index_box_next_3d_test():' )
  print ( '  index_box_next_3d() produces IJK indices that' )
  print ( '  lie on the surface of a box.' )
  print ( '' )
  print ( '  The box has logical dimensions:' )
  print ( '  %3d  %3d  %3d' % ( n1, n2, n3 ) )
  print ( '' )
  print ( '   #    I   J   K' )
  print ( '' )

  n = 0

  while ( True ):

    i, j, k, more = index_box_next_3d ( n1, n2, n3, i, j, k, more )

    if ( not more ):
      break

    n = n + 1
    print ( '  %3d  %3d  %3d  %3d' % ( n, i, j, k ) )

  return

def index_next0 ( n, hi, a, more ):

#*****************************************************************************80
#
## index_next0() generates all index vectors within given upper limits.
#
#  Discussion:
#
#    The index vectors are generated in such a way that the reversed
#    sequences are produced in lexicographic order.
#
#  Example:
#
#    N = 3,
#    HI = 3
#
#    1   2   3
#    ---------
#    1   1   1
#    2   1   1
#    3   1   1
#    1   2   1
#    2   2   1
#    3   2   1
#    1   3   1
#    2   3   1
#    3   3   1
#    1   1   2
#    2   1   2
#    3   1   2
#    1   2   2
#    2   2   2
#    3   2   2
#    1   3   2
#    2   3   2
#    3   3   2
#    1   1   3
#    2   1   3
#    3   1   3
#    1   2   3
#    2   2   3
#    3   2   3
#    1   3   3
#    2   3   3
#    3   3   3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer HI, the upper limit for the array indices.
#    The lower limit is implicitly 1 and HI must be at least 1.
#
#    integer A(N), contains the output value of A from
#    the previous call.  On a startup call, with MORE = FALSE,
#    the input value of A doesn't matter.
#
#    bool MORE.  Set this variable FALSE before
#    the first call.  Normally, MORE will be returned TRUE but
#    once all the vectors have been generated, MORE will be
#    reset to FALSE and you should stop calling the program.
#
#  Output:
#
#    integer A(N), the next index set.
#
#    bool MORE, is normally TRUE on but
#    once all the vectors have been generated, MORE will be
#    reset to FALSE and you should stop calling the program.
#
  if ( not more ):

    if ( hi < 1 ):
      print ( '' )
      print ( 'index_next0(): Fatal error!' )
      print ( '  HI is %d' % ( hi ) )
      print ( '  but HI must be at least 1.' )
      raise Exception ( 'index_next0(): Fatal error!' )
 
    for i in range ( 0, n ):
      a[i] = 1

  else:

    inc = 0

    while ( hi <= a[inc] ):
      a[inc] = 1
      inc = inc + 1

    a[inc] = a[inc] + 1
#
#  See if there are more entries to compute.
#
  more = False

  for i in range ( 0, n ):
    if ( a[i] < hi ):
      more = True
      break

  return a, more

def index_next0_test ( ):

#*****************************************************************************80
#
## index_next0_test() tests index_next0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
  hi = 3

  print ( '' )
  print ( 'index_next0_test():' )
  print ( '  index_next0() generates all indices of an' )
  print ( '  array of given shape, with' )
  print ( '  lower limit 1 and given upper limit.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '  Coordinate maximum HI =   %d' % ( hi ) )
 
  print ( '' )
  print ( '  Index arrays:' )
  print ( '' )

  a = np.zeros ( n )
  more = False

  while ( True ):

    a, more = index_next0 ( n, hi, a, more )

    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def index_next1 ( n, hi, a, more ):

#*****************************************************************************80
#
## index_next1() generates all index vectors within given upper limits.
#
#  Discussion:
#
#    The index vectors are generated in such a way that the reversed
#    sequences are produced in lexicographic order.
#
#  Example:
#
#    N = 3,
#    HI(1) = 4, HI(2) = 2, HI(3) = 3
#
#    1   2   3
#    ---------
#    1   1   1
#    2   1   1
#    3   1   1
#    4   1   1
#    1   2   1
#    2   2   1
#    3   2   1
#    4   2   1
#    1   1   2
#    2   1   2
#    3   1   2
#    4   1   2
#    1   2   2
#    2   2   2
#    3   2   2
#    4   2   2
#    1   1   3
#    2   1   3
#    3   1   3
#    4   1   3
#    1   2   3
#    2   2   3
#    3   2   3
#    4   2   3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer HI(N), the upper limits for the array indices.
#    The lower limit is implicitly 1, and each HI(I) should be at least 1.
#
#    integer A(N), the output value of A on the previous call.
#    On startup calls with MORE = FALSE, the input value of A doesn't matter.
#
#    bool MORE, is set to the output value of MORE on the
#    previous call, or to FALSE on a startup call.
#
#  Output:
#
#    integer A(N), the next index vector.
#
#    bool MORE, is normally TRUE, but will be FALSE once there
#    are no more index vectors to generate.
#
  if ( not more ):

    for i in range ( 0, n ):
      a[i] = 1

    for i in range ( 0, n ):
      if ( hi[i] < 1 ):
        print ( '' )
        print ( 'index_next1(): Fatal error!' )
        print ( '  Entry %d of HI is %d' % ( i, hi[i] ) )
        raise Exception ( '  but all entries must be at least 1.' )

  else:

    inc = 0

    while ( hi[inc] <= a[inc] ):
      a[inc] = 1
      inc = inc + 1

    a[inc] = a[inc] + 1
#
#  See if there are more entries to compute.
#
  more = False

  for i in range ( 0, n ):
    if ( a[i] < hi[i] ):
      more = True

  return a, more

def index_next1_test ( ):

#*****************************************************************************80
#
## index_next1_test() tests index_next1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
  hi = np.array ( [ 4, 2, 3 ] )

  print ( '' )
  print ( 'index_next1_test():' )
  print ( '  index_next1() generates all indices of an' )
  print ( '  array of given shape, with' )
  print ( '  lower limit 1 and given upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d\n' % ( n ) )

  i4vec_print ( n, hi, '  Coordinate maximum indices:' )
 
  print ( '' )
  print ( '  Index arrays:' )
  print ( '' )

  a = np.zeros ( n )
  more = False

  while ( True ):

    a, more = index_next1 ( n, hi, a, more )

    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def index_next2 ( n, lo, hi, a, more ):

#*****************************************************************************80
#
## index_next2() generates all index vectors within given lower and upper limits.
#
#  Example:
#
#    N = 3,
#    LO(1) = 1, LO(2) = 10, LO(3) = 4
#    HI(1) = 2, HI(2) = 11, HI(3) = 6
#
#    1   2   3
#    ---------
#    1  10   4
#    2  10   4
#    1  11   4
#    2  11   4
#    1  10   5
#    2  10   5
#    1  11   5
#    2  11   5
#    1  10   6
#    2  10   6
#    1  11   6
#    2  11   6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.  The rank of
#    the object being indexed.
#
#    integer LO(N), HI(N), the lower and upper limits for the array
#    indices.  LO(I) should be less than or equal to HI(I), for each I.
#
#    integer A(N), the output value of A from the previous call.
#    This value is not needed on startup calls with MORE = FALSE.
#
#    bool MORE, the output value of MORE from the previous call,
#    or set to FALSE if this is a startup call.
#
#  Output:
#
#    integer A(N), the successor set of indices to the input
#    value.
#
#    bool MORE, will normally be returned TRUE but
#    once all the vectors have been generated, it will be
#    reset FALSE and you should stop calling the program.
#
  if ( not more ):

    for i in range ( 0, n ):
      a[i] = lo[i]

    for i in range ( 0, n ):
      if ( hi[i] < lo[i] ):
        print ( '' )
        print ( 'index_next2(): Fatal error!' )
        print ( '  Entry %d of HI is %d' % ( i, hi[i] ) )
        print ( '  Entry %d of LO is %d' % ( i, lo[i] ) )
        print ( '  but LO(I) <= HI(I) is required.' )
        raise Exception ( 'index_next2(): Fatal error!' )

  else:

    inc = 0

    while ( hi[inc] <= a[inc] ):
      a[inc] = lo[inc]
      inc = inc + 1

    a[inc] = a[inc] + 1
#
#  See if there are more entries to compute.
#
  more = False

  for i in range ( 0, n ):
    if ( a[i] < hi[i] ):
      more = True
      break

  return a, more

def index_next2_test ( ):

#*****************************************************************************80
#
## index_next2_test() tests index_next2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
  lo = np.array ( [ 10, -5, 0 ] )
  hi = np.array ( [ 11, -3, 1 ] )

  print ( '' )
  print ( 'index_next2_test():' )
  print ( '  index_next2 generates all indices of an' )
  print ( '  array of given shape with given' )
  print ( '  lower and upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '' )
  print ( '  Coordinate, Maximum Index' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %8d  %8d' % ( i, lo[i], hi[i] ) )
 
  print ( '' )
  print ( '  Index arrays:' )
  print ( '' )

  a = np.zeros ( n )
  more = False

  while ( True ):

    a, more = index_next2 ( n, lo, hi, a, more )

    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def index_rank0 ( n, hi, a ):

#*****************************************************************************80
#
## index_rank0() ranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI = 3
#    A = ( 3, 1, 2 )
#
#    RANK = 12
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer HI, the upper limit for the array indices.
#    The lower limit is implicitly 1, and HI should be at least 1.
#
#    integer A(N), the index vector to be ranked.
#
#  Output:
#
#    integer RANK, the rank of the index vector, or -1 if A
#    is not a legal index.
#
  rank = -1

  for i in range ( 0, n ):
    if ( a[i] < 1 or hi < a[i] ):
      return rank

  rank = 0
  for i in range ( n - 1, -1, -1 ):
    rank = hi * rank + a[i]

  rank = 1
  rang = 1
  for i in range ( 0, n ):
    rank = rank + ( a[i] - 1 ) * rang
    rang = rang * hi

  return rank

def index_rank0_test ( ):

#*****************************************************************************80
#
## index_rank0_test() tests index_rank0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
  a = np.array ( [ 3, 1, 2 ] )
  hi = 3

  print ( '' )
  print ( 'index_rank0_test():' )
  print ( '  index_rank0() ranks an index with' )
  print ( '  lower limit 1 and given upper limit.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '  Coordinate maximum index = %d' % ( hi ) )

  i4vec_print ( n, a, '  The index array:' )

  rank = index_rank0 ( n, hi, a )

  print ( '' )
  print ( '  The rank of this object is %d' % ( rank ) )

  return

def index_rank1 ( n, hi, a ):

#*****************************************************************************80
#
## index_rank1() ranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI(1) = 4, HI(2) = 2, HI(3) = 3
#    A = ( 4, 1, 2 )
#
#    RANK = 12
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
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer HI(N), the upper limits for the array indices.
#    The lower limit is implicitly 1, and each HI(I) should be at least 1.
#
#    integer A(N), the index to be ranked.
#
#  Output:
#
#    integer RANK, the rank of the index vector, or -1 if A
#    is not a legal index.
#
  rank = -1
  for i in range ( 0, n ):
    if ( a[i] < 1 or hi[i] < a[i] ):
      return rank

  rank = 0
  for i in range ( n - 1, -1, -1 ):
    rank = hi[i] * rank + a[i]

  rank = 1
  rang = 1
  for i in range ( 0, n ):
    rank = rank + ( a[i] - 1 ) * rang
    rang = rang * hi[i]

  return rank

def index_rank1_test ( ):

#*****************************************************************************80
#
## index_rank1_test() tests index_rank1().
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
 
  n = 3
  a = np.array ( [ 4, 1, 2 ] )
  hi = np.array ( [ 4, 2, 3 ] )

  print ( '' )
  print ( 'index_rank1_test():' )
  print ( '  index_rank1() ranks an index with' )
  print ( '  lower limit 1 and given upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '' )
  print ( '  Coordinate, Maximum Index' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %8d' % ( i, hi[i] ) )
 
  i4vec_print ( n, a, '  The index array:' )

  rank = index_rank1 ( n, hi, a )

  print ( '' )
  print ( '  The rank of this object is %d' % ( rank ) )

  return

def index_rank2 ( n, lo, hi, a ):

#*****************************************************************************80
#
## index_rank2() ranks an index vector within given lower and upper limits.
#
#  Example:
#
#    N = 3,
#    LO(1) = 1, LO(2) = 10, LO(3) = 4
#    HI(1) = 2, HI(2) = 11, HI(3) = 6
#    A = ( 1, 11, 5 )
#
#    RANK = 7
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
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer LO(N), HI(N), the lower and upper limits for the array
#    indices.  LO(I) should be less than or equal to HI(I), for each I.
#
#    integer A(N), the index vector to be ranked.
#
#  Output:
#
#    integer RANK, the rank of the index vector, or -1 if A
#    is not a legal index vector.
#
  for i in range ( 0, n ):
    if ( a[i] < lo[i] or hi[i] < a[i] ):
      rank = -1
      return rank

  rank = 1
  rang = 1
  for i in range ( 0, n ):
    rank = rank + ( a[i] - lo[i] ) * rang
    rang = rang * ( hi[i] + 1 - lo[i] )

  return rank

def index_rank2_test ( ):

#*****************************************************************************80
#
## index_rank2_test() tests index_rank2().
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

  n = 3

  a = np.array ( [ 1, 11, 5 ] )
  hi = np.array ( [ 2, 11, 6 ] )
  lo = np.array ( [ 1, 10, 4 ] )

  print ( '' )
  print ( 'index_rank2_test():' )
  print ( '  index_rank2() ranks an index with given' )
  print ( '  lower and upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '' )
  print ( '  Coordinate, Minimum index, Maximum Index' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %8d  %8d' % ( i, lo[i], hi[i] ) )
 
  i4vec_print ( n, a, '  The index array:' )

  rank = index_rank2 ( n, lo, hi, a )

  print ( '' )
  print ( '  The rank of this object is %d' % ( rank ) )

  return

def index_unrank0 ( n, hi, rank ):

#*****************************************************************************80
#
## index_unrank0() unranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI = 3
#    RANK = 12
#
#    A = ( 3, 1, 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer HI, the upper limit for the array indices.
#    The lower limit is implicitly 1, and HI should be at least 1.
#
#    integer RANK, the rank of the desired index vector.
#
#  Output:
#
#    integer A(N), the index vector of the given rank.
#
  import numpy as np

  a = np.zeros ( n )
#
#  The rank might be too small.
#
  if ( rank < 1 ):
    return a

  rang = hi ** n
#
#  The rank might be too large.
#
  if ( rang < rank ):
    return a

  k = rank - 1
  for i in range ( n - 1, -1, -1 ):
    rang = ( rang // hi )
    j = ( k // rang )
    a[i] = j + 1
    k = k - j * rang

  return a

def index_unrank0_test ( ):

#*****************************************************************************80
#
## index_unrank0_test() tests index_unrank0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  n = 3
  hi = 3

  print ( '' )
  print ( 'index_unrank0_test():' )
  print ( '  index_unrank0() unranks a multi-index.' )
  print ( '' )
  print ( '  The multi-index has dimension %d' % ( n ) )
  print ( '' )
  print ( '  The upper limit is HI = %d' % ( hi ) )
  print ( '' )
  print ( '  Rank, Multi-Index:' )
  print ( '' )
 
  maxrank = hi ** n

  for rank in range ( 1, maxrank + 1 ):
    a = index_unrank0 ( n, hi, rank )
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

  return

def index_unrank1 ( n, hi, rank ):

#*****************************************************************************80
#
## index_unrank1() unranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI(1) = 4, HI(2) = 2, HI(3) = 3
#    RANK = 11
#
#    A = ( 3, 1, 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer HI(N), the upper limits for the array indices.
#    The lower limit is implicitly 1, and each HI(I) should be at least 1.
#
#    integer RANK, the rank of the desired index vector.
#
#  Output:
#
#    integer A(N), the index vector of the given rank.
#
  import numpy as np

  a = np.zeros ( n )
#
#  The rank might be too small.
#
  if ( rank < 1 ):
    return a

  rang = i4vec_product ( n, hi )
#
#  The rank might be too large.
#
  if ( rang < rank ):
    return a

  k = rank - 1

  for i in range ( n - 1, -1, -1 ):
    rang = ( rang // hi[i] )
    j = ( k // rang )
    a[i] = j + 1
    k = k - j * rang

  return a

def index_unrank1_test ( ):

#*****************************************************************************80
#
## index_unrank1_test() tests index_unrank1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
  hi = np.array ( [ 4, 2, 3 ] )

  print ( '' )
  print ( 'index_unrank1_test():' )
  print ( '  index_unrank1() unranks a multi-index.' )
  print ( '' )
  print ( '  The multi-index has dimension %d' % ( n ) )

  i4vec_print ( n, hi, '  The upper limits:' )

  print ( '' )
  print ( '  Rank, Multi-Index:' )
  print ( '' )
 
  maxrank = i4vec_product ( n, hi )

  for rank in range ( 1, maxrank + 1 ): 
    a = index_unrank1 ( n, hi, rank )
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

  return

def index_unrank2 ( n, lo, hi, rank ):

#*****************************************************************************80
#
## index_unrank2() unranks an index vector within given lower and upper limits.
#
#  Example:
#
#    N = 3,
#    LO(1) = 1, LO(2) = 10, LO(3) = 4
#    HI(1) = 2, HI(2) = 11, HI(3) = 6
#    RANK = 7
#
#    A = ( 1, 11, 5 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    integer LO(N), HI(N), the lower and upper limits for the array
#    indices.  It should be the case that LO(I) <= HI(I) for each I.
#
#    integer RANK, the rank of the desired index.
#
#  Output:
#
#    integer A(N), the index vector of the given rank.
#
  import numpy as np

  a = np.zeros ( n )
#
#  The rank might be too small.
#
  if ( rank < 1 ):
    return a

  rang = 1
  for i in range ( 0, n ):
    rang = rang * ( hi[i] + 1 - lo[i] )
#
#  The rank might be too large.
#
  if ( rang < rank ):
    return a

  k = rank - 1

  for i in range ( n - 1, -1, -1 ):
    rang = ( rang // ( hi[i] + 1 - lo[i] ) )
    j = ( k // rang )
    a[i] = j + lo[i]
    k = k - j * rang

  return a

def index_unrank2_test ( ):

#*****************************************************************************80
#
## index_unrank2_test() tests index_unrank2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
  hi = np.array ( [ 2, 11, 6 ] )
  lo = np.array ( [ 1, 10, 4 ] )

  print ( '' )
  print ( 'index_unrank2_test():' )
  print ( '  index_unrank2() unranks a multi-index.' )
  print ( '' )
  print ( '  The multi-index has dimension %d' % ( n ) )
  print ( '' )
  print ( '  The lower and upper limits are:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %8d  %8d  %8d' % ( i, lo[i], hi[i] ) )
  print ( '' )
  print ( '  Rank, Multi-Index:' )
  print ( '' )
 
  rank = 7

  a = index_unrank2 ( n, lo, hi, rank )
  print ( '  %2d' % ( rank ), end = '' )
  for i in range ( 0, n ):
    print ( '  %2d' % ( a[i] ), end = '' )
  print ( '' )

  return

def inverse_mod_n ( b, n ):

#*****************************************************************************80
#
## inverse_mod_n() computes the inverse of B mod N.
#
#  Discussion:
#
#    If
#
#      Y = inverse_mod_n ( B, N )
#
#    then
#
#      mod ( B * Y, N ) = 1
#
#    The value Y will exist if and only if B and N are relatively prime.
#
#  Examples:
#
#    B  N  Y
#
#    1  2  1
#
#    1  3  1
#    2  3  2
#
#    1  4  1
#    2  4  0
#    3  4  3
#
#    1  5  1
#    2  5  3
#    3  5  2
#    4  5  4
#
#    1  6  1
#    2  6  0
#    3  6  0
#    4  6  0
#    5  6  5
#
#    1  7  1
#    2  7  4
#    3  7  5
#    4  7  2
#    5  7  3
#    6  7  6
#
#    1  8  1
#    2  8  0
#    3  8  3
#    4  8  0
#    5  8  5
#    6  8  0
#    7  8  7
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
#    integer B, the number whose inverse mod N is desired.
#    B should be positive.  Normally, B < N, but this is not required.
#
#    integer N, the number with respect to which the
#    modulus is computed.  N should be positive.
#
#  Output:
#
#    integer Y, the inverse of B mod N, or 0 if there
#    is not inverse for B mode N.  1 <= Y < N if the inverse exists.
#
  n0 = n
  b0 = b
  t0 = 0
  t = 1

  q = ( n // b )
  r = n - q * b

  while ( 0 < r ):

    temp = t0 - q * t

    if ( 0 <= temp ):
      temp = ( temp % n )

    if ( temp < 0 ):
      temp = n - ( ( - temp ) % n )

    t0 = t
    t = temp
    n0 = b0
    b0 = r
    q = ( n0 // b0 )
    r = n0 - q * b0

  if ( b0 != 1 ):
    y = 0
  else:
    y = ( t % n )

  return y

def inverse_mod_n_test ( ):

#*****************************************************************************80
#
## inverse_mod_n_test() tests inverse_mod_n().
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
  print ( '' )
  print ( 'inverse_mod_n_test():' )
  print ( '  inverse_mod_n() seeks Y, the inverse of B mod N,' )
  print ( '  so that mod ( B * Y, N ) = 1, but returns 0' )
  print ( '  if the inverse does not exist.' )

  print ( '' )
  print ( '     B     N     Y     Z = mod ( B * Y, N )' )

  for n in range ( 1, 11 ):
    print ( '' )
    for b in range ( 1, n ):
      y = inverse_mod_n ( b, n )
      z = ( ( b * y ) % n )
      print ( '  %4d  %4d  %4d  %4d' % ( b, n, y, z ) )

  return

def inversion_to_perm0 ( n, ins ):

#*****************************************************************************80
#
## inversion_to_perm0(): inversion sequence to permutation of (0,...,N-1).
#
#  Discussion:
#
#    For a given permutation P acting on objects 0 through N-1, the
#    inversion sequence INS is defined as:
#
#      INS(1) = 0
#      INS(I) = number of values J < I for which P(I) < P(J).
#
#  Example:
#
#    Input:
#
#      ( 0, 0, 2, 1, 3 )
#
#    Output:
#
#      ( 2, 4, 0, 3, 1 )
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
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer INS(N), the inversion sequence of a permutation.
#    It must be the case that 0 <= INS(I) < I for I = 1 to N.
#
#  Output:
#
#    integer P(N), the permutation.
#
  p = i4vec_indicator0 ( n )

  for i in range ( n, 1, -1 ):

    itemp = p[i-1-ins[i-1]]

    for j in range ( i - ins[i-1], i ):
      p[j-1] = p[j]

    p[i-1] = itemp

  return p

def inversion_to_perm0_test ( ):

#*****************************************************************************80
#
## inversion_to_perm0_test() tests inversion_to_perm0().
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
  import numpy as np

  n = 5

  print ( '' )
  print ( 'inversion_to_perm0_test():' )
  print ( '  inversion_to_perm0(): inversion => permutation (0,...,N-1).' )

  perm = np.array ( [ 2, 4, 0, 3, 1 ] )
  i4vec_print ( n, perm, '  Permutation:' )

  ins = perm0_to_inversion ( n, perm )
  i4vec_print ( n, ins, '  Inversion:' )

  perm2 = inversion_to_perm0 ( n, ins )
  i4vec_print ( n, perm2, '  Recovered permutation:' )

  return

def involute_enum ( n ):

#*****************************************************************************80
#
## involute_enum() enumerates the involutions of N objects.
#
#  Discussion:
#
#    An involution is a permutation consisting only of fixed points and
#    pairwise transpositions.
#
#    An involution is its own inverse permutation.
#
#  Recursion:
#
#    S(0) = 1
#    S(1) = 1
#    S(N) = S(N-1) + (N-1) * S(N-2)
#
#  First values:
#
#     N         S(N)
#     0           1
#     1           1
#     2           2
#     3           4
#     4          10
#     5          26
#     6          76
#     7         232
#     8         764
#     9        2620
#    10        9496
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects to be permuted.
#
#  Output:
#
#    integer S(0:N), the number of involutions of 0, 1, 2, ... N
#    objects.
#
  import numpy as np

  s = np.zeros ( n + 1 )

  s[0] = 1

  if ( n <= 0 ):
    return s

  s[1] = 1

  for i in range ( 2, n + 1 ):
    s[i] = s[i-1] + ( i - 1 ) * s[i-2]

  return s

def involute_enum_test ( ):

#*****************************************************************************80
#
## involute_enum_test() tests involute_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'involute_enum_test():' )
  print ( '  involute_enum() counts involutions;' )
  print ( '' )
  print ( '  N    # of involutions' )
  print ( '' )

  s = involute_enum ( n )

  for i in range ( 0, n + 1 ):
    print ( '  %8d  %8d' % ( i, s[i] ) )

  return

def jfrac_to_rfrac ( m, r, s ):

#*****************************************************************************80
#
## jfrac_to_rfrac() converts a J-fraction into a rational polynomial fraction.
#
#  Discussion:
#
#    The routine accepts a J-fraction:
#
#        R(1) / ( X + S(1)
#      + R(2) / ( X + S(2)
#      + R(3) / ...
#      + R(M) / ( X + S(M) )... ))
#
#    and returns the equivalent rational polynomial fraction:
#
#      P(1) + P(2) * X + ... + P(M) * X^(M-1)
#      -------------------------------------------------------
#      Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Input:
#
#    integer M, defines the number of P, R, and S
#    coefficients, and is one less than the number of Q
#    coefficients.
#
#    real R(M), S(M), the coefficients defining the J-fraction.
#
#  Output:
#
#    real P(M), Q(M+1), the coefficients defining the rational
#    polynomial fraction.  The algorithm used normalizes the coefficients
#    so that Q(M+1) = 1.0.
#
  import numpy as np

  a = np.zeros ( [ m, m ] )
  b = np.zeros ( [ m, m ] )

  a[0,0] = r[0]
  b[0,0] = s[0]

  if ( 1 < m ):

    for k in range ( 1, m ):
      a[k,k] = r[0]
      b[k,k] = b[k-1,k-1] + s[k]

    a[0,1] = r[0] * s[1]
    b[0,1] = r[1] + s[0] * s[1]

    for k in range ( 2, m ):
      a[0,k] = s[k] * a[0,k-1] + r[k] * a[0,k-2]
      a[k-1,k] = a[k-2,k-1] + s[k] * r[0]
      b[0,k] = s[k] * b[0,k-1] + r[k] * b[0,k-2]
      b[k-1,k] = b[k-2,k-1] + s[k] * b[k-1,k-1] + r[k]

    for k in range ( 3, m ):
      for i in range ( 1, k - 1 ):
        a[i,k] = a[i-1,k-1] + s[k] * a[i,k-1] + r[k] * a[i,k-2]
        b[i,k] = b[i-1,k-1] + s[k] * b[i,k-1] + r[k] * b[i,k-2]

  p = np.zeros ( m )
  for i in range ( 0, m ):
    p[i] = a[i,m-1]

  q = np.zeros ( m + 1 )
  for i in range ( 0, m ):
    q[i] = b[i,m-1]
  q[m] = 1.0

  return p, q

def jfrac_to_rfrac_test ( rng ):

#*****************************************************************************80
#
## jfrac_to_rfrac_test() tests jfrac_to_rfrac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np
#
#  Generate the data, but force Q(M+1) to be 1.  
#  That will make it easier to see that the two operations are inverses
#  of each other.  jfrac_to_rfrac is free to scale its and chooses
#  a scaling in which Q(M+1) is 1.
#
  m = 6
  p = rng.random ( size = m )
  q = rng.random ( size = m + 1 )

  t = q[m]
  for i in range ( 0, m + 1 ):
    q[i] = q[i] / t

  print ( '' )
  print ( 'jfrac_to_rfrac_test():' )
  print ( '  jfrac_to_rfrac() converts a J fraction' )
  print ( '  to a rational polynomial fraction.' )

  r8vec_print ( m, p, '  RFRAC P:' )
  r8vec_print ( m + 1, q, '  RFRAC Q:' )
 
  r, s = rfrac_to_jfrac ( m, p, q )
 
  r8vec_print ( m, r, '  JFRAC R:' )
  r8vec_print ( m, s, '  JFRAC S:' )
 
  p2, q2 = jfrac_to_rfrac ( m, r, s )

  r8vec_print ( m, p2, '  Recovered RFRAC P:' )
  r8vec_print ( m + 1, q2, '  Recovered RFRAC Q:' )

  return

def josephus ( n, m, k ):

#*****************************************************************************80
#
## josephus() returns the position X of the K-th man to be executed.
#
#  Discussion:
#
#    The classic Josephus problem concerns a circle of 41 men.
#    Every third man is killed and removed from the circle.  Counting
#    and executing continues until all are dead.  Where was the last
#    survivor sitting?
#
#    Note that the first person killed was sitting in the third position.
#    Moreover, when we get down to 2 people, and we need to count the
#    "third" one, we just do the obvious thing, which is to keep counting
#    around the circle until our count is completed.
#
#    The process may be regarded as generating a permutation of
#    the integers from 1 to N.  The permutation would be the execution
#    list, that is, the list of the executed men, by position number.
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
#    W W Rouse Ball,
#    Mathematical Recreations and Essays,
#    Macmillan, 1962, pages 32-36.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, pages 158-159.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 3, Sorting and Searching,
#    Addison Wesley, 1968, pages 18-19.
#
#  Input:
#
#    integer N, the number of men.
#    N must be positive.
#
#    integer M, the counting index.
#    M must not be zero.  Ordinarily, M is positive, and no greater than N.
#
#    integer K, the index of the executed man of interest.
#    K must be between 1 and N.
#
#  Output:
#
#    integer X, the position of the K-th man.
#    X will be between 1 and N.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'josephus(): Fatal error!' )
    print ( '  N <= 0.' )
    raise Exception ( 'josephus(): Fatal error!' )

  if ( m == 0 ):
    print ( '' )
    print ( 'josephus(): Fatal error!' )
    print ( '  M = 0.' )
    raise Exception ( 'josephus(): Fatal error!' )

  if ( k <= 0 or n < k ):
    print ( '' )
    print ( 'josephus(): Fatal error!' )
    print ( '  J <= 0 or N < K.' )
    raise Exception ( 'josephus(): Fatal error!' )
#
#  In case M is bigger than N, or negative, get the
#  equivalent positive value between 1 and N.
#  You can skip this operation if 1 <= M <= N.
#
  m2 = i4_modp ( m, n )

  x = k * m2

  while ( n < x ):
    x = ( ( m2 * ( x - n ) - 1 ) // ( m2 - 1 ) )

  return x

def josephus_test ( ):

#*****************************************************************************80
#
## josephus_test() tests josephus().
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
  print ( '' )
  print ( 'josephus_test():' )
  print ( '  josephus() solves Josephus problems.' )
  print ( '' )
  print ( '     N     M     K     X' )
  print ( '' )

  m = 3
  n = 41
  k = 41
  x = josephus ( n, m, k )
  print ( '  %4d  %4d  %4d  %4d' % ( n, m, k, x ) )

  m = -38
  n = 41
  k = 41
  x = josephus ( n, m, k )

  print ( '  %4d  %4d  %4d  %4d' % ( n, m, k, x ) )

  m = 3
  n = 41
  k = 40
  x = josephus ( n, m, k )

  print ( '  %4d  %4d  %4d  %4d' % ( n, m, k, x ) )

  m = 2
  n = 64
  k = 64
  x = josephus ( n, m, k )

  print ( '  %4d  %4d  %4d  %4d' % ( n, m, k, x ) )

  m = 2
  n = 1000
  k = 1000
  x = josephus ( n, m, k )

  print ( '  %4d  %4d  %4d  %4d' % ( n, m, k, x ) )

  return

def ksub_next2 ( n, k, a ):

#*****************************************************************************80
#
## ksub_next2() generates the subsets of size K from a set of size N, one at a time.
#
#  Discussion:
#
#    This routine uses the revolving door method.  It has no "memory".
#    As far as this routine is concerned, the subsets of size K are
#    arranged in a ring that "wraps around".  There is no last subset,
#    and so the routine can be started anywhere, and called indefinitely.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
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
#    integer N, the size of the set from which subsets are drawn.
#    N must be positive.
#
#    integer K, the size of the desired subset.  K must be
#    between 0 and N.
#
#    integer A(K), a subset of size K.  A must contain K unique 
#    numbers, in order, between 1 and N.  
#
#  Output:
#
#    integer A(K), the "next" subset of size K.  
#
#    integer INN, the element of the output subset which
#    was not in the input set.  Each new subset differs from the
#    last one by adding one element and deleting another.
#
#    integer OUT, the element of the input subset which
#    is not in the output subset.
#  
  if ( n <= 0 ):
    print ( '' )
    print ( 'ksub_next2(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  but 0 < N is required!' )
    raise Exception ( 'ksub_next2(): Fatal error!' )

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_next2(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    raise Exception ( 'ksub_next2(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_next2(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    raise Exception ( 'ksub_next2(): Fatal error!' )

  j = 0

  while ( True ):

    if ( 0 < j or ( k % 2 ) == 0 ):

      j = j + 1

      if ( k < j ):
        a[k-1] = k
        inn = k
        out = n
        return a, inn, out

      if ( a[j-1] != j ):

        out = a[j-1]
        inn = out - 1
        a[j-1] = inn

        if ( j != 1 ):
          inn = j - 1
          a[j-2] = inn

        return a, inn, out

    j = j + 1
    m = n

    if ( j < k ):
      m = a[j] - 1

    if ( m != a[j-1] ):
      break

  inn = a[j-1] + 1
  a[j-1] = inn
  out = inn - 1

  if ( j != 1 ):
    a[j-2] = out
    out = j - 1

  return a, inn, out

def ksub_next2_test ( ):

#*****************************************************************************80
#
## ksub_next2_test() tests ksub_next2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_next2_test():' )
  print ( '  ksub_next2() generates the next K subset of an' )
  print ( '  N set by the revolving door method.' )
  print ( '' )
  print ( 'Rank         Subset      Add  Remove' )
  print ( '          -----------' )
  print ( '' )
#
#  ksub_next2 doesn't have a good way of stopping.  
#  We will save the starting subset, and stop when the
#  new subset is the same as the starting one.
#
  inn = 0
  out = 0
  rank = 0
 
  a = i4vec_indicator1 ( k )
 
  while ( True ):
 
    rank = rank + 1
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '    %2d' % ( inn ), end = '' )
    print ( '  %2d' % ( out ) )
 
    a, inn, out = ksub_next2 ( n, k, a )
 
    more = False

    for i in range ( 0, k ):
      if ( a[i] != i + 1 ):
        more = True
        break

    if ( not more ):
      break

  return

def ksub_next3 ( n, k, a, more ):

#*****************************************************************************80
#
## ksub_next3() generates the subsets of size K from a set of size N, one at a time.
#
#  Discussion:
#
#    The routine uses the revolving door method.
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
#    integer N, the size of the set from which subsets are drawn.
#    N must be positive.
#
#    integer K, the size of the desired subsets.  K must be
#    between 0 and N.
#
#    integer A(K).  A(I) is the I-th element of the
#    output subset.  The elements of A are sorted.
#
#    bool MORE.  On first call, set MORE = FALSE
#    to signal the beginning.  MORE will be set to TRUE, and on
#    each call, the routine will return another K-subset.
#    Finally, when the last subset has been returned,
#    MORE will be set FALSE and you may stop calling.
#
#  Output:
#
#    integer A(K).  A(I) is the I-th element of the
#    output subset.  The elements of A are sorted.
#
#    bool MORE.  On first call, set MORE = FALSE
#    to signal the beginning.  MORE will be set to TRUE, and on
#    each call, the routine will return another K-subset.
#    Finally, when the last subset has been returned,
#    MORE will be set FALSE and you may stop calling.
#
#    integer INN, the element of the output subset which
#    was not in the input set.  Each new subset differs from the
#    last one by adding one element and deleting another.  IN is not
#    defined the first time that the routine returns, and is
#    set to -1.
#
#    integer IOUT, the element of the input subset which is
#    not in the output subset.  IOUT is not defined the first time
#    the routine returns, and is set to -1.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'ksub_next3(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  but 0 < N is required!' )
    raise Exception ( 'ksub_next3(): Fatal error!' )

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_next3(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    raise Exception ( 'ksub_next3(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_next3(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    raise Exception ( 'ksub_next3(): Fatal error!' )

  if ( not more ):
    inn = -1
    iout = -1
    a = i4vec_indicator1 ( k )
    more = ( k != n )
    return a, more, inn, iout

  j = 0

  while ( True ):

    if ( 0 < j or ( k % 2 ) == 0 ):

      j = j + 1

      if ( a[j-1] != j ):

        iout = a[j-1]
        inn = iout - 1
        a[j-1] = inn

        if ( j != 1 ):
          inn = j - 1
          a[j-2] = inn

        if ( k != 1 ):
          more = ( a[k-2] == k - 1 )

        more = ( not more ) or ( a[k-1] != n )

        return a, more, inn, iout

    j = j + 1
    m = n

    if ( j < k ):
      m = a[j] - 1

    if ( m != a[j-1] ):
      break

  inn = a[j-1] + 1
  a[j-1] = inn
  iout = inn - 1

  if ( j != 1 ):
    a[j-2] = iout
    iout = j - 1

  if ( k != 1 ):
    more = ( a[k-2] == k - 1 )

  more = ( ( not more ) or ( a[k-1] != n ) )

  return a, more, inn, iout

def ksub_next3_test ( ):

#*****************************************************************************80
#
## ksub_next3_test() tests ksub_next3().
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
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_next3_test():' )
  print ( '  ksub_next3() generates all K subsets of an N set' )
  print ( '  using the revolving door method.' )
  print ( '' )
  print ( 'Rank    Subset  Added Removed' )
  print ( '' )

  rank = 0
  a = np.zeros ( k )
  more = False
 
  while ( True ):

    a, more, inn, out = ksub_next3 ( n, k, a, more)

    rank = rank + 1
    print ( '  %2d' % ( rank ), end = '' )
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '     %2d  %2d' % ( inn, out ) )

    if ( not more ):
      break

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
#    logical DONE, is TRUE if the routine is returning the
#    next K subset, and FALSE if there are no more subsets to return.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_next4(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    raise Exception ( 'ksub_next4(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_next4(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    raise Exception ( 'ksub_next4(): Fatal error!' )
#
#  First call:
#
  if ( done ):

    a = np.zeros ( n, dtype = np.int32 )

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
  import platform

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

def ksub_next ( n, k, a, more, m, m2 ):

#*****************************************************************************80
#
## ksub_next() generates the subsets of size K from a set of size N, one at a time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
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
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, the desired size of the subsets.  K must
#    be between 0 and N.
#
#    integer A(K).  A(I) is the I-th element of the
#    subset.  Thus A(I) will be an integer between 1 and N.
#    Note that the routine will return the values in A
#    in sorted order: 1 <= A(1) < A(2) < ... < A(K) <= N
#
#    bool MORE.  Set MORE = FALSE before first call
#    for a new sequence of subsets.  It then is set and remains
#    TRUE as long as the subset computed on this call is not the
#    final one.  When the final subset is computed, MORE is set to
#    FALSE as a signal that the computation is done.
#
#    integer M, M2, two variables used by this
#    procedure for bookkeeping.  The user must declare these variables,
#    and the output values from one call must be used as the input values
#    on the next.  The user should not change these values.
#
#  Output:
#
#    integer A(K).  A(I) is the I-th element of the
#    subset.  Thus A(I) will be an integer between 1 and N.
#    Note that the routine will return the values in A
#    in sorted order: 1 <= A(1) < A(2) < ... < A(K) <= N
#
#    bool MORE.  Set MORE = FALSE before first call
#    for a new sequence of subsets.  It then is set and remains
#    TRUE as long as the subset computed on this call is not the
#    final one.  When the final subset is computed, MORE is set to
#    FALSE as a signal that the computation is done.
#
#    integer M, M2, bookkeeping variables.
#
  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_next(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    raise Exception ( 'ksub_next(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_next(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    raise Exception ( 'ksub_next(): Fatal error!' )

  if ( not more ):
    m2 = 0
    m = k
  else:
    if ( m2 < n - m ):
      m = 0
    m = m + 1
    m2 = a[k-m]

  for j in range ( 1, m + 1 ):
    a[k+j-m-1] = m2 + j

  more = ( a[0] != ( n - k + 1 ) )

  return a, more, m, m2

def ksub_next_test ( ):

#*****************************************************************************80
#
## ksub_next_test() tests ksub_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ksub_next_test():' )
  print ( '  ksub_next() generates all K subsets of an N set' )
  print ( '  in lexicographic order.' )
  print ( '' )

  rank = 0

  n = 5
  k = 3
  a = np.zeros ( k )
  more = False
  m = 0
  m2 = 0
 
  while ( True ):

    a, more, m, m2 = ksub_next ( n, k, a, more, m, m2 )

    rank = rank + 1
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def ksub_random2 ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random2() selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This algorithm is designated Algorithm RKS2 in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
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
#    A Bebbington,
#    A simple method of drawing a sample without replacement,
#    Journal of Applied Statistics,
#    Volume 24, 1975, page 136.
#
#  Input:
#
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K).  A(I) is the I-th element of the
#    output set.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_random2(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    raise Exception ( 'ksub_random2(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_random2(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    raise Exception ( 'ksub_random2(): Fatal error!' )

  a = np.zeros ( k, dtype = np.int32 )

  if ( k == 0 ):
    return a

  need = k
  have = 0

  available = n
  candidate = 0

  while ( True ):

    candidate = candidate + 1

    r = rng.random ( )

    if ( available * r <= need ):

      need = need - 1;
      a[have] = candidate
      have = have + 1

      if ( need <= 0 ):
        break

    available = available - 1

  return a

def ksub_random2_test ( rng ):

#*****************************************************************************80
#
## ksub_random2_test() tests ksub_random2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_random2_test():' )
  print ( '  ksub_random2() generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  for i in range ( 0, 10 ):

    a = ksub_random2 ( n, k, rng )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ), end = '' )
    print ( '' )

  return

def ksub_random3 ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random3() selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This routine uses Floyd's algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(N).  I is an element of the subset
#    if A(I) = 1, and I is not an element if A(I)=0.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_random3(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    raise Exception ( 'ksub_random3(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_random3(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    raise Exception ( 'ksub_random3(): Fatal error!' )

  a = np.zeros ( n )

  for i in range ( n - k, n ):

    j = rng.integers ( 0, i, endpoint = True )

    if ( a[j] == 0 ):
      a[j] = 1
    else:
      a[i] = 1

  return a

def ksub_random3_test ( rng ):

#*****************************************************************************80
#
## ksub_random3_test() tests ksub_random3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#

  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_random3_test():' )
  print ( '  ksub_random3() generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  for i in range ( 0, 10 ):

    a = ksub_random3 ( n, k, rng )

    for j in range ( 0, n ):
      print ( '  %3d' % ( a[j] ), end = '' )
    print ( '' )

  return

def ksub_random4 ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random4() selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This routine is somewhat impractical for the given problem, but
#    it is included for comparison, because it is an interesting
#    approach that is superior for certain applications.
#
#    The approach is mainly interesting because it is "incremental";
#    it proceeds by considering every element of the set, and does not
#    need to know how many elements there are.
#
#    This makes this approach ideal for certain cases, such as the
#    need to pick 5 lines at random from a text file of unknown length,
#    or to choose 6 people who call a certain telephone number on a
#    given day.  Using this technique, it is possible to make the
#    selection so that, whenever the input stops, a valid uniformly
#    random subset has been chosen.
#
#    Obviously, if the number of items is known in advance, and
#    it is easy to extract K items directly, there is no need for
#    this approach, and it is less efficient since, among other costs,
#    it has to generate a random number for each item, and make an
#    acceptance/rejection test.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Tom Christiansen and Nathan Torkington,
#    "8.6: Picking a Random Line from a File",
#    Perl Cookbook, pages 284-285,
#    O'Reilly, 1999.
#
#  Input:
#
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K), contains the indices of the selected items.
#
  import numpy as np

  a = np.zeros ( k )

  next = 0
#
#  Here, we use a DO WHILE to suggest that the algorithm
#  proceeds to the next item, without knowing how many items
#  there are in total.
#
#  Note that this is really the only place where N occurs,
#  so other termination criteria could be used, and we really
#  don't need to know the value of N!
#
  while ( next < n ):

    if ( next < k ):

      i = next
      a[i] = next

    else:

      r = rng.random ( )

      if ( r * ( next + 1 ) <= k ):
        i4_lo = 0
        i4_hi = k - 1
        i = rng.integers ( i4_lo, i4_hi, endpoint = True )
#
#  If we slide the current items down, and insert at the end, we preserve order.
#
        for j in range ( i, k ):
          a[j-1] = a[j]
        a[k-1] = next

#       a[i] = next

    next = next + 1

  return a

def ksub_random4_test ( rng ):

#*****************************************************************************80
#
## ksub_random4_test() tests ksub_random4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import platform

  k = 3
  n = 100

  print ( '' )
  print ( 'ksub_random4_test():' )
  print ( '  ksub_random4() generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  for i in range ( 0, 10 ):

    a = ksub_random4 ( n, k, rng )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ), end = '' )
    print ( '' )

  return

def ksub_random5 ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random5() selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    Consider the set A(1:N) = 1, 2, 3, ... N.
#    Choose a random index I1 between 1 and N, and swap items A(1) and A(I1).
#    Choose a random index I2 between 2 and N, and swap items A(2) and A(I2).
#    repeat K times.
#    A(1:K) is your random K-subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the set from which subsets
#    are drawn.
#
#    integer K, number of elements in desired subsets.
#    1 <= K <= N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K), the indices of the randomly
#    chosen elements.
#
  import numpy as np
#
#  Let B index the set.
#
  b = np.zeros ( n )
  for i in range ( 0, n ):
    b[i] = i
#
#  Choose item 1 from N things,
#  choose item 2 from N-1 things,
#  choose item K from N-K+1 things.
#
  for i in range ( 0, k ): 

    j = rng.integers ( i, n - 1, endpoint = True )

    t    = b[i]
    b[i] = b[j]
    b[j] = t
#
#  Copy the first K elements.
#
  a = np.zeros ( k )
  for i in range ( 0, k ):
    a[i] = b[i]
#
#  Put the elements in ascending order.
#
  a = np.sort ( a )

  return a

def ksub_random5_test ( rng ):

#*****************************************************************************80
#
## ksub_random5_test() tests ksub_random5().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import platform

  k = 3
  n = 100

  print ( '' )
  print ( 'ksub_random5_test():' )
  print ( '  ksub_random5() generates a random K subset of an N set.' )
  print ( '  Set size is N =    ', n )
  print ( '  Subset size is K = ', k )
  print ( '' )

  for i in range ( 0, 10 ):

    a = ksub_random5 ( n, k, rng )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ), end = '' )
    print ( '' )

  return

def ksub_random ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random() selects a random subset of size K from a set of size N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2014
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
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K).  A(I) is the I-th element of the
#    output set.  The elements of A are in order.
#
  import numpy as np

  if ( k <= 0 ):
    print ( '' )
    print ( 'ksub_random(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    raise Exception ( 'ksub_random(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_random(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    raise Exception ( 'ksub_random(): Fatal error!' )

  a = np.zeros ( k, dtype = np.int32 )

  for i in range ( 1, k + 1 ):
    a[i-1] = ( ( ( i - 1 ) * n ) // k )

  for i in range ( 1, k + 1 ):

    while ( True ):

      ix = rng.random_integers ( 1, n )

      l = ( ( ix * k - 1 ) // n )

      if ( a[l-1] < ix ):
        break

    a[l-1] = a[l-1] + 1

  ip = 0
  iq = k

  for i in range ( 1, k + 1 ):

    m = a[i-1]
    a[i-1] = 0

    if ( m != ( ( ( i - 1 ) * n ) // k ) ):
      ip = ip + 1
      a[ip-1] = m

  ihi = ip

  for i in range ( 1, ihi + 1 ):

    ip = ihi + 1 - i
    l = 1 + ( ( a[ip-1] * k - 1 ) // n )
    ids = a[ip-1] - ( ( ( l - 1 ) * n ) // k )
    a[ip-1] = 0
    a[iq-1] = l
    iq = iq - ids

  for ll in range ( 1, k + 1 ):

    l = k + 1 - ll

    if ( a[l-1] != 0 ):
      ir = l
      m0 = ( ( ( a[l-1] - 1 ) * n ) // k ) + 1
      m =  ( (   a[l-1]       * n ) // k ) + 1 - m0

    ix = rng.random_integers ( m0, m + m0 - 1 )

    i = l + 1

    while ( i <= ir ):

      if ( ix < a[i-1] ):
        break

      ix = ix + 1
      a[i-2] = a[i-1]
      i = i + 1

    a[i-2] = ix
    m = m - 1

  return a

def ksub_random_test ( rng ):

#*****************************************************************************80
#
## ksub_random_test() tests ksub_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_random_test():' )
  print ( '  ksub_random() generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  for i in range ( 0, 5 ):

    a = ksub_random ( n, k, rng )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ), end = '' )
    print ( '' )

  return

def ksub_rank ( k, a ):

#*****************************************************************************80
#
## ksub_rank() computes the rank of a K subset of an N set.
#
#  Discussion:
#
#    The routine accepts an array representing a subset of size K from a set
#    of size N, and returns the rank (or order) of that subset. 
#
#    It uses the same ranking that ksub_next2 uses to generate all the subsets 
#    one at a time.  
#
#    Note the value of N is not and is not, in fact,
#    needed.
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
#    integer K, the number of elements in the subset.
#
#    integer A(K), contains K distinct numbers between
#    1 and N, in order.
#
#  Output:
#
#    integer RANK, the rank of this subset.
#
  rank = 0

  for i in range ( 0, k ):

    iprod = 1

    for j in range ( i + 2, a[i] ):
      iprod = iprod * j

    for j in range ( 1, a[i] - i - 1 ):
      iprod =  ( iprod // j )

    if ( a[i] == 1 ):
      iprod = 0

    rank = rank + iprod

  rank = rank + 1

  return rank

def ksub_rank_test ( ):

#*****************************************************************************80
#
## ksub_rank_test() tests ksub_rank().
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
  import platform

  n = 5
  k = 3
  a = np.array ( [ 1, 3, 5 ] )

  print ( '' )
  print ( 'ksub_rank_test():' )
  print ( '  ksub_rank() computes rank of a K subset of an N set.' )
  print ( '' )
  print ( '  For N = %d' % ( n ) )
  print ( '  and K = %d' % ( k ) )
  print ( '  the subset is:' )
  for i in range ( 0, k ):
    print ( '  %4d' % ( a[i] ), end = '' )
  print ( '' )
 
  rank = ksub_rank ( k, a )
 
  print ( '' )
  print ( '  The rank is %d' % ( rank ) )

  return

def ksub_to_compnz ( ns, ks, bs ):

#*****************************************************************************80
#
## ksub_to_compnz() converts a K-subset to a nonzero composition.
#
#  Discussion:
#
#    There is a bijection between K subsets and nonzero compositions.
#
#    Let BS be a KS subset of a set of the integers 1 through NS.
#
#    Then let 
#      NC = NS + 1, 
#      KC = KS + 1, 
#    and define
#      AC(1) = BS(1);
#      AC(2:KC-1) = BS(2:KC-1) - BS(1:KC-2);
#      AC(KC) = NC - BS(KS).
#
#    Then AC is a composition of NC into KC parts.
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
#    integer NS, the size of the set.
#
#    integer KS, the size of the subset.
#
#    integer BS(KS), the entries of the K-subset, in increasing order.
#
#  Output:
#
#    integer NC, the composition sum.
#
#    integer KC, the number of parts of the composition.
#
#    integer AC(KC), the parts of the composition.
#
  import numpy as np

  nc = ns + 1
  kc = ks + 1
  ac = np.zeros ( kc )

  ac[0] = bs[0]
  for i in range ( 1, kc - 1 ):
    ac[i] = bs[i] - bs[i-1]

  ac[kc-1] = nc - bs[ks-1]

  return nc, kc, ac

def ksub_to_compnz_test ( rng ):

#*****************************************************************************80
#
## ksub_to_compnz_test() tests ksub_to_compnz().
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
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'ksub_to_compnz_test():' )
  print ( '  ksub_to_compnz() returns the nonzero composition' )
  print ( '  corresponding to a K subset.' )

  ns = 14
  ks = 4

  for i in range ( 0, 5 ):

    print ( '' )

    bs = ksub_random2 ( ns, ks, rng )
    print ( '  KSUB:  ', end = '' )
    for j in range ( 0, ks ):
      print ( '  %2d' % ( bs[j] ), end = '' )
    print ( '' )

    nc, kc, ac = ksub_to_compnz ( ns, ks, bs )
    print ( '  COMPNZ:', end = '' )
    for j in range ( 0, kc ):
      print ( '  %2d' % ( ac[j] ), end = '' )
    print ( '' )

  return

def ksub_to_comp ( ns, ks, bs ):

#*****************************************************************************80
#
## ksub_to_comp() converts a K-subset to a composition.
#
#  Discussion:
#
#    There is a bijection between K subsets and compositions.
#
#    Because we allow a composition to have entries that are 0, we need
#    to implicitly add 1 to each entry before establishing the bijection.
#
#    Let BS be a KS subset of a set of the integers 1 through NS.
#
#    Then let 
#      NC = NS - KS, 
#      KC = KS + 1, 
#    and define
#      AC(1) = BS(1) - 1;
#      AC(2:KC-1) = BS(2:KC-1) - BS(1:KC-2) - 1;
#      AC(KC) = NS - BS(KS).
#
#    Then AC is a composition of NC into KC parts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2015
#
#  Input:
#
#    integer NS, the size of the set.
#
#    integer KS, the size of the subset.
#
#    integer BS(KS), the entries of the K-subset, in increasing order.
#
#  Output:
#
#    integer NC, the composition sum.
#
#    integer KC, the number of parts of the composition.
#
#    integer AC(KC), the parts of the composition.
#
  import numpy as np

  nc = ns - ks
  kc = ks + 1
  ac = np.zeros ( kc )

  ac[0] = bs[0] - 1
  for i in range ( 1, kc - 1 ):
    ac[i] = bs[i] - bs[i-1]
  ac[kc-1] = ns - bs[ks-1]

  return nc, kc, ac

def ksub_to_comp_test ( rng ):

#*****************************************************************************80
#
## ksub_to_comp_test() tests ksub_to_comp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'ksub_to_comp_test():' )
  print ( '  ksub_to_comp() returns the composition corresponding to a K subset.' )

  ns = 14
  ks = 4

  for i in range ( 0, 5 ):

    print ( '' )

    bs = ksub_random2 ( ns, ks, rng )
    print ( '  KSUB:', end = '' )
    for j in range ( 0, ks ):
      print ( '  %2d' % ( bs[j] ), end = '' )
    print ( '' )

    nc, kc, ac = ksub_to_comp ( ns, ks, bs )
    print ( '  COMP:', end = '' )
    for j in range ( 0, kc ):
      print ( '  %2d' % ( ac[j] ), end = '' )
    print ( '' )

  return

def ksub_unrank ( k, rank ):

#*****************************************************************************80
#
## ksub_unrank() returns the subset of a given rank.
#
#  Discussion:
#
#    The routine is given a rank and returns the corresponding subset of K
#    elements of a set of N elements.  
#
#    It uses the same ranking that ksub_next2 uses to generate all the subsets 
#    one at a time.  
#
#    Note that the value of N itself is not nor is it needed.
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
#    integer K, the number of elements in the subset.
#
#    integer RANK, the rank of the desired subset.
#    There are ( N*(N-1)*...*(N+K-1)) / ( K*(K-1)*...*2*1) such
#    subsets, so RANK must be between 1 and that value.
#
#  Output:
#
#    integer A(K), K distinct integers in order between
#    1 and N, which define the subset.
#
  import numpy as np

  a = np.zeros ( k )

  jrank = rank - 1

  for i in range ( k, 0, -1 ):

    ip = i - 1
    iprod = 1

    while ( True ):

      ip = ip + 1

      if ( ip != i ):
        iprod = ( ( ip * iprod ) // ( ip - i ) )

      if ( jrank < iprod ):
        break

    if ( ip != i ):
      iprod = ( ( ( ip - i ) * iprod ) // ip )

    jrank = jrank - iprod
    a[i-1] = ip

  return a

def ksub_unrank_test ( ):

#*****************************************************************************80
#
## ksub_unrank_test() tests ksub_unrank().
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
  import platform

  n = 5

  k = 3
  rank = 8

  print ( '' )
  print ( 'ksub_unrank_test():' )
  print ( '  ksub_unrank() finds the K-subset of an N set' )
  print ( '  of a given rank.' )
  print ( '' )
  print ( '  N is %d' % ( n ) )
  print ( '  K is %d' % ( k ) )
  print ( '  and the desired rank is %d' % ( rank ) )
 
  a = ksub_unrank ( k, rank )
 
  print ( '' )
  print ( '  The subset of the given rank is:' )
  for i in range ( 0, k ):
    print ( '  %2d' % ( a[i] ), end = '' )
  print ( '' )

  return

def l4vec_next ( n, l4vec ):

#*****************************************************************************80
#
## l4vec_next() generates the next logical vector.
#
#  Discussion:
#
#    In the following discussion, we will let '0' stand for FALSE and
#    '1' for TRUE.
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
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    bool L4VEC(N), the vector whose successor is desired.
#
#  Output:
#
#    bool L4VEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( not l4vec[i] ):
      l4vec[i] = True
      break

    l4vec[i] = False

  return l4vec

def l4vec_next_test ( ):

#*****************************************************************************80
#
## l4vec_next_test() tests l4vec_next().
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
  import platform

  print ( '' )
  print ( 'l4vec_next_test():' )
  print ( '  l4vec_next() generates logical vectors of dimension N one at a time.' )

  for n in range ( 2, 4 ):

    print ( '' )
    print ( '  Vector size N = %d' % ( n ) )
    print ( '' )

    k = 0

    l4vec = np.zeros ( n, dtype = bool )

    for i in range ( 0, n ):
      l4vec[i] = False

    while ( True ):

      print ( '  %2d:  ' % ( k ), end = '' )
      for i in range ( 0, n ):
        print ( '  %s' % ( l4vec[i] ), end = '' )
      print ( '' )

      l4vec = l4vec_next ( n, l4vec )

      if ( not any ( l4vec ) ):
        break

      k = k + 1

  return

def moebius_values ( n_data ):

#*****************************************************************************80
#
## moebius_values() returns some values of the Moebius function.
#
#  Discussion:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1;
#              0 if N is divisible by the square of a prime;
#              (-1)^K, if N is the product of K distinct primes.
#
#    In Mathematica, the function can be evaluated by:
#
#      MoebiusMu[n]
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#  Formula:
#
#    The Moebius function is related to Euler's totient function:
#
#      PHI(N) = Sum ( D divides N ) MU(D) * ( N / D ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer N, the argument of the Moebius function.
#
#    integer C, the value of the Moebius function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
      1,  -1,  -1,   0,  -1,   1,  -1,   0,   0,   1, \
     -1,   0,  -1,   1,   1,   0,  -1,   0,  -1,   0 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     11,  12,  13,  14,  15,  16,  17,  18,  19,  20 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def moebius_values_test ( ):

#*****************************************************************************80
#
## moebius_values_test() tests moebius_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moebius_values_test():' )
  print ( '  moebius_values() stores values of the Moebius function.' )
  print ( '' )
  print ( '             N    MOEBIUS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def monomial_count ( degree_max, dim ):

#*****************************************************************************80
#
## monomial_count() counts the number of monomials up to a given degree.
#
#  Discussion:
#
#    In 3D, there are 10 monomials of degree 3 or less:
#
#    Degree  Count  List
#    ------  -----  ----
#         0      1  1
#         1      3  x y z
#         2      6  xx xy xz yy yz zz
#         3     10  xxx xxy xxz xyy xyz xzz yyy yyz yzz zzz
#
#    Total      20
#
#    The formula is
#
#      COUNTS(DEGREE,DIM) = (DIM-1+DEGREE)! / (DIM-1)! / DEGREE!
#
#      TOTAL              = (DIM  +DEGREE)! / (DIM)!   / DEGREE!
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
#  Input:
#
#    integer DEGREE_max, the maximum degree.
#
#    integer DIM, the spatial dimension.
#
#  Output:
#
#    integer TOTAL, the total number of monomials
#    of degrees 0 through DEGREE_max.
#
  total = 1

  if ( degree_max < dim ):

    top = dim + 1
    for bot in range ( 1, degree_max + 1 ):
      total = ( total * top ) // bot
      top = top + 1

  else:

    top = degree_max + 1
    for bot in range ( 1, dim + 1 ):
      total = ( total * top ) // bot
      top = top + 1

  return total

def monomial_count_test ( ):

#*****************************************************************************80
#
## monomial_count_test() tests monomial_count().
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
  import platform

  degree_max = 9

  print ( '' )
  print ( 'monomial_count_test():' )
  print ( '  monomial_count() counts the number of monomials of' )
  print ( '  degrees 0 through degree_max in a space of dimension DIM.' )
  print ( '' )
  print ( '  Using DEGREE_max = %d' % ( degree_max ) )
  print ( '' )
  print ( '  Dim  Count' )
  print ( '' )

  for dim in range ( 1, 7 ):

    total = monomial_count ( degree_max, dim )
    print ( '  %2d  %8d' % ( dim, total ) )

  return

def monomial_counts ( degree_max, dim ):

#*****************************************************************************80
#
## monomial_counts() counts the number of monomials up to a given degree.
#
#  Discussion:
#
#    In 3D, there are 10 monomials of degree 3 or less:
#
#    Degree  Count  List
#    ------  -----  ----
#         0      1  1
#         1      3  x y z
#         2      6  xx xy xz yy yz zz
#         3     10  xxx xxy xxz xyy xyz xzz yyy yyz yzz zzz
#
#    Total      20
#
#    The formula is
#
#      COUNTS(DEGREE,DIM) = (DIM-1+DEGREE)% / (DIM-1)% / DEGREE%
#
#      TOTAL              = (DIM  +DEGREE)% / (DIM)%   / DEGREE%
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
#  Input:
#
#    integer DEGREE_max, the maximum degree.
#
#    integer DIM, the spatial dimension.
#
#  Output:
#
#    integer COUNTS(1:DEGREE_max+1), the number of
#    monomials of each degree.
#
  import numpy as np

  counts = np.zeros ( degree_max + 1 )

  degree = 0
  counts[degree] = 1

  for degree in range ( 1, degree_max + 1 ):
    counts[degree] = ( counts[degree-1] * ( dim - 1 + degree ) ) / degree

  return counts

def monomial_counts_test ( ):

#*****************************************************************************80
#
## monomial_counts_test() tests monomial_counts().
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
  import platform

  degree_max = 9

  print ( '' )
  print ( 'monomial_counts_test():' )
  print ( '  monomial_counts counts the number of monomials of' )
  print ( '  degrees 0 through degree_max in a space of dimension DIM.' )

  for dim in range ( 1, 7 ):

    counts = monomial_counts ( degree_max, dim )

    s = np.sum ( counts )

    print ( '' )
    print ( '  DIM = %d' % ( dim ) )
    print ( '' )
    for degree in range ( 0, degree_max + 1 ):
      print ( '  %8d  %8d' % ( degree + 1, counts[degree] ) )
    print ( '' )
    print ( '     Total  %8d' % ( s ) )

  return

def morse_thue ( i ):

#*****************************************************************************80
#
## morse_thue() generates a morse_thue number.
#
#  Discussion:
#
#    The morse_thue sequence can be defined in a number of ways.
#
#    A) Start with the string containing the single letter '0' then
#       repeatedly apply the replacement rules '0' -> '01' and
#       '1' -> '10' to the letters of the string.  The morse_thue sequence
#       is the resulting letter sequence.
#
#    B) Starting with the string containing the single letter '0',
#       repeatedly append the binary complement of the string to itself.
#       Thus, '0' becomes '0' + '1' or '01', then '01' becomes
#       '01' + '10', which becomes '0110' + '1001', and so on.
#
#    C) Starting with I = 0, the I-th Morse-Thue number is determined
#       by taking the binary representation of I, adding the digits,
#       and computing the remainder modulo 2.
#
#  Example:
#
#     I  binary   S
#    --  ------  --
#     0       0   0
#     1       1   1
#     2      10   1
#     3      11   0
#     4     100   1
#     5     101   0
#     6     110   0
#     7     111   1
#     8    1000   1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the Morse-Thue number.
#    Normally, I is 0 or greater, but any value is allowed.
#
#  Output:
#
#    integer S, the Morse-Thue number of index I.
#
  import numpy as np

  nbits = 32

  i_copy = abs ( i )
#
#  Expand I into binary form.
#
  b = ui4_to_ubvec ( i_copy, nbits )
#
#  Sum the 1's in the binary representation.
#
  s = np.sum ( b )
#
#  Take the value modulo 2.
#
  s = ( s % 2 )
  
  return s

def morse_thue_test ( ):

#*****************************************************************************80
#
## morse_thue_test() tests morse_thue().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 100

  print ( '' )
  print ( 'morse_thue_test():' )
  print ( '  morse_thue() computes the Morse-Thue numbers.' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    s = morse_thue ( i )
    print ( '  %4d  %d' % ( i, s ) )

  return

def multinomial_coef1 ( nfactor, factor ):

#*****************************************************************************80
#
## multinomial_coef1() computes a multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    The log of the gamma function is used, to avoid overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NFACTOR, the number of factors.
#
#    integer FACTOR(NFACTOR), contains the factors.
#    0 <= FACTOR(I)
#
#  Output:
#
#    integer NCOMB, the value of the multinomial coefficient.
#
  import numpy as np
  from scipy.special import gamma
#
#  Each factor must be nonnegative.
#
  for i in range ( 0, nfactor ):

    if ( factor[i] < 0 ):
      print ( '' )
      print ( 'multinomial_coef1(): Fatal error!' )
      print ( '  Factor %d = %d' % ( i, factor[i] ) )
      print ( '  But this value must be nonnegative.' )
      raise Exception ( 'multinomial_coef1(): Fatal error!' )
#
#  The factors sum to N.
#
  n = np.sum ( factor )

  arg = float ( n + 1 )

  facn = np.log ( gamma ( arg ) )

  for i in range ( 0, nfactor ):

    arg = float ( factor[i] + 1 )
    fack = np.log ( gamma ( arg ) )
    facn = facn - fack

  ncomb = int ( round ( np.exp ( facn ) ) )

  return ncomb

def multinomial_coef1_test ( ):

#*****************************************************************************80
#
## multinomial_coef1_test() tests multinomial_coef1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  maxfactor = 5

  print ( '' )
  print ( 'multinomial_coef1_test():' )
  print ( '  multinomial_coef1() computes multinomial' )
  print ( '  coefficients using the Gamma function' )
 
  print ( '' )
  print ( '  Line 10 of the BINOMIAL table:' )
  print ( '' )

  n = 10
  nfactor = 2
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i
    factor[1] = n - i

    ncomb = multinomial_coef1 ( nfactor, factor )

    print ( '  %2d  %2d   %3d' % ( factor[0], factor[1], ncomb ) )

  print ( '' )
  print ( '  Level 5 of the TRINOMIAL coefficients:' )

  n = 5
  nfactor = 3
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i

    print ( '' )

    for j in range ( 0, n - factor[0] + 1 ):

      factor[1] = j
      factor[2] = n - factor[0] - factor[1]

      ncomb = multinomial_coef1 ( nfactor, factor )

      print ( '  %2d  %2d  %2d   %3d' % ( factor[0], factor[1], factor[2], ncomb ) )

  return

def multinomial_coef2 ( nfactor, factor ):

#*****************************************************************************80
#
## multinomial_coef2() computes a multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    A direct method is used, which should be exact.  However, there
#    is a possibility of intermediate overflow of the result.
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
#    integer NFACTOR, the number of factors.
#
#    integer FACTOR(NFACTOR), contains the factors.
#    0 <= FACTOR(I)
#
#  Output:
#
#    integer NCOMB, the value of the multinomial coefficient.
#

#
#  Each factor must be nonnegative.
#
  for i in range ( 0, nfactor ): 

    if ( factor[i] < 0 ):
      print ( '' )
      print ( 'multinomial_coef2(): Fatal error!' )
      print ( '  Factor %d = %d' % ( i, factor[i] ) )
      print ( '  But this value must be nonnegative.' )
      raise Exception ( 'multinomial_coef2(): Fatal error!' )

  ncomb = 1
  k = 0

  for i in range ( 0, nfactor ):

    for j in range ( 1, factor[i] + 1 ):
      k = k + 1
      ncomb = ( ncomb * k ) // j

  return ncomb

def multinomial_coef2_test ( ):

#*****************************************************************************80
#
## multinomial_coef2_test() tests multinomial_coef2().
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
  import numpy as np
  import platform

  maxfactor = 5

  print ( '' )
  print ( 'multinomial_coef2_test():' )
  print ( '  multinomial_coef2() computes multinomial' )
  print ( '  coefficients directly.' )

  print ( '' )
  print ( '  Line 10 of the BINOMIAL table:' )
  print ( '' )

  n = 10
  nfactor = 2
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i
    factor[1] = n - i

    ncomb = multinomial_coef2 ( nfactor, factor )

    print ( '  %2d  %2d   %3d' % ( factor[0], factor[1], ncomb ) )

  print ( '' )
  print ( '  Level 5 of the TRINOMIAL coefficients:' )

  n = 5
  nfactor = 3
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i

    print ( '' )

    for j in range ( 0, n - factor[0] + 1 ):

      factor[1] = j
      factor[2] = n - factor[0] - factor[1]

      ncomb = multinomial_coef2 ( nfactor, factor )

      print ( '  %2d  %2d  %2d   %3d' % ( factor[0], factor[1], factor[2], ncomb ) )

  return

def multiperm_enum ( n, k, counts ):

#*****************************************************************************80
#
## multiperm_enum() enumerates multipermutations.
#
#  Discussion:
#
#    A multipermutation is a permutation of objects, some of which are
#    identical.
#
#    While there are 6 permutations of the distinct objects A,B,C, there
#    are only 3 multipermutations of the objects A,B,B.
#
#    In general, there are N! permutations of N distinct objects, but
#    there are N! / ( ( M1! ) ( M2! ) ... ( MK! ) ) multipermutations
#    of N objects, in the case where the N objects consist of K
#    types, with M1 examples of type 1, M2 examples of type 2 and so on,
#    and for which objects of the same type are indistinguishable.
#
#  Example:
#
#    Input:
#
#      N = 5, K = 3, COUNTS = (/ 1, 2, 2 /)
#
#    Output:
#
#      Number = 30
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items in the multipermutation.
#
#    integer K, the number of types of items.
#    1 <= K.  Ordinarily, K <= N, but we allow any positive K, because
#    we also allow entries in COUNTS to be 0.
#
#    integer COUNTS(K), the number of items of each type.
#    0 <= COUNTS(1:K) <= N and sum ( COUNTS(1:K) ) = N.
#
#  Output:
#
#    integer VALUE, the number of multipermutations.
#
  if ( n < 0 ):
    value = -1
    return value

  if ( n == 0 ):
    value = 1
    return value

  if ( k < 1 ):
    value = -1
    return value

  if ( any ( counts < 0 ) ):
    value = -1
    return value

  if ( sum ( counts ) != n ):
    number = -1
    return value
#
#  Ready for computation.
#  By design, the integer division should never have a remainder.
#
  top = 0
  value = 1

  for i in range ( 0, k ):

    for j in range ( 1, counts[i] + 1 ):
      top = top + 1
      value = int ( round ( ( value * top ) / j ) )

  return value

def multiperm_enum_test ( rng ):

#*****************************************************************************80
#
## multiperm_enum_test() tests multiperm_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 5
  test_num = 5
  
  print ( '' )
  print ( 'multiperm_enum_test():' )
  print ( '  multiperm_enum() enumerates multipermutations.' )
  print ( '' )
  print ( '  N is the number of objects to be permuted.' )
  print ( '  K is the number of distinct types of objects.' )
  print ( '  COUNTS is the number of objects of each type.' )
  print ( '  NUMBER is the number of multipermutations.' )
  print ( '' )
  print ( '  Number       N       K       Counts(1:K)' )
  print ( '' )

  for test in range ( 0, test_num ):

    k = rng.integers ( low = 1, high = n, endpoint = True )

    counts = compnz_random ( n, k, rng )

    number = multiperm_enum ( n, k, counts )

    print ( '  %6d  %6d  %6d' % ( number, n, k ), end = '' )
    for i in range ( 0, k ):
      print ( '  %4d' % ( counts[i] ), end = '' )
    print ( '' )

  return

def multiperm_next ( n, a ):

#*****************************************************************************80
#
## multiperm_next() returns the next multipermutation.
#
#  Discussion:
#
#    To begin the computation, the user must set up the first multipermutation.
#    To compute ALL possible multipermutations, this first permutation should
#    list the values in ascending order.
#
#    The routine will compute, one by one, the next multipermutation,
#    in lexicographical order.  On the call after computing the last 
#    multipermutation, the routine will return MORE = FALSE (and will
#    reset the multipermutation to the FIRST one again.)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items in the multipermutation.
#
#    integer A[N], the current multipermutation.
#
#  Output:
#
#    integer A[N], the next multipermutation.
#
#    bool MORE, is TRUE if the next multipermutation
#    was computed, or FALSE if no further multipermutations could
#    be computed.
#

#
#  Step 1:
#  Find M, the last location in A for which A(M) < A(M+1).
#
  m = 0
  for i in range ( 1, n ):
    if ( a[i-1] < a[i] ):
      m = i
#
#  Step 2:
#  If no M was found, we've run out of multipermutations.
#
  if ( m == 0 ):
    more = False
    for i in range ( 0, n ):
      for j in range ( i + 1, n ):
        if ( a[j] < a[i] ):
          t    = a[i]
          a[i] = a[j]
          a[j] = t
    return a, more

  more = True
#
#  Step 3:
#  Ascending sort A(M+1:N).
#
  if ( m + 1 < n ):
    for i in range ( m, n ):
      for j in range ( i + 1, n ):
        if ( a[j] < a[i] ):
          t    = a[i]
          a[i] = a[j]
          a[j] = t
#
#  Step 4:
#  Locate the first larger value after A(M).
#
  i = 1
  while ( a[m+i-1] <= a[m-1] ):
    i = i + 1
#
#  Step 5:
#  Interchange A(M) and next larger value.
#
  temp = a[m-1]
  a[m-1] = a[m+i-1]
  a[m+i-1] = temp

  return a, more

def multiperm_next_test ( ):

#*****************************************************************************80
#
## multiperm_next_test() tests multiperm_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'multiperm_next_test():' )
  print ( '  multiperm_next() computes multipermutations in' )
  print ( '  lexical order.' )
  print ( '' )

  rank = 0
  a = np.array ( [ 1, 2, 2, 3, 3, 3 ] )
  n = 6
  more = True
  
  while ( more ):
      
    rank = rank + 1
    
    print ( '  %4d    ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )

    a, more = multiperm_next ( n, a )

  return

def nim_sum ( i, j ):

#*****************************************************************************80
#
## nim_sum computes() the Nim sum of two integers.
#
#  Discussion:
#
#    If K is the Nim sum of I and J, then each bit of K is the exclusive
#    OR of the corresponding bits of I and J.
#
#  Example:
#
#     I     J     K     I base 2    J base 2    K base 2
#   ----  ----  ----  ----------  ----------  ----------
#      0     0     0           0           0           0
#      1     0     1           1           0           1
#      1     1     0           1           1           0
#      2     7     5          10         111         101
#     11    28    23        1011       11100       10111
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the integers to be Nim-summed.
#
#  Output:
#
#    integer K, the Nim sum of I and J.
#
  nbits = 32

  ivec = ui4_to_ubvec ( i, nbits )
  jvec = ui4_to_ubvec ( j, nbits )

  kvec = ubvec_xor ( nbits, ivec, jvec )

  k = ubvec_to_ui4 ( nbits, kvec )

  return k

def nim_sum_test ( rng ):

#*****************************************************************************80
#
## nim_sum_test() tests nim_sum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 32
  ihi = 1000
  ilo = 0
  ntest = 5

  print ( '' )
  print ( 'nim_sum_test():' )
  print ( '  nim_sum() computes the Nim sum of two integers.' )
  print ( '' )
  print ( '    I    J    Nim(I+J)' )
  print ( '' )

  for i in range ( 0, ntest ):

    i1 = rng.integers ( low = ilo, high = ihi, endpoint = True )
    i1vec = ui4_to_ubvec ( i1, n )

    i2 = rng.integers ( low = ilo, high = ihi, endpoint = True )
    i2vec = ui4_to_ubvec ( i2, n )

    i3 = nim_sum ( i1, i2 )
    i3vec = ui4_to_ubvec ( i3, n )

    print ( '' )
    print ( '  I1, I2, I3 in decimal:' )
    print ( '' )
    print ( '  %3d' % ( i1 ) )
    print ( '  %3d' % ( i2 ) )
    print ( '  %3d' % ( i3 ) )
    print ( '' )
    print ( '  I1, I2, I3 in binary:' )
    print ( '' )

    ubvec_print ( n, i1vec, '' )
    ubvec_print ( n, i2vec, '' )
    ubvec_print ( n, i3vec, '' )

  return

def padovan ( n ):

#*****************************************************************************80
#
## padovan() returns the first N values of the Padovan sequence.
#
#  Discussion:
#
#    The Padovan sequence has the initial values:
#
#      P(0) = 1
#      P(1) = 1
#      P(2) = 1
#
#    and subsequent entries are generated by the recurrence
#
#      P(I+1) = P(I-1) + P(I-2)
#
#  Example:
#
#    0   1
#    1   1
#    2   1
#    3   2
#    4   2
#    5   3
#    6   4
#    7   5
#    8   7
#    9   9
#   10  12
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ian Stewart,
#    "A Neglected Number",
#    Scientific American, Volume 274, pages 102-102, June 1996.
#
#    Ian Stewart,
#    Math Hysteria,
#    Oxford, 2004.
#
#  Input:
#
#    integer N, the number of terms.
#
#  Output:
#
#    integer P(N), terms 0 though N-1 of the Perrin sequence.
#
  import numpy as np

  p = np.zeros ( n )

  if ( 1 <= n ):

    p[0] = 1

    if ( 2 <= n ):

      p[1] = 1

      if ( 3 <= n ):
 
        p[2] = 1

        for i in range ( 3, n ):
          p[i] = p[i-2] + p[i-3]

  return p

def padovan_test ( ):

#*****************************************************************************80
#
## padovan_test() tests padovan().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'padovan_test():' )
  print ( '  padovan() computes the Padovan numbers.' )

  p = padovan ( n );

  i4vec_print ( n, p, '  Initial Padovan sequence:' )

  return

def pell_basic ( d ):

#*****************************************************************************80
#
## pell_basic() returns the fundamental solution for Pell's basic equation.
#
#  Discussion:
#
#    Pell's equation has the form:
#
#      X^2 - D * Y^2 = 1
#
#    where D is a given non-square integer, and X and Y may be assumed
#    to be positive integers.
#
#  Example:
#
#     D   X0   Y0
#
#     2    3    2
#     3    2    1
#     5    9    4
#     6    5    2
#     7    8    3
#     8    3    1
#    10   19    6
#    11   10    3
#    12    7    2
#    13  649  180
#    14   15    4
#    15    4    1
#    17   33    8
#    18   17    4
#    19  170   39
#    20    9    2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#   John Burkardt
#
#  Reference:
#
#    Mark Herkommer,
#    Number Theory, A Programmer's Guide,
#    McGraw Hill, 1999, pages 294-307
#
#  Input:
#
#    integer D, the coefficient in Pell's equation.  D should be
#    positive, and not a perfect square.
#
#  Output:
#
#    integer X0, Y0, the fundamental or 0'th solution.
#    If X0 = Y0 = 0, then the calculation was canceled because of an error.
#    Both X0 and Y0 will be nonnegative.
#
  import numpy as np
 
  max_term = 100
#
#  If these values are returned, an error has occurred.
#
  x0 = 0
  y0 = 0
#
#  Check D.
#
  if ( d <= 0 ):
    print ( '' )
    print ( 'pell_basic(): Fatal error!' )
    print ( '  Pell coefficient D <= 0.' )
    raise Exception ( 'pell_basic(): Fatal error!' )

  q, r = i4_sqrt ( d )

  if ( r == 0 ):
    print ( '' )
    print ( 'pell_basic(): Fatal error!' )
    print ( '  Pell coefficient is a perfect square.' )
    raise Exception ( 'pell_basic(): Fatal error!' )
#
#  Find the continued fraction representation of sqrt ( D ).
#
  b, n_term = i4_sqrt_cf ( d, max_term )
#
#  If necessary, go for two periods.
#
  if ( ( n_term % 2 ) == 1 ):

    n2_term = 2 * n_term
    b2 = np.zeros ( n2_term )
    for i in range ( 0, n_term ):
      b2[i] = b[i]
    for i in range ( n_term, 2 * n_term ):
      b2[i] = b[i-n_term]

    n_term = n2_term
    b = np.zeros ( n_term )
    for i in range ( 0, n_term ):
      b[i] = b2[i]
#
#  Evaluate the continued fraction using the forward recursion algorithm.
#
  pm2 = 0
  pm1 = 1
  qm2 = 1
  qm1 = 0

  for i in range ( 0, n_term ):
    p = b[i] * pm1 + pm2
    q = b[i] * qm1 + qm2
    pm2 = pm1
    pm1 = p
    qm2 = qm1
    qm1 = q
#
#  Get the fundamental solution.
#
  x0 = p
  y0 = q

  return x0, y0

def pell_basic_test ( ):

#*****************************************************************************80
#
## pell_basic_test() tests pell_basic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pell_basic_test():' )
  print ( '  pell_basic() solves the basic Pell equation.' )
  print ( '' )
  print ( '        D        X        Y        R' )
  print ( '' )

  for d in range ( 2, 21 ):

    q, r = i4_sqrt ( d )

    if ( r != 0 ):

      x0, y0 = pell_basic ( d )

      r = x0 ** 2 - d * y0 ** 2

      print ( '  %7d  %7d  %7d  %7d' % ( d, x0, y0, r ) )

  return

def pell_next ( d, x0, y0, xn, yn ):

#*****************************************************************************80
#
## pell_next() returns the next solution of Pell's equation.
#
#  Discussion:
#
#    Pell's equation has the form:
#
#      X^2 - D * Y^2 = 1
#
#    where D is a given non-square integer, and X and Y may be assumed
#    to be positive integers.
#
#    To compute X0, Y0, call pell_basic.
#    To compute X1, Y1, call this routine, with XN and YN set to X0 and Y0.
#    To compute further solutions, call again with X0, Y0 and the previous
#    solution.
#
#  Example:
#
#    ------INPUT--------  --OUTPUT--
#
#    D  X0  Y0   XN   YN  XNP1  YNP1
#
#    2   3   2    3    2    17    12
#    2   3   2   17   12    99    70
#    2   3   2   99   70   577   408
#    2   3   2  577  408  3363  2378
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#   John Burkardt
#
#  Reference:
#
#    Mark Herkommer,
#    Number Theory, A Programmer's Guide,
#    McGraw Hill, 1999, pages 294-307
#
#  Input:
#
#    integer D, the coefficient in Pell's equation.
#
#    integer X0, Y0, the fundamental or 0'th solution.
#
#    integer XN, YN, the N-th solution.
#
#  Output:
#
#    integer XNP1, YNP1, the N+1-th solution.
#
  xnp1 = x0 * xn + d * y0 * yn
  ynp1 = x0 * yn +     y0 * xn

  return xnp1, ynp1

def pell_next_test ( ):

#*****************************************************************************80
#
## pell_next_test() tests pell_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pell_next_test():' )
  print ( '  pell_next() computes the "next" solution of the Pell equation.' )
  print ( '' )
  print ( '       D       X        Y         R' )
  print ( '' )

  for d in range ( 2, 21 ):

    q, r = i4_sqrt ( d )

    if ( r != 0 ):

      x0, y0 = pell_basic ( d )

      r = x0 ** 2 - d * y0 ** 2

      print ( '  %7d  %7d  %7d  %7d' % ( d, x0, y0, r ) )

      x1, y1 = pell_next ( d, x0, y0, x0, y0 )

      r = x1 ** 2 - d * y1 ** 2

      print ( '           %7d  %7d  %7d' % ( x1, y1, r ) )

  return

def pell_number ( n ):

#*****************************************************************************80
#
## pell_number() returns the N-th Pell number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2023
#
#  Author:
#
#   John Burkardt
#
#  Input:
#
#    integer n: the index, which must be 0 or greater.
#
#  Output:
#
#    integer pn: the N-th Pell number.
#
  if ( n < 0 ):
    raise Exception ( 'pell_number(): Fatal error!' )

  for m in range ( 0, n + 1 ):

    if ( m == 0 ):
      pn = 0
    elif ( m == 1 ):
      pnm1 = pn
      pn = 1
    else:
      pnm2 = pnm1
      pnm1 = pn
      pn = 2 * pnm1 + pnm2
 
  return pn

def pell_number_test ( ):

#*****************************************************************************80
#
## pell_number_test() tests pell_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 December 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pell_number_test():' )
  print ( '  pell_number() evaluates the N-th Pell number.' )
  print ( '' )

  print ( '' )
  print ( '  N    P(N)' )
  print ( '' )

  for n in range ( 0, 11 ):
    pn = pell_number ( n )
    print ( ' %2d  %6d' % ( n, pn ) )

  return

def pent_enum ( n ):

#*****************************************************************************80
#
## pent_enum() computes the N-th pentagonal number.
#
#  Discussion:
#
#    The pentagonal number P(N) counts the number of dots in a figure of
#    N nested pentagons.  The pentagonal numbers are defined for both
#    positive and negative N.
#
#    The pentagonal numbers are also useful in determining the
#    number of partitions of an integer.
#
#  First values:
#
#     N    P
#
#    -5   40
#    -4   26
#    -3   15
#    -2    7
#    -1    2
#     0    0
#     1    1
#     2    5
#     3   12
#     4   22
#     5   35
#     6   51
#     7   70
#     8   92
#     9  117
#    10  145
#
#  Formula:
#
#    P(N) = ( N * ( 3 * N - 1 ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the pentagonal number desired.
#
#  Output:
#
#    integer VALUE, the value of the N-th pentagonal number.
#
  value = ( n * ( 3 * n - 1 ) ) // 2

  return value

def pent_enum_test ( ):

#*****************************************************************************80
#
## pent_enum_test() tests pent_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'pent_enum_test():' )
  print ( '  pent_enum() counts points in pentagons;' )
  print ( '' )
  print ( '  N    Pent(N)' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    print ( '  %8d  %8d' % ( i, pent_enum ( i ) ) )

  return

def perm0_break_count ( n, p ):

#*****************************************************************************80
#
## perm0_break_count() counts breaks in a permutation of (0,...,N-1).
#
#  Discussion:
#
#    We begin with a permutation of order N.  We prepend an element
#    labeled "-1" and append an element labeled "N".  There are now
#    N+1 pairs of neighbors.  A "break" is a pair of neighbors whose
#    value differs by more than 1.  
#
#    The identity permutation has a break count of 0.  The maximum
#    break count is N+1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the permutation.
#
#    integer P(N), a permutation, in standard index form.
#
#  Output:
#
#    integer BREAK_count, the number of breaks in the permutation.
#
  break_count = 0
#
#  Make sure the permutation is a legal one.
#  (This is not an efficient way to do so!)
#
  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_break_count(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_break_count(): Fatal error!' )

  if ( p[0] != 0 ):
    break_count = break_count + 1

  for i in range ( 0, n - 1 ):
    if ( abs ( p[i+1] - p[i] ) != 1 ):
      break_count = break_count + 1

  if ( p[n-1] != n - 1 ):
    break_count = break_count + 1

  return break_count

def perm0_break_count_test ( ):

#*****************************************************************************80
#
## perm0_break_count_test() tests perm0_break_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  p = np.array ( [ 3, 4, 1, 0, 5, 2 ] )

  print ( '' )
  print ( 'perm0_break_count_test():' )
  print ( '  perm0_break_count() counts the breaks in a permutation.' )
 
  perm0_print ( n, p, '  The permutation:' )
 
  break_count = perm0_break_count ( n, p )

  print ( '' )
  print ( '  The number of breaks is %d' % ( break_count ) )

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
  import platform

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

def perm0_cycle ( n, p ):

#*****************************************************************************80
#
## perm0_cycle() analyzes a permutation of (0,...,N-1).
#
#  Discussion:
#
#    The routine will count cycles, find the sign of a permutation,
#    and tag a permutation.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P = 1, 2, 8, 5, 6, 7, 4, 3, 0
#
#    Output:
#
#      S = +1
#      NCYCLE = 3
#      TAG = -1, 1, 1,-1, -1, 1, 1, 1, 1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
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
#    integer N, the number of objects being permuted.
#
#    integer P(N), the permutation to be analyzed.  
#
#  Output:
#
#    integer S, the "sign" of the permutation, which is
#    +1 if the permutation is even, -1 if odd.  Every permutation
#    may be produced by a certain number of pairwise switches.
#    If the number of switches is even, the permutation itself is
#    called even.
#
#    integer NCYCLE, the number of cycles in the permutation.
#
#    integer TAG(N).  If TAG(I) is -1, then P(I) is the first element
#    of a cycle.
#
  import numpy as np

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_cycle(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_cycle(): Fatal error!' )

  ncycle = n
  tag = np.ones ( n, dtype = np.int32 )

  for i in range ( 0, n ):

    i1 = p[i] * tag[i]

    while ( i < i1 ):
      ncycle = ncycle - 1
      i2 = p[i1]
      tag[i1] = - tag[i1]
      i1 = i2

  s = 1 - 2 * ( ( n - ncycle ) % 2 )

  for i in range ( 0, n ):
    tag[i] = - tag[i]

  return s, ncycle, tag

def perm0_cycle_test ( ):

#*****************************************************************************80
#
## perm0_cycle_test() tests perm0_cycle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 9

  p = np.array ( [ 1, 2, 8, 5, 6, 7, 4, 3, 0 ], dtype = np.int32 )

  print ( '' )
  print ( 'perm0_cycle_test():' )
  print ( '  perm0_cycle() analyzes cycles in a permutation.' )
 
  perm0_print ( n, p, '  The permutation:' )
 
  s, ncycle, tag = perm0_cycle ( n, p )

  print ( '' )
  print ( '  S    =   %d' % ( s ) )
  print ( '  NCYCLE = %d' % ( ncycle ) )

  perm0_print ( n, tag, '  The permutation cycle tags:' )

  return

def perm0_distance ( n, a, b ):

#*****************************************************************************80
#
## perm0_distance() computes the distance of two permutations of (0,...,N-1).
#
#  Discussion:
#
#    The distance is known as the Ulam metric.
#
#    If we let N be the order of the permutations A and B, and L(P) be
#    the length of the longest ascending subsequence of a permutation P,
#    then the Ulam metric distance between A and B is
#
#      N - L ( A * inverse ( B ) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the permutation.
#
#    integer A(N), B(N), the permutations to be examined.
#
#  Output:
#
#    integer K, the Ulam metric distance between A and B.
#
  binv = perm0_inverse ( n, b )

  c = perm0_mul ( n, a, binv )

  length, c2 = perm_ascend ( n, c )

  k = n - length

  return k

def perm0_distance_test ( rng ):

#*****************************************************************************80
#
## perm0_distance_test() tests perm0_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'perm0_distance_test():' )
  print ( '  perm0_distance() computes the Ulam metric distance' )
  print ( '  between two permutations.' )

  p1 = perm0_random2 ( n, rng )
  perm0_print ( n, p1, '  Permutation P1' )
  p2 = perm0_random2 ( n, rng )
  perm0_print ( n, p2, '  Permutation P2' )
  p3 = perm0_random2 ( n, rng )
  perm0_print ( n, p3, '  Permutation P3' )

  k11 = perm0_distance ( n, p1, p1 )
  k12 = perm0_distance ( n, p1, p2 )
  k21 = perm0_distance ( n, p2, p1 )
  k13 = perm0_distance ( n, p1, p3 )
  k23 = perm0_distance ( n, p2, p3 )

  print ( '' )
  print ( '  K(P1,P1) should be 0.' )
  print ( '' )
  print ( '  K(P1,P1) = %d' % ( k11 ) )
  print ( '' )
  print ( '  K(P1,P2) should equal K(P2,P1).' )
  print ( '' )
  print ( '  K(P1,P2) = %d' % ( k12 ) )
  print ( '  K(P2,P1) = %d' % ( k21 ) )
  print ( '' )
  print ( '  K(P1,P3) <= K(P1,P2) + K(P2,P3).' )
  print ( '' )
  print ( '  K(P1,P3) = %d' % ( k13 ) )
  print ( '  K(P1,P2) = %d' % ( k12 ) )
  print ( '  K(P2,P3) = %d' % ( k23 ) )
  print ( '  K(P1,P2) + K(P2,P3) = %d' % ( k12 + k23 ) )

  return

def perm0_free ( npart, ipart, nfree ):

#*****************************************************************************80
#
## perm0_free() reports unused items in a partial permutation of (0,...,N-1).
#
#  Discussion:
#
#    It is assumed that the N objects being permuted are the integers from
#    0 to N-1, and that IPART contains a "partial" permutation, that
#    is, the NPART entries of IPART represent the beginning of a
#    permutation of all N items.
#
#    The routine returns in IFREE the items that have not been used yet.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPART, the number of entries in IPART.  NPART may be 0.
#
#    integer IPART(NPART), the partial permutation, which should
#    contain, at most once, some of the integers between 1 and
#    NPART+NFREE.
#
#    integer NFREE, the number of integers that have not been
#    used in IPART.  This is simply N - NPART.  NFREE may be zero.
#
#  Output:
#
#    integer IFREE(NFREE), the integers between 1 and NPART+NFREE
#    that were not used in IPART.
#
  import numpy as np

  n = npart + nfree

  if ( npart < 0 ):

    print ( '' )
    print ( 'perm0_free(): Fatal error!' )
    print ( '  NPART < 0.' )
    raise Exception ( 'perm0_free(): Fatal error!' )

  elif ( npart == 0 ):

    ifree = i4vec_indicator0 ( n )

  elif ( nfree < 0 ):

    print ( '' )
    print ( 'perm0_free(): Fatal error!' )
    print ( '  NFREE < 0.' )
    raise Exception ( 'perm0_free(): Fatal error!' )

  elif ( nfree == 0 ):

    ifree = np.zeros ( 0 )
    return ifree

  else:

    ifree = np.zeros ( nfree )

    k = 0

    for i in range ( 0, n ):

      match = False

      for j in range ( 0, npart ):

        if ( ipart[j] == i ):
          match = True
          break

      if ( not match ):

        if ( nfree < k ):
          print ( '' )
          print ( 'perm0_free(): Fatal error!' )
          print ( '  The partial permutation is illegal.' )
          raise Exception ( 'perm0_free(): Fatal error!' )

        ifree[k] = i
        k = k + 1

  return ifree

def perm0_free_test ( ):

#*****************************************************************************80
#
## perm0_free_test() tests perm0_free().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  p = np.array ( [ 4, 1, 2, 3, 0 ] )

  print ( '' )
  print ( 'perm0_free_test():' )
  print ( '  perm0_free() returns the unused values in a partial permutation.' )

  for npart in range ( 1, n + 1 ):
    ipart = np.zeros ( npart )
    for j in range ( 0, npart ):
      ipart[j] = p[j]
    nfree = n - npart
    ifree = perm0_free ( npart, ipart, nfree )
    i4vec_transpose_print ( npart, ipart, '  Partial permutation:' )
    i4vec_transpose_print ( nfree, ifree, '  Values not yet used:' )

  return

def perm0_inverse ( n, p1 ):

#*****************************************************************************80
#
## perm0_inverse() inverts a permutation of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer P1(N), the permutation.
#
#  Output:
#
#    integer P2(N), the inverse permutation
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'perm0_inverse(): Fatal error!' )
    print ( '  Input value of N = ', n )
    raise Exception ( 'perm0_inverse(): Fatal error!' )

  check = perm0_check ( n, p1 )

  if ( not check ):
    print ( '' )
    print ( 'perm0_inverse(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_inverse(): Fatal error!' )

  p2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p2[i] = p1[i] + 1

  s = 1

  for i in range ( 1, n + 1 ):

    i1 = p2[i-1]

    while ( i < i1 ):
      i2 = p2[i1-1]
      p2[i1-1] = - i2
      i1 = i2

    s = - i4_sign ( p2[i-1] )
    p2[i-1] = i4_sign ( s ) * abs ( p2[i-1] )

  for i in range ( 1, n + 1 ):

    i1 = - p2[i-1]

    if ( 0 <= i1 ):

      i0 = i

      while ( True ):

        i2 = p2[i1-1]
        p2[i1-1] = i0

        if ( i2 < 0 ):
          break

        i0 = i1
        i1 = i2

  for i in range ( 0, n ):
    p2[i] = p2[i] - 1

  return p2

def perm0_inverse_test ( ):

#*****************************************************************************80
#
## perm0_inverse_test() tests perm0_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  p1 = np.array ( [ 3, 2, 4, 0, 6, 5, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'perm0_inverse_test():' )
  print ( '  perm0_inverse() inverts a permutation of (0,...,N-1)' )

  perm0_print ( n, p1, '  The original permutation:' )
 
  p2 = perm0_inverse ( n, p1 )
 
  perm0_print ( n, p2, '  The inverted permutation:' )

  return

def perm0_inverse2 ( n, p ):

#*****************************************************************************80
#
## perm0_inverse2() inverts a permutation of (0,...,N-1).
#
#  Discussion:
#
#    The routine needs no extra vector storage in order to compute the
#    inverse of a permutation.
#
#    This feature might be useful if the permutation is large.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of objects in the permutation.
#
#    integer P(N), the permutation.
#
#  Output:
#
#    integer P_INV(N), the inverse permutation.
#
  import numpy as np

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_inverse2(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_inverse2(): Fatal error!' )

  p_inv = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p_inv[i] = p[i]

  tag = np.ones ( n, dtype = np.int32 )

  for m in range ( n - 1, -1, -1 ):

    i = p_inv[m]
    ti = tag[m]

    if ( ti < 0 ):

      tag[m] = +1

    elif ( i != m ):

      k = m

      while ( True ):

        j = p_inv[i]

        tag[i] = -1
        p_inv[i] = k

        if ( j == m ):
          p_inv[m] = i
          break

        k = i
        i = j

  return p_inv

def perm0_inverse2_test ( ):

#*****************************************************************************80
#
## perm0_inverse2()_test tests perm0_inverse2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  p = np.array ( [ 3, 2, 4, 0, 6, 5, 1 ] )

  print ( '' )
  print ( 'perm0_inverse2_test():' )
  print ( '  perm0_inverse2() inverts a permutation in place.' )

  perm0_print ( n, p, '  The original permutation:' )
 
  p_inv = perm0_inverse2 ( n, p )
 
  perm0_print ( n, p_inv, '  The inverted permutation:' )

  return

def perm0_inverse3 ( n, p ):

#*****************************************************************************80
#
## perm0_inverse3() produces the inverse of a permutation of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items permuted.
#
#    integer P(N), a permutation.
#
#  Output:
#
#    integer P_INV(N), the inverse permutation.
#
  import numpy as np

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_inverse3(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_inverse3(): Fatal error!' )

  p_inv = np.zeros ( n )

  for i in range ( 0, n ):
    p_inv[p[i]] = i
 
  return p_inv

def perm0_inverse3_test ( ):

#*****************************************************************************80
#
## perm0_inverse3_test() tests perm0_inverse3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  p = np.array ( [ 3, 2, 4, 0, 6, 5, 1 ] )

  print ( '' )
  print ( 'perm0_inverse3_test():' )
  print ( '  perm0_inverse3() inverts a permutation.' )

  perm0_print ( n, p, '  The original permutation:' )
 
  p_inv = perm0_inverse3 ( n, p )
 
  perm0_print ( n, p_inv, '  The inverted permutation:' )

  return

def perm0_lex_next ( n, p, more ):

#*****************************************************************************80
#
## perm0_lex_next() generates permutations of (0,...,N-1) in lexical order.
#
#  Example:
#
#    N = 3
#
#    1   0 1 2
#    2   0 2 1
#    3   1 0 2
#    4   1 2 0
#    5   2 0 1
#    6   2 1 0
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
#  Reference:
#
#    Mok-Kong Shen,
#    Algorithm 202: Generation of Permutations in Lexicographical Order,
#    Communications of the ACM,
#    Volume 6, September 1963, page 517.
#
#  Input:
#
#    integer N, the number of elements being permuted.
#
#    integer P(N), the permutation, in standard index form.
#
#    bool MORE.
#    On the first call, the user should set MORE = FALSE, which signals
#    the routine to do initialization.
#    On return, if MORE is TRUE, then another permutation has been
#    computed and returned, while if MORE is FALSE, there are no more
#    permutations.
#
#  Output:
#
#    integer P(N), the next permutation.
#
#    bool MORE.
#    On the first call, the user should set MORE = FALSE, which signals
#    the routine to do initialization.
#    On return, if MORE is TRUE, then another permutation has been
#    computed and returned, while if MORE is FALSE, there are no more
#    permutations.
#

#
#  Initialization.
#
  if ( not more ):

    p = i4vec_indicator0 ( n )
    more = True

  else:

    if ( n <= 1 ):
      more = False
      return p, more

    w = n

    while ( p[w-1] < p[w-2] ):

      if ( w == 2 ):
        more = False
        return p, more

      w = w - 1

    u = p[w-2]

    for j in range ( n, w - 1, -1 ):

      if ( u < p[j-1] ):

        p[w-2] = p[j-1]
        p[j-1] = u

        khi = ( n - w - 1 ) // 2

        for k in range ( 0, khi + 1 ):
          t        = p[n-k-1]
          p[n-k-1] = p[w+k-1]
          p[w+k-1] = t

        return p, more

  return p, more

def perm0_lex_next_test ( ):

#*****************************************************************************80
#
## perm0_lex_next_test() tests perm0_lex_next().
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
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'perm0_lex_next_test():' )
  print ( '  perm0_lex_next() generates permutations in order.' )
  print ( '' )
  
  p = np.zeros ( n )
  more = False
 
  while ( True ):

    p, more = perm0_lex_next ( n, p, more )

    if ( not more ):
      break

    perm0_print ( n, p, '' )

  return

def perm0_mul ( n, p1, p2 ):

#*****************************************************************************80
#
## perm0_mul() "multiplies" two permutations of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the permutations.
#
#    integer P1(N), P2(N), the permutations.
#
#  Output:
#
#    integer P3(N), the product permutation.
#
  import numpy as np

  check = perm0_check ( n, p1 )

  if ( not check ):
    print ( '' )
    print ( 'perm0_mul(): Fatal error!' )
    print ( '  The input array P1 does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_mul(): Fatal error!' )

  check = perm0_check ( n, p2 )

  if ( not check ):
    print ( '' )
    print ( 'perm0_mul(): Fatal error!' )
    print ( '  The input array P2 does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_mul(): Fatal error!' )

  p3 = np.zeros ( n )

  for i in range ( 0, n ):
    p3[i] = p2[p1[i]]

  return p3

def perm0_mul_test ( rng ):

#*****************************************************************************80
#
## perm0_mul_test() tests perm0_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'perm0_mul_test():' )
  print ( '  perm0_mul() multiplies two permutations.' )

  p1 = perm0_random ( n, rng )
  p2 = perm0_random ( n, rng )

  perm0_print ( n, p1, '  Permutation P1:' )

  perm0_print ( n, p2, '  Permutation P2:' )

  p3 = perm0_mul ( n, p1, p2 )

  perm0_print ( n, p3, '  Product permutation:' )

  return

def perm0_next3 ( n, p, more, rank ):

#*****************************************************************************80
#
## perm0_next3() computes permutations of (0,...,N-1).
#
#  Discussion:
#
#    The routine is initialized by calling with MORE = TRUE, in which case
#    it returns the identity permutation.
#
#    If the routine is called with MORE = FALSE, then the successor of the
#    input permutation is computed.
#
#    Trotter's algorithm is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hale Trotter,
#    PERM, Algorithm 115,
#    Communications of the Association for Computing Machinery,
#    Volume 5, 1962, pages 434-435.
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer P(N).  The previous permutation, 
#    if MORE is TRUE.  But on a startup call, with MORE FALSE, the input value 
#    of P is not needed.  
#
#    bool MORE.  On should be set to FALSE on an
#    initialization call, and on subsequent inputs should have its output
#    value from the previous call.  
#
#    integer RANK, the rank of the current permutation.  
#
#  Output:
#
#    integer P(N), the next permutation (if MORE is FALSE).
#
#    bool MORE.  TRUE if there was a next permutation to produce, or 
#    FALSE if there are no more permutations to produce.
#
#    integer RANK, the rank of the output permutation.  
#
  if ( not more ):

    for i in range ( 0, n ):
      p[i] = i
    more = True
    rank = 1

  else:

    n2 = n
    m2 = rank
    s = n

    while ( True ):

      q = ( m2 % n2 )
      t = ( m2 % ( 2 * n2 ) )

      if ( q != 0 ):
        break

      if ( t == 0 ):
        s = s - 1

      m2 = ( m2 // n2 )
      n2 = n2 - 1

      if ( n2 == 0 ):
        for i in range ( 0, n ):
          p[i] = i
        more = False
        rank = 1
        break

    if ( n2 != 0 ):

      if ( q == t ):
        s = s - q
      else:
        s = s + q - n2

      t      = p[s-1]
      p[s-1] = p[s]
      p[s]   = t

      rank = rank + 1

  return p, more, rank

def perm0_next3_test ( ):

#*****************************************************************************80
#
## perm0_next3_test() tests perm0_next3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'perm0_next3_test():' )
  print ( '  perm0_next3() generates permutations in order.' )
  print ( '' )

  n = 4
  p = np.zeros ( n )
  more = False
  rank = 0
 
  while ( True ):

    p, more, rank = perm0_next3 ( n, p, more, rank )

    if ( not more ):
      break

    print ( '  %3d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )

  return

def perm0_next ( n, p, more, even ):

#*****************************************************************************80
#
## perm0_next() computes permutations of (0,...,N-1), one at a time.
#
#  Discussion:
#
#    The routine is initialized by calling with MORE = TRUE, in which case
#    it returns the identity permutation.
#
#    If the routine is called with MORE = FALSE, then the successor of the
#    input permutation is computed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
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
#    integer N, the number of objects being permuted.
#
#    integer P(N), the output value of P from the previous call.
#    However, on an initialization call, with MORE = FALSE, the value of P
#    is not needed.
#
#    bool MORE, should be FALSE on the first call, to force
#    initialization.  Thereafter, it should be TRUE, to request the next
#    permutation in the sequence.
#
#    bool EVEN, is the output value of EVEN from the previous call.
#    However, on an initialization call, with MORE = FALSE, the value of EVEN
#    is not needed.
#
#  Output:
#
#    integer P(N), the next permutation.
#
#    bool MORE, indicates that there are more permutations
#    that may be generated.
#
#    bool EVEN, is TRUE if the output permutation is even,
#    that is, involves an even number of transpositions.
#
  if ( n == 1 ):
    p[0] = 0
    more = False
    even = True
    return p, more, even

  if ( not more ):

    p = i4vec_indicator0 ( n )
    more = True
    even = True

    if ( p[n-1] != 0 or p[0] != 1 + ( n % 2 ) ):
      return p, more, even

    for i in range ( 0, n - 3 ):
      if ( p[i+1] != p[i] + 1 ):
        return p, more, even

    more = False

  else:

    if ( even ):

      ia = p[0] + 1
      p[0] = p[1]
      p[1] = ia - 1
      even = False

      if ( p[n-1] != 0 or p[0] != 1 + ( n % 2 ) ):
        return p, more, even

      for i in range ( 0, n - 3 ):
        if ( p[i+1] != p[i] + 1 ):
          return p, more, even

      more = False
      return p, more, even

    else:

      more = False

      s = 0

      for i1 in range ( 1, n ):

        ia = p[i1] + 1
        i = i1 - 1
        id = 0

        for j in range ( 0, i + 1 ):
          if ( ia < p[j] + 1 ):
            id = id + 1

        s = id + s

        if ( id != ( i + 1 ) * ( s % 2 ) ):
          more = True
          break

      if ( not more ):
        p[0] = -1
        return p, more, even

    m = ( ( s + 1 ) % 2 ) * ( n + 1 )

    for j in range ( 0, i + 1 ):

      if ( i4_sign ( p[j] + 1 - ia ) != i4_sign ( p[j] + 1 - m ) ):
        m = p[j] + 1
        l = j

    p[l] = ia - 1
    p[i1] = m - 1
    even = True

  return p, more, even

def perm0_next_test ( ):

#*****************************************************************************80
#
## perm0_next_test() tests perm0_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'perm0_next_test():' )
  print ( '  perm0_next() generates permutations.' )
  print ( '' )

  more = False
  p = np.zeros ( n, dtype = np.int32 )
  even = False
 
  while ( True ):

    p, more, even = perm0_next ( n, p, more, even )

    perm0_print ( n, p, '' )

    if ( not more ):
      break

  return

def perm0_print ( n, p, title ):

#*****************************************************************************80
#
## perm0_print() prints a permutation of (0,...,N-1).
#
#  Example:
#
#    Input:
#
#      P = 6 1 3 0 4 2 5
#
#    Printed output:
#
#      "This is the permutation:"
#
#      0 1 2 3 4 5 6
#      6 1 3 0 4 2 5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer P(N), the permutation, in standard index form.
#
#    string TITLE, an optional title.
#    If no title is supplied, then only the permutation is printed.
#
  inc = 20

  if ( len ( title ) != 0 ):

    print ( '' )
    print ( title )

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )

      print ( '' )
      print ( '  ', end = '' )
      
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( i ), end = '' )
      print ( '' )

      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  else:

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )
      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  return

def perm0_print_test ( ):

#*****************************************************************************80
#
## perm0_print_test() tests perm0_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'perm0_print_test():' )
  print ( '  perm0_print() prints a permutation.' )

  n = 7
  p = np.array ( [ 6, 1, 3, 0, 4, 2, 5 ] )
  perm0_print ( n, p, '  A 0-based permutation:' )

  return

def perm0_random2 ( n, rng ):

#*****************************************************************************80
#
## perm0_random2() selects a random permutation of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    K L Hoffman, D R Shier,
#    Algorithm 564,
#    A Test Problem Generator for Discrete Linear L1 Approximation Problems,
#    ACM Transactions on Mathematical Software,
#    Volume 6, Number 4, December 1980, pages 615-617.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation in standard index form.
#
  import numpy as np

  p = i4vec_indicator0 ( n )

  for i in range ( 0, n ):

    iadd = rng.integers ( low = 1, high = n, endpoint = True )
    j = ( ( i + iadd ) % n )

    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def perm0_random2_test ( rng ):

#*****************************************************************************80
#
## perm0_random2_test() tests perm0_random2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'perm0_random2_test():' )
  print ( '  perm0_random2() randomly selects a 0-based permutation.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm0_random2 ( n, rng )
    perm0_print ( n, p, '' )

  return

def perm0_random ( n, rng ):

#*****************************************************************************80
#
## perm0_random() selects a random permutation of N objects.
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
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation of the digits 0 through N-1.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p[i] = i

  for i in range ( 0, n - 1 ):
    j = rng.integers ( low = i, high = n, endpoint = False )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def perm0_random_test ( rng ):

#*****************************************************************************80
#
## perm0_random_test() tests perm0_random().
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
#    rng(): the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'perm0_random_test():' )
  print ( '  perm0_random() randomly selects a 0-based permutation.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm0_random ( n, rng )
    perm0_print ( n, p, '' )

  return

def perm0_rank ( n, p ):

#*****************************************************************************80
#
## perm0_rank() ranks a permutation of (0,...,N-1).
#
#  Discussion:
#
#    This is the same as asking for the step at which perm0_next2
#    would compute the permutation.  The value of the rank will be
#    between 1 and N!.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Input:
#
#    integer N, the number of elements in the set that
#    is permuted by P.
#
#    integer P(N), a permutation, in standard index form.
#
#  Output:
#
#    integer RANK, the rank of the permutation.  This
#    gives the order of the given permutation in the set of all
#    the permutations on N elements.
#

#
#  Make sure the permutation is a legal one.
#  (This is not an efficient way to do so!)
#
  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_rank(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_rank(): Fatal error!' )
#
#  Compute the inverse permutation.
#
  inverse = perm0_inverse2 ( n, p )

  rank = 0

  for i in range ( 0, n ):

    count = 0

    for j in range ( 0, inverse[i] + 1 ):
      if ( p[j] < i ):
        count = count + 1

    if ( ( rank % 2 ) == 1 ):
      rem = count
    else:
      rem = i - count

    rank = ( i + 1 ) * rank + rem

  rank = rank + 1

  return rank

def perm0_rank_test ( ):

#*****************************************************************************80
#
## perm0_rank_test() tests perm0_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  p = np.array ( [ 0, 3, 1, 2 ] )

  print ( '' )
  print ( 'perm0_rank_test():' )
  print ( '  perm0_rank() ranks a permutation.' )

  perm0_print ( n, p, '  The permutation:' )
 
  rank = perm0_rank ( n, p )
 
  print ( '' )
  print ( '  The rank is: %d' % ( rank ) )

  return

def perm0_sign ( n, p ):

#*****************************************************************************80
#
## perm0_sign() returns the sign of a permutation of (0,...,N-1).
#
#  Discussion:
#
#    A permutation can always be replaced by a sequence of pairwise
#    transpositions.  A given permutation can be represented by
#    many different such transposition sequences, but the number of
#    such transpositions will always be odd or always be even.
#    If the number of transpositions is even or odd, the permutation is
#    said to be even or odd.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P = 1, 2, 8, 5, 6, 7, 4, 3, 0
#
#    Output:
#
#      P_sign = +1
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
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer P(N), a permutation, in standard index form.
#
#  Output:
#
#    integer P_sign, the "sign" of the permutation.
#    +1, the permutation is even,
#    -1, the permutation is odd.
#
  import numpy as np

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_sign(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.  In particular, the' )
    print ( '  array is missing the value %d' % ( ierror ) )
    raise Exception ( 'perm0_sign(): Fatal error!' )
#
#  Make a temporary copy of P.
#  Apparently, the input P is a pointer, and so changes to P
#  that in MATLAB would be local are, in Python, global!
#
# q = np.zeros ( n )
# for i in range ( 0, n ):
#   q[i] = p[i]

  q = p.copy ( )
#
#  Start with P_sign indicating an even permutation.
#  Restore each element of the permutation to its correct position,
#  updating P_sign as you go.
#
  p_sign = 1

  for i in range ( 0, n - 1 ):

    j = i4vec_index ( n, q, i )

    if ( j != i ):
      t    = q[i]
      q[i] = q[j]
      q[j] = t
      p_sign = - p_sign

  return p_sign

def perm0_sign_test ( ):

#*****************************************************************************80
#
## perm0_sign_test() tests perm0_sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'perm0_sign_test():' )
  print ( '  perm0_sign() computes the sign of a permutation of (0,...,N-1).' )
  print ( '' )
  print ( '  RANK  SIGN  Permutation' )
  print ( '' )

  n = 4
  p = np.zeros ( n )
  more = False

  rank = 0

  while ( True ):

    p, more = perm0_lex_next ( n, p, more )

    p_sign = perm0_sign ( n, p )

    if ( not more ):
      break

    print ( '  %2d  %4d  ' % ( rank, p_sign ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )

    rank = rank + 1

  return

def perm0_to_equiv ( n, p ):

#*****************************************************************************80
#
## perm0_to_equiv() computes the partition induced by a permutation of (0,...,N-1).
#
#  Example:
#
#    Input:
#
#      N = 9
#      P = 1, 2, 8, 5, 6, 7, 4, 3, 0
#
#    Output:
#
#      NPART = 3
#      JARRAY = 4, 3, 2
#      IARRAY = 1, 1, 1, 2  3  2  3  2, 1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer P(N), a permutation, in standard index form.
#
#  Output:
#
#    integer NPART, number of subsets in the partition.
#
#    integer JARRAY(N).  JARRAY(I) is the number of elements
#    in the I-th subset of the partition.
#
#    integer IARRAY(N).  IARRAY(I) is the class to which
#    element I belongs.
#
  import numpy as np

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_to_equiv(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_to_equiv(): Fatal error!' )
#
#  Initialize.
#
  iarray = np.zeros ( n, dtype = np.int32 )
  jarray = np.zeros ( n, dtype = np.int32 )

  npart = 0
#
#  Search for the next item J which has not been assigned a subset/orbit.
#
  for j in range ( 1, n + 1 ):

    if ( iarray[j-1] != 0 ):
      continue
#
#  Begin a new subset/orbit.
#
    npart = npart + 1
    k = j
#
#  Add the item to the subset/orbit.
#
    while ( True ):

      jarray[npart-1] = jarray[npart-1] + 1
      iarray[k-1] = npart
#
#  Apply the permutation.  If the permuted object isn't already in the
#  subset/orbit, add it.
#
      k = p[k-1] + 1

      if ( iarray[k-1] != 0 ):
        break

  return npart, jarray, iarray

def perm0_to_equiv_test ( ):

#*****************************************************************************80
#
## perm0_to_equiv_test() tests perm0_to_equiv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9
  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ] )

  print ( '' )
  print ( 'perm0_to_equiv_test():' )
  print ( '  perm0_to_equiv() returns the set partition' )
  print ( '  or equivalence classes determined by a' )
  print ( '  permutation.' )

  perm0_print ( n, p, '  The input permutation:' )
 
  npart, jarray, a = perm0_to_equiv ( n, p )

  equiv_print ( n, a, '  The partition:' )

  return

def perm0_to_inversion ( n, p ):

#*****************************************************************************80
#
## perm0_to_inversion(): permutation (0,...,N-1) to inversion sequence.
#
#  Discussion:
#
#    For a given permutation P acting on objects 0 through N-1, the inversion
#    sequence INS is defined as:
#
#      INS(1) = 0
#      INS(I) = number of values J < I for which P(I) < P(J).
#
#  Example:
#
#    Input:
#
#      ( 2, 4, 0, 3, 1 )
#
#    Output:
#
#      ( 0, 0, 2, 1, 3 )
#
#    The original permutation can be recovered from the inversion sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton and Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer P(N), the permutation, in standard index form.
#    The I-th item has been mapped to P(I).
#
#  Output:
#
#    integer INS(N), the inversion sequence of the permutation.
#
  import numpy as np

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm0_to_inversion(): Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    raise Exception ( 'perm0_to_inversion(): Fatal error!' )

  ins = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      if ( p[i] < p[j] ):
        ins[i] = ins[i] + 1

  return ins

def perm0_to_inversion_test ( ):

#*****************************************************************************80
#
## perm0_to_inversion_test() tests perm0_to_inversion().
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
  import numpy as np

  n = 5

  print ( '' )
  print ( 'perm0_to_inversion_test():' )
  print ( '  perm0_to_inversion() converts permutation (0,...,N-1) => inversion.' )

  perm = np.array ( [ 2, 4, 0, 3, 1 ] )
  perm0_print ( n, perm, '  Permutation:' )

  ins = perm0_to_inversion ( n, perm )
  i4vec_print ( n, ins, '  Inversion:' )

  perm2 = inversion_to_perm0 ( n, ins )
  perm0_print ( n, perm2, '  Recovered permutation:' )

  return

def perm0_to_ytb ( n, p ):

#*****************************************************************************80
#
## perm0_to_ytb() converts a permutation of (0,...,N-1) to a Young tableau.
#
#  Discussion:
#
#    The mapping is not invertible.  In most cases, several permutations
#    correspond to the same tableau.
#
#  Example:
#
#    N = 7
#    P = 6 1 3 0 4 2 5
#
#    YTB =
#      1 2 3 6
#      4 5
#      7
#
#    LAM = 4 2 1 0 0 0 0
#
#    A = 1 1 1 2 2 1 3
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
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#
#    integer P(N), a permutation, in standard index form.
#
#  Output:
#
#    integer LAM(N).  LAM(I) is the length of the I-th row.
#
#    integer A(N).  A(I) is the row containing I.
#
  import numpy as np
#
#  Initialize.
#
  lam = np.zeros ( n )
  a = np.zeros ( n )
  for i in range ( 0, n):
    a[i] = -1
#
#  Insert each item of the permutation.
#
  for put_index in range ( 0, n ):

    put_value = p[put_index]
    put_row = 0

    while ( True ):

      another = False

      for compare in range ( put_value + 1, n ):

        if ( a[compare] == put_row ):
          another = True
          a[put_value] = put_row
          a[compare] = -1
          put_value = compare
          put_row = put_row + 1
          break

      if ( not another ):
        break

    a[put_value] = put_row
    lam[put_row] = lam[put_row] + 1
#
#  YTB is still 1-based, so add 1 to A values.
#
  for i in range ( 0, n ):
    a[i] = a[i] + 1

  return lam, a

def perm0_to_ytb_test ( ):

#*****************************************************************************80
#
## perm0_to_ytb_test() tests perm0_to_ytb().
#
#  Licensing
#
#    This code is distributed under the MIT license.
#
#  Modified
#
#    16 June 2015
#
#  Author
#
#    John Burkardt
#
  import numpy as np

  n = 7
  p = np.array ( [ 6, 1, 3, 0, 4, 2, 5 ] )

  print ( '' )
  print ( 'perm0_to_ytb_test():' )
  print ( '  perm0_to_ytb() converts a permutation to a Young tableau.' )

  perm0_print ( n, p, '  The permutation' )
 
  lam, a = perm0_to_ytb ( n, p )

  ytb_print ( n, a, '  The Young tableau' )

  return

def perm0_unrank ( n, rank ):

#*****************************************************************************80
#
## perm0_unrank() produces the permutation of (0,...,N-1) of given rank.
#
#  Discussion:
#
#    The value of the rank should be between 1 and N!.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 June 2004
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Input:
#
#    integer N, the number of elements in the set.
#
#    integer RANK, the desired rank of the permutation.  This
#    gives the order of the given permutation in the set of all
#    the permutations on N elements.
#
#  Output:
#
#    integer P(N), the permutation, in standard index form.
#
  import numpy as np
  
  p = np.zeros ( n )
  for i in range ( 0, n ):
    p[i] = -1

  nfact = 1

  for i in range ( 1, n + 1 ):
    nfact = nfact * i

  if ( rank < 1 or nfact < rank ):
    print ( '' )
    print ( 'perm0_unrank(): Fatal error!' )
    print ( '  Illegal input value for RANK.' )
    print ( '  RANK must be between 1 and %d' % ( nfact ) )
    print ( '  but the input value is %d' % ( rank ) )
    raise Exception ( 'perm0_unrank(): Fatal error!' )

  jrank = rank - 1

  for iprev in range ( n, 0, -1 ):

    irem = ( jrank % iprev )
    jrank = ( jrank // iprev )

    if ( ( jrank % 2 ) == 1 ):
      j = 0
      jdir = 1
    else:
      j = n + 1
      jdir = -1

    icount = 0

    while ( True ):

      j = j + jdir

      if ( p[j-1] == -1 ):
        icount = icount + 1

      if ( irem < icount ):
        break

    p[j-1] = iprev - 1

  return p

def perm0_unrank_test ( ):

#*****************************************************************************80
#
## perm0_unrank_test() tests perm0_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
# 
  n = 4

  print ( '' )
  print ( 'perm0_unrank_test():' )
  print ( '  perm0_unrank(), given a rank, computes the' )
  print ( '  corresponding permutation.' )
  print ( '' )

  rank = 6

  print ( '  The requested rank is %d' % ( rank ) )
 
  p = perm0_unrank ( n, rank )
 
  perm0_print ( n, p, '  The permutation:' )

  return

def perm1_canon_to_cycle ( n, p1 ):

#*****************************************************************************80
#
## perm1_canon_to_cycle(): permutation of (1,...,N) from canonical to cycle form.
#
#  Example:
#
#    Input:
#
#      4 5 2 1 6 3
#
#    Output:
#
#      -4 5 -2 -1 6 3,
#      indicating the cycle structure
#      ( 4, 5 ) ( 2 ) ( 1, 6, 3 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, page 176.
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer P1(N), the permutation, in canonical form.
#
#  Output:
#
#    integer P2(N), the permutation, in cycle form.
#
  import numpy as np

  p2 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p2[i] = p1[i]

  pmin = p2[0] + 1

  for i in range ( 0, n ):

    if ( p2[i] < pmin ):
      pmin = p2[i]
      p2[i] = - p2[i]

  return p2

def perm1_canon_to_cycle_test ( ):

#*****************************************************************************80
#
## perm1_canon_to_cycle_test() tests perm1_canon_to_cycle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
  p1 = np.array ( [ 4, 5, 2, 1, 6, 3 ] )

  print ( '' )
  print ( 'perm1_canon_to_cycle_test():' )
  print ( '  perm1_canon_to_cycle() converts a permutation of (1,...,N) from' )
  print ( '  canonical to cycle form.' )
 
  perm1_print ( n, p1, '  The permutation in canonical form:' )
 
  p2 = perm1_canon_to_cycle ( n, p1 )

  perm1_print ( n, p2, '  The permutation in cycle form:' )

  return

def perm1_check ( n, p ):

#*****************************************************************************80
#
## perm1_check() checks a permutation of (1,...,N).
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

  perm1_print ( n, p1, '  Permutation 1:' )
  check = perm1_check ( n, p1 )

  perm1_print ( n, p2, '  Permutation 2:' )
  check = perm1_check ( n, p2 )

  perm1_print ( n, p3, '  Permutation 3:' )
  check = perm1_check ( n, p3 )

  return

def perm1_cycle_max ( p ):

#*****************************************************************************80
#
## perm1_cycle_max() returns the length of a longest cycle in a permutation.
#
#  Discussion:
#
#    The permutation is assumed to be over the integers 1 through N.
#
#  Example:
#
#      P = 2, 3, 9, 6, 7, 8, 5, 4, 1
#
#      Cycles: ( 1, 2, 3, 9 ), ( 4, 6, 8 ), ( 5, 7 )
# 
#      cycle_max = 4
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer p(n): the permutation to be analyzed.  
#
#  Output:
#
#    integer cycle_max: the length of a longest cycle in P.
#
  n = len ( p )

  cycle_max = 0;

  for i in range ( 0, n ):

    j = p[i] - 1
    cycle_length = 1

    while ( j != i ):
      j = p[j] - 1
      cycle_length = cycle_length + 1;

    cycle_max = max ( cycle_max, cycle_length );

  return cycle_max

def perm1_cycle_max_test ( ):

#*****************************************************************************80
#
## perm1_cycle_max_test() tests perm1_cycle_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9
  p1 = np.array ( [ 2,3,9,6,7,8,5,4,1 ] )

  print ( '' )
  print ( 'perm1_cycle_max_test():' )
  print ( '  perm1_cycle_max() returns the length of the longest' )
  print ( '  cycle in a permutation.' )
  print ( '' )
  print ( '  The permutation:' )
  print ( p1 )

  perm1_print ( n, p1, '  The permutation:' )
 
  p2 = perm1_index_to_cycle ( n, p1 )

  print ( '' )
  print ( '  The permutation in cycle form:' )
  print ( p2 )

  cycle_max = perm1_cycle_max ( p1 )
 
  print ( '' )
  print ( '  The longest cycle has length ', cycle_max )

  return

def perm1_cycle_stats ( p ):

#*****************************************************************************80
#
## perm1_cycle_stats() returns permutation cycle length statistics.
#
#  Discussion:
#
#    The permutation is assumed to be over the integers 1 through N.
#
#  Example:
#
#      P = 2, 3, 9, 6, 7, 8, 5, 4, 1
#
#      Cycles: ( 1, 2, 3, 9 ), ( 4, 6, 8 ), ( 5, 7 )
# 
#      cycle_max = 4
#                      1, 2, 3, 4, 5, 6, 7, 8, 9
#      cycle_stats = ( 0, 1, 1, 1, 0, 0, 0, 0, 0 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer p(n): the permutation to be analyzed.  
#
#  Output:
#
#    integer cycle_stats(n): the number of cycles of each length.
#
  import numpy as np

  n = len ( p )

  cycle_stats = np.zeros ( n )

  for i in range ( 0, n ):

    j = p[i] - 1
    cycle_length = 1

    while ( j != i ):
      j = p[j] - 1
      cycle_length = cycle_length + 1

    cycle_stats[cycle_length-1] = cycle_stats[cycle_length-1] + 1

  for i in range ( 0, n ):
    cycle_stats[i] = cycle_stats[i] / ( i + 1 )
  
  cycle_stats = cycle_stats.astype ( int )

  return cycle_stats

def perm1_cycle_stats_test ( rng ):

#*****************************************************************************80
#
## perm1_cycle_stats_test() tests perm1_cycle_stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 9
  p1 = np.array ( [ 2, 3, 9, 6, 7, 8, 5, 4, 1 ] )

  print ( '' )
  print ( 'perm1_cycle_stats_test():' )
  print ( '  perm1_cycle_stats() counts cycles of each length' )
  print ( '  in a permutation of 1 through N.' )

  perm1_print ( n, p1, '  The standard index form permutation:' )
 
  cycle_stats = perm1_cycle_stats ( p1 )

  print ( '' )
  print ( '  Cycle lengths:' )
  for i in range ( 0, n ):
    print ( '  %2d  %2d' % ( i + 1, cycle_stats[i] ) )

  print ( '' )
  print ( '  Now average over 1000 permutations of length 100:' )
  n = 100
  trials = 1000
  cycle_stats = np.zeros ( n )
  for i in range ( 0, trials ):
    p = rng.permutation ( n )
    p = p + 1
    cycle_stats = cycle_stats + perm1_cycle_stats ( p )

  cycle_stats = cycle_stats / trials

  print ( '' )
  print ( '  Cycle length averages:' )
  for i in range ( 0, n ):
    prob = 1.0 / ( i + 1 )
    print ( '  %2d  %g  %g' % ( i + 1, cycle_stats[i], prob ) )

  return

def perm1_cycle_to_canon ( n, p1 ):

#*****************************************************************************80
#
## perm1_cycle_to_canon(): permutation of (1,...,N) from cycle to canonical form.
#
#  Example:
#
#    Input:
#
#      -6 3 1 -5, 4 -2,
#      indicating the cycle structure
#      ( 6, 3, 1 ) ( 5, 4 ) ( 2 )
#
#    Output:
#
#      4 5 2 1 6 3
#
#  Discussion:
#
#    The procedure is to "rotate" the elements of each cycle so that
#    the smallest element is first:
#
#      ( 1, 6, 3 ) ( 4, 5 ) ( 2 )
#
#    and then to sort the cycles in decreasing order of their first
#    (and lowest) element:
#
#      ( 4, 5 ) ( 2 ) ( 1, 6, 3 )
#
#    and then to drop the parentheses:
#
#      4 5 2 1 6 3
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, pages 176.
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer P1(N), the permutation, in cycle form.
#
#  Output:
#
#    integer P2(N), the permutation, in canonical form.
#
  import numpy as np

  hi = np.zeros ( n, dtype = np.int32 )
  lo = np.zeros ( n, dtype = np.int32 )
  pmin = np.zeros ( n, dtype = np.int32 )
  ptemp = np.zeros ( n, dtype = np.int32 )

  p2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p2[i] = p1[i]
#
#  Work on the next cycle.
#
  nlo = 1
  ncycle = 0

  while ( nlo <= n ):
#
#  Identify NHI, the last index in this cycle.
#
    ncycle = ncycle + 1

    nhi = nlo

    while ( nhi < n ):
      if ( p2[nhi] < 0 ):
        break
      nhi = nhi + 1
#
#  Identify the smallest value in this cycle.
#
    p2[nlo-1] = - p2[nlo-1]
    pmin[ncycle-1] = p2[nlo-1]
    nmin = nlo

    for i in range ( nlo + 1, nhi + 1 ):
      if ( p2[i-1] < pmin[ncycle-1] ):
        pmin[ncycle-1] = p2[i-1]
        nmin = i
#
#  Rotate the cycle so A_MIN occurs first.
#
    for i in range ( nlo, nmin ):
      ptemp[i+nhi-nmin] = p2[i-1]
    for i in range ( nmin, nhi + 1 ):
      ptemp[i-nmin+nlo-1] = p2[i-1]

    lo[ncycle-1] = nlo
    hi[ncycle-1] = nhi
#
#  Prepare to operate on the next cycle.
#
    nlo = nhi + 1
#
#  Compute a sorting index for the cycle minima.
#  This is a 0-based index.
#
  indx = i4vec_sort_heap_index_d ( ncycle, pmin )
#
#  Copy the cycles out of the temporary array in sorted order.
#
  j = 0
  for i in range ( 0, ncycle ):
    next = indx[i]
    nlo = lo[next]
    nhi = hi[next]
    for k in range ( nlo, nhi + 1 ):
      j = j + 1
      p2[j-1] = ptemp[k-1]

  return p2

def perm1_cycle_to_canon_test ( ):

#*****************************************************************************80
#
## perm1_cycle_to_canon_test() tests perm1_cycle_to_canon().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
  p1 = np.array ( [ -6, 3, 1, -5, 4, -2 ] )

  print ( '' )
  print ( 'perm1_cycle_to_canon_test():' )
  print ( '  perm1_cycle_to_canon() converts a permutation of (1,...,N) from' )
  print ( '  cycle to canonical form.' )
 
  perm1_print ( n, p1, '  The permutation in cycle form:' )
 
  p2 = perm1_cycle_to_canon ( n, p1 )

  perm1_print ( n, p2, '  The permutation in canonical form:' )

  return

def perm1_cycle_to_index ( n, p1 ):

#*****************************************************************************80
#
## perm1_cycle_to_index(): permutation of (1,...,N) from cycle to index form.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P1 = -1, 2, 3, 9, -4, 6, 8, -5, 7
#
#    Output:
#
#      P2 = 2, 3, 9, 6, 7, 8, 5, 4, 1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 June 2015
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
#    integer N, the number of objects being permuted.
#
#    integer P1(N), the permutation, in cycle form.
#
#  Output:
#
#    integer P2(N), the permutation, in standard index form.
#
  import numpy as np

  p2 = np.zeros ( n, dtype = np.int32 )

  for j in range ( 1, n + 1 ):

    k1 = p1[j-1]

    if ( k1 < 0 ):
      k1 = -k1
      k3 = k1

    if ( j + 1 <= n ):
      k2 = p1[j]
      if ( k2 < 0 ):
        k2 = k3
    else:
      k2 = k3

    p2[k1-1] = k2

  return p2

def perm1_cycle_to_index_test ( ):

#*****************************************************************************80
#
## perm1_cycle_to_index_test() tests perm1_cycle_to_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9
  p1 = np.array ( [ 2,3,9,6,7,8,5,4,1 ] )

  print ( '' )
  print ( 'perm1_cycle_to_index_test():' )
  print ( '  perm1_cycle_to_index() converts a permutation of (1,...,N) from' )
  print ( '  cycle to standard index form.' )
 
  perm1_print ( n, p1, '  The standard index form permutation:' )
 
  p2 = perm1_index_to_cycle ( n, p1 )

  perm1_print ( n, p2, '  The permutation in cycle form:' )

  p3 = perm1_cycle_to_index ( n, p2 )
 
  perm1_print ( n, p3, '  The standard index form permutation:' )

  return

def perm1_index_to_cycle ( n, p1 ):

#*****************************************************************************80
#
## perm1_index_to_cycle(): permutation of (1,...,N) from index to cycle form.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P1 = 2, 3, 9, 6, 7, 8, 5, 4, 1
#
#    Output:
#
#      P2 = -1, 2, 3, 9, -4, 6, 8, -5, 7
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 June 2015
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
#    integer N, the number of objects being permuted.
#
#    integer P1(N), the permutation, in standard index form.
#
#  Output:
#
#    integer P2(N), the permutation, in cycle form.
#
  import numpy as np

  p2 = np.zeros ( n, dtype = np.int32 )

  i = 0
  j = 1

  while ( j <= n ):

    if ( p1[j-1] < 0 ):

      j = j + 1

    else:

      k = j

      i = i + 1
      p2[i-1] = -k

      while ( p1[k-1] != j ):
        i = i + 1
        p2[i-1] = p1[k-1]
        p1[k-1] = -p1[k-1]
        k = abs ( p1[k-1] )

      p1[k-1] = -p1[k-1]

  for i in range ( 0, n ):
    p1[i] = abs ( p1[i] )

  return p2

def perm1_index_to_cycle_test ( ):

#*****************************************************************************80
#
## perm1_index_to_cycle_test() tests perm1_index_to_cycle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9
  p1 = np.array ( [ 2,3,9,6,7,8,5,4,1 ] )

  print ( '' )
  print ( 'perm1_index_to_cycle_test():' )
  print ( '  perm1_index_to_cycle() converts a permutation of (1,...,N) from' )
  print ( '  standard index to cycle form.' )
 
  perm1_print ( n, p1, '  The standard index form permutation:' )
 
  p2 = perm1_index_to_cycle ( n, p1 )

  perm1_print ( n, p2, '  The permutation in cycle form:' )

  p3 = perm1_cycle_to_index ( n, p2 )
 
  perm1_print ( n, p3, '  The standard index form permutation:' )

  return

def perm1_print ( n, p, title ):

#*****************************************************************************80
#
## perm1_print() prints a permutation of (1,...,N).
#
#  Example:
#
#    Input:
#
#      P = 7 2 4 1 5 3 6
#
#    Printed output:
#
#      "This is the permutation:"
#
#      1 2 3 4 5 6 7
#      7 2 4 1 5 3 6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer P(N), the permutation, in standard index form.
#
#    string TITLE, an optional title.
#    If no title is supplied, then only the permutation is printed.
#
  inc = 20

  if ( len ( title ) != 0 ):

    print ( '' )
    print ( title )

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )

      print ( '' )
      print ( '  ', end = '' )
      
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( i + 1 ), end = '' )
      print ( '' )

      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  else:

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )
      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  return

def perm1_print_test ( ):

#*****************************************************************************80
#
## perm1_print_test() tests perm1_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'perm1_print_test():' )
  print ( '  perm1_print() prints a permutation of (1,...,N).' )

  n = 7
  p = np.array ( [ 7, 2, 4, 1, 5, 3, 6 ] )
  perm1_print ( n, p, '  A 1-based permutation:' )

  return

def perm_ascend ( n, p ):

#*****************************************************************************80
#
## perm_ascend() computes the longest ascending subsequence of permutation.
#
#  Discussion:
#
#    Although this routine is intended to be applied to a permutation,
#    it will work just as well for an arbitrary vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the permutation.
#
#    integer P(N), the permutation to be examined.
#
#  Output:
#
#    integer LENGTH, the length of the longest increasing subsequence.
#
#    integer SUB(LENGTH), a longest increasing subsequence of A.
#
  import numpy as np

  top = np.zeros ( n + 1, dtype = np.int32 )
  top_prev = np.zeros ( n + 1, dtype = np.int32 )

  length = 0

  if ( n <= 0 ):
    sub = np.zeros ( length )
    return length, sub

  for i in range ( 0, n ):

    k = 0

    for j in range ( 1, length + 1 ):
      if ( p[i] <= p[top[j]] ):
        k = j
        break

    if ( k == 0 ):
      length = length + 1
      k = length

    top[k] = i
    top_prev[i] = top[k-1]
#
#  Construct the subsequence.
#
  sub = np.zeros ( length, dtype = np.int32 )

  j = top[length]
  sub[length-1] = p[j]

  for i in range ( length - 2, -1, -1 ):
    j = top_prev[j]
    sub[i] = p[j]

  return length, sub

def perm_ascend_test ( ):

#*****************************************************************************80
#
## perm_ascend_test() tests perm_ascend().
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

  n = 9
  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ], dtype = np.int32 )

  print ( '' )
  print ( 'perm_ascend_test():' )
  print ( '  perm_ascend() determines the length of the longest' )
  print ( '  increasing subsequence in a permutation.' )

  perm0_print ( n, p, '  The permutation:' )

  length, subseq = perm_ascend ( n, p )

  print ( '' )
  print ( '  The longest increasing subsequence has length %d' % ( length ) )

  i4vec_print ( length, subseq, '  A longest increasing subsequence:' )

  return

def perm_fixed_enum ( n, m ):

#******************************************************************************/
#
## perm_fixed_enum() enumerates the permutations of N objects with M fixed.
#
#  Discussion:
#
#    A permutation of N objects with M fixed is a permutation in which
#    exactly M of the objects retain their original positions.  If
#    M = 0, the permutation is a "derangement".  If M = N, the
#    permutation is the identity.
#
#  Formula:
#
#    F(N,M) = ( N! / M! ) * ( 1 - 1/1! + 1/2! - 1/3! ... 1/(N-M)! )
#           = COMB(N,M) * D(N-M)
#
#    where D(N-M) is the number of derangements of N-M objects.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 June 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects to be permuted.
#    N should be at least 1.
#
#    integer M, the number of objects that retain their
#    position.  M should be between 0 and N.
#
#  Output:
#
#    integer VALUE, the number of derangements of N objects
#    in which M objects retain their positions.
#
  if ( n <= 0 ):

    value = 1

  elif ( m < 0 ):

    value = 0

  elif ( n < m ):

    value = 0

  elif ( m == n ):

    value = 1

  elif ( n == 1 ):

    if ( m == 1 ):
      value = 1
    else:
      value = 0

  else:

    value = i4_choose ( n, m ) * derange_enum ( n - m )

  return value

def perm_fixed_enum_test ( ):

#*****************************************************************************80
#
## perm_fixed_enum_test() tests perm_fixed_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'perm_fixed_enum_test():' )
  print ( '  perm_fixed_enum() enumerates the permutations' )
  print ( '  of N objects that leave M unchanged.' )
  print ( '' )
  print ( '  For this test, N = %d' % ( n ) )
  print ( '' )
  print ( '  M    F(N,M)' )
  print ( '' )

  for m in range ( 0, n + 1 ):
    value = perm_fixed_enum ( n, m )
    print ( '  %2d  %8d' % ( m, value ) )

  return

def perrin ( n ):

#*****************************************************************************80
#
## perrin() returns the first N values of the Perrin sequence.
#
#  Discussion:
#
#    The Perrin sequence has the initial values:
#
#      P(0) = 3
#      P(1) = 0
#      P(2) = 2
#
#    and subsequent entries are generated by the recurrence
#
#      P(I+1) = P(I-1) + P(I-2)
#
#    Note that if N is a prime, then N must evenly divide P(N).
#
#  Example:
#
#    0   3
#    1   0
#    2   2
#    3   3
#    4   2
#    5   5
#    6   5
#    7   7
#    8  10
#    9  12
#   10  17
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ian Stewart,
#    "A Neglected Number",
#    Scientific American, Volume 274, pages 102-102, June 1996.
#
#    Ian Stewart,
#    Math Hysteria,
#    Oxford, 2004.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1999.
#
#  Input:
#
#    integer N, the number of terms.
#
#  Output:
#
#    integer P(N), the first N terms of the sequence.
#
  import numpy as np

  p = np.zeros ( n )

  if ( 0 < n ):
    p[0] = 3

    if ( 1 < n ):
      p[1] = 0

      if ( 2 < n ):
        p[2] = 2

        for i in range ( 3, n ):
          p[i] = p[i-2] + p[i-3]

  return p

def perrin_test ( ):

#*****************************************************************************80
#
## perrin_test() tests perrin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 20

  print ( '' )
  print ( 'perrin_test():' )
  print ( '  perrin() computes the Perrin numbers.' )

  p = perrin ( n )

  i4vec_print ( n, p, '  The Perrin sequence:' )

  return

def pord_check ( n, a ):

#*****************************************************************************80
#
## pord_check() checks a matrix representing a partial ordering.
#
#  Discussion:
#
#    The array A is supposed to represent a partial ordering of
#    the elements of a set of N objects.
#
#    For distinct indices I and J, the value of A(I,J) is:
#
#      1, if I << J
#      0, otherwise ( I and J may be unrelated, or perhaps J << I).
#
#    Diagonal elements of A are ignored.
#
#    This routine checks that the values of A do represent
#    a partial ordering.
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
#    integer N, the number of elements in the set.
#
#    integer A(N,N), the partial ordering.
#    1 if I is less than J in the partial ordering, 
#    0 otherwise.
#
#  Output:
#
#    integer IERROR, error flag.
#    0, no errors detected.  A is a partial ordering.
#    1, N <= 0.
#    2, 0 < A(I,J) and 0 < A(J,I) for some I and J.
#
  ierror = 0

  if ( n <= 0 ):
    ierror = 1
    return ierror

  for i in range ( 0, n ): 
    for j in range ( i + 1, n ):

      if ( 0 < a[i,j] ):
        if ( 0 < a[j,i] ):
          ierror = 2
          return ierror

  return ierror

def pord_check_test ( ):

#*****************************************************************************80
#
## pord_check_test() tests pord_check().
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
  import numpy as np

  n = 10

  a = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 1, 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 0, 0, 1, 0, 1 ] ] )

  print ( '' )
  print ( 'pord_check_test():' )
  print ( '  pord_check() checks a partial ordering.' )

  i4mat_print ( n, n, a, '  The partial ordering matrix:' )
 
  ierror = pord_check ( n, a )
 
  print ( '' )
  print ( '  CHECK FLAG = %d' % ( ierror ) )
  print ( '  0 means no error.' )
  print ( '  1 means illegal value of N.' )
  print ( '  2 means some A(I,J) and A(J,I) are both nonzero.' )

  return

def power_mod ( a, n, m ):

#*****************************************************************************80
#
## power_mod() computes mod ( A^N, M ).
#
#  Discussion:
#
#    Some programming tricks are used to speed up the computation, and to
#    allow computations in which A^N is much too large to store in a
#    real word.
#
#    First, for efficiency, the power A^N is computed by determining
#    the binary expansion of N, then computing A, A^2, A^4, and so on
#    by repeated squaring, and multiplying only those factors that
#    contribute to A^N.
#
#    Secondly, the intermediate products are immediately "mod'ed", which
#    keeps them small.
#
#    For instance, to compute mod ( A^13, 11 ), we essentially compute
#
#       13 = 1 + 4 + 8
#
#       A^13 = A * A^4 * A^8
#
#       mod ( A^13, 11 ) = mod ( A, 11 ) * mod ( A^4, 11 ) * mod ( A^8, 11 ).
#
#    Fermat's little theorem says that if P is prime, and A is not divisible
#    by P, then ( A^(P-1) - 1 ) is divisible by P.
#
#  Example:
#
#     A  N  M  X
#
#    13  0 31  1
#    13  1 31 13
#    13  2 31 14
#    13  3 31 27
#    13  4 31 10
#    13  5 31  6
#    13  6 31 16
#    13  7 31 22
#    13  8 31  7 
#    13  9 31 29
#    13 10 31  5
#    13 11 31  3
#    13 12 31  8
#    13 13 31 11
#    13 14 31 19
#    13 15 31 30
#    13 16 31 18
#    13 17 31 17
#    13 18 31  4
#    13 19 31 21
#    13 20 31 25
#    13 21 31 15
#    13 22 31  9
#    13 23 31 24
#    13 24 31  2
#    13 25 31 26
#    13 26 31 28
#    13 27 31 23
#    13 28 31 20
#    13 29 31 12
#    13 30 31  1
#    13 31 31 13
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 November 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the base of the expression to be tested.
#    A should be nonnegative.
#
#    integer N, the power to which the base is raised.
#    N should be nonnegative.
#
#    integer M, the divisor against which the expression is tested.
#    M should be positive.
#
#  Output:
#
#    integer X, the remainder when A^N is divided by M.
#
  if ( a < 0 ):
    x = -1
    return x

  if ( int ( a ) != a ):
    x = -1
    return x

  if ( n < 0 ):
    x = -1
    return x

  if ( int ( n ) != n ):
    x = -1
    return x

  if ( m <= 0 ):
    x = -1
    return x

  if ( int ( m ) != m ):
    x = -1
    return x
#
#  A contains the successive squares of A.
#
  x = 1

  while ( 0 < n ):

    d = ( n % 2 )

    if ( d == 1 ):
      x = ( ( x * a ) % m )

    a = ( ( a * a ) % m )
    n = ( ( n - d ) // 2 )
#
#  Ensure that 0 <= X.
#
  while ( x < 0 ):
    x = x + m

  return x

def power_mod_test ( ):

#*****************************************************************************80
#
## power_mod_test() tests power_mod().
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
  print ( '' )
  print ( 'power_mod_test():' )
  print ( '  power_mod() computes the remainder of a power' )
  print ( '  of an integer modulo another integer.' )

  a = 7
  n = 50
  m = 11

  x = power_mod ( a, n, m )

  print ( '' )
  print ( '  A = %d' % ( a ) )
  print ( '  N = %d' % ( n ) )
  print ( '  M = %d' % ( m ) )
  print ( '  mod ( A^N, M ) = %d' % ( x ) )

  a = 3
  n = 118
  m = 119

  x = power_mod ( a, n, m )

  print ( '' )
  print ( '  A = %d' % ( a ) )
  print ( '  N = %d' % ( n ) )
  print ( '  M = %d' % ( m ) )
  print ( '  mod ( A^N, M ) = %d' % ( x ) )

  return

def power_series1 ( n, alpha, a ):

#*****************************************************************************80
#
## power_series1() computes the power series for G(Z) = (1+F(Z))^ALPHA.
#
#  Discussion:
#
#    The power series for F(Z) is given.
#
#    The form of the power series are:
#
#      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
#
#      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 June 2015
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
#    integer N, the number of terms in the power series.
#
#    real ALPHA, the exponent of 1+F(Z) in the definition of G(Z).
#
#    real A(N), the power series coefficients for F(Z).
#
#  Output:
#
#    real B(N), the power series coefficients for G(Z).
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):

    v = 0.0

    for i in range ( 0, j + 1 ):
      v = v + b[i] * a[j-i-1] * ( alpha * ( j - i ) - i - 1 )

    b[j] = ( alpha * a[j] + v / float ( j + 1 ) )

  return b

def power_series1_test ( ):

#*****************************************************************************80
#
## power_series1_test() tests power_series1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'power_series1_test():' )
  print ( '  power_series1() composes a power series' )

  n = 10
  alpha = 7.0
  a = np.zeros ( n )
  a[0] = 1.0

  print ( '' )
  print ( '  Power series of G(x) = (1+F(x))^alpha' )
  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '  Series for F(x):' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %12g' % ( a[i] ), end = '' )
    if (  ( ( i + 1 ) % 5 ) == 0 or i == n - 1 ):
      print ( '' )
   
  b = power_series1 ( n, alpha, a )

  print ( '' )
  print ( '  Series for G(x):' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %12g' % ( b[i] ), end = '' )
    if (  ( ( i + 1 ) % 5 ) == 0 or i == n - 1 ):
      print ( '' )

  return

def power_series2 ( n, a ):

#*****************************************************************************80
#
## power_series2() computes the power series for G(Z) = exp(F(Z)) - 1.
#
#  Discussion:
#
#    The power series for F(Z) is given.
#
#    The power series have the form:
#
#      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
#
#      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
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
#    integer N, the number of terms in the power series.
#
#    real A(N), the power series coefficients for F(Z).
#
#  Output:
#
#    real B(N), the power series coefficients for G(Z).
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 1, n + 1 ):

    v = 0.0

    for i in range ( 1, j ):
      v = v + b[i-1] * a[j-i-1] * float ( j - i )

    b[j-1] = a[j-1] + v / float ( j )

  return b

def power_series2_test ( ):

#*****************************************************************************80
#
## power_series2_test() tests power_series2().
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
  import numpy as np

  n = 4
  a = np.zeros ( n )
  a[0] = -4.0

  print ( '' )
  print ( 'power_series2_test():' )
  print ( '  power_series2() composes a power series' )
  print ( '  Here we compute the power series of G(x) = exp(F(x))-1' )
  print ( '  The number of terms is N = %d' % ( n ) )

  r8vec_print ( n, a, '  Series for F(x):' )
 
  b = power_series2 ( n, a )
 
  r8vec_print ( n, b, '  Series for G(x):' )

  return

def power_series3 ( n, a, b ):

#*****************************************************************************80
#
## power_series3() computes the power series for H(Z) = G(F(Z)).
#
#  Discussion:
#
#    The power series for G and H are given.
#
#    We assume that
#
#      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
#      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
#      H(Z) = C1*Z + C2*Z^2 + C3*Z^3 + ... + CN*Z^N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 June 2015
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
#    integer N, the number of terms in the power series.
#
#    real A(N), the power series for F.
#
#    real B(N), the power series for G.
#
#  Output:
#
#    real C(N), the power series for H.
#
  import numpy as np

  c = np.zeros ( n )
  for i in range ( 0, n ):
    c[i] = b[0] * a[i]
#
#  Search for IQ, the index of the first nonzero entry in A.
#
  iq = 0

  for i in range ( 0, n ):

    if ( a[i-1] != 0.0 ):
      iq = i
      break

  d = np.zeros ( n )

  if ( iq != 0 ):

    m = 1

    while ( True ):

      m = m + 1

      if ( n < m * iq ):
        break

      if ( b[m-1] == 0.0 ):
        continue

      r = b[m-1] * a[iq-1] ** m
      c[m*iq-1] = c[m*iq-1] + r

      for j in range ( 1, n-m*iq + 1 ):

        v = 0.0
        for i in range ( 1, j ):
          v = v + d[i-1] * a[j-i+iq-1] * ( m * ( j - i ) - i )

        d[j-1] = ( m * a[j-1] + v / j ) / a[iq-1]

      for i in range ( 1, n-m*iq + 1 ):
        c[i+m*iq-1] = c[i+m*iq-1] + d[i-1] * r

  return c

def power_series3_test ( ):

#*****************************************************************************80
#
## power_series3_test() tests power_series3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'power_series3_test():' )
  print ( '  power_series3() composes a power series' )
 
  a = np.zeros ( n )
  a[0] = 1.0
  a[1] = 1.0
 
  b = np.zeros ( n )
  b[0] = 1.0
  b[1] = 1.0

  print ( '' )
  print ( '  Power series of H(x) = G(F(x))' )
  print ( '' )
  print ( '  Number of terms, N = %d' % ( n ) )

  r8vec_print ( n, a, '  Series for F(x):' )
  r8vec_print ( n, b, '  Series for G(x):' )
 
  c = power_series3 ( n, a, b )
 
  r8vec_print ( n, c, '  Series for H(x):' )

  return

def power_series4 ( n, a, b ):

#*****************************************************************************80
#
## power_series4() computes the power series for H(Z) = G ( 1/F(Z) ).
#
#  Discussion:
#
#    The routine is given the power series for the functions F and G.
#
#    We assume that
#
#      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
#      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
#      H(Z) = C1*Z + C2*Z^2 + C3*Z^3 + ... + CN*Z^N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 June 2014
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
#    integer N, the number of terms in the power series.
#
#    real A(N), the power series for F.  A(1) may not be 0.0.
#
#    real B(N), the power series for G.
#
#  Output:
#
#    real C(N), the power series for H.
#
  import numpy as np

  if ( a[0] == 0.0 ):
    print ( '' )
    print ( 'power_series4(): Fatal error!' )
    print ( '  A(1) is zero.' )
    raise Exception ( 'power_series4(): Fatal error!' )

  c = np.zeros ( n )
  work = np.zeros ( n )

  t = 1.0

  for i in range ( 0, n ):
    t = t / a[0]
    c[i] = b[i] * t
    work[i] = a[i] * t

  for k in range ( 2, n + 1 ):
    s = -work[k-1]
    for i in range ( k, n + 1 ):
      for j in range ( i, n + 1 ):
        c[j-1] = c[j-1] + s * c[j-k]
        work[j-1] = work[j-1] + s * work[j-k]

  return c

def power_series4_test ( ):

#*****************************************************************************80
#
## power_series4_test() tests power_series4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'power_series4_test():' )
  print ( '  power_series4() composes a power series.' )
  print ( '  Power series of H(x) = G(1/F(x))' )
  print ( '' )
  print ( '  Number of terms N = %d' % ( n ) )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = 1.0 / float ( i + 1 )

  b = np.zeros ( n )
  b[0] = 1.0

  r8vec_print ( n, a, '  Series for F(x):' )
  r8vec_print ( n, b, '  Series for G(x):' )
 
  c = power_series4 ( n, a, b )
 
  r8vec_print ( n, c, '  Series for H(x):' )

  return

def prime ( n ):

#*****************************************************************************80
#
## prime() returns returns any of the first PRIME_max prime numbers.
#
#  Discussion:
#
#    PRIME_max is 1600, and the largest prime stored is 13499.
#
#    Thanks to Bart Vandewoestyne for pointing out a typo, 18 February 2005.
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
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964, pages 870-873.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 95-98.
#
#  Input:
#
#    integer N, the index of the desired prime number.
#    In general, is should be true that 0 <= N <= PRIME_max.
#    N = -1 returns PRIME_max, the index of the largest prime available.
#    N = 0 is legal, returning PRIME = 1.
#
#  Output:
#
#    integer P, the N-th prime.  If N is out of range, P
#    is returned as -1.
#
  prime_max = 1600

  prime_vector = ( (
        2,    3,    5,    7,   11,   13,   17,   19,   23,   29, \
       31,   37,   41,   43,   47,   53,   59,   61,   67,   71, \
       73,   79,   83,   89,   97,  101,  103,  107,  109,  113, \
      127,  131,  137,  139,  149,  151,  157,  163,  167,  173, \
      179,  181,  191,  193,  197,  199,  211,  223,  227,  229, \
      233,  239,  241,  251,  257,  263,  269,  271,  277,  281, \
      283,  293,  307,  311,  313,  317,  331,  337,  347,  349, \
      353,  359,  367,  373,  379,  383,  389,  397,  401,  409, \
      419,  421,  431,  433,  439,  443,  449,  457,  461,  463, \
      467,  479,  487,  491,  499,  503,  509,  521,  523,  541, \
      547,  557,  563,  569,  571,  577,  587,  593,  599,  601, \
      607,  613,  617,  619,  631,  641,  643,  647,  653,  659, \
      661,  673,  677,  683,  691,  701,  709,  719,  727,  733, \
      739,  743,  751,  757,  761,  769,  773,  787,  797,  809, \
      811,  821,  823,  827,  829,  839,  853,  857,  859,  863, \
      877,  881,  883,  887,  907,  911,  919,  929,  937,  941, \
      947,  953,  967,  971,  977,  983,  991,  997, 1009, 1013, \
     1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, \
     1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, \
     1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, \
     1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, \
     1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, \
     1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, \
     1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, \
     1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, \
     1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, \
     1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, \
     1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, \
     1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, \
     1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, \
     1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, \
     2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, \
     2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, \
     2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, \
     2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, \
     2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, \
     2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, \
     2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, \
     2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, \
     2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, \
     2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, \
     2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, \
     2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, \
     3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, \
     3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, \
     3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, \
     3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, \
     3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, \
     3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, \
     3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, \
     3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, \
     3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, \
     3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, \
     3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, \
     3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, \
     4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, \
     4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, \
     4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, \
     4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, \
     4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, \
     4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, \
     4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, \
     4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, \
     4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, \
     4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, \
     4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, \
     4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, \
     5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, \
     5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, \
     5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, \
     5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, \
     5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, \
     5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, \
     5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, \
     5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, \
     5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, \
     5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, \
     5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, \
     5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, \
     6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, \
     6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, \
     6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, \
     6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, \
     6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, \
     6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, \
     6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, \
     6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, \
     6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, \
     6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, \
     6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, \
     7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, \
     7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, \
     7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, \
     7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, \
     7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, \
     7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, \
     7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, \
     7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, \
     7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, \
     7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919, \
     7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017, \
     8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111, \
     8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, \
     8221, 8231, 8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, \
     8293, 8297, 8311, 8317, 8329, 8353, 8363, 8369, 8377, 8387, \
     8389, 8419, 8423, 8429, 8431, 8443, 8447, 8461, 8467, 8501, \
     8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573, 8581, 8597, \
     8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677, \
     8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, \
     8747, 8753, 8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, \
     8837, 8839, 8849, 8861, 8863, 8867, 8887, 8893, 8923, 8929, \
     8933, 8941, 8951, 8963, 8969, 8971, 8999, 9001, 9007, 9011, \
     9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091, 9103, 9109, \
     9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199, \
     9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, \
     9293, 9311, 9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, \
     9391, 9397, 9403, 9413, 9419, 9421, 9431, 9433, 9437, 9439, \
     9461, 9463, 9467, 9473, 9479, 9491, 9497, 9511, 9521, 9533, \
     9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623, 9629, 9631, \
     9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733, \
     9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, \
     9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, \
     9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973,10007, \
    10009,10037,10039,10061,10067,10069,10079,10091,10093,10099, \
    10103,10111,10133,10139,10141,10151,10159,10163,10169,10177, \
    10181,10193,10211,10223,10243,10247,10253,10259,10267,10271, \
    10273,10289,10301,10303,10313,10321,10331,10333,10337,10343, \
    10357,10369,10391,10399,10427,10429,10433,10453,10457,10459, \
    10463,10477,10487,10499,10501,10513,10529,10531,10559,10567, \
    10589,10597,10601,10607,10613,10627,10631,10639,10651,10657, \
    10663,10667,10687,10691,10709,10711,10723,10729,10733,10739, \
    10753,10771,10781,10789,10799,10831,10837,10847,10853,10859, \
    10861,10867,10883,10889,10891,10903,10909,10937,10939,10949, \
    10957,10973,10979,10987,10993,11003,11027,11047,11057,11059, \
    11069,11071,11083,11087,11093,11113,11117,11119,11131,11149, \
    11159,11161,11171,11173,11177,11197,11213,11239,11243,11251, \
    11257,11261,11273,11279,11287,11299,11311,11317,11321,11329, \
    11351,11353,11369,11383,11393,11399,11411,11423,11437,11443, \
    11447,11467,11471,11483,11489,11491,11497,11503,11519,11527, \
    11549,11551,11579,11587,11593,11597,11617,11621,11633,11657, \
    11677,11681,11689,11699,11701,11717,11719,11731,11743,11777, \
    11779,11783,11789,11801,11807,11813,11821,11827,11831,11833, \
    11839,11863,11867,11887,11897,11903,11909,11923,11927,11933, \
    11939,11941,11953,11959,11969,11971,11981,11987,12007,12011, \
    12037,12041,12043,12049,12071,12073,12097,12101,12107,12109, \
    12113,12119,12143,12149,12157,12161,12163,12197,12203,12211, \
    12227,12239,12241,12251,12253,12263,12269,12277,12281,12289, \
    12301,12323,12329,12343,12347,12373,12377,12379,12391,12401, \
    12409,12413,12421,12433,12437,12451,12457,12473,12479,12487, \
    12491,12497,12503,12511,12517,12527,12539,12541,12547,12553, \
    12569,12577,12583,12589,12601,12611,12613,12619,12637,12641, \
    12647,12653,12659,12671,12689,12697,12703,12713,12721,12739, \
    12743,12757,12763,12781,12791,12799,12809,12821,12823,12829, \
    12841,12853,12889,12893,12899,12907,12911,12917,12919,12923, \
    12941,12953,12959,12967,12973,12979,12983,13001,13003,13007, \
    13009,13033,13037,13043,13049,13063,13093,13099,13103,13109, \
    13121,13127,13147,13151,13159,13163,13171,13177,13183,13187, \
    13217,13219,13229,13241,13249,13259,13267,13291,13297,13309, \
    13313,13327,13331,13337,13339,13367,13381,13397,13399,13411, \
    13417,13421,13441,13451,13457,13463,13469,13477,13487,13499 ) )

  if ( n == -1 ):
    p = prime_max
  elif ( n == 0 ):
    p = 1
  elif ( n <= prime_max ):
    p = prime_vector[n-1]
  else:
    p = -1

  return p

def prime_test ( ):

#*****************************************************************************80
#
## prime_test() tests prime().
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
  print ( '' )
  print ( 'prime_test():' )
  print ( '  prime() returns primes from a table.' )

  n = -1
  prime_max = prime ( n )

  print ( '' )
  print ( '  Number of primes stored is %d' % ( prime_max ) )
  print ( '' )
  print ( '     I    Prime(I)' )
  print ( '' )
  for i in range ( 1, 11 ):
    print ( '    %4d  %6d' % ( i, prime(i) ) )
  print ( '' )
  for i in range ( prime_max - 10, prime_max + 1 ):
    print ( '    %4d  %6d' % ( i, prime(i) ) )

  return

def pythag_triple_ijk ( i, j, k ):

#*****************************************************************************80
#
## pythag_triple_ijk() computes any primitive Pythagorean triple.
#
#  Example:
#
#     I       J       K       A       B       C    A^2+B^2 = C^2
#
#     0       0       0       3       4       5        25
#     0       0       1       5      12      13       169
#     0       1       0      15       8      17       289
#     1       0       0      20      21      29       841
#     0       2       1     117      44     125     15625
#     1       1       1     207     224     305     93025
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Generating all primitive Pythagorean triples using linear algebra,
#    https://www.johndcook.com/blog/2020/10/16/primitive-pythagorean-triples/
#
#  Input:
#
#    integer I, J, K, the matrix powers.
#    These should be nonnegative.  Otherwise, some entries of A, B, C may
#    be negative.
#
#  Output:
#
#    integer A, B, C, the corresponding primitive Pythagorean triple.
#    A, B, and C are positive integers which have no common factors,
#    and A^2 + B^2 = C^2.
#
  import numpy as np

  M1 = np.array ( [ \
    [  1,  2,  2 ], \
    [  2,  1,  2 ], \
    [  2,  2,  3 ] ] )

  M2 = np.array ( [ \
    [ -1,  2,  2 ], \
    [ -2,  1,  2 ], \
    [ -2,  2,  3 ] ] )

  M3 = np.array ( [ \
    [  1, -2,  2 ], \
    [  2, -1,  2 ], \
    [  2, -2,  3 ] ] )

  abc = np.array ( [ [ 3 ], [4], [5] ] )

  ABC = np.matmul ( np.linalg.matrix_power ( M1, i ), \
        np.matmul ( np.linalg.matrix_power ( M2, j ), \
        np.matmul ( np.linalg.matrix_power ( M3, k ), abc ) ) )
#
#  We have some awkward unpacking to do here.
#
  a = ABC[0,0]
  b = ABC[1,0]
  c = ABC[2,0]

  return a, b, c

def pythag_triple_ijk_test ( ):

#*****************************************************************************80
#
## pythag_triple_ijk_test() tests pythag_triple_ijk().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pythag_triple_ijk_test():' )
  print ( '  pythag_triple_ijk() computes a primitive Pythagorean triple' )
  print ( '  by the i, j, k "coordinates".' )
  print ( '' )
  print ( '   I   J   K   A   B   C  A^2+B^2   C^2' )
  print ( '' )

  for i in range ( 0, 4 ):
    for j in range ( 0, 4 ):
      for k in range ( 0, 4 ):
        a, b, c = pythag_triple_ijk ( i, j, k )
        d = a * a + b * b
        e = c * c
        print ( '%4d  %4d  %4d  %6d  %6d  %6d  %11d  %11d' \
          % ( i, j, k, a, b, c, d, e ) )

  return

def pythag_triple_next ( i, j ):

#*****************************************************************************80
#
## pythag_triple_next() computes the next Pythagorean triple.
#
#  Example:
#
#     I       J       A       B       C    A^2+B^2 = C^2
#
#     2       1       3       4       5      25
#     3       2       5      12      13     169
#     4       1      15       8      17     289
#     4       3       7      24      25     625
#     5       2      21      20      29     841
#     5       4       9      40      41    1681
#     6       1      35      12      37    1369
#     6       3      27      36      45    2025
#     6       5      11      60      61    3721
#     7       2      45      28      53    2809
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
#    integer I, J, the generators.
#    On first call, set I = J = 0.  On repeated calls, set I and J
#    to the output values of I and J from the previous call.
#
#  Output:
#
#    integer A, B, C, the next Pythagorean triple.
#    A, B, and C are positive integers which have no common factors,
#    and A^2 + B^2 = C^2.
#
#    integer I, J, the updated values of the generators,
#    which should be used as the input values of I and J if the routine
#    is to be called again.
#

#
#  I starts at 2, and when it increases, increases by 1 and resets J;
#
#  When I is reset, J starts out at 2 if I is odd, or 1 if I is even;
#  Then I is held fixed and J increases by 2, as long as it remains less than I.
#
  if ( i == 0 and j == 0 ):
    i = 2
    j = 1
  elif ( j + 2 < i ):
    j = j + 2
  else:
    i = i + 1
    j = ( i % 2 ) + 1

  a = i ** 2 - j ** 2
  b = 2 * i * j
  c = i ** 2 + j ** 2

  return a, b, c, i, j

def pythag_triple_next_test ( ):

#*****************************************************************************80
#
## pythag_triple_next_test() tests pythag_triple_next().
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
  print ( '' )
  print ( 'pythag_triple_next_test():' )
  print ( '  pythag_triple_next() computes the "next"' )
  print ( '    Pythagorean triple.' )
  print ( '' )
  print ( '   I   J   A   B   C  A^2+B^2   C^2' )
  print ( '' )

  i = 0
  j = 0

  for k in range ( 0, 21 ):
    a, b, c, i, j = pythag_triple_next ( i, j )
    d = a ** 2 + b ** 2
    e = c ** 2
    print ( '%4d  %4d  %4d  %4d  %4d  %8d  %8d' % ( i, j, a, b, c, d, e ) )

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
  import numpy as  np

  it_max = 1000

  if ( a < 0.0 ):
    print ( '' )
    print ( 'r8_agm(): Fatal error!' )
    print ( '  Argument A < 0.' )
    raise Exception ( 'r8_agm(): Fatal error!' )

  if ( b < 0.0 ):
    print ( '' )
    print ( 'r8_agm(): Fatal error!' )
    print ( '  Argument B < 0.' )
    raise Exception ( 'r8_agm(): Fatal error!' )

  if ( a == 0.0 or b == 0.0 ):
    value = 0.0
    return value

  if ( a == b ):
    value = a
    return value

  it = 0
  tol = 100.0 * np.finfo(float).eps

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
      print ( 'r8_agm - Warning!' )
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

def r8_fall ( x, n ):

#*****************************************************************************80
#
## r8_fall() computes the falling factorial function [X]_n.
#
#  Discussion:
#
#    Note that the number of "injections" or 1-to-1 mappings from
#    a set of N elements to a set of M elements is [M]_n.
#
#    The number of permutations of N objects out of M is [M]_n.
#
#    Moreover, the Stirling numbers of the first kind can be used
#    to convert a falling factorial into a polynomial, as follows:
#
#      [X]_n = S^0_n + S^1_n * X + S^2_n * X^2 + ... + S^N_n X^N.
#
#  Formula:
#
#    [X]_n = X * ( X - 1 ) * ( X - 2 ) * ... * ( X - N + 1 ).
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
  print ( '      X        N                     Exact', end = '' )
  print ( '                  Computed' )

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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
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

def r8mat_2perm0 ( m, n, a, p, q ):

#*****************************************************************************80
#
## r8mat_2perm0() uses permutations of (0,...,M-1) and (0,...,N-1) on an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
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
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#
#    real A(M,N), the matrix to be permuted.
#
#    integer P(M), the row permutation.  P(I) is the new number of row I.
#
#    integer Q(N), the column permutation.  Q(I) is the new number
#    of column I. 
#
#  Output:
#
#    real A(M,N), the permuted matrix.
#
  sp, ncp, tagp = perm0_cycle ( m, p )

  sq, ncq, tagq = perm0_cycle ( n, q )

  for i in range ( 0, m ):

    i1 = - tagp[i] * p[i]

    if ( 0 < i1 ):

      lc = 0

      while ( True ):

        i1 = tagp[i1] * p[i1]
        lc = lc + 1

        if ( i1 < 0 ):
          break

      i1 = i

      for j in range ( 0, n ):

        if ( tagq[j] < 0 ):

          j2 = j
          k = lc

          while ( True ):

            j1 = j2
            it = a[i1,j1]

            while ( True ):

              i1 = p[i1]
              j1 = q[j1]

              t        = a[i1,j1]
              a[i1,j1] = it
              it       = t

              if ( j1 != j2 ):
                continue

              k = k - 1

              if ( i1 == i ):
                break

            j2 = q[j2]

            if ( k == 0 ):
              break

  return a

def r8mat_2perm0_test ( ):

#*****************************************************************************80
#
## r8mat_2perm0_test() test r8mat_2perm0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 9
  n = 7

  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ] )
  q = np.array ( [ 2,3,4,5,6,0,1 ] )

  print ( '' )
  print ( 'r8mat_2perm0_test():' )
  print ( '  r8mat_2perm0() reorders an R8MAT in place.' )
  print ( '  Rows and columns use different permutations.' )

  a = np.zeros ( [ m, n ] )
 
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = float ( ( i + 1 ) * 10 + ( j + 1 ) )
 
  r8mat_print ( m, n, a, '  The input matrix:' )
 
  perm0_print ( m, p, '  The row permutation:' )

  perm0_print ( n, q, '  The column permutation:' )
 
  a = r8mat_2perm0 ( m, n, a, p, q )
 
  r8mat_print ( m, n, a, '  The permuted matrix:' )

  return

def r8mat_det ( n, a ):

#*****************************************************************************80
#
## r8mat_det() finds the determinant of an R8MAT.
#
#  Discussion:
#
#    A brute force calculation is made.
#
#    This routine should only be used for small matrices, since this
#    calculation requires the summation of N! products of N numbers.
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
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#    real A(N,N), the matrix whose determinant is desired.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  import numpy as np

  det = 0.0

  p = np.zeros ( n )
  more = False
  even = False

  while ( True ):

    p, more, even = perm0_next ( n, p, more, even )

    if ( even ):
      term = 1.0
    else:
      term = -1.0

    for i in range ( 0, n ):
      term = term * a[i,p[i]]

    det = det + term

    if ( not more ):
      break

  return det

def r8mat_det_test ( ):

#*****************************************************************************80
#
## r8mat_det_test() tests r8mat_det().
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

  print ( '' )
  print ( 'r8mat_det_test():' )
  print ( '  r8mat_det(): determinant of a real matrix.' )
 
  n = 3
  a = np.zeros ( [ n, n ] )

  k = 0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )
 
  r8mat_print ( n, n, a, '  The 123/456/789 matrix:' )

  det = r8mat_det ( n, a )
 
  print ( '' )
  print ( '  Determinant of the 123/456/789 matrix is %g' % ( det ) )
 
  n = 4
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / float ( i + j + 2 )
 
  r8mat_print ( n, n, a, '  The Hilbert matrix:' )

  det = r8mat_det ( n, a )
 
  print ( '' )
  print ( '  Determinant of the Hilbert matrix is %g' % ( det ) )
 
  n = 3
  a = np.zeros ( [ n, n ] )
 
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = -1.0
      else:
        a[i,j] = 0.0
 
  r8mat_print ( n, n, a, '  The -1,2,-1 matrix:' )

  det = r8mat_det ( n, a )
 
  print ( '' )
  print ( '  Determinant of the -1,2,-1 matrix is %g' % ( det ) )

  return

def r8mat_perm0 ( n, a, p ):

#*****************************************************************************80
#
## r8mat_perm0() applies a permutation of (0,...,N-1) to a square R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
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
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix to be permuted.
#
#    integer P(N), the permutation.  P(I) is the new number of row
#    and column I.
#
#  Output:
#
#    integer A(N,N), the permuted matrix.
#
  s, nc, tag = perm0_cycle ( n, p )

  for i in range ( 0, n ):

    i1 = - tag[i] * p[i]

    if ( 0 < i1 ):

      lc = 0

      while ( True ):

        i1 = tag[i1] * p[i1]
        lc = lc + 1

        if ( i1 < 0 ):
          break

      i1 = i

      for j in range ( 0, n ):

        if ( tag[j] < 0 ):

          j2 = j
          k = lc

          while ( True ):

            j1 = j2
            it = a[i1,j1]

            while ( True ):

              i1 = p[i1]
              j1 = p[j1]

              t = a[i1,j1]
              a[i1,j1] = it
              it = t

              if ( j1 != j2 ):
                continue

              k = k - 1

              if ( i1 == i ):
                break

            j2 = p[j2]

            if ( k == 0 ):
              break

  return a

def r8mat_perm0_test ( ):

#*****************************************************************************80
#
## r8mat_perm0_test() test r8mat_perm0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 9

  p = np.array ( [ 1, 2, 8, 5, 6, 7, 4, 3, 0 ] )

  print ( '' )
  print ( 'r8mat_perm0_test():' )
  print ( '  r8mat_perm0() reorders an integer matrix in place.' )
  print ( '  The rows and columns use the same permutation.' )

  a = np.zeros ( [ n, n ], dtype = np.float64 )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( ( i + 1 ) * 10 + j + 1 )

  r8mat_print ( n, n, a, '  The input matrix:' )
 
  perm0_print ( n, p, '  The row and column permutation:' )
 
  a = r8mat_perm0 ( n, a, p )
 
  r8mat_print ( n, n, a, '  The permuted matrix:' )

  return

def r8mat_permanent ( n, a ):

#*****************************************************************************80
#
## r8mat_permanent() computes the permanent of an R8MAT.
#
#  Discussion:
#
#    The permanent function is similar to the determinant.  Recall that
#    the determinant of a matrix may be defined as the sum of all the
#    products:
#
#      S * A(1,I(1)) * A(2,I(2)) * ... * A(N,I(N))
#
#    where I is any permutation of the columns of the matrix, and S is the
#    sign of the permutation.  By contrast, the permanent function is
#    the (unsigned) sum of all the products
#
#      A(1,I(1)) * A(2,I(2)) * ... * A(N,I(N))
#
#    where I is any permutation of the columns of the matrix.  The only
#    difference is that there is no permutation sign multiplying each summand.
#
#    Symbolically, then, the determinant of a 2 by 2 matrix
#
#      a b
#      c d
#
#    is a*d-b*c, whereas the permanent of the same matrix is a*d+b*c.
#
#
#    The permanent is invariant under row and column permutations.
#    If a row or column of the matrix is multiplied by S, then the
#      permanent is likewise multiplied by S.
#    If the matrix is square, then the permanent is unaffected by
#      transposing the matrix.
#    Unlike the determinant, however, the permanent does change if
#      one row is added to another, and it is not true that the
#      permanent of the product is the product of the permanents.
#
#
#    Note that if A is a matrix of all 1's and 0's, then the permanent
#    of A counts exactly which permutations hit exactly 1's in the matrix.
#    This fact can be exploited for various combinatorial purposes.
#
#    For instance, setting the diagonal of A to 0, and the offdiagonals
#    to 1, the permanent of A counts the number of derangements of N
#    objects.
#
#    Setting the diagonal of A to 0, and ensuring that the offdiagonal
#    entries are symmetric, then A is the adjacency matrix of a graph,
#    and its permanent counts the number of perfect matchings.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2015
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
#    integer N, the order of the matrix.
#
#    real A(N,N), the value of the matrix.
#
#  Output:
#
#    real PERM, the value of the permanent of the matrix.
#
  import numpy as np

  more = False

  c = np.zeros ( n )

  for i in range ( 0, n ):
    s = 0.0
    for j in range ( 0, n ):
      s = s + a[i,j]
    c[i] = a[i,n-1] - 0.5 * s

  p = 0.0
  sgn = -1.0
  b = np.zeros ( n )
  ncard = 0

  while ( True ):

    sgn = -sgn
#
#  The proper form of this call to subset_gray_next has not been set yet.
#
    b, more, ncard, iadd = subset_gray_next ( n - 1, b, more, ncard )

    if ( ncard != 0 ):
      z = ( 2 * b[iadd] - 1 )
      for i in range ( 0, n ):
        c[i] = c[i] + z * a[i,iadd]

    p = p + sgn * np.prod ( c )

    if ( not more ):
      break

  perm = p * ( 4 * ( n % 2 ) - 2 )

  return perm

def r8mat_permanent_test ( ):

#*****************************************************************************80
#
## r8mat_permanent_test() tests r8mat_permanent().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_permanent_test():' )
  print ( '  r8mat_permanent(): the matrix permanent function.' )
  print ( '  We will analyze matrices with 0 diagonal and' )
  print ( '  1 on all offdiagonals.' )
  print ( '' )
  print ( '  Order	    Permanent.' )
  print ( '' )
 
  for n in range ( 2, 13 ):
 
    a = np.ones ( [ n, n ] )

    for i in range ( 0, n ):
      a[i,i] = 0.0

    perm = r8mat_permanent ( n, a )
 
    print ( '  %2d  %18g' % ( n, perm ) )

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

def r8poly_f2p ( n, a ):

#*****************************************************************************80
#
## r8poly_f2p() converts a real polynomial from factorial form to power sum form.
#
#  Discussion:
#
#    The (falling) factorial form is
#
#      p(x) =   a(1)
#             + a(2) * x
#             + a(3) * x*(x-1)
#             ...
#             + a(n) * x*(x-1)*...*(x-(n-2))
#
#    The power sum form is
#
#      p(x) = a(1) + a(2)*x + a(3)*x^2 + ... + a(n)*x^(n-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(N), the polynomial coefficients in factorial form.
#
#  Output:
#
#    real B(N),  the polynomial coefficients in power sum form.
#
  import numpy as np

  b = np.zeros ( n )
  for i in range ( 0, n ):
    b[i] = a[i]

  w = - float ( n )

  for m in range ( 0, n ):

    val = 0.0
    z = w

    for i in range ( m, n ):
      z = z + 1.0
      val = b[n-1+m-i] + z * val
      b[n-1+m-i] = val

    w = w + 1.0

  return b

def r8poly_f2p_test ( ):

#*****************************************************************************80
#
## r8poly_f2p_test() tests r8poly_f2p().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4
  a = r8vec_indicator1 ( n )
 
  print ( '' )
  print ( 'r8poly_f2p_test():' )
  print ( '  r8poly_f2p(): factorial => power sum.' )

  r8poly_print ( n - 1, a, '  The power sum polynomial:' )
 
  b = r8poly_p2f ( n, a )
 
  r8vec_print ( n, b, '  The factorial polynomial coefficients:' )
 
  c = r8poly_f2p ( n, b )
 
  r8poly_print ( n - 1, c, '  The recovered power sum polynomial:' )

  return

def r8poly_fval ( n, a, x ):

#*****************************************************************************80
#
## r8poly_fval() evaluates a real polynomial in factorial form.
#
#  Discussion:
#
#    The (falling) factorial form of a polynomial is:
#
#      p(x) = a(1)
#           + a(2)  *x
#           + a(3)  *x*(x-1)
#           +...
#           + a(n-1)*x*(x-1)*(x-2)...*(x-(n-3))
#           + a(n)  *x*(x-1)*(x-2)...*(x-(n-3))*(x-(n-2))
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(N), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    real X, the point at which the polynomial is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the polynomial at X.
#
  value = 0.0
  for i in range ( 0, n ):
    value = a[n-1-i] + ( x - n + 1 + i ) * value

  return value

def r8poly_fval_test ( ):

#*****************************************************************************80
#
## r8poly_fval_test() tests r8poly_fval().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8poly_fval_test():' )
  print ( '  r8poly_fval() evaluates a polynomial in factorial form.' )

  a = r8vec_indicator1 ( n )
 
  r8vec_print ( n, a, '  The factorial polynomial coefficients:' )

  x = 2.0

  val = r8poly_fval ( n, a, x )

  print ( '' )
  print ( '  R8POLY(%g) = %g' % ( x, val ) )
  print ( '  The correct value is 11.' )

  return

def r8poly_n2p ( n, a, xarray ):

#*****************************************************************************80
#
## r8poly_n2p() converts a real polynomial from Newton form to power sum form.
#
#  Discussion:
#
#    This is done by shifting all the Newton abscissas to zero.
#
#    Actually, what happens is that the abscissas of the Newton form
#    are all shifted to zero, which means that A is the power sum
#    polynomial description and A, XARRAY is the Newton polynomial
#    description.  It is only because all the abscissas are shifted to
#    zero that A can be used as both a power sum and Newton polynomial
#    coefficient array.
#
#    The Newton form of a polynomial is described by an array of N coefficients
#    A and N abscissas X:
#
#      p(x) =   a(1)
#             + a(2) * (x-x(1))
#             + a(3) * (x-x(1)) * (x-x(2))
#             ...
#             + a(n) * (x-x(1)) * (x-x(2)) * ... * (x-x(n-1))
#
#    X(N) does not occur explicitly in the formula for the evaluation of p(x),
#    although it is used in deriving the coefficients A.
#
#    The power sum form of a polynomial is:
#
#      p(x) = a(1) + a(2)*x + ... + a(n-1)*x^(n-2) + a(n)*x^(n-1)
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
#    integer N, the dimension of A.
#
#    real A(N), the coefficients of the polynomial in Newton
#    form.
#
#    real XARRAY(N), the abscissas of the Newton form of the
#    polynomial.
#
#  Output:
#
#    real A(N), the coefficients in power sum form.
#
  x = 0.0
  for i in range ( 0, n ):
    a, xarray = r8poly_nx ( n, a, xarray, x )

  return a

def r8poly_n2p_test ( ):

#*****************************************************************************80
#
## r8poly_n2p_test() tests r8poly_n2p().
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

  n = 4
  ap = r8vec_indicator1 ( n )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = 2.0 * ap[i]
 
  print ( '' )
  print ( 'r8poly_n2p_test():' )
  print ( '  r8poly_n2p(): Newton => power sum' )

  r8poly_print ( n - 1, ap, '  The power sum polynomial:' )
 
  an = r8poly_p2n ( n, ap, x )
 
  r8vec_print ( n, an,  '  Newton polynomial coefficients:' )
  r8vec_print ( n, x,  '  Newton polynomial abscissas:' )
 
  ap2 = r8poly_n2p ( n, an, x )
 
  r8poly_print ( n-1, ap2, '  The recovered power sum polynomial:' )

  return

def r8poly_nval ( n, a, xarray, x ):

#*****************************************************************************80
#
## r8poly_nval() evaluates a real polynomial in Newton form().
#
#  Definition:
#
#    The Newton form of a polynomial is
#
#      p(x) = a(1)
#           + a(2)  *(x-x1)
#           + a(3)  *(x-x1)*(x-x2)
#           +...
#           + a(n-1)*(x-x1)*(x-x2)*(x-x3)...*(x-x(n-2))
#           + a(n)  *(x-x1)*(x-x2)*(x-x3)...*(x-x(n-2))*(x-x(n-1))
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(N), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    real XARRAY(N-1), the N-1 points X which are part
#    of the definition of the polynomial.
#
#    real X, the point at which the polynomial is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the polynomial at X.
#
  value = a[n-1]
  for i in range ( n - 2, -1, -1 ):
    value = a[i] + ( x - xarray[i] ) * value

  return value

def r8poly_nval_test ( ):

#*****************************************************************************80
#
## r8poly_nval_test() tests r8poly_nval().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8poly_nval_test():' )
  print ( '  r8poly_nval() evaluates a Newton polynomial.' )

  a = r8vec_indicator1 ( n )

  x = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    x[i] = a[i] - 1.0
 
  r8vec_print ( n, a, '  Newton polynomial coefficients:' )
  r8vec_print ( n - 1, x, '  Newton polynomial abscissas:' )

  xval = 2.0
 
  aval = r8poly_nval ( n, a, x, xval )
 
  print ( '' )
  print ( '  R8POLY(%g) = %g' % ( xval, aval ) )
  print ( '  The correct value is 11.' )

  return

def r8poly_nx ( n, a, xarray, x ):

#*****************************************************************************80
#
## r8poly_nx() replaces one of the base points in a polynomial in Newton form.
#
#  Discussion:
#
#    The Newton form of a polynomial is described by an array of N coefficients
#    A and N abscissas X:
#
#      p(x) =   a(1)
#             + a(2) * (x-x(1))
#             + a(3) * (x-x(1)) * (x-x(2))
#             ...
#             + a(n) * (x-x(1)) * (x-x(2)) * ... * (x-x(n-1))
#
#    X(N) does not occur explicitly in the formula for the evaluation of p(x),
#    although it is used in deriving the coefficients A.
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
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(N), the polynomial coefficients of the Newton form.
#
#    real XARRAY(N), the set of abscissas that
#    are part of the Newton form of the polynomial.  #
#    real X, the new point to be shifted into XARRAY.
#
#  Output:
#
#    real A(N), the updated polynomial coefficients
#    of the Newton form.
#
#    real XARRAY(N), the shifted abscissas.  The first
#    entry is now equal to X.
#
  for i in range ( n - 2, -1, -1 ):
    a[i] = a[i] + ( x - xarray[i] ) * a[i+1]

  for i in range ( n - 1, 0, -1 ):
    xarray[i] = xarray[i-1]
  xarray[0] = x

  return a, xarray

def r8poly_nx_test ( ):

#*****************************************************************************80
#
## r8poly_nx_test() tests r8poly_nx().
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
  n = 3

  print ( '' )
  print ( 'r8poly_nx_test():' )
  print ( '  r8poly_nx() replaces one abscissa in a Newton polynomial.' )

  a = r8vec_indicator1 ( n )
  xarray = r8vec_indicator1 ( n )
 
  r8vec_print ( n, a, '  Newton polynomial coefficients:' )
  r8vec_print ( n, xarray, '  Newton polynomial abscissas:' )
#
#  Shift the X array by inserting X=0.
#
  x = 0.0

  print ( '' )
  print ( '  Replace one abscissa by X = %g' % ( x ) )

  a, xarray = r8poly_nx ( n, a, xarray, x )
#
#  Report the new polynomial form.
#
  r8vec_print ( n, a, '  Newton polynomial coefficients:' )
  r8vec_print ( n, xarray, '  Newton polynomial abscissas:' )

  return

def r8poly_p2f ( n, a ):

#*****************************************************************************80
#
## r8poly_p2f() converts a real polynomial from power sum form to factorial form.
#
#  Discussion:
#
#    The power sum form is
#
#      p(x) = a(1) + a(2) * x + a(3) * x^2 + ... + a(n) * x^(n-1)
#
#    The (falling) factorial form is
#
#      p(x) =   a(1)
#             + a(2) * x
#             + a(3) * x * (x-1)
#             ...
#             + a(n) * x * (x-1) *...* (x-(n-2))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(N), on the polynomial coefficients in power sum form.
#
#  Output:
#
#    real B(N), the polynomial coefficients in factorial form.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    b[i] = a[i]

  for m in range ( 0, n ):
    value = 0.0;
    for i in range ( m, n ):
      value = b[n-1+m-i] + float ( m ) * value
      b[n-1+m-i] = value

  return b

def r8poly_p2f_test ( ):

#*****************************************************************************80
#
## r8poly_p2f_test() tests r8poly_p2f().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4
  a = r8vec_indicator1 ( n )
 
  print ( '' )
  print ( 'r8poly_p2f_test():' )
  print ( '  r8poly_p2f(): power sum => factorial;' )

  r8poly_print ( n - 1, a, '  The power sum polynomial:' )
 
  b = r8poly_p2f ( n, a )
 
  r8vec_print ( n, b, '  The factorial polynomial coefficients:' )
 
  c = r8poly_f2p ( n, b )
 
  r8poly_print ( n - 1, c, '  The recovered power sum polynomial:' )

  return

def r8poly_p2n ( n, a, xarray ):

#*****************************************************************************80
#
## r8poly_p2n() converts a real polynomial from power sum form to Newton form.
#
#  Discussion:
#
#    This is done by shifting all the Newton abscissas from zero.
#
#    The power sum form of a polynomial is:
#
#      p(x) = a(1) + a(2) * x + ... + a(n-1) * x^(n-2) + a(n) * x^(n-1)
#
#    The Newton form of a polynomial is described by an array of N coefficients
#    A and N abscissas X:
#
#      p(x) =   a(1)
#             + a(2) * (x-x(1))
#             + a(3) * (x-x(1)) * (x-x(2))
#             ...
#             + a(n) * (x-x(1)) * (x-x(2)) * ... * (x-x(n-1))
#
#    X(N) does not occur explicitly in the formula for the evaluation of p(x),
#    although it is used in deriving the coefficients A.
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
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(N), the coefficients of the polynomial in power sum form.
#
#    real XARRAY(N), the desired abscissas of
#    the Newton form of the polynomial.
#
#  Output:
#
#    real A(N), the coefficients in Newton form.
#
  import numpy as np
 
  work = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    xval = xarray[i]
    a, work = r8poly_nx ( n, a, work, xval )

  return a

def r8poly_p2n_test ( ):

#*****************************************************************************80
#
## r8poly_p2n_test() tests r8poly_p2n().
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

  n = 4
  ap = r8vec_indicator1 ( n )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = 2.0 * ap[i]
 
  print ( '' )
  print ( 'r8poly_p2n_test():' )
  print ( '  r8poly_p2n(): Power sum => Newton.' )

  r8poly_print ( n-1, ap, '  The power sum polynomial:' )
 
  an = r8poly_p2n ( n, ap, x )
 
  r8vec_print ( n, an, '  Newton polynomial coefficients:' )
  r8vec_print ( n, x,  '  Newton polynomial abscissas:' )
 
  ap2 = r8poly_n2p ( n, an, x )
 
  r8poly_print ( n-1, ap2, '  The recovered power sum polynomial:' )

  return

def r8poly_p2t ( n, a1, x ):

#*****************************************************************************80
#
## r8poly_p2t() converts a real polynomial from power sum form to Taylor form.
#
#  Discussion:
#
#    The power sum form is
#
#      p(x) = a(1) + a(2)*x + a(3)*x^2 + ... + a(n)*x^(n-1)
#
#    The Taylor form of a polynomial based at X0 is
#
#      p(x) =   a(1)
#             + a(2) * (x-x0)
#             + a(3) * (x-x0)^2
#             ...
#             + a(n) * (x-x0)^(n-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A1(N), on the coefficients in power sum form.
#
#    real X, the point at which the Taylor form of the
#    polynomial is to be based.
#
#  Output:
#
#    real A2(N), the coefficients in Taylor form.
#
  import numpy as np

  a2 = np.zeros ( n )

  for i in range ( 0, n ):
    a2[i] = a1[i]

  for m in range ( 1, n + 1 ):
    value = 0.0
    for i in range ( m, n + 1 ):
      value = a2[n+m-i-1] + x * value
      a2[n+m-i-1] = value

  return a2

def r8poly_p2t_test ( ):

#*****************************************************************************80
#
## r8poly_p2t_test() tests r8poly_p2t().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4
  a = r8vec_indicator1 ( n )
  x = 2.0

  print ( '' )
  print ( 'r8poly_p2t_test():' )
  print ( '  r8poly_p2t(): Power sum => Taylor.' )
  print ( '' )
  print ( '  Taylor expansion point is X = %g' % ( x ) )

  r8vec_print ( n, a, '  The Taylor coefficients:' )

  a2 = r8poly_t2p ( n, a, x )

  r8poly_print ( n-1, a2, '  The power sum polynomial:' )

  a3 = r8poly_p2t ( n, a2, x )
 
  r8vec_print ( n, a3, '  The recovered Taylor coefficients:' )

  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## r8poly_print() prints out a polynomial.
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
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of the polynomial.
#
#    real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

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
  print ( 'r8poly_print_test():' )
  print ( '  r8poly_print() prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )

  return

def r8poly_pval ( n, a, x ):

#*****************************************************************************80
#
## r8poly_pval() evaluates a real polynomial in power sum form.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(n-1) * x^(n-1) + a(n) * x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A(1:N+1), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    real X, the point at which the polynomial is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the polynomial at X.
#
  value = 0.0
  for i in range ( n, -1, -1 ):
    value = value * x + a[i]

  return value

def r8poly_pval_test ( ):

#*****************************************************************************80
#
## r8poly_pval_test() tests r8poly_pval().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  a = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    a[i] = float ( i + 1 )

  print ( '' )
  print ( 'r8poly_pval_test():' )
  print ( '  r8poly_pval() evaluates a polynomial in power sum form.' )

  r8poly_print ( n, a, '  The polynomial to be evaluated:' )

  x = 2.0
 
  val = r8poly_pval ( n, a, x )

  print ( '' )
  print ( '  At X = %f' % ( x ) )
  print ( '  Computed polynomial value is %f' % ( val ) )
  print ( '  Correct value is 129.' )

  return

def r8poly ( n, a, x0, iopt ):

#*****************************************************************************80
#
## r8poly() performs operations on real polynomials in power or factorial form.
#
#  Discussion:
#
#    The power sum form of a polynomial is
#
#      P(X) = A1 + A2*X + A3*X^2 + ... + (AN+1)*X^N
#
#    The Taylor expansion at C has the form
#
#      P(X) = A1 + A2*(X-C) + A3*(X-C)^2 + ... + (AN+1)*(X-C)^N
#
#    The factorial form of a polynomial is
#
#      P(X) = A1 + A2*X + A3*(X)*(X-1) + A4*(X)*(X-1)*(X-2)+...
#        + (AN+1)*(X)*(X-1)*...*(X-N+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
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
#    integer N, the number of coefficients in the polynomial
#    (in other words, the polynomial degree + 1)
#
#    real A(N), the coefficients of the polynomial.
#
#    real X0, for IOPT = -1, 0, or positive, the value of the
#    argument at which the polynomial is to be evaluated, or the
#    Taylor expansion is to be carried out.
#
#    integer IOPT, a flag describing which algorithm is to
#    be carried out:
#
#    -3: Reverse Stirling.  Input the coefficients of the polynomial in
#    factorial form, output them in power sum form.
#
#    -2: Stirling.  Input the coefficients in power sum form, output them
#    in factorial form.
#
#    -1: Evaluate a polynomial which has been input in factorial form.
#
#    0:  Evaluate a polynomial input in power sum form.
#
#    1 or more:  Given the coefficients of a polynomial in
#    power sum form, compute the first IOPT coefficients of
#    the polynomial in Taylor expansion form.
#
#  Output:
#
#    real A(N), the coefficients of the output polynomial.
#    Depending on the option chosen, these coefficients are the input values,
#    or those of a different form of the polynomial.
#
#    real VAL, for IOPT = -1 or 0, the value of the
#    polynomial at the point X0.
#
  val = 0.0

  n1 = min ( n, iopt )
  n1 = max ( 1, n1 )

  if ( iopt < -1 ):
    n1 = n

  delta = float ( ( max ( -iopt, 0 ) % 2 ) )

  w = - float ( n ) * delta

  if ( -2 < iopt ):
    w = w + x0

  for m in range ( 1, n1 + 1 ):

    val = 0.0
    z = w

    for i in range ( m, n + 1 ):
      z = z + delta
      val = a[n+m-i-1] + z * val
      if ( iopt != 0 and iopt != -1 ):
        a[n+m-i-1] = val

    if ( iopt < 0 ):
      w = w + 1.0

  return a, val

def r8poly_test ( ):

#*****************************************************************************80
#
## r8poly_test() tests r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6

  print ( '' )
  print ( 'r8poly_test():' )
  print ( '  r8poly() converts between power sum, factorial' )
  print ( '  and Taylor forms, and can evaluate a polynomial' )
  print ( '' )
 
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      iopt = -3
      x0 = 0.0
    elif ( test == 2 ):
      iopt = -2
      x0 = 0.0
    elif ( test == 3 ):
      iopt = -1
      x0 = 2.0
    elif ( test == 4 ):
      iopt = 0
      x0 = 2.0
    elif ( test == 5 ):
      iopt = 6
      x0 = 2.0
    elif ( test == 6 ):
      iopt = 6
      x0 = -2.0

    a = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ] )

    if ( test == 1 ):
      print ( '' )
      print ( '  All calls have input A as follows:' )
      for i in range ( 0, n ):
        print ( '  %g' % ( a[i] ) )
      print ( '' )
 
    a, val = r8poly ( n, a, x0, iopt )
 
    print ( '' )
    print ( '  Option IOPT = %d' % ( iopt ) )

    if ( -1 <= iopt ):
      print ( '  X0 = %g' % ( x0 ) )

    if ( iopt == -3 or iopt == -2 or 0 < iopt ):
      print ( '  Output array:' )
      for i in range ( 0, n ):
        print ( '  %g' % ( a[i] ), end = '' )
      print ( '' )

    if ( iopt == -1 or iopt == 0 ):
      print ( '  Value = %g' % ( val ) )

  return

def r8poly_t2p ( n, a1, x ):

#*****************************************************************************80
#
## r8poly_t2p() converts a real polynomial from Taylor form to power sum form.
#
#  Discussion:
#
#    The Taylor form of a polynomial based at X0 is
#
#      p(x) =   a(1)
#             + a(2) * (x-x0)
#             + a(3) * (x-x0)^2
#             ...
#             + a(n) * (x-x0)^(n-1)
#
#    The power sum form is
#
#      p(x) = a(1) + a(2)*x + a(3)*x^2 + ... + a(n)*x^(n-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of A.
#
#    real A1(N), the coefficients in Taylor form.
#
#    real X, the point at which the Taylor form polynomial is based.
#
#  Output:
#
#    real A2(N), the coefficients in power sum form.
#
  import numpy as np

  a2 = np.zeros ( n )

  for i in range ( 0, n ):
    a2[i] = a1[i]

  for i in range ( n - 1, -1, -1 ):
    for j in range ( i, n - 1 ):
      a2[j] = a2[j] - a2[j+1] * x

  return a2

def r8poly_t2p_test ( ):

#*****************************************************************************80
#
## r8poly_t2p_test() tests r8poly_t2p().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 4
  a = r8vec_indicator1 ( n )
  x = 2.0

  print ( '' )
  print ( 'r8poly_t2p_test():' )
  print ( '  r8poly_t2p(): Taylor => Power sum' )
  print ( '' )
  print ( '  Taylor expansion point is X = %g' % ( x ) )

  r8vec_print ( n, a, '  The Taylor coefficients:' )

  a2 = r8poly_t2p ( n, a, x )

  r8poly_print ( n-1, a2, '  The power sum polynomial:' )

  a3 = r8poly_p2t ( n, a2, x )
 
  r8vec_print ( n, a3, '  The recovered Taylor coefficients:' )

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
  import platform

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
#    integer N_dATA.  The user sets N_dATA to 0 before the first call.
#
#  Output:
#
#    integer N_dATA.  On each call, the routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
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
  import platform

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

def r8_to_cfrac ( r, n ):

#*****************************************************************************80
#
## r8_to_cfrac() converts an R8 to a continued fraction.
#
#  Discussion:
#
#    The routine is given a real number R.  It computes a sequence of
#    continued fraction approximations to R, returning the results as
#    simple fractions of the form P(I) / Q(I).
#
#  Example:
#
#    X = 2 * PI
#    N = 7
#
#    A = [ *, 6,  3,  1,  1,   7,   2,    146,      3 ]
#    P = [ 1, 6, 19, 25, 44, 333, 710, 103993, 312689 ]
#    Q = [ 0, 1,  3,  4,  7,  53, 113,  16551,  49766 ]
#
#    (This ignores roundoff error, which will cause later terms to differ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Norman Richert,
#    Strang's Strange Figures,
#    American Mathematical Monthly,
#    Volume 99, Number 2, February 1992, pages 101-107.
#
#  Input:
#
#    real R, the real value.
#
#    integer N, the number of convergents to compute.
#
#  Output:
#
#    integer A(1:N+1), the partial quotients.
#
#    integer P(1:N+2), Q(1:N+2), the numerators and denominators
#    of the continued fraction approximations.
#
  import numpy as np

  a = np.zeros ( n + 1, dtype = np.int32 )
  p = np.zeros ( n + 2, dtype = np.int32 )
  q = np.zeros ( n + 2, dtype = np.int32 )
  x = np.zeros ( n + 1, dtype = np.float64 )

  if ( r == 0.0 ):
    for i in range ( 0, n + 2 ):
      q[i] = 1
    return a, p, q

  p[0] = 1
  q[0] = 0

  p[1] = int ( abs ( r ) )
  q[1] = 1
  x[0] = abs ( r )
  a[0] = int ( x[0] )

  for i in range ( 1, n + 1 ):

    if ( ( x[i-1] - a[i-1] ) == 0.0 ):
      break

    x[i]   = 1.0 / ( x[i-1] - a[i-1] )
    a[i]   = int ( x[i] )
    p[i+1] = a[i] * p[i] + p[i-1]
    q[i+1] = a[i] * q[i] + q[i-1]

  if ( r < 0.0 ):
    for i in range ( 0, n + 2 ):
      p[i] = - p[i]

  return a, p, q

def r8_to_cfrac_test ( ):

#*****************************************************************************80
#
## r8_to_cfrac_test() tests r8_to_cfrac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7

  print ( '' )
  print ( 'r8_to_cfrac_test():' )
  print ( '  r8_to_cfrac() converts a real number to a sequence' )
  print ( '  of continued fraction convergents.' )

  r = 2.0 * np.pi

  print ( '' )
  print ( '  Use the real number R = %g' % ( r ) )

  a, p, q = r8_to_cfrac ( r, n )

  print ( '' )

  for i in range ( 0, n ):
    temp = float ( p[i+1] ) / float ( q[i+1] )
    print ( '  %6d  %6d  %6d  %12f  %12f' \
      % ( a[i], p[i+1], q[i+1], temp, r - temp ) )

  return

def r8_to_dec ( dval, dec_digit ):

#*****************************************************************************80
#
## r8_to_dec() converts a double precision quantity to a decimal representation.
#
#  Discussion:
#
#    Given the double precision value DVAL, the routine computes integers
#    MANTISSA and EXPONENT so that it is approximately true that:
#
#      DVAL = MANTISSA * 10 ^ EXPONENT
#
#    In particular, only dec_digit digits of DVAL are used in constructing the
#    representation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    double precision DVAL, the value whose decimal representation
#    is desired.
#
#    integer dec_digit, the number of decimal digits.
#
#  Output:
#
#    integer MANTISSA, EXPONENT, the approximate decimal 
#    representation of DVAL.
#

#
#  Special cases.
#
  if ( dval == 0.0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent
#
#  Factor DVAL = MANTISSA_dOUBLE * 10^EXPONENT
#
  mantissa_double = dval
  exponent = 0
#
#  Now normalize so that 
#  10^(dec_digit-1) <= ABS(MANTISSA_dOUBLE) < 10^(dec_digit)
#
  ten1 = 10.0 ** ( dec_digit - 1 )
  ten2 = 10.0 ** dec_digit

  while ( abs ( mantissa_double ) < ten1 ):
    mantissa_double = mantissa_double * 10.0
    exponent = exponent - 1

  while ( ten2 <= abs ( mantissa_double ) ):
    mantissa_double = mantissa_double / 10.0
    exponent = exponent + 1
#
#  MANTISSA is the integer part of MANTISSA_dOUBLE, rounded.
#
  mantissa = int ( mantissa_double )
#
#  Now divide out any factors of ten from MANTISSA.
#
  if ( mantissa != 0 ):
    while ( 10 * ( mantissa // 10 ) == mantissa ):
      mantissa = ( mantissa // 10 )
      exponent = exponent + 1

  return mantissa, exponent

def r8_to_dec_test ( rng ):

#*****************************************************************************80
#
## r8_to_dec() tests r8_to_dec().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_to_dec_test():' )
  print ( '  r8_to_dec() converts a real number to a decimal' )

  dec_digit = 5

  print ( '' )
  print ( '  The number of decimal digits is %d' % ( dec_digit ) )

  r8_lo = -10.0
  r8_hi = +10.0

  print ( '' )
  print ( '     R   =>  A * 10^B  =>  R2' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    a, b = r8_to_dec ( r, dec_digit )
    r2 = dec_to_r8 ( a, b )
    print ( '  %10.6f  %6d  %6d  %10.6f' % ( r, a, b, r2 ) )

  return

def r8_to_rat ( r, ndig ):

#*****************************************************************************80
#
## r8_to_rat() converts a real value to a rational value.
#
#  Discussion:
#
#    The rational value (IATOP/IABOT) is essentially computed by truncating
#    the decimal representation of the real value after a given number of
#    decimal digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the real value to be converted.
#
#    integer NDIG, the number of decimal digits used.
#
#  Output:
#
#    integer IATOP, IABOT, the numerator and denominator
#    of the rational value that approximates the real number.
#
  factor = 10 ** ndig

  if ( 0 < ndig ):
    ifac = 10 ** ndig
    jfac = 1
  else:
    ifac = 1
    jfac = 10 ** ( - ndig )

  itop = int ( round ( r * factor ) * jfac )
  ibot = ifac
#
#  Factor out the greatest common factor.
#
  itemp = i4_gcd ( itop, ibot )

  iatop = ( itop // itemp )
  iabot = ( ibot // itemp )

  return iatop, iabot

def r8_to_rat_test ( rng ):

#*****************************************************************************80
#
## r8_to_rat_test() tests r8_to_rat().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  ndig = 4

  print ( '' )
  print ( 'r8_to_rat_test():' )
  print ( '  r8_to_rat() converts a real number to a rational' )
  print ( '' )
  print ( '  The maximum number of digits allowed is %d' % ( ndig ) )

  print ( '' )
  print ( '     R   =>  A / B  =>  R2' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = rng.random ( )
    r = 10.0 * ( r - 0.25 )
    a, b = r8_to_rat ( r, ndig )
    r2 = rat_to_r8 ( a, b )
    print ( '  %10g  %6d  %6d  %10g' % ( r, a, b, r2 ) )

  return

def r8vec_backtrack ( n, maxstack, x, indx, k, nstack, stacks, ncan ):

#*****************************************************************************80
#
## r8vec_backtrack() supervises a backtrack search for a vector.
#
#  Discussion:
#
#    The routine tries to construct a vector one index at a time,
#    using possible candidates as supplied by the user.
#
#    At any time, the partially constructed vector may be discovered to be
#    unsatisfactory, but the routine records information about where the
#    last arbitrary choice was made, so that the search can be
#    carried out efficiently, rather than starting out all over again.
#
#    First, call the routine with INDX = 0 so it can initialize itself.
#
#    Now, on each return from the routine, if INDX is:
#      1, you've just been handed a complete candidate vector
#         Admire it, analyze it, do what you like.
#      2, please determine suitable candidates for position X(K).
#         Return the number of candidates in NCAN(K), adding each
#         candidate to the end of STACKS, and increasing NSTACK.
#      3, you're done.  Stop calling the routine
#
#    At one time, the variable "stacks" was called "stack", but MATLAB
#    now seems to have taken "stack" as a keyword that is no longer
#    acceptable as a variable name.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
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
#    integer N, the number of positions to be filled in the vector.
#
#    integer MAXSTACK, the maximum length of the stack.
#
#    real X(N), the partially filled in candidate vector.
#
#    integer INDX, a communication flag.
#    * 0, to begin a backtracking search.
#    * 2, the requested candidates for position K have been added to
#      STACKS, and NCAN(K) was updated.
#
#    integer K, the index in X that we are trying to fill.
#
#    integer NSTACK, the current length of the stack.
#
#    real STACKS(MAXSTACK), a list of all current candidates for
#    all positions 1 through K.
#
#    integer NCAN(N), lists the current number of candidates for
#    all positions 1 through K.
#
#  Output:
#
#    real X(N), the partially filled in candidate vector.
#
#    integer INDX, a communication flag.
#    * 1, a complete output vector has been determined and returned in X(1:N)
#    * 2, candidates are needed for position X(K)
#    * 3, no more possible vectors exist.
#
#    integer K, the index in X that we are trying to fill.
#
#    integer NSTACK, the current length of the stack.
#
#    real STACKS(MAXSTACK), a list of all current candidates for
#    all positions 1 through K.
#
#    integer NCAN(N), lists the current number of candidates for
#    all positions 1 through K.
#

#
#  If this is the first call, request a candidate for position 1.
#
  if ( indx == 0 ):
    k = 1
    nstack = 0
    indx = 2
    return x, indx, k, nstack, stacks, ncan
#
#  Examine the stack.
#
  while ( True ):
#
#  If there are candidates for position K, take the first available
#  one off the stack, and increment K.
#
#  This may cause K to reach the desired value of N, in which case
#  we need to signal the user that a complete set of candidates
#  is being returned.
#
    if ( 0 < ncan[k-1] ):
      x[k-1] = stacks[nstack-1]
      nstack = nstack - 1

      ncan[k-1] = ncan[k-1] - 1

      if ( k != n ):
        k = k + 1
        indx = 2
      else:
        indx = 1

      break
#
#  If there are no candidates for position K, then decrement K.
#  If K is still positive, repeat the examination of the stack.
#
    else:

      k = k - 1

      if ( k <= 0 ):
        indx = 3
        break

  return x, indx, k, nstack, stacks, ncan

def r8vec_backtrack_test ( ):

#*****************************************************************************80
#
## r8vec_backtrack_test() tests r8vec_backtrack().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_backtrack_test():' )
  print ( '  r8vec_backtrack() uses backtracking, seeking a vector X of' )
  print ( '  N values which satisfies some condition.' )

  print ( '' )
  print ( '  In this demonstration, we have 8 values W(I).' )
  print ( '  We seek all subsets that sum to 53.0.' )
  print ( '  X(I) is 0.0 or 1.0 if the entry is skipped or used.' )
  print ( '' )

  n = 8
  maxstack = 100
  stacks = np.zeros ( maxstack )
  x = np.zeros ( n )
  indx = 0
  k = 1
  nstack = 0
  ncan = np.zeros ( n )

  w = np.array ( [ 15.0, 22.0, 14.0, 26.0, 32.0, 9.0, 16.0, 8.0 ] )
  t = 53.0

  found_num = 0

  while ( True ):

    x, indx, k, nstack, stacks, ncan = r8vec_backtrack ( n, maxstack, \
    x, indx, k, nstack, stacks, ncan )

    if ( indx == 1 ):

      found_num = found_num + 1
      print ( '  %2d   ' % ( found_num ), end = '' )

      total = 0
      for i in range ( 0, n ):
        if ( x[i] == 1.0 ):
          total = total + w[i]
      print ( '  %g:  ' % ( total ), end = '' )

      for i in range ( 0, n ):
        if ( x[i] == 1.0 ):
          print ( '  %g' % ( w[i] ), end = '' )
      print ( '' )
#
#  Given that we've chose X(1:K-1), what are our choices for X(K)?
#
#    if T < TOTAL, 
#      no choices
#    if T = TOTAL, 
#      X(K) = 0
#    if T > TOTAL and K < N, 
#      X(k) = 0
#      If ( W(K)+TOTAL <= T ) X(K) = 1
#    If T > TOTAL and K = N,
#      If ( W(K) + TOTAL) = T ) X(K) = 1
#
    elif ( indx == 2 ):

      total = 0.0
      for i in range ( 0, k - 1 ):
        if ( x[i] == 1.0 ):
          total = total + w[i]

      if ( t < total ):

        ncan[k-1] = 0

      elif ( t == total ):

        ncan[k-1] = ncan[k-1] + 1
        nstack = nstack + 1
        stacks[nstack-1] = 0.0

      elif ( total < t and k < n ):

        ncan[k-1] = ncan[k-1] + 1
        nstack = nstack + 1
        stacks[nstack-1] = 0.0

        if ( total + w[k-1] <= t ):
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1.0

      elif ( total < t and k == n ):

        if ( total + w[k-1] == t ):
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1.0

    else:

      print ( '' )
      print ( '  Done!' )
      break

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
    print ( 'r8vec_frac(): Fatal error!' )
    print ( '  Illegal nonpositive value of N = %d' % ( n ) )
    raise Exception ( 'r8vec_frac(): Fatal error!' )

  if ( k <= 0 ):
    print ( '' )
    print ( 'r8vec_frac(): Fatal error!' )
    print ( '  Illegal nonpositive value of K = %d' % ( k ) )
    raise Exception ( 'r8vec_frac(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'r8vec_frac(): Fatal error!' )
    print ( '  Illegal N < K, K = %d' % ( k ) )
    raise Exception ( 'r8vec_frac(): Fatal error!' )

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
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  ahi = 10.0
  alo = 0.0

  print ( '' )
  print ( 'r8vec_frac_test():' )
  print ( '  r8vec_frac(): K-th smallest real vector entry;' )

  a = alo + ( ahi - alo ) * rng.random ( n )

  r8vec_print ( n, a, '  The real array to search: ' )

  print ( '' )
  print ( 'Frac   r8vec_frac' )
  print ( '' )

  for k in range ( 1, n + 1 ):

    afrac = r8vec_frac ( n, a, k )
    print ( '  %2d  %6f' % ( k, afrac ) )

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
  import numpy

  a = numpy.zeros ( n );

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
  import platform
 
  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

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
#    will nonethess stop when it reaches the value of A in which
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
  import platform

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

def rat_add ( top1, bot1, top2, bot2 ):

#*****************************************************************************80
#
## rat_add() adds two rational values.
#
#  Discussion:
#
#    The routine computes
#
#      TOP/BOT = TOP1/BOT1 + TOP2/BOT2
#
#    while trying to avoid integer overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TOP1, BOT1, the first value to add.
#
#    integer TOP2, BOT2, the second value to add.
#
#  Output:
#
#    integer TOP, BOT, the sum.
#
#    integer IERROR.
#    0, no error occurred.
#    1, an error occurred.  The addition of the two values
#    requires a numerator or denominator larger than the
#    maximum legal integer.
#
  i_max = i4_huge ( )

  ierror = 0

  if ( top1 == 0 ):
    top = top2
    bot = bot2
    return top, bot, ierror
  elif ( top2 == 0 ):
    top = top1
    bot = bot1
    return top, bot, ierror
#
#  Compute the greatest common factor of the two denominators,
#  and factor it out.
#
  bot3 = i4_gcd ( bot1, bot2 )
  bot1 = bot1 // bot3
  bot2 = bot2 // bot3
#
#  The fraction may now be formally written as:
#
#    (top1*bot2 + top2*bot1) / (bot1*bot2*bot3)
#
#  Check the tops for overflow.
#
  if ( i_max < abs ( top1 * bot2 ) ):
    print ( '' )
    print ( 'rat_add - Warning!' )
    print ( '  Overflow of top of rational sum.' )
    top = 0
    bot = 1
    ierror = 1
    return top, bot, ierror

  top1 = top1 * bot2

  if ( i_max < abs ( top2 * bot1 ) ):
    ierror = 1
    print ( '' )
    print ( 'rat_add(): Fatal error!' )
    print ( '  Overflow of top of rational sum.' )
    top = 0
    bot = 1
    ierror = 1
    return top, bot, ierror

  top2 = top2 * bot1

  if ( i_max < abs ( top1 + top2 ) ):
    print ( '' )
    print ( 'rat_add(): Fatal error!' )
    print ( '  Overflow of top of rational sum.' )
    top = 0
    bot = 1
    return top, bot, ierror

  top = top1 + top2
#
#  Check the bottom for overflow.
#
  if ( i_max < abs ( bot1 * bot2 * bot3 ) ):
    print ( '' )
    print ( 'rat_add(): Fatal error!' )
    print ( '  Overflow of bottom of rational sum.' )
    top = 0
    bot = 1
    ierror = 1
    return top, bot, ierror

  bot = bot1 * bot2 * bot3
#
#  Put the fraction in lowest terms.
#
  itemp = i4_gcd ( top, bot )
  top = top // itemp
  bot = bot // itemp
#
#  The bottom should be positive.
#
  if ( bot < 0 ):
    bot = -bot
    top = -top

  return top, bot, ierror

def rat_add_test ( ):

#*****************************************************************************80
#
## rat_add_test() tests rat_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rat_add_test():' )
  print ( '  rat_add() adds two rationals.' )

  atop = 3
  abot = 4
  btop = 10
  bbot = 7

  ctop, cbot, ierror = rat_add ( atop, abot, btop, bbot )

  print ( '' )
  s = rat_to_s ( atop, abot )
  print ( '  A = %s' % ( s ) )
  s = rat_to_s ( btop, bbot )
  print ( '  B = %s' % ( s ) )
  s = rat_to_s ( ctop, cbot )
  print ( '  C = A + B = %s' % ( s ) )

  return

def rat_div ( top1, bot1, top2, bot2 ):

#*****************************************************************************80
#
## rat_div() divides one rational value by another.
#
#  Discussion:
#
#    The routine computes
#
#      TOP / BOT = ( TOP1 / BOT1 ) / ( TOP2 / BOT2 ).
#
#    while avoiding integer overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TOP1, BOT1, the numerator.
#
#    integer TOP2, BOT2, the denominator.
#
#  Output:
#
#    integer TOP, BOT, the result.
#
#    integer IERROR.
#    0, no error occurred.
#    1, an error occurred.  One of the quantities BOT1, BOT2,
#    or TOP2 is zero, or the result of the division
#    requires a numerator or denominator larger than the
#    maximum legal integer.
#
  ierror = 0
  top = 0
  bot = 1

  i_max = i4_huge ( )

  if ( bot1 == 0 or top2 == 0 or bot2 == 0 ):
    ierror = 1
    return top, bot, ierror

  if ( top1 == 0 ):
    top = 0
    bot = 1
    return top, bot, ierror
#
#  Implicitly invert the divisor fraction here.  The rest of
#  the code will be a multiply operation.
#
  jbot1 = bot1
  jbot2 = top2
  jtop1 = top1
  jtop2 = bot2
#
#  Get rid of all common factors in top and bottom.
#
  itemp = i4_gcd ( jtop1, jbot1 )
  jtop1 = jtop1 // itemp
  jbot1 = jbot1 // itemp
  itemp = i4_gcd ( jtop1, jbot2 )
  jtop1 = jtop1 // itemp
  jbot2 = jbot2 // itemp
  itemp = i4_gcd ( jtop2, jbot1 )
  jtop2 = jtop2 // itemp
  jbot1 = jbot1 // itemp
  itemp = i4_gcd ( jtop2, jbot2 )
  jtop2 = jtop2 // itemp
  jbot2 = jbot2 // itemp
#
#  The fraction (TOP1*BOT2)/(BOT1*TOP2) is in lowest terms.
#
#  Check the top for overflow.
#
  if ( i_max < abs ( jtop1 * jtop2 ) ):
    print ( '' )
    print ( 'rat_div - Warning!' )
    print ( '  Overflow of top of rational fraction.' )
    top = 0
    bot = 1
    ierror = 1
    return top, bot, ierror

  top = jtop1 * jtop2
#
#  Check the bottom BOT1*TOP2 for overflow.
#
  if ( i_max < abs ( jbot1 * jbot2 ) ):
    print ( '' )
    print ( 'rat_div(): Fatal error!' )
    print ( '  Overflow of bottom of rational fraction.' )
    top = 0
    bot = 1
    ierror = 1
    return top, bot, ierror

  bot = jbot1 * jbot2
#
#  The bottom should be positive.
#
  if ( bot < 0 ):
    bot = -bot
    top = -top

  return top, bot, ierror

def rat_div_test ( ):

#*****************************************************************************80
#
## rat_div_test() tests rat_div().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rat_div_test():' )
  print ( '  rat_div() divides two rationals.' )

  atop = 3
  abot = 4
  btop = 10
  bbot = 7

  ctop, cbot, ierror = rat_div ( atop, abot, btop, bbot )

  print ( '' )
  s = rat_to_s ( atop, abot )
  print ( '  A = %s' % ( s ) )
  s = rat_to_s ( btop, bbot )
  print ( '  B = %s' % ( s ) )
  s = rat_to_s ( ctop, cbot )
  print ( '  C = A / B = %s' % ( s ) )

  return

def rat_farey2 ( n, a, b ):

#*****************************************************************************80
#
## rat_farey2() computes the next row of the Farey fraction table.
#
#  Example:
#
#    Input:
#
#      N = 3
#      A =  0  1  1  2  1
#      B =  1  3  2  3  1
#
#    Output:
#
#      A =  0  1  1  2  1  3  2  3  1
#      B =  1  4  3  5  2  5  3  4  1
#
#  Discussion:
#
#    In this form of the Farey fraction table, fractions in row N lie between
#    0 and 1, and are in lowest terms.  For every adjacent pair of input
#    fractions, A1/B1 and A2/B2, the mediant (A1+A2)/(B1+B2) is computed
#    and inserted between them.
#
#    The number of items in the N-th row is 1+2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the input row number.  N must be nonnegative.
#    If N is zero, then the input values A and B are ignored, and the entries of
#    row 1 are computed directly.
#
#    integer A(1+2^(N-1)), B(1+2^(N-1)),the entries of row N.
#
#  Output:
#
#    integer A2(1+2^N), B2(1+2^N), the entries of row N+1.
#
  import numpy as np

  a2 = np.zeros ( 1 + 2 ** n )
  b2 = np.zeros ( 1 + 2 ** n )

  if ( n == 0 ):

    a2[0] = 0
    a2[1] = 1
    b2[0] = 1
    b2[1] = 1

  else:
#
#  Shift the current data.
#
    for i in range ( 2 ** ( n - 1 ), -1, -1 ):
      a2[2*i] = a[i]
      b2[2*i] = b[i]
#
#  Compute the mediants.
#
    for i in range ( 1, 2 ** n, 2 ):
      a2[i] = a2[i-1] + a2[i+1]
      b2[i] = b2[i-1] + b2[i+1]

  return a2, b2

def rat_farey2_test ( ):

#*****************************************************************************80
#
## rat_farey2_test() tests rat_farey2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  max_n = 4
  
  print ( '' )
  print ( 'rat_farey2_test():' )
  print ( '  rat_farey2() computes a row of the Farey fraction table.' )

  n = 0
  a = np.zeros ( n )
  b = np.zeros ( n )
  
  for n in range ( 0, 5 ):

    a, b = rat_farey2 ( n, a, b )
    num_frac = 2 ** n + 1

    print ( '' )
    print ( '  Row %d' % ( n ) )
    print ( '  Number of fractions: %d' % ( num_frac ) )

    for i in range ( 0, num_frac ):
      print ( '  %d/%d' % ( a[i], b[i] ), end = '' )
      if ( ( ( i + 1 ) % 10 == 0 ) or i == num_frac - 1 ):
        print ( '' )

  return

def rat_farey ( n, max_frac ):

#*****************************************************************************80
#
## rat_farey() computes the N-th row of the Farey fraction table.
#
#  Example:
#
#    N = 5
#
#    NUM_frac = 11
#    A =  0  1  1  1  2  1  3  2  3  4  1
#    B =  1  5  4  3  5  2  5  3  4  5  1
#
#  Discussion:
#
#    In this form of the Farey fraction table, fractions in row N lie between
#    0 and 1, are in lowest terms, and have a denominator that is no greater
#    than N.  Row N is computed directly, and does not require the computation
#    of previous rows.
#
#    The data satisfy the relationship:
#
#      A(K+1) * B(K) - A(K) * B(K+1) = 1
#
#    The number of items in the N-th row is roughly N^2 / PI^2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, page 157.
#
#  Input:
#
#    integer N, the desired row number.  N must be positive.
#
#    integer MAX_frac, the maximum number of fractions to compute.
#
#  Output:
#
#    integer A(NUM_frac), B(NUM_frac), contains the
#    numerators and denominators of the N-th row of the Farey fraction table.
#
#    integer NUM_frac, the number of fractions computed.
#
  import numpy as np

  a = np.zeros ( max_frac )
  b = np.zeros ( max_frac )

  if ( max_frac <= 0 ):
    num_frac = 0
    return a, b, num_frac

  if ( n <= 0 ):
    num_frac = 0
    return a, b, num_frac

  k = 0
  a[k] = 0
  b[k] = 1

  if ( max_frac <= k + 1 ):
    num_frac = k + 1
    return a, b, num_frac

  k = 1
  a[k] = 1
  b[k] = n

  while ( k + 1 < max_frac ):

    if ( a[k] == 1 and b[k] == 1 ):
      break

    k = k + 1
    c = ( ( b[k-2] + n ) // b[k-1] )
    a[k] = c * a[k-1] - a[k-2]
    b[k] = c * b[k-1] - b[k-2]

  num_frac = k + 1

  return a, b, num_frac

def rat_farey_test ( ):

#*****************************************************************************80
#
## rat_farey_test() tests rat_farey().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  max_frac = 20

  print ( '' )
  print ( 'rat_farey_test():' )
  print ( '  rat_farey() computes a row of the Farey fraction table.' )

  for n in range ( 1, 8 ):

    a, b, num_frac = rat_farey ( n, max_frac )
 
    print ( '' )
    print ( '  Row %d' % ( n ) )
    print ( '  Number of fractions: %d' % ( num_frac ) )

    for i in range ( 0, num_frac ):
      print ( '  %d/%d' % ( a[i], b[i] ), end = '' )
      if ( ( ( i + 1 ) % 10 == 0 ) or i == num_frac - 1 ):
        print ( '' )

  return

def rat_mul ( top1, bot1, top2, bot2 ):

#*****************************************************************************80
#
## rat_mul() multiplies two fractions.
#
#  Discussion:
#
#    The routine computes
#
#      TOP / BOT = ( TOP1 / BOT1 ) * ( TOP2 / BOT2 ).
#
#    while avoiding integer overflow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TOP1, BOT1, the first factor.
#
#    integer TOP2, BOT2, the second factor.
#
#  Output:
#
#    integer TOP, BOT, the product.
#
  i_max = i4_huge ( )

  if ( top1 == 0 or top2 == 0 ):
    top = 0
    bot = 1
    return top, bot
#
#  Get rid of all common factors in top and bottom.
#
  temp = i4_gcd ( top1, bot1 )
  top1 = top1 // temp
  bot1 = bot1 // temp
  temp = i4_gcd ( top1, bot2 )
  top1 = top1 // temp
  bot2 = bot2 // temp
  temp = i4_gcd ( top2, bot1 )
  top2 = top2 // temp
  bot1 = bot1 // temp
  temp = i4_gcd ( top2, bot2 )
  top2 = top2 // temp
  bot2 = bot2 // temp
#
#  The fraction (TOP1*TOP2)/(BOT1*BOT2) is in lowest terms.
#
#  Check the top TOP1*TOP2 for overflow.
#
  if ( i_max < abs ( top1 * top2 ) ):
    print ( '' )
    print ( 'rat_mul(): Fatal error!' )
    print ( '  Overflow of top of rational product.' )
    raise Exception ( 'rat_mul(): Fatal error!' )

  top = top1 * top2
#
#  Check the bottom BOT1*BOT2 for overflow.
#
  if ( i_max < abs ( bot1 * bot2 ) ):
    print ( '' )
    print ( 'rat_mul(): Fatal error!' )
    print ( '  Overflow of bottom of rational product.' )
    raise Exception ( 'rat_mul(): Fatal error!' )

  bot = bot1 * bot2
#
#  The bottom should be positive.
#
  if ( bot < 0 ):
    bot = -bot
    top = -top

  return top, bot

def rat_mul_test ( ):

#*****************************************************************************80
#
## rat_mul_test() tests rat_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rat_mul_test():' )
  print ( '  rat_mul() multiplies two rationals.' )

  atop = 3
  abot = 4
  btop = 10
  bbot = 7

  ctop, cbot = rat_mul ( atop, abot, btop, bbot )

  print ( '' )
  s = rat_to_s ( atop, abot )
  print ( '  A = %s' % ( s ) )
  s = rat_to_s ( btop, bbot )
  print ( '  B = %s' % ( s ) )
  s = rat_to_s ( ctop, cbot )
  print ( '  C = A * B = %s' % ( s ) )

  return

def rat_normalize ( a, b ):

#*****************************************************************************80
#
## rat_normalize() normalizes a rational number.
#
#  Discussion:
#
#    If A = B = 0, return.
#
#    If A = 0 (and B nonzero) set B => 1 and return.
#
#    If A nonzero, and B = 0, then A => 1 and return.
#
#    If A = B, then set A => 1, B => 1 and return.
#
#    If B < 0, then A => -A, B => -B.
#
#    If 1 < C = GCD(|A|,|B|), A => A/C, B => B/C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the rational number.
#
#  Output:
#
#    integer A, B, the normalized rational number.
#

#
#  Cases where one or both is 0.
#
  if ( a == 0 and b == 0 ):
    return a, b
  elif ( a == 0 and b != 0 ):
    b = 1
    return a, b
  elif ( a != 0 and b == 0 ):
    a = 1
    return a, b

  if ( a == b ):
    a = 1
    b = 1
    return a, b

  if ( b < 0 ):
    a = -a
    b = -b

  c = i4_gcd ( abs ( a ), abs ( b ) )

  if ( 1 < c ):
    a = a // c
    b = b // c

  return a, b

def rat_normalize_test ( ):

#*****************************************************************************80
#
## rat_normalize_test() tests rat_normalize().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rat_normalize_test():' )
  print ( '  rat_normalize() normalizes a rational.' )

  rat_num = 7
  rat_top = np.array ( [ 3, 1,    20,  8, -10,   9, -11 ] )
  rat_bot = np.array ( [ 4, 1000,  1,  4,   7, -15, -11 ] )

  print ( '' )
  print ( '           A           B             A             B' )
  print ( '                                 normalized     normalized' )
  print ( '' )

  for i in range ( 0, rat_num ):
    a1 = rat_top[i]
    b1 = rat_bot[i]
    a2, b2 = rat_normalize ( a1, b1 )
    print ( '  %10d  %10d    %10d  %10d' % ( a1, b1, a2, b2 ) )

  return

def rat_to_cfrac ( p, q ):

#*****************************************************************************80
#
## rat_to_cfrac() converts a rational value to a continued fraction.
#
#  Discussion:
#
#    The routine is given a rational number represented by P/Q, and
#    computes the monic or "simple" continued fraction representation
#    with integer coefficients of the number:
#
#      A(1) + 1/ (A(2) + 1/ (A(3) + ... + 1/A(N) ...))
#
#    The user must dimension A to a value M which is "large enough".
#    The actual number of terms needed in the continued fraction
#    representation cannot be known beforehand.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 August 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Input:
#
#    integer P, Q, the numerator and denominator of the
#    rational value whose continued fraction representation is
#    desired.
#
#  Output:
#
#    integer N, the number of entries in A.
#
#    integer A(N), contains the continued fraction
#    representation of the number.
#
  import numpy as np

  b = []

  n = 0

  while ( True ):

    b.append ( p // q )
    n = n + 1
    p = ( p % q )

    if ( p == 0 ):
      break

    b.append ( q // p )
    n = n + 1
    q = ( q % p )

    if ( q == 0 ):
      break

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = b[i]

  return n, a

def rat_to_cfrac_test ( ):

#*****************************************************************************80
#
## rat_to_cfrac_test() tests rat_to_cfrac().
#
#  Discussion:
#
#    Compute the continued fraction form of 4096/15625.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 10

  print ( '' )
  print ( 'rat_to_cfrac_test():' )
  print ( '  rat_to_cfrac() fraction => continued fraction,' )
  print ( '' )

  top = 4096
  bot = 15625

  print ( '  Regular fraction is %6d / %6d' % ( top, bot ) )
 
  n, a = rat_to_cfrac ( top, bot )
 
  i4vec_print ( n, a, '  Continued fraction coefficients:' )

  p, q = cfrac_to_rat ( n, a )
 
  print ( '' )
  print ( '  The continued fraction convergents.' )
  print ( '  The last row contains the value of the continued' )
  print ( '  fraction, written as a common fraction.' )
  print ( '' )
  print ( '  I, P(I), Q(I), P(I)/Q(I)' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %3d  %6d  %6d  %14f' % ( i, p[i], q[i], p[i] / q[i] ) )

  return

def rat_to_dec ( top, bot ):

#*****************************************************************************80
#
## rat_to_dec() converts a rational to a decimal representation.
#
#  Discussion:
#
#    A rational value is represented by TOP / BOT.
#
#    A decimal value is represented as MANTISSA * 10^EXPONENT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TOP, BOT, the rational value.
#
#  Output:
#
#    integer MANTISSA, EXPONENT, the decimal number.
#
  if ( top == 0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent

  gcd = i4_gcd ( top, bot )
  top = ( top // gcd )
  bot = ( bot // gcd )

  if ( bot < 0 ):
    top = -top
    bot = -bot

  if ( bot == 1 ):
    mantissa = top
    exponent = 0
    return mantissa, exponent

  exponent = 0

  while ( ( bot % 10 ) == 0 ):
    exponent = exponent - 1
    bot = ( bot // 10 )

  while ( ( top % 10 ) == 0 ):
    exponent = exponent + 1
    top = ( top // 10 )

  r = float ( top ) / float ( bot )

  if ( r < 0.0 ):
    s = -1
    r = -r
  else:
    s = 1

  while ( r != round ( r ) ):
    r = r * 10.0
    exponent = exponent - 1

  mantissa = s * r

  return mantissa, exponent

def rat_to_dec_test ( rng ):

#*****************************************************************************80
#
## rat_to_dec_test() tests rat_to_dec().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'rat_to_dec_test():' )
  print ( '  rat_to_dec() fraction => decimal,' )
  print ( '' )
  print ( '  In this test, choose the top and bottom' )
  print ( '  of a rational at random, and compute the' )
  print ( '  equivalent real number.' )
  print ( '' )
  print ( '  Then convert to decimal, and the equivalent real.' )
  print ( '' )
  print ( '  Then convert back to rational and the equivalent real.' )
  
  for i in range ( 0, 10 ):

    rat_top = rng.integers ( low = -1000, high = 1000, endpoint = True )
    rat_bot = rng.integers ( low = 1, high = 1000, endpoint = True )

    r1 = float ( rat_top ) / float ( rat_bot )
    mantissa, exponent = rat_to_dec ( rat_top, rat_bot )
    r2 = float ( mantissa ) * 10.0 ** exponent
    rat_top2, rat_bot2 = dec_to_rat ( mantissa, exponent )
    r3 = float ( rat_top2 ) / float ( rat_bot2 )

    print ( '' )
    print ( '  %g = %d / %d' % ( r1, rat_top, rat_bot ) )
    print ( '  %g = %d * 10^%d' % ( r2, mantissa, exponent ) )
    print ( '  %g = %d / %d' % ( r1, rat_top2, rat_bot2 ) )

  return

def rat_to_r8 ( a, b ):

#*****************************************************************************80
#
## rat_to_r8() converts rational values to real values.
#
#  Example:
#
#    A    B    R
#   --   --    ---
#    1    2    0.5
#    7    5    1.4
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the rational quantity to be converted.
#
#  Output:
#
#    real R, the value of the rational quantity as a real number.
#
  if ( b == 0 ):
    print ( '' )
    print ( 'rat_to_r8(): Fatal error!' )
    print ( '  The input fraction to be converted had a' )
    print ( '  zero denominator.' )
    raise Exception ( 'rat_to_r8(): Fatal error!' )

  r = a / b

  return r

def rat_to_r8_test ( rng ):

#*****************************************************************************80
#
## rat_to_r8_test() tests rat_to_r8().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  ndig = 4

  print ( '' )
  print ( 'rat_to_r8_test():' )
  print ( '  rat_to_r8() converts a rational to a real number.' )
  print ( '' )
  print ( '  The maximum number of digits allowed is %d' % ( ndig ) )

  print ( '' )
  print ( '     R   =>  A / B  =>  R2' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = rng.random ( )
    r = 10.0 * ( r - 0.25 )
    a, b = r8_to_rat ( r, ndig )
    r2 = rat_to_r8 ( a, b )
    print ( '  %10g  %6d  %6d  %10g' % ( r, a, b, r2 ) )

  return

def rat_to_s ( a, b ):

#*****************************************************************************80
#
## rat_to_s() returns a left-justified representation of A/B.
#
#  Discussion:
#
#    If the ratio is negative, a minus sign precedes A.
#    A slash separates A and B.
#
#    Note that if A is nonzero and B is 0, S will
#    be returned as "Inf" or "-Inf" (Infinity), and if both
#    A and B are zero, S will be returned as "NaN"
#    (Not-a-Number).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the numerator and denominator.
#
#  Output:
#
#    character S(*), a left-justified string
#    containing the representation of A/B.
#

#
#  Take care of simple cases right away.
#
  if ( a == 0 ):

    if ( b != 0 ):
      s = '0'
    else:
      s = 'NaN'

  elif ( b == 0 ):

    if ( 0 < a ):
      s = 'Inf'
    else:
      s = '-Inf'

  else:

    s = str ( a ) + '/' + str ( b )

  return s

def rat_to_s_test ( ):

#*****************************************************************************80
#
## rat_to_s_test() tests rat_to_s().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rat_to_s_test():' )
  print ( '  rat_to_s() converts a rational to a string.' )

  rat_num = 7
  rat_top = np.array ( [ 3, 1,    20,  8, -10,   9, -11 ] )
  rat_bot = np.array ( [ 4, 1000,  1,  4,   7, -15, -11 ] )

  print ( '' )
  print ( '           A           B    A/B' )
  print ( '' )

  for i in range ( 0, rat_num ):
    a = rat_top[i]
    b = rat_bot[i]
    s = rat_to_s ( a, b )
    print ( '  %10d  %10d    %s' % ( a, b, s ) )

  return

def rat_width ( a, b ):

#*****************************************************************************80
#
## rat_width() returns the "width" of a rational number.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the rational number.
#
#  Output:
#
#    integer WIDTH, the "width" of the rational number.
#
  width = 1
  ten_pow = 10

  if ( a == 0 ):
    return width
  
  abs_a = abs ( a )

  while ( ten_pow <= abs_a ):
    width = width + 1
    ten_pow = ten_pow * 10
#
#  If the fraction is negative, a minus sign will be prepended to the
#  numerator.
#
  if ( a * b < 0 ):
    width = width + 1
    ten_pow = ten_pow * 10

  abs_b = abs ( b )

  while ( ten_pow <= abs_b ):
    width = width + 1
    ten_pow = ten_pow * 10

  return width

def rat_width_test ( ):

#*****************************************************************************80
#
## rat_width_test() tests rat_width().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_test = 17

  a_test = np.array ( \
    [ 1000, 1000, 1000, 1000,  1000,    1,      -1, -10, -100, -1000, \
         1,   10,  100, 1000, 10000,   17, 4000000 ] )
  b_test = np.array ( \
    [    3,   40,  500, 6000, 70000,    1,     200, 200,  200,   200, \
      -200, -200, -200, -200,  -200, 3000, 4000000 ] )

  print ( '' )
  print ( 'rat_width_test():' )
  print ( '  rat_width() determines the "width" of a rational.' )
  print ( '' )
  print ( '       Top    Bottom   Width' )
  print ( '' )

  for i in range ( 0, n_test ):
    a = a_test[i]
    b = b_test[i]
    width = rat_width ( a, b )
    print ( '  %8d  %8d  %6d' % ( a, b, width ) )

  return

def regro_next ( n, v, vmax, done ):

#*****************************************************************************80
#
## regro_next() computes restricted growth functions one at a time.
#
#  Discussion:
#
#    A restricted growth function on N is a vector (V(1), ..., V(N) )
#    of values V(I) between 1 and N, satisfying the requirements:
#      V(1) = 1;
#      V(I) <= 1 + max ( V(1), V(2), ..., V(I-1) ).
#
#    The number of restricted growth functions on N is equal to
#    the Bell number B(N).
#
#    There is a bijection between restricted growth functions on N
#    and set partitions of N.
#
#  Example:
#
#    The 15 restricted growth functions for N = 4 are:
#
#    (1111), (1112), (1121), (1122), (1123),
#    (1211), (1212), (1213), (1221), (1222),
#    (1223), (1231), (1232), (1233), (1234).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986, page 19.
#
#  Input:
#
#    integer N, the number of components in the restricted
#    growth function.
#
#    integer V(N), the output value of V from the previous call.
#    This value is not needed on an initial call with DONE = TRUE.
#
#    integer VMAX(N), the output value of VMAX from the previous call.
#    This value is not needed on an initial call with DONE = TRUE.
#
#    bool DONE, should be set to TRUE on an initial call to begin
#    a sequence of computations.  On subsequent calls, it should be set to the
#    output value of DONE from the previous call.
#
#  Output:
#
#    integer V(N), the componentwise values of the next restricted
#    growth function.
#
#    integer VMAX(N), records the largest value that component V(I)
#    could take, given the values of components 1 through I-1.
#
#    bool DONE, will be FALSE if the routine has computed another
#    restricted growth function, or TRUE if all the restricted
#    growth functions have been returned.
#

#
#  First call:
#
  if ( done ):
 
    for i in range ( 0, n ):
      v[i] = 1

    vmax[0] = 1
    for i in range ( 1, n ):
      vmax[i] = 2

    done = False
#
#  Later calls.
#
  else:

    j = n - 1

    while ( True ):

      if ( j == 0 ):
        done = True
        return v, vmax, done

      if ( v[j] != vmax[j] ):
        break

      j = j - 1

    v[j] = v[j] + 1

    for i in range ( j + 1, n ):

      v[i] = 1

      if ( v[j] == vmax[j] ):
        vmax[i] = vmax[j] + 1
      else:
        vmax[i] = vmax[j]

  return v, vmax, done

def regro_next_test ( ):

#*****************************************************************************80
#
## regro_next_test() tests regro_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'regro_next_test():' )
  print ( '  regro_next() generates all restricted growth' )
  print ( '  functions.' )
  print ( '' )

  rank = 0

  n = 4
  v = np.zeros ( n )
  vmax = np.zeros ( n )
  done = True
 
  while ( True ):

    v, vmax, done = regro_next ( n, v, vmax, done )

    if ( done ):
      break

    rank = rank + 1
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( v[i] ), end = '' )
    print ( '' )

  return

def rfrac_to_cfrac ( m, p, q ):

#*****************************************************************************80
#
## rfrac_to_cfrac() converts a rational polynomial fraction to a continued fraction.
#
#  Discussion:
#
#    That is, it accepts
#
#      P(1) + P(2) * X + ... + P(M) * X^(M-1)
#      -------------------------------------------------------
#      Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
#
#    and returns the equivalent continued fraction:
#
#      1 / ( T(1) + X / ( T(2) + X / (...T(2*M-1) + X / ( T(2*M) ... )))
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Input:
#
#    integer M, defines the number of P coefficients,
#    and is one less than the number of Q coefficients, and one
#    half the number of T coefficients.
#
#    real P(M), Q(M+1), the coefficients defining the rational
#    polynomial fraction.
#
#  Output:
#
#    real T(2*M), the coefficients defining the continued fraction.
#
  import numpy as np

  a = np.zeros ( [ m + 1, 2 * m + 1 ] )
  t = np.zeros ( 2 * m )

  for i in range ( 0, m + 1 ):
    a[i,0] = q[i]

  for i in range ( 0, m ):
    a[i,1] = p[i]

  t[0] = a[0,0] / a[0,1]
  ta = a[m,0]

  for i in range ( 1, m + 1 ):
    a[m-i,2*i] = ta

  for k in range ( 1, 2 * m - 1 ):

    ihi = ( 2 * m - k ) // 2

    for i in range ( 1, ihi + 1 ):
      a[i-1,k+1] = a[i,k-1] - t[k-1] * a[i,k]

    if ( a[0,k+1] == 0.0 ):
      print ( '' )
      print ( 'rfrac_to_cfrac(): Fatal error!' )
      print ( '  A(1,K+2) is zero for K = %d' % ( k ) )
      raise Exception ( 'rfrac_to_cfrac(): Fatal error!' )

    t[k] = a[0,k] / a[0,k+1]

  t[2*m-1] = a[0,2*m-1] / a[0,2*m]

  return t

def rfrac_to_cfrac_test ( ):

#*****************************************************************************80
#
## rfrac_to_cfrac_test() tests rfrac_to_cfrac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  maxm = 10
  m = 3

  p = np.array ( [ 1.0, 1.0, 2.0 ] )
  q = np.array ( [ 1.0, 3.0, 1.0, 1.0 ] )

  print ( '' )
  print ( 'rfrac_to_cfrac_test():' )
  print ( '  rfrac_to_cfrac(): rational polynomial fraction to continued fraction.' )

  r8vec_print ( m, p, '  Rational polynomial numerator coefficients:' )
  r8vec_print ( m + 1, q, '  Rational polynomial numerator coefficients:' )
 
  h = rfrac_to_cfrac ( m, p, q )
 
  r8vec_print ( 2 * m, h, '  Continued fraction coefficients:' )

  g = np.ones ( 2 * m )

  p2, q2 = cfrac_to_rfrac ( 2 * m, g, h )
 
  r8vec_print ( m, p2, '  Recovered rational polynomial numerator coefficients:' )
  r8vec_print ( m + 1, q2, '  Recovered rational polynomial numerator coefficients:' )

  return

def rfrac_to_jfrac ( m, p, q ):

#*****************************************************************************80
#
## rfrac_to_jfrac() converts a rational polynomial fraction to a J fraction.
#
#  Discussion:
#
#    The routine accepts
#
#    P(1) + P(2) * X + ... + P(M) * X^(M-1)
#    -------------------------------------------------------
#    Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
#
#    and returns the equivalent J-fraction:
#
#    R(1) / ( X + S(1) + 
#    R(2) / ( X + S(2) + 
#    R(3) / ...        +
#    R(M) / ( X + S(M) )... ))
#
#    Thanks to Henry Amuasi for noticing and correcting an error in a
#    previous formulation of this routine, 02 October 2010.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly, Charles Mesztenyi, 
#    John Rice, Henry Thatcher, Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Input:
#
#    integer M, defines the number of P, R, and S coefficients,
#    and is one less than the number of Q coefficients.
#    1 <= M.
#
#    real P(M), Q(M+1), the coefficients defining the rational
#    polynomial fraction.
#
#  Output:
#
#    real R(M), S(M), the coefficients defining the
#    J-fraction.
#
  import numpy as np

  if ( m < 1 ):
    print ( '' )
    print ( 'rfrac_to_jfrac(): Fatal error!' )
    print ( '  M < 1' )
    raise Exception ( 'rfrac_to_jfrac(): Fatal error!' )

  a = np.zeros ( [ m + 1, m + 1] )
  
  for i in range ( 0, m + 1 ):
    a[i,0] = q[i]

  for i in range ( 0, m ):
    a[i,1] = p[i]

  r = np.zeros ( m )
  s = np.zeros ( m )

  if ( 1 < m ):

    r[0] = a[m-1,1] / a[m,0]
    s[0] = ( r[0] * a[m-1,0] - a[m-2,1] ) / a[m-1,1]

    for k in range ( 0, m - 2 ):

      a[0,k+2] = r[k] * a[0,k] - s[k] * a[0,k+1]

      for i in range ( 1, m - k - 1 ):
        a[i,k+2] = r[k] * a[i,k] - a[i-1,k+1] - s[k] * a[i,k+1]

      if ( a[m-k-2,k+2] == 0.0 ):
        print ( '' )
        print ( 'rfrac_to_jfrac(): Fatal error!' )
        print ( '  A(M-K-2,K+2) = 0 for K = %d' % ( k ) )
        raise Exception ( 'rfrac_to_jfrac(): Fatal error!' )

      r[k+1] = a[m-k-2,k+2] / a[m-k-1,k+1]
      s[k+1] = ( r[k+1] * a[m-k-2,k+1] - a[m-k-3,k+2] ) / a[m-k-2,k+2]

    a[0,m] = r[m-2] * a[0,m-2] - s[m-2] * a[0,m-1]

  r[m-1] = a[0,m] / a[1,m-1]
  s[m-1] = a[0,m-1] / a[1,m-1]

  return r, s

def rfrac_to_jfrac_test ( rng ):

#*****************************************************************************80
#
## rfrac_to_jfrac_test() tests rfrac_to_jfrac().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np
#
#  Generate the data, but force Q(M+1) to be 1.  
#  That will make it easier to see that the two operations are inverses
#  of each other.  jfrac_to_rfrac is free to scale its and chooses
#  a scaling in which Q(M+1) is 1.
#
  m = 6
  p = rng.random ( size = m )
  q = rng.random ( size = m + 1 )

  t = q[m]
  for i in range ( 0, m + 1 ):
    q[i] = q[i] / t

  print ( '' )
  print ( 'rfrac_to_jfrac_test():' )
  print ( '  rfrac_to_jfrac() converts a rational polynomial' )
  print ( '  fraction to a J fraction.' )

  r8vec_print ( m, p, '  RFRAC P:' )
  r8vec_print ( m + 1, q, '  RFRAC Q:' )
 
  r, s = rfrac_to_jfrac ( m, p, q )
 
  r8vec_print ( m, r, '  JFRAC R:' )
  r8vec_print ( m, s, '  JFRAC S:' )
 
  p2, q2 = jfrac_to_rfrac ( m, r, s )

  r8vec_print ( m, p2, '  Recovered RFRAC P:' )
  r8vec_print ( m + 1, q2, '  Recovered RFRAC Q:' )

  return

def schroeder ( n ):

#*****************************************************************************80
#
## schroeder() generates the Schroeder numbers.
#
#  Discussion:
#
#    The Schroeder number S(N) counts the number of ways to insert
#    parentheses into an expression of N items, with two or more items within
#    a parenthesis.
#
#    Note that the Catalan number C(N) counts the number of ways
#    to legally arrange a set of N left and N right parentheses.
#
#  Example:
#
#    N = 4
#
#    1234
#    12(34)
#    1(234)
#    1(2(34))
#    1(23)4
#    1((23)4)
#    (123)4
#    (12)34
#    (12)(34)
#    (1(23))4
#    ((12)3)4
#
#  First Values:
#
#           1
#           1
#           3
#          11
#          45
#         197
#         903
#        4279
#       20793
#      103049
#      518859
#     2646723
#    13648869
#    71039373
#
#  Formula:
#
#    S(N) = ( P(N)(3.0) - 3 P(N-1)(3.0) ) / ( 4 * ( N - 1 ) )
#    where P(N)(X) is the N-th Legendre polynomial.
#
#  Recursion:
#
#    S(1) = 1
#    S(2) = 1
#    S(N) = ( ( 6 * N - 9 ) * S(N-1) - ( N - 3 ) * S(N-2) ) / N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R P Stanley,
#    Hipparchus, Plutarch, Schroeder, and Hough,
#    American Mathematical Monthly,
#    Volume 104, Number 4, 1997, pages 344-350.
#
#    Laurent Habsieger, Maxim Kazarian, Sergei Lando,
#    On the Second Number of Plutarch,
#    American Mathematical Monthly, May 1998, page 446.
#
#  Input:
#
#    integer N, the number of Schroeder numbers desired.
#
#  Output:
#
#    integer S(N), the Schroeder numbers.
#
  import numpy as np

  s = np.zeros ( n, dtype = np.int32 )

  if ( 1 <= n ):

    s[0] = 1

    if ( 2 <= n ):

      s[1] = 1

      for i in range ( 3, n + 1 ):
        s[i-1] = ( ( 6 * i - 9 ) * s[i-2] - ( i - 3 ) * s[i-3] ) // i

  return s

def schroeder_test ( ):

#*****************************************************************************80
#
## schroeder_test() tests schroeder().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'schroeder_test():' )
  print ( '  schroeder() computes the Schroeder numbers.' )

  s = schroeder ( n )

  print ( '' )
  print ( '     N        S(N)' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8d' % ( i, s[i] ) )

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
#    integer I1, J1, K0, K1, N1, bookkeeping variables.
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
#  Input:
#
#    rng(): the current random number generator.
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

def subcomp_next ( n, k, a, more, h, t, n2, more2 ):

#*****************************************************************************80
#
## subcomp_next() computes the next subcomposition of N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to a value of N.
#
#    A subcomposition of the integer N into K parts is a composition
#    of M into K parts, where 0 <= M <= N.
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
#  Input:
#
#    integer N, the integer whose subcompositions are desired.
#
#    integer K, the number of parts in the subcomposition.
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the user to start the computation.
#
#    integer H, T, N2, internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#    bool MORE2, an internal parameter needed for the
#    computation.  The user may need to initialize this before the
#    very first call, but the initial value is not important.
#    The user should not alter this parameter once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the routine to end the computation.
#
#    integer H, T, N2, updated values.
#
#    bool MORE2, an updated value.
#

#
#  The first computation.
#
  if ( not more ):

    for i in range ( 0, k ):
      a[i] = 0
    more = True
    h = 0
    t = 0
    n2 = 0
    more2 = False
#
#  Do the next element at the current value of N.
#
  elif ( more2 ):

    a, more2, h, t = comp_next ( n2, k, a, more2, h, t )

  else:

    more2 = False
    n2 = n2 + 1

    a, more2, h, t = comp_next ( n2, k, a, more2, h, t )
#
#  Termination occurs if MORE2 = FALSE and N2 = N.
#
  if ( not more2 and n2 == n ):
    more = False

  return a, more, h, t, n2, more2

def subcomp_next_test ( ):

#*****************************************************************************80
#
## subcomp_next_test() tests subcomp_next().
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
  import platform

  n = 6
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0
  n2 = 0
  more2 = False

  print ( '' )
  print ( 'subcomp_next_test():' )
  print ( '  subcomp_next() generates subcompositions.' )
  print ( '' )
  print ( '  Seek all subcompositions of N = %d' % ( n ) )
  print ( '  Into K = %d parts.' % ( k ) )
  print ( '' )
  print ( '     #   Sum' )
  print ( '' )

  rank = 0

  while ( True ):

    a, more, h, t, n2, more2 = subcomp_next ( n, k, a, more, h, t, n2, more2 )

    rank = rank + 1
    print ( '  %4d  %4d  ' % ( rank, np.sum ( a ) ), end = '' )
    for i in range ( 0, k ):
      print ( '%4d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def subcompnz2_next ( n_lo, n_hi, k, a, more, h, t, n2, more2 ):

#*****************************************************************************80
#
## subcompnz2_next() computes the next subcomposition of N into K nonzero parts.
#
#  Discussion:
#
#    A composition of the integer N into K nonzero parts is an ordered sequence
#    of K positive integers which sum to a value of N.
#
#    A subcomposition of the integer N into K nonzero parts is a composition
#    of M into K nonzero parts, where 0 < M <= N.
#
#    This routine computes all compositions of K into nonzero parts which sum
#    to values between N_LO and N_HI.
#
#    The routine subcompnz_next can be regarded as a special case where 
#    N_LO = K.
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
#  Input:
#
#    integer N_LO, N_HI, the range of values N for which
#    compositions are desired.
#
#    integer K, the number of parts in the subcomposition.
#    K must be no greater than N_HI.
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the user to start the computation.
#
#    integer H, T, N2, internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#    bool MORE2, an internal parameter needed for the
#    computation.  The user may need to initialize this before the
#    very first call, but the initial value is not important.
#    The user should not alter this parameter once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the routine to end the computation.
#
#    integer H, T, N2, updated values.
#
#    bool MORE2, an updated value.
#

  if ( n_hi < k ):
    more = False
    for i in range ( 0, k ):
      a[i] = -1
    return a, more, h, t, n2, more2

  if ( n_hi < n_lo ):
    more = False
    for i in range ( 0, k ):
      a[i] = -1
    return a, more, h, t, n2, more2
#
#  The first computation.
#
  if ( not more ):

    more = True

    n2 = max ( k, n_lo )
    more2 = False
    h = 0
    t = 0

    a, more2, h, t = compnz_next ( n2, k, a, more2, h, t )
#
#  Do the next element at the current value of N.
#
  elif ( more2 ):

    a, more2, h, t = compnz_next ( n2, k, a, more2, h, t )

  else:

    n2 = n2 + 1

    a, more2, h, t = compnz_next ( n2, k, a, more2, h, t )
#
#  Termination occurs if MORE2 = FALSE and N2 = N_HI.
#
  if ( not more2 and n2 == n_hi ):
    more = False

  return a, more, h, t, n2, more2

def subcompnz2_next_test ( ):

#*****************************************************************************80
#
## subcompnz2_next_test() tests subcompnz2_next().
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
  import platform

  n_lo = 5
  n_hi = 7
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0
  n2 = 0
  more2 = False

  print ( '' )
  print ( 'subcompnz2_next_test():' )
  print ( '  subcompnz2_next() generates subcompositions' )
  print ( '  using nonzero parts.' )
  print ( '' )
  print ( '  Seek all subcompositions of N' )
  print ( '  using K = %d nonzero parts' % ( k ) )
  print ( '  for %d <= N <= %d' % ( n_lo, n_hi ) )
  print ( '' )
  print ( '     #     N' )
  print ( '' )

  rank = 0

  while ( True ):

    a, more, h, t, n2, more2 = subcompnz2_next ( n_lo, n_hi, k, a, more, h, t, n2, more2 )

    rank = rank + 1
    n = np.sum ( a )
    print ( '  %4d  %4d  ' % ( rank, n ), end = '' )
    for i in range ( 0, k ):
      print ( '%4d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def subcompnz_next ( n, k, a, more, h, t, n2, more2 ):

#*****************************************************************************80
#
## subcompnz_next() computes the next subcomposition of N into K nonzero parts.
#
#  Discussion:
#
#    A composition of the integer N into K nonzero parts is an ordered sequence
#    of K positive integers which sum to a value of N.
#
#    A subcomposition of the integer N into K nonzero parts is a composition
#    of M into K nonzero parts, where 0 < M <= N.
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
#  Input:
#
#    integer N, the integer whose subcompositions are desired.
#
#    integer K, the number of parts in the subcomposition.
#    K must be no greater than N.
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the user to start the computation.
#
#    integer H, T, N2, internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#    bool MORE2, an internal parameter needed for the
#    computation.  The user may need to initialize this before the
#    very first call, but the initial value is not important.
#    The user should not alter this parameter once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the routine to end the computation.
#
#    integer H, T, N2, updated values.
#
#    bool MORE2, an updated value.
#
  if ( n < k ):

    more = False
    for i in range ( 0, k ):
      a[i] = -1
    return a, more, h, t, n2, more2
#
#  The first computation.
#
  if ( not more ):

    for i in range ( 0, k ):
      a[i] = 1
    more = True
    h = 0
    t = 0
    n2 = k
    more2 = False
#
#  Do the next element at the current value of N.
#
  elif ( more2 ):

    a, more2, h, t = compnz_next ( n2, k, a, more2, h, t )

  else:

    more2 = False
    n2 = n2 + 1

    a, more2, h, t = compnz_next ( n2, k, a, more2, h, t )
#
#  Termination occurs if MORE2 = FALSE and N2 = N.
#
  if ( not more2 and n2 == n ):
    more = False

  return a, more, h, t, n2, more2

def subcompnz_next_test ( ):

#*****************************************************************************80
#
## subcompnz_next_test() tests subcompnz_next().
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
  import platform

  n = 6
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0
  n2 = 0
  more2 = False

  print ( '' )
  print ( 'subcompnz_next_test():' )
  print ( '  subcompnz_next() generates subcompositions' )
  print ( '  using nonzero parts.' )
  print ( '' )
  print ( '  Seek all subcompositions of N = %d' % ( n ) )
  print ( '  using K = %d nonzero parts.' % ( k ) )
  print ( '' )
  print ( '     #   Sum' )
  print ( '' )

  rank = 0

  while ( True ):

    a, more, h, t, n2, more2 = subcompnz_next ( n, k, a, more, h, t, n2, more2 )

    rank = rank + 1
    print ( '  %4d  %4d  ' % ( rank, np.sum ( a ) ), end = '' )
    for i in range ( 0, k ):
      print ( '%4d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def subset_by_size_next ( n, a, subsize, more, more2, m, m2 ):

#*****************************************************************************80
#
## subset_by_size_next() returns all subsets of an N set, in order of size.
#
#  Example:
#
#    N = 4:
#
#    1 2 3 4
#    1 2 3
#    1 2 4
#    1 3 4
#    1 3
#    1 4
#    2 3
#    1
#    2
#    3
#    (the empty set)
#
#  Discussion:
#
#    The subsets are returned in decreasing order of size, with the
#    empty set last.
#
#    For a given size K, the K subsets are returned in lexicographic order.
#
#    On the first call, it is only important that MORE be set FALSE.  The
#    input values of A and SUBSIZE are not important.
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
#    integer N, the size of the set.
#
#    integer A(N), the previous output subset.
#
#    integer SUBSIZE, the size of the previous output subset.
#
#    bool MORE, is FALSE on the first call, which signals
#    the routine to initialize itself.  Thereafter, MORE should be TRUE.
#
#    bool MORE2, a variable for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
#    integer M, M2, variables for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
#  Output:
#
#    integer A(N), the next subset.
#
#    integer SUBSIZE, the size of the next subset.
#
#    bool MORE, is TRUE as long as there are even more subsets
#    that can be produced by further calls.
#
#    bool MORE2, a variable for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
#    integer M, M2, variables for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
  if ( not more ):
    subsize = n
    more = True
    more2 = False
    m = 0
    m2 = 0
  else:
    if ( not more2 ):
      subsize = subsize - 1
#
#  Compute the next subset of size SIZE.
#
  if ( 0 < subsize ):
    a, more2, m, m2 = ksub_next ( n, subsize, a, more2, m, m2 )
  else:
    more = False

  return a, subsize, more, more2, m, m2

def subset_by_size_next_test ( ):

#*****************************************************************************80
#
## subset_by_size_next_test() tests subset_by_size_next().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_by_size_next_test():' )
  print ( '  subset_by_size_next() generates all subsets of an N set.' )
  print ( '' )

  n = 5
  a = np.zeros ( n )
  subsize = 0
  more = False
  more2 = False
  m = 0
  m2 = 0

  rank = 0

  while ( True ):

    a, subsize, more, more2, m, m2 = subset_by_size_next ( n, a, \
      subsize, more, more2, m, m2 )

    rank = rank + 1
    print ( '  %2d' % ( rank ), end = '' )

    if ( 0 < subsize ):
      for i in range ( 0, subsize ):
        print ( '  %2d' % ( a[i] ), end = '' )
      print ( '' )
    else:
      print ( '  The empty set' )

    if ( not more ):
      break

  return

def subset_gray_next ( n, a, more, ncard ):

#*****************************************************************************80
#
## subset_gray_next() generates all subsets of a set of order N, one at a time.
#
#  Discussion:
#
#    This routine generates the subsets one at a time, by adding or subtracting
#    exactly one element on each step.
#
#    This uses a Gray code ordering of the subsets.
#
#    The user should set MORE = FALSE and the value of N before
#    the first call.  On return, the user may examine A which contains
#    the definition of the new subset, and must check MORE, because
#    as soon as it is FALSE on return, all the subsets have been
#    generated and the user probably should cease calling.
#
#    The first set returned is the empty set.
#
#  Example:
#
#    N = 4
#
#    0 0 0 0
#    1 0 0 0
#    1 1 0 0
#    0 1 0 0
#    0 1 1 0
#    1 1 1 0
#    1 0 1 0
#    0 0 1 0
#    0 0 1 1
#    1 0 1 1
#    1 1 1 1
#    0 1 1 1
#    0 1 0 1
#    1 1 0 1
#    1 0 0 1
#    0 0 0 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
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
#    integer N, the order of the total set from which
#    subsets will be drawn.
#
#    integer A(N), the value of A on the previous call.
#    This value is not needed on the first call, with MORE = FALSE.
#
#    bool MORE, should be set to FALSE on the first call, and
#    then set to TRUE for all subsequent calls.
#
#    integer NCARD, the cardinality of A.  This value is not needed
#    on the first call, with MORE = FALSE.
#
#  Output:
#
#    integer A(N), the Gray code for the next subset.  A(I) = 0
#    if element I is in the subset, 1 otherwise.
#
#    bool MORE. will be returned TRUE until all the subsets
#    have been generated.
#
#    integer NCARD, the cardinality of A.
#
#    integer IADD, the element which was added or removed to the
#    previous subset to generate the current one.  Exception:
#    the empty set is returned on the first call, and IADD is set to -1.
#

#
#  The first set returned is the empty set.
#
  if ( not more ):

    for i in range ( 0, n ):
      a[i] = 0
    more = True
    ncard = 0
    iadd = -1

  else:

    iadd = 0

    if ( ( ncard % 2 ) != 0 ):

      while ( True ):

        iadd = iadd + 1
        if ( a[iadd-1] != 0 ):
          break

    a[iadd] = 1 - a[iadd]
    ncard = ncard + 2 * a[iadd] - 1
#
#  The last set returned is the singleton A(N).
#
    if ( ncard == a[n-1] ):
      more = False

  return a, more, ncard, iadd

def subset_gray_next_test ( ):

#*****************************************************************************80
#
## subset_gray_next_test() tests subset_gray_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_gray_next_test():' )
  print ( '  subset_gray_next() generates all subsets of an N set.' )
  print ( '  using the Gray code ordering:' )
  print ( '  0 0 1 0 1 means the subset contains 3 and 5.' )
  print ( '' )
  print ( '  Gray code' )
  print ( '' )
 
  rank = 0
  n = 5
  a = np.zeros ( n )
  more = False
  ncard = -1
  
  while ( True ):
 
    a, more, ncard, iadd = subset_gray_next ( n, a, more, ncard )

    rank = rank + 1

    print ( '  %2d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break

  return

def subset_gray_rank ( n, a ):

#*****************************************************************************80
#
## subset_gray_rank() ranks a subset of an N set, using the Gray code ordering.
#
#  Example:
#
#    N = 4
#
#       A       Rank
#    -------   -----
#
#    0 0 0 0       1
#    1 0 0 0       2
#    1 1 0 0       3
#    0 1 0 0       4
#    0 1 1 0       5
#    1 1 1 0       6
#    1 0 1 0       7
#    0 0 1 0       8
#    0 0 1 1       9
#    1 0 1 1      10
#    1 1 1 1      11
#    0 1 1 1      12
#    0 1 0 1      13
#    1 1 0 1      14
#    1 0 0 1      15
#    0 0 0 1      16
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the total set from which
#    subsets will be drawn.
#
#    integer A(N); A(I) is 1 if element I is in the set,
#    and 0 otherwise.
#
#  Output:
#
#    integer RANK, the rank of the subset in the Gray code ordering.
#
  gray = ubvec_to_ui4 ( n, a )

  rank = gray_rank2 ( gray )

  rank = rank + 1

  return rank

def subset_gray_rank_test ( ):

#*****************************************************************************80
#
## subset_gray_rank_test() tests subset_gray_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  a = np.array ( [ 1, 0, 1, 1, 0 ] )

  print ( '' )
  print ( 'subset_gray_rank_test():' )
  print ( '  subset_gray_rank() returns rank of a subset of an N set' )
  print ( '  using the Gray code ordering.' )
  print ( '' )
  print ( '  For N = %d' % ( n ) )
  print ( '  the subset is:' )
  for i in range ( 0, n ):
    print ( '  %4d' % ( a[i] ), end = '' )
  print ( '' )
 
  rank = subset_gray_rank ( n, a )
 
  print ( '' )
  print ( '  The rank is %d' % ( rank ) )

  return

def subset_gray_unrank ( rank, n ):

#*****************************************************************************80
#
## subset_gray_unrank() produces a subset of an N set of the given Gray code rank.
#
#  Example:
#
#    N = 4
#
#     Rank     A    
#    -----  -------
#
#        1  0 0 0 0
#        2  1 0 0 0
#        3  1 1 0 0
#        4  0 1 0 0
#        5  0 1 1 0
#        6  1 1 1 0
#        7  1 0 1 0
#        8  0 0 1 0
#        9  0 0 1 1
#       10  1 0 1 1
#       11  1 1 1 1
#       12  0 1 1 1
#       13  0 1 0 1
#       14  1 1 0 1
#       15  1 0 0 1
#       16  0 0 0 1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer RANK, the rank of the subset in the Gray code ordering.
#
#    integer N, the order of the total set from which
#    subsets will be drawn.
#
#  Output:
#
#    integer A(N) A(I) is 1 if element I is in the set,
#    and 0 otherwise.
#
  gray = gray_unrank2 ( rank-1 )

  a = ui4_to_ubvec ( gray, n )

  return a

def subset_gray_unrank_test ( ):

#*****************************************************************************80
#
## subset_gray_unrank_test() tests subset_gray_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'subset_gray_unrank_test():' )
  print ( '  subset_gray_unrank() finds the subset of an N set' )
  print ( '  of a given rank under the Gray code ordering.' )
  print ( '' )
  print ( '  N is %d' % ( n ) )
  print ( '' )
  print ( '  Rank   Subset' )
  print ( '' )

  for rank in range ( 1, 11 ):
 
    a = subset_gray_unrank ( rank, n )

    print ( '  %4d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % (a[i] ), end = '' )
    print ( '' )

  return

def subset_lex_next ( n, jmp, ndim, k, a ):

#*****************************************************************************80
#
## subset_lex_next() generates the subsets of a set of N elements, one at a time.
#
#  Discussion:
#
#    The subsets are generated in lexicographical order.  
#
#    The routine can also be forced to generate only those subsets whose 
#    size is no greater than some user-specified maximum.
#
#  Example:
#
#    N = 5, JMP = ( K == 3 )
#
#    1
#    1 2
#    1 2 3
#    1 2 4
#    1 2 5
#    1 3
#    1 3 4
#    1 3 5
#    1 4
#    1 4 5
#    1 5
#    2
#    2 3
#    2 3 4
#    2 3 5
#    2 4
#    2 4 5
#    2 5
#    3
#    3 4
#    3 4 5
#    3 5
#    4
#    4 5
#    5
#    empty set.
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
#    integer N, the order of the main set from which subsets
#    are chosen.
#
#    bool JMP.  In the simplest case, set JMP = FALSE for
#    a normal computation.  But to jump over supersets of the input set,
#    set JMP = TRUE.  Setting JMP = ( K == 3 ) before every new call
#    will, for example, force all the subsets returned
#    to have cardinality 3 or less.
#
#    integer NDIM, the allowed storage for A.  If NDIM < N,
#    JMP must be used to avoid creation of a subset too large to store in A.
#
#    integer K.  On first call, the user must set K = 0 as
#    a startup signal to the program.  Thereafter, set K to the output
#    value of K from the previous call. 
#
#    integer A(NDIM).  On first call, the value of A is not important.  
#    Thereafter, set A to the output value of A from the previous call.
#
#  Output:
#
#    integer K, the size of the computed subset.  On the last 
#    return, the empty set is returned and K is 0, which is a signal to
#    the user that the computation is complete.
#
#    integer A(NDIM).  A(I) is the I-th element of the
#    subset, listed in increasing order, with 0's in entries
#    beyond entry K.
#  
  if ( k <= 0 ):

    if ( jmp ):
      return k, a

    i = 0
    k = 1
    a[0] = 1

  elif ( a[k-1] != n ):

    i = a[k-1]

    if ( not jmp ):
      k = k + 1

    a[k-1] = i + 1

  else:

    k = k - 1

    if ( k != 0 ):
      a[k-1] = a[k-1] + 1

  return k, a

def subset_lex_next_test ( ):

#*****************************************************************************80
#
## subset_lex_next_test() tests subset_lex_next() with size restrictions.
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
  import platform

  print ( '' )
  print ( 'subset_lex_next_test():' )
  print ( '  subset_lex_next() generates all subsets of an N set.' )
  print ( '  The user can impose a restriction on the' )
  print ( '  maximum size of the subsets.' )

  n = 5
  ndim = 3
  k = 0
  a = np.zeros ( ndim )
  
  print ( '' )
  print ( '  Here, we require the subsets to be no larger' )
  print ( '  than %d' % ( ndim ) )

  while ( True ):
 
    ltest = ( k == ndim )

    k, a = subset_lex_next ( n, ltest, ndim, k, a )
 
    if ( 0 < k ):
      for i in range ( 0, k ):
        print ( '  %4d' % ( a[i] ), end = '' )
      print ( '' )
    else:
      print ( 'The empty set.' )
 
    if ( k == 0 ):
      break

  return

def subset_random ( n, rng ):

#*****************************************************************************80
#
## subset_random() selects a random subset of an N-set.
#
#  Example:
#
#    N = 4
#
#    0 0 1 1
#    0 1 0 1
#    1 1 0 1
#    0 0 1 0
#    0 0 0 1
#    1 1 0 0
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 May 2015
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
#    integer N, the size of the full set.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(N).  A vector to hold the information about
#    the set chosen.  On return, if A(I) = 1, then
#    I is in the random subset, otherwise, A(I) = 0
#    and I is not in the random subset.
#
  import numpy as np

  a = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

  return a

def subset_random_test ( rng ):

#*****************************************************************************80
#
## subset_random_test() tests subset_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'subset_random_test():' )
  print ( '  subset_random() randomly selects a subset.' )
  print ( '  The number of elements in the set is %d' % ( n ) )
  print ( '' )

  for test in range ( 0, 5 ):
    a = subset_random ( n, rng )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%4d' % ( a[i] ), end = '' )
    print ( '' )

  return

def subtriangle_next ( n, more, i1, j1, i2, j2, i3, j3 ):

#*****************************************************************************80
#
## subtriangle_next() computes the next subtriangle of a triangle.
#
#  Discussion:
#
#    The three sides of a triangle have been subdivided into N segments,
#    inducing a natural subdivision of the triangle into N*N subtriangles.
#    It is desired to consider each subtriangle, one at a time, in some
#    definite order.  This routine can produce information defining each 
#    of the subtriangles, one after another.
#
#    The subtriangles are described in terms of the integer coordinates 
#    (I,J) of their vertices.  These coordinates both range from 0 to N,
#    with the additional restriction that I + J <= N.
#
#    The vertices of each triangle are listed in counterclockwise order.
#
#  Example:
#
#    N = 4
#
#    4  *
#       |\
#       16\
#    3  *--*
#       |14|\
#       13\15\
#    2  *--*--*
#       |\9|11|\
#       |8\10\12\
#    1  *--*--*--*
#       |\2|\4|\6|\
#       |1\|3\|5\|7\
#   0   *--*--*--*--*
#
#       0  1  2  3  4
#
#    Rank  I1 J1  I2 J2  I3 J3
#    ----  -----  -----  ----- 
#       1   0  0   1  0   0  1
#       2   1  1   0  1   1  0
#       3   1  0   2  0   1  1
#       4   2  1   1  1   2  0
#       5   2  0   3  0   2  1
#       6   3  1   1  1   3  0
#       7   3  0   4  0   3  1
#       8   0  1   1  1   0  2
#       9   1  2   0  2   1  1
#      10   1  1   2  1   1  2
#      11   2  2   1  2   2  1
#      12   2  1   3  1   2  2
#      13   0  2   1  2   0  3
#      14   1  3   0  3   1  2
#      15   1  2   2  2   1  3
#      16   0  3   1  3   0  4
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
#  Input:
#
#    integer N, indicates the number of subdivisions of each side
#    of the original triangle.
#
#    bool MORE.  On first call, set MORE to FALSE.  Thereafter, 
#    the input value of MORE should be the output value from the previous
#    call.
#
#    integer I1, J1, I2, J2, I3, J3, the indices of the vertices 
#    of the subtriangle as computed on the previous call.  On the first call
#    with MORE set to FALSE, set these values to 0.
#
#  Output:
#
#    bool MORE, the output value of MORE will be TRUE if there 
#    are more subtriangles that can be generated by further calls.  However, 
#    if MORE is returned as FALSE, the accompanying subtriangle information 
#    refers to the last subtriangle that can be generated.
#
#    integer I1, J1, I2, J2, I3, J3, the indices of the 
#    vertices of the subtriangle.
#
  if ( n < 1 ):
    more = False
    return more, i1, j1, i2, j2, i3, j3

  if ( not more ):

    i1 = 0
    j1 = 0
    i2 = 1
    j2 = 0
    i3 = 0
    j3 = 1

    if ( n == 1 ):
      more = False
    else:
      more = True
#
#  We last generated a triangle like:
#
#    2---1
#     \  |
#      \ |
#       \|
#        3
#
  elif ( i2 < i3 ):

    i1 = i3
    j1 = j3
    i2 = i1 + 1
    j2 = j1
    i3 = i1
    j3 = j1 + 1
#
#  We last generated a triangle like
#
#    3
#    |\
#    | \
#    |  \
#    1---2
#
  elif ( i1 + 1 + j1 + 1 <= n ):

    i1 = i1 + 1
    j1 = j1 + 1
    i2 = i1 - 1
    j2 = j1
    i3 = i1
    j3 = j1 - 1
#
#  We must be at the end of a row.
#
  else:

    i1 = 0
    j1 = j1 + 1
    i2 = i1 + 1
    j2 = j1
    i3 = i1
    j3 = j1 + 1

    if ( n <= j1 + 1 ):
      more = False

  return more, i1, j1, i2, j2, i3, j3

def subtriangle_next_test ( ):

#*****************************************************************************80
#
## subtriangle_next_test() tests subtriangle_next().
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
  n = 4
  rank = 0

  more = False
  i1 = 0
  j1 = 0
  i2 = 0
  j2 = 0
  i3 = 0
  j3 = 0

  print ( '' )
  print ( 'subtriangle_next_test():' )
  print ( '  subtriangle_next() generates the indices of subtriangles' )
  print ( '  in a triangle whose edges were divided into N subedges.' )
  print ( '' )
  print ( '  For this test, N = %d' % ( n  ) )
  print ( '' )
  print ( '  Rank    I1  J1    I2  J2    I3  J3' )
  print ( '' )

  while ( True ):

    more, i1, j1, i2, j2, i3, j3 = subtriangle_next ( n, more, \
      i1, j1, i2, j2, i3, j3 )

    rank = rank + 1

    print ( '  %4d    %2d  %2d    %2d  %2d    %2d  %2d' \
      % ( rank, i1, j1, i2, j2, i3, j3 ) )

    if ( not more ):
      break

  return

def thue_binary_next ( n, thue ):

#*****************************************************************************80
#
## thue_binary_next() returns the next element in a binary Thue sequence.
#
#  Discussion:
#
#    Thue demonstrated that arbitrarily long sequences of 0's and
#    1's could be generated which had the "cubefree" property.  In
#    other words, for a given string S, there was no substring W
#    such that S contained "WWW".  In fact, a stronger result holds:
#    if "a" is the first letter of W, it is never the case that S
#    contains the substring "WWa".
#
#    In this example, the digits allowed are binary, that is, just
#    "0" and "1".  The replacement rules are:
#
#    "0" -> "01"
#    "1" -> "10"
#
#    This routine produces the next binary Thue sequence in a given series.
#    However, the input sequence must be a Thue sequence in order for
#    us to guarantee that the output sequence will also have the
#    cubic nonrepetition property.
#
#    Also, enough space must be set aside in THUE to hold the
#    output sequence.  This will always be twice the input
#    value of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the input sequence.
#
#    integer THUE(N), the initial Thue sequence.
#
#  Output:
#
#    integer N, the length of the output sequence.
#
#    integer THUE(N), the result of applying the substitution rules once.
#
  import numpy as np

  n2 = 2 * n
  thue2 = np.zeros ( n2, dtype = np.int32 )

  i2 = 0
  for i in range ( 0, n ):

    if ( thue[i] == 0 ):
      thue2[i2] = 0
      i2 = i2 + 1
      thue2[i2] = 1
      i2 = i2 + 1
    elif ( thue[i] == 1 ):
      thue2[i2] = 1
      i2 = i2 + 1
      thue2[i2] = 0
      i2 = i2 + 1
    else:
      print ( '' )
      print ( 'thue_binary_next(): Fatal error!' )
      print ( '  The input sequence contains a non-binary digit' )
      print ( '  THUE[%d] = %d' % ( i, thue[i] ) )
      raise Exception ( 'thue_binary_next(): Fatal error!' )
 
  return n2, thue2

def thue_binary_next_test ( ):

#*****************************************************************************80
#
## thue_binary_next_test() tests thue_binary_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'thue_binary_next_test():' )
  print ( '  thue_binary_next() returns the next Thue binary sequence.' )
  print ( '' )

  n = 1
  thue = np.zeros ( n, dtype = np.int32 )
  thue[0] = 0

  print ( '  %2d:  ' % ( n ), end = '' )
  for i in range ( 0, n ):
    print ( '%d' % ( thue[i] ), end = '' )
  print ( '' )

  for i in range ( 0, 6 ): 

    n, thue = thue_binary_next ( n, thue )

    print ( '  %2d:  ' % ( n ), end = '' )
    for i in range ( 0, n ):
      print ( '%d' % ( thue[i] ), end = '' )
    print ( '' )

  return

def thue_ternary_next ( n, thue ):

#*****************************************************************************80
#
## thue_ternary_next() returns the next element in a ternary Thue sequence.
#
#  Discussion:
#
#    Thue was interested in showing that there were arbitrarily long
#    sequences of digits which never displayed a pair of contiguous
#    repetitions of any length.  That is, there was no occurrence of
#    "00" or "1010" or "121121", anywhere in the string.  This makes
#    the string "squarefree".
#
#    To do this, he demonstrated a way to start with a single digit,
#    and to repeatedly apply a series of transformation rules to each
#    digit of the sequence, deriving nonrepeating sequences of ever
#    greater length.
#
#    In this example, the digits allowed are ternary, that is, just
#    "0", "1" and "2".  The replacement rules are:
#
#    "0" -> "12"
#    "1" -> "102"
#    "2" -> "0"
#
#    This routine produces the next Thue sequence in a given series.
#    However, the input sequence must be a Thue sequence in order for
#    us to guarantee that the output sequence will also have the
#    nonrepetition property.
#
#    Also, enough space must be set aside in THUE to hold the
#    output sequence.  This will never be more than 3 times the input
#    value of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    Third Base,
#    American Scientist,
#    Volume 89, Number 6, pages 490-494, November-December 2001.
#
#  Input:
#
#    integer N, the length of the input sequence.
#
#    integer THUE(N), the initial Thue sequence.
#
#  Output:
#
#    integer N, the length of the output sequence.
#
#    integer THUE(N), the result of applying the substitution rules once.
#
  import numpy as np
#
#  Determine length.
#
  n2 = 0

  for i in range ( 0, n ):

    if ( thue[i] == 0 ):
      n2 = n2 + 2
    elif ( thue[i] == 1 ):
      n2 = n2 + 3
    elif ( thue[i] == 2 ):
      n2 = n2 + 1
    else:
      print ( '' )
      print ( 'thue_ternary_next(): Fatal error!' )
      print ( '  The input sequence contains a non-ternary digit' )
      print ( '  THUE[%d] = %d' % ( i, thue[i] ) )
      raise Exception ( 'thue_ternary_next(): Fatal error!' )
#
#  Create new string.
#
  thue2 = np.zeros ( n2 )

  i2 = 0

  for i in range ( 0, n ): 

    if ( thue[i] == 0 ):
      thue2[i2] = 1
      i2 = i2 + 1
      thue2[i2] = 2
      i2 = i2 + 1
    elif ( thue[i] == 1 ):
      thue2[i2] = 1
      i2 = i2 + 1
      thue2[i2] = 0
      i2 = i2 + 1
      thue2[i2] = 2
      i2 = i2 + 1
    elif ( thue[i] == 2 ):
      thue2[i2] = 0
      i2 = i2 + 1

  return n2, thue2

def thue_ternary_next_test ( ):

#*****************************************************************************80
#
## thue_ternary_next_test() tests thue_ternary_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'thue_ternary_next_test():' )
  print ( '  thue_ternary_next() returns the next' )
  print ( '  Thue ternary sequence.' )
  print ( '' )

  thue = np.zeros ( 1 )
  n = 1
  thue[0] = 1

  i4vec_transpose_print ( n, thue, str ( 0 ) )

  for i in range ( 1, 6 ):
    [ n, thue ] = thue_ternary_next ( n, thue )
    i4vec_transpose_print ( n, thue, str ( i ) )

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

  return None

def triang ( n, zeta ):

#*****************************************************************************80
#
## triang() renumbers elements in accordance with a partial ordering.
#
#  Discussion:
#
#    TRIANG is given a partially ordered set.  The partial ordering
#    is defined by a matrix ZETA, where element I is partially less than
#    or equal to element J if and only if ZETA(I,J) = 1.
#
#    TRIANG renumbers the elements with a permutation P so that if
#    element I is partially less than element J in the partial ordering,
#    then P(I) < P(J) in the usual, numerical ordering.
#
#    In other words, the elements are relabeled so that their labels
#    reflect their ordering.  This is equivalent to relabeling the
#    matrix so that, on unscrambling it, the matrix would be upper
#    triangular.
#
#    Calling i4mat_perm or r8mat_perm with P used for both the row
#    and column permutations applied to matrix ZETA will result in
#    an upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
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
#    integer N, the number of elements in the set.  
#
#    integer ZETA(N,N), describes the partial ordering.  
#    ZETA(I,J) =:
#      0, for diagonal elements (I = J), or 
#         for unrelated elements, or
#         if J << I.
#      1, if I << J.
#
#  Output:
#
#    integer P(N), a permutation of (0,...,N-1) that reflects
#    the partial ordering of the elements.  P(I) is the new label of element 
#    I, with the property that if ZETA(I,J) = 1, that is, I << J,
#    then P(I) < P(J) (in the usual ordering).
#
  import numpy as np
#
#  Make sure ZETA represents a partially ordered set.  In other words,
#  if ZETA(I,J) = 1, then ZETA(J,I) must NOT be 1.
#
  ierror = pord_check ( n, zeta )

  if ( ierror != 0 ):
    print ( '' )
    print ( 'TRIANG(): Fatal error!' )
    print ( '  The matrix ZETA does not represent a' )
    print ( '  partial ordering.' )
    raise Exception ( 'TRIANG(): Fatal error!' )

  m = 1
  l = 0
  p = np.zeros ( n, dtype = np.int32 )

  it = m + 1
  ir = m + 1

  while ( True ):

    if ( ir <= n ):

      if ( p[ir-1] == 0 and zeta[ir-1,m-1] != 0 ):
        p[ir-1] = m
        m = ir
        ir = it
      else:
        ir = ir + 1

    else:

      l = l + 1
      iq = p[m-1]
      p[m-1] = l

      if ( iq != 0 ):

        ir = m + 1
        m = iq

      elif ( m == n ):

        break

      else:

        while ( True ):

          m = m + 1

          if ( p[m-1] == 0 ):
            break

          if ( m == n ):
            p = i4vec_decrement ( n, p )
            return p

        it = m + 1
        ir = m + 1

  p = i4vec_decrement ( n, p )

  return p

def triang_test ( ):

#*****************************************************************************80
#
## triang_test() tests triang().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  a = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 1, 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 0, 0, 1, 0, 1 ] ], dtype = np.int32 )

  print ( '' )
  print ( 'triang_test():' )
  print ( '  triang() relabels elements for a partial ordering,' )

  i4mat_print ( n, n, a, '  The input matrix:' )
 
  p = triang ( n, a )
 
  perm0_print ( n, p, '  The new ordering:' )

  a = i4mat_2perm0 ( n, n, a, p, p )
 
  i4mat_print ( n, n, a, '  The reordered matrix:' )

  return

def tuple_next2 ( n, xmin, xmax, rank, x ):

#*****************************************************************************80
#
## tuple_next2() computes the next element of an integer tuple space.
#
#  Discussion:
#
#    The elements X are N vectors.
#
#    Each entry X(I) is constrained to lie between XMIN(I) and XMAX(I).
#
#    The elements are produced one at a time.
#
#    The first element is
#      (XMIN(1), XMIN(2), ..., XMIN(N)),
#    the second is (probably)
#      (XMIN(1), XMIN(2), ..., XMIN(N)+1),
#    and the last element is
#      (XMAX(1), XMAX(2), ..., XMAX(N))
#
#    Intermediate elements are produced in a lexicographic order, with
#    the first index more important than the last, and the ordering of
#    values at a fixed index implicitly defined by the sign of
#    XMAX(I) - XMIN(I).
#
#  Example:
#
#    N = 2,
#    XMIN = (/ 1, 10 /)
#    XMAX = (/ 3,  8 /)
#
#    RANK    X
#    ----  -----
#      1   1 10
#      2   1  9
#      3   1  8
#      4   2 10
#      5   2  9
#      6   2  8
#      7   3 10
#      8   3  9
#      9   3  8
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components.
#
#    integer XMIN(N), XMAX(N), the "minimum" and "maximum" entry values.
#    These values are minimum and maximum only in the sense of the lexicographic
#    ordering.  In fact, XMIN(I) may be less than, equal to, or greater
#    than XMAX(I).
#
#    integer RANK, is set to 0 on the first call.  Thereafter, RANK
#    should be the value output by RANK on the previous call.
#
#    integer X(N), except on the first call, X should contain
#    the value output in X on the previous call.
#
#  Output:
#
#    integer RANK, the rank of the output item.  
#    If RANK is zero, there are no more items in the sequence.
#
#    integer X(N), the next tuple.
#
  if ( rank < 0 ):
    print ( '' )
    print ( 'tuple_next2(): Fatal error!' )
    print ( '  Illegal value of RANK = %d' % ( rank ) )
    raise Exception ( 'tuple_next2(): Fatal error!' )

  t = 1
  for i in range ( 0, n ):
    t = t * ( 1 + abs ( xmax[i] - xmin[i] ) )

  if ( t < rank ):
    print ( '' )
    print ( 'tuple_next2(): Fatal error!' )
    print ( '  Illegal value of RANK = %d' % ( rank ) )
    raise Exception ( 'tuple_next2(): Fatal error!' )

  if ( rank == 0 ):

    for i in range ( 0, n ):
      x[i] = xmin[i]
    rank = 1

  else:
  
    rank = rank + 1
    i = n - 1

    while ( True ):

      if ( x[i] != xmax[i] ):
        x[i] = x[i] + i4_sign ( xmax[i] - xmin[i] )
        break

      x[i] = xmin[i]

      if ( i == 0 ):
        rank = 0
        break

      i = i - 1

  return rank, x

def tuple_next2_test ( ):

#*****************************************************************************80
#
## tuple_next2_test() tests tuple_next2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  xmin = np.array ( [ 2, 3, 8 ] )
  xmax = np.array ( [ 4, 3, 5 ] )

  print ( '' )
  print ( 'tuple_next2_test():' )
  print ( '  tuple_next2() returns the next "tuple", that is,' )
  print ( '  a vector of N integers.' )
  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )

  print ( '  Min ', end = '' )
  for i in range ( 0, n ):
    print ( '  %2d' % ( xmin[i] ), end = '' )
  print ( '' )
  print ( '' )

  rank = 0
  x = np.zeros ( n )
  
  while ( True ):

    rank, x = tuple_next2 ( n, xmin, xmax, rank, x )

    if ( rank == 0 ):
      break

    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x[i] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  Max ', end = '' )
  for i in range ( 0, n ):
    print ( '  %2d' % ( xmax[i] ), end = '' )
  print ( '' )

  return

def tuple_next_fast ( m, n, rank, base ):

#*****************************************************************************80
#
## tuple_next_fast() computes the next element of a tuple space, "fast".
#
#  Discussion:
#
#    The elements are N vectors.  Each entry is constrained to lie
#    between 1 and M.  The elements are produced one at a time.
#    The first element is
#      (1,1,...,1)
#    and the last element is
#      (M,M,...,M)
#    Intermediate elements are produced in lexicographic order.
#
#    This code was written as a possibly faster version of tuple_next.
#
#  Example:
#
#    N = 2,
#    M = 3
#
#    INPUT        OUTPUT
#    -------      -------
#    Rank          X
#    ----          ----
#   -1            -1 -1
#
#    0             1  1
#    1             1  2
#    2             1  3
#    3             2  1
#    4             2  2
#    5             2  3
#    6             3  1
#    7             3  2
#    8             3  3
#    9             1  1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the maximum entry in each component.
#    M must be greater than 0.
#
#    integer N, the number of components.
#    N must be greater than 0.
#
#    integer RANK, indicates the rank of the tuples.
#    Typically, 0 <= RANK < N^M values greater than this are
#    legal and meaningful, being equivalent to the corresponding
#    value mod N^M.  RANK < 0 indicates that this is the first
#    call for the given values of (M,N).  Initialization is done,
#    and X is set to a dummy value.
#
#    integer BASE(N), a bookkeeping array needed by 
#    this procedure.  The user should allocate space for this array, but
#    should not alter it between successive calls.
#
#  Output:
#
#    integer X(N), the next tuple of the given rank,
#    or a dummy value if initialization is being done.
#
#    integer BASE(N), a bookkeeping array.
#
  import numpy as np

  x = np.zeros ( n, dtype = np.int32 )

  if ( rank < 0 ):

    if ( m <= 0 ):
      print ( '' )
      print ( 'tuple_next_fast(): Fatal error!' )
      print ( '  M <= 0 is illegal.' )
      print ( '  M = %d' % ( m ) )
      raise Exception ( 'tuple_next_fast(): Fatal error!' )

    if ( n <= 0 ):
      print ( '' )
      print ( 'tuple_next_fast(): Fatal error!' )
      print ( '  N <= 0 is illegal.' )
      print ( '  N = %d' % ( n ) )
      raise Exception ( 'tuple_next_fast(): Fatal error!' )

    base[n-1] = 1
    for i in range ( n - 2, -1, -1 ):
      base[i] = base[i+1] * m

    for i in range ( 0, n ):
      x[i] = -1

  else:

    for i in range ( 0, n ):
      x[i] = ( ( rank // base[i] ) % m ) + 1

  return x, base

def tuple_next_fast_test ( ):

#*****************************************************************************80
#
## tuple_next_fast_test() tests tuple_next_fast().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 2
  m = 3

  print ( '' )
  print ( 'tuple_next_fast_test():' )
  print ( '  tuple_next_fast() returns the next "tuple", that is,' )
  print ( '  a vector of N integers, each between 1 and M.' )
  print ( '' )
  print ( '  M = %d' % ( m ) )
  print ( '  N = %d' % ( n ) )
  print ( '' )
#
#  Initialize.
#
  rank = -1
  base = np.zeros ( n )
  x, base = tuple_next_fast ( m, n, rank, base )

  rank_max = ( m ** n ) - 1

  for rank in range ( 0, rank_max + 1 ):

    x, base = tuple_next_fast ( m, n, rank, base )

    print ( '%4d  ' % ( rank ), end = '' )
    for j in range ( 0, n ):
      print ( '%10d  ' % ( x[j] ), end = '' )
    print ( '' )

  return

def tuple_next_ge ( m, n, rank, x ):

#*****************************************************************************80
#
## tuple_next_ge() computes the next "nondecreasing" element of a tuple space.
#
#  Discussion:
#
#    The elements are N vectors.  Each element is constrained to lie
#    between 1 and M, and to have components that are nondecreasing.
#    That is, for an element X, and any positive K,
#      X(I) <= X(I+K)
#
#    The elements are produced one at a time.
#    The first element is
#      (1,1,...,1)
#    and the last element is
#      (M,M,...,M)
#    Intermediate elements are produced in lexicographic order.
#
#  Example:
#
#    N = 3, M = 3
#
#    RANK   X
#    ----  -----
#       1  1 1 1
#       2  1 1 2
#       3  1 1 3
#       4  1 2 2
#       5  1 2 3
#       6  1 3 3
#       7  2 2 2
#       8  2 2 3
#       9  2 3 3
#      10  3 3 3
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
#  Input:
#
#    integer M, the maximum entry.
#
#    integer N, the number of components.
#
#    integer RANK, the rank of the input tuple.
#    On first call, set K to 0.  Thereafter, K will indicate the
#    order of the element returned.  When there are no more elements,
#    K will be returned as 0.
#
#    integer X(N), on input the previous tuple (except
#    on the first call, when the input value of X is not needed.)
#    On the next tuple.
#
#  Output:
#
#    integer RANK, the rank of the output tuple.
#    When there are no more elements, RANK will be returned as 0.
#
#    integer X(N), on input the previous tuple (except
#    on the first call, when the input value of X is not needed.)
#    On the next tuple.
#
  if ( rank <= 0 ):
    for i in range ( 0, n ):
      x[i] = 1
    rank = 1
    return rank, x

  for i in range ( n - 1, -1, -1 ):

    if ( x[i] < m ):
      x[i] = x[i] + 1
      for j in range ( i + 1, n ):
        x[j] = x[i]
      rank = rank + 1
      return rank, x

  rank = 0
  for i in range ( 0, n ):
    x[i] = 0

  return rank, x

def tuple_next_ge_test ( ):

#*****************************************************************************80
#
## tuple_next_ge_test() tests tuple_next_ge().
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

  m = 3
  n = 3
  rank = 0
  x = np.zeros ( n )

  print ( '' )
  print ( 'tuple_next_ge_test():' )
  print ( '  tuple_next_ge() returns the next "tuple", that is,' )
  print ( '  a vector of N integers, each between 1 and M,' )
  print ( '  with the constraint that the entries be' )
  print ( '  nondecreasing.' )
  print ( '' )
  print ( '  M = %d' % ( m ) )
  print ( '  N = %d' % ( n ) )
  print ( '' )

  while ( True ):

    rank, x = tuple_next_ge ( m, n, rank, x )

    if ( rank == 0 ):
      break

    print ( '  %2d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( x[i] ), end = '' )
    print ( '' )

  return

def tuple_next ( m1, m2, n, rank, x ):

#*****************************************************************************80
#
## tuple_next() computes the next element of a tuple space.
#
#  Discussion:
#
#    The elements are N vectors.  Each entry is constrained to lie
#    between M1 and M2.  The elements are produced one at a time.
#    The first element is
#      (M1,M1,...,M1),
#    the second element is
#      (M1,M1,...,M1+1),
#    and the last element is
#      (M2,M2,...,M2)
#    Intermediate elements are produced in lexicographic order.
#
#  Example:
#
#    N = 2, M1 = 1, M2 = 3
#
#    INPUT        OUTPUT
#    -------      -------
#    Rank  X      Rank   X
#    ----  ---    -----  ---
#    0     * *    1      1 1
#    1     1 1    2      1 2
#    2     1 2    3      1 3
#    3     1 3    4      2 1
#    4     2 1    5      2 2
#    5     2 2    6      2 3
#    6     2 3    7      3 1
#    7     3 1    8      3 2
#    8     3 2    9      3 3
#    9     3 3    0      0 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M1, M2, the minimum and maximum entries.
#
#    integer N, the number of components.
#
#    integer RANK, counts the elements.
#    On first call, set RANK to 0.  On subsequent calls, the input value of
#    RANK should be the output value of RANK from the previous call.
#
#    integer X(N), the previous tuple.
#
#  Output:
#
#    integer RANK, the order of the next tuple.  When there are no
#    more elements, RANK will be returned as 0.
#
#    integer X(N), the next tuple.
#
  if ( m2 < m1 ):

    rank = 0

  elif ( rank <= 0 ):

    for i in range ( 0, n ):
      x[i] = m1
      rank = 1

  else:

    rank = rank + 1
    i = n - 1

    while ( True ):

      if ( x[i] < m2 ):
        x[i] = x[i] + 1
        break

      x[i] = m1

      if ( i == 0 ):
        rank = 0
        for i in range ( 0, n ):
          x[i] = m1
          break

      i = i - 1

  return rank, x

def tuple_next_test ( ):

#*****************************************************************************80
#
## tuple_next_test() tests tuple_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 2
  m1 = 2
  m2 = 4

  print ( '' )
  print ( 'tuple_next_test():' )
  print ( '  tuple_next() returns the next "tuple", that is,' )
  print ( '  a vector of N integers, each between M1 and M2.' )
  print ( '' )
  print ( '  M1 = %d' % ( m1 ) )
  print ( '  M2 = %d' % ( m2 ) )
  print ( '  N =  %d' % ( n ) )
  print ( '' )
  print ( '   #    X[0]   X[1]' )
  print ( '' )

  rank = 0
  x = np.zeros ( n )

  while ( True ):

    rank, x = tuple_next ( m1, m2, n, rank, x )

    if ( rank == 0 ):
      break

    print ( '%4d  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '%4d  ' % ( x[i] ), end = '' )
    print ( '' )

  return

def ubvec_add ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## ubvec_add() adds two unsigned binary vectors.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#     UBVEC1       +  UBVEC2       =  UBVEC3
#
#    ( 1 0 0 0 )   + ( 1 1 0 0 )   = ( 0 0 1 0 )
#
#      1           +   3           =   4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), UBVEC2(N), the vectors to be added.
#
#  Output:
#
#    integer UBVEC3(N), the sum of the two input vectors.
#
  import numpy as np

  overflow = False

  ubvec3 = np.zeros ( n )
#
#  Add.
#
  for i in range ( 0, n ):
    ubvec3[i] = ubvec1[i] + ubvec2[i]
#
#  Carry.
#
  for i in range ( n - 1, -1, -1 ):
    while ( 2 <= ubvec3[i] ):
      ubvec3[i] = ubvec3[i] - 2
      if ( 0 < i ):
        ubvec3[i-1] = ubvec3[i-1] + 1
      else:
        overflow = True

  return ubvec3

def ubvec_add_test ( rng ):

#*****************************************************************************80
#
## ubvec_add_test() tests ubvec_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'ubvec_add_test():' )
  print ( '  ubvec_add() adds unsigned binary vectors representing' )
  print ( '  unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I + J' )
  print ( '' )

  for test in range ( 0, 10 ):
    
    i = rng.integers ( low = 0, high = 100, endpoint = True )
    j = rng.integers ( low = 0, high = 100, endpoint = True )

    print ( '' )

    print ( '  %8d  %8d' % ( i, j ) )

    k = i + j

    print ( '  Directly:           %8d' % ( k ) )

    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )

    ubvec3 = ubvec_add ( n, ubvec1, ubvec2 )
    k = ubvec_to_ui4 ( n, ubvec3 )

    print ( '  ubvec_add           %8d' % ( k ) )

  return

def ubvec_print ( n, ubvec, title ):

#*****************************************************************************80
#
## ubvec_print() prints a UBVEC, with an optional title.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer UBVEC(N), the vector to be printed.
#
#    character TITLE, a title to be printed first.
#    TITLE may be blank.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ihi in range ( n - 1, -1, -70 ):
    ilo = max ( ihi - 70 + 1, 0 )
    print ( '  ', end = '' )
    for i in range ( ihi, ilo - 1, -1 ):
      print ( '%1d' % ( ubvec[i] ), end = '' )
    print ( '' )

  return

def ubvec_print_test ( ):

#*****************************************************************************80
#
## ubvec_print_test() tests ubvec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  ubvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ( '' )
  print ( 'ubvec_print_test():' )
  print ( '  ubvec_print() prints an unsigned binary vector.' )

  ubvec_print ( n, ubvec, '  UBVEC:' )

  return

def ubvec_to_ui4 ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_to_ui4() makes an unsigned integer from an unsigned binary vector.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#        UBVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1      11  3
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    1001  9
#    1, 1, 1, 1    1111 15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer UBVEC(N), the binary representation.
#
#  Output:
#
#    integer VALUE, the integer.
#
  value = 0
  for i in range ( 0, n ):
    value = 2 * value + ubvec[i]

  return value

def ubvec_to_ui4_test ( ):

#*****************************************************************************80
#
## ubvec_to_ui4_test() tests ubvec_to_ui4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'ubvec_to_ui4_test():' )
  print ( '  ubvec_to_ui4() converts an unsigned binary vector' )
  print ( '  to an unsigned integer' )
  print ( '' )
  print ( '  ui4 --> UBVEC  -->  ui4' )
  print ( '' )

  for ui4 in range ( 0, 11 ):
    ubvec = ui4_to_ubvec ( ui4, n )
    i2 = ubvec_to_ui4 ( n, ubvec )
    print ( '  %2d  ' % ( ui4 ), end = '' )
    for j in range ( 0, n ):
      print ( '%1d' % ( ubvec[j] ), end = '' )
    print ( '  %2d' % ( i2 ) )

  return

def ubvec_xor ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## ubvec_xor() computes the exclusive OR of two UBVEC's.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), UBVEC2(N), the binary vectors to be XOR'ed.
#
#    integer UBVEC3(N), the exclusive OR of the two vectors.
#
  import numpy as np

  ubvec3 = np.zeros ( n )

  for i in range ( 0, n ):
    ubvec3[i] = ( ( ubvec1[i] + ubvec2[i] ) % 2 )

  return ubvec3

def ubvec_xor_test ( rng ):

#*****************************************************************************80
#
## ubvec_xor_test() tests ubvec_xor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10
  test_num = 10

  print ( '' )
  print ( 'ubvec_xor_test():' )
  print ( '  ubvec_xor() exclusive-ors unsigned binary vectors representing' )
  print ( '  unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I XOR J' )
  print ( '' )

  for test in range ( 0, 10 ):
    i = rng.integers ( low = 0, high = 100, endpoint = True )
    j = rng.integers ( low = 0, high = 100, endpoint = True )
    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )
    ubvec3 = ubvec_xor ( n, ubvec1, ubvec2 )
    k = ubvec_to_ui4 ( n, ubvec3 )
    print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  return

def ui4_to_ubvec ( ui4, n ):

#*****************************************************************************80
#
## ui4_to_ubvec() makes a unsigned binary vector from an integer.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2**(N-1).
#
#    To guarantee that there will be enough space for any
#    value of I, it would be necessary to set N = 32.
#
#  Example:
#
#     I       BVEC         binary
#    --  ----------------  ------
#     1  1, 0, 0, 0, 0, 0       1
#     2  0, 1, 0, 0, 0, 0      10
#     3  1, 1, 0, 0, 0, 0      11
#     4  0, 0, 1, 0, 0, 0     100
#     9  1, 0, 0, 1, 0, 0    1001
#    -9  1, 1, 1, 0, 1, 1  110111
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ui4, an integer to be represented.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    integer BVEC(N), the unsigned binary representation.
#
  import numpy as np

  ubvec = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    ubvec[i] = ( ui4 % 2 )
    ui4 = ( ui4 // 2 )

  return ubvec

def ui4_to_ubvec_test ( ):

#*****************************************************************************80
#
## ui4_to_ubvec_test() tests ui4_to_ubvec();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'ui4_to_ubvec_test():' )
  print ( '  ui4_to_ubvec() converts an unsigned integer to an' )
  print ( '  unsigned binary vector;' )
  print ( '' )
  print ( '  ui4 --> UBVEC  -->  ui4' )
  print ( '' )

  for i in range ( 0, 11 ):
    bvec = ui4_to_ubvec ( i, n )
    i2 = ubvec_to_ui4 ( n, bvec )
    print ( '  %2d  ' % ( i ), end = '' )
    for i in range ( 0, n ):
      print ( '%1d' % ( bvec[i] ), end = '' )
    print ( '  %2d' % ( i2 ) )

  return

def vec_colex_next2 ( dim_num, base, a, more ):

#*****************************************************************************80
#
## vec_colex_next2() generates vectors in colex order.
#
#  Discussion:
#
#    The vectors are produced in colexical order, starting with
#    (0,0,...,0),
#    (1,0,...,0),
#    ...
#    (BASE(1)-1,BASE(2)-1,...,BASE(DIM_nUM)-1).
#
#  Example:
#
#    DIM_nUM = 2, 
#    BASE = [ 3, 3]
#
#    0   0
#    1   0
#    2   0
#    0   1
#    1   1
#    2   1
#    0   2
#    1   2
#    2   2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer DIM_nUM, the spatial dimension.
#
#    integer BASE(DIM_nUM), the base to be used in each dimension.
#
#    integer A(DIM_nUM), except on the first call, this should
#    be the output value of A on the last call.
#
#    bool MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(DIM_nUM), the next vector.
#
#    bool MORE, is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  if ( not more ):

    for i in range ( 0, dim_num ):
      a[i] = 0

    more = True

  else:

    more = False

    for i in range ( 0, dim_num ):

      a[i] = a[i] + 1

      if ( a[i] < base[i] ):
        more = True
        break

      a[i] = 0

  return a, more

def vec_colex_next2_test ( ):

#*****************************************************************************80
#
## vec_colex_next2_test() tests vec_colex_next2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vec_colex_next2_test():' )
  print ( '  vec_colex_next2() generates all DIM_nUM-vectors' )
  print ( '  in colex order in a given base BASE.' )
  
  dim_num = 3
  base = np.array ( [ 2, 1, 3 ] )
  a = np.zeros ( dim_num )
  more = False

  print ( '' )
  print ( '  The spatial dimension DIM_nUM = %d' % ( dim_num ) )
  i4vec_transpose_print ( dim_num, base, '  The base vector:' )
  print ( '' )

  while ( True ):

    a, more = vec_colex_next2 ( dim_num, base, a, more )

    if ( not more ):
      break

    i4vec_transpose_print ( dim_num, a, '' )

  return

def vec_colex_next3 ( dim_num, base, a, more ):

#*****************************************************************************80
#
## vec_colex_next3() generates vectors in colex order.
#
#  Discussion:
#
#    The vectors are produced in colexical order, starting with
#    (1,1,...,1),
#    (2,1,...,1),
#    ...
#    (BASE(1),BASE(2),...,BASE(DIM_nUM)).
#
#  Example:
#
#    DIM_nUM = 2, 
#    BASE = [ 3, 3]
#
#    1   1
#    2   1
#    3   1
#    1   2
#    2   2
#    3   2
#    1   3
#    2   3
#    3   3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer DIM_nUM, the spatial dimension.
#
#    integer BASE(DIM_nUM), the base to be used in each dimension.
#
#    integer A(DIM_nUM), except on the first call, this should
#    be the output value of A on the last call.
#
#    bool MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(DIM_nUM), the next vector.
#
#    bool MORE, is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  if ( not more ):

    for i in range ( 0, dim_num ):
      a[i] = 1

    more = True

  else:
      
    more = False

    for i in range ( 0, dim_num ):

      a[i] = a[i] + 1

      if ( a[i] <= base[i] ):
        more = True
        break

      a[i] = 1

  return a, more

def vec_colex_next3_test ( ):

#*****************************************************************************80
#
## vec_colex_next3_test() tests vec_colex_next3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vec_colex_next3_test():' )
  print ( '  vec_colex_next3() generates all DIM_nUM-vectors' )
  print ( '  in colex order in a given base BASE.' )
  
  dim_num = 3
  base = np.array ( [ 2, 1, 3 ] )
  a = np.zeros ( dim_num )
  more = False

  print ( '' )
  print ( '  The spatial dimension DIM_nUM = %d' % ( dim_num ) )
  i4vec_transpose_print ( dim_num, base, '  The base vector:' )
  print ( '' )

  while ( True ):

    a, more = vec_colex_next3 ( dim_num, base, a, more )

    if ( not more ):
      break

    i4vec_transpose_print ( dim_num, a, '' )

  return

def vec_colex_next ( dim_num, base, a, more ):

#*****************************************************************************80
#
## vec_colex_next() generates vectors in colex order.
#
#  Discussion:
#
#    The vectors are produced in colexical order, starting with
#    (0,0,...,0),
#    (1,0,...,0),
#    ...
#    (BASE-1,BASE-1,...,BASE-1).
#
#  Examples:
#
#    DIM_nUM = 2, 
#    BASE = 3
#
#    0   0
#    1   0
#    2   0
#    0   1
#    1   1
#    2   1
#    0   2
#    1   2
#    2   2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer DIM_nUM, the spatial dimension.
#
#    integer BASE, the base to be used.  BASE = 2 will
#    give vectors of 0's and 1's, for instance.
#
#    integer A(DIM_nUM), except on the first call, this should
#    be the output value of A on the last call.
#
#    bool MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(DIM_nUM), the next vector.
#
#    bool MORE, is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  if ( not more ):

    for i in range ( 0, dim_num ):
      a[i] = 0
      more = True

  else:
  
    more = False

    for i in range ( 0, dim_num ):

      a[i] = a[i] + 1

      if ( a[i] < base ):
        more = True
        break

      a[i] = 0

  return a, more

def vec_colex_next_test ( ):

#*****************************************************************************80
#
## vec_colex_next_test() tests vec_colex_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vec_colex_next_test():' )
  print ( '  vec_colex_next() generates all DIM_nUM-vectors' )
  print ( '  in colex order in a given base BASE.' )
  
  dim_num = 3
  base = 3
  a = np.zeros ( dim_num )
  more = False

  print ( '' )
  print ( '  The spatial dimension DIM_nUM = %d' % ( dim_num ) )
  print ( '  The base BASE =                 %d' % ( base ) )
  print ( '' )

  while ( True ):

    a, more = vec_colex_next ( dim_num, base, a, more )

    if ( not more ):
      break

    i4vec_transpose_print ( dim_num, a, '' )

  return

def vec_gray_next ( n, base, a, done, active, dir ):

#*****************************************************************************80
#
## vec_gray_next() computes the elements of a product space.
#
#  Discussion:
#
#    The elements are produced one at a time.
#
#    This routine handles the case where the number of degrees of freedom may
#    differ from one component to the next.
#
#    A method similar to the Gray code is used, so that successive
#    elements returned by this routine differ by only a single element.
#
#    A previous version of this routine used internal static memory.
#
#  Example:
#
#    N = 2, BASE = ( 2, 3 ), DONE = TRUE
#
#     A    DONE  CHANGE
#    ---  -----  ------
#    0 0  FALSE    1
#    0 1  FALSE    2
#    0 2  FALSE    2
#    1 2  FALSE    1
#    1 1  FALSE    2
#    1 0  FALSE    2
#    1 0   TRUE   -1  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer N, the number of components.
#
#    integer BASE(N), contains the number of degrees of
#    freedom of each component.  The output values of A will
#    satisfy 0 <= A(I) < BASE(I).
#
#    integer A(N).  On the first call, the input value
#    of A doesn't matter.  Thereafter, it should be the same as
#    its output value from the previous call. 
#
#    bool DONE.  On the first call, the user must
#    set DONE to TRUE.  Thereafter, DONE should be set to the output
#    value of DONE on the previous call.  
#
#    integer ACTIVE(N), DIR(N), bookkeeping arrays needed by the 
#    function.  The user should create them before the first call, but 
#    thereafter should not change their values, passing in the output values 
#    of the previous call for the next call.
#
#  Output:
#
#    integer A(N), the next vector. 
#
#    bool DONE.  If the output value is FALSE,
#    then the program has computed another entry in A.  If the output
#    value of DONE is TRUE, then there are no more entries.
#
#    integer ACTIVE(N), DIR(N), bookkeeping arrays.
#
#    integer CHANGE, is set to the index of the element whose
#    value was changed.  On return from the first call, CHANGE
#    is 0, even though all the elements have been "changed".  On
#    return with DONE equal to TRUE, CHANGE is -1.
#

#
#  The user is calling for the first time.
#
  if ( done ):

    done = False
    for i in range ( 0, n ):
      a[i] = 0
      dir[i] = 1
      active[i] = 1

    for i in range ( 0, n ):

      if ( base[i] < 1 ):
        print ( '' )
        print ( 'vec_gray_next - Warning!' )
        print ( '  For index I = %d' % ( i ) )
        print ( '  the nonpositive value of BASE(I) = %d' % ( base[i] ) )
        print ( '  which was reset to 1!' )
        base[i] = 1
        active[i] = 0
      elif ( base[i] == 1 ):
        active[i] = 0

    change = 0
#
#  Find the maximum active index.
#
  else:

    change = -1

    for i in range ( 0, n ):
      if ( active[i] != 0 ):
        change = i
#
#  If there are NO active indices, we have generated all vectors.
#
    if ( change == -1 ):

      done = True

    else:
#
#  Increment the element with maximum active index.
#
      a[change] = a[change] + dir[change]
#
#  If we attained a minimum or maximum value, reverse the direction
#  vector, and deactivate the index.
#
      if ( a[change] == 0 or a[change] == base[change] - 1 ):
        dir[change] = - dir[change]
        active[change] = 0
#
#  Activate all subsequent indices.
#
      for i in range ( change + 1, n ):
        if ( 1 < base[i] ):
          active[i] = 1

  return a, done, active, dir, change

def vec_gray_next_test ( ):

#*****************************************************************************80
#
## vec_gray_next_test() tests vec_gray_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  base = np.array ( [ 2, 2, 1, 4 ] )
  number = np.prod ( base )

  print ( '' )
  print ( 'vec_gray_next_test():' )
  print ( '  vec_gray_next() generates product space elements.' )
  print ( '' )
  print ( '  The number of components is %d' % ( n ) )
  print ( '  The number of elements is %d' % ( number ) )
  print ( '  Each component has its own number of degrees of' )
  print ( '  freedom.' )
  print ( '' )
  print ( '  Rank Change     ', end = '' )
  for i in range ( 0, n ):
    print ( '  %4d' % ( base[i] ), end = '' )
  print ( '' )
  print ( '' )

  rank = 0  
  a = np.zeros ( n )
  done = True
  active = np.zeros ( n )
  dir = np.zeros ( n )
 
  while ( True ):
 
    rank = rank + 1
 
    a, done, active, dir, change = vec_gray_next ( n, base, a, done, active, dir )
 
    if ( done ):
      break

    print ( '  %4d  %4d      ' % ( rank, change ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )

  return

def vec_gray_rank ( n, base, a ):

#*****************************************************************************80
#
## vec_gray_rank() computes the rank of a product space element.
#
#  Discussion:
#
#    The rank applies only to the elements as produced by the routine
#    vec_gray_next.
#
#  Example:
#
#    N = 2, BASE = (/ 2, 3 /), A = ( 1, 2 ),
#
#    RANK = 4.
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
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer N, the number of components.
#
#    integer BASE(N), contains the number of degrees of
#    freedom of each component.  The output values of A will
#    satisfy 0 <= A(I) < BASE(I).
#
#    integer A(N), the product space element, with the
#    property that 0 <= A(I) < BASE(I) for each entry I.
#
#  Output:
#
#    integer RANK, the rank, or order, of the element in
#    the list of all elements.  The rank count begins at 1.
#
  rank = 0

  for i in range ( 0, n ):

    if ( ( rank % 2 ) == 1 ):
      c = base[i] - a[i] - 1
    else:
      c = a[i]

    rank = base[i] * rank + c

  rank = rank + 1

  return rank

def vec_gray_rank_test ( ):

#*****************************************************************************80
#
## vec_gray_rank_test() tests vec_gray_rank().
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
  import numpy as np

  n = 4
  base = np.array ( [ 2, 2, 1, 4 ] )
  ne = np.prod ( base )

  print ( '' )
  print ( 'vec_gray_rank_test():' )
  print ( '  vec_gray_rank() ranks product space elements.' )
  print ( '' )
  print ( '  The number of components is %d' % ( n ) )
  print ( '  The number of elements is %d' % ( ne ) )
  print ( '  Each component has its own number of degrees of' )
  print ( '  freedom.' )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = base[i] // 2

  rank = vec_gray_rank ( n, base, a )

  print ( '' )
  print ( '  vec_gray_rank reports the element' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %d' % ( a[i] ), end = '' )
  print ( '' )
  print ( '' )
  print ( '  has rank %d' % ( rank ) )

  return

def vec_gray_unrank ( n, base, rank ):

#*****************************************************************************80
#
## vec_gray_unrank() computes the product space element of a given rank.
#
#  Discussion:
#
#    The rank applies only to the elements as produced by the routine
#    vec_gray_next.
#
#  Examples:
#
#    N = 2, BASE = ( 2, 3 ), RANK = 4.
#
#    A = ( 1, 2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer N, the number of components.
#
#    integer BASE(N), contains the number of degrees of
#    freedom of each component.  The output values of A will
#    satisfy 0 <= A(I) < BASE(I).
#
#    integer RANK, the desired rank, or order, of the element in
#    the list of all elements.  The rank count begins at 1 and extends
#    to MAXRANK = Product ( 1 <= I <= N ) BASE(I).
#
#  Output:
#
#    integer A(N), the product space element of the given rank.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  s = rank - 1

  for i in range ( n - 1, -1, -1 ):

    a[i] = ( s % base[i] )
    s = ( s // base[i] )

    if ( ( s % 2 ) == 1 ):
      a[i] = base[i] - a[i] - 1

  return a

def vec_gray_unrank_test ( ):

#*****************************************************************************80
#
## vec_gray_unrank_test() tests vec_gray_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  base = np.array ( [ 2, 2, 1, 4 ] )
  number = np.prod ( base )

  print ( '' )
  print ( 'vec_gray_unrank_test():' )
  print ( '  vec_gray_unrank() unranks product space elements.' )
  print ( '' )
  print ( '  The number of components is %d' % ( n ) )
  print ( '  The number of elements is %d' % ( number ) )
  print ( '  Each component has its own number of degrees of' )
  print ( '  freedom.' )

  rank = 7
  a = vec_gray_unrank ( n, base, rank )

  print ( '' )
  print ( '  vec_gray_unrank reports the element of rank %d:' % ( rank ) )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %d' % ( a[i] ), end = '' )
  print ( '' )

  return

def vec_lex_next ( dim_num, base, a, more ):

#*****************************************************************************80
#
## vec_lex_next() generates vectors in lex order.
#
#  Discussion:
#
#    The vectors are produced in lexical order, starting with
#    (0,0,...,0),
#    (0,0,...,1),
#    ...
#    (BASE-1,BASE-1,...,BASE-1).
#
#  Example:
#
#    DIM_nUM = 2,
#    BASE = 3
#
#    0   0
#    0   1
#    0   2
#    1   0
#    1   1
#    1   2
#    2   0
#    2   1
#    2   2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer DIM_nUM, the size of the vectors to be used.
#
#    integer BASE, the base to be used.  BASE = 2 will
#    give vectors of 0's and 1's, for instance.
#
#    integer A(DIM_nUM), except on the first call, this should
#    be the output value of A on the last call.
#
#    bool MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(DIM_nUM), the next vector.
#
#    bool MORE, is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  if ( not more ):

    for i in range ( 0, dim_num ):
      a[i] = 0
    more = True

  else:
      
    more = False
    for i in range ( dim_num - 1, -1, -1 ):

      a[i] = a[i] + 1

      if ( a[i] < base ):
        more = True
        break

      a[i] = 0

  return a, more

def vec_lex_next_test ( ):

#*****************************************************************************80
#
## vec_lex_next_test() tests vec_lex_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'vec_lex_next_test():' )
  print ( '  vec_lex_next() generates all DIM_nUM-vectors' )
  print ( '  in lex order in a given base BASE.' )
  
  dim_num = 3
  base = 3
  a = np.zeros ( dim_num )
  more = False

  print ( '' )
  print ( '  The spatial dimension DIM_nUM = %d' % ( dim_num ) )
  print ( '  The base BASE =                 %d' % ( base ) )
  print ( '' )

  while ( True ):

    a, more = vec_lex_next ( dim_num, base, a, more )

    if ( not more ):
      break

    i4vec_transpose_print ( dim_num, a, '' )

  return

def vec_random ( n, base ):

#*****************************************************************************80
#
## vec_random() selects a random N-vector of integers modulo a given base.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the vector to be generated.
#
#    integer BASE, the base to be used.
#
#  Output:
#
#    integer A(N), a list of N random values between
#    0 and BASE-1.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = rng.integers ( low = 0, high = base, size = n, endpoint = False )

  return a

def vec_random_test ( ):

#*****************************************************************************80
#
## vec_random_test() tests vec_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 3
  base = 3

  print ( '' )
  print ( 'vec_random_test():' )
  print ( '  vec_random() generates a random N-vector' )
  print ( '  in a given base.' )
  print ( '  Here, we use base %d' % ( base ) )
  print ( '' )

  for i in range ( 0, 5 ):
    a = vec_random ( n, base )
    for j in range ( 0, n ): 
      print ( '  %2d' % ( a[j] ), end = '' )
    print ( '' )

  return

def vector_constrained_next2 ( n, x_min, x_max, x, more ):

#*****************************************************************************80
#
## vector_constrained_next2() returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider all vectors of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_max(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      sum ( 1 <= I <= N ) ( X(I) / X_max(I) ) <= 1
#
#    We can carry out this check using integer arithmetic if we
#    multiply through by P = product ( X_max(1:N) ):
#
#      sum ( 1 <= I <= N ) ( X(I) * ( P / X_max(I) ) ) <= P.
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    X_MIN:   1   1   1
#    X_max:   5   6   4
#
#    P = 120
#
#    #  X(1)  X(2)  X(3)  CONSTRAINT
#
#    1    1     1     1       74
#    2    2     1     1       98
#    3    1     2     1       94
#    4    2     2     1      119
#    5    1     3     1      114
#    6    1     1     2      104
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
#    integer N, the number of components in the vector.
#
#    integer X_MIN(N), X_max(N), the minimum and maximum
#    values allowed in each component.
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
#  Output:
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    integer CONSTRAINT, the constraint value for X.  Valid vectors X
#    will have a CONSTRAINT value between product(X_MIN(1:N)) (automatically)
#    and product(X_max(1:N)) (because we skip over vectors with a
#    constraint larger than this value).
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  import numpy as np

  x_prod = np.prod ( x_max )

  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]

    constraint = 0.0
    for i in range ( 0, n):
      constraint = constraint + x[i] * ( x_prod / x_max[i] )

    if ( x_prod < constraint ):
      more = False
    else:
      more = True

    return x, constraint, more

  else:

    j = 1

    while ( True ):

      if ( x[j] < x_max[j] ):

        x[j] = x[j] + 1

        constraint = 0.0
        for i in range ( 0, n):
          constraint = constraint + x[i] * ( x_prod / x_max[i] )

        if ( constraint <= x_prod ):
          break

      x[j] = x_min[j]

      j = j + 1

      if ( n - 1 < j ):
        more = False
        break

  return x, constraint, more

def vector_constrained_next2_test ( ):

#*****************************************************************************80
#
## vector_constrained_next2_test() tests vector_constrained_next2().
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
  import numpy as np
 
  n_max = 3

  print ( '' )
  print ( 'vector_constrained_next2_test():' )
  print ( '  vector_constrained_next2():' )
  print ( '  Consider vectors:' )
  print ( '    X_MIN(1:N) <= X(1:N) <= X_max(1:N),' )
  print ( '  Set' )
  print ( '    P = Product X_max(1:N)' )
  print ( '  Accept only vectors for which:' )
  print ( '    sum ( X(1:N) * P / X_max(1:N) ) <= P' )

  x_min = np.array ( [ 1, 1, 1 ] )
  x_max = np.array ( [ 5, 6, 4 ] )

  for n in range ( 2, n_max + 1 ):

    more = False

    i4vec_transpose_print ( n, x_min, '  XMIN:' )
    i4vec_transpose_print ( n, x_max, '  XMAX:' )

    i = 0
    x_prod = np.prod ( x_max )

    print ( '' )
    print ( '  Maximum allowed CONSTRAINT = P =        %d' % ( x_prod ) )
    print ( '' )

    x = np.zeros ( n )

    while ( True ):

      x, constraint, more = vector_constrained_next2 ( n, x_min, x_max, x, \
        more )

      if ( not more ):
        break

      i = i + 1
      print ( '  %8d' % ( i ), end = '' )
      for j in range ( 0, n ):
        print ( '  %8d' % ( x[j] ), end = '' )
      print ( '  %12d' % ( constraint ) )

  return

def vector_constrained_next3 ( n, x_min, x_max, x, more ):

#*****************************************************************************80
#
## vector_constrained_next3() returns the "next" constrained vector.
#
#  Discussion:
#
#    This routine addresses the same problem as vector_constrained_next2,
#    and differs only in that real arithmetic is used, rather than
#    integer arithmetic.  Integer arithmetic allows us to do an exact
#    calculation, but we run into overflow problems in simple cases
#    where N is 10 and the X_max entries are of order 10, for instance.
#
#    We consider all vectors of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_max(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      sum ( 1 <= I <= N ) ( X(I) / X_max(I) ) <= 1
#
#  Example:
#
#    N = 3
#    X_MIN:   1   1   1
#    X_max:   5   6   4
#
#    P = 120
#
#    #  X(1)  X(2)  X(3)  CONSTRAINT
#
#    1    1     1     1      0.62
#    2    2     1     1      0.82
#    3    1     2     1      0.78
#    4    2     2     1      0.98
#    5    1     3     1      0.95
#    6    1     1     2      0.87
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components in the vector.
#
#    integer X_MIN(N), X_max(N), the minimum and maximum
#    values allowed in each component.
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
#  Output:
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    real CONSTRAINT, the constraint value for X.  
#    Valid vectors X will have a CONSTRAINT value between 
#      product(X_MIN(1:N)) / product(X_max(1:N))
#    and 1.0.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]

    constraint = 0.0
    for i in range ( 0, n ):
      constraint = constraint + float ( x[i] ) / float ( x_max[i] )

    if ( 1.0 < constraint ):
      more = False
    else:
      more = True

    return x, constraint, more

  else:

    j = 0

    while ( True ):

      if ( x[j] < x_max[j] ):

        x[j] = x[j] + 1

        constraint = 0.0
        for i in range ( 0, n ):
          constraint = constraint + float ( x[i] ) / float ( x_max[i] )

        if ( constraint <= 1.0 ):
          break

      x[j] = x_min[j]

      j = j + 1

      if ( n - 1 < j ):
        more = False
        break

  return x, constraint, more

def vector_constrained_next3_test ( ):

#*****************************************************************************80
#
## vector_constrained_next3_test() tests vector_constrained_next3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_max = 3

  print ( '' )
  print ( 'vector_constrained_next3_test():' )
  print ( '  vector_constrained_next3():' )
  print ( '  Consider vectors:' )
  print ( '    X_MIN(1:N) <= X(1:N) <= X_max(1:N),' )
  print ( '  Set' )
  print ( '    CONSTRAINT = sum ( X(1:N) / X_max(1:N) )' )
  print ( '  Accept only vectors for which:' )
  print ( '    CONSTRAINT <= 1' )

  x_min = np.array ( [ 1, 1, 1 ] )
  x_max = np.array ( [ 5, 6, 4 ] )

  for n in range ( 2, n_max + 1 ):

    more = False

    i4vec_transpose_print ( n, x_min, '  XMIN:' )
    i4vec_transpose_print ( n, x_max, '  XMAX:' )

    i = 0
    x_prod = np.prod ( x_max )

    print ( '' )
    print ( '  Maximum allowed CONSTRAINT = P =        %d' % ( x_prod ) )
    print ( '' )

    x = np.zeros ( n )

    while ( True ):

      x, constraint, more = vector_constrained_next3 ( n, x_min, x_max, x, \
        more )

      if ( not more ):
        break

      i = i + 1
      print ( '  %8d' % ( i ), end = '' )
      for j in range ( 0, n ):
        print ( '  %8d' % ( x[j] ), end = '' )
      print ( '  %12g' % ( constraint ) )

  return

def vector_constrained_next4 ( n, alpha, x_min, x_max, x, q, more ):

#*****************************************************************************80
#
## vector_constrained_next4() returns the "next" constrained vector.
#
#  Discussion:
#
#    This routine is similar to vector_constrained_next2 and 
#    vector_constrained_next3.
#
#    We consider all vectors X of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_max(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      sum ( 1 <= I <= N ) ALPHA(I) * X(I) <= Q
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    ALPHA    4.0  3.0  5.0
#    Q       20.0
#    X_MIN:   1   1   1
#    X_max:   5   6   4
#
#    #  X(1)  X(2)  X(3)     Total
#
#    1    1     1     1       12.0
#    2    2     1     1       20.0
#    3    1     2     1       15.0
#    4    2     2     1       19.0
#    5    1     3     1       18.0
#    6    1     1     2       17.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components in the vector.
#
#    real ALPHA(N), the coefficient vector.
#
#    integer X_MIN(N), X_max(N), the minimum and maximum
#    values allowed in each component.
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#
#    real Q, the limit on the sum.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.
#
#  Output:
#
#    integer X(N).  On (with MORE = TRUE), the value of
#    X will be the "next" vector in the reverse lexicographical list of 
#    vectors that satisfy the condition.  However, on output with 
#    MORE = FALSE, the vector X is meaningless, because there are no 
#    more vectors in the list.
#
#    bool MORE.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]

    total = 0.0
    for i in range ( 0, n ):
      total = total + alpha[i] * x[i]

    if ( q < total ):
      more = False
    else:
      more = True

    return x, more

  else:

    j = 0

    while ( True ):

      if ( x[j] < x_max[j] ):

        x[j] = x[j] + 1

        total = 0.0
        for i in range ( 0, n ):
          total = total + alpha[i] * x[i]

        if ( total <= q ):
          break

      x[j] = x_min[j]

      j = j + 1

      if ( n - 1 < j ):
        more = False
        break

  return x, more

def vector_constrained_next4_test ( ):

#*****************************************************************************80
#
## vector_constrained_next4_test() tests vector_constrained_next4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_max = 3

  alpha = np.array ( [ 4.0, 3.0, 5.0 ] )
  x_max = np.array ( [ 2, 6, 4 ] )
  x_min = np.array ( [ 1, 0, 1 ] )

  print ( '' )
  print ( 'vector_constrained_next4_test():' )
  print ( '  vector_constrained_next4():' )
  print ( '  Consider vectors:' )
  print ( '    X_MIN(1:N) <= X(1:N) <= X_max(1:N),' )
  print ( '  Set' )
  print ( '    TOTAL = sum ( ALPHA(1:N) * X(1:N) )' )
  print ( '  Accept only vectors for which:' )
  print ( '    TOTAL <= Q' )

  for n in range ( 2, n_max + 1 ):

    x = np.zeros ( n )
    q = 20.0
    more = False

    print ( '' )
    print ( '  ALPHA:', end = '' )
    for i in range ( 0, n ):
      print ( '  %14f' % ( alpha[i] ), end = '' )
    print ( '' )
    print ( '  Q:    %14f' % ( q ) )

    i4vec_transpose_print ( n, x_min, '  XMIN:' )
    i4vec_transpose_print ( n, x_max, '  XMAX:' )

    print ( '' )

    j = 0

    while ( True ):

      x, more = vector_constrained_next4 ( n, alpha, x_min, x_max, x, q, more )

      if ( not more ):
        break

      total = 0.0
      for i in range ( 0, n ):
        total = total + alpha[i] * x[i]
      j = j + 1
      print ( '  %8d  %14f' % ( j, total ), end = '' )
      for i in range ( 0, n ):
        print ( '  %8d' % ( x[i] ), end = '' )
      print ( '' )

  return

def vector_constrained_next5 ( n, x, sum_min, sum_max, base, more ):

#*****************************************************************************80
#
## vector_constrained_next5() returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider all positive integer vectors of dimension N whose
#    components satisfy SUM_MIN <= X(1:N) <= SUM_max.
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    SUM_MIN = 5
#    SUM_max = 6
#
#    #  X(1)  X(2)  X(3)     SUM
#
#    1    3     1     1        5
#    2    2     2     1        5
#    3    2     1     2        5
#    4    1     3     1        5
#    5    1     2     2        5
#    6    1     1     3        5
#
#    7    4     1     1        6
#    8    3     2     1        6
#    9    3     1     2        6
#   10    2     3     1        6
#   11    2     2     2        6
#   12    2     1     3        6
#   13    1     4     1        6
#   14    1     3     2        6
#   15    1     2     3        6
#   16    1     1     4        6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components in the vector.
#
#    integer SUM_MIN, SUM_max, the minimum and maximum sums..
#
#    integer X(N).   On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#
#    integer BASE, a bookkeeping variable which is used only by
#    this function, but which must be declared by the calling program.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  
#
#  Output:
#
#    integer X(N).  If MORE = TRUE, the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    integer BASE, a bookkeeping variable.
#
#    bool MORE.  If MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#

#
#  Initialization.
#
  if ( not more ):

    if ( sum_max < n ):
      more = False
      return x, base, more

    if ( sum_max < sum_min ):
      more = False
      return x, base, more

    more = True

    base = max ( sum_min, n )

    x[0] = base - n + 1
    for i in range ( 1, n ):
      x[i] = 1

    return x, base, more
#
#  Next element.
#
  else:
#
#  Search from the right, seeking an index I < N for which 1 < X(I).
#
    for i in range ( n - 2, -1, -1 ):
#
#  If you find such an I, decrease X(I) by 1, and add that to X(I+1).
#
      if ( 1 < x[i] ):

        x[i]   = x[i]   - 1
        x[i+1] = x[i+1] + 1
#
#  Now grab all the "excess" 1's from the entries to the right of X(I+1).
#
        for j in range ( i + 2, n ):
          if ( 1 < x[j] ):
            x[i+1] = x[i+1] + x[j] - 1
            x[j] = 1

        return x, base, more
#
#  The current vector is (1,1,1,...,BASE-N+1).
#  If BASE < SUM_max, then increase BASE by 1, and start the new series.
#
    if ( base < sum_max ):
      base = base + 1
      x[0] = base - n + 1
      for i in range ( 1, n ):
        x[i] = 1
      return x, base, more
#
#  We returned the last legal vector on the previous call.
#  The calculation is done.
#
    more = False

  return x, base, more

def vector_constrained_next5_test ( ):

#*****************************************************************************80
#
## vector_constrained_next5_test() tests vector_constrained_next5().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vector_constrained_next5_test():' )
  print ( '  vector_constrained_next5():' )
  print ( '  Generate integer vectors X such that:' )
  print ( '    SUM_MIN <= sum ( X(1:N) ) <= SUM_max,' )
  print ( '  We require every X(I) to be at least 1.' )

  n = 3
  sum_min = 5
  sum_max = 7
  base = 0
  more = False

  print ( '' )
  print ( '  N =       %d' % ( n ) )
  print ( '  SUM_MIN = %d' % ( sum_min ) )
  print ( '  SUM_max = %d' % ( sum_max ) )
  print ( '' )
  print ( '         #        X(1)      X(2)      X(3)' )
  print ( '' )

  i = 0
  x = np.zeros ( n )
  
  while ( True ):

    x, base, more = vector_constrained_next5 ( n, x, sum_min, sum_max, base, more )

    if ( not more ):
      break

    i = i + 1
    print ( '  %8d:' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '  %8d' % ( x[j] ), end = '' )
    print ( '' )

  return

def vector_constrained_next6 ( n, alpha, x_min, x_max, x, q_min, q_max, more ):

#*****************************************************************************80
#
## vector_constrained_next6() returns the "next" constrained vector.
#
#  Discussion:
#
#    This routine is similar to vector_constrained_next2,
#    vector_constrained_next3, and vector_constrained_next4.
#
#    We consider all vectors X of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_max(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      Q_MIN <= sum ( 1 <= I <= N ) ALPHA(I) * X(I) <= Q_max
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    ALPHA    4.0  3.0  5.0
#    Q_MIN   16.0
#    Q_max   20.0
#    X_MIN:   1   1   1
#    X_max:   5   6   4
#
#    #  X(1)  X(2)  X(3)     Total
#
#    1    2     1     1       20.0
#    2    2     2     1       19.0
#    3    1     3     1       18.0
#    4    1     1     2       17.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components in the vector.
#
#    real ALPHA(N), the coefficient vector.
#
#    integer X_MIN(N), X_max(N), the minimum and maximum
#    values allowed in each component.
#
#    integer X(N), the output value of X from the previous call.
#    On first call, the user must set X = []
#
#    real Q_MIN, Q_max, the lower and upper
#    limits on the sum.
#
#    bool MORE, should be FALSE on the first call, and
#    TRUE thereafter.
#
#  Output:
#
#    integer X(N), (with MORE = TRUE), the value of X will be 
#    the "next" vector in the reverse lexicographical list of vectors 
#    that satisfy the condition.  However, on output with MORE = FALSE, 
#    the vector X is meaningless, because there are no more vectors 
#    in the list.
#
#    bool MORE is TRUE if the next value of X was found, and
#    FALSE if there were no more values of X to compute.  
#
  if ( not more ):

    more = True

    for i in range ( 0, n ):
      x[i] = x_min[i]

    total = 0.0
    for i in range ( 0, n ):
      total = total + alpha[i] * x[i]

    if ( q_min <= total and total <= q_max ):
      return x, more

  while ( True ):

    j = n - 1

    while ( True ):

      if ( x[j] < x_max[j] ):
        break

      if ( j <= 0 ):
        more = False
        return x, more

      j = j - 1

    x[j] = x[j] + 1
    for i in range ( j + 1, n ):
      x[i] = x_min[i]

    total = 0.0
    for i in range ( 0, n ):
      total = total + alpha[i] * x[i]

    if ( q_min <= total and total <= q_max ):
      break

  return x, more

def vector_constrained_next6_test ( ):

#*****************************************************************************80
#
## vector_constrained_next6_test() tests vector_constrained_next6().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vector_constrained_next6_test():' )
  print ( '  vector_constrained_next6():' )
  print ( '  Consider vectors:' )
  print ( '    X_MIN(1:N) <= X(1:N) <= X_max(1:N),' )
  print ( '  Set' )
  print ( '    TOTAL = sum ( ALPHA(1:N) * X(1:N) )' )
  print ( '  Accept only vectors for which:' )
  print ( '    Q_MIN <= TOTAL <= Q_max' )

  for n in range ( 2, 4 ):

    if ( n == 2 ):
      alpha = np.array ( [ 4.0, 3.0 ] )
      x_min = np.array ( [ 1, 0 ] )
      x_max = np.array ( [ 2, 6 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False
    elif ( n == 3 ):
      alpha = np.array ( [ 4.0, 3.0, 5.0 ] )
      x_min = np.array ( [ 1, 0, 1 ] )
      x_max = np.array ( [ 2, 6, 4 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False

    print ( '' )
    print ( '  ALPHA:', end = '' )
    for i in range ( 0, n ):
      print ( '  %14f' % ( alpha[i] ), end = '' )
    print ( '' )
    print ( '' )
    print ( '  Q_MIN:%14f' % ( q_min ) )
    print ( '  Q_max:%14f' % ( q_max ) )
    print ( '  X_MIN:', end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x_min[i] ), end = '' )
    print ( '' )
    print ( '  X_max:', end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x_max[i] ), end = '' )
    print ( '' )
    print ( '' )

    rank = 0

    while ( True ):

      x, more = vector_constrained_next6 ( n, alpha, x_min, x_max, x, \
        q_min, q_max, more )

      if ( not more ):
        break
 
      total = 0.0
      for i in range ( 0, n ):
        total = total + alpha[i] * x[i]

      rank = rank + 1
      print ( '  %8d  %14f' % ( rank, total ), end = '' )
      for i in range ( 0, n ):
        print ( '  %8d' % ( x[i] ), end = '' )
      print ( '' )

  return

def vector_constrained_next7 ( n, level_weight, x_max, x, q_min, q_max, more ):

#*****************************************************************************80
#
## vector_constrained_next7() returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider vectors X of dimension N satisfying:
#
#      0 <= X(1:N) <= X_max(1:N).
#
#    and the following constraint:
#
#      Q_MIN < sum ( 1 <= I <= N ) LEVEL_WEIGHT(I) * X(I) <= Q_max
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    LEVEL_WEIGHT    4.0  3.0  5.0
#    Q_MIN   16.0
#    Q_max   20.0
#    X_max:   5   6   4
#
#    #  X(1)  X(2)  X(3)     Total
#
#    1    3     1     1       20.0
#    2    2     2     1       19.0
#    3    1     3     1       18.0
#    4    1     1     2       17.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components in the vector.
#
#    real LEVEL_WEIGHT(N), the coefficient vector.
#
#    integer X_max(N), the maximum
#    values allowed in each component.
#
#    integer X(N).  On first call, with
#    MORE = FALSE, the input value of X is not important.  On subsequent calls,
#    the input value of X should be the output value from the previous call.
#
#    real Q_MIN, Q_max, the lower and upper
#    limits on the sum.
#
#    bool MORE.  If the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  
#
#  Output:
#
#    integer X(N), (with MORE = TRUE), the value of X will be 
#    the "next" vector in the reverse lexicographical list of vectors 
#    that satisfy the condition.  However, on output with MORE = FALSE, 
#    the vector X is meaningless, because there are no more vectors 
#    in the list.
#
#    bool MORE is TRUE if the next value of X was found, and
#    FALSE if there were no more values of X to compute.  
#
  if ( not more ):

    more = True

    for i in range ( 0, n ):
      x[i] = 0

    total = 0.0
    for i in range ( 0, n ):
      total = total + level_weight[i] * x[i]

    if ( q_min < total and total <= q_max ):
      return x, more

  while ( True ):

    j = n - 1

    while ( True ):

      if ( x[j] < x_max[j] ):
        break

      if ( j <= 0 ):
        more = False
        return x, more

      j = j - 1

    x[j] = x[j] + 1
    for i in range ( j + 1, n ):
      x[i] = 0

    total = 0.0
    for i in range ( 0, n ):
      total = total + level_weight[i] * x[i]

    if ( q_min < total and total <= q_max ):
      break

  return x, more

def vector_constrained_next7_test ( ):

#*****************************************************************************80
#
## vector_constrained_next7_test() tests vector_constrained_next7().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vector_constrained_next7_test():' )
  print ( '  vector_constrained_next7():' )
  print ( '  Consider vectors:' )
  print ( '    0 <= X(1:N) <= X_max(1:N),' )
  print ( '  Set' )
  print ( '    TOTAL = sum ( ALPHA(1:N) * X(1:N) )' )
  print ( '  Accept only vectors for which:' )
  print ( '    Q_MIN <= TOTAL <= Q_max' )

  for n in range ( 2, 4 ):

    if ( n == 2 ):
      alpha = np.array ( [ 4.0, 3.0 ] )
      x_max = np.array ( [ 2, 6 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False
    elif ( n == 3 ):
      alpha = np.array ( [ 4.0, 3.0, 5.0 ] )
      x_max = np.array ( [ 2, 6, 4 ] )
      x = np.zeros ( n )
      q_min = 16.0
      q_max = 20.0
      more = False

    print ( '' )
    print ( '  ALPHA:', end = '' )
    for i in range ( 0, n ):
      print ( '  %14f' % ( alpha[i] ), end = '' )
    print ( '' )
    print ( '' )
    print ( '  Q_MIN:%14f' % ( q_min ) )
    print ( '  Q_max:%14f' % ( q_max ) )
    print ( '  X_max:', end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( x_max[i] ), end = '' )
    print ( '' )
    print ( '' )

    rank = 0

    while ( True ):

      x, more = vector_constrained_next7 ( n, alpha, x_max, x, q_min, q_max, more )

      if ( not more ):
        break
 
      total = 0.0
      for i in range ( 0, n ):
        total = total + alpha[i] * x[i]

      rank = rank + 1
      print ( '  %8d  %14f' % ( rank, total ), end = '' )
      for i in range ( 0, n ):
        print ( '  %8d' % ( x[i] ), end = '' )
      print ( '' )

  return

def vector_constrained_next ( n, x_min, x_max, x, more ):

#*****************************************************************************80
#
## vector_constrained_next() returns the "next" constrained vector.
#
#  Discussion:
#
#    We consider all vectors of dimension N whose components
#    satisfy X_MIN(1:N) <= X(1:N) <= X_max(1:N).
#
#    We are only interested in the subset of these vectors which
#    satisfy the following constraint:
#
#      sum ( 1 <= I <= N ) ( ( X(I) - 1 ) / X_max(I) ) <= 1
#
#    We can carry out this check using integer arithmetic if we
#    multiply through by P = product ( X_max(1:N) ):
#
#      sum ( 1 <= I <= N ) ( ( X(I) - 1 ) * ( P / X_max(I) ) ) <= P.
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, exactly those vectors which satisfy
#    the constraint.
#
#  Example:
#
#    N = 3
#    X_MIN:   2   2   1
#    X_max:   4   5   3
#
#    P = 60
#
#    #  X(1)  X(2)  X(3)  CONSTRAINT
#
#    1    2     2     1       27
#    2    3     2     1       42
#    3    4     2     1       57
#    4    2     3     1       39
#    5    3     3     1       54
#    6    2     4     1       51
#    7    2     2     2       47
#    8    2     3     2       59
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components in the vector.
#
#    integer X_MIN(N), X_max(N), the minimum and maximum
#    values allowed in each component.
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
#  Output:
#
#    integer X(N).  On first call (with MORE = FALSE),
#    the input value of X is not important.  On subsequent calls, the
#    input value of X should be the output value from the previous call.
#    On (with MORE = TRUE), the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors that satisfy
#    the condition.  However, on output with MORE = FALSE, the vector
#    X is meaningless, because there are no more vectors in the list.
#
#    integer CONSTRAINT, the constraint value for X.  Valid vectors X
#    will have a CONSTRAINT value between product(X_MIN(1:N)) (automatically)
#    and product(X_max(1:N)) (because we skip over vectors with a
#    constraint larger than this value).
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.  On if MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  import numpy as np

  x_prod = np.prod ( x_max )

  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]

    constraint = 0.0
    for i in range ( 0, n ):
      constraint = constraint + ( x[i] - 1 ) * ( x_prod / x_max[i] )

    if ( x_prod < constraint ):
      more = False
    else:
      more = True

  else:

    j = 0

    while ( True ):

      if ( x[j] < x_max[j] ):

        x[j] = x[j] + 1

        constraint = 0.0
        for i in range ( 0, n ):
          constraint = constraint + ( x[i] - 1 ) * ( x_prod / x_max[i] )

        if ( constraint <= x_prod ):
          break

      x[j] = x_min[j]

      j = j + 1

      if ( n - 1 < j ):
        more = False
        break

  return x, constraint, more

def vector_constrained_next_test ( ):

#*****************************************************************************80
#
## vector_constrained_next_test() tests vector_constrained_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'vector_constrained_next_test():' )
  print ( '  vector_constrained_next():' )
  print ( '  Consider vectors:' )
  print ( '    X_MIN(1:N) <= X(1:N) <= X_max(1:N),' )
  print ( '  Set' )
  print ( '    P = Product X_max(1:N)' )
  print ( '  Accept only vectors for which:' )
  print ( '    sum ( (X(1:N)-1) * P / X_max(1:N) ) <= P' )

  more = False
  x_min = np.array ( [ 2, 2, 1 ] )
  x_max = np.array ( [ 4, 5, 3 ] )

  i4vec_transpose_print ( n, x_min, '  XMIN:' )
  i4vec_transpose_print ( n, x_max, '  XMAX:' )

  i = 0
  x_prod = np.prod ( x_max )

  print ( '' )
  print ( '  Maximum allowed CONSTRAINT = P =        %d' % ( x_prod ) )
  print ( '' )

  x = np.zeros ( n )

  while ( True ):

    x, constraint, more = vector_constrained_next ( n, x_min, x_max, x, more )

    if ( not more ):
      break

    i = i + 1
    print ( '  %8d:  %8d  %8d  %8d  %12d' % ( i, x[0], x[1], x[2], constraint ) )

  return

def vector_next ( n, x_min, x_max, x, more ):

#*****************************************************************************80
#
## vector_next() returns the "next" integer vector between two ranges.
#
#  Discussion:
#
#    We consider all integer vectors of dimension N satisfying:
#
#      X_MIN(1:N) <= X(1:N) <= X_max(1:N).
#
#    This routine returns, one at a time, and in right-to-left
#    lexicographic order, all these vectors.
#
#  Example:
#
#    N = 3
#    X_MIN:   2   2   0
#    X_max:   4   3   1
#
#    #  X(1)  X(2)  X(3)
#
#    1    2     2     0
#    2    3     2     0
#    3    4     2     0
#    4    2     3     0
#    5    3     3     0
#    6    4     3     0
#    7    2     2     1
#    8    3     2     1
#    9    4     2     1
#   10    2     3     1
#   11    3     3     1
#   12    4     3     1
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
#  Input:
#
#    integer N, the number of components in the vector.
#
#    integer X_MIN(N), X_max(N), the minimum and maximum
#    values allowed in each component.
#
#    integer X(N).  On first call, with
#    MORE = FALSE, the input value of X is not important.  On subsequent calls,
#    the input value of X should be the output value from the previous call.
#
#    bool MORE.  On if the user has set MORE
#    FALSE, the user is requesting the initiation of a new sequence
#    of values.  If MORE is TRUE, then the user is requesting "more"
#    values in the current sequence.
#
#  Output:
#
#    integer X(N).  If MORE = TRUE, the value of X will be the "next"
#    vector in the reverse lexicographical list of vectors.  However, on
#    output with MORE = FALSE, the vector X is meaningless, because there
#    are no more vectors in the list.
#
#    bool MORE.  If MORE is TRUE,
#    then another value was found and returned in X, but if MORE is
#    FALSE, then there are no more values in the sequence, and X is
#    NOT the next value.
#
  if ( not more ):

    for i in range ( 0, n ):
      x[i] = x_min[i]
    more = True

  else:

    i = 0

    while ( True ):

      if ( x[i] < x_max[i] ):
        x[i] = x[i] + 1
        more = True
        break
      else:
        x[i] = x_min[i]
        i = i + 1
        if ( n <= i ):
          more = False
          break

  return x, more

def vector_next_test ( ):

#*****************************************************************************80
#
## vector_next_test() tests vector_next().
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

  n_max = 3

  x_min = np.array ( [ 1, 4, 3 ] )
  x_max = np.array ( [ 2, 6, 4 ] )

  print ( '' )
  print ( 'vector_next_test():' )
  print ( '  vector_next() generates all vectors X such that:' )
  print ( '  X_MIN(1:N) <= X(1:N) <= X_max(1:N)' )

  for n in range ( 2, n_max + 1 ):

    more = False

    print ( '' )
    print ( '  X_MIN: ', end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( x_min[i] ), end = '' )
    print ( '' )

    k = 0
    x = np.zeros ( n )

    while ( True ):

      x, more = vector_next ( n, x_min, x_max, x, more )

      if ( not more ):
        break

      k = k + 1

      print ( '  X(%2d): ' % ( k ), end = '' )
      for i in range ( 0, n ):
        print ( '  %4d' % ( x[i] ), end = '' )
      print ( '' )

    print ( '  X_max: ', end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( x_max[i] ), end = '' )
    print ( '' )

  return

def vector_sumlex_next ( x ):

#*****************************************************************************80
#
## vector_sumlex_next() returns the next integer vector in sumlex order.
#
#  Discussion:
#
#    Consider integer vectors of length N, ordered by their sum.
#    Vectors of equal sum are ordered lexically.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X(N), the current vector.
#
#  Output:
#
#    integer X(N), the next vector.
#
  import numpy as np

  s = np.sum ( x )
  n = len ( x )
#
#  Case:  (0,0,0,...0,S) -> (S+1,0,0,...,0)
#
  if ( x[0] == s ):
    x[0] = 0
    x[n-1] = s + 1
#
#  Case: 
#    Rightmost nonzero sends one unit left, and the rest to last position.
#
  else:

    t = 0

    for j in range ( n - 1, 0, -1 ):

      if ( x[j] != 0 ):
        t = x[j]
        x[j] = 0
        x[j-1] = x[j-1] + 1
        x[n-1] = t - 1
        break

    if ( t == 0 ):
      print ( '' )
      print ( 'vector_sumlex_next(): Fatal error!' )
      print ( '  Could not find an entry to borrow from.' )
      raise Exception ( 'vector_sumlex_next(): Fatal error!' )

  return x

def vector_sumlex_next_test ( ):

#*****************************************************************************80
#
## vector_sumlex_next_test() tests vector_sumlex_next_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'vector_sumlex_next_test():' )
  print ( '  vector_sumlex_next() generates integer vectors of dimension n.' )
  print ( '  The vectors are listed in order by the sum of their entries.' )
  print ( '  For a given sum, vectors are listed in lexicographic order.' )

  n = 4
  x = np.zeros ( n )
  
  for i in range ( 0, 31 ):

    print ( '  %2d:  (' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '%d' % ( x[j] ), end = '' )
      if ( j < n - 1 ):
        print ( ',', end = '' )
      else:
        print ( ')' )

    x = vector_sumlex_next ( x )

  return

def ytb_conjugate ( n, a ):

#*****************************************************************************80
#
## ytb_conjugate() conjugates a Young tableau.
#
#  Discussion:
#
#    A Young tableau is also known as a Ferrers diagram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer that is partitioned.
#
#    integer A(N), describes the Young tableau.
#    A(I) is the row of the tableau on which I occurs.
#
#  Output:
#
#    integer AC(N), describes the conjugate Young tableau.
#
  import numpy as np

  ac = np.zeros ( n, dtype = int )

  row = 0

  while ( True ):

    row = row + 1

    col = 0

    for j in range ( 0, n ):

      if ( a[j] == row ):
        col = col + 1
        ac[j] = col

    if ( col == 0 ):
      break

  return ac

def ytb_conjugate_test ( ):

#*****************************************************************************80
#
## ytb_conjugate_test() tests ytb_conjugate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ytb_conjugate_test():' )
  print ( '  ytb_conjugate() conjugates a Young tableau.' )

  n = 6
  a = np.array ( [ 1, 1, 2, 2, 3, 1 ] )
  ytb_print ( n, a, '  A Young tableau:' )

  ac = ytb_conjugate ( n, a )
  ytb_print ( n, ac, '  The conjugate Young tableau:' )

  return

def ytb_enum ( n ):

#*****************************************************************************80
#
## ytb_enum() enumerates the Young tableaus of size N.
#
#  Discussion:
#
#    If A(N) is the number of Young tableau of size N, then A(1) = 1,
#    A(2) = 2, and
#
#    A(N) = A(N-1) + (N-1) * A(N-2).
#
#    A Young tableau is also known as a Ferrers diagram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer which is to be partitioned.
#
#  Output:
#
#    integer VALUE, the number of Young tableaus of N.
#
  if ( n <= 0 ):
    value = 0
  elif ( n == 1 ):
    value = 1
  elif ( n == 2 ):
    value = 2
  else:
    a2 = 1
    a3 = 2
    for i in range ( 2, n ):
      a1 = a2
      a2 = a3
      a3 = a2 + i * a1
    value = a3

  return value

def ytb_enum_test ( ):

#*****************************************************************************80
#
## ytb_enum_test() tests ytb_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'ytb_enum_test():' )
  print ( '  ytb_enum() counts Young tableaus.' )
  print ( '' )
  print ( '   N       YTB(N)' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    value = ytb_enum ( i )
    print ( '  %2d  %8d' % ( i, value ) )

  return

def ytb_next ( n, lam, a, more ):

#*****************************************************************************80
#
## ytb_next() computes the next Young tableau for a given shape.
#
#  Discussion:
#
#    When the routine is called with MORE = FALSE (the first time), and
#    if LAM on this call has M parts, with M < N, then the user
#    must also make sure that LAM(M+1) = 0.
#
#    A Young tableau is also known as a Ferrers diagram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
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
#    integer N, the integer which is to be partitioned.
#
#    integer LAM(N), contains a partition of N.
#    The elements of LAM are nonnegative integers that sum to N.
#    On the first call, with MORE = FALSE, the user sets LAM.
#    After the first call, the input value of LAM is not important.
#
#    integer A(N).  On the first call, with MORE = FALSE,
#    no value of A needs to be set.  After the first call, the input
#    value of A should be the output value of A from the previous call.
#
#    bool MORE.  Set MORE to FALSE before the first call.
#    Thereafter, set it to the output value of MORE on the previous call.
#
#  Output:
#
#    integer LAM(N), contains the partition of N,
#    corresponding to the Young tableau.
#
#    integer A(N), the next Young tableau.  A(I) is the
#    row containing I in the output tableau.
#
#    bool MORE, is TRUE until the last tableau is returned,
#    when the value of MORE is FALSE.
#
  it = n

  if ( more ):

    lam[0] = 1
    for i in range ( 1, n ):
      lam[i] = 0

    isave = 0

    for i in range ( 2, n + 1 ):

      lam[a[i-1]-1] = lam[a[i-1]-1] + 1

      if ( a[i-1] < a[i-2] ):
        isave = i
        break

    if ( isave == 0 ):
      more = False
      return lam, a, more

    it = lam[1+a[isave-1]-1]

    for i in range ( n, 0, -1 ):

      if ( lam[i-1] == it ):
        a[isave-1] = i
        lam[i-1] = lam[i-1] - 1
        it = isave - 1
        break

  k = 1
  ir = 1

  while ( True ):

    if ( n < ir ):
      break

    if ( lam[ir-1] != 0 ):
      a[k-1] = ir
      lam[ir-1] = lam[ir-1] - 1
      k = k + 1
      ir = ir + 1
      continue

    if ( it < k ):
      break

    ir = 1

  if ( n == 1 ):
    more = False
    return lam, a, more

  for j in range ( 2, n + 1 ):
    if ( a[j-1] < a[j-2] ):
      more = True
      return lam, a, more

  more = False

  return lam, a, more

def ytb_next_test ( ):

#*****************************************************************************80
#
## ytb_next_test() tests ytb_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ytb_next_test():' )
  print ( '  ytb_next() generates Young tableaus.' )

  n = 6
  lam = np.array ( [ 3, 2, 1, 0, 0, 0 ], dtype = int )
  a = np.zeros ( n, dtype = int )
  more = False
 
  while ( True ):
 
    lam, a, more = ytb_next ( n, lam, a, more )
 
    ytb_print ( n, a, '' )
 
    if ( not more ):
      break

  return

def ytb_print ( n, a, title ):

#*****************************************************************************80
#
## ytb_print() prints a Young tableau.
#
#  Discussion:
#
#    A Young tableau is also known as a Ferrers diagram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer that is partitioned.
#
#    integer A(N), describes the Young tableau.
#    A[I-1] is the row of the tableau on which I occurs.
#
#    string TITLE, an optional title.
#
  print ( '' )
  if ( 0 < len ( title ) ):
    print ( title )

  row = 0

  while ( True ):

    row = row + 1

    row_length = 0

    for jm1 in range ( 0, n ):

      j = jm1 + 1

      if ( a[jm1] == row ):
        row_length = row_length + 1
        print ( '%4d  ' % ( j ), end = '' )

    if ( row_length <= 0 ):
      break
    else:
      print ( '' )

  return

def ytb_print_test ( ):

#*****************************************************************************80
#
## ytb_print_test() tests ytb_print().
#
#  Discussion:
#
#    A Young tableau is also known as a Ferrers diagram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ytb_print_test():' )
  print ( '  ytb_print() prints a Young tableau.' )

  n = 6
  a = np.array ( [ 1, 1, 2, 2, 3, 1 ], dtype = int )
  ytb_print ( n, a, '  A Young tableau:' )

  return

def ytb_random ( n, lam, rng ):

#*****************************************************************************80
#
## ytb_random() selects a random Young tableau of a given shape.
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
#    integer N, the integer which has been partitioned.
#
#    integer LAM(N), the partition of N.
#    N = sum ( 1 <= I <= N ) LAM(I).
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(N), the vector describing the Young tableau.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  i = 0
  k = 0

  while ( True ):

    for j in range ( 0, lam[i] ):
      a[j] = a[j] + 1
      k = k + 1

    i = i + 1

    if ( n <= k ):
      break

  for m in range ( 0, n ):

    while ( True ):

      i = rng.integers ( low = 1, high = a[0], endpoint = True )
      im1 = i - 1
      j = rng.integers ( low = 1, high = lam[0], endpoint = True )
      jm1 = j - 1

      if ( i <= a[jm1] and j <= lam[im1] ):
        break

    while ( True ):

      ih = a[jm1] + lam[im1] - i - j

      if ( ih == 0 ):
        break;

      k = rng.integers ( low = 1, high = ih, endpoint = True )

      if ( k <= lam[im1] - j ):
        j = j + k
        jm1 = j - 1
      else:
        i = k - lam[im1] + i + j
        im1 = i - 1

    lam[im1] = lam[im1] - 1
    a[jm1] = a[jm1] - 1
    a[n-1-m] = i

  for i in range ( 0, n ):
    lam[a[i]-1] = lam[a[i]-1] + 1

  return a

def ytb_random_test ( rng ):

#*****************************************************************************80
#
## ytb_random_test() tests ytb_random().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'ytb_random_test():' )
  print ( '  ytb_random() generates a random Young tableau' )

  n = 6
  lam = np.array ( [ 3, 2, 1, 0, 0, 0 ], dtype = np.int32 )

  for i in range ( 0, 5 ):
 
    a = ytb_random ( n, lam, rng )
    ytb_print ( n, a, '' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  subset_test ( )
  timestamp ( )

