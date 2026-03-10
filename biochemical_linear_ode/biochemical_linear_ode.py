#! /usr/bin/env python3
#
def biochemical_linear_conserved ( y ):

#*****************************************************************************80
#
## biochemical_linear_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real Y(2): the current solution.
#
#  Output:
#
#    real H: the conserved quantity.
#
  h = y[0] + y[1]

  return h

def biochemical_linear_deriv ( t, y ):

#*****************************************************************************80
#
## biochemical_linear_deriv() evaluates the derivative of biochemical_linear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T, Y(2): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2): the value of the derivative.
#
  import numpy as np

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  y1 = y[0]
  y2 = y[1]

  S = np.array ( [ \
    [ -1.0,  1.0 ],
    [  1.0, -1.0 ] ] )

  r = np.array ( [ a * y1, b * y2 ] )
  
  dydt = np.matmul ( S, r )

  return dydt

def biochemical_linear_exact ( t ):

#*****************************************************************************80
#
## biochemical_linear_exact() returns exact solution of biochemical_linear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T: the current time.
#
#  Output:
#
#    real Y(2): the exact solution.
#
  import numpy as np

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  y10 = y0[0]
  y20 = y0[1]

  y1 = y10 + ( 1.0 - np.exp ( - ( a + b ) * ( t - t0 ) ) ) \
    * ( - a * y10 + b * y20 ) / ( a + b )
  y2 = y20 + ( 1.0 - np.exp ( - ( a + b ) * ( t - t0 ) ) ) \
    * (   a * y10 - b * y20 ) / ( a + b )

  y = np.array ( [ y1, y2 ] )

  return y

def biochemical_linear_ode_test ( ):

#*****************************************************************************80
#
## biochemical_linear_ode_test() tests biochemical_linear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'biochemical_linear_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test biochemical_linear_ode().' )

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a =    ', a )
  print ( '    b =    ', b )
  print ( '    t0 =   ', t0 )
  print ( '    y0 =   ', y0 )
  print ( '    tstop = ', tstop )

  biochemical_linear_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'biochemical_linear_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def biochemical_linear_solve_ivp ( ):

#*****************************************************************************80
#
## biochemical_linear_solve_ivp() applies solve_ivp() to biochemical_linear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  tspan = ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( biochemical_linear_deriv, \
    t_span = tspan, y0 = y0, t_eval = t )

  ye = biochemical_linear_exact ( t )

  plt.clf ( )
  plt.plot ( t, sol.y[0,:], 'ro', t, ye[0,:], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y1, y1exact  --->' )
  plt.title ( 'biochemical_linear_ode(): y1' )
  plt.legend ( ( 'y1', 'y1exact' ) )
  filename = 'biochemical_linear_ode_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, sol.y[1,:], 'ro', t, ye[1,:], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y2, y2exact  --->' )
  plt.title ( 'biochemical_linear_ode(): y2' )
  plt.legend ( ( 'y2', 'y2exact' ) )
  filename = 'biochemical_linear_ode_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def biochemical_linear_parameters ( a_user = None, b_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## biochemical_linear_parameters() returns parameters for biochemical_linear_ode().
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER, B_USER: parameters;
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A, B: parameters;
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( biochemical_linear_parameters, "a_default" ):
    biochemical_linear_parameters.a_default = 1.0

  if not hasattr ( biochemical_linear_parameters, "b_default" ):
    biochemical_linear_parameters.b_default = 1.0

  if not hasattr ( biochemical_linear_parameters, "t0_default" ):
    biochemical_linear_parameters.t0_default = 0.0

  if not hasattr ( biochemical_linear_parameters, "y0_default" ):
    biochemical_linear_parameters.y0_default = np.array ( [ 29.98, 9.98 ] )

  if not hasattr ( biochemical_linear_parameters, "tstop_default" ):
    biochemical_linear_parameters.tstop_default = 13.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    biochemical_linear_parameters.a_default = a_user

  if ( b_user is not None ):
    biochemical_linear_parameters.b_default = b_user

  if ( t0_user is not None ):
    biochemical_linear_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    biochemical_linear_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    biochemical_linear_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = biochemical_linear_parameters.a_default
  b = biochemical_linear_parameters.b_default
  t0 = biochemical_linear_parameters.t0_default
  y0 = biochemical_linear_parameters.y0_default
  tstop = biochemical_linear_parameters.tstop_default
  
  return a, b, t0, y0, tstop

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
  biochemical_linear_ode_test ( )
  timestamp ( )

