#! /usr/bin/env python3
#
def bessel_j_test ( ):

#*****************************************************************************80
#
## bessel_j_test() tests the scipy() Bessel function evaluator jn().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import jn
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bessel_j_test():' )
  print ( '  Plot some Bessel Jn(x) functions for n = 0, 1, ... ' )

  x = np.linspace ( 0.0, 15.0, 101 )

  plt.clf ( )

  for n in range ( 0, 5 ):
    y = jn ( n, x )
    plt.plot ( x, y, linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<-- x -->' )
  plt.ylabel ( '<-- jn(x) -->' )
  plt.title ( 'Bessel Jn functions' )
  filename = 'bessel_j_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

if ( __name__ == "__main__" ):
  bessel_j_test ( )

