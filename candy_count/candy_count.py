#! /usr/bin/env python3
#
def candy_count_test ( ):

#*****************************************************************************80
#
## candy_count_test() tests candy_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'candy_count_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test candy_count().' )

  candy_count_vector_test ( )
  candy_count_matrix_test ( )
  candy_count_box_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'candy_count_test():' )
  print ( '  Normal end of execution.' )

  return

def candy_count_box ( c, l, m, n ):

#*****************************************************************************80
#
## candy_count_box() counts candy types in an LxMxN box.
#
#  Discussion:
#
#    We are given a box of candy containing C distinct types, and
#    asked to report how many of each type there are.
#
#    In this case, the box is an L by M by N matrix represented as A(I,J,K).  
#
#    The box entry in row I, column J, level K will store candy type C, where
#    A(i,j,k) = mod ( I + J + K, C ).
#
#    The effect of this numbering scheme is that the candy type is
#    constant along diagonal lines and sheets.
#
#    The task is to determine, for a given set of C, L, M and N,
#    the number of candies of each type.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer c: the number of types of candy.
#
#    integer l, m, n: the number of rows, columns, and levels in the candy box.
#
#  Output:
#
#    integer counts(c): the number of each type of candy in the box.
#
  import numpy as np
#
#  Do the computation for the first level:
#
  counts_2d = candy_count_matrix ( c, m, n )
#
#  L = LF * C + LR
#
  lf = ( l // c )
  lr = l - lf * c
#
#  Part of the box can be regarded as LF repetitions 
#  of a stack of sheets for which the item in the (K,1,1) position is 
#  successively 1, 2, ..., C.
#
  counts = np.zeros ( c, dtype = int )

  for k in range ( 0, c ):
    counts = counts + lf * np.roll ( counts_2d, k )
#
#  Now there are 0 <= LR < C more sheets, for which the item in the (K,1,1) 
#  position successively is 1, 2, ..., LR.
#  
  for k in range ( 0, lr ):
    counts = counts + np.roll ( counts_2d, k )

  return counts

def candy_count_box_sum ( c, l, m, n ):

#*****************************************************************************80
#
## candy_count_box_sum() counts candy types in an LxMxN box.
#
#  Discussion:
#
#    This function is a "stupid" version of candy_count_box().  Instead of
#    using a formula, it sets up the candy box, and counts items one by one.
#    It is useful as a check of the intelligent version.
#
#    We are given a box of candy containing C distinct types, and
#    asked to report how many of each type there are.
#
#    In this case, the box is an L by M by N matrix represented as A(I,J,K).  
#
#    The box entry in row I, column J, level K will store candy type C, where
#    A(i,j,k) = mod ( I + J + K, C ).
#
#    The effect of this numbering scheme is that the candy type is
#    constant along diagonal lines and sheets.
#
#    The task is to determine, for a given set of C, L, M and N,
#    the number of candies of each type.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer c: the number of types of candy.
#
#    integer l, m, n: the number of rows, columns, and levels in the candy box.
#
#  Output:
#
#    integer counts(c): the number of each type of candy in the box.
#
  import numpy as np

  counts = np.zeros ( c, dtype = int )

  for i in range ( 0, l ):
    for j in range ( 0, m ):
      for k in range ( 0, n ):
        cijk = ( ( i + j + k ) % c )
        counts[cijk] = counts[cijk] + 1

  return counts

def candy_count_box_test ( ):

#*****************************************************************************80
#
## candy_count_box_test() tests candy_count_box().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'candy_count_box_test():' )
  print ( '  candy_count_box() counts candy types in a 3D box.' )
  print ( '  There are LxMxN entries in the box A().' )
  print ( '  There are C candy types.' )
  print ( '  Candy types are assigned cyclically to matrix entries:' )
  print ( '  A(I,J,K) = mod ( i + j + k - 3, c ) + 1' )
  print ( '  Count the number of candies of each type.' )
#
#  Test 1
#
  c = 4
  l = 7
  m = 10
  n = 13
  print ( '' )
  print ( '  Count using candy_count_box()' )
  print ( '' )
  print ( '   C   L   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '   #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_box ( c, l, m, n )
  print ( '  %2d  %2d  %2d  %2d: ' % ( c, l, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %3d' % ( counts[i] ), end = '' )
  print ( '' )

  c = 4
  l = 7
  m = 10
  n = 13
  print ( '' )
  print ( '  Repeat calculation using candy_count_box_sum()' )
  print ( '' )
  print ( '   C   L   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '   #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_box ( c, l, m, n )
  print ( '  %2d  %2d  %2d  %2d: ' % ( c, l, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %3d' % ( counts[i] ), end = '' )
  print ( '' )
#
#  Test 2
#
  c = 5
  l = 12
  m = 13
  n = 19
  print ( '' )
  print ( '  Count using candy_count_box()' )
  print ( '' )
  print ( '   C   L   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '   #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_box ( c, l, m, n )
  print ( '  %2d  %2d  %2d  %2d: ' % ( c, l, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %3d' % ( counts[i] ), end = '' )
  print ( '' )

  c = 5
  l = 12
  m = 13
  n = 19
  print ( '' )
  print ( '  Repeat calculation using candy_count_box_sum()' )
  print ( '' )
  print ( '   C   L   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '   #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_box ( c, l, m, n )
  print ( '  %2d  %2d  %2d  %2d: ' % ( c, l, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %3d' % ( counts[i] ), end = '' )
  print ( '' )

  return

def candy_count_matrix ( c, m, n ):

#*****************************************************************************80
#
## candy_count_matrix() counts candy types in a matrix.
#
#  Discussion:
#
#    We are given a box of candy containing C distinct types, and
#    asked to report how many of each type there are.
#
#    In this case, the box is an M by N matrix represented as A(I,J).  
#    We will assume that rows and columns are indexed by I and J.
#
#    The box entry in row I, column J will store candy type C, where
#    A(i,j) = mod ( I + J, C ).
#
#    The effect of this numbering scheme is that the candy type is
#    constant along diagonal lines.
#
#    The task is to determine, for a given set of C, M and N,
#    the number of candies of each type.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer c: the number of types of candy.
#
#    integer m, n: the number of rows and columns in the candy box.
#
#  Output:
#
#    integer counts(c): the number of each type of candy in the box.
#
  import numpy as np

  counts = np.zeros ( c, dtype = int )

  a = ( m % c )
  b = ( n % c )

  nmin = ( ( m * n - a * b ) // c )

  for i in range ( 0, c ):

    if ( ( i + 1 ) <= a + b - 1 - c ):
      counts[i] = nmin + a + b - c
    elif ( ( i + 1 ) < min ( a, b ) ):
      counts[i] = nmin + ( i + 1 )
    elif ( ( i + 1 ) <= max ( a, b ) ):
      counts[i] = nmin + min ( a, b )
    elif ( ( i + 1 ) < a + b - 1 ):
      counts[i] = nmin + a + b - ( i + 1 )
    else:
      counts[i] = nmin

  return counts

def candy_count_matrix_sum ( c, m, n ):

#*****************************************************************************80
#
## candy_count_matrix_sum() counts candy types in a matrix.
#
#  Discussion:
#
#    This function is a "stupid" version of candy_count_matrix().  Instead of
#    using a formula, it sets up the candy box, and counts items one by one.
#    It is useful as a check of the intelligent version.
#
#    We are given a box of candy containing C distinct types, and
#    asked to report how many of each type there are.
#
#    In this case, the box is an M by N matrix represented as A(I,J).  
#    We will assume that rows and columns are indexed by I and J.
#
#    The box entry in row I, column J will store candy type C, where
#    A(i,j) = mod ( I + J, C ).
#
#    The effect of this numbering scheme is that the candy type is
#    constant along diagonal lines.
#
#    The task is to determine, for a given set of C, M and N,
#    the number of candies of each type.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer c: the number of types of candy.
#
#    integer m, n: the number of rows and columns in the candy box.
#
#  Output:
#
#    integer counts(c): the number of each type of candy in the box.
#
  import numpy as np

  counts = np.zeros ( c, dtype = int )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      cij = ( ( i + j ) % c )
      counts[cij] = counts[cij] + 1

  return counts

def candy_count_matrix_test ( ):

#*****************************************************************************80
#
## candy_count_matrix_test() tests candy_count_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'candy_count_matrix_test():' )
  print ( '  candy_count_matrix() counts candy types in a matrix.' )
  print ( '  There are MxN entries in the matrix A().' )
  print ( '  There are C candy types.' )
  print ( '  Candy types are assigned cyclically to matrix entries:' )
  print ( '  A(I,J) = mod ( i + j - 2, c ) + 1' )
  print ( '  Count the number of candies of each type.' )
#
#  Test 1
#
  c = 4
  m = 10
  n = 13
  print ( '' )
  print ( '  Count using candy_count_matrix()' )
  print ( '' )
  print ( '   C   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '  #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_matrix ( c, m, n )
  print ( '  %2d  %2d  %2d: ' % ( c, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %2d' % ( counts[i] ), end = '' )
  print ( '' )

  c = 4
  m = 10
  n = 13
  print ( '' )
  print ( '  Repeat using candy_count_matrix_sum()' )
  print ( '' )
  print ( '   C   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '  #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_matrix_sum ( c, m, n )
  print ( '  %2d  %2d  %2d: ' % ( c, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %2d' % ( counts[i] ), end = '' )
  print ( '' )
#
#  Test 2
#
  c = 5
  m = 13
  n = 19
  print ( '' )
  print ( '  Count using candy_count_matrix()' )
  print ( '' )
  print ( '   C   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '  #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_matrix ( c, m, n )
  print ( '  %2d  %2d  %2d: ' % ( c, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %2d' % ( counts[i] ), end = '' )
  print ( '' )

  c = 5
  m = 13
  n = 19
  print ( '' )
  print ( '  Repeat using candy_count_matrix_sum()' )
  print ( '' )
  print ( '   C   M   N  ', end = '' )
  for i in range ( 0, c ):
    print ( '  #%d' % ( i ), end = '' )
  print ( '' )
  counts = candy_count_matrix_sum ( c, m, n )
  print ( '  %2d  %2d  %2d: ' % ( c, m, n ), end = '' )
  for i in range ( 0, c ):
    print ( '  %2d' % ( counts[i] ), end = '' )
  print ( '' )

  return

def candy_count_vector ( c, n ):

#*****************************************************************************80
#
## candy_count_vector() counts candy types in a vector.
#
#  Discussion:
#
#    We are given a box of candy containing C distinct types, and
#    asked to report how many of each type there are.
#
#    In this case, the box is a vector, which can hold N items,
#    indexed 0 through N-1.
#
#    The candy types occur in sequence, 0, 1, 2, ..., C-1, and then
#    the types repeat, so the next item is type 0, and so on.
#
#    This version of the problem is simple to understand and solve.
#    The problem is more interesting if the candy is stored in a 
#    rectangular array, or a 3-dimensional box.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer c: the number of types of candy.
#
#    integer n: the number of columns in the candy box.
#
#  Output:
#
#    integer counts(c): the number of each type of candy in the box.
#
  import numpy as np
#
#  N = N_MIN * C + N_REM
#
  n_min = ( n // c )
#
#  Everybody gets at least N_MIN.
#
  counts = n_min * np.ones ( c, dtype = int )
#
#  There are N_REM candies remaining.
#  Give 1 each to types 0 through N_REM-1.
#
  n_rem = n - n_min * c

  counts[0:n_rem] = counts[0:n_rem] + 1

  return counts

def candy_count_vector_sum ( c, n ):

#*****************************************************************************80
#
## candy_count_vector_sum() counts candy types in a vector.
#
#  Discussion:
#
#    This function is a "stupid" version of candy_count_vector().  Instead of
#    using a formula, it sets up the candy box, and counts items one by one.
#    It is useful as a check of the intelligent version.
#
#    We are given a box of candy containing C distinct types, and
#    asked to report how many of each type there are.
#
#    In this case, the box is a vector, which can hold N items,
#    indexed 0 through N-1.
#
#    The candy types occur in sequence, 0, 1, 2, ..., C-1, and then
#    the types repeat, so the next item is type 0, and so on.
#
#    This version of the problem is simple to understand and solve.
#    The problem is more interesting if the candy is stored in a 
#    rectangular array, or a 3-dimensional box.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer c: the number of types of candy.
#
#    integer n: the number of columns in the candy box.
#
#  Output:
#
#    integer counts(c): the number of each type of candy in the box.
#
  import numpy as np

  counts = np.zeros ( c, dtype = int )

  for i in range ( 0, n ):
    ci = ( i % c )
    counts[ci] = counts[ci] + 1

  return counts

def candy_count_vector_test ( ):

#*****************************************************************************80
#
## candy_count_vector_test() tests candy_count_vector().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'candy_count_vector_test():' )
  print ( '  candy_count_vector() counts candy types in a vector.' )
  print ( '  There are N entries in the vector A().' )
  print ( '  There are C candy types.' )
  print ( '  Candy types are assigned cyclically to vector entries:' )
  print ( '  A(i) = mod ( i, c )' )
  print ( '  Count the number of candies of each type.' )

  c = 4
  print ( '' )
  print ( '  Count using candy_count_vector()' )
  print ( '  Fix value of C = ', c )
  print ( '  Consider a range of values of N:' )
  print ( '' )
  print ( '   N    #0  #1  #2  #3' )
  print ( '' )

  for n in range ( 3, 11 ):
    counts = candy_count_vector ( c, n )
    print ( '  %2d: ' % ( n ), end = '' )
    for i in range ( 0, c ):
      print ( '  %2d' % ( counts[i] ), end = '' )
    print ( '' )

  c = 4
  print ( '' )
  print ( '  Repeat calculation, using candy_count_vector_sum()' )
  print ( '  Fix value of C = ', c )
  print ( '  Consider a range of values of N:' )
  print ( '' )
  print ( '   N    #0  #1  #2  #3' )
  print ( '' )

  for n in range ( 3, 11 ):
    counts = candy_count_vector_sum ( c, n )
    print ( '  %2d: ' % ( n ), end = '' )
    for i in range ( 0, c ):
      print ( '  %2d' % ( counts[i] ), end = '' )
    print ( '' )

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
  candy_count_test ( )
  timestamp ( )

