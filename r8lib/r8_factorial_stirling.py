#! /usr/bin/env python3
#
def r8_factorial_stirling ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL_STIRLING computes Stirling's approximation to N!.
#
#  Discussion:
#
#    N! = Product ( 1 <= I <= N ) I
#
#    Stirling ( N ) = sqrt ( 2 * PI * N ) * ( N / E )^N * E^(1/(12*N) )
#
#    This routine returns the raw approximation for all nonnegative
#    values of N.  If N is less than 0, the value is returned as 0,
#    and if N is 0, the value of 1 is returned.  In all other cases,
#    Stirling's formula is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the function.
#
#    Output, real R8_FACTORIAL_STIRLING, an approximation to N!.
#
  import numpy as np

  r8_e = 2.71828182845904523

  if ( n < 0 ):

    value = 0.0

  elif ( n == 0 ):

    value = 1.0

  else:

    value = np.sqrt ( 2.0 * np.pi * n ) * ( n / r8_e ) ** n \
      * np.exp ( 1.0 / ( 12 * n ) )

  return value

def r8_factorial_stirling_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_STIRLING_TEST tests R8_FACTORIAL_STIRLING
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL_STIRLING_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL_STIRLING computes Stirling\'s' )
  print ( '  approximate factorial function' )
  print ( '' )
  print ( '  N      Factorial    Factorial' )
  print ( '         Stirling' )
  print ( '' )

  f2 = 1.0
  for i in range ( 1, 21 ):
    f1 = r8_factorial_stirling ( i )
    f2 = f2 * i
    print ( '  %6d  %14g  %14g' % ( i, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL_STIRLING_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_factorial_stirling_test ( )
  timestamp ( )
 
