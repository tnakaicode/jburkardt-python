#! /usr/bin/env python3
#
def sphere_sample ( n, dim_num ):

#*****************************************************************************80
#
## sphere_sample() samples points on the unit sphere in 3D.
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
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    George Marsaglia,
#    Choosing a point from the surface of a sphere,
#    Annals of Mathematical Statistics,
#    Volume 43, Number 2, April 1972, pages 645-646.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 234.
#
#  Input:
#
#    integer N, the number of points.
#
#    integer DIM_NUM, the spatial dimension.
#
#  Output:
#
#    real X(N,DIM_NUM), the points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = rng.standard_normal ( size = ( n, dim_num ) )
  v = np.linalg.norm ( x, axis = 1 )
  for j in range ( 0, dim_num ):
    x[:,j] = x[:,j] / v

  return x

def svd_sphere ( A ):

#*****************************************************************************80
#
## svd_sphere() plots the images of sphere points under the 3x3 matrix A.
#
#  Discussion:
#
#    The horrid documentation for Axes3D makes it impossible to figure
#    how to present the resulting plot with equal aspect ratios.
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
#    real A(3,3), the matrix whose mapping of the unit sphere is to be studied.
#
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'svd_sphere():' )
  print ( '  Given a 3x3 matrix A, plot points x on the unit sphere, and' )
  print ( '  the images A*x of those points.' )
  print ( '  Show right singular vectors V' )
  print ( '  and their images, the scaled left singular vectors U.' )
  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
#
#  Get the SVD.
#
  U, svec, V = np.linalg.svd ( A )

  print ( '  Singular values of A:' )
  print ( svec )
  print ( '  Right singular vectors are rows of V:' )
  print ( V )
  print ( '  Left singular vectors are columns of U:' )
  print ( U )
#
#  Select points on the surface of the unit sphere.
#
  n = 500
  dim_num = 3
  x = sphere_sample ( n, dim_num )
#
#  ATX contains the image of each point under the mapping X -> A*X.
#
  atx = np.dot ( A, x.T )
#
#  Determine a common plot range.
#
  p_min = min ( np.min ( atx ), np.min ( x ) )
  p_max = max ( np.max ( atx ), np.max ( x ) )
#
#  Plot the corners of the region.  This is a trick to force MATLAB
#  to plot in a square with equal axes.  
#
  fig1 = plt.figure ( )
  ax1 = fig1.add_subplot ( 111, projection = '3d' )

  ax1.scatter ( x[:,0], x[:,1], x[:,2], 'b' );
#
#  Plot V1 and V2.  NEED TO TRANSPOSE THESE!
#
  ax1.plot3D ( [ 0, V[0,0]], [ 0, V[0,1]], [ 0, V[0,2]], 'b', linewidth = 3 )
  ax1.plot3D ( [ 0, V[1,0]], [ 0, V[1,1]], [ 0, V[1,2]], 'b', linewidth = 3 )
  ax1.plot3D ( [ 0, V[2,0]], [ 0, V[1,2]], [ 0, V[2,2]], 'b', linewidth = 3 )

  ax1.set_xlabel ( '--X axis--' )
  ax1.set_ylabel ( '--Y axis--' )
  ax1.set_zlabel ( '--Z axis--' )
  ax1.set_title ( 'Sphere points, Right singular vectors' )
  ax1.grid ( True )
  filename = 'svd_sphere_1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Label the points ATX on the image of the unit circle.
#
  fig2 = plt.figure ( )
  ax2 = fig2.add_subplot ( 111, projection = '3d' )

  ax2.scatter ( atx[0,:], atx[1,:], atx[2,:], 'r' );
#
#  Plot the images of V1 and V2.
#
  ax2.plot3D ( \
    [ 0, svec[0]*U[0,0]], \
    [ 0, svec[0]*U[1,0]], \
    [ 0, svec[0]*U[2,0]], 'r', linewidth = 3 )
  ax2.plot3D ( \
    [ 0, svec[1]*U[0,1]], \
    [ 0, svec[1]*U[1,1]], \
    [ 0, svec[1]*U[2,1]], 'r', linewidth = 3 )
  ax2.plot3D ( \
    [ 0, svec[2]*U[0,2]], \
    [ 0, svec[2]*U[1,2]], \
    [ 0, svec[2]*U[2,2]], 'r', linewidth = 3 )

  ax2.set_xlabel ( '--X axis--' )
  ax2.set_ylabel ( '--Y axis--' )
  ax2.set_xlabel ( '--Z axis--' )
  ax2.set_title ( 'Sphere point images, scaled left singular vectors' )
  ax2.grid ( 'True' )
  filename = 'svd_sphere_2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def svd_sphere_test ( ):

#*****************************************************************************80
#
## svd_sphere_test() tests svd_sphere().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'svd_sphere_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test svd_sphere().' )

  A = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  svd_sphere ( A )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_sphere_test():' )
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
  svd_sphere_test ( )
  timestamp ( )

