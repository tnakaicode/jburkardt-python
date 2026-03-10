#! /usr/bin/env python3
#
def curve_animation ( ):

#*****************************************************************************80
#
## curve_animation() uses FuncAnimation() to animate the drawing of two curves.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.animation as animation
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'curve_animation():' )
  print ( '  Use FuncAnimation() to animate the drawing of two curves.' )

  fig, ax = plt.subplots()
  t = np.linspace ( 0.0, 3.0, 31 )

  g = -9.81
  v0 = 12.0
  z = g * t**2 / 2 + v0 * t

  v02 = 5.0
  z2 = g * t**2 / 2 + v02 * t
#
#  Define the initial states of scat, a scatter plot, and line2,
#  a line plot.
#
  scat = ax.scatter ( t[0], z[0], c = "b", s = 5, \
    label = 'v0 = ' + str ( v0 ) +'m/s' )
  line2 = ax.plot ( t[0], z2[0], \
    label = f'v0 = ' + str ( v02 ) + 'm/s')[0]
#
#  Define properties of the plot axis.
#
  ax.set ( xlim = [ 0.0, 3.0 ], \
           ylim = [ -4.0, 10.0 ], \
           xlabel = 'Time [s]', \
           ylabel = 'Z [m]')
  ax.legend ( )
  ax.grid ( True )
#
#  If FuncAnimation() is called within a function, then update()
#  has to be defined within the function, and before the call to
#  FuncAnimation().
#
  def update ( frame ):
#
## update() updates the information in the next plot frame.
#
#  Input:
#
#    integer frame: the index of the current frame.
#
#  Output:
#
#    scat, line2: the information defining the scatterplot and line plot.
#

#
#  Update the x and y data.
#  In this case, it's just one more entry of the t, z, and z2 vectors.
#
    x = t[:frame]
    y = z[:frame]
    y2 = z2[:frame]
#
#  Update the scatter plot data:
#
    data = np.stack ( [ x, y ] ).T
    scat.set_offsets ( data )
#
#  Update the line plot data:
#
    line2.set_xdata ( x )
    line2.set_ydata ( y2 )
#
#  Return the updated information as a (tuple).
#
    return ( scat, line2 )
#
#  Call FuncAnimation to create the animation by repeated calls to update.
#
  ani = animation.FuncAnimation ( \
    fig = fig, \
    func = update, \
    frames = 31, \
    interval = 30, \
    repeat = False )

  filename = 'curve_animation.mp4'
  ani.save ( filename )

  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'curve_animation():' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  curve_animation ( )
  timestamp ( )

