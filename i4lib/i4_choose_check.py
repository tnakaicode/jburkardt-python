#! /usr/bin/env python
#
def i4_choose_check ( n, k ):

#*****************************************************************************80
#
## I4_CHOOSE_CHECK reports whether the binomial coefficient can be computed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, K, the binomial parameters.
#
#    Output, logical CHECK is:
#    TRUE, if C(N,K) < maximum integer.
#    FALSE, otherwise.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log

  i4_huge = 2147483647

  i4_huge_log = np.log ( i4_huge )

  choose_nk_log = \
      r8_gamma_log ( n + 1 ) \
    - r8_gamma_log ( k + 1 ) \
    - r8_gamma_log ( n - k + 1 )

  check = ( choose_nk_log < i4_huge_log )
        
  return check

def i4_choose_check_test ( ):

#*****************************************************************************80
#
## I4_CHOOSE_CHECK_TEST tests I4_CHOOSE_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4_choose import i4_choose

  k_test = np.array ( [ 3, 999, 3, 10 ] )
  n_test = np.array ( [ 10, 1000, 100, 100 ] )

  print ( '' )
  print ( 'I4_CHOOSE_CHECK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_CHOOSE_CHECK checks whether C(N,K)' )
  print ( '  can be computed with integer arithmetic' )
  print ( '  or not.' )
  print ( '' )
  print ( '     N     K    CHECK?    I4_CHOOSE' )
  print ( '' )
 
  for i in range ( 0, 4 ):
    n = n_test[i]
    k = k_test[i]
    check = i4_choose_check ( n, k )
    print ( '  %4d  %4d        %d' % ( n, k, check ), end = '' )
    if ( check ):
      cnk = i4_choose ( n, k )
      print ( '        %d' % ( cnk ) )
    else:
      print ( '   Not computable' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_CHOOSE_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_choose_check_test ( )
  timestamp ( )

