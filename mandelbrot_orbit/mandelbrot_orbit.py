#! /usr/bin/env python3
#
def mandelbrot_orbit ( z0, n ):

#*****************************************************************************80
#
## mandelbrot_orbit() follows the orbit of a point in a Mandelbrot iteration.
#
#  Discussion:
#
#    The iteration has the form:
#
#      Z = Z^2 + Z0
#
#  Example:
#
#    mandelbrot_orbit ( -0.04+0.6i, 100 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex z0: the starting point.
#
#    integer n: the number of steps.
#
#  Output:
#
#    complex z(n+1,1): the sequence of iterates.
#
  import numpy as np

  z = z0 * np.ones ( n + 1 )

  for j in range ( 0, n ):
    z[j+1] = z[j] ** 2 + z0
    if ( 2.0 < abs ( z[j+1] ) ):
      break

  return z

def mandelbrot_orbit_test ( ):

#*****************************************************************************80
#
## mandelbrot_orbit_test() tests mandelbrot_orbit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'mandelbrot_orbit_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  mandelbrot_orbit() applies n steps of the mandebrlot' )
  print ( '  iteration z = z^2 + c to a given starting point z0.' )

  n = 100

  for test in range ( 1, 9 ):

    if ( test == 1 ):
      z0 = complex ( -0.04, 0.6 )
    elif ( test == 2 ):
      z0 = complex ( -1.0, 0.1 )
    elif ( test == 3 ):
      z0 = complex ( -0.8, 0.01 )
    elif ( test == 4 ):
      z0 = complex ( -0.6, 0.2 )
    elif ( test == 5 ):
      z0 = complex ( -0.4, 0.4 )
    elif ( test == 6 ):
      z0 = complex ( -0.2, 0.6 )
    elif ( test == 7 ):
      z0 = complex ( 0.0, 0.4 )
    elif ( test == 8 ):
      z0 = complex ( 0.1, 0.2 )

    z = mandelbrot_orbit ( z0, n )

    plt.clf ( )
    plt.plot ( z.real, z.imag, '.', markersize = 15 )
    plt.grid ( True )
    plt.axis ( 'equal' )
    s = 'z0=' + str ( z0 )
    plt.title ( s )
    filename = 'mandelbrot_orbit_test' + str ( test ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mandelbrot_orbit_test():' )
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
  mandelbrot_orbit_test ( )
  timestamp ( )



