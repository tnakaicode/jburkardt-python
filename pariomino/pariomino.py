#! /usr/bin/env python3
#
def filename_inc ( filename ):

#*****************************************************************************80
#
## filename_inc() generates the next filename in a series.
#
#  Discussion:
#
#    It is assumed that the digits in the name, whether scattered or
#    connected, represent a number that is to be increased by 1 on
#    each call.  If this number is all 9's on input, the output number
#    is all 0's.  Non-numeric letters of the name are unaffected..
#
#    If the name is empty, then the routine stops.
#
#    If the name contains no digits, the empty string is returned.
#
#  Example:
#
#      Input            Output
#      -----            ------
#      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
#      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
#      'a9to99.txt'     'a0to00.txt'  (wrap around)
#      'cat.txt'        ' '           (no digits in input name.)
#      ' '              STOP!         (error.)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the string to be incremented.
#
#  Output:
#
#    string FILENAME, the incremented string.
#
  i0 = ord ( '0' )
  i8 = ord ( '8' )
  i9 = ord ( '9' )

  lens = len ( filename )

  if ( lens <= 0 ):
    return None

  change = 0
  filename2 = ''

  for i in range ( lens - 1, -1, -1 ):

    c = filename[i]

    ic = ord ( c )

    if ( change < 2 and i0 <= ic and ic <= i8 ):
      ic = ic + 1
      filename2 = chr ( ic ) + filename2
      change = 2
    elif ( change == 0 and ic == i9 ):
      change = 1
      c = '0'
      filename2 = c + filename2
    else:
      filename2 = c + filename2

  if ( change == 0 ):
    filename2 = None

  return filename2

def filename_inc_test ( ):

#*****************************************************************************80
#
## filename_inc_test() tests filename_inc().
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
  print ( '' )
  print ( 'filename_inc_test():' )
  print ( '  filename_inc() "increments" a string' )
  print ( '' )
  print ( '     Input             Output' )

  for i in range ( 0, 4 ):

    if ( i == 0 ):
      filename = 'file???.dat'
    elif ( i == 1 ):
      filename = 'file072.dat'
    elif ( i == 2 ):
      filename = '2cat9.dat  '
    elif ( i == 3 ):
      filename = 'fred99.txt '

    print ( '' )
    for j in range ( 0, 4 ):
      filename2 = filename_inc ( filename )
      print ( '  ', filename, ' ' , filename2 )
      filename = filename2
      if ( filename == None ):
        break

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
#    bool i4mat_is_ternary, is true (1) if X only contains
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
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, \
    '  Here is I4MAT, rows 0:2, cols 3:5:' )
#
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
#    bool DONE, should be TRUE on the first call, to force initialization,
#    and then FALSE on subsequent calls.
#
#  Output:
#
#    integer A(K), as long as DONE is returned FALSE, A 
#    is the next K subset.
#
#    bool DONE, is TRUE if the routine is returning the
#    next K subset, and FALSE if there are no more subsets to return.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_next4 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    raise Exception ( 'ksub_next4 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_next4 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    raise Exception ( 'ksub_next4 - Fatal error!' )
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

def pariomino_test ( ):

#*****************************************************************************80
#
## pariomino_test() tests pariomino().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pariomino_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pariomino().' )

  filename_inc_test ( )

  i4mat_is_ternary_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )

  ksub_next4_test ( )

  pariomino_area_test ( )
  pariomino_condense_test ( )
  pariomino_embed_list_test ( )
  pariomino_embed_number_test ( )
  pariomino_equal_test ( )
  pariomino_index_test ( )
  pariomino_lp_write_test ( )
  pariomino_matrix_test ( )
  pariomino_matrix_reid_test ( )
  pariomino_parity_test ( )
  pariomino_print_test ( )
  pariomino_reverse_test ( )
# pariomino_tiling_plot_test01 ( )
# pariomino_tiling_plot_test02 ( )
  pariomino_tiling_print_test01 ( )
  pariomino_tiling_print_test02 ( )
  pariomino_tiling_solver_test01 ( )
  pariomino_tiling_solver_test02 ( )
  pariomino_transform_test ( )
  pariomino_variants_test01 ( )
  pariomino_variants_test02 ( )

  pariominoes_print_test ( )

  polyomino_charge_test ( )
  polyomino_print_test ( )

  r8mat_rref_test ( )
  r8mat_rref_solve_binary_test ( )
  r8mat_rref_solve_binary_nz_test ( )
  r8mat_u_solve_test ( )

  r8vec_binary_next_test ( )
  r8vec_identity_row_test ( )
  r8vec_is_binary_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pariomino_test():' )
  print ( '  Normal end of execution.' )

  return

def pariomino_area ( p ):

#*****************************************************************************80
#
## pariomino_area() returns the area of a pariomino.
#
#  Discussion:
#
#    A pariomino is a shape formed by connecting unit squares edgewise.
#
#    A pariomino can be represented by an MxN matrix, whose entries are
#    +1 or -1 for squares that are part of the pariomino, and 0 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(MP,NP), a matrix of -1's, 0's and +1's representing the pariomino.  
#
#  Output:
#
#    integer AREA, the area of the pariomino.
#
  area = sum ( sum ( abs ( p ) ) )

  return area

def pariomino_area_test ( ):

#*****************************************************************************80
#
## pariomino_area_test() tests pariomino_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_area_test' )
  print ( '  pariomino_area() returns the area of a pariomino.' )

  p = np.array ( [ \
    [ 1, -1, 1, -1 ] ] )
  pariomino_print ( p, '  pariomino #1:' )
  area = pariomino_area ( p )
  print ( '  Area is', area )

  p = np.array ( [ \
    [ -1,  1,  0 ], \
    [  0, -1,  0 ], \
    [  0,  1, -1 ] ] )
  pariomino_print ( p, '  pariomino #2:' )
  area = pariomino_area ( p )
  print ( '  Area is', area )

  p = np.array ( [ \
    [  1,  0,  0 ], \
    [ -1,  1, -1 ] ] )
  pariomino_print ( p, '  pariomino #3:' )
  area = pariomino_area ( p )
  print ( '  Area is', area )

  p = np.array ( [ \
    [  0,  0,  0,  0, -1,  0 ], \
    [ +1,  0,  0,  0, +1, -1 ], \
    [ -1,  0, -1, +1, -1,  0 ], \
    [ +1,  0, +1,  0, +1,  0 ], \
    [ -1, +1, -1, +1, -1,  0 ] ] )
  pariomino_print ( p, '  pariomino #4:' )
  area = pariomino_area ( p )
  print ( '  Area is', area )
 
  return

def pariomino_condense ( p ):

#*****************************************************************************80
#
## pariomino_condense() condenses a pariomino.
#
#  Discussion:
#
#    A pariomino is a shape formed by connecting unit squares edgewise.
#
#    A pariomino can be represented by an MxN matrix, whose entries are
#    -1 or +1 for squares that are part of the pariomino, and 0 otherwise.
#
#    This program is given an MxN matrix that is meant to represent a 
#    pariomino.  It  "condenses" the matrix, if possible, by removing initial 
#    and final rows and columns that are entirely zero.
#
#    While this procedure might save a slight amount of space, its purpose
#    is to simplify the task of manipulating pariominos, embedding them in
#    larger shapes, and detecting whether two pariominos describe the same
#    shape.
#
#    It is entirely possible, and usual, that the output quantities are
#    simply copies of the input quantities.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(MP,NP), the representation of the pariomino.  
#
#  Output:
#
#    integer Q(MQ,NQ), the representation of the condensed pariomino.
#
  import numpy as np

  prow, pcol = p.shape
#
#  Discard nonsense.
#
  if ( prow <= 0 or pcol <= 0 ):
    mq = 0
    nq = 0
    q = np.zeros ( [ mq, nq ] )
    return q
#
#  Copy the input.
#
  mq = prow
  nq = pcol
  q = np.copy ( p )
#
#  Strip initial rows of zeros.
#
  while ( sum ( abs ( q[0,:] ) ) == 0 ):
    q = q[1:mq,:]
    mq = mq - 1
    if ( mq <= 0 ):
      mq = 0
      nq = 0
      q = np.zeros ( [ mq, nq ] )
      return q
#
#  Strip final rows of zeros.
#
  while ( sum ( abs ( q[mq-1,:] ) ) == 0 ):
    q = q[0:mq-1,:]
    mq = mq - 1
    if ( mq <= 0 ):
      mq = 0
      nq = 0
      q = np.zeros ( [ mq, nq ] )
      return q
#
#  Strip initial columns of zeros.
#
  while ( sum ( abs ( q[:,0] ) ) == 0 ):
    q = q[:,1:nq]
    nq = nq - 1
    if ( nq <= 0 ):
      mq = 0
      nq = 0
      q = np.zeros ( [ mq, nq ] )
      return q
#
#  Strip final columns of zeros.
#
  while ( sum ( abs ( q[:,nq-1] ) ) == 0 ):
    q = q[:,0:nq-1]
    nq = nq - 1
    if ( nq <= 0 ):
      mq = 0
      nq = 0
      q = np.zeros ( [ mq, nq ] )
      return q

  return q

def pariomino_condense_test ( ):

#*****************************************************************************80
#
## pariomino_condense_test() tests pariomino_condense().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_condense_test:' )
  print ( '  pariomino_condense() "cleans up" a matrix that' )
  print ( '  represents a pariomino by eliminating initial and final:' )
  print ( '  rows and columns of zeros.' )
#
#  Nothing happens:
#
  p = np.array ( [ \
    [  0, -1, +1 ], \
    [ -1, +1,  0 ], \
    [  0, -1,  0 ] ] )
  condense_demo ( p )
#
#  Nonzero, but non-one entries are set to 1.
#
  p = np.array ( [ \
    [ 0,  0,  0, 0 ], \
    [ 0, +1, -1, 0 ], \
    [ 0, -1, +1, 0 ], \
    [ 0,  0,  0, 0 ] ] )
  condense_demo ( p )
#
#  Internal zero rows and columns are NOT removed.
#
  p = np.array ( [ \
    [ +1, -1,  0, -1 ], \
    [  0,  0,  0,  0 ], \
    [ +1, -1,  0, -1 ] ] )
  condense_demo ( p )
#
#  Null matrices are detected.
#
  p = np.array ( [ \
    [ 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0 ] ] )
  condense_demo ( p )

  return

def condense_demo ( p ):

#*****************************************************************************80
#
## condense_demo() demonstrates the result of calling pariomino_condense().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(MP,NP), a matrix representing the pariomino.  
#
  mp, np = p.shape
  label = ( '  The initial (%d,%d) pariomino P:' % ( mp, np ) )
  pariomino_print ( p, label )

  q = pariomino_condense ( p )
  mq, nq = q.shape
  label = ( '  The condensed (%d,%d) pariomino Q:' % ( mq, nq ) )
  pariomino_print ( q, label )

  return

def pariomino_embed_list ( r,  p, number ):

#*****************************************************************************80
#
## pariomino_embed_list() lists the pariomino embeddings in a region.
#
#  Discusion:
#
#    A region R is a subset of an MRxNR grid of squares.
#
#    A pariomino P is a subset of an MPxNP grid of squares.
#
#    Both objects are represented by -1, 0, +1 matrices, with the property that
#    there are no initial or final zero rows or columns.
#
#    For this computation, we regard P as a "fixed" pariomino in other words,
#    no reflections or rotations will be allowed.
#
#    An "embedding" of P into R is an offset (MI,NJ) such that 
#      P(I,J) = R(I+MI,J+NJ) 
#      for 1 <= I <= MP, 1 <= J <= NP, and 
#      for 0 <= MI <= MR-MP, 0 <= MJ <= NR-NP.
#    We can detect an embedding simply by taking what amounts to a kind of
#    dot product of P with a corresponding subregion of R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer R(MR,NR), a matrix of -1's, 0's and 1's representing the region.
#
#    integer P(MP,NP), a matrix of -1's, 0's and 1's representing the pariomino.
#
#    integer NUMBER, the number of embeddings.
#
#  Output:
#
#    integer LST(NUMBER,2), for each embedding, the I and J offsets applied 
#    to the pariomino P.
#
  import numpy as np

  m_r, n_r = r.shape
  m_p, n_p = p.shape

  lst = np.zeros ( [ number, 2 ], dtype = int )
#
#  Count the -1's and +1's in P.
#
  pr = pariomino_area ( p )
#
#  For each possible (I,J) coordinate of the upper left corner of a subset of R,
#  see if such a subset exactly matches P.
#
  k = 0
  for m_i in range ( 0, m_r - m_p + 1 ):
    for n_j in range ( 0, n_r - n_p + 1 ):
      srp = sum ( sum ( p * r[m_i:m_p+m_i,n_j:n_p+n_j] ) )
      if ( srp == pr ):
        lst[k,0] = m_i
        lst[k,1] = n_j
        k = k + 1

  return lst

def pariomino_embed_list_test ( ):

#*****************************************************************************80
#
## pariomino_embed_list_test() tests pariomino_embed_list().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#   27 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_embed_list_test:' )
  print ( '  pariomino_embed_list() lists the offsets used' )
  print ( '  to embed a fixed pariomino in a region.' )

  m_r = 4
  n_r = 4
  r = np.array ( [ \
    [  0, +1, -1, +1 ], \
    [ +1, -1,  0, -1 ], \
    [ -1, +1, -1, +1 ], \
    [ +1,  0, +1, -1 ] ] )

  pariomino_print ( r, '  region R:' )

  m_p = 3
  n_p = 2
  p = np.array ( [ \
    [  0, +1 ], \
    [  0, -1 ], \
    [ -1, +1 ] ] )

  pariomino_print ( p, '  pariomino P:' )
#
#  Get the number of embeddings.
#
  number = pariomino_embed_number ( r, p )

  print ( '' )
  print ( '  P can be embedded in R in ', number, ' ways.', sep = '' )
#
#  Get the list of embeddings.
#
  list = pariomino_embed_list ( r, p, number )

  for k in range ( 0, number ):
    m_k = list[k,0]
    n_k = list[k,1]
    m_q = m_r
    n_q = n_r
    q = r
    q[m_k:m_p+m_k,n_k:n_p+n_k] = q[m_k:m_p+m_k,n_k:n_p+n_k] + p[0:m_p,0:n_p]
    print ( '' )
    print ( '  Embedding #', k, sep = '' )
    print ( '' )
    for i in range ( 0, m_q ):
      print ( '  ', end = '' )
      for j in range ( 0, n_q ):
        if ( q[i,j] == -2 ):
          print ( '*', sep = '', end = '' )
        elif ( q[i,j] == -1 ):
          print ( 'B', sep = '', end = '' ) 
        elif ( q[i,j] == 0 ):
          print ( '.', sep = '', end = '' )
        elif ( q[i,j] == +1 ):
          print ( 'W', sep = '', end = '' )
        elif ( q[i,j] == +2 ):
          print ( '*', sep = '', end = '' )
      print ( '' )

  return

def pariomino_embed_number ( r, p ):

#*****************************************************************************80
#
## pariomino_embed_number() counts pariomino embeddings in a region.
#
#  Discusion:
#
#    A region R is a subset of an MRxNR grid of squares.
#
#    A polyomino P is a subset of an MPxNP grid of squares.
#
#    Both objects are represented by parity (-1/+1) matrices, with the 
#    property that there are no initial or final zero rows or columns.
#
#    For this computation, we regard P as a "fixed" pariomino; in other words,
#    no reflections or rotations will be allowed.
#
#    An "embedding" of P into R is an offset (MI,NJ) such that 
#      P(I,J) = R(I+MI,J+NJ) 
#      for 1 <= I <= MP, 1 <= J <= NP, and 
#      for 0 <= MI <= MR-MP, 0 <= MJ <= NR-NP.
#    We can detect an embedding simply by taking what amounts to a kind of
#    dot product of P with a corresponding subregion of R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer R(MR,NR), a matrix of -1's, 0's, and 1's representing the region.
#
#    integer P(MP,NP), a matrix of -1's, 0's and 1's representing the pariomino.
#
#  Output:
#
#    integer NUMBER, the number of distinct embeddings of P into R.
#
  number = 0

  rm, rn = r.shape
  pm, pn = p.shape
#
#  Count the -1's and +1's in P.
#
  pr = pariomino_area ( p )
#
#  For each possible (I,J) coordinate of the upper left corner of a subset of R,
#  see if it matches P.
#
  for im in range ( 0, rm - pm + 1 ):
    for jn in range ( 0, rn - pn + 1 ):
      pr2 = sum ( sum ( p * r[im:im+pm,jn:jn+pn] ) )
      if ( pr2 == pr ):
        number = number + 1

  return number

def pariomino_embed_number_test ( ):

#*****************************************************************************80
#
## pariomino_embed_number_test() tests pariomino_embed_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_embed_number_test:' )
  print ( '  pariomino_embed_number() reports the number of ways a' )
  print ( '  fixed pariomino can be embedded in a region.' )

  r = np.array ( [ \
    [  0, -1, +1, -1 ], \
    [ -1, +1,  0, +1 ], \
    [ +1, -1, +1, -1 ], \
    [ -1,  0, -1, +1 ] ] )

  pariomino_print ( r, '  Region R:' )

  p = np.array ( [ \
    [  0, -1 ], \
    [  0, +1 ], \
    [ +1, -1 ] ] )

  pariomino_print ( p, '  Pariomino P:' )

  number = pariomino_embed_number ( r, p )

  print ( '' )
  print ( '  P can be embedded in R in', number, 'ways.' )

  p = np.array ( [ \
    [  0, +1 ], \
    [  0, -1 ], \
    [ -1, +1 ] ] )

  pariomino_print ( p, '  Pariomino P:' )

  number = pariomino_embed_number ( r, p )

  print ( '' )
  print ( '  P can be embedded in R in', number, 'ways.' )

  return

def pariomino_equal ( p1, p2 ):

#*****************************************************************************80
#
## pariomino_equal() determines if pariominoes P1 and P2 are equal.
#
#  Discussion:
#
#    P1 and P2 should only contain -1, 0 and 1 entries.
#
#    The matrix representations P1 and P2 should be "tight", that is, there 
#    should be a nonzero in the first and last rows, and in the first 
#    and last columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P1(M1,N1), the representation of pariomino P1. 
#
#    integer P2(M2,N2), the representation of pariomino P2. 
#
#  Output:
#
#    bool VALUE, is true if P1 and P2 represent the same pariomino.
#
  import numpy as np

  m1, n1 = p1.shape
  m2, n2 = p2.shape
 
  if ( m1 != m2 ):
    value = False
  elif ( n1 != n2 ):
    value = False
  else:
    value = np.all ( np.all ( p1 == p2 ) )

  return value

def pariomino_equal_test ( ):

#*****************************************************************************80
#
## pariomino_equal_test() tests pariomino_equal().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_equal_test' )
  print ( '  pariomino_equal() determines if pariominoes are equal.' )

  p1 = np.array ( [ \
    [ +1,  0, +1, -1 ], \
    [ -1, +1, -1,  0 ], \
    [  0, -1, +1,  0 ] ] )
  pariomino_print ( p1, '  The pariomino P1:' )

  p2 = np.array ( [ \
    [ +1,  0, +1, -1 ], \
    [ -1, +1, -1,  0 ], \
    [  0, -1,  0,  0 ] ] )
  pariomino_print ( p1, '  The pariomino P2:' )

  p3 = np.array ( [ \
    [ +1,  0, +1, -1,  0 ], \
    [ -1, +1, -1,  0,  0 ], \
    [  0, -1, +1,  0,  0 ] ] )
  pariomino_print ( p3, '  The pariomino P3:' )

  p4 = np.array ( [ \
    [ +1,  0, +1, -1 ], \
    [ -1, +1, -1,  0 ], \
    [  0, -1, +1,  0 ] ] )
  pariomino_print ( p4, '  The pariomino P4:' )

  print ( '' )
  value = pariomino_equal ( p1, p1 )
  print ( '  P1 == P1?', value )
  value = pariomino_equal ( p1, p2 )
  print ( '  P1 == P2?', value )
  value = pariomino_equal ( p1, p3 )
  print ( '  P1 == P3?', value )
  value = pariomino_equal ( p1, p4 )
  print ( '  P1 == P4?', value )

  return

def pariomino_index ( p ):

#*****************************************************************************80
#
## pariomino_index() assigns an index to each nonzero entry of a polyomino.
#
#  Discussion:
#
#    The indexing scheme arbitrarily proceeds by rows.
#
#  Example:
#
#    P = 
#      +1  0 +1 -1
#      -1 +1 -1  0
#       0 -1 +1  0
#
#    PIN =
#      1 0 2 3
#      4 5 6 0
#      0 7 8 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(M,N), the pariomino, with entries -1, 0, or +1.
#
#  Output:
#
#    integer PIN(M,N), the index of each nonzero entry.
#
  import numpy as np

  m, n = p.shape

  pv = np.reshape ( p, m * n )

  pv = abs ( pv )

  pc = np.cumsum ( pv ) * pv

  pin = np.reshape ( pc, [ m, n ] )

  return pin

def pariomino_index_test ( ):

#*****************************************************************************80
#
## pariomino_index_test() tests pariomino_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_index_test' )
  print ( '  pariomino_index() assigns an index to each nonzero entry' )
  print ( '  of a pariomino.' )

  p = np.array ( [ \
    [ +1,  0, +1, -1 ], \
    [ -1, +1, -1,  0 ], \
    [  0, -1, +1,  0 ] ] )

  pariomino_print ( p, '  The pariomino P:' )

  pin = pariomino_index ( p )

  m, n = pin.shape

  i4mat_print ( m, n, pin, '  The index array for P:' )

  return

def pariomino_lp_write ( filename, label, m, n, a, b ):

#*****************************************************************************80
#
## pariomino_lp_write() writes an LP file for the pariomino problem.
#
#  Discussion:
#
#    We have begun to look at rather large problems, and have encountered
#    software packages that put limits on the maximum length of a line
#    in an LP file.  We try to control this by adding line breaks so that,
#    at least when there are no more than 99,999 variables, the lines of the
#    LP file should be no more than 80 characters long.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the output filename.
#
#    string LABEL, the problem title.
#
#    integer M, the number of equations
#
#    integer N, the number of variables.
#
#    integer A(M,N), the coefficients.
#
#    integer B(M), the right hand sides.
#

#
#  Open the file.
#
  output = open ( filename, 'w' )

  output.write ( label )
  output.write ( '\n' )
  output.write ( '\n' )

  output.write ( 'Maximize\n' )
  output.write ( '  Obj: 0\n' )

  output.write ( 'Subject to\n' )

  for i in range ( 0, m ):

    first = True
    output.write ( ' ' )

    for j in range ( 0, n ):

      if ( a[i,j] != 0 ):

        if ( a[i,j] < 0 ):
          output.write ( ' -' )
        elif ( not first ):
          output.write ( ' +' )

        if ( abs ( a[i,j] ) == 1 ):
          output.write ( ' x%d'%(j+1) )
        else:
          output.write ( ' %d x%d' % ( abs ( a[i,j] ), j+1 ) )

        first = False

    output.write ( ' = %d\n' % ( b[i] ) )

  output.write ( 'Binary\n' )
  output.write ( ' ' )
  for j in range ( 0, n ):
    output.write ( ' x%d' % ( j+1 ) )
  output.write ( '\n' )

  output.write ( 'End' )
#
#  Close the file.
#
  output.close ( )

  return

def pariomino_lp_write_test ( ):

#*****************************************************************************80
#
## pariomino_lp_write_test() tests pariomino_lp_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pariomino_lp_write_test:' )
  print ( '  pariomino_lp_write() writes an LP file associated' )
  print ( '  with a binary programming problem for tiling a region' )
  print ( '  with copies of a single pariomino.' )
#
#  Get the coefficients and right hand side for the Reid system.
#
  a, b = pariomino_matrix_reid ( )
#
#  Create the LP file.
#
  filename = 'reid.lp'
  label = '\ LP file for the Reid example.'
  m, n = a.shape

  pariomino_lp_write ( filename, label, m, n, a, b )

  print ( '' )
  print ( '  pariomino_lp_write created the LP file "%s"' % ( filename ) )

  return

def pariomino_matrix ( r, p_num, p, d ):

#*****************************************************************************80
#
## pariomino_matrix(): linear system pariomino tiling.
#
#  Discussion:
#
#    A region R is represented by an MRxNR binary matrix.
#
#    It is to be tiled by copies of pariominoes which are stored in a
#    MRxNRxP_NUM array P.  Each pariomino can be reflected, rotated,
#    and translated.
#
#    This function computes the linear system A*x=b that can be used to 
#    search for solutions to this tiling problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer R(MR,NR), a binary matrix describing the region.
#
#    integer P(MR,NR,P_NUM), a binary matrix describing the pariominoes.
#    The matrix is "top-left tight", that is, the I-th pariomino is stored
#    in P(1:MR,1:NR,I) with a nonzero in the first row, a nonzero in the 
#    first column, but with trailing rows and columns of zeros allowed.
#
#    integer D(P_NUM), tells us how many copies of each pariomino
#    we must use in the tiling.
#
#  Output:
#
#    integer A(EQN_NUM,VAR_NUM), the system matrix.
#
#    integer B(EQN_NUM), the right hand side.
#
#    integer VAR_P(VAR_NUM).  If variable I is a variant of pariomino
#    J, then VAR_P(I) = J.
#
  import numpy as np
#
#  E will index the nonzero cells in R, and represents equations.
#  Each equation essentially says "Some pariomino covers this cell".
#
  e = pariomino_index ( r )
  e1 = e - 1
#
#  Get the size or R.
#
  mr, nr = r.shape
#
#  From the original set of pariominoes P, compute all the
#  variants obtainable by reflection and rotation.
#
  v_num, v, v_p = pariomino_variants ( mr, nr, p_num, p, d )
#
#  Determine the number of equations:
#  * pariomino_area ( R ) accounts for "this cell is covered" equations.
#  * P_NUM reflects the equations that tell us how many of each pariomino
#    we are to use.
#  * 1 reflects the equation that the total area of the pariominos must
#    equal the area of R.  This equation is extraneous, assuming that
#    the P_NUM equations are consistent.
#
  eqn_num = pariomino_area ( r ) + p_num + 1
#
#  Determine the number of variables.
#  For variable I, set var_p(i) to the index in P of the "parent" pariomino.
#
  var_num = 0
  var_p = np.zeros ( var_num )

  for k in range ( 0, v_num ):

    q = v[0:mr,0:nr,k]

    s = pariomino_condense ( q )

    number = pariomino_embed_number ( r, s )

    for l in range ( 0, number ):
      var_p = np.append ( var_p, [ v_p[k] ] )
      var_num = var_num + 1
#
#  Set aside space for the linear system.
#
  a = np.zeros ( [ eqn_num, var_num ] )
  b = np.ones ( eqn_num )
#
#  Start variable count at 0.
#
  var = 0
#
#  For each V, determine the embeddings.
#  This sets column VAR.
#
  for k in range ( 0, v_num ):

    q = v[0:mr,0:nr,k]

    s = pariomino_condense ( q )

    ms, ns = s.shape

    number = pariomino_embed_number ( r, s )

    list = pariomino_embed_list ( r, s, number )

    for l in range ( 0, number ):
      ioff = list[l,0]
      joff = list[l,1]
      s2 = np.zeros ( [ mr, nr ], dtype = np.int32 )
      s2[0+ioff:ms+ioff,0+joff:ns+joff] = s[0:ms,0:ns]
      e_dot_s2 = e * abs ( s2 )
      eqn = e_dot_s2[e_dot_s2 != 0 ] - 1
      a[eqn,var] = 1
      var = var + 1
#
#  The next equations specify how many P's of a given type may be used.
#
  eqn = pariomino_area ( r )

  var = 0
  for k in range ( 0, p_num ):
    pk_vars = sum ( var_p == k )
    a[eqn,var:var+pk_vars] = 1
    b[eqn] = d[k]
    eqn = eqn + 1
    var = var + pk_vars  
#
#  A final equation says the area of the P's that are used must 
#  equal the area of R.
#
  var = 0
  for k in range ( 0, p_num ):
    pk_vars = sum ( var_p == k )
    pk_area = pariomino_area ( p[0:mr,0:nr,k] )
    a[eqn,var:var+pk_vars] = pk_area
#   a[eqn,var+1:var+pk_vars] = pk_area
    var = var + pk_vars
  b[eqn] = pariomino_area ( r )
  eqn = eqn + 1
 
  return a, b, var_p

def pariomino_matrix_test ( ):

#*****************************************************************************80
#
## pariomino_matrix_test() tests pariomino_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_matrix_test:' )
  print ( '  pariomino_matrix() sets up the linear system' )
  print ( '  associated with a pariomino tiling problem.' )
#
#  Define R.
#
  shape_r = np.array ( [ \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )
  m_r, n_r = shape_r.shape
  pariomino_print ( shape_r, '  Region R:' )
#
#  Define N, O, P
#
  shape_n = np.array ( [ \
    [ -1 ] ] )
  m_n, n_n = shape_n.shape
  pariomino_print ( shape_n, '  pariomino N:' )

  shape_o = np.array ( [ \
    [ +1, -1, +1 ] ] )
  m_o, n_o = shape_o.shape
  pariomino_print ( shape_o, '  pariomino O:' )

  shape_p = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_p, n_p = shape_p.shape
  pariomino_print ( shape_p, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p = np.zeros ( [ m_r, n_r, p_num ] )
  p[0:m_n,0:n_n,0] = shape_n[0:m_n,0:n_n]
  p[0:m_o,0:n_o,1] = shape_o[0:m_o,0:n_o]
  p[0:m_p,0:n_p,2] = shape_p[0:m_p,0:n_p]
#
#  D indicates how many copies of each pariomino we can use.
#
  d = np.ones ( p_num )
#
#  Compute the system matrix.
#
  a, b, parent = pariomino_matrix ( shape_r, p_num, p, d )
  m, n = a.shape
#
#  Print the linear system.
#
  print ( '' )
  print ( '  System matrix A and right hand side B:' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  %2d:  ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( a[i,j] ), end = '' )
    print ( '  %2d' % ( b[i] ) )
#
#  Write the linear system to an LP file.
#
  filename = '2x4.lp'
  label = '\ LP file for the 2x4 example, created by pariomino_lp_write.'
  pariomino_lp_write ( filename, label, m, n, a, b )

  print ( '' )
  print ( '  Linear system saved in LP file:"%s"' % ( filename ) )

  return

def pariomino_matrix_reid ( ):

#*****************************************************************************80
#
## pariomino_matrix_reid() sets the matrix for the Reid problem.
#
#  Discussion:
#
#    This function sets up the linear system A*x=b associated with
#    the Reid pariomino tiling problem.
#
#    While it is desirable to have a general procedure that can automatically
#    deduce the linear system from the problem specification, for simplicity
#    in this example, we simply provide the linear system directly.
#
#    I have modified this file so that the numbering of equations and
#    variables agrees with the paper.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(9,10), the system matrix.
#
#    real B(9), the right hand side.
#
  import numpy as np
#
#  Each of 8 cells must be covered by one of 10 tile positions.
#
  a1 = np.array ( [ \
    [ 1,0,0,0,0,1,0,0,0,0 ], \
    [ 0,0,1,0,0,1,0,0,0,0 ], \
    [ 1,1,0,0,0,0,1,0,0,0 ], \
    [ 0,0,1,1,0,0,1,1,0,0 ], \
    [ 0,0,0,0,1,0,0,1,0,0 ], \
    [ 0,1,0,0,0,0,0,0,1,0 ], \
    [ 0,0,0,1,0,0,0,0,1,1 ], \
    [ 0,0,0,0,1,0,0,0,0,1 ] ] )

  b1 = np.ones ( 8 )
#
#  Each tile covers two cells.  The total number of cells covered must be 8.
#
  a2 = np.array ( [ \
    [ 2,2,2,2,2,2,2,2,2,2 ] ] )
  b2 = np.array ( [ 8 ] )
#
#  Combined system.
#
  a = np.concatenate ( ( a1, a2 ) )
  b = np.concatenate ( ( b1, b2 ) )

  return a, b

def pariomino_matrix_reid_test ( ):

#*****************************************************************************80
#
## pariomino_matrix_reid_test() tests pariomino_matrix_reid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pariomino_matrix_reid_test:' )
  print ( '  pariomino_matrix_reid() sets up the linear system' )
  print ( '  associated with the Reid pariomino tiling problem.' )

  a, b = pariomino_matrix_reid ( )
  m, n = a.shape
#
#  Print the linear system.
#
  print ( '' )
  print ( '  System matrix A and right hand side B:' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( a[i,j] ), end = '' )
    print ( '  %2d' % ( b[i] ) )

  return

def pariomino_parity ( p ):

#*****************************************************************************80
#
## pariomino_parity() returns the parity of a pariomino.
#
#  Discussion:
#
#    A pariomino is a shape formed by connecting unit squares edgewise.
#
#    A pariomino can be represented by an MxN matrix, whose entries are
#    +1 or -1 for squares that are part of the pariomino, and 0 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(MP,NP), a matrix of -1's, 0's and +1's representing 
#    the pariomino.  
#
#  Output:
#
#    integer PARITY, the parity of the pariomino.
#
  parity = sum ( sum ( p ) )

  return parity

def pariomino_parity_test ( ):

#*****************************************************************************80
#
## pariomino_parity_test() tests pariomino_parity().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_parity_test' )
  print ( '  pariomino_parity() returns the parity of a pariomino.' )

  p = np.array ( [ \
    [ 1, -1, 1, -1 ] ] )
  pariomino_print ( p, '  pariomino #1:' )
  parity = pariomino_parity ( p )
  print ( '  parity is', parity )

  p = np.array ( [ \
    [ -1,  1,  0 ], \
    [  0, -1,  0 ], \
    [  0,  1, -1 ] ] )
  pariomino_print ( p, '  pariomino #2:' )
  parity = pariomino_parity ( p )
  print ( '  parity is', parity )

  p = np.array ( [ \
    [  1,  0,  0 ], \
    [ -1,  1, -1 ] ] )
  pariomino_print ( p, '  pariomino #3:' )
  parity = pariomino_parity ( p )
  print ( '  parity is', parity )

  p = np.array ( [ \
    [  0,  0,  0,  0, -1,  0 ], \
    [ +1,  0,  0,  0, +1, -1 ], \
    [ -1,  0, -1, +1, -1,  0 ], \
    [ +1,  0, +1,  0, +1,  0 ], \
    [ -1, +1, -1, +1, -1,  0 ] ] )
  pariomino_print ( p, '  pariomino #4:' )
  parity = pariomino_parity ( p )
  print ( '  parity is', parity )

  return

def pariomino_print ( p, label ):

#*****************************************************************************80
#
## pariomino_print() prints a pariomino.
#
#  Discussion:
#
#    A pariomino is represented as a subset of an MxN grid.
#    The matrix entry Pij is 0 if square(i,j) is not part of the pariomino.
#    Otherwise, it is -1 (black) or +1 (white).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(M,N), a matrix representing the pariomino.  
#
#    string LABEL, a label to be printed.  
#
  print ( '' )
  print ( label )
  print ( '' )

  m, n = p.shape

  if ( m <= 0 or n <= 0 ):
    print ( '  [ Null matrix ]' )
  else:
    for i in range ( 0, m ):
      print ( '  ', end = '', sep = '' )
      for j in range ( 0, n ):
        if ( p[i,j] == 0 ):
          print ( '.', end = '', sep = '' )
        elif ( p[i,j] == -1 ):
          print ( 'B', end = '', sep = '' )
        else:
          print ( 'W', end = '', sep = '' )
      print ( '' )

  return

def pariomino_print_test ( ):

#*****************************************************************************80
#
## pariomino_print_test() tests pariomino_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_print_test' )
  print ( '  pariomino_print() prints a pariomino.' )
#
#  Define several pariominos.
#
  p = np.array ( [ \
    [ 1, -1, 1, -1 ] ] )
  pariomino_print ( p, '  pariomino #1:' )

  p = np.array ( [ \
    [ -1,  1,  0 ], \
    [  0, -1,  0 ], \
    [  0,  1, -1 ] ] )
  pariomino_print ( p, '  pariomino #2:' )

  p = np.array ( [ \
    [  1,  0,  0 ], \
    [ -1,  1, -1 ] ] )
  pariomino_print ( p, '  pariomino #3:' )

  p = np.array ( [ \
    [  0,  0,  0,  0, -1,  0 ], \
    [ +1,  0,  0,  0, +1, -1 ], \
    [ -1,  0, -1, +1, -1,  0 ], \
    [ +1,  0, +1,  0, +1,  0 ], \
    [ -1, +1, -1, +1, -1,  0 ] ] )
  pariomino_print ( p, '  pariomino #4:' )

  return

def pariomino_reverse ( p1 ):

#*****************************************************************************80
#
## pariomino_reverse() reverses the parity of each cell of a pariomino.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P1(M,N), the representation of pariomino P1. 
#
#  Output:
#
#    integer P2(M,N), the representation of pariomino P2. 
#
  p2 = - p1

  return p2

def pariomino_reverse_test ( ):

#*****************************************************************************80
#
## pariomino_reverse_test() tests pariomino_reverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_reverse_test' )
  print ( '  pariomino_reverse() reverses the parity of the cells' )
  print ( '  of a pariomino.')

  p1 = np.array ( [ \
    [  0,  0,  0,  0, -1,  0 ], \
    [ +1,  0,  0,  0, +1, -1 ], \
    [ -1,  0, -1, +1, -1,  0 ], \
    [ +1,  0, +1,  0, +1,  0 ], \
    [ -1, +1, -1, +1, -1,  0 ] ] )
  pariomino_print ( p1, '  pariomino:' )

  p2 = pariomino_reverse ( p1 )
  pariomino_print ( p2, '  reverse parity pariomino:' )

  return

def pariomino_tiling_plot ( r_shape, p_num, p_shapes, d, x, filename, label ):

#*****************************************************************************80
#
## pariomino_tiling_plot() plots pariomino tilings.
#
#  Discussion:
#
#    You need a tiling problem definition (R_SHAPE, P_NUM, P_SHAPES, D) and
#    one or more solution vectors in the array X, in order for this function
#    to create a plot of the proposed tiling.
#
#    This function cannot detect bogus tilings.  If your vector X describes
#    a tiling that actually does not cover some cells of R, those cells will
#    appear white, as though they were not part of the region.  If X indicates
#    more than one pariomino covering a cell, then that cell will be assigned
#    a color that is the sum of the indices of all the colors of pariominoes
#    covering the cell, which will result in a bogus and somewhat chaotic plot.
#
#
#    The interpretation of X, that is, the association of an index into X with
#    a particular pariomino that has been reflected, rotated, and translated,
#    depends entirely on the scheme used by pariomino_variants().
#
#
#    The value of the internally set variable COLOR_CHOICE determines whether
#    1: all pariominoes have the same color
#    2: all visible pariominoes have unique colors
#    3: all pariominoes have unique colors.
#    4: each pariomino "parent" has a unique color, shared by all variants.
#
#
#    The color map is internally set to jet.  Other choices for MATLAB's
#    build-in color maps include parula, hsv, hot, cool, spring, summer,
#    winter, and gray.  
#
#    To use a different color map, find the following line:
#      colormap ( jet ( color_num ) )
#    and change "jet" to your desired color map.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Inpu:
#
#    integer R_SHAPE(R_M,R_N), a matrix of -1's, 0's and 1's representing the 
#    region.
#
#    integer P_NUM, the number of pariomino shapes to be used.
#
#    integer P_SHAPES(R_M,R_N,P_NUM), a ternary matrix describing the 
#    pariominoes.  The matrix is "top-left tight", that is, the I-th pariomino 
#    is stored in P_SHAPES(1:R_M,1:R_N,I) with a nonzero in the first row, 
#    a nonzero in the first column, but with trailing rows and columns 
#    of zeros allowed.
#
#    integer D(P_NUM), tells us how many copies of each pariomino
#    we must use in the tiling.
#
#    integer X(X_M,X_N), a binary vector describing one or more
#    solutions of the tiling problem.  Every possible placement of every variant 
#    of a pariomino in P has been assigned an index.  If X(I,J) is 1, then 
#    the I-th placement is included in solution J.
#
#    string FILENAME, a filename to be used for storing plots.
#
#    string LABEL, a label for the printout, such as 
#    'Solution of the 2x4 Example'.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
#
#  Color_choice:
#  white for space, and:
#  1: 2 colors, a single color for all pariominoes.
#  2: NZ+1 colors, separate color for each visible pariomino.
#  3: VAR_NUM+1, separate color for every pariomino, visible or not.
#  4: P_NUM+1, separate color for each pariomino "parent", and variants.
#
  color_choice = 4
#
#  Get the linear system satisfied by A*x=b.
#
  a, b, parent = pariomino_matrix ( r_shape, p_num, p_shapes, d )
#
#  Get the size of the linear system.
#
  a_m, a_n = a.shape
#
#  Get the size of R.
#
  r_m, r_n = r_shape.shape
#
#  Get tne number of nonzero cells in R.
#
  r_num = pariomino_area ( r_shape )
#
#  Index the nonzero cells in R.
#
  r_index = pariomino_index ( r_shape )
#
#  Get the size of X.
#
  x_m = x.shape[0]
  x_n = x.shape[1]
#
#  Replace each nonzero X(I,*) by an increasing index.
#
  for k in range ( 0, x_n ):

    xc = np.zeros ( x_m )
    xi = np.zeros ( x_m )

    nz = 0
    var = 0
    par = 0

    for i in range ( 0, x_m ):

      if ( x[i,k] == 0 ):
        color = 0
      else:
        nz = nz + 1

        if ( color_choice == 1 ):
          color = 1
        elif ( color_choice == 2 ):
          color = nz
        elif ( color_choice == 3 ):
          color = i
        elif ( color_choice == 4 ):
          color = parent[i]

        xc[i] = color
        xi[i] = nz
#
#  The first R_NUM rows of A are equations about covering each cell of R.
#
#  Multiplying this matrix times XC gives us:
#
    axc = np.matmul ( a[0:r_num,0:a_n], xc )
    axi = np.matmul ( a[0:r_num,0:a_n], xi )
#
#  R_SHAPE is ternary (-1, 0 or 1).
#  R_TILING replaces each nonzero by the index of the pariomino variant which
#  covers it.
#
    r_color = np.zeros ( [ r_m, r_n ] )
    for i in range ( 0, r_m ):
      for j in range ( 0, r_n ):
        if ( r_index[i,j] == 0 ):
          r_color[i,j] = 0
        else:
          r_color[i,j] = axc[r_index[i,j]-1] + 1

    r_label = np.zeros ( [ r_m, r_n ] )
    for i in range ( 0, r_m ):
      for j in range ( 0, r_n ):
        if ( r_index[i,j] == 0 ):
          r_label[i,j] = 0
        else:
          r_label[i,j] = axi[r_index[i,j]-1]
#
#  Begin new figure.
#
    plt.clf ( )
#
#  Flip each column.
#
    r_color = np.flipud ( r_color )
    r_label = np.flipud ( r_label )
#
#  Display the solution as a matrix.
#
    plt.imshow ( r_color, cmap = 'rainbow' )
#
#  Draw tile boundaries.
#
    lw = 0.04

    for i in range ( 0, r_m ):
      for j in range ( 0, r_n ):

        if ( r_label[i,j] != 0 ): 
#
#  Horizontal separator above.
#
          if ( i == 0 ):
            xl = [ j - 0.5 - lw, j + 0.5 + lw, j + 0.5 + lw, j - 0.5 - lw ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i - 0.5 + lw, i - 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i-1,j] == 0 ):
            xl = [ j - 0.5,      j + 0.5,      j + 0.5,      j - 0.5      ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i - 0.5 + lw, i - 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i-1,j] != r_label[i,j] ):
            xl = [ j - 0.5, j + 0.5, j + 0.5,      j - 0.5      ]
            yl = [ i - 0.5, i - 0.5, i - 0.5 + lw, i - 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
#
#  Horizontal separator below.
#
          if ( i == r_m - 1 ):
            xl = [ j - 0.5,      j + 0.5,      j + 0.5,      j - 0.5      ]
            yl = [ i + 0.5 + lw, i + 0.5 + lw, i + 0.5 - lw, i + 0.5 - lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i+1,j] == 0 ):
            xl = [ j - 0.5,      j + 0.5,      j + 0.5,      j - 0.5      ]
            yl = [ i + 0.5 + lw, i + 0.5 + lw, i + 0.5 - lw, i + 0.5 - lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i+1,j] != r_label[i,j] ):
            xl = [j - 0.5, j + 0.5, j + 0.5,      j - 0.5      ]
            yl = [ i + 0.5, i + 0.5, i + 0.5 - lw, i + 0.5 - lw ]
            plt.fill ( xl, yl, 'k' )
#
#  Vertical separator to left.
#
          if ( j == 0 ):
            xl = [ j - 0.5 - lw, j - 0.5 + lw, j - 0.5 + lw, j - 0.5 - lw ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i,j-1] == 0 ):
            xl = [ j - 0.5 - lw, j - 0.5 + lw, j - 0.5 + lw, j - 0.5 - lw ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i,j-1] != r_label[i,j] ):
            xl = [ j - 0.5,      j - 0.5 + lw, j - 0.5 + lw, j - 0.5      ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
#
#  Vertical separator to right.
#
          if ( j == r_n - 1 ):
            xl = [ j + 0.5 - lw, j + 0.5 + lw, j + 0.5 + lw, j + 0.5 - lw ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i,j+1] == 0 ):
            xl = [ j + 0.5 - lw, j + 0.5 + lw, j + 0.5 + lw, j + 0.5 - lw ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
          elif ( r_label[i,j+1] != r_label[i,j] ):
            xl = [ j + 0.5 - lw, j + 0.5,      j + 0.5,      j + 0.5 - lw ]
            yl = [ i - 0.5 - lw, i - 0.5 - lw, i + 0.5 + lw, i + 0.5 + lw ]
            plt.fill ( xl, yl, 'k' )
#
#  Title the plot.
#
    plt.title ( filename )
#
#  Use the same scale for X and Y directions.
#
    plt.axis ( 'equal' )
#
#  Don't display the graph axes.
#
    plt.axis ( False )
#
#  Save a version of the plot.
#
    plt.savefig ( filename )
    print ( '  Graphics saved as', filename )

    filename = filename_inc ( filename )

    plt.close ( )

  return

def pariomino_tiling_plot_test01 ( ):

#*****************************************************************************80
#
## pariomino_tiling_plot_test01() sets up test example 1.
#
#  Discussion:
#
#    The region R consists of the following arrangement of square cells:
#
#      1 1 1 1
#      1 1 1 1
#
#    This region is to be tiled by 1 copy each of 3 pariominoes.
#
#    The shapes of the 3 pariominoes are
#
#      N = 1 
# 
#      O = 1 1 1
#
#      P = 0 0 1
#          1 1 1
#
#    For this problem, there are four solutions:
#
#      O O O P = x5 + x9 + x14
#      N P P P
#
#      P P P N = x4 + x12 + x15
#      P O O O
#
#      P O O O = x8 + x10 + x17
#      P P P N
#
#      N P P P = x1 + x11 + x20
#      O O O P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_tiling_plot_test01' )
  print ( '  Given solutions for the 2x4 pariomino' )
  print ( '  tiling problem, plot corresponding tilings.' )
#
#  Define R.
#
  r_shape = np.array ( [ \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )
  m_r, n_r = r_shape.shape
  pariomino_print ( r_shape, '  Region R:' )
#
#  Define N, O, P
#
  n_shape = np.array ( [ \
    [ -1 ] ] )
  m_n, n_n = n_shape.shape
  pariomino_print ( n_shape, '  pariomino N:' )

  o_shape = np.array ( [ \
    [ +1, -1, +1 ] ] )
  m_o, n_o = o_shape.shape
  pariomino_print ( o_shape, '  pariomino O:' )

  p_shape = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_p, n_p = p_shape.shape
  pariomino_print ( p_shape, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p_shapes = np.zeros ( [ m_r, n_r, p_num ] )
  p_shapes[0:m_n,0:n_n,0] = n_shape[0:m_n,0:n_n]
  p_shapes[0:m_o,0:n_o,1] = o_shape[0:m_o,0:n_o]
  p_shapes[0:m_p,0:n_p,2] = p_shape[0:m_p,0:n_p]
#
#  D indicates how many times each pariomino is to be used.
#
  d = np.ones ( p_num )
#
#  Define the solutions X, obtained by pariomino_tiling_solver.
#
  x = np.array ( [ \
   [ 0, 0 ], \
   [ 0, 1 ], \
   [ 1, 0 ], \
   [ 0, 0 ], \
   [ 1, 0 ], \
   [ 0, 1 ], \
   [ 1, 0 ], \
   [ 0, 1 ], \
   [ 0, 0 ], \
   [ 0, 0 ] ] )
#
#  Plot the tilings corrresponding to each solution.
#
  filename = 'twobyfour01.png'
  label = '2x4 Pariomino Tiling'
  pariomino_tiling_plot ( r_shape, p_num, p_shapes, d, x, filename, label )

  return

def pariomino_tiling_plot_test02 ( ):

#*****************************************************************************80
#
## pariomino_tiling_plot_test02() sets up test example 2.
#
#  Discussion:
#
#    The region R consists of the following arrangement of square cells:
#
#      +1  0  0  0
#      -1  0  0  0
#      +1 -1 +1 -1
#      -1 +1 -1 +1
#
#    This region is to be tiled by 1 copy each of 3 pariominoes.
#
#    The shapes of the 3 pariominoes are
#
#      N =  0  0 -1
#          +1 -1 +1
# 
#      O = -1 +1 -1
#
#      P =  0 +1
#          +1 -1
#
#    For this problem, there is one solution:
#
#      N 0 0 0
#      N 0 0 0
#      N N P P
#      O O O P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pariomino_tiling_plot_test02' )
  print ( '  Given 4 solutions for the 2x4 pariomino' )
  print ( '  tiling problem, plot corresponding tilings.' )
#
#  Define R.
#
  r_shape = np.array ( [ \
    [ +1,  0,  0,  0 ], \
    [ -1,  0,  0,  0 ], \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )
  m_r, n_r = r_shape.shape
  pariomino_print ( r_shape, '  Region R:' )
#
#  Define N, O, P
#
  n_shape = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_n, n_n = n_shape.shape
  pariomino_print ( n_shape, '  pariomino N:' )

  o_shape = np.array ( [ \
    [ -1, +1, -1 ] ] )
  m_o, n_o = o_shape.shape
  pariomino_print ( o_shape, '  pariomino O:' )

  p_shape = np.array ( [ \
    [  0, +1 ], \
    [ +1, -1 ] ] )
  m_p, n_p = p_shape.shape
  pariomino_print ( p_shape, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p_shapes = np.zeros ( [ m_r, n_r, p_num ] )
  p_shapes[0:m_n,0:n_n,0] = n_shape[0:m_n,0:n_n]
  p_shapes[0:m_o,0:n_o,1] = o_shape[0:m_o,0:n_o]
  p_shapes[0:m_p,0:n_p,2] = p_shape[0:m_p,0:n_p]
#
#  D indicates how many times each pariomino is to be used.
#
  d = np.ones ( p_num )
#
#  Define the 1 solution X, obtained by pariomino_tiling_solver.
#
  x = np.array ( [ \
   [ 0 ], \
   [ 0 ], \
   [ 1 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ], \
   [ 1 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ], \
   [ 1 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ] ] )
#
#  Plot the tiling corresponding to the solution.
#
  filename = 'fourbyfour01.png'
  label = '4x4 Pariomino Tiling'
  pariomino_tiling_plot ( r_shape, p_num, p_shapes, d, x, filename, label )

  return

def pariomino_tiling_print ( r_shape, p_num, p_shapes, d, x, label ):

#*****************************************************************************80
#
## pariomino_tiling_print() prints a pariomino tiling.
#
#  Discussion:
#
#    You can change the internal parameter "COLOR_CHOICE" to specify how to 
#    set the numbers that identify each pariomino component of the tiling.
#
#    You can change the internal parameter "SHOW_ZERO" to specify whether zero 
#    cells should be shown, or blanked out.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer R_SHAPE(R_M,R_N), a matrix of -1's, 0's, and 1's representing 
#    the region.
#
#    integer P_NUM, the number of pariomino shapes to be used.
#
#    integer P_SHAPES(M_R,N_R,P_NUM), a binary matrix describing the 
#    pariominoes.  The matrix is "top-left tight", that is, the I-th pariomino 
#    is stored in P_SHAPES(1:M_R,1:N_R,I) with a 1 in the first row, a 1 in the 
#    first column, but with trailing rows and columns of zeros allowed.
#
#    integer D(P_NUM), tells us how many copies of each pariomino
#    we must use in the tiling.
#
#    integer X(X_M), a solution to the problem, consisting 
#    of a binary value (0 or 1) for every possible placement of a pariomino 
#    variant onto R.
#
#    string LABEL, a label for the printout, such as 
#    'Solution #3 of the 2x4 Example'.
#
#  Output:
#
#    integer R_LABEL(R_M,R_N), an array of indices that suggest
#    the structure of the tiling.  Regions of R that are not used will either
#    be blank, or marked with zero.  Regions of R corresponding to a given
#    pariomino will be marked by a numeric label whose value depends on the
#    value of the internal parameter "color_choice".
#
#    integer R_COLOR(R_M,R_N), an array of indices that indicate
#    the colors applied to the tiling.  Regions of R that are not used will 
#    either be blank, or marked with zero.  The color range depends on the
#    value of the internal parameter "color_choice".
#
  import numpy as np
#
#  COLOR_CHOICE:
#
#  white for space, and:
#  1: 2 colors, a single color for all pariominoes.
#  2: NZ+1 colors, separate color for each visible pariomino.
#  3: VAR_NUM+1, separate color for every pariomino, visible or not.
#  4: P_NUM+1, separate color for each pariomino "parent", and variants.
#
  color_choice = 4
#
#  SHOW_ZERO
#  0: do not show zero regions.
#  1: show zero regions.
#
  show_zero = 1
#
#  Get the linear system satisfied by A*x=b.
#
  a, b, parent = pariomino_matrix ( r_shape, p_num, p_shapes, d )
#
#  Get the size of the linear system.
#
  a_m, a_n = a.shape
#
#  Get the size of R.
#
  r_m, r_n = r_shape.shape
#
#  Get the number of cells in R.
#
  r_num = pariomino_area ( r_shape )
#
#  Index the nonzero cells in R.
#
  r_index = pariomino_index ( r_shape )
#
#  Get the size of X.
#  Code modified so it can only handle 1 solution at a time.
#
  x_m = x.shape[0]

  x_index = 0
#
#  Replace each nonzero X(I,*) by an increasing index.
#
  xc = np.zeros ( x_m )
  xi = np.zeros ( x_m )

  nz = 0
  var = 0
  par = 0

  for i in range ( 0, x_m ):

    if ( x[i] == 0 ):
      color = 0
    else:
      nz = nz + 1

      if ( color_choice == 1 ):
       color = 1
      elif ( color_choice == 2 ):
        color = nz
      elif ( color_choice == 3 ):
        color = i
      elif ( color_choice == 4 ):
        color = parent[i]

      xc[i] = color
      xi[i] = nz
#
#  The first R_NUM rows of A are equations about covering each cell of R.
#
#  Multiplying this matrix times XC gives us:
#
  axc = np.matmul ( a[0:r_num,0:a_n], xc )
  axi = np.matmul ( a[0:r_num,0:a_n], xi )
#
#  R_SHAPE is binary (0 or 1).
#  R_LABEL replaces each 1 by the index of the pariomino variant which covers it.
#
  r_color = np.zeros ( [ r_m, r_n ] )

  for i in range ( 0, r_m ):
    for j in range ( 0, r_n ):
      if ( r_index[i,j] == 0 ):
        r_color[i,j] = 0
      else:
        r_color[i,j] = axc[r_index[i,j]-1] + 1

  r_label = np.zeros ( [ r_m, r_n ] )
  for i in range ( 0, r_m ):
    for j in range ( 0, r_n ):
      if ( r_index[i,j] == 0 ):
        r_label[i,j] = 0
      else:
        r_label[i,j] = axi[r_index[i,j]-1]
#
#  Print R_LABEL.
#
  print ( '' )
  print ( label )
  print ( '  Numeric Labels' )
  print ( '' )

  smax = np.amax ( r_label )
  
  for i in range ( 0, r_m ):
    print ( ' ', end = '' )
    for j in range ( 0, r_n ):
      if ( 10 <= smax and smax < 100 ):
        if ( r_label[i,j] == 0 and show_zero == 0 ):
          print ( '   ', end = '' )
        else:
          print ( ' %2d' % ( r_label[i,j] ), end = '' )
      else:
        if ( r_label[i,j] == 0 and show_zero == 0 ):
          print ( '  ', end = '' )
        else:
          print ( ' %d' % ( r_label[i,j] ), end = '' )
    print ( '' )
#
#  Print R_COLOR
#
  print ( '' )
  print ( label )
  print ( '  "Colors"' )
  print ( '' )

  smax = np.amax ( r_label )
  
  for i in range ( 0, r_m ):
    print ( ' ', end = '' )
    for j in range ( 0, r_n ):
      if ( 10 <= smax and smax < 100 ):
        if ( r_label[i,j] == 0 and show_zero == 0 ):
          print ( '   ', end = '' )
        else:
          print ( ' %2d' % ( r_color[i,j] ), end = '' )
      else:
        if ( r_label[i,j] == 0 and show_zero == 0 ):
          print ( '  ', end = '' )
        else:
          print ( ' %d' % ( r_color[i,j] ), end = '' )
    print ( '' )

  return r_label, r_color

def pariomino_tiling_print_test01 ( ):

#*****************************************************************************80
#
## pariomino_tiling_print_test01() sets up test example 1.
#
#  Discussion:
#
#    The region R consists of the following arrangement of square cells:
#
#      1 1 1 1
#      1 1 1 1
#
#    This region is to be tiled by 1 copy each of 3 pariominoes.
#
#    The shapes of the 3 pariominoes are
#
#      N = 1 
# 
#      O = 1 1 1
#
#      P = 0 0 1
#          1 1 1
#
#    For this problem, there are four solutions:
#
#      O O O P = x5 + x9 + x14
#      N P P P
#
#      P P P N = x4 + x12 + x15
#      P O O O
#
#      P O O O = x8 + x10 + x17
#      P P P N
#
#      N P P P = x1 + x11 + x20
#      O O O P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_tiling_print_test01' )
  print ( '  Given solutions for the 2x4 pariomino' )
  print ( '  tiling problem, print a representation of the tiling' )
  print ( '  corresponding to each solution.' )
#
#  Define R.
#
  r_shape = np.array ( [ \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )

  m_r, n_r = r_shape.shape
  pariomino_print ( r_shape, '  Region R:' )
#
#  Define N, O, P
#
  n_shape = np.array ( [ \
    [ -1 ] ] )
  m_n, n_n = n_shape.shape
  pariomino_print ( n_shape, '  pariomino N:' )

  o_shape = np.array ( [ \
    [ +1, -1, +1 ] ] )
  m_o, n_o = o_shape.shape
  pariomino_print ( o_shape, '  pariomino O:' )

  p_shape = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_p, n_p = p_shape.shape
  pariomino_print ( p_shape, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p_shapes = np.zeros ( [ m_r, n_r, p_num ] )
  p_shapes[0:m_n,0:n_n,0] = n_shape[0:m_n,0:n_n]
  p_shapes[0:m_o,0:n_o,1] = o_shape[0:m_o,0:n_o]
  p_shapes[0:m_p,0:n_p,2] = p_shape[0:m_p,0:n_p]
#
#  D indicates how many times each pariomino is to be used.
#
  d = np.ones ( p_num )
#
#  Define the solutions X, obtained by pariomino_tiling_solver.
#
  x = np.array ( [ \
   [ 0, 0 ], \
   [ 0, 1 ], \
   [ 1, 0 ], \
   [ 0, 0 ], \
   [ 1, 0 ], \
   [ 0, 1 ], \
   [ 1, 0 ], \
   [ 0, 1 ], \
   [ 0, 0 ], \
   [ 0, 0 ] ] )
 
  m_x, n_x = x.shape
#
#  Print the tilings.
#
  for j in range ( 0, n_x ):
    label = ( '  2x4 Tiling #%d' % ( j  ) )
    pariomino_tiling_print ( r_shape, p_num, p_shapes, d, x[:,j], label )

  return

def pariomino_tiling_print_test02 ( ):

#*****************************************************************************80
#
## pariomino_tiling_print_test02() sets up test example 2.
#
#  Discussion:
#
#    The region R consists of the following arrangement of square cells:
#
#      +1  0  0  0
#      -1  0  0  0
#      +1 -1 +1 -1
#      -1 +1 -1 +1
#
#    This region is to be tiled by 1 copy each of 3 pariominoes.
#
#    The shapes of the 3 pariominoes are
#
#      N =  0  0 -1
#          +1 -1 +1
# 
#      O = -1 +1 -1
#
#      P =  0 +1
#          +1 -1
#
#    For this problem, there is one solution:
#
#      N 0 0 0
#      N 0 0 0
#      N N P P
#      O O O P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_tiling_print_test02' )
  print ( '  Given 4 solutions for the 2x4 pariomino' )
  print ( '  tiling problem, print corresponding tilings.' )
#
#  Define R.
#
  r_shape = np.array ( [ \
    [ +1,  0,  0,  0 ], \
    [ -1,  0,  0,  0 ], \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )
  m_r, n_r = r_shape.shape
  pariomino_print ( r_shape, '  Region R:' )
#
#  Define N, O, P
#
  n_shape = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_n, n_n = n_shape.shape
  pariomino_print ( n_shape, '  pariomino N:' )

  o_shape = np.array ( [ \
    [ -1, +1, -1 ] ] )
  m_o, n_o = o_shape.shape
  pariomino_print ( o_shape, '  pariomino O:' )

  p_shape = np.array ( [ \
    [  0, +1 ], \
    [ +1, -1 ] ] )
  m_p, n_p = p_shape.shape
  pariomino_print ( p_shape, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p_shapes = np.zeros ( [ m_r, n_r, p_num ] )
  p_shapes[0:m_n,0:n_n,0] = n_shape[0:m_n,0:n_n]
  p_shapes[0:m_o,0:n_o,1] = o_shape[0:m_o,0:n_o]
  p_shapes[0:m_p,0:n_p,2] = p_shape[0:m_p,0:n_p]
#
#  D indicates how many times each pariomino is to be used.
#
  d = np.ones ( p_num )
#
#  Define the 1 solution X, obtained by pariomino_tiling_solver.
#
  x = np.array ( [ \
   [ 0 ], \
   [ 0 ], \
   [ 1 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ], \
   [ 1 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ], \
   [ 1 ], \
   [ 0 ], \
   [ 0 ], \
   [ 0 ] ] )
#
#  Print the tiling.
#
  label = '  4x4 Pariomino Tiling'
  pariomino_tiling_print ( r_shape, p_num, p_shapes, d, x, label )

  return

def pariomino_tiling_solver ( r_shape, p_num, p_shapes, d, filename, comment ):

#*****************************************************************************80
#
## pariomino_tiling_solver() analyzes tiling a region with pariominoes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer R_SHAPE(M_R,N_R), the binary matrix describing the region.
#
#    integer P_NUM, the number of pariomino shapes to be used.
#
#    integer P_SHAPES(M_R,N_R,P_NUM), a binary matrix describing the 
#    pariominoes.  The matrix is "top-left tight", that is, the I-th pariomino 
#    is stored in P_SHAPES(1:M_R,1:N_R,I) with a nonzero in the first row, 
#    and in the first column, but with trailing rows and columns 
#    of zeros allowed.
#
#    integer D(P_NUM), tells us how many copies of each pariomino
#    we must use in the tiling.
#
#    string FILENAME, a name for the LP file that will contain the
#    definition of the problem.
#
#    string COMMENT, a comment that will be the first line of the LP file.
#
#  Output:
#
#    integer M, N, X_NUM, the number of equations, the number of 
#    variables, and the number of binary solutions found.
#
#    integer A(M,N), the matrix of equation coefficients, which should
#    all be 0 or 1.
#
#    integer B(M), the right hand sides, which should all be 1.
#
#    integer X(N,X_NUM), a set of X_NUM solutions to the problem, each
#    consisting of a binary value (0 or 1) for every possible placement
#    of a pariomino onto R.
#
  import numpy as np

  verbose = False

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  The internal variable "verbose" is set to "true"' )
    print ( '  Print statements marked "VERBOSE" can be suppressed' )
    print ( '  by setting "verbose" to "false".' )

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( 'pariomino_tiling_solver:' )
    print ( '  Analyze the problem of tiling a region R using copies,' )
    print ( '  possibly rotated or reflected, of several pariominoes.' )
#
#  A: Check the binary matrix describing the region.
#  Make sure it is binary.
#  Make sure it is "tight".
#
  m_r, n_r = r_shape.shape

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Input R_SHAPE has shape (%d,%d).' % ( m_r, n_r ) )

  if ( not i4mat_is_ternary ( m_r, n_r, r_shape ) ):
    print ( '' )
    print ( 'pariomino_tiling_solver - Fatal error!' )
    print ( '  The matrix R_SHAPE has entries that are not -1, 0, or +1.' )
    raise Exception ( 'pariomino_tiling_solver - Fatal error!' )

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Input R_SHAPE is a ternary matrix.' )

  r_shape = pariomino_condense ( r_shape )

  m_r, n_r = r_shape.shape

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Condensed R_SHAPE has shape (%d,%d).' % ( m_r, n_r ) )
#
#  B: Check the ternary matrices describing the pariominoes.
#  Make sure they are ternary.
#  Make sure they are top-left "tight".
#
  for k in range ( 0, p_num ):

    p = p_shapes[:,:,k]

    m_p, n_p = p.shape

    if ( verbose ):
      print ( '' )
      print ( 'VERBOSE:' )
      print ( '  Input P(%d) has shape (%d,%d).' % ( k, m_p, n_p ) )

    if ( not i4mat_is_ternary ( m_p, n_p, p ) ):
      print ( '' )
      print ( 'pariomino_tiling_solver - Fatal error!' )
      print ( '  The matrix P(%d) has entries that are not -1, 0 or 1.'% ( k ) )

    if ( verbose ):
      print ( '' )
      print ( 'VERBOSE:' )
      print ( '  Input P(%d) is a ternary matrix.' % ( k ) )

    p = pariomino_condense ( p )

    m_p, n_p = p.shape

    if ( verbose ):
      print ( '' )
      print ( 'VERBOSE:' )
      print ( '  Condensed P(%d) has shape (#d,#d).' % ( k, m_p, n_p ) )

    p_shapes[0:m_r,0:n_r,k] = 0
    p_shapes[0:m_p,0:n_p,k] = p[0:m_p,0:n_p]
#
#  C: Make simple checks.
#

#
#  D: Construct the (usually underdetermined) linear system A*x=b.
#
  a, b, parent = pariomino_matrix ( r_shape, p_num, p_shapes, d )
  m, n = a.shape
#
#  Print the linear system.
#
  print ( '' )
  print ( '  %dx%d system matrix A and right hand side B:'% ( m, n ) )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( a[i,j] ), end = '' )
    print ( '  %2d' % ( b[i] ) )
#
#  E: Write the linear system to an LP file.
#
  pariomino_lp_write ( filename, comment, m, n, a, b )
#
#  F: Solve the linear system.
#
  at = np.transpose ( a )
  abt = np.append ( at, [ b ], axis = 0 )
  ab = np.transpose ( abt )
  ab_real = ab.astype ( dtype = float )

  ab_rref, det = r8mat_rref ( m, n + 1, ab_real )

  a_rref = np.round ( ab_rref[0:m,0:n] )
  b_rref = np.round ( ab_rref[0:m,n] )

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  RREF has determinant = ', det )
    print ( '' )
    print ( '  %dx%d RREF matrix A and right hand side b:' % ( m, n ) )
    print ( '' )
    for i in range ( 0, m ):
      print ( '  ', end = '' )
      for j in range ( 0, n ):
        print ( '%2d' % ( a_rref[i,j] ), end = '' )
      print ( '  %2d' % ( b_rref[i] ) )
#
#  Augment the RREF system, and look for binary solutions.
#
  nz = np.sum ( d )
  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Seek binary solutions with exactly %d nonzeros' % ( nz ) )

  x_num, x = r8mat_rref_solve_binary_nz ( m, n, nz, a_rref, b_rref )
#
#  G: Print solution vectors.
#
  print ( '' )
  print ( '  %d binary solutions were found.' % ( x_num ) )

  if ( x_num == 0 ):
    return m, n, x_num, a, b, x

  print ( '' )
  print ( '  Binary solution vectors x:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  ',  end = '' )
    for j in range ( 0, x_num ):
      print ( '%2d' % ( x[i,j] ), end = '' )
    print ( '' )
#
#  H: Verify that solutions are correct.
#
  check = np.zeros ( x_num )

  print ( '' )
  print ( '  Check Loo residuals ||Ax-b||:' )
  print ( '' )
  ax = np.matmul ( a, x )
  resid_max = 0.0
  for j in range ( 0, x_num ):
    resid = np.amax ( np.abs ( ax[:,j] - b[:] ) )
    check[j] = ( resid == 0 )
    resid_max = max ( resid_max, resid )
    if ( not check[j] ):
      print ( '  Solution %d has a nonzero Loo residual of %g' % ( j, resid ) )

  if ( resid_max == 0.0 ):
    print ( '  All solutions had zero residual.' )
#
#  H2: Verify that solutions are correct.
#
  check = np.zeros ( x_num )

  print ( '' )
  print ( '  Check Loo residuals ||Ax-b||:' )
  print ( '' )

  ax = np.matmul ( a_rref, x )
  resid_max = 0.0
  for j in range ( 0, x_num ):
    resid = np.amax ( np.abs ( ax[:,j] - b_rref[:] ) )
    check[j] = ( resid == 0 )
    resid_max = max ( resid_max, resid )
    if ( not check[j] ):
      print ( '  Solution %d has a nonzero Loo residual of %g' % ( j, resid ) )

  if ( resid_max == 0.0 ):
    print ( '  All solutions had zero residual.' )

  if ( not np.any ( check ) ):
    print ( '  Returning with no satisfactory solutions.' )
    return m, n, x_num, a, b, x
#
#  I: Print solutions as patterns.
#
  print ( '' )
  print ( '  Translate each correct solution into a tiling:' )

  for j in range ( 0, x_num ):
    if ( check[j] ):
      label = ( '  Tiling based on solution %d' % ( j ) )
      pariomino_tiling_print ( r_shape, p_num, p_shapes, d, x[:,j], label )

  return m, n, x_num, a, b, x

def pariomino_tiling_solver_test01 ( ):

#*****************************************************************************80
#
## pariomino_tiling_solver_test01() tests pariomino_tiling_solver.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_tiling_solver_test01:' )
  print ( '  pariomino_tiling_solver solves a pariomino' )
  print ( '  tiling problem for a 2x4 rectangle.' )
#
#  Define R.
#
  shape_r = np.array ( [ \
    [ -1, +1, -1, +1 ], \
    [ +1, -1, +1, -1 ] ] )
  m_r, n_r = shape_r.shape
  pariomino_print ( shape_r, '  Region R:' )
#
#  Define N, O, P
#
  shape_n = np.array ( [ \
    [ -1 ] ] )
  m_n, n_n = shape_n.shape
  pariomino_print ( shape_n, '  pariomino N:' )

  shape_o = np.array ( [ \
    [ +1, -1, +1 ] ] )
  m_o, n_o = shape_o.shape
  pariomino_print ( shape_o, '  pariomino O:' )

  shape_p = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_p, n_p = shape_p.shape
  pariomino_print ( shape_p, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p = np.zeros ( [ m_r, n_r, p_num ] )
  p[0:m_n,0:n_n,0] = shape_n[0:m_n,0:n_n]
  p[0:m_o,0:n_o,1] = shape_o[0:m_o,0:n_o]
  p[0:m_p,0:n_p,2] = shape_p[0:m_p,0:n_p]
#
#  Set the vector D, which indicates how many copies of each pariomino
#  we can use: one of each, in this case.
#
  d = np.ones ( p_num )
#
#  Set up and solve the system.
#
  filename = '2x4_case1.lp'
  comment = 'The 2x4 example, case 1.'
  m, n, k, a, b, x = pariomino_tiling_solver ( shape_r, p_num, p, d, \
     filename, comment )
#
#  Reverse parity of the pieces.
#
  shape_n = pariomino_reverse ( shape_n )
  pariomino_print ( shape_n, '  pariomino -N:' )

  shape_o = pariomino_reverse ( shape_o )
  pariomino_print ( shape_o, '  pariomino -O:' )

  shape_p = pariomino_reverse ( shape_p )
  pariomino_print ( shape_p, '  pariomino -P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p = np.zeros ( [ m_r, n_r, p_num ] )
  p[0:m_n,0:n_n,0] = shape_n[0:m_n,0:n_n]
  p[0:m_o,0:n_o,1] = shape_o[0:m_o,0:n_o]
  p[0:m_p,0:n_p,2] = shape_p[0:m_p,0:n_p]
#
#  Set the vector D, which indicates how many copies of each pariomino
#  we can use: one of each, in this case.
#
  d = np.ones ( p_num )
#
#  Set up and solve the system.
#
  filename = '2x4_case2.lp'
  comment = 'The 2x4 example, case 2.'
  m, n, k, a, b, x = pariomino_tiling_solver ( shape_r, p_num, p, d, \
     filename, comment )

  return

def pariomino_tiling_solver_test02 ( ):

#*****************************************************************************80
#
## pariomino_tiling_solver_test02() tests pariomino_tiling_solver.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_tiling_solver_test02:' )
  print ( '  pariomino_tiling_solver solves a pariomino' )
  print ( '  tiling problem for a subset of a 4x4 rectangle.' )
#
#  Define R.
#
  shape_r = np.array ( [
    [ +1,  0,  0,  0 ], \
    [ -1,  0,  0,  0 ], \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )

  m_r, n_r = shape_r.shape
  pariomino_print ( shape_r, '  Region R:' )
#
#  Define N, O, P
#
  shape_n = np.array ( [
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  m_n, n_n = shape_n.shape
  pariomino_print ( shape_n, '  pariomino N:' )

  shape_o =  np.array ( [ \
    [ -1, +1, -1 ] ] )
  m_o, n_o = shape_o.shape
  pariomino_print ( shape_o, '  pariomino O:' )

  shape_p = np.array ( [
    [  0, +1 ], \
    [ +1, -1 ] ] )
  m_p, n_p = shape_p.shape
  pariomino_print ( shape_p, '  pariomino P:' )
#
#  Pack the arrays into P.
#
  p_num = 3
  p = np.zeros ( [ m_r, n_r, p_num ] )
  p[0:m_n,0:n_n,0] = shape_n[0:m_n,0:n_n]
  p[0:m_o,0:n_o,1] = shape_o[0:m_o,0:n_o]
  p[0:m_p,0:n_p,2] = shape_p[0:m_p,0:n_p]
#
#  Set the vector D, which indicates how many copies of each pariomino
#  we can use: one of each, in this case.
#
  d = np.ones ( p_num )
#
#  Set up and solve the system.
#
  filename = '4x4.lp'
  comment = 'The 4x4 example.'
  m, n, k, a, b, x = pariomino_tiling_solver ( shape_r, p_num, p, d, \
     filename, comment )

  return

def pariomino_transform ( p, rotate, reflect ):

#*****************************************************************************80
#
## pariomino_transform() transforms a pariomino.
#
#  Discussion:
#
#    A pariomino can be rotated or reflected.
#
#    This program is given a pariomino and returns the resulting pariomino
#    after the specified reflection and rotation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(M,N), a matrix of -1's, 0's and 1's representing the 
#    pariomino.  The matrix should be "tight", that is, there should be a
#    nonzero in row 1, and in column 1, and in row M, and in column N.
#
#    integer ROTATE, is 0, 1, 2, or 3, the number of 90 degree
#    counterclockwise rotations to be applied.
#
#    integer REFLECT, is 0 or 1.  If it is 1, then each row of the
#    pariomino matrix is to be reflected before any rotations are performed.
#
#  Output:
#
#    integer Q(MQ,NQ), the transformed pariomino.
#
  import numpy as np

  reflect = ( reflect % 2 )

  if ( reflect == 1 ):
    q = np.fliplr ( p )
  else:
    q = np.copy ( p )

  rotate = ( rotate % 4 )

  for k in range ( 0, rotate ):
    q = np.transpose ( q )
    q = np.flipud ( q )

  return q

def pariomino_transform_test ( ):

#*****************************************************************************80
#
## pariomino_transform_test() tests pariomino_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Local parameters:
#
#    integer P(M,N), a matrix of -1's, 0's and +1's representing the 
#    pariomino.  The matrix should be "tight", that is, there should be a
#    nonzero in row 1, and in column 1, and in row M, and in column N.
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_transform_test:' )
  print ( '  pariomino_transform() transforms a pariomino.' )
  print ( '  Generate all 8 combinations of rotation and reflection' )
  print ( '  applied to a pariomino represented by a -1/0/+1 matrix.' )

  p = np.array ( [ \
   [  0, -1, +1 ], \
   [ -1, +1,  0 ], \
   [  0, -1,  0 ] ] )

  pariomino_print ( p, '  The given pariomino P:' )

  for reflect in range ( 0, 2 ):
    for rotate in range ( 0, 4 ):

      q = pariomino_transform ( p, rotate, reflect )

      label = ( '  P after %d reflections and %d rotations:' \
        % ( reflect, rotate ) )
      pariomino_print ( q, label )

  return

def pariomino_variants ( p_m, p_n, p_num, p, d ):

#*****************************************************************************80
#
## pariomino_variants() finds variants of pariominoes in an array.
#
#  Discussion:
#
#    We are supplied with an array P of pariominoes.  We wish to "tile" a
#    region R, using, for each I, D(I) copies of pariomino P(I).
#    We are asked to return an array containing all the variants of these 
#    polynomials that can be generated by rotation and reflection.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P_M, P_N, the rows and columns in the pariomino P.
#
#    integer P_NUM, the number of pariominoes.
#
#    integer P(P_M,P_N,P_NUM), for each value K, P(:,:,K) is a matrix of 
#    -1's, 0's and 1's representing the K-th pariomino.  Each matrix should be 
#    "top-left tight", that is, there should be a nonzero in row 1, and in 
#    column 1.  However, there may be trailing rows and columns of zeros.
#
#    integer D(P_NUM), the number of copies of each pariomino that
#    may be used.  If D(I) <= 0, no variants of pariomino I will be generated.
#
#  Output:
#
#    integer V_NUM, the number of variants found.
#
#    integer V(P_M,P_N,V_NUM), the variants.
#
#    integer V_P(V_NUM) if V(:,:,I) is a variant of the pariomino
#    P(:,:,L), then V_P(I) is set to L.
#
  import numpy as np

  v_num = 0
  v = np.zeros ( [ p_m, p_n, 0 ] )
  v_p = np.zeros ( 0 )

  for l in range ( 0, p_num ):
#
#  Only use pariominoes for which the user has set D to at least 1.
#
    if ( 1 <= d[l] ):
#
#  Make a condensed version of the pariomino called "Q".
#
      q = pariomino_condense ( p[0:p_m,0:p_n,l] )

      mq, nq = q.shape
#
#  Generate all variants.
#
      for reflect in range ( 0, 2 ):
        for rotate in range ( 0, 5 ):

          s = pariomino_transform ( q, rotate, reflect )

          ms, ns = s.shape
#
#  Only proceed if this variant S will fit in [P_M,P_N].
#
          if ( ms <= p_m and ns <= p_n ):
#
#  Expand S to an [P_M,P_N] array T.
#
            t = np.zeros ( [ p_m, p_n ] )
            t[0:ms,0:ns] = s
#
#  Compare T to all previous variants.
#
            different = True
            for k in range ( 0, v_num ):
              test = ( t[0:p_m,0:p_n] == v[0:p_m,0:p_n,k] )
              if ( test.all ( ) ):
                different = False
                break
#
#  Once again, numpy's process of appending a value to a vector, or
#  a row or column to an array is stultifyingly stupid.
#
            if ( different ):
              t = np.reshape ( t, ( p_m, p_n, 1 ) )
              v = np.append ( v, t, axis = 2 )
              v_p = np.append ( v_p, [ l ] )
              v_num = v_num + 1
 
  return v_num, v, v_p

def pariomino_variants_test01 ( ):

#*****************************************************************************80
#
## pariomino_variants_test01() tests pariomino_variants().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_variants_test01' )
  print ( '  pariomino_variants() determines variants' )
  print ( '  of an array of pariominoes.' )
#
#  Define several pariominoes.
#
  p1 = np.array ( [ \
    [ +1, -1, +1, -1 ] ] )
  mp1, np1 = p1.shape

  p2 = np.array ( [ \
    [ +1, -1,  0 ], \
    [  0, +1,  0 ], \
    [  0, -1, +1 ] ] )
  mp2, np2 = p2.shape

  p3 = np.array ( [ \
    [ +1,  0,  0 ], \
    [ -1, +1, -1 ] ] )
  mp3, np3 = p3.shape
#
#  Set the encompassing region.
#
  r = np.array ( [ \
    [ +1, -1, +1, -1, +1 ], \
    [ -1, +1, -1, +1, -1 ], \
    [ +1, -1, +1, -1, +1 ] ] )
  mr, nr = r.shape
#
#  Pack the pariominoes into a single array.
#
  mq = mr
  nq = nr
  q_num = 3

  q = np.zeros ( [ mq, nq, q_num ] )
 
  q[0:mp1,0:np1,0] = p1[0:mp1,0:np1]
  q[0:mp2,0:np2,1] = p2[0:mp2,0:np2]
  q[0:mp3,0:np3,2] = p3[0:mp3,0:np3]
#
#  Specify number of copies.
#
  d = np.ones ( q_num )
#
#  Print the region.
#
  label = '  Region in which pariominoes must fit:'
  pariomino_print ( r, label )
#
#  Print the array of pariominoes.
#
  label = '  Array of pariominoes to be analyzed:'
  pariominoes_print ( mq, nq, q_num, q, label )
#
#  Request all the variants.
#
  v_num, v, v_p = pariomino_variants ( mq, nq, q_num, q, d )

  print ( '' )
  print ( '  %d variants fit the region' % ( v_num ) )

  for k in range ( 0, v_num ):
    label = ( '  Variant #%d of pariomino #%d' % ( k, v_p[k] ) )
    pc = pariomino_condense ( v[0:mq,0:nq,k] )
    pariomino_print ( pc, label )
 
  return

def pariomino_variants_test02 ( ):

#*****************************************************************************80
#
## pariomino_variants_test02() tests pariomino_variants().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariomino_variants_test02' )
  print ( '  pariomino_variants() determines variants' )
  print ( '  of an array of pariominoes.' )
#
#  Define several pariominoes.
#
  p1 = np.array ( [ \
    [ -1 ] ] )
  mp1, np1 = p1.shape

  p2 = np.array ( [ \
    [ +1, -1, +1 ] ] )
  mp2, np2 = p2.shape

  p3 = np.array ( [ \
    [  0,  0, -1 ], \
    [ +1, -1, +1 ] ] )
  mp3, np3 = p3.shape
#
#  Set the encompassing region.
#
  r = np.array ( [ \
    [ +1, -1, +1, -1 ], \
    [ -1, +1, -1, +1 ] ] )
  mr, nr = r.shape
#
#  Pack the pariominoes into a single array.
#
  mq = mr
  nq = nr
  q_num = 3

  q = np.zeros ( [ mq, nq, q_num ] )
 
  q[0:mp1,0:np1,0] = p1[0:mp1,0:np1]
  q[0:mp2,0:np2,1] = p2[0:mp2,0:np2]
  q[0:mp3,0:np3,2] = p3[0:mp3,0:np3]
#
#  Specify the number of duplicates.
#
  d = np.ones ( q_num )
#
#  Print the region.
#
  label = '  Region in which pariominoes must fit:'
  pariomino_print ( r, label )
#
#  Print the array of pariominoes.
#
  label = '  Array of pariominoes to be analyzed:'
  pariominoes_print ( mq, nq, q_num, q, label )
#
#  Request all the variants.
#
  v_num, v, v_p = pariomino_variants ( mq, nq, q_num, q, d )

  print ( '' )
  print ( '  %d variants fit the region' % ( v_num ) )

  for k in range ( 0, v_num ):
    label = ( '  Variant %d of pariomino %d' % ( k, v_p[k] ) )
    pc = pariomino_condense ( v[0:mq,0:nq,k] )
    pariomino_print ( pc, label )
 
  return

def pariominoes_print ( p_m, p_n, p_num, p, label ):

#*****************************************************************************80
#
## pariominoes_print() prints pariominoes packed in an array.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P_M, P_N, the rows and columns in the representation.
#
#    integer P_NUM, the number of pariominoes.
#
#    integer P(P_M,P_N,P_NUM), a matrix representing the pariominoes.  
#
#    string LABEL, a label to be printed first.  
#
  print ( '' )
  print ( label )
  print ( '' )

  if ( p_m <= 0 or p_n <= 0 or p_num <= 0 ):
    print ( '  [ Null matrix ]' )
  else:
    print ( '  %dx%d array of %d pariominoes:' % ( p_m, p_n, p_num ) )
    for k in range ( 0, p_num ):
      q = pariomino_condense ( p[0:p_m,0:p_n,k] )
      label2 = ( '  pariomino #%d' % ( k ) )
      pariomino_print ( q, label2 )

  return

def pariominoes_print_test ( ):

#*****************************************************************************80
#
## pariominoes_print_test() tests pariominoes_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pariominoes_print_test' )
  print ( '  pariominoes_print() prints an array of pariominoes.' )
#
#  Define several pariominos.
#
  p1 = np.array ( [ \
    [ +1, -1, +1, -1 ] ] )
  mp1, np1 = p1.shape

  p2 = np.array ( [ \
    [ +1, -1,  0 ], \
    [  0, +1,  0 ], \
    [  0, -1, +1 ] ] )
  mp2, np2 = p2.shape

  p3 = np.array ( [ \
    [ +1,  0,  0 ], \
    [ -1, +1, -1 ] ] )
  mp3, np3 = p3.shape
#
#  Pack the pariominoes into a single array.
#
  mq = 3
  nq = 5
  q_num = 3

  q = np.zeros ( [ 3, 5, q_num ] )
 
  q[0:mp1,0:np1,0] = p1[0:mp1,0:np1]
  q[0:mp2,0:np2,1] = p2[0:mp2,0:np2]
  q[0:mp3,0:np3,2] = p3[0:mp3,0:np3]
#
#  Print the array of pariominoes.
#
  label = '  Array of pariominoes to be analyzed:'
  pariominoes_print ( mq, nq, q_num, q, label )

  return

def polyomino_charge ( p1 ):

#*****************************************************************************80
#
## polyomino_charge() assigns a parity to each cell of a polyomino.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P1(M,N), the representation of polyomino P1. 
#
#  Output:
#
#    integer P2(M,N), the representation of pariomino P2. 
#
  p2 = abs ( p1 )
  m, n = p2.shape

  si = +1
  for i in range ( 0, m ):
    sj = +1
    for j in range ( 0, n ):
      p2[i,j] = si * sj * p2[i,j]
      sj = -sj
    si = - si

  return p2

def polyomino_charge_test ( ):

#*****************************************************************************80
#
## polyomino_charge_test() tests polyomino_charge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polyomino_charge_test' )
  print ( '  polyomino_charge() charges the cells of a polyomino,' )
  print ( '  creating a pariomino.')

  p1 = np.array ( [ \
     [ 0,  0,  0,  0,  1,  0 ], \
     [ 1,  0,  0,  0,  1,  1 ], \
     [ 1,  0,  1,  1,  1,  0 ], \
     [ 1,  0,  1,  0,  1,  0 ], \
     [ 1,  1,  1,  1,  1,  0 ] ] )

  polyomino_print ( p1, '  polyomino:' )

  p2 = polyomino_charge ( p1 )
  pariomino_print ( p2, '  resulting pariomino:' )

  return

def polyomino_print ( p, label ):

#*****************************************************************************80
#
## polyomino_print() prints a polyomino.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(M,N), a matrix of 0's and 1's representing the 
#    polyomino.  The matrix should be "tight", that is, there should be a
#    1 in row 1, and in column 1, and in row M, and in column N.
#
#    string LABEL, a title for the polyomino.
#
  m, n = p.shape

  print ( '' )
  print ( label )
  print ( '' )
  if ( m <= 0 or n <= 0 ):
    print ( '  [ Null matrix ]' )
  else:
    for i in range ( 0, m ):
      for j in range ( 0, n ):
        print ( '  %d' % ( p[i,j] ), end = '' )
      print ( '' )

  return

def polyomino_print_test ( ):

#*****************************************************************************80
#
## polyomino_print_test() tests polyomino_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polyomino_print_test:' )
  print ( '  polyomino_print prints a polyomino.' )

  p = np.array ( [ \
    [ 1, 0, 1, 1 ], \
    [ 1, 1, 1, 0 ], \
    [ 0, 1, 1, 0 ] ] )

  label = '  A sample polyomino:'

  polyomino_print ( p, label )

  print ( '' )
  print ( 'polyomino_print_test:' )
  print ( '  Normal end of execution.' )

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

def r8mat_rref ( m, n, a ):

#*****************************************************************************80
#
## r8mat_rref() computes the reduced row echelon form of a matrix.
#
#  Discussion:
#
#    A matrix is in row echelon form if:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Example:
#
#    Input matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#    -2.0 -6.0  0.0 -2.0 -8.0  3.0  1.0
#     3.0  9.0  0.0  0.0  6.0  6.0  2.0
#    -1.0 -3.0  0.0  1.0  0.0  9.0  3.0
#
#    Output matrix:
#
#     1.0  3.0  0.0  0.0  2.0  0.0  0.0
#     0.0  0.0  0.0  1.0  2.0  0.0  0.0
#     0.0  0.0  0.0  0.0  0.0  1.0  0.3
#     0.0  0.0  0.0  0.0  0.0  0.0  0.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
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
#    integer M, N, the number of rows and columns of
#    the matrix A.
#
#    real A(M,N), the matrix to be analyzed. 
#
#  Output:
#
#    real A(M,N), the RREF form of the matrix.
#
#    real DET, the pseudo-determinant.
#
  import numpy as np

  det = 1.0
  asum = 0.0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      asum = asum + abs ( a[i,j] )
  tol = asum * np.finfo(float).eps
  lead = 0

  for r in range ( 0, m ):

    if ( n <= lead ):
      break

    i = r
    
    while ( abs ( a[i,lead] ) <= tol ):

      i = i + 1

      if ( m <= i ):
        i = r
        lead = lead + 1
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break

    for j in range ( 0, n ):
      t      = a[i,j]
      a[i,j] = a[r,j]
      a[r,j] = t

    det = det * a[r,lead]
    a[r,0:n] = a[r,0:n] / a[r,lead]

    for i in range ( 0, m ):
      if ( i != r ):
        a[i,0:n] = a[i,0:n] - a[i,lead] * a[r,0:n]

    lead = lead + 1

  return a, det

def r8mat_rref_test ( ):

#*****************************************************************************80
#
## r8mat_rref_test() tests r8mat_rref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array( [ \
    [  1.0,  3.0,  0.0,  2.0,  6.0,  3.0,  1.0 ], \
    [ -2.0, -6.0,  0.0, -2.0, -8.0,  3.0,  1.0 ], \
    [  3.0,  9.0,  0.0,  0.0,  6.0,  6.0,  2.0 ], \
    [ -1.0, -3.0,  0.0,  1.0,  0.0,  9.0,  3.0 ] ] )

  print ( '' )
  print ( 'r8mat_rref_test' )
  print ( '  r8mat_rref computes the reduced row echelon form of a matrix.' )

  r8mat_print ( m, n, a, '  Input A:' )

  a, det = r8mat_rref ( m, n, a )

  print ( '' )
  print ( '  Pseudo-determinant = %g' % ( det ) )

  r8mat_print ( m, n, a, '  RREF form:' )

  return

def r8mat_rref_solve_binary ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary() seeks binary solutions of an RREF system.
#
#  Discussion:
#
#    An MxN linear system Ax = b is considered, in which only binary
#    solutions are allowed that is, each entry of x is either 0 or 1.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to row-reduced echelon form.  Therefore, the matrix A satisfies:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the rows and columns of the RREF matrix A.
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
#  Remove the zero rows of A.
#
  while ( 0 < m ):
    if ( np.sum ( abs ( a[m-1,0:n] ) ) == 0.0 ):
      a = np.delete ( a, m-1, axis = 0 )
      m = m - 1
    else:
      break
#
#  Number of dimensions of freedom is n - m.
#
  klog = n - m
#
#  Determine the indeterminate variables.
#  Insert corresponding data in A and B.
#
  freedom = np.zeros ( 0, dtype = int )

  if ( 0 < klog ):

    for j in range ( 0, n ):
      if ( j+1 <= m ):
        if ( a[j,j] != 1 ):
          r = r8vec_identity_row ( n, j )
          a = np.insert ( a, j, r, axis = 0 )
          b = np.insert ( b, j, 0, axis = 0 )
          freedom = np.append ( freedom, j )
          m = m + 1
      else:
        r = r8vec_identity_row ( n, j )
        a = np.append ( a, r, axis = 0 )
        b = np.append ( b, 0 )
        freedom = np.append ( freedom, j )
        m = m + 1
#
#  The indeterminate variables have a simple equation 
#    x(i) = b(i) = 0 or 1
#  Set up and solve every variation of this system.
#  If a solution is binary, accept it.
#
  x_num = 0
  x = np.zeros ( [ n, 0 ], dtype = float )

  binary = np.zeros ( klog )

  while ( True ):

    b2 = b
    for k in range ( 0, klog ):
      i = freedom[k]
      b2[i] = binary[k]

    y = r8mat_u_solve ( n, a, b2 )

    if ( r8vec_is_binary ( n, y ) ):
      y = np.reshape ( y, ( n, 1 ) )
      x = np.append ( x, y, axis = 1 )
      x_num = x_num + 1

    binary = r8vec_binary_next ( klog, binary )

    if ( np.sum ( binary ) == 0 ):
      break

  return x_num, x

def r8mat_rref_solve_binary_test ( ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary_test() tests r8mat_rref_solve_binary().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_rref_solve_binary_test():' )
  print ( '  r8mat_rref_solve_binary() seeks binary solutions of' )
  print ( '  a Row-Reduced Echelon Form linear system A*x=b.' )

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

  r8mat_print ( m, n, a, '  The RREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  r8vec_print ( m, b, '  The RREF right hand side b:' )

  x_num, x = r8mat_rref_solve_binary ( m, n, a, b )

  r8mat_print ( n, x_num, x, '  Binary solution vectors x:' )

  return

def r8mat_rref_solve_binary_nz ( m, n, nz, a, b ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary_nz() seeks binary solutions of an RREF system.
#
#  Discussion:
#
#    Any acceptable binary solution must have exactly NZ nonzero entries.
#
#    An MxN linear system Ax = b is considered, in which only binary
#    solutions are allowed that is, each entry of x is either 0 or 1.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to row-reduced echelon form.  Therefore, the matrix A satisfies:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the rows and columns of the RREF matrix A.
#
#    integer NZ, the number of nonzeros required in any binary solution.
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

  verbose = True
#
#  Remove the zero rows of A.
#
  while ( 0 < m ):
    if ( np.sum ( abs ( a[m-1,0:n] ) ) == 0.0 ):
      a = np.delete ( a, m-1, axis = 0 )
      m = m - 1
    else:
      break
#
#  Number of dimensions of freedom is n - m.
#
  klog = n - m

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  System has', klog, 'degrees of freedom.' )
#
#  Determine the indeterminate variables.
#  Insert corresponding data in A and B.
#
  freedom = np.zeros ( 0, dtype = int )

  if ( 0 < klog ):

    for j in range ( 0, n ):
      if ( j+1 <= m ):
        if ( a[j,j] != 1 ):
          r = r8vec_identity_row ( n, j )
          a = np.insert ( a, j, r, axis = 0 )
          b = np.insert ( b, j, 0, axis = 0 )
          freedom = np.append ( freedom, j )
          m = m + 1
      else:
        r = r8vec_identity_row ( n, j )
        a = np.append ( a, r, axis = 0 )
        b = np.append ( b, 0 )
        freedom = np.append ( freedom, j )
        m = m + 1
#
#  For debugging, print augmented system.
#
  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Augmented Row-Reduced Echelon Form system matrix A and right hand side B:' )
    print ( '  Columns associated with a free variable are headed with a "*"' )
    print ( '' )

    label = n * ':'
    label = list ( label )
    for k in range ( 0, klog ):
      j = freedom[k]
      label[j] = '*'

    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( ' ', label[j], sep = '', end = '' )
    print ( '' )

    for i in range ( 0, m ):
      print ( '  ', end = '' )
      for j in range ( 0, n ):
        print ( '%2d' % ( a[i,j] ), sep = '', end = '' )
      print ( '  %2d' % ( b[i] ) )
#
#  Initialize to "empty" a list of binary soutions.
#
#  There are KLOG degrees of freedom, each of which could be set to 1.
#  There must be NZ variables set to 1.
#  Consider setting NZ2 degrees of freedom to 1, where NZ2 is between 0
#  and the minimum of NZ and KLOG.
#
#  Choose every possible selection of NZ2 degrees of freedom, and solve
#  the system.
#
#  If the resulting solution is binary, then add it to the list.
#
  x_num = 0
  x = np.zeros ( [ n, 0 ], dtype = float )
  b_num = 0

  nz2_max = int ( min ( nz, klog ) )

  for nz2 in range ( 0, nz2_max + 1 ):

    done = True
    free_sub = np.zeros ( nz2_max )

    while ( True ):

      free_sub, done = ksub_next4 ( klog, nz2, free_sub, done )

      if ( done ):
        break

      b2 = np.copy ( b )
      b2[freedom[free_sub[0:nz2]-1]] = 1
      b_num = b_num + 1

      y = r8mat_u_solve ( n, a, b2 )

      if ( r8vec_is_binary ( n, y ) ):
        y = np.reshape ( y, ( n, 1 ) )
        x = np.append ( x, y, axis = 1 )
        x_num = x_num + 1

  if ( verbose ):
    print ( '' )
    print ( 'VERBOSE:' )
    print ( '  Tried', b_num, 'right hands sides, found', x_num, 'solutions.' )

  return x_num, x

def r8mat_rref_solve_binary_nz_test ( ):

#*****************************************************************************80
#
## r8mat_rref_solve_binary_nz_test() tests r8mat_rref_solve_binary_nz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_rref_solve_binary_nz_test():' )
  print ( '  r8mat_rref_solve_binary_nz() seeks binary solutions of' )
  print ( '  a Row-Reduced Echelon Form linear system A*x=b' )
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

  r8mat_print ( m, n, a, '  The RREF matrix A:' )

  b = np.array ( [ 0, 1, 0, 1, 1, 1, 0, 0, 0 ] )

  r8vec_print ( m, b, '  The RREF right hand side b:' )

  nz = 4
  print ( '' )
  print ( '  Only consider binary solutions with exactly', nz, 'nonzeros.' )

  x_num, x = r8mat_rref_solve_binary_nz ( m, n, nz, a, b )

  r8mat_print ( n, x_num, x, '  Binary solution vectors x:' )

  return

def r8mat_u_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_u_solve() solves an upper triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#    real A(N,N), the N by N upper triangular matrix.
#
#    real B(N), the right hand side of the linear system.
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

def r8mat_u_solve_test ( ):

#*****************************************************************************80
#
## r8mat_u_solve_test() tests r8mat_u_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2015
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
  print ( 'r8mat_u_solve_test' )
  print ( '  r8mat_u_solve() solves an upper triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_u_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )

  return

def r8vec_binary_next ( n, bvec ):

#*****************************************************************************80
#
## r8vec_binary_next() generates the next binary vector.
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
#    real BVEC(N), the vector whose successor is desired.
#
#  Output:
#
#    real BVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( bvec[i] == 0.0 ):
      bvec[i] = 1.0
      break

    bvec[i] = 0.0

  return bvec

def r8vec_binary_next_test ( ):

#*****************************************************************************80
#
## r8vec_binary_next_test() tests r8vec_binary_next().
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

  n = 3

  print ( '' )
  print ( 'r8vec_binary_next_test' )
  print ( '  r8vec_binary_next() generates the next binary vector.' )
  print ( '' )
 
  bvec = np.zeros ( n, dtype = np.float64 )

  while ( True ):

    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%d' % ( bvec[i] ), end = '' )
    print ( '' )

    if ( all ( bvec[0:n] == 1.0 ) ):
      break

    bvec = r8vec_binary_next ( n, bvec )

  return

def r8vec_identity_row ( n, i ):

#*****************************************************************************80
#
## r8vec_identity_row() returns a row of the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2018
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
#    0-based indexing is used.
#
#  Output:
#
#    real A[1,N], the vector.
#
  import numpy as np

  a = np.zeros ( [ 1, n ] );

  if ( 0 <= i and i < n ):
    a[0,i] = 1.0

  return a

def r8vec_identity_row_test ( ):

#*****************************************************************************80
#
## r8vec_identity_row_test() tests r8vec_identity_row().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8vec_identity_row_test' )
  print ( '  r8vec_identity_row() returns a row of the identity matrix.' )
  print ( '' )

  n = 5
  for i in range ( -1, 6 ):
    a = r8vec_identity_row ( n, i )
    print ( '  %2d: ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( ' %d' % ( a[0,j] ), end = '' )
    print ( '' )

  return

def r8vec_is_binary ( n, x ):

#*****************************************************************************80
#
## r8vec_is_binary() is true if an R8VEC only contains 0 and 1 entries.
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
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    real VALUE, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, n ):

    if ( x[i] != 0.0 and x[i] != 1.0 ):
      value = False
      break

  return value

def r8vec_is_binary_test ( ):

#*****************************************************************************80
#
## r8vec_is_binary_test() tests r8vec_is_binary().
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
  print ( 'r8vec_is_binary_test():' )
  print ( '  r8vec_is_binary() is TRUE if an R8VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1.0, 0.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0.0, 2.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

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

def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_transpose_print() prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
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
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## r8vec_transpose_print_test() tests r8vec_transpose_print().
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

  n = 11

  print ( '' )
  print ( 'r8vec_transpose_print_test():' )
  print ( '  r8vec_transpose_print() prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x = np.array ( [ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 ] )

  r8vec_transpose_print ( n, x, '  The vector X:' )

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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  pariomino_test ( )
  timestamp ( )

