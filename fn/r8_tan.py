#! /usr/bin/env python
#
def r8_tan ( x ):

#*****************************************************************************80
#
## R8_TAN evaluates the tangent of an R8 argument.
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
#    Output, real VALUE, the tangent of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from sys import exit

  pi2rec = 0.011619772367581343075535053490057

  tancs = np.array ( [ \
      +0.22627932763129357846578636531752, \
      +0.43017913146548961775583410748067E-01, \
      +0.68544610682565088756929473623461E-03, \
      +0.11045326947597098383578849369696E-04, \
      +0.17817477903926312943238512588940E-06, \
      +0.28744968582365265947529646832471E-08, \
      +0.46374854195902995494137478234363E-10, \
      +0.74817609041556138502341633308215E-12, \
      +0.12070497002957544801644516947824E-13, \
      +0.19473610812823019305513858584533E-15, \
      +0.31417224874732446504614586026666E-17, \
      +0.50686132555800153941904891733333E-19, \
      +0.81773105159836540043979946666666E-21, \
      +0.13192643412147384408951466666666E-22, \
      +0.21283995497042377309866666666666E-24, \
      +0.34337960192345945292800000000000E-26, \
      +0.55398222121173811200000000000000E-28, \
      +0.89375227794352810666666666666666E-30, \
      +0.14419111371369130666666666666666E-31 ] )

  nterms = r8_inits ( tancs, 19, 0.1 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xsml = np.sqrt ( 3.0 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( xmax < y ):
    print ( '' )
    print ( 'R8_TAN - Warning!' )
    print ( '  No precision because |X| is big.' )
    value = 0.0
    return value

  ainty = r8_aint ( y )
  yrem = y - ainty
  prodbg = 0.625 * ainty
  ainty = r8_aint ( prodbg )
  y = ( prodbg - ainty ) + 0.625 * yrem + pi2rec * y
  ainty2 = r8_aint ( y )
  ainty = ainty + ainty2
  y = y - ainty2

  ifn = r8_aint ( ainty % 2.0 )

  if ( ifn == 1 ):
    y = 1.0 - y

  if ( 1.0 - y < abs ( x ) * sqeps ):
    print ( '' )
    print ( 'R8_TAN - Warning!' )
    print ( '  Answer < half precision.' )
    print ( '  |X| big or X near pi/2 or 3*pi/2.' )

  if ( y == 1.0 ):
    print ( '' )
    print ( 'R8_TAN - Fatal error!' )
    print ( '  X is pi/2 or 3*pi/2.' )
    value = 0.0
    exit ( 'R8_TAN - Fatal error!' )

  if ( y <= 0.25 ):

    value = y
    if ( xsml < y ):
      value = y * ( 1.5 + r8_csevl ( 32.0 * y * y - 1.0, tancs, nterms ) )

  elif ( y <= 0.5 ):

    value = 0.5 * y * ( 1.5 + r8_csevl ( \
      8.0 * y * y - 1.0, tancs, nterms ) )
    value = 2.0 * value / ( 1.0 - value * value )

  else:

    value = 0.25 * y * ( 1.5 + r8_csevl ( \
      2.0 * y * y - 1.0, tancs, nterms ) )
    value = 2.0 * value / ( 1.0 - value * value )
    value = 2.0 * value / ( 1.0 - value * value )

  if ( x < 0.0 ):
    value = - abs ( value )
  elif ( 0.0 < x ):
    value = + abs ( value )

  if ( ifn == 1 ):
    value = - value

  return value

def r8_tan_test ( ):

#*****************************************************************************80
#
#% R8_TAN_TEST tests R8_TAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from tan_values import tan_values

  print ( '' )
  print ( 'R8_TAN_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_TAN evaluates the tangent function.' )
  print ( '' )
  print ( '             X         TAN(X)  R8_TAN(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = tan_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_tan ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_TAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_tan_test ( )
  timestamp ( )

