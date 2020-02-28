#! /usr/bin/env python
#
def gray_next ( n, change, k, a ):

#*****************************************************************************80
#
## GRAY_NEXT generates the next Gray code by switching one item at a time.
#
#  Discussion:
#
#    On the first call only, the user must set CHANGE = -N.
#    This initializes the routine to the Gray code for N zeroes.
#
#    Each time it is called thereafter, it returns in CHANGE the index
#    of the item to be switched in the Gray code.  The sign of CHANGE
#    indicates whether the item is to be added or subtracted (or
#    whether the corresponding bit should become 1 or 0).  When
#    CHANGE is equal to N+1 on output, all the Gray codes have been
#    generated.
#
#  Example:
#
#    N  CHANGE         Subset in/out   Binary Number
#                      Interpretation  Interpretation
#                       1 2 4 8
#   --  ---------      --------------  --------------
#
#    4   -4 / 0         0 0 0 0         0
#
#        +1             1 0 0 0         1
#          +2           1 1 0 0         3
#        -1             0 1 0 0         2
#            +3         0 1 1 0         6
#        +1             1 1 1 0         7
#          -2           1 0 1 0         5
#        -1             0 0 1 0         4
#              +4       0 0 1 1        12
#        +1             1 0 1 1        13
#          +2           1 1 1 1        15
#        -1             0 1 1 1        14
#            -3         0 1 0 1        10
#        +1             1 1 0 1        11
#          -2           1 0 0 1         9
#        -1             0 0 0 1         8
#              -4       0 0 0 0         0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the order of the total set from which
#    subsets will be drawn.
#
#    Input, integer CHANGE.  This is an input item only
#    on the first call for a particular sequence of Gray codes,
#    at which time it must be set to -N.  This corresponds to
#    all items being excluded, or all bits being 0, in the Gray code.
#
#    Output, integer CHANGE, indicates which of the N items must be
#    "changed", and the sign indicates whether the item is to be added
#    or removed (or the bit is to become 1 or 0).  Note that on return
#    from the first call only, CHANGE has the value 0, indicating
#    that the first set is the empty set, or the number 0.
#
#    Input/output, integer K, a bookkeeping variable.
#    The user must declare this variable before the first call.
#    The output value from one call should be the input value for the next.
#    The user should not change this variable.
#
#    Input/output, integer A(N), a bookkeeping variable.
#    The user must declare this variable before the first call.
#    The output value from one call should be the input value for the next.
#    The user should not change this variable.
#
  from sys import exit

  if ( n <= 0 ):
    print ( '' )
    print ( 'GRAY_NEXT - Fatal error!' )
    print ( '  Input value of N <= 0.' )
    exit ( 'GRAY_NEXT - Fatal error!' )

  if ( change == - n ):
    change = 0
    k = 1
    for i in range ( 0, n ):
      a[i] = 0
    return change, k, a
#
#  First determine WHICH item is to be changed.
#
  if ( ( k % 2 ) == 1 ):

    change = 1

  else:

    for i in range ( 0, n ):
      if ( a[i] == 1 ):
        change = i + 2
        break
#
#  Take care of the terminal case CHANGE = N.
#
  if ( change == n + 1 ):
    change = n
#
#  Now determine HOW the item is to be changed.
#
  if ( a[change-1] == 0 ):
    a[change-1] = 1
  elif ( a[change-1] == 1 ):
    a[change-1] = 0
    change = - change
#
#  Update the counter.
#
  k = k + 1
#
#  If the output CHANGE = -N, then we're done.
#
  if ( change == - n ):
    k = 0

  return change, k, a

def gray_next_test ( ):

#*****************************************************************************80
#
## GRAY_NEXT_TEST tests GRAY_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'GRAY_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRAY_NEXT returns the index of the single item' )
  print ( '  to be changed in order to get the next Gray code.' )
  print ( '' )
  print ( '   K  Change  Gray Code' )
  print ( '' )

  n = 4
  change = -n
  k = 0
  a = np.zeros ( n )

  g = np.zeros ( n )

  while ( True ):

    change, k, a = gray_next ( n, change, k, a )

    if ( change == -n ):
      break
    elif ( change == 0 ):
      for i in range ( 0, n ):
        g[i] = 0
    else:
      g[abs(change)-1] = 1 - g[abs(change)-1]

    print ( '  %2d  %6d  ' % ( k, change ) ),
    for i in range ( 0, n ):
      print ( '%d' % ( g[i] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRAY_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_next_test ( )
  timestamp ( )

