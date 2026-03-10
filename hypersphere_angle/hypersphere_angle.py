#! /usr/bin/env python3
#
def hypersphere_angle_test ( ):

#*****************************************************************************80
#
## hypersphere_angle_test() tests hypersphere_angle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypersphere_angle_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypersphere_angle().' )

  for m in [ 2, 3, 5, 10, 20, 40, 80, 160 ]:
    n = 10000
    cost_mu, cost_std, theta_mu, theta_std = hypersphere_angle_stats ( m, n )
    print ( '' )
    print ( '  Spatial dimension M = ', m )
    print ( '  Number of samples N = ', n )
    print ( '  COST = absolute value of cosine between two random points:' )
    print ( '    Estimated mean = ', cost_mu )
    print ( '    Estimated std  = ', cost_std )
    print ( '  THETA = arc cosine of absolute value of cosine between two random points:' )
    print ( '    Estimated mean = ', theta_mu,  ' (radians) =', theta_mu * 180 / np.pi, ' (degrees)' )
    print ( '    Estimated std  = ', theta_std, ' (radians) =', theta_std * 180 / np.pi, ' (degrees)' )

  m_max = 100
  x = np.zeros ( m_max )
  y = np.zeros ( m_max  )
  n = 10000

  for m in range ( 1, m_max + 1 ):
    cost_mu, cost_std, theta_mu, theta_std = hypersphere_angle_stats ( m, n )
    x[m-1] = m 
    y[m-1] = theta_mu * 180.0 / np.pi

  plt.plot ( x, y, 'b-', linewidth = 3 )
  plt.xlabel ( '<-- Spatial dimension -->' )
  plt.ylabel ( '<-- Angle in degrees -->' )
  plt.title ( 'Average (positive) angle between random unit vectors' )
  plt.grid ( True )
  filename = 'hypersphere_angle.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypersphere_angle_test():' )
  print ( '  Normal end of execution.' )

  return

def hypersphere_angle_stats ( m, n ):

#*****************************************************************************80
#
## hypersphere_angle_stats() estimates unit hypersphere angle statistics.
#
#  Discussion:
#
#    Select two points at random on the unit hypersphere.
#    Compute the absolute value of the cosine of the angle between them.
#    Compute the angle corresponding to this nonnegative cosine.
#
#    Return mean and standard deviation of the cosine and angle statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of sample points to use.
#
#  Output:
#
#    real COST_MU, COST_STD, the estimated mean and standard
#    deviation of the absolute value of the cosine of the angle between 
#    two random points on the unit hypersphere.
#
#    real THETA_MU, THETA_STD, the estimated mean and standard
#    deviation of the (nonnegative) angle between two random points on 
#    the unit hypersphere.  
#
  import numpy as np

  cost = np.zeros ( n )

  for i in range ( 0, n ):
    p = hypersphere_unit_sample ( m )
    q = hypersphere_unit_sample ( m )
    cost[i] = np.abs ( np.dot ( p, q ) )

  cost_mu = np.mean ( cost )
  cost_std = np.std ( cost )

  theta_mu = np.mean ( np.arccos ( cost ) )
  theta_std = np.std ( np.arccos ( cost ) )
  
  return cost_mu, cost_std, theta_mu, theta_std

def hypersphere_unit_sample ( m ):

#*****************************************************************************80
#
## hypersphere_unit_sample() returns sample points on the unit hypersphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 232.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real X(M,1), the point.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = rng.standard_normal ( size = m )
#
#  Normalize the vector.
#
  x = x / np.linalg.norm ( x )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  hypersphere_angle_test ( )
  timestamp ( )

