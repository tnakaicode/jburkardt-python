#! /usr/bin/env python3
#
def solve_ivp_test ( ):

#*****************************************************************************80
#
## solve_ivp_test() tests the scipy() solve_ivp() function on the logistic ODE.
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'solve_ivp_test():' )
  print ( '  solve_ivp() is used to solve the logistic ODE.' )

  tmin = 0.0
  tmax = 4.0
  y0 =  np.array ( [ 1.0 ] )
  sol = solve_ivp ( logistic_dydt, [tmin,tmax], y0 )
  plt.clf ( )
  plt.plot ( sol.t, sol.y[0] )
  plt.grid ( True )
  filename = 'solve_ivp_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "'+ filename + '"' )
  plt.close ( )
  return

def logistic_dydt ( t, y ):
  dydt = 2.0 * y * ( 3.0 - y )
  return dydt

if ( __name__ == "__main__" ):
  solve_ivp_test ( )

