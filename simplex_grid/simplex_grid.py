#! /usr/bin/env python3
#
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
#    integer XC[KC], the current composition.
#    Each entry of XC must be nonnegative.
#
#  Output:
#
#    integer XC[KC], the next composition.
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
  import platform

  kc = 3

  print ( '' )
  print ( 'comp_next_grlex_test' )
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
    print ( 'comp_random_grlex - Fatal error!' )
    print ( '  KC < 1' )
    raise Exception ( 'comp_random_grlex - Fatal error!' );
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
  print ( 'comp_random_grlex_test' )
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
#    Albert Nijenhuis Herbert Wilf,
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
  k = 5

  print ( '' )
  print ( 'comp_random_test():' )
  print ( '  comp_random() generates random compositions.' )
  print ( '' )

  n = 10

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
  import platform

  kc = 3

  print ( '' )
  print ( 'comp_unrank_grlex_test' )
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
#    22 December 2014
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
#    output set.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_random2 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    raise Exception ( 'ksub_random2 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_random2 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    raise Exception ( 'ksub_random2 - Fatal error!' )

  a = np.zeros ( k )

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

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_write() writes an R8MAT to a file.
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
#    string FILENAME, the name of the output file.
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_write_test ( ):

#*****************************************************************************80
#
## r8mat_write_test() tests r8mat_write().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_write_test:' )
  print ( '  r8mat_write() writes an R8MAT to a file.' )

  filename = 'r8mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )

  return

def simplex_grid_count ( m, n ):

#*****************************************************************************80
#
## simplex_grid_count() counts the grid points inside a simplex.
#
#  Discussion:
#
#    The size of a grid with parameters M, N is C(M+N,N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of subintervals.
#
#  Output:
#
#    integer NG, the number of grid points.
#
  ng = 1
  for i in range ( 1, m + 1 ):
    ng = ( ng * ( n + i ) ) // i

  return ng

def simplex_grid_count_test ( ):

#*****************************************************************************80
#
## simplex_grid_count_test() tests simplex_grid_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'simplex_grid_count_test:' )
  print ( '  simplex_grid_count counts the points in a regular grid' )
  print ( '  with N+1 points on a side, in an M-dimensional simplex.' )
  print ( '' )
  print ( '        M:  0      1      2      3      4      5' )
  print ( '    N:' )
  for n in range ( 0, 11 ):
    print ( '  %3d:' % ( n ), end = '' )
    for m in range ( 0, 6 ):
      print ( '%6d' % ( simplex_grid_count ( m, n ) ), end = '' )
    print ( '' )

  return
  
def simplex_grid_index_all ( m, n, ng ):

#*****************************************************************************80
#
## simplex_grid_index_all() returns all the simplex grid indices.
#
#  Discussion:
#
#    The number of grid indices can be determined by calling 
#      ng = simplex_grid_size ( m, n );
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
#    integer M, the spatial dimension.
#
#    integer N, the number of subintervals.
#
#    integer NG, the number of values in the grid.
#
#  Output:
#
#    integer G(NG,M+1), the current, and then the next, grid index.
#
  import numpy as np

  g = np.zeros ( ( ng, m + 1 ), dtype = np.int32 )

  grow = np.zeros ( m + 1, dtype = np.int32 )
  grow[m] = n

  i = 0
  for j in range ( 0, m + 1 ):
    g[i,j] = grow[j]

  i = i + 1

  while ( i < ng ):
    grow = comp_next_grlex ( m + 1, grow )
    for j in range ( 0, m + 1 ):
      g[i,j] = grow[j]
    i = i + 1

  return g

def simplex_grid_index_all_test ( ):

#*****************************************************************************80
#
## simplex_grid_index_all_test() tests simplex_grid_index_all().
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
  import platform

  print ( '' )
  print ( 'simplex_grid_index_all_test:' )
  print ( '  simplex_grid_index_all returns all the indices' )
  print ( '  of a simplex grid that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )

  m = 3
  n = 3
  ng = simplex_grid_count ( m, n )

  grid = simplex_grid_index_all ( m, n, ng )

  i4mat_print ( ng, m + 1, grid, '  Simplex Grid Index Matrix:' )

  return

def simplex_grid_index_next ( m, n, g ):

#*****************************************************************************80
#
## simplex_grid_index_next() returns the next simplex grid index.
#
#  Discussion:
#
#    The vector G has dimension M+1.  The first M entries may be regarded
#    as grid coordinates.  These coordinates must have a sum between 0 and N.
#    The M+1 entry contains the remainder, that is N minus the sum of the
#    first M coordinates.
#
#    Each time the function is called, it is given a current grid index, and
#    computes the next one.  The very first index is all zero except for a 
#    final value of N, and the very last index has all zero except for an'
#    intial value of N.
#
#    For example, here are the coordinates in order for M = 3, N = 3:
#
#     0  0 0 0 3
#     1  0 0 1 2
#     2  0 0 2 1
#     3  0 0 3 0
#     4  0 1 0 2
#     5  0 1 1 1
#     6  0 1 2 0
#     7  0 2 0 1
#     8  0 2 1 0
#     9  0 3 0 0
#    10  1 0 0 2
#    11  1 0 1 1
#    12  1 0 2 0
#    13  1 1 0 1
#    14  1 1 1 0
#    15  1 2 0 0
#    16  2 0 0 1
#    17  2 0 1 0
#    18  2 1 0 0
#    19  3 0 0 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of subintervals.
#
#    integer G(M+1), the current grid index.
#
#  Output:
#
#    integer G(M+1), the next grid index.
#
  g = comp_next_grlex ( m + 1, g )

  return g

def simplex_grid_index_next_test ( ):

#*****************************************************************************80
#
## simplex_grid_index_next_test() tests simplex_grid_index_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'simplex_grid_index_next_test:' )
  print ( '  simplex_grid_index_next lists, one by one, the indices' )
  print ( '  of a simplex grid that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )
  print ( '' )
  print ( '   #:  1  2  3  (*)' )
  print ( '' )

  m = 3
  n = 3

  j = 0
  g = np.zeros ( m + 1 )
  g[m] = n
  
  while ( True ):

    print ( '  %2d:' % ( j ), end = '' )
    for i in range ( 0, m ):
      print ( ' %2d' % ( g[i] ), end = '' )
    print ( ' (%2d)' % ( g[m] ) )

    if ( g[0] == n ):
      break

    g = simplex_grid_index_next ( m, n, g )

    j = j + 1

  return

def simplex_grid_index_sample ( m, n, ng, rng ):

#*****************************************************************************80
#
## simplex_grid_index_sample() returns a random simplex grid index.
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
#    integer M, the spatial dimension.
#
#    integer N, the number of subintervals in each dimension.
#
#    ingeger L, the number of indices to return.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer G(NG,M+1), randomly selected indices in the simplex grid.
#
  import numpy as np

  g = np.zeros ( ( ng, m + 1 ) )

  for i in range ( 0, ng ):
    grow = comp_random ( n, m + 1, rng )
    for j in range ( 0, m + 1 ):
      g[i,j] = grow[j]

  return g

def simplex_grid_index_sample_test ( rng ):

#*****************************************************************************80
#
## simplex_grid_index_sample_test() tests simplex_grid_index_sample().
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
  print ( '' )
  print ( 'simplex_grid_index_sample_test:' )
  print ( '  simplex_grid_index_sample returns a randomly selected' )
  print ( '  index of a simplex grid that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )
  print ( '' )
  print ( '   #:  1  2  3  (*)' )
  print ( '' )

  m = 3
  n = 3
  ng = 20

  g = simplex_grid_index_sample ( m, n, ng, rng )

  for i in range ( 0, ng ):
    print ( '  %2d:' % ( i ), end = '' )
    for j in range ( 0, m ):
      print ( ' %2d' % ( g[i,j] ), end = '' )
    print ( ' (%2d)' % ( g[i,m] ) )

  return

def simplex_grid_index_to_point ( m, n, ng, g, v ):

#*****************************************************************************80
#
## simplex_grid_index_to_point() returns  points corresponding to simplex indices.
#
#  Discussion:
#
#    The M-dimensional simplex is defined by M+1 vertices.
#
#    Given a regular grid that uses N subintervals along the edge between
#    each pair of vertices, a simplex grid index G is a set of M+1 values
#    each between 0 and N, and summing to N. 
#
#    This function determines the coordinates X of the point corresponding
#    to the index G.
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
#    integer M, the spatial dimension.
#
#    integer N, the number of subintervals.
#
#    integer NG, the number of grid indices to be converted.
#
#    integer G(NG,M+1), the grid indices of 1 or more points.
#
#    real V(M+1,M), the coordinates of the vertices of the simplex.
#
#  Output:
#
#    real X(NG,M), the coordinates of one or more points.
#
  import numpy as np
#
#  This could be done more "efficiently" by declaring G and V to be 
#  of type numpy.matrix and writing x = g * v / n but I am not happy
#  having arrays and matrices being different kinds of objects.
#
  x = np.zeros ( ( ng, m ) )

  for k in range ( 0, m ):
    for i in range ( 0, ng ):
      for j in range ( 0, m + 1 ):
        x[i,k] = x[i,k] + g[i,j] * v[j,k]
      x[i,k] = x[i,k] / float ( n )

  return x

def simplex_grid_index_to_point_test01 ( rng ):

#*****************************************************************************80
#
## simplex_grid_index_to_point_test01() tests simplex_grid_index_to_point().
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
  import numpy as np

  print ( '' )
  print ( 'simplex_grid_index_to_point_test01:' )
  print ( '  simplex_grid_index_to_point returns the physical point' )
  print ( '  corresponding to a grid index of a simplex grid that' )
  print ( '  that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )

  m = 2
  n = 5
  ng = 10

  v = np.array ( [ \
    [ 20.0,  0.0 ], \
    [ 30.0, 40.0 ], \
    [ 10.0, 20.0 ] ] )

  r8mat_print ( m + 1, m, v, '  Simplex vertices:' )

  print ( '' )
  print ( '  Choosing random simplex indices to convert:' )
  print ( '   #:  1  2  3     X        Y' )
  print ( '' )

  g = simplex_grid_index_sample ( m, n, ng, rng )

  x = simplex_grid_index_to_point ( m, n, ng, g, v )

  for i in range ( 0, ng ):
    print ( '  %2d:' % ( i ), end = '' )
    for j in range ( 0, m + 1 ):
      print ( ' %2d' % ( g[i,j] ), end = '' )
    for j in range ( 0, m ):
      print ( ' %8.4f' % ( x[i,j] ), end = '' )
    print ( '' )

  return

def simplex_grid_index_to_point_test02 ( ):

#*****************************************************************************80
#
## simplex_grid_index_to_point_test02() tests simplex_grid_index_to_point().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'simplex_grid_index_to_point_test02:' )
  print ( '  simplex_grid_index_to_point returns the physical point' )
  print ( '  corresponding to a grid index of a simplex grid that' )
  print ( '  that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )

  m = 2
  n = 5
  ng = simplex_grid_count ( m, n )

  v = np.array ( [ \
    [ 20.0,  0.0 ], \
    [ 30.0, 40.0 ], \
    [ 10.0, 20.0 ] ] )

  r8mat_print ( m + 1, m, v, '  Simplex vertices:' )

  grid = simplex_grid_index_all ( m, n, ng )

  x = simplex_grid_index_to_point ( m, n, ng, grid, v )

  r8mat_print ( ng, m, x, '  Grid Point Coordinates:' )

  return

def simplex_grid_test ( ):

#*****************************************************************************80
#
## simplex_grid_test() tests simplex_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'simplex_grid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test simplex_grid().' )

  rng = default_rng ( )
#
#  Utilities:
#
  comp_next_grlex_test ( )
  comp_random_test ( rng )
  comp_random_grlex_test ( rng )
  comp_rank_grlex_test ( rng )
  comp_unrank_grlex_test ( )
 
  ksub_random2_test ( rng )
#
#  Library.
#
  simplex_grid_count_test ( )
  simplex_grid_index_next_test ( )
  simplex_grid_index_sample_test ( rng )
  simplex_grid_index_all_test ( )
  simplex_grid_index_to_point_test01 ( rng )
  simplex_grid_index_to_point_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'simplex_grid_test():' )
  print ( '  Normal end of execution.' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  simplex_grid_test ( )
  timestamp ( )

