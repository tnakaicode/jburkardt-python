#! /usr/bin/env python3
#
def closest_pair_divcon_test ( ):

#*****************************************************************************80
#
## closest_pair_divcon_test() tests closest_pair_divcon().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'closest_pair_divcon_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test closest_pair_divcon().' )
#
#  Solve a sequence of problems of increasing size N.
#
  nvec = np.array ( [ 500, 1000, 1500, 2000, 2500, 3000 ] )
  n = len ( nvec )
  s1vec = np.zeros ( n )
  s2vec = np.zeros ( n )

  for i in range ( 0, n ):
    n = nvec[i]
    s1vec[i], s2vec[i] = closest_pair_divcon_test01 ( n )

  plt.clf ( )
  plt.plot ( nvec, s1vec, '-ro', linewidth = 2 )
  plt.plot ( nvec, s2vec, '-bo', linewidth = 2 )
  plt.grid ( 'on' )
  plt.xlabel ( 'Number of data points' )
  plt.ylabel ( 'Execution time (seconds)' )
  plt.title ( 'Time complexity for closest pair problem' )
  plt.legend ( [ 'brute()', 'divcon()' ] )
  filename = 'closest_pair_divcon.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'closest_pair_divcon_test():' )
  print ( '  Normal end of execution.' )

  return

def closest_pair_divcon_test01 ( n ):

#*****************************************************************************80
#
## closest_pair_divcon_test01() tests closest_pair_divcon().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2024
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
#    real s1, s2: execution time in seconds for brute() and divcon().
#
  from numpy.random import default_rng
  import time

  rng = default_rng ( )
  z = rng.random ( size = [ n, 2 ] )

  s1 = time.time ( )
  d, i, j = brute ( z )
  s1 = time.time ( ) - s1

  s2 = time.time ( )
  d, i, j = divcon ( z )
  s2 = time.time ( ) - s2

  print ( '' )
  print ( '  Points n = ', n )
  print ( '  brute() time = ', s1, ' seconds' )
  print ( '  divcon time  = ', s2, ' seconds' )
  print ( '  z(', i, ') = ', z[i,:] )
  print ( '  z(', j, ') = ', z[j,:] )
  print ( '  ||z(', i, ')-z(', j, ')|| = ', d )

  return s1, s2

def brute ( z ):

#*****************************************************************************80
#
## brute() finds closest pair of points in 2d using brute force.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2024
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
#    real z[n,2]: the X and Y coordinates of n points.
#
#  Output:
#
#    real d: the distance of the closest pair.
#
#    integer i, j: the indices of the closest pair.
#
  import numpy as np

  n = len ( z )
  d = np.inf 
  i = -1
  j = -1

  for i2 in range ( 0, n ):
    for j2 in range ( i2 + 1, n ):
      d2 = np.linalg.norm ( z[i2,:] - z[j2,:] )
      if ( d2 < d ):
        d = d2
        i = i2
        j = j2

  return d, i, j

def center_strip ( z, din ):

#*****************************************************************************80
#
## center_strip() examines the strip of half-width d about the center point.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2024
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
#    real z[n,2]: the X and Y coordinates of the points.
#
#    real din: the width of the center strip.
#
#  Output:
#
#    real d: the distance of the closest pair in the strip.
#
#    integer kout, jout: the indices of the closest pair in the strip.
#
  import numpy as np

  n = len ( z )
  m = n // 2
  xh = z[m,0]
  d = din
#
#  It's hard to believe that the output of argsort() works this way.
#
  p = np.argsort ( z[:,1] )
  z = z[p]
#
#  Collect points S in the strip.
#  Careful to use append() correctly here.
#
  s = np.zeros ( [ 0, 2 ] )
  ks = np.zeros ( 0, dtype = int )
  ns = 0
  for k in range ( 0, n ):
    if ( np.abs ( z[k,0] - xh ) < d ):
      s = np.append ( s, [z[k,:]], axis = 0 )
      ks = np.append ( ks, [ k ] )
      ns = ns + 1
#
#  Now check pairs in the strip.
#
  kout = np.nan
  jout = np.nan
  for k in range ( 0, ns ):
    for j in range ( k + 1, ns ):
      if ( ( s[j,1] - s[k,1] ) < d and \
          np.linalg.norm ( s[k,:] - s[j,:] ) < d ):
        d = np.linalg.norm  ( s[j,:] - s[k,:] )
        kout = p[ks[k]]
        jout = p[ks[j]]

  return d, kout, jout

def divcon ( z, p = None ):

#*****************************************************************************80
#
## divcon() finds the closest pair of points in 2d using divide and conquer.
#
#  Discussion:
#
#    The algorithm is recursive, and uses an auxilliary function center_strip()
#    to examine the center strip.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2024
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
#    real z[n,2]: the X and Y coordinates of the points.
#
#    integer p(n): an index of the points, sorted by the real part,
#    which is generally not included in the user level call, but is
#    internally generated on the first call and passed to the recursive
#    calls.
#
#  Output:
#
#    real d: the distance of the closest pair.
#
#    integer i, j: the indices of the closest pair.
#
  import numpy as np

  n = len ( z )

  if ( n <= 3 ):
    d, kout, jout = brute ( z )
    return d, kout, jout
#
#  Sort Z=(x,y) based on x.
#  It's hard to believe that the output of argsort() works this way.
#
  if ( p is None ):
    p = np.argsort ( z[:,0] )
    z = z[p]
  else:
    p = np.arange ( 0, n, dtype = int )

  m = n // 2
#
#  Left half.
#
  dl, kl, jl = divcon ( z[0:m,:], True )
#
#  Right half.
#
  dr, kr, jr = divcon ( z[m:,:], True )
#
#  Remember the better of the left and right results.
#
  if ( dl < dr ):
    d = dl 
    k = kl
    j = jl
  else:
    d = dr
    k = kr + m
    j = jr + m
#
#  Center strip.
#
  ds, ks, js = center_strip ( z, d )

  if ( ds < d ):
    d = ds
    k = ks
    j = js

  kout = min ( p[k], p[j] )
  jout = max ( p[k], p[j] )

  return d, kout, jout

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
  closest_pair_divcon_test ( )
  timestamp ( )

