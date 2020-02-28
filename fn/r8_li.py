#! /usr/bin/env python
#
def r8_li ( x ):

#*****************************************************************************80
#
## R8_LI evaluates the logarithmic integral for an R8 argument.
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
#    Output, real VALUE, the logarithmic integral evaluated at X.
#
  import numpy as np
  from r8_ei import r8_ei
  from r8_log import r8_log
  from machine import r8_mach
  from sys import exit

  sqeps = np.sqrt ( r8_mach ( 3 ) )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'R8_LI - Fatal error!' )
    print ( '  Function undefined for X <= 0.' )
    exit ( 'R8_LI - Fatal error!' )

  if ( x == 0.0 ):
    value = 0.0
    return value

  if ( x == 1.0 ):
    print ( '' )
    print ( 'R8_LI - Fatal error!' )
    print ( '  Function undefined for X = 1.' )
    exit ( 'R8_LI - Fatal error!' )

  if ( abs ( 1.0 - x ) < sqeps ):
    print ( '' )
    print ( 'R8_LI - Warning!' )
    print ( '  Answer less than half precision.' )
    print ( '  X is too close to 1.' )

  value = r8_ei ( r8_log ( x ) )

  return value

def r8_li_test ( ):

#*****************************************************************************80
#
## R8_LI_TEST tests R8_LI.
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
  from logarithmic_integral_values import logarithmic_integral_values

  print ( '' )
  print ( 'R8_LI_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LI evaluates the logarithmic integral.' )
  print ( '' )
  print ( '             X           LI(X)  R8_LI(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = logarithmic_integral_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_li ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LI_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_li_test ( )
  timestamp ( )
