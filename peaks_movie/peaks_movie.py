#! /usr/bin/env python3
#
def peaks_movie_test ( ):

#*****************************************************************************80
#
## peaks_movie_test() tests peaks_movie().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'peaks_movie_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test peaks_movie().' )
#
#  Generate the frames.
#
  frame_max = 40
  make_frames ( frame_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'peaks_movie_test():' )
  print ( '  Normal end of execution.' )

  return

def filename_inc ( filename ):

#*****************************************************************************80
#
## filename_inc() generates the next filename in a series.
#
#  Discussion:
#
#    It is assumed that the digits in the name, whether scattered or
#    connected, represent a number that is to be increased by 1 on
#    each call.  If this number is all 9's on input, the output number
#    is all 0's.  Non-numeric letters of the name are unaffected..
#
#    If the name is empty, then the routine stops.
#
#    If the name contains no digits, the empty string is returned.
#
#  Example:
#
#      Input            Output
#      -----            ------
#      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
#      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
#      'a9to99.txt'     'a0to00.txt'  (wrap around)
#      'cat.txt'        ' '           (no digits in input name.)
#      ' '              STOP!         (error.)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the string to be incremented.
#
#  Output:
#
#    string FILENAME, the incremented string.
#
  i0 = ord ( '0' )
  i8 = ord ( '8' )
  i9 = ord ( '9' )

  lens = len ( filename )

  if ( lens <= 0 ):
    return None

  change = 0
  filename2 = ''

  for i in range ( lens - 1, -1, -1 ):

    c = filename[i]

    ic = ord ( c )

    if ( change < 2 and i0 <= ic and ic <= i8 ):
      ic = ic + 1
      filename2 = chr ( ic ) + filename2
      change = 2
    elif ( change == 0 and ic == i9 ):
      change = 1
      c = '0'
      filename2 = c + filename2
    else:
      filename2 = c + filename2

  if ( change == 0 ):
    filename2 = None

  return filename2

def make_frame ( frame_id, frame_max, filename ):

#*****************************************************************************80
#
## make_frame() makes a particular frame of an animation.
#
#  Discussion:
#
#    Making frames from 0 to frame_max will create a sequence of JPG
#    files that constitute the frames of an animation, in which a
#    "hilly" plot gradually flattens out.
#
#    QUICKTIME is one program that can collect these individual frames into
#    a single animation file.
#
#    The value of frame_max does not really limit the possible values
#    of FRAME_ID.  It is simply the value at which the plot first returns to
#    its initial state.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer FRAME_ID, the index of the frame to be created.
#
#    integer frame_max, the index of the last frame in the sequence.
#
#    string filename: the filename to be used in storing this frame.
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  import numpy as np

  x = np.linspace ( -3.0, 3.0, 49 )
  y = np.linspace ( -3.0, 3.0, 49 )
  X, Y = np.meshgrid ( x, y )
#
#  PEAKS returns a 49 x 49 matrix of data that can be plotted
#  as a surface.
#
  Z = peaks ( X, Y )
#
#  Force all frames to share the same axis.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( X, Y, Z, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  az = 5.0
  az = frame_id * 5.0
  el = 40.0
  ax.view_init ( elev = el, azim = az )
  ax.set_title ( 'Peak movie', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return
 
def make_frames ( frame_max ):

#*****************************************************************************80
#
## make_frames() makes the frames of an animation.
#
#  Discussion:
#
#    This program makes JPEG files 0 through frame_max, which constitute
#    individual frames of an animation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer frame_max: the program will create frames 0 through frame_max.
#
  print ( '' )
  print ( 'make_frames()' )
  print ( '  Create a sequence of JPG image files,' )
  print ( '  each containing one frame of a potential animation.' )

  print ( '' )
  print ( '  This program has been asked to create' )
  print ( '  frames 0 through', frame_max )

  filename = 'peaks_frame0000.png'
  for frame_id in range ( 0, frame_max + 1 ):
    make_frame ( frame_id, frame_max, filename )
    filename = filename_inc ( filename )

  return

def peaks ( x, y ):

#*****************************************************************************80
#
## peaks() evaluates the peaks function.
#
#  Discussion:
#
#    peaks() is a MATLAB library function used for various demonstrations
#    including the creation of contour plots and optimization.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x, y: evaluation points.
#
#  Output:
#
#    real z: the value of peaks(x,y).
#
  import numpy as np

  e1 = - x**2 - ( y + 1.0 )**2
  e2 = - x**2 - y**2
  e3 = - ( x + 1.0 )**2 - y**2

  z = 3.0 * ( 1.0 - x**2 )             * np.exp ( e1 ) \
    - 10.0 * ( x / 5.0 - x**3 - y**5 ) * np.exp ( e2 ) \
    - 1.0 / 3.0                        * np.exp ( e3 )

  return z

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
  peaks_movie_test ( )
  timestamp ( )

