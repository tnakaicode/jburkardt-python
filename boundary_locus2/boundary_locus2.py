#! /usr/bin/env python3
#
def boundary_locus2 ( t, f, label, filename ):

#*****************************************************************************80
#
## boundary_locus2() plots the region of absolute stability.
#
#  Discussion:
#
#    An ODE solution method is analyzed by applying it to the problem
#      y' = lambda * y
#
#    A stepsize h is assumed.  The method is then transformed into an 
#    equation of the form
#      rho(z) = h * lambda * sigma(z)
#    or 
#      h * lambda = rho(z) / sigma(z)
#
#    We now consider 
#      f(z) = rho(z) / sigma(z)
#    and trace the curve f(z) for those complex z with unit norm,
#    which marks the boundary of the region of absolute stability.
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
#  Input:
#
#    real t(*): a vector containing the range of angles to be used.
#    The z values will be generated as exp(i*t).
#    In most cases, t = np.linspace ( 0.0, 2.0 * np.pi, 101 ) will do.
#
#    function handle f: evaluates the ratio rho(z)/sigma(z).
#
#    string label: a title to be used in the plot.
#
#    string filename: the name of the png graphics file to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Evaluate f(z) for z's of unit norm.
#
  z = np.exp ( t * 1j )
  fz = f ( z )
#
#  As a help in judging which side of the boundary is the stability region,
#  include a second line for z's of norm 0.9.
#
  z2 = 0.9 * np.exp ( t * 1j )
  fz2 = f ( z2 )
#
#  Get the range of the data.
#
  xmin = min ( np.min ( fz.real ), np.min ( fz2.real ) )
  xmax = max ( np.max ( fz.real ), np.max ( fz2.real ) )
  ymin = min ( np.min ( fz.imag ), np.min ( fz2.imag ) )
  ymax = max ( np.max ( fz.imag ), np.max ( fz2.imag ) )
#
#  Display the plot.
#
  plt.clf ( )
  plt.plot ( fz.real, fz.imag, 'r-', linewidth = 3 )
  plt.plot ( fz2.real, fz2.imag, 'm-', linewidth = 3 )
  plt.plot ( [ 0.0, 0.0 ], [ymin,ymax], 'k:', linewidth = 3 )
  plt.plot ( [xmin,xmax], [0.0,0.0], 'k:', linewidth = 3 )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.xlabel ( '<-- real(z) -->' )
  plt.ylabel ( '<-- imag(z) -->' )
  plt.title ( label )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def boundary_locus2_test ( ):

#*****************************************************************************80
#
## boundary_locus2_test() tests boundary_locus2().
#
#  Discussion:
#
#    Thanks to Professor Catalin Trenchea for pointing out how to deal
#    with the trapezoidal method, whose stability region boundary includes
#    a point at infinity.
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
  print ( 'boundary_locus2_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  boundary_locus2() plots the absolute stability boundary' )
  print ( '  for an ODE solution method.' )
#
#  ab2
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: ( z**2 - z ) / ( 1.5 * z - 0.5 )
  label = 'AB2'
  filename = 'ab2.png'
  boundary_locus2 ( t, f, label, filename )
#
#  ab3
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: ( z**3 - z**2 ) / ( 23 * z**2 - 16 * z + 5 ) / 12
  label = 'AB3'
  filename = 'ab3.png'
  boundary_locus2 ( t, f, label, filename )
#
#  ab4
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: ( z**4 - z**3 ) / ( 55 * z**3 - 59 * z**2 + 37 * z - 9 ) / 24
  label = 'AB4'
  filename = 'ab4.png'
  boundary_locus2 ( t, f, label, filename )
#
#  euler_backward
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: ( 1 - z )
  label = 'Backward Euler'
  filename = 'euler_backward.png'
  boundary_locus2 ( t, f, label, filename )
#
#  euler_backward_filter
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: ( z**2 - 4.0/3.0 * z + 1.0/3.0 ) / ( z**2 - 2.0/3.0 * z + 1.0/3.0 )
  label = 'Backward Euler + Time Filter'
  filename = 'euler_backward_filtered.png'
  boundary_locus2 ( t, f, label, filename )
#
#  euler_forward
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: ( z - 1 )
  label = 'Forward Euler'
  filename = 'euler_forward.png'
  boundary_locus2 ( t, f, label, filename )
#
#  gear
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: 0.5 * ( 3 * z**2 - 4 * z + 1 ) / z**2
  label = 'Gear'
  filename = 'gear.png'
  boundary_locus2 ( t, f, label, filename )
#
#  leapfrog
#
  t = np.linspace ( 0.0, 2.0 * np.pi, 101 )
  f = lambda z: 0.5 * ( z**2 - 1 ) / z
  label = 'Leapfrog'
  filename = 'leapfrog.png'
  boundary_locus2 ( t, f, label, filename )
#
#  trapezoidal
#
  print ( '' )
  print ( '  For the trapezoidal rule, the function f(z) has a ' )
  print ( '  singularity at z=-1.  Correspondingly, the stability' )
  print ( '  region is infinite, and the boundary has to go to infinity.' )
  print ( '  To avoid this problem, we restrict the angle t to avoid' )
  print ( '  z = -1.' )

  t = np.linspace ( - 0.95 * np.pi, + 0.95 * np.pi, 101 )
  f = lambda z: 2 * ( z - 1 ) / ( z + 1 )
  label = 'Trapezoidal'
  filename = 'trapezoidal.png'
  boundary_locus2 ( t, f, label, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'boundary_locus2_test():' )
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
  boundary_locus2_test ( )
  timestamp ( )


