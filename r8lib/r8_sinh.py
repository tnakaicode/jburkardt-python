#! /usr/bin/env python
#
def r8_sinh ( x ):

#*****************************************************************************80
#
## R8_SINH evaluates the hyperbolic sine of an R8 argument.
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
#    Input, real X, the argument.
#
#    Output, real VALUE, the hyperbolic sine of X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach

  sinhcs = np.array ( [ \
      +0.17304219404717963167588384698501, \
      +0.87594221922760477154900263454440E-01, \
      +0.10794777745671327502427270651579E-02, \
      +0.63748492607547504815685554571850E-05, \
      +0.22023664049230530159190496019502E-07, \
      +0.49879401804158493149425807203661E-10, \
      +0.79730535541157304814411480441186E-13, \
      +0.94731587130725443342927317226666E-16, \
      +0.86934920504480078871023098666666E-19, \
      +0.63469394403318040457397333333333E-22, \
      +0.37740337870858485738666666666666E-25, \
      +0.18630213719570056533333333333333E-28, \
      +0.77568437166506666666666666666666E-32 ] )

  nterms = r8_inits ( sinhcs, 13, 0.1 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( 6.0 * r8_mach ( 3 ) )
  ymax = 1.0 / np.sqrt ( r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= sqeps ):

    value = x

  elif ( y <= 1.0 ):

    value = x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, sinhcs, nterms ) )

  else:

    y = np.exp ( y )

    if ( ymax <= y ):
      value = 0.5 * y
    else:
      value = 0.5 * ( y - 1.0 / y )

    if ( x < 0.0 ):
      value = - value

  return value

def r8_sinh_test ( ):

#*****************************************************************************80
#
#% R8_SINH_TEST tests R8_SINH.
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
  from sinh_values import sinh_values

  print ( '' )
  print ( 'R8_SINH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SINH evaluates the hyperbolic sine function.' )
  print ( '' )
  print ( '             X         SINH(X)  R8_SINH(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = sinh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_sinh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SINH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sinh_test ( )
  timestamp ( )

