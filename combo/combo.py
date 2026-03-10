#! /usr/bin/env python3
#
def combo_test ( ):

#*****************************************************************************80
#
## combo_test() tests combo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'combo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test combo().' )

  backtrack_test ( )

  bal_seq_check_test ( )
  bal_seq_enum_test ( )
  bal_seq_random_test ( rng )
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

  gray_code_check_test ( )
  gray_code_enum_test ( )
  gray_code_random_test ( rng )
  gray_code_rank_test ( )
  gray_code_successor_test ( )
  gray_code_unrank_test ( )

  i4_fall_test ( )
  i4_fall_values_test ( )
  i4_huge_test ( )

  i4mat_print_test ( );
  i4mat_print_some_test ( )

  i4vec_backtrack_test ( )
  i4vec_dot_product_test ( rng )
  i4vec_indicator1_test ( )
  i4vec_part1_test ( )
  i4vec_part2_test ( )
  i4vec_print_test ( )
  i4vec_reverse_test ( rng )
  i4vec_search_binary_a_test ( )
  i4vec_search_binary_d_test ( )
  i4vec_sort_insert_a_test ( rng )
  i4vec_sort_insert_d_test ( rng )

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
  ksubset_random_test ( rng )
  ksubset_revdoor_rank_test ( )
  ksubset_revdoor_successor_test ( )
  ksubset_revdoor_unrank_test ( )

  marriage_test ( )

  mountain_test ( )

  npart_enum_test ( )
  npart_rsf_lex_random_test ( rng )
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
  perm_parity_test ( rng )
  perm_print_test ( )
  perm_random_test ( rng )
  perm_tj_rank_test ( )
  perm_tj_successor_test ( )
  perm_tj_unrank_test ( )
  perm_to_cycle_test ( )

  pivot_sequence_check_test ( )
  pivot_sequence_enum_test ( )
  pivot_sequence_random_test ( rng )
  pivot_sequence_successor_test ( )

  pruefer_check_test ( )
  pruefer_enum_test ( )
  pruefer_random_test ( rng )
  pruefer_rank_test ( )
  pruefer_successor_test ( )
  pruefer_to_tree_test ( rng )
  pruefer_unrank_test ( )

  queens_test ( )

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
  subset_complement_test ( rng )
  subset_distance_test ( rng )
  subset_enum_test ( )
  subset_intersect_test ( rng )
  subset_lex_rank_test ( )
  subset_lex_successor_test ( )
  subset_lex_unrank_test ( )
  subset_random_test ( rng )
  subset_union_test ( rng )
  subset_weight_test ( rng )
  subset_xor_test ( rng )

  subset_sum_swap_test ( )

  tableau_check_test ( )
  tableau_enum_test ( )
  tableau_to_bal_seq_test ( )

  tree_check_test ( )
  tree_enum_test ( )
  tree_random_test ( rng )
  tree_rank_test ( )
  tree_successor_test ( )
  tree_to_pruefer_test ( rng )
  tree_unrank_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'combo_test():' )
  print ( '  Normal end of execution.' )
  return

def backtrack ( l, iarray, indx, k, nstack, stack, maxstack ):

#*****************************************************************************80
#
## backtrack() supervises a backtrack search.
#
#  Discussion:
#
#    The routine builds a vector, one element at a time, which is
#    required to satisfy some condition.
#
#    At any time, the partial vector may be discovered to be
#    unsatisfactory, but the routine records information about where the
#    last arbitrary choice was made, so that the search can be
#    carried out efficiently, rather than starting out all over again.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    Original FORTRAN77 version by Albert Nijenhuis, Herbert Wilf.
#    This version by John Burkardt.
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
#    integer L, the length of the completed candidate vector.
#
#    integer IARRAY(L), the candidate vector.
#
#    integer INDX, set INDX = 0 to start a search.
#
#    integer K, the current length of the candidate vector.
#
#    integer NSTACK, the current length of the stack.
#
#    integer STACK(MAXSTACK), a list of more candidates
#    for positions 1 through K.
#
#    integer MAXSTACK, the maximum length of the stack.
#
#  Output:
#
#    integer L, the length of the completed candidate vector.
#
#    integer IARRAY(L), the candidate vector.
#
#    integer INDX.
#    1, a complete output vector has been determined.
#    2, candidates are needed.
#    3, no more possible vectors exist.
#
#    integer K, the current length of the candidate vector.
#
#    integer NSTACK, the current length of the stack.
#
#    integer STACK(MAXSTACK), a list of more candidates
#    for positions 1 through K.
#

#
#  If this is the first call, request a candidate for position 1.
#
  if ( indx == 0 ):
    k = 1
    nstack = 0
    indx = 2
    return l, iarray, indx, k, nstack, stack
#
#  Examine the stack.
#
  while ( True ):

    nstack = nstack - 1
#
#  If there are candidates for position K, take the first available
#  one off the stack, and increment K.
#
#  This may cause K to reach the desired value of L, in which case
#  we need to signal the user that a complete set of candidates
#  is being returned.
#
    if ( stack[nstack+1-1] != 0 ):

      iarray[k-1] = stack[nstack-1]
      stack[nstack-1] = stack[nstack+1-1] - 1

      if ( k != l ):
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

  return l, iarray, indx, k, nstack, stack

def backtrack_test ( ):

#*****************************************************************************80
#
## backtrack_test() tests backtrack().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'backtrack_test():' )
  print ( '  backtrack() supervises a backtrack search.' )
  print ( '  We demonstrate by searching for a nonattacking arrangement' )
  print ( '  of queens on a chessboard.' )
  print ( '' )

  n = 8
  iarray = np.zeros ( n )
  indx = 0
  k = -1
  nstack = -1
  maxstack = n * n
  stack = np.zeros ( maxstack )

  while ( True ):

    n, iarray, indx, k, nstack, stack = backtrack ( n, iarray, \
      indx, k, nstack, stack, maxstack )

    if ( indx == 1 ):

      i4vec_transpose_print ( n, iarray, '' )

    elif ( indx == 2 ):

      nstack, stack = queens ( n, iarray, k, nstack, stack, maxstack )

    else:

      break

  return

def bal_seq_check ( n, t ):

#*****************************************************************************80
#
## bal_seq_check() checks a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    integer T(2*N), a balanced sequence.
#
#  Output:
#
#    bool CHECK, error flag.
#    TRUE, T is a legal balanced sequence.
#    FALSE, T is not a legal balanced sequence.
#
  check = True

  if ( n < 1 ):
    check = False
    return check

  one_count = 0
  zero_count = 0

  for i in range ( 0, 2 * n ):

    if ( t[i] == 0 ):
      zero_count = zero_count + 1
    elif ( t[i] == 1 ):
      one_count = one_count + 1
    else:
      check = False
      return check

    if ( zero_count < one_count ):
      check = False
      return check

  if ( one_count != zero_count ):
    check = False

  return check

def bal_seq_check_test ( ):

#*****************************************************************************80
#
## bal_seq_check_test() tests bal_seq_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bal_seq_check_test():' )
  print ( '  bal_seq_check() checks N and T(1:2*N).' )
  print ( '' )
  print ( '  Check?   N    T(1:2*N)' )
  print ( '' )
  
  for test in range ( 1, 4 ):

    n = 5

    if ( test == 1 ):
      t = np.array ( [ 0, 0, 1, 0, 1, 0, 0, 1, 1, 1 ] )
    elif ( test == 2 ):
      t = np.array ( [ 1, 1, 0, 1, 0, 1, 1, 0, 0, 0 ] )
    elif ( test == 3 ):
      t = np.array ( [ 0, 0, 1, 0, 1, 0, 0, 1, 0, 1 ] )

    check = bal_seq_check ( n, t )

    print ( '      %2d  %2d' % ( check, n ), end = '' )
    i4vec_transpose_print ( n, t, '' )

  return

def bal_seq_enum ( n ):

#*****************************************************************************80
#
## bal_seq_enum() enumerates the balanced sequences.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of 0's (and 1's) in the sequence.
#    N must be nonnegative.
#
#  Output:
#
#    integer NSEQ, the number of balanced sequences.
#
  from scipy.special import comb

  nseq = comb ( 2 * n, n ) / ( n + 1 )

  return nseq

def bal_seq_enum_test ( ):

#*****************************************************************************80
#
## bal_seq_enum_test() tests bal_seq_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bal_seq_enum_test():' )
  print ( '  bal_seq_enum() enumerates balanced sequences of N terms.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    nseq = bal_seq_enum ( n )
    print ( '  %2d  %6d' % ( n, nseq ) )

  return

def bal_seq_random ( n, rng ):

#*****************************************************************************80
#
## bal_seq_random() randomly selects a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N: the number of 0's (and 1's) in the sequence.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer T(2*N): a balanced sequence.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'bal_seq_random(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'bal_seq_random(): Fatal error!' )
#
#  Count the balanced sequences.
#
  bal_seq_num = bal_seq_enum ( n )
#
#  Choose RANK between 1 and BAL_SEQ_NUM.
#
  rank = rng.integers ( low = 1, high = bal_seq_num, endpoint = True )
#
#  Compute the balanced sequence of given rank.
#
  t = bal_seq_unrank ( rank, n )

  return t

def bal_seq_random_test ( rng ):

#*****************************************************************************80
#
## bal_seq_random_test() tests bal_seq_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bal_seq_random_test():' )
  print ( '  bal_seq_random() selects a random balanced sequence of N items.' )

  n = 5
  bal_seq_num = bal_seq_enum ( n )

  print ( '  Let n = ', n )
  print ( '  Number of possible balanced sequences is %', bal_seq_num )

  print ( '' )

  for test in range ( 0, 10 ):

    t = bal_seq_random ( n, rng )
    i4vec_transpose_print ( 2 * n, t, '' )

  return

def bal_seq_rank ( n, t ):

#*****************************************************************************80
#
## bal_seq_rank() ranks a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    integer T(2*N), a balanced sequence.
#
#  Output:
#
#    integer RANK, the rank of the balanced sequence.
#

#
#  Check.
#
  check = bal_seq_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'bal_seq_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'bal_seq_rank(): Fatal error!' )

  y = 0
  rank = 0

  for x in range ( 1, 2 * n ):

    if ( t[x-1] == 0 ):
      y = y + 1
    else:
      mxy = mountain ( n, x, y + 1 )
      rank = rank + mxy
      y = y - 1

  return rank

def bal_seq_rank_test ( ):

#*****************************************************************************80
#
## bal_seq_rank_test() tests bal_seq_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bal_seq_rank_test():' )
  print ( '  bal_seq_rank() ranks balanced sequences of N items.' )

  n = 5
  t = np.array ( [ 0, 0, 1, 0, 1, 1, 0, 0, 1, 1 ] )
  rank = bal_seq_rank ( n, t )

  print ( '' )
  print ( '  The element to be ranked is:' )
  i4vec_transpose_print ( 2 * n, t, '' )

  print ( '' )
  print ( '  Computed rank: %d' % ( rank ) )

  return

def bal_seq_successor ( n, t, rank ):

#*****************************************************************************80
#
## bal_seq_successor() computes the lexical balanced sequence successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    integer T(2*N), a balanced sequence.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(2*N), the lexical successor.
#
#    integer RANK, the rank of the output.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      t[i] = 0
    for i in range ( n, 2 * n ):
      t[i] = 1
    rank = 0
    return t, rank
#
#  Check.
#
  check = bal_seq_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'bal_seq_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'bal_seq_successor(): Fatal error!' )
#
#  After the I-th 0 there is a 'slot' with the capacity to
#  hold between 0 and I ones.
#
#  The first element of the sequence has all the 1's cowering
#  behind the N-th 0.
#
#  We seek to move a 1 to the left, and to do it lexically,
#  we will move a 1 to the rightmost slot that is under capacity.
#
#  Find the slot.
#
  slot = 0
  slot_index = 0
  slot_ones = 0

  open = 0
  open_index = 0

  for i in range ( 1, 2 * n + 1 ):

    if ( t[i-1] == 0 ):

      if ( 0 < slot ):
        if ( slot_ones < slot ):
          open = slot
          open_index = slot_index

      slot = slot + 1
      slot_index = i

    else:

      slot_ones = slot_ones + 1
#
#  If OPEN is not 0, then preserve the string up to the OPEN-th 0,
#  preserve the 1's that follow, but then write a 1, then
#  all the remaining 0's and all the remaining 1's.
#
  if ( open != 0 ):

    j = open_index + 1

    while ( t[j-1] == 1 ):
      j = j + 1

    t[j-1] = 1

    for i in range ( open + 1, n + 1 ):
      j = j + 1
      t[j-1] = 0

    for i in range ( j + 1, 2 * n + 1 ):
      t[i-1] = 1
#
#  If OPEN is 0, the last element was input.
#  Return the first one.
#
  else:

    for i in range ( 0, n ):
      t[i] = 0
    for i in range ( n, 2 * n ):
      t[i] = 1
    rank = 0
    return t, rank

  rank = rank + 1

  return t, rank

def bal_seq_successor_test ( ):

#*****************************************************************************80
#
## bal_seq_successor_test() tests bal_seq_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bal_seq_successor_test():' )
  print ( '  bal_seq_successor() lists balanced sequences of N items, one at a time.' )

  n = 5
  t = np.zeros ( 2 * n )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = bal_seq_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( 2 * n, t, '' )

  return

def bal_seq_to_tableau ( n, t ):

#*****************************************************************************80
#
## bal_seq_to_tableau() converts a balanced sequence to a 2 by N tableau.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    integer T(2*N), a balanced sequence.
#
#  Output:
#
#    integer TAB(2,N), a 2 by N tableau.
#
  import numpy as np
#
#  Check.
#
  check = bal_seq_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'bal_seq_to_tableau(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'bal_seq_to_tableau(): Fatal error!' )

  c = np.zeros ( 2, dtype = np.int32 )
  tab = np.zeros ( [ 2, n ], dtype = np.int32 )

  for i in range ( 0, 2 * n ):
    r = t[i] + 1
    c[r-1] = c[r-1] + 1
    tab[r-1,c[r-1]-1] = i + 1

  return tab

def bal_seq_to_tableau_test ( ):

#*****************************************************************************80
#
## bal_seq_to_tableau_test() tests bal_seq_to_tableau().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4

  print ( '' )
  print ( 'bal_seq_to_tableau_test():' )
  print ( '  bal_seq_to_tableau() converts a balanced' )
  print ( '  sequence to a tableau' )
#
#  Pick a "random" balanced sequence.
#
  rank = 7

  t = bal_seq_unrank ( rank, n )

  i4vec_transpose_print ( 2 * n, t, '  Balanced sequence:' )
#
#  Convert to a tableau.
#
  tab = bal_seq_to_tableau ( n, t )

  i4mat_print ( 2, n, tab, '  tableau:' )

  return

def bal_seq_unrank ( rank, n ):

#*****************************************************************************80
#
## bal_seq_unrank() unranks a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the balanced sequence.
#
#    integer N, the number of 0's (and 1's) in the sequence.
#
#  Output:
#
#    integer T(2*N), a balanced sequence.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'bal_seq_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'bal_seq_unrank(): Fatal error!' )

  nseq = bal_seq_enum ( n )

  if ( rank < 0 or nseq < rank ):
    print ( '' )
    print ( 'bal_seq_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'bal_seq_unrank(): Fatal error!' )

  y = 0
  low = 0

  t = np.zeros ( 2 * n, dtype = np.int32 )

  for x in range ( 1, 2 * n + 1 ):

    m = mountain ( n, x, y + 1 )

    if ( rank <= low + m - 1 ):
      y = y + 1
      t[x-1] = 0
    else:
      low = low + m
      y = y - 1
      t[x-1] = 1

  return t

def bal_seq_unrank_test ( ):

#*****************************************************************************80
#
## bal_seq_unrank_test() tests bal_seq_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bal_seq_unrank_test():' )
  print ( '  bal_seq_unrank() unranks a balanced sequence of N items.' )

  rank = 21
  n = 5

  t = bal_seq_unrank ( rank, n )

  print ( '' )
  print ( '  Rank = %d' % ( rank ) )
  print ( '' )
  print ( '  The element of that rank is:' )
  i4vec_transpose_print ( 2 * n, t, '' )

  return

def bell_numbers ( m ):

#*****************************************************************************80
#
## bell_numbers() computes the Bell numbers.
#
#  Discussion:
#
#    There are B(M) restricted growth functions of length M.
#
#    There are B(M) partitions of a set of M objects.
#
#    B(M) is the sum of the Stirling numbers of the second kind,
#    S(M,N), for N = 0 to M.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, indicates how many Bell numbers are to
#    compute.  M must be nonnegative.
#
#  Output:
#
#    integer B(1:M+1), the first M+1 Bell numbers.
#
  from scipy.special import comb
  import numpy as np

  b = np.zeros ( m + 1 )

  offset = 1

  b[0] = 1
  for j in range ( 1, m + 1 ):
    b[j] = 0
    for i in range ( 0, j ):
      b[j] = b[j] + comb ( j - 1, i ) * b[i]

  return b

def bell_numbers_test ( ):

#*****************************************************************************80
#
## bell_numbers_test() tests bell_numbers().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bell_numbers_test():' )
  print ( '  bell_numbers() computes Bell numbers.' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, bn = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    b = bell_numbers ( n )

    print ( '  %8d  %12d  %12d' % ( n, bn, b[n] ) )

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
#      B(N) = S^1_N + S^2_N + ... + S^N_N.
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
  print ( '  bell_values() returns values of the Bell numbers.' )
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

def cycle_check ( n, ncycle, t, index ):

#*****************************************************************************80
#
## cycle_check() checks a permutation in cycle form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of items permuted.
#    N must be positive.
#
#    integer NCYCLE, the number of cycles.
#    1 <= NCYCLE <= N.
#
#    integer T(N), INDEX(NCYCLE), describes the permutation
#    as a collection of NCYCLE cycles.
#
#  Output:
#
#    integer CHECK, error flag.
#    1, the data is legal.
#    0, the data is not legal.
#
  import numpy as np

  check = True
#
#  N must be at least 1.
#
  if ( n < 1 ):
    check = False
    return check
#
#  1 <= NCYCLE <= N.
#
  if ( ncycle < 1 or n < ncycle ):
    check = False
    return check
#
#  1 <= INDEX(I) <= N.
#
  for i in range ( 0, ncycle ):
    if ( index[i] < 1 or n < index[i] ):
      check = False
      return check
#
#  The INDEX values sum to N.
#
  if ( np.sum ( index ) != n ):
    check = False
    return check
#
#  1 <= T(I) <= N.
#
  for i in range ( 0, n ):
    if ( t[i] < 1 or n < t[i] ):
      check = 0
      return check
#
#  Verify that every value from 1 to N occurs in T.
#
  for iseek in range ( 1, n + 1 ):

    ifind = False

    for i in range ( 0, n ):
      if ( t[i] == iseek ):
        ifind = True
        break

    if ( not ifind ):
      check = False
      return check

  return check

def cycle_check_test ( ):

#*****************************************************************************80
#
## cycle_check_test() tests cycle_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'cycle_check_test():' )
  print ( '  cycle_check() checks a permutation in cycle form.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      n = 0
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 2 ):
      n = 8
      ncycle = 0
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 3 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 2 ] )
    elif ( test == 4 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 12, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 5 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 5, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 6 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )

    print ( '' )
    print ( '  Permutation in cycle form:' )
    print ( '  Number of cycles is %d' % ( ncycle ) )
    print ( '' )
    jlo = 0
    for i in range ( 0, ncycle ):
      print ( '    ', end = '' )
      for j in range ( jlo, jlo + index[i] ):
        print ( '%4d'% ( t[j] ), end = '' )
      print ( '' )
      jlo = jlo + index[i]

    check = cycle_check ( n, ncycle, t, index )
    print ( '  Check = %2d' % ( check ) )

  return

def cycle_to_perm ( n, ncycle, t, index ):

#*****************************************************************************80
#
## cycle_to_perm() converts a permutation from cycle to array form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of items permuted.
#    N must be positive.
#
#    integer NCYCLE, the number of cycles.
#    1 <= NCYCLE <= N.
#
#    integer T(N), INDEX(NCYCLE), describes the permutation
#    as a collection of NCYCLE cycles.  The first cycle is
#    T(1) -> T(2) -> ... -> T(INDEX(1)) -> T(1).
#
#  Output:
#
#    integer P(N), describes the permutation using a
#    single array.  For each index I, I -> P(I).
#
  import numpy as np
#
#  Check.
#
  check = cycle_check ( n, ncycle, t, index )

  if ( not check ):
    print ( '' )
    print ( 'cycle_to_perm(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'cycle_to_perm(): Fatal error!' )

  p = np.zeros ( n )

  jhi = 0

  for  i in range ( 0, ncycle  ):

    jlo = jhi + 1
    jhi = jhi + index[i]

    for j in range ( jlo, jhi + 1 ):

      if ( j < jhi ):
        p[t[j-1]-1] = t[j]
      else:
        p[t[j-1]-1] = t[jlo-1]

  return p

def cycle_to_perm_test ( ):

#*****************************************************************************80
#
## cycle_to_perm_test() tests cycle_to_perm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'cycle_to_perm_test():' )
  print ( '  cycle_to_perm() converts a permutation from' )
  print ( '  cycle to array form.' )

  n = 7
  ncycle = 3
  t = np.array ( [ 4, 2, 5, 3, 1, 6, 7 ] )
  index = np.array ( [ 5, 1, 1 ] )

  print ( '' )
  print ( '  Permutation in cycle form:' )
  print ( '  Number of cycles is %d' % ( ncycle ) )
  print ( '' )
  jlo = 0
  for i in range ( 0, ncycle ):
    print ( '    ', end = '' )
    for j in range ( jlo, jlo + index[i] ):
      print ( '%4d'% ( t[j] ), end = '' )
    print ( '' )
    jlo = jlo + index[i]

  p = cycle_to_perm ( n, ncycle, t, index )

  perm_print ( n, p, '  Corresponding permutation form:' )

  return

def dist_enum ( m, n ):

#*****************************************************************************80
#
## dist_enum() returns the number of distributions of indistinguishable objects.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of distinguishable "slots".
#
#    integer N, the number of indistinguishable objects.
#
#  Output:
#
#    integer dist_NUM, the number of distributions of N
#    indistinguishable objects about M distinguishable slots.
#
  from scipy.special import comb

  dist_num = comb ( m + n - 1, n )

  return dist_num

def dist_enum_test ( ):

#*****************************************************************************80
#
## dist_enum_test() tests dist_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'dist_enum_test():' )
  print ( '  dist_enum() enumerates distributions of N indistinguishable' )
  print ( '  objects among M distinguishable slots:' )
  print ( '' )
  print ( '      N:      0       1       2       3       4       5' )
  print ( '   M' )
  for m in range ( 0, 11 ):
    print ( '  %2d:  ' % ( m ), end = '' )
    for n in range ( 0, 6 ):
      print ( '  %5d' % ( dist_enum ( m, n ) ), end = '' )
    print ( '' )

  return

def dist_next ( k, m, q, leftmost, more ):

#*****************************************************************************80
#
## dist_next() returns the next distribution of indistinguishable objects.
#
#  Discussion:
#
#    A distribution of M objects into K parts is an ordered sequence
#    of K nonnegative integers which sum to M.  This is similar to
#    a partition of a set into K subsets, except that here the order
#    matters.  That is, (1,1,2) and (1,2,1) are considered to be
#    different distributions.
#
#    On the first call to this routine, the user should set MORE = FALSE,
#    to signal that this is a startup for the given computation.  The routine
#    will return the first distribution, and set MORE = TRUE.
#
#    If the user calls again, with MORE = TRUE, the next distribution
#    is being requested.  If the routine returns with MORE = TRUE, then
#    that distribution was found and returned.  However, if the routine
#    returns with MORE = FALSE, then no more distributions were found
#    and the enumeration of distributions has finished.
#
#    A "distribution of M indistinguishable objects into K slots" is
#    sometimes called a "composition of the integer M into K parts".
#
#  Example:
#
#    K = 3, M = 5
#
#    0           0           5
#    0           1           4
#    0           2           3
#    0           3           2
#    0           4           1
#    0           5           0
#    1           0           4
#    1           1           3
#    1           2           2
#    1           3           1
#    1           4           0
#    2           0           3
#    2           1           2
#    2           2           1
#    2           3           0
#    3           0           2
#    3           1           1
#    3           2           0
#    4           0           1
#    4           1           0
#    5           0           0
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
#  Reference:
#
#    Robert Fenichel,
#    Algorithm 329:
#    Distribution of Indistinguishable Objects into
#    Distinguishable Slots,
#    Communications of the ACM,
#    Volume 11, Number 6, June 1968, page 430.
#
#  Input:
#
#    integer K, the number of distinguishable "slots".
#
#    integer M, the number of indistinguishable objects.
#
#    integer Q(K), the number of objects in each slot.
#
#    integer LEFTMOST, used to speed up the computation.
#    On first call, set LEFTMOST to 0.
#
#    logical MORE, used by the user to start the computation.
#
#  Output:
#
#    integer Q(K), the number of objects in each slot.
#
#    integer LEFTMOST, used to speed up the computation.
#
#    logical MORE, used by the routine to stop the computation.
#
  import numpy as np
#
#  The startup call.
#
  if ( not more ):

    more = True

    q = np.zeros ( k )
    q[k-1] = m

    leftmost = k
#
#  There are no more distributions.
#  Reset Q to the first distribution in the sequence.
#
  elif ( q[0] == m ):

    more = False

    q = np.zeros ( k )
    q[k-1] = m

    leftmost = k

  elif ( leftmost < k ):

    leftmost = leftmost - 1
    q[k-1] = q[leftmost] - 1
    q[leftmost] = 0
    q[leftmost-1] = q[leftmost-1] + 1
    if ( q[k-1] != 0 ):
      leftmost = k

  else:

    if ( q[k-1] == 1 ):
      leftmost = k - 1

    q[k-1] = q[k-1] - 1
    q[k-2] = q[k-2] + 1

  return q, leftmost, more

def dist_next_test ( ):

#*****************************************************************************80
#
## dist_next_test() tests dist_next().
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
  import numpy as np

  k = 3
  m = 5
  q = np.array ( [] )
  leftmost = 0
  more = False

  print ( '' )
  print ( 'dist_next_test():' )
  print ( '  dist_next() produces the "next" distribution of M' )
  print ( '  indistinguishable objects among K distinguishable slots:' )
  print ( '' )
  print ( '  Number of:' )
  print ( '    indistinguishable objects = %d' % ( m ) )
  print ( '    distinguishable slots =     %d' % ( k ) )
  print ( '    distributions is            %d' % ( dist_enum ( k, m ) ) )
  print ( '' )

  idist = 0

  while ( True ):

    q, leftmost, more = dist_next ( k, m, q, leftmost, more )

    if ( not more ):
      break

    idist = idist + 1
    print ( '    %5d: ' % ( idist ), end = '' )
    for i in range ( 0, k ):
      print ( '%5d' % ( q[i] ), end = '' )
    print ( '' )

  return

def edge_check ( n_node, n_edge, t ):

#*****************************************************************************80
#
## edge_check() checks a graph stored by edges.
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
#    integer  N_NODE, the number of nodes in the graph.
#
#    integer N_EDGE, the number of edges in the graph.
#
#    integer T(2,N_EDGE), describes the edges of the tree
#    as pairs of nodes.
#
#  Output:
#
#    integer CHECK
#    1, the data is legal.
#    0, the data is not legal. 
#
  check = True

  if ( n_node < 0 ):
    check = False
    return check

  if ( n_edge < 0 ):
    check = False
    return check
#
#  Every edge must join two legal nodes.
#
  for i in range ( 0, 2 ):
    for j in range ( 0, n_edge ):
      if ( t[i,j] < 1 or n_node < t[i,j] ):
        check = False
        return check
#
#  Every edge must join distinct nodes.
#
  for j in range ( 0, n_edge ):
    if ( t[0,j] == t[1,j] ):
      check = False
      return check
#
#  Every edge must be distinct.
#
  for j in range ( 0, n_edge - 1 ):
    for j2 in range ( j + 1, n_edge ):
      if ( t[0,j] == t[0,j2] and t[1,j] == t[1,j2] ):
        check = False
        return check
      elif ( t[0,j] == t[1,j2] and t[1,j] == t[0,j2] ):
        check = False
        return check

  return check

def edge_check_test ( ):

#*****************************************************************************80
#
## edge_check_test() tests edge_check().
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
  import numpy as np

  print ( '' )
  print ( 'edge_check_test():' )
  print ( '  edge_check() checks a graph described by edges.' )
  print ( '' )
  print ( '  Check?  Nodes  Edges    EdgeList' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      node_num = -5
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 1 ] ] )
    elif ( test == 2 ):
      node_num = 3
      edge_num = -1
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 1 ] ] )
    elif ( test == 3 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 4 ] ] )
    elif ( test == 4 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 2, 1 ] ] )
    elif ( test == 5 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 2 ], \
        [ 2, 3, 1 ] ] )
    elif ( test == 6 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 1 ] ] )

    print ( '' )
    check = edge_check ( node_num, edge_num, edge_list )
    print ( '      %2d     %2d     %2d' % ( check, node_num, edge_num ) )
    i4mat_print ( 2, edge_num, edge_list, '  Edge list of graph:' )

  return

def edge_degree ( n_node, n_edge, t ):

#*****************************************************************************80
#
## edge_degree() returns the degree of the nodes of a graph stored by edges.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N_NODE, the number of nodes in the graph.
#    N_NODE must be positive.
#
#    integer N_EDGE, the number of edges in the graph.
#    N_EDGE must be positive.
#
#    integer T(2,N_EDGE), describes the edges of the tree
#    as pairs of nodes.
#
#  Output:
#
#    integer D(N_NODE), the degree of each node.
#
  import numpy as np
#
#  Check.
#
  check = edge_check ( n_node, n_edge, t )

  if ( not check ):
    print ( '' )
    print ( 'edge_degree(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'edge_degree(): Fatal error!' )
#
#  Compute the degree of each node.
#
  d = np.zeros ( n_node )

  for j in range ( 0, n_edge ):
    d[t[0,j]-1] = d[t[0,j]-1] + 1;
    d[t[1,j]-1] = d[t[1,j]-1] + 1;

  return d

def edge_degree_test ( ):

#*****************************************************************************80
#
## edge_degree_test() tests edge_degree().
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
  import numpy as np

  print ( '' )
  print ( 'edge_degree_test():' )
  print ( '  edge_degree() determines the degree of each node in a graph.' )

  node_num = 5
  edge_num = 5
  edge = np.array ( [ \
    [ 1, 2, 2, 3, 4 ], \
    [ 2, 3, 4, 4, 5 ] ] )

  i4mat_print ( 2, edge_num, edge, '  The edge array:' )

  d = edge_degree ( node_num, edge_num, edge );

  i4vec_print ( node_num, d, '  The degree vector:' );

  return

def edge_enum ( node_num ):

#*****************************************************************************80
#
## edge_enum() enumerates the maximum number of edges in a graph on NODE_NUM nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NODE_NUM, the number of nodes in the graph.
#    N_NODE must be positive.
#
#  Output:
#
#    integer edge_NUM, the maximum number of edges in a graph
#    on N_NODE nodes.
#
  edge_num = ( node_num * ( node_num - 1 ) ) / 2

  return edge_num

def edge_enum_test ( ):

#*****************************************************************************80
#
## edge_enum_test() tests edge_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'edge_enum_test():' )
  print ( '  edge_enum() enumerates the maximum number of edges' )
  print ( '  possible in a graph of NODE_NUM nodes.' )
  print ( '' )
  print ( '   NODE_NUM    edge_NUM(max)' )
  print ( '' )

  for node_num in range ( 1, 11 ):
    edge_num = edge_enum ( node_num )
    print ( '         %2d      %6d' % ( node_num, edge_num ) )

  return

def gray_code_check ( n, t ):

#*****************************************************************************80
#
## gray_code_check() checks a Gray code element.
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
#    integer N, the number of digits in each element.
#    N must be positive.
#
#    integer T(N), an element of the Gray code.
#    Each entry T(I) is either 0 or 1.
#
#  Output:
#
#    bool CHECK, error flag.
#    True, T represents a Gray code.
#    False, T does not represent a Gray code.
#
  check = True

  if ( n < 1 ):
    check = False
    return check

  for i in range ( 0, n ):

    if ( t[i] != 0 and t[i] != 1 ):
      check = False
      return check

  return check

def gray_code_check_test ( ):

#*****************************************************************************80
#
## gray_code_check_test() tests gray_code_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gray_code_check_test():' )
  print ( '  gray_code_check() checks N and T(1:N).' )
  print ( '' )
  print ( '  Check?      N    T(1:N)' )
  print ( '' )
  
  for test in range ( 1, 4 ):

    n = 5

    if ( test == 1 ):
      t = np.array ( [ 0, 1, 1, 0, 1 ] )
    elif ( test == 2 ):
      t = np.array ( [ 1, 0, 7, 1, 0 ] )
    elif ( test == 3 ):
      t = np.array ( [ 1, 1, 1, 1, 1 ] )

    check = gray_code_check ( n, t )
    print ( '      %5s  %2d:  ' % ( check, n ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( t[i] ), end = '' )
    print ( '' )

  return

def gray_code_enum ( n ):

#*****************************************************************************80
#
## gray_code_enum() enumerates the Gray codes on N digits.
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
#  Input:
#
#    integer N, the number of digits in each element.
#    N must be nonnegative.
#
#  Output:
#
#    integer NGRAY, the number of distinct elements.
#
  ngray = 2 ** n

  return ngray

def gray_code_enum_test ( ):

#*****************************************************************************80
#
## gray_code_enum_test() tests gray_code_enum().
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
  n = 5

  print ( '' )
  print ( 'gray_code_enum_test():' )
  print ( '  gray_code_enum() enumerates Gray codes on N elements.' )
  print ( '' )
  print ( '   N    Enum(N)' )
  print ( '' )

  for n in range ( 0, 11 ):
    ngray = gray_code_enum ( n );
    print ( '  %2d  %6d' % ( n, ngray ) )

  return

def gray_code_random ( n, rng ):

#*****************************************************************************80
#
## gray_code_random() returns a random Gray code of N digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of digits in each element.
#    N must be positive.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer T(N), the random Gray code.
#
  t = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

  return t

def gray_code_random_test ( rng ):

#*****************************************************************************80
#
## gray_code_random_test() tests gray_code_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gray_code_random_test():' )
  print ( '  gray_code_random() returns a random Gray code of N digits.' )

  n = 6

  for i in range ( 0, 10 ):
    t = gray_code_random ( n, rng )
    print ( t )

  return

def gray_code_rank ( n, t ):

#*****************************************************************************80
#
## gray_code_rank() computes the rank of a Gray code element.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of digits in each element.
#    N must be positive.
#
#    integer T(N), an element of the Gray code.
#    Each entry T(I) is either 0 or 1.
#
#  Output:
#
#    integer RANK, the rank of the element.
#

#
#  Check.
#
  check = gray_code_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'gray_code_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'gray_code_rank(): Fatal error!' )

  rank = 0
  b = 0

  for i in range ( n - 1, -1, -1 ):

    if ( t[n-1-i] != 0 ):
      b = 1 - b

    if ( b == 1 ):
      rank = rank + 2 ** i

  return rank

def gray_code_rank_test ( ):

#*****************************************************************************80
#
## gray_code_rank_test() tests gray_code_rank().
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

  print ( '' )
  print ( 'gray_code_rank_test():' )
  print ( '  gray_code_rank() ranks a given Gray code.' )

  n = 5
  t = np.array ( [ 1, 1, 0, 0, 0 ] )

  rank = gray_code_rank ( n, t )

  i4vec_print ( n, t, '  Element to be ranked:' )

  print ( '' )
  print ( '  Computed rank: %d' % ( rank ) )

  return

def gray_code_successor ( n, t, rank ):

#*****************************************************************************80
#
## gray_code_successor() computes the binary reflected Gray code successor.
#
#  Example:
#
#    000, 001, 011, 010, 110, 111, 101, 100,
#    after which the sequence repeats.
#
#  Discussion:
#
#    In the original code, the successor of the element that has an
#    initial 1 followed by N-1 zeroes is undefined.  In this version,
#    the successor is the element with N zeroes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of digits in each element.
#    N must be positive.
#
#    integer T(N), T contains an element of the Gray code, that is,
#    each entry T(I) is either 0 or 1.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(N), T contains the successor to the input value this
#    is an element of the Gray code, which differs from the input
#    value in a single position.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  import numpy as np
#
#  Return the first element.
#
  if ( rank == -1 ):

    t = np.zeros ( n )
    rank = 0
    return t, rank
#
#  Check.
#
  check = gray_code_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'gray_code_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'gray_code_successor(): Fatal error!' )

  weight = np.sum ( t )

  if ( ( weight % 2 ) == 0 ):

    if ( t[n-1] == 0 ):
      t[n-1] = 1
    else:
      t[n-1] = 0

    rank = rank + 1
    return t, rank

  else:

    for i in range ( n - 1, 0, -1 ):
      if ( t[i] == 1 ):
        if ( t[i-1] == 0 ):
          t[i-1] = 1
        else:
          t[i-1] = 0
        rank = rank + 1
        return t, rank
#
#  The final element was input.
#  Return the first element.
#
    t = np.zeros ( n )
    rank = 0

  return t, rank

def gray_code_successor_test ( ):

#*****************************************************************************80
#
## gray_code_successor_test() tests gray_code_successor().
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

  print ( '' )
  print ( 'gray_code_successor_test():' )
  print ( '  gray_code_successor() returns the next Gray code.' )

  n = 5
  t = np.zeros ( n )
  rank = -1

  print ( '' )
  while ( True ):

    rank_old = rank

    t, rank = gray_code_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    print ( '    %4d:  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( t[i] ), end = '' )
    print ( '' )

  return

def gray_code_unrank ( rank, n ):

#*****************************************************************************80
#
## gray_code_unrank() computes the Gray code element of given rank.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the element.
#    0 <= RANK <= 2^N.
#
#    integer N, the number of digits in each element.
#    N must be positive.
#
#  Output:
#
#    integer T(N), the element of the Gray code which has
#    the given rank.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'gray_code_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'gray_code_rank(): Fatal error!' )

  ngray = gray_code_enum ( n )

  if ( rank < 0 or ngray < rank ):
    print ( '' )
    print ( 'gray_code_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'gray_code_rank(): Fatal error!' )

  rank_copy = rank
  t = np.zeros ( n )
  bprime = 0

  for i in range ( n - 1, -1, -1 ): 

    b = ( rank_copy // ( 2 ** i ) )

    if ( b != bprime ):
      t[n-1-i] = 1

    bprime = b
    rank_copy = rank_copy - b * ( 2 ** i )

  return t

def gray_code_unrank_test ( ):

#*****************************************************************************80
#
## gray_code_unrank_test() tests gray_code_unrank().
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
  print ( '' )
  print ( 'gray_code_unrank_test():' )
  print ( '  gray_code_unrank() unranks a Gray code.' )

  n = 5
  ngray = gray_code_enum ( n )

  rank = ( ngray // 2 )

  print ( '' )
  print ( '  Seek the element of rank %d' % ( rank ) )

  t = gray_code_unrank ( rank, n )

  i4vec_print ( n, t, '  The item of the given rank' )

  return

def i4_fall ( x, n ):

#*****************************************************************************80
#
## i4_fall() computes the falling factorial function [X]_N.
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
#    integer VALUE, the dot product of X and Y.
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

def i4vec_part1 ( n, npart ):

#*****************************************************************************80
#
## i4vec_part1() partitions an integer N into NPART parts.
#
#  Example:
#
#    Input:
#
#      N = 17, NPART = 5
#
#    Output:
#
#      X = ( 13, 1, 1, 1, 1 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be partitioned.  N
#    may be positive, zero, or negative.
#
#    integer NPART, the number of entries in the array.
#    1 <= NPART <= N.
#
#  Output:
#
#    integer X(NPART), the partition of N.  The entries of
#    X add up to N.  X(1) = N + 1 - NPART, and all other entries
#    are equal to 1.
#
  import numpy as np

  if ( npart < 1 or n < npart ):
    print ( '' )
    print ( 'i4vec_part1(): Fatal error!' )
    print ( '  The input value of NPART is illegal.' )
    raise Exception ( 'i4vec_part1(): Fatal error!' )

  x = np.ones ( npart )

  x[0] = n + 1 - npart

  return x

def i4vec_part1_test ( ):

#*****************************************************************************80
#
## i4vec_part1_test() tests i4vec_part1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4vec_part1_test():' )
  print ( '  i4vec_part1() partitions an integer N into NPART parts.' )

  n = 17
  npart = 5

  print ( '' )
  print ( '  Partition N = %d into NPART = %d parts:' % ( n, npart ) )
  print ( '' )

  x = i4vec_part1 ( n, npart )

  for i in range ( 0, npart ):
    print ( '  %2d  %2d' % ( i, x[i] ) )

  return

def i4vec_part2 ( n, npart ):

#*****************************************************************************80
#
## i4vec_part2() partitions an integer N into NPART nearly equal parts.
#
#  Example:
#
#    Input:
#
#      N = 17, NPART = 5
#
#    Output:
#
#      X = ( 4, 4, 3, 3, 3 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be partitioned.  N
#    may be positive, zero, or negative.
#
#    integer NPART, the number of entries in the array.
#    1 <= NPART
#
#  Output:
#
#    integer X(NPART), the partition of N.  The entries of
#    X add up to N.  The entries of X are either all equal, or
#    differ by at most 1.  The entries of X all have the same sign
#    as N, and the "largest" entries occur first.
#
  import numpy as np

  if ( npart < 1 ):
    print ( '' )
    print ( 'i4vec_part2(): Fatal error!' )
    print ( '  The input value of NPART is illegal.' )
    raise Exception ( 'i4vec_part2(): Fatal error!' )

  x = np.zeros ( npart )

  if ( 0 < n ):

    j = 0
    for i in range ( 0, n ):
      x[j] = x[j] + 1
      j = j + 1
      if ( npart <= j ):
        j = 0

  elif ( n < 0 ):

    j = 0
    for i in range ( n - 1, -1, -1 ):
      x[j] = x[j] - 1
      j = j + 1
      if ( npart <= j ):
        j = 0

  return x

def i4vec_part2_test ( ):

#*****************************************************************************80
#
## i4vec_part2_test() tests i4vec_part2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4vec_part2_test():' )
  print ( '  i4vec_part2() partitions an integer N into NPART parts.' )

  n = 17
  npart = 5

  print ( '' )
  print ( '  Partition N = %d into NPART = %d parts:' % ( n, npart ) )
  print ( '' )

  x = i4vec_part2 ( n, npart )

  for i in range ( 0, npart ):
    print ( '  %2d  %2d' % ( i, x[i] ) )

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
  import numpy as np

  n = 10
  b = 0
  c = 3 * n

  print ( '' )
  print ( 'i4vec_reverse_test()' )
  print ( '  i4vec_reverse() reverses a list of integers.' )

  a = rng.integers ( low = b, high = c, size = n, endpoint = True )

  i4vec_print ( n, a, '  Original vector:' )

  a = i4vec_reverse ( n, a )

  i4vec_print ( n, a, '  Reversed:' )

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

def knapsack_01 ( n, mass_limit, p, w ):

#*****************************************************************************80
#
## knapsack_01() solves the 0/1 knapsack problem.
#
#  Discussion:
#
#    The 0/1 knapsack problem is as follows:
#
#      Given:
#        a set of N objects,
#        a profit P(I) and weight W(I) associated with each object,
#        and a weight limit MASS_LIMIT,
#      Determine:
#        a set of choices X(I) which are 0 or 1, that maximizes the profit
#          P = Sum ( 1 <= I <= N ) P(I) * X(I)
#        subject to the constraint
#          Sum ( 1 <= I <= N ) W(I) * X(I) <= MASS_LIMIT.
#
#    This routine assumes that the objects have already been sorted
#    in order of decreasing "profit density", P(I)/W(I).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of objects.
#
#    real MASS_LIMIT, the weight limit of the
#    chosen objects.
#
#    real P(N), the "profit" or value of each object.
#    P is assumed to be nonnegative.
#
#    real W(N), the "weight" or cost of each object.
#    W is assumed to be  nonnegative.
#
#  Output:
#
#    real X(N), the choice function for the objects.
#    0, the object was not taken.
#    1, the object was taken.
#
#    real MASS, the total mass of the objects taken.
#
#    real PROFIT, the total profit of the objects taken.
#
  import numpy as np
#
#  Initialize the "best so far" data.
#
  x_best = np.zeros ( n )
  profit_best = 0.0
  mass_best = 0
#
#  Begin the backtracking solution.
#
  maxstack = 100
  stacks = np.zeros ( maxstack )
  x = np.zeros ( n )
  indx = 0
  k = 1
  nstack = 0
  ncan = np.zeros ( n )

  while ( True ):

    x, indx, k, nstack, stacks, ncan = r8vec_backtrack ( n, maxstack, x, indx, k, \
      nstack, stacks, ncan )
#
#  Got a new candidate.  Compare it to the best so far.
#
    if ( indx == 1 ):

      profit = np.dot ( p, x )
      mass = np.dot ( w, x )

      if ( profit_best < profit or \
         ( profit == profit_best and mass < mass_best ) ):
        profit_best = profit
        mass_best = mass
        for i in range ( 0, n ):
          x_best[i] = x[i]
#
#  Need candidates for X(K).
#
#  X(K) = 1 is possible if:
#
#    * adding W(K) to our mass doesn't put us over our mass limit
#    * and adding P(K) to our current profit, and taking the best we
#      could get using rational X for the remainder would put us over
#      our current best.
#
#  X(K) = 0 is always possible.
#
    elif ( indx == 2 ):

      ncan[k-1] = 0

      mass_1 = w[k-1]
      for i in range ( 0, k - 1 ):
        mass_1 = mass_1 + w[i] * x[i]

      if ( mass_1 <= mass_limit ):

        mass_remaining = mass_limit - mass_1

        profit_1 = p[k-1]
        for i in range ( 0, k - 1 ):
          profit_1 = profit_1 + p[i] * x[i]

        if ( k < n ):

          ptemp = np.zeros ( n - k )
          for i in range ( k, n ):
            ptemp[i-k] = p[i]
          wtemp = np.zeros ( n - k )
          for i in range ( k, n ):
            wtemp[i-k] = w[i]

          xtemp, mass_2, profit_2 = knapsack_rational ( n - k, \
            mass_remaining, ptemp, wtemp )

          for i in range ( k, n ):
            x[i] = xtemp[i-k]

        else:

          profit_2 = 0.0

        if ( profit_best < profit_1 + profit_2 ):

          if ( maxstack <= nstack ):
            print ( '' )
            print ( 'knapsack_01(): Fatal error!' )
            print ( '  Exceeded stack space.' )
            raise Exception ( 'knapsack_01(): Fatal error!' )
 
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1.0

      if ( maxstack <= nstack ):
        print ( '' )
        print ( 'knapsack_01(): Fatal error!' )
        print ( '  Exceeded stack space.' )
        raise Exception ( 'knapsack_01(): Fatal error!' )

      ncan[k-1] = ncan[k-1] + 1
      nstack = nstack + 1
      stacks[nstack-1] = 0.0
#
#  Done.  Return the best solution.
#
    else:

      profit = profit_best
      mass = mass_best
      for i in range ( 0, n ):
        x[i] = x_best[i]
      break

  return x, mass, profit

def knapsack_01_test ( ):

#*****************************************************************************80
#
## knapsack_01_test() tests knapsack_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  mass_limit = 26.0
  p = np.array ( [ 24.0, 13.0, 23.0, 15.0, 16.0 ] )
  w = np.array ( [ 12.0,  7.0, 11.0,  8.0,  9.0 ] )

  print ( '' )
  print ( 'knapsack_01_test():' )
  print ( '  knapsack_01() solves the 0/1 knapsack problem.' )

  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  p, w = knapsack_reorder ( n, p, w )

  print ( '' )
  print ( '  After reordering by Profit Density:' )
  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  print ( '' )
  print ( '  Total mass restriction is %f' % ( mass_limit ) )

  x, mass, profit = knapsack_01 ( n, mass_limit, p, w )

  print ( '' )
  print ( '  Object, Density, Choice, Profit, Mass' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %7.3f  %7.3f  %7.3f  %7.3f' \
      % ( i, p[i] / w[i], x[i],  x[i] * p[i], x[i] * w[i] ) )

  print ( '' )
  print ( '  Total:                  %7.3f  %7.3f' % ( profit, mass ) )

  return

def knapsack_rational ( n, mass_limit, p, w ):

#*****************************************************************************80
#
## knapsack_rational() solves the rational knapsack problem.
#
#  Discussion:
#
#    The rational knapsack problem is a generalization of the 0/1 knapsack
#    problem.  It is mainly used to derive a bounding function for the
#    0/1 knapsack problem.
#
#    The 0/1 knapsack problem is as follows:
#
#      Given:
#        a set of N objects,
#        a profit P(I) and weight W(I) associated with each object,
#        and a weight limit MASS_LIMIT,
#      Determine:
#        a set of choices X(I) which are 0 or 1, that maximizes the profit
#          P = Sum ( 1 <= I <= N ) P(I) * X(I)
#        subject to the constraint
#          Sum ( 1 <= I <= N ) W(I) * X(I) <= MASS_LIMIT.
#
#    By contrast, the rational knapsack problem allows the values X(I)
#    to be any value between 0 and 1.  A solution for the rational knapsack
#    problem is known.  Arrange the objects in order of their "profit density"
#    ratios P(I)/W(I), and then take in order as many of these as you can.
#    If you still have "room" in the weight constraint, then you should
#    take the maximal fraction of the very next object, which will complete
#    your weight limit, and maximize your profit.
#
#    If should be obvious that, given the same data, a solution for
#    the rational knapsack problem will always have a profit that is
#    at least as high as for the 0/1 problem.  Since the rational knapsack
#    maximum profit is easily computed, this makes it a useful bounding
#    function.
#
#    Note that this routine assumes that the objects have already been
#    arranged in order of the "profit density".
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of objects.
#
#    real MASS_LIMIT, the weight limit of the
#    chosen objects.
#
#    real P(N), the "profit" or value of each object.
#    The entries of P are assumed to be nonnegative.
#
#    real W(N), the "weight" or cost of each object.
#    The entries of W are assumed to be nonnegative.
#
#  Output:
#
#    real X(N), the choice function for the objects.
#    0.0, the object was not taken.
#    1.0, the object was taken.
#    R, where 0 < R < 1, a fractional amount of the object was taken.
#
#    real MASS, the total mass of the objects taken.
#
#    real PROFIT, the total profit of the objects taken.
#
  import numpy as np

  x = np.zeros ( n )
  mass = 0.0
  profit = 0.0

  for i in range ( 0, n ):

    if ( mass_limit <= mass ):
      x[i] = 0.0
    elif ( mass + w[i] <= mass_limit ):
      x[i] = 1.0
      mass = mass + w[i]
      profit = profit + p[i]
    else:
      x[i] = ( mass_limit - mass ) / w[i]
      mass = mass_limit
      profit = profit + p[i] * x[i]

  return x, mass, profit

def knapsack_rational_test ( ):

#*****************************************************************************80
#
## knapsack_rational_test() tests knapsack_rational().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2011
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  mass_limit = 26.0
  p = np.array ( [ 24.0, 13.0, 23.0, 15.0, 16.0 ] )
  w = np.array ( [ 12.0,  7.0, 11.0,  8.0,  9.0 ] )

  print ( '' )
  print ( 'knapsack_rational_test():' )
  print ( '  knapsack_rational() solves the rational knapsack problem.' )

  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  p, w = knapsack_reorder ( n, p, w )

  print ( '' )
  print ( '  After reordering by Profit Density:' )
  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  print ( '' )
  print ( '  Total mass restriction is %f' % ( mass_limit ) )

  x, mass, profit = knapsack_rational ( n, mass_limit, p, w  )

  print ( '' )
  print ( '  Object, Density, Choice, Profit, Mass' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %7.3f  %7.3f  %7.3f  %7.3f' \
      % ( i, p[i] / w[i], x[i], x[i] * p[i], x[i] * w[i] ) )

  print ( '' )
  print ( '  Total:                  %7.3f  %7.3f' % ( profit, mass ) )

  return

def knapsack_reorder ( n, p, w ):

#*****************************************************************************80
#
## knapsack_reorder() reorders the knapsack data by "profit density".
#
#  Discussion:
#
#    This routine must be called to rearrange the data before calling
#    routines that handle a knapsack problem.
#
#    The "profit density" for object I is defined as P(I)/W(I).
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of objects.
#
#    real P(N), the "profit" or value of each object.
#
#    real W(N), the "weight" or cost of each object.
#
#  Output:
#
#    real P(N), the reordered "profit" or value of each object.
#
#    real W(N), the reordered "weight" or cost of each object.
#

#
#  Rearrange the objects in order of "profit density".
#
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):

      if ( p[i] * w[j] < p[j] * w[i] ):

        t    = p[i]
        p[i] = p[j]
        p[j] = t

        t    = w[i]
        w[i] = w[j]
        w[j] = t

  return p, w

def knapsack_reorder_test ( ):

#*****************************************************************************80
#
## knapsack_reorder_test() tests knapsack_reorder().
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
  import numpy as np

  n = 5
  p = np.array ( [ 24.0, 13.0, 23.0, 15.0, 16.0 ] )
  w = np.array ( [ 12.0,  7.0, 11.0,  8.0,  9.0 ] )

  print ( '' )
  print ( 'knapsack_reorder_test():' )
  print ( '  knapsack_reorder() reorders knapsack data.' )

  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  p, w = knapsack_reorder ( n, p, w )

  print ( '' )
  print ( '  After reordering by Profit Density:' )
  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  return

def ksubset_colex_check ( k, n, t ):

#*****************************************************************************80
#
## ksubset_colex_check() checks a K subset in colex form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have. 0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    0 <= N.
#
#    integer T(K), describes a K subset.  T(I) is the I-th
#    element of the K subset.  The elements must be listed in
#    DESCENDING order.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 0 ):
    check = False
    return check

  if ( k < 0 or n < k ):
    check = False
    return check
#
#  Check that entries are in descending order, and between 1 and N.
#
  tmax = n + 1

  for i in range ( 0, k ):

    if ( t[i] <= 0 or tmax <= t[i] ):
      check = False
      return check

    tmax = t[i]

  return check

def ksubset_colex_check_test ( ):

#*****************************************************************************80
#
## ksubset_colex_check_test() tests ksubset_colex_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ksubset_colex_check_test():' )
  print ( '  ksubset_colex_check() checks a K subset of an N set.' )
  
  for test in range ( 1, 8 ):

    if ( test == 1 ):
      k = -1
      n = 5
      s = np.array ( [ ] )
    elif ( test == 2 ):
      k = 3
      n = 0
      s = np.array ( [ 5, 3, 2 ] )
    elif ( test == 3 ):
      k = 3
      n = 5
      s = np.array ( [ 5, 2, 3 ] )
    elif ( test == 4 ):
      k = 3
      n = 5
      s = np.array ( [ 7, 3, 2 ] )
    elif ( test == 5 ):
      k = 3
      n = 5
      s = np.array ( [ 5, 3, 2 ] )
    elif ( test == 6 ):
      k = 0
      n = 5
      s = np.array ( [ ] )
    elif ( test == 7 ):
      k = 0
      n = 0
      s = np.array ( [ ] )

    check = ksubset_colex_check ( k, n, s )
    i4vec_transpose_print ( k, s, '  Subset:' )
    print ( '  N = %d, K = %d' % ( n, k ) )
    print ( '  Check = %s' %  ( check ) )

  return

def ksubset_colex_rank ( k, n, t ):

#*****************************************************************************80
#
## ksubset_colex_rank() computes the colex rank of a K subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(K), describes a K subset.  T(I) is the I-th
#    element of the K subset.  The elements must be listed in DESCENDING order.
#
#  Output:
#
#    integer RANK, the rank of the subset.
#
  from scipy.special import comb
#
#  Check.
#
  check = ksubset_colex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'ksubset_colex_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'ksubset_colex_rank(): Fatal error!' )

  rank = 0

  for i in range ( 0, k ):
    rank = rank + comb ( t[i] - 1, k - i )

  return rank

def ksubset_colex_rank_test ( ):

#*****************************************************************************80
#
## ksubset_colex_rank_test() tests ksubset_colex_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5
  t = np.array ( [ 5, 3, 1 ] )

  print ( '' )
  print ( 'ksubset_colex_rank_test():' )
  print ( '  ksubset_colex_rank() ranks K-subsets of an N set,' )
  print ( '  using the colexicographic ordering.' )

  i4vec_transpose_print ( k, t, '  The element to be ranked:' )

  rank = ksubset_colex_rank ( k, n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d.' % ( rank ) )

  return

def ksubset_colex_successor ( k, n, t, rank ):

#*****************************************************************************80
#
## ksubset_colex_successor() computes the K subset colex successor.
#
#  Discussion:
#
#    In the original code, there is a last element with no successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(K), describes a K subset.  T(I) is the
#    I-th element.  The elements must be listed in DESCENDING order.
#    On input, T describes a K subset.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(K), T describes the next K subset in the ordering.
#    If the input T was the last in the ordering, then the output T
#    will be the first.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, k ):
      t[i] = k - i
    rank = 0
    return t, rank
#
#  Check.
#
  check = ksubset_colex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'ksubset_colex_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'ksubset_colex_successor(): Fatal error!' )

  for i in range ( k - 1, 0, -1 ):
    if ( t[k-i] + 1 < t[k-i-1] ):
      t[k-i] = t[k-i] + 1
      rank = rank + 1
      return t, rank

  if ( t[0] < n ):
    t[0] = t[0] + 1
    for i in range ( 1, k ):
      t[k-i] = i
    rank = rank + 1
    return t, rank
#
#  The last K subset was input.
#  Return the first one.
#
  for i in range ( 1, k + 1 ):
    t[i-1] = k + 1 - i

  rank = 0

  return t, rank

def ksubset_colex_successor_test ( ):

#*****************************************************************************80
#
## ksubset_colex_successor_test() tests ksubset_colex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_colex_successor_test():' )
  print ( '  ksubset_colex_successor() lists K-subsets of an N set,' )
  print ( '  using the colexicographic ordering.' )
  print ( '' )

  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = ksubset_colex_successor ( k, n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( k, t, '' )

  return

def ksubset_colex_unrank ( rank, k, n ):

#*****************************************************************************80
#
## ksubset_colex_unrank() computes the K subset of given colex rank.
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
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the K subset.
#
#    integer K, the number of elements each K subset must
#    have.  0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#  Output:
#
#    integer T(K), describes the K subset of the given
#    rank.  T(I) is the I-th element.  The elements must be listed in
#    DESCENDING order.
#
  import numpy as np
  from scipy.special import comb
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'ksubset_colex_unrank(): Fatal error!' )
    print ( '  The input N = %d is illegal.' % ( n ) )
    raise Exception ( 'ksubset_colex_unrank(): Fatal error!' )

  if ( k == 0 ):
    t = np.zeros ( k )
    return t

  if ( k < 0 or n < k ):
    print ( '' )
    print ( 'ksubset_colex_unrank(): Fatal error!' )
    print ( '  The input K = %d is illegal.' % ( k ) )
    raise Exception ( 'ksubset_colex_unrank(): Fatal error!' )

  nksub = ksubset_enum ( k, n )

  if ( rank < 0 or nksub < rank ):
    print ( '' )
    print ( 'ksubset_colex_unrank(): Fatal error!' )
    print ( '  The input RANK = %d is illegal.' % ( rank ) )
    raise Exception ( 'ksubset_colex_unrank(): Fatal error!' )
 
  t = np.zeros ( k )

  x = n

  for i in range ( 0, k ):

    while ( rank < comb ( x, k - i ) ):
      x = x - 1

    t[i] = x + 1
    rank = rank - comb ( x, k - i )

  return t

def ksubset_colex_unrank_test ( ):

#*****************************************************************************80
#
## ksubset_colex_unrank_test() tests ksubset_colex_unrank().
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
  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_colex_unrank_test():' )
  print ( '  ksubset_colex_unrank() unranks K-subsets of an N set,' )
  print ( '  using the colexicographic ordering:' )

  nksub = ksubset_enum ( k, n )
  rank = ( nksub // 2 )

  t = ksubset_colex_unrank ( rank, k, n )

  print ( '' )
  print ( '  The element of rank %d:' % ( rank ) )
  print ( '' )
  i4vec_print ( k, t, '  The element:' )

  return

def ksubset_enum ( k, n ):

#*****************************************************************************80
#
## ksubset_enum() enumerates the K element subsets of an N set.
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
#    integer K, the number of elements each K subset must
#    have. 0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    0 <= N.
#
#  Output:
#
#    integer NKSUB, the number of distinct elements.
#
  from scipy.special import comb

  nksub = comb ( n, k )

  return nksub

def ksubset_enum_test ( ):

#*****************************************************************************80
#
## ksubset_enum_test() tests ksubset_colex_enum().
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
  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_enum_test():' )
  print ( '  ksubset_enum() enumerates K-subsets of an N set.' )
#
#  Enumerate.
#
  print ( '' )
  print ( '      K:   0    1    2    3    4    5' )
  print ( '   N' )
  print ( '' )
  for n in range ( 0, 6 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      nksub = ksubset_enum ( k, n )
      print ( '  %2d' % ( nksub ), end = '' )
    print ( '' )

  return

def ksubset_lex_check ( k, n, t ):

#*****************************************************************************80
#
## ksubset_lex_check() checks a K subset in lex form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must have. 
#    0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    0 <= N.
#
#    integer T(K), describes a K subset.  T(I) is the I-th
#    element of the K subset.  The elements must be listed in ASCENDING order.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 0 ):
    check = False
    return check

  if ( k < 0 or n < k ):
    check = False
    return check
#
#  Items are between 0 and N, and in ascending order?
#
  tmin = 0

  for i in range ( 0, k ):

    if ( t[i] <= tmin or n < t[i] ):
      check = False
      return check

    tmin = t[i]

  return check

def ksubset_lex_check_test ( ):

#*****************************************************************************80
#
## ksubset_lex_check_test() tests ksubset_lex_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ksubset_lex_check_test():' )
  print ( '  ksubset_lex_check() checks a K subset of an N set.' )
  
  for test in range ( 1, 8 ):

    if ( test == 1 ):
      k = -1
      n = 5
      s = np.zeros ( n )
    elif ( test == 2 ):
      k = 3
      n = 0
      s = np.array ( [ 2, 3, 5 ] )
    elif ( test == 3 ):
      k = 3
      n = 5
      s = np.array ( [ 3, 2, 5 ] )
    elif ( test == 4 ):
      k = 3
      n = 5
      s = np.array ( [ 2, 3, 7 ] )
    elif ( test == 5 ):
      k = 3
      n = 5
      s = np.array ( [ 2, 3, 5 ] )
    elif ( test == 6 ):
      k = 0
      n = 5
      s = np.array ( [] )
    elif ( test == 7 ):
      k = 0
      n = 0
      s = np.array ( [] )

    check = ksubset_lex_check ( k, n, s )
    i4vec_transpose_print ( k, s, '  Subset:' )
    print ( '  N = %d, K = %d', ( n, k ) )
    print ( '  Check = %s' % ( check ) )

  return

def ksubset_lex_rank ( k, n, t ):

#*****************************************************************************80
#
## ksubset_lex_rank() computes the lexicographic rank of a K subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(K), describes a K subset.  T(I) is the I-th
#    element.  The elements must be listed in ascending order.
#
#  Output:
#
#    integer RANK, the rank of the K subset.
#
  from scipy.special import comb
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'ksubset_lex_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'ksubset_lex_rank(): Fatal error!' )

  rank = 0

  for i in range ( 0, k ):

    if ( i == 0 ):
      tim1 = 0
    else:
      tim1 = t[i-1]

    if ( tim1 + 1 <= t[i] - 1 ):
      for j in range ( tim1 + 1, t[i] ):
        rank = rank + comb ( n - j, k - 1 - i )

  return rank

def ksubset_lex_rank_test ( ):

#*****************************************************************************80
#
## ksubset_lex_rank_test() tests ksubset_lex_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_lex_rank_test():' )
  print ( '  ksubset_lex_rank() ranks K-subsets of an N set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.array ( [ 1, 4, 5 ] )
  i4vec_transpose_print ( k, t, '  The element to be ranked:' )

  rank = ksubset_lex_rank ( k, n, t )

  print ( '' )
  print ( '  The rank is computed as %d.' % ( rank ) )

  return

def ksubset_lex_successor ( k, n, t, rank ):

#*****************************************************************************80
#
## ksubset_lex_successor() computes the K subset lexicographic successor.
#
#  Discussion:
#
#    In the original code, there is a last element with no successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have. 1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(K), describes a K subset.  T(I) is
#    the I-th element.  The elements must be listed in ascending order.
#    On input, T describes a K subset.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(K), T describes the next K subset in the ordering.
#    If the input T was the last in the ordering, then the output T
#    will be the first.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, k ):
      t[i] = i + 1
    rank = 0
    return t, rank
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'ksubset_lex_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'ksubset_lex_successor(): Fatal error!' )

  isave = -1

  for i in range ( k, 0, -1 ):
    if ( t[i-1] != n - k + i ):
      isave = i
      break
#
#  The last K subset was input.
#  Return the first one.
#
  if ( isave == -1 ):

    for i in range ( 0, k ):
      t[i] = i + 1
    rank = 0

  else:

    for j in range ( k, isave - 1, -1 ):
      t[j-1] = t[isave-1] + 1 + j - isave

    rank = rank + 1

  return t, rank

def ksubset_lex_successor_test ( ):

#*****************************************************************************80
#
## ksubset_lex_successor_test() tests ksubset_lex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_lex_successor_test():' )
  print ( '  ksubset_lex_successor() lists K-subsets of an N set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.zeros ( k )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = ksubset_lex_successor ( k, n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( k, t, '' )

  return

def ksubset_lex_unrank ( rank, k, n ):

#*****************************************************************************80
#
## ksubset_lex_unrank() computes the K subset of given lexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the K subset.
#
#    integer K, the number of elements each K subset must
#    have.  0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#  Output:
#
#    integer T(K), describes the K subset of the given
#    rank.  T(I) is the I-th element.  The elements must be listed in
#    ascending order.
#
  import numpy as np
  from scipy.special import comb
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'ksubset_lex_rank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'ksubset_lex_unrank(): Fatal error!' )

  t = np.zeros ( k )

  if ( k == 0 ):
    return t

  if ( k < 0 or n < k ):
    print ( '' )
    print ( 'ksubset_lex_rank(): Fatal error!' )
    print ( '  Input K is illegal.' )
    raise Exception ( 'ksubset_lex_unrank(): Fatal error!' )

  nksub = ksubset_enum ( k, n )

  if ( rank < 0 or nksub < rank ):
    print ( '' )
    print ( 'ksubset_lex_unrank(): Fatal error!' )
    print ( '  Input rank is illegal.' )
    raise Exception ( 'ksubset_lex_unrank(): Fatal error!' )

  x = 1

  for i in range ( 1, k + 1 ):

    while ( comb ( n - x, k - i ) <= rank ):
      rank = rank - comb ( n - x, k - i )
      x = x + 1

    t[i-1] = x
    x = x + 1

  return t

def ksubset_lex_unrank_test ( ):

#*****************************************************************************80
#
## ksubset_lex_unrank_test() tests ksubset_lex_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_lex_unrank_test():' )
  print ( '  ksubset_lex_unrank() unranks K-subsets of an N set,' )
  print ( '  using the lexicographic ordering.' )

  rank = 5

  t = ksubset_lex_unrank ( rank, k, n )

  i4vec_transpose_print ( k, t, '  The element of rank 5:' )

  return

def ksubset_random ( k, n, rng ):

#*****************************************************************************80
#
## ksubset_random() selects a random subset of size K from a set of size N.
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
#    12 Septembe r2022
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
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    integer N, the size of the set from which subsets are drawn.
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

def ksubset_random_test ( rng ):

#*****************************************************************************80
#
## ksubset_random_test() tests ksubset_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 September 2022
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 100

  print ( '' )
  print ( 'ksubset_random_test():' )
  print ( '  ksubset_random() generates a random K subset of an N set.' )
  print ( '  Set size is N =    ', n )
  print ( '  Subset size is K = ', k )
  print ( '' )

  for i in range ( 0, 10 ):

    a = ksubset_random ( k, n, rng )
    print ( a )

  return

def ksubset_revdoor_rank ( k, n, t ):

#*****************************************************************************80
#
## ksubset_revdoor_rank() computes the revolving door rank of a K subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(K), describes a K subset.  T(I) is the I-th
#    element.  The elements must be listed in ascending order.
#
#  Output:
#
#    integer RANK, the rank of the K subset.
#
  from scipy.special import comb
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'ksubset_revdoor_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'ksubset_revdoor_rank(): Fatal error!' )

  if ( ( k % 2 ) == 0 ):

    rank = 0

  else:

    rank = - 1

  s = 1

  for i in range ( k, 0, -1 ):
    rank = rank + s * comb ( t[-1], i )
    s = - s

  return rank

def ksubset_revdoor_rank_test ( ):

#*****************************************************************************80
#
## ksubset_revdoor_rank_test() tests ksubset_revdoor_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_revdoor_rank_test():' )
  print ( '  ksubset_revdoor_rank() ranks K-subsets of an N set' )
  print ( '  using the revolving door ordering.' )

  t = np.array ( [ 2, 4, 5 ] )
  i4vec_transpose_print ( k, t, '  The K-subset to be ranked:' )

  rank = ksubset_revdoor_rank ( k, n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d' % ( rank ) )

  return

def ksubset_revdoor_successor ( k, n, t, rank ):

#*****************************************************************************80
#
## ksubset_revdoor_successor() computes the K subset revolving door successor.
#
#  Discussion:
#
#    After numerous attempts to implement the algorithm published in
#    Kreher and Stinson, the Nijenhuis and Wilf version was implemented
#    instead.  The K and S algorithm is supposedly based on the N and W one.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2011
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
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(K), describes a K subset.  T(I) is the
#    I-th element.  The elements must be listed in ascending order.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(K), T describes the next K subset in the ordering.
#    If the input T was the last in the ordering, then the output T
#    will be the first.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == - 1 ):
    for i in range ( 0, k ):
      t [i] = i + 1
    rank = 0
    return t, rank
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'ksubset_revdoor_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'ksubset_revdoor_successor(): Fatal error!' )

  j = 0

  while ( True ):

    if ( 0 < j or ( k % 2 ) == 0 ):

      j = j + 1

      if ( k < j ):
        t[k-1] = k
        rank = 0
        return t, rank

      if ( t[j-1] != j ):

        t[j-1] = t[j-1] - 1

        if ( j != 1 ):
          t[j-2] = j - 1

        rank = rank + 1
        return t, rank

    j = j + 1

    if ( j < k ):
      if ( t[j-1] != t[j] - 1 ):
        break
    else:
      if ( t[j-1] != n ):
        break

  t[j-1] = t[j-1] + 1

  if ( j != 1 ):
    t[j-2] = t[j-1] - 1

  rank = rank + 1

  return t, rank

def ksubset_revdoor_successor_test ( ):

#*****************************************************************************80
#
## ksubset_revdoor_successor_test() tests ksubset_revdoor_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_revdoor_successor_test():' )
  print ( '  ksubset_revdoor_successor() lists K-subsets of an N set' )
  print ( '  using the revolving door ordering.' )
  print ( '' )

  t = np.zeros ( k )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = ksubset_revdoor_successor ( k, n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( k, t, '' )

  return

def ksubset_revdoor_unrank ( rank, k, n ):

#*****************************************************************************80
#
## ksubset_revdoor_unrank() computes the K subset of given revolving door rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the K subset.
#
#    integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#  Output:
#
#    integer T(K), describes the K subset of the given
#    rank.  T(I) is the I-th element.  The elements must be listed in
#    ascending order.
#
  import numpy as np
  from scipy.special import comb
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'ksubset_revdoor_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'ksubset_revdoor_unrank(): Fatal error!' )

  if ( k < 1 or n < k ):
    print ( '' )
    print ( 'ksubset_revdoor_unrank(): Fatal error!' )
    print ( '  Input K is illegal.' )
    raise Exception ( 'ksubset_revdoor_unrank(): Fatal error!' )

  nksub = ksubset_enum ( k, n )

  if ( rank < 0 or nksub < rank ):
    print ( '' )
    print ( 'ksubset_revdoor_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'ksubset_revdoor_unrank(): Fatal error!' )

  t = np.zeros ( k )

  x = n

  for i in range ( k, 0, -1 ):

    while ( rank < comb ( x, i ) ):
      x = x - 1

    t[i-1] = x + 1
    rank = comb ( x + 1, i ) - rank - 1

  return t

def ksubset_revdoor_unrank_test ( ):

#*****************************************************************************80
#
## ksubset_revdoor_unrank_test() tests ksubset_revdoor_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_revdoor_unrank_test():' )
  print ( '  ksubset_revdoor_unrank() unranks K-subsets of an N set' )
  print ( '  using the revolving door ordering.' )

  rank = 5

  t = ksubset_revdoor_unrank ( rank, k, n )

  i4vec_transpose_print ( k, t, '  The element of rank 5:' )

  return

def marriage ( n, prefer, rank ):

#*****************************************************************************80
#
## marriage() finds a stable set of marriages for given preferences.
#
#  Discussion:
#
#    Given a set of N men and N women who must be married in pairs,
#    and information defining the relative rankings that each person
#    assigns to the candidates of the opposite sex, this routine finds
#    a stable set of marriages for them.
#
#    A stable set of marriages is a pairing of the men and women with
#    the stability property: if M1 marries W1 and M2 marries W2, then
#    it is never the case that M1 and W2 would both prefer to be married
#    to each other.
#
#    An important application of stable marriage algorithms occurs in
#    the annual matching of medical residents to hospitals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Sedgewick,
#    Algorithms in C,
#    Addison-Wesley, 1990,
#    ISBN: 0-201-51425-7,
#    LC: QA76.73.C15S43.
#
#  Input:
#
#    integer N, the number of pairs of men and women.
#
#    integer PREFER(N,N) for man I, the value of
#    PREFER(I,J) represents his J-th preference for a wife.
#
#    integer RANK(N,N) for woman I, the value of RANK(I,J)
#    represents her ranking of man number J.  A value of 1 for RANK(I,J)
#    means woman I ranks man J most preferable, while a value of N
#    would mean she ranked him least preferable.
#
#  Output:
#
#    integer FIANCEE(N) for woman I, FIANCEE(I) is the
#    man to whom she is now engaged.
#
#    integer NEXT(N) for man I, NEXT(I) is his preference
#    ranking for the woman to whom he is now engaged.  A value of 1 represents
#    his first choice, a value of N his last.
#
  import numpy as np
#
#  For man I, NEXT(I) is the woman I has most recently proposed to,
#  and hence NEXT(I)+1 is the next one to try.
#
  next = np.zeros ( n, dtype = np.int32 )
#
#  For woman I, FIANCEE(I) is the man she has agree to marry,
#  or 0 if she has not agreed to any man yet.
#
  fiancee = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    fiancee[i] = -1
#
#  Start with an unengaged man, and end with an engaged woman.
#
  for i in range ( 0, n ):

    m = i

    while ( True ):

      next[m] = next[m] + 1

      w = prefer[m,next[m]-1] - 1

      if ( fiancee[w] == -1 ):
        fiancee[w] = m
        break

      if ( rank[w,m] < rank[w,fiancee[w]] ):
        temp       = fiancee[w]
        fiancee[w] = m
        m          = temp

  return fiancee, next

def marriage_test ( ):

#*****************************************************************************80
#
## marriage_test() tests marriage().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
#
#  PREFER(M,W) is the index of women W on man M's list.
#
  prefer = np.array ( [ \
    [ 2, 5, 1, 3, 4 ], \
    [ 1, 2, 3, 4, 5 ], \
    [ 2, 3, 5, 4, 1 ], \
    [ 1, 3, 2, 4, 5 ], \
    [ 5, 3, 2, 1, 4 ] ], dtype = np.int32 )
#
#  RANK(W,M) is the index of man M on woman W's list.
#
  rank = np.array ( [ \
    [ 2, 4, 5, 3, 1 ], \
    [ 4, 3, 5, 1, 2 ], \
    [ 1, 3, 4, 2, 5 ], \
    [ 4, 2, 1, 3, 5 ], \
    [ 5, 2, 3, 1, 4 ] ], dtype = np.int32 )

  print ( '' )
  print ( 'marriage_test():' )
  print ( '  marriage() arranges a set of stable marriages' )
  print ( '  given a set of preferences.' )

  fiancee, next = marriage ( n, prefer, rank )

  print ( '' )
  print ( '  Man, Wife\'s rank, Wife' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %6d  %6d' % ( i + 1, next[i], prefer[i,next[i]-1] ) )

  print ( '' )
  print ( '  Woman, Husband\'s rank, Husband' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %6d  %6d' % ( i + 1, rank[i,fiancee[i]], fiancee[i]+1 ) )

  print ( '' )
  print ( '  Correct result:' )
  print ( '' )
  print ( '  M:W 1  2  3  4  5' )
  print ( '   1  +  .  .  .  .' )
  print ( '   2  .  .  .  +  .' )
  print ( '   3  .  .  .  .  +' )
  print ( '   4  .  .  +  .  .' )
  print ( '   5  .  +  .  .  .' )

  return

def mountain ( n, x, y ):

#*****************************************************************************80
#
## mountain() enumerates the mountains.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, ...
#    N must be positive.
#
#    integer X, Y, ...
#    0 <= X <= 2 * N,
#
#  Output:
#
#    integer VALUE, the value of the "mountain function"
#    M ( N, X, Y ), which is the number of all mountain ranges from
#    (X,Y) to (2*N,0) which do not drop below sea level.
#
  from scipy.special import comb
#
#  Check.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'mountain(): Fatal error!' )
    print ( '  N <= 0.' )
    print ( '  N = %d' % ( n ) )
    raise Exception ( 'mountain(): Fatal error!' )

  if ( x < 0 ):
    print ( '' )
    print ( 'mountain(): Fatal error!' )
    print ( '  X < 0.' )
    print ( '  X = %d' % ( x ) )
    raise Exception ( 'mountain(): Fatal error!' )

  if ( 2 * n < x ):
    print ( '' )
    print ( 'mountain(): Fatal error!' )
    print ( '  2 * N < X.' )
    print ( '  X = %d' % ( x ) )
    print ( '  N = %d' % ( n ) )
    raise Exception ( 'mountain(): Fatal error!' )
#
#  Special cases.
#
  if ( y < 0 ):
    value = 0
    return value

  if ( 2 * n < x + y ):
    value = 0
    return value

  if ( ( ( x + y ) % 2 ) == 1 ):
    value = 0
    return value

  a = 2 * n - x
  b = n - ( ( x + y ) // 2 )
  c = n - 1 - ( ( x + y ) // 2 )

  value = comb ( a, b ) - comb ( a, c )

  return value

def mountain_test ( ):

#*****************************************************************************80
#
## mountain_test() tests mountain().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'mountain_test():' )
  print ( '  mountain() computes mountain numbers.' )
  print ( '' )
  print ( '   Y    MXY' )
  print ( '' )

  for y in range ( 0, n + 1 ):
    print ( '  %2d   ' % ( y ), end = '' )
    for x in range ( 0, 2 * n + 1 ):
      mxy = mountain ( n, x, y )
      print ( '%4d' % ( mxy ), end = '' )
    print ( '' )

  return

def npart_enum ( n, npart ):

#*****************************************************************************80
#
## npart_enum() enumerates the number of partitions of N with NPART parts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    Normally N must be positive, but for this routine any
#    N is allowed.
#
#    integer NPART, the number of parts of the partition.
#    Normally, 1 <= NPART <= N is required,
#    but for this routine any value of NPART is allowed.
#
#  Output:
#
#    integer NPARTITIONS is the number of partitions of N
#    with NPART parts.
#
  if ( n <= 0 ):

    npartitions = 0

  elif ( npart <= 0 or n < npart ):

    npartitions = 0

  else:

    p = npart_table ( n, npart )

    npartitions = p[n,npart]

  return npartitions

def npart_enum_test ( ):

#*****************************************************************************80
#
## npart_enum_test() tests npart_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'npart_enum_test():' )
  print ( '  npart_enum() enumerates partitions of N into part_NUM parts.' )
  print ( '' )
  print ( '   part_NUM:  1       2       3       4       5       6' )
  print ( '   N' )
  for n in range ( 0, 11 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for part_num in range ( 1, min ( n, 6 ) + 1 ):
      npart_num = npart_enum ( n, part_num )
      print ( '  %6d' % ( npart_num ), end = '' )
    print ( '' )

  return

def npart_rsf_lex_random ( n, npart, rng ):

#*****************************************************************************80
#
## npart_rsf_lex_random() returns a random RSF NPART partition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
  import numpy as np

  npartitions = npart_enum ( n, npart );

  rank = rng.integers ( low = 1, high = npartitions, endpoint = True )

  a = npart_rsf_lex_unrank ( rank, n, npart )

  return a

def npart_rsf_lex_random_test ( rng ):

#*****************************************************************************80
#
## npart_rsf_lex_random_test() tests npart_rsf_lex_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  npart = 3
  n = 12

  print ( '' )
  print ( 'npart_rsf_lex_random_test():' )
  print ( '  npart_rsf_lex_random() produces random examples' )
  print ( '  of partitions of N = %d' % ( n ) )
  print ( '  with NPART = %d parts' % ( npart ) )
  print ( '  in reverse standard form.' )
  print ( '' )

  for i in range ( 0, 10 ):

    t = npart_rsf_lex_random ( n, npart, rng )

    for i in range ( 0, npart ):
      print ( '%5d' % ( t[i] ), end = '' )
    print ( '' )

  return

def npart_rsf_lex_rank ( n, npart, a ):

#*****************************************************************************80
#
## npart_rsf_lex_rank() computes the lex rank of an RSF NPART partition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#  Output:
#
#    integer RANK, the rank of the partition.
#

#
#  Check.
#
  check = part_rsf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'npart_rsf_lex_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'npart_rsf_lex_rank(): Fatal error!' )
#
#  Get the table of partitions of N with NPART parts.
#
  p = npart_table ( n, npart )
#
#  Copy the partition "backwards".
#
  b = i4vec_reverse ( npart, a )

  rank = 0

  while ( 0 < n and 0 < npart ):

    if ( b[npart-1] == 1 ):

      n = n - 1
      npart = npart - 1

    else:

      for i in range ( 0, npart ):
        b[i] = b[i] - 1
      rank = rank + p[n-1,npart-1]
      n = n - npart

  return rank

def npart_rsf_lex_rank_test ( ):

#*****************************************************************************80
#
## npart_rsf_lex_rank_test() tests npart_rsf_lex_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  npart = 3
  n = 12

  print ( '' )
  print ( 'npart_rsf_lex_rank_test():' )
  print ( '  npart_rsf_lex_rank() ranks partitions of N with NPART parts' )
  print ( '  in reverse standard form.' )

  t = np.array ( [ 1, 5, 6 ] )
  i4vec_transpose_print ( npart, t, '  Element:' )

  rank = npart_rsf_lex_rank ( n, npart, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )

  return

def npart_rsf_lex_successor ( n, npart, a, rank ):

#*****************************************************************************80
#
## npart_rsf_lex_successor() computes the RSF lex successor for NPART partitions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be at least 1.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer A(NPART), contains the successor partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, npart ):
      a[i] = 1
    a[npart-1] = n - ( npart - 1 )
    rank = 0
    return a, rank
#
#  Check.
#
  check = part_rsf_check ( n, npart, a )
  if ( not check ):
    print ( '' )
    print ( 'npart_rsf_lex_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'npart_rsf_lex_successor(): Fatal error!' )
#
#  Find the first index I for which A(NPART+1-I) + 1 < A(NPART).
#
  i = 2

  while ( True ):

    if ( npart < i ):
      break

    if ( a[npart+1-i-1] + 1 < a[npart-1] ):
      break

    i = i + 1
#
#  If no such index, we've reached the end of the line.
#
  if ( i == npart + 1 ):

    for i in range ( 0, npart ):
      a[i] = 1
    a[npart-1] = n - ( npart - 1 )
    rank = 0
    return a, rank
#
#  Otherwise, increment A(NPART+1-I), and adjust other entries.
#
  else:

    a[npart+1-i-1] = a[npart+1-i-1] + 1
    d = - 1

    for j in range ( i - 1, 1, -1 ):
      d = d + a[npart+1-j-1] - a[npart+1-i-1]
      a[npart+1-j-1] = a[npart+1-i-1]

    a[npart-1] = a[npart-1] + d

  rank = rank + 1

  return a, rank

def npart_rsf_lex_successor_test ( ):

#*****************************************************************************80
#
## npart_rsf_lex_successor_test() tests npart_rsf_lex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  npart = 3
  n = 12

  print ( '' )
  print ( 'npart_rsf_lex_successor_test():' )
  print ( '  npart_rsf_lex_successor() lists' )
  print ( '  partitions of N with NPART parts' )
  print ( '  in reverse standard form.' )
  print ( '' )

  t = np.zeros ( npart )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = npart_rsf_lex_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )

  return

def npart_rsf_lex_unrank ( rank, n, npart ):

#*****************************************************************************80
#
## npart_rsf_lex_unrank() unranks an RSF NPART partition in the lex ordering.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the partition.
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#  Output:
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
  import numpy as np
#
#  Check.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'npart_rsf_lex_unrank(): Fatal error!' )
    print ( '  The input N is illegal.' )
    raise Exception ( 'npart_rsf_lex_unrank(): Fatal error!' )

  if ( npart < 1 or n < npart ):
    print ( '' )
    print ( 'npart_rsf_lex_unrank(): Fatal error!' )
    print ( '  The input NPART is illegal.' )
    raise Exception ( 'npart_rsf_lex_unrank(): Fatal error!' )

  npartitions = npart_enum ( n, npart )

  if ( rank < 0 or npartitions < rank ):
    print ( '' )
    print ( 'npart_rsf_lex_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'npart_rsf_lex_unrank(): Fatal error!' )
#
#  Get the table of partitions of N with NPART parts.
#
  p = npart_table ( n, npart )

  a = np.zeros ( npart )
  npartcopy = npart

  while ( 0 < n ):

    if ( rank < p[n-1,npartcopy-1] ):
      a[npart-npartcopy] = a[npart-npartcopy] + 1
      n = n - 1
      npartcopy = npartcopy - 1
    else:
      for i in range ( 0, npartcopy ):
        a[npart-1-i] = a[npart-1-i] + 1
      rank = rank - p[n-1,npartcopy-1]
      n = n - npartcopy

  return a

def npart_rsf_lex_unrank_test ( ):

#*****************************************************************************80
#
## npart_rsf_lex_unrank_test() tests npart_rsf_lex_unrank().
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
  npart = 3
  n = 12

  print ( '' )
  print ( 'npart_rsf_lex_unrank_test():' )
  print ( '  npart_rsf_lex_unrank() unranks' )
  print ( '  partitions of N with NPART parts' )
  print ( '  in reverse standard form.' )

  rank = 4

  t = npart_rsf_lex_unrank ( rank, n, npart )

  i4vec_transpose_print ( npart, t, '  The element of rank 4:' )

  return

def npart_sf_lex_successor ( n, npart, a, rank ):

#*****************************************************************************80
#
## npart_sf_lex_successor() computes SF NPART partition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The values in A must be in DESCENDING order.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer A(NPART), contains the successor partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The values in A must be in DESCENDING order.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    a = i4vec_part2 ( n, npart )
    rank = 0
    return a, rank
#
#  Check.
#
  check = part_sf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'npart_sf_lex_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'npart_sf_lex_successor(): Fatal error!' )
#
#  Find the last entry that is 2 or more.
#
  for i in range ( npart - 1, -1, -1 ):
    if ( 1 < a[i] ):
      indx = i
      break
#
#  As long as the last nonunit occurs after the first position,
#  have it donate 1 to the left.
#
  if ( 0 < indx ):

    a[indx] = a[indx] - 1
    a[indx-1] = a[indx-1] + 1
    indx = indx - 1

    while ( True ):

      if ( indx <= 0 ):
        break

      if ( a[indx] <= a[indx-1] ):
        break

      temp      = a[indx]
      a[indx]   = a[indx-1]
      a[indx-1] = temp

      indx = indx - 1
#
#  Sum the tail.
#
    temp = 0
    for i in range ( indx + 1, npart ):
      temp = temp + a[i]
      a[i] = 0
    temp = int ( temp )
#
#  Partition the tail sum equally over the tail.
#
    j = 0
    for i in range ( 0, temp ):
      a[indx+1+j] = a[indx+1+j] + 1
      j = j + 1
      if ( npart - indx - 1 <= j ):
        j = 0

    rank = rank + 1
#
#  If A(2) through A(NPART) are 1, then this is the last element.
#  Return the first one.
#
  else:

    a = i4vec_part2 ( n, npart )
    rank = 0

  return a, rank

def npart_sf_lex_successor_test ( ):

#*****************************************************************************80
#
## npart_sf_lex_successor_test() tests npart_sf_lex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  npart = 3
  n = 12

  print ( '' )
  print ( 'npart_sf_lex_successor_test():' )
  print ( '  npart_sf_lex_successor() lists' )
  print ( '  Partitions of N with NPART parts' )
  print ( '  in standard form.' )

  npartitions = npart_enum ( n, npart )

  print ( '' )
  print ( '  For N = %d' % ( n ) )
  print ( '  and NPART = %d' % ( npart ) )
  print ( '  the number of partitions is %d' % ( npartitions ) )
  print ( '' )
#
#  List.
#
  t = np.zeros ( npart )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = npart_sf_lex_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )

  return

def npart_table ( n, npart ):

#*****************************************************************************80
#
## npart_table() tabulates the number of partitions of N having NPART parts.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#  Output:
#
#    integer P(1:N+1,1:NPART+1), P(I+1,J+1) is the number of
#    partitions of I having J parts.
#
  import numpy as np

  p = np.zeros ( [ n + 1, npart + 1 ] )

  p[0,0] = 1

  for i in range ( 1, n + 1 ):
    for j in range ( 1, npart + 1 ):
      if ( i < j ):
        p[i,j] = 0
      elif ( i < 2 * j ):
        p[i,j] = p[i-1,j-1]
      else:
        p[i,j] = p[i-1,j-1] + p[i-j,j]

  return p

def npart_table_test ( ):

#*****************************************************************************80
#
## npart_table_test() tests npart_table().
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
  maxn = 10
  maxpart = 5

  print ( '' )
  print ( 'npart_table_test():' )
  print ( '  npart_table() tabulates partitions' )
  print ( '  of N with NPART parts' )

  p = npart_table ( maxn, maxpart )

  print ( '' )
  print ( '    I P(I,0) P(I,1) P(I,2) P(I,3) P(I,4) P(I,5)' )
  print ( '' )

  for i in range ( 0, maxn + 1 ):
    print ( '%5d' % ( i ), end = '' )
    for j in range ( 0, maxpart + 1 ):
      print ( '%5d' % ( p[i,j] ), end = '' )
    print ( '' )

  return

def part_enum ( n ):

#*****************************************************************************80
#
## part_enum() enumerates the number of partitions of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    Normally N must be positive, but for this routine any
#    N is allowed.
#
#  Output:
#
#    integer NPARTITIONS is the number of partitions of N.
#
  if ( n < 0 ):

    npartitions = 0

  else:

    p = part_table ( n )

    npartitions = p[n]

  return npartitions

def part_enum_test ( ):

#*****************************************************************************80
#
## part_enum_test() tests part_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'part_enum_test():' )
  print ( '  part_enum() enumerates partitions of N.' )
  print ( '' )
  print ( '   N     #' )
  print ( '' )

  for n in range ( 0, 11 ):
    part_num = part_enum ( n )
    print ( '  %2d  %6d' % ( n, part_num ) )

  return

def partition_greedy ( n, a ):

#*****************************************************************************80
#
## partition_greedy() attacks the partition problem with a greedy algorithm.
#
#  Discussion:
#
#    Given a collection of N not necessarily distinct positive integers A(I),
#    it is desired to partition the values into two groups, whose sums are
#    as close as possible.
#
#  Algorithm:
#
#    Begin with sets 1 and 2 empty.
#
#    Process the data in descending order of magnitude.
#
#    The next item A(I) is added to set 1 or set 2, whichever has the
#    smallest current sum.
#
#    Stop as soon as all items have been allocated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    The Easiest Hard Problem,
#    American Scientist,
#    Volume 90, Number 2, March-April 2002, pages 113-117.
#
#  Input:
#
#    integer N, the number of values.  N must be positive.
#
#    integer A(N), a collection of positive values.
#
#  Output:
#
#    integer A(N), a collection of positive values, sorted into descending order.
#
#    integer INDX(N), is 0 if A(I) is part of
#    set 0, and 1 if it is assigned to set 1.
#
  import numpy as np

  sums = np.zeros ( 2 )
  indx = np.zeros ( n )

  a = i4vec_sort_insert_d ( n, a )

  for i in range ( 0, n ):

    if ( sums[0] < sums[1] ):
      j = 0
    else:
      j = 1

    indx[i] = j
    sums[j] = sums[j] + a[i]

  return a, indx

def partition_greedy_test ( ):

#*****************************************************************************80
#
## partition_greedy_test() tests partition_greedy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'partition_greedy_test():' )
  print ( '  partition_greedy() partitions an integer vector into' )
  print ( '  two subsets with nearly equal sum.' )

  for test in range ( 0, 2 ):

    if ( test == 0 ):
      a = np.array ( [ 2, 10, 3, 8, 5, 7, 9, 5, 3, 2 ] )
    elif ( test == 1 ):
      a = np.array ( [ 771, 121, 281, 854, 885, 734, 486, 1003, 83, 62 ] )

    a, indx = partition_greedy ( n, a )

    print ( '' )
    print ( '  Data set', test, ' partitioned:' )
    print ( '' )

    sums = np.zeros ( 2 )

    for i in range ( 0, n ):

      if ( indx[i] == 0 ):
        sums[0] = sums[0] + a[i]
        print ( '  %4d' % ( a[i] ) )
      else:
        print ( '        %4d' % ( a[i] ) )
        sums[1] = sums[1] + a[i]

    print ( '' )
    print ( '  Sums:' )
    print ( '' )
    print ( '  %4d  %4d' % ( sums[0], sums[1] ) )

  return

def partn_enum ( n, nmax ):

#*****************************************************************************80
#
## partn_enum() enumerates the partitions of N with maximum element NMAX.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    Normally N must be positive, but for this routine any
#    N is allowed.
#
#    integer NMAX, the maximum element in the partition.
#    Normally, 1 <= NMAX <= N is required,
#    but for this routine any value of NMAX is allowed.
#
#  Output:
#
#    integer NPARTITIONS is the number of partitions of N
#    with maximum element NMAX.
#
  if ( n <= 0 ):

    value = 0

  elif ( nmax <= 0 or n < nmax ):

    value = 0

  else:

    p = npart_table ( n, nmax )

    value = p[n,nmax]

  return value

def partn_enum_test ( ):

#*****************************************************************************80
#
## partn_enum_test() tests partn_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'partn_enum_test():' )
  print ( '  partn_enum() enumerates partitions of N with maximum part NMAX.' )
  print ( '' )
  print ( '   NMAX:      1       2       3       4       5       6' )
  print ( '   N' )

  for n in range ( 0, 11 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for nmax in range ( 1, min ( n, 6 ) + 1 ):
      partn_num = partn_enum ( n, nmax )
      print ( '  %6d' % ( partn_num ), end = '' )
    print ( '' )

  return

def partn_sf_check ( n, nmax, npart, a ):

#*****************************************************************************80
#
## partn_sf_check() checks an SF partition of an integer with largest entry NMAX.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NMAX, the value of the largest entry.
#    1 <= NMAX <= N.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The entries must be in DESCENDING order.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  import numpy as np

  check = True

  if ( n < 1 ):
    check = False
    return check

  if ( nmax < 1 or n < nmax ):
    check = False
    return check

  if ( npart < 1 or n < npart ):
    check = False
    return check
#
#  Entry 1 must be NMAX.
#
  if ( a[0] != nmax ):
    check = False
    return check
#
#  Every entry must lie between 1 and N.
#
  for i in range ( 0, npart ):
    if ( a[i] < 1 or n < a[i] ):
      check = False
      return check
#
#  The entries must be in descending order.
#
  for i in range ( 1, npart ):
    if ( a[i-1] < a[i] ):
      check = False
      return check
#
#  The entries must add up to N.
#
  asum = 0
  for i in range ( 0, npart ):
    asum = asum + a[i]
  if ( asum != n ):
    check = False
    return check

  return check

def partn_sf_check_test ( ):

#*****************************************************************************80
#
## partn_sf_check_test() tests partn_sf_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'partn_sf_check_test():' )
  print ( '  partn_sf_check() checks a standard form partition' )
  print ( '  of N with largest entry NMAX.' )

  for test in range ( 1, 8 ):

    if ( test == 1 ):
      n = 0
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 2 ):
      n = 15
      nmax = 6
      npart = 0
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 3 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 6, 6, -3 ] )
    elif ( test == 4 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 8, 4, 2, 1 ] )
    elif ( test == 5 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 1, 4, 4, 6 ] )
    elif ( test == 6 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 5, 4, 1 ] )
    elif ( test == 7 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )

    print ( '' )
    print ( '  Partition in SF form.' )
    print ( '  Partition of N = %d' % ( n ) )
    print ( '  Maximum entry NMAX = %d' % ( nmax ) )
    print ( '  Number of parts NPART = %d' % ( npart ) )
    i4vec_transpose_print ( npart, a, '' )
    check = partn_sf_check ( n, nmax, npart, a )
    print ( '  Check = %s' % ( check ) )

  return

def partn_successor ( n, nmax, npart, a, rank ):

#*****************************************************************************80
#
## partn_successor() computes partitions whose largest part is NMAX.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NMAX, the maximum size of any part of the
#    partition.  1 <= NMAX <= N.
#
#    integer NPART, the number of parts of the
#    partition.  1 <= NPART <= N.
#
#    integer A(N), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer NPART, the number of parts of the
#    partition.  1 <= NPART <= N.
#
#    integer A(N), contains the successor partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  import numpy as np
#
#  Return the first element.
#
  if ( rank == -1 ):

    npart = n + 1 - nmax
    a[0] = nmax
    for i in range ( 1, npart ):
      a[i] = 1
    rank = 0
    return npart, a, rank
#
#  Check.
#
  check = partn_sf_check ( n, nmax, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'partn_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'partn_successor(): Fatal error!' )
#
#  If there are at least two parts, and the next to last is not NMAX,
#  then rob the last part and pay the next to the last part.
#  Then, if the next to last part is too big, swap it leftwards.
#
  if ( 1 < npart ):

    if ( a[npart-2] < nmax ):

      a[npart-1] = a[npart-1] - 1
      a[npart-2] = a[npart-2] + 1
      index = npart - 1

      while ( True ):

        if ( index <= 1 ):
          break

        if ( a[index-1] <= a[index-2] ):
          break

        temp       = a[index-2]
        a[index-2] = a[index-1]
        a[index-1] = temp

        index = index - 1
#
#  Sum the tail.
#
      temp = 0
      for i in range ( index, npart ):
        temp = temp + a[i]
        a[i] = 0
      temp = int ( temp )
#
#  Spread the sum as 1's.
#
      npart = index + temp
      for i in range ( index, npart ):
        a[i] = 1
      rank = rank + 1
      return npart, a, rank
#
#  Otherwise, we've reached the last item.
#  Return the first one.
#
  else:

    npart = n + 1 - nmax
    a[0] = nmax
    for i in range ( 1, npart ):
      a[i] = 1
    rank = 0
    return npart, a, rank

  return npart, a, rank

def partn_successor_test ( ):

#*****************************************************************************80
#
## partn_successor_test() tests partn_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 11
  nmax = 4

  print ( '' )
  print ( 'partn_successor_test():' )
  print ( '  partn_successor() lists partitions of N with maximum element NMAX.' )
  print ( '' )
  print ( '  Here, N = %d' % ( n ) )
  print ( '  NMAX = %d' % ( nmax ) )
  print ( '' )
#
#  List.
#
  npart = 0
  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    npart, t, rank = partn_successor ( n, nmax, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )

  return

def part_rsf_check ( n, npart, a ):

#*****************************************************************************80
#
## part_rsf_check() checks a reverse standard form partition of an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The entries must be in ASCENDING order.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  import numpy as np

  check = True

  if ( n < 1 ):
    check = False
    return check

  if ( npart < 1 or n < npart ):
    check = False
    return check
#
#  Every entry must lie between 1 and N.
#
  for i in range ( 0, npart ):
    if ( a[i] < 1 or n < a[i] ):
      check = False
      return check
#
#  The entries must be in ascending order.
#
  for i in range ( 1, npart ):
    if ( a[i] < a[i-1] ):
      check = False
      return check
#
#  The entries must add up to N.
#
  if ( np.sum ( a ) != n ):
    check = False
    return check

  return check

def part_rsf_check_test ( ):

#*****************************************************************************80
#
## part_rsf_check_test() tests part_rsf_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'part_rsf_check_test():' )
  print ( '  part_rsf_check() checks a reverse standard form partition.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      n = 0
      npart = 4
      a = np.array ( [ 1, 4, 4, 6 ] )
    elif ( test == 2 ):
      n = 15
      npart = 0
      a = np.array ( [ 1, 4, 4, 6 ] )
    elif ( test == 3 ):
      n = 15
      npart = 4
      a = np.array ( [ -9, 4, 4, 16 ] )
    elif ( test == 4 ):
      n = 15
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 5 ):
      n = 15
      npart = 4
      a = np.array ( [ 1, 4, 5, 6 ] )
    elif ( test == 6 ):
      n = 15
      npart = 4
      a = np.array ( [ 1, 4, 4, 6 ] )

    print ( '' )
    print ( '  Partition in RSF form.' )
    print ( '  Partition of N = %d' % ( n ) )
    print ( '  Number of parts NPART = %d' % ( npart ) )
    i4vec_transpose_print ( npart, a, '' )
    check = part_rsf_check ( n, npart, a )
    print ( '  Check = %s' % ( check ) )

  return

def part_sf_check ( n, npart, a ):

#*****************************************************************************80
#
## part_sf_check() checks a standard form partition of an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The entries must be in DESCENDING order.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  import numpy as np

  check = True

  if ( n < 1 ):
    check = False
    return check

  if ( npart < 1 or n < npart ):
    check = False
    return check
#
#  Every entry must lie between 1 and N.
#
  for i in range ( 0, npart ):
    if ( a[i] < 1 or n < a[i] ):
      check = False
      return check
#
#  The entries must be in descending order.
#
  for i in range ( 1, npart ):
    if ( a[i] > a[i-1] ):
      check = False
      return check
#
#  The entries must add up to N.
#
  if ( np.sum ( a ) != n ):
    check = False
    return check

  return check

def part_sf_check_test ( ):

#*****************************************************************************80
#
## part_sf_check_test() tests part_sf_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'part_sf_check_test():' )
  print ( '  part_sf_check() checks a standard form partition.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      n = 0
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 2 ):
      n = 15
      npart = 0
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 3 ):
      n = 15
      npart = 4
      a = np.array ( [ 16, 4, 4, -9 ] )
    elif ( test == 4 ):
      n = 15
      npart = 4
      a = np.array ( [ 1, 4, 4, 6 ] )
    elif ( test == 5 ):
      n = 15
      npart = 4
      a = np.array ( [ 6, 5, 4, 1 ] )
    elif ( test == 6 ):
      n = 15
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )

    print ( '' )
    print ( '  Partition in SF form.' )
    print ( '  Partition of N = %d' % ( n ) )
    print ( '  Number of parts NPART = %d' % ( npart ) )
    i4vec_transpose_print ( npart, a, '' )
    check = part_sf_check ( n, npart, a )
    print ( '  Check = %s' % ( check ) )

  return

def part_sf_conjugate ( n, npart, a ):

#*****************************************************************************80
#
## part_sf_conjugate() computes the conjugate of a partition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    integer A(N), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#  Output:
#
#    integer NPART2, the number of parts of the conjugate
#    partition.
#
#    integer B(N), contains the conjugate partition.
#
  import numpy as np
#
#  Check.
#
  check = part_sf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'part_sf_conjugate(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'part_sf_conjugate(): Fatal error!' )

  npart2 = a[0]
  b = np.zeros ( npart2, dtype = np.int32 )

  for i in range ( 0, npart ):
    for j in range ( 0, a[i] ):
      b[j] = b[j] + 1

  return npart2, b

def part_sf_conjugate_test ( ):

#*****************************************************************************80
#
## part_sf_conjugate_test() tests part_sf_conjugate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 8

  print ( '' )
  print ( 'part_sf_conjugate_test():' )
  print ( '  part_sf_conjugate() produces the conjugate of a partition.' )
  print ( '' )
  print ( '  Partitions of N = %d' % ( n ) )

#
#  List.
#
  npart = 0
  t = np.zeros ( n, dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    npart, t, rank = part_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    print ( '' )
    print ( '  %d' % ( rank ) )
    i4vec_transpose_print ( npart, t, '' )

    npartb, b = part_sf_conjugate ( n, npart, t )

    i4vec_transpose_print ( npartb, b, '' )

  return

def part_sf_majorize ( n, nparta, a, npartb, b ):

#*****************************************************************************80
#
## part_sf_majorize() determines if partition A majorizes partition B.
#
#  Discussion:
#
#    The partitions must be in standard form.
#
#    If A, with NPARTA parts, and B, with NPARTB parts, are both partitions
#    of the same positive integer N, then we say that A majorizes B if,
#    for every index K from 1 to N, it is true that
#
#      sum ( 1 <= I <= K ) B(I) <= sum ( 1 <= I <= K ) A(I)
#
#    where entries of A beyond index NPARTA, and of B beyond BPARTB
#    are assumed to be 0.  We say that A strictly majorizes B if
#    A majorizes B, and for at least one index K the inequality is strict.
#
#    For any two partitions of N, it is possible that A majorizes B,
#    B majorizes A, both partitions majorize each other (in which case
#    they are equal), or that neither majorizes the other.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jack vanLint, Richard Wilson,
#    A Course in Combinatorics,
#    Cambridge, 1992,
#    ISBN: 0-521-42260-4,
#    LC: QA164.L56.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPARTA, the number of parts in partition A.
#    1 <= NPARTA <= N.
#
#    integer A(NPARTA), contains partition A in standard
#    form.  A(1) through A(NPARTA) contain nonzero integers which sum to N.
#
#    integer NPARTB, the number of parts in partition B.
#    1 <= NPARTB <= N.
#
#    integer B(NPARTB), contains partition B in standard
#    form.  B(1) through B(NPARTB) contain nonzero integers which sum to N.
#
#  Output:
#
#    integer RESULT, the result of the comparison.
#    -2, A and B are incomparable, would have been -1.
#    -1, A < B, (A is strictly majorized by B),
#     0, A = B, (A and B are identical),
#    +1, A > B, (A strictly majorizes B),
#    +2, A and B are incomparable, would have been +1.
#

#
#  Check.
#
  check = part_sf_check ( n, nparta, a )

  if ( not check ):
    print ( '' )
    print ( 'part_sf_majorize(): Fatal error!' )
    print ( '  The input array A is illegal.' )
    raise Exception ( 'part_sf_majorize(): Fatal error!' )

  check = part_sf_check ( n, npartb, b )

  if ( not check ):
    print ( '' )
    print ( 'part_sf_majorize(): Fatal error!' )
    print ( '  The input array B is illegal.' )
    raise Exception ( 'part_sf_majorize(): Fatal error!' )
 
  result = 0
  suma = 0
  sumb = 0

  for i in range ( 0, min ( nparta, npartb ) ):

    suma = suma + a[i]
    sumb = sumb + b[i]

    if ( result == -1 ):

      if ( sumb < suma ):
        result = -2
        return result

    elif ( result == 0 ):

      if ( suma < sumb ):
        result = -1
      elif ( sumb < suma ):
        result = +1

    elif ( result == + 1 ):

      if ( suma < sumb ):
        result = +2
        return result

  return result

def part_sf_majorize_test ( ):

#*****************************************************************************80
#
## part_sf_majorize_test() tests part_sf_majorize().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 8

  a = np.array ( [ 2, 2, 2, 1, 1, 0, 0, 0 ] )
  b = np.array ( [ 3, 1, 1, 1, 1, 1, 0, 0 ] )
  c = np.array ( [ 2, 2, 1, 1, 1, 1, 0, 0 ] )
  nparta = 5
  npartb = 6
  npartc = 6

  print ( '' )
  print ( 'part_sf_majorize_test():' )
  print ( '  part_sf_majorize() determines if one partition' )
  print ( '  majorizes another.' )
  print ( '' )
  print ( '  Partitions of N = %d' % ( n ) )
  print ( '' )

  i4vec_transpose_print ( nparta, a, '  A:' )
  i4vec_transpose_print ( npartb, b, '  B:' )
  i4vec_transpose_print ( npartc, c, '  C:' )

  result = part_sf_majorize ( n, nparta, a, npartb, b )
  print ( '' )
  print ( '  A compare B: %d' % ( result ) )
  result = part_sf_majorize ( n, npartb, b, npartc, c )
  print ( '  B compare C: %d' % ( result ) )
  result = part_sf_majorize ( n, npartc, c, nparta, a )
  print ( '  C compare A: %d' % ( result ) )
  result = part_sf_majorize ( n, npartc, c, npartc, c )
  print ( '  C compare C: %d' % ( result ) )

  return

def part_successor ( n, npart, a, rank ):

#*****************************************************************************80
#
## part_successor() computes the lexicographic partition successor.
#
#  Discussion:
#
#    part_successor is "inspired by" the GenPartitions algorithm,
#    but instead of relying on recursion, generates the partitions
#    one at a time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#    integer NPART, the number of parts of the
#    partition.  1 <= NPART <= N.
#
#    integer A(N), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer NPART, the number of parts of the
#    partition.  1 <= NPART <= N.
#
#    integer A(N), contains the successor partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    integer RANK, the rank.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      a[i] = 1
    npart = n
    rank = 0
    return npart, a, rank
#
#  Check.
#
  check = part_sf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'part_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'part_successor(): Fatal error!' )
#
#  If possible, increment the first intermediate position that
#  is less than its left hand neighbor, and has at least one
#  right hand neighbor.
#
  ihi = npart - 1

  for i in range ( ihi - 1, 0, -1 ):

    if ( a[i] < a[i-1] ):
      asum = 0
      for j in range ( i + 1, npart ):
        asum = asum + a[j]
      asum = asum - 1
      a[i] = a[i] + 1
      for j in range ( i + 1, npart ):
        a[j] = 0
      npart = int ( i + 1 + asum )
      for j in range ( i + 1, npart ):
        a[j] = 1
      rank = rank + 1
      return npart, a, rank
#
#  A) there are two or more parts
#  Increment the first, replace the rest by 1's.
#
  if ( 2 <= npart ):
    a[0] = a[0] + 1
    for i in range ( 1, npart ):
      a[i] = 0
    npart = int ( n - a[0] + 1 )
    for i in range ( 1, npart ):
      a[i] = 1
    rank = rank + 1
#
#  B) there is only one part.
#  We've reached the last item.
#  Return the first one.
#
  elif ( npart == 1 ):
    for i in range ( 0, n ):
      a[i] = 1
    npart = n
    rank = 0

  return npart, a, rank

def part_successor_test ( ):

#*****************************************************************************80
#
## part_successor_test() tests part_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 8

  print ( '' )
  print ( 'part_successor_test():' )
  print ( '  part_successor() produces partitions of N,' )
  print ( '' )
  print ( '  Partitions of N = %d' % ( n ) )
  print ( '' )
#
#  List.
#
  npart = 0
  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    npart, t, rank = part_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )

  return

def part_table ( n ):

#*****************************************************************************80
#
## part_table() tabulates the number of partitions of N.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#    N must be positive.
#
#  Output:
#
#    integer P(1:N+1), P(I+1) is the number of partitions of I.
#
  import numpy as np

  p = np.zeros ( n + 1 )

  p[0] = 1

  if ( n <= 0 ):
    return p

  p[1] = 1

  for i in range ( 2, n + 1 ):
 
    sign = 1
    psum = 0
    w = 1
    j = 1
    wprime = w + j

    while ( w < n ):

      if ( 0 <= i - w ):
        if ( sign == 1 ):
          psum = psum + p[i-w];
        else:
          psum = psum - p[i-w];

      if ( wprime <= i ):

        if ( sign == 1 ):
          psum = psum + p[i-wprime]
        else:
          psum = psum - p[i-wprime]

      w = w + 3 * j + 1
      j = j + 1
      wprime = w + j
      sign = - sign

    p[i] = psum

  return p

def part_table_test ( ):

#*****************************************************************************80
#
## part_table_test() tests part_table().
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
  maxn = 10
  maxpart = 5

  print ( '' )
  print ( 'part_table_test():' )
  print ( '  part_table() tabulates partitions of N.' )

  p = part_table ( maxn )

  i4vec_print ( maxn + 1, p, '    I      P(I)' )

  return

def perm_check ( n, p ):

#*****************************************************************************80
#
## perm_check() checks that a vector represents a permutation.
#
#  Discussion:
#
#    The routine verifies that each of the integers from 1
#    to N occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
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
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  for seek in range ( 1, n + 1 ):

    check = False

    for find in range ( 0, n ):
      if ( p[find] == seek ):
        check = True
        break

    if ( not check ):
      return check

  return check

def perm_check_test ( ):

#*****************************************************************************80
#
## perm_check_test() tests perm_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'perm_check_test():' )
  print ( '  perm_check() checks a permutation.' )
  
  for test in range ( 1, 4 ):

    if ( test == 1 ):
      n = 5
      s = np.array ( [ 5, 1, 8, 3, 4 ] )
    elif ( test == 2 ):
      n = 5
      s = np.array ( [ 5, 1, 4, 3, 4 ] )
    elif ( test == 3 ):
      n = 5
      s = np.array ( [ 5, 1, 2, 3, 4 ] )

    check = perm_check ( n, s )
    i4vec_transpose_print ( n, s, '  Permutation:' )
    print ( '  Check = %s' % ( check ) )

  return

def perm_enum ( n ):

#*****************************************************************************80
#
## perm_enum() enumerates the permutations on N digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be nonnegative.
#
#  Output:
#
#    integer NPERM, the number of distinct elements.
#
  from math import factorial

  nperm = factorial ( n )

  return nperm

def perm_enum_test ( ):

#*****************************************************************************80
#
## perm_enum_test() tests perm_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'perm_enum_test():' )
  print ( '  perm_enum() enumerates permutations of N items.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    perm_num = perm_enum ( n )
    print ( '  %2d  %6d' % ( n, perm_num ) )

  return

def perm_inv ( n, p ):

#*****************************************************************************80
#
## perm_inv() computes the inverse of a permutation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#  Output:
#
#    integer PINV(N), the inverse permutation.
#
  import numpy as np
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_inv(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_inv(): Fatal error!' )

  pinv = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    pinv[p[i]-1] = i + 1

  return pinv

def perm_inv_test ( ):

#*****************************************************************************80
#
## perm_inv_test() tests perm_inv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'perm_inv_test():' )
  print ( '  perm_inv() computes an inverse permutation.' )

  p = np.array ( [ 3, 1, 2, 4 ], dtype = np.int32 )
  perm_print ( n, p, '  The permutation P:' )

  q = perm_inv ( n, p )

  perm_print ( n, q, '  The inverse permutation Q:' )

  r = perm_mul ( n, p, q )

  perm_print ( n, r, '  The product R = P * Q:' )

  return

def perm_lex_rank ( n, p ):

#*****************************************************************************80
#
## perm_lex_rank() computes the lexicographic rank of a permutation.
#
#  Discussion:
#
#    The original code altered the input permutation.  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#  Output:
#
#    integer RANK, the rank of the permutation.
#
  from math import factorial
  import numpy as np
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_lex_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_lex_rank(): Fatal error!' )

  p2 = np.zeros ( n )
  for i in range ( 0, n ):
    p2[i] = p[i]

  rank = 0

  for j in range ( 0, n ):

    rank = rank + ( p2[j] - 1 ) * factorial ( n - j )

    for i in range ( j + 1, n ):
      if ( p2[j] < p2[i] ):
        p2[i] = p2[i] - 1

  return rank

def perm_lex_rank_test ( ):

#*****************************************************************************80
#
## perm_lex_rank_test() tests perm_lex_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'perm_lex_rank_test():' )
  print ( '  perm_lex_rank() ranks' )
  print ( '  permutations using the lexicographic ordering.' )

  p = np.array ( [ 3, 1, 2, 4 ] )
  perm_print ( n, p, '  Element to be ranked:' )

  rank = perm_lex_rank ( n, p )
  print ( '' )
  print ( '  The rank is computed to be %d.' % ( rank ) )

  return

def perm_lex_successor ( n, p, rank ):

#*****************************************************************************80
#
## perm_lex_successor() computes the lexicographic permutation successor.
#
#  Example:
#
#    RANK  Permutation
#
#       0  1 2 3 4
#       1  1 2 4 3
#       2  1 3 2 4
#       3  1 3 4 2
#       4  1 4 2 3
#       5  1 4 3 2
#       6  2 1 3 4
#       ...
#      23  4 3 2 1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), the input permutation.
#
#    integer RANK, the rank of the input permutation.
#    If RANK = -1, then the input permutation is ignored, and the
#    function returns the first permutation in the ordered list,
#    with RANK = 1.
#
#  Output:
#
#    integer P(N), the successor permutation.  
#    If the input permutation was the last in the ordered list,
#    then the output permutation is the first permutation.
#
#    integer RANK, the rank of the output permutation.
#
  import numpy as np
#
#  If RANK <= -1, return the first permutation.
#
  if ( rank <= -1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
    return p, rank
#
#  Make sure the input permutation is legal.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_lex_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_lex_successor(): Fatal error!' )
#
#  Seek I, the highest index for which the next element is bigger.
#
  i = n - 2

  while ( True ):

    if ( i < 0 ):
      break

    if ( p[i] <= p[i+1] ):
      break

    i = i - 1
#
#  If no I could be found, then we have reach the final permutation,
#  N, N-1, ..., 2, 1.  Time to start over again.
#
  if ( i == -1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
  else:
#
#  Otherwise, look for the the highest index after I whose element
#  is bigger than I's.  We know that I+1 is one such value, so the
#  loop will never fail.
#
    j = n - 1
    while ( p[j] < p[i] ):
      j = j - 1
#
#  Interchange elements I and J.
#
    t    = p[i]
    p[i] = p[j]
    p[j] = t
#
#  Reverse the elements between indices I+1 and N-1.
#
    p[i+1:n] = p[n-1:i:-1]

    rank = rank + 1

  return p, rank

def perm_lex_successor_test ( ):

#*****************************************************************************80
#
## perm_lex_successor_test() tests perm_lex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'perm_lex_successor_test():' )
  print ( '  perm_lex_successor() lists' )
  print ( '  permutations using the lexicographic ordering.' )

  p = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    p, rank = perm_lex_successor ( n, p, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, p, '' )

  return

def perm_lex_unrank ( rank, n ):

#*****************************************************************************80
#
## perm_lex_unrank() computes the permutation of given lexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the permutation.
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#  Output:
#
#    integer P(N), describes the permutation.
#
  from math import factorial
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'perm_lex_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'perm_lex_unrank(): Fatal error!' )

  nperm = perm_enum ( n )

  if ( rank < 0 or nperm < rank ):
    print ( '' )
    print ( 'perm_lex_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'perm_lex_unrank(): Fatal error!' )

  p = np.zeros ( n )

  p[n-1] = 1

  for j in range ( 1, n ):

    d = ( rank % factorial ( j + 1 ) ) // factorial ( j )
    rank = rank - d * factorial ( j )
    p[n-1-j] = d + 1

    for i in range ( n - j, n ):

      if ( d < p[i] ):
        p[i] = p[i] + 1

  return p

def perm_lex_unrank_test ( ):

#*****************************************************************************80
#
## perm_lex_unrank_test() tests perm_lex_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4

  print ( '' )
  print ( 'perm_lex_unrank_test():' )
  print ( '  perm_lex_unrank() unranks' )
  print ( '  permutations using the lexicographic ordering.' )

  rank = 12

  p = perm_lex_unrank ( rank, n )

  perm_print ( n, p, '  The element of rank 12:' )

  return

def perm_mul ( n, p, q ):

#*****************************************************************************80
#
## perm_mul() computes the product of two permutations.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,inson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), Q(N), describes the permutation factors.
#
#  Output:
#
#    integer R(N), the product permutation P * Q.
#    R(I) = P(Q(I)).
#
  import numpy as np
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_mul(): Fatal error!' )
    print ( '  The input array P is illegal.' )
    raise Exception ( 'perm_mul(): Fatal error!' )

  check = perm_check ( n, q )

  if ( not check ):
    print ( '' )
    print ( 'perm_mul(): Fatal error!' )
    print ( '  The input array Q is illegal.' )
    raise Exception ( 'perm_mul(): Fatal error!' )

  r = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    r[i] = p[q[i]-1]

  return r

def perm_mul_test ( ):

#*****************************************************************************80
#
## perm_mul_test() tests perm_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'perm_mul_test():' )
  print ( '  perm_mul() multiplies two permutations.' )

  p = np.array ( [ 3, 1, 2, 4 ], dtype = np.int32 )
  perm_print ( n, p, '  The permutation P:' )

  q = np.array ( [ 2, 3, 1, 4 ], dtype = np.int32 )
  perm_print ( n, q, '  The permutation Q:' )
#
#  Multiply.
#
  r = perm_mul ( n, p, q )
  perm_print ( n, r, '  The product R = P * Q:' )

  return

def perm_parity ( n, p ):

#*****************************************************************************80
#
## perm_parity() computes the parity of a permutation.
#
#  Discussion:
#
#    The routine requires the use of a temporary array.
#
#    A permutation is called "even" or "odd", depending on whether
#    it is equivalent to an even or odd number of pairwise 
#    transpositions.  This is known as the "parity" of the 
#    permutation.
#
#    The "sign" of a permutation is +1 if it has even parity,
#    and -1 if it has odd parity.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#  Output:
#
#    integer PARITY, the parity of the permutation.
#    0, the permutation has even parity.
#    1, the permutation has odd parity.
#
  import numpy as np
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_parity(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_parity(): Fatal error!' )

  a = np.zeros ( n, dtype = np.int32 )

  c = 0

  for j in range ( 1, n + 1 ):

    if ( a[j-1] == 0 ):

      c = c + 1
      a[j-1] = 1
      i = j

      while ( p[i-1] != j ):
        i = p[i-1]
        a[i-1] = 1

  parity = ( ( n - c ) % 2 )

  return parity

def perm_parity_test ( rng ):

#*****************************************************************************80
#
## perm_parity_test() tests perm_parity().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'perm_parity_test():' )
  print ( '  perm_parity() computes the parity of a permutation.' )

  n = 5
 
  for test in range ( 0, 5 ):
    p = perm_random ( n, rng )
    perm_print ( n, p, '  The permutation P:' )
    parity = perm_parity ( n, p )
    print ( '' )
    print ( '  The parity is %d' % ( parity ) )

  return

def perm_print ( n, p, title ):

#*****************************************************************************80
#
## perm_print() prints a permutation of (1,...,N).
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

def perm_print_test ( ):

#*****************************************************************************80
#
## perm_print_test() tests perm_print().
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
  print ( 'perm_print_test():' )
  print ( '  perm_print() prints a permutation of (1,...,N).' )

  n = 7
  p = np.array ( [ 7, 2, 4, 1, 5, 3, 6 ] )
  perm_print ( n, p, '  A 1-based permutation:' )

  return

def perm_random ( n, rng ):

#*****************************************************************************80
#
## perm_random() selects a random permutation of 1, ..., N.
#
#  Discussion:
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
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
#    integer N, the number of objects to be permuted.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P(N), a permutation of ( 1, 2, ..., N ), in standard
#    index form.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p[i] = i + 1

  for i in range ( 0, n - 1 ):

    j = rng.integers ( low = i, high = n, endpoint = False )

    temp = p[i]
    p[i] = p[j]
    p[j] = temp

  return p

def perm_random_test ( rng ):

#*****************************************************************************80
#
## perm_random_test() tests perm_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'perm_random_test():' )
  print ( '  perm_random() randomly selects a permutation of 1, ..., N.' )
  print ( '' )

  for test in range ( 0, 5 ):

    p = perm_random ( n, rng )

    i4vec_transpose_print ( n, p, '' )

  return

def perm_tj_rank ( n, p ):

#*****************************************************************************80
#
## perm_tj_rank() computes the Trotter-Johnson rank of a permutation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#  Output:
#
#    integer RANK, the rank of the permutation.
#

#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_tj_rank(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_tj_rank(): Fatal error!' )

  rank = 0

  for j in range ( 2, n + 1 ):

    k = 1
    i = 0

    while ( p[i] != j ):
      if ( p[i] < j ):
        k = k + 1
      i = i + 1
    
    if ( ( rank % 2 ) == 0 ):
      rank = j * rank + j - k
    else:
      rank = j * rank + k - 1

  return rank

def perm_tj_rank_test ( ):

#*****************************************************************************80
#
## perm_tj_rank_test() tests perm_tj_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'perm_tj_rank_test():' )
  print ( '  perm_tj_rank() ranks' )
  print ( '  permutations using the Trotter-Johnson ordering.' )

  p = np.array ( [ 4, 3, 2, 1 ] )
  perm_print ( n, p, '  Element to be ranked:' )

  rank = perm_tj_rank ( n, p )
  print ( '' )
  print ( '  The rank is computed to be %d.' % ( rank ) )

  return

def perm_tj_successor ( n, p, rank ):

#*****************************************************************************80
#
## perm_tj_successor() computes the Trotter-Johnson permutation successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 January 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.  
#
#  Output:
#
#    integer P(N), describes the successor permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  import numpy as np
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
    return p, rank
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_tj_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_tj_successor(): Fatal error!' )

  st = 0

  q = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    q[i] = p[i]
  done = False
  m = n

  while ( 1 < m and not done ):

    d = 1
    while ( q[d-1] != m ):
      d = d + 1

    for i in range ( d, m ):
      q[i-1] = q[i]

    par = perm_parity ( m - 1, q )

    if ( par == 1 ):

      if ( d == m ):
        m = m - 1
      else:
        t           = p[st+d-1]
        p[st+d-1]   = p[st+d+1-1]
        p[st+d+1-1] = t
        done = True

    else:

      if ( d == 1 ):
        m = m - 1
        st = st + 1
      else:
        t             = p[st+d-1]
        p[st+d-1]     = p[st+d-1-1]
        p[st+d-1-1]   = t
        done = True
#
#  Last element was input.  Return first one.
#
  if ( m == 1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
    return p, rank

  rank = rank + 1

  return p, rank

def perm_tj_successor_test ( ):

#*****************************************************************************80
#
## perm_tj_successor_test() tests perm_tj_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'perm_tj_successor_test():' )
  print ( '  perm_tj_successor() lists' )
  print ( '  permutations using the Trotter-Johnson ordering.' )

  p = np.zeros ( n, dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    p, rank = perm_tj_successor ( n, p, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, p, '' )

  return

def perm_tj_unrank ( rank, n ):

#*****************************************************************************80
#
## perm_tj_unrank() computes the permutation of given Trotter-Johnson rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the permutation.
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#  Output:
#
#    integer P(N), describes the permutation.
#
  from math import factorial
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'perm_tj_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'perm_tj_unrank(): Fatal error!' )

  nperm = perm_enum ( n )

  if ( rank < 0 or nperm < rank ):
    print ( '' )
    print ( 'perm_tj_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'perm_tj_unrank(): Fatal error!' )

  p = np.zeros ( n, dtype = np.int32 )

  p[0] = 1
  r2 = 0

  for j in range ( 2, n + 1 ):
#
#  Replace this ratio of factorials!
#
    r1 = ( rank * factorial ( j ) ) // factorial ( n )
    k = r1 - j * r2

    if ( ( r2 % 2 ) == 0 ):
      jhi = j - k
    else:
      jhi = k + 1

    for i in range ( j - 1, jhi - 1, -1 ):
      p[i] = p[i-1]
    p[jhi-1] = j

    r2 = r1

  return p

def perm_tj_unrank_test ( ):

#*****************************************************************************80
#
## perm_tj_unrank_test() tests perm_tj_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4

  print ( '' )
  print ( 'perm_tj_unrank_test():' )
  print ( '  perm_tj_unrank() unranks' )
  print ( '  permutations using the Trotter-Johnson ordering.' )

  rank = 12

  p = perm_tj_unrank ( rank, n )

  perm_print ( n, p, '  The element of rank 12:' )

  return

def perm_to_cycle ( n, p ):

#*****************************************************************************80
#
## perm_to_cycle() converts a permutation from array to cycle form.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation using a
#    single array.  For each index I, I -> P(I).
#
#  Output:
#
#    integer NCYCLE, the number of cycles.
#    1 <= NCYCLE <= N.
#
#    integer T(N), INDEX(N), describes the permutation
#    as a collection of NCYCLE cycles.  The first cycle is
#    T(1) -> T(2) -> ... -> T(INDEX(1)) -> T(1).
#
  import numpy as np
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'perm_to_cycle(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'perm_to_cycle(): Fatal error!' )
#
#  Initialize.
#
  ncycle = 0

  index = np.zeros ( n, dtype = np.int32 )
  t = np.zeros ( n, dtype = np.int32 )
  nset = 0
#
#  Find the next unused entry.      
#
  for i in range ( 1, n + 1 ):

    if ( 0 < p[i-1] ):

      ncycle = ncycle + 1
      index[ncycle-1] = 1

      nset = nset + 1
      t[nset-1] = p[i-1]
      p[i-1] = - p[i-1]

      while ( True ):

        j = t[nset-1]

        if ( p[j-1] < 0 ):
          break

        index[ncycle-1] = index[ncycle-1] + 1

        nset = nset + 1
        t[nset-1] = p[j-1]
        p[j-1] = - p[j-1]

  return ncycle, t, index

def perm_to_cycle_test ( ):

#*****************************************************************************80
#
## perm_to_cycle_test() tests perm_to_cycle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'perm_to_cycle_test():' )
  print ( '  perm_to_cycle() converts a permutation from' )
  print ( '  array to cycle form.' )

  n = 7
  p = np.array ( [ 4, 5, 1, 2, 3, 6, 7 ], dtype = np.int32 )
  perm_print ( n, p, '  Permutation:' )

  ncycle, t, index = perm_to_cycle ( n, p )

  print ( '' )
  print ( '  Corresponding cycle form:' )
  print ( '  Number of cycles is %d' % ( ncycle ) )
  print ( '' )
  jlo = 0
  for i in range ( 0, ncycle ):
    print ( '    ', end = '' )
    for j in range ( jlo, jlo + index[i] ):
      print ( '%4d' % ( t[j] ), end = '' )
    print ( '' )
    jlo = jlo + index[i]

  return

def pivot_sequence_check ( t ):

#*****************************************************************************80
#
## pivot_sequence_check() checks a pivot sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer t(n): a pivot sequence.
#
#  Output:
#
#    logical CHECK, error flag.
#    true, T is a pivot sequence.
#    false, T is not a legal pivot sequence.
#
  verbose = False
  check = True

  n = len ( t )

  for i in range ( 0, n ):

    if ( t[i] <= 0 ):

      if ( verbose ):
        print ( '' )
        print ( 'pivot_sequence_check(): Fatal error!' )
        print ( '  t(', i, ') =', t[i], ' <= 0' )

      check = False
      return check

    elif ( n - i < t[i] ):

      if ( verbose ):
        print ( '' )
        print ( 'pivot_seq_check(): Fatal error!' )
        print ( '  n - i = ', n - i, ' < t(', i, ') = ', t[i] )

      check = False
      return check

  return check

def pivot_sequence_check_test ( ):

#*****************************************************************************80
#
## pivot_sequence_check_test() tests pivot_sequence_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pivot_sequence_check test():' )
  print ( '  pivot_sequence_check() checks N and T.' )
  print ( '' )
  print ( '  Check?    T' )
  print ( '' )
  
  for test in range ( 0, 3 ):

    n = 5

    if ( test == 0 ):
      t = np.array ( [ 5, 3, 2, 2, 1 ], dtype = int )
    elif ( test == 1 ):
      t = np.array ( [ 5, 2, 2, 3, 1 ], dtype = int )
    elif ( test == 2 ):
      t = np.array ( [ 4, 3, 0, 2, 1 ], dtype = int )
 
    check = pivot_sequence_check ( t )

    print ( '  %5s :  ' % ( check ), end = '' )
    for i in range ( 0, n ):
      print ( '  ', t[i], end = '' )
    print ( '' )

  return

def pivot_sequence_enum ( n ):

#*****************************************************************************80
#
## pivot_sequence_enum() enumerates pivot sequences.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of pivot steps.
#
#  Output:
#
#    integer pivot_sequence_num: the number of pivot sequences of n steps.
#
  from math import factorial

  pivot_sequence_num = factorial ( n )

  return pivot_sequence_num

def pivot_sequence_enum_test ( ):

#*****************************************************************************80
#
## pivot_sequence_enum_test() tests pivot_sequence_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pivot_sequence_enum_test():' )
  print ( '  pivot_sequence_enum() enumerates pivot sequences of N steps.' )
  print ( '' )
  print ( '   N      #' )
  print ( '  ' )

  for n in range ( 0, 11 ):
    pivot_sequence_num = pivot_sequence_enum ( n )
    print ( '  %2d  %10d' % ( n, pivot_sequence_num ) )

  return

def pivot_sequence_random ( n, rng ):

#*****************************************************************************80
#
## pivot_sequence_random() selects a pivot sequence at random.
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
#    integer n: the number of steps.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    t(n): a randomly selected pivot_sequence.
#
  import numpy as np

  t = np.zeros ( n, dtype = int )

  for i in range ( 0, n ):
    t[i] = rng.integers ( low = 1, high = n - i, endpoint = True )

  return t

def pivot_sequence_random_test ( rng ):

#*****************************************************************************80
#
## pivot_sequence_random_test() tests pivot_sequence_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pivot_sequence_random_test():' )
  print ( '  pivot_sequence_random() randomly selects a pivot' )
  print ( '  sequence of N terms' )

  n = 5
  pivot_sequence_num = pivot_sequence_enum ( n )

  print ( '  Let n = ', n )
  print ( '  Number of possible pivot sequences is', pivot_sequence_num )

  print ( '' )

  for test in range ( 0, 10 ):

    t = pivot_sequence_random ( n, rng )
    for i in range ( 0, n ):
      print ( '  ', t[i], end = '' )
    print ( '' )

  return

def pivot_sequence_successor ( t ):

#*****************************************************************************80
#
## pivot_sequence_successor() computes the pivot sequence successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer t(n): the previous pivot sequence.
#    To initiate the routine, call with t=linspace(n,1,n).
#
#  Output:
#
#    integer t(n): the lexical successor of the input.
#
  import numpy as np
#
#  Check.
#
  check = pivot_sequence_check ( t )

  if ( not check ):
    print ( '' )
    print ( 'pivot_sequence_successor(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'pivot_sequence_successor(): Fatal error!' )
#
#  Find last entry that is less than its maximum value.
#
  n = len ( t )

  last = -1
  for i in range ( n - 1, -1, -1 ):
    if ( t[i] < n - i ):
      last = i
      break

  if ( last == -1 ):
    t = np.ones ( n, dtype = int )
  else:
    t[last] = t[last] + 1
    t[last+1:n] = 1

  return t

def pivot_sequence_successor_test ( ):

#*****************************************************************************80
#
## pivot_sequence_successor_test() tests pivot_sequence_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pivot_sequence_successor_test():' )
  print ( '  pivot_sequence_successor() lists pivot sequences of N items,' )
  print ( '  one at a time.' )

  n = 4
  t = np.linspace ( n, 1, n, dtype = int )
  pivot_sequence_num = pivot_sequence_enum ( n )

  for i in range ( 0, pivot_sequence_num ):

    t = pivot_sequence_successor ( t )
    for i in range ( 0, n ):
      print ( '  ', t[i], end = '' )
    print ( '' )

  return

def pruefer_check ( n, p ):

#*****************************************************************************80
#
## pruefer_check() checks a Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    integer P(N-2), the Pruefer code for the tree.
#
#  Output:
#
#    Output, bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 3 ):
    check = False
    return check

  for i in range ( 0, n - 2 ):
    if ( p[i] < 1 or n < p[i] ):
      check = False
      return check

  return check

def pruefer_check_test ( ):

#*****************************************************************************80
#
## pruefer_check_test() tests pruefer_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pruefer_check_test():' )
  print ( '  pruefer_check() checks a Pruefer code.' )
  print ( '' )
  print ( '     Check?   N      P(1:N-2)' )
  print ( '' )
  
  for test in range ( 1, 5 ):

    if ( test == 1 ):
      n = 2
      p = np.array ( [ ] )
    elif ( test == 2 ):
      n = 3
      p = np.array ( [ 1 ] )
    elif ( test == 3 ):
      n = 4
      p = np.array ( [ 5, 2 ] )
    elif ( test == 4 ):
      n = 5
      p = np.array ( [ 5, 1, 3 ] )

    check = pruefer_check ( n, p )
    print ( '      %5s  %2d:  ' % ( check, n ), end = '' )
    for i in range ( 0, n - 2 ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )

  return

def pruefer_enum ( n ):

#*****************************************************************************80
#
## pruefer_enum() enumerates the Pruefer codes on N-2 digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of digits in the code, plus 2.
#    N must be at least 3.
#
#  Output:
#
#    integer NCODE, the number of distinct elements.
#
  if ( n < 3 ):
    ncode = 1
  else:
    ncode = n ** ( n - 2 )

  return ncode

def pruefer_enum_test ( ):

#*****************************************************************************80
#
## pruefer_enum_test() tests pruefer_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pruefer_enum_test():' )
  print ( '  pruefer_enum() enumerates trees on N nodes, using the Pruefer code' )
  print ( '' )
  print ( '   N           #' )
  print ( '' )

  for n in range ( 0, 11 ):
    pruefer_num = pruefer_enum ( n )
    print ( '  %2d  %10d' % ( n, pruefer_num ) )

  return

def pruefer_random ( n, rng ):

#*****************************************************************************80
#
## pruefer_random() returns a random Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P(N-2), the random Pruefer code.
#
  p = rng.integers ( low = 1, high = n, size = n - 2, endpoint = True )

  return p

def pruefer_random_test ( rng ):

#*****************************************************************************80
#
## pruefer_random_test() tests pruefer_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  n = 6

  print ( '' )
  print ( 'pruefer_random_test():' )
  print ( '  pruefer_random() returns a random Pruefer code.' )

  for i in range ( 0, 10 ):

    p = pruefer_random ( n, rng )

    print ( p )

  return

def pruefer_rank ( n, p ):

#*****************************************************************************80
#
## pruefer_rank() ranks a Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    integer P(N-2), the Pruefer code for the tree.
#
#  Output:
#
#    integer RANK, the rank of the Pruefer code.
#

#
#  Check.
#
  check = pruefer_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'pruefer_rank(): Fatal error!' )
    print ( '  Input array is illegal.' )
    raise Exception ( 'pruefer_rank(): Fatal error!' )

  rank = 0
  k = 1
  for i in range ( n - 3, -1, -1 ):
    rank = rank + k * ( p[i] - 1 )
    k = k * n

  return rank

def pruefer_rank_test ( ):

#*****************************************************************************80
#
## pruefer_rank_test() tests pruefer_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'pruefer_rank_test():' )
  print ( '  pruefer_rank() ranks Pruefer codes.' )

  p = np.array ( [ 3, 1 ] )
  i4vec_transpose_print ( n - 2, p, '  Element to be ranked:' )

  rank = pruefer_rank ( n, p )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )

  return

def pruefer_successor ( n, p, rank ):

#*****************************************************************************80
#
## pruefer_successor() computes the lexical Pruefer sequence successor.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    integer P(N-2), the Pruefer code for a tree.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer P(N-2), the Pruefer code for the successor tree.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  import numpy as np
#
#  Return the first element.
#
  if ( rank == -1 ):
    p = np.ones ( n - 2, dtype = np.int32 )
    rank = 0
    return p, rank
#
#  Check.
#
  check = pruefer_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'pruefer_successor(): Fatal error!' )
    print ( '  Input array is illegal.' )
    raise Exception ( 'pruefer_successor(): Fatal error!' )

  j = n - 3

  while ( True ):

    if ( p[j] != n ):
      break

    j = j - 1

    if ( j <= -1 ):
      break

  if ( j != -1 ):
    p[j] = p[j] + 1
    for i in range ( j + 1, n - 2 ):
      p[i] = 1
    rank = rank + 1
  else:
    p = np.ones ( n - 2, dtype = np.int32 )
    rank = 0

  return p, rank

def pruefer_successor_test ( ):

#*****************************************************************************80
#
## pruefer_successor_test() tests pruefer_successor().
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
  import numpy as np

  n = 4

  print ( '' )
  print ( 'pruefer_successor_test():' )
  print ( '  pruefer_successor() lists Pruefer codes.' )
  print ( '' )

  p = np.zeros ( n - 2, dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    p, rank = pruefer_successor ( n, p, rank )

    if ( rank <= rank_old ):
      break

    print ( '  %3d  ' % ( rank ), end = '' )
    for i in range ( 0, n - 2 ):
      print ( '%5d' % ( p[i] ), end = '' )
    print ( '' )

  return

def pruefer_to_tree ( n, p ):

#*****************************************************************************80
#
## pruefer_to_tree() converts a Pruefer code to a tree.
#
#  Discussion:
#
#    The original code attempts to tack on an extra entry to P.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    integer P(N-2), the Pruefer code for the tree.
#
#  Output:
#
#    integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
  import numpy as np
#
#  Check.
#
  check = pruefer_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'pruefer_to_tree(): Fatal error!' )
    print ( '  Input array is illegal.' )
    raise Exception ( 'pruefer_to_tree(): Fatal error!' )
#
#  Initialize the tree to 0.
#
  t = np.zeros ( [ 2, n - 1 ], dtype = np.int32 )

  d = np.ones ( n, dtype = np.int32 )

  for i in range ( 0, n - 2 ):
    d[p[i]-1] = d[p[i]-1] + 1

  for i in range ( 0, n - 1 ):

    x = n
    while ( d[x-1] != 1 ):
      x = x - 1

    if ( i == n - 2 ):
      y = 1
    else:
      y = p[i]

    d[x-1] = d[x-1] - 1
    d[y-1] = d[y-1] - 1

    t[0,i] = x
    t[1,i] = y

  return t

def pruefer_to_tree_test ( rng ):

#*****************************************************************************80
#
## pruefer_to_tree_test() tests pruefer_to_tree().
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
  import numpy as np

  n = 5
 
  print ( '' )
  print ( 'pruefer_to_tree_test():' )
  print ( '  pruefer_to_tree() converts a Pruefer code to a tree;' )

  pruefer_num = pruefer_enum ( n )

  for test in range ( 0, 5 ):
#
#  Pick a "random" Pruefer code.
#
    rank = rng.integers ( low = 0, high = pruefer_num, endpoint = False )

    p = pruefer_unrank ( rank, n )

    i4vec_print ( n - 2, p, '  Pruefer code' )
#
#  Convert the Pruefer code to a tree.
#
    t = pruefer_to_tree ( n, p )

    i4mat_print ( 2, n - 1, t, '  Edge list of tree:' )

  return

def pruefer_unrank ( rank, n ):

#*****************************************************************************80
#
## pruefer_unrank() unranks a Pruefer code.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the Pruefer code.
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#  Output:
#
#    integer P(N-2), the Pruefer code for the tree.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'pruefer_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'pruefer_unrank(): Fatal error!' )

  ncode = pruefer_enum ( n )

  if ( rank < 0 or ncode < rank ):
    print ( '' )
    print ( 'pruefer_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'pruefer_unrank(): Fatal error!' )

  p = np.zeros ( n - 2, dtype = np.int32 )

  for i in range ( n - 3, -1, -1 ):
    p[i] = ( rank % n ) + 1;
    rank = ( ( rank - p[i] + 1 ) ) // n;

  return p

def pruefer_unrank_test ( ):

#*****************************************************************************80
#
## pruefer_unrank_test() tests pruefer_unrank().
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
  n = 4

  print ( '' )
  print ( 'pruefer_unrank_test():' )
  print ( '  pruefer_unrank() unranks Pruefer codes.' )

  rank = 8

  p = pruefer_unrank ( rank, n )

  i4vec_transpose_print ( n - 2, p, '  The element of rank 8:' )

  return

def queens ( n, iarray, k, nstack, istack, maxstack ):

#*****************************************************************************80
#
## queens() finds possible positions for the K-th nonattacking queen.
#
#  Discussion:
#
#    The chessboard is N by N, and is being filled one column at a time,
#    with a tentative solution to the nonattacking queen problem.  So
#    far, K-1 rows have been chosen, and we now need to provide a list
#    of all possible rows that might be used in column K.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the total number of queens to place, and
#    the length of a side of the chessboard.
#
#    integer IARRAY(N).  The first K-1 entries of IARRAY
#    record the rows into which queens have already been placed.
#
#    integer K, the column for which we need possible
#    row positions for the next queen.
#
#    integer NSTACK, the current length of stack.
#    On output, this has been updated.
#
#    integer ISTACK(MAXSTACK).  On output, we have added
#    the candidates, and the number of candidates, to the end of the
#    stack.
#
#    integer MAXSTACK, maximum dimension of ISTACK.
#
#  Output:
#
#    integer NSTACK, the updated length of stack.
#
#    integer ISTACK(MAXSTACK), the updated stack.
#
  ncan = 0

  for irow in range ( 1, n + 1 ):
#
#  If row IROW has already been used, that is it.
#
    row = False

    for jcol in range ( 1, k ):
      if ( iarray[jcol-1] == irow ):
        row = True

    if ( not row ):

      diag = False

      for jcol in range ( 1, k ):
 
        if ( irow == ( iarray[jcol-1] + k - jcol ) or \
             irow == ( iarray[jcol-1] - ( k - jcol ) ) ):

          diag = True

      if ( not diag ):
        ncan = ncan + 1
        nstack = nstack + 1
        istack[nstack-1] = irow

  nstack = nstack + 1
  istack[nstack-1] = ncan

  return nstack, istack

def queens_test ( ):

#*****************************************************************************80
#
## queens_test() tests queens().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'queens_test():' )
  print ( '  queens() produces nonattacking queens' )
  print ( '  on a chessboard using a backtrack search.' )
  print ( '' )

  n = 8
  iarray = np.zeros ( n )
  indx = 0
  k = -1
  nstack = -1
  maxstack = n * n
  stack = np.zeros ( maxstack )

  while ( True ):

    n, iarray, indx, k, nstack, stack = backtrack ( n, iarray, \
      indx, k, nstack, stack, maxstack )

    if ( indx == 1 ):

      i4vec_transpose_print ( n, iarray, '' )

    elif ( indx == 2 ):

      nstack, stack = queens ( n, iarray, k, nstack, stack, maxstack )

    else:

      break

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

def rgf_check ( m, f ):

#*****************************************************************************80
#
## rgf_check() checks a restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    integer F(M), the restricted growth function.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( m <= 0 ):
    check = False
    return check

  fmax = 0
  for i in range ( 0, m ):
    if ( f[i] <= 0 or fmax + 1 < f[i] ):
      check = False
      return check
    fmax = max ( fmax, f[i] )

  return check

def rgf_check_test ( ):

#*****************************************************************************80
#
## rgf_check_test() tests rgf_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rgf_check_test():' )
  print ( '  rgf_check() checks a restricted growth function.' )
  
  for test in range ( 1, 5 ):

    if ( test == 1 ):
      m = -1
      f = np.array ( [] )
    elif ( test == 2 ):
      m = 7
      f = np.array ( [ 0, 1, 2, 3, 4, 5, 6 ] )
    elif ( test == 3 ):
      m = 7
      f = np.array ( [ 1, 3, 5, 8, 9, 10, 12 ] )
    elif ( test == 4 ):
      m = 7
      f = np.array ( [ 1, 2, 3, 1, 4, 5, 4 ] )

    check = rgf_check ( m, f )
    i4vec_transpose_print ( m, f, '  RGF:' )
    print ( '  Check = %s' % ( check ) )

  return

def rgf_enum ( m ):

#*****************************************************************************80
#
## rgf_enum() enumerates the restricted growth functions on M.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.  However, for the enumeration routine
#    only, it is legal to call with any value of M.
#
#  Output:
#
#    integer VALUE, the number of restricted growth functions.
#
  from scipy.special import comb
  import numpy as np

  if ( m < 0 ):

    value = 0

  elif ( m == 0 ):

    value = 1

  else:

    b = np.zeros ( m + 1 )
    b[0] = 1
    for j in range ( 1, m + 1 ):
      for i in range ( 0, j ):
        b[j] = b[j] + comb ( j - 1, i ) * b[i]

    value = b[m]

  return value

def rgf_enum_test ( ):

#*****************************************************************************80
#
## rgf_enum_test() tests rgf_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'rgf_enum_test():' )
  print ( '  rgf_enum() enumerates restricted growth functions.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    rgf_num = rgf_enum ( n )
    print ( '  %2d  %6d' % ( n, rgf_num ) )

  return

def rgf_g_table ( m ):

#*****************************************************************************80
#
## rgf_g_table() tabulates the generalized restricted growth functions.
#
#  Example:
#
#    M = 6
#
#    D =  1    1    1    1    1    1    1
#         1    2    3    4    5    6    0
#         2    5   10   17   26    0    0
#         5   15   37   77    0    0    0
#        15   52  151    0    0    0    0
#        52  203    0    0    0    0    0
#       203    0    0    0    0    0    0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, indicates how many rows and columns are to
#    be computed.  M must be nonnegative.
#
#  Output:
#
#    integer D(1:M+1,1:M+1), the first M+1 rows and
#    M+1 columns of the table of the number of generalized restricted growth
#    functions.  D(I+1,J+1) is the number of GRGF's of length I with restriction
#    parameter J.
#
  import numpy as np

  d = np.zeros ( [ m + 1, m + 1 ] )

  for j in range ( 0, m + 1 ):
    d[0,j] = 1

  for i in range ( 1, m + 1 ):
    for j in range ( 0, m + 1 ):
      if ( j <= m - i ):
        d[i,j] = j * d[i-1,j] + d[i-1,j+1]

  return d

def rgf_g_table_test ( ):

#*****************************************************************************80
#
## rgf_g_table_test() tests rgf_g_table().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  m = 6

  print ( '' )
  print ( 'rgf_g_table_test():' )
  print ( '  rgf_g_table() tabulates generalized restricted' )
  print ( '  growth functions.' )
  print ( '' )

  d = rgf_g_table ( m )

  for i in range ( 0, m + 1 ):
    for j in range ( 0, m - i + 1 ):
      print ( '%6d' % ( d[i,j] ), end = '' )
    print ( '' )

  return

def rgf_rank ( m, f ):

#*****************************************************************************80
#
## rgf_rank() ranks a restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    integer F(M), the restricted growth function.
#
#  Output:
#
#    integer RANK, the rank of the restricted growth
#    function.
#

#
#  Check.
#
  check = rgf_check ( m, f )

  if ( not check ):
    print ( '' )
    print ( 'rgf_rank(): Fatal error!' )
    print ( '  The input array is illegal!' )
    raise Exception ( 'rgf_rank(): Fatal error!' )
#
#  Get the generalized restricted growth function table.
#
  d = rgf_g_table ( m )

  rank = 0
  j = 1
  for i in range ( 2, m + 1 ):
    rank = rank + ( f[i-1] - 1 ) * d[m-i,j]
    j = max ( j, f[i-1] )

  return rank

def rgf_rank_test ( ):

#*****************************************************************************80
#
## rgf_rank_test() tests rgf_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4

  print ( '' )
  print ( 'rgf_rank_test():' )
  print ( '  rgf_rank() ranks restricted growth functions.' )

  f = np.array ( [ 1, 2, 1, 3 ] )
  i4vec_transpose_print ( m, f, '  Element to be ranked:' )

  rank = rgf_rank ( m, f )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )

  return

def rgf_successor ( m, f, rank ):

#*****************************************************************************80
#
## rgf_successor() generates the next restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    integer F(M), the restricted growth function.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer F(M), the successor restricted growth function.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, m ):
      f[i] = 1
    rank = 0
    return f, rank
#
#  Check.
#
  check = rgf_check ( m, f )

  if ( not check ):
    print ( '' )
    print ( 'rgf_successor(): Fatal error!' )
    print ( '  The input array is illegal!' )
    raise Exception ( 'rgf_successor(): Fatal error!' )
#
#  Find the first position from the right which can be incremented.
#
  for i in range ( m, 1, -1 ):
    fmax = 1
    for j in range ( 2, i ):
      fmax = max ( fmax, f[j-1] )
#
#  Increment the function at this position, and set later entries to 1.
#
    if ( f[i-1] != fmax + 1 ):
      f[i-1] = f[i-1] + 1
      for j in range ( i + 1, m + 1 ):
        f[j-1] = 1
      rank = rank + 1
      return f, rank
#
#  The final element was input.
#  Return the first element.
#
  for i in range ( 0, m ):
    f[i] = 1
  rank = 0

  return f, rank

def rgf_successor_test ( ):

#*****************************************************************************80
#
## rgf_successor_test() tests rgf_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4

  print ( '' )
  print ( 'rgf_successor_test():' )
  print ( '  rgf_successor() lists restricted growth functions.' )
  print ( '' )

  f = np.zeros ( m )
  rank = -1

  while ( True ):

    rank_old = rank

    f, rank = rgf_successor ( m, f, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( m, f, '' )

  return

def rgf_to_setpart ( m, f ):

#*****************************************************************************80
#
## rgf_to_setpart() converts a restricted growth function to a set partition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    integer F(M), the restricted growth function.
#
#  Output:
#
#    integer NSUB, the number of nonempty subsets into
#    which the set is partitioned.
#
#    integer S(M), describes the partition of a set of
#    M objects into NSUB nonempty subsets.  If element I of the
#    superset belongs to subset J, then S(I) = J.
#
#    integer INDEX(M), lists the location in S of the last
#    element of each subset.  Thus, the elements of subset 1
#    are S(1) through S(INDEX(1)), the elements of subset 2
#    are S(INDEX(1)+1) through S(INDEX(2)) and so on.
#
  import numpy as np
#
#  Check.
#
  check = rgf_check ( m, f )

  if ( not check ):
    print ( '' )
    print ( 'rgf_to_setpart(): Fatal error!' )
    print ( '  The input array is illegal!' )
    raise Exception ( 'rgf_to_setpart(): Fatal error!' )
#
#  Determine the number of subsets.
#
  nsub = max ( f )
#
#  Initialize.
#
  s = np.zeros ( m, dtype = np.int32 )
  index = np.zeros ( nsub, dtype = np.int32 )
#
#  For each subset I, collect the indices of F which have value I.
#  These are the elements of the I-th subset.
#
  k = 0
  for i in range ( 1, nsub + 1 ):
    for j in range ( 0, m ):
      if ( f[j] == i ):
        s[k] = j + 1
        k = k + 1
    index[i-1] = k

  return nsub, s, index

def rgf_to_setpart_test ( ):

#*****************************************************************************80
#
## rgf_to_setpart_test() tests rgf_to_setpart().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 8

  print ( '' )
  print ( 'rgf_to_setpart_test():' )
  print ( '  rgf_to_setpart() converts a balanced' )
  print ( '  sequence to a restricted growth function' )

  f = np.array ( [ 1, 1, 1, 1, 1, 2, 1, 3 ] )

  i4vec_transpose_print ( m, f,  '  Restricted growth function:' )
#
#  Convert the RGF to a set partition.
#
  nsub, s, index = rgf_to_setpart ( m, f )

  print ( '' )
  print ( '  Corresponding set partition:' )
  print ( '' )
  jlo = 0
  for i in range ( 0, nsub ):
    for j in range ( jlo, index[i] ):
      print ( '%4d' % ( s[j] ), end = '' )
    print ( '' )
    jlo = index[i]

  return

def rgf_unrank ( rank, m ):

#*****************************************************************************80
#
## rgf_unrank() returns the restricted growth function of a given rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the restricted growth
#    function.
#
#    integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#  Output:
#
#    integer F(M), the restricted growth function.
#
  import numpy as np
#
#  Check.
#
  if ( m < 1 ):
    print ( '' )
    print ( 'rgf_unrank(): Fatal error!' )
    print ( '  Input M is illegal.' )
    raise Exception ( 'rgf_unrank(): Fatal error!' )

  nrgf = rgf_enum ( m )

  if ( rank < 0 or nrgf < rank ):
    print ( '' )
    print ( 'rgf_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'rgf_unrank(): Fatal error!' )
#
#  Get the generalized restricted growth function table.
#
  d = rgf_g_table ( m )

  f = np.zeros ( m )
  j = 1
  f[0] = 1

  for i in range ( 2, m + 1 ):

    if ( j * d[m-i,j] <= rank ):
      f[i-1] = j + 1
      rank = rank - j * d[m-i,j]
      j = j + 1
    else:
      f[i-1] = 1 + ( rank // d[m-i,j] )
      rank = ( rank % d[m-i,j] )

  return f

def rgf_unrank_test ( ):

#*****************************************************************************80
#
## rgf_unrank_test() tests rgf_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  m = 4

  print ( '' )
  print ( 'rgf_unrank_test():' )
  print ( '  rgf_unrank() unranks restricted growth functions.' )

  rank = 7

  f = rgf_unrank ( rank, m )

  i4vec_transpose_print ( m, f, '  The element of rank 7' )

  return

def setpart_check ( m, nsub, s, index ):

#*****************************************************************************80
#
## setpart_check() checks a set partition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the number of elements of the set.
#    M must be positive.
#
#    integer NSUB, the number of nonempty subsets into
#    which the set is partitioned.  1 <= NSUB <= M.
#
#    integer S(M), contains the integers from 1 to M,
#    grouped into subsets as described by INDEX.
#
#    integer INDEX(NSUB), lists the location in S of the
#    last element of each subset.  Thus, the elements of subset 1
#    are S(1) through S(INDEX(1)), the elements of subset 2
#    are S(INDEX(1)+1) through S(INDEX(2)) and so on.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True
#
#  Check M.
#
  if ( m < 1 ):
    check = False
    return check
#
#  Check NSUB.
#
  if ( nsub < 1 or m < nsub ):
    check = False
    return check
#
#  Check INDEX.
#
  imin = 0
  for i in range ( 0, nsub ):
    if ( index[i] <= imin or m < index[i] ):
      check = False
      return check
    imin = index[i]
#
#  Check the elements of S.
#
  for i in range ( 0, m ):

    if ( s[i] <= 0 or m < s[i] ):
      check = False
      return check

    for j in range ( 0, i ):
      if ( s[j] == s[i] ):
        check = False
        return check

  return check

def setpart_check_test ( ):

#*****************************************************************************80
#
## setpart_check_test() tests setpart_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'setpart_check_test():' )
  print ( '  setpart_check() checks a set partition.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      m = 0
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 2 ):
      m = 8
      nsub = 0
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 3 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 8, 5 ] )
    elif ( test == 4 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 9, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 5 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 6, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 6 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )

    print ( '' )
    print ( '  The set partition' )
    print ( '  M = %d' % ( m ) )
    print ( '  NSUB = %d' % ( nsub ) )
    print ( '' )
    jlo = 0
    for i in range ( 0, nsub ):
      for j in range ( jlo, index[i] ):
        print ( '%4d' % ( s[j] ), end = '' )
      print ( '' )
      jlo = index[i]

    check = setpart_check ( m, nsub, s, index )
    print ( '  Check = %s' % ( check ) )

  return

def setpart_enum ( m ):

#*****************************************************************************80
#
## setpart_enum() enumerates the partitions of a set of M elements.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the number of elements in the set.
#    M must be positive.  However, for the enumeration routine only,
#    it is legal to call with any value of M.
#
#  Output:
#
#    integer NPART, the number of partitions of the set.
#
  from scipy.special import comb
  import numpy as np

  if ( m < 0 ):

    npart = 0

  elif ( m == 0 ):

    npart = 1

  else:

    b = np.zeros ( m + 1 )

    b[0] = 1
    for j in range ( 1, m + 1 ):
      b[j] = 0
      for i in range ( 0, j ):
        b[j] = b[j] + comb ( j - 1, i ) * b[i]

    npart = b[m]

  return npart

def setpart_enum_test ( ):

#*****************************************************************************80
#
## setpart_enum_test() tests setpart_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'setpart_enum_test():' )
  print ( '  setpart_enum() enumerates set partitions.' )
  print ( '' )
#
#  Enumerate.
#
  for n in range ( 1, 7 ):
    npart = setpart_enum ( n )
    print ( '  %4d  %4d' % ( n, npart ) )

  return

def setpart_to_rgf ( m, nsub, s, index ):

#*****************************************************************************80
#
## setpart_to_rgf() converts a set partition to a restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the number of elements of the set.
#    M must be positive.
#
#    integer NSUB, the number of nonempty subsets into
#    which the set is partitioned.  1 <= NSUB <= M.
#
#    integer INDEX(NSUB), lists the location in S of the
#    last element of each subset.  Thus, the elements of subset 1
#    are S(1) through S(INDEX(1)), the elements of subset 2
#    are S(INDEX(1)+1) through S(INDEX(2)) and so on.
#
#    integer S(M), contains the integers from 1 to M,
#    grouped into subsets as described by INDEX.
#
#  Output:
#
#    integer F(M), the restricted growth function from
#    M to NSUB.
#
  import numpy as np
#
#  Check.
#
  check = setpart_check ( m, nsub, s, index )

  if ( not check ):
    print ( '' )
    print ( 'setpart_to_rgf(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'setpart_to_rgf(): Fatal error!' )

  f = np.zeros ( m )

  khi = 0
  for i in range ( 0, nsub ):
    klo = khi + 1
    khi = index[i]
    for k in range ( klo, khi + 1 ):
      f[s[k-1]-1] = i + 1

  return f

def setpart_to_rgf_test ( ):

#*****************************************************************************80
#
## setpart_to_rgf_test() tests setpart_to_rgf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 8

  print ( '' )
  print ( 'setpart_to_rgf_test():' )
  print ( '  setpart_to_rgf() converts a set partition' )
  print ( '  to a restricted growth function.' )

  nsub = 3
  s = np.array ( [ 1, 2, 3, 4, 5, 6, 7, 8 ] )
  index = np.array ( [ 6, 7, 8 ] )

  print ( '' )
  print ( '  The set partition' )
  print ( '  M = %d' % ( m ) )
  print ( '  NSUB = %d' % ( nsub ) )
  print ( '' )
  jlo = 0
  for i in range ( 0, nsub ):
    for j in range ( jlo, index[i] ):
      print ( '%4d' % ( s[j] ), end = '' )
    print ( '' )
    jlo = index[i]
#
#  Convert the set partition back to an RGF.
#
  f = setpart_to_rgf ( m, nsub, s, index )

  i4vec_transpose_print ( m, f,  '  Recovered restricted growth function:' )

  return

def stirling_numbers1 ( m, n ):

#*****************************************************************************80
#
## stirling_numbers1() computes Stirling numbers of the first kind.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the maximum row to compute.
#    M must be nonnegative.
#
#    integer N, the maximum column to compute.
#    N must be nonnegative.
#
#  Output:
#
#    integer S(0:M,0:N), the first M+1 rows and N+1 columns
#    of the table of Stirling numbers of the first kind.
#
  import numpy as np

  s = np.zeros ( [ m + 1, n + 1 ] )

  s[0,0] = 1

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( j <= i ):
        s[i+1,j+1] = s[i,j] - i * s[i,j+1]

  return s

def stirling_numbers1_test ( ):

#*****************************************************************************80
#
## stirling_numbers1_test() tests stirling_numbers1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  maxm = 6
  maxn = 6
  offset = 1

  print ( '' )
  print ( 'stirling_numbers1_test():' )
  print ( '  stirling_numbers1() computes a table of Stirling' )
  print ( '  numbers of the first kind.' )

  s = stirling_numbers1 ( maxm, maxn )

  i4mat_print ( maxm + 1, maxn + 1, s, '  Stirling numbers:' )

  return

def stirling_numbers2 ( m, n ):

#*****************************************************************************80
#
## stirling_numbers2() computes Stirling numbers of the second kind.
#
#  Discussion:
#
#    The reference has a typographical error, referring to
#    S(I-J,J-1) instead of S(I-1,J-1).
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer M, the maximum row to compute.
#    M must be nonnegative.
#
#    integer N, the maximum column to compute.
#    N must be nonnegative.
#
#  Output:
#
#    integer S(1:M+1,1:N+1), the first M+1 rows and N+1 columns
#    of the table of Stirling numbers of the second kind.
#
  import numpy as np

  s = np.zeros ( [ m + 1, n + 1 ] )

  s[0,0] = 1

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( j <= i ):
        s[i+1,j+1] = ( j + 1 ) * s[i,j+1] + s[i,j]

  return s

def stirling_numbers2_test ( ):

#*****************************************************************************80
#
## stirling_numbers2_test() tests stirling_numbers2().
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
  maxm = 6
  maxn = 6
  offset = 1

  print ( '' )
  print ( 'stirling_numbers2_test():' )
  print ( '  stirling_numbers2() computes a table of Stirling' )
  print ( '  numbers of the second kind.' )

  s = stirling_numbers2 ( maxm, maxn )

  i4mat_print ( maxm + 1, maxn + 1, s, '  Stirling numbers:' )

  return

def subset_check ( n, t ):

#*****************************************************************************80
#
## subset_check() checks a subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(N), the subset.  If T(I) = 0, item I is
#    not in the subset; if T(I) = 1, item I is in the subset.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 1 ):
    check = False
    return check

  for i in range ( 0, n ):

    if ( t[i] != 0 and t[i] != 1 ):
      check = False
      return check

  return check

def subset_check_test ( ):

#*****************************************************************************80
#
## subset_check_test() tests subset_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'subset_check_test():' )
  print ( '  subset_check() checks a subset.' )
  
  for test in range ( 1, 4 ):

    if ( test == 1 ):
      n = 0
      s = np.array ( [] )
    elif ( test == 2 ):
      n = 3
      s = np.array ( [ 1, 2, 0 ] )
    elif ( test == 3 ):
      n = 5
      s = np.array ( [ 1, 0, 0, 1, 0 ] )

    check = subset_check ( n, s )
    i4vec_transpose_print ( n, s, '  Subset:' )
    print ( '  Check = %s' % ( check ) )

  return

def subset_colex_rank ( n, t ):

#*****************************************************************************80
#
## subset_colex_rank() computes the colexicographic rank of a subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of items in the master set.
#    N must be positive.
#
#    integer T(N), the subset.  If T(I) = 0, item I is
#    not in the subset; if T(I) = 1, item I is in the subset.
#
#  Output:
#
#    integer RANK, the rank of the subset.
#

#
#  Check.
#
  check = subset_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'subset_colex_rank(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_colex_rank(): Fatal error!\n' )

  rank = 0

  for i in range ( 0, n ):

    if ( t[i] == 1 ):
      rank = rank + 2 ** i

  return rank

def subset_colex_rank_test ( ):

#*****************************************************************************80
#
## subset_colex_rank_test() tests subset_colex_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'subset_colex_rank_test():' )
  print ( '  subset_colex_rank() ranks subsets of a set,' )
  print ( '  using the colexicographic ordering.' )

  t = np.array ( [ 0, 1, 0, 1, 0 ] )
  i4vec_transpose_print ( n, t, '  The element:' )

  rank = subset_colex_rank ( n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )

  return

def subset_colex_successor ( n, t, rank ):

#*****************************************************************************80
#
## subset_colex_successor() computes the subset colexicographic successor.
#
#  Discussion:
#
#    In the original code, there is a last element with no successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(N), describes a subset.  T(I) is 0 if
#    the I-th element of the master set is not in the subset, and is
#    1 if the I-th element is part of the subset.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(N), describes the successor subset.  
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      t[i] = 0
    rank = 0
    return t, rank
#
#  Check.
#
  check = subset_check ( n, t );

  if ( not check ):
    print ( '' )
    print ( 'subset_colex_successor(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_colex_successor(): Fatal error!\n' )

  for i in range ( 0, n ):

    if ( t[i] == 0 ):
      t[i] = 1
      rank = rank + 1
      return t, rank
    else:
      t[i] = 0

  rank = 0

  return t, rank

def subset_colex_successor_test ( ):

#*****************************************************************************80
#
## subset_colex_successor_test() tests subset_colex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'subset_colex_successor_test():' )
  print ( '  subset_colex_successor() lists subsets of a set,' )
  print ( '  using the colexicographic ordering.' )

  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = subset_colex_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, t, '' )

  return

def subset_colex_unrank ( rank, n ):

#*****************************************************************************80
#
## subset_colex_unrank() computes the subset of given colexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the subset.
#
#    integer N, the number of items in the master set.
#    N must be positive.
#
#  Output:
#
#    integer T(N), the subsetof the given rank.
#    If T(I) = 0, item I is not in the subset; if T(I) = 1, item I is
#    in the subset.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'subset_colex_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'subset_colex_unrank(): Fatal error!' )

  nsub = subset_enum ( n )

  if ( rank < 0 or nsub < rank ):
    print ( '' )
    print ( 'subset_colex_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'subset_colex_unrank(): Fatal error!' )

  t = np.zeros ( n )

  for i in range ( 0, n ):
    t[i] = ( rank % 2 )
    rank = ( rank // 2 )

  return t

def subset_colex_unrank_test ( ):

#*****************************************************************************80
#
## subset_colex_unrank_test() tests subset_colex_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'subset_colex_unrank_test():' )
  print ( '  subset_colex_unrank() unranks subsets of a set,' )
  print ( '  using the colexicographic ordering.' )

  rank = 10

  t = subset_colex_unrank ( rank, n )

  i4vec_transpose_print ( n, t, '  The subset of rank 10:' )

  return

def subset_complement ( n, a ):

#*****************************************************************************80
#
## subset_complement() computes the complement of a set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the order of the master set, of which A is
#    a subset.  N must be positive.
#
#    integer A(N), a subset of the master set.
#    A(I) = 0 if the I-th element is in the subset A, and is
#    1 otherwise.
#
#  Output:
#
#    integer B(N), the complement of A.
#
  import numpy as np
#
#  Check.
#
  check = subset_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'subset_complement(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_complement(): Fatal error!\n' )

  b = np.zeros ( n )

  b = 1 - a

  return b

def subset_complement_test ( rng ):

#*****************************************************************************80
#
## subset_complement_test() tests subset_complement().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_complement_test():' )
  print ( '  subset_complement() returns the complement of a subset.' )

  n = 5

  s1 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2 = subset_complement ( n, s1 )
  i4vec_transpose_print ( n, s2, '  S2 = complement of S1:' )

  return

def subset_distance ( n, t1, t2 ):

#*****************************************************************************80
#
## subset_distance() computes the Hamming distance between two sets.
#
#  Discussion:
#
#    The sets T1 and T2 are assumed to be subsets of a set of N elements.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the order of the master set, of which T1 and
#    T2 are subsets.  N must be positive.
#
#    integer T1(N), T2(N), two subsets of the master set.
#    T1(I) = 0 if the I-th element is in the subset T1, and is
#    1 otherwise T2 is defined similarly.
#
#  Output:
#
#    integer DIST, the Hamming distance between T1 and T2,
#    defined as the number of elements of the master set which are
#    in either T1 or T2 but not both.
#
  import numpy as np
#
#  Check.
#
  check = subset_check ( n, t1 )

  if ( not check ):
    print ( '' )
    print ( 'subset_distance(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_distance(): Fatal error!\n' )

  check = subset_check ( n, t2 )

  if ( not check ):
    print ( '' )
    print ( 'subset_distance(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_distance(): Fatal error!\n' )

  dist = np.sum ( abs ( t1 - t2 ) )

  return dist

def subset_distance_test ( rng ):

#*****************************************************************************80
#
## subset_distance_test() tests subset_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
# 
  print ( '' )
  print ( 'subset_distance_test():' )
  print ( '  subset_distance() returns the distance between two subsets.' )

  n = 10

  s1 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s2, '  Subset S2:' )

  d = subset_distance ( n, s1, s2 )
  print ( '' )
  print ( '  distance between S1 and S2 is %d' % ( d ) )

  return

def subset_enum ( n ):

#*****************************************************************************80
#
## subset_enum() enumerates the subsets of a set with N elements.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements in the set.
#    N must be at least 0.
#
#  Output:
#
#    integer NSUB, the number of distinct elements.
#
  nsub = 2 ** n

  return nsub

def subset_enum_test ( ):

#*****************************************************************************80
#
## subset_enum_test() tests subset_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_enum_test():' )
  print ( '  subset_enum() enumerates subsets of a set of N items.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    subset_num = subset_enum ( n )
    print ( '  %2d  %6d' % ( n, subset_num ) )

  return

def subset_intersect ( n, a, b ):

#*****************************************************************************80
#
## subset_intersect() computes the intersection of two sets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the order of the master set, of which A and
#    B are subsets.  N must be positive.
#
#    integer A(N), B(N), two subsets of the master set.
#    A(I) = 0 if the I-th element is in the subset A, and is
#    1 otherwise B is defined similarly.
#
#  Output:
#
#    integer C(N), the intersection of A and B.
#
  import numpy as np
#
#  Check.
#
  check = subset_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'subset_intersect(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_intersect(): Fatal error!' )

  check = subset_check ( n, b )

  if ( not check ):
    print ( '' )
    print ( 'subset_intersect(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_intersect- Fatal error!' )

  c = np.zeros ( n )
  for i in range ( 0, n ):
    c[i] = min ( a[i], b[i] )

  return c

def subset_intersect_test ( rng ):

#*****************************************************************************80
#
## subset_intersect_test() tests subset_intersect().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_intersect_test():' )
  print ( '  subset_intersect() returns the intersection of two subsets.' )

  n = 10

  s1 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s2, '  Subset S2:' )

  s3 = subset_intersect ( n, s1, s2 )
  i4vec_transpose_print ( n, s3, '  intersection S3:' )

  return

def subset_lex_rank ( n, t ):

#*****************************************************************************80
#
## subset_lex_rank() computes the lexicographic rank of a subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of items in the master set.
#    N must be positive.
#
#    integer T(N), the subset.  If T(I) = 0, item I is
#    not in the subset if T(I) = 1, item I is in the subset.
#
#  Output:
#
#    integer RANK, the rank of the subset.
#

#
#  Check.
#
  check = subset_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'subset_lex_rank(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_lex_rank(): Fatal error!' )

  rank = 0

  for i in range ( 0, n ):

    if ( t[i] == 1 ):
      rank = rank + 2 ** ( n - 1 - i )

  return rank

def subset_lex_rank_test ( ):

#*****************************************************************************80
#
## subset_lex_rank_test() tests subset_lex_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'subset_lex_rank_test():' )
  print ( '  subset_lex_rank() ranks subsets of a set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.array ( [ 0, 1, 0, 1, 0 ] )
  i4vec_transpose_print ( n, t, '  The element:' )

  rank = subset_lex_rank ( n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d' % ( rank ) )

  return

def subset_lex_successor ( n, t, rank ):

#*****************************************************************************80
#
## subset_lex_successor() computes the subset lexicographic successor.
#
#  Discussion:
#
#    In the original code, there is a last element with no successor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    integer T(N), describes a subset.  T(I) is 0 if
#    the I-th element of the master set is not in the subset, and is
#    1 if the I-th element is part of the subset.
#
#    integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer T(N), describes the successor subset.
#
#    integer RANK, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      t[i] = 0
    rank = 0
    return t, rank
#
#  Check.
#
  check = subset_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'subset_lex_successor(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_lex_successor(): Fatal error!' )

  for i in range ( n - 1, -1, -1 ):

    if ( t[i] == 0 ):
      t[i] = 1
      rank = rank + 1;
      return t, rank
    else:
      t[i] = 0

  rank = 0

  return t, rank

def subset_lex_successor_test ( ):

#*****************************************************************************80
#
## subset_lex_successor_test() tests subset_lex_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'subset_lex_successor_test():' )
  print ( '  subset_lex_successor() lists subsets of a set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = subset_lex_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, t, '' )

  return

def subset_lex_unrank ( rank, n ):

#*****************************************************************************80
#
## subset_lex_unrank() computes the subset of given lexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the subset.
#
#    integer N, the number of items in the master set.
#    N must be positive.
#
#  Output:
#
#    integer T(N), the subset of the given rank.
#    If T(I) = 0, item I is not in the subset; if T(I) = 1, item I is in
#    the subset.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'subset_lex_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'subset_lex_unrank(): Fatal error!' )

  nsub = subset_enum ( n );

  if ( rank < 0 or nsub < rank ):
    print ( '' )
    print ( 'subset_lex_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'subset_lex_unrank(): Fatal error!' )

  t = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    t[i] = ( rank % 2 )
    rank = ( rank // 2 )

  return t

def subset_lex_unrank_test ( ):

#*****************************************************************************80
#
## subset_lex_unrank_test() tests subset_lex_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#

  n = 5

  print ( '' )
  print ( 'subset_lex_unrank_test():' )
  print ( '  subset_lex_unrank() unranks subsets of a set,' )
  print ( '  using the lexicographic ordering.' )

  rank = 10

  t = subset_lex_unrank ( rank, n )

  i4vec_transpose_print ( n, t, '  The element of rank 10:' )

  return

def subset_random ( n, rng ):

#*****************************************************************************80
#
## subset_random() returns a random subset.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the set.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer S(N), defines the subset using 0 and 1 values.
#
  import numpy as np

  s = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

  return s

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
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_random_test():' )
  print ( '  subset_random() returns a random subset.' )

  n = 5

  for i in range ( 0, 10 ):
    s = subset_random ( n, rng )
    i4vec_transpose_print ( n, s, '  Subset:' )

  return

def subset_sum_swap ( n, a, sum_desired ):

#*****************************************************************************80
#
## subset_sum_swap() seeks a solution of the subset sum problem by swapping.
#
#  Discussion:
#
#    Given a collection of N not necessarily distinct positive integers A(I),
#    and a positive integer SUM_DESIRED, select a subset of the values so that
#    their sum is as close as possible to SUM_DESIRED without exceeding it.
#
#  Algorithm:
#
#    Start with no values selected, and SUM_ACHIEVED = 0.
#
#    Consider each element A(I):
#
#      If A(I) is not selected and SUM_ACHIEVED + A(I) <= SUM_DESIRED,
#        select A(I).
#
#      If A(I) is still not selected, and there is a selected A(J)
#      such that SUM_GOT < SUM_ACHIEVED + A(I) - A(J),
#        select A(I) and deselect A(J).
#
#      If no items were selected on this sweep,
#        end the search
#      Otherwise,
#        repeat the search.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of values.  N must be positive.
#
#    integer A(N), a collection of positive values.
#
#    integer SUM_dESIRED, the desired sum.
#
#  Output:
#
#    integer A(N), a collection of positive values, sorted into descending order.
#
#    integer INDEX(N) INDEX(I) is 1 if A(I) is part of the
#    sum, and 0 otherwise.
#
#    integer SUM_ACHIEVED, the sum of the selected elements.
#
  import numpy as np
#
#  Initialize.
#
  sum_achieved = 0

  index = np.zeros ( n )
#
#  Sort into descending order.
#
  np.sort ( a )
  np.flip ( a )

  while ( True ):

    nmove = 0

    for i in range ( 0, n ):

      if ( index[i] == 0 ):

        if ( sum_achieved + a[i] <= sum_desired ):
          index[i] = 1
          sum_achieved = sum_achieved + a[i]
          nmove = nmove + 1
          continue

      if ( index[i] == 0 ):

        for j in range ( 0, n ):

          if ( index[j] == 1 ):

            if ( sum_achieved < sum_achieved + a[i] - a[j] and \
              sum_achieved + a[i] - a[j] <= sum_desired ):
              index[j] = 0
              index[i] = 1
              nmove = nmove + 2
              sum_achieved = sum_achieved + a[i] - a[j]
              break

    if ( nmove <= 0 ):
      break

  return a, index, sum_achieved

def subset_sum_swap_test ( ):

#*****************************************************************************80
#
## subset_sum_swap_test() tests subset_sum_swap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 7

  sum_desired = 17

  print ( '' )
  print ( 'subset_sum_swap_test():' )
  print ( '  subset_sum_swap() seeks a solution of the subset' )
  print ( '  sum problem using pair swapping.' )
  print ( '' )
  print ( '  The desired sum is', sum_desired )

  a = np.array ( [ 12, 8, 11, 30, 8, 3, 7 ] )

  a, index, sum_achieved = subset_sum_swap ( n, a, sum_desired )

  print ( '' )
  print ( '    A(I), INDEX(I)' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %5d  %5d' % ( a[i], index[i] ) )

  print ( '' )
  print ( '  The achieved sum is %d' % ( sum_achieved ) )

  return

def subset_union ( n, a, b ):

#*****************************************************************************80
#
## subset_union() computes the union of two sets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the order of the master set, of which A and
#    B are subsets.  N must be positive.
#
#    integer A(N), B(N), two subsets of the master set.
#    A(I) = 0 if the I-th element is in the subset A, and is
#    1 otherwise B is defined similarly.
#
#  Output:
#
#    integer C(N), the union of A and B.
#
  import numpy as np
#
#  Check.
#
  check = subset_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'subset_union(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_union(): Fatal error!' )

  check = subset_check ( n, b )

  if ( not check ):
    print ( '' )
    print ( 'subset_union(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_union(): Fatal error!' )

  c = np.zeros ( n )
  for i in range ( 0, n ):
    c[i] = max ( a[i], b[i] )

  return c

def subset_union_test ( rng ):

#*****************************************************************************80
#
## subset_union_test() tests subset_union().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_union_test():' )
  print ( '  subset_union() returns the union of two subsets.' )

  n = 10

  s1 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s2, '  Subset S2:' )

  s3 = subset_union ( n, s1, s2 )
  i4vec_transpose_print ( n, s3, '  Union S3:' )

  return

def subset_weight ( n, t ):

#*****************************************************************************80
#
## subset_weight() computes the Hamming weight of a set.
#
#  Discussion:
#
#    The Hamming weight is simply the number of elements in the set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the order of the master set, of which T
#    is a subset.  N must be positive.
#
#    integer T(N), defines the subset T.
#    T(I) is 1 if I is an element of T, and 0 otherwise.
#
#  Output:
#
#    integer WEIGHT, the Hamming weight of the subset T.
#
  import numpy as np
#
#  Check.
#
  check = subset_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'subset_weight(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_weight(): Fatal error!' )

  weight = np.sum ( t )

  return weight

def subset_weight_test ( rng ):

#*****************************************************************************80
#
## subset_weight_test() tests subset_weight().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_weight_test():' )
  print ( '  subset_weight() returns the weight of a subset.' )

  n = 10

  s1 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  w = subset_weight ( n, s1 )
  print ( '' )
  print ( '  The weight of the subset is %d' % ( w ) )

  return

def subset_xor ( n, a, b ):

#*****************************************************************************80
#
## subset_xor() computes the symmetric difference of two sets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the order of the master set, of which A and
#    B are subsets.  N must be positive.
#
#    integer A(N), B(N), two subsets of the master set.
#    A(I) = 0 if the I-th element is in the subset A, and is
#    1 otherwise B is defined similarly.
#
#  Output:
#
#    integer C(N), the symmetric difference of A and B.
#
  import numpy as np
#
#  Check.
#
  check = subset_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'subset_xor(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_xor(): Fatal error!' )

  check = subset_check ( n, b )

  if ( not check ):
    print ( '' )
    print ( 'subset_xor(): Fatal error!' )
    print ( '  The subset is not legal.' )
    raise Exception ( 'subset_xor(): Fatal error!' )

  c = np.zeros ( n )
  for i in range ( 0, n ):
    c[i] = max ( a[i], b[i] ) - min ( a[i], b[i] )

  return c

def subset_xor_test ( rng ):

#*****************************************************************************80
#
## subset_xor_test() tests subset_xor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'subset_xor_test():' )
  print ( '  subset_xor() returns the exclusive OR of two subsets.' )

  n = 10

  s1 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2 = subset_random ( n, rng )
  i4vec_transpose_print ( n, s2, '  Subset S2:' )

  s3 = subset_xor ( n, s1, s2 )
  i4vec_transpose_print ( n, s3, '  S3 = S1 xor S2:' )

  return

def tableau_check ( n, tab ):

#*****************************************************************************80
#
## tableau_check() checks a 2 by N tableau.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of columns in the tableau.
#    N must be positive.
#
#    integer TAB(2,N), a 2 by N tableau.
#
#  Output:
#
#    bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 1 ):
    check = False
    return check
#
#  The entries must be between 1 and 2*N.
#
  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      if ( tab[i,j] < 1 or 2 * n < tab[i,j] ):
        check = False
        return check
#
#  The entries must be increasing to the right.
#
  for i in range ( 0, 2 ):
    for j in range ( 1, n ):
      if ( tab[i,j] <= tab[i,j-1] ):
        check = False
        return check
#
#  The entries must be increasing down.
#
  for j in range ( 0, n ):
    if ( tab[1,j] <= tab[0,j] ):
      check = False
      return check

  return check

def tableau_check_test ( ):

#*****************************************************************************80
#
## tableau_check_test() tests tableau_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'tableau_check_test():' )
  print ( '  tableau_check() checks a 2xN tableau.' )
  print ( '' )
  print ( '  Check?' )
  print ( '' )
  
  for test in range ( 1, 6 ):

    if ( test == 1 ):
      n = 0
      t = np.array ( [ \
        [ ],
        [ ] ] )
    elif ( test == 2 ):
      n = 4
      t = np.array ( [ \
        [ 1, 2, 3, 4 ], \
        [ 2, 4, 7, 9 ] ] )
    elif ( test == 3 ):
      n = 4
      t = np.array ( [ \
        [ 1, 3, 5, 3 ], \
        [ 2, 4, 5, 3 ] ] )
    elif ( test == 4 ):
      n = 4
      t = np.array ( [ \
        [ 1, 3, 4, 5 ], \
        [ 2, 4, 5, 3 ] ] )
    elif ( test == 5 ):
      n = 4
      t = np.array ( [ \
        [ 1, 3, 6, 7 ], \
        [ 3, 4, 7, 8 ] ] )

    print ( '' )
    check = tableau_check ( n, t )
    print ( '      Check = %2d' % ( check ) )
    i4mat_print ( 2, n, t, '  tableau:' )

  return

def tableau_enum ( n ):

#*****************************************************************************80
#
## tableau_enum() enumerates tableaus on N nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of nodes in each tree.
#    N must normally be at least 3, but for this routine,
#    any value of N is allowed.
#
#  Output:
#
#    integer VALUE, the number of 2 by N standard tableaus.
#
  from scipy.special import comb

  value = comb ( 2 * n, n ) / ( n + 1 )

  return value

def tableau_enum_test ( ):

#*****************************************************************************80
#
## tableau_enum_test() tests tableau_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tableau_enum_test():' )
  print ( '  tableau_enum() enumerates tableaus on N nodes.' )
  print ( '' )
  print ( '   N           #' )
  print ( '' )

  for n in range ( 0, 11 ):
    tableau_num = tableau_enum ( n )
    print ( '  %2d  %10d' % ( n, tableau_num ) )

  return

def tableau_to_bal_seq ( n, tab ):

#*****************************************************************************80
#
## tableau_to_bal_seq() converts a 2 by N tableau to a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    integer TAB(2,N), a 2 by N tableau.
#
#  Output:
#
#    integer T(2*N), a balanced sequence.
#
  import numpy as np
#
#  Check.
#
  check = tableau_check ( n, tab )

  if ( not check ):
    print ( '' )
    print ( 'tableau_to_bal_seq(): Fatal error!' )
    print ( '  The input array is illegal.' )
    raise Exception ( 'tableau_to_bal_seq(): Fatal error!' )

  t = np.zeros ( 2 * n )

  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      t[tab[i,j]-1] = i

  return t

def tableau_to_bal_seq_test ( ):

#*****************************************************************************80
#
## tableau_to_bal_seq_test() tests tableau_to_bal_seq().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'tableau_to_bal_seq_test():' )
  print ( '  tableau_to_bal_seq() converts a tableau' )
  print ( '  to a balanced sequence.' )

  tab = np.array ( [ \
    [ 1, 2, 5, 6 ], \
    [ 3, 4, 7, 8 ] ] )

  i4mat_print ( 2, n, tab, '  tableau:' )

  t = tableau_to_bal_seq ( n, tab )

  i4vec_transpose_print ( 2 * n, t, '  Balanced sequence:' )

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

def tree_check ( n, t ):

#*****************************************************************************80
#
## tree_check() checks a tree.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be positive.
#
#    integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
#  Output:
#
#    bool CHECK, error flag.
#    True, the data is legal.
#    False, the data is not legal.
#
  import numpy as np

  check = True

  if ( n < 1 ):
    check = False
    return check

  for i in range ( 0, 2 ):
    for j in range ( 0, n - 2 ):
      if ( t[i,j] < 1 or n < t[i,j] ):
        check = False
        return check
#
#  Compute the degree of each node.
#
  d = edge_degree ( n, n - 1, t )
#
#  Make a copy of T.
#
  t2 = np.zeros ( [ 2, n - 1 ], dtype = np.int32 )

  for i in range ( 0, 2 ):
    for j in range ( 0, n - 1 ):
      t2[i,j] = t[i,j]
#
#  Delete a node of degree 1, N-1 times.
#
  for k in range ( 0, n - 1 ):

    x = 1

    while ( d[x-1] != 1 ):

      x = x + 1

      if ( n < x ):
        check = False
        return check
#
#  Find its neighbor.
#
    j = 0

    while ( True ):

      if ( t2[0,j] == x ):
        y = t2[1,j]
        break

      if ( t2[1,j] == x ):
        y = t2[0,j]
        break

      j = j + 1

      if ( n - 2 < j ):
        check = False
        return check
#
#  Delete the edge.
#
    t2[0,j] = - t2[0,j]
    t2[1,j] = - t2[1,j]

    d[x-1] = d[x-1] - 1
    d[y-1] = d[y-1] - 1

  return True

def tree_check_test ( ):

#*****************************************************************************80
#
## tree_check_test() tests tree_check().
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
  import numpy as np

  print ( '' )
  print ( 'tree_check_test():' )
  print ( '  tree_check() checks a tree.' )
  print ( '' )
  print ( '  Check?   N    T(1:N)' )
  print ( '' )
  
  for test in range ( 1, 5 ):

    if ( test == 1 ):

      n = 0
      t = np.array ( [ \
        [], \
        [] ], dtype = np.int32 )

    elif ( test == 2 ):

      n = 3
      t = np.array ( [ \
        [ 1, 2 ], \
        [ 2, 3 ] ], dtype = np.int32 )

    elif ( test == 3 ):

      n = 5
      t = np.array ( [ 
        [ 1, 3, 4, 5 ], \
        [ 2, 4, 5, 3 ] ], dtype = np.int32 )

    elif ( test == 4 ):

      n = 6
      t = np.array ( [ \
        [ 1, 2, 3, 4, 5 ], \
        [ 3, 3, 4, 5, 6 ] ], dtype = np.int32 )

    print ( '' )
    check = tree_check ( n, t )
    print ( '      Check = %s' % ( check ) )
    i4mat_print ( 2, n - 1, t, '  Tree:' )

  return

def tree_enum ( n ):

#*****************************************************************************80
#
## tree_enum() enumerates the trees on N nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of nodes in each tree.
#    N must normally be at least 3, but for this routine,
#    any value of N is allowed.
#
#  Output:
#
#    integer NTREE, the number of distinct elements.
#
  if ( n < 1 ):
    ntree = 0
  elif ( n == 1 ):
    ntree = 1
  elif ( n == 2 ):
    ntree = 1
  else:
    ntree = n ** ( n - 2 )

  return ntree

def tree_enum_test ( ):

#*****************************************************************************80
#
## tree_enum_test() tests tree_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tree_enum_test():' )
  print ( '  tree_enum() enumerates trees on N nodes.' )
  print ( '' )
  print ( '   N           #' )
  print ( '' )

  for n in range ( 0, 11 ):
    tree_num = tree_enum ( n )
    print ( '  %2d  %10d' % ( n, tree_num ) )

  return

def tree_random ( n, rng ):

#*****************************************************************************80
#
## tree_random() randomly selects a tree on N nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#

#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'tree_random(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'tree_random(): Fatal error!' )
#
#  Compute the number of trees.
#
  tree_num = tree_enum ( n );
#
#  Choose RANK betweeen 1 and TREE_NUM.
#
  rank = rng.integers ( low = 1, high = tree_num, endpoint = True )
#
#  Compute the Pruefer code P of the given RANK.
#
  p = pruefer_unrank ( rank, n )
#
#  Convert the Pruefer code P to a tree T.
#
  t = pruefer_to_tree ( n, p )

  return t

def tree_random_test ( rng ):

#*****************************************************************************80
#
## tree_random_test() tests tree_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  n = 6

  print ( '' )
  print ( 'tree_random_test():' )
  print ( '  tree_random() randomly selects a tree on N nodes.' )

  for i in range ( 0, 10 ):
    t = tree_random ( n, rng )
    i4mat_print ( 2, n - 1, t, '  A random tree:' )

  return

def tree_rank ( n, t ):

#*****************************************************************************80
#
## tree_rank() ranks a tree.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
#  Output:
#
#    integer RANK, the rank of the tree.
#

#
#  Check the tree.
#
  check = tree_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'tree_rank(): Fatal error!' )
    print ( '  Input tree is illegal.' )
    raise Exception ( 'tree_rank(): Fatal error!' )
#
#  Convert the tree to a Pruefer code.
#
  p = tree_to_pruefer ( n, t )
#
#  Find the rank of the Pruefer code.
#
  rank = pruefer_rank ( n, p )

  return rank

def tree_rank_test ( ):

#*****************************************************************************80
#
## tree_rank_test() tests tree_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'tree_rank_test():' )
  print ( '  tree_rank() ranks trees.' )

  n = 4

  t = np.array ( [ \
    [ 4, 3, 3 ], \
    [ 1, 2, 1 ] ] )

  i4mat_print ( 2, n - 1, t, '  The element:' )

  rank = tree_rank ( n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )

  return

def tree_successor ( n, t, rank ):

#*****************************************************************************80
#
## tree_successor() returns the successor of a tree.
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
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    integer T(2,N-1), describes the edges of the
#    tree as pairs of nodes.  
#
#    integer RANK, the rank of the tree.
#
#  Output:
#
#    integer T(2,N-1), describes the edges of the
#    successor tree as pairs of nodes.  
#
#    integer RANK, the rank of the tree.
#
  import numpy as np
#
#  Return the first element.
#
  if ( rank == -1 ):
    p = np.ones ( n - 2, dtype = np.int32 )
    t = pruefer_to_tree ( n, p )
    rank = 0
    return t, rank
#
#  Check the tree.
#
  check = tree_check ( n, t );

  if ( not check ):
    print ( '' )
    print ( 'tree_successor(): Fatal error!' )
    print ( '  Input tree is illegal.' )
    raise Exception ( 'tree_successor(): Fatal error!' )
#
#  Convert the tree to a Pruefer code.
#
  p = tree_to_pruefer ( n, t )
#
#  Find the successor of the Pruefer code.
#
  p, rank = pruefer_successor ( n, p, rank )
#
#  Convert the Pruefer code to the tree.
#
  t = pruefer_to_tree ( n, p )

  return t, rank

def tree_successor_test ( ):

#*****************************************************************************80
#
## tree_successor_test() tests tree_successor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'tree_successor_test():' )
  print ( '  tree_successor() lists trees.' )

  t = np.array ( [ 2, n - 1 ], dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = tree_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    print ( '%5d  ' % ( rank ), end = '' )
    for j in range ( 0, n - 1 ):
      print ( '%5d' % ( t[0,j] ), end = '' )
    print ( '' )
    print ( '       ', end = '' )
    for j in range ( 0, n - 1 ):
      print ( '%5d' % ( t[1,j] ), end = '' )
    print ( '' )

  return

def tree_to_pruefer ( n, t ):

#*****************************************************************************80
#
## tree_to_pruefer() converts a tree to a Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of nodes in the tree.
#    N must be positive.
#
#    integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
#  Output:
#
#    integer P(N-2), the Pruefer code for the tree.
#
  import numpy as np
#
#  Check.
#
  check = tree_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'tree_to_pruefer(): Fatal error!' )
    print ( '  Input tree is illegal.' )
    raise Exception ( 'tree_to_pruefer(): Fatal error!' )
#
#  Compute the degree of each node.
#
  d = edge_degree ( n, n - 1, t )

  p = np.zeros ( n - 1, dtype = np.int32 )
#
#  Make a copy of T.
#
  t2 = np.zeros ( [ 2, n - 1 ], dtype = np.int32 )

  for i in range ( 0, 2 ):
    for j in range ( 0, n - 1 ):
      t2[i,j] = t[i,j]
#
#  Delete N-1 nodes of degree 1.
#
  for j in range ( 0, n - 2 ):
#
#  Find a node of degree 1.
#
    x = n
    while ( d[x-1] != 1 ):
      x = x - 1
#
#  Find its neighbor.
#
    k = 0

    while ( True ):

      if ( t2[0,k] == x ):
        y = t2[1,k]
        break

      if ( t2[1,k] == x ):
        y = t2[0,k]
        break

      k = k + 1
#
#  Store the neighbor.
#
    p[j] = y
#
#  Delete the edge from the tree.
#
    d[x-1] = d[x-1] - 1
    d[y-1] = d[y-1] - 1

    t2[0,k] = - t2[0,k]
    t2[1,k] = - t2[1,k]

  return p

def tree_to_pruefer_test ( rng ):

#*****************************************************************************80
#
## tree_to_pruefer_test() tests tree_to_pruefer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  test_num = 5

  print ( '' )
  print ( 'tree_to_pruefer_test():' )
  print ( '  tree_to_pruefer() converts a tree to a Pruefer code.' )

  pruefer_num = pruefer_enum ( n )

  for test in range ( 0, test_num ):
#
#  Pick a "random" Pruefer code.
#
    rank = rng.integers ( low = 0, high = pruefer_num, endpoint = False )

    p = pruefer_unrank ( rank, n )

    i4vec_transpose_print ( n - 2, p, '  Pruefer code:' )
#
#  Convert the Pruefer code to a tree.
#
    t = pruefer_to_tree ( n, p )

    i4mat_print ( 2, n - 1, t, '  Edge list for corresponding tree:' )
#
#  Convert the tree to a Pruefer code.
#
    p = tree_to_pruefer ( n, t )

    i4vec_transpose_print ( n - 2, p, '  Recovered Pruefer code:' )

  return

def tree_unrank ( rank, n ):

#*****************************************************************************80
#
## tree_unrank() unranks a tree.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the tree.
#
#    integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#  Output:
#
#    integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#

#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'tree_unrank(): Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'tree_unrank(): Fatal error!' )

  tree_num = tree_enum ( n );

  if ( rank < 0 or tree_num < rank ):
    print ( '' )
    print ( 'tree_unrank(): Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'tree_unrank(): Fatal error!' )
#
#  Unrank the Pruefer code.
#
  p = pruefer_unrank ( rank, n )
#
#  Convert the Pruefer code to a tree.
#
  t = pruefer_to_tree ( n, p )

  return t

def tree_unrank_test ( ):

#*****************************************************************************80
#
## tree_unrank_test() tests tree_unrank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  n = 4

  print ( '' )
  print ( 'tree_unrank_test():' )
  print ( '  tree_unrank() unranks trees.' )

  n = 4

  rank = 8

  t = tree_unrank ( rank, n )

  i4mat_print ( 2, n - 1, t, '  The element of rank 8:' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  combo_test ( )
  timestamp ( )

