#! /usr/bin/env python3
#
def arenstorf_dydt ( t, xy ):

#*****************************************************************************80
#
## arenstorf_dydt() evaluates the right hand side of the Arenstorf ODE.
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
  import numpy as np

  global mu1, mu2

  x = xy[0]
  y = xy[1]
  xp = xy[2]
  yp = xy[3]

  d1 = np.sqrt ( ( ( x + mu1 )**2 + y**2 )**3 )
  d2 = np.sqrt ( ( ( x - mu2 )**2 + y**2 )**3 )

  dxdt = xp
  dydt = yp
  dxpdt = x + 2.0 * yp - mu2 * ( x + mu1 ) / d1 - mu1 * ( x - mu2 ) / d2
  dypdt = y - 2.0 * xp - mu2 * y / d1 - mu1 * y / d2

  dxydt = np.array ( [ dxdt, dydt, dxpdt, dypdt ] )

  return dxydt

def arenstorf_animation ( ):

#*****************************************************************************80
#
## arenstorf_animation() animates the solution of the Arenstorf ODE.
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import os

  global mu1, mu2

  print ( '' )
  print ( 'arenstorf_animation():' )
  print ( '  Create multiple images of Arenstorf orbit for later animation.' )

  mu1 = 0.012277471
  mu2 = 1.0 - mu1
  tmin = 0.0
  tmax = 17.0652165601579625588917206249
  n = 71

  tspan = np.array ( [ tmin, tmax ] )
  t = np.linspace ( tmin, tmax, n )
  y0 = np.array ( [ 0.994, 0.0, 0.0, -2.00158510637908252240537862224 ] )

  sol = solve_ivp ( arenstorf_dydt, tspan, y0, t_eval = t )
#
#  Compute the moon's location.
#
  theta = np.linspace ( 0.0, 2.0 * np.pi, n )
  moon_x = np.cos ( theta )
  moon_y = np.sin ( theta )
#
#  Plot the orbit as a sequence of frames.
#
  for i in range ( 0, n ):
#
#  Clear figure.
#
    plt.clf ( )
#
#  Set common limits for all frames.
#  As far as I can tell, you cannot follow this command with any call
#  to "axis()"!
#
    plt.xlim ( -2.0, 2.0 )
    plt.ylim ( -1.5, 1.5 )
#
#  Plot the earth as a blue circle.
#
    plt.plot ( 0.0, 0.0, 'bo', markersize = 25 )
#
#  Plot the moon as a green circle.
#
    plt.plot ( moon_x[0:i+1], moon_y[0:i+1], 'go', markersize = 8 )
#
#  Plot satellite as a red circle.
#
    plt.plot ( sol.y[0,0:i+1], sol.y[1,0:i+1], 'ro', markersize = 6 )
#
#  Finish up the plot.
#
    plt.grid ( True )
    plt.xlabel ( '<---  x  --->' )
    plt.ylabel ( '<---  y  --->' )
    plt.title ( 'Arenstorf frame ' + str ( i ) )
    filename = 'arenstorf' + str ( i ).zfill(3) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Merge png images into a gif.
#
  print ( '  Use "convert()" to merge png files into "arenstorf_animation.gif".' )
  os.system ( "convert -delay 10 -loop 1 arenstorf*.png arenstorf_animation.gif" )
#
#  Cleanup
#
  print ( '  Remove "arenstorf*.png" files.' )
  os.system ( "rm arenstorf*.png" )

#
#  Terminate.
#
  print ( '' )
  print ( 'arenstorf_animation():' )
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
  arenstorf_animation ( )
  timestamp ( )
