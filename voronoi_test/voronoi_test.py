#! /usr/bin/env python3
#
def voronoi_test ( ):

#*****************************************************************************80
#
## voronoi_test() tests voronoi() and voronoi_plot_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2016
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  from scipy.spatial import Voronoi
  from scipy.spatial import voronoi_plot_2d
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'voronoi_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy.spatial.Voronoi computes the Voronoi diagram of a set of points.' )
  print ( '  scipy.spatial.voronoi_plot_2d will plot it.' )

  rng = default_rng ( )
#
#  Select the points.
#
  nc = 25
  xy = rng.random ( size = [ nc, 2 ] )
#
#  Compute the diagram.
#
  diagram = Voronoi ( xy )
#
#  Plot the diagram.
#
  voronoi_plot_2d ( diagram )
#
#  Save the plot.
#
  filename = 'voronoi_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'voronoi_test():' )
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
  import numpy as np
  timestamp ( )
  voronoi_test ( )
  timestamp ( )

