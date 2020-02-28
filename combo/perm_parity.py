#! /usr/bin/env python
#
def perm_parity ( n, p ):

#*****************************************************************************80
#
## PERM_PARITY computes the parity of a permutation.
#
#  Discussion:
#
#    The routine requires the use of a temporary array.
#
#    A permutation is called "even" or "odd", depending on whether
#    it is equivalent to an even or odd number of pairwise 
#    transpositions.  This is known as the "parity" of the 
#    permutation.
#
#    The "sign" of a permutation is +1 if it has even parity,
#    and -1 if it has odd parity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    Output, integer PARITY, the parity of the permutation.
#    0, the permutation has even parity.
#    1, the permutation has odd parity.
#
  import numpy as np
  from perm_check import perm_check
  from sys import exit
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_PARITY - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PERM_PARITY - Fatal error!' )

  a = np.zeros ( n, dtype = np.int32 )

  c = 0

  for j in range ( 1, n + 1 ):

    if ( a[j-1] == 0 ):

      c = c + 1
      a[j-1] = 1
      i = j

      while ( p[i-1] != j ):
        i = p[i-1]
        a[i-1] = 1

  parity = ( ( n - c ) % 2 )

  return parity

def perm_parity_test ( ):

#*****************************************************************************80
#
## PERM_PARITY_TEST tests PERM_PARITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from perm_print import perm_print
  from perm_random import perm_random

  n = 5

  print ( '' )
  print ( 'PERM_PARITY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_PARITY computes the parity of a permutation.' )

  n = 5
  seed = 123456789

  for test in range ( 0, 5 ):
    p, seed = perm_random ( n, seed )
    perm_print ( n, p, '  The permutation P:' )
    parity = perm_parity ( n, p )
    print ( '' )
    print ( '  The parity is %d' % ( parity ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_PARITY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_parity_test ( )
  timestamp ( )
 
