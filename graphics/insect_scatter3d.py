#! /usr/bin/env python3
#
def insect_scatter3d ( ):

#*****************************************************************************80
#
## insect_scatter3d makes a 3D scatter plot.
#
#  Discussion:
#
#    For each of three insect species, there is a data file.
#
#    Each data file reports three measurements on 10 individuals
#    in the species, the first tarsus, second tarsus, and maximum
#    width of aedeagus.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 May 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  import numpy as np
  import platform

  print ( '' )
  print ( 'insect_scatter3d:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Create a 3D scatter plot of measurements of three' )
  print ( '  physical characteristics of 3 species of insects.' )
#
#  Read three sets of data:
#
  filename = 'insect_a_data.txt'
  a_data = np.loadtxt ( filename )
  filename = 'insect_b_data.txt'
  b_data = np.loadtxt ( filename )
  filename = 'insect_c_data.txt'
  c_data = np.loadtxt ( filename )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.scatter ( a_data[:,0], a_data[:,1], a_data[:,2], color = 'r' )
  ax.scatter ( b_data[:,0], b_data[:,1], b_data[:,2], color = 'g' )
  ax.scatter ( c_data[:,0], c_data[:,1], c_data[:,2], color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<-- First Tarsus -->', fontsize = 16 )
  ax.set_ylabel ( '<-- Second Tarsus -->', fontsize = 16 )
  ax.set_zlabel ( '<-- Max Aedeagus -->', fontsize = 16 )
  ax.set_title ( 'Sample Measurements of 3 Insect Species', fontsize = 16 )
  filename = 'insect_scatter3d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'insect_scatter3d' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  insect_scatter3d ( )
  timestamp ( )
 
