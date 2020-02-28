#! /usr/bin/env python3
#
def r8_aint ( x ):

#****************************************************************************80
#
## R8_AINT truncates an R8 argument to an integer.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the truncated version of X.
#
  if ( x < 0.0 ):
    value = - int ( abs ( x ) )
  else:
    value =   int ( abs ( x ) )

  return value

def r8_aint_test ( ):

#*****************************************************************************80
#
## R8_AINT_TEST tests R8_AINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_AINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_AINT truncates a real number to its integer part.' )
  print ( '' )
  print ( '        X           R8_AINT(X)' )
  print ( '' )

  seed = 123456789

  for test in range ( 1, 11 ):
    x, seed = r8_uniform_ab ( -10.0, +10.0, seed )
    x2 = r8_aint ( x )
    print ( '  %12f  %12f' % ( x, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_AINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_aint_test ( )
  timestamp ( )
