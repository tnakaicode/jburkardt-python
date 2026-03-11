#! /usr/bin/env python3
#
def minimize_himmelblau_test ( ):

#*****************************************************************************80
#
## minimize_himmelblau_test() test the scipy() minimize() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.optimize import minimize

  print ( '' )
  print ( 'minimize_himmelblau_test():' )
  print ( '  Use minimize() to find a minimizer of the Himmelblau function.' )

  start = np.array ( [ 0.0, 0.0 ] )
  print ( '  Starting at x = ', start )
  print ( '  f(x) = ', himmelblau ( start ) )

  result = minimize ( himmelblau, start )

  print ( '' )
  print ( '  Minimizer found at ', result.x )
  print ( '  f(x) = ', himmelblau ( result.x ) )

  return

def himmelblau ( x ):  
  f = ( x[0]**2 + x[1] - 11.0 )**2 + ( x[0] + x[1]**2 - 7.0 )**2
  return f

if ( __name__ == '__main__' ):
  minimize_himmelblau_test ( )

