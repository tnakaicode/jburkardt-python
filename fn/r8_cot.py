#! /usr/bin/env python
#
def r8_cot ( x ):

#*****************************************************************************80
#
## R8_COT evaluates the cotangent of an R8 argument.
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
#    Output, real VALUE, the cotangent of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from sys import exit

  pi2rec = 0.011619772367581343075535053490057

  cotcs = np.array ( [ \
      +0.240259160982956302509553617744970, \
      -0.165330316015002278454746025255758E-01, \
      -0.429983919317240189356476228239895E-04, \
      -0.159283223327541046023490851122445E-06, \
      -0.619109313512934872588620579343187E-09, \
      -0.243019741507264604331702590579575E-11, \
      -0.956093675880008098427062083100000E-14, \
      -0.376353798194580580416291539706666E-16, \
      -0.148166574646746578852176794666666E-18, \
      -0.583335658903666579477984000000000E-21, \
      -0.229662646964645773928533333333333E-23, \
      -0.904197057307483326719999999999999E-26, \
      -0.355988551920600064000000000000000E-28, \
      -0.140155139824298666666666666666666E-30, \
      -0.551800436872533333333333333333333E-33 ] )

  nterms = r8_inits ( cotcs, 15, 0.1 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xsml = np.sqrt ( 3.0 * r8_mach ( 3 ) )
  xmin = np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) )  + 0.01 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( y < xmin ):
    print ( '' )
    print ( 'R8_COT - Fatal error!' )
    print ( '  |X| is too small.' )
    exit ( 'R8_COT - Fatal error!' )

  if ( xmax < y ):
    print ( '' )
    print ( 'R8_COT - Fatal error!' )
    print ( '  |X| is too big.' )
    exit ( 'R8_COT - Fatal error!' )

  ainty = r8_aint ( y )
  yrem = y - ainty
  prodbg = 0.625 * ainty
  ainty = r8_aint ( prodbg )
  y = ( prodbg - ainty ) + 0.625 * yrem + y * pi2rec
  ainty2 = r8_aint ( y )
  ainty = ainty + ainty2
  y = y - ainty2

  ifn = r8_aint ( ( ainty % 2.0 ) )

  if ( ifn == 1 ):
    y = 1.0 - y

  if ( 0.5 < abs ( x ) and y < abs ( x ) * sqeps ):
    print ( '' )
    print ( 'R8_COT - Warning!' )
    print ( '  Answer less than half precision.' )
    print ( '  |X| too big, or X nearly a nonzero multiple of pi.' )

  if ( y == 0.0 ):
    print ( '' )
    print ( 'R8_COT - Fatal error!' )
    print ( '  X is a multiple of pi.' )
    exit ( 'R8_COT - Fatal error!' )

  elif ( y <= xsml ):

    value = 1.0 / y

  elif ( y <= 0.25 ):

    value = ( 0.5 + r8_csevl ( 32.0 * y * y - 1.0, cotcs, nterms ) ) / y

  elif ( y <= 0.5 ):

    value = ( 0.5 + r8_csevl ( 8.0 * y * y - 1.0, \
      cotcs, nterms ) ) / ( 0.5 * y )

    value = ( value * value - 1.0 ) * 0.5 / value

  else:

    value = ( 0.5 + r8_csevl ( 2.0 * y * y - 1.0, \
      cotcs, nterms ) ) / ( 0.25 * y )
    value = ( value * value - 1.0 ) * 0.5 / value
    value = ( value * value - 1.0 ) * 0.5 / value

  if ( x < 0.0 ):
    value = - abs ( value )
  else:
    value = + abs ( value )

  if ( ifn == 1 ):
    value = - value

  return value

def r8_cot_test ( ):

#*****************************************************************************80
#
#% R8_COT_TEST tests R8_COT.
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
  from cot_values import cot_values

  print ( '' )
  print ( 'R8_COT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_COT evaluates the cotangent function.' )
  print ( '' )
  print ( '             X         COT(X)  R8_COT(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cot_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cot ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_COT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cot_test ( )
  timestamp ( )
