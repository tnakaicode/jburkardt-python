#! /usr/bin/env python
#
def r8_atan2 ( sn, cs ):

#*****************************************************************************80
#
## R8_ATAN2 evaluates the arc-tangent of two R8 arguments.
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
#    Input, real SN, CS, the Y and X coordinates of a
#    point on the angle.
#
#    Output, real VALUE, the arc-tangent of the angle.
#
  import numpy as np
  from r8_atan import r8_atan
  from machine import r8_mach
  from sys import exit

  sml = r8_mach ( 1 )
  big = r8_mach ( 2 )
#
#  We now make sure SN can be divided by CS.  It is painful.
#
  abssn = abs ( sn )
  abscs = abs ( cs )

  if ( abscs <= abssn ):

    if ( abscs < 1.0 and abscs * big <= abssn ):

      if ( sn < 0.0 ):
        value = - 0.5 * np.pi
      elif ( sn == 0.0 ):
        print ( '' )
        print ( 'R8_ATAN2 - Fatal error!' )
        print ( '  Both arguments are 0.' )
        exit ( 'R8_ATAN2 - Fatal error!' )
      else:
        value = 0.5 * np.pi

      return value

  else:

    if ( 1.0 < abscs and abssn <= abscs * sml ):

      if ( 0.0 <= cs ):
        value = 0.0
      else:
        value = np.pi

      return value

  value = r8_atan ( sn / cs )

  if ( cs < 0.0 ):
    value = value + np.pi

  if ( np.pi < value ):
    value = value - 2.0 * np.pi

  return value

def r8_atan2_test ( ):

#*****************************************************************************80
#
## R8_ATAN2_TEST tests R8_ATAN2.
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
  from arctan2_values import arctan2_values

  print ( '' )
  print ( 'R8_ATAN2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ATAN2 evaluates the arctangent function' )
  print ( '' )
  print ( '             X               Y   ARCTAN2(Y,X)  R8_ATAN2(Y,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, fx1 = arctan2_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_atan2 ( y, x )

    print ( '  %14.4g  %14.4f  %14.6g  %14.6g  %14.6g' \
      % ( x, y, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ATAN2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_atan2_test ( )
  timestamp ( )
