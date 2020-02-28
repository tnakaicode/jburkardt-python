#! /usr/bin/env python3
#
def predator_plot3d ( ):

#*****************************************************************************80
#
## predator_plot3d computes and plots some predator/prey data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D

  print ( '' )
  print ( 'predator_plot3d:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Model the interaction between rabbits and foxes.' )
#
#  Define N points (X,Y,Z) along a curve.
#
  n = 1001
  dt = ( 5.0 - 0.0 ) / float ( n - 1 )

  t = np.zeros ( n )
  prey = np.zeros ( n )
  pred = np.zeros ( n )

  t[0] = 0.0
  prey[0] = 5000.0
  pred[0] = 100.0

  for i in range ( 1, n ):
    t[i] = t[i-1] + dt
    prey[i] = prey[i-1] + dt * (    2.0 * prey[i-1] - 0.001 * pred[i-1] * prey[i-1] )
    pred[i] = pred[i-1] + dt * ( - 10.0 * pred[i-1] + 0.002 * pred[i-1] * prey[i-1] )
#
#  Save the data to a file.
#
  filename = 'predator_data.txt'
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g  %g  %g\n' % ( t[i], prey[i], prey[i] )
    output.write ( s )

  output.close ( )

  print ( '' )
  print ( '  Data saved as "%s"' % ( filename ) )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( prey, pred, t, linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- Prey -->', fontsize = 16 )
  ax.set_ylabel ( '<-- Predator -->', fontsize = 16 )
  ax.set_zlabel ( '<-- Time -->', fontsize = 16 )
  ax.set_title ( 'Predator/prey evolution', fontsize = 16 )
  
  filename = 'predator_plot3d.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'predator_plot3d' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  predator_plot3d ( )
  timestamp ( )
