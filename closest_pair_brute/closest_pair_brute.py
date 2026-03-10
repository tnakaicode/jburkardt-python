#! /usr/bin/env python3
#
def closest_pair_brute_test ( ):

#*****************************************************************************80
#
## closest_pair_brute_test() tests closest_pair_brute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'closest_pair_brute_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test closest_pair_brute().' )
#
#  Solve a sequence of problems of increasing size N.
#
  nvec = np.array ( [ 100, 200, 400, 800, 1600, 3200 ] )
  svec = np.zeros ( 6 )
  for i in range ( 0, 6 ):
    svec[i] = closest_pair_brute_test01 ( nvec[i] )

  plt.clf ( )
  plt.plot ( nvec, svec, '-o', linewidth = 2 )
  plt.grid ( 'on' )
  plt.xlabel ( 'Number of data points' )
  plt.ylabel ( 'Execution time (seconds)' )
  plt.title ( 'Time complexity for closest pair problem' )
  filename = 'closest_pair_brute.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'closest_pair_brute_test():' )
  print ( '  Normal end of execution.' )

  return

def closest_pair_brute_test01 ( n ):

#*****************************************************************************80
#
## closest_pair_brute_test01() tests the closest_pair_brute program.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of points.
#
#  Output:
#
#    real s: execution time in seconds.
#
  from numpy.random import default_rng
  from time import time

  print ( '' )
  print ( 'closest_pair_brute_test01():' )
  print ( '  closest_pair_brute() on a set of N points in 2D.' )

  rng = default_rng ( )
  xy = rng.random ( size = [ n, 2 ] )

  s = time ( )
  d, i, j = closest_pair_brute ( xy )
  s = time ( ) - s

  print ( '' )
  print ( '  n = ', n )
  print ( '  time = ', s, ' seconds' )
  print ( '  xy(', i, ') = ', xy[i,:] )
  print ( '  xy(', j, ') = ', xy[j,:] )
  print ( '  ||xy(',i,')-xy(',j,')|| =', d )

  return s

def closest_pair_brute ( xy ):

#*****************************************************************************80
#
## closest_pair_brute() finds closest pair of points in 2d using brute force.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2024
#
#  Author:
#
#    Original MATLAB code by Cleve Moler.
#    This version by John Burkardt.
#
#  Reference:
#
#    Cleve Moler,
#    https://blogs.mathworks.com/cleve/2024/03/28/closest-pair-of-points-problem/
#    Closest pair of points problem,
#    28 March 2024.
#
#  Input:
#
#    real xy(n): the X and Y coordinates of the points.
#
#  Output:
#
#    real d: the distance of the closest pair.
#
#    integer i, j: the indices of the closest pair.
#
  import numpy as np

  n = len ( xy )
  d = np.inf
  i = -1
  j = -1

  for i2 in range ( 0, n ):
    for j2 in range ( i2 + 1, n ):
      d2 = np.linalg.norm ( xy[i2,:] - xy[j2,:] )
      if ( d2 < d ):
        d = d2
        i = i2
        j = j2

  return d, i, j

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
  closest_pair_brute_test ( )
  timestamp ( )

