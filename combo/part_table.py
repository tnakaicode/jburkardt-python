#! /usr/bin/env python
#
def part_table ( n ):

#*****************************************************************************80
#
## PART_TABLE tabulates the number of partitions of N.
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
#    Input, integer N, the integer to be partitioned.
#    N must be positive.
#
#    Output, integer P(1:N+1), P(I+1) is the number of partitions of I.
#
  import numpy as np

  p = np.zeros ( n + 1 )

  p[0] = 1

  if ( n <= 0 ):
    return p

  p[1] = 1

  for i in range ( 2, n + 1 ):
 
    sign = 1
    psum = 0
    w = 1
    j = 1
    wprime = w + j

    while ( w < n ):

      if ( 0 <= i - w ):
        if ( sign == 1 ):
          psum = psum + p[i-w];
        else:
          psum = psum - p[i-w];

      if ( wprime <= i ):

        if ( sign == 1 ):
          psum = psum + p[i-wprime]
        else:
          psum = psum - p[i-wprime]

      w = w + 3 * j + 1
      j = j + 1
      wprime = w + j
      sign = - sign

    p[i] = psum

  return p

def part_table_test ( ):

#*****************************************************************************80
#
## PART_TABLE_TEST tests PART_TABLE.
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
  from i4vec_print import i4vec_print

  maxn = 10
  maxpart = 5

  print ( '' )
  print ( 'PART_TABLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PART_TABLE tabulates partitions of N.' )

  p = part_table ( maxn )

  i4vec_print ( maxn + 1, p, '    I      P(I)' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PART_TABLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  part_table_test ( )
  timestamp ( )
 
