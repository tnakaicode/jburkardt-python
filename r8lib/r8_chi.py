#! /usr/bin/env python
#
def r8_chi ( x ):

#*****************************************************************************80
#
## R8_CHI evaluates the hyperbolic cosine integral of an R8 argument.
#
#  Discussion:
#
#    The hyperbolic cosine integral is defined by
#
#      CHI(X) = gamma + log ( x )
#        + integral ( 0 <= T < X ) ( cosh ( T ) - 1 ) / T  dT
#
#    where gamma is Euler's constant.
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
#    Output, real VALUE, the hyperbolic cosine integral
#    evaluated at X.
#
  from r8_e1 import r8_e1
  from r8_ei import r8_ei

  value = 0.5 * ( r8_ei ( x ) - r8_e1 ( x ) )

  return value

def r8_chi_test ( ):

#*****************************************************************************80
#
## R8_CHI_TEST tests R8_CHI.
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
  from chi_values import chi_values

  print ( '' )
  print ( 'R8_CHI_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHI evaluates the hyperbolic cosine integral.' )
  print ( '' )
  print ( '             X          CHI(X)  R8_CHI(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = chi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_chi ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHI_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_chi_test ( )
  timestamp ( )

