#! /usr/bin/env python
#
def l4_to_i4 ( l ):

#*****************************************************************************80
#
## L4_TO_I4 converts an L4 to an I4.
#
#  Discussion:
#
#    0 is FALSE, and anything else if TRUE.
#
#    An I4 is an integer value.
#    An L4 is a logical value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, bool L, a logical value.
#
#    Output, integer VALUE, the integer value of L.
#
  if ( l ):
    value = 1
  else:
    value = 0

  return value

def l4_to_i4_test ( ):

#*****************************************************************************80
#
## L4_TO_I4_TEST tests L4_TO_I4. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'L4_TO_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  L4_TO_I4 converts an L4 to an I4.' )
  print ( '' )
  print ( '      L4   I4' )
  print ( '' )

  l4 = False
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )

  l4 = True
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4_TO_I4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4_to_i4_test ( )
  timestamp ( )

