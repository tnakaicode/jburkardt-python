#! /usr/bin/env python
#
def i4_partitions_next ( s, m1 ):

#*****************************************************************************80
#
## I4_PARTITIONS_NEXT: next partition into S parts.
#
#  Discussion:
#
#    This function generates, one at a time, entries from the list of
#    nondecreasing partitions of the integers into S or fewer parts.
#
#    The list is ordered first by the integer that is partitioned
#    (the sum of the entries), and second by decreasing lexical order
#    in the partition vectors.
#
#    The first value returned is the only such partition of 0.
#
#    Next comes the only partition of 1.
#
#    There follow two partitions of 2, and so on.
#
#    Typical use of this function begins with an initialization call,
#    and then repeated calls in which the output from the previous call
#    is used as input to the next call:
#
#    m = [ 0, 0, 0 ]
#
#    while ( condition )
#      m = i4_partitions_next ( s, m )
#    end
#
#  Example:
#
#    S = 3
#
#    P  D    M
#    _  _  _____
#    1  0  0 0 0
#    2  1  1 0 0
#    3  2  2 0 0
#    4  2  1 1 0
#    5  3  3 0 0
#    6  3  2 1 0
#    7  3  1 1 1
#    8  4  4 0 0
#    9  4  3 1 0
#   10  4  2 2 0
#   11  4  2 1 1
#   12  5  5 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer S, the number of items in the partition.
#
#    Input, integer M1(S), the current partition.  On first call, this
#    should be a nondecreasing partition.  Thereafter, it should be the
#    output partition from the previous call.
#
#    Output, integer M2(S), the next partition.
#
  import numpy as np

  m2 = np.zeros ( s )
  for i in range ( 0, s ):
    m2[i] = m1[i]

  msum = m2[0]

  for i in range ( 1, s ):

    msum = msum + m2[i]

    if ( m2[0] <= m2[i] + 1 ):
      m2[i] = 0
    else:
      m2[0] = msum - i * ( m2[i] + 1 )
      for j in range ( 1, i + 1 ):
        m2[j] = m2[i] + 1
      return m2
#
#  If we failed to find a suitable index I, put
#  the entire sum into M(1), increment by 1, and
#  prepare to partition the next integer.
#
  m2[0] = msum + 1

  return m2

def i4_partitions_next_test ( ):

#*****************************************************************************80
#
## I4_PARTITIONS_NEXT_TEST tests I4_PARTITIONS_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4_PARTITIONS_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_PARTITIONS_NEXT produces the next' )
  print ( '  nondecreasing partitions of an integer, and' )
  print ( '  if necessary, increments the integer to keep on going.' )
  print ( '' )
  print ( '   I Sum    Partition' )
  print ( '' )

  i = 0
  s = 3
  m = np.array ( [ 0, 0, 0 ] )

  print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ) ),
  for j in range ( 0, s ):
    print ( '  %2d' % ( m[j] ) ),
  print ( '' )

  for i in range ( 0, 15 ):

    m = i4_partitions_next ( s, m )

    print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ) ),
    for j in range ( 0, s ):
      print ( '  %2d' % ( m[j] ) ),
    print ( '' )

  print ( '' )
  print ( '  You can start from any legal partition.' )
  print ( '  Here, we restart at ( 2, 1, 0 ).' )
  print ( '' )
  print ( '   I Sum    Partition' )
  print ( '' )

  i = 0
  s = 3
  m = np.array ( [ 2, 1, 0 ] )

  print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ) ),
  for j in range ( 0, s ):
    print ( '  %2d' % ( m[j] ) ),
  print ( '' )

  for i in range ( 0, 15 ):

    m = i4_partitions_next ( s, m )

    print ( '  %2d  %2d  ' % ( i, np.sum ( m ) ) ),
    for j in range ( 0, s ):
      print ( '  %2d' % ( m[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_PARTITIONS_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partitions_next_test ( )
  timestamp ( )

