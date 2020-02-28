#! /usr/bin/env python3
#
def knapsack_01_brute ( n, w, c ):

#*****************************************************************************80
#
## KNAPSACK_01_BRUTE seeks a solution of the 0/1 Knapsack problem.
#
#  Discussion:
#
#    In the 0/1 knapsack problem, a knapsack of capacity C is given,
#    as well as N items, with the I-th item of weight W(I).
#
#    A selection is "acceptable" if the total weight is no greater than C.
#
#    It is desired to find an optimal acceptable selection, that is,
#    an acceptable selection such that there is no acceptable selection
#    of greater weight.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), the weights.
#
#    Input, integer C, the maximum weight.
#
#    Output, integer S[N], is a binary vector which defines an optimal
#    selection.  It is 1 for the weights to be selected, and 0 otherwise.
#
  import numpy as np

  more = False
  ncard = 0

  s_test = np.zeros ( n )
  t_test = 0

  s_opt = np.zeros ( n )
  t_opt = 0;

  while ( True ):

    s_test, more, ncard, iadd = subset_gray_next ( n, s_test, more, ncard )
    t_test = 0
    for i in range ( 0, n ):
      t_test = t_test + s_test[i] * w[i]

    if ( t_opt < t_test and t_test <= c ):
      t_opt = t_test
      for i in range ( 0, n ):
        s_opt[i] = s_test[i]

    if ( not more ):
      break

  return s_opt

def knapsack_01_brute_test ( ):

#*****************************************************************************80
#
## KNAPSACK_01_BRUTE+TEST seeks a solution of the 0/1 Knapsack problem.
#
#  Discussion:
#
#    In the 0/1 knapsack problem, a knapsack of capacity C is given,
#    as well as N items, with the I-th item of weight W(I).
#
#    A selection is "acceptable" if the total weight is no greater than C.
#
#    It is desired to find an optimal acceptable selection, that is,
#    an acceptable selection such that there is no acceptable selection
#    of greater weight.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  w = np.array ( [ 16, 17, 23, 24, 39, 40 ] )
  c = 100
  n = 6

  print ( '' )
  print ( 'KNAPSACK_01_BRUTE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Knapsack maximum capacity is %d' % ( c ) )
  print ( '  Come as close as possible to filling the knapsack.' )

  s = knapsack_01_brute ( n, w, c )

  print ( '' )
  print ( '   # 0/1  Weight' )
  print ( '' )
  total = 0
  for i in range ( 0, n ):
    total = total + s[i] * w[i]
    print ( '  %2d  %1d  %4d' % ( i, s[i], w[i] ) )
  print ( '' )
  print ( '  Total: %4d' % ( total ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KNAPSACK_01_BRUTE_TEST' )
  print ( '  Normal end of execution.' )
  return

def knapsack_01_test ( ):

#*****************************************************************************80
#
## KNAPSACK_01_TEST tests the KNAPSACK_01 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'KNAPSACK_01_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the KNAPSACK_01 library.' )

  subset_gray_next_test ( )
  knapsack_01_brute_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'KNAPSACK_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def subset_gray_next ( n, a, more, ncard ):

#*****************************************************************************80
#
## SUBSET_GRAY_NEXT generates all subsets of a set of order N, one at a time.
#
#  Discussion:
#
#    This routine generates the subsets one at a time, by adding or subtracting
#    exactly one element on each step.
#
#    This uses a Gray code ordering of the subsets.
#
#    The user should set MORE = FALSE and the value of N before
#    the first call.  On return, the user may examine A which contains
#    the definition of the new subset, and must check MORE, because
#    as soon as it is FALSE on return, all the subsets have been
#    generated and the user probably should cease calling.
#
#    The first set returned is the empty set.
#
#  Example:
#
#    N = 4
#
#    0 0 0 0
#    1 0 0 0
#    1 1 0 0
#    0 1 0 0
#    0 1 1 0
#    1 1 1 0
#    1 0 1 0
#    0 0 1 0
#    0 0 1 1
#    1 0 1 1
#    1 1 1 1
#    0 1 1 1
#    0 1 0 1
#    1 1 0 1
#    1 0 0 1
#    0 0 0 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
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
#    Input, integer N, the order of the total set from which
#    subsets will be drawn.
#
#    Input, integer A(N), the value of A on the previous call.
#    This value is not needed on the first call, with MORE = FALSE.
#
#    Input, logical MORE, should be set to FALSE on the first call, and
#    then set to TRUE for all subsequent calls.
#
#    Input, integer NCARD, the cardinality of A.  This value is not needed
#    on the first call, with MORE = FALSE.
#
#    Output, integer A(N), the Gray code for the next subset.  A(I) = 0
#    if element I is in the subset, 1 otherwise.
#
#    Output, logical MORE. will be returned TRUE until all the subsets
#    have been generated.
#
#    Output, integer NCARD, the cardinality of A.
#
#    Output, integer IADD, the element which was added or removed to the
#    previous subset to generate the current one.  Exception:
#    the empty set is returned on the first call, and IADD is set to -1.
#

#
#  The first set returned is the empty set.
#
  if ( not more ):

    for i in range ( 0, n ):
      a[i] = 0
    more = True
    ncard = 0
    iadd = -1

  else:

    iadd = 0

    if ( ( ncard % 2 ) != 0 ):

      while ( True ):

        iadd = iadd + 1
        if ( a[iadd-1] != 0 ):
          break

    a[iadd] = 1 - a[iadd]
    ncard = ncard + 2 * a[iadd] - 1
#
#  The last set returned is the singleton A(N).
#
    if ( ncard == a[n-1] ):
      more = False

  return a, more, ncard, iadd

def subset_gray_next_test ( ):

#*****************************************************************************80
#
## SUBSET_GRAY_NEXT_TEST tests SUBSET_GRAY_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SUBSET_GRAY_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_GRAY_NEXT generates all subsets of an N set.' )
  print ( '  using the Gray code ordering:' )
  print ( '  0 0 1 0 1 means the subset contains 3 and 5.' )
  print ( '' )
  print ( '  Gray code' )
  print ( '' )
 
  rank = 0
  n = 5
  a = np.zeros ( n )
  more = False
  ncard = -1
  
  while ( True ):
 
    a, more, ncard, iadd = subset_gray_next ( n, a, more, ncard )

    rank = rank + 1

    print ( '  %2d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_GRAY_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  knapsack_01_test ( )
  timestamp ( )

