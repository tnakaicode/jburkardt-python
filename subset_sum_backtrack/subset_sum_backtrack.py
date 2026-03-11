#! /usr/bin/env python3
#
def subset_sum_backtrack ( s, n, v, more, u, t ):
 
#*****************************************************************************80
#
## subset_sum_backtrack() seeks, one at a time, subsets of V that sum to S.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer S, the desired sum.
#
#    integer N, the number of values.
#
#    integer V(N), the values.
#    These must be nonnegative, and sorted in ascending order.  
#    Duplicate values are allowed.
#
#    bool MORE, should be set to FALSE before the first call.
#    Thereafter, it should be the output value of the previous call.
#
#    integer U(N), should be set to 0 before the first call.
#    Thereafter, it should be the output value of the previous call.
#
#    integer T, should be set to 0 before the first call.
#    Thereafter, it should be the output value of the previous call.
#
#  Output:
#
#    bool MORE, is TRUE if a new solution has been returned in U.
#    Process this solution, and call again if more solutions should be sought.
#
#    integer U(N), if MORE is true, U indexes the solution values.
#
#    integer T, if MORE is true, T is the highest index of the selected values.
#
  import numpy as np

  if ( not more ):
  
    t = -1
    u = np.zeros ( n )

  else:
  
    more = False
    u[t] = 0

    told = t
    t = -1

    for i in range ( told - 1, -1, -1 ):
      if ( u[i] == 1 ):
        t = i;
        break
    
    if ( t < 0 ):
      return more, u, t

    u[t] = 0
    t = t + 1
    u[t] = 1
    
  while ( True ):

    su = np.dot ( u, v )
  
    if ( su < s and t < n - 1 ):

      t = t + 1
      u[t] = 1

    else:

      if ( su == s ):
        more = True;
        return more, u, t

      u[t] = 0

      told = t
      t = -1

      for i in range ( told - 1, -1, -1 ):
        if ( u[i] == 1 ):
          t = i;
          break
  
      if ( t < 0 ):
        break

      u[t] = 0
      t = t + 1
      u[t] = 1

  return more, u, t

def subset_sum_backtrack_test_all ( ):

#*****************************************************************************80
#
## subset_sum_backtrack_test_all() calls subset_sum_backtrack_test_one().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'subset_sum_backtrack_test_all():' )
  print ( '  call subset_sum_backtrack_test_one() for each subset_sum problem.' )
  
  s = 9
  n = 5
  v = np.array ( [ 1, 2, 3, 5, 7 ] )
  subset_sum_backtrack_test_one ( s, n, v )
  
  s = 8
  n = 9
  v = np.array ( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
  subset_sum_backtrack_test_one ( s, n, v )
#
#  What happens with a repeated target?
#
  s = 8
  n = 9
  v = np.array ( [ 1, 2, 3, 3, 5, 6, 7, 8, 9 ] )
  subset_sum_backtrack_test_one ( s, n, v )
#
#  What happens with a target that needs all the values?
#
  s = 18
  n = 5
  v = np.array ( [ 1, 2, 3, 5, 7 ] )
  subset_sum_backtrack_test_one ( s, n, v )
#
#  A larger S.
#
  s = 5842
  n = 10
  v = np.array ( [ 267, 493, 869, 961, 1000, 1153, 1246, 1598, 1766, 1922 ] )
  subset_sum_backtrack_test_one ( s, n, v )

  return

def subset_sum_backtrack_test_one ( s, n, v ):

#*****************************************************************************80
#
## subset_sum_backtrack_test_one() tests subset_sum_backtrack().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer S, the desired sum.
#
#    integer N, the number of values.
#
#    integer V(N), the values.
#    These must be nonnegative, and sorted in ascending order.  
#    Duplicate values are allowed.
#
  import numpy as np

  print ( '' )
  print ( 'subset_sum_backtrack_test_one():' )
  print ( '  subset_sum_backtrack() uses backtracking to find solutions of the' )
  print ( '  subset sum problem.' )

  more = False
  u = np.zeros ( n )
  t = 0
  
  print ( '' )
  print ( '  Desired sum S = %d' % ( s ) )
  print ( '  Number of targets = %d' % ( n ) )
  print ( '  Targets:' ),
  for i in range ( 0, n ):
    print ( ' %d' % ( v[i] ), end = '' )
  print ( '' )
  print ( '' )

  k = 0
  
  while ( True ):
    more, u, t = subset_sum_backtrack ( s, n, v, more, u, t )
    if ( not more ):
      break
    k = k + 1
    print ( '  %d:  %d = ' % ( k, s ), end = '' )
    plus = False
    for i in range ( 0, n ):
      if ( u[i] != 0 ):
        if ( plus ):
          print ( '+', end = '' )
        print ( '%d' % ( v[i] ), end = '' )
        plus = True
    print ( '' )
  
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def subset_sum_backtrack_test ( ):

#*****************************************************************************80
#
## subset_sum_backtrack_test tests subset_sum_backtrack().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_sum_backtrack_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test subset_sum_backtrack().' )

  subset_sum_backtrack_test_all( )
#
#  Terminate.
#
  print ( '' )
  print ( 'subset_sum_backtrack_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  subset_sum_backtrack_test ( )
  timestamp ( )

