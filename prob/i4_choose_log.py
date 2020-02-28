#! /usr/bin/env python
#
def i4_choose_log ( n, k ):

#*****************************************************************************80
#
## I4_CHOOSE_LOG computes the logarithm of the Binomial coefficient.
#
#  Discussion:
#
#    LOG ( C(N,K) ) = LOG ( N! / ( K! * (N-K)! ) ).
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
#    Input, integer N, K, are the values of N and K.
#
#    Output, real VALUE, the logarithm of C(N,K).
#
  from r8_gamma_log import r8_gamma_log

  value = \
      r8_gamma_log ( float ( n + 1 ) ) \
    - r8_gamma_log ( float ( k + 1 ) ) \
    - r8_gamma_log ( float ( n - k + 1 ) )

  return value

def i4_choose_log_test ( ):

#*****************************************************************************80
#
## I4_CHOOSE_LOG_TEST tests I4_CHOOSE_LOG.
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
  from i4_choose import i4_choose

  print ( '' )
  print ( 'I4_CHOOSE_LOG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_CHOOSE_LOG evaluates log(C(N,K)).' )
  print ( '' )
  print ( '     N     K            lcnk           elcnk   CNK' )
  print ( '' )
 
  for n in range ( 0, 5 ):
    for k in range ( 0, n + 1 ):
      lcnk = i4_choose_log ( n, k )
      elcnk = np.exp ( lcnk )
      cnk = i4_choose ( n, k )
      print ( '  %4d  %4d  %14.6g  %14.6g  %4d' % ( n, k, lcnk, elcnk, cnk ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_CHOOSE_LOG_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_choose_log_test ( )
  timestamp ( )
 
