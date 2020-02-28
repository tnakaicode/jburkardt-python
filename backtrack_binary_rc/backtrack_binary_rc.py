#! /usr/bin/env python3
#
def backbin_rc ( n, reject, n2, choice ):

#*****************************************************************************80
#
## BACKBIN_RC uses reverse communication for binary backtracking.
#
#  Discussion:
#
#    If this procedure returns a solution with N2 = N, which is acceptable
#    to the user, then a full solution has been found.
#
#    If this procedure returns N2 = -1, no more potential solutions are
#    available to consider.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the full solution.
#
#    Input, logical REJECT, is TRUE if the proposed partial solution
#    in the first N2 entries of CHOICE must be rejected.  On first call,
#    this value is ignored.
#
#    Input/output, integer N2, the length of the current
#    partial solution.  On first call for a given problem, the user
#    should set N2 to -1.  If the program has exhausted the search space,
#    the value of N2 will be returned as -1.
#
#    Input/output, integer CHOICE(N), indicates the current
#    partial solution in entries 1 through N2, which will contain 0 or 1.
#    On first call, set CHOICE to []
#

#
#  N2 = -1 means an initialization call.
#
  if ( n2 == -1 ):

    choice[0:n] = -1
    n2 = 1
    choice[n2-1] = 1
#
#  1 <= FOCUS means we asked the user to evaluate CHOICE(1:N2).
#
#  N2 = N means we returned a full prospective solution
#  so in any case we must increment CHOICE.
#
#  Returning REJECT = 1 means no solution begins this way
#  so we must increment CHOICE.
#
  elif ( n2 == n or reject ):

    while ( 1 < n2 ):
      if ( choice[n2-1] == 1 ):
        choice[n2-1] = 0
        break
      choice[n2-1] = -1
      n2 = n2 - 1
#
#  Have we exhausted the solution space?
#
    if ( n2 == 1 ):
      if ( choice[n2-1] == 1 ):
        choice[n2-1] = 0
      else:
        choice[n2-1] = -1
        n2 = -1
#
#  N2 < N and not REJECT means we can increment N2.
#
  else:

    n2 = n2 + 1
    choice[n2-1] = 1

  return n2, choice

def backtrack_binary_rc_test01 ( ):

#*****************************************************************************80
#
## BACKTRACK_BINARY_RC_TEST01 seeks binary powers that have a given sum.
#
#  Discussion:
#
#    We consider the binary powers 1, 2, 4, ... 2^(n-1).
#
#    We wish to select some of these powers, so that the sum is equal
#    to a given target value.  We are actually simply seeking the binary
#    representation of an integer.
#
#    A partial solution is acceptable if it is less than the target value.
#
#    We list the powers in descending order, so that the bactracking
#    procedure makes the most significant choices first, thus quickly
#    eliminating many unsuitable choices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 8
  test_num = 3
  targets = np.array ( [ 73, 299, -3 ] )

  print ( '' )
  print ( 'BACKTRACK_BINARY_RC_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use BACKBIN_RC to find the binary expansion of' )
  print ( '  an integer between 0 and 255.' )
  print ( '  The choices are 0/1 for the 8 digits.' )

  for test in range ( 0, test_num ):

    target = targets[test]
    print ( '' )
    print ( '  TARGET = %d' % ( target ) )
    call_num = 0
    reject = False
    n2 = -1
    choice = np.zeros ( n, dtype = np.int32 )

    while ( True ):

      n2, choice = backbin_rc ( n, reject, n2, choice )
      call_num = call_num + 1

      if ( n2 == -1 ):
        print ( '  Termination without solution.' )
        break
#
#  Evaluate the integer determined by the choices.
#
      factor = 1
      for i in range ( n, n2, -1 ):
        factor = factor * 2

      result = 0
      for i in range ( 0, n2 ):
        result = result * 2 + choice[i]

      result = result * factor
#
#  If the integer is too big, then we reject it, and
#  all the related integers formed by making additional choices.
#
      reject = ( target < result )
#
#  If we hit the target, then in this case, we can exit because
#  the solution is unique.
#
      if ( result == target ):
        break

    print ( '  Number of calls = %d' % ( call_num ) )
    print ( '  Binary search space = %d' % ( 2 ** n ) )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( choice[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BACKTRACK_BINARY_RC_TEST01' )
  print ( '  Normal end of execution.' )
  return

def backtrack_binary_rc_test02 ( ):

#*****************************************************************************80
#
## BACKTRACK_BINARY_RC_TEST02 seeks a subset of numbers which add to a given sum.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 8
  target = 53
  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ] )

  print ( '' )
  print ( 'BACKTRACK_BINARY_RC_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use BACKBIN_RC to seek subsets of a set W' )
  print ( '  that sum to a given target value.' )
  print ( '  The choices are 0/1 to select each element of W.' )

  print ( '' )
  print ( '  TARGET = %d' % ( target ) )
  print ( '' )
  call_num = 0
  reject = 0
  n2 = -1
  choice = np.zeros ( n, dtype = np.int32 )

  while ( True ):

    n2, choice = backbin_rc ( n, reject, n2, choice )
    call_num = call_num + 1

    if ( n2 == -1 ):
      break
#
#  Evaluate the partial sum.
#
    result = 0
    for i in range ( 0, n2 ):
      result = result + choice[i] * w[i]
#
#  If the sum is too big, then we reject it, and
#  all the related sums formed by making additional choices.
#
    reject = ( target < result )
#
#  If we hit the target, print out the information.
#
    if ( result == target and n2 == n ):
      print ( '  ', end = '' )
      for i in range ( 0, n ):
        print ( '%2d' % ( choice[i] ), end = '' )
      print ( '' )

  print ( '' )
  print ( '  Number of calls = %d' % ( call_num ) )
  print ( '  Binary search space = %d' % ( 2 ** n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BACKTRACK_BINARY_RC_TEST02' )
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

def backtrack_binary_rc_test ( ):

#*****************************************************************************80
#
## BACKTRACK_BINARY_RC_TEST tests BACKTRACK_BINARY_RC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BACKTRACK_BINARY_RC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the BACKTRACK_BINARY_RC library.' )

  backtrack_binary_rc_test01 ( )
  backtrack_binary_rc_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'BACKTRACK_BINARY_RC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  backtrack_binary_rc_test ( )
  timestamp ( )

