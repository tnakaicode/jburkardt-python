#! /usr/bin/env python
#
def r8_ei ( x ):

#*****************************************************************************80
#
## R8_EI evaluates the exponential integral Ei for an R8 argument.
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
#    Output, real VALUE, the exponential integral Ei
#    evaluated at X.
#
  from r8_e1 import r8_e1

  value = - r8_e1 ( - x )

  return value

def r8_ei_test ( ):

#*****************************************************************************80
#
## R8_EI_TEST tests R8_EI.
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
  from ei_values import ei_values

  print ( '' )
  print ( 'R8_EI_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EI evaluates the exponential integral Ei(X).' )
  print ( '' )
  print ( '             X           EI(X)  R8_EI(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = ei_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_ei ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EI_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_ei_test ( )
  timestamp ( )
