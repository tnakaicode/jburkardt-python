#! /usr/bin/env python3
#
def drum_normal_modes_test ( ):

#*****************************************************************************80
#
## drum_normal_modes_test() computes and plots normal vibration modes of a drumhead.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    Original python version by Christian Hill.
#    This version by John Burkardt.
#
#  Reference:
#
#    Christian Hill,
#    Learning Scientific Programming with Python,
#    Cambridge University Press,
#    Second Edition, 2020,
#    ISBN: 978-1108745918
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'drum_normal_modes_test():' )
  print ( '  Display normal modes of a vibrating drumhead.' )
#
#  Set maximum normal mode allowed.
#
  r = np.linspace ( 0.0, 1.0, 101 )
  theta = np.linspace ( 0.0, 2.0 * np.pi, 101 )

  R, T = np.meshgrid ( r, theta )
  X = R * np.cos ( T )
  Y = R * np.sin ( T )

  n = 3
  m = 4
  Z = R * displacement ( n, m, R, T )

  plot_contour ( X, Y, Z )
  plot_contourf ( X, Y, Z )
  plot_surface ( X, Y, Z )

  return

def plot_contour ( X, Y, Z ):

#*****************************************************************************80
#
## plot_contour() plots contour lines.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.contour ( X, Y, Z )
  plt.axis ( 'equal' )
  filename = 'drum_contour.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def plot_contourf ( X, Y, Z ):

#*****************************************************************************80
#
## plot_contourf() plots filled contours.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.contourf ( X, Y, Z )
  plt.contour ( X, Y, Z, colors = 'white' )
  plt.axis ( 'equal' )
  filename = 'drum_contourf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def plot_surface ( X, Y, Z ):

#*****************************************************************************80
#
## plot_surface() plots a 3D surface.
#
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import matplotlib.pyplot as plt

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  p = ax.plot_surface ( X, Y, Z, \
    cmap = cm.coolwarm, edgecolor = 'none' )
# ax.set ( 'equal' )
  fig.colorbar ( p, ax = ax )
  filename = 'drum_surface.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def displacement ( n, m, r, theta ):

#*****************************************************************************80
#
## displacement() calculates the drum displacement at (r,theta)
#
  import numpy as np
  from scipy.special import jn
  from scipy.special import jn_zeros

  bessel_zeros = jn_zeros ( n, m + 1 )
  k = bessel_zeros[m]
  disp = np.sin ( n * theta ) * jn ( n, r * k )
  return disp

if ( __name__ == "__main__" ):
  drum_normal_modes_test ( )

