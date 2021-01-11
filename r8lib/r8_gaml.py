#! /usr/bin/env python
#
def r8_gaml ( ):

#*****************************************************************************80
#
## R8_GAML evaluates bounds for an R8 argument of the gamma function.
#
#  Discussion:
#
#    This function calculates the minimum and maximum legal bounds
#    for X in the evaluation of GAMMA ( X ).
#
#    XMIN and XMAX are not the only bounds, but they are the only
#    non-trivial ones to calculate.
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
#    Output, real XMIN, XMAX, the bounds.
#
  import numpy as np
  from machine import r8_mach
  from sys import exit

  alnsml = np.log ( r8_mach ( 1 ) )
  xmin = - alnsml

  for i in range ( 0, 10 ):

    xold = xmin
    xln = np.log ( xmin )
    xmin = xmin - xmin * ( ( xmin + 0.5 ) * xln - xmin \
      - 0.2258 + alnsml ) / ( xmin * xln + 0.5 )

    if ( abs ( xmin - xold ) < 0.005 ):

      xmin = - xmin + 0.01

      alnbig = np.log ( r8_mach ( 2 ) )
      xmax = alnbig

      for j in range ( 0, 10 ):

        xold = xmax
        xln = np.log ( xmax )
        xmax = xmax - xmax * ( ( xmax - 0.5 ) * xln - xmax \
          + 0.9189 - alnbig ) / ( xmax * xln - 0.5 )

        if ( abs ( xmax - xold ) < 0.005 ):
          xmax = xmax - 0.01
          xmin = max ( xmin, - xmax + 1.0 )
          return xmin, xmax

      print ( '' )
      print ( 'R8_GAML - Fatal error!' )
      print ( '  Unable to find XMAX.' )
      exit ( 'R8_GAML - Fatal error!' )

  print ( '' )
  print ( 'R8_GAML - Fatal error!' )
  print ( '  Unable to find XMIN.' )
  exit ( 'R8_GAML - Fatal error!' )

def r8_gaml_test ( ):

#*****************************************************************************80
#
## R8_GAML_TEST tests R8_GAML.
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

  print ( '' )
  print ( 'R8_GAML_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAML returns bounds for the argument of the gamma function.' )

  xmin, xmax = r8_gaml ( )

  print ( '' )
  print ( '  Lower limit XMIN = %g' % ( xmin ) )
  print ( '  Upper limit XMAX = %g' % ( xmax ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAML_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_gaml_test ( )
  timestamp ( )

