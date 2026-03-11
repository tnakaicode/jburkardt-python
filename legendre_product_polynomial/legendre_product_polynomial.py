#! /usr/bin/env python3
#
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
#    integer VALUE, the number of compositions of N
#    into K parts.
#
  from scipy.special import comb

  value = comb ( n + k - 1, n )

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
    print ( 'comp_next_grlex - Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_next_grlex - Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ( '' )
      print ( 'comp_next_grlex - Fatal error!' )
      print ( '  XC[I] < 0' )
      raise Exception ( 'comp_next_grlex - Fatal error!' )
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
  print ( '  comp_next_grlex determines the next COMP in' )
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
#    integer KC, the number of parts in the composition.
#
#    integer RANK1, RANK2, the minimum and maximum ranks.
#    1 <= RANK1 <= RANK2.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer X[KC], the random composition.
#
#    integer RANK, the rank of the composition.
#
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_random_grlex(): Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_random_grlex(): Fatal error!' );
#
#  Ensure that 1 <= RANK1.
#
  if ( rank1 < 1 ):
    print ( '' )
    print ( 'comp_random_grlex - Fatal error!' )
    print ( '  RANK1 < 1' )
    raise Exception ( 'comp_random_grlex - Fatal error!' );
#
#  Ensure that RANK1 <= RANK2.
#
  if ( rank2 < rank1 ):
    print ( '' )
    print ( 'comp_random_grlex - Fatal error!' )
    print ( '  RANK2 < RANK1' )
    raise Exception ( 'comp_random_grlex - Fatal error!' )
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
#  Input:
#
#    rng(): the current random number generator.
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'comp_random_grlex_test():' )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  comp_random_grlex selects a random COMP in' )
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
#    int RANK, the rank of the composition.
#
  from scipy.special import comb
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_rank_grlex - Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_rank_grlex - Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ( '' )
      print ( 'comp_rank_grlex - Fatal error!' )
      print ( '  XC[I] < 0' )
      raise Exception ( 'comp_rank_grlex - Fatal error!' );
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
        rank = rank + comb ( ns - j, ks - i )

  for n in range ( 0, nc ):
    rank = rank + comb ( n + kc - 1, n )

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
  print ( '  comp_rank_grlex determines the rank of a COMP' )
  print ( '  from its parts.' )
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
#    int XC[KC], the composition XC of the given rank.
#    For each I, 0 <= XC[I] <= NC, and 
#    sum ( 1 <= I <= KC ) XC[I] = NC.
#
  from scipy.special import comb
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'comp_unrank_grlex - Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_unrank_grlex - Fatal error!' )
#
#  Ensure that 1 <= RANK.
#
  if ( rank < 1 ):
    print ( '' )
    print ( 'comp_unrank_grlex - Fatal error!' )
    print ( '  RANK < 1' )
    raise Exception ( 'comp_unrank_grlex - Fatal error!' )
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
    r = comb ( nc + kc - 1, nc )
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
  nksub = comb ( ns, ks )

  j = 1

  for i in range ( 1, ks + 1 ):
    r = comb ( ns - j, ks - i )
    while ( r <= rank2 and 0 < r ):
      rank2 = rank2 - r
      j = j + 1
      r = comb ( ns - j, ks - i )
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
  print ( '  comp_unrank_grlex determines the parts' )
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
    print ( 'i4vec_permute - Fatal error!' )
    print ( '  perm0_check rejects the permutation.' )
    raise Exception ( 'i4vec_permute - Fatal error!' )
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
          print ( 'i4vec_permute - Fatal error!' )
          print ( '  Entry IPUT = %d has' % ( iput ) )
          print ( '  an illegal value IGET = %d.' % (iget ) )
          raise Exception ( 'i4vec_permute - Fatal error!' )

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

  a = rng.integers ( low = 0, high = n, size = n, endpoint = True )

  i4vec_print ( n, a, '  A[*], before rearrangement:' )

  p = perm0_uniform ( n, rng )

  i4vec_print ( n, p, '  Permutation vector P[*]:' )

  a = i4vec_permute ( n, p, a )

  i4vec_print ( n, a, '  A[P[*]]:' )

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
  print ( 'i4vec_sort_heap_index_a_test()' )
  print ( '  i4vec_sort_heap_index_a() creates an ascending' )
  print ( '  sort index for an I4VEC.' )

  a = rng.integers ( low = 0, high = 3 * n, size = n, endpoint = True )

  i4vec_print ( n, a, '  Unsorted array A:' )

  indx = i4vec_sort_heap_index_a ( n, a )

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

def legendre_product_polynomial_test ( ):

#*****************************************************************************80
#
## legendre_product_polynomial_test() tests legendre_product_polynomial().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'legendre_product_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test legendre_product_polynomial().' )

  rng = default_rng ( )

  i4vec_permute_test ( rng )
  i4vec_sort_heap_index_a_test ( rng )

  r8vec_permute_test ( )

  perm0_uniform_test ( rng )

  comp_enum_test ( )
  comp_next_grlex_test ( )
  comp_random_grlex_test ( rng )
  comp_rank_grlex_test ( rng )
  comp_unrank_grlex_test ( )

  mono_next_grlex_test ( rng )
  mono_print_test ( )
  mono_rank_grlex_test ( )
  mono_unrank_grlex_test ( rng )
  mono_upto_enum_test ( )
  mono_upto_next_grlex_test ( )
  mono_upto_random_test ( rng )
  mono_value_test ( rng )

  polynomial_compress_test ( )
  polynomial_print_test ( )
  polynomial_sort_test ( )
  polynomial_value_test ( )

  lp_coefficients_test ( )
  lp_value_test ( )
  lp_values_test ( )

  lpp_to_polynomial_test ( )
  lpp_value_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_product_polynomial_test():' )
  print ( '  Normal end of execution.' )
  return

def lp_coefficients ( n ):

#*****************************************************************************80
#
## lp_coefficients(): coefficients of Legendre polynomials P(n,x).
#
#  First terms:
#
#     1
#     0     1
#    -1/2   0      3/2
#     0    -3/2    0     5/2
#     3/8   0    -30/8   0     35/8
#     0    15/8    0   -70/8    0     63/8
#    -5/16  0    105/16  0   -315/16   0    231/16
#     0   -35/16   0   315/16   0   -693/16   0    429/16
#
#     1.00000
#     0.00000  1.00000
#    -0.50000  0.00000  1.50000
#     0.00000 -1.50000  0.00000  2.5000
#     0.37500  0.00000 -3.75000  0.00000  4.37500
#     0.00000  1.87500  0.00000 -8.75000  0.00000  7.87500
#    -0.31250  0.00000  6.56250  0.00000 -19.6875  0.00000  14.4375
#     0.00000 -2.1875   0.00000  19.6875  0.00000 -43.3215  0.00000  26.8125
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
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    int N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#  Output:
#
#    int O, the number of coefficients.
#
#    double C[(N+2)/2], the coefficients of the Legendre
#    polynomial of degree N.
#
#    int F[(N+2)/2], the exponents.
#
  import numpy as np

  ctable = np.zeros ( ( n + 1, n + 1 ), dtype = np.float64 )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      ctable[i][j] = 0.0

  ctable[0][0] = 1.0

  if ( 0 < n ):
    ctable[1][1] = 1.0

    for i in range ( 2, n + 1 ):
      for j in range ( 0, i - 1 ):
        ctable[i][j] = ( - i + 1 ) * ctable[i-2][j] / i
      for j in range ( 1, i + 1 ):
        ctable[i][j] = ctable[i][j] + ( i + i - 1 ) * ctable[i-1][j-1] / i
#
#  Extract the nonzero data from the alternating columns of the last row.
#
  o = ( n + 2 ) // 2

  c = np.zeros ( o, dtype = np.float64 )
  f = np.zeros ( o, dtype = np.int32 )

  k = o
  for j in range ( n, -1, -2 ):
    k = k - 1
    c[k] = ctable[n][j]
    f[k] = j

  return o, c, f

def lp_coefficients_test ( ):

#*****************************************************************************80
#
## lp_coefficients_test() tests lp_coefficients().
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

  m = 1
  n_max = 10

  print ( '' )
  print ( 'lp_coefficients_test():' )
  print ( '  lp_coefficients(): coefficients of Legendre polynomial P(n,x).' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):

    o, c, f = lp_coefficients ( n )

    e = np.zeros ( o, dtype = np.int32 )

    for i in range ( 0, o ):
      e[i] = f[i] + 1

    label = '  P(' + repr ( n ) + ',x) = '
    polynomial_print ( m, o, c, e, label )

  return

def lpp_to_polynomial ( m, l, o_max ):

#*****************************************************************************80
#
## lpp_to_polynomial() writes a Legendre Product Polynomial as a polynomial.
#
#  Discussion:
#
#    For example, if 
#      M = 3,
#      L = ( 1, 0, 2, end = '' )
#    then
#      L(1,0,2)(X,Y,Z) 
#      = L(1)(X) * L(0)(Y) * L(2)(Z)
#      = X * 1 * ( 3Z^2-1)/2
#      = - 1/2 X + (3/2) X Z^2
#    so
#      O = 2 (2 nonzero terms)
#      C = -0.5
#           1.5
#      E = 4    <-- index in 3-space of exponent (1,0,0)
#          15   <-- index in 3-space of exponent (1,0,2)
#
#    The output value of O is no greater than
#      O_MAX = product ( 1 <= I <= M ) (L(I)+2)/2
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
#    int M, the spatial dimension.
#
#    int L[M], the index of each Legendre product 
#    polynomial factor.  0 <= L(*).
#
#    int O_MAX, an upper limit on the size of the 
#    output arrays.
#      O_MAX = product ( 1 <= I <= M ) (L(I)+2)/2.
#
#  Output:
#
#    int O, the "order" of the polynomial product.
#
#    double C[O], the coefficients of the polynomial product.
#
#    int E[O], the indices of the exponents of the 
#    polynomial product.
#
  import numpy as np

  c1 = np.zeros ( o_max, dtype = np.float64 )
  c2 = np.zeros ( o_max, dtype = np.float64 )
  e1 = np.zeros ( o_max, dtype = np.int32 )
  e2 = np.zeros ( o_max, dtype = np.int32 )
  f2 = np.zeros ( o_max, dtype = np.int32 )
  pp = np.zeros ( m, dtype = np.int32 )

  o1 = 1
  c1[0] = 1.0
  e1[0] = 1
#
#  Implicate one factor at a time.
#
  for i in range ( 0, m ):

    o2, c2, f2 = lp_coefficients ( l[i] );
 
    o = 0;
    c = np.zeros ( o_max, dtype = np.float64 )
    e = np.zeros ( o_max, dtype = np.int32 )

    for j2 in range ( 0, o2 ):
      for j1 in range ( 0, o1 ):
        c[o] = c1[j1] * c2[j2]
        if ( 0 < i ):
          p = mono_unrank_grlex ( i, e1[j1] )
        for i2 in range ( 0, i ):
          pp[i2] = p[i2]
        pp[i] = f2[j2]
        e[o] = mono_rank_grlex ( i + 1, pp )
        o = o + 1

    c, e = polynomial_sort ( o, c, e )
    o, c, e = polynomial_compress ( o, c, e )

    o1 = o;
    for i1 in range ( 0, o ):
      c1[i1] = c[i1]
      e1[i1] = e[i1]

  return o1, c1, e1

def lpp_to_polynomial_test ( ):

#*****************************************************************************80
#
## lpp_to_polynomial_test() tests lpp_to_polynomial().
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

  m = 2

  print ( '' )
  print ( 'lpp_to_polynomial_test():' )
  print ( '  lpp_to_polynomial() is given a Legendre product polynomial' )
  print ( '  and determines its polynomial representation.' )

  print ( '' )
  print ( '  Using spatial dimension M = %d' % ( m ) )

  for rank in range ( 1, 12 ):
    l = comp_unrank_grlex ( m, rank )

    o_max = 1
    for i in range ( 0, m ):
      o_max = o_max * ( l[i] + 2 ) // 2

    c = np.zeros ( o_max, dtype = np.float64 )
    e = np.zeros ( o_max, dtype = np.int32 )

    o, c, e = lpp_to_polynomial ( m, l, o_max )

    label = '  LPP #' + repr ( rank ) + ' = L(' + repr ( l[0] ) \
      + ',X)*L(' + repr ( l[1] ) + ',Y) = '

    print ( '' )
    polynomial_print ( m, o, c, e, label )

  return

def lpp_value ( m, n, o, x ):

#*****************************************************************************80
#
## lpp_value() evaluates a Legendre Product Polynomial at several points X.
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
#    int M, the spatial dimension.
#
#    int N, the number of evaluation points.
#
#    int O[M], the degree of the polynomial factors.
#    0 <= O(*).
#
#    double X[M][N], the evaluation points.
#
#  Output:
#
#    double V[N], the value of the Legendre Product 
#    Polynomial of degree O at the points X.
#
  import numpy as np

  v = np.zeros ( n, dtype = np.float64 )

  for j in range ( 0, n ):
    v[j] = 1.0

  xi = np.zeros ( n, dtype = np.float64 )
 
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      xi[j] = x[i][j]
    vi = lp_value ( n, o[i], xi )
    for j in range ( 0, n ):
      v[j] = v[j] * vi[j]

  return v

def lpp_value_test ( rng ):

#*****************************************************************************80
#
## lpp_value_test() tests lpp_value().
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'lpp_value_test():' )
  print ( '  lpp_value() evaluates a Legendre product polynomial.' )

  m = 3
  n = 1
  xlo = -1.0
  xhi = +1.0
  x = xlo + ( xhi - xlo ) * rng.random ( size = [ m, n ] )

  print ( '' )
  print ( '  Evaluate at X = ', end = '' )
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      print ( '%g  ' % ( x[i][j] ), end = '' )
  print ( '' )
  print ( '' )
  print ( '  Rank  I1  I2  I3:  L(I1,X1)*L(I2,X2)*L(I3,X3)    P(X1,X2,X3)' )
  print ( '' )

  for rank in range ( 1, 21 ):
    l = comp_unrank_grlex ( m, rank )
#
#  Evaluate the LPP directly.
#
    v1 = lpp_value ( m, n, l, x )
#
#  Convert the LPP to a polynomial.
#
    o_max = 1
    for i in range ( 0, m ):
      o_max = o_max * ( l[i] + 2 ) // 2
 
    o, c, e = lpp_to_polynomial ( m, l, o_max )
#
#  Evaluate the polynomial.
#
    v2 = polynomial_value ( m, o, c, e, n, x )
#
#  Compare results.
#
    print ( '  %4d  %2d  %2d  %2d  %14.6g  %14.6g' % \
      ( rank, l[0], l[1], l[2], v1[0], v2[0] ) )

  return

def lp_value ( n, o, x ):

#*****************************************************************************80
#
## lp_value() evaluates the Legendre polynomials P(n,x).
#
#  Discussion:
#
#    P(n,1) = 1.
#    P(n,-1) = (-1)^N.
#    | P(n,x) | <= 1 in [-1,1].
#
#    The N zeroes of P(n,x) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#    The Legendre polynomials are orthogonal under the inner product defined
#    as integration from -1 to 1:
#
#      Integral ( -1 <= X <= 1 ) P(I,X) * P(J,X) dX
#        = 0 if I =/= J
#        = 2 / ( 2*I+1 ) if I = J.
#
#    Except for P(0,X), the integral of P(I,X) from -1 to 1 is 0.
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#      C0*P(0,x) + C1*P(1,x) + ... + CN*P(n,x)
#    where
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I,x) dx.
#
#    The formula is:
#
#      P(n,x) = (1/2^N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Differential equation:
#
#    (1-X*X) * P(n,x)'' - 2 * X * P(n,x)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0,x) =      1
#    P( 1,x) =      1 X
#    P( 2,x) = (    3 X^2 -       1)/2
#    P( 3,x) = (    5 X^3 -     3 X)/2
#    P( 4,x) = (   35 X^4 -    30 X^2 +     3)/8
#    P( 5,x) = (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6,x) = (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7,x) = (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8,x) = ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9,x) = (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10,x) = (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63)/256
#
#  Recursion:
#
#    P(0,x) = 1
#    P(1,x) = x
#    P(n,x) = ( (2*n-1)*x*P(n-1,x)-(n-1)*P(n-2,x) ) / n
#
#    P'(0,x) = 0
#    P'(1,x) = 1
#    P'(N,x) = ( (2*N-1)*(P(N-1,x)+X*P'(N-1,x)-(N-1)*P'(N-2,x) ) / N
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
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    int N, the number of evaluation points.
#
#    int O, the degree of the polynomial.
#
#    double X[N], the evaluation points.
#
#  Output:
#
#    double V[N], the value of the Legendre polynomial 
#    of degree N at the points X.
#
  import numpy as np

  vtable = np.zeros ( [ n, o + 1 ], dtype = np.float64 )

  for i in range ( 0, n ):
    vtable[i][0] = 1.0

  if ( 1 <= o ):
    for i in range ( 0, n ):
      vtable[i][1] = x[i]

    for j in range ( 2, o + 1 ):
      for i in range ( 0, n ):
        vtable[i][j] = \
          ( ( 2 * j - 1 ) * x[i] * vtable[i][j-1]   \
          - (     j - 1 ) *        vtable[i][j-2] ) \
          / (     j     )

  v = np.zeros ( n, dtype = np.float64 )

  for i in range ( 0, n ):
    v[i] = vtable[i][o]

  return v

def lp_value_test ( ):

#*****************************************************************************80
#
## lp_value_test() tests lp_value().
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

  n = 1
  xvec = np.zeros ( 1, dtype = np.float64 )

  print ( '' )
  print ( 'lp_value_test():' )
  print ( '  lp_value() evaluates a Legendre polynomial.' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     O        X           L(O,X)                    L(O,X)', end = '' )
  print ( '                   Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, o, x, fx1 = lp_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x

    fx2 = lp_value ( n, o, xvec )

    e = fx1 - fx2[0]

    print ( '  %4d  %12.8f  %24.16g  %24.16g  %8.2g' % ( o, x, fx1, fx2[0], e ) )

  return

def lp_values ( n_data ):

#*****************************************************************************80
#
## lp_values() returns values of the Legendre polynomials P(n,x).
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
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 22

  fx_vec = np.array ( [
      0.1000000000000000E+01,
      0.2500000000000000E+00,
     -0.4062500000000000E+00,
     -0.3359375000000000E+00,
      0.1577148437500000E+00,
      0.3397216796875000E+00,
      0.2427673339843750E-01,
     -0.2799186706542969E+00,
     -0.1524540185928345E+00,
      0.1768244206905365E+00,
      0.2212002165615559E+00,
      0.0000000000000000E+00,
     -0.1475000000000000E+00,
     -0.2800000000000000E+00,
     -0.3825000000000000E+00,
     -0.4400000000000000E+00,
     -0.4375000000000000E+00,
     -0.3600000000000000E+00,
     -0.1925000000000000E+00,
      0.8000000000000000E-01,
      0.4725000000000000E+00,
      0.1000000000000000E+01 ], dtype = np.float64 )

  n_vec = np.array ( [
     0,  1,  2,
     3,  4,  5,
     6,  7,  8,
     9, 10,  3,
     3,  3,  3,
     3,  3,  3,
     3,  3,  3,
     3 ], dtype = np.int32 )

  x_vec = np.array ( [
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.00E+00,
     0.10E+00,
     0.20E+00,
     0.30E+00,
     0.40E+00,
     0.50E+00,
     0.60E+00,
     0.70E+00,
     0.80E+00,
     0.90E+00,
     1.00E+00 ], dtype = np.float64 )

  if ( n_data < 0 ):
    n_data = 0

  n_data = n_data + 1

  if ( n_max < n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data-1]
    x = x_vec[n_data-1]
    fx = fx_vec[n_data-1]

  return n_data, n, x, fx

def lp_values_test ( ):

#*****************************************************************************80
#
## lp_values_test() tests lp_values().
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
  print ( '' )
  print ( 'lp_values_test():' )
  print ( '  lp_values() stores values of' )
  print ( '  the Legendre polynomial P(o,x).' )
  print ( '' )
  print ( '                        Tabulated' )
  print ( '     O        X           L(O,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, o, x, fx = lp_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %12.8f  %24.16g' % ( o, x, fx ) )

  return

def mono_next_grlex ( m, x ):

#*****************************************************************************80
#
## mono_next_grlex() returns the next monomial in grlex order.
#
#  Discussion:
#
#    Example:
#
#    M = 3
#
#    #  X(1)  X(2)  X(3)  Degree
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
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, 0 ].
#
#  Output:
#
#    integer X[M], the next monomial.
#

#
#  Ensure that 1 <= D.
#
  if ( m < 1 ):
    print ( '' )
    print ( 'mono_next_grlex - Fatal error!' )
    print ( '  M < 1' )
    raise Exception ( 'mono_next_grlex - Fatal error!' )
#
#  Ensure that 0 <= X(I).
#
  for i in range ( 0, m ):
    if ( x[i] < 0 ):
      print ( '' )
      print ( 'mono_next_grlex - Fatal error!' )
      print ( '  X[I] < 0' )
      raise Exception ( 'mono_next_grlex - Fatal error!' )
#
#  Find I, the index of the rightmost nonzero entry of X.
#
  i = 0
  for j in range ( m, 0, -1 ):
    if ( 0 < x[j-1] ):
      i = j
      break
#
#  set T = X(I)
#  set X(I) to zero,
#  increase X(I-1) by 1,
#  increment X(M) by T-1.
#
  if ( i == 0 ):
    x[m-1] = 1
    return x
  elif ( i == 1 ):
    t = x[0] + 1
    im1 = m
  elif ( 1 < i ):
    t = x[i-1]
    im1 = i - 1

  x[i-1] = 0
  x[im1-1] = x[im1-1] + 1
  x[m-1] = x[m-1] + t - 1

  return x

def mono_next_grlex_test ( rng ):

#*****************************************************************************80
#
## mono_next_grlex_test() tests mono_next_grlex().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 4

  print ( '' )
  print ( 'mono_next_grlex_test():' )
  print ( '  mono_next_grlex() computes the next monomial' )
  print ( '  in M variables in grlex order.' )
  print ( '' )
  print ( '  Let M =  %d' % ( m ) )

  for i in range ( 0, 10 ):

    x = rng.integers ( low = 0, high = 3, size = m, endpoint = True )
    print ( '' )
    print ( '  ', end = '' )
    for k in range ( 0, m ):
      print ( '%2d' % ( x[k] ), end = '' )
    print ( '' )

    for j in range ( 0, 5 ):
      x = mono_next_grlex ( m, x )
      print ( '  ', end = '' )
      for k in range ( 0, m ):
        print ( '%2d' %  ( x[k] ), end = '' )
      print ( '' )

  return

def mono_print ( m, f, title ):

#*****************************************************************************80
#
## mono_print() prints a monomial.
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
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer F[M], the exponents.
#
#    string TITLE, a title.
#
  import sys

  sys.stdout.write ( title )
  
  sys.stdout.write ( '  x^' )
  if ( 1 < m or f[0] < 0 ):
    sys.stdout.write ( '(' )
  for i in range ( 0, m ):
    sys.stdout.write ( repr ( f[i] ) )
    if ( i < m - 1 ):
      sys.stdout.write ( ',' )
    elif ( 1 < m or f[0] < 0 ):
      sys.stdout.write ( ')' )
  sys.stdout.write ( '\n' )

  return

def mono_print_test ( ):

#*****************************************************************************80
#
## mono_print_test() tests mono_print().
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

  print ( '' )
  print ( 'mono_print_test():' )
  print ( '  mono_print() can print out a monomial.' )
  print ( '' )

  m = 1
  f = np.array ( [ 5 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [5]:' )

  m = 1
  f = np.array ( [ -5 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [-5]:' )

  m = 4
  f = np.array ( [ 2, 1, 0, 3 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [2,1,0,3]:' )

  m = 3
  f = np.array ( [ 17, -3, 199 ], dtype = np.int32 )
  mono_print ( m, f, '  Monomial [17,-3,199]:' )

  return

def mono_rank_grlex ( m, x ):

#*****************************************************************************80
#
## mono_rank_grlex() computes the graded lexicographic rank of a monomial.
#
#  Discussion:
#
#    The graded lexicographic ordering is used, over all monomials in 
#    M dimensions, for total degree = 0, 1, 2, ...
#
#    For example, if M = 3, the ranking begins:
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
#   This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#    1 <= M.
#
#    integer X[M], the composition.
#    For each 1 <= I <= M, we have 0 <= X(I).
#
#  Output:
#
#    integer RANK, the rank.
#
  from scipy.special import comb
  import numpy as np
#
#  Ensure that 1 <= M.
#
  if ( m < 1 ):
    print ( '' )
    print ( 'mono_rank_grlex - Fatal error!' )
    print ( '  M < 1' )
    raise Exception ( 'mono_rank_grlex - Fatal error!' )
#
#  Ensure that 0 <= X(I).
#
  for i in range ( 0, m ):
    if ( x[i] < 0 ):
      print ( '' )
      print ( 'mono_rank_grlex - Fatal error!' )
      print ( '  X[I] < 0' )
      raise Exception ( 'mono_rank_grlex - Fatal error!' )
#
#  NM = sum ( X )
#
  nm = np.sum ( x )
#
#  Convert to KSUBSET format.
#
  ns = nm + m - 1
  ks = m - 1
  if ( 0 < ks ):
    xs = np.zeros ( ks, dtype = np.int32 )
    xs[0] = x[0] + 1
    for i in range ( 2, m ):
      xs[i-1] = xs[i-2] + x[i-1] + 1
#
#  Compute the rank.
#
  rank = 1

  for i in range ( 1, ks + 1 ):
    if ( i == 1 ):
      tim1 = 0
    else:
      tim1 = xs[i-2]

    if ( tim1 + 1 <= xs[i-1] - 1 ):
      for j in range ( tim1 + 1, xs[i-1] ):
        rank = rank + comb ( ns - j, ks - i )

  for n in range ( 0, nm ):
    rank = rank + comb ( n + m - 1, n )

  return rank

def mono_rank_grlex_test ( ):

#******************************************************************************/
#
## mono_rank_grlex_test() tests mono_rank_grlex().
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
  import numpy as np

  m = 3
  test_num = 8
  x_test = np.array (  [ \
    0, 0, 0, \
    1, 0, 0, \
    0, 0, 1, \
    0, 2, 0, \
    1, 0, 2, \
    0, 3, 1, \
    3, 2, 1, \
    5, 2, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'mono_rank_grlex_test():' )
  print ( '  mono_rank_grlex() returns the rank of a monomial in the sequence' )
  print ( '  of all monomials in M dimensions, in grlex order.' )

  print ( '' )
  print ( '  Print a monomial sequence with ranks assigned.' )

  n = 4

  print ( '' )
  print ( '  Let M = %d' % ( m ) )
  print ( '      N = %d' % ( n ) )
  print ( '' )

  x = np.zeros ( m, dtype = np.int32 )

  x[0] = 0
  x[1] = 0
  x[2] = 0

  i = 1

  while ( True ):
    print ( '  %2d    ' % ( i ), end = '' )
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ), end = '' )
    print ( '' )

    if ( x[0] == n ):
      break

    mono_upto_next_grlex ( m, n, x )
    i = i + 1

  print ( '' )
  print ( '  Now, given a monomial, retrieve its rank in the sequence:' )
  print ( '' )

  for test in range ( 0, test_num ):
    for j in range ( 0, m ):
      x[j] = x_test[j+test*m]
    rank = mono_rank_grlex ( m, x )

    print ( '  %3d    ' % ( rank ), end = '' )
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ), end = '' )
    print ( '' )

  return

def mono_unrank_grlex ( m, rank ):

#*****************************************************************************80
#
## mono_unrank_grlex() computes the monomial of given grlex rank.
#
#  Licensing:
#
#   This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#    1 <= M.
#
#    integer RANK, the rank of the monomial.
#
#  Output:
#
#    integer X[M], the monomial.
#
  from scipy.special import comb
  import numpy as np
#
#  Ensure that 1 <= M.
#
  if ( m < 1 ):
    print ( '' )
    print ( 'mono_unrank_grlex - Fatal error!' )
    print ( '  M < 1' )
    raise Exception ( 'mono_unrank_grlex - Fatal error!' )
#
#  Ensure that 1 <= RANK.
#
  if ( rank < 1 ):
    print ( '' )
    print ( 'mono_unrank_grlex - Fatal error!' )
    print ( '  RANK < 1' )
    raise Exception ( 'mono_unrank_grlex - Fatal error!' )

  x = np.zeros ( m, dtype = np.int32 )
#
#  Special case M = 1.
#
  if ( m == 1 ):
    x[0] = rank - 1
    return x
#
#  Determine the appropriate value of NM.
#  Do this by adding up the number of compositions of sum 0, 1, 2, 
#  ..., without exceeding RANK.  Moreover, RANK - this sum essentially
#  gives you the rank of the composition within the set of compositions
#  of sum NM.  And that's the number you need in order to do the
#  unranking.
#
  rank1 = 1
  nm = -1
  while ( True ):
    nm = nm + 1
    r = comb ( nm + m - 1, nm )
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
  ks = m - 1
  ns = nm + m - 1
  xs = np.zeros ( ks, dtype = np.int32 )

  nksub = comb ( ns, ks )

  j = 1

  for i in range ( 1, ks + 1 ):
    r = comb ( ns - j, ks - i )

    while ( r <= rank2 and 0 < r ):
      rank2 = rank2 - r
      j = j + 1
      r = comb ( ns - j, ks - i )

    xs[i-1] = j
    j = j + 1
#
#  Convert from KSUBSET format to COMP format.
#
  x[0] = xs[0] - 1
  for i in range ( 2, m ):
    x[i-1] = xs[i-1] - xs[i-2] - 1
  x[m-1] = ns - xs[ks-1]

  return x

def mono_unrank_grlex_test ( rng ):

#******************************************************************************/
#
## mono_unrank_grlex_test() tests mono_unrank_grlex().
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

  m = 3
  print ( '' )
  print ( 'mono_unrank_grlex():' )
  print ( '  mono_unrank_grlex() is given a rank, and returns the corresponding' )
  print ( '  monomial in the sequence of all monomials in M dimensions' )
  print ( '  in grlex order.' )

  print ( '' )
  print ( '  For reference, print a monomial sequence with ranks.' )

  n = 4
  rank_max = mono_upto_enum ( m, n )

  print ( '' )
  print ( '  Let M = %d' % ( m ) )
  print ( '      N = %d' % ( n ) )
  print ( '' )

  x = np.zeros ( m, dtype = np.int32 )

  i = 1

  while ( True ):
    print ( '  %2d    ' % ( i ), end = '' )
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ), end = '' )
    print ( '' )

    if ( x[0] == n ):
      break

    mono_upto_next_grlex ( m, n, x )
    i = i + 1

  print ( '' )
  print ( '  Now choose random ranks between 1 and %d' % ( rank_max ) )
  print ( '' )

  test_num = 5

  for test in range ( 0, test_num ):
    rank = rng.integers ( low = 1, high = rank_max, endpoint = True )
    x = mono_unrank_grlex ( m, rank )
    print ( '  %2d    ' % ( rank ), end = '' )
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ), end = '' )
    print ( '' )

  return

def mono_upto_enum ( m, n ):

#*****************************************************************************80
#
## mono_upto_enum() enumerates monomials in M dimensions of degree up to N.
#
#  Discussion:
#
#    For M = 2, we have the following values:
#
#    N  VALUE
#
#    0    1
#    1    3
#    2    6
#    3   10
#    4   15
#    5   21
#
#    In particular, VALUE(2,3) = 10 because we have the 10 monomials:
#
#      1, x, y, x^2, xy, y^2, x^3, x^2y, xy^2, y^3.
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
#    integer M, the spatial dimension.
#
#    integer N, the maximum degree.
#
#  Output:
#
#    integer VALUE, the number of monomials in
#    M variables, of total degree N or less.
#
  from scipy.special import comb

  value = comb ( n + m, n )

  return value

def mono_upto_enum_test ( ):

#*****************************************************************************80
#
## mono_upto_enum_test() tests mono_upto_enum().
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
  print ( '' )
  print ( 'mono_upto_enum_test():' )
  print ( '  mono_upto_enum() can enumerate the number of monomials' )
  print ( '  in M variables, of total degree between 0 and N.' )

  print ( '' )
  print ( '    N:', end = '' )
  for n in range ( 0, 9 ):
    print ( '  %4d' % ( n ), end = '' )
  print ( '' )
  print ( '   M +---------------------------------------------------------------' )
  for m in range ( 1, 9 ):
    print ( '  %2d |' % ( m ), end = '' )
    for n in range ( 0, 9 ):
      v = mono_upto_enum ( m, n )
      print ( ' %5d' % ( v ), end = '' )
    print ( '' )

  return

def mono_upto_next_grlex ( m, n, x ):

#*****************************************************************************80
#
## mono_upto_next_grlex(): grlex next monomial, total degree up to N.
#
#  Discussion:
#
#    We consider all monomials in an M-dimensional space, with total
#    degree N.
#
#    For example:
#
#    M = 3
#    N = 3
#
#    #  X(1)  X(2)  X(3)  Degree
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
#    24 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the maximum degree.
#    0 <= N.
#
#    integer X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, 0 ].
#    The last is [ N, 0, ..., 0, 0 ].
#
#  Output:
#
#    integer X[M], the next monomial.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'mono_upto_next_grlex - Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'mono_upto_next_grlex - Fatal error!' )

  if ( np.sum ( x ) < 0 ):
    print ( '' )
    print ( 'mono_upto_next_grlex - Fatal error!' )
    print ( '  Input X sum is less than 0.' )
    raise Exception ( 'mono_upto_next_grlex - Fatal error!' )

  if ( n < np.sum ( x ) ):
    print ( '' )
    print ( 'mono_upto_next_grlex - Fatal error!' )
    print ( '  Input X sum is more than N.' )
    raise Exception ( 'mono_upto_next_grlex - Fatal error!' )

  if ( n == 0 ):
    return x

  if ( x[0] == n ):
    x[0] = 0
  else:
    x = mono_next_grlex ( m, x )

  return x

def mono_upto_next_grlex_test ( ):

#*****************************************************************************80
#
## mono_upto_next_grlex_test() tests mono_upto_next_grlex().
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

  m = 3

  print ( '' )
  print ( 'mono_upto_next_grlex_test()' )
  print ( '  mono_upto_next_grlex() can list the monomials' )
  print ( '  in M variables, of total degree up to N,' )
  print ( '  in grlex order, one at a time.' )
  print ( '' )
  print ( '  We start the process with (0,0,...,0,0).' )
  print ( '  The process ends with (N,0,...,0,0)' )

  n = 4

  print ( '' )
  print ( '  Let M =   %d' % ( m ) )
  print ( '      N =   %d' % ( n ) )
  print ( '' )

  x = np.array ( [ 0, 0, 0 ], dtype = np.int32 )
 
  i = 1;

  while ( True ):

    print ( '  %2d    ' % ( i ), end = '' )
    for k in range ( 0, m ):
      print ( '%2d' % ( x[k] ), end = '' )
    print ( '' )

    if ( x[0] == n ):
      break

    x = mono_upto_next_grlex ( m, n, x )
    i = i + 1

  return

def mono_upto_random ( m, n, rng ):

#*****************************************************************************80
#
## mono_upto_random(): random monomial with total degree less than or equal to N.
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
#    integer M, the spatial dimension.
#
#    integer N, the degree.
#    0 <= N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer X[M], the random monomial.
#
#    integer RANK, the rank of the monomial.
#
  import numpy as np

  rank_min = 1
  rank_max = mono_upto_enum ( m, n )
  rank = rng.integers ( low = rank_min, high = rank_max, endpoint = True )
  x = mono_unrank_grlex ( m, rank )

  return x, rank

def mono_upto_random_test ( rng ):

#*****************************************************************************80
#
## mono_upto_random_test() tests mono_upto_random().
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
  m = 3

  print ( '' )
  print ( 'mono_upto_random_test():' )
  print ( '  mono_upto_random() selects at random a monomial' )
  print ( '  in M dimensions of total degree no greater than N.' )

  n = 4

  print ( '' )
  print ( '  Let M = %d' % ( m ) )
  print ( '      N = %d' % ( n ) )
  print ( '' )

  test_num = 5

  for test in range ( 0, test_num ):
    x, rank = mono_upto_random ( m, n, rng )
    print ( '  %2d    ' % ( rank ), end = '' )
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ), end = '' )
    print ( '' )

  return

def mono_value ( m, n, f, x ):

#*****************************************************************************80
#
## mono_value() evaluates a monomial.
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
#    integer M, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer F[M], the exponents of the monomial.
#
#    real X[M,N], the coordinates of the evaluation points.
#
#  Output:
#
#    real mono_value[N], the value of the monomial at X.
#
  import numpy as np

  v = np.ones ( n, dtype = np.float64 )

  for i in range ( 0, m ):
    v = v * ( x[i,:] ** f[i] )

  return v

def mono_value_test ( rng ):

#*****************************************************************************80
#
## mono_value_test() tests mono_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2025
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
  print ( 'mono_value_test()' )
  print ( '  mono_value() evaluates a monomial.' )

  m = 3
  n = 6
  print ( '' )
  print ( '  Let M = %d' % ( m ) )
  print ( '      N = %d' % ( n ) )

  test_num = 5

  for test in range ( 0, test_num ):
    f, rank = mono_upto_random ( m, n, rng )
    print ( '' )
    mono_print ( m, f, '  M(X) = ' )
    nx = 2
    x = np.array ( [ \
      [ 1.0, -2.0 ], \
      [ 2.0,  4.0 ], \
      [ 3.0,  1.0 ] ] )

    v = mono_value ( m, nx, f, x )
    for j in range ( 0, nx ):
      print ( '  M(%g,%g,%g) = %g' % ( x[0,j], x[1,j], x[2,j], v[j] ) )

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
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation of 0, ..., N-1.
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
  print ( 'perm0_uniform_test()' )
  print ( '  perm0_uniform() randomly selects a permutation of 0,...,N-1.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm0_uniform ( n, rng )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%4d' % ( p[i] ), end = '' )
    print ( '' )

  return

def perm_check0 ( n, p ):

#*****************************************************************************80
#
## perm_check0() checks a 0-based permutation.
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
  for value in range ( 0, n ):

    ierror = 1

    for location in range ( 0, n ):
      if ( p[location] == value ):
        ierror = 0
        break

    if ( ierror != 0 ):
      print ( '' )
      print ( 'perm_check0 - Fatal error!' )
      print ( '  Permutation is missing the value %d.' % ( value ) )
      raise Exception ( 'perm_check0 - Fatal error!' )

  return

def perm_uniform ( n, rng ):

#*****************************************************************************80
#
## perm_uniform() selects a random permutation of N objects.
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

def perm_uniform_test ( rng ):

#*****************************************************************************80
#
## perm_uniform_test() tests perm_uniform().
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
  print ( 'perm_uniform_test():' )
  print ( '  perm_uniform() randomly selects a permutation.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm_uniform ( n, rng )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%4d' % ( p[i] ), end = '' )
    print ( '' )

  return

def polynomial_compress ( o1, c1, e1 ):

#*****************************************************************************80
#
## polynomial_compress() compresses a polynomial.
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
#    integer O1, the "order" of the polynomial.
#
#    real C1(O1), the coefficients.
#
#    integer E1(O1), the indices of the exponents.
#
#  Output:
#
#    integer O2, the "order" of the compressed polynomial.
#
#    real C2(O2), the coefficients of the compressed polynomial.
#
#    integer E2(O2), the indices of the exponents of the 
#    compress polynomial.
#
  import numpy as np

  epsilon = np.finfo(float).eps
#
#  Add coefficients associated with the same exponent.
#
  get = 0
  put = 0

  c2 = np.zeros ( o1, dtype = np.float64 )
  e2 = np.zeros ( o1, dtype = np.int32 )

  while ( get < o1 ):
    get = get + 1

    if ( 0 == put ):
      put = put + 1
      c2[put-1] = c1[get-1]
      e2[put-1] = e1[get-1]
    else:
      if ( e2[put-1] == e1[get-1] ):
        c2[put-1] = c2[put-1] + c1[get-1]
      else:
        put = put + 1
        c2[put-1] = c1[get-1]
        e2[put-1] = e1[get-1]

  o2 = put
#
#  Clear out zeros and tiny coefficients.
#
  get = 0
  put = 0

  while ( get < o2 ):
    if ( np.sqrt ( epsilon ) < np.abs ( c2[get] ) ):
      c2[put] = c2[get]
      e2[put] = e2[get]
      put = put + 1
    get = get + 1

  o2 = put

  return o2, c2, e2

def polynomial_compress_test ( ):

#*****************************************************************************80
#
## polynomial_compress_test() tests polynomial_compress().
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
  import numpy as np

  print ( '' )
  print ( 'polynomial_compress_test()' )
  print ( '  polynomial_compress() compresses a polynomial.' )

  m = 3
  o = 10
  c = np.array ( [ 7.0, - 5.0, 5.0, 9.0, 11.0, 3.0, 6.0, 0.0, - 13.0, 1.0E-20 ], \
    dtype = np.float64 )
  e = np.array ( [ 1, 2, 2, 4, 5, 5, 5, 12, 33, 35 ], dtype = np.int32 )

  print ( '' )
  title = '  Uncompressed polynomial ='
  polynomial_print ( m, o, c, e, title )

  o2, c2, e2 = polynomial_compress ( o, c, e )
  print ( '' )
  title = '  Compressed polynomial ='
  polynomial_print ( m, o2, c2, e2, title )

  return

def polynomial_print ( m, o, c, e, title ):

#*****************************************************************************80
#
## polynomial_print() prints a polynomial.
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
#    integer M, the spatial dimension.
#
#    integer O, the "order" of the polynomial, that is,
#    simply the number of terms.
#
#    real C(O), the coefficients.
#
#    integer E(O), the indices of the exponents.
#        
#    string TITLE, a title.
#
  import sys

  sys.stdout.write ( title )
  sys.stdout.write ( '\n' )

  if ( o == 0 ):
    sys.stdout.write ( '      0.' )
  else:
    for j in range ( 0, o ):
      sys.stdout.write ( '    ' )
      if ( c[j] < 0 ):
        sys.stdout.write ( '- ' )
      else:
        sys.stdout.write ( '+ ' )
      sys.stdout.write ( repr ( abs ( c[j] ) ) )
      sys.stdout.write ( ' * x^(' )
      f = mono_unrank_grlex ( m, e[j] )
      for i in range ( 0, m ):
        sys.stdout.write ( repr ( f[i] ) )
        if ( i < m - 1 ):
          sys.stdout.write ( ',' )
        else:
          sys.stdout.write ( ')' )
      if ( j == o - 1 ):
        sys.stdout.write ( '.' )
      sys.stdout.write ( '\n' )

  return

def polynomial_print_test ( ):

#*****************************************************************************80
#
## polynomial_print_test() tests polynomial_print().
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
  import numpy as np

  print ( '' )
  print ( 'polynomial_print_test()' )
  print ( '  polynomial_print() prints a polynomial.' )

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )
  title = '  P1(X) ='

  print ( '' )
  polynomial_print ( m, o, c, e, title )

  return

def polynomial_sort ( o, c, e ):

#*****************************************************************************80
#
## polynomial_sort() sorts the information in a polynomial.
#
#  Discussion:
#
#    The coefficients C and exponents E are rearranged so that 
#    the elements of E are in ascending order.
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
#    integer O, the "order" of the polynomial.
#
#    real C[O], the coefficients of the scaled polynomial.
#
#    integer E[O], the indices of the exponents of 
#    the scaled polynomial.
#
#  Output:
#
#    real C[O], the coefficients of the sorted polynomial.
#
#    integer E[O], the indices of the exponents of 
#    the sorted polynomial.
#
  indx = i4vec_sort_heap_index_a ( o, e )

  e = i4vec_permute ( o, indx, e )
  c = r8vec_permute ( o, indx, c )

  return c, e

def polynomial_sort_test ( ):

#*****************************************************************************80
#
## polynomial_sort_test() tests polynomial_sort().
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
  import numpy as np

  m = 3
  o = 6
  c = np.array ( [ 0.0, 9.0, -5.0, - 13.0, 7.0, 11.0 ], dtype = np.float64 )
  e = np.array ( [ 12, 4, 2, 33, 1, 5 ], dtype = np.int32 )

  print ( '' )
  print ( 'polynomial_sort_test():' )
  print ( '  polynomial_sort() sorts a polynomial by exponent index.' )

  print ( '' )
  title = '  Unsorted polynomial:'
  polynomial_print ( m, o, c, e, title )

  c, e = polynomial_sort ( o, c, e )

  print ( '' )
  title = '  Sorted polynomial:'
  polynomial_print ( m, o, c, e, title )

  return

def polynomial_value ( m, o, c, e, nx, x ):

#*****************************************************************************80
#
## polynomial_value() evaluates a polynomial.
#
#  Discussion:
#
#    The polynomial is evaluated term by term, and no attempt is made to
#    use an approach such as Horner's method to speed up the process.
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
#    int M, the spatial dimension.
#
#    integer O, the "order" of the polynomial.
#
#    real C[O], the coefficients of the scaled polynomial.
#
#    integer E[O], the indices of the exponents of 
#    the scaled polynomial.
#
#    integer NX, the number of evaluation points.
#
#    real X[M*NX], the coordinates of the evaluation points.
#
#  Output:
#
#    real V[NX], the value of the polynomial at X.
#
  import numpy as np

  p = np.zeros ( nx, dtype = np.float64 )

  for j in range ( 0, o ):
    f = mono_unrank_grlex ( m, e[j] )
    v = mono_value ( m, nx, f, x )
    for k in range ( 0, nx ):
      p[k] = p[k] + c[j] * v[k]

  return p

def polynomial_value_test ( ):

#*****************************************************************************80
#
## polynomial_value_test() tests polynomial_value().
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
  import numpy as np

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )
  nx = 2
  x = np.array ( [ \
    [ 1.0, -2.0 ], \
    [ 2.0,  4.0 ], \
    [ 3.0,  1.0 ] ] )

  print ( '' )
  print ( 'polynomial_value_test():' )
  print ( '  polynomial_value() evaluates a polynomial.' )

  print ( '' )
  title = '  P(X) = '
  polynomial_print ( m, o, c, e, title )

  p = polynomial_value ( m, o, c, e, nx, x )

  print ( '' )
  for j in range ( 0, nx ):
    print ( '  P(%f,%f,%f) = %g' % ( x[0,j], x[1,j], x[2,j], p[j] ) )

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

def r8vec_permute ( n, p, a ):

#*****************************************************************************80
#
## r8vec_permute() permutes an R8VEC in place.
#
#  Discussion:
#
#    An I4VEC is a vector of R8's.
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

  x = np.array ( [ 1.1, 2.2, 3.3, 4.4, 5.5 ], dtype = np.float64 )
  p = np.array ( [ 1, 3, 4, 0, 2 ], dtype = np.int32 )

  r8vec_print ( n, x, '  Original array X[]:' )

  i4vec_print ( n, p, '  Permutation vector P[]:' )

  x = r8vec_permute ( n, p, x )

  r8vec_print ( n, x, '  Permuted array X[P[*]]:' )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  legendre_product_polynomial_test ( )
  timestamp ( )

