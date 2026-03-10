#! /usr/bin/env python3
#
def cvt_circle_uniform_test ( ):

#*****************************************************************************80
#
## cvt_circle_uniform_test() tests cvt_circle_uniform().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 January 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'cvt_circle_uniform_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  cvt_circle_uniform() seeks uniformly scattered points in a circle.' )

  point_num = 50
  sample_num = 1000
  step_num = 10
  cvt_circle_uniform ( point_num, sample_num, step_num, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'cvt_circle_uniform_test():' )
  print ( '  Normal end of execution.' )
  return

def cvt_circle_uniform ( point_num, sample_num, step_num, rng ):

#*****************************************************************************80
#
## cvt_circle_uniform() estimates a CVT on the unit circle with uniform density.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer point_num:
#
#    integer sample_num:
#
#    integer step_num:
#
#    random number generator rng:
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  For the plot, compute points along the circle boundary.
#
  boundary_num = 65
  boundary_theta = np.linspace ( 0.0, 2.0 * np.pi, boundary_num )
  boundary_x = np.cos ( boundary_theta )
  boundary_y = np.sin ( boundary_theta )
#
#  Now take CVT steps 0, 1, ..., step_num.
#
  for step in range ( 0, step_num + 1 ):
#
#  Step 0, initialize
#
    if ( step == 0 ):
      p = circle_sample ( point_num, rng )
#
#  Step 1 to step_num: 
#    compute sample points S
#    for each S, find K, index of nearest point P.
#    replace P by average of P and nearest sample points.
#
    else:
      s = circle_sample ( sample_num, rng )

      k = [ np.argmin ( \
        [ np.inner ( point - sample, point - sample ) \
        for point in p ] ) for sample in s ]

      w = np.ones ( sample_num )
      m = np.bincount ( k, weights = w )
      p[:,0] = ( np.bincount ( k, weights = s[:,0] ) + p[:,0] ) / ( m[:] + 1 )
      p[:,1] = ( np.bincount ( k, weights = s[:,1] ) + p[:,1] ) / ( m[:] + 1 )
#
#  Plot points at this STEP.
#
    plt.clf ( )
    plt.plot ( boundary_x, boundary_y, 'r-', linewidth = 2 )
    plt.plot ( p[:,0], p[:,1], 'b.', markersize = 15 )
    plt.title ( 'CVT ' + str ( step ) )
    plt.axis ( 'equal' )
    plt.axis ( 'off' )
    if ( step == 0 ):
      filename = 'circle_initial.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    elif ( step == step_num ):
      filename = 'circle_final.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )

  return

def circle_sample ( n, rng ):

#*****************************************************************************80
#
## circle_sample() returns sample points inside the unit circle.
#
#  Discussion:
#
#    The unit circle has center at the origin, and radius 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 April 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of sample points requested.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real x[n,2]: the sample points.
#
  import numpy as np

  r = rng.random ( size = n )
  r = np.sqrt ( r )

  t = rng.random ( size = n )
  t = 2.0 * np.pi * t

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = r * np.cos ( t )
  x[:,1] = r * np.sin ( t )

  return x
  
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
  cvt_circle_uniform_test ( )
  timestamp ( )

