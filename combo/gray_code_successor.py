#! /usr/bin/env python
#
def gray_code_successor ( n, t, rank ):

#*****************************************************************************80
#
## GRAY_CODE_SUCCESSOR computes the binary reflected Gray code successor.
#
#  Example:
#
#    000, 001, 011, 010, 110, 111, 101, 100,
#    after which the sequence repeats.
#
#  Discussion:
#
#    In the original code, the successor of the element that has an
#    initial 1 followed by N-1 zeroes is undefined.  In this version,
#    the successor is the element with N zeroes.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 November 2015
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
#    Input, integer N, the number of digits in each element.
#    N must be positive.
#
#    Input/output, integer T(N).
#    On input, T contains an element of the Gray code, that is,
#    each entry T(I) is either 0 or 1.
#    On output, T contains the successor to the input value this
#    is an element of the Gray code, which differs from the input
#    value in a single position.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  import numpy as np
  from gray_code_check import gray_code_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):

    t = np.zeros ( n )
    rank = 0
    return t, rank
#
#  Check.
#
  check = gray_code_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'GRAY_CODE_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'GRAY_CODE_SUCCESSOR - Fatal error!' )

  weight = np.sum ( t )

  if ( ( weight % 2 ) == 0 ):

    if ( t[n-1] == 0 ):
      t[n-1] = 1
    else:
      t[n-1] = 0

    rank = rank + 1
    return t, rank

  else:

    for i in range ( n - 1, 0, -1 ):
      if ( t[i] == 1 ):
        if ( t[i-1] == 0 ):
          t[i-1] = 1
        else:
          t[i-1] = 0
        rank = rank + 1
        return t, rank
#
#  The final element was input.
#  Return the first element.
#
    t = np.zeros ( n )
    rank = 0

  return t, rank

def gray_code_successor_test ( ):

#*****************************************************************************80
#
## GRAY_CODE_SUCCESSOR_TEST tests GRAY_CODE_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'GRAY_CODE_SUCCESSOR_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRAY_CODE_SUCCESSOR returns the next Gray code.' )

  n = 5
  t = np.zeros ( n )
  rank = -1

  print ( '' )
  while ( True ):

    rank_old = rank

    t, rank = gray_code_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    print ( '    %4d:  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( t[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRAY_CODE_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_code_successor_test ( )
  timestamp ( )
 
