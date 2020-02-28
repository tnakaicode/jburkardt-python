#! /usr/bin/env python
#
def pruefer_successor ( n, p, rank ):

#*****************************************************************************80
#
## PRUEFER_SUCCESSOR computes the lexical Pruefer sequence successor.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
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
#    Input, integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    Input/output, integer P(N-2), on input, the Pruefer code for a tree.
#    and on output, its lexical successor.
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
  from pruefer_check import pruefer_check 
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    p = np.ones ( n - 2, dtype = np.int32 )
    rank = 0
    return p, rank
#
#  Check.
#
  check = pruefer_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PRUEFER_SUCCESSOR - Fatal error!' )
    print ( '  Input array is illegal.' )
    exit ( 'PRUEFER_SUCCESSOR - Fatal error!' )

  j = n - 3

  while ( True ):

    if ( p[j] != n ):
      break

    j = j - 1

    if ( j <= -1 ):
      break

  if ( j != -1 ):
    p[j] = p[j] + 1
    for i in range ( j + 1, n - 2 ):
      p[i] = 1
    rank = rank + 1
  else:
    p = np.ones ( n - 2, dtype = np.int32 )
    rank = 0

  return p, rank

def pruefer_successor_test ( ):

#*****************************************************************************80
#
## PRUEFER_SUCCESSOR_TEST tests PRUEFER_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'PRUEFER_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PRUEFER_SUCCESSOR lists Pruefer codes.' )
  print ( '' )

  p = np.zeros ( n - 2, dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    p, rank = pruefer_successor ( n, p, rank )

    if ( rank <= rank_old ):
      break

    print ( '  %3d  ' % ( rank ), end = '' )
    for i in range ( 0, n - 2 ):
      print ( '%5d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRUEFER_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pruefer_successor_test ( )
  timestamp ( )
