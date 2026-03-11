#! /usr/bin/env python3
#
def brentq_test ( ):

#*****************************************************************************80
#
## brentq_test() seeks a root of a function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2023
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import brentq
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'brentq_test():' )
  print ( '  brentq() seeks a root of a given function.' )

  x = np.linspace ( -1.0, 1.0, 101 )
  y = f ( x )

  plt.clf ( )
  plt.plot ( x, y )
  plt.plot ( [-1.0,1.0], [0.0,0.0], 'k--' )
  plt.grid ( True )
  filename = 'brentq_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
  
  x = brentq ( f, -0.7, -0.5 )

  print ( '' )
  print ( '  Root found at ', x )
  print ( '  f(x) = ', f ( x ) )

  return

def f ( x ): 
  import numpy as np
  value = 0.2 + x * np.cos ( 3.0 / x )

  return value

if ( __name__ == '__main__' ):
  brentq_test ( )

