#! /usr/bin/env python3
#
def minimize_scalar_test ( ):

#*****************************************************************************80
#
## minimize_scalar_test() seeks a minimizer of a scalar polynomial.
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
  from scipy.optimize import minimize_scalar
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'minimize_scalar_polynomial():' )
  print ( '  minimize_scalar() seeks a minimizer of a scalar function.' )

  x = np.linspace ( -6.0, 8.0, 101 )
  y = p ( x )
  plt.clf ( )
  plt.plot ( x, y )
  plt.grid ( True )
  filename = 'minimize_scalar_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
  
  result = minimize_scalar ( p )

  print ( '' )
  print ( '  Minimizer found at ', result.x )
  print ( '  p(x) = ', p ( result.x ) )

  result = minimize_scalar ( p, bounds = [0.0, 6.0] )

  print ( '' )
  print ( '  Specifying search interval of [0,6]:' )
  print ( '  Minimizer found at ', result.x )
  print ( '  p(x) = ', p ( result.x ) )
  return

def p ( x ):  
  value = x**4 - 3.0 * x**3 - 24 * x**2 + 28 * x + 48
  return value

if ( __name__ == '__main__' ):
  minimize_scalar_test ( )

