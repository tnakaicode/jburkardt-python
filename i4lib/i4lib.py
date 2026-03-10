#! /usr/bin/env python3
#
def i4lib_test ( ):

#*****************************************************************************80
#
## i4lib_test() test i4lib().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 July 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4lib_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test i4lib().' )

  rng = default_rng ( )

  gamma_log_values_test ( )

  i4_abs_test ( rng )
  i4_and_test ( rng )
  i4_bclr_test ( )
  i4_bit_hi1_test ( rng )
  i4_bit_lo0_test ( rng )
  i4_bit_lo1_test ( rng )
  i4_bit_reverse_test ( )
  i4_bset_test ( )
  i4_btest_test ( )
  i4_ceiling_test ( rng )
  i4_characteristic_test ( )
  i4_choose_test ( )
  i4_choose_check_test ( )
  i4_choose_log_test ( )
  i4_div_rounded_test ( rng )
  i4_division_test ( rng )
  i4_divp_test ( rng )
  i4_factorial_test ( )
  i4_factorial_log_test ( )
  i4_factorial2_test ( )
  i4_fall_test ( )
  i4_floor_test ( rng )
  i4_gcd_test ( )
  i4_gcdb_test ( )
  i4_huge_test ( )
  i4_huge_normalizer_test ( )
  i4_is_even_test ( )
  i4_is_integer_test ( )
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
  i4_max_test ( rng )
  i4_min_test ( rng )
  i4_moddiv_test ( )
  i4_modp_test ( )
  i4_mop_test ( rng )
  i4_normal_ab_test ( rng )
  i4_not_test ( rng )
  i4_or_test ( rng )
  i4_power_test ( )
  i4_rise_test ( )
  i4_sign_test ( )
  i4_sign3_test ( )
  i4_swap_test ( )
  i4_swap3_test ( )
  i4_to_angle_test ( )
  i4_to_digits_binary_test ( )
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
  i4_xor_test ( rng )

  i4mat_flip_cols_test ( )
  i4mat_flip_rows_test ( )
  i4mat_indicator_test ( )
  i4mat_is_binary_test ( )
  i4mat_is_integer_test ( )
  i4mat_is_ternary_test ( )
  i4mat_max_test ( rng )
  i4mat_min_test ( rng )
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
  i4mat_sum_test ( rng )
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

  i4vec_add_test ( rng )
  i4vec_amax_test ( rng )
  i4vec_amin_test ( rng )
  i4vec_binary_next_test ( )
  i4vec_choose_test ( rng )
  i4vec_concatenate_test ( )
  i4vec_copy_test ( )
  i4vec_cum_test ( rng )
  i4vec_cum0_test ( rng )
  i4vec_decrement_test ( rng )
  i4vec_dot_product_test ( rng )
  i4vec_frac_test ( rng )
  i4vec_heap_d_test ( rng )
  i4vec_gcd_test ( )
  i4vec_identity_row_test ( )
  i4vec_increment_test ( rng )
  i4vec_index_test ( rng )
  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_is_ascending_test ( )
  i4vec_is_binary_test ( )
  i4vec_is_coprime_test ( )
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
  i4vec_is_zero_test ( )
  i4vec_lcm_test ( )
  i4vec_max_test ( rng )
  i4vec_max_index_last_test ( rng )
  i4vec_max_last_test ( rng )
  i4vec_mean_test ( rng )
  i4vec_mean_i4_test ( rng )
  i4vec_min_test ( rng )
  i4vec_permute_test ( rng )
  i4vec_permute_uniform_test ( rng )
  i4vec_print_test ( )
  i4vec_print_mask_test ( )
  i4vec_product_test ( rng )
  i4vec_red_test ( )
  i4vec_reverse_test ( rng )
  i4vec_run_count_test ( rng )
  i4vec_search_binary_a_test ( )
  i4vec_search_binary_d_test ( )
  i4vec_shift_circular_test ( )
  i4vec_sort_bubble_a_test ( rng )
  i4vec_sort_heap_a_test ( rng )
  i4vec_sort_heap_index_a_test ( rng )
  i4vec_sort_heap_index_d_test ( rng )
  i4vec_sort_insert_a_test ( rng )
  i4vec_sort_insert_d_test ( rng )
  i4vec_sorted_unique_test ( rng )
  i4vec_sorted_unique_count_test ( rng )
  i4vec_sorted_unique_hist_test ( rng )
  i4vec_sum_test ( rng )
  i4vec_sum_vec_test ( rng )
  i4vec_transpose_print_test ( )
  i4vec_uniform_ab_test ( )
  i4vec_unique_count_test ( rng )
  i4vec_variance_test ( rng )
  i4vec_width_test ( )

  i4vec2_compare_test ( )
  i4vec2_print_test ( )
  i4vec2_sort_insert_a_test ( )
  i4vec2_sorted_unique_test ( )
  i4vec2_sorted_unique_count_test ( )

  intspace_test ( )

  ksub_next4_test ( )

  l4_to_i4_test ( )

  pascal_to_i4_test ( ) 

  perm0_check_test ( )
  perm0_uniform_test ( rng )

  perm1_check_test ( )
  perm1_uniform_test ( rng )

  permutation_symbol_test ( )

  prime_test ( )

  triangle_lower_to_i4_test ( )
  triangle_upper_to_i4_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4lib_test():' )
  print ( '  Normal end of execution.' )
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
#    Input, integer N_dATA.  The user sets N_dATA to 0 before the
#    first call.  
#
#  Output:
#
#    integer N_dATA.  The routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
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

def i4_abs ( a ):

#*****************************************************************************80
#
## i4_abs() returns the absolute value of an I4.
#
#  Discussion:
#
#    An I4 is an integer.
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
#    integer A, the value.
#
#  Output:
#
#    integer VALUE, the absolute value.
#
  if ( a < 0 ):
    value = -a
  else:
    value = a

  return value

def i4_abs_test ( rng ):

#*****************************************************************************80
#
## i4_abs_test() tests i4_abs().
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4_abs_test():' )
  print ( '  i4_abs() computes the absolute value of an I4.' )

  i4_lo = - 100
  i4_hi = + 100

  print ( '' )
  print ( '         A         B=i4_abs(A)' )
  print ( '' )

  for i in range ( 0, 10 ):
    a = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    b = i4_abs ( a )
    print ( '  %8d  %8d' % ( a, b ) )

  return

def i4_and ( i, j ):

#*****************************************************************************80
#
## i4_and() calculates the AND of two I4's.
#
#  Discussion:
#
#    An I4 is an integer value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, two values whose AND is needed.
#
#  Output:
#
#    integer VALUE, the AND of I and J.
#
  i1 = i
  j1 = j
  value = 0
  l = 1

  while ( i1 != 0 or j1 != 0 ):

    i2 = i1 // 2
    j2 = j1 // 2

    if ( ( i1 != 2 * i2 ) and ( j1 != 2 * j2 ) ):
      value = value + l

    i1 = i2
    j1 = j2
    l = 2 * l

  return value

def i4_and_test ( rng ):

#*****************************************************************************80
#
## i4_and_test() tests i4_and().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2016
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

  i4_lo = 0
  i4_hi = 100
  test_num = 10

  print ( '' )
  print ( 'i4_and_test():' )
  print ( '  i4_and() returns the AND of two I4\'s.' )
  print ( '' )
  print ( '         I         J    i4_and       I&J' )
  print ( '' )

  for test in range ( 0, test_num ):

    i = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    j = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    k = i4_and ( i, j )
    l = ( i & j )
    print ( '  %8d  %8d  %8d  %8d' % ( i, j, k, l ) )

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

def i4_bit_hi1 ( n ) :

#*****************************************************************************80
#
## i4_bit_hi1() returns the position of the high 1 bit base 2 in an I4.
#
#  Discussion:
#
#    An I4 is an integer value.
#
#  Example:
#
#       N    Binary    Hi 1
#    ----    --------  ----
#       0           0     0
#       1           1     1
#       2          10     2
#       3          11     2
#       4         100     3
#       5         101     3
#       6         110     3
#       7         111     3
#       8        1000     4
#       9        1001     4
#      10        1010     4
#      11        1011     4
#      12        1100     4
#      13        1101     4
#      14        1110     4
#      15        1111     4
#      16       10000     5
#      17       10001     5
#    1023  1111111111    10
#    1024 10000000000    11
#    1025 10000000001    11
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
#    integer N, the integer to be measured.
#    N should be nonnegative.  If N is nonpositive, the function
#    will always be 0.
#
#  Output:
#
#    integer BIT, the position of the highest bit.
#
  i = n
  bit = 0

  while ( True ):

    if ( i <= 0 ):
      break

    bit = bit + 1
    i = i // 2

  return bit

def i4_bit_hi1_test ( rng ):

#*****************************************************************************80
#
## i4_bit_hi1_test() tests i4_bit_hi1().
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
#    rng(): the current random number generator.
#
  import numpy as np

  test_num = 10

  print ( '' )
  print ( 'i4_bit_hi1_test():' )
  print ( '  i4_bit_hi1 returns the location of the high 1 bit.' )
  print ( '' )
  print ( '       I  i4_bit_hi1(I)' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = rng.integers ( low = 0, high = 100, endpoint = True )
    j = i4_bit_hi1 ( i )
    print ( '  %8d  %8d' % ( i, j ) )

  return

def i4_bit_lo0 ( n ):

#*****************************************************************************80
#
## i4_bit_lo0() returns the position of the low 0 bit base 2 in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       N    Binary    Lo 0
#    ----    --------  ----
#       0           0     1
#       1           1     2
#       2          10     1
#       3          11     3
#       4         100     1
#       5         101     2
#       6         110     1
#       7         111     4
#       8        1000     1
#       9        1001     2
#      10        1010     1
#      11        1011     3
#      12        1100     1
#      13        1101     2
#      14        1110     1
#      15        1111     5
#      16       10000     1
#      17       10001     2
#    1023  1111111111    11
#    1024 10000000000     1
#    1025 10000000001     2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be measured.
#    N should be nonnegative.
#
#  Output:
#
#    integer BIT, the position of the low 1 bit.
#
  bit = 0
  i = n

  while ( True ):

    bit = bit + 1
    i2 = i // 2

    if ( i == 2 * i2 ):
      break

    i = i2

  return bit

def i4_bit_lo0_test ( rng ):

#*****************************************************************************80
#
## i4_bit_lo0_test() tests i4_bit_lo0().
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
#    rng(): the current random number generator.
#
  import numpy as np

  test_num = 10

  print ( '' )
  print ( 'i4_bit_lo0_test():' )
  print ( '  i4_bit_lo0() returns the location of the low 0 bit.' )
  print ( '' )
  print ( '       I  i4_bit_lo0(I)' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = rng.integers ( low = 0, high = 100, endpoint = True )
    j = i4_bit_lo0 ( i )
    print ( '  %8d  %8d' % ( i, j ) )

  return

def i4_bit_lo1 ( n ) :

#*****************************************************************************80
#
## i4_bit_lo1() returns the position of the low 1 bit base 2 in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       N    Binary    Lo 1
#    ----    --------  ----
#       0           0     0
#       1           1     1
#       2          10     2
#       3          11     1
#       4         100     3
#       5         101     1
#       6         110     2
#       7         111     1
#       8        1000     4
#       9        1001     1
#      10        1010     2
#      11        1011     1
#      12        1100     3
#      13        1101     1
#      14        1110     2
#      15        1111     1
#      16       10000     5
#      17       10001     1
#    1023  1111111111     1
#    1024 10000000000    11
#    1025 10000000001     1
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
#    integer N, the integer to be measured.
#    N should be nonnegative.
#
#  Output:
#
#    integer BIT, the position of the low 1 bit.
#
  bit = 0
  i = n

  while ( True ):

    bit = bit + 1
    i2 = i // 2

    if ( i != 2 * i2 ):
      break

    i = i2

  return bit

def i4_bit_lo1_test ( rng ):

#*****************************************************************************80
#
## i4_bit_lo1_test() tests i4_bit_lo1().
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
#    rng(): the current random number generator.
#
  import numpy as np

  test_num = 10

  print ( '' )
  print ( 'i4_bit_lo1_test():' )
  print ( '  i4_bit_lo1() returns the location of the low 1 bit.' )
  print ( '' )
  print ( '       I  i4_bit_lo1(I)' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = rng.integers ( low = 0, high = 100, endpoint = True )
    print ( '  %8d' % ( i ), end = '' )
    j = i4_bit_lo1 ( i )
    print ( '  %8d' % ( j ) )

  return

def i4_bit_reverse ( i, n ):

#*****************************************************************************80
#
## i4_bit_reverse() reverses the bits in an I4.
#
#  Discussion:
#
#    An I4 is an integer ( kind = 4 ) value.
#
#  Example:
#
#       I      N  2^N     i4_bit_reverse ( I, N )
#    ----    --------  -----------------------
#       0      0    1     0
#       1      0    1     1
#
#       0      3    8     0
#       1      3    8     4
#       2      3    8     2
#       3      3    8     6
#       4      3    8     1
#       5      3    8     5
#       6      3    8     3
#       7      3    8     7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the integer to be bit reversed.
#    I should be nonnegative.  Normally I < 2^N.
#
#    integer N, indicates the number of bits to
#    be reverse (N+1) or the base with respect to which the integer is to
#    be reversed (2^N).  N should be nonnegative.
#
#  Output:
#
#    integer VALUE, the bit reversed value.
#
  if ( i < 0 ):

    value = -1

  elif ( n < 0 ):

    value = -1

  else:

    b = 2 ** n
    j = ( i % b )

    value = 0

    while ( True ):

      if ( b == 1 ):

        value = value + j
        j = 0
        break

      else:

        if ( ( j % 2 ) == 1 ):
          value = value + b // 2
          j = j - 1

        j = j // 2
        b = b // 2

  return value

def i4_bit_reverse_test ( ):

#*****************************************************************************80
#
## i4_bit_reverse_test() tests i4_bit_reverse().
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
  test_num = 10

  print ( '' )
  print ( 'i4_bit_reverse_test():' )
  print ( '  i4_bit_reverse bit reverses I with respect to 2^J.' )
  print ( '' )
  print ( '         I         J  i4_bit_reverse(I,J)' )
  print ( '' )
 
  for j in range ( 0, 5 ):
    i_hi = 2 ** j
    for i in range ( 0, i_hi ):
      k = i4_bit_reverse ( i, j )
      print ( '  %8d  %8d  %8d' % ( i, j, k ) )

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
  print ( '  i4_btest reports whether a given bit is 0 or 1.' )

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

def i4_ceiling ( x ) :

#*****************************************************************************80
#
## i4_ceiling() rounds an R8 up to the next I4.
#
#  Example:
#
#    X         Value
#
#   -1.1      -1
#   -1.0      -1
#   -0.9       0
#   -0.1       0
#    0.0       0
#    0.1       1
#    0.9       1
#    1.0       1
#    1.1       2
#    2.9       3
#    3.0       3
#    3.14159   4
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
#  Input:
#
#    real X, the number to be rounded up.
#
#  Output:
#
#    integer VALUE, the rounded value of X.
#
  import numpy as np

  value = int ( np.ceil ( x ) )

  return value

def i4_ceiling_test ( rng ):

#*****************************************************************************80
#
## i4_ceiling_test() tests i4_ceiling().
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
#    rng(): the current random number generator.
#
  import numpy as np

  r8_lo = -100.0
  r8_hi =  100.0

  print ( '' )
  print ( 'i4_ceiling_test():' )
  print ( '  i4_ceiling() evaluates the "ceiling" of a real number.' )
  print ( ' ' )
  print ( '      R8    i4_ceiling(R8)' )
  print ( ' ' )

  for i in range ( 0, 10 ):
    r8 = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    i4 = i4_ceiling ( r8 )
    print ( '  %8.4f            %4d' % ( r8, i4 ) )

  return

def i4_characteristic ( q ) :

#*****************************************************************************80
#
## i4_characteristic() gives the characteristic for an I4.
#
#  Discussion:
#
#    For any positive integer Q, the characteristic is:
#
#    Q, if Q is a prime;
#    P, if Q = P^N for some prime P and some integer N;
#    0, otherwise, that is, if Q is negative, 0, 1, or the product
#       of more than one distinct prime.
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
#    John Burkardt.
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Harald Niederreiter,
#    Algorithm 738:
#    Programs to Generate Niederreiter's Low-Discrepancy Sequences,
#    ACM Transactions on Mathematical Software,
#    Volume 20, Number 4, pages 494-495, 1994.
#
#  Input:
#
#    integer Q, the value to be tested.
#
#  Output:
#
#    integer VALUE, the characteristic of Q.
#
  import numpy as np

  if ( q <= 1 ):
    value = 0
    return value
#
#  If Q is not prime, then there is at least one prime factor
#  of Q no greater than SQRT(Q)+1.
#
#  A faster code would only consider prime values of I,
#  but that entails storing a table of primes and limiting the
#  size of Q.  Simplicity and flexibility for now!
#
  i_max = int ( np.sqrt ( q ) ) + 1

  for i in range ( 2, i_max + 1 ):

    if ( ( q % i ) == 0 ):

      while ( ( q % i ) == 0 ):
        q = q / i

      if ( q == 1 ):
        value = i
      else:
        value = 0

      return value
#
#  If no factor was found, then Q is prime.
#
  value = q

  return value

def i4_characteristic_test ( ):

#*****************************************************************************80
#
## i4_characteristic_test() tests i4_characteristic().
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
  test_num = 10

  print ( '' )
  print ( 'i4_characteristic_test():' )
  print ( '  i4_characteristic() computes the characteristic' )
  print ( '  of an integer Q, which is  ' )
  print ( '    Q if Q is prime;' )
  print ( '    P, if Q = P^N for some prime P;' )
  print ( '    0, if Q is negative, 0, 1, or the product of ' )
  print ( '      more than 1 distinct prime.' )
  print ( '' )
  print ( '   I  i4_characteristic' )
  print ( ' ' )
 
  for i in range ( 1, 51 ):
    j = i4_characteristic ( i )
    print ( '  %2d             %4d' % ( i, j ) )

  return

def i4_choose_check ( n, k ):

#*****************************************************************************80
#
## i4_choose_check() reports whether the binomial coefficient can be computed.
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
#    integer N, K, the binomial parameters.
#
#  Output:
#
#    logical CHECK is:
#    TRUE, if C(N,K) < maximum integer.
#    FALSE, otherwise.
#
  import numpy as np
  from scipy.special import gammaln

  i4_huge = 2147483647

  i4_huge_log = np.log ( i4_huge )

  choose_nk_log = \
      gammaln ( n + 1 ) \
    - gammaln ( k + 1 ) \
    - gammaln ( n - k + 1 )

  check = ( choose_nk_log < i4_huge_log )
        
  return check

def i4_choose_check_test ( ):

#*****************************************************************************80
#
## i4_choose_check_test() tests i4_choose_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k_test = np.array ( [ 3, 999, 3, 10 ] )
  n_test = np.array ( [ 10, 1000, 100, 100 ] )

  print ( '' )
  print ( 'i4_choose_check_test():' )
  print ( '  i4_choose_check() checks whether C(N,K)' )
  print ( '  can be computed with integer arithmetic' )
  print ( '  or not.' )
  print ( '' )
  print ( '     N     K    CHECK?    i4_choose' )
  print ( '' )
 
  for i in range ( 0, 4 ):
    n = n_test[i]
    k = k_test[i]
    check = i4_choose_check ( n, k )
    print ( '  %4d  %4d        %d' % ( n, k, check ), end = '' )
    if ( check ):
      cnk = i4_choose ( n, k )
      print ( '        %d' % ( cnk ) )
    else:
      print ( '   Not computable' )

  return

def i4_choose_log ( n, k ):

#*****************************************************************************80
#
## i4_choose_log() computes the logarithm of the Binomial coefficient.
#
#  Discussion:
#
#    LOG ( C(N,K) ) = LOG ( N! / ( K! * (N-K)! ) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
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
#    real VALUE, the logarithm of C(N,K).
#
  value = i4_factorial_log ( n ) - i4_factorial_log ( k ) \
    - i4_factorial_log ( n - k )

  return value

def i4_choose_log_test ( ):

#*****************************************************************************80
#
## i4_choose_log_test() tests i4_choose_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4_choose_log_test():' )
  print ( '  i4_choose_log() evaluates log(C(N,K)).' )
  print ( '' )
  print ( '     N     K            lcnk           elcnk   CNK' )
  print ( '' )
 
  for n in range ( 0, 5 ):
    for k in range ( 0, n + 1 ):
      lcnk = i4_choose_log ( n, k )
      elcnk = np.exp ( lcnk )
      cnk = i4_choose ( n, k )
      print ( '  %4d  %4d  %14.6g  %14.6g  %4d' % ( n, k, lcnk, elcnk, cnk ) )

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

def i4_division ( a, b ):

#*****************************************************************************80
#
## i4_division() returns the result of integer division.
#
#  Discussion:
#
#    This routine computes C = A / B, where the result is rounded to the
#    integer value nearest 0.
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
#    integer A, B, the number to be divided, and the divisor.
#
#  Output:
#
#    integer C, the rounded result of the division.
#
  import numpy as np

  if ( a * b < 0.0 ):
    s = -1
  else:
    s = +1

  a = np.abs ( a )
  b = np.abs ( b )
  c = s * ( a // b )

  return c

def i4_division_test ( rng ):

#*****************************************************************************80
#
## i4_division_test() tests i4_division().
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
  import numpy as np

  a_hi =  100
  a_lo = -100
  b_hi =  10
  b_lo = -10
  test_num = 20

  print ( '' )
  print ( 'i4_division_test():' )
  print ( '  i4_division() performs integer division.' )
  print ( ' ' )
  print ( '  C0 = real ( a ) / real ( b )' )
  print ( '  C1 = i4_division ( A, B )' )
  print ( '  C2 = nint ( real ( a ) / real ( b ) )' )
  print ( '  C3 = int ( A / B )' )
  print ( '  C4 = floor ( real ( a ) / real ( b ) )' )
  print ( '  C5 = a // b' )
  print ( ' ' )
  print ( '  C1 and C3 and C4 and C5 should be equal.' )
  print ( '  (They are not, for some negative cases!)' )
  print ( '  C2 may differ;' )
  print ( ' ' )
  print ( '     A     B           C0         C1    C2      C3    C4      C5' )
  print ( ' ' )

  for test in range ( 1, test_num ):
    a = rng.integers ( low = a_lo, high = a_hi, endpoint = True )
    b = rng.integers ( low = b_lo, high = b_hi, endpoint = True )
    if ( b == 0 ):
      b = 7
    c0 = float ( a ) / float ( b )
    c1 = i4_division ( a, b )
    c2 = round ( float ( a ) / float ( b ) )
    c3 = int ( a / b )
    c4 = np.floor ( float ( a ) / float ( b ) )
    c5 = a // b
    print ( '  %4d  %4d    %14.6f  %4d  %4d    %4d  %4d    %4d' \
      % ( a, b, c0, c1, c2, c3, c4, c5 ) )

  return

def i4_divp ( i, j ):

#*****************************************************************************80
#
## i4_divp() returns the smallest multiple of J greater than or equal to I.
#
#  Example:
#
#    I  J  VALUE
#
#    0  4    0
#    1  4    1
#    2  4    1
#    3  4    1
#    4  4    1
#    5  4    2
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
#    integer I, the number to be analyzed.
#
#    integer J, the number, multiples of which will
#    be compared against I.  J may not be zero.
#
#  Output:
#
#    integer VALUE, the smallest multiple of J that
#    is greater than or equal to I.
#
  import numpy as np

  if ( j != 0 ):
    value = 1 + np.floor ( ( i - 1 ) / j )
  else:
    value = 0
    print ( '' )
    print ( 'i4_divp(): Fatal error!' )
    print ( '  The input value of J was zero!' )
    raise Exception ( 'i4_divp(): Fatal error!\n' )

  return value

def i4_divp_test ( rng ) :

#*****************************************************************************80
#
## i4_divp_test() tests i4_divp().
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
#    rng(): the current random number generator.
#
  import numpy as np

  a_hi =  100
  a_lo = -100
  b_hi =  10
  b_lo = -10
  test_num = 20

  print ( '' )
  print ( 'i4_divp_test():' )
  print ( '  i4_divp() returns the smallest multiplier of J' )
  print ( '  that is less than I' )
  print ( '' )
  print ( '     A     B     C     D' )
  print ( '' )

  for test in range ( 1, test_num + 1 ):
    a = rng.integers ( low = a_lo, high = a_hi, endpoint = True )
    b = rng.integers ( low = b_lo, high = b_hi, endpoint = True )
    if ( b == 0 ):
      b = 7 
    c = i4_divp ( a, b )
    d = c * b
    print ( '  %4d  %4d  %4d  %4d' % ( a, b, c, d ) )

  return

def i4_div_rounded ( a, b ):

#*****************************************************************************80
#
## i4_div_rounded() computes the rounded result of I4 division.
#
#  Discussion:
#
#    This routine computes C = A / B, where A, B and C are integers
#    and C is the closest integer value to the exact real result.
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
#    integer A, B, the number to be divided, and the divisor.
#
#  Output:
#
#    integer VALUE, the rounded result of the division.
#
  import numpy as np

  i4_huge = 2147483647

  if ( a == 0 and b == 0 ):

    value = i4_huge
 
  elif ( a == 0 ):

    value = 0

  elif ( b == 0 ):

    if ( a < 0 ):
      value = - i4_huge
    else:
      value = + i4_huge

  else:

    a_abs = np.abs ( a )
    b_abs = np.abs ( b )

    value = np.floor ( a_abs / b_abs )
#
#  Round the value.
#
    if ( ( 2 * value + 1 ) * b_abs < 2 * a_abs ):
      value = value + 1
#
#  Set the sign.
#
    if ( ( a < 0 and 0 < b ) or ( 0 < a and b < 0 ) ):
      value = - value

  return value

def i4_div_rounded_test ( rng ):

#*****************************************************************************80
#
## i4_div_rounded_test() tests i4_div_rounded().
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
#    rng(): the current random number generator.
#
  import numpy as np

  a_hi =  100
  a_lo = -100
  b_hi =  10
  b_lo = -10
  test_num = 20

  print ( '' )
  print ( 'i4_div_rounded_test():' )
  print ( '  i4_div_rounded() performs rounded integer division.' )
  print ( ' ' )
  print ( '  C0 = real ( a ) / real ( b )' )
  print ( '  C1 = i4_div_rounded ( A, B )' )
  print ( '  C2 = nint ( real ( a ) / real ( b ) )' )
  print ( '  C3 = int ( A / B )' )
  print ( '  C4 = floor ( real ( a ) / real ( b ) )' )
  print ( '  C5 = a // b' )
  print ( ' ' )
  print ( '  C1 and C2 should be equal;' )
  print ( '  C3 and C4 should be equal.' )
  print ( ' ' )
  print ( '     A     B           C0         C1    C2      C3    C4      C5' )
  print ( ' ' )

  for test in range ( 1, test_num ):
    a = rng.integers ( low = a_lo, high = a_hi, endpoint = True )
    b = rng.integers ( low = b_lo, high = b_hi, endpoint = True )
    if ( b == 0 ):
      b = 7
    c0 = float ( a ) / float ( b )
    c1 = i4_div_rounded ( a, b )
    c2 = round ( float ( a ) / float ( b ) )
    c3 = int ( a / b )
    c4 = np.floor ( float ( a ) / float ( b ) )
    c5 = a // b
    print ( '  %4d  %4d    %14.6f  %4d  %4d    %4d  %4d    %4d' \
      % ( a, b, c0, c1, c2, c3, c4, c5 ) )

  return

def i4_factorial2 ( n ) :

#*****************************************************************************80
#
## i4_factorial2() computes the double factorial N!!
#
#  Discussion:
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
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the double factorial function.
#    If N is less than 1, the value is returned as 1.
#
#  Output:
#
#    integer VALUE, the value of N!!.
#
  if ( n < 1 ):
    value = 1
    return value

  value = 1

  for i in range ( n, 1, -2 ):
    value = value * i

  return value

def i4_factorial2_test ( ):

#*****************************************************************************80
#
## i4_factorial2_test() tests i4_factorial2().
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
  print ( 'i4_factorial2_test():' )
  print ( '  i4_factorial2() evaluates the double factorial function.' )
  print ( '' )
  print ( '         N      Exact         i4_factorial2(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = i4_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_factorial2 ( n )

    print ( '  %8d  %12d  %12d' % ( n, f1, f2 ) ) 

  return

def i4_factorial2_values ( n_data ):

#*****************************************************************************80
#
## i4_factorial2_values() returns values of the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * \ * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * \ * 1 )  (N odd)
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
#    17 December 2014
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
#    integer N_dATA.  The user sets N_dATA to 0 before the
#    first call.  
#
#  Output:
#
#    integer N_dATA.  The routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    integer FN, the value of the function.
# 
  import numpy as np

  n_max = 16

  fn_vec = np.array ( ( 
          1, \
          1, \
          2, \
          3, \
          8, \
         15, \
         48, \
        105, \
        384, \
        945, \
       3840, \
      10395, \
      46080, \
     135135, \
     645120, \
    2027025 ) )

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
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def i4_factorial2_values_test ( ):

#*****************************************************************************80
#
## i4_factorial2_values_test() tests i4_factorial2_values().
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
  print ( 'i4_factorial2_values_test():' )
  print ( '  i4_factorial2_values() returns values of the double factorial function.' )
  print ( '' )
  print ( '     N        N!!' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %10d' % ( n, fn ) )

  return

def i4_factorial_log ( n ):

#*****************************************************************************80
#
## i4_factorial_log() returns the logarithm of N factorial.
#
#  Discussion:
#
#    N! = Product ( 1 <= I <= N ) I
#
#    N! = Gamma(N+1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2016
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
#    real VALUE, the logarithm of N factorial.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'i4_factorial_log(): Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'i4_factorial_log(): Fatal error!' )

  value = 0.0

  for i in range ( 2, n + 1 ):
    value = value + np.log ( i )

  return value

def i4_factorial_log_test ( ):

#*****************************************************************************80
#
## i4_factorial_log_test() tests i4_factorial_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4_factorial_log_test():' )
  print ( '  i4_factorial_log() evaluates the log(N!).' )
  print ( '' )
  print ( '         N           lfact          elfact         fact' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fact = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    lfact = i4_factorial_log ( n )
    elfact = np.exp ( lfact )

    print ( '  %8d  %14.6g  %14.6g  %12d' % ( n, lfact, elfact, fact ) )

  return

def i4_factorial ( n ) :

#*****************************************************************************80
#
## i4_factorial() computes the factorial function.
#
#  Discussion:
#
#    You might prefer to use
#      result = math.factorial ( n )
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
#    integer N, the argument.
#
#  Output:
#
#    integer VALUE, the value of the factorial function.
#
  value = 1
  for i in range ( 1, n + 1 ):
    value = value * i

  return value

def i4_factorial_test ( ):

#*****************************************************************************80
#
## i4_factorial_test() tests i4_factorial().
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
  print ( 'i4_factorial_test():' )
  print ( '  i4_factorial() evaluates the factorial function.' )
  print ( '' )
  print ( '         N      Exact         i4_factorial(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_factorial ( n )

    print ( '  %8d  %12d  %12d' % ( n, f1, f2 ) ) 

  return

def i4_factorial_values ( n_data ):

#*****************************************************************************80
#
## i4_factorial_values() returns values of the factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) I
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
#    18 December 2014
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
#    integer N_dATA.  The user sets N_dATA to 0 before the
#    first call.  
#
#  Output:
#
#    integer N_dATA.  The routine increments N_dATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_dATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    integer FN, the value of the function.
#
  import numpy as np

  n_max = 13

  fn_vec = np.array ( [ \
            1, \
            1, \
            2, \
            6, \
           24, \
          120, \
          720, \
         5040, \
        40320, \
       362880, \
      3628800, \
     39916800, \
    479001600 ] )
  n_vec = np.array ( [ \
     0,  1,  2,  3, \
     4,  5,  6,  7, \
     8,  9, 10, 11, \
    12 ] )

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

def i4_factorial_values_test ( ):

#*****************************************************************************80
#
## i4_factorial_values_test() tests i4_factorial_values().
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
  print ( 'i4_factorial_values_test:' )
  print ( '  i4_factorial_values() returns values of the integer factorial function.' )
  print ( '' )
  print ( '          N          i4_factorial(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %12d' % ( n, fn ) )

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
## i4_factor_test() tests i4_factor.
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
## i4_fall computes the falling factorial function [X]_N.
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
## i4_fall_test() tests i4_fall.
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
## i4_fall_values returns values of the integer falling factorial function.
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
#    integer N_dATA.  The user sets N_dATA to 0 before the
#    first call.  
#
#  Output:
#
#    integer N_dATA.  The routine increments N_dATA by 1, and
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
## i4_fall_values_test() tests i4_fall_values.
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
  print ( 'i4_fall_values_test:' )
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

def i4_floor ( x ) :

#*****************************************************************************80
#
## i4_floor rounds an R8 down to the next I4.
#
#  Example:
#
#    X         Value
#
#   -1.1      -2
#   -1.0      -1
#   -0.9      -1
#   -0.1      -1
#    0.0       0
#    0.1       0
#    0.9       0
#    1.0       1
#    1.1       1
#    2.9       2
#    3.0       3
#    3.14159   3
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
#    real X, the number to be rounded up.
#
#  Output:
#
#    integer VALUE, the rounded value of X.
#
  import numpy as np

  value = int ( np.floor ( x ) )

  return value

def i4_floor_test ( rng ):

#*****************************************************************************80
#
## i4_floor_test() tests i4_floor.
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
#    rng(): the current random number generator.
#
  import numpy as np

  r8_lo = -100.0
  r8_hi =  100.0

  print ( '' )
  print ( 'i4_floor_test():' )
  print ( '  i4_floor() evaluates the "floor" of a real number.' )
  print ( '' )
  print ( '      R8       i4_floor(R8)' )
  print ( '' )

  for i in range ( 0, 10 ):
    r8 = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    i4 = i4_floor ( r8 )
    print ( '  %8.4f            %4d' % ( r8, i4 ) )

  return

def i4_fraction ( i, j ):

#*****************************************************************************80
#
## i4_fraction computes a ratio and returns an integer result.
#
#  Discussion:
#
#    Given variables I and J, MATLAB will evaluate an expression such as 
#    "I/J" using real arithmetic.  Thus "7/3" produces the 2.333...
#
#    In the case where the result is negative, such as -2.33..., we might
#    choose to round down to -3 or up to -2.  In MATLAB, this is the
#    difference between the floor() and round() functions.  Here, we
#    choose the ROUND function so that, for instance, it will be true that
#
#      i4_fraction ( i, j ) + i4_fraction ( -i, j ) = 0
#
#  Example:
#
#       I     J     Real    i4_fraction
#
#       1     2     0.5      0
#       8     4     2.00     2
#       9     4     2.25     2
#       7     4     1.75     1
#      -7     4    -1.75    -1
#       7    -4    -1.75    -1     
#      -7    -4     1.75     1
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
#    integer I, J, the arguments.
#
#  Output:
#
#    integer VALUE, the value of the ratio.
#
  value = round ( i / j )

  return value

def i4_gcdb ( i, j, k ) :

#*****************************************************************************80
#
## i4_gcdb finds the greatest common divisor of the form K^N of two numbers.
#
#  Discussion:
#
#    Note that if J is negative, i4_gcdb will also be negative.
#    This is because it is likely that the caller is forming
#    the fraction I/J, and so any minus sign should be
#    factored out of J.
#
#    If I and J are both zero, i4_gcdb is returned as 1.
#
#    If I is zero and J is not, i4_gcdb is returned as J,
#    and vice versa.
#
#    If I and J are nonzero, and have no common divisor of the
#    form K^N, i4_gcdb is returned as 1.
#
#    Otherwise, i4_gcdb is returned as the largest common divisor
#    of the form K^N shared by I and J.
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
#    integer I, J, two numbers whose greatest common divisor K**N
#    is desired.
#
#    integer K, the possible divisor of I and J.
#
#  Output:
#
#    integer VALUE, the greatest common divisor of
#    the form K^N shared by I and J.
#
  value = 1
#
#  If both I and J are zero, i4_gcdb is 1.
#
  if ( i == 0 and j == 0 ):
    value = 1
    return value
#
#  If just one of I and J is zero, i4_gcdb is the other one.
#
  if ( i == 0 ):
    value = j
    return value
  elif ( j == 0 ):
    value = i
    return value
#
#  Divide out K as long as you can.
#
  if ( 0 < j ):
    value = 1
  else:
    value = -1

  while ( True ):

    if ( ( i % k ) != 0 or ( j % k ) != 0 ):
      break

    value = value * k
    i = i // k
    j = j // k

  return value

def i4_gcdb_test ( ):

#*****************************************************************************80
#
## i4_gcdb_test() tests i4_gcdb.
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

  test_num = 4

  i_test = np.array ( [ 288, 288, 288, 288 ] )
  j_test = np.array ( [ 2880, 2880, 2880, 2880 ] )
  k_test = np.array ( [ 2, 3, 4, 5 ] )

  print ( '' )
  print ( 'i4_gcdb_test():' )
  print ( '  i4_gcdb() computes the greatest common factor' )
  print ( '  of the form K^N.' )
  print ( '' )
  print ( '       I       J       K    i4_gcdb' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = k_test[test]
    l = i4_gcdb ( i, j, k )
    print ( '  %6d  %6d  %6d  %6d' % ( i, j, k, l ) )

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
## i4_gcd_test() tests i4_gcd.
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

def i4_huge_normalizer ( ) :

#*****************************************************************************80
#
## i4_huge_normalizer() returns the "normalizer" for i4_huge.
#
#  Discussion:
#
#    The value returned is 1 / ( i4_huge + 1 ).
#
#    For any I4, it should be the case that
#
#     -1 < I4 * i4_huge_normalizer < 1.
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
#  Output:
#
#    real VALUE, the "normalizer" for i4_huge.
#
  value = 4.656612873077392578125E-10

  return value

def i4_huge_normalizer_test ( ):

#*****************************************************************************80
#
## i4_huge_normalizer_test() tests i4_huge_normalizer().
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
  i4 = i4_huge ( )
  r8 = i4_huge_normalizer ( )

  print ( '' )
  print ( 'i4_huge_normalizer_test():' )
  print ( '  i4_huge_normalizer() returns 1/(i4_huge+1).' )
  print ( '' )
  print ( '  i4_huge() = %d' % ( i4 ) )
  print ( '  i4_huge_normalizer() = %g' % ( r8 ) )

  product = i4 * r8

  print ( '' )
  print ( '  i4_huge * i4_huge_normalizer = %g' % ( product ) )

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

def i4_is_even ( i ):

#*****************************************************************************80
#
## i4_is_even() returns TRUE if I is even.
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
#    integer I, the integer to be tested.
#
#  Output:
#
#    boolean VALUE, is TRUE if I is even.
#
  value = ( ( i % 2 ) == 0 )

  return value

def i4_is_even_test ( ) :

#*****************************************************************************80
#
## i4_is_even_test() tests i4_is_even().
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
  print ( 'i4_is_even_test():' )
  print ( '  i4_is_even() reports whether an I4 is even.' )
  print ( ' ' )
  print ( '         I  i4_is_even(I)' )
  print ( ' ' )

  for i in range ( -2, 26 ):
    j = i4_is_even ( i )
    print ( '  %8d  %r' % ( i, j ) )

  return

def i4_is_integer ( a ):

#*****************************************************************************80
#
## i4_is_integer() is TRUE if an I4 has an integer value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    some type A, the value.
#
#  Output:
#
#    logical VALUE: true if A has an integer value.
#
  import numpy as np

  if ( np.isnan ( a ) ):
    value = False
  elif ( np.isinf ( a ) ):
    value = False
  elif ( np.iscomplex ( a ) ):
    value = ( np.imag ( a ) == 0 and int ( np.real ( a ) ) == np.real ( a ) ) 
  else:
    value = ( int ( np.real ( a ) ) == a ) 

  return value

def i4_is_integer_test ( ) :

#*****************************************************************************80
#
## i4_is_integer_test() tests i4_is_integer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4_is_integer_test():' )
  print ( '  i4_is_integer() is True if the argument has an integer value.' )
  print ( ' ' )
  print ( '         arg  i4_is_integer(arg)' )
  print ( ' ' )
  arg = np.pi
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = 1+2j
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = 3+0j
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = np.finfo(float).eps
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = 3.0
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = 0
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = -17
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = np.Inf
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )
  arg = np.NAN
  print ( '  ', arg, '  ', i4_is_integer ( arg ) )

  return

def i4_is_odd ( i ):

#*****************************************************************************80
#
## i4_is_odd() returns TRUE if I is odd.
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
#    integer I, the integer to be tested.
#
#  Output:
#
#    logical VALUE, is TRUE if I is odd.
#
  value = ( ( i % 2 ) == 1 )

  return value

def i4_is_odd_test ( ) :

#*****************************************************************************80
#
## i4_is_odd_test() tests i4_is_odd().
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
  print ( 'i4_is_odd_test():' )
  print ( '  i4_is_odd() reports whether an I4 is odd.' )
  print ( '' )
  print ( '         I  i4_is_odd(I)' )
  print ( '' )

  for i in range ( -2, 26 ):
    j = i4_is_odd ( i )
    print ( '  %8d  %r' % ( i, j ) )

  return

def i4_is_power_of_10 ( n ):

#*****************************************************************************80
#
## i4_is_power_of_10() reports whether an integer is a power of 10.
#
#  Discussion:
#
#    The powers of 10 are 1, 10, 100, 1000, 10000, and so on.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be tested.
#
#  Output:
#
#    logical VALUE, is TRUE if N is a power of 10.
#
  value = False

  if ( n <= 0 ):
    return value

  while ( 1 < n ):

    if ( ( n % 10 ) != 0 ):
      return value

    n = n // 10

  value = True

  return value

def i4_is_power_of_10_test ( ):

#*****************************************************************************80
#
## i4_is_power_of_10_test() tests i4_is_power_of_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_is_power_of_10_test():' )
  print ( '  i4_is_power_of_10() reports whether an I4 is a power of 10.' )
  print ( '' )
  print ( '  I     i4_is_power_of_10(I)' )
  print ( '' )

  for i in range ( 97, 104 ):
    print ( '  %6d  %s' % ( i, i4_is_power_of_10 ( i ) ) )

  return

def i4_is_power_of_2 ( n ):

#*****************************************************************************80
#
## i4_is_power_of_2() reports whether an integer is a power of 2.
#
#  Discussion:
#
#    The powers of 2 are 1, 2, 4, 8, 16, and so on.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be tested.
#
#  Output:
#
#    logical VALUE, is TRUE if N is a power of 2.
#
  value = False

  if ( n <= 0 ):
    return value

  while ( 1 < n ):

    if ( ( n % 2 ) == 1 ):
      return value

    n = n // 2

  value = True

  return value

def i4_is_power_of_2_test ( ):

#*****************************************************************************80
#
## i4_is_power_of_2_test() tests i4_is_power_of_2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_is_power_of_2_test():' )
  print ( '  i4_is_power_of_2() reports whether an I4 is a power of 2.' )
  print ( '' )
  print ( '  I     i4_is_power_of_2(I)' )
  print ( '' )

  for i in range ( -4, 26 ):
    print ( '  %6d  %s' % ( i, i4_is_power_of_2 ( i ) ) )

  return

def i4_is_prime ( n ) :

#*****************************************************************************80
#
## i4_is_prime() reports whether an I4 is prime.
#
#  Discussion:
#
#    A simple, unoptimized sieve of Eratosthenes is used to
#    check whether N can be divided by any integer between 2
#    and SQRT(N).
#
#    Note that negative numbers, 0 and 1 are not considered prime.
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
#    integer N, the integer to be tested.
#
#  Output:
#
#    boolean VALUE, is TRUE if N is prime, and FALSE otherwise.
#
  import numpy as np

  if ( n <= 0 ):
    value = False
    return value

  if ( n == 1 ):
    value = False
    return value

  if ( n <= 3 ):
    value = True
    return value

  nhi = int ( np.sqrt ( float ( n ) ) )

  for i in range ( 2, nhi + 1 ):
    if ( ( n % i ) == 0 ):
      value = False
      return value

  value = True

  return value

def i4_is_prime_test ( ) :

#*****************************************************************************80
#
## i4_is_prime_test() tests i4_is_prime().
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
  print ( 'i4_is_prime_test():' )
  print ( '  i4_is_prime() reports whether an I4 is prime.' )
  print ( '' )
  print ( '         I  i4_is_prime(I)' )
  print ( '' )

  for i in range ( -2, 26 ):
    j = i4_is_prime ( i )
    print ( '  %8d  %r' % ( i, j ) )

  return

def i4_lcm_12n ( n ):

#*****************************************************************************80
#
## i4_lcm_12n() computes the least common multiple of the integers 1 through N.
#
#  Examples:
#
#    N    LCM_12n
#
#    1          1
#    2          2
#    3          3
#    4         12
#    5         60
#    6         60
#    7        420
#    8        840
#    9       2520
#   10       2520
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
#    integer N, the value of N.
#
#  Output:
#
#    integer VALUE, the least common multiple of the integers 1 to N.
#
  value = 1

  for i in range ( 2, n + 1 ):

    mult = i

    for j in range ( 1, i ):

      if ( ( mult % ( i - j ) ) == 0 ):
        mult = mult / ( i - j )

    value = value * mult

  return value

def i4_lcm_12n_test ( ):

#*****************************************************************************80
#
## i4_lcm_12n_test() tests i4_lcm_12n().
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
  print ( '' )
  print ( 'i4_lcm_12n_test():' )
  print ( '  i4_lcm_12n() computes the least common multiple' )
  print ( '  of integer 1 through N' )
  print ( '' )
  print ( '     N   i4_lcm_12n' )
  print ( '' )

  for n in range ( 1, 11 ):
    print ( '  %2d  %10d' % ( n, i4_lcm_12n ( n ) ) )

  return

def i4_lcm ( i, j ) :

#*****************************************************************************80
#
## i4_lcm() computes the least common multiple of two I4's.
#
#  Discussion:
#
#    The least common multiple may be defined as
#
#      LCM(I,J) = ABS( I * J ) / GCD(I,J)
#
#    where GCD(I,J) is the greatest common divisor of I and J.
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
#  Input:
#
#    integer I, J, the integers whose LCM is desired.
#
#  Output:
#
#    integer VALUE, the least common multiple of I and J.
#    VALUE is never negative.  VALUE is 0 if either I or J is zero.
#
  value = abs ( i * ( j // i4_gcd ( i, j ) ) )

  return value

def i4_lcm_test ( ):

#*****************************************************************************80
#
## i4_lcm_test() tests i4_lcm().
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
  print ( 'i4_lcm_test():' )
  print ( '  i4_lcm() computes the least common multiple.' )
  print ( '' )
  print ( '       I       J  i4_lcm' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_lcm ( i, j )
    print ( '  %6d  %6d  %6d' % ( i, j, k ) )

  return

def i4_length ( i4 ):

#*****************************************************************************80
#
## i4_length() computes the number of characters needed to print an I4.
#
#  Example:
#
#        I4    i4_length
#
#         0       1
#         1       1
#        -1       2
#      1952       4
#    123456       6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the integer whose length is desired.
#
#  Output:
#
#    integer VALUE, the number of characters required to print the integer.
#

#
#  Ensure that I4 is an integer.
#
  i4 = int ( i4 )

  if ( i4 < 0 ):
    value = 1
    i4 = - i4
  elif ( i4 == 0 ):
    value = 1
    return value
  else:
    value = 0

  while ( i4 != 0 ):
    value = value + 1
    i4 = ( i4 // 10 )

  return value

def i4_length_test ( ):

#*****************************************************************************80
#
## i4_length_test() tests i4_length().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 6

  i4_test = np.array ( [ 0, 1, -1, 140, -1952, 123456 ], dtype = int )

  print ( '' )
  print ( 'i4_length_test():' )
  print ( '  i4_length() computes an integer\'s "length".' )
  print ( '' )
  print ( '        I4    Length' )
  print ( '' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    j4 = i4_length ( i4 )

    print ( '  %8d  %8d' % ( i4, j4 ) )

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
  print ( '  i4_log_10() returns the whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def i4_log_2 ( i ):

#*****************************************************************************80
#
## i4_log_2() returns the integer part of the logarithm base 2 of |I|.
#
#  Discussion:
#
#    For positive i4_log_2(I), it should be true that
#      2^i4_log_2(X) <= |I| < 2^(i4_log_2(I)+1).
#    The special case of i4_log_2(0) returns -HUGE().
#
#  Example:
#
#     I  Value
#
#     0  -1
#     1,  0
#     2,  1
#     3,  1
#     4,  2
#     5,  2
#     6,  2
#     7,  2
#     8,  3
#     9,  3
#    10,  3
#   127,  6
#   128,  7
#   129,  7
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
#    integer I, the number whose logarithm base 2 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 2 of
#    the absolute value of I.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0

    i = abs ( i )

    while ( 2 <= i ):
      i = np.floor ( i / 2 )
      value = value + 1

  return value

def i4_log_2_test ( ):

#*****************************************************************************80
#
## i4_log_2_test() tests i4_log_2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  test_num = 17

  x_test = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, \
    -3, -9, 1000, 1023, 1024, 1025 ]
 
  print ( '' )
  print ( 'i4_log_2_test():' )
  print ( '  i4_log_2() returns the whole part of log base 2.' )
  print ( '' )
  print ( '       X     i4_log_2' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test]
    j = i4_log_2 ( x )
    print ( '  %6d  %12d' % ( x, j ) )

  return

def i4_log_i4 ( i4, j4 ):

#*****************************************************************************80
#
## i4_log_i4() returns the logarithm of an I4 to an I4 base.
#
#  Discussion:
#
#    Only the integer part of the logarithm is returned.
#
#    If
#
#      K4 = i4_log_J4 ( I4, J4 )
#
#    then we ordinarily have
#
#      J4^(K4-1) < I4 <= J4^K4.
#
#    The base J4 should be positive, and at least 2.  If J4 is negative,
#    a computation is made using the absolute value of J4.  If J4 is
#    -1, 0, or 1, the logarithm is returned as 0.
#
#    The number I4 should be positive and at least 2.  If I4 is negative,
#    a computation is made using the absolute value of I4.  If I4 is
#    -1, 0, or 1, then the logarithm is returned as 0.
#
#    An I4 is an integer value.
#
#  Example:
#
#    I4  J4  K4
#
#     0   3   0
#     1   3   0
#     2   3   0
#     3   3   1
#     4   3   1
#     8   3   1
#     9   3   2
#    10   3   2
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
#    integer I4, the number whose logarithm is desired.
#
#    integer J4, the base of the logarithms.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm
#    base abs(J4) of abs(I4).
#
  import numpy as np

  value = 0

  i4_abs = np.abs ( i4 )

  if ( 2 <= i4_abs ):

    j4_abs = np.abs ( j4 )

    if ( 2 <= j4_abs ):

      while ( j4_abs <= i4_abs ):
        i4_abs = np.floor ( i4_abs / j4_abs )
        value = value + 1

  return value

def i4_log_i4_test ( ) :

#*****************************************************************************80
#
## i4_log_i4_test() tests i4_log_i4().
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
  print ( 'i4_log_i4_test():' )
  print ( '  i4_log_i4() returns logarithm of I4 base J4,' )
  print ( '' )
  print ( '        I4        J4 i4_log_i4' )
  print ( '' )

  for j4 in range ( 2, 6 ):
    for i4 in range ( 0, 11 ):
      k = i4_log_i4 ( i4, j4 )
      print ( '  %8d  %8d  %8d' % ( i4, j4, k ) )
    print ( '' )

  return

def i4_log_r8 ( x, b ):

#*****************************************************************************80
#
## i4_log_r8() returns the integer part of the logarithm base ABS(B) of ABS(X).
#
#  Example:
#
#    If B is greater than 1, and X is positive:
#
#    if 1/B^2  <  X <= 1/B   i4_log_r8(X) = -1,
#    if 1/B    <  X <= 1     i4_log_r8(X) = 0,
#    if 1      <= X <  B,    i4_log_r8(X) = 0,
#    if B      <= X <  B^2   i4_log_r8(X) = 1,
#    if B^2    <= X <  B^3   i4_log_r8(X) = 2.
#
#    For positive i4_log_r8(X), it should be true that
#
#      ABS(B)^i4_log_r8(X) <= ABS(X) < ABS(B)^(i4_log_r8(X)+1).
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
#    integer X, the number whose logarithm base B is desired.
#    If X is 0, then i4_log_r8 is returned as -HUGE().
#
#    real B, the absolute value of the base of the
#    logarithms.  B must not be -1, 0, or 1.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm
#    base abs(B) of X.
#
  import numpy as np

  i4_huge = 2147483647

  x = np.floor ( x )

  if ( x == 0 ):
    value = - i4_huge
    return value

  b = np.abs ( b )
  value = 0

  if ( b == 1.0 ):
    return value

  if ( b == 0.0 ):
    return value

  x = np.abs ( x )

  if ( b < 1.0 ):
    value_sign = -1
    b = 1.0 / b
  else:
    value_sign = +1

  if ( 1.0 <= x and x < b ):
    value = value_sign * value
    return value

  while ( b < x ):
    x = x / b
    value = value + 1

  while ( x * b <= 1.0 ):
    x = x * b
    value = value - 1
#
#  If the absolute value of the base was less than 1, we inverted
#  earlier.  Now negate the logarithm to account for that.
#
  value = value_sign * value

  return value

def i4_log_r8_test ( ):

#*****************************************************************************80
#
## i4_log_r8_test() tests i4_log_r8().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  test_num = 10

  b_test = [ 2.0, 3.0,  4.0,  5.0,   6.0, 7.0, 8.0, 16.0, 32.0, 256.0 ]

  x = 16
 
  print ( '' )
  print ( 'i4_log_r8_test():' )
  print ( '  i4_log_r8() returns whole part of log base B,' )
  print ( '' )
  print ( '  X    B   i4_log_r8' )
  print ( '' )

  for test in range ( 0, test_num ):
 
    b = b_test[test]
    j = i4_log_r8 ( x, b )

    print ( '  %6d  %12f  %12d' % ( x, b, j ) )

  return

def i4_mant ( x ) :

#*****************************************************************************80
#
## i4_mant() computes the "mantissa" of an R8.
#
#  Discussion:
#
#    This routine computes the "mantissa" or "fraction part" of a real
#    number X, which it stores as a pair of integers, (J/K).
#
#    It also computes the sign, and the integer part of the logarithm
#    (base 2) of X.
#
#    On return:
#
#      X = S * (J/K) * 2^L
#
#    where
#
#      S is +1 or -1,
#      K is a power of 2,
#      1 <= (J/K) < 2,
#      L is an integer.
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
#    integer J, the top part of the mantissa fraction.
#
#    integer K, the bottom part of the mantissa
#    fraction.  K is a power of 2.
#
#    integer L, the integer part of the logarithm (base 2) of X.
#

#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    s = 1
    j = 0
    k = 1
    l = 0
    return s, j, k, l
#
#  2: Determine the sign S.
#
  if ( 0.0 < x ):
    s = 1
  else:
    s = -1
    x = -x
#
#  3: Force X to lie between 1 and 2, and compute the logarithm L.
#
  l = 0

  while ( 2.0 <= x ):
    x = x / 2.0
    l = l + 1

  while ( x < 1.0 ):
    x = x * 2.0
    l = l - 1
#
#  4: Now strip out the mantissa as J/K.
#
  j = 0
  k = 1

  while ( True ):

    j = 2 * j

    if ( 1.0 <= x ):
      j = j + 1
      x = x - 1.0

    if ( x == 0.0 ):
      break

    k = 2 * k
    x = x * 2.0

  return s, j, k, l

def i4_mant_test ( ) :

#*****************************************************************************80
#
## i4_mant_test() tests i4_mant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  x = -314.159

  print ( '' )
  print ( 'i4_mant_test():' )
  print ( '  i4_mant() decomposes an integer.' )
  print ( '' )
  print ( '  Number to be decomposed is X = %f' % ( x ) )

  s, j, k, l = i4_mant ( x )

  print ( '' )
  print ( '  X = %d * ( %d / %d ) * 2 ^ (%d)' % ( s, j, k, l ) )

  return

def i4mat_flip_cols ( m, n, a ):

#*****************************************************************************80
#
## i4mat_flip_cols() swaps the columns of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#    To "flip" the columns of an I4MAT is to start with something like
#
#      11 12 13 14 15
#      21 22 23 24 25
#      31 32 33 34 35
#      41 42 43 44 45
#      51 52 53 54 55
#
#    and return
#
#      15 14 13 12 11
#      25 24 23 22 21
#      35 34 33 32 31
#      45 44 43 42 41
#      55 54 53 52 51
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#  Output:
#
#    integer B(M,N), the flipped matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ], dtype = int )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i,j] = a[i,n-1-j]

  return b

def i4mat_flip_cols_test ( ):

#*****************************************************************************80
#
## i4mat_flip_cols_test() tests i4mat_flip_cols().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_flip_cols_test():' )
  print ( '  i4mat_flip_cols() reverses the order of matrix columns.' )

  m = 6
  n = 5
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  b = i4mat_flip_cols ( m, n, a )

  i4mat_print ( m, n, b, '  The column-flipped matrix:' )

  return

def i4mat_flip_rows ( m, n, a ):

#*****************************************************************************80
#
## i4mat_flip_rows() swaps the rows of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#    To "flip" the rows of an I4MAT is to start with something like
#
#      11 12 13 14 15
#      21 22 23 24 25
#      31 32 33 34 35
#      41 42 43 44 45
#      51 52 53 54 55
#
#    and return
#
#      51 52 53 54 55
#      41 42 43 44 45
#      31 32 33 34 35
#      21 22 23 24 25
#      11 12 13 14 15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#  Output:
#
#    integer B(M,N), the flipped matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i,j] = a[m-1-i,j]

  return b

def i4mat_flip_rows_test ( ):

#*****************************************************************************80
#
## i4mat_flip_rows_test() tests i4mat_flip_rows().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_flip_rows_test():' )
  print ( '  i4mat_flip_rows() reverses the order of matrix rows.' )

  m = 6
  n = 5
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  b = i4mat_flip_rows ( m, n, a )

  i4mat_print ( m, n, b, '  The row-flipped matrix:' )

  return

def i4mat_indicator ( m, n ):

#*****************************************************************************80
#
## i4mat_indicator() sets up an indicator I4MAT.
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
#    integer TABLE(M,N), the indicator table.
#
  import numpy as np

  table = np.zeros ( ( m, n ), dtype = int )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      table[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return table

def i4mat_indicator_test ( ):

#*****************************************************************************80
#
## i4mat_indicator_test() tests i4mat_indicator().
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
  print ( 'i4mat_indicator_test():' )
  print ( '  i4mat_indicator() creates an "indicator" I4MAT.' )

  m = 5
  n = 4
  a = i4mat_indicator ( m, n )
  i4mat_print ( m, n, a, '  The indicator matrix:' )

  return

def i4mat_is_binary ( m, n, x ):

#*****************************************************************************80
#
## i4mat_is_binary() is true if an I4MAT only contains 0 and 1 entries.
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
#    integer X(M,N), the array to be checked.
#
#  Output:
#
#    logical i4mat_is_binary, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      if ( x[i,j] != 0 and x[i,j] != 1 ):
        value = False
        break

  return value

def i4mat_is_binary_test ( ):

#*****************************************************************************80
#
## i4mat_is_binary_test() tests i4mat_is_binary().
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
  print ( 'i4mat_is_binary_test():' )
  print ( '  i4mat_is_binary() is TRUE if an I4MAT only contains' )
  print ( '  0 or 1 entries.' )

  m = 2
  n = 3

  x = np.array ( [ \
    [ 0, 1, 0 ], \
    [ 1, 0, 1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ \
    [ 1, 1, 1 ], \
    [ 1, 1, 1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ \
    [ 0, 1, 0 ], \
    [ 1, 2, 1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_binary ( m, n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  return

def i4mat_is_integer ( m, n, a ):

#*****************************************************************************80
#
## i4mat_is_integer() is TRUE if all entries of an I4MAT are integer.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the array.
#
#  Output:
#
#    logical VALUE, is true if all entries are integer.
#
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( a[i,j] != round ( a[i,j] ) ):
        return False

  return True

def i4mat_is_integer_test ( ):

#*****************************************************************************80
#
## i4mat_is_integer_test() tests i4mat_is_integer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_is_integer_test():' )
  print ( '  i4mat_is_integer() is TRUE if every entry of an I4MAT' )
  print ( '  is an integer.' )

  print ( '' )
  print ( '  Example 1: Obviously integer:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  print ( '' )
  print ( '  Example 2: Obviously NOT integer:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6.5 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  print ( '' )
  print ( '  Example 3: Not Integer, Not obvious:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5.000000001, 6 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  print ( '' )
  print ( '  Example 4: Not Integer, Not obvious:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1.0, 2, 300000000.2 ], \
    [ 4, 5, 6 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  return

def i4mat_is_ternary ( m, n, x ):

#*****************************************************************************80
#
## i4mat_is_ternary() is true if an I4MAT only contains -1, 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimension of the array.
#
#    integer X(M,N), the array to be checked.
#
#  Output:
#
#    logical i4mat_is_ternary, is true (1) if X only contains
#    -1, 0 and 1 entries.
#
  value = True

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      if ( x[i,j] != -1 and x[i,j] != 0 and x[i,j] != 1 ):
        value = False
        break

  return value

def i4mat_is_ternary_test ( ):

#*****************************************************************************80
#
## i4mat_is_ternary_test() tests i4mat_is_ternary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_is_ternary_test():' )
  print ( '  i4mat_is_ternary() is TRUE if an I4MAT only contains' )
  print ( '  -1, 0 and +1 entries.' )

  m = 2
  n = 3

  x = np.array ( [ \
    [  0, -1,  0 ], \
    [ +1,  0, +1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_ternary ( m, n, x ) ):
    print ( '  X is ternary' )
  else:
    print ( '  X is NOT ternary.' )

  x = np.array ( [ \
    [ +1, +1, +1 ], \
    [ +1, +1, +1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_ternary ( m, n, x ) ):
    print ( '  X is ternary' )
  else:
    print ( '  X is NOT ternary.' )

  x = np.array ( [ \
    [  0, +1,  0 ], \
    [ -1, +2, -1 ] ] )
  i4mat_print ( m, n, x, '  X:' )
  if ( i4mat_is_ternary ( m, n, x ) ):
    print ( '  X is ternary' )
  else:
    print ( '  X is NOT ternary.' )

  return

def i4mat_max ( m, n, a ):

#*****************************************************************************80
#
## i4mat_max() returns the largest value in an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix.
#
#  Output:
#
#    integer VALUE, the largest of the entries.
#
  i4_huge = 2147483647
  value = - i4_huge

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = max ( value, a[i,j] )

  return value

def i4mat_max_test ( rng ):

#*****************************************************************************80
#
## i4mat_max_test() tests i4mat_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2014
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
  print ( 'i4mat_max_test():' )
  print ( '  i4mat_max() returns the maximum entry.' )

  m = 5
  n = 7
  a = 0
  b = 10
  x = rng.integers ( low = a, high = b, size = ( m, n ), endpoint = True )

  i4mat_print ( m, n, x, '  The matrix:' )
  
  x_max = i4mat_max ( m, n, x )

  print ( '' )
  print ( '  Maximum entry = %d' % ( x_max ) )

  return

def i4mat_min ( m, n, a ):

#*****************************************************************************80
#
## i4mat_min() returns the smallest value in an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix.
#
#  Output:
#
#    integer VALUE, the smallest of the entries.
#
  i4_huge = 2147483647
  value = i4_huge

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = min ( value, a[i,j] )

  return value

def i4mat_min_test ( rng ):

#*****************************************************************************80
#
## i4mat_min_test() tests i4mat_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2014
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
  print ( 'i4mat_min_test():' )
  print ( '  i4mat_min() returns the minimum entry.' )

  m = 5
  n = 7
  a = 0
  b = 10
  x = rng.integers ( low = a, high = b, size = ( m, n ), endpoint = True )

  i4mat_print ( m, n, x, '  The matrix:' )
  
  x_min = i4mat_min ( m, n, x )

  print ( '' )
  print ( '  Minimum entry = %d' % ( x_min ) )

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

  c = np.zeros ( [ n1, n3 ], dtype = int )

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
  print ( 'i4mat_print_test:' )
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

def i4mat_product_elementwise ( m, n, a, b ):

#*****************************************************************************80
#
## i4mat_product_elementwise() returns the elementwise produce to two I4MAT's.
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
#    integer A(M,N), B(M,N), the two matrices.
#
#  Output:
#
#    integer VALUE, the elementwise product of A and B.
#
  value = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      value = value + a[i,j] * b[i,j]

  return value

def i4mat_product_elementwise_test ( ):

#*****************************************************************************80
#
## i4mat_product_elementwise_test() tests i4mat_product_elementwise().
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
  print ( 'i4mat_product_elementwise_test():' )
  print ( '  i4mat_product_elementwise() computes the elementwise' )
  print ( '  product of two I4MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ] ] )

  b = np.array ( [ \
    [ 1, 3, 5 ], \
    [ 2, 4, 6 ] ])

  i4mat_print ( m, n, a, '  A:' )
  i4mat_print ( m, n, b, '  B:' )

  t = i4mat_product_elementwise ( m, n, a, b )
 
  print ( '' );
  print ( '  Elementwise product = %d' % ( t ) )

  return

def i4mat_rank ( m, n, a ):

#*****************************************************************************80
#
## i4mat_rank() computes the rank of an I4MAT.
#
#  Discussion:
#
#    Because this function assumes the input matrix contains only integer
#    values, it is possible to report the matrix rank without any fear
#    of roundoff error producing an incorrect result.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be analyzed. 
#
#  Output:
#
#    integer RANK_a, the rank of the matrix.
#    0 <= RANK_a <= min ( M, N ).
#
  if ( not i4mat_is_integer ( m, n, a ) ):
    print ( '' )
    print ( 'i4mat_ref(): Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    raise Exception ( 'i4mat_ref(): Fatal error!' )

  lead = 0
  rank_a = 0
 
  for r in range ( 0, m ):

    if ( n <= lead ):
      break
#
#  Start I at row R, and search for nonzero pivot entry A(I,LEAD).
#
    i = r

    while ( a[i,lead] == 0 ):

      i = i + 1
#
#  If reach last row, reset I to R, and increment LEAD.
#
      if ( m <= i ):
        i = r
        lead = lead + 1
#
#  If reach last column, we can find no more pivots.
#
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break
#
#  Increase rank by 1.
#
    rank_a = rank_a + 1
#
#  Move pivot I into row R.
#
    if ( i != r ):
      temp     = a[i,0:n]
      a[i,0:n] = a[r,0:n]
      a[r,0:n] = temp
#
#  Ensure pivot is positive.
#
    if ( a[r,lead] < 0 ):
      a[r,0:n] = - a[r,0:n]
#
#  Remove any common factor from row R.
#
    a[r,0:n], ifact = i4vec_red ( n, a[r,0:n], 1 )
#
#  Use a multiple of A(R,LEAD) to eliminate A(R+1:M,LEAD).
#
    for i in range ( 0, m ):

      if ( i != r ):

        a[i,0:n] = a[r,lead] * a[i,0:n] - a[i,lead] * a[r,0:n]

        a[i,0:n], ifact = i4vec_red ( n, a[i,0:n], 1 )

    lead = lead + 1

  return rank_a

def i4mat_rank_test ( ):

#*****************************************************************************80
#
## i4mat_rank_test() tests i4mat_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_rank_test():' )
  print ( '  i4mat_rank() computes the rank of an integer matrix.' )

  m = 3
  n = 3
  a1 = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ], \
    [ 7, 8, 9 ] ] )

  i4mat_print ( m, n, a1, '  Matrix A1:' )

  rank_a = i4mat_rank ( m, n, a1 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 3
  n = 3
  a2 = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ], \
    [ 7, 8, 0 ] ] )

  i4mat_print ( m, n, a2, '  Matrix A2:' )

  rank_a = i4mat_rank ( m, n, a2 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 4
  n = 3
  a3 = np.array ( [ \
    [  1,  2,  3 ], \
    [  4,  5,  6 ], \
    [  7,  8,  0 ], \
    [ 10, 11, 12 ] ] )

  i4mat_print ( m, n, a3, '  Matrix A3:' )

  rank_a = i4mat_rank ( m, n, a3 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 3
  n = 4
  a4 = np.array ( [ \
    [ 1, 2, 3, 7 ], \
    [ 4, 5, 6, 8 ], \
    [ 7, 8, 0, 3 ] ] )

  i4mat_print ( m, n, a4, '  Matrix A4:' )

  rank_a = i4mat_rank ( m, n, a4 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 5
  n = 3
  a5 = np.array ( [ \
    [  1,  2,  3 ], \
    [  4,  5,  6 ], \
    [  7,  8,  9 ], \
    [ 10, 11, 12  ], \
    [  3,  3,  3 ] ] )

  i4mat_print ( m, n, a5, '  Matrix A5:' )

  rank_a = i4mat_rank ( m, n, a5 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 3
  n = 2
  a6 = np.array ( [ \
    [ 0,  0 ], \
    [ 0,  0 ], \
    [ 0,  0 ] ] )

  i4mat_print ( m, n, a6, '  Matrix A6:' )

  rank_a = i4mat_rank ( m, n, a6 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  return

def i4mat_ref ( m, n, a ):

#*****************************************************************************80
#
## i4mat_ref() computes the integer row echelon form (IREF) of an I4MAT.
#
#  Discussion:
#
#    If a matrix A contains only integer entries, then when it is reduced
#    to row echelon form, it is likely that many entries will no longer
#    be integers, due to the elimination process.
#
#    In some cases, tiny arithmetic errors in this elimination process can
#    result in spurious, tiny nonzero values which can invalidate the
#    calculation, particular if the elimination is being done in an effort
#    to determine the rank of the matrix.  These serious errors can easily
#    occur in very small matrices, such as of size 7x10.
#
#    If we, instead, insist on using only integer operations on an integer
#    matrix, we can guarantee that tiny roundoff errors will not cause
#    such problems.  On the other hand, as the elimination process proceeds,
#    we may instead calculate integer matrix entries of increasingly
#    large, and then ultimately meaningless magnitude.  I imagine this is 
#    likely to happen for moderate size matrices of order 50x50, say, but
#    this is a huge improvement over the unreliability of the real
#    arithmetic case.
#
#
#    Thus, we define "integer row echelon form" (IREF).
#
#
#    A matrix is in integer row echelon form if:
#
#    * The leading nonzero in each row is positive.
#
#    * Each row has no common factor greater than 1.
#
#    * The leading nonzero in each row occurs in a column to
#      the right of the leading nonzero in the previous row.
#
#    * Rows which are entirely zero occur last.
#
#  Example:
#
#    Input matrix:
#
#     1    3    0    2    6    3    1
#    -2   -6    0   -2   -8    3    1
#     3    9    0    0    6    6    2
#    -1   -3    0    1    0    9    3
#
#    Output matrix:
#
#     1    3    0    2    6    3    1
#     0    0    0    2    4    9    3
#     0    0    0    0    0    3    1
#     0    0    0    0    0    0    0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2018
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
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be analyzed.
#
#  Output:
#
#    integer A(M,N), the IREF of the matrix.
#
#    integer DET, the pseudo-determinant of the REF.
#
  if ( not i4mat_is_integer ( m, n, a ) ):
    print ( '' )
    print ( 'i4mat_ref(): Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    raise Exception ( 'i4mat_ref(): Fatal error!' )

  lead = 0
  det = 1
 
  for r in range ( 0, m ):

    if ( n <= lead ):
      break
#
#  Start I at row R, and search for nonzero pivot entry A(I,LEAD).
#
    i = r

    while ( a[i,lead] == 0.0 ):

      i = i + 1
#
#  If reach last row, reset I to R, and increment LEAD.
#
      if ( m <= i ):
        i = r
        lead = lead + 1
#
#  If reach last column, we can find no more pivots.
#
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break
#
#  Move pivot I into row R.
#
    if ( i != r ):
      i4mat_row_swap ( m, n, a, i, r )
#
#  Ensure pivot is positive.
#
    if ( a[r,lead] < 0 ):
      a[r,0:n] = - a[r,0:n]
      det = - det
#
#  Update the pseudo-determinant.
#
    det = det * a[r,lead]
#
#  Remove any common factor from row R.
#
    a[r,0:n], ifact = i4vec_red ( n, a[r,0:n], 1 )
#
#  Use a multiple of A(R,LEAD) to eliminate A(R+1:M,LEAD).
#
    for i in range ( r + 1, m ):

      a[i,0:n] = a[r,lead] * a[i,0:n] - a[i,lead] * a[r,0:n]

      a[i,0:n], ifact = i4vec_red ( n, a[i,0:n], 1 )

    lead = lead + 1

  return a, det

def i4mat_ref_test ( ):

#*****************************************************************************80
#
## i4mat_ref_test() tests i4mat_ref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array ( [ \
    [  1,  3,  0,  2,  6,  3,  1 ], \
    [ -2, -6,  0, -2, -8,  3,  1 ], \
    [  3,  9,  0,  0,  6,  6,  2 ], \
    [ -1, -3,  0,  1,  0,  9,  3 ] ] )

  print ( '' )
  print ( 'i4mat_ref_test():' )
  print ( '  i4mat_ref() computes the integer row echelon form of an I4MAT.' )

  i4mat_print ( m, n, a, '  Input A:' )

  a, det = i4mat_ref ( m, n, a )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a, '  IREF of A:' )

  return

def i4mat_row_reduce ( m, n, i, a ):

#*****************************************************************************80
#
## i4mat_row_reduce() divides out common factors in row I of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's.
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
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#
#    integer I, the row to be reduced.  0 <= I < M.
#
#    integer A[M,N], the matrix whose row is to be reduced.
#
#  Output:
#
#    integer A[M,N], row I of the matrix has been reduced.
#
  a[i,:], common_factor = i4vec_red ( n, a[i,:], 1 )

  return a

def i4mat_row_reduce_test ( ):

#*****************************************************************************80
#
## i4mat_row_reduce_test() tests i4mat_row_reduce().
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

  m = 5
  n = 3

  print ( '' )
  print ( 'i4mat_row_reduce_test():' )
  print ( '  i4mat_row_reduce() divides out any common factors in the' )
  print ( '  entries of a row of an I4MAT.' )

  a = np.array ( [ \
    [  12, 88,   9 ], \
    [   4,  8, 192 ], \
    [ -12, 99,  94 ], \
    [  30, 18,  42 ], \
    [   0,  4,   8 ] ] )

  i4mat_print ( m, n, a, '  Original matrix:' )

  for i in range ( m - 1, -1, -1 ):
    a = i4mat_row_reduce ( m, n, i, a )
    i4mat_print ( m, n, a, '  After reducing a row:' )

  return

def i4mat_row_swap ( m, n, a, i1, i2 ):

#*****************************************************************************80
#
## i4mat_row_swap() swaps rows in an I4MAT.
#
#  Discussion:
#
#    Because Python/Numpy makes it fiendishly difficult to do simple things.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#    integer I1, I2, the indices of the rows.
#    0 <= I1, I2 < M.
#
#  Output:
#
#    integer B(M,N), the flipped matrix.
#
  if ( i1 != i2 ):

    for j in range ( 0, n ):
      t       = a[i1,j]
      a[i1,j] = a[i2,j]
      a[i2,j] = t

  return a

def i4mat_row_swap_test ( ):

#*****************************************************************************80
#
## i4mat_row_swap_test() tests i4mat_row_swap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_row_swap_test():' )
  print ( '  i4mat_row_swap() swaps two rows in an I4MAT.' )

  m = 6
  n = 5
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  i1 = 1
  i2 = 4
  a2 = i4mat_row_swap ( m, n, a, i1, i2 )

  i4mat_print ( m, n, a2, '  After swapping rows 1 and 4:' )

  return

def i4mat_rref ( m, n, a ):

#*****************************************************************************80
#
## i4mat_rref() computes the reduced row echelon form of an I4MAT.
#
#  Discussion:
#
#    If a matrix A contains only integer entries, then when it is transformed
#    to row reduced echelon form, it is likely that many entries will no longer
#    be integers, due to the elimination process.
#
#    In some cases, tiny arithmetic errors in this elimination process can
#    result in spurious, tiny nonzero values which can invalidate the
#    calculation, particular if the elimination is being done in an effort
#    to determine the rank of the matrix.  These serious errors can easily
#    occur in very small matrices, such as of size 7x10.
#
#    If we, instead, insist on using only integer operations on an integer
#    matrix, we can guarantee that tiny roundoff errors will not cause
#    such problems.  On the other hand, as the elimination process proceeds,
#    we may instead calculate integer matrix entries of increasingly
#    large, and then ultimately meaningless magnitude.  I imagine this is 
#    likely to happen for moderate size matrices of order 50x50, say, but
#    this is a huge improvement over the unreliability of the real
#    arithmetic case.
#
#
#    Thus, we define "integer row reduced echelon form" (IRREF):
#
#
#    A matrix is in integer row reduced echelon form if:
#
#    * The leading nonzero in each row is positive.
#
#    * Each row has no common factor greater than 1.
#
#    * The leading nonzero in each row occurs in a column to
#      the right of the leading nonzero in the previous row.
#
#    * Rows which are entirely zero occur last.
#
#    * When a row contains a leading nonzero in column J, then column J
#      is otherwise entirely zero.
#
#  Example:
#
#    Input matrix:
#
#     1    3    0    2    6    3    1
#    -2   -6    0   -2   -8    3    1
#     3    9    0    0    6    6    2
#    -1   -3    0    1    0    9    3
#
#    Output matrix:
#
#     1    3    0    0    2    0    0
#     0    0    0    1    2    0    0
#     0    0    0    0    0    3    1
#     0    0    0    0    0    0    0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2018
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
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be analyzed. 
#
#  Output:
#
#    integer A(M,N), the IRREF of the matrix.
#
#    integer DET, the pseudo-determinant.
#
  if ( not i4mat_is_integer ( m, n, a ) ):
    print ( '' )
    print ( 'i4mat_ref(): Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    raise Exception ( 'i4mat_ref(): Fatal error!' )

  lead = 0
  det = 1
 
  for r in range ( 0, m ):

    if ( n <= lead ):
      break
#
#  Start I at row R, and search for nonzero pivot entry A(I,LEAD).
#
    i = r

    while ( a[i,lead] == 0.0 ):

      i = i + 1
#
#  If reach last row, reset I to R, and increment LEAD.
#
      if ( m <= i ):
        i = r
        lead = lead + 1
#
#  If reach last column, we can find no more pivots.
#
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break
#
#  Move pivot I into row R.
#
    if ( i != r ):
      i4mat_row_swap ( m, n, a, i, r )
#
#  Ensure pivot is positive.
#
    if ( a[r,lead] < 0 ):
      a[r,0:n] = - a[r,0:n]
      det = - det
#
#  Update the pseudo-determinant.
#
    det = det * a[r,lead]
#
#  Remove any common factor from row R.
#
    a[r,0:n], ifact = i4vec_red ( n, a[r,0:n], 1 )
#
#  Use a multiple of A(R,LEAD) to eliminate A(R+1:M,LEAD).
#
    for i in range ( 0, m ):

      if ( i != r ):

        a[i,0:n] = a[r,lead] * a[i,0:n] - a[i,lead] * a[r,0:n]

        a[i,0:n], ifact = i4vec_red ( n, a[i,0:n], 1 )

    lead = lead + 1

  return a, det

def i4mat_rref_test ( ):

#*****************************************************************************80
#
## i4mat_rref_test() tests i4mat_rref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array ( [ \
    [  1,  3,  0,  2,  6,  3,  1 ], \
    [ -2, -6,  0, -2, -8,  3,  1 ], \
    [  3,  9,  0,  0,  6,  6,  2 ], \
    [ -1, -3,  0,  1,  0,  9,  3 ] ] )

  print ( '' )
  print ( 'i4mat_rref_test():' )
  print ( '  i4mat_rref() computes the integer reduced row echelon form (IRREF)' )
  print ( '  of an I4MAT.' )

  i4mat_print ( m, n, a, '  Input A:' )

  a, det = i4mat_rref ( m, n, a )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a, '  IRREF form:' )

  return

def i4mat_rref_solve_binary_nz ( m, n, nz, a, b ):

#*****************************************************************************80
#
## i4mat_rref_solve_binary_nz() seeks binary solutions of an IRREF system.
#
#  Discussion:
#
#    An MxN linear system A*x = b is considered.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to integer row-reduced echelon form (IRREF).
#
#    In order to solve a particular combinatorial problem, only binary
#    solutions x are of interest that is, each entry of x is either 0 or 1.
#
#    Moreover, we know that exactly NZ of the variables are 1.
#
#    The solution procedure involves two steps:
#    * assign each free variable a value of 0 or 1, but never assign more
#      that NZ nonzeroes
#    * solve for the dependent variables.
#
#    We consider every possible assignment of free variables, and we save
#    the solutions in which all the variables take on only 0 or 1 values.
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
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer NZ, the number of nonzeros required in any binary solution.
#
#    real A(M,N), the IRREF matrix to be analyzed. 
#
#    real B(M), the right hand side.
#
#  Output:
#
#    integer X_NUM, the number of binary solutions discovered.
#    Note that there may be no binary solutions at all.
#
#    real X(N,X_NUM), the solutions.
#
  import numpy as np
#
#  Augment the original linear system to the NxN system A2 x = B2.
#
  a2, b2, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a, b )
#
#  Initialize the list of solutions.
#
  x_num = 0
  x = np.zeros ( [ n, x_num ] )
#
#  If FREEDOM_NUM < 0, then the system is overdetermined and cannot be solved.
#
  if ( freedom_num < 0 ):
    return x_num, x
#
#  There are FREEDOM_NUM degrees of freedom, each of which could be set to 1.
#  There must be NZ variables set to 1.
#  Consider setting NZ2 degrees of freedom to 1, where NZ2 is between 0
#  and the minimum of NZ and FREEDOM_NUM.
#
#  Choose every possible selection of NZ2 degrees of freedom, and solve
#  the system.
#
#  If the resulting solution is binary, then add it to the list.
#
  b_num = 0

  for nz2 in range ( 0, min ( nz, freedom_num ) + 1 ):

    done = True
    free_sub = []

    while ( True ):

      free_sub, done = ksub_next4 ( freedom_num, nz2, free_sub, done )

      if ( done ):
        break

      b3 = b2.copy ( )
#
#  Moron error:
#  only integer scalar arrays can be converted to a scalar index
#     b2[freedom[free_sub[0:nz2]]] = 1
#
      for k in range ( 0, nz2 ):
        j = free_sub[k] - 1
        i = freedom[j]
        b3[i] = 1

      b_num = b_num + 1

      y = i4mat_u_solve ( n, a2, b3 )

      if ( i4vec_is_binary ( y ) ):
        y = np.reshape ( y, ( n, 1 ) )
        x = np.hstack ( ( x, y ) )
        x_num = x_num + 1

  return x_num, x

def i4mat_rref_solve_binary_nz_test ( ):

#*****************************************************************************80
#
## i4mat_rref_solve_binary_nz_test() tests i4mat_rref_solve_binary_nz().
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

  print ( '' )
  print ( 'i4mat_rref_solve_binary_nz_test():' )
  print ( '  i4mat_rref_solve_binary_nz() seeks binary solutions of' )
  print ( '  an Integer Reduced Row Echelon Form (IRREF) system A*x=b' )
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

  i4mat_print ( m, n, a, '  The IRREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  i4vec_print ( m, b, '  The right hand side b:' )

  nz = 4
  print ( '' )
  print ( '  Only consider binary solutions with exactly %d nonzeros.' % ( nz ) )

  x_num, x = i4mat_rref_solve_binary_nz ( m, n, nz, a, b )

  i4mat_print ( n, x_num, x, '  Binary solution vectors x:' )

  return

def i4mat_rref_solve_binary ( m, n, a, b ):

#*****************************************************************************80
#
## i4mat_rref_solve_binary() seeks binary solutions of an IRREF system.
#
#  Discussion:
#
#    An MxN linear system A*x = b is considered.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to integer row-reduced echelon form (IRREF).
#
#    In order to solve a particular combinatorial problem, only binary
#    solutions x are of interest that is, each entry of x is either 0 or 1.
#
#    The solution procedure involves two steps:
#    * assign each free variable a value of 0 or 1
#    * solve for the dependent variables.
#
#    We consider every possible assignment of free variables, and we save
#    the solutions in which all the variables take on only 0 or 1 values.
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
#  Input:
#
#    integer M, N, the number of rows and columns of
#    the RREF matrix A.
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
#  Augment the original linear system to the NxN system A2 x = B2.
#
  a2, b2, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a, b )
#
#  Initialize the list of solutions.
#
  x_num = 0
  x = np.zeros ( [ n, x_num ] )
#
#  If FREEDOM_NUM < 0, then the system is overdetermined and cannot be solved.
#
  if ( freedom_num < 0 ):
    return x_num, x
#
#  The indeterminate variables have a simple equation 
#    x(i) = b(i) = 0 or 1
#  Set up and solve every variation of this system.
#  If a solution is binary, accept it.
#
  binary = np.zeros ( freedom_num )

  while ( True ):

    b3 = b2.copy ( )
    for k in range ( 0, freedom_num ):
      i = freedom[k]
      b3[i] = binary[k]

    y = i4mat_u_solve ( n, a2, b3 )

    if ( i4vec_is_binary ( y ) ):
      y = np.reshape ( y, ( n, 1 ) )
      x = np.hstack ( ( x, y ) )
      x_num = x_num + 1

    binary = i4vec_binary_next ( freedom_num, binary )

    if ( np.sum ( binary ) == 0 ):
      break

  return x_num, x

def i4mat_rref_solve_binary_test ( ):

#*****************************************************************************80
#
## i4mat_rref_solve_binary_test() tests i4mat_rref_solve_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_rref_solve_binary_test():' )
  print ( '  i4mat_rref_solve_binary() seeks binary solutions of' )
  print ( '  an Integer Reduced Row Echelon Form (IRREF) system A*x=b' )
  print ( '  when A and b contain integer values.' )

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

  i4mat_print ( m, n, a, '  The IRREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  i4vec_print ( m, b, '  The right hand side b:' )

  x_num, x = i4mat_rref_solve_binary ( m, n, a, b )

  i4mat_print ( n, x_num, x, '  Binary solution vectors x:' )

  return

def i4mat_rref_system ( m, n, a, b ):

#*****************************************************************************80
#
## i4mat_rref_solve_system() sets up an augmented IRREF linear system.
#
#  Discussion:
#
#    An MxN linear system A*X = B is considered.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to integer row-reduced echelon form (IRREF).
#
#    To create, if possible, a solvable NxN system, this function removes
#    trailing zero rows, and inserts where necessary, rows of the identity
#    matrix in A and zeros in B, corresponding to undetermined degrees of 
#    freedom, producing the NxN system:
#
#      A2 * X = B2
#
#    The function also indicates whether the initial system was inconsistent,
#    and identifies those rows of A2 that correspond to degrees of freedom.
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
#  Input:
#
#    integer M, N, the number of rows and columns of the IRREF matrix A.
#
#    integer A(M,N), the IRREF matrix to be analyzed. 
#
#    integer B(M), the IRREF right hand side.
#
#  Output:
#
#    integer A2(N,N), the modified IRREF matrix.
#
#    integer B2(N), the modified IRREF right hand side.
#
#    logical INCON, is TRUE if the system A*X=B is inconsistent.
#
#    integer FREEDOM_NUM, the number of degrees of freedom.
#    If FREEDOM_NUM < 0, then there are no degrees of freedom and the
#    system is overdetermined.
#
#    integer FREEDOM(FREEDOM_NUM), the indices of the degrees
#    of freedom, presuming 0 <= FREEDOM_NUM.
#
  import numpy as np
#
#  Determine 0 <= M2 <= M, the location of the last nonzero row in A.
#  If any zero row of A has a nonzero B, then the equations are inconsistent.
#
  m2 = m
  incon = False

  while ( 0 < m2 ):

    if ( np.any ( a[m2-1,0:n] != 0 ) ):
      break

    if ( b[m2-1] != 0 ):
      incon = True

    m2 = m2 - 1
#
#  Copying data in Python is obscure.
#  Copying submatrices in Numpy is doubly obscure.
#  Let's do something stupid, but correct!
#
  a2 = np.zeros ( [ n, n ] )
  b2 = np.zeros ( n )
  a2[0:m2,:] = a[0:m2,:]
  b2[0:m2] = b[0:m2]
#
#  Count the indeterminate variables.
#
  freedom_num = n - m2
#
#  If pivot in column J is missing,
#  modify matrix and right hand side.
#  Add J to list of indeterminate variables.
#
  freedom = []

  if ( 0 < freedom_num ):

    for j in range ( 0, n ):
      if ( m2 <= j ):
        row_j = i4vec_identity_row ( n, j )
        a2 = np.vstack ( ( a2[0:m2,0:n], row_j ) )
        b2 = np.concatenate ( ( b2[0:m2], [0] ) )
        freedom.append ( j )
        m2 = m2 + 1
      elif ( a2[j,j] == 0 ):
        row_j = i4vec_identity_row ( n, j )
        a2 = np.vstack ( ( a2[0:j,0:n], row_j, a2[j:m2,0:n] ) )
        b2 = np.concatenate ( ( b2[0:j], [0], b2[j:m2] ) )
        freedom.append ( j )
        m2 = m2 + 1

  return a2, b2, incon, freedom_num, freedom

def i4mat_rref_system_test ( ):

#*****************************************************************************80
#
## i4mat_rref_system_test() tests i4mat_rref_system().
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
  print ( 'i4mat_rref_system_test():' )
  print ( '  i4mat_rref_system() computes the linear system associated' )
  print ( '  with an integer reduced row echelon form of an I4MAT.' )
#
#  "Wide" matrix.
#
  print ( '' )
  print ( '  Look at a "wide" matrix:' )

  m = 4
  n = 7

  a1 = np.array ( [ \
   [  1,  3, 0,  2,  6, 3, 1 ], \
   [ -2, -6, 0, -2, -8, 3, 1 ], \
   [  3,  9, 0,  0,  6, 6, 2 ], \
   [ -1, -3, 0,  1,  0, 9, 3 ] ] )

  i4mat_print ( m, n, a1, '  Input A1:' )

  a2, det = i4mat_rref ( m, n, a1 )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a2, '  A2, the IRREF of A1:' )

  b2 = np.array ( [ 1, 1, 1, 0 ] )
  i4vec_print ( m, b2, '  B2, the right hand side:' )

  a3, b3, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a2, b2 )

  print ( '' )
  if ( incon ):
    print ( '  The original system is INCONSISTENT.' )
  else:
    print ( '  The original system is CONSISTENT.' )

  i4mat_print ( n, n, a3, '  A3, the augmented IRREF:' )
  i4vec_print ( n, b3, '  B3, the augmented RHS:' )
  i4vec_print ( freedom_num, freedom, '  Indices of degrees of freedom.' )
#
#  "Tall" matrix.
#
  print ( '' )
  print ( '  Look at a "tall" matrix:' )

  m = 7
  n = 4

  a1 = np.array ( [ \
    [ 1, -2, 3, -1 ], \
    [ 3, -6, 9, -3 ], \
    [ 0,  0, 0,  0 ], \
    [ 2, -2, 0,  1 ], \
    [ 6, -8, 6,  0 ], \
    [ 3,  3, 6,  9 ], \
    [ 1,  1, 2,  3 ] ] )

  i4mat_print ( m, n, a1, '  Input A1:' )

  a2, det = i4mat_rref ( m, n, a1 )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a2, '  A2, the IRREF of A1:' )

  b2 = np.ones ( m )
  i4vec_print ( m, b2, '  B2, the right hand side:' )

  a3, b3, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a2, b2 )

  print ( '' )
  if ( incon ):
    print ( '  The original system is INCONSISTENT.' )
  else:
    print ( '  The original system is CONSISTENT.' )

  i4mat_print ( n, n, a3, '  A3, the augmented IRREF:' )
  i4vec_print ( n, b3, '  B3, the augmented RHS:' )
  i4vec_print ( freedom_num, freedom, '  Indices of degrees of freedom.' )

  return

def i4mat_sum ( m, n, a ):

#*****************************************************************************80
#
## i4mat_sum() returns the sum of the entries in an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix.
#
#  Output:
#
#    integer VALUE, the sum of the entries.
#
  value = 0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = value + a[i,j]

  return value

def i4mat_sum_test ( rng ):

#*****************************************************************************80
#
## i4mat_sum_test() tests i4mat_sum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2018
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
  print ( 'i4mat_sum_test():' )
  print ( '  i4mat_sum() sums the entries in an I4MAT.' )

  m = 4
  n = 3
  a = 0
  b = 5
  x = rng.integers ( low = a, high = b, size = ( m, n ), endpoint = True )

  i4mat_print ( m, n, x, '  The matrix:' )
  
  x_sum = i4mat_sum ( m, n, x )

  print ( '' )
  print ( '  Sum of entries = %d' % ( x_sum ) )

  return

def i4mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_transpose_print() prints an I4MAT, transposed.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_transpose_print_test ( ):

#*****************************************************************************80
#
## i4mat_transpose_print_test() tests i4mat_transpose_print().
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
  import numpy as np

  print ( '' )
  print ( 'i4mat_transpose_print_test():' )
  print ( '  i4mat_transpose_print() prints an I4MAT, tranposed.' )

  m = 5
  n = 3
  a = np.array ( ( \
    ( 11, 12, 13 ), \
    ( 21, 22, 23 ), \
    ( 31, 32, 33 ), \
    ( 41, 42, 43 ), \
    ( 51, 52, 53 ) ) )
  title = '  A 5 x 3 integer matrix:'
  i4mat_transpose_print ( m, n, a, title )

  return

def i4mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_transpose_print_some() prints a portion of an I4MAT, transposed.
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
      print ( '%7d  ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( ' %4d: ' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_transpose_print_some_test() tests i4mat_transpose_print_some().
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
  print ( 'i4mat_transpose_print_some_test():' )
  print ( '  i4mat_transpose_print_some() prints some of an I4MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, \
    '  Here is I4MAT, rows 0:2, cols 3:5:' )

  return

def i4mat_transpose ( m, n, a ):

#*****************************************************************************80
#
## i4mat_transpose() transposes an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#  Output:
#
#    integer B(N,M), the transposed matrix.
#
  import numpy as np

  b = np.zeros ( [ n, m ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[j,i] = a[i,j]

  return b

def i4mat_transpose_test ( ):

#*****************************************************************************80
#
## i4mat_transpose_test() tests i4mat_transpose().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_transpose_test():' )
  print ( '  i4mat_transpose() transposes an I4MAT.' )

  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  b = i4mat_transpose ( m, n, a )

  i4mat_print ( n, m, b, '  The transposed matrix:' )

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

def i4mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## i4mat_uniform_ab() returns a scaled pseudorandom I4MAT.
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
#    integer M, N, the row and column dimensions of the matrix.
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    integer C(M,N), the randomly chosen integer vector.
#
#    integer SEED, the updated seed.
#
  import numpy as np

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4mat_uniform_ab(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4mat_uniform_ab(): Fatal error!' )

  a = round ( a )
  b = round ( b )

  c = np.zeros ( [ m, n ], dtype = np.int32 )

  for j in range ( 0, n ):

    for i in range ( 0, m ): 

      k =  ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
      r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
        +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
      value = round ( r )

      value = max ( value, min ( a, b ) )
      value = min ( value, max ( a, b ) )

      c[i,j] = value

  return c, seed

def i4mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## i4mat_uniform_ab_test() tests i4mat_uniform_ab().
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

  m = 5
  n = 4
  a = -1
  b = +5
  seed = 123456789

  print ( '' )
  print ( 'i4mat_uniform_ab_test():' )
  print ( '  i4mat_uniform_ab() computes a random R8MAT.' )
  print ( '' )
  print ( '  %d <= X <= %d' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = i4mat_uniform_ab ( m, n, a, b, seed )

  i4mat_print ( m, n, v, '  Random I4MAT:' )

  return

def i4mat_u_solve ( n, a, b ):

#*****************************************************************************80
#
## i4mat_u_solve() solves an upper triangular linear system.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's, stored by (I,J) -> [I+J*M].
#
#    Note that, although A and B are integer valued, the solution X
#    may, in general, be real-valued.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    integer A(N,N), the N by N upper triangular matrix.
#
#    integer B(N), the right hand side of the linear system.
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

def i4mat_u_solve_test ( ):

#*****************************************************************************80
#
## i4mat_u_solve_test() tests i4mat_u_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2018
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
  print ( 'i4mat_u_solve_test():' )
  print ( '  i4mat_u_solve() solves an upper triangular system.' )

  i4mat_print ( n, n, a, '  Input matrix A:' )

  i4vec_print ( n, b, '  Right hand side b:' )

  x = i4mat_u_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )

  return

def i4mat_width ( m, n, a ):

#*****************************************************************************80
#
## i4mat_width() returns the printing width of an I4MAT.
#
#  Discussion:
#
#    The width of an I4MAT is simply the maximum of the widths of
#    its entries.
#
#    The width of a single integer is the number of characters 
#    necessary to print it.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimensions of the array.
#
#    integer A[M,N], the array.
#
#  Output:
#
#    integer VALUE, the width of the array.
#
  value = 0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = max ( value, i4_width ( a[i,j] ) )

  return value

def i4mat_width_test ( ):

#*****************************************************************************80
#
## i4mat_width_test() tests i4mat_width().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4mat_width_test():' )
  print ( '  i4mat_width() determines the printing width of an I4MAT.' )

  m1 = 3
  n1 = 3
  a1 = np.array ( [ \
    [ 11, 211, 3111 ], \
    [ 12, 222, 3222 ], \
    [ 13, 233, 3333 ] ] )

  i4mat_print ( m1, n1, a1, '  A1:' )

  w = i4mat_width ( m1, n1, a1 )

  print ( '' )
  print ( '  The printing width of A1 is %d' % ( w ) )

  m2 = 3
  n2 = 3
  a2 = np.array ( [ \
    [ 10,    23, 45 ], \
    [ 42, -1000, 63 ], \
    [ 77,    63, 90 ] ] )

  i4mat_print ( m2, n2, a2, '  A2:' )

  w = i4mat_width ( m2, n2, a2 )

  print ( '' )
  print ( '  The printing width of A2 is %d' % ( w ) )

  return

def i4_max ( a, b ):

#*****************************************************************************80
#
## i4_max() returns the maximum of two I4's.
#
#  Discussion:
#
#    An I4 is an integer.
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
#    integer A, B, values to compare.
#
#  Output:
#
#    integer VALUE, the maximum of A and B.
#
  if ( a < b ):
    value = b
  else:
    value = a

  return value

def i4_max_test ( rng ):

#*****************************************************************************80
#
## i4_max_test() tests i4_max().
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
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'i4_max_test():' )
  print ( '  i4_max() computes the maximum of two I4\'s.' )

  i4_lo = - 100
  i4_hi = + 100

  print ( '' )
  print ( '         A         B     C=i4_max(A,B)' )
  print ( '' )

  for i in range ( 0, 10 ):
    a = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    b = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    c = i4_max ( a, b )
    print ( '  %8d  %8d  %8d' % ( a, b, c ) )

  return

def i4_min ( a, b ):

#*****************************************************************************80
#
## i4_min() returns the minimum of two I4's.
#
#  Discussion:
#
#    An I4 is an integer.
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
#    integer A, B, values to compare.
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

def i4_min_test ( rng ):

#*****************************************************************************80
#
## i4_min_test() tests i4_min().
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4_min_test():' )
  print ( '  i4_min() computes the minimum of two I4\'s.' )

  i4_lo = - 100
  i4_hi = + 100

  print ( '' )
  print ( '         A         B     C=i4_min(A,B)' )
  print ( '' )

  for i in range ( 0, 10 ):
    a = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    b = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    c = i4_min ( a, b )
    print ( '  %8d  %8d  %8d' % ( a, b, c ) )

  return

def i4_moddiv ( n, d ):

#*****************************************************************************80
#
## i4_moddiv() breaks a number into a multiple of a divisor and remainder.
#
#  Discussion:
#
#    N = M * D + R
#
#    0 <= || R || < || D ||
#
#    R has the sign of N.
#
#  Example:
#
#    N         D       M      R
#
#   107       50      2      7
#   107      -50     -2      7
#  -107       50     -2     -7
#  -107      -50      2     -7
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
#    integer N, the number to be decomposed.
#
#    integer D, the divisor.  D may not be zero.
#
#  Output:
#
#    integer M, the number of times N is evenly divided by D.
#
#    integer R, a remainder.
#
  if ( d == 0 ):
    print ( '' )
    print ( 'i4_moddiv(): Fatal error!' )
    print ( '  Input divisor D = 0' )
    raise Exception ( 'i4_moddiv(): Fatal error!' )

  m = ( n // d )
  r = n - d * m

  return m, r

def i4_moddiv_test ( ):

#*****************************************************************************80
#
## i4_moddiv_test() tests i4_moddiv().
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
  print ( 'i4_moddiv_test():' )
  print ( '  i4_moddiv() factors a number' )
  print ( '  into a multiple M and a remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m, r = i4_moddiv ( n, d )
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

def i4_mod_inv ( b, n ):

#*****************************************************************************80
#
## i4_mod_inv() calculates the inverse of B mod N.
#
#  Discussion:
#
#    This function uses the extended Euclidean algorithm.
#
#    Unless the algorithm fails, the output value Y will satisfy
#
#      ( B * Y ) mod N = 1
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
#    John Burkardt.
#
#  Reference:
#
#    Wade Trappe, Lawrence Washington,
#    Introduction to Cryptography with Coding Theory,
#    Prentice Hall, 2005,
#    ISBN13: 978-0131862395,
#    LC: QA268.T73.
#
#  Input:
#
#    integer B, the value whose inverse is desired.
#    B must not be 0, or a multiple of N.  However, B can be negative.
#
#    integer N, the value with respect to which the inverse is desired.
#    N must be 2 or greater.
#
#  Output:
#
#    integer Y, the inverse of B mod N.  However, if the inverse
#    does not exist, Y is returned as the empty value [].
#
  from numpy import floor

  n0 = n
  b0 = abs ( b )
  t0 = 0
  t = 1

  q = ( n0 // b0 )
  r = n0 - q * b0

  while ( 0 < r ):

    temp = t0 - q * t

    if ( 0 <= temp ):
      temp =           temp   % n
    else:
      temp = n - ( ( - temp ) % n )

    n0 = b0
    b0 = r
    t0 = t
    t = temp

    q = ( n0 // b0 )
    r = n0 - q * b0

  if ( b0 != 1 ):
    y = 0
  else:
    y = ( t % n )
    if ( b < 0 ):
      y = - y

  return y

def i4_mod_inv_test ( ):

#*****************************************************************************80
#
## i4_mod_inv_test() tests i4_mod_inv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_mod_inv_test():' )
  print ( '  i4_mod_inv() finds the inverse of B mod N,' )
  print ( '  that is, Y such that ( B * Y ) mod N = 1.' )
  print ( '' )
  print ( '       B       N       Y     B*YmodN' )
  print ( ' ' )

  n = 17
  for b in range ( 1, 17 ):
    y = i4_mod_inv ( b, n )
    t = ( ( b * y ) % n )
    print ( '  %6d  %6d  %6d  %6d' % ( b, n, y, t ) )

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
  import numpy as np

  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp(): Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp(): Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + np.abs ( j )

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

def i4_mop ( i ):

#*****************************************************************************80
#
## i4_mop() returns the I-th power of -1 as an I4.
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
#    integer I, the power of -1.
#
#  Output:
#
#    integer VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1
  else:
    value = - 1

  return value

def i4_mop_test ( rng ):

#*****************************************************************************80
#
## i4_mop_test() tests i4_mop().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4_mop_test():' )
  print ( '  i4_mop() computes a minus-one-power (-1)^I.' )
  print ( '' )
  print ( '        I4  i4_mop(I4)' )
  print ( '' )

  i4_lo = -1000000
  i4_hi = +1000000
  
  for i in range ( 0, 10 ):
    i4 = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    print ( '  %8d  %10d' % ( i4, i4_mop ( i4 ) ) )

  return

def i4_normal_ab ( mu, sigma, rng ):

#*****************************************************************************80
#
## i4_normal_ab() returns a scaled pseudonormal I4.
#
#  Discussion:
#
#    The normal probability distribution function (PDF) is sampled,
#    with mean MU and standard deviation SIGMA.
#
#    The result is rounded to the nearest integer.
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
#    real MU, the mean of the PDF.
#
#    real SIGMA, the standard deviation of the PDF.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer VALUE, a normally distributed random value.
#
  import numpy as np

  r1 = rng.random ( )
  r2 = rng.random ( )
  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )
  value = int ( mu + sigma * value )

  return value

def i4_normal_ab_test ( rng ):

#*****************************************************************************80
#
## i4_normal_ab_test() tests i4_normal_ab().
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
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'i4_normal_ab_test():' )
  print ( '  i4_normal_ab() computes integer pseudonormal values with' )
  print ( '  mean MU and standard deviation SIGMA.' )

  mu = 10.0
  sigma = 2.0

  print ( '' )
  print ( '  MU = %g' % ( mu ) )
  print ( '  SIGMA = %g' % ( sigma ) )
  print ( '' )
  for i in range ( 0, 10 ):
    r = i4_normal_ab ( mu, sigma, rng )
    print ( '  %2d  %12d' % ( i, r ) )

  return

def i4_not ( i, j ):

#*****************************************************************************80
#
## i4_not() calculates the NOT of an I4 with respect to a maximum value.
#
#  Discussion:
#
#    An I4 is an integer value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the value whose NOT is needed.
#
#    integer J, the maximum value.
#
#  Output:
#
#    integer VALUE, the NOT of I with respect to J.
#
  i1 = i
  j1 = j
  value = 0
  l = 1

  while ( j1 != 0 ):

    i2 = i1 // 2

    if ( i1 == 2 * i2 ):
      value = value + l

    i1 = i2
    l = 2 * l

    j1 = j1 // 2

  return value

def i4_not_test ( rng ):

#*****************************************************************************80
#
## i4_not_test() tests i4_not().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2016
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

  i4_lo = 0
  i4_hi = 100
  test_num = 10
  j = 255

  print ( '' )
  print ( 'i4_not_test():' )
  print ( '  i4_not() returns the NOT of an I4 with respect to a value J.' )
  print ( '' )
  print ( '         I         J    i4_not    ~I+J+1' )
  print ( '' )

  for test in range ( 0, test_num ):

    i = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    k = i4_not ( i, j )
    l = ~ i + j + 1
    print ( '  %8d  %8d  %8d  %8d' % ( i, j, k, l ) )

  return

def i4_or ( i, j ):

#*****************************************************************************80
#
## i4_or() calculates the inclusive OR of two I4's.
#
#  Discussion:
#
#    An I4 is an integer value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, two values whose inclusive OR is needed.
#
#  Output:
#
#    integer VALUE, the inclusive OR of I and J.
#
  i1 = i
  j1 = j
  value = 0
  l = 1

  while ( i1 != 0 or j1 != 0 ):

    i2 = i1 // 2
    j2 = j1 // 2

    if ( ( i1 != 2 * i2 ) or ( j1 != 2 * j2 ) ):
      value = value + l

    i1 = i2
    j1 = j2
    l = 2 * l

  return value

def i4_or_test ( rng ):

#*****************************************************************************80
#
## i4_or_test() tests i4_or().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2016
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

  i4_lo = 0
  i4_hi = 100
  test_num = 10

  print ( '' )
  print ( 'i4_or_test():' )
  print ( '  i4_or() returns the bitwise inclusive OR of two I4\'s.' )
  print ( '' )
  print ( '         I         J     i4_or       I|J' )
  print ( '' )

  for test in range ( 0, test_num ):

    i = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    j = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    k = i4_or ( i, j )
    l = ( i | j )
    print ( '  %8d  %8d  %8d  %8d' % ( i, j, k, l ) )

  return

def i4_power ( i, j ):

#*****************************************************************************80
#
## i4_power() returns the value of I to the power J.
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
#    integer I, J, the base and the power.  J should be nonnegative.
#
#  Output:
#
#    integer VALUE, the value of I^J.
#
  if ( j < 0 ):

    if ( i == 1 ):
      value = 1
    elif ( i == 0 ):
      print ( '' )
      print ( 'i4_power(): Fatal error!' )
      print ( '  I^J requested, with I = 0 and J negative.' )
      raise Exception ( 'i4_power(): Fatal error!' )
    else:
      value = 0

  elif ( j == 0 ):

    if ( i == 0 ):
      print ( '' )
      print ( 'i4_power(): Fatal error!' )
      print ( '  I^J requested, with I = 0 and J = 0.' )
      raise Exception ( 'i4_power(): Fatal error!' )
    else:
      value = 1

  elif ( j == 1 ):

    value = i

  else:

    value = 1
    for k in range ( 1, j + 1 ):
      value = value * i

  return value

def i4_power_test ( ):

#*****************************************************************************80
#
## i4_power_test() tests i4_power().
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

  test_num = 7
  i_test = np.array ( [ 0, 1, 2, 3, 10, -1, -2 ] )
  j_test = np.array ( [ 1, 2, 3, 3, 3, 4, 5 ] )

  print ( '' )
  print ( 'i4_power_test():' )
  print ( '  i4_power() computes I^J' )
  print ( '' )
  print ( '         I       J  i4_power(I,J)' )
  print ( '' )

  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    print ( '  %8d  %8d  %8d' % ( i, j, i4_power ( i, j ) ) )

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
#    integer N_dATA.  The user sets N_dATA to 0 before the
#    first call.
#
#  Output:
#
#    integer N_dATA.  The routine increments N_dATA by 1, and
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
## i4_rise_values_test() tests i4_rise_values().
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

def i4row_max ( m, n, x ):

#*****************************************************************************80
#
## i4row_max() returns the maximums of rows of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer X(M,N), the I4ROW.
#
#  Output:
#
#    integer XMAX(M), the maximums of the rows of X.
#
  import numpy as np

  xmax = np.zeros ( m, dtype = np.int32 )

  for i in range ( 0, m ):
    xmax[i] = x[i,0]
    for j in range ( 1, n ):
      xmax[i] = max ( xmax[i], x[i,j] )

  return xmax

def i4row_max_test ( ):

#*****************************************************************************80
#
## i4row_max_test() tests i4row_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_max_test():' )
  print ( '  i4row_max() computes maximums of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  amax = i4row_max ( m, n, a )

  i4vec_print ( m, amax, '  Row maximums:' )

  return

def i4row_mean ( m, n, a ):

#*****************************************************************************80
#
## i4row_mean() returns the means of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the I4ROW
#
#  Output:
#
#    real ROW_mean(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def i4row_mean_test ( ):

#*****************************************************************************80
#
## i4row_mean_test() tests i4row_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_mean_test():' )
  print ( '  i4row_mean() computes row means of an I4ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  means = i4row_mean ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )

  return

def i4row_min ( m, n, x ):

#*****************************************************************************80
#
## i4row_min() returns the minimums of rows of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer X(M,N), the I4ROW.
#
#  Output:
#
#    integer XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m, dtype = np.int32 )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def i4row_min_test ( ):

#*****************************************************************************80
#
## i4row_min_test() tests i4row_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'i4row_min_test():' )
  print ( '  i4row_min() computes minimums of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  amin = i4row_min ( m, n, a )

  i4vec_print ( m, amin, '  Row minimums:' )

  return

def i4rows_to_i4mat ( m, n, i4rows ):

#*****************************************************************************80
#
## i4rows_to_i4mat() converts a row-major vector to an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's, in column major order.
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
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer i4rows(M*N), the data. stored rowwise in a vector.
#
#  Output:
#
#    integer I4MAT(M,N), a copy of the data, stored columnwise in an array.
#
  import numpy as np

  k = 0
  i4mat = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      i4mat[i,j] = i4rows[k]
      k = k + 1

  return i4mat

def i4rows_to_i4mat_test ( ):

#*****************************************************************************80
#
## i4rows_to_i4mat_test() tests i4rows_to_i4mat().
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

  m = 3
  n = 4
  i4rows = np.array ( [ \
    11, 12, 13, 14, \
    21, 22, 23, 24, \
    31, 32, 33, 34 ] )

  print ( '' )
  print ( 'i4rows_to_i4mat_test():' )
  print ( '  i4rows_to_i4mat() allows an I4MAT to be initialized' )
  print ( '  by data stored ROW-WISE in a vector.' )

  i4vec_print ( m * n, i4rows, '  The data vector:' )

  i4mat = i4rows_to_i4mat ( m, n, i4rows )

  i4mat_print ( m, n, i4mat, '  The data copied into an array:' )

  return

def i4row_variance ( m, n, x ):

#*****************************************************************************80
#
## i4row_variance() returns the variances of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer X(M,N), the I4ROW whose row means are desired.
#
#  Output:
#
#    real VARIANCE(M), the variances of the rows of X.
#
  import numpy as np

  variance = np.zeros ( m, dtype = np.float32 )

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

def i4row_variance_test ( ):

#*****************************************************************************80
#
## i4row_variance_test() tests i4row_variance().
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
  print ( 'i4row_variance_test():' )
  print ( '  i4row_variance() computes variances of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  variance = i4row_variance ( m, n, a )

  r8vec_print ( m, variance, '  The row variances:' )

  return

def i4_sign3 ( i ):

#*****************************************************************************80
#
## i4_sign3() returns the three-way sign of an integer.
#
#  Discussion:
#
#    The value is +1 if the number is positive, 0 if zero, and -1 otherwise.
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
#    integer I, the number whose sign is desired.
#
#  Output:
#
#    integer VALUE, the sign of I.
#
  if ( i < 0 ):
    value = -1
  elif ( i == 0 ):
    value = 0
  else:
    value = +1

  return value

def i4_sign3_test ( ):

#*****************************************************************************80
#
## i4_sign3_test() tests i4_sign3().
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
  print ( 'i4_sign3_test():' )
  print ( '  i4_sign3() returns the three-way sign of an I4.' )
  print ( '' )
  print ( '    I4  i4_sign3(I4)' )
  print ( '' )

  for test in range ( 0, test_num ):
    i4 = i4_vec[test]
    s = i4_sign3 ( i4 )
    print ( '  %4d  %11d' % ( i4, s ) )

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

def i4_swap3 ( i, j, k ) :

#*****************************************************************************80
#
## i4_swap3() swaps three I4's.
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
#  Input:
#
#    integer I, J, K, the values to swap.
#
#  Output:
#
#    integer I, J, K, the swapped values.
#
  return j, k, i

def i4_swap3_test ( ):

#*****************************************************************************80
#
## i4_swap3_test() tests i4_swap3().
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
  print ( '' )
  print ( 'i4_swap3_test():' )
  print ( '  i4_swap3() swaps three I4\'s.' )
  print ( '' )
  print ( '  Starting with (I,J,K), swap 3 times.' )
  print ( '' )

  i = 1
  j = 202
  k = 3003003

  print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  for l in range ( 0, 3 ):
    i, j, k = i4_swap3 ( i, j, k )
    print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  return

def i4_swap ( x, y ) :

#*****************************************************************************80
#
## i4_swap() swaps two I4's.
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
#  Input:
#
#    integer X, Y, two values to interchange.
#
#  Output:
#
#    integer X, Y, the interchanged values.
#
  return y, x

def i4_swap_test ( ):

#*****************************************************************************80
#
## i4_swap_test() tests i4_swap().
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
  print ( '' )
  print ( 'i4_swap_test():' )
  print ( '  i4_swap() swaps two I4\'s.' )

  i = 1
  j = 202

  print ( '' )
  print ( '  Before swapping: ' )
  print ( '' )
  print ( '  I = %d' % ( i ) )
  print ( '  J = %d' % ( j ) )

  i, j = i4_swap ( i, j )

  print ( '' )
  print ( '  After swapping: ' )
  print ( '' )
  print ( '  I = %d' % ( i ) )
  print ( '  J = %d' % ( j ) )

  return

def i4_to_angle ( i ) :

#*****************************************************************************80
#
## i4_to_angle() maps integers to points on a circle.
#
#  Discussion:
#
#    The angles are intended to be used to select colors on a color
#    hexagon whose 6 vertices are red, yellow, green, cyan, blue,
#    magenta.
#
#  Example:
#
#     I   X      ANGLE
#
#     0   0/3      0
#     1   1/3    120
#     2   2/3    240
#
#     3   1/6     60
#     4   3/6    180
#     5   5/6    300
#
#     6   1/12    30
#     7   3/12    90
#     8   5/12   150
#     9   7/12   210
#    10   9/12   270
#    11  11/12   330
#
#    12   1/24    15
#    13   3/24    45
#    14   5/24    75
#    etc
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
#    integer I, the index of the desired color.
#
#  Output:
#
#    real ANGLE, an angle, measured in degrees, between 0 and 360.
#
  import numpy as np

  if ( 0 <= np.abs ( i ) and np.abs ( i ) <= 2 ):

    angle = 120.0 * np.abs ( i )

  else:

    i1 = i4_log_2 ( np.floor ( np.abs ( i ) / 3 ) )
    i2 = np.abs ( i ) + 1 - 3 * ( 2 ** i1 )
    i3 = 2 * ( i2 - 1 ) + 1
    i4 = 3 * ( 2 ** ( i1 + 1 ) )

    angle = ( 360.0 * i3 ) / float ( i4 )

  return angle

def i4_to_angle_test ( ):

#*****************************************************************************80
#
## i4_to_angle_test() tests i4_to_angle(). 
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
  print ( '' )
  print ( 'i4_to_angle_test():' )
  print ( '  i4_to_angle() converts an I4 to an angle in degrees.' )
  print ( '  The angles sample the circle at finer levels.' )
  print ( '' )
  print ( '  I4   ANGLE' )
  print ( '' )

  for i4 in range ( 0, 16 ):

    angle = i4_to_angle ( i4 )
    print ( '  %2d  %14.6g' % ( i4, angle ) )

  return

def i4_to_digits_binary ( i, n ):

#*****************************************************************************80
#
## i4_to_digits_binary() produces the binary digits of an I4.
#
#  Discussion:
#
#    An I4 is an integer.
#
#  Example:
#
#     I    N     C               Binary
#    --  ---   ---         ------------
#     0    1   0                      0
#     0    2   0, 0                  00
#     1    3   1, 0, 0              100
#     2    3   0, 1, 0              010
#     3    3   1, 1, 0              011
#     4    3   0, 0, 1              100
#     8    3   0, 0, 0           (1)000
#     8    5   0, 0, 0, 1, 0      01000
#    -8    5   0, 0, 0, 1, 0  (-) 01000
#
#     0    3   0, 0, 0
#     1    3   1, 0, 0
#     2    3   0, 1, 0
#     3    3   1, 1, 0
#     4    3   0, 0, 1
#     5    3   1, 0, 1
#     6    3   0, 1, 1
#     7    3   1, 1, 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, an integer to be represented.
#
#    integer N, the number of binary digits to produce.
#
#  Output:
#
#    integer C(N), the first N binary digits of I,
#    with C(1) being the units digit.
#
  import math
  import numpy as np

  i_copy = math.floor ( abs ( i ) )

  c = np.zeros ( n )

  for j in range ( 0, n ):

    c[j] = math.floor ( i_copy % 2 )
    i_copy = math.floor ( i_copy / 2 )

  return c

def i4_to_digits_binary_test ( ):

#*****************************************************************************80
#
## i4_to_digits_binary_test() tests i4_to_digits_binary(). 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_digits_binary_test():' )
  print ( '  i4_to_digits_binary() gets N binary digits of an I4.' )
  print ( '' )
  print ( '  I4   Digits' )
  print ( '' )

  n = 6

  for i4 in range ( 0, 16 ):

    c = i4_to_digits_binary ( i4, n )
    print ( '  %2d:' % ( i4 ), end = '' )
    print ( c )

  return

def i4_to_halton ( dim_num, step, seed, leap, base ):

#*****************************************************************************80
#
## i4_to_halton() computes one element of a leaped Halton subsequence.
#
#  Discussion:
#
#    The DIM_NUM-dimensional Halton sequence is really DIM_NUM separate
#    sequences, each generated by a particular base.
#
#    This routine selects elements of a "leaped" subsequence of the
#    Halton sequence.  The subsequence elements are indexed by a
#    quantity called STEP, which starts at 0.  The STEP-th subsequence
#    element is simply element
#
#      SEED(1:DIM_NUM) + STEP * LEAP(1:DIM_NUM)
#
#    of the original Halton sequence.
#
#    An I4 is an integer value.
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
#  Reference:
#
#    John Halton,
#    On the efficiency of certain quasi-random sequences of points
#    in evaluating multi-dimensional integrals,
#    Numerische Mathematik,
#    Volume 2, Number 1, December 1960, pages 84-90
#
#    John Halton, GB Smith,
#    Algorithm 247:
#    Radical-Inverse Quasi-Random Point Sequence,
#    Communications of the ACM,
#    Volume 7, Number 12, December 1964, pages 701-702.
#
#    Ladislav Kocis, William Whiten,
#    Computational Investigations of Low-Discrepancy Sequences,
#    ACM Transactions on Mathematical Software,
#    Volume 23, Number 2, June 1997, pages 266-294.
#
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#    1 <= DIM_NUM is required.
#
#    integer STEP, the index of the subsequence element.
#    0 <= STEP is required.
#
#    integer SEED(DIM_NUM), the Halton sequence index
#    corresponding to STEP = 0.
#    0 <= SEED(1:DIM_NUM) is required.
#
#    integer LEAP(DIM_NUM), the successive jumps in the
#    Halton sequence.  1 <= LEAP(1:DIM_NUM) is required.
#
#    integer BASE(DIM_NUM), the Halton bases.
#    1 < BASE(1:DIM_NUM) is required.
#
#  Output:
#
#    real R(DIM_NUM), the STEP-th element of the leaped Halton subsequence.
#
  import numpy as np
#
#  Check the input.
#
  if ( dim_num < 1 ):
    print ( '' )
    print ( 'i4_to_halton(): Fatal error!' )
    print ( '  DIM_NUM < 1.' )
    raise Exception ( 'i4_to_halton(): Fatal error!' )

  if ( step < 0 ):
    print ( '' )
    print ( 'i4_to_halton(): Fatal error!' )
    print ( ' STEP < 0.' )
    raise Exception ( 'i4_to_halton(): Fatal error!' )

  if ( any ( seed < 0 ) ):
    print ( '' )
    print ( 'i4_to_halton(): Fatal error!' )
    print ( '  Some SEED(*) < 0.' )
    raise Exception ( 'i4_to_halton(): Fatal error!' )

  if ( any ( leap < 1 ) ):
    print ( '' )
    print ( 'i4_to_halton(): Fatal error!' )
    print ( '  Some LEAP < 1.' )
    raise Exception ( 'i4_to_halton(): Fatal error!' )

  if ( any ( base <= 1 ) ):
    print ( '' )
    print ( 'i4_to_halton(): Fatal error!' )
    print ( '  Some BASE <= 1.' )
    raise Exception ( 'i4_to_halton(): Fatal error!' )
#
#  Calculate the data.
#
  r = np.zeros ( dim_num )

  for i in range ( 0, dim_num ):
 
    seed2 = seed[i] + step * leap[i]

    base_inv = 1.0 / base[i]

    while ( seed2 != 0 ):
      digit = ( seed2 % base[i] )
      r[i] = r[i] + digit * base_inv
      base_inv = base_inv / base[i]
      seed2 = seed2 / base[i]
 
  return r

def i4_to_halton_test ( ):

#*****************************************************************************80
#
## i4_to_halton_test() tests i4_to_halton(). 
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
  print ( 'i4_to_halton_test():' )
  print ( '  i4_to_halton() computes a Halton sequence.' )
  print ( '  The user specifies all data explicitly.' )
  print ( '' )
  print ( '  In this test, we call i4_to_halton repeatedly.' )
  print ( '  We use distinct primes as bases.' )

  n = 11

  dim_num = 3
  seed = np.array ( [ 0, 0, 0 ] )
  leap = np.array ( [ 1, 1, 1 ] )
  base = np.array ( [ 2, 3, 5 ] )

  print ( '' )
  print ( '   I    R(0)      R(1)      R(2)' )
  print ( '' )
  for step in range ( 0, n ):
    r = i4_to_halton ( dim_num, step, seed, leap, base )
    print ( '  %2d  %8.4f  %8.4f  %8.4f' % ( step, r[0], r[1], r[2] ) )

  return

def i4_to_isbn ( i ) :

#*****************************************************************************80
#
## i4_to_isbn() converts an I4 to an ISBN digit.
#
#  Discussion:
#
#    Only the integers 0 through 10 can be input.  The representation
#    of 10 is 'X'.
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
#  Reference:
#
#    Book Industry Study Group,
#    The Evolution in Product Identification:
#    Sunrise 2005 and the ISBN-13,
#    http://www.bisg.org/docs/The_Evolution_in_product_ID.pdf
#
#  Input:
#
#    integer I, an integer between 0 and 10.
#
#  Output:
#
#    character VALUE, the ISBN character code of the integer.
#    If I is illegal, then VALUE is set to '?'.
#
  if ( i == 0 ):
    value = '0'
  elif ( i == 1 ):
    value = '1'
  elif ( i == 2 ):
    value = '2'
  elif ( i == 3 ):
    value = '3'
  elif ( i == 4 ):
    value = '4'
  elif ( i == 5 ):
    value = '5'
  elif ( i == 6 ):
    value = '6'
  elif ( i == 7 ):
    value = '7'
  elif ( i == 8 ):
    value = '8'
  elif ( i == 9 ):
    value = '9'
  elif ( i == 10 ):
    value = 'X'
  else:
    value = '?'

  return value

def i4_to_isbn_test ( ):

#*****************************************************************************80
#
## i4_to_isbn_test() tests i4_to_isbn(). 
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
  print ( '' )
  print ( 'i4_to_isbn_test():' )
  print ( '  i4_to_isbn() converts an I4 digit to an ISBN symbol.' )
  print ( '' )
  print ( '  I4   S' )
  print ( '' )

  for i4 in range ( 0, 11 ):

    s1 = i4_to_isbn ( i4 )
    print ( '  %2d   %c' % ( i4, s1 ) )

  return

def i4_to_l4 ( i4 ):

#*****************************************************************************80
#
## i4_to_l4() converts an I4 to an L4.
#
#  Discussion:
#
#    An I4 is an integer value.
#    An L4 is a boolean value.
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
#    integer I4, an integer.
#
#  Output:
#
#    boolean VALUE, the logical value of I4.
#
  value = ( i4 != 0 )

  return value

def i4_to_l4_test ( ):

#*****************************************************************************80
#
## i4_to_l4_test() tests i4_to_l4(). 
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
  print ( '' )
  print ( 'i4_to_l4_test():' )
  print ( '  i4_to_l4() converts an I4 to an L4.' )
  print ( '' )
  print ( '  I4   L4' )
  print ( '' )

  for i4 in range ( - 5, + 6 ):

    l4 = i4_to_l4 ( i4 )
    print ( '  %2d  %s' % ( i4, l4 ) )

  return

def i4_to_pascal_degree ( k ):

#*****************************************************************************80
#
## i4_to_pascal_degree() converts a linear index to a Pascal triangle degree.
#
#  Discussion:
#
#    We describe the grid points in Pascal's triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#    The quantity D represents the "degree" of the corresponding monomial,
#    that is, D = I + J.
#
#    We can compute D directly from K using the quadratic formula.
#
#  Example:
#
#     K  I  J  D
#
#     1  0  0  0
#
#     2  1  0  1
#     3  0  1  1
#
#     4  2  0  2
#     5  1  1  2
#     6  0  2  2
#
#     7  3  0  3
#     8  2  1  3
#     9  1  2  3
#    10  0  3  3
#
#    11  4  0  4
#    12  3  1  4
#    13  2  2  4
#    14  1  3  4
#    15  0  4  4
#
#    16  5  0  5
#    17  4  1  5
#    18  3  2  5
#    19  2  3  5
#    20  1  4  5
#    21  0  5  5
#
#    22  6  0  6
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the linear index of the (I,J) element.
#    1 <= K.
#
#  Output:
#
#    integer D, the degree (sum) of the corresponding Pascal indices.
#
  import numpy as np

  if ( k <= 0 ):
    print ( '' )
    print ( 'i4_to_pascal_degree(): Fatal error!' )
    print ( '  K must be positive.' )
    raise Exception ( 'i4_to_pascal_degree(): Fatal error!' )

  d = int ( 0.5 * ( - 1.0 + np.sqrt ( 1.0 + 8.0 * ( k - 1 ) ) ) )

  return d

def i4_to_pascal_degree_test ( ):

#*****************************************************************************80
#
## i4_to_pascal_degree_test() tests i4_to_pascal_degree().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_pascal_degree_test():' )
  print ( '  i4_to_pascal_degree() converts a linear index to' )
  print ( '  the degree of the corresponding Pascal triangle indices.' )
  print ( '' )
  print ( '     K  =>   D' )
  print ( '' )

  for k in range ( 1, 21 ):

    d = i4_to_pascal_degree ( k )

    print ( '  %4d    %4d' % ( k, d ) )

  return

def i4_to_pascal ( k ):

#*****************************************************************************80
#
## i4_to_pascal() converts a linear index to Pascal triangle coordinates.
#
#  Discussion:
#
#    We describe the grid points in Pascal's triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#  Example:
#
#     K  I  J
#
#     1  0  0
#     2  1  0
#     3  0  1
#     4  2  0
#     5  1  1
#     6  0  2
#     7  3  0
#     8  2  1
#     9  1  2
#    10  0  3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the linear index of the (I,J) element.
#    1 <= K.
#
#  Output:
#
#    integer I, J, the Pascal indices.
#
  if ( k <= 0 ):
    print ( '' )
    print ( 'i4_to_pascal(): Fatal error!' )
    print ( '  K must be positive.' )
    raise Exception ( 'i4_to_pascal(): Fatal error!' )

  d = i4_to_pascal_degree ( k )

  j = k - ( d * ( d + 1 ) ) // 2 - 1
  i = d - j

  return i, j

def i4_to_pascal_test ( ):

#*****************************************************************************80
#
## i4_to_pascal_test() tests i4_to_pascal().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_pascal_test():' )
  print ( '  i4_to_pascal() converts a linear index to' )
  print ( '  Pascal triangle indices.' )
  print ( '' )
  print ( '     K  =>   I     J' )
  print ( '' )

  for k in range ( 1, 21 ):

    i, j = i4_to_pascal ( k )

    print ( '  %4d    %4d  %4d' % ( k, i, j ) )

  return

def i4_to_triangle_lower ( k ):

#*****************************************************************************80
#
## i4_to_triangle_lower() converts an integer to lower triangular coordinates.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the lower half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1)
#    (2,1) (2,2)
#    (3,1) (3,2) (3,3)
#    (4,1) (4,2) (4,3) (4,4)
#
#    as the linear array
#
#    (1,1) (2,1) (2,2) (3,1) (3,2) (3,3) (4,1) (4,2) (4,3) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    In this routine, we are given the location K of an item in the
#    linear array, and wish to determine the row I and column J
#    of the item when stored in the triangular array.
#
#  First Values:
#
#     K  I  J
#
#     0  0  0
#     1  1  1
#     2  2  1
#     3  2  2
#     4  3  1
#     5  3  2
#     6  3  3
#     7  4  1
#     8  4  2
#     9  4  3
#    10  4  4
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
#  Input:
#
#    integer K, the linear index of the (I,J) element, which
#    must be nonnegative.
#
#  Output:
#
#    integer I, J, the row and column indices.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'i4_to_triangle_lower(): Fatal error!' )
    print ( '  K < 0.' )
    print ( '  K = %d' % ( k ) )
    raise Exception ( 'i4_to_triangle_lower(): Fatal error!' )

  if ( k == 0 ):
    i = 0
    j = 0
  else:
    i = int ( np.sqrt ( float ( 2 * k ) ) )

    if ( i * i + i < 2 * k ):
      i = i + 1

    j = k - ( i * ( i - 1 ) ) // 2

  return i, j

def i4_to_triangle_lower_test ( ):

#*****************************************************************************80
#
## i4_to_triangle_lower_test() tests i4_to_triangle_lower().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_triangle_lower_test():' )
  print ( '  i4_to_triangle_lower() converts a linear index to a lower' )
  print ( '  triangular one.' )
  print ( '' )
  print ( '     K  ==>  ( I  J )' )
  print ( '' )

  for k in range ( 1, 21 ):
 
    i, j = i4_to_triangle_lower ( k )

    print ( '  %4d    %4d  %4d' % ( k, i, j )   )    

  return

def i4_to_triangle_upper ( k ):

#*****************************************************************************80
#
## i4_to_triangle_upper() converts an integer to upper triangular coordinates.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the upper half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1) (1,2) (1,3) (1,4)
#          (2,2) (2,3) (2,4)
#                (3,3) (3,4)
#                      (4,4)
#
#    as the linear array
#
#    (1,1) (1,2) (2,2) (1,3) (2,3) (3,3) (1,4) (2,4) (3,4) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    In this routine, we are given the location K of an item in the
#    linear array, and wish to determine the row I and column J
#    of the item when stored in the triangular array.
#
#  First Values:
#
#     K  I  J
#
#     0  0  0
#     1  1  1
#     2  1  2
#     3  2  2
#     4  1  3
#     5  2  3
#     6  3  3
#     7  1  4
#     8  2  4
#     9  3  4
#    10  4  4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the linear index of the (I,J) element, which
#    must be nonnegative.
#
#  Output:
#
#    integer I, J, the row and column indices.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'i4_to_triangle_upper(): Fatal error!' )
    print ( '  K < 0.' )
    print ( '  K = %d' % ( k ) )
    raise Exception ( 'i4_to_triangle_upper(): Fatal error!' )

  if ( k == 0 ):
    i = 0
    j = 0
  else:
    j = int ( np.sqrt ( float ( 2 * k ) ) )

    if ( j * j + j < 2 * k ):
      j = j + 1

    i = k - ( j * ( j - 1 ) ) // 2

  return i, j

def i4_to_triangle_upper_test ( ):

#*****************************************************************************80
#
## i4_to_triangle_upper_test() tests i4_to_triangle_upper().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 March 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_triangle_upper_test():' )
  print ( '  i4_to_triangle_upper() converts a linear index to an upper triangular one.' )
  print ( '' )
  print ( '     K  ==>  ( I  J )' )
  print ( '' )

  for k in range ( 1, 21 ):
 
    i, j = i4_to_triangle_upper ( k )

    print ( '  %4d    %4d  %4d' % ( k, i, j )   )    

  return

def i4_uniform_ab ( a, b, seed ):

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
#    integer A, B, the minimum and maximum acceptable values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    integer C, the randomly chosen integer.
#
#    integer SEED, the updated seed.
#
  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4_uniform_ab(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4_uniform_ab(): Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

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
  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'i4_uniform_ab_test():' )
  print ( '  i4_uniform_ab() computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )

  return

def i4_unswap3 ( i, j, k ) :

#*****************************************************************************80
#
## i4_unswap3() unswaps three integer values.
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
#  Input:
#
#    integer I, J, K, the values to be unswapped.
#
#  Output:
#
#    integer I, J, K, the unswapped values.
#
  return k, i, j

def i4_unswap3_test ( ):

#*****************************************************************************80
#
## i4_unswap3_test() tests i4_unswap3().
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
  print ( '' )
  print ( 'i4_unswap3_test():' )
  print ( '  i4_unswap3() swaps three I4\'s.' )
  print ( '  It can also reverse the effect of i4_swap3.' )
  print ( '' )
  print ( '  Starting with (I,J,K), unswap 3 times.' )
  print ( '' )

  i = 1
  j = 202
  k = 3003003

  print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  for l in range ( 0, 3 ):
    i, j, k = i4_unswap3 ( i, j, k )
    print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  print ( '' )
  print ( '  Start with (I,J,K), swap, then unswap.' )
  print ( '' )

  i = 1
  j = 202
  k = 3003003

  print ( '  %8d  %8d  %8d' % ( i, j, k ) )
  i, j, k = i4_swap3 ( i, j, k )
  print ( '  %8d  %8d  %8d' % ( i, j, k ) )
  i, j, k = i4_unswap3 ( i, j, k )
  print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  return

def i4_walsh_1d ( x, digit ) :

#*****************************************************************************80
#
## i4_walsh_1d() evaluates the Walsh function.
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
#    09 May 2013
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
#    integer VALUE, the value of the Walsh function.
# 
  import numpy as np
#
#  Hide the effect of the sign of X.
#
  x = np.abs ( x )
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
  n = int ( np.floor ( x ) )
#
#  Is the units digit odd or even?
#
  if ( ( n % 2 ) == 0 ):
    value = 0
  else:
    value = 1

  return value

def i4_walsh_1d_test ( ):

#*****************************************************************************80
#
## i4_walsh_1d_test() tests i4_walsh_1d().
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
  print ( '' )
  print ( 'i4_walsh_1d_test():' )
  print ( '  i4_walsh_1d() evaluates 1D Walsh functions.' )
  print ( '' )
  print ( '      X       +2  +1   0  -1  -2  -3' )
  print ( '' )

  for i in range ( 0, 33 ):

    x = i / 4.0

    wp2 = i4_walsh_1d ( x,  2 )
    wp1 = i4_walsh_1d ( x,  1 )
    w0  = i4_walsh_1d ( x,  0 )
    wm1 = i4_walsh_1d ( x, -1 )
    wm2 = i4_walsh_1d ( x, -2 )
    wm3 = i4_walsh_1d ( x, -3 )

    print ( '  %10.6f  %2d  %2d  %2d  %2d  %2d  %2d' % ( x, wp2, wp1, w0, wm1, wm2, wm3 ) )

  return

def i4_width ( i ):

#*****************************************************************************80
#
## i4_width() returns the "width" of an I4.
#
#  Example:
#
#        I  VALUE
#    -----  -------
#    -1234    5
#     -123    4
#      -12    3
#       -1    2
#        0    1
#        1    1
#       12    2
#      123    3
#     1234    4
#    12345    5
#
#  Discussion:
#
#    The width of an integer is the number of characters necessary to print it.
#
#    The width of an integer can be useful when setting the appropriate output
#    format for a vector or array of values.
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
#  Input:
#
#    integer I, the number whose width is desired.
#
#  Output:
#
#    integer VALUE, the number of characters necessary to represent
#    the integer in base 10, including a negative sign if necessary.
#
  if ( 0 <= i ):
    value = i4_log_10 ( i ) + 1
  else:
    value = i4_log_10 ( i ) + 2
 
  return value

def i4_width_test ( ):

#*****************************************************************************80
#
## i4_width_test() tests i4_width().
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

  test_num = 13
  x_test = np.array ( [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ] )

  print ( '' )
  print ( 'i4_width_test():' )
  print ( '  i4_width() determines the printing "width" of an I4.' )
  print ( ' ' )
  print ( '            I4      i4_width' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test];
    print ( '  %12d  %12d' % ( x, i4_width ( x ) ) )

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

def i4_xor ( i, j ):

#*****************************************************************************80
#
## i4_xor() calculates the exclusive OR of two I4's.
#
#  Discussion:
#
#    An I4 is an integer value.
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
#    integer I, J, two values whose exclusive OR is needed.
#
#  Output:
#
#    integer VALUE, the exclusive OR of I and J.
#
  i1 = i
  j1 = j
  value = 0
  l = 1

  while ( i1 != 0 or j1 != 0 ):

    i2 = i1 // 2
    j2 = j1 // 2

    if ( \
      ( ( i1 == 2 * i2 ) and ( j1 != 2 * j2 ) ) or \
      ( ( i1 != 2 * i2 ) and ( j1 == 2 * j2 ) ) ):
      value = value + l

    i1 = i2
    j1 = j2
    l = 2 * l

  return value

def i4_xor_test ( rng ):

#*****************************************************************************80
#
## i4_xor_test() tests i4_xor().
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
#    rng(): the current random number generator.
#
  import numpy as np

  i4_lo = 0
  i4_hi = 100
  test_num = 10

  print ( '' )
  print ( 'i4_xor_test():' )
  print ( '  i4_xor() returns the bitwise exclusive OR of two I4s.' )
  print ( '' )
  print ( '         I         J    i4_xor       I^J' )
  print ( '' )

  for test in range ( 0, test_num ):

    i = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    j = rng.integers ( low = i4_lo, high = i4_hi, endpoint = True )
    k = i4_xor ( i, j )
    l = ( i ^ j )
    print ( '  %8d  %8d  %8d  %8d' % ( i, j, k, l ) )

  return

def i4vec_add ( n, a, b ):

#*****************************************************************************80
#
## i4vec_add() computes C = A + B for I4VEC's.
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
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#    integer A(N), the first vector.
#
#    integer B(N), the second vector.
#
#  Output:
#
#    integer C(N), the sum of the vectors.
#
  import numpy as np

  c = np.zeros ( n, dtype = np.int32 );

  for i in range ( 0, n ):
    c[i] = a[i] + b[i]

  return c

def i4vec_add_test ( rng ):

#*****************************************************************************80
#
## i4vec_add_test() tests i4vec_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2014
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
  print ( 'i4vec_add_test():' )
  print ( '  i4vec_add() adds two I4VECs.' )

  n = 10

  lo = - n
  hi = n

  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  b = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  c = i4vec_add ( n, a, b )

  print ( '' )
  print ( '     I     A     B     C' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d%6d%6d%6d' % ( i, a[i], b[i], c[i] ) )

  return

def i4vec_amax ( n, a ):

#*****************************************************************************80
#
## i4vec_amax() returns the largest magnitude in an I4VEC.
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
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the largest of the magnitudes of the entries.
#
  i4_huge = 2147483647
  value = - i4_huge

  for i in range ( 0, n ):
    value = max ( value, abs ( a[i] ) )

  return value

def i4vec_amax_test ( rng ):

#*****************************************************************************80
#
## i4vec_amax_test() tests i4vec_amax().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2014
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
  print ( 'i4vec_amax_test():' )
  print ( '  i4vec_amax() computes the largest of the magnitudes of the' )
  print ( '  entries of an I4VEC.' )

  n = 10
  lo = - 10
  hi = 5

  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, a, '  Vector A:' )
  a_amax = i4vec_amax ( n, a )
  print ( '' )
  print ( '  Largest magnitude of entries of A = %d' % ( a_amax ) )

  return

def i4vec_amin ( n, a ):

#*****************************************************************************80
#
## i4vec_amin() returns the smallest magnitude in an I4VEC.
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
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the smallest of the magnitudes of the entries.
#
  value = 2147483647

  for i in range ( 0, n ):
    value = min ( value, abs ( a[i] ) )

  return value

def i4vec_amin_test ( rng ):

#*****************************************************************************80
#
## i4vec_amin_test() tests i4vec_amin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2014
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
  print ( 'i4vec_amin_test():' )
  print ( '  i4vec_amin() computes the smallest of the magnitudes of the' )
  print ( '  entries of an I4VEC.' )

  n = 10
  lo = - 10
  hi = 5

  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, a, '  Vector A:' )
  a_amin = i4vec_amin ( n, a )
  print ( '' )
  print ( '  Smallest magnitude of entries of A = %d' % ( a_amin ) )

  return

def i4vec_binary_next ( n, bvec ):

#*****************************************************************************80
#
## i4vec_binary_next() generates the next binary vector.
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
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer BVEC(N), the vector whose successor is desired.
#
#  Output:
#
#    integer BVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( bvec[i] == 0 ):
      bvec[i] = 1
      break

    bvec[i] = 0

  return bvec

def i4vec_binary_next_test ( ):

#*****************************************************************************80
#
## i4vec_binary_next_test() tests i4vec_binary_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'i4vec_binary_next_test():' )
  print ( '  i4vec_binary_next() generates the next binary vector.' )
  print ( '' )
 
  bvec = np.zeros ( n )

  while ( True ):

    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%d' % ( bvec[i] ), end = '' )
    print ( '' )

    if ( all ( bvec[0:n] == 1 ) ):
      break

    bvec = i4vec_binary_next ( n, bvec )

  return

def i4vec_choose ( m, n, k ):

#*****************************************************************************80
#
## i4vec_choose() computes the generalized binomial coefficient C(M,N,K).
#
#  Discussion:
#
#    C(M,N,K) = product ( 1 <= I <= M ) C(N,K)
#
#    where:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N(M), K(M), the parameters for each dimension.
#
#  Output:
#
#    integer i4vec_choose, the generalized binomial coefficient.
#
  value = 1
  for i in range ( 0, m ):
    value = value * i4_choose ( n[i], k[i] )

  return value

def i4vec_choose_test ( rng ):

#*****************************************************************************80
#
## i4vec_choose_test() tests i4vec_choose().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2015
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
  print ( 'i4vec_choose_test():' )
  print ( '  i4vec_choose() computes the generalized binomial coefficient.' )

  m = 5
 
  j = rng.integers ( low = 0, high = 6, size = m, endpoint = True )
  k = rng.integers ( low = 0, high = 6, size = m, endpoint = True )
  n = i4vec_sum_vec ( m, j, k )

  i4vec_transpose_print ( m, n, '  N:' )
  i4vec_transpose_print ( m, k, '  K:' )

  print ( '' )
  print ( '   M        V1        V2' )
  print ( '' )
  v1 = 1
  for mm in range ( 0, m + 1 ):
 
    if ( mm == 0 ):
      v1 = 1
    else:
      v1 = v1 * i4_choose ( n[mm-1], k[mm-1] )
    v2 = i4vec_choose ( mm, n, k )
    print ( '  %2d  %8d  %8d' % ( mm, v1, v2 ) )

  return

def i4vec_concatenate ( n1, a1, n2, a2 ):

#*****************************************************************************80
#
## i4vec_concatenate() concatenates two I4VEC's.
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
#    integer A1(N1), the first vector.
#
#    integer N2, the number of entries in the second vector.
#
#    integer A2(N2), the second vector.
#
#  Output:
#
#    integer A3(N1+N2), the concatenation of A1 and A2.
#
  import numpy as np

  a3 = np.concatenate ( ( a1, a2 ), axis = 0 )

  return a3

def i4vec_concatenate_test ( ):

#*****************************************************************************80
#
## i4vec_concatenate_test() tests i4vec_concatenate().
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

  a1 = np.array ( [ 91, 31, 71, 51, 31 ] )
  a2 = np.array ( [ 42, 22, 12 ] )

  print ( '' )
  print ( 'i4vec_concatenate_test():' )
  print ( '  i4vec_concatenate() concatenates two I4VECs' )

  i4vec_print ( n1, a1, '  Array 1:' )
  i4vec_print ( n2, a2, '  Array 2:' )
  a3 = i4vec_concatenate ( n1, a1, n2, a2 )
  i4vec_print ( n3, a3, '  Array 3 = Array 1 + Array 2:' )

  return

def i4vec_copy ( n1, a1 ):

#*****************************************************************************80
#
## i4vec_copy() copies an I4VEC.
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
#    integer A1(N1), the vector.
#
#  Output:
#
#    integer A2(N1), a copy of A2.
#
  import numpy as np

  a2 = np.zeros ( n1, dtype = np.int32 )
  for i in range ( 0, n1 ):
    a2[i] = a1[i]

  return a2

def i4vec_copy_test ( ):

#*****************************************************************************80
#
## i4vec_copy_test() tests i4vec_copy().
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

  a1 = np.array ( [ 91, 31, 71, 51, 31 ], dtype = np.int32 )
 
  print ( '' )
  print ( 'i4vec_copy_test():' )
  print ( '  i4vec_copy() copies an I4VEC.' )

  i4vec_print ( n1, a1, '  Array 1:' );
  a2 = i4vec_copy ( n1, a1 );
  i4vec_print ( n1, a2, '  Array 2:' );

  return

def i4vec_cum0 ( n, a ):

#*****************************************************************************80
#
## i4vec_cum0() computes the zero-based cumulative sum of the entries of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Example:
#
#    Input:
#
#      A = (/ 1, 2, 3, 4 /)
#
#    Output:
#
#      A_cum0 = (/ 0, 1, 3, 6, 10 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector to be summed.
#
#  Output:
#
#    integer A_cum(0:N), the cumulative sum of the entries of A.
#
  import numpy as np

  a_cum = np.zeros ( n + 1, dtype = np.int32 )

  a_cum[0] = 0.0

  for i in range ( 0, n ):
    a_cum[i+1] = a_cum[i] + a[i]

  return a_cum

def i4vec_cum0_test ( rng ):

#*****************************************************************************80
#
## i4vec_cum0_test() tests i4vec_cum0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2014
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
  print ( 'i4vec_cum0_test():' )
  print ( '  i4vec_cum0():  zero-based cumulative sum of I4VEC entries;' )

  b = 0
  c = n

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  a_cum = i4vec_cum0 ( n, a )

  i4vec_print ( n + 1, a_cum, '  Cumulative sums:' )

  return

def i4vec_cum ( n, a ):

#*****************************************************************************80
#
## i4vec_cum() computes the cumulative sum of the entries of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Example:
#
#    Input:
#
#      A = (/ 1, 2, 3, 4 /)
#
#    Output:
#
#      A_cum = (/ 1, 3, 6, 10 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector to be summed.
#
#  Output:
#
#    integer A_cum(0:N-1), the cumulative sum of the entries of A.
#
  import numpy as np

  a_cum = np.zeros ( n, dtype = np.int32 )

  a_cum[0] = a[0]

  for i in range ( 1, n ):
    a_cum[i] = a_cum[i-1] + a[i]

  return a_cum

def i4vec_cum_test ( rng ):

#*****************************************************************************80
#
## i4vec_cum_test() tests i4vec_cum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2014
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
  print ( 'i4vec_cum_test():' )
  print ( '  i4vec_cum():  cumulative sum of I4VEC entries;' )
 
  b = 0
  c = n

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  a_cum = i4vec_cum ( n, a )

  i4vec_print ( n, a_cum, '  Cumulative sums:' )

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

def i4vec_distances ( k, locate ):

#*****************************************************************************80
#
## i4vec_distances() computes a pairwise distance table.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the number of objects.
#
#    integer LOCATE(K), the obect locations.
#
#  Output:
#
#    integer D(K*(K-1)/2), the pairwise distances.
#
  import numpy as np

  d = np.zeros ( k * ( k - 1 ) / 2 )

  l = 0
  for i in range ( 0, k ):
    for j in range ( i + 1, k ):
      d[l] = abs ( locate[i] - locate[j] )
      l = l + 1

  return d

def i4vec_distances_test ( ):

#*****************************************************************************80
#
## i4vec_distances_test() tests i4vec_distances().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_distances_test():' )
  print ( '  i4vec_distances() computes the pairwise distances between' )
  print ( '  elements of an I4VEC.' )

  n = 5
  locate = np.array ( [ 0, 3, 10, 20, 100 ] )
  d = i4vec_distances ( n, locate )

  i4vec_print ( n, locate, '  Locations:' )
  i4vec_print ( n * ( n - 1 ) / 2, d, '  Distances:' )

  return

def i4vec_dot_product ( n, x, y ):

#*****************************************************************************80
#
## i4vec_dot_product() computes the dot product of two I4VEC's.
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
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the array.
#
#    integer X(N), Y(N), the arrays.
#
#  Output:
#
#    integer i4vec_dot_product, the dot product of X and Y.
#
  value = 0
  for i in range ( 0, n ):
    value = value + x[i] * y[i]

  return value

def i4vec_dot_product_test ( rng ):

#*****************************************************************************80
#
## i4vec_dot_product_test() tests i4vec_dot_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2015
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
  print ( 'i4vec_dot_product_test():' )
  print ( '  i4vec_dot_product() computes the dot product of two I4VECs.' )

  n = 5
  lo = 0
  hi = 10

  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, a, '  The vector A:' )

  b = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, b, '  The vector B:' )

  d = i4vec_dot_product ( n, a, b )
  print ( '' )
  print ( '  The dot product is %d' % ( d ) )

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
  print ( '  i4vec_frac() returns the K-th smallest integer vector entry.' )

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

def i4vec_gcd ( v ):

#*****************************************************************************80
#
## i4vec_gcd() returns the greatest common divisor of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The value GCD returned has the property that it is the greatest integer
#    which evenly divides every entry of V.
#
#    The entries in V may be negative.
#
#    Any zero entries in V are ignored.  If all entries of V are zero,
#    GCD is returned as 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer V(:), the vector.
#
#  Output:
#
#    integer VALUE, the greatest common divisor of V.
#
  import numpy as np

  n = len ( v )

  value = abs ( v[0] )

  for i in range ( 1, n ):
    value = np.gcd ( value, v[i] )

  return value

def i4vec_gcd_test ( ):

#*****************************************************************************80
#
## i4vec_gcd_test() tests i4vec_gcd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4;
  i4vec = np.array ( [ \
    2**3*3   *5   *7*11   *13, \
    2   *3**2*5   *7*11   *13, \
    2   *3   *5**3*7*11   *13, \
    2   *3   *5   *7*11**2*13 ] )

  print ( '' );
  print ( 'i4vec_gcd_test():' )
  print ( '  i4vec_gcd() computes the greatest common divisor of the' )
  print ( '  entries in an I4VEC.' )

  i4vec_print ( n, i4vec, '  The I4VEC:' )

  value = i4vec_gcd ( i4vec )

  print ( '' )
  print ( '  GCD = ', value )

  return

def i4vec_heap_d ( n, a ):

#*****************************************************************************80
#
## i4vec_heap_d() reorders an I4VEC into an descending heap.
#
#  Definition:
#
#    A descending heap is an array A with the property that, for every index J,
#    A(J) >= A(2*J) and A(J) >= A(2*J+1), (as long as the indices
#    2*J and 2*J+1 are legal).
#
#  Diagram:
#
#                  A(1)
#                /      \
#            A(2)         A(3)
#          /     \        /  \
#      A(4)       A(5)  A(6) A(7)
#      /  \       /   \
#    A(8) A(9) A(10) A(11)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 September 2015
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
#    integer N, the size of the input array.
#
#    integer A(N), an unsorted array.
#
#  Output:
#
#    integer A_OUT(N), the array has been reordered into a heap.
#
  import numpy as np

  a_out = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    a_out[i] = a[i]
#
#  Only nodes N/2-1 down to 0 can be "parent" nodes.
#
  i_hi = ( n // 2 )

  for i in range ( i_hi - 1, -1, -1 ):
#
#  Copy the value out of the parent node.
#  Position IFREE is now "open".
#
    key = a_out[i]
    ifree = i

    while ( True ):
#
#  Positions 2*IFREE and 2*IFREE + 1 are the descendants of position
#  IFREE.  (One or both may not exist because they exceed N.)
#
      m = 2 * ifree + 1
#
#  Does the first position exist?
#
      if ( n - 1 < m ):
        break
#
#  Does the second position exist?
#
      if ( m + 1 < n ):
#
#  If both positions exist, take the larger of the two values,
#  and update M if necessary.
#
        if ( a_out[m] < a_out[m+1] ):
          m = m + 1
#
#  If the large descendant is larger than KEY, move it up,
#  and update IFREE, the location of the free position, and
#  consider the descendants of THIS position.
#
      if ( a_out[m] <= key ):
        break

      a_out[ifree] = a_out[m]
      ifree = m
#
#  Once there is no more shifting to do, KEY moves into the free spot IFREE.
#
    a_out[ifree] = key

  return a_out

def i4vec_heap_d_test ( rng ):

#*****************************************************************************80
#
## i4vec_heap_d_test() tests i4vec_heap_d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2015
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
  c = n

  print ( '' )
  print ( 'i4vec_heap_d_test():' )
  print ( '  i4vec_heap_d() puts an I4VEC into descending heap form.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array:' )
 
  a = i4vec_heap_d ( n, a )
 
  i4vec_print ( n, a, '  Descending heap form:' )

  return

def i4vec_identity_row ( n, i ):

#*****************************************************************************80
#
## i4vec_identity_row() returns a row of the identity matrix as an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2018
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
#    0 <= I < N.
#
#  Output:
#
#    integer A(N), the vector.
#
  import numpy as np

  a = np.zeros ( n )

  if ( 0 <= i and i < n ):
    a[i] = 1

  return a

def i4vec_identity_row_test ( ):

#*****************************************************************************80
#
## i4vec_identity_row_test() tests i4vec_identity_row().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4vec_identity_row_test():' )
  print ( '  i4vec_identity_row() returns a row of the identity matrix.' )
  print ( '' )

  n = 5
  for i in range ( -1, 6 ):
    a = i4vec_identity_row ( n, i )
    print ( '%2d: ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( ' %d' % ( a[j] ), end = '' )
    print ( '' )

  return

def i4vec_increment ( n, v ):

#*****************************************************************************80
#
## i4vec_increment() increments an I4VEC.
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
#    integer V[N], the vector to be incremented.
#
#  Output:
#
#    integer V[N], the incremented vector.
#
  v[0:n] = v[0:n] + 1

  return v

def i4vec_increment_test ( rng ):

#*****************************************************************************80
#
## i4vec_increment_test() tests i4vec_increment().
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
  print ( 'i4vec_increment_test():' )
  print ( '  i4vec_increment() increments an I4VEC.' )

  v_lo = -5
  v_hi = 10
  v = rng.integers ( low = v_lo, high = v_hi, size = n, endpoint = True )
  i4vec_print ( n, v, '  The I4VEC:' )
  v = i4vec_increment ( n, v )
  i4vec_print ( n, v, '  The I4VEC after incrementing:' )

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
## i4vec_index_test() tests i4vec_index().
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

  i4_lo = -n
  i4_hi = n

  a = rng.integers ( low = i4_lo, high = i4_hi, size = n, endpoint = True )

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

def i4vec_is_ascending ( n, x ):

#*****************************************************************************80
#
## i4vec_is_ascending() is TRUE if an I4VEC is increasing.
#
#  Example:
#
#    X = ( 9, 7, 7, 3, 2, 1, -8 )
#
#    i4vec_is_ascending = FALSE
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
#    logical VALUE, is TRUE if the entries of X ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i] > x[i+1] ):
      value = False
      break

  return value

def i4vec_is_ascending_test ( ):

#*****************************************************************************80
#
## i4vec_is_ascending_test() tests i4vec_is_ascending().
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
  print ( 'i4vec_is_ascending_test():' )
  print ( '  i4vec_is_ascending() determines if an I4VEC ascends.' )

  for i in range ( 0, test_num ):

    x = np.zeros ( n )
    for j in range ( 0, n ):
      x[j] = x_test[i,j]

    i4vec_transpose_print ( n, x, '  Test vector:' )

    value = i4vec_is_ascending ( n, x )

    print ( '  i4vec_is_ascending = %s' % ( value ) )

  return

def i4vec_is_binary ( x ):

#*****************************************************************************80
#
## i4vec_is_binary() is true if an I4VEC only contains 0 and 1 entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X(N): the vector to be checked.
#
#  Output:
#
#    logical i4vec_is_binary: True if X only contains 0 or 1 entries.
#
  import numpy as np

  value = np.all ( ( x == 1 ) | ( x == 0 ) )

  return value

def i4vec_is_binary_test ( ):

#*****************************************************************************80
#
## i4vec_is_binary_test() tests i4vec_is_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_binary_test():' )
  print ( '  i4vec_is_binary() is TRUE if an I4VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1, 0, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0, 2, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  return

def i4vec_is_coprime ( n, a ):

#*****************************************************************************80
#
## i4vec_is_coprime(): every pair of entries is coprime.
#
#  Discussion:
#
#    Two positive integers I and J are coprime if they have no common
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
#    logical VALUE, is TRUE if all pairs of entries are coprime.
#
  value = True

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      if ( i4_gcd ( a[i], a[j] ) != 1 ):
        value = False
        break

  return value

def i4vec_is_coprime_test ( ):

#*****************************************************************************80
#
## i4vec_is_coprime_test() tests i4vec_is_coprime().
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
  print ( 'i4vec_is_coprime_test():' )
  print ( '  i4vec_is_coprime() determines if a vector of' )
  print ( '  integers is pairwise prime.' )
  print ( '' )
  print ( '  Row Vector              Coprime?' )
  print ( ''
 )
  for test in range ( 0, test_num ):

    for j in range ( 0, n ):
      x[j] = x_test[test,j]

    value = i4vec_is_coprime ( n, x )

    for j in range ( 0, n ):
      print ( '  %3d' % ( x[j] ), end = '' )
    print ( '  %s' % ( value ) )

  return

def i4vec_is_descending ( n, x ):

#*****************************************************************************80
#
## i4vec_is_descending() is TRUE if an I4VEC is decreasing.
#
#  Example:
#
#    X = ( 9, 7, 7, 3, 2, 1, -8 )
#
#    i4vec_is_descending = TRUE
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
#    logical VALUE, is TRUE if the entries of X descend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i] < x[i+1] ):
      value = False
      break

  return value

def i4vec_is_descending_test ( ):

#*****************************************************************************80
#
## i4vec_is_descending_test() tests i4vec_is_descending().
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
  print ( 'i4vec_is_descending_test():' )
  print ( '  i4vec_is_descending() determines if an I4VEC descends.' )

  for i in range ( 0, test_num ):

    x = np.zeros ( n )
    for j in range ( 0, n ):
      x[j] = x_test[i,j]

    i4vec_transpose_print ( n, x, '  Test vector:' )

    value = i4vec_is_descending ( n, x )

    print ( '  i4vec_is_descending = %s' % ( value ) )

  return

def i4vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## i4vec_is_distinct() is true if the entries in an I4VEC are distinct.
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
#    integer A(N), the vector to be checked.
#
#  Output:
#
#    logical VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

def i4vec_is_distinct_test ( ):

#*****************************************************************************80
#
## i4vec_is_distinct_test() tests i4vec_is_distinct().
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
  print ( 'i4vec_is_distinct_test():' )
  print ( '  i4vec_is_distinct() computes the maximum entry in an I4VEC.' )

  n = 5
  a = np.array ( [ 1, 2, 5, 3, 4 ] )
  i4vec_print ( n, a, '  Input vector:' )
  if ( i4vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  n = 5
  a = np.array ( [ 1, 2, 5, 2, 4 ] )
  i4vec_print ( n, a, '  Input vector:' )
  if ( i4vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  return

def i4vec_is_equal ( n, a, b ):

#*****************************************************************************80
#
## i4vec_is_equal() is TRUE if two I4VEC's are equal.
#
#  Example:
#
#    A = ( 9, 7, 7, 3, 2, 1, -8 )
#    B = ( 9, 7, 6, 3, 2, 1, -8 )
#    i4vec_is_equal = FALSE
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
#    integer N, the size of the arrays.
#
#    integer A(N), B(N), the arrays to be compared.
#
#  Output:
#
#    logical VALUE, is TRUE if the arrays are equal.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( a[i] != b[i] ):
      value = False
      break

  return value

def i4vec_is_equal_test ( ):

#*****************************************************************************80
#
## i4vec_is_equal_test() tests i4vec_is_equal().
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
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 2, 2 ], \
    [ 1, 2, 2, 4 ], \
    [ 1, 2, 3, 4 ] ] )

  b_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 1, 2 ], \
    [ 4, 1, 1, 3 ], \
    [ 1, 2, 3, 4 ] ] )

  print ( '' )
  print ( 'i4vec_is_equal_test():' )
  print ( '  i4vec_is_equal() is TRUE if two I4VECs are equal.' )

  for i in range ( 0, test_num ):

    a = a_test[i,0:n].copy ( )
    b = b_test[i,0:n].copy ( )

    i4vec2_print ( a, b, '  Vectors A and B:' )

    value = i4vec_is_equal ( n, a, b )

    print ( '  i4vec_is_equal(A,B) = %s' % ( value ) )

  return

def i4vec_is_even_all ( n, x ):

#*****************************************************************************80
#
## i4vec_is_even_all() is true if all entries of an I4VEC are even.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if all entries of X are even.
#
  value = all ( x[0:n] % 2 == 0 )

  return value

def i4vec_is_even_all_test ( ):

#*****************************************************************************80
#
## i4vec_is_even_all_test() tests i4vec_is_even_all().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_even_all_test():' )
  print ( '  i4vec_is_even_all() is TRUE if an I4VEC only contains' )
  print ( '  even entries.' )

  n = 3

  x = np.array ( [ 1, 5, 19 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_even_all ( n, x ) ):
    print ( '  X is only even values.' )
  else:
    print ( '  X is NOT only even values.' )

  x = np.array ( [ 3, 2, 77 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_even_all ( n, x ) ):
    print ( '  X is only even values.' )
  else:
    print ( '  X is NOT only even values.' )

  x = np.array ( [ 2, 4, 88 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_even_all ( n, x ) ):
    print ( '  X is only even values.' )
  else:
    print ( '  X is NOT only even values.' )

  return

def i4vec_is_even_any ( n, x ):

#*****************************************************************************80
#
## i4vec_is_even_any() is true if any entry of an I4VEC are even.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if any entry of X is even.
#
  value = any ( x[0:n] % 2 == 0 )

  return value

def i4vec_is_even_any_test ( ):

#*****************************************************************************80
#
## i4vec_is_even_any_test() tests i4vec_is_even_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_even_any_test():' )
  print ( '  i4vec_is_even_any() is TRUE if an I4VEC contains' )
  print ( '  any even entries.' )

  n = 3

  x = np.array ( [ 1, 5, 19 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_even_any ( n, x ) ):
    print ( '  X contains at least one even value.' )
  else:
    print ( '  X contains NO even values.' )

  x = np.array ( [ 3, 2, 77 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_even_any ( n, x ) ):
    print ( '  X contains at least one even value.' )
  else:
    print ( '  X contains NO even values.' )

  x = np.array ( [ 2, 4, 88 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_even_any ( n, x ) ):
    print ( '  X contains at least one even value.' )
  else:
    print ( '  X contains NO even values.' )

  return

def i4vec_is_lt_any ( n, a, b ):

#*****************************************************************************80
#
## i4vec_is_lt_any(): ( any ( A < B ) ) for I4VEC's.
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
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    integer A(N), the first vector.
#
#    integer B(N), the second vector.
#
#  Output:
#
#    logical i4vec_is_lt_any is 1 if any entry
#    of A is less than the corresponding entry of B.
#
  import numpy as np

  value = np.any ( a[0:n] < b[0:n] )

  return value

def i4vec_is_lt_any_test ( ):

#*****************************************************************************80
#
## i4vec_is_lt_any_test() tests i4vec_is_lt_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_binary_test():' )
  print ( '  i4vec_is_lt_any() is TRUE if any entry of one I4VEC' )
  print ( '  is less than the corresponding entry of another.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  y = np.array ( [ 1, 2, 3 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  i4vec_transpose_print ( n, y, '  Y:' )
  if ( i4vec_is_lt_any ( n, x, y ) ):
    print ( '  Some X is < some Y.' )
  else:
    print ( '  NO X is < any Y.' )

  x = np.array ( [ 3, 2, 1 ] )
  y = np.array ( [ 1, 2, 3 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  i4vec_transpose_print ( n, y, '  Y:' )
  if ( i4vec_is_lt_any ( n, x, y ) ):
    print ( '  Some X is < some Y.' )
  else:
    print ( '  NO X is < any Y.' )

  x = np.array ( [ 2, 3, 4 ] )
  y = np.array ( [ 1, 2, 3 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  i4vec_transpose_print ( n, y, '  Y:' )
  if ( i4vec_is_lt_any ( n, x, y ) ):
    print ( '  Some X is < some Y.' )
  else:
    print ( '  NO X is < any Y.' )

  return

def i4vec_is_negative_any ( n, x ):

#*****************************************************************************80
#
## i4vec_is_negative_any() is true if any entry of an I4VEC is negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if any entry of X is < 0.
#
  value = any ( x[0:n] < 0 )

  return value

def i4vec_is_negative_any_test ( ):

#*****************************************************************************80
#
## i4vec_is_negative_any_test() tests i4vec_is_negative_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_negative_any_test():' )
  print ( '  i4vec_is_negative_any() is TRUE if an I4VEC contains' )
  print ( '  at least one negative entry.' )

  n = 3

  x = np.array ( [ -1, -2, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_negative_any ( n, x ) ):
    print ( '  X has at least one negative entry.' )
  else:
    print ( '  X has no negative entries.' )

  x = np.array ( [ -1, 0, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_negative_any ( n, x ) ):
    print ( '  X has at least one negative entry.' )
  else:
    print ( '  X has no negative entries.' )

  x = np.array ( [ 1, 3, 99 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_negative_any ( n, x ) ):
    print ( '  X has at least one negative entry.' )
  else:
    print ( '  X has no negative entries.' )

  return

def i4vec_is_nonpositive_all ( n, x ):

#*****************************************************************************80
#
## i4vec_is_nonpositive_all() is true if all entries of an I4VEC are nonpositive.
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
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if all entries of X are <= 0.
#
  value = all ( x[0:n] <= 0 )

  return value

def i4vec_is_nonpositive_all_test ( ):

#*****************************************************************************80
#
## i4vec_is_nonpositive_all_test() tests i4vec_is_nonpositive_all().
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
  print ( 'i4vec_is_nonpositive_all_test():' )
  print ( '  i4vec_is_nonpositive_all() is TRUE if an I4VEC only contains' )
  print ( '  nonpositive entries.' )

  n = 3

  x = np.array ( [ -1, -2, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonpositive_all ( n, x ) ):
    print ( '  X is only nonpositives.' )
  else:
    print ( '  X is NOT only nonpositives.' )

  x = np.array ( [ -1, 0, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonpositive_all ( n, x ) ):
    print ( '  X is only nonpositives.' )
  else:
    print ( '  X is NOT only nonpositives.' )

  x = np.array ( [ -1, -3, -99 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonpositive_all ( n, x ) ):
    print ( '  X is only nonpositives.' )
  else:
    print ( '  X is NOT only nonpositives.' )

  return

def i4vec_is_nonzero_any ( n, x ):

#*****************************************************************************80
#
## i4vec_is_nonzero_any() is true if any entry of an I4VEC is nonzero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if any entry of X is not 0.
#
  value = any ( x[0:n] != 0 )

  return value

def i4vec_is_nonzero_any_test ( ):

#*****************************************************************************80
#
## i4vec_is_nonzero_any_test() tests i4vec_is_nonzero_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_nonzero_any_test():' )
  print ( '  i4vec_is_nonzero_any() is TRUE if an I4VEC contains' )
  print ( '  at least one nonzero entry.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonzero_any ( n, x ) ):
    print ( '  X has at least one nonzero entry.' )
  else:
    print ( '  X has no nonzero entries.' )

  x = np.array ( [ 0, -1, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonzero_any ( n, x ) ):
    print ( '  X has at least one nonzero entry.' )
  else:
    print ( '  X has no nonzero entries.' )

  x = np.array ( [ 1, 3, 99 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonzero_any ( n, x ) ):
    print ( '  X has at least one nonzero entry.' )
  else:
    print ( '  X has no nonzero entries.' )

  return

def i4vec_is_odd_all ( n, x ):

#*****************************************************************************80
#
## i4vec_is_odd_all() is true if all entries of an I4VEC are odd.
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
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if all entries of X are odd.
#
  value = all ( x[0:n] % 2 == 1 )

  return value

def i4vec_is_odd_all_test ( ):

#*****************************************************************************80
#
## i4vec_is_odd_all_test() tests i4vec_is_odd_all().
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
  print ( 'i4vec_is_odd_all_test():' )
  print ( '  i4vec_is_odd_all() is TRUE if an I4VEC only contains' )
  print ( '  odd entries.' )

  n = 3

  x = np.array ( [ 1, 5, 19 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_all ( n, x ) ):
    print ( '  X is only odd values.' )
  else:
    print ( '  X is NOT only odd values.' )

  x = np.array ( [ 3, 2, 77 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_all ( n, x ) ):
    print ( '  X is only odd values.' )
  else:
    print ( '  X is NOT only odd values.' )

  x = np.array ( [ 2, 4, 88 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_all ( n, x ) ):
    print ( '  X is only odd values.' )
  else:
    print ( '  X is NOT only odd values.' )

  return

def i4vec_is_odd_any ( n, x ):

#*****************************************************************************80
#
## i4vec_is_odd_any() is true if any entry of an I4VEC are odd.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if any entry of X is odd.
#
  value = any ( x[0:n] % 2 == 1 )

  return value

def i4vec_is_odd_any_test ( ):

#*****************************************************************************80
#
## i4vec_is_odd_any_test() tests i4vec_is_odd_any().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_is_odd_any_test():' )
  print ( '  i4vec_is_odd_all() is TRUE if an I4VEC contains' )
  print ( '  any odd entries.' )

  n = 3

  x = np.array ( [ 1, 5, 19 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_any ( n, x ) ):
    print ( '  X contains at least one odd value.' )
  else:
    print ( '  X contains NO odd values.' )

  x = np.array ( [ 3, 2, 77 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_any ( n, x ) ):
    print ( '  X contains at least one odd value.' )
  else:
    print ( '  X contains NO odd values.' )

  x = np.array ( [ 2, 4, 88 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_odd_any ( n, x ) ):
    print ( '  X contains at least one odd value.' )
  else:
    print ( '  X contains NO odd values.' )

  return

def i4vec_is_one ( n, x ):

#*****************************************************************************80
#
## i4vec_is_one() is true if all entries of an I4VEC are 1.
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
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if all entries of X are 1.
#
  value = all ( x[0:n] == 1 )

  return value

def i4vec_is_one_test ( ):

#*****************************************************************************80
#
## i4vec_is_one_test() tests i4vec_is_one().
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
  print ( 'i4vec_is_one_test():' )
  print ( '  i4vec_is_one() is TRUE if an I4VEC only contains' )
  print ( '  1 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_one ( n, x ) ):
    print ( '  X is only ones.' )
  else:
    print ( '  X is NOT only ones.' )

  x = np.array ( [ 0, 1, 2 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_one ( n, x ) ):
    print ( '  X is only ones.' )
  else:
    print ( '  X is NOT only ones.' )

  x = np.array ( [ 1, 1, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_one ( n, x ) ):
    print ( '  X is only ones.' )
  else:
    print ( '  X is NOT only ones.' )

  return

def i4vec_is_zero ( n, x ):

#*****************************************************************************80
#
## i4vec_is_zero() is true if all entries of an I4VEC are 0
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
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    logical VALUE, is true if all entries of X are 0.
#
  value = all ( x[0:n] == 0 )

  return value

def i4vec_is_zero_test ( ):

#*****************************************************************************80
#
## i4vec_is_zero_test() tests i4vec_is_zero().
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
  print ( 'i4vec_is_zero_test():' )
  print ( '  i4vec_is_zero() is TRUE if an I4VEC only contains' )
  print ( '  0 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_zero ( n, x ) ):
    print ( '  X is only zeros.' )
  else:
    print ( '  X is NOT only zeros.' )

  x = np.array ( [ 0, 1, 2 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_zero ( n, x ) ):
    print ( '  X is only zeros.' )
  else:
    print ( '  X is NOT only zeros.' )

  x = np.array ( [ 1, 1, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_zero ( n, x ) ):
    print ( '  X is only zeros.' )
  else:
    print ( '  X is NOT only zeros.' )

  return

def i4vec_lcm ( n, v ):

#*****************************************************************************80
#
## i4vec_lcm() returns the least common multiple of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The value LCM returned has the property that it is the smallest integer
#    which is evenly divisible by every element of V.
#
#    The entries in V may be negative.
#
#    If any entry of V is 0, then LCM is 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of V.
#
#    integer V(N), the vector.
#
#  Output:
#
#    integer VALUE, the least common multiple of V.
#
  value = 1

  for i in range ( 0, n ):

    if ( v[i] == 0 ):
      value = 0
      return value

    value = i4_lcm ( value, v[i] )

  return value

def i4vec_lcm_test ( ):

#*****************************************************************************80
#
## i4vec_lcm_test() tests i4vec_lcm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  i4vec = np.array ( [ \
    2**3 *3    *5    *7*11    *13, \
    2    *3**2 *5    *7*11    *13, \
    2    *3    *5**3 *7*11    *13, \
    2    *3    *5    *7*11**2 *13 ] )

  print ( '' )
  print ( 'i4vec_lcm_test()' )
  print ( '  i4vec_lcm() computes the least common multiple of the' )
  print ( '  entries in an I4VEC.' )

  print ( '' )
  print ( '  i4vec:' )
  print ( i4vec )

  value = i4vec_lcm ( n, i4vec )

  print ( '\n' )
  print ( '  i4vec_lcm = ', value )

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
  print ( '  i4vec_max_index_last():     last maximal index' )

  i4_lo = 0
  i4_hi = + ( n // 4 )

  a = rng.integers ( low = i4_lo, high = i4_hi, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  print ( '' )

  ival = i4vec_max_index_last ( n, a )
  print ( '  Last maximum index: %d' % ( ival ) )

  return

def i4vec_max_last ( l_length, l ):

#*****************************************************************************80
#
## i4vec_max_last() moves the maximum entry of an I4VEC to the last position.
#
#  Discussion:
#
#    This routine finds the largest entry in an array and moves
#    it to the end of the array.
#
#    If we ignore this last array entry, then the effect is the same
#    as "deleting" the maximum entry from the array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_length, the length of the array.
#
#    integer L(L_length), the array.
#
#  Output:
#
#    integer L(L_length), the maximum entry has been shifted to the end.
#
#    integer VALUE, the maximum entry in the input array.
#
  for i in range ( 1, l_length ):
    if ( l[i] < l[i-1] ):
      t = l[i]
      l[i] = l[i-1]
      l[i-1] = t
 
  value = l[l_length-1];

  return l, value

def i4vec_max_last_test ( rng ):

#*****************************************************************************80
#
## i4vec_max_last_test() tests i4vec_max_last().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#   John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'i4vec_max_last_test():' )
  print ( '  i4vec_max_last() identifies the largest element in an' )
  print ( '  I4VEC, and moves it to the final entry.' )

  x = rng.integers ( low = 1, high = 30, size = n, endpoint = True )

  i4vec_print ( n, x, '  Input vector:' )

  x, x_max = i4vec_max_last ( n, x )

  print ( '' )
  print ( '  Maximum: %d' % ( x_max ) )

  i4vec_print ( n, x, '  Output vector:' )

  return

def i4vec_max ( n, a ):

#*****************************************************************************80
#
## i4vec_max() returns the largest value in an I4VEC.
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
#    18 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the largest of the entries.
#
  i4_huge = 2147483647
  value = - i4_huge

  for i in range ( 0, n ):
    value = max ( value, a[i] )

  return value

def i4vec_max_test ( rng ):

#*****************************************************************************80
#
## i4vec_max_test() tests i4vec_max().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_max_test():' )
  print ( '  i4vec_max() returns the maximum entry in an I4VEC.' )

  n = 10
  a = 1
  b = 30
  x = rng.integers ( low = a, high = b, size = n, endpoint = True )

  i4vec_print ( n, x, '  The vector:' )
  
  x_max = i4vec_max ( n, x )
 
  print ( '' )
  print ( '  Maximum entry = %d' % ( x_max ) )

  return

def i4vec_mean_i4 ( n, a ):

#*****************************************************************************80
#
## i4vec_mean_i4() computes the I4 mean of an I4VEC.
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
#    04 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the rounded mean of the entries.
#
  mean = 0.0

  for i in range ( 0, n ):
    mean = mean + float ( a[i] )
  mean = mean / float ( n )

  value = int ( round ( mean ) )

  return value

def i4vec_mean_i4_test ( rng ):

#*****************************************************************************80
#
## i4vec_mean_i4_test() tests i4vec_mean_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2017
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
  print ( 'i4vec_mean_i4_test():' )
  print ( '  i4vec_mean_i4() computes the I4 mean of an I4VEC.' )

  n = 5
  lo = 0
  hi = 10
  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_mean_i4 ( n, a )
  print ( '' )
  print ( '  The I4 mean value is %d' % ( s ) )

  return

def i4vec_mean ( n, a ):

#*****************************************************************************80
#
## i4vec_mean() computes the mean of an I4VEC.
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
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    real VALUE, the mean of the entries.
#
  value = 0.0

  for i in range ( 0, n ):
    value = value + float ( a[i] )
  value = value / float ( n )

  return value

def i4vec_mean_test ( rng ):

#*****************************************************************************80
#
## i4vec_mean_test() tests i4vec_mean().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
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
  print ( 'i4vec_mean_test():' )
  print ( '  i4vec_mean() computes the mean of an I4VEC.' )

  n = 5
  lo = 0
  hi = 10
  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_mean ( n, a )
  print ( '' )
  print ( '  The mean value is %g' % ( s ) )

  return

def i4vec_min ( n, a ):

#*****************************************************************************80
#
## i4vec_min() returns the smallest entry in an I4VEC.
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
#    01 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the smallest entry.
#
  import numpy as np

  value = np.min ( a )

  return value

def i4vec_min_test ( rng ):

#*****************************************************************************80
#
## i4vec_min_test() tests i4vec_min().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_min_test():' )
  print ( '  i4vec_min() returns the minimum entry in an I4VEC.' )

  n = 10
  a = 1
  b = 30
  x = rng.integers ( low = a, high = b, size = n, endpoint = True )

  i4vec_print ( n, x, '  The vector:' )
  
  x_min = i4vec_min ( n, x )
 
  print ( '' )
  print ( '  Minimum entry = %d' % ( x_min ) )

  return

def i4vec_permute ( n, p, a ):

#*****************************************************************************80
#
## i4vec_permute() permutes an I4VEC in place.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    This routine permutes an array of integer "objects", but the same
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
#      A = (   1,   2,   3,   4,   5 )
#
#    Output:
#
#      A    = (   2,   4,   5,   1,   3 ).
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
#    integer N, the number of objects.
#
#    integer P[N], the permutation.  P(I) = J means
#    that the I-th element of the output array should be the J-th
#    element of the input array.
#
#    integer A[N], the array to be permuted.
#
#  Output:
#
#    integer A[N], the permuted array.
#
  check = perm0_check ( n, p );

  if ( not check ):
    print ( '' )
    print ( 'i4vec_permute(): Fatal error!' )
    print ( '  perm0_check rejects the permutation.' )
    raise Exception ( 'i4vec_permute(): Fatal error!' )
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
          print ( 'i4vec_permute(): Fatal error!' )
          print ( '  Entry IPUT = %d has' % ( iput ) )
          print ( '  an illegal value IGET = %d.' % (iget ) )
          raise Exception ( 'i4vec_permute(): Fatal error!' )

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

def i4vec_permute_test ( rng ):

#*****************************************************************************80
#
## i4vec_permute_test() tests i4vec_permute().
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
  import numpy as np

  n = 12

  print ( '' )
  print ( 'i4vec_permute_test():' )
  print ( '  i4vec_permute() reorders an I4VEC' )
  print ( '  according to a given permutation.' )

  b = 0
  c = n
  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  A[*], before rearrangement:' )

  p = perm0_uniform ( n, rng )

  i4vec_print ( n, p, '  Permutation vector P[*]:' )

  a = i4vec_permute ( n, p, a )

  i4vec_print ( n, a, '  A[P[*]]:' )

  return

def i4vec_permute_uniform ( n, a, rng ):

#*****************************************************************************80
#
## i4vec_permute_uniform() randomly permutes an I4VEC.
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
#    integer A(N), the array to be permuted.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(N), the permuted array.
#
  p = perm0_uniform ( n, rng )

  a = i4vec_permute ( n, p, a )

  return a

def i4vec_permute_uniform_test ( rng ):

#*****************************************************************************80
#
## i4vec_permute_uniform_test() tests i4vec_permute_uniform().
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
#    rng(): the current random number generator.
#
  import numpy as np

  n = 12

  print ( '' )
  print ( 'i4vec_permute_uniform_test():' )
  print ( '  i4vec_permute_uniform() randomly reorders an I4VEC.' )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = 101 + i

  i4vec_print ( n, a, '  A, before rearrangement:' )

  a = i4vec_permute_uniform ( n, a, rng )

  i4vec_print ( n, a, '  A, after rearrangement:' )

  return

def i4vec_print_mask ( n, a, mask, title ):

#*****************************************************************************80
#
## i4vec_print_mask() prints masked elements of an I4VEC.
#
#  Discussion:
#
#    Vector elements with a nonzero mask will be printed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2017
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
#    integer MASK(N), the mask.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    if ( mask[i] != 0 ):
      print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_mask_test ( ):

#*****************************************************************************80
#
## i4vec_print_mask_test() tests i4vec_print_mask().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_print_mask_test():' )
  print ( '  i4vec_print_mask() prints the masked elements of an I4VEC.' )

  n = 10
  v = np.array (    [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], dtype = np.int32 )
  mask = np.array ( [ 0, 1, 1, 0, 1, 0, 1, 0, 0,  0 ], dtype = np.int32 )

  i4vec_print ( n, v, '  Here is the full vector:' )
  i4vec_print ( n, mask, '  Here is the vector mask:' )
  i4vec_print_mask ( n, v, mask, '  Here is the masked vector I4VEC:' )

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

def i4vec_red ( n, a, incx ):

#*****************************************************************************80
#
## i4vec_red() divides out common factors in an I4VEC.
#
#  Discussion:
#
#    If A is a simple vector, then it has dimension N.
#
#    If A is a row of a matrix, then INCX will not be 1, and
#    the actual dimension of A is at least 1+(N-1)*INCX.
#
#    On output, the entries of A have no common factor
#    greater than 1.
#
#    If A is a simple vector, then INCX is 1, and we simply
#    check the first N entries of A.
#
#    If A is a row of a matrix, then INCX will be the number
#    of rows declared in the matrix, in order to allow us to
#    "skip" along the row.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(*), the vector to be reduced.
#
#    integer INCX, the distance between successive
#    entries of A that are to be checked.
#
#  Output:
#
#    integer A(*), the reduced vector.
#
#    integer IFACT, the common factor that was divided out.
#

#
#  Find the smallest nonzero value.
#
  ifact = 0
  indx = 0

  for i in range ( 0, n ):

    if ( a[indx] != 0 ):

      if ( ifact == 0 ):
        ifact = abs ( a[indx] )
      else:
        ifact = min ( ifact, abs ( a[indx] ) )

    indx = indx + incx

  if ( ifact == 0 ):
    return a, ifact
#
#  Find the greatest common factor of the entire vector.
#
  indx = 0
  for i in range ( 0, n ):
    ifact = i4_gcd ( a[indx], ifact )
    indx = indx + incx

  if ( ifact == 1 ):
    return a, ifact
#
#  Divide out the common factor.
#
  indx = 0
  for i in range ( 0, n ):
    a[indx] = a[indx] / ifact
    indx = indx + incx

  return a, ifact

def i4vec_red_test ( ):

#*****************************************************************************80
#
## i4vec_red_test() tests i4vec_red().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_red_test():' )
  print ( '  i4vec_red() divides out any common factors in the' )
  print ( '  entries of an I4VEC.' )

  m = 5
  n = 3
  a = np.array ( [ \
   [ 12, 88,   9 ], \
   [  4,  8, 192 ], \
   [-12, 88,  94 ], \
   [ 30, 18,  42 ], \
   [  0,  4,   8 ] ] )
 
  i4mat_print ( m, n, a, '  Apply i4vec_red to each row of this matrix:' )

  for i in range ( 0, m ):
    a[i,0:n], factor = i4vec_red ( n, a[i,0:n], 1 )

  i4mat_print ( m, n, a, '  Reduced matrix:' )

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

def i4vec_run_count ( n, a ):

#*****************************************************************************80
#
## i4vec_run_count() counts runs of equal values in an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of integer values.
#
#    A run is a sequence of equal values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector to be examined.
#
#  Output:
#
#    integer RUN_count, the number of runs.
#
  run_count = 0

  if ( n < 1 ):
    return run_count

  test = -1

  for i in range ( 0, n ):

    if ( i == 0 or a[i] != test ):
      run_count = run_count + 1
      test = a[i]

  return run_count

def i4vec_run_count_test ( rng ):

#*****************************************************************************80
#
## i4vec_run_count_test() tests i4vec_run_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2016
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
  print ( 'i4vec_run_count_test():' )
  print ( '  i4vec_run_count() counts runs in an I4VEC' )
  print ( '' )
  print ( ' Run Count        Sequence' )
  print ( '' )

  for test in range ( 0, 10 ):

    a = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

    run_count = i4vec_run_count ( n, a )

    print ( '  %8d        ' % ( run_count ), end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( a[i] ), end = '' )
    print ( '' )

  return

def i4vec_search_binary_a ( n, a, b ):

#*****************************************************************************80
#
## i4vec_search_binary_a() searches an ascending sorted I4VEC.
#
#  Discussion:
#
#    Binary search is used.
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
#  Reference:
#
#    Donald Kreher and Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 26.
#
#  Input:
#
#    integer N, the number of elements in the vector.
#
#    integer A(N), the array to be searched.  A must
#    be sorted in ascending order.
#
#    integer B, the value to be searched for.
#
#  Output:
#
#    integer INDX, the result of the search.
#    -1, B does not occur in A.
#    I, A(I) = B.
#
  indx = -1

  low = 0
  high = n - 1

  while ( low <= high ):

    mid = ( ( low + high ) // 2 )

    if ( a[mid] == b ):
      indx = mid;
      break
    elif ( a[mid] < b ):
      low = mid + 1
    elif ( b < a[mid] ):
      high = mid - 1

  return indx

def i4vec_search_binary_a_test ( ):

#*****************************************************************************80
#
## i4vec_search_binary_a_test() tests i4vec_search_binary_a().
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
  import numpy as np

  n = 10

  print ( '' )
  print ( 'i4vec_search_binary_a_test():' )
  print ( '  i4vec_search_binary_a() searches a ascending sorted vector.' )

  a = np.array ( [ 0, 1, 1, 2, 3, 4, 5, 6, 7, 8 ] )

  i4vec_print ( n, a, '  Ascending sorted array:' )

  b = 5

  print ( '' )
  print ( '  Now search for an instance of the value %d' % ( b ) )

  index = i4vec_search_binary_a ( n, a, b )

  print ( '' )
  if ( index == -1 ):
    print ( '  The value does not occur.' )
  else:
    print ( '  The value occurs at index = %d' % ( index ) )

  return

def i4vec_search_binary_d ( n, a, b ):

#*****************************************************************************80
#
## i4vec_search_binary_d() searches a descending sorted I4VEC.
#
#  Discussion:
#
#    Binary search is used.
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
#  Reference:
#
#    Donald Kreher and Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 26.
#
#  Input:
#
#    integer N, the number of elements in the vector.
#
#    integer A(N), the array to be searched.  A must
#    be sorted in descending order.
#
#    integer B, the value to be searched for.
#
#  Output:
#
#    integer INDX, the result of the search.
#    -1, B does not occur in A.
#    I, A(I) = B.
#
  indx = -1

  low = 0
  high = n - 1

  while ( low <= high ):

    mid = ( ( low + high ) // 2 )

    if ( a[mid] == b ):
      indx = mid;
      break
    elif ( b < a[mid] ):
      low = mid + 1
    elif ( a[mid] < b ):
      high = mid - 1

  return indx

def i4vec_search_binary_d_test ( ):

#*****************************************************************************80
#
## i4vec_search_binary_d_test() tests i4vec_search_binary_d().
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
  import numpy as np

  n = 10

  print ( '' )
  print ( 'i4vec_search_binary_d_test():' )
  print ( '  i4vec_search_binary_d() searches a descending sorted vector.' )

  a = np.array ( [ 8, 7, 6, 5, 4, 3, 2, 1, 1, 0 ] )

  i4vec_print ( n, a, '  Descending sorted array:' )

  b = 5

  print ( '' )
  print ( '  Now search for an instance of the value %d' % ( b ) )

  index = i4vec_search_binary_d ( n, a, b )

  print ( '' )
  if ( index == -1 ):
    print ( '  The value does not occur.' )
  else:
    print ( '  The value occurs at index = %d' % ( index ) )

  return

def i4vec_shift_circular ( n, x, k ):

#*****************************************************************************80
#
## i4vec_shift_circular() performs a circular shift on an I4VEC.
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
#    24 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vector entries.
#
#    integer X(N), the vector to be shifted.
#
#    integer K, the amount by which each entry is to
#    be shifted.  K should be nonnegative.
#
#  Output:
#
#    integer X(N), the shifted vector.
#
  import numpy as np

  x = np.roll ( x, k )

  return x

def i4vec_shift_circular_test ( ):

#*****************************************************************************80
#
## i4vec_shift_circular_test() tests i4vec_shift_circular().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4vec_shift_circular_test():' )
  print ( '  i4vec_shift_circular() circularly shifts a vector by K positions.' )

  n = 10
  a = i4vec_indicator1 ( n )
  i4vec_print ( n, a, '  The vector:' )

  k = 3
  print ( '' )
  print ( '  Using a circular shift of K = ', k )

  a2 = i4vec_shift_circular ( n, a, k )
  i4vec_print ( n, a2, '  Shifted vector:' )

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

def i4vec_sorted_unique_count ( n, a ):

#*****************************************************************************80
#
## i4vec_sorted_unique_count() counts the unique elements in a sorted I4VEC.
#
#  Discussion:
#
#    Because the array is sorted, this algorithm is O(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 April 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    integer A(N), the sorted array to examine.
#
#  Output:
#
#    integer UNIQUE_NUM, the number of unique elements of A.
#
  unique_num = 0

  if ( n < 1 ):
    return unique_num

  unique_num = 1

  for i in range ( 1, n ):

    if ( a[i-1] != a[i] ):
      unique_num = unique_num + 1

  return unique_num

def i4vec_sorted_unique_count_test ( rng ):

#*****************************************************************************80
#
## i4vec_sorted_unique_count_test() tests i4vec_sorted_unique_count().
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
#    rng(): the current random number generator.
#
  import numpy as np

  n = 20
  b = 0
  c = n

  print ( '' )
  print ( 'i4vec_sorted_unique_count_test():' )
  print ( '  i4vec_sorted_unique_count() counts unique entries in a sorted I4VEC.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  a = i4vec_sort_heap_a ( n, a )

  i4vec_print ( n, a, '  Input vector:' )

  a_unique = i4vec_sorted_unique_count ( n, a )

  print ( '' )
  print ( '  Number of unique entries is %d' % ( a_unique ) )

  return

def i4vec_sorted_unique_hist ( n, a ):

#*****************************************************************************80
#
## i4vec_sorted_unique_hist() histograms unique elements of a sorted I4VEC.
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
#    integer N, the number of elements of A.
#
#    integer A(N), the array to examine.  The elements of A
#    should have been sorted.
#
#  Output:
#
#    integer UNIQUE_NUM, the number of unique elements of A.
#
#    integer AUNIQ(UNIQUE_NUM), the unique elements of A.
#
#    integer ACOUNT(UNIQUE_NUM), the number of times each element
#    of AUNIQ occurs in A.
#
  import numpy as np

  auniq = np.unique ( a )
  unique_num = len ( auniq )
  acount = np.zeros ( unique_num )
#
#  Start taking statistics.
#
  k = 0
  acount[k] = 1

  for i in range ( 1, n ):

    if ( a[i] == auniq[k] ):

      acount[k] = acount[k] + 1

    else:

      k = k + 1
      acount[k] = 1

  return unique_num, auniq, acount

def i4vec_sorted_unique_hist_test ( rng ):

#*****************************************************************************80
#
## i4vec_sorted_unique_hist_test() tests i4vec_sorted_unique_hist_test().
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_sorted_unique_hist_test():' )
  print ( '  i4vec_sorted_unique_hist_test() is given a sorted array' )
  print ( '  of integers, and returns the number of unique values,' )
  print ( '  the unique values, and their frequency.' )

  n = 50
  a = 0
  b = 10
 
  v1 = rng.integers ( low = a, high = b, size = n, endpoint = True )

  v2 = rng.integers ( low = a, high = b, size = n, endpoint = True )

  v3 = np.zeros ( n, dtype = np.int32 )

  v3 = v1 * v2

  v3 = np.sort ( v3 )

  print ( '' )
  print ( '  The sorted vector' )
  print ( v3 )
  i4vec_print ( n, v3, '  The sorted vector:' )

  unique_num, unique_value,  unique_freq = i4vec_sorted_unique_hist ( n, v3 )

  print ( '' )
  print ( '  Unique values and frequencies:' )
  print ( np.c_ [ unique_value, unique_freq ] )

  return

def i4vec_sorted_unique ( n, a ):

#*****************************************************************************80
#
## i4vec_sorted_unique() finds the unique elements in a sorted I4VEC.
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
#    integer N, the number of elements in A.
#
#    integer A(N), the sorted integer array.
#
#  Output:
#
#    integer N_unique, the number of unique elements in A.
#
#    integer A_unique[N_unique], the unique elements.
#
  import numpy as np

  if ( n <= 0 ):
    n_unique = 0
    a_unique = np.zeros ( 0 )
    return n_unique, a_unique

  n_unique = i4vec_sorted_unique_count ( n, a )

  a_unique = np.zeros ( n_unique, dtype = np.int32 )

  k = 0
  a_unique[0] = a[0];

  for i in range ( 1, n ):

    if ( a[i] != a_unique[k] ):
      k = k + 1
      a_unique[k] = a[i]

  return n_unique, a_unique

def i4vec_sorted_unique_test ( rng ):

#*****************************************************************************80
#
## i4vec_sorted_unique_test() tests i4vec_sorted_unique().
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
#    rng(): the current random number generator.
#
  import numpy as np

  n = 20
  b = 0
  c = n

  print ( '' )
  print ( 'i4vec_sorted_unique_test():' )
  print ( '  i4vec_sorted_unique() finds unique entries in a sorted array.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  a = i4vec_sort_heap_a ( n, a )

  i4vec_print ( n, a, '  Input vector:' )

  unique_num, a_unique = i4vec_sorted_unique ( n, a )

  i4vec_print ( unique_num, a_unique, '  Unique entries:' )

  return

def i4vec_sort_heap_a ( n, a ):

#*****************************************************************************80
#
## i4vec_sort_heap_a() ascending sorts an I4VEC using heap sort.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 September 2015
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
#    integer N, the number of entries in the array.
#
#    integer A(N), the array to be sorted;
#
#  Output:
#
#    integer A_sorted(N), the sorted array.
#
  import numpy as np

  if ( n == 1 ):
    a_sorted = np.zeros ( n )
    a_sorted[0] = a[0]
    return a_sorted
#
#  1: Put A into descending heap form.
#
  a_sorted = i4vec_heap_d ( n, a )
#
#  2: Sort A.
#
#  The largest object in the heap is in A(0).
#  Move it to position A(N-1).
#
  temp = a_sorted[0]
  a_sorted[0] = a_sorted[n-1]
  a_sorted[n-1] = temp
#
#  Consider the diminished heap of size N1.
#
  for n1 in range ( n - 1, 0, -1 ):
#
#  Restore the heap structure of A(0) through A(N1-1).
#
    a_resorted = i4vec_heap_d ( n1, a_sorted )

    for i in range ( 0, n1 ):
      a_sorted[i] = a_resorted[i]
#
#  Take the largest object from A(1) and move it to A(N1).
#
    temp = a_sorted[0]
    a_sorted[0] = a_sorted[n1-1]
    a_sorted[n1-1] = temp

  return a_sorted

def i4vec_sort_heap_a_test ( rng ):

#*****************************************************************************80
#
## i4vec_sort_heap_a_test() tests i4vec_sort_heap_a().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2015
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
  print ( 'i4vec_sort_heap_a_test():' )
  print ( '  i4vec_sort_heap_a() ascending sorts an I4VEC.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted:' )

  a = i4vec_sort_heap_a ( n, a )

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

def i4vec_sort_insert_a ( n, a ):

#*****************************************************************************80
#
## i4vec_sort_insert_a() uses an ascending insertion sort on an I4VEC.
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
#  Reference:
#
#    Donald Kreher and Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 11.
#
#  Input:
#
#    integer N, the number of items in the vector.
#    N must be positive.
#
#    integer A(N), the array to be sorted.
#
#  Output:
#
#    integer A(N), the sorted array.
#
  for i in range ( 1, n ):

    x = a[i]

    j = i - 1

    while ( 0 <= j ):

      if ( a[j] <= x ):
        break

      a[j+1] = a[j]
      j = j - 1

    a[j+1] = x

  return a

def i4vec_sort_insert_a_test ( rng ):

#*****************************************************************************80
#
## i4vec_sort_insert_a_test() tests i4vec_sort_insert_a().
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

  n = 10

  print ( '' )
  print ( 'i4vec_sort_insert_a_test():' )
  print ( '  i4vec_sort_insert_a() sorts an integer array.' )

  b = 0
  c = n

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array:' )

  a = i4vec_sort_insert_a ( n, a )

  i4vec_print ( n, a, '  Sorted array:' )

  return

def i4vec_sort_insert_d ( n, a ):

#*****************************************************************************80
#
## i4vec_sort_insert_d() uses a descending insertion sort on an I4VEC.
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
#  Reference:
#
#    Algorithm 1.1,
#    Donald Kreher and Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 11.
#
#  Input:
#
#    integer N, the number of items in the vector.
#    N must be positive.
#
#    integer A(N), the array to be sorted.
#
#  Output:
#
#    integer A(N), the sorted array.
#
  for i in range ( 1, n ):

    x = a[i]

    j = i - 1

    while ( 0 <= j ):

      if ( x <= a[j] ):
        break

      a[j+1] = a[j]
      j = j - 1

    a[j+1] = x

  return a

def i4vec_sort_insert_d_test ( rng ):

#*****************************************************************************80
#
## i4vec_sort_insert_d_test() tests i4vec_sort_insert_d().
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

  n = 10

  print ( '' )
  print ( 'i4vec_sort_insert_d_test():' )
  print ( '  i4vec_sort_insert_d() descending sorts an I4VEC.' )

  b = 0
  c = n

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array:' )

  a = i4vec_sort_insert_d ( n, a )

  i4vec_print ( n, a, '  Descending sorted array:' )

  return

def i4vec_sum ( n, a ):

#*****************************************************************************80
#
## i4vec_sum() sums the entries of an I4VEC.
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
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the sum of the entries.
#
  value = 0

  for i in range ( 0, n ):
    value = value + a[i]

  return value

def i4vec_sum_test ( rng ):

#*****************************************************************************80
#
## i4vec_sum_test() tests i4vec_sum().
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

  print ( '' )
  print ( 'i4vec_sum_test():' )
  print ( '  i4vec_sum() sums the entries of an I4VEC.' )

  n = 5
  lo = 0
  hi = 10
  a = rng.integers ( low = lo, high = hi, size = n, endpoint = True )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_sum ( n, a )
  print ( '' )
  print ( '  The vector entries sum to %d' % ( s ) )

  return

def i4vec_sum_vec ( n, a, b ):

#*****************************************************************************80
#
## i4vec_sum_vec() does a pairwise sum of two I4VEC's.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Example:
#
#    Input:
#
#      A = ( 1, 2, 3, 4 )
#      B = ( 5, 6, 7, 8 )
#
#    Output:
#
#      C = ( 6, 8, 10, 12 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A(N), B(N), the vectors to be summed.
#
#  Output:
#
#    integer C(N), the pairwise sum of A and B.
#
  import numpy as np

  c = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    c[i] = a[i] + b[i]

  return c

def i4vec_sum_vec_test ( rng ):

#*****************************************************************************80
#
## i4vec_sum_vec_test() tests i4vec_sum_vec().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2016
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
  print ( 'i4vec_sum_vec_test():' )
  print ( '  i4vec_sum_vec() sums the entries in an I4VEC.' )

  n = 5
  a = rng.integers ( low = 0, high = 10, size = n, endpoint = True )
  i4vec_transpose_print ( n, a, '  A:' );

  b = rng.integers ( low = 0, high = 10, size = n, endpoint = True )
  i4vec_transpose_print ( n, b, '  B:' )

  c = i4vec_sum_vec ( n, a, b )
  i4vec_transpose_print ( n, c, '  C = A + B:' )

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

def i4vec_uniform_ab ( n, a, b, seed ):

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
#    integer N, the number of entries in the vector.
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    integer C(N), the randomly chosen integer vector.
#
#    integer SEED, the updated seed.
#
  import numpy as np

  i4_huge = 2147483647

  seed = int ( seed  )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4vec_uniform_ab(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4vec_uniform_ab(): Fatal error!' )

  a = round ( a )
  b = round ( b )

  c = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    seed = ( seed % i4_huge )

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
      +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round ( r )

    value = max ( value, min ( a, b ) )
    value = min ( value, max ( a, b ) )

    c[i] = value

  return c, seed

def i4vec_uniform_ab_test ( ):

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
  n = 20
  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'i4vec_uniform_ab_test():' )
  print ( '  i4vec_uniform_ab() computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  v, seed = i4vec_uniform_ab ( n, a, b, seed )

  i4vec_print ( n, v, '  The random vector:' )

  return

def i4vec_unique_count ( n, a ):

#*****************************************************************************80
#
## i4vec_unique_count() counts the unique elements in an I4VEC.
#
#  Discussion:
#
#    Because the array is sorted, this algorithm is O(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 April 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    integer A(N), the sorted array to examine.
#
#  Output:
#
#    integer UNIQUE_NUM, the number of unique elements of A.
#
  unique_num = 0

  for i in range ( 0, n ):

    unique_num = unique_num + 1

    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        unique_num = unique_num - 1
        break

  return unique_num

def i4vec_unique_count_test ( rng ):

#*****************************************************************************80
#
## i4vec_unique_count_test() tests i4vec_unique_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2016
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
  c = n

  print ( '' )
  print ( 'i4vec_unique_count_test():' )
  print ( '  i4vec_unique_count() counts unique entries in an I4VEC.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  a_unique = i4vec_unique_count ( n, a )

  print ( '' )
  print ( '  Number of unique entries is %d' % ( a_unique ) )

  return

def i4vec_variance ( n, x ):

#*****************************************************************************80
#
## i4vec_variance() returns the variance of an I4VEC.
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
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer X(N), the vector.
#
#  Output:
#
#    real VALUE, the variance of the vector.
#
  import numpy as np

  mean = 0.0
  for i in range ( 0, n ):
    mean = mean + float ( x[i] )
  mean = mean / float ( n )

  value = 0.0
  for i in range ( 0, n ):
    value = value + ( float ( x[i] ) - mean ) ** 2

  value = value / float ( n - 1 )

  return value

def i4vec_variance_test ( rng ):

#*****************************************************************************80
#
## i4vec_variance_test() tests i4vec_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2016
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
  print ( 'i4vec_variance_test():' )
  print ( '  i4vec_variance() computes the variance of an I4VEC.' )

  n = 10
  i4_lo = -5
  i4_hi = +5

  a = rng.integers ( low = i4_lo, high = i4_hi, size = n, endpoint = True )

  i4vec_print ( n, a, '  Input vector:' )

  value = i4vec_variance ( n, a )

  print ( '' )
  print ( '  Value = %g' % ( value ) )

  return

def i4vec_width ( n, a ):

#*****************************************************************************80
#
## i4vec_width() returns the "width" of an I4VEC.
#
#  Discussion:
#
#    The width of an integer vector is simply the maximum of the widths of
#    its entries.
#
#    The width of a single integer is the number of characters 
#    necessary to print it.
#
#    The width of an integer vector can be useful when the vector is 
#    to be printed.
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
#    integer N, the number of entries in the vector.
#
#    integer A(N), the vector.
#
#  Output:
#
#    integer VALUE, the width of the vector.
#
  value = -1

  for i in range ( 0, n ):
    value = max ( value, i4_width ( a[i] ) )

  return value

def i4vec_width_test ( ):

#*****************************************************************************80
#
## i4vec_width_test() tests i4vec_width().
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
  import numpy as np

  n = 13
  i4vec = np.array ( [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ] )

  print ( '' )
  print ( 'i4vec_width_test():' )
  print ( '  i4vec_width() determines the printing "width" of an I4VEC.' )

  i4vec_print ( n, i4vec, '  The vector' )

  w = i4vec_width ( n, i4vec )

  print ( '' )
  print ( '  The printing width is %d' % ( w ) )

  return

def i4vec2_compare ( n, a1, a2, i, j ):

#*****************************************************************************80
#
## i4vec2_compare() compares two I4VEC2's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data items.
#
#    integer A1(N), A2(N), contain the two components of each item.
#
#    integer I, J, the items to be compared.
#
#  Output:
#
#    integer ISGN, the results of the comparison:
#    -1, item I < item J,
#     0, item I = item J,
#    +1, item J < item I.
#
  isgn = 0

  if ( a1[i] < a1[j] ):

    isgn = -1

  elif ( a1[i] == a1[j] ):

    if ( a2[i] < a2[j] ):
      isgn = -1
    elif ( a2[i] < a2[j] ):
      isgn = 0
    elif ( a2[j] < a2[i] ):
      isgn = +1

  elif ( a1[j] < a1[i] ):

    isgn = +1

  return isgn

def i4vec2_compare_test ( ):

#*****************************************************************************80
#
## i4vec2_compare_test() tests i4vec2_compare().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '\n' )
  print ( 'i4vec2_compare_test():\n' )
  print ( '  i4vec2_compare() order-compares two I4VEC2''s;\n' )
#
#  N = the number of items.
#
  n = 5
#
#  For 1 <= I <= N, the values A1(I), A2(I) are an item.
#
  a1 = np.array ( [ 1, 1, 2, 2, 3 ] )
  a2 = np.array ( [ 4, 0, 1, 2, 2 ] )

  print ( '' )
  print ( '   I:  A1  A2' )
  print ( '' )
  for i in range ( 0, n ):
    print ( i, a1[i], a2[i] )
#
#  Compare all pairs.
#
  b = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      b[i,j] = i4vec2_compare ( n, a1, a2, i, j )
#
#  Print the comparison matrix.
#
  print ( '' );
  print ( '  Comparison matrix:' )
  print ( b )

  return

def i4vec2_print ( a, b, title ):

#*****************************************************************************80
#
## i4vec2_print() prints an I4VEC2.
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
#    integer A(N), B(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d  %6d' % ( i, a[i], b[i] ) )

  return

def i4vec2_print_test ( ):

#*****************************************************************************80
#
## i4vec2_print_test() tests i4vec2_print().
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

  n = 10

  print ( '' )
  print ( 'i4vec2_print_test():' )
  print ( '  i4vec2_print() prints a pair of I4VECs' )

  a = np.zeros ( n + 1, dtype = np.int32 )
  b = np.zeros ( n + 1, dtype = np.int32 )

  for i in range ( 0, n + 1 ):
    a[i] = ( i * ( i + 1 ) ) / 2
    b[i] = ( i * ( i + 1 ) * ( 2 * i + 1 ) ) / 6

  i4vec2_print ( a, b, '  I, sum of I, sum of I^2:' )

  return

def i4vec2_sort_insert_a ( a1, a2 ):

#*****************************************************************************80
#
## i4vec2_sort_insert_a() uses an ascending insertion sort on an I4VEC2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 11.
#
#  Input:
#
#    integer A1(N), A2(N), the pair of arrays to be sorted.
#
#  Output:
#
#    integer B1(N), B2(N), the sorted arrays.
#
  n = len ( a1 )

  b1 = a1.copy ( )
  b2 = a2.copy ( )

  for i in range ( 1, n ):

    x1 = b1[i]
    x2 = b2[i]

    j = i - 1

    while ( 0 <= j ):

      if ( b1[j] < x1 or ( b1[j] == x1 and b2[j] < x2 ) ):
        break

      b1[j+1] = b1[j]
      b2[j+1] = b2[j]
      j = j - 1

    b1[j+1] = x1
    b2[j+1] = x2

  return b1, b2

def i4vec2_sort_insert_a_test (  ):

#*****************************************************************************80
#
## i4vec2_sort_insert_a_test() tests i4vec2_sort_insert_a().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec2_sort_insert_a_test():' )
  print ( '  i4vec2_sort_insert_a() uses insertion to perform an' )
  print ( '  ascending sort of a pair of I4VECs;' )

  v1 = np.array ( [ 3, 2, 3, 3, 2, 1, 3, 3, 3, 1 ] )
  v2 = np.array ( [ 2, 1, 2, 2, 1, 3, 2, 3, 2, 3 ] )

  i4vec2_print ( v1, v2, '  The array:' );

  v1, v2 = i4vec2_sort_insert_a ( v1, v2 )

  i4vec2_print ( v1, v2, '  After ascending insertion sort:' )

  return

def i4vec2_sorted_unique ( a1, a2 ):

#*****************************************************************************80
#
## i4vec2_sorted_unique() keeps unique elements of a sorted I4VEC2.
#
#  Discussion:
#
#    Item I is stored as the pair A1(I), A2(I).
#
#    The items must have been sorted, or at least it must be the
#    case that equal items are stored in adjacent vector locations.
#
#    If the items were not sorted, then this routine will only
#    replace a string of equal values by a single representative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A1(N), A2(N), the array of N items.
#
#  Output:
#
#    integer B1(UNIQUE_NUM), B2(UNIQUE_NUM), an array of NUNIQ unique items.
#
  import numpy as np

  n = len ( a1 )
  b1 = np.zeros ( 0 )
  b2 = np.zeros ( 0 )

  if ( n <= 0 ):
    return b1, b2

  iu = 0
  b1 = np.array ( [ a1[iu] ] )
  b2 = np.array ( [ a2[iu] ] )

  for i in range ( 1, n ):

    if ( a1[i] != a1[iu] or a2[i] != a2[iu] ):
      iu = i
      b1 = np.append ( b1, a1[iu] )
      b2 = np.append ( b2, a2[iu] )

  return b1, b2

def i4vec2_sorted_unique_test (  ):

#*****************************************************************************80
#
## i4vec2_sorted_unique_test() tests i4vec2_sorted_unique().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec2_sorted_unique_test():' )
  print ( '  i4vec2_sorted_unique() returns unique entries' )
  print ( '  in a pair of sorted I4VECs.' )

  a1 = np.array ( [ 1, 1, 2, 2, 3, 3, 3, 3, 3, 3 ] )
  a2 = np.array ( [ 3, 3, 1, 1, 2, 2, 2, 2, 2, 3 ] )

  i4vec2_print ( a1, a2, '  The sorted array:' )

  b1, b2 = i4vec2_sorted_unique ( a1, a2 )

  i4vec2_print ( b1, b2, '  The unique values:' )

  return

def i4vec2_sorted_unique_count ( a1, a2 ):

#*****************************************************************************80
#
## i4vec2_sorted_unique_count() counts unique elements of a sorted I4VEC2.
#
#  Discussion:
#
#    Item I is stored as the pair A1(I), A2(I).
#
#    The items must have been sorted, or at least it must be the
#    case that equal items are stored in adjacent vector locations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A1(N), A2(N), the array of N items.
#
#  Output:
#
#    integer UNIQUE_NUM, the number of unique items.
#
  n = len ( a1 )

  unique_num = 0

  if ( n <= 0 ):
    return unique_num

  iu = 0
  unique_num = 1
  
  for i in range ( 1, n ):

    if ( a1[i] != a1[iu] or a2[i] != a2[iu] ):
      iu = i
      unique_num = unique_num + 1

  return unique_num

def i4vec2_sorted_unique_count_test (  ):

#*****************************************************************************80
#
## i4vec2_sorted_unique_count_test() tests i4vec2_sorted_unique_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec2_sorted_unique_count_test():' )
  print ( '  i4vec2_sorted_unique_count() counts unique entries' )
  print ( '  in a pair of sorted I4VECs.' )

  v1 = np.array ( [ 1, 1, 2, 2, 3, 3, 3, 3, 3, 3 ] )
  v2 = np.array ( [ 3, 3, 1, 1, 2, 2, 2, 2, 2, 3 ] )

  i4vec2_print ( v1, v2, '  The sorted array:' )

  unique_num = i4vec2_sorted_unique_count ( v1, v2 )

  print ( '' )
  print ( '  Number of unique items is', unique_num )

  return

def intspace ( a, b, n ):

#*****************************************************************************80
#
## intspace() returns roughly equally spaced integers in an interval.
#
#  Discussion:
#
#    intspace() is a sort of "linspace()" for integers.
#
#    An interval is defined by integers A <= B.
#
#    If possible, a vector C of N integers is to be determined, with
#    C(1) = A and C(N) = B.
#
#    So far as possible, the entries of C should be equally spaced in [A,B].
#
#    However, if B-A+1 < N, then we simply return C = A:B.
#
#    A use for this code can be imagined in which a large array of data
#    has been computed, and it is desired to make a plot.  However, displaying
#    all the data might result in an ugly plot, or one that takes too long
#    to display.  One can then specify an index set like 
#      c = intspace ( 1, max, 100 )
#    and restrict the plot to the data indexed by C.
#
#    Similarly, it might be desired to print out sample values of a large
#    array of data; this function would make it easy to do this in a
#    fairly regular fashion.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer A, B: the left and right endpoints.
#
#    integer N: the number of samples desired.
#
#  Output:
#
#    integer C[*]: the sample values.  The first and last entries
#    of C will be A and B respectively.  The number of entries in C
#    will be min ( N, B+1-A).  The entries of C will be roughly
#    equally spaced.
#
  import numpy as np

  if ( b + 1 - a <= n ):
    c = np.arange ( a, b + 1 )
  else:
    i = np.arange ( n - 1, -1, -1 )
    j = np.arange ( 0, n )
    c = np.round ( ( i * a + j * b ) / ( n - 1 ) )

  c = c.astype ( int )

  return c

def intspace_test ( ):

#*****************************************************************************80
#
## intspace_test() tests intspace().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2022
#
#  Author:
#
#    John Burkardt.
#
  print ( '' )
  print ( 'intspace_test():' )
  print ( '  intspace() returns a set of min(N,B+1-A)' )
  print ( '  equally spaced integers between A and B.' )
  print ( '' )

  a = 5
  b = 10
  n = 20
  c = intspace ( a, b, n )
  print ( '  a = ', a, ', b =', b, ', n = ', n, '\n' )
  print ( c )

  a = 5
  b = 77
  n = 20
  c = intspace ( a, b, n )
  print ( '  a = ', a, ', b =', b, ', n = ', n, '\n' )
  print ( c )

  a = 5
  b = 100
  n = 20
  c = intspace ( a, b, n )
  print ( '  a = ', a, ', b =', b, ', n = ', n, '\n' )
  print ( c )

  a = 5
  b = 1000
  n = 20
  c = intspace ( a, b, n )
  print ( '  a = ', a, ', b =', b, ', n = ', n, '\n' )
  print ( c )

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

def l4_to_i4 ( l ):

#*****************************************************************************80
#
## l4_to_i4() converts an L4 to an I4.
#
#  Discussion:
#
#    0 is FALSE, and anything else if TRUE.
#
#    An I4 is an integer value.
#    An L4 is a logical value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    bool L, a logical value.
#
#  Output:
#
#    integer VALUE, the integer value of L.
#
  if ( l ):
    value = 1
  else:
    value = 0

  return value

def l4_to_i4_test ( ):

#*****************************************************************************80
#
## l4_to_i4_test() tests l4_to_i4(). 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'l4_to_i4_test():' )
  print ( '  l4_to_i4() converts an L4 to an I4.' )
  print ( '' )
  print ( '      L4   I4' )
  print ( '' )

  l4 = False
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )

  l4 = True
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )

  return

def pascal_to_i4 ( i, j ):

#*****************************************************************************80
#
## pascal_to_i4() converts Pacal triangle coordinates to a linear index.
#
#  Discussion:
#
#    We describe the grid points in a Pascal triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#  Example:
#
#     K  I  J
#
#     1  0  0
#     2  1  0
#     3  0  1
#     4  2  0
#     5  1  1
#     6  0  2
#     7  3  0
#     8  2  1
#     9  1  2
#    10  0  3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the row and column indices.  I and J must
#    be nonnegative.
#
#  Output:
#
#    integer K, the linear index of the (I,J) element.
#
  if ( i < 0 ):
    print ( '' )
    print ( 'pascal_to_i4(): Fatal error!' )
    print ( '  I < 0.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'pascal_to_i4(): Fatal error!' );
  elif ( j < 0 ):
    print ( '' )
    print ( 'pascal_to_i4(): Fatal error!' )
    print ( '  J < 0.' )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'pascal_to_i4(): Fatal error!' )

  d = i + j

  k = ( d * ( d + 1 ) ) // 2 + j + 1

  return k

def pascal_to_i4_test ( ):

#*****************************************************************************80
#
## pascal_to_i4_test() tests pascal_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pascal_to_i4_test():' )
  print ( '  pascal_to_i4() converts Pascal triangle indices to a' )
  print ( '  linear index.' )
  print ( '' )
  print ( '     I     J =>    K' )
  print ( '' )

  for d in range ( 0, 5 ):
    for i in range ( d, -1, -1 ):
      j = d - i;
      k = pascal_to_i4 ( i, j )
      print ( '  %4d  %4d    %4d' % ( i, j, k ) )
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
#    logical CHECK:
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
## perm0_uniform() selects a random permutation of 0, ..., N-1.
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
#    rng(): the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'perm0_uniform_test():' )
  print ( '  perm0_uniform() randomly selects a permutation of 0, ..., N-1.' )
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
#    logical CHECK:
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
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation of the digits 1 through N.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

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
#    rng(): the current random number generator.
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

def permutation_symbol ( n, ivec ):

#*****************************************************************************80
#
## permutation_symbol() evaluates the Levi-Civita permutation symbol.
#
#  Discussion:
#
#    Given a vector of N values I(), 
#
#      epsilon = product ( q < p ) ( i(p) - i(q) ) / abs ( i(p) - i(q) )
#
#    where epsilon is 0 if any pair of values are equal.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    integer IVEC(N), the vector of values.
#
#  Output:
#
#    integer VALUE, the value of the Levi-Civita permutation symbol,
#    which will be -1, 0, or 1.
#
  value = 1

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      if ( ivec[i] == ivec[j] ):
        value = 0
        return value
      elif ( ivec[i] < ivec[j] ):
        value = - value

  return value

def permutation_symbol_test ( ):

#*****************************************************************************80
#
## permutation_symbol_test() tests permutation_symbol().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'permutation_symbol_test():' )
  print ( '  permutation_symbol() evaluates the Levi-Civita permutation symbol.' )

  n = 5
  a = np.array ( [ 1, 2, 3, 4, 5 ] )
  i4vec_transpose_print ( n, a, '  Input vector:' )
  value = permutation_symbol ( n, a )
  print ( '  Levi-Civita permutation symbol = %d' % ( value ) )

  n = 5
  a = np.array ( [ 4, 2, 3, 1, 5 ] )
  i4vec_transpose_print ( n, a, '  Input vector:' )
  value = permutation_symbol ( n, a )
  print ( '  Levi-Civita permutation symbol = %d' % ( value ) )

  n = 5
  a = np.array ( [ 1, 2, 3, 4, 2 ] )
  i4vec_transpose_print ( n, a, '  Input vector:' )
  value = permutation_symbol ( n, a )
  print ( '  Levi-Civita permutation symbol = %d' % ( value ) )

  return

def prime ( n ):

#*****************************************************************************80
#
## prime returns() returns any of the first PRIME_max prime numbers.
#
#  Discussion:
#
#    prime_max is 1600, and the largest prime stored is 13499.
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

def triangle_lower_to_i4 ( i, j ):

#*****************************************************************************80
#
## triangle_lower_to_i4() converts a lower triangular coordinate to an integer.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the lower half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1)
#    (2,1) (2,2)
#    (3,1) (3,2) (3,3)
#    (4,1) (4,2) (4,3) (4,4)
#
#    as the linear array
#
#    (1,1) (2,1) (2,2) (3,1) (3,2) (3,3) (4,1) (4,2) (4,3) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    Thus, our goal is, given the row I and column J of the data,
#    to produce the value K which indicates its position in the linear
#    array.
#
#    The triangular numbers are the indices associated with the
#    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
#    and so on.
#
#  Formula:
#
#    K = J + ( (I-1) * I ) / 2
#
#  First Values:
#
#     I  J  K
#
#     0  0  0
#     1  1  1
#     2  1  2
#     2  2  3
#     3  1  4
#     3  2  5
#     3  3  6
#     4  1  7
#     4  2  8
#     4  3  9
#     4  4 10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the row and column indices.  I and J must
#    be nonnegative, and J must not be greater than I.
#
#  Output:
#
#    integer VALUE, the linear index of the (I,J) element.
#
  if ( i < 0 ):
    print ( '' )
    print ( 'triangle_lower_to_i4(): Fatal error!' )
    print ( '  I < 0.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'triangle_lower_to_i4(): Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'triangle_lower_to_i4(): Fatal error!' )
    print ( '  J < 0.' )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_lower_to_i4(): Fatal error!' )

  if ( i < j ):
    print ( '' )
    print ( 'triangle_lower_to_i4(): Fatal error!' )
    print ( '  I < J.' )
    print ( '  I = %d' % ( i ) )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_lower_to_i4(): Fatal error!' )

  value = j + ( ( i + 1 ) * i ) // 2

  return value

def triangle_lower_to_i4_test ( ):

#*****************************************************************************80
#
## triangle_lower_to_i4_test() tests triangle_lower_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'triangle_lower_to_i4_test():' )
  print ( '  triangle_lower_to_i4() converts a lower triangular index to a linear one.' )
  print ( '' )
  print ( '   ( I,    J ) ==> K' )
  print ( '' )

  for i in range ( 0, 5 ):
    for j in range ( 0, i + 1 ):
      k = triangle_lower_to_i4 ( i,j )  
      print ( '  %4d  %4d    %4d' % ( i, j, k ) )

  return

def triangle_upper_to_i4 ( i, j ):

#*****************************************************************************80
#
## triangle_upper_to_i4() converts an upper triangular coordinate to an integer.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the upper half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1) (1,2) (1,3) (1,4)
#          (2,2) (2,3) (2,4)
#                (3,3) (3,4)
#                      (4,4)
#
#    as the linear array
#
#    (1,1) (1,2) (2,2) (1,3) (2,3) (3,3) (1,4) (2,4) (3,4) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    Thus, our goal is, given the row I and column J of the data,
#    to produce the value K which indicates its position in the linear
#    array.
#
#    The triangular numbers are the indices associated with the
#    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
#    and so on.
#
#  Formula:
#
#    K = I + ( (J-1) * J ) / 2
#
#  First Values:
#
#     I  J  K
#
#     0  0  0
#     1  1  1
#     1  2  2
#     2  2  3
#     1  3  4
#     2  3  5
#     3  3  6
#     1  4  7
#     2  4  8
#     3  4  9
#     4  4 10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the row and column indices.  I and J must
#    be nonnegative, and I must not be greater than J.
#
#  Output:
#
#    integer VALUE, the linear index of the (I,J) element.
#
  if ( i < 0 ):
    print ( '' )
    print ( 'triangle_upper_to_i4(): Fatal error!' )
    print ( '  I < 0.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'triangle_upper_to_i4(): Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'triangle_upper_to_i4(): Fatal error!' )
    print ( '  J < 0.' )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_upper_to_i4(): Fatal error!' )

  if ( j < i ):
    print ( '' )
    print ( 'triangle_upper_to_i4(): Fatal error!' )
    print ( '  I < J.' )
    print ( '  I = %d' % ( i ) )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_upper_to_i4(): Fatal error!' )

  value = i + ( ( j + 1 ) * j ) // 2

  return value

def triangle_upper_to_i4_test ( ):

#*****************************************************************************80
#
## triangle_upper_to_i4_test() tests triangle_upper_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'triangle_upper_to_i4_test():' )
  print ( '  triangle_upper_to_i4() converts an upper triangular index to a linear one.' )
  print ( '' )
  print ( '   ( I,    J ) ==> K' )
  print ( '' )

  for j in range ( 0, 5 ):
    for i in range ( 0, j + 1 ):
      k = triangle_upper_to_i4 ( i,j )  
      print ( '  %4d  %4d    %4d' % ( i, j, k ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  i4lib_test ( )
  timestamp ( )

