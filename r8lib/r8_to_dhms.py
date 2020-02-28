#! /usr/bin/env python3
#
def r8_to_dhms ( r ):

#*****************************************************************************80
#
## R8_TO_DHMS converts decimal days into days, hours, minutes, seconds.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, a decimal number representing a time 
#    period measured in days.
#
#    Output, integer D, integer H, integer M, real S, the equivalent number of 
#    days, hours, minutes and seconds.
#
  from r8_sign import r8_sign

  r_sign = r8_sign ( r )
  r = abs ( r )

  d = int ( r )

  r = r - d
  r = 24.0 * r
  h = int ( r )

  r = r - h
  r = 60.0 * r
  m = int ( r )

  r = r - m
  s = 60.0 * r

  d = r_sign * d
  h = r_sign * h
  m = r_sign * m
  s = r_sign * s

  return d, h, m, s

def r8_to_dhms_test ( ):

#*****************************************************************************80
#
## R8_TO_DHMS_TEST tests R8_TO_DHMS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_TO_DHMS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_TO_DHMS converts a real day measure into days, hours, minutes, seconds.' )
  print ( '' )
  print ( '         X         D     H     M         S' )
  print ( '' )

  seed = 123456789

  for i in range ( 1, 11 ):
    x, seed = r8_uniform_ab ( - 2.0, +10.0, seed )
    d, h, m, s = r8_to_dhms ( x )
    print ( '  %12g  %4d  %4d  %4d  %12g' % ( x, d, h, m, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_TO_DHMS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_to_dhms_test ( )
  timestamp ( )

