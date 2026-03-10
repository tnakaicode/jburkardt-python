#! /usr/bin/env python3
#
def fractal_coastline_test ( ):

#*****************************************************************************80
#
## fractal_coastline_test() tests fractal_coastline().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 Deeember 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fractal_coastline():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test fractal_coastline().' )
#
#  Australia
#
  australia_13 = np.loadtxt ( 'australia_13.txt' )
  coastline_display ( australia_13, 'australia_13' )

  mu = 0.10
  australia_26 = coastline_perturb ( australia_13, mu )
  coastline_display ( australia_26, 'australia_26' )

  australia_52 = coastline_perturb ( australia_26, mu )
  coastline_display ( australia_52, 'australia_52' )

  mu = 0.20
  bustralia_26 = coastline_perturb ( australia_13, mu )
  coastline_display ( bustralia_26, 'bustralia_26' )

  bustralia_52 = coastline_perturb ( bustralia_26, mu )
  coastline_display ( bustralia_52, 'bustralia_52' )
#
#  Florida.
#
  florida_16 = np.loadtxt ( 'florida_16.txt' )
  coastline_display ( florida_16, 'florida_16' )

  mu = 0.10
  florida_32 = coastline_perturb ( florida_16, mu )
  coastline_display ( florida_32, 'florida_32' )

  florida_64 = coastline_perturb ( florida_32, mu )
  coastline_display ( florida_64, 'florida_64' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fractal_coastline():' )
  print ( '  Normal end of execution.' )

  return

def coastline_display ( p, prefix ):

#*****************************************************************************80
#
## coastline_display() displays a coastline, a closed polygonal curve.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 Deeember 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    real p(n,2): the coordinates of a closed polygonal curve.
#
#    string prefix: a prefix defining the title and output filename.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.fill ( p[:,0], p[:,1], 'r' )
  plt.plot ( p[:,0], p[:,1], 'k.', markersize = 15 )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.title ( prefix )
  filename = prefix + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def coastline_perturb ( p, mu ):

#*****************************************************************************80
#
## coastline_perturb() inserts intermediate points in a closed curve.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 Deeember 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    real p(n,2): the coordinates of a closed polygonal curve.
#
#    real mu: controls the degree of peturbation.
#    0 <= mu <= 0.25 is recommended.
#
#  Output:
#
#    real q(2*n,2): the coordinates of the perturbed curve.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n, d = p.shape

  sig = mu * mu
  w = mu + sig * rng.standard_normal ( size = n )
#
#  Need to give make a double copy of w.
#
  w = np.transpose ( np.vstack ( [ w, w ] ) )
#
#  A value w = 0 returns the average of the two neighbors.
#
  perturb =  \
     0.5 * ( p                           + np.roll ( p, 1, axis = 0 ) ) \
    + w  * ( p                           + np.roll ( p, 1, axis = 0 ) ) \
    - w  * ( np.roll ( p, -1, axis = 0 ) + np.roll ( p, 2, axis = 0 ) )
#
#  Shift the sequence by one place to make it easier to merge.
#
  perturb = np.roll ( perturb, -1, axis = 0 )
#
#  Q is twice the length of P.
#  Odd values contain the original P.
#  Even values are intermediate perturbulants.
#
  q = np.zeros ( [ 2 * n, d ] )
  q[0:2*n-1:2,:] = p[:,:]
  q[1:2*n:2,:] = perturb[:,:]

  return q

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
  fractal_coastline_test ( )
  timestamp ( )

