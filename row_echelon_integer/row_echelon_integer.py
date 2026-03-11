#! /usr/bin/env python3
#
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
  import platform

  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ( '' )
  print ( 'i4_gcd_test' )
  print ( '  i4_gcd computes the greatest common factor' )
  print ( '' )
  print ( '     I     J   i4_gcd' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_gcd ( i, j )
    print ( '  %6d  %6d  %6d' % ( i, j, k ) )

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
#    bool VALUE, is true if all entries are integer.
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
  import platform

  print ( '' )
  print ( 'i4mat_is_integer_test' )
  print ( '  i4mat_is_integer is TRUE if every entry of an I4MAT' )
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
  import platform

  print ( '' )
  print ( 'i4mat_print_test:' )
  print ( '  Test i4mat_print, which prints an I4MAT.' )

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
  import platform

  print ( '' )
  print ( 'i4mat_print_some_test' )
  print ( '  i4mat_print_some prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )

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
    print ( 'i4mat_ref - Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    raise Exception ( 'i4mat_ref - Fatal error!' )

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
  import platform

  m = 4
  n = 7

  a = np.array ( [ \
    [  1,  3,  0,  2,  6,  3,  1 ], \
    [ -2, -6,  0, -2, -8,  3,  1 ], \
    [  3,  9,  0,  0,  6,  6,  2 ], \
    [ -1, -3,  0,  1,  0,  9,  3 ] ] )

  print ( '' )
  print ( 'i4mat_ref_test' )
  print ( '  i4mat_ref computes the integer row echelon form of an I4MAT.' )

  i4mat_print ( m, n, a, '  Input A:' )

  a, det = i4mat_ref ( m, n, a )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a, '  IREF of A:' )

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
  import platform

  print ( '' )
  print ( 'i4mat_row_swap_test:' )
  print ( '  i4mat_row_swap swaps two rows in an I4MAT.' )

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
    print ( 'i4mat_ref - Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    raise Exception ( 'i4mat_ref - Fatal error!' )

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
  import platform

  m = 4
  n = 7

  a = np.array ( [ \
    [  1,  3,  0,  2,  6,  3,  1 ], \
    [ -2, -6,  0, -2, -8,  3,  1 ], \
    [  3,  9,  0,  0,  6,  6,  2 ], \
    [ -1, -3,  0,  1,  0,  9,  3 ] ] )

  print ( '' )
  print ( 'i4mat_rref_test' )
  print ( '  i4mat_rref computes the integer reduced row echelon form (IREF)' )
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

      if ( i4vec_is_binary ( n, y ) ):
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
  import platform

  print ( '' )
  print ( 'i4mat_rref_solve_binary_nz_test:' )
  print ( '  i4mat_rref_solve_binary_nz seeks binary solutions of' )
  print ( '  an Integer Row-Reduced Echelon Form (IRREF) system A*x=b' )
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

    if ( i4vec_is_binary ( n, y ) ):
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
  import platform

  print ( '' )
  print ( 'i4mat_rref_solve_binary_test:' )
  print ( '  i4mat_rref_solve_binary seeks binary solutions of' )
  print ( '  an Integer Row-Reduced Echelon Form (IRREF) system A*x=b' )
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
#    bool INCON, is TRUE if the system A*X=B is inconsistent.
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
  import platform

  print ( '' )
  print ( 'i4mat_rref_system_test' )
  print ( '  i4mat_rref_system computes the linear system associated' )
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
  import platform

  n = 4

  a = np.array ( [ \
    [ 1.0,  2.0,  4.0,  7.0 ], \
    [ 0.0,  3.0,  5.0,  8.0 ], \
    [ 0.0,  0.0,  6.0,  9.0 ], \
    [ 0.0,  0.0,  0.0, 10.0 ] ] )

  b = np.array ( [ 45.0, 53.0, 54.0, 40.0 ] )

  print ( '' )
  print ( 'i4mat_u_solve_test' )
  print ( '  i4mat_u_solve solves an upper triangular system.' )

  i4mat_print ( n, n, a, '  Input matrix A:' )

  i4vec_print ( n, b, '  Right hand side b:' )

  x = i4mat_u_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )

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
  import platform

  n = 3

  print ( '' )
  print ( 'i4vec_binary_next_test' )
  print ( '  i4vec_binary_next generates the next binary vector.' )
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
  import platform

  print ( '' )
  print ( 'i4vec_identity_row_test' )
  print ( '  i4vec_identity_row returns a row of the identity matrix.' )
  print ( '' )

  n = 5
  for i in range ( -1, 6 ):
    a = i4vec_identity_row ( n, i )
    print ( '%2d: ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( ' %d' % ( a[j] ), end = '' )
    print ( '' )

  return

def i4vec_is_binary ( n, x ):

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
#    integer X(N), the vector to be compared against.
#
#  Output:
#
#    bool i4vec_is_binary, is true (1) if X only contains
#    0 or 1 entries.
#
  value = True

  for i in range ( 0, n ):

    if ( x[i] != 0 and x[i] != 1 ):
      value = False
      break

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
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_is_binary_test' )
  print ( '  i4vec_is_binary is TRUE if an I4VEC only contains' )
  print ( '  0 or 1 entries.' )

  n = 3

  x = np.array ( [ 0, 0, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 1, 0, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

  x = np.array ( [ 0, 2, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_binary ( n, x ) ):
    print ( '  X is binary' )
  else:
    print ( '  X is NOT binary.' )

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
  print ( 'i4vec_print_test' )
  print ( '  i4vec_print prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

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
#    On the entries of A have no common factor
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
  import platform

  print ( '' )
  print ( 'i4vec_red_test' )
  print ( '  i4vec_red divides out any common factors in the' )
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
  import platform

  print ( '' )
  print ( 'i4vec_transpose_print_test' )
  print ( '  i4vec_transpose_print prints an I4VEC' )
  print ( '  with 5 entries to a row, and an optional title.' )

  n = 12
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  print ( '' )
  i4vec_transpose_print ( n, a, '  My array:  ' )

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
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'ksub_next4_test' )
  print ( '  ksub_next4 generates K subsets of an N set.' )
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

def r8vec_is_integer ( n, x ):

#*****************************************************************************80
#
## r8vec_is_integer() is true if every entry is an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
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
#    bool VALUE, is true if all entries are integers.
#
  import numpy as np

  value = np.all ( x[0:n] == np.round ( x[0:n] ) )

  return value

def r8vec_is_integer_test ( ):

#*****************************************************************************80
#
## r8vec_is_integer_test() tests r8vec_is_integer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_is_integer_test' )
  print ( '  r8vec_is_integer is TRUE if an R8VEC contains' )
  print ( '  only integer entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  x = np.array ( [ 1.0, 2.5, 3.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

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
  import platform

  n = 11

  print ( '' )
  print ( 'r8vec_transpose_print_test' )
  print ( '  r8vec_transpose_print() prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x = np.array ( [ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 ] )

  r8vec_transpose_print ( n, x, '  The vector X:' )

  return

def row_echelon_integer_test ( ):

#*****************************************************************************80
#
## row_echelon_integer_test() tests row_echelon_integer().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'row_echelon_integer_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test the row_echelon_integer().' )

  i4_gcd_test ( )

  i4mat_is_integer_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4mat_ref_test ( )
  i4mat_row_swap_test ( )
  i4mat_rref_test ( )
  i4mat_rref_solve_binary_test ( )
  i4mat_rref_solve_binary_nz_test ( )
  i4mat_rref_system_test ( )
  i4mat_u_solve_test ( )

  i4vec_binary_next_test ( )
  i4vec_identity_row_test ( )
  i4vec_is_binary_test ( )
  i4vec_print_test ( )
  i4vec_red_test ( )

  ksub_next4_test ( )

  r8vec_is_integer_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'row_echelon_integer_test():' )
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
  row_echelon_integer_test ( )
  timestamp ( )

