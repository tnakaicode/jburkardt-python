#! /usr/bin/env python
#
def r8_sqrt ( x ):

#*****************************************************************************80
#
## R8_SQRT computes the square root of an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real X, the number whose square root is desired.
#
#    Output, real VALUE, the square root of X.
#
  import numpy as np
  from r8_log import r8_log
  from machine import r8_mach
  from r8_pak import r8_pak
  from r8_pak import r8_upak
  from sys import exit

  sqrt2 = np.array ( [ \
    0.70710678118654752440084436210485, \
    1.0, \
    1.41421356237309504880168872420970 ] )

  niter = int ( 1.443 * r8_log ( - 0.104 * r8_log ( 0.1 * r8_mach ( 3 ) ) ) + 1.0 )

  if ( x < 0.0 ):

    print ( '' )
    print ( 'R8_SQRT - Fatal error!' )
    print ( '  X < 0.0' )
    exit ( 'R8_SQRT - Fatal error!' )

  elif ( x == 0.0 ):

    value = 0.0

  else:

    y, n = r8_upak ( x )
    ixpnt = ( n // 2 )
    irem = int ( np.fix ( n - 2 * ixpnt + 2 ) )
    value = 0.261599 + y * ( 1.114292 + y * ( -0.516888 + y * 0.141067 ) )

    for iter in range ( 0, niter ):
      value = value + 0.5 * ( y - value * value ) / value

    value = r8_pak ( sqrt2[irem-1] * value, ixpnt )

  return value

def r8_sqrt_test ( ):

#*****************************************************************************80
#
## R8_SQRT_TEST tests R8_SQRT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from sqrt_values import sqrt_values

  print ( '' )
  print ( 'R8_SQRT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SQRT evaluates the square root function.' )
  print ( '' )
  print ( '             X         SQRT(X)  R8_SQRT(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = sqrt_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_sqrt ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SQRT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sqrt_test ( )
  timestamp ( )

