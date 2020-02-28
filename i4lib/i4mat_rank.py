#! /usr/bin/env python
#
def i4mat_rank ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_RANK computes the rank of an I4MAT.
#
#  Discussion:
#
#    Because this function assumes the input matrix contains only integer
#    values, it is possible to report the matrix rank without any fear
#    of roundoff error producing an incorrect result.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the matrix to be analyzed. 
#
#    Output, integer RANK_A, the rank of the matrix.
#    0 <= RANK_A <= min ( M, N ).
#
  from sys import exit
  from i4mat_is_integer import i4mat_is_integer
  from i4vec_red import i4vec_red

  if ( not i4mat_is_integer ( m, n, a ) ):
    print ( '' )
    print ( 'I4MAT_REF - Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    exit ( 'I4MAT_REF - Fatal error!' )

  lead = 0
  rank_a = 0
 
  for r in range ( 0, m ):

    if ( n <= lead ):
      break
#
#  Start I at row R, and search for nonzero pivot entry A(I,LEAD).
#
    i = r

    while ( a[i,lead] == 0 ):

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
#  Increase rank by 1.
#
    rank_a = rank_a + 1
#
#  Move pivot I into row R.
#
    if ( i != r ):
      temp     = a[i,0:n]
      a[i,0:n] = a[r,0:n]
      a[r,0:n] = temp
#
#  Ensure pivot is positive.
#
    if ( a[r,lead] < 0 ):
      a[r,0:n] = - a[r,0:n]
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

  return rank_a

def i4mat_rank_test ( ):

#*****************************************************************************80
#
## I4MAT_RANK_TEST tests I4MAT_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4MAT_RANK_TEST' )
  print ( '  I4MAT_RANK computes the rank of an integer matrix.' )

  m = 3
  n = 3
  a1 = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ], \
    [ 7, 8, 9 ] ] )

  i4mat_print ( m, n, a1, '  Matrix A1:' )

  rank_a = i4mat_rank ( m, n, a1 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 3
  n = 3
  a2 = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ], \
    [ 7, 8, 0 ] ] )

  i4mat_print ( m, n, a2, '  Matrix A2:' )

  rank_a = i4mat_rank ( m, n, a2 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 4
  n = 3
  a3 = np.array ( [ \
    [  1,  2,  3 ], \
    [  4,  5,  6 ], \
    [  7,  8,  0 ], \
    [ 10, 11, 12 ] ] )

  i4mat_print ( m, n, a3, '  Matrix A3:' )

  rank_a = i4mat_rank ( m, n, a3 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 3
  n = 4
  a4 = np.array ( [ \
    [ 1, 2, 3, 7 ], \
    [ 4, 5, 6, 8 ], \
    [ 7, 8, 0, 3 ] ] )

  i4mat_print ( m, n, a4, '  Matrix A4:' )

  rank_a = i4mat_rank ( m, n, a4 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 5
  n = 3
  a5 = np.array ( [ \
    [  1,  2,  3 ], \
    [  4,  5,  6 ], \
    [  7,  8,  9 ], \
    [ 10, 11, 12  ], \
    [  3,  3,  3 ] ] )

  i4mat_print ( m, n, a5, '  Matrix A5:' )

  rank_a = i4mat_rank ( m, n, a5 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )

  m = 3
  n = 2
  a6 = np.array ( [ \
    [ 0,  0 ], \
    [ 0,  0 ], \
    [ 0,  0 ] ] )

  i4mat_print ( m, n, a6, '  Matrix A6:' )

  rank_a = i4mat_rank ( m, n, a6 )

  print ( '' )
  print ( '  The rank is %d' % ( rank_a ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_RANK_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_rank_test ( )
  timestamp ( )

