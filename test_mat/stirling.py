#! /usr/bin/env python
#
def stirling ( m, n ):

#*****************************************************************************80
#
## STIRLING returns the STIRLING matrix.
#
#  Comments:
#
#    The absolute value of the Stirling number S1(I,J) gives the number
#    of permutations on I objects having exactly J cycles, while the
#    sign of the Stirling number records the sign (odd or even) of
#    the permutations.  For example, there are six permutations on 3 objects:
#
#      A B C   3 cycles (A) (B) (C)
#      A C B   2 cycles (A) (BC)
#      B A C   2 cycles (AB) (C)
#      B C A   1 cycle  (ABC)
#      C A B   1 cycle  (ABC)
#      C B A   2 cycles (AC) (B)
#
#    There are
#
#      2 permutations with 1 cycle, and S1(3,1) = 2
#      3 permutations with 2 cycles, and S1(3,2) = -3,
#      1 permutation with 3 cycles, and S1(3,3) = 1.
#
#    Since there are N! permutations of N objects, the sum of the absolute
#    values of the Stirling numbers in a given row,
#
#      sum ( 1 <= J <= I ) abs ( S1(I,J) ) = N!
#
#  First terms:
#
#    I/J:  1     2      3     4     5    6    7    8
#
#    1     1     0      0     0     0    0    0    0
#    2    -1     1      0     0     0    0    0    0
#    3     2    -3      1     0     0    0    0    0
#    4    -6    11     -6     1     0    0    0    0
#    5    24   -50     35   -10     1    0    0    0
#    6  -120   274   -225    85   -15    1    0    0
#    7   720 -1764   1624  -735   175  -21    1    0
#    8 -5040 13068 -13132  6769 -1960  322  -28    1
#
#  Recursion:
#
#    S1(I,1) = (-1)^(I-1) * (I-1)! for all I.
#    S1(I,I) = 1 for all I.
#    S1(I,J) = 0 if I < J.
#
#    S1(I,J) = S1(I-1,J-1) - (I-1) * S1(I-1,J)
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is lower triangular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    After row 1, each row sums to 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) );
  
  a[0,0] = 1.0

  for i in range ( 1, m ):

    a[i,0] = - float ( i ) * a[i-1,0]

    for j in range ( 1, n ):
      a[i,j] = a[i-1,j-1] - float ( i ) * a[i-1,j]

  return a

def stirling_determinant ( n ):

#*****************************************************************************80
#
## STIRLING_DETERMINANT computes the determinant of the STIRLING matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def stirling_determinant_test ( ):

#*****************************************************************************80
#
## STIRLING_DETERMINANT_TEST tests STIRLING_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from stirling import stirling
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'STIRLING_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STIRLING_DETERMINANT computes the STIRLING determinant.' )

  m = 5
  n = m
 
  a = stirling ( m, n )

  r8mat_print ( m, n, a, '  STIRLING matrix:' )

  value = stirling_determinant ( n )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STIRLING_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def stirling_inverse ( n ):

#*****************************************************************************80
#
#% STIRLING_INVERSE returns the inverse of the STIRLING matrix.
#
#  Comments:
#
#    The inverse of S1, the matrix of Stirling numbers of the first kind,
#    is S2, the matrix of Stirling numbers of the second kind.
#
#    S2(I,J) represents the number of distinct partitions of I elements
#    into J nonempty sets.  For any I, the sum over J of the Stirling
#    numbers S2(I,J) is represented by B(I), called "Bell's number",
#    and represents the number of distinct partitions of I elements.
#
#    For example, with 4 objects, there are:
#
#    1 partition into 1 set:
#
#      (A,B,C,D)
#
#    7 partitions into 2 sets:
#
#      (A,B,C) (D)
#      (A,B,D) (C)
#      (A,C,D) (B)
#      (A) (B,C,D)
#      (A,B) (C,D)
#      (A,C) (B,D)
#      (A,D) (B,C)
#
#    6 partitions into 3 sets:
#
#      (A,B) (C) (D)
#      (A) (B,C) (D)
#      (A) (B) (C,D)
#      (A,C) (B) (D)
#      (A,D) (B) (C)
#      (A) (B,D) (C)
#
#    1 partition into 4 sets:
#
#      (A) (B) (C) (D)
#
#    So S2(4,1) = 1, S2(4,2) = 7, S2(4,3) = 6, S2(4,4) = 1, and B(4) = 15.
#
#
#  First terms:
#
#    I/J: 1    2    3    4    5    6    7    8
#
#    1    1    0    0    0    0    0    0    0
#    2    1    1    0    0    0    0    0    0
#    3    1    3    1    0    0    0    0    0
#    4    1    7    6    1    0    0    0    0
#    5    1   15   25   10    1    0    0    0
#    6    1   31   90   65   15    1    0    0
#    7    1   63  301  350  140   21    1    0
#    8    1  127  966 1701 1050  266   28    1
#
#  Recursion:
#
#    S2(I,1) = 1 for all I.
#    S2(I,I) = 1 for all I.
#    S2(I,J) = 0 if I < J.
#
#    S2(I,J) = J * S2(I-1,J) + S2(I-1,J-1)
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is lower triangular.
#
#    A is nonnegative.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the  matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  for i in range ( 1, n ):

    a[i,0] = 1.0

    for j in range ( 1, n ):
      a[i,j] = float ( j + 1 ) * a[i-1,j] + a[i-1,j-1]

  return a

def stirling_test ( ):

#*****************************************************************************80
#
## STIRLING_TEST tests STIRLING.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'STIRLING_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STIRLING computes the STIRLING matrix.' )

  m = 5
  n = m

  a = stirling ( m, n )
 
  r8mat_print ( m, n, a, '  STIRLING matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'STIRLING_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  stirling_test ( )
  timestamp ( )
 
