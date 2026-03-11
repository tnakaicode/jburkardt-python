#! /usr/bin/env python3
#
def lissajous_test ( ):

#*****************************************************************************80
#
## lissajous_test() tests lissajous().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lissajous_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Display a Lissajous figure, using N points, of the form:' )
  print ( '    x(i) = sin ( A1 * t + B1 ).' )
  print ( '    y(i) = sin ( A2 * t + B2 ).' )
  print ( '  for 0 <= t <= TSTOP.' )

  a1 = 5.0
  b1 = np.pi / 2.0
  a2 = 4.0
  b2 = 0.0
  tstop = 2.0 * np.pi
  n = 500

  lissajous ( a1, b1, a2, b2, tstop, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'lissajous_test():' )
  print ( '  Normal end of execution.' )

  return

def lissajous ( a1, b1, a2, b2, tstop, n ):

#*****************************************************************************80
#
## lissajous() draws a Lissajous curve.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real a1, b1, a2, b2: the parameters in the Lissajous curve.
#
#    real tstop: the final value of t.
#
#    integer n: the number of points to draw.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lissajous_plot():' )
#
#  Generate the data.
#
  t1 = 0.0
  t = np.linspace ( t1, tstop, n )
  x = np.sin ( a1 * t + b1 )
  y = np.sin ( a2 * t + b2 )
#
#  Plot it.
#
  plt.clf ( )
  plt.plot ( x, y, 'm-', linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -1.1, +1.1, -1.1, +1.1 ] )
  plt.axis ( 'equal' )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Lissajous curve' )
  filename = 'lissajous.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
  lissajous_test ( )
  timestamp ( )

