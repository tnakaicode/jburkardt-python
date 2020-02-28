#! /usr/bin/env python3
#
def brownian_animation ( ):

#*****************************************************************************80
#
## brownian_animation animates Brownian motion by drawing one step at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'brownian_animation:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Simulate and plot Brownian motion in two dimensions.' )
  print ( '  Animate the process by drawing one step at a time.' )
#
#  Simulate.
#
  t = 1.0
  d = 10.0
  n = 100
  x = brownian_2d_simulate ( n, d, t )
#
#  Display.
#
  brownian_animation_display ( n, x )
#
#  Terminate.
#
  print ( '' )
  print ( 'brownian_animation:' )
  print ( '  Normal end of execution.' )

  return

def brownian_2d_simulate ( n, d, t ):

#*****************************************************************************80
#
## BROWNIAN_2D_SIMULATE simulates Brownian motion in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of time steps to take. 
#
#    Input, real D, the diffusion coefficient.  
#
#    Input, real T, the total time.
#
#    Output, real X(2,N), the initial position at time 0.0, and 
#    the N-1 successive locations of the particle.
#
  import numpy as np
#
#  Set the time step.
#
  dt = t / ( n - 1 )
#
#  Make space X for the locations.
#
  x = np.zeros ( [ 2, n ] )

  for j in range ( 1, n ):
#
#  S is the stepsize
#
    s = np.sqrt ( 2.0 * 2 * d * dt ) * np.random.randn ( 1 )
#
#  Direction is random.
#
    dx = np.random.randn ( 2 )
    norm_dx = np.sqrt ( np.sum ( dx ** 2 ) )
    for i in range ( 0, 2 ):
      dx[i] = s * dx[i] / norm_dx
#
#  Each position is the sum of the previous steps.
#
    x[0:2,j] = x[0:2,j-1] + dx[0:2]

  return x

def brownian_animation_display ( n, x ):

#*****************************************************************************80
#
## BROWNIAN_ANIMATION_DISPLAY displays successive Brownian motion positions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of time steps. 
#
#    Input, real X(2,N), the particle positions.
#
  import matplotlib.pyplot as plt
  import numpy as np

  xmin = np.min ( x[0,:] )
  xmax = np.max ( x[0,:] )
  ymin = np.min ( x[1,:] )
  ymax = np.max ( x[1,:] )

  plt.clf
  plt.axis ( [ xmin, xmax, ymin, ymax ] )
  plt.grid ( True )
  plt.xlabel ( '<--X-->', fontsize = 16 )
  plt.ylabel ( '<--Y-->', fontsize = 16 )
  plt.title ( 'Animation of Brownian motion', fontsize = 16 )

  plt.plot ( x[0,0], x[1,0], color = 'g', marker = '.', markersize = 35 )
  for i in range ( 0, n - 1 ):
    plt.plot ( [ x[0,i], x[0,i+1] ], [ x[1,i], x[1,i+1] ], linewidth = 2, color = 'b' )
    plt.pause ( 0.25 )
  plt.plot ( x[0,n-1], x[1,n-1], color = 'r', marker = '.', markerSize = 35 )

  filename = 'brownian_animation.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Plot saved as "%s".' % ( filename ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  brownian_animation ( )
  timestamp ( )
 
