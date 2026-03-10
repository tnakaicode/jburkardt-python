#! /usr/bin/env python3
#
def gaussian_2d_test ( ):

#*****************************************************************************80
#
## gaussian_2d_test() tests gaussian_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2023
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'gaussian_2d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  gaussian_2d() evaluates a general gaussian' )
  print ( '  function of a 2D argument.' )
#
  c = 1.0

  x = np.linspace ( -5.0, 5.0, 21 )
  y = np.linspace ( -5.0, 5.0, 21 )
  X, Y = np.meshgrid ( x, y )

  xmu = 0.0
  ymu = 0.0

  xsigma = 1.0
  ysigma = 2.0

  A = np.array ( [ \
    [ 5, 1 ], \
    [ 1, 2 ] ], dtype = float )

  Z = gaussian_2d ( c, X, Y, xmu, ymu, xsigma, ysigma, A )

  plt.clf ( )
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, Z, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Gaussian function Z(X,Y)' )
  ax.set_xlabel ( '<--- X --->' )
  ax.set_ylabel ( '<--- Y --->' )
  ax.set_zlabel ( '<--- Z(X,Y) --->' )
  filename = 'gaussian_2d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gaussian_2d_test():' )
  print ( '  Normal end of execution.' )

  return

def gaussian_2d ( c, X, Y, xmu, ymu, xsigma, ysigma, A ):

#*****************************************************************************80
#
## gaussian_2d() evaluates a Gaussian function of a 2D argument.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C, the multiplier.
#
#    real X(M,N), Y(M,N), the evaluation points.
#
#    real XMU, YMU, the mean or center of the gaussian function.
#
#    real XSIGMA, YSIGMA, the variance.
#
#    real A(2,2), a symmetric positive definite (SPD) matrix.
#
#  Output:
#
#    real Z(M,N), the value of the gaussian function.
#
  import numpy as np

  m, n = X.shape

  x = np.reshape ( X, m * n )
  y = np.reshape ( Y, m * n )
#
#  v is a 2 * m*n array.
#
  v = np.array ( \
    [ ( x - xmu ) / xsigma, \
      ( y - ymu ) / ysigma ] )
#
#  Av = A * v is a 2 * m*n array.
#
  Av = np.dot ( A, v )
#
#  vtAv = A * v is a 1 * m*n array.
#
  vtAv = v[0,:] * Av[0,:] + v[1,:] * Av[1,:]

  z = c * np.exp ( - 0.5 * vtAv )

  Z = np.reshape ( z, ( m, n ) )

  return Z

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
  gaussian_2d_test ( )
  timestamp ( )


