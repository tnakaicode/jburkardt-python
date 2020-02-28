#! /usr/bin/env python
#
def r8_gamma_log_int ( n ):

#*****************************************************************************80
#
## R8_GAMMA_LOG_INT computes the logarithm of Gamma of an integer N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the logarithm of the Gamma function.
#    0 < N.
#
#    Output, real VALUE, the logarithm of
#    the Gamma function of N.
#
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  if ( n <= 0 ):
    print ( '' )
    print ( 'R8_GAMMA_LOG_INT - Fatal error!' )
    print ( '  Illegal input value of N = %d' % ( n ) )
    print ( '  But N must be strictly positive.' )
    exit ( 'R8_GAMMA_LOG_INT - Fatal error!' )

  value = r8_gamma_log ( float ( n ) )

  return value

def r8_gamma_log_int_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_LOG_INT_TEST tests R8_GAMMA_LOG_INT
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_GAMMA_LOG_INT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_LOG_INT evaluates the logarithm of the' )
  print ( '  gamma function for integer argument.' )

  print ( '' )
  print ( '       I    R8_GAMMA_LOG_INT(I)' )
  print ( '' )

  for i in range ( 1, 21 ):
    g = r8_gamma_log_int ( i )
    print ( '  %6d  %14g' % ( i, g ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_LOG_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_gamma_log_int_test ( )
  timestamp ( )
