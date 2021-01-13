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

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from subset.agm_values import agm_values_test
from subset.asm_enum import asm_enum_test
from subset.asm_triangle import asm_triangle_test
from subset.bell import bell_test
from subset.bell_values import bell_values_test
from subset.catalan import catalan_test
from subset.catalan_row_next import catalan_row_next_test
from subset.catalan_values import catalan_values_test
from subset.cfrac_to_rat import cfrac_to_rat_test
from subset.cfrac_to_rfrac import cfrac_to_rfrac_test
from subset.ch_to_digit import ch_to_digit_test
from subset.change_greedy import change_greedy_test
from subset.change_next import change_next_test
from subset.chinese_check import chinese_check_test
from subset.comb_next import comb_next_test
from subset.comb_row_next import comb_row_next_test
from subset.comb_unrank import comb_unrank_test
from subset.comp_enum import comp_enum_test
from subset.comp_next import comp_next_test
from subset.comp_next_grlex import comp_next_grlex_test
from subset.comp_random_grlex import comp_random_grlex_test
from subset.comp_rank_grlex import comp_rank_grlex_test
from subset.comp_to_ksub import comp_to_ksub_test
from subset.comp_unrank_grlex import comp_unrank_grlex_test
from subset.compnz_enum import compnz_enum_test
from subset.compnz_next import compnz_next_test
from subset.compnz_to_ksub import compnz_to_ksub_test
from subset.compnz_random import compnz_random_test
from subset.congruence import congruence_test
from subset.count_pose_random import count_pose_random_test
from subset.debruijn import debruijn_test
from subset.dec_add import dec_add_test
from subset.dec_div import dec_div_test
from subset.dec_mul import dec_mul_test
from subset.dec_round import dec_round_test
from subset.dec_to_r8 import dec_to_r8_test
from subset.dec_to_rat import dec_to_rat_test
from subset.dec_to_s import dec_to_s_test
from subset.dec_width import dec_width_test
from subset.derange_enum import derange_enum_test
from subset.derange_enum2 import derange_enum2_test
from subset.derange_enum3 import derange_enum3_test
from subset.derange0_back_next import derange0_back_next_test
from subset.derange0_check import derange0_check_test
from subset.derange0_weed_next import derange0_weed_next_test
from subset.digit_to_ch import digit_to_ch_test
from subset.digraph_arc_euler import digraph_arc_euler_test
from subset.digraph_arc_print import digraph_arc_print_test
from subset.diophantine import diophantine_test
from subset.diophantine_solution_minimize import diophantine_solution_minimize_test
from subset.dvec_add import dvec_add_test
from subset.dvec_complementx import dvec_complementx_test
from subset.dvec_mul import dvec_mul_test
from subset.dvec_print import dvec_print_test
from subset.dvec_sub import dvec_sub_test
from subset.equiv_print import equiv_print_test
from subset.equiv_print2 import equiv_print2_test
from subset.equiv0_next import equiv0_next_test
from subset.equiv0_random import equiv0_random_test
from subset.equiv1_next import equiv1_next_test
from subset.equiv1_next2 import equiv1_next2_test
from subset.euler_row import euler_row_test
from subset.frobenius_number_order2 import frobenius_number_order2_test
from subset.frobenius_number_order2_values import frobenius_number_order2_values_test
from subset.gamma_values import gamma_values_test
from subset.gamma_log_values import gamma_log_values_test
from subset.gray_next import gray_next_test
from subset.gray_rank2 import gray_rank2_test
from subset.gray_unrank2 import gray_unrank2_test
from subset.index_box_next_2d import index_box_next_2d_test
from subset.index_box_next_3d import index_box_next_3d_test
from subset.index_box2_next_2d import index_box2_next_2d_test
from subset.index_box2_next_3d import index_box2_next_3d_test
from subset.index_next0 import index_next0_test
from subset.index_next1 import index_next1_test
from subset.index_next2 import index_next2_test
from subset.index_rank0 import index_rank0_test
from subset.index_rank1 import index_rank1_test
from subset.index_rank2 import index_rank2_test
from subset.index_unrank0 import index_unrank0_test
from subset.index_unrank1 import index_unrank1_test
from subset.index_unrank2 import index_unrank2_test
from subset.inverse_mod_n import inverse_mod_n_test
from subset.involute_enum import involute_enum_test
from subset.jfrac_to_rfrac import jfrac_to_rfrac_test
from subset.josephus import josephus_test
from subset.ksub_next import ksub_next_test
from subset.ksub_next2 import ksub_next2_test
from subset.ksub_next3 import ksub_next3_test
from subset.ksub_next4 import ksub_next4_test
from subset.ksub_random import ksub_random_test
from subset.ksub_random2 import ksub_random2_test
from subset.ksub_random3 import ksub_random3_test
from subset.ksub_random4 import ksub_random4_test
from subset.ksub_random5 import ksub_random5_test
from subset.ksub_rank import ksub_rank_test
from subset.ksub_to_comp import ksub_to_comp_test
from subset.ksub_to_compnz import ksub_to_compnz_test
from subset.ksub_unrank import ksub_unrank_test
from subset.l4vec_next import l4vec_next_test
from subset.moebius_values import moebius_values_test
from subset.monomial_count import monomial_count_test
from subset.monomial_counts import monomial_counts_test
from subset.morse_thue import morse_thue_test
from subset.multinomial_coef1 import multinomial_coef1_test
from subset.multinomial_coef2 import multinomial_coef2_test
from subset.multiperm_enum import multiperm_enum_test
from subset.multiperm_next import multiperm_next_test
from subset.nim_sum import nim_sum_test
from subset.padovan import padovan_test
from subset.pell_basic import pell_basic_test
from subset.pell_next import pell_next_test
from subset.pent_enum import pent_enum_test
from subset.perm_ascend import perm_ascend_test
from subset.perm_fixed_enum import perm_fixed_enum_test
from subset.perm0_break_count import perm0_break_count_test
from subset.perm0_check import perm0_check_test
from subset.perm0_cycle import perm0_cycle_test
from subset.perm0_distance import perm0_distance_test
from subset.perm0_free import perm0_free_test
from subset.perm0_inverse import perm0_inverse_test
from subset.perm0_inverse2 import perm0_inverse2_test
from subset.perm0_inverse3 import perm0_inverse3_test
from subset.perm0_lex_next import perm0_lex_next_test
from subset.perm0_mul import perm0_mul_test
from subset.perm0_next import perm0_next_test
from subset.perm0_next3 import perm0_next3_test
from subset.perm0_print import perm0_print_test
from subset.perm0_random import perm0_random_test
from subset.perm0_random2 import perm0_random2_test
from subset.perm0_rank import perm0_rank_test
from subset.perm0_sign import perm0_sign_test
from subset.perm0_to_equiv import perm0_to_equiv_test
from subset.perm0_to_inversion import perm0_to_inversion_test
from subset.perm0_to_ytb import perm0_to_ytb_test
from subset.perm0_unrank import perm0_unrank_test
from subset.perm1_canon_to_cycle import perm1_canon_to_cycle_test
from subset.perm1_check import perm1_check_test
from subset.perm1_cycle_to_canon import perm1_cycle_to_canon_test
from subset.perm1_cycle_to_index import perm1_cycle_to_index_test
from subset.perm1_index_to_cycle import perm1_index_to_cycle_test
from subset.perm1_print import perm1_print_test
from subset.perrin import perrin_test
from subset.pord_check import pord_check_test
from subset.power_mod import power_mod_test
from subset.power_series1 import power_series1_test
from subset.power_series2 import power_series2_test
from subset.power_series3 import power_series3_test
from subset.power_series4 import power_series4_test
from subset.prime import prime_test
from subset.pythag_triple_next import pythag_triple_next_test
from subset.rat_add import rat_add_test
from subset.rat_div import rat_div_test
from subset.rat_farey import rat_farey_test
from subset.rat_farey2 import rat_farey2_test
from subset.rat_mul import rat_mul_test
from subset.rat_normalize import rat_normalize_test
from subset.rat_to_cfrac import rat_to_cfrac_test
from subset.rat_to_dec import rat_to_dec_test
from subset.rat_to_r8 import rat_to_r8_test
from subset.rat_to_s import rat_to_s_test
from subset.rat_width import rat_width_test
from subset.regro_next import regro_next_test
from subset.rfrac_to_cfrac import rfrac_to_cfrac_test
from subset.rfrac_to_jfrac import rfrac_to_jfrac_test
from subset.schroeder import schroeder_test
from subset.subcomp_next import subcomp_next_test
from subset.sort_heap_external import sort_heap_external_test
from subset.subcompnz_next import subcompnz_next_test
from subset.subcompnz2_next import subcompnz2_next_test
from subset.subset_by_size_next import subset_by_size_next_test
from subset.subset_gray_next import subset_gray_next_test
from subset.subset_gray_rank import subset_gray_rank_test
from subset.subset_gray_unrank import subset_gray_unrank_test
from subset.subset_lex_next import subset_lex_next_test
from subset.subset_random import subset_random_test
from subset.subtriangle_next import subtriangle_next_test
from subset.thue_binary_next import thue_binary_next_test
from subset.thue_ternary_next import thue_ternary_next_test
from subset.triang import triang_test
from subset.tuple_next import tuple_next_test
from subset.tuple_next2 import tuple_next2_test
from subset.tuple_next_fast import tuple_next_fast_test
from subset.tuple_next_ge import tuple_next_ge_test
from subset.ubvec_add import ubvec_add_test
from subset.ubvec_print import ubvec_print_test
from subset.ubvec_xor import ubvec_xor_test
from subset.vec_colex_next import vec_colex_next_test
from subset.vec_colex_next2 import vec_colex_next2_test
from subset.vec_colex_next3 import vec_colex_next3_test
from subset.vec_gray_next import vec_gray_next_test
from subset.vec_gray_rank import vec_gray_rank_test
from subset.vec_gray_unrank import vec_gray_unrank_test
from subset.vec_lex_next import vec_lex_next_test
from subset.vec_random import vec_random_test
from subset.vector_constrained_next import vector_constrained_next_test
from subset.vector_constrained_next2 import vector_constrained_next2_test
from subset.vector_constrained_next3 import vector_constrained_next3_test
from subset.vector_constrained_next4 import vector_constrained_next4_test
from subset.vector_constrained_next5 import vector_constrained_next5_test
from subset.vector_constrained_next6 import vector_constrained_next6_test
from subset.vector_constrained_next7 import vector_constrained_next7_test
from subset.vector_next import vector_next_test
from subset.ytb_enum import ytb_enum_test
from subset.ytb_next import ytb_next_test
from subset.ytb_print import ytb_print_test
from subset.ytb_random import ytb_random_test


def subset_test():

    # *****************************************************************************80
    #
    # SUBSET_TEST tests SUBSET.
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

    print('')
    print('SUBSET_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SUBSET library.')

    agm_values_test()
    asm_enum_test()
    asm_triangle_test()

    bell_test()
    bell_values_test()

    catalan_test()
    catalan_row_next_test()
    catalan_values_test()

    cfrac_to_rat_test()

    ch_to_digit_test()

    change_greedy_test()
    change_next_test()

    chinese_check_test()

    comb_next_test()
    comb_row_next_test()
    comb_unrank_test()

    comp_enum_test()
    comp_next_test()
    comp_next_grlex_test()
    comp_random_grlex_test()
    comp_rank_grlex_test()
    comp_to_ksub_test()
    comp_unrank_grlex_test()

    compnz_enum_test()
    compnz_next_test()
    compnz_random_test()
    compnz_to_ksub_test()

    congruence_test()

    count_pose_random_test()

    debruijn_test()

    dec_add_test()
    dec_div_test()
    dec_mul_test()
    dec_round_test()
    dec_to_r8_test()
    dec_to_rat_test()
    dec_to_s_test()
    dec_width_test()

    derange_enum_test()
    derange_enum2_test()
    derange_enum3_test()

    derange0_back_next_test()
    derange0_check_test()
    derange0_weed_next_test()

    digit_to_ch_test()

    digraph_arc_euler_test()
    digraph_arc_print_test()

    diophantine_test()
    diophantine_solution_minimize_test()

    dvec_add_test()
    dvec_complementx_test()
    dvec_mul_test()
    dvec_print_test()
    dvec_sub_test()

    equiv_print_test()
    equiv_print2_test()

    equiv0_next_test()
    equiv0_random_test()

    equiv1_next_test()
    equiv1_next2_test()

    euler_row_test()

    frobenius_number_order2_test()
    frobenius_number_order2_values_test()

    gamma_values_test()
    gamma_log_values_test()

    gray_next_test()
    gray_rank2_test()
    gray_unrank2_test()

    index_box_next_2d_test()
    index_box_next_3d_test()
    index_box2_next_2d_test()
    index_box2_next_3d_test()

    index_next0_test()
    index_next1_test()
    index_next2_test()
    index_rank0_test()
    index_rank1_test()
    index_rank2_test()
    index_unrank0_test()
    index_unrank1_test()
    index_unrank2_test()

    inverse_mod_n_test()

    involute_enum_test()

    josephus_test()

    ksub_next_test()
    ksub_next2_test()
    ksub_next3_test()
    ksub_next4_test()
    ksub_random_test()
    ksub_random2_test()
    ksub_random3_test()
    ksub_random4_test()
    ksub_random5_test()
    ksub_rank_test()
    ksub_to_comp_test()
    ksub_to_compnz_test()
    ksub_unrank_test()

    moebius_values_test()

    monomial_count_test()
    monomial_counts_test()

    morse_thue_test()

    multinomial_coef1_test()
    multinomial_coef2_test()

    multiperm_enum_test()
    multiperm_next_test()

    nim_sum_test()

    padovan_test()

    pell_basic_test()
    pell_next_test()

    pent_enum_test()

    perm_ascend_test()
    perm_fixed_enum_test()

    perm0_break_count_test()
    perm0_check_test()
    perm0_cycle_test()
    perm0_distance_test()
    perm0_free_test()
    perm0_inverse_test()
    perm0_inverse2_test()
    perm0_inverse3_test()
    perm0_lex_next_test()
    perm0_mul_test()
    perm0_next_test()
    perm0_next3_test()
    perm0_print_test()
    perm0_random_test()
    perm0_random2_test()
    perm0_rank_test()
    perm0_sign_test()
    perm0_to_equiv_test()
    perm0_to_inversion_test()
    perm0_to_ytb_test()
    perm0_unrank_test()

    perm1_canon_to_cycle_test()
    perm1_check_test()
    perm1_cycle_to_canon_test()
    perm1_cycle_to_index_test()
    perm1_index_to_cycle_test()
    perm1_print_test()

    perrin_test()

    pord_check_test()

    power_mod_test()
    power_series1_test()
    power_series2_test()
    power_series3_test()
    power_series4_test()

    pythag_triple_next_test()

    rat_add_test()
    rat_div_test()
    rat_farey_test()
    rat_farey2_test()
    rat_mul_test()
    rat_normalize_test()
    rat_to_cfrac_test()
    rat_to_dec_test()
    rat_to_r8_test()
    rat_to_s_test()
    rat_width_test()

    regro_next_test()

    rfrac_to_cfrac_test()
    rfrac_to_jfrac_test()

    schroeder_test()

    sort_heap_external_test()

    subcomp_next_test()
    subcompnz_next_test()
    subcompnz2_next_test()

    subset_by_size_next_test()
    subset_gray_next_test()
    subset_gray_rank_test()
    subset_gray_unrank_test()
    subset_lex_next_test()
    subset_random_test()

    subtriangle_next_test()

    thue_binary_next_test()
    thue_ternary_next_test()

    tuple_next_test()
    tuple_next2_test()
    tuple_next_fast_test()
    tuple_next_ge_test()

    triang_test()

    ubvec_print_test()
    ubvec_add_test()
    ubvec_xor_test()

    vec_colex_next_test()
    vec_colex_next2_test()
    vec_colex_next3_test()
    vec_gray_next_test()
    vec_gray_rank_test()
    vec_gray_unrank_test()
    vec_lex_next_test()
    vec_random_test()

    vector_constrained_next_test()
    vector_constrained_next2_test()
    vector_constrained_next3_test()
    vector_constrained_next4_test()
    vector_constrained_next5_test()
    vector_constrained_next6_test()
    vector_constrained_next7_test()
    vector_next_test()

    ytb_enum_test()
    ytb_next_test()
    ytb_print_test()
    ytb_random_test()

    print('')
    print('SUBSET_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    subset_test()
    timestamp()
