#! /usr/bin/env python
#
def r8_choose ( n, k ):

#*****************************************************************************80
#
## R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, K, are the values of N and K.
#
#    Output, real VALUE, the number of combinations of N
#    things taken K at a time.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log

  if ( n < 0 ):

    value = 0.0

  elif ( k == 0 ):

    value = 1.0

  elif ( k == 1 ):

    value = float ( n )

  elif ( 1 < k and k < n - 1 ):

    facn = r8_gamma_log ( float ( n + 1 ) )
    fack = r8_gamma_log ( float ( k + 1 ) )
    facnmk = r8_gamma_log ( float ( n - k + 1 ) )

    value = round ( np.exp ( facn - fack - facnmk ) )

  elif ( k == n - 1 ):

    value = float ( n )

  elif ( k == n ):

    value = 1.0

  else:

    value = 0.0

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## R8_CHOOSE_TEST tests R8_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHOOSE evaluates C(N,K).' )
  print ( '' )
  print ( '         N         K       CNK' )
 
  for n in range ( 0, 6 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print ( '  %8d  %8d  %14.6g' % ( n, k, cnk ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_choose_test ( )
  timestamp ( )
