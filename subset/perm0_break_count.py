#! /usr/bin/env python
#
def perm0_break_count ( n, p ):

#*****************************************************************************80
#
## PERM0_BREAK_COUNT counts breaks in a permutation of (0,...,N-1).
#
#  Discussion:
#
#    We begin with a permutation of order N.  We prepend an element
#    labeled "-1" and append an element labeled "N".  There are now
#    N+1 pairs of neighbors.  A "break" is a pair of neighbors whose
#    value differs by more than 1.  
#
#    The identity permutation has a break count of 0.  The maximum
#    break count is N+1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the permutation.
#
#    Input, integer P(N), a permutation, in standard index form.
#
#    Output, integer BREAK_COUNT, the number of breaks in the permutation.
#
  from perm0_check import perm0_check
  from sys import exit

  break_count = 0
#
#  Make sure the permutation is a legal one.
#  (This is not an efficient way to do so!)
#
  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_BREAK_COUNT - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_BREAK_COUNT - Fatal error!' )

  if ( p[0] != 0 ):
    break_count = break_count + 1

  for i in range ( 0, n - 1 ):
    if ( abs ( p[i+1] - p[i] ) != 1 ):
      break_count = break_count + 1

  if ( p[n-1] != n - 1 ):
    break_count = break_count + 1

  return break_count

def perm0_break_count_test ( ):

#*****************************************************************************80
#
## PERM0_BREAK_COUNT_TEST tests PERM0_BREAK_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm0_print import perm0_print

  n = 6
  p = np.array ( [ 3, 4, 1, 0, 5, 2 ] )

  print ( '' )
  print ( 'PERM0_BREAK_COUNT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_BREAK_COUNT counts the breaks in a permutation.' )
 
  perm0_print ( n, p, '  The permutation:' )
 
  break_count = perm0_break_count ( n, p )

  print ( '' )
  print ( '  The number of breaks is %d' % ( break_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_BREAK_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_break_count_test ( )
  timestamp ( )

