#! /usr/bin/env python
#
def gray_code_rank ( n, t ):

#*****************************************************************************80
#
## GRAY_CODE_RANK computes the rank of a Gray code element.
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
#    Input, integer T(N), an element of the Gray code.
#    Each entry T(I) is either 0 or 1.
#
#    Output, integer RANK, the rank of the element.
#
  from gray_code_check import gray_code_check
  from sys import exit
#
#  Check.
#
  check = gray_code_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'GRAY_CODE_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'GRAY_CODE_RANK - Fatal error!' )

  rank = 0
  b = 0

  for i in range ( n - 1, -1, -1 ):

    if ( t[n-1-i] != 0 ):
      b = 1 - b

    if ( b == 1 ):
      rank = rank + 2 ** i

  return rank

def gray_code_rank_test ( ):

#*****************************************************************************80
#
## GRAY_CODE_RANK_TEST tests GRAY_CODE_RANK.
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
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'GRAY_CODE_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRAY_CODE_RANK ranks a given Gray code.' )

  n = 5
  t = np.array ( [ 1, 1, 0, 0, 0 ] )

  rank = gray_code_rank ( n, t )

  i4vec_print ( n, t, '  Element to be ranked:' )

  print ( '' )
  print ( '  Computed rank: %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRAY_CODE_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_code_rank_test ( )
  timestamp ( )

