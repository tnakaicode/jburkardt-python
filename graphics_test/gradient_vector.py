#! /usr/bin/env python3
#
def gradient_vector ( ):

#*****************************************************************************80
#
## gradient_vector() makes a vector plot of the gradient of a function f(x,y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2022
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'gradient_vector():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a vector plot of the gradient of a function z(x,y).' )
#
#  Create the mesh vectors.
#
  xvec = np.linspace ( -2.0, 2.0, 31 )
  yvec = np.linspace ( -2.0, 2.0, 31 )
#
#  Create the mesh matrices.
#
  xmat, ymat = np.meshgrid ( xvec, yvec )
#
#  Evaluate the function at the mesh points.
#
  zmat = hex_z ( xmat, ymat )
  umat, vmat = hex_grad ( xmat, ymat )
#
#  Plot
#
  plt.clf ( )

  levels = 15
  plt.contourf ( xmat, ymat, zmat, levels, cmap = cm.Pastel1 )
  plt.quiver ( xmat, ymat, -umat, -vmat )

  plt.title ( 'Contour and gradient vectors', fontsize = 16 )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  filename = 'gradient_vector.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gradient_vector():' )
  print ( '  Normal end of execution.' )
  return

def hex_z ( x, y ):

#*****************************************************************************80
#
## hex_z() evaluates the hex function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 October 2019
#
#  Input:
#
#    real x(), y(): the x and y arguments.
#
#  Output:
#
#    real z(): the function value.
#  
  z = 2.0 * x**2 - 1.05 * x**4 + x**6 / 6.0 + x * y + y**2

  return z

def hex_grad ( x, y ):

#*****************************************************************************80
#
## hex_grad() evaluates the gradient of the hex function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2022
#
#  Input:
#
#    real x(), y(): the x and y arguments.
#
#  Output:
#
#    real dzdx(), dzdy(): the gradient components.
#
  dzdx = 4.0 * x - 4.2 * x**3 + x**5 + y
  dzdy =  x + 2.0 * y

  return dzdx, dzdy

if ( __name__ == '__main__' ):
  gradient_vector ( )
 
