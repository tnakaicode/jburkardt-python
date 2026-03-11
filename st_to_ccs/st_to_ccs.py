#! /usr/bin/env python3
#
def ccs_header_print ( icc, ccc, title ):

#*****************************************************************************80
#
## ccs_header_print() prints the header of a CCS matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ICC(NCC), CCC(N+1), row and compressed column indices.
#
#    string TITLE: a title for the matrix.
#
  import numpy as np

  m = np.max ( icc ) + 1
  n = len ( ccc ) - 1
  ncc = len ( icc )

  print ( '' )
  print ( title )
  print ( '  CCS matrix header:' )
  print ( '  Number of rows        M = ', m )
  print ( '  Number of columns     N = ', n )
  print ( '  Number of nonzeros  NCC = ', ncc )
  print ( '  Compressed column indices:' )
  print ( ccc )
  print ( '  row indices:' )
  print ( icc )

  return

def ccs_mv ( m, n, ncc, icc, ccc, acc, x ):

#*****************************************************************************80
#
## ccs_mv() multiplies a CCS matrix by a vector
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
#  Reference:
#
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NCC, the number of values.
#
#    integer ICC(NCC), the row indices.
#
#    integer CCC(N+1), the compressed columns
#
#    real ACC(NCC), the values.
#
#    real X(N), the vector to be multiplied.
#
#  Output:
#
#    real B(M), the product A*X.
#
  import numpy as np

  b = np.zeros ( m )

  for j in range ( 0, n ):
    for k in range ( ccc[j], ccc[j+1] ):
      i = icc[k]
      b[i] = b[i] + acc[k] * x[j]

  return b

def ccs_print ( icc, ccc, acc, title ):

#*****************************************************************************80
#
## ccs_print() prints a sparse matrix in CCS format.
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
#  Input:
#
#    integer ICC(NCC), the row indices.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
#    character TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '     #     I     J       A' )
  print ( '  ----  ----  ----  --------------' )
  print ( '' )

  ncc = len ( icc )

  if ( ccc[0] == 0 ):

    j = 0
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+1] <= k ):
        j = j + 1
      print ( '  %4d  %4d  %4d  %16.8g' % ( k, i, j, acc[k] ) )
#
#  Matrix uses 1-based indexing.
#
  else:

    j = 1
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j] <= k + 1 ):
        j = j + 1
      print ( '  %4d  %4d  %4d  %16.8g' % ( k + 1, i, j, acc[k] ) )

  return

def ccs_print_some ( i_min, i_max, j_min, j_max, ncc, n, icc, ccc, acc, title ):

#*****************************************************************************80
#
## ccs_print_some() prints some of a sparse matrix in CCS format.
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
#  Input:
#
#    integer I_MIN, IMAX, the first and last rows to print.
#
#    integer J_MIN, J_MAX, the first and last columns 
#    to print.
#
#    integer NCC, the number of elements.
#
#    integer N, the number of columns.
#
#    integer ICC(NCC), the row indices.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
#    string TITLE, a title.
#
  if ( ccc[0] == 0 ):

    j = 0
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+2] <= k - 1 ):
        j = j + 1
      if ( i_min <= i and i <= i_max and j_min <= j and j <= j_max ):
        print ( '  %4d  %4d  %4d  %16.8g' % ( k - 1, i, j, acc[k] ) )

  else:

    j = 1
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+1] <= k ):
        j = j + 1
      if ( i_min <= i and i <= i_max and j_min <= j and j <= j_max ):
        print ( '  %4d  %4d  %4d  %16.8g' % ( k, i, j, acc[k] ) )

  return

def ccs_write ( prefix, icc, ccc, acc ):

#*****************************************************************************80
#
## ccs_write() writes a sparse matrix in CCS format to 3 files.
#
#  Discussion:
#
#    Three files will be created:
#    * prefix_icc.txt contains NCC ICC values
#    * prefix_ccc.txt contains N+1 CCC values
#    * prefix_acc.txt contains NCC ACC values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, a common prefix for the filenames.
#
#    integer ICC(NCC), the row indices.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
  import numpy as np

  filename_icc = prefix + '_icc.txt'
  np.savetxt ( filename_icc, icc )

  filename_ccc = prefix + '_ccc.txt'
  np.savetxt ( filename_ccc, ccc )

  filename_acc = prefix + '_acc.txt'
  np.savetxt ( filename_acc, acc )

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
#    26 June 2022
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

def st_read ( filename ):

#*****************************************************************************80
#
## st_read() reads a file describing an matrix in ST format.
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
#  Input:
#
#    string FILENAME, the name of the ST file.
#
#  Output:
#
#    integer IST(NST), JST(NST), the 0-based row and column
#    index of a nonzero matrix entry.
#
#    real AST(NST), the value of a nonzero matrix entry.
#
  import numpy as np

  data = np.loadtxt ( filename )
  nst = data.shape[0]

  ist = data[:,0].astype(int)
  jst = data[:,1].astype(int)
  ast = data[:,2]
#
#  If indexing is 1-based, convert it to 0-based.
#
  if ( np.min ( ist ) == 1 or np.min ( jst ) == 1 ):
    print ( '' )
    print ( '  Input matrix indices seem to be 1-based.' )
    ist = ist - 1
    jst = jst - 1
#
#  Need to SORT information.
#
  for i in range ( 0, nst ):

    x1 = ist[i]
    x2 = jst[i]
    x3 = ast[i]

    j = i - 1

    while ( 0 <= j ):

      if ( ist[j] < x1 or ( ist[j] == x1 and jst[j] < x2 ) ):
        break

      ist[j+1] = ist[j]
      jst[j+1] = jst[j]
      ast[j+1] = ast[j]
      j = j - 1

    ist[j+1] = x1
    jst[j+1] = x2
    ast[j+1] = x3
#
#  Need to detect duplicate (I,J) sets and merge A values.
#
  nst2 = 0
  ist2 = np.array ( [ ist[0] ] )
  jst2 = np.array ( [ jst[0] ] )
  ast2 = np.array ( [ ast[0] ] )
  nst2 = nst2 + 1

  for i in range ( 1, nst ):
    if ( ist[i] == ist2[nst2-1] and jst[i] == jst2[nst2-1] ):
      ast2[nst2-1] = ast2[nst2-1] + ast[i]
    else:
      ist2 = np.append ( ist2, ist[i] )
      jst2 = np.append ( jst2, jst[i] )
      ast2 = np.append ( ast2, ast[i] )
      nst2 = nst2 + 1

  print ( 'st_read: was ', nst, ' now is ', nst2 )

  return ist, jst, ast

def st_header_print ( ist, jst, title ):

#*****************************************************************************80
#
## st_header_print() prints the header of an ST file.
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
#  Input:
#
#    integer IST(NST), JST(NST), row and column indices of nonzeros.
#
  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  m = i_max - i_min + 1
  n = j_max - j_min + 1
  nst = len ( ist )

  print ( '' )
  print ( title )
  print ( '  Header information:' )
  print ( '  Minimum row index I_MIN = ', i_min )
  print ( '  Maximum row index I_MAX = ', i_max )
  print ( '  Minimum col index J_MIN = ', j_min )
  print ( '  Maximum col index J_MAX = ', j_max )
  print ( '  Number of rows        M = ', m )
  print ( '  Number of columns     N = ', n )
  print ( '  Number of nonzeros  NST = ', nst )

  return

def st_mv ( ist, jst, ast, x ):

#*****************************************************************************80
#
## st_mv() multiplies an ST matrix by a vector.
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
#  Input:
#
#    integer IST(NST), JST(NST), the row and 
#    column indices of the nonzero elements.
#
#    real AST(NST), the nonzero elements of the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product vector A*X.
#
  import numpy as np

  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  m = i_max - i_min + 1
  n = j_max - j_min + 1

  b = np.zeros ( m )

  nst = len ( ist )

  for k in range ( 0, nst ):
    i = ist[k]
    j = jst[k]
    b[i] = b[i] + ast[k] * x[j]

  return b

def st_print ( ist, jst, ast, title ):

#*****************************************************************************80
#
## st_print() prints an ST file.
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
#  Input:
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
#    string TITLE, a title.
#
  import numpy as np

  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  m = i_max - i_min + 1
  n = j_max - j_min + 1
  nst = len ( ist )

  print ( '' )
  print ( title )
  print ( '' )

  for k in range ( 0, nst ):
    print ( '  %8d  %8d  %8d  %16.8f' % ( k, ist[k], jst[k], ast[k] ) )

  return

def st_to_ccs_index ( ist, jst ):

#*****************************************************************************80
#
## st_to_ccs_index() creates CCS indices from ST data.
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
#    integer IST(NST), JST(NST), the ST rows and columns.
#
#  Output:
#
#    integer ICC(NCC), the row indices.
#
#    integer CCC(N+1), the compressed CCS columns.
#
  import numpy as np

  nst = len ( ist )
  n = np.max ( jst ) + 1
#
#  Sort the elements.
#
  jst2, ist2 = i4vec2_sort_insert_a ( jst, ist )
#
#  Get the unique elements.
#
  jcc, icc = i4vec2_sorted_unique ( jst2, ist2 )
  ncc = len ( jcc )
#
#  Compress the column index.
#
  ccc = np.zeros ( n + 1, dtype = int )

  ccc[0] = 0
  jlo = 0
  for i in range ( 0, ncc ):
    jhi = jcc[i]
    if ( jhi != jlo ):
      ccc[jlo+1:jhi+1] = i
      jlo = jhi

  jhi = n + 1
  ccc[jlo+1:jhi+1] = ncc

  return icc, ccc

def st_to_ccs_size ( ist, jst ):

#*****************************************************************************80
#
## st_to_ccs_size() sizes CCS indexes based on ST data.
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
#    integer IST(NST), JST(NST), the ST rows and columns.
#
#  Output:
#
#    integer NCC, the number of CCS elements.
#
  nst = len ( ist )
#
#  Sort by column first, then row.
#
  jst2, ist2 = i4vec2_sort_insert_a ( jst, ist )
#
#  Count the unique pairs.
#
  ncc = i4vec2_sorted_unique_count ( jst2, ist2 )

  return ncc

def st_to_ccs_test ( ):

#*****************************************************************************80
#
## st_to_ccs_test() tests st_to_ccs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'st_to_ccs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test st_to_ccs().' )

  st_to_ccs_test01 ( )
  st_to_ccs_test02 ( )
  st_to_ccs_test03 ( )
  st_to_ccs_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'st_to_ccs_test():' )
  print ( '  Normal end of execution.' )

  return

def st_to_ccs_test01 ( ):

#*****************************************************************************80
#
## st_to_ccs_test01() tests st_to_ccs() using a tiny matrix.
#
#  Discussion:
#
#    This test uses a trivial matrix whose full representation is:
#
#          2  3  0  0  0
#          3  0  4  0  6
#      A = 0 -1 -3  2  0
#          0  0  1  0  0
#          0  4  2  0  1
#
#    A (1-based) ST representation, reading in order by rows is:
#
#      I  J   A
#     -- --  --
#      1  1   2
#      1  2   3
#
#      2  1   3
#      2  3   4
#      2  5   6
#
#      3  2  -1
#      3  3  -3
#      3  4   2
#
#      4  3   1
#
#      5  2   4
#      5  3   2
#      5  5   1
#
#    The CCS representation (which goes in order by columns) is
#
#      #   I  JC   A
#     --  --  --  --
#      1   1   1   2
#      2   2       3
#
#      3   1   3   3
#      4   3      -1
#      5   5       4
#
#      6   2   6   4
#      7   3      -3
#      8   4       1
#      9   5       2
#
#     10   3  10   2
#
#     11   2  11   6
#     12   5       1
#
#     13   *  13
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
  print ( 'st_to_ccs_test01():' )
  print ( '  Convert a sparse matrix from ST to CCS format.' )
  print ( '  ST:  sparse triplet,    I, J,  A.' )
  print ( '  CCS: compressed column, I, CC, A.' )
#
#  Read the ST matrix.
#
  if ( True ):

    filename_st = 'tiny_st.txt'
    ist, jst, ast = st_read ( filename_st )
#
#  Set the matrix.
#
  else:

    m = 5
    n = 5
    nst = 12

    ast = np.array ( [ \
      0.0,  1.0, \
     10.0,  12.0,  14.0, \
     21.0,  22.0,  23.0, \
     32.0, \
     41.0,  42.0,  44.0 ] )

    ist = np.array ( [ \
      0, 0, \
      1, 1, 1, \
      2, 2, 2, \
      3, \
      4, 4, 4 ] )

    jst = np.array ( [ \
      0, 1, \
      0, 2, 4, \
      1, 2, 3, \
      2, \
      1, 2, 4 ] )
#
#  Print the matrix.
#
  title = 'The ST matrix:'
  st_header_print ( ist, jst, title )
  st_print ( ist, jst, ast, title )
#
#  Get the CCS size.
#
  ncc = st_to_ccs_size ( ist, jst )

  print ( '' )
  print ( '  Number of ST values =  ', len ( ast ) )
  print ( '  Number of CCS values = ', ncc )
#
#  Create the CCS indices.
#
  icc, ccc = st_to_ccs_index ( ist, jst )
#
#  Create the CCS values.
#
  acc = st_to_ccs_values ( ist, jst, ast, icc, ccc )
#
#  Print the CCS matrix.
#
  title = 'The CCS matrix:'
  ccs_header_print ( icc, ccc, title )
  ccs_print ( icc, ccc, acc, title )

  return

def st_to_ccs_test02 ( ):

#*****************************************************************************80
#
## st_to_ccs_test02() tests st_to_ccs() on a matrix stored in a file.
#
#  Discussion:
#
#    We assume no prior knowledge about the matrix except the filename.
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
  filename_st = 'west_st.txt'

  print ( '' )
  print ( 'st_to_ccs_test02():' )
  print ( '  Convert a sparse matrix from ST to CC format.' )
  print ( '  ST:  sparse triplet,    I, J,  A.' )
  print ( '  CCS: compressed column, I, CC, A.' )
  print ( '  This matrix is read from the file "' + filename_st + '"' )
#
#  Read the ST matrix.
#
  ist, jst, ast = st_read ( filename_st )
#
#  Print the ST matrix.
#
  title = 'The ST matrix:'
  st_header_print ( ist, jst, title )
  st_print ( ist, jst, ast, title )
#
#  Get the CCS size.
#
  ncc = st_to_ccs_size ( ist, jst )

  print ( '' )
  print ( '  Number of ST values =  ', len ( ast ) )
  print ( '  Number of CCS values = ', ncc )
#
#  Create the CCS indices.
#
  icc, ccc = st_to_ccs_index ( ist, jst )
#
#  Create the CCS values.
#
  acc = st_to_ccs_values ( ist, jst, ast, icc, ccc )
#
#  Print the CCS matrix.
#
  title = 'The CCS matrix:'
  ccs_print ( icc, ccc, acc, title )

  return

def st_to_ccs_test03 ( ):

#*****************************************************************************80
#
## st_to_ccs_test03() creates a CCS sparse matrix file from an ST file.
#
#  Discussion:
#
#    We assume no prior knowledge about the matrix except the filename.
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
  prefix = 'west'
  filename_st = prefix + '_st.txt'
  filename_icc = prefix + '_icc.txt'
  filename_ccc = prefix + '_ccc.txt'
  filename_acc = prefix + '_acc.txt'

  print ( '' )
  print ( 'st_to_ccs_test03()' )
  print ( '  Convert a sparse matrix from ST to CCS format.' )
  print ( '  ST:  sparse triplet,    I, J,  A.' )
  print ( '  CCS: compressed column, I, CC, A.' )
  print ( '  The ST matrix is read from the file "' + filename_st + '"' )
  print ( '  and the CCS matrix is written to the files:' )
  print ( '    "' + filename_icc + '",' )
  print ( '    "' + filename_ccc + '",' )
  print ( '    "' + filename_acc + '"' )
#
#  Read the ST matrix.
#
  ist, jst, ast = st_read ( filename_st )
  nst = len ( ist )
#
#  Print the ST matrix.
#
  title = 'The ST matrix:'
  st_header_print ( ist, jst, title )
#
#  Get the CCS size.
#
  ncc = st_to_ccs_size ( ist, jst )

  print ( '' )
  print ( '  Number of ST values =  ', nst )
  print ( '  Number of CCS values = ', ncc )
#
#  Create the CCS indices.
#
  icc, ccc = st_to_ccs_index ( ist, jst )
#
#  Create the CCS values.
#
  acc = st_to_ccs_values ( ist, jst, ast, icc, ccc )
#
#  Write the CCS matrix.
#
  ccs_write ( prefix, icc, ccc, acc )

  return

def st_to_ccs_test04 ( ):

#*****************************************************************************80
#
## st_to_ccs_test04() works with a CCS sparse matrix with repeated index pairs.
#
#  Discussion:
#
#    To complete this test, I want to compare AST * X and ACC * X.
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
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'st_to_ccs_test04():' )
  print ( '  Convert a sparse matrix from ST to CCS format.' )
  print ( '  ST:  sparse triplet,    I, J,  A.' )
  print ( '  CCS: compressed column, I, CC, A.' )
  print ( '  The ST matrix is the Wathen finite element matrix.' )
  print ( '  It has many repeated index pairs.' )
  print ( '  To check, compare ACC*X - AST*X for a random X.' )
#
#  Get the size of the ST matrix.
#
  nx = 3
  ny = 3
  nst = wathen_st_size ( nx, ny )
#
#  Set the formal matrix size
#
  m = 3 * nx * ny + 2 * nx + 2 * ny + 1
  n = m
  print ( '  Number of rows and columns N = ', n )
#
#  Set a random vector.
#
  x = rng.random ( size = n )
#
#  Create the ST matrix.
#
  print ( '  NX = ', nx )
  print ( '  NY = ', ny )
  print ( '  NST = ', nst )

  ist, jst, ast = wathen_st ( nx, ny )
#
#  Print the ST matrix.
#
  title = 'The ST matrix:'
  st_header_print ( ist, jst, title )
  st_print ( ist, jst, ast, title )
#
#  Compute B1 = AST * X
#
  b1 = st_mv ( ist, jst, ast, x )
#
#  Get the CCS size.
#
  ncc = st_to_ccs_size ( ist, jst )

  print ( '' )
  print ( '  Number of ST values =  ', nst )
  print ( '  Number of CCS values = ', ncc )
#
#  Create the CCS indices.
#
  icc, ccc = st_to_ccs_index ( ist, jst )
#
#  Create the CCS values.
#
  acc = st_to_ccs_values ( ist, jst, ast, icc, ccc )
#
#  Debug: print the CCS matrix.
#
  title = 'CCS matrix:'
  ccs_print ( icc, ccc, acc, title )
#
#  Compute B2 = ACC * X.
#
  b2 = ccs_mv ( m, n, ncc, icc, ccc, acc, x )
#
#  Compare B1 and B2.
#
  r = np.linalg.norm ( b1 - b2 )
  print ( '  | ACC*X - AST*X| = ', r )

  return

def st_to_ccs_values ( ist, jst, ast, icc, ccc ):

#*****************************************************************************80
#
## st_to_ccs_values() creates CCS values from ST data.
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
#    integer IST(NST), JST(NST), the ST rows and columns.
#
#    real AST(NST), the ST values.
#
#    integer ICC(NCC), the CCS rows.
#
#    integer CCC(N+1), the CCS compressed columns.
#
#  Output:
#
#    real ACC(NCC), the CCS values.
#
  import numpy as np

  nst = len ( ist )
  ncc = len ( icc )
  n = len ( ccc ) - 1
  acc = np.zeros ( ncc )

  for kst in range ( 0, nst ):

    i = ist[kst]
    j = jst[kst]

    clo = ccc[j]
    chi = ccc[j+1]

    fail = True

    for kcc in range ( clo, chi ):
      if ( icc[kcc] == i ):
        acc[kcc] = acc[kcc] + ast[kst]
        fail = False
        break

    if ( fail ):
      print ( '' )
      print ( 'st_to_ccs_values(): Fatal error!' )
      print ( '  ST entry cannot be located in CCS array.' )
      print ( '  ST index KST    =', kst )
      print ( '  ST row IST(KST) =', ist[kst] )
      print ( '  ST col JST(KST) =', jst[kst] )
      print ( '  ST val AST(KST) =', ast[kst] )
      raise Exception ( 'st_to_ccs_values(): Fatal error!' )

  return acc

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

def wathen_st ( nx, ny ):

#*****************************************************************************80
#
## wathen_st(): Wathen matrix stored in sparse triplet format.
#
#  Discussion:
#
#    When dealing with sparse matrices, it can be much more efficient
#    to work first with a triple of I, J, and X vectors, and only once
#    they are complete, convert to MATLAB's sparse format.
#
#    The Wathen matrix is a finite element matrix which is sparse.
#
#    The entries of the matrix depend in part on a physical quantity
#    related to density.  That density is here assigned random values between
#    0 and 100.
#
#    The matrix order N is determined by the input quantities NX and NY,
#    which would usually be the number of elements in the X and Y directions.
#
#    The value of N is
#
#      N = 3*NX*NY + 2*NX + 2*NY + 1,
#
#    The matrix is the consistent mass matrix for a regular NX by NY grid
#    of 8 node serendipity elements.
#
#    The local element numbering is
#
#      3--2--1
#      |     |
#      4     8
#      |     |
#      5--6--7
#
#    Here is an illustration for NX = 3, NY = 2:
#
#     23-24-25-26-27-28-29
#      |     |     |     |
#     19    20    21    22
#      |     |     |     |
#     12-13-14-15-16-17-18
#      |     |     |     |
#      8     9    10    11
#      |     |     |     |
#      1--2--3--4--5--6--7
#
#    For this example, the total number of nodes is, as expected,
#
#      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#    The matrix is symmetric positive definite for any positive values of the
#    density RHO(X,Y).
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
#    John Burkardt.
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#  Output:
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices 
#    of the nonzero entries.
#
#    real A(NZ_NUM), the nonzero values.
#
  import numpy as np

  nz_num = wathen_st_size ( nx, ny )

  em = np.array \
  ( \
    ( ( 6.0, -6.0,  2.0, -8.0,  3.0, -8.0,  2.0, -6.0 ), \
      (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0 ), \
      ( 2.0, -6.0,  6.0, -6.0,  2.0, -8.0,  3.0, -8.0 ), \
      (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0 ), \
      ( 3.0, -8.0,  2.0, -6.0,  6.0, -6.0,  2.0, -8.0 ), \
      (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0 ), \
      ( 2.0, -8.0,  3.0, -8.0,  2.0, -6.0,  6.0, -6.0 ), \
      (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0 ) )\
  )

  node = np.zeros ( 8, dtype = np.int32 )
  row = np.zeros ( nz_num, dtype = np.int32 )
  col = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num )

  k = 0

  for j in range ( 1, ny + 1 ):

    for i in range ( 1, nx + 1 ):

      node[0] = 3 * j * nx + 2 * i + 2 * j + 1
      node[1] = node[0] - 1
      node[2] = node[1] - 1
      node[3] = ( 3 * j - 1 ) * nx + 2 * j + i - 1
      node[4] = 3 * ( j - 1 ) * nx + 2 * i + 2 * j - 3
      node[5] = node[4] + 1
      node[6] = node[5] + 1
      node[7] = node[3] + 1

      rho = 50.0

      for krow in range ( 0, 8 ):
        for kcol in range ( 0, 8 ):
          row[k] = node[krow] - 1
          col[k] = node[kcol] - 1
          a[k] = rho * em[krow,kcol]
          k = k + 1

  return row, col, a

def wathen_st_size ( nx, ny ):

#*****************************************************************************80
#
## wathen_st_size(): Size of Wathen matrix stored in sparse triplet format.
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
#    John Burkardt.
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#  Output:
#
#    integer NZ_NUM, the number of items of data.
#
  nz_num = nx * ny * 64

  return nz_num

if ( __name__ == "__main__" ):
  timestamp ( )
  st_to_ccs_test ( )
  timestamp ( )

