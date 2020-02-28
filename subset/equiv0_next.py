#! /usr/bin/env python
#
def equiv0_next ( n, npart, jarray, iarray, more ):

#*****************************************************************************80
#
## EQUIV0_NEXT partitions a set into subsets whose first label is 0.
#
#  Discussion:
#
#    A partition of a set assigns each element to exactly one subset.
#
#    The number of partitions of a set of size N is the Bell number B(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set to be partitioned.
#
#    Input, integer NPART, the number of subsets in the previous partition.
#
#    Input, integer JARRAY(N), the number of elements in each subset
#    of the previous partition.
#
#    Input, integer IARRAY(N), the subset to which each element belongs
#    in the previous partition.
#
#    Input, logical MORE, is set to FALSE on the first call, and the
#    input values of NPART, JARRAY and IARRAY are not needed.  On subsequent
#    calls, MORE should be TRUE, and NPART, JARRAY, and IARRAY should have the
#    values of the output quantities NPART, JARRAY and IARRAY
#    from the previous call.
#
#    Output, integer NPART, the number of subsets in the new partition.
#
#    Output, integer JARRAY(N), the number of elements in each subset
#    of the new partition.
#
#    Output, integer IARRAY(N), the subset to which each element belongs
#    in the new partition.
#
#    Output, logical MORE, is TRUE as long as the new partition returned
#    is not the last one.  When MORE is returned FALSE, all the partitions
#    have been computed and returned.
#
  import numpy as np

  if ( not more ):

    npart = 1
    for i in range ( 0, n ):
      iarray[i] = 0
    jarray[0] = n
    for i in range ( 1, n ):
      jarray[i] = 0

  else:

    m = n

    while ( jarray[iarray[m-1]] == 1 ):
      iarray[m-1] = 0
      m = m - 1

    l = iarray[m-1] + 1
    npart = npart + m - n
    jarray[0] = jarray[0] + n - m

    if ( l == npart ):
      npart = npart + 1
      jarray[npart-1] = 0

    iarray[m-1] = l
    jarray[l-1] = jarray[l-1] - 1
    jarray[l] = jarray[l] + 1

  more = ( npart != n )

  return npart, jarray, iarray, more

def equiv0_next_test ( ):

#*****************************************************************************80
#
## EQUIV0_NEXT_TEST tests EQUIV0_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  npart = 0
  jarray = np.zeros ( n, dtype = np.int32 )
  a = np.zeros ( n, dtype = np.int32 )
  more = False

  print ( '' )
  print ( 'EQUIV0_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EQUIV0_NEXT generates all partitions of a set.' )
  print ( '' )
  print ( '          ', end = '' )
  for i in range ( 0, n ):
    print ( '  %4d' % ( i ), end = '' )
  print ( '' )
  print ( '' )
 
  rank = 0

  while ( True ):
 
    npart, jarray, a, more = equiv0_next ( n, npart, jarray, a, more )
 
    rank = rank + 1
    print ( '  %2d  %2d: ' % ( rank, npart ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )
 
    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'EQUIV0_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  equiv0_next_test ( )
  timestamp ( )

