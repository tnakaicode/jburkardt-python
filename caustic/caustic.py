#! /usr/bin/env python3
#
def caustic ( m = 102, n = 500 ):

#*****************************************************************************80
#
## caustic() draws a caustic inside a circle.
#
#  Discussion:
#
#    caustic(m,n) connects n points, z(j), equally spaced around the unit 
#    circle, by n+1 straight lines.  The j-th line connects z(j+1) 
#    to z(mod(j*m,n)+1).
#
#    A particularly interesting plot is created by caustic(102,500).
#
#    Other good pairs include:
#      ( 88, 179)
#      ( 89, 220)
#      ( 99, 200)
#      (101, 200)
#      (111, 200)
#      (113, 188)
#      (126, 188)
#      (126, 200)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    Paul Villain, Cleve Moler.
#    This version by John Burkardt.
#
#  Reference:
#
#    Cleve Moler,
#    modfun, A Short Program Produces Impressive Graphics,
#    https://blogs.mathworks.com/cleve/2022/10/17/modfun-a-short-program-produces-impressive-graphics/
#    Posted 17 October 2022.
#
#  Input:
#
#    integer m: controls the spacing of the line endpoints.
#
#    integer n: the number of points in the circle.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.clf ( )
  plt.axis ( [ -1.0, 1.0, -1.0, 1.0 ] )
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  theta = np.linspace ( 0, 2.0 * np.pi, n + 1 )

  for j in range ( 0, n + 1 ):
    ax = np.cos ( theta[j] )
    ay = np.sin ( theta[j] )
    k = ( ( j * m ) % n )
    bx = np.cos ( theta[k] )
    by = np.sin ( theta[k] )
    plt.plot ( [ ax, bx ], [ ay, by ], 'b-', linewidth = 0.25 )

  return

def caustic_test ( ):

#*****************************************************************************80
#
## caustic_test() tests caustic().
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'caustic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test caustic().' )

  m = 102
  n = 500
  caustic ( m, n )
  filename = 'caustic_' + str ( m ) + '_' + str ( n ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'caustic_test():' )
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
  caustic_test ( )
  timestamp ( )

