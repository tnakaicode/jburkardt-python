#! /usr/bin/env python
#
def bell_numbers ( m ):

#*****************************************************************************80
#
## BELL_NUMBERS computes the Bell numbers.
#
#  Discussion:
#
#    There are B(M) restricted growth functions of length M.
#
#    There are B(M) partitions of a set of M objects.
#
#    B(M) is the sum of the Stirling numbers of the second kind,
#    S(M,N), for N = 0 to M.
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
#    Input, integer M, indicates how many Bell numbers are to
#    compute.  M must be nonnegative.
#
#    Output, integer B(1:M+1), the first M+1 Bell numbers.
#
  import numpy as np
  from i4_choose import i4_choose

  b = np.zeros ( m + 1 )

  offset = 1

  b[0] = 1
  for j in range ( 1, m + 1 ):
    b[j] = 0
    for i in range ( 0, j ):
      b[j] = b[j] + i4_choose ( j - 1, i ) * b[i]

  return b

def bell_numbers_test ( ):

#*****************************************************************************80
#
## BELL_NUMBERS_TEST tests BELL_NUMBERS.
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
  import platform
  from bell_values import bell_values

  print ( '' )
  print ( 'BELL_NUMBERS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BELL_NUMBERS computes Bell numbers.' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, bn = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    b = bell_numbers ( n )

    print ( '  %8d  %12d  %12d' % ( n, bn, b[n] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BELL_NUMBERS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bell_numbers_test ( )
  timestamp ( )
 
