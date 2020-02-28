#! /usr/bin/env python
#
def npart_table ( n, npart ):

#*****************************************************************************80
#
## NPART_TABLE tabulates the number of partitions of N having NPART parts.
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
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Output, integer P(1:N+1,1:NPART+1), P(I+1,J+1) is the number of
#    partitions of I having J parts.
#
  import numpy as np

  p = np.zeros ( [ n + 1, npart + 1 ] )

  p[0,0] = 1

  for i in range ( 1, n + 1 ):
    for j in range ( 1, npart + 1 ):
      if ( i < j ):
        p[i,j] = 0
      elif ( i < 2 * j ):
        p[i,j] = p[i-1,j-1]
      else:
        p[i,j] = p[i-1,j-1] + p[i-j,j]

  return p

def npart_table_test ( ):

#*****************************************************************************80
#
## NPART_TABLE_TEST tests NPART_TABLE.
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

  maxn = 10
  maxpart = 5

  print ( '' )
  print ( 'NPART_TABLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_TABLE tabulates partitions' )
  print ( '  of N with NPART parts' )

  p = npart_table ( maxn, maxpart )

  print ( '' )
  print ( '    I P(I,0) P(I,1) P(I,2) P(I,3) P(I,4) P(I,5)' )
  print ( '' )

  for i in range ( 0, maxn + 1 ):
    print ( '%5d' % ( i ), end = '' )
    for j in range ( 0, maxpart + 1 ):
      print ( '%5d' % ( p[i,j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_TABLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_table_test ( )
  timestamp ( )
 
