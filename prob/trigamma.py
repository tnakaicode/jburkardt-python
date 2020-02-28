#! /usr/bin/env python
#
def trigamma ( x ):

#*****************************************************************************80
#
## TRIGAMMA calculates trigamma(x) = d^2 log(Gamma(x)) / dx^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    B Schneider,
#    Trigamma Function,
#    Algorithm AS 121,
#    Applied Statistics,
#    Volume 27, Number 1, page 97-99, 1978.
#
#  Parameters:
#
#    Input, X, the argument of the trigamma function.
#    0 < X.
#
#    Output, real VALUE, the value of the trigamma function at X.
#
  from sys import exit

  a = 0.0001
  b = 5.0
  b2 =  1.0 / 6.0
  b4 = -1.0 / 30.0
  b6 =  1.0 / 42.0
  b8 = -1.0 / 30.0
#
#  1): If X is not positive, fail.
#
  if ( x <= 0.0 ):

    value = 0.0
    print ( '' )
    print ( 'TRIGAMMA - Fatal error!' )
    print ( '  X <= 0.' )
    exit ( 'TRIGAMMA - Fatal error!' )
#
#  2): If X is smaller than A, use a small value approximation.
#
  elif ( x <= a ):

    value = 1.0 / x ** 2
#
#  3): Otherwise, increase the argument to B <= ( X + I ).
#
  else:

    z = x
    value = 0.0

    while ( z < b ):
      value = value + 1.0 / z ** 2
      z = z + 1.0
#
#  ...and then apply an asymptotic formula.
#
    y = 1.0 / z ** 2

    value = value + 0.5 * \
            y + ( 1.0 \
          + y * ( b2 \
          + y * ( b4 \
          + y * ( b6 \
          + y *   b8 )))) / z

  return value

def trigamma_test ( ):

#*****************************************************************************80
#
## TRIGAMMA_TEST tests TRIGAMMA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from trigamma_values import trigamma_values

  print ( '' )
  print ( 'TRIGAMMA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIGAMMA evaluates the TriGamma function.' )
  print ( '' )
  print ( '      X               FX               FX' )
  print ( '                      Tabulated        Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = trigamma_values ( n_data )

    if ( n_data == 0 ):
      break
 
    fx2 = trigamma ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIGAMMA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  trigamma_test ( )
  timestamp ( )
 
