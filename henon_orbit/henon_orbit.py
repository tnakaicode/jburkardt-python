#! /usr/bin/env python3
#
def henon_orbit_test ( ):

#*****************************************************************************80
#
## henon_orbit_test() tests henon_orbit().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Henon's dynamical system,
#    https://www.johndcook.com/blog/2023/02/08/henon/
#    Posted 08 February 2023.
#
#    Michel Hénon,
#    Numerical study of quadratic area-preserving mappings. 
#    Quarterly of Applied Mathematics. 
#    October 1969, pages 291-312.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'henon_orbit_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  henon_orbit() plots examples of the ' )
  print ( '  Henon dynamical system.' )
  print ( '' )

  fig4 = [
    [ 0.1,   0.0,    200.0 ],
    [ 0.2,   0.0,    360.0 ],
    [ 0.3,   0.0,    840.0 ],
    [ 0.4,   0.0,    871.0 ],
    [ 0.5,   0.0,    327.0 ],
    [ 0.58,  0.0,   1164.0 ],
    [ 0.61,  0.0,   1000.0 ],
    [ 0.63,  0.2,    180.0 ],
    [ 0.66,  0.22,   500.0 ],
    [ 0.66,  0.0,    694.0 ],
    [ 0.73,  0.0,    681.0 ],
    [ 0.795, 0.0,    657.0 ],
  ]

  henon_orbit ( 0.4, fig4, "fig4.png" )

  fig5 = [
    [ 0.2,   0.0,    651.0 ],
    [ 0.35,  0.0,    187.0 ],
    [ 0.44,  0.0,   1000.0 ],
    [ 0.60, -0.1,   1000.0 ],
    [ 0.68,  0.0,    250.0 ],
    [ 0.718, 0.0,   3000.0 ],
    [ 0.75,  0.0,   1554.0 ],
    [ 0.82,  0.0,    233.0 ],
  ]

  henon_orbit ( 0.24, fig5, "fig5.png" )

  fig7 = [
    [ 0.1,  0.0,  182.0 ],
    [ 0.15, 0.0, 1500.0 ],
    [ 0.35, 0.0,  560.0 ],
    [ 0.54, 0.0,  210.0 ],
    [ 0.59, 0.0,  437.0 ],
    [ 0.68, 0.0,  157.0 ],
  ]

  henon_orbit ( -0.01, fig7, "fig7.png" )
#
#  Terminate.
#
  print ( '' )
  print ( 'henon_orbit_test():' )
  print ( '  Normal end of execution.' )

  return

def henon_orbit ( c, data, filename ):

#*****************************************************************************80
#
## henon_orbit() plots the Henon dynamical system map for given starting values.
#
#  Discussion:
#
#    This code reproduces plots of Henon's dynamical system.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt.
#
#  Input:
#
#    real c: the cosine of alpha, the dynamical system parameter.
#
#    data[*,3]: sets of x, y, n values.
#
#    string filename: the name of the file in which the plot is to be saved.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Compute the sine of alpha.
#
  s = np.sqrt ( 1.0 - c * c )

  plt.clf ( )

  for d in data:

    x, y, n = d
    n = int ( n )
#
#  Choose a random RGB color for each starting point.
#
    r = np.round ( np.random.rand(), 1 )
    g = np.round ( np.random.rand(), 1 )
    b = np.round ( np.random.rand(), 1 )

    for i in range ( 0, n ):

      if ( abs ( x ) < 1.0 and abs ( y ) < 1.0 ):
        xnew = x * c - ( y - x**2 ) * s
        ynew = x * s + ( y - x**2 ) * c
        x = xnew
        y = ynew
        plt.scatter ( x, y, s = 1, color = [r,g,b] )

  plt.gca().set_aspect ( "equal" )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
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

if ( __name__ == "__main__" ):
  timestamp ( )
  henon_orbit_test ( )
  timestamp ( )

