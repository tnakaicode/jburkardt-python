#! /usr/bin/env python3
#
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
#    integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  
#
#  Output:
#
#    integer N_DATA.  The routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
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
  import platform

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
  import platform

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
#    rng: the current random number generator.
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
  import platform

  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

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
#    rng: the current random number generator.
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
#    int M, the spatial dimension.
#
#    int X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, 0 ].
#
#  Output:
#
#    int X[M], the next monomial.
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
#    rng: the current random number generator.
#
  import numpy as np

  m = 4

  print ( '' )
  print ( 'mono_next_grlex_test():' )
  print ( '  mono_next_grlex() computes the next monomial' )
  print ( '  in M variables in grlex order.' )
  print ( '' )
  print ( '  Let M =  %d' % ( m ) )

  a = 0
  b = 3

  for i in range ( 0, 10 ):

    x = rng.integers ( low = a, high = b, size = m, endpoint = True )
    print ( '' )
    print ( '  ' ),
    for k in range ( 0, m ):
      print ( '%2d' % ( x[k] ) ),
    print ( '' )

    for j in range ( 0, 5 ):
      x = mono_next_grlex ( m, x )
      print ( '  ' ),
      for k in range ( 0, m ):
        print ( '%2d' %  ( x[k] ) ),
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
  import platform

  print ( '' )
  print ( 'mono_print_tes()t' )
  print ( '  mono_print() prints a monomial.' )
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
  import platform
 
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
    print ( '  %2d    ' % ( i ) ),
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ) ),
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

    print ( '  %3d    ' % ( rank ) ),
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ) ),
    print ( '' )

  return

def mono_total_next_grlex ( m, n, x ):

#*****************************************************************************80
#
## mono_total_next_grlex(): grlex next monomial, total degree equal to N.
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
#    1 |  0     0     3        3
#    2 |  0     1     2        3
#    3 |  0     2     1        3
#    4 |  0     3     0        3
#    5 |  1     0     2        3
#    6 |  1     1     1        3
#    7 |  1     2     0        3
#    8 |  2     0     1        3
#    9 |  2     1     0        3
#   10 |  3     0     0        3
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
#    integer N, the total degree.
#    0 <= N1 <= N2.
#
#    integer X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, N ].
#    The last is [ N, 0, ..., 0, 0 ].
#
#  Output:
#
#    integer X[M], the next monomial.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'mono_total_next_grlex - Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'mono_total_next_grlex - Fatal error!' )

  if ( np.sum ( x ) != n ):
    print ( '' )
    print ( 'mono_total_next_grlex - Fatal error!' )
    print ( '  Input X sums is not N.' )
    raise Exception ( 'mono_total_next_grlex - Fatal error!' )

  if ( n == 0 ):
    return x

  if ( x[0] == n ):
    x[0] = 0
    x[m-1] = n
  else:
    x = mono_next_grlex ( m, x )

  return x

def mono_total_next_grlex_test ( ):

#*****************************************************************************80
#
## mono_total_next_grlex_test() tests mono_total_next_grlex().
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
  print ( 'mono_total_next_grlex_test():' )
  print ( '  mono_total_next_grlex() lists the monomials' )
  print ( '  in M variables, of total degree N,' )
  print ( '  in grlex order, one at a time.' )
  print ( '' )
  print ( '  We start the process with (0,0,...,0,N).' )
  print ( '  The process ends with (N,0,...,0,0)' )

  n = 3;

  print ( '' )
  print ( '  Let M =   %d' % ( m ) )
  print ( '      N =   %d' % ( n ) )
  print ( '' )

  x = np.array ( [ 0, 0, n ], dtype = np.int32 )
 
  i = 1;

  while ( True ):

    print ( '  %2d    ' % ( i ) ),
    for k in range ( 0, m ):
      print ( '%2d' % ( x[k] ) ),
    print ( '' )

    if ( x[0] == n ):
      break

    x = mono_total_next_grlex ( m, n, x )
    i = i + 1

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
#    rng: the current random number generator.
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
    print ( '  %2d    ' % ( i ) ),
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ) ),
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
    print ( '  %2d    ' % ( rank ) ),
    for j in range ( 0, m ):
      print ( '%2d' % ( x[j] ) ),
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
#    int M, the spatial dimension.
#
#    int N, the maximum degree.
#
#  Output:
#
#    int VALUE, the number of monomials in
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
  import platform

  print ( '' )
  print ( 'mono_upto_enum_test():' )
  print ( '  mono_upto_enum() can enumerate the number of monomials' )
  print ( '  in M variables, of total degree between 0 and N.' )

  print ( '' )
  print ( '    N:' ),
  for n in range ( 0, 9 ):
    print ( '  %4d' % ( n ) ),
  print ( '' )
  print ( '   M +---------------------------------------------------------------' )
  for m in range ( 1, 9 ):
    print ( '  %2d |' % ( m ) ),
    for n in range ( 0, 9 ):
      v = mono_upto_enum ( m, n )
      print ( ' %5d' % ( v ) ),
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
  import platform

  m = 3

  print ( '' )
  print ( 'mono_upto_next_grlex_test():' )
  print ( '  mono_upto_next_grlex() lists the monomials' )
  print ( '  in M variables, of total degree up to N,' )
  print ( '  in grlex order, one at a time.' )
  print ( '' )
  print ( '  We start the process with (0,0,...,0,0).' )
  print ( '  The process ends with (N,0,...,0,0)' )

  n = 4;

  print ( '' )
  print ( '  Let M =   %d' % ( m ) )
  print ( '      N =   %d' % ( n ) )
  print ( '' )

  x = np.array ( [ 0, 0, 0 ], dtype = np.int32 )
 
  i = 1;

  while ( True ):

    print ( '  %2d    ' % ( i ) ),
    for k in range ( 0, m ):
      print ( '%2d' % ( x[k] ) ),
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
#    rng: the current random number generator.
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
#    rng: the current random number generator.
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
#    real X[M*N], the coordinates of the evaluation points.
#
#  Output:
#
#    real mono_value[N], the value of the monomial at X.
#
  import numpy as np

  v = np.zeros ( n, dtype = np.float64 )

  for j in range ( 0, n ):
    v[j] = 1.0
    for i in range ( 0, m ):
      v[j] = v[j] * ( x[i+j*m] ** f[i] )

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
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  m = 3
  nx = 2
  x = np.array ( [ 1.0, 2.0, 3.0, -2.0, 4.0, 1.0 ], dtype = np.float64 )

  print ( '' )
  print ( 'mono_value_test():' )
  print ( '  mono_value() evaluates a monomial.' )

  n = 6

  print ( '' )
  print ( '  Let M = %d' % ( m ) )
  print ( '      N = %d' % ( n ) )

  test_num = 5

  for test in range ( 0, test_num ):
    f, rank = mono_upto_random ( m, n, rng )
    print ( '' )
    mono_print ( m, f, '  M(X) = ' )
    v = mono_value ( m, nx, f, x )
    for j in range ( 0, nx ):
      print ( '  M(%g,%g,%g) = %g' % ( x[0+j*m], x[1+j*m], x[2+j*m], v[j] ) )

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
#    rng: the current random number generator.
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
#    rng: the current random number generator.
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
    print ( ' ' )

  return

def polynomial_add ( o1, c1, e1, o2, c2, e2 ):

#*****************************************************************************80
#
## polynomial_add() adds two polynomials.
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
#    integer O1, the "order" of polynomial 1.
#
#    real C1[O1], the coefficients of polynomial 1.
#
#    integer E1[O1], the indices of the exponents of 
#    polynomial 1.
#
#    integer O2, the "order" of polynomial 2.
#
#    real C2[O2], the coefficients of polynomial 2.
#
#    integer E2[O2], the indices of the exponents of 
#    polynomial 2.
#
#  Output:
#
#    integer O, the "order" of the polynomial sum.
#
#    real C[O], the coefficients of the polynomial sum.
#
#    integer E[O], the indices of the exponents of 
#    the polynomial sum.
#
  o = o1 + o2
  c = r8vec_concatenate ( o1, c1, o2, c2 )
  e = i4vec_concatenate ( o1, e1, o2, e2 )

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_add_test ( ):

#*****************************************************************************80
#
## polynomial_add_test() tests polynomial_add().
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
  import platform

  m = 3
  o1 = 6
  c1 = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )

  o2 = 5
  c2 = np.array ( [ 2.0, 3.0, -8.0, 4.0, 9.0 ], dtype = np.float64 )
  e2 = np.array ( [ 1, 3, 4, 30, 33 ], dtype = np.int32 )

  print ( '' )
  print ( 'polynomial_add_test():' )
  print ( '  polynomial_add() adds two polynomials' )

  print ( '' )
  title = '  P1(X):'
  polynomial_print ( m, o1, c1, e1, title )

  print ( '' )
  title = '  P2(X):'
  polynomial_print ( m, o2, c2, e2, title )

  o, c, e = polynomial_add ( o1, c1, e1, o2, c2, e2 )

  print ( '' )
  title = '  P(X) = P1(X) + P2(X):'
  polynomial_print ( m, o, c, e, title )

  return

def polynomial_axpy ( s, o1, c1, e1, o2, c2, e2 ):

#*****************************************************************************80
#
## polynomial_axpy() adds a multiple of one polynomial to another.
#
#  Discussion:
#
#    P(X) = S * P1(X) + P2(X)
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
#    real S, the multiplier for the first polynomial.
#
#    integer O1, the "order" of polynomial 1.
#
#    real C1[O1], the coefficients of polynomial 1.
#
#    integer E1[O1], the indices of the exponents of 
#    polynomial 1.
#
#    integer O2, the "order" of polynomial 2.
#
#    real C2[O2], the coefficients of polynomial 2.
#
#    integer E2[O2], the indices of the exponents of 
#    polynomial 2.
#
#  Output:
#
#    integer O, the "order" of the polynomial sum.
#
#    real C[O], the coefficients of the polynomial sum.
#
#    integer E[O], the indices of the exponents of 
#    the polynomial sum.
#
  import numpy as np

  o = o1 + o2

  sc1 = np.zeros ( o1, dtype = np.float64 )
  for i in range ( 0, o1 ):
    sc1[i] = s * c1[i]

  c = r8vec_concatenate ( o1, sc1, o2, c2 )
  e = i4vec_concatenate ( o1, e1, o2, e2 )

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_axpy_test ( ):

#*****************************************************************************80
#
## polynomial_axpy_test() tests polynomial_axpy().
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
  import platform

  m = 3
  o1 = 6
  c1 = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )

  o2 = 5
  c2 = np.array ( [ 2.0, 3.0, -8.0, 4.0, 9.0 ], dtype = np.float64 )
  e2 = np.array ( [ 1, 3, 4, 30, 33 ], dtype = np.int32 )

  s = 10.0

  print ( '' )
  print ( 'polynomial_axpy_test():' )
  print ( '  polynomial_axpy() adds a multiple of one polynomial to another.' )

  print ( '' )
  title = '  P1(X):'
  polynomial_print ( m, o1, c1, e1, title )

  print ( '' )
  title = '  P2(X):'
  polynomial_print ( m, o2, c2, e2, title )

  print ( '' )
  print ( '  Use the multiplier S = %g' % ( s ) )
  o, c, e = polynomial_axpy ( s, o1, c1, e1, o2, c2, e2 )

  print ( '' )
  title = '  P(X) = S * P1(X) + P2(X):'
  polynomial_print ( m, o, c, e, title )

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
  import platform

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

def polynomial_dif ( m, o1, c1, e1, dif ):

#*****************************************************************************80
#
## polynomial_dif() differentiates a polynomial.
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
#    integer M, the spatial dimension.
#
#    integer O1, the "order" of polynomial 1.
#
#    real C1[O1], the coefficients of polynomial 1.
#
#    integer E1[O1], the indices of the exponents of 
#    polynomial 1.
#
#    integer DIF[M], indicates the number of 
#    differentiations in each component.
#
#  Output:
#
#    integer O, the "order" of the polynomial derivative.
#
#    real C[O], the coefficients of the polynomial derivative.
#
#    integer E[O], the indices of the exponents of 
#    the polynomial derivative.
#
  import numpy as np

  o = o1
  c = np.zeros ( o, dtype = np.float64 )
  for i in range ( 0, o ):
    c[i] = c1[i]
  e = np.zeros ( o, dtype = np.int32 )

  for j in range ( 0, o1 ):
    f1 = mono_unrank_grlex ( m, e1[j] )
    for i in range ( 0, m ):
      c[j] = c[j] * i4_fall ( f1[i], dif[i] )
      f1[i] = max ( f1[i] - dif[i], 0 )
    e[j] = mono_rank_grlex ( m, f1 )

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_dif_test ( ):

#*****************************************************************************80
#
## polynomial_dif_test() tests polynomial_dif().
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
  import platform

  m = 2
  o1 = 4
  c1 = np.array ( [ 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 10, 12, 32 ], dtype = np.int32 )
  dif = np.array ( [ 2, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'polynomial_dif_test():' )
  print ( '  polynomial_dif() differentiates a polynomial.' )

  print ( '' )
  title = '  P(X):'
  polynomial_print ( m, o1, c1, e1, title )

  o, c, e = polynomial_dif ( m, o1, c1, e1, dif )

  print ( '' )
  title = '  d3 P(X) dx1 dx1 dx2 ='
  polynomial_print ( m, o, c, e, title )

  return

def polynomial_mul ( m, o1, c1, e1, o2, c2, e2 ):

#*****************************************************************************80
#
## polynomial_mul() multiplies two polynomials.
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
#    integer M, the spatial dimension.
#
#    integer O1, the "order" of polynomial 1.
#
#    real C1[O1], the coefficients of polynomial 1.
#
#    integer E1[O1], the indices of the exponents of 
#    polynomial 1.
#
#    integer O2, the "order" of polynomial 2.
#
#    real C2[O2], the coefficients of polynomial 2.
#
#    integer E2[O2], the indices of the exponents of 
#    polynomial 2.
#
#  Output:
#
#    integer O, the "order" of the polynomial product.
#
#    real C[O], the coefficients of the polynomial product.
#
#    integer E[O], the indices of the exponents of 
#    the polynomial product.
#
  import numpy as np

  f = np.zeros ( m, dtype = np.int32 )
  c = np.zeros ( o1 * o2, dtype = np.float32 )
  e = np.zeros ( o1 * o2, dtype = np.int32 )

  o = 0
  for j in range ( 0, o2 ):
    for i in range ( 0, o1 ):
      c[o] = c1[i] * c2[j]
      f1 = mono_unrank_grlex ( m, e1[i] )
      f2 = mono_unrank_grlex ( m, e2[j] )
      for k in range ( 0, m ):
        f[k] = f1[k] + f2[k]
      e[o] = mono_rank_grlex ( m, f )
      o = o + 1

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_mul_test ( ):

#*****************************************************************************80
#
## polynomial_mul_test() tests polynomial_mul().
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

  m = 3
  o1 = 4
  c1 = np.array ( [ 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 3, 4, 6 ], dtype = np.int32 )

  o2 = 2
  c2 = np.array ( [ 6.0, 7.0 ], dtype = np.float64 )
  e2 = np.array ( [ 2, 5 ], dtype = np.int32 )

  print ( '' )
  print ( 'polynomial_mul_test():' )
  print ( '  polynomial_mul() multiplies two polynomials' )

  print ( '' )
  title = '  P1(X):'
  polynomial_print ( m, o1, c1, e1, title )

  print ( '' )
  title = '  P2(X):'
  polynomial_print ( m, o2, c2, e2, title )

  o, c, e = polynomial_mul ( m, o1, c1, e1, o2, c2, e2 )

  print ( '' )
  title = '  P(X) = P1(X) * P2(X):'
  polynomial_print ( m, o, c, e, title )

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
  import platform

  print ( '' )
  print ( 'polynomial_print_test():' )
  print ( '  polynomial_print() prints a polynomial.' )

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )
  title = '  P1(X) ='

  print ( '' )
  polynomial_print ( m, o, c, e, title )

  return

def polynomial_test ( ):

#*****************************************************************************80
#
## polynomial_test() tests polynomial().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomial().' )

  rng = default_rng ( )

  i4_fall_test ( )

  i4vec_concatenate_test ( )
  i4vec_permute_test ( rng )
  i4vec_sort_heap_index_a_test ( rng )

  r8vec_concatenate_test ( )
  r8vec_permute_test ( )
 
  perm0_uniform_test ( rng )

  mono_upto_enum_test ( )
  mono_next_grlex_test ( rng )
  mono_rank_grlex_test ( )
  mono_total_next_grlex_test ( )
  mono_unrank_grlex_test ( rng )
  mono_value_test ( rng )

  polynomial_add_test ( )
  polynomial_axpy_test ( )
  polynomial_compress_test ( )
  polynomial_dif_test ( )
  polynomial_mul_test ( )
  polynomial_print_test ( )
  polynomial_scale_test ( )
  polynomial_sort_test ( )
  polynomial_value_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomial_test():' )
  print ( '  Normal end of execution.' )
  return

def polynomial_scale ( s, m, o, c, e ):

#*****************************************************************************80
#
## polynomial_scale() scales a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real S, the scale factor.
#
#    integer M, the spatial dimension.
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
#    integer O, the "order" of the polynomial.
#
#    real C[O], the coefficients of the scaled polynomial.
#
#    integer E[O], the indices of the exponents of 
#    the scaled polynomial.
#
  for i in range ( 0, o ):
    c[i] = c[i] * s

  return o, c, e

def polynomial_scale_test ( ):

#*****************************************************************************80
#
## polynomial_scale_test() tests polynomial_scale().
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
  import platform

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )

  print ( '' )
  print ( 'polynomial_scale_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polynomial_scale() scales a polynomial by a multiplier S.' )

  print ( '' )
  title = '  Original P(X):'
  polynomial_print ( m, o, c, e, title )

  s = - 0.5
  print ( '' )
  print ( '  Apply scale factor S = %g' % ( s ) )
  o, c, e = polynomial_scale ( s, m, o, c, e )

  print ( '' )
  title = '  S * P(X):'
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
  import platform

  m = 3
  o = 6
  c = np.array ( [ 0.0, 9.0, -5.0, - 13.0, 7.0, 11.0 ], dtype = np.float64 )
  e = np.array ( [ 12, 4, 2, 33, 1, 5 ], dtype = np.int32 )

  print ( '' )
  print ( 'polynomial_sort_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  import platform

  m = 3
  o = 6
  c = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )
  nx = 2
  x = np.array ( [ 1.0, 2.0, 3.0, \
                  -2.0, 4.0, 1.0 ], dtype = np.float64 );

  print ( '' )
  print ( 'polynomial_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polynomial_value() evaluates a polynomial.' )

  print ( '' )
  title = '  P(X) = '
  polynomial_print ( m, o, c, e, title )

  p = polynomial_value ( m, o, c, e, nx, x )

  print ( '' )
  for j in range ( 0, nx ):
    print ( '  P(%f,%f,%f) = %g' % ( x[0+j*m], x[1+j*m], x[2+j*m], p[j] ) )

  return

def r8vec_concatenate ( n1, a1, n2, a2 ):

#*****************************************************************************80
#
## r8vec_concatenate() concatenates two R8VEC's.
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
#    real A1(N1), the first vector.
#
#    integer N2, the number of entries in the second vector.
#
#    real A2(N2), the second vector.
#
#  Output:
#
#    real A3(N1+N2), the concatenation of A1 and A2.
#
  import numpy as np

  a3 = np.concatenate ( ( a1, a2 ), axis = 0 )

  return a3

def r8vec_concatenate_test ( ):

#*****************************************************************************80
#
## r8vec_concatenate_test() tests r8vec_concatenate().
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
  import platform

  n1 = 5
  n2 = 3
  n3 = n1 + n2

  a1 = np.array ( [ 91.1, 31.2, 71.3, 51.4, 31.5 ] )
  a2 = np.array ( [ 42.6, 22.7, 12.8 ] )

  print ( '' )
  print ( 'r8vec_concatenate_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_concatenate() concatenates two R8VECs' )

  r8vec_print ( n1, a1, '  Array 1:' )
  r8vec_print ( n2, a2, '  Array 2:' )
  a3 = r8vec_concatenate ( n1, a1, n2, a2 )
  r8vec_print ( n3, a3, '  Array 3 = Array 1 + Array 2:' )

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
  import platform

  n = 5

  print ( '' )
  print ( 'r8vec_permute_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  polynomial_test ( )
  timestamp ( )

