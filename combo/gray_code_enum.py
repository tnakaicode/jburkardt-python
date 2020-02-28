#! /usr/bin/env python
#
def gray_code_enum ( n ):

#*****************************************************************************80
#
## GRAY_CODE_ENUM enumerates the Gray codes on N digits.
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
#  Parameters:
#
#    Input, integer N, the number of digits in each element.
#    N must be nonnegative.
#
#    Output, integer NGRAY, the number of distinct elements.
#
  ngray = 2 ** n

  return ngray

def gray_code_enum_test ( ):

#*****************************************************************************80
#
## GRAY_CODE_ENUM_TEST tests GRAY_CODE_ENUM.
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

  n = 5

  print ( '' )
  print ( 'GRAY_CODE_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRAY_CODE_ENUM enumerates Gray codes on N elements.' )
  print ( '' )
  print ( '   N    Enum(N)' )
  print ( '' )

  for n in range ( 0, 11 ):
    ngray = gray_code_enum ( n );
    print ( '  %2d  %6d' % ( n, ngray ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRAY_CODE_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_code_enum_test ( )
  timestamp ( )
