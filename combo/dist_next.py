#! /usr/bin/env python
#
def dist_next ( k, m, q, leftmost, more ):

#*****************************************************************************80
#
## DIST_NEXT returns the next distribution of indistinguishable objects.
#
#  Discussion:
#
#    A distribution of M objects into K parts is an ordered sequence
#    of K nonnegative integers which sum to M.  This is similar to
#    a partition of a set into K subsets, except that here the order
#    matters.  That is, (1,1,2) and (1,2,1) are considered to be
#    different distributions.
#
#    On the first call to this routine, the user should set MORE = FALSE,
#    to signal that this is a startup for the given computation.  The routine
#    will return the first distribution, and set MORE = TRUE.
#
#    If the user calls again, with MORE = TRUE, the next distribution
#    is being requested.  If the routine returns with MORE = TRUE, then
#    that distribution was found and returned.  However, if the routine
#    returns with MORE = FALSE, then no more distributions were found
#    the enumeration of distributions has terminated.
#
#    A "distribution of M indistinguishable objects into K slots" is
#    sometimes called a "composition of the integer M into K parts".
#
#  Example:
#
#    K = 3, M = 5
#
#    0           0           5
#    0           1           4
#    0           2           3
#    0           3           2
#    0           4           1
#    0           5           0
#    1           0           4
#    1           1           3
#    1           2           2
#    1           3           1
#    1           4           0
#    2           0           3
#    2           1           2
#    2           2           1
#    2           3           0
#    3           0           2
#    3           1           1
#    3           2           0
#    4           0           1
#    4           1           0
#    5           0           0
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
#    Robert Fenichel,
#    Algorithm 329:
#    Distribution of Indistinguishable Objects into
#    Distinguishable Slots,
#    Communications of the ACM,
#    Volume 11, Number 6, June 1968, page 430.
#
#  Parameters:
#
#    Input, integer K, the number of distinguishable "slots".
#
#    Input, integer M, the number of indistinguishable objects.
#
#    Input/output, integer Q(K), the number of objects in each
#    slot.
#
#    Input/output, integer LEFTMOST, used to speed up the computation.
#    On first call, set LEFTMOST to 0.
#
#    Input/output, logical MORE, used by the user to start the computation,
#    and by the routine to stop the computation.
#
  import numpy as np
#
#  The startup call.
#
  if ( not more ):

    more = True

    q = np.zeros ( k )
    q[k-1] = m

    leftmost = k
#
#  There are no more distributions.
#  Reset Q to the first distribution in the sequence.
#
  elif ( q[0] == m ):

    more = False

    q = np.zeros ( k )
    q[k-1] = m

    leftmost = k

  elif ( leftmost < k ):

    leftmost = leftmost - 1
    q[k-1] = q[leftmost] - 1
    q[leftmost] = 0
    q[leftmost-1] = q[leftmost-1] + 1
    if ( q[k-1] != 0 ):
      leftmost = k

  else:

    if ( q[k-1] == 1 ):
      leftmost = k - 1

    q[k-1] = q[k-1] - 1
    q[k-2] = q[k-2] + 1

  return q, leftmost, more

def dist_next_test ( ):

#*****************************************************************************80
#
## DIST_NEXT_TEST tests DIST_NEXT.
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
  import numpy as np
  import platform
  from dist_enum import dist_enum

  k = 3
  m = 5
  q = np.array ( [] )
  leftmost = 0
  more = False

  print ( '' )
  print ( 'DIST_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIST_NEXT produces the "next" distribution of M' )
  print ( '  indistinguishable objects among K distinguishable slots:' )
  print ( '' )
  print ( '  Number of:' )
  print ( '    indistinguishable objects = %d' % ( m ) )
  print ( '    distinguishable slots =     %d' % ( k ) )
  print ( '    distributions is            %d' % ( dist_enum ( k, m ) ) )
  print ( '' )

  idist = 0

  while ( True ):

    q, leftmost, more = dist_next ( k, m, q, leftmost, more )

    if ( not more ):
      break

    idist = idist + 1
    print ( '    %5d: ' % ( idist ), end = '' )
    for i in range ( 0, k ):
      print ( '%5d' % ( q[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIST_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dist_next_test ( )
  timestamp ( )
 
