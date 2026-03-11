#! /usr/bin/env python3
#
def numgrid_test ( ):

#*****************************************************************************80
#
## numgrid_test() tests numgrid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'numgrid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test numgrid()' )

  n = 13

  for R in [ 'A', 'B', 'C', 'D', 'H', 'L', 'S' ]:
    G = numgrid ( R, n )
    print ( '' )
    print ( '  numgrid region "' + R + '" with n = ', n )
    print ( G )
#
#  Terminate.
#
  print ( '' )
  print ( 'numgrid_test():' )
  print ( '  Normal end of execution.' )

  return

def numgrid ( R, n ):

#*****************************************************************************80
#
## numgrid() numbers grid points in a two-dimensional region.
#
#  Discussion:
#
#    G = NUMGRID(R,N) numbers the points on an N-by-N grid in
#    the subregion of -1<=x<=1 and -1<=y<=1 determined by R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2023
#
#  Author:
#
#    Original MATLAB version by The MathWorks, Inc.
#    This version by John Burkardt
#
#  Input:
#
#    character R: specifies the region:
#      'S' - the entire square.
#      'L' - the L-shaped domain made from 3/4 of the entire square.
#      'C' - like the 'L', but with a quarter circle in the 4-th square.
#      'D' - the unit disc.
#      'A' - an annulus.
#      'H' - a heart-shaped cardioid.
#      'B' - the exterior of a "Butterfly".
#
#    integer n: the number of rows and columns in the grid.
#
#  Output:
#
#    real G(n,n): a grid containing node numbers.
#
  import numpy as np

  if ( n < 2 ):
    raise Exception ( 'numgrid(): Invalid number of points.' );

  x = np.outer ( np.ones ( n ), np.linspace ( -1.0, 1.0, n ) )
  y = np.flipud ( np.transpose ( x ) )

  if ( R == 'S' ):
    G = (x > -1) & (x < 1) & (y > -1) & (y < 1)
  elif ( R == 'L' ):
    G = (x > -1) & (x < 1) & (y > -1) & (y < 1) & ( (x > 0) | (y > 0))
  elif ( R == 'C' ):
    G = (x > -1) & (x < 1) & (y > -1) & (y < 1) & ((x+1) ** 2 + (y+1) ** 2 > 1)
  elif ( R == 'D' ):
    G = ( x ** 2 + y ** 2 < 1 )
  elif ( R == 'A' ):
    G = ( x ** 2 + y ** 2 < 1 ) & ( x ** 2 + y ** 2 > 1/3 )
  elif ( R == 'H' ):
    RHO = 0.75
    SIGMA = 0.75
    G = ( x ** 2 + y ** 2 ) * ( x ** 2 + y ** 2 - SIGMA * y ) < RHO * x ** 2
  elif ( R == 'B' ):
    t = np.arctan2 ( y, x )
    r = np.sqrt ( x ** 2 + y ** 2 )
    G = ( r >= np.sin ( 2.0 * t ) + 0.2 * np.sin ( 8.0 * t ) ) & \
        ( x > -1 ) & ( x < 1 ) & ( y > -1 ) & ( y < 1 )
  else:

    raise Exception ( 'numgrid(): Invalid region type.' )
#
#  Convert from logical to int.
#
  k = np.nonzero ( G )
  nz = np.shape ( k )[1]
  G = 0 * G
  G[k] = list ( range ( 1, nz + 1 ) )

  return G

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
  numgrid_test ( )
  timestamp ( )

