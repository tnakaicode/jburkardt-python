#! /usr/bin/env python
#
def i4_factorial_log ( n ):

#*****************************************************************************80
#
## I4_FACTORIAL_LOG returns the logarithm of N factorial.
#
#  Discussion:
#
#    N! = Product ( 1 <= I <= N ) I
#
#    N! = Gamma(N+1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the function.
#    0 <= N.
#
#    Output, real VALUE, the logarithm of N factorial.
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'I4_FACTORIAL_LOG - Fatal error!' )
    print ( '  N < 0.' )
    exit ( 'I4_FACTORIAL_LOG - Fatal error!' )

  value = 0.0

  for i in range ( 2, n + 1 ):
    value = value + np.log ( i )

  return value

def i4_factorial_log_test ( ):

#*****************************************************************************80
#
## I4_FACTORIAL_LOG_TEST tests I4_FACTORIAL_LOG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4_factorial_values import i4_factorial_values

  print ( '' )
  print ( 'I4_FACTORIAL_LOG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_FACTORIAL_LOG evaluates the log(N!).' )
  print ( '' )
  print ( '         N           lfact          elfact         fact' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fact = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    lfact = i4_factorial_log ( n )
    elfact = np.exp ( lfact )

    print ( '  %8d  %14.6g  %14.6g  %12d' % ( n, lfact, elfact, fact ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_FACTORIAL_LOG_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_factorial_log_test ( )
  timestamp ( )
 
