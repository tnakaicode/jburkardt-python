#! /usr/bin/env python
#
def pruefer_rank ( n, p ):

#*****************************************************************************80
#
## PRUEFER_RANK ranks a Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
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
#    Input, integer P(N-2), the Pruefer code for the tree.
#
#    Output, integer RANK, the rank of the Pruefer code.
#
  from pruefer_check import pruefer_check
  from sys import exit
#
#  Check.
#
  check = pruefer_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PRUEFER_RANK - Fatal error!' )
    print ( '  Input array is illegal.' )
    exit ( 'PRUEFER_RANK - Fatal error!' )

  rank = 0
  k = 1
  for i in range ( n - 3, -1, -1 ):
    rank = rank + k * ( p[i] - 1 )
    k = k * n

  return rank

def pruefer_rank_test ( ):

#*****************************************************************************80
#
## PRUEFER_RANK_TEST tests PRUEFER_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 4

  print ( '' )
  print ( 'PRUEFER_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PRUEFER_RANK ranks Pruefer codes.' )

  p = np.array ( [ 3, 1 ] )
  i4vec_transpose_print ( n - 2, p, '  Element to be ranked:' )

  rank = pruefer_rank ( n, p )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRUEFER_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pruefer_rank_test ( )
  timestamp ( )
