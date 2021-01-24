#! /usr/bin/env python3
#
def track_bar ( ):

#*****************************************************************************80
#
## track_bar makes a bar plot of eye-tracking data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'track_bar:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read a text file containing durations' )
  print ( '  representing results of an eye-tracking experiment.' )
  print ( '  Make a bar plot of the results, with labeled bars.' )
#
#  Read the values from the file.
#
  filename = 'track_data.txt'
  data = np.loadtxt ( filename )
  duration = data[:]
  n = len ( duration )
  region = np.arange ( n )
#
#  Create the bar plot.
#
  plt.bar ( region, duration )
  plt.grid ( True )
  plt.title ( 'Fixation Duration to Eye Region', fontsize = 16 )
  plt.xlabel ( 'Eye Region', fontsize = 16 )
  plt.ylabel ( 'Duration (msec)', fontsize = 16 )
  plt.xticks ( region, ( 'anger', 'disgust', 'fear', 'happy', 'sad', 'surprise' ) )
  filename = 'track_bar.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'track_bar:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  track_bar ( )
  timestamp ( )

