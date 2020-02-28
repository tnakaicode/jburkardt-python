#! /usr/bin/env python3
#
def r8_nth_root ( x, n ):

#*****************************************************************************80
#
## R8_NTH_ROOT returns the nth-root of an R8.
#
#  Discussion:
#
#    The nth root of X is x^(1/n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose Nth root is desired.
#
#    Input, integer N, the index of the root.
#
#    Output, real VALUE, the Nth root of X.
#
  import numpy as np
#
#  Potential Error 1: 0^0
#  But we will use it as 1.
#
  if ( x == 0.0 and n == 0 ):

    value = 1.0
#
#  Error 2: 0^(negative power)
#
  elif ( x == 0.0 and n < 0 ):

    value = np.inf
#
#  Error 3: (negative)^(even strictly positive root)
#
  elif ( x < 0.0 and ( n % 2 ) == 0 and 0 < n ):

    value = np.nan
#
#  X^0 = 1
#
  elif ( n == 0 ):

    value = 1.0
#
#  X^1 = X
#
  elif ( n == 1 ):

    value = x
#
#  X^(-1) = 1/X
#
  elif ( n == -1 ):

    value = 1.0 / x

  else:
  
    e = 1.0 / abs ( n )

    if ( 0.0 < x ):
      value = x ** e
    elif ( x == 0.0 ):
      value = 0.0
    else:
      value = - ( - x ) ** e

    if ( n < 0 ):
      value = 1.0 / value

  return value


def r8_nth_root_test ( ):

#*****************************************************************************80
#
## R8_NTH_ROOT_TEST tests R8_NTH_ROOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_NTH_ROOT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NTH_ROOT computes the nth root of an R8.' )
  print ( '' )
  print ( '         X        -3        -2        -1         0         1         2         3' )
  print ( '' )

  for i in range ( -3, 4 ):

    x = float ( i )
    print ( '  %8.4g' % ( x ), end = '' )

    for n in range ( -3, 4 ):
      y = r8_nth_root ( x, n )
      print ( '  %8.4g' % ( y ), end = '' )

    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NTH_ROOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_nth_root_test ( )
  timestamp ( )
 
