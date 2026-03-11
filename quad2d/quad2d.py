#! /usr/bin/env python3
#
def f ( x, y ):

#*****************************************************************************80
#
## f() evaluates the function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the coordinates of a point.
#
#  Output:
#
#    real VALUE, the function value at (X,Y).
#
  value = 1.0 / ( 1.0 - x * y )

  return value

def quad2d ( nx, ny, a, b, c, d, f ):

#*****************************************************************************80
#
## quad2d() estimates the integral of a function over the rectangle [a,b]x[c,d].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 Octobe 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
  estimate = 0.0

  for i in range ( 0, nx ):
    x = ( ( 2 * nx - 2 * i - 1 ) * a + ( 2 * i + 1 ) * b ) / ( 2 * nx )
    for j in range ( 0, ny ):
      y = ( ( 2 * ny - 2 * j - 1 ) * c + ( 2 * j + 1 ) * d ) / ( 2 * ny )
      estimate = estimate + f ( x, y )

  estimate = ( b - a ) * ( d - c ) * estimate / nx / ny

  return estimate

def quad2d_test ( ):

#*****************************************************************************80
#
## quad2d_test() tests quad2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2022
#
#  Author:
#
#    John Burkardt
#
  from time import time
  import numpy as np
  import platform

  print ( '' )
  print ( 'quad2d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test quad2d().' )

  a = 0.0
  b = 1.0
  c = 0.0
  d = 1.0
  nx = 16384
  ny = 16384
  n = nx * ny

  print ( '  Estimate the integral of f(x,y) over [a,b]x[c,d].' )
  print ( '  f(x,y) = 1 / ( 1 - x * y ).' )
  print ( '  using a ',nx, ' x ', ny, ' grid of ', n, ' points.' )
  print ( '  ', a, ' <= x <= ', b )
  print ( '  ', c, ' <= y <= ', d )

  seconds = time ( )

  estimate = quad2d ( nx, ny, a, b, c, d, f )

  seconds = time ( ) - seconds

  exact = ( np.pi )**2 / 6.0
  error = abs ( exact - estimate )
 
  print ( '' )
  print ( '  Exact =    ', exact )
  print ( '  Estimate = ', estimate )
  print ( '  Error    = ', error )
  print ( '  Time     = ', seconds )
#
#  Terminate.
#
  print ( '' )
  print ( 'quad2d_test():' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  quad2d_test ( )
  timestamp ( )

