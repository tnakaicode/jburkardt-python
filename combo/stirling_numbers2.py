#! /usr/bin/env python
#
def stirling_numbers2 ( m, n ):

#*****************************************************************************80
#
## STIRLING_NUMBERS2 computes Stirling numbers of the second kind.
#
#  Discussion:
#
#    The reference has a typographical error, referring to
#    S(I-J,J-1) instead of S(I-1,J-1).
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
#    Input, integer M, the maximum row to compute.
#    M must be nonnegative.
#
#    Input, integer N, the maximum column to compute.
#    N must be nonnegative.
#
#    Output, integer S(1:M+1,1:N+1), the first M+1 rows and N+1 columns
#    of the table of Stirling numbers of the second kind.
#
  import numpy as np

  s = np.zeros ( [ m + 1, n + 1 ] )

  s[0,0] = 1

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( j <= i ):
        s[i+1,j+1] = ( j + 1 ) * s[i,j+1] + s[i,j]

  return s

def stirling_numbers2_test ( ):

#*****************************************************************************80
#
## STIRLING_NUMBERS2_TEST tests STIRLING_NUMBERS2.
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
  from i4mat_print import i4mat_print

  maxm = 6
  maxn = 6
  offset = 1

  print ( '' )
  print ( 'STIRLING_NUMBERS2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STIRLING_NUMBERS2 computes a table of Stirling' )
  print ( '  numbers of the second kind.' )

  s = stirling_numbers2 ( maxm, maxn )

  i4mat_print ( maxm + 1, maxn + 1, s, '  Stirling numbers:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'STIRLING_NUMBERS2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  stirling_numbers2_test ( )
  timestamp ( )
