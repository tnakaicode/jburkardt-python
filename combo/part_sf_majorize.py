#! /usr/bin/env python
#
def part_sf_majorize ( n, nparta, a, npartb, b ):

#*****************************************************************************80
#
## PART_SF_MAJORIZE determines if partition A majorizes partition B.
#
#  Discussion:
#
#    The partitions must be in standard form.
#
#    If A, with NPARTA parts, and B, with NPARTB parts, are both partitions
#    of the same positive integer N, then we say that A majorizes B if,
#    for every index K from 1 to N, it is true that
#
#      sum ( 1 <= I <= K ) B(I) <= sum ( 1 <= I <= K ) A(I)
#
#    where entries of A beyond index NPARTA, and of B beyond BPARTB
#    are assumed to be 0.  We say that A strictly majorizes B if
#    A majorizes B, and for at least one index K the inequality is strict.
#
#    For any two partitions of N, it is possible that A majorizes B,
#    B majorizes A, both partitions majorize each other (in which case
#    they are equal), or that neither majorizes the other.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jack vanLint, Richard Wilson,
#    A Course in Combinatorics,
#    Cambridge, 1992,
#    ISBN: 0-521-42260-4,
#    LC: QA164.L56.
#
#  Parameters:
#
#    Input, integer N, the integer to be partitioned.
#    N must be positive.
#
#    Input, integer NPARTA, the number of parts in partition A.
#    1 <= NPARTA <= N.
#
#    Input, integer A(NPARTA), contains partition A in standard
#    form.  A(1) through A(NPARTA) contain nonzero integers which sum to N.
#
#    Input, integer NPARTB, the number of parts in partition B.
#    1 <= NPARTB <= N.
#
#    Input, integer B(NPARTB), contains partition B in standard
#    form.  B(1) through B(NPARTB) contain nonzero integers which sum to N.
#
#    Output, integer RESULT, the result of the comparison.
#    -2, A and B are incomparable, would have been -1.
#    -1, A < B, (A is strictly majorized by B),
#     0, A = B, (A and B are identical),
#    +1, A > B, (A strictly majorizes B),
#    +2, A and B are incomparable, would have been +1.
#
  from sys import exit
  from part_sf_check import part_sf_check
#
#  Check.
#
  check = part_sf_check ( n, nparta, a )

  if ( not check ):
    print ( '' )
    print ( 'PART_SF_MAJORIZE - Fatal error!' )
    print ( '  The input array A is illegal.' )
    exit ( 'PART_SF_MAJORIZE - Fatal error!' )

  check = part_sf_check ( n, npartb, b )

  if ( not check ):
    print ( '' )
    print ( 'PART_SF_MAJORIZE - Fatal error!' )
    print ( '  The input array B is illegal.' )
    exit ( 'PART_SF_MAJORIZE - Fatal error!' )
 
  result = 0
  suma = 0
  sumb = 0

  for i in range ( 0, min ( nparta, npartb ) ):

    suma = suma + a[i]
    sumb = sumb + b[i]

    if ( result == -1 ):

      if ( sumb < suma ):
        result = -2
        return result

    elif ( result == 0 ):

      if ( suma < sumb ):
        result = -1
      elif ( sumb < suma ):
        result = +1

    elif ( result == + 1 ):

      if ( suma < sumb ):
        result = +2
        return result

  return result

def part_sf_majorize_test ( ):

#*****************************************************************************80
#
## PART_SF_MAJORIZE_TEST tests PART_SF_MAJORIZE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 8

  a = np.array ( [ 2, 2, 2, 1, 1, 0, 0, 0 ] )
  b = np.array ( [ 3, 1, 1, 1, 1, 1, 0, 0 ] )
  c = np.array ( [ 2, 2, 1, 1, 1, 1, 0, 0 ] )
  nparta = 5
  npartb = 6
  npartc = 6

  print ( '' )
  print ( 'PART_SF_MAJORIZE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PART_SF_MAJORIZE determines if one partition' )
  print ( '  majorizes another.' )
  print ( '' )
  print ( '  Partitions of N = %d' % ( n ) )
  print ( '' )

  i4vec_transpose_print ( nparta, a, '  A:' )
  i4vec_transpose_print ( npartb, b, '  B:' )
  i4vec_transpose_print ( npartc, c, '  C:' )

  result = part_sf_majorize ( n, nparta, a, npartb, b )
  print ( '' )
  print ( '  A compare B: %d' % ( result ) )
  result = part_sf_majorize ( n, npartb, b, npartc, c )
  print ( '  B compare C: %d' % ( result ) )
  result = part_sf_majorize ( n, npartc, c, nparta, a )
  print ( '  C compare A: %d' % ( result ) )
  result = part_sf_majorize ( n, npartc, c, npartc, c )
  print ( '  C compare C: %d' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PART_SF_MAJORIZE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  part_sf_majorize_test ( )
  timestamp ( )
 
