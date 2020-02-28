#! /usr/bin/env python
#
def equiv1_next2 ( n, a, done ):

#*****************************************************************************80
#
## EQUIV1_NEXT2 computes, one at a time, the partitions of a set.
#
#  Discussion:
#
#    A partition of a set assigns each element to exactly one subset.
#
#    The number of partitions of a set of size N is the Bell number B(N).
#
#    The entries of IARRAY are the partition subset to which each
#    element of the original set belongs.  If there are NPART distinct
#    parts of the partition, then each entry of IARRAY will be a
#    number between 1 and NPART.  Every number from 1 to NPART will
#    occur somewhere in the list.  If the entries of IARRAY are
#    examined in order, then each time a new partition subset occurs,
#    it will be the next unused integer.
#
#    For instance, for N = 4, the program will describe the set
#    where each element is in a separate subset as 1, 2, 3, 4,
#    even though such a partition might also be described as
#    4, 3, 2, 1 or even 1, 5, 8, 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set.
#
#    Input, integer A(N), the previous partition, that is, the output value
#    of A on the previous call.  On the first call, with DONE = TRUE,
#    the value of A is not needed.
#
#    Input, logical DONE, should be set to TRUE for the first call, to set
#    up initialization, and should be FALSE thereafter.
#
#    Output, integer A(N), the next partition.
#
#    Output, logical DONE, is TRUE if there are more partitions to generate.
#
  if ( done ):

    done = False
    for i in range ( 0, n ):
      a[i] = 1

  else:
#
#  Find the last element J that can be increased by 1.
#  This is the element that is not equal to its maximum possible value,
#  which is the maximum value of all preceding elements +1.
#
    jmax = a[0]
    imax = 0

    for j in range ( 1, n ):

      if ( jmax < a[j] ):
        jmax = a[j]
      else:
        imax = j
#
#  If no element can be increased by 1, we are done.
#
    if ( imax == 0 ):
      done = True
      return a, done
#
#  Increase the value of the IMAX-th element by 1, set its successors to 1.
#
    done = False
    a[imax] = a[imax] + 1
    for j in range ( imax + 1, n ):
      a[j] = 1

  return a, done

def equiv1_next2_test ( ):

#*****************************************************************************80
#
## EQUIV1_NEXT2_TEST tests EQUIV1_NEXT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  a = np.zeros ( n )
  done = True

  print ( '' )
  print ( 'EQUIV1_NEXT2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EQUIV1_NEXT2 generates all partitions of a set.' )
  print ( '  Here, N = %d' % ( n ) )
  print ( ' ' )
  print ( '      ' ),
  for i in range ( 0, n ):
    print ( '  %4d' % ( i ) ),
  print ( '' )
  print ( '' )
 
  rank = 0

  while ( True ):

    a, done = equiv1_next2 ( n, a, done )

    if ( done ):
      break

    rank = rank + 1
    print ( '  %2d: ' % ( rank ) ),
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'EQUIV1_NEXT2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  equiv1_next2_test ( )
  timestamp ( )

