#! /usr/bin/env python
#
def r8_aint ( x ):

#*****************************************************************************80
#
## R8_AINT rounds an R8 argument towards 0.
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
#    John Burkardt.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the truncated version of X.
#
  import numpy as np

  if ( x < 0.0 ):
    value = - np.floor ( abs ( x ) )
  else:
    value =   np.floor ( abs ( x ) )

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
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from int_values import int_values

  print ( '' )
  print ( 'R8_AINT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_AINT rounds an R8 towards 0.' )
  print ( '' )
  print ( '             X         AINT(X)  R8_AINT(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_aint ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_AINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_aint_test ( )
  timestamp ( )
