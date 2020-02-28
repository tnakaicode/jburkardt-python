#! /usr/bin/env python
#
def r8_int ( x ):

#*****************************************************************************80
#
## R8_INT returns the integer part of an R8 argument.
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
#    Output, real VALUE, the integer part of X.
#
  import numpy as np
  from machine import i4_mach
  from machine import r8_mach

  ibase = i4_mach ( 10 )
  xmax = 1.0 / r8_mach ( 4 )
  xbig = min ( i4_mach ( 9 ), xmax )
  expo = np.floor ( np.log ( xbig ) / np.log ( ibase ) - 0.5 )
  scale = ibase ** expo
  npart = np.floor ( np.log ( xmax ) / np.log ( scale ) + 1.0 )

  if ( x < - xmax ):

    value = x

  elif ( x < - xbig ):

    xscl = - x

    for i in range ( 0, npart ):
      xscl = xscl / scale

    value = 0.0
    for i in range ( 0, npart ):
      xscl = xscl * scale
      ipart = np.ceil ( xscl )
      part = ipart
      xscl = xscl - part
      value = value * scale + part

    value = - value

  elif ( x < 0 ):

    value = np.ceil ( x )

  elif ( x < + xbig ):

    value = np.floor ( x )

  elif ( x < + xmax ):

    xscl = x

    for i in range ( 0, npart ):
      xscl = xscl / scale

    value = 0.0
    for i in range ( 0, npart ):
      xscl = xscl * scale
      ipart = np.floor ( xscl )
      part = ipart
      xscl = xscl - part
      value = value * scale + part

  else:

    value = x

  return value

def r8_int_test ( ):

#*****************************************************************************80
#
## R8_INT_TEST tests R8_INT.
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
  from int_values import int_values

  print ( '' )
  print ( 'R8_INT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_INT computes the integer part of an R8.' )
  print ( '' )
  print ( '             X         INT(X)  R8_INT(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_int ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_INT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_int_test ( )
  timestamp ( )
