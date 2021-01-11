#! /usr/bin/env python
#
def r8_gamr ( x ):

#*****************************************************************************80
#
## R8_GAMR evaluates the reciprocal gamma function of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
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
#    Input, real X, the argument.
#
#    Output, real VALUE, the value of the reciprocal gamma
#    function at X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_gamma import r8_gamma
  from r8_lgams import r8_lgams

  if ( x <= 0.0 and r8_aint ( x ) == x ):

    value = 0.0

  elif ( abs ( x ) <= 10.0 ):

    value = 1.0 / r8_gamma ( x )

  else:

    alngx, sgngx = r8_lgams ( x )
    value = sgngx * np.exp ( - alngx )

  return value

def r8_gamr_test ( ):

#*****************************************************************************80
#
## R8_GAMR_TEST tests R8_GAMR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from gamma_values import gamma_values

  print ( '' )
  print ( 'R8_GAMR_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMR computes the 1/Gamma(x).' )
  print ( '' )
  print ( '             X      1/GAMMA(X)  R8_GAMR(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, gx = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx1 = 1.0 / gx
    fx2 = r8_gamr ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_gamr_test ( )
  timestamp ( )


