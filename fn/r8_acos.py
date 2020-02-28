#! /usr/bin/env python
#
def r8_acos ( x ):

#*****************************************************************************80
#
## R8_ACOS evaluates the arc-cosine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
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
#    Output, real VALUE, the arc-cosine of X.
#
  import numpy as np
  from r8_asin import r8_asin

  value = 0.5 * np.pi - r8_asin ( x )

  return value

def r8_acos_test ( ):

#*****************************************************************************80
#
## R8_ACOS_TEST R8_ACOS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from arccos_values import arccos_values

  print ( '' )
  print ( 'R8_ACOS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ACOS evaluates the arc-cosine function' )
  print ( '' )
  print ( '             X      ARCCOS(X)  R8_ACOS(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arccos_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_acos ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ACOS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_acos_test ( )
  timestamp ( )
