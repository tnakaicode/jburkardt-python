#! /usr/bin/env python
#
def gray_code_unrank ( rank, n ):

#*****************************************************************************80
#
## GRAY_CODE_UNRANK computes the Gray code element of given rank.
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
#    Input, integer RANK, the rank of the element.
#    0 <= RANK <= 2^N.
#
#    Input, integer N, the number of digits in each element.
#    N must be positive.
#
#    Output, integer T(N), the element of the Gray code which has
#    the given rank.
#
  import numpy as np
  from gray_code_enum import gray_code_enum
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'GRAY_CODE_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'GRAY_CODE_RANK - Fatal error!' )

  ngray = gray_code_enum ( n )

  if ( rank < 0 or ngray < rank ):
    print ( '' )
    print ( 'GRAY_CODE_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'GRAY_CODE_RANK - Fatal error!' )

  rank_copy = rank
  t = np.zeros ( n )
  bprime = 0

  for i in range ( n - 1, -1, -1 ): 

    b = ( rank_copy // ( 2 ** i ) )

    if ( b != bprime ):
      t[n-1-i] = 1

    bprime = b
    rank_copy = rank_copy - b * ( 2 ** i )

  return t

def gray_code_unrank_test ( ):

#*****************************************************************************80
#
## GRAY_CODE_UNRANK_TEST tests GRAY_CODE_UNRANK.
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
  import platform
  from gray_code_enum import gray_code_enum
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'GRAY_CODE_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRAY_CODE_UNRANK unranks.' )

  n = 5
  ngray = gray_code_enum ( n )

  rank = ( ngray // 2 )

  print ( '' )
  print ( '  Seek the element of rank %d' % ( rank ) )

  t = gray_code_unrank ( rank, n )

  i4vec_print ( n, t, '  The item of the given rank' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRAY_CODE_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_code_unrank_test ( )
  timestamp ( )

