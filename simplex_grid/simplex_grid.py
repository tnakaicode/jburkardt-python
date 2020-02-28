#! /usr/bin/env python3
#
def comp_next_grlex ( kc, xc ):

#*****************************************************************************80
#
## COMP_NEXT_GRLEX returns the next composition in grlex order.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int KC, the number of parts of the composition.
#    1 <= KC.
#
#    Input/output, int XC[KC], the current composition.
#    Each entry of XC must be nonnegative.
#    On return, XC has been replaced by the next composition in the
#    grlex order.
#
  from sys import exit
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'COMP_NEXT_GRLEX - Fatal error!' )
    print ( '  KC < 1' )
    exit ( 'COMP_NEXT_GRLEX - Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ( '' )
      print ( 'COMP_NEXT_GRLEX - Fatal error!' )
      print ( '  XC[I] < 0' )
      exit ( 'COMP_NEXT_GRLEX - Fatal error!' )
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
## COMP_NEXT_GRLEX_TEST tests COMP_NEXT_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'COMP_NEXT_GRLEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  COMP_NEXT_GRLEX determines the next COMP in' )
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

    nc = i4vec_sum ( kc, xc )

    print ( '   %3d: ' % ( rank ) ),
    print ( '    %2d = ' % ( nc ) ),
    for j in range ( 0, kc - 1 ):
      print ( '%2d + ' % ( xc[j] ) ),
    print ( '%2d' % ( xc[kc-1] ) )
#
#  When XC(1) == NC, we have completed the compositions associated with
#  a particular integer, and are about to advance to the next integer.
#
    if ( xc[0] == nc ):
      print ( '  ----:     --   ------------' )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMP_NEXT_GRLEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def comp_random_grlex ( kc, rank1, rank2, seed ):

#*****************************************************************************80
#
## COMP_RANDOM_GRLEX: random composition with degree less than or equal to NC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int KC, the number of parts in the composition.
#
#    Input, int RANK1, RANK2, the minimum and maximum ranks.
#    1 <= RANK1 <= RANK2.
#
#    Input, int SEED, the random number seed.
#
#    Output, int X[KC], the random composition.
#
#    Output, int RANK, the rank of the composition.
#
#    Output, int SEED, the random number seed.
#
  from sys import exit
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'COMP_RANDOM_GRLEX - Fatal error!' )
    print ( '  KC < 1' )
    exit ( 'COMP_RANDOM_GRLEX - Fatal error!' );
#
#  Ensure that 1 <= RANK1.
#
  if ( rank1 < 1 ):
    print ( '' )
    print ( 'COMP_RANDOM_GRLEX - Fatal error!' )
    print ( '  RANK1 < 1' )
    exit ( 'COMP_RANDOM_GRLEX - Fatal error!' );
#
#  Ensure that RANK1 <= RANK2.
#
  if ( rank2 < rank1 ):
    print ( '' )
    print ( 'COMP_RANDOM_GRLEX - Fatal error!' )
    print ( '  RANK2 < RANK1' )
    exit ( 'COMP_RANDOM_GRLEX - Fatal error!' )
#
#  Choose RANK between RANK1 and RANK2.
#
  rank, seed = i4_uniform_ab ( rank1, rank2, seed )
#
#  Recover the composition of given RANK.
#
  xc = comp_unrank_grlex ( kc, rank )

  return xc, rank, seed

def comp_random_grlex_test ( ):

#*****************************************************************************80
#
## COMP_RANDOM_GRLEX_TEST tests COMP_RANDOM_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COMP_RANDOM_GRLEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  COMP_RANDOM_GRLEX selects a random COMP in' )
  print ( '  graded lexicographic (grlex) order between indices RANK1 and RANK2.' )
  print ( '' )

  kc = 3
  rank1 = 20
  rank2 = 60
  seed = 123456789

  for test in range ( 0, 5 ):
    xc, rank, seed = comp_random_grlex ( kc, rank1, rank2, seed )
    nc = i4vec_sum ( kc, xc )
    print ( '   %3d: ' % ( rank ) ),
    print ( '    %2d = ' % ( nc ) ),
    for j in range ( 0, kc - 1 ):
      print ( '%2d + ' % ( xc[j] ) ),
    print ( '%2d' % ( xc[kc-1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMP_RANDOM_GRLEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def comp_random ( n, k, seed ):

#*****************************************************************************80
#
## COMP_RANDOM selects a random composition of the integer N into K parts.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the integer to be decomposed.
#
#    Input, integer K, the number of parts in the composition.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K), the parts of the composition.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  b, seed = ksub_random2 ( n + k - 1, k - 1, seed )

  a = np.zeros ( k )
  for i in range ( 0, k - 1 ):
    a[i] = b[i]
  a[k-1] = n + k

  l = 0

  for i in range ( 0, k ):
    m = a[i]
    a[i] = a[i] - l - 1
    l = m

  return a, seed

def comp_random_test ( ):

#*****************************************************************************80
#
## COMP_RANDOM_TEST tests COMP_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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

  k = 5

  print ( '' )
  print ( 'COMP_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COMP_RANDOM generates random compositions.' )
  print ( '' )

  n = 10
  seed = 123456789

  for i in range ( 1, 6 ):
    a, seed = comp_random ( n, k, seed )
    for j in range ( 0, k ):
      print ( '  %2d' % ( a[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMP_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def comp_rank_grlex ( kc, xc ):

#*****************************************************************************80
#
## COMP_RANK_GRLEX computes the graded lexicographic rank of a composition.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int KC, the number of parts in the composition.
#    1 <= KC.
#
#    Input, int XC[KC], the composition.
#    For each 1 <= I <= KC, we have 0 <= XC(I).
#
#    Output, int RANK, the rank of the composition.
#
  from sys import exit
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'COMP_RANK_GRLEX - Fatal error!' )
    print ( '  KC < 1' )
    exit ( 'COMP_RANK_GRLEX - Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ( '' )
      print ( 'COMP_RANK_GRLEX - Fatal error!' )
      print ( '  XC[I] < 0' )
      exit ( 'COMP_RANK_GRLEX - Fatal error!' );
#
#  NC = sum ( XC )
#
  nc = i4vec_sum ( kc, xc )
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

def comp_rank_grlex_test ( ):

#*****************************************************************************80
#
## COMP_RANK_GRLEX_TEST tests COMP_RANK_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COMP_RANK_GRLEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  COMP_RANK_GRLEX determines the rank of a COMP' )
  print ( '  from its parts.' )
  print ( '' )
  print ( '        Actual  Inferred' )
  print ( '  Test    Rank      Rank' )
  print ( '' )

  kc = 3
  rank1 = 20
  rank2 = 60
  seed = 123456789

  for test in range ( 0, 5 ):
    xc, rank3, seed = comp_random_grlex ( kc, rank1, rank2, seed )
    rank4 = comp_rank_grlex ( kc, xc )
    print ( '  %4d  %6d  %8d' % ( test, rank3, rank4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMP_RANK_GRLEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def comp_unrank_grlex ( kc, rank ):

#*****************************************************************************80
#
## COMP_UNRANK_GRLEX computes the composition of given grlex rank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int KC, the number of parts of the composition.
#    1 <= KC.
#
#    Input, int RANK, the rank of the composition.
#    1 <= RANK.
#
#    Output, int XC[KC], the composition XC of the given rank.
#    For each I, 0 <= XC[I] <= NC, and 
#    sum ( 1 <= I <= KC ) XC[I] = NC.
#
  from sys import exit
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ( '' )
    print ( 'COMP_UNRANK_GRLEX - Fatal error!' )
    print ( '  KC < 1' )
    exit ( 'COMP_UNRANK_GRLEX - Fatal error!' )
#
#  Ensure that 1 <= RANK.
#
  if ( rank < 1 ):
    print ( '' )
    print ( 'COMP_UNRANK_GRLEX - Fatal error!' )
    print ( '  RANK < 1' )
    exit ( 'COMP_UNRANK_GRLEX - Fatal error!' )
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
## COMP_UNRANK_GRLEX_TEST tests COMP_UNRANK_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  kc = 3

  print ( '' )
  print ( 'COMP_UNRANK_GRLEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  A COMP is a composition of an integer N into K parts.' )
  print ( '  Each part is nonnegative.  The order matters.' )
  print ( '  COMP_UNRANK_GRLEX determines the parts' )
  print ( '  of a COMP from its rank.' )
 
  print ( '' )
  print ( '  Rank: ->  NC       COMP    ' )
  print ( '  ----:     --   ------------ ' )

  for rank in range ( 1, 72 ):
    xc = comp_unrank_grlex ( kc, rank )
    nc = i4vec_sum ( kc, xc )
    print ( '   %3d: ' % ( rank ) ),
    print ( '    %2d = ' % ( nc ) ),
    for j in range ( 0, kc - 1 ):
      print ( '%2d + ' % ( xc[j] ) ),
    print ( '%2d' % ( xc[kc-1] ) )
#
#  When XC(1) == NC, we have completed the compositions associated with
#  a particular integer, and are about to advance to the next integer.
#
    if ( xc[0] == nc ):
      print ( '  ----:     --   ------------' )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMP_UNRANK_GRLEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_choose ( n, k ):

#*****************************************************************************80
#
## I4_CHOOSE computes the binomial coefficient C(N,K) as an I4.
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
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, K, are the values of N and K.
#
#    Output, integer VALUE, the number of combinations of N
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
      value = ( value * ( mx + i ) ) / i

  return value

def i4_choose_test ( ):

#*****************************************************************************80
#
## I4_CHOOSE_TEST tests I4_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_CHOOSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_CHOOSE evaluates C(N,K).' )
  print ( '' )
  print ( '       N       K     CNK' )

  for n in range ( 0, 5 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = i4_choose ( n, k )

      print ( '  %6d  %6d  %6d' % ( n, k, cnk ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_CHOOSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## I4MAT_PRINT prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, integer A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## I4MAT_PRINT_TEST tests I4MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'I4MAT_PRINT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test I4MAT_PRINT, which prints an I4MAT.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## I4MAT_PRINT_SOME prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, integer A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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
## I4MAT_PRINT_SOME_TEST tests I4MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'I4MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_PRINT_SOME prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

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
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
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
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_sum ( n, a ):

#*****************************************************************************80
#
## I4VEC_SUM sums the entries of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements.
#
#    Input, integer A(N), the vector.
#
#    Output, integer VALUE, the sum of the entries.
#
  value = 0

  for i in range ( 0, n ):
    value = value + a[i]

  return value

def i4vec_sum_test ( ):

#*****************************************************************************80
#
## I4VEC_SUM_TEST tests I4VEC_SUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4VEC_SUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SUM sums the entries of an I4VEC.' )

  n = 5
  lo = 0
  hi = 10
  seed = 123456789
  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, a, '  The vector:' )

  s = i4vec_sum ( n, a )
  print ( '' )
  print ( '  The vector entries sum to %d' % ( s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C(N), the randomly chosen integer vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed  )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4VEC_UNIFORM_AB - Fatal error!' )

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
## I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 20
  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  v, seed = i4vec_uniform_ab ( n, a, b, seed )

  i4vec_print ( n, v, '  The random vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ksub_random2 ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM2 selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This algorithm is designated Algorithm RKS2 in the reference.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the size of the set from which subsets are drawn.
#
#    Input, integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K).  A(I) is the I-th element of the
#    output set.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  if ( k < 0 ):
    print ( '' )
    print ( 'KSUB_RANDOM2 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    exit ( 'KSUB_RANDOM2 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'KSUB_RANDOM2 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    exit ( 'KSUB_RANDOM2 - Fatal error!' )

  a = np.zeros ( k )

  if ( k == 0 ):
    return a

  need = k
  have = 0

  available = n
  candidate = 0

  while ( True ):

    candidate = candidate + 1

    r, seed = r8_uniform_01 ( seed )

    if ( available * r <= need ):

      need = need - 1;
      a[have] = candidate
      have = have + 1

      if ( need <= 0 ):
        break

    available = available - 1

  return a, seed

def ksub_random2_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM2_TEST tests KSUB_RANDOM2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUB_RANDOM2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_RANDOM2 generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random2 ( n, k, seed )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_RANDOM2_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_WRITE writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
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
## R8MAT_WRITE_TEST tests R8MAT_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8MAT_WRITE, which writes an R8MAT to a file.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
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
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def simplex_grid_count ( m, n ):

#*****************************************************************************80
#
## SIMPLEX_GRID_COUNT counts the grid points inside a simplex.
#
#  Discussion:
#
#    The size of a grid with parameters M, N is C(M+N,N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals.
#
#    Output, integer NG, the number of grid points.
#
  ng = 1
  for i in range ( 1, m + 1 ):
    ng = ( ng * ( n + i ) ) // i

  return ng

def simplex_grid_count_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_COUNT_TEST tests SIMPLEX_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'SIMPLEX_GRID_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_GRID_COUNT counts the points in a regular grid' )
  print ( '  with N+1 points on a side, in an M-dimensional simplex.' )
  print ( '' )
  print ( '        M:  0      1      2      3      4      5' )
  print ( '    N:' )
  for n in range ( 0, 11 ):
    print ( '  %3d:' % ( n ) ),
    for m in range ( 0, 6 ):
      print ( '%6d' % ( simplex_grid_count ( m, n ) ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def simplex_grid_index_all ( m, n, ng ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_ALL returns all the simplex grid indices.
#
#  Discussion:
#
#    The number of grid indices can be determined by calling 
#      ng = simplex_grid_size ( m, n );
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals.
#
#    Input, integer NG, the number of values in the grid.
#
#    Output, integer G(NG,M+1), the current, and then the next, grid index.
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
## SIMPLEX_GRID_INDEX_ALL_TEST tests SIMPLEX_GRID_INDEX_ALL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'SIMPLEX_GRID_INDEX_ALL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_GRID_INDEX_ALL returns all the indices' )
  print ( '  of a simplex grid that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )

  m = 3
  n = 3
  ng = simplex_grid_count ( m, n )

  grid = simplex_grid_index_all ( m, n, ng )

  i4mat_print ( ng, m + 1, grid, '  Simplex Grid Index Matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_ALL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def simplex_grid_index_next ( m, n, g ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_NEXT returns the next simplex grid index.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals.
#
#    Input/output, integer G(M+1), the current, and then the next, grid index.
#
  g = comp_next_grlex ( m + 1, g )

  return g

def simplex_grid_index_next_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_NEXT_TEST tests SIMPLEX_GRID_INDEX_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'SIMPLEX_GRID_INDEX_NEXT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_GRID_INDEX_NEXT lists, one by one, the indices' )
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

    print ( '  %2d:' % ( j ) ),
    for i in range ( 0, m ):
      print ( ' %2d' % ( g[i] ) ),
    print ( ' (%2d)' % ( g[m] ) )

    if ( g[0] == n ):
      break

    g = simplex_grid_index_next ( m, n, g )

    j = j + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def simplex_grid_index_sample ( m, n, ng, seed ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_SAMPLE returns a random simplex grid index.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals in each dimension.
#
#    Input, ingeger L, the number of indices to return.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer G(NG,M+1), randomly selected indices in the simplex grid.
#
#    Output, integer SEED, the updated random number seed.
#
  import numpy as np

  g = np.zeros ( ( ng, m + 1 ) )

  for i in range ( 0, ng ):
    grow, seed = comp_random ( n, m + 1, seed )
    for j in range ( 0, m + 1 ):
      g[i,j] = grow[j]

  return g, seed

def simplex_grid_index_sample_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_SAMPLE_TEST tests SIMPLEX_GRID_INDEX_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'SIMPLEX_GRID_INDEX_SAMPLE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_GRID_INDEX_SAMPLE returns a randomly selected' )
  print ( '  index of a simplex grid that uses N+1 points on a side,' )
  print ( '  in an M-dimensional simplex.' )
  print ( '' )
  print ( '   #:  1  2  3  (*)' )
  print ( '' )

  m = 3
  n = 3
  ng = 20
  seed = 123456789

  g, seed = simplex_grid_index_sample ( m, n, ng, seed )

  for i in range ( 0, ng ):
    print ( '  %2d:' % ( i ) ),
    for j in range ( 0, m ):
      print ( ' %2d' % ( g[i,j] ) ),
    print ( ' (%2d)' % ( g[i,m] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def simplex_grid_index_to_point ( m, n, ng, g, v ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_TO_POINT returns  points corresponding to simplex indices.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of subintervals.
#
#    Input, integer NG, the number of grid indices to be converted.
#
#    Input, integer G(NG,M+1), the grid indices of 1 or more points.
#
#    Input, real V(M+1,M), the coordinates of the vertices of the simplex.
#
#    Output, real X(NG,M), the coordinates of one or more points.
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

def simplex_grid_index_to_point_test01 ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_TO_POINT_TEST01 tests SIMPLEX_GRID_INDEX_TO_POINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_TO_POINT_TEST01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_GRID_INDEX_TO_POINT returns the physical point' )
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

  seed = 123456789

  g, seed = simplex_grid_index_sample ( m, n, ng, seed )

  x = simplex_grid_index_to_point ( m, n, ng, g, v )

  for i in range ( 0, ng ):
    print ( '  %2d:' % ( i ) ),
    for j in range ( 0, m + 1 ):
      print ( ' %2d' % ( g[i,j] ) ),
    for j in range ( 0, m ):
      print ( ' %8.4f' % ( x[i,j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_TO_POINT_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def simplex_grid_index_to_point_test02 ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_INDEX_TO_POINT_TEST02 tests SIMPLEX_GRID_INDEX_TO_POINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_TO_POINT_TEST02:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_GRID_INDEX_TO_POINT returns the physical point' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_INDEX_TO_POINT_TEST02:' )
  print ( '  Normal end of execution.' )
  return

def simplex_grid_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_TEST tests the SIMPLEX_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SIMPLEX_GRID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SIMPLEX_GRID library.' )
#
#  Utilities:
#
  comp_next_grlex_test ( )
  comp_random_test ( )
  comp_random_grlex_test ( )
  comp_rank_grlex_test ( )
  comp_unrank_grlex_test ( )

  i4_choose_test ( )
  i4_uniform_ab_test ( )

  i4mat_print_test ( )
  i4mat_print_some_test ( )

  i4vec_print_test ( )
  i4vec_sum_test ( )
  i4vec_uniform_ab_test ( )

  ksub_random2_test ( )

  r8_uniform_01_test ( )

  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )

  timestamp_test ( )
#
#  Library.
#
  simplex_grid_count_test ( )
  simplex_grid_index_next_test ( )
  simplex_grid_index_sample_test ( )
  simplex_grid_index_all_test ( )
  simplex_grid_index_to_point_test01 ( )
  simplex_grid_index_to_point_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  simplex_grid_test ( )
  timestamp ( )

