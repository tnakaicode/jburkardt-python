#! /usr/bin/env python
#
def perm0_to_ytb ( n, p ):

#*****************************************************************************80
#
## PERM0_TO_YTB converts a permutation of (0,...,N-1) to a Young tableau.
#
#  Discussion
#
#    The mapping is not invertible.  In most cases, several permutations
#    correspond to the same tableau.
#
#  Example
#
#    N = 7
#    P = 6 1 3 0 4 2 5
#
#    YTB =
#      1 2 3 6
#      4 5
#      7
#
#    LAM = 4 2 1 0 0 0 0
#
#    A = 1 1 1 2 2 1 3
#
#  Licensing
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified
#
#    16 June 2015
#
#  Author
#
#    John Burkardt
#
#  Reference
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters
#
#    Input, integer N, the integer to be partitioned.
#
#    Input, integer P(N), a permutation, in standard index form.
#
#    Output, integer LAM(N).  LAM(I) is the length of the I-th row.
#
#    Output, integer A(N).  A(I) is the row containing I.
#
  import numpy as np
#
#  Initialize.
#
  lam = np.zeros ( n )
  a = np.zeros ( n )
  for i in range ( 0, n):
    a[i] = -1
#
#  Insert each item of the permutation.
#
  for put_index in range ( 0, n ):

    put_value = p[put_index]
    put_row = 0

    while ( True ):

      another = False

      for compare in range ( put_value + 1, n ):

        if ( a[compare] == put_row ):
          another = True
          a[put_value] = put_row
          a[compare] = -1
          put_value = compare
          put_row = put_row + 1
          break

      if ( not another ):
        break

    a[put_value] = put_row
    lam[put_row] = lam[put_row] + 1
#
#  YTB is still 1-based, so add 1 to A values.
#
  for i in range ( 0, n ):
    a[i] = a[i] + 1

  return lam, a

def perm0_to_ytb_test ( ):

#*****************************************************************************80
#
## PERM0_TO_YTB_TEST tests PERM0_TO_YTB.
#
#  Licensing
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified
#
#    16 June 2015
#
#  Author
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm0_print import perm0_print
  from ytb_print import ytb_print

  n = 7
  p = np.array ( [ 6, 1, 3, 0, 4, 2, 5 ] )

  print ( '' )
  print ( 'PERM0_TO_YTB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_TO_YTB converts a permutation to a' )
  print ( '  Young tableau.' )

  perm0_print ( n, p, '  The permutation' )
 
  lam, a = perm0_to_ytb ( n, p )

  ytb_print ( n, a, '  The Young tableau' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_TO_YTB_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_to_ytb_test ( )
  timestamp ( )
