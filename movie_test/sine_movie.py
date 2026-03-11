#! /usr/bin/env python3
#
def sine_movie ( ):

#*****************************************************************************80
#
## sine_movie() creates a movie in which a red ball traces a sine curve.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2023
#
#  Author:
#
#    Original Python version by Qingkai Kong, Timmy Siauw, Alexandre Bayen.
#    This version by John Burkardt.
#
#  Reference:
#
#    Qingkai Kong, Timmy Siauw, Alexandre Bayen, 
#    Python Programming and Numerical Methods,
#    Academic Press, 2022,
#    ISBN: 978-0-12-819549-9
#
  import matplotlib.pyplot as plt
  import matplotlib.animation as manimation
  import numpy as np
  import platform

  print ( '' )
  print ( 'sine_movie():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Create a movie of a red ball tracing a sine curve.' )

  n = 1000
  x = np.linspace ( 0, 6 * np.pi, n )
  y = np.sin ( x )
#
#  Define the meta data for the movie.
#
  FFMpegWriter = manimation.writers [ 'ffmpeg' ]

  metadata = dict ( \
    title = 'sine_movie()', \
    artist = 'Matplotlib',
    comment = 'A red circle traces a blue sine wave' )

  writer = FFMpegWriter ( fps = 15, metadata = metadata )
#
#  Initialize the movie.
#
  fig = plt.figure ( )
#
#  Create a graphical rendering of the sine curve.
#  Because we are saving a reference to the sine curve, we need to 
#  follow "sine_line" by a comma, since it's the first object returned
#  (even though it's actually the ONLY object returned in this case).
#
# sine_line, = plt.plot ( x, y, 'b' )
#
#  Create a graphical rendering of the red circle.
#  We give it empty coordinates for now, and will locate it later
#  with "set_data".
#
  red_circle, = plt.plot ( [], [], 'ro', markersize = 10 )
#
#  Label the plot.
#
  plt.xlabel ( 'x' )
  plt.ylabel ( 'sin(x)' )
#
#  Add grid lines.
#
  plt.grid ( True )
#
#  Specify the plot limits.
#
  plt.xlim ( 0.0, 6.0 * np.pi )
  plt.ylim ( -1.0, +1.0 )
#
#  Update the frames for the movie
#
  dpi = 100

  with writer.saving ( fig, "sine_movie.mp4", dpi ):

    announce = 0
    for i in range ( n ):
      if ( i == announce or i == n - 1 ):
        print ( '  Frame', i )
        announce = announce + n // 10
#
#  Plot part of the sine curve.
#
      plt.plot ( x[0:i+1], y[0:i+1], 'b' )
#
#  Update the location of the red circle.
#
      x0 = x[i]
      y0 = y[i]
      red_circle.set_data ( x0, y0 )
#
#  Grab the current frame.
#
      writer.grab_frame ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_movie():' )
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

if ( __name__ == "__main__" ):
  timestamp ( )
  sine_movie ( )
  timestamp ( )


