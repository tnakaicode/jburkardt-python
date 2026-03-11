#! /usr/bin/env python3
#
def contour_himmelblau_test ( ):

#*****************************************************************************80
#
## contour_himmelblau_test() draws a contour plot of the Himmelblau function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  from matplotlib import cm

  print ( '' )
  print ( 'contour_himmelblau_test():' )
  print ( '  Draw a contour plot of the Himmelblau function.' )

  x = np.linspace ( -5.0, 5.0, 51 )
  y = np.linspace ( -5.0, 5.0, 51 )
  X, Y = np.meshgrid ( x, y )  
  Z = ( X**2 + Y - 11.0 )**2 + ( X + Y**2 - 7.0 )**2
#
#  Form the figure.
#
  plt.clf ( )
  levels = 35
  plt.contourf ( X, Y, Z, levels, cmap = cm.OrRd )
  plt.colorbar ( )
  plt.contour ( X, Y, Z, levels, colors = 'black' )
  plt.title ( 'The Himmelblau function' )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  filename = 'contour_himmelblau_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

if ( __name__ == '__main__' ):
  contour_himmelblau_test ( )

