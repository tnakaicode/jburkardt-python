#! /usr/bin/env python
#
def pruefer_unrank ( rank, n ):

#*****************************************************************************80
#
## PRUEFER_UNRANK unranks a Pruefer code.
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
#    Input, integer RANK, the rank of the Pruefer code.
#
#    Input, integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    Output, integer P(N-2), the Pruefer code for the tree.
#
  import numpy as np
  from pruefer_enum import pruefer_enum
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'PRUEFER_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'PRUEFER_UNRANK - Fatal error!' )

  ncode = pruefer_enum ( n )

  if ( rank < 0 or ncode < rank ):
    print ( '' )
    print ( 'PRUEFER_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'PRUEFER_UNRANK - Fatal error!' )

  p = np.zeros ( n - 2, dtype = np.int32 )

  for i in range ( n - 3, -1, -1 ):
    p[i] = ( rank % n ) + 1;
    rank = ( ( rank - p[i] + 1 ) ) // n;

  return p

def pruefer_unrank_test ( ):

#*****************************************************************************80
#
## PRUEFER_UNRANK_TEST tests PRUEFER_UNRANK.
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
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 4

  print ( '' )
  print ( 'PRUEFER_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PRUEFER_UNRANK unranks Pruefer codes.' )

  rank = 8

  p = pruefer_unrank ( rank, n )

  i4vec_transpose_print ( n - 2, p, '  The element of rank 8:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRUEFER_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pruefer_unrank_test ( )
  timestamp ( )
 
