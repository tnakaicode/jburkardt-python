#! /usr/bin/env python3
#
def boundary_locus ( f, pbox, label, filename ):

#*****************************************************************************80
#
## boundary_locus() plots the region of absolute stability.
#
#  Discussion:
#
#    An ODE solution method is analyzed by applying it to the problem
#      y' = lambda * y
#
#    A stepsize h is assumed.  The method is then transformed into an 
#    equation of the form
#      rho(z) = h*lambda*sigma(z)
#    or 
#      h * lambda = rho(z) / sigma(z)
#
#    We now plot f(z) = rho(z) / sigma(z), identifying those complex z for
#    which |f(z)| <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2019
#
#  Author:
#
#    Original version by Randall Leveque.
#    Modifications by John Burkardt
#
#  Reference:
#
#    Randall Leveque,
#    Finite difference methods for ordinary and partial differential equations,
#    Society for Industrial and Applied Mathematics, 2007,
#    ISBN13: 978-0-898716-29-0.
#
#  Input:
#
#    function handle R: an approximation to exp(z) obtained by applying a 
#    finite difference ODE method to y' = lambda y, where z = dt*lambda.
#
#    real pbox(4): xmin, xmax, ymin, ymax for the region to be displayed.
#
#    string label: a title to be used in the plot.
#
#    string filename: the name of the png file into which a copy of the plot
#    will be saved.
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  import numpy as np

  xa = pbox[0]
  xb = pbox[1]
  ya = pbox[2]
  yb = pbox[3]
#
#  Create a fine grid.
#
  nptsx = 251
  nptsy = 251
  x = np.linspace ( xa, xb, nptsx )
  y = np.linspace ( ya, yb, nptsy )
  X, Y = np.meshgrid ( x, y )
#
#  Evaluate R(z).
#
  Z = X + Y * 1j
  Rval = f ( Z )
  Rabs = np.abs ( Rval )
#
#  Make a contour plot of the z values for which |R|<=1.
#  In order to fill 0<=|R|<=1 with color, we need to specify 
#  contour levels of 0 and 1.
#  In order to fill with a "nice" color, we have to add a bogus level of -2.
#
  plt.clf ( )
  levels = np.array ( [ -2.0, 0.0, 1.0 ] )
  plt.contourf ( x, y, Rabs, levels, cmap = cm.coolwarm )
#
#  Label the plot.
#
  plt.grid ( 'True' )
  plt.title ( label )
  plt.xlabel ( '<--- real(R) --->' )
  plt.ylabel ( '<--- imag(R) --->' )
#
#  Draw axes.
#
  plt.plot ( [ xa, xb ], [ 0.0, 0.0 ], 'k:' )
  plt.plot ( [ 0.0, 0.0 ], [ ya, yb ], 'k:' )
  plt.axis ( 'equal' )
#
#  Save a copy of the plot in a file.
#
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def boundary_locus_test ( ):

#*****************************************************************************80
#
## boundary_locus_test() tests boundary_locus().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'boundary_locus_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  boundary_locus() plots the region of absolute stability for' )
  print ( '  an ODE solution method, using the boundary locus method.' )
  print ( '' )
#
#  euler_backward
#  y1 = y0 + z * y1
#  y1 = 1 / ( 1 - z ) * y0
#
  r = lambda z: 1 / ( 1 - z )
  pbox = np.array ( [ -2.1, +2.1, -2.1, +2.1 ] )
  label = 'Backward Euler'
  filename = 'euler_backward.png'
  boundary_locus ( r, pbox, label, filename )
#
#  euler_forward.
#  y1 = y0 + z * y0
#  y1 = ( 1 + z ) * y0
#
  r = lambda z: ( 1 + z )
  pbox = np.array ( [ -2.1, +2.1, -2.1, +2.1 ] )
  label = 'Forward Euler'
  filename = 'euler_forward.png'
  boundary_locus ( r, pbox, label, filename )
#
#  gear
#
  r = lambda z: 0.5 * (3*z**2-4*z+1) / z**2
  pbox = np.array ( [ -2.0, +5.0, -2.0, +2.0 ] )
  label = 'Gear'
  filename = 'gear.png'
  boundary_locus ( r, pbox, label, filename )
#
#  leapfrog.
#
  r = lambda z: z**2-1
  pbox = np.array ( [ -2.0, +2.0, -2.0, +2.0 ] )
  label = 'Leapfrog'
  filename = 'leapfrog.png'
  boundary_locus ( r, pbox, label, filename )
#
#  runge kutta 2
#  y1 = y0 + z * y0 + z^2/2 y0
#  y1 = ( 1 + z + z^2/2) * y0
#
  r = lambda z: 1 + z + 0.5*z**2
  pbox = np.array ( [ -2.1, +2.1, -2.1, +2.1 ] )
  label = 'Runge-Kutta 2'
  filename = 'rk2.png'
  boundary_locus ( r, pbox, label, filename )
#
#  runge kutta 4
#  y1 = ( 1 + z + z^2/2 + z^3/6 + z^4/24) * y0
#
  r = lambda z: 1 + z + (1/2)*z**2 + (1/6)*z**3 + (1/24)*z**4
  pbox = np.array ( [ -3.0, +3.0, -3.0, +3.0 ] )
  label = 'Runge-Kutta 4'
  filename = 'rk4.png'
  boundary_locus ( r, pbox, label, filename )
#
#  trapezoidal
#  y1 = y0 + 0.5 ( z * y0 + z * y1 )
#  y1 = ( 1 + z/2)/(1-z/2) * y0
#
  r = lambda z: ( 1 + 0.5 * z ) / ( 1 - 0.5 * z )
  pbox = np.array ( [ -2.0, +2.0, -2.0, +2.0 ] )
  label = 'Trapezoidal'
  filename = 'trapezoidal.png'
  boundary_locus ( r, pbox, label, filename )
#
#  trbdf2
#
  r = lambda z: (1 + (5/12) * z) / (1 - (7/12) * z + (1/12) * z**2 )
  pbox = np.array ( [ -5.0, +15.0, -10.0, +10.0 ] )
  label = 'TR-BDF2'
  filename = 'trbdf2.png'
  boundary_locus ( r, pbox, label, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'boundary_locus_test():' )
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
  boundary_locus_test ( )
  timestamp ( )


