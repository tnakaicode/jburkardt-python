#! /usr/bin/env python3
#
def fern_chaos_test ( ):

#*****************************************************************************80
#
## fern_chaos_test() tests fern_chaos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fern_chaos_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  fern_chaos() makes an n-point image of the Barnsley fractal fern.' )

  n = 10000
  fern_chaos ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'fern_chaos_test():' )
  print ( '  Normal end of execution.' )

  return

def fern_chaos ( n = 10000 ):

#*****************************************************************************80
#
## fern_chaos() displays the Barnsley fractal fern.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2022
#
#  Author:
#
#    Original code by Cleve Moler.
#    This version by John Burkardt.
#
#  Reference:
#
#    Michael Barnsley,
#    Fractals Everywhere,
#    Academic Press, 1988,
#    ISBN: 0120790696,
#    LC: QA614.86.B37.
#
#    Cleve Moler,
#    Experiments with MATLAB,
#    ebook: https://www.mathworks.com/moler/exm/index.html
#
#  Input:
#
#    integer N, the number of points to display.
#    A value of 10,000 or so is enough to see the fern.
#    For values of 500 or less, larger dots are displayed to suggest
#    how the plot is drawn.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  rng = default_rng ( )

  prob = np.array ( [ 0.85, 0.92, 0.99, 1.00 ] )
#
#  Compute the points.
#
  p = np.zeros ( [ n, 2 ] )

  p[0,0:2] = rng.random ( size = 2 )

  for i in range ( 1, n ):

    r = rng.random ( 1 )

    if ( r < prob[0] ):
      p[i,0] =   0.85 * p[i-1,0] + 0.04 * p[i-1,1] + 0.0
      p[i,1] = - 0.04 * p[i-1,0] + 0.85 * p[i-1,1] + 1.6
    elif ( r < prob[1] ):
      p[i,0] =   0.20 * p[i-1,0] - 0.26 * p[i-1,1] + 0.0
      p[i,1] =   0.23 * p[i-1,0] + 0.22 * p[i-1,1] + 1.6
    elif ( r < prob[2] ):
      p[i,0] = - 0.15 * p[i-1,0] + 0.28 * p[i-1,1] + 0.0
      p[i,1] =   0.26 * p[i-1,0] + 0.24 * p[i-1,1] + 0.44
    else:
      p[i,0] =   0.00 * p[i-1,0] + 0.00 * p[i-1,1] + 0.0
      p[i,1] =   0.00 * p[i-1,0] + 0.16 * p[i-1,1] + 0.0
#
#  Plot the points as small green dots.
#
  if ( n <= 500 ):
    dot_size = 5
  else:
    dot_size = 1

  plt.clf ( )
  plt.plot ( p[:,0], p[:,1], 'g.', markersize = dot_size )
  plt.axis ( 'equal' )
  plt.title ( 'Fractal Fern, N = ' + str ( n ) )
  filename = 'fern_chaos.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

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
  fern_chaos_test ( )
  timestamp ( )

