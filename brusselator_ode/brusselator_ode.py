#! /usr/bin/env python3
#
def brusselator_deriv ( t, xy ):

#*****************************************************************************80
#
## brusselator_deriv() defines brusselator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Behold! The Brusselator!,
#    https://www.johndcook.com/blog/
#    Posted 07 February 2020.
#
#    Rene Lefever, Gregoire Nicholis,
#    Chemical instabilities and sustained oscillations,
#    Journal of Theoretical Biology,
#    Volume 30, Issue 2, February 1971, Pages 267-284.
#
#  Input:
#
#    real T, the current time.
#
#    real XY(2), the current solution variables.
#
#  Output:
#
#    real DXYDT(2), the right hand side of the 2 ODE's.
#
  import numpy as np

  a, b, t0, xy0, tstop = brusselator_parameters ( )

  x = xy[0]
  y = xy[1]

  dxdt = a + x * x * y - ( b + 1.0 ) * x
  dydt = b * x - x * x * y

  dxydt = np.array ( [ dxdt, dydt ] )

  return dxydt

def brusselator_ode_test ( ):

#*****************************************************************************80
#
## brusselator_ode_test() tests brusselator_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Behold! The Brusselator!,
#    https://www.johndcook.com/blog/
#    Posted 07 February 2020.
#
#    Rene Lefever, Gregoire Nicholis,
#    Chemical instabilities and sustained oscillations,
#    Journal of Theoretical Biology,
#    Volume 30, Issue 2, February 1971, Pages 267-284.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'brusselator_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test brusselator_ode().' )

  a, b, t0, xy0, tstop = brusselator_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a =    ', a )
  print ( '    b =    ', b )
  print ( '    t0 =   ', t0 )
  print ( '    xy0 =  ', xy0 )
  print ( '    tstop = ', tstop )

  brusselator_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'brusselator_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def brusselator_solve_ivp ( ):

#*****************************************************************************80
#
## brusselator_solve_ivp() applies solve_ivp() to brusselator_ode().
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

  a, b, t0, xy0, tstop = brusselator_parameters ( )

  plt.clf ( )

  for x0 in range ( 0, 6 ):
    for y0 in range ( 0, 4 ):
      xy0 = np.array ( [ x0, y0 ] )
      tspan = np.array ( [ t0, tstop ] )
      t = np.linspace ( t0, tstop, 101 )

      sol = solve_ivp ( brusselator_deriv, tspan, xy0, t_eval = t )

      plt.plot ( sol.y[0,:], sol.y[1,:] )

  plt.grid ( True );
  plt.xlabel ( '<---  x(t)  --->' )
  plt.ylabel ( '<---  y(t)  --->' )
  plt.title ( 'brusselator_ode(): phase plot' )
  filename = 'brusselator_ode_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def brusselator_parameters ( a_user = None, b_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## brusselator_parameters() returns parameters for brusselator_ode().
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
#    04 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER: a parameter.
#
#    real B_USER: a parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[2]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A: a parameter.
#
#    real B: a parameter.
#
#    real T0: the initial time.
#
#    real Y0[2]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( brusselator_parameters, "a_default" ):
    brusselator_parameters.a_default = 1.0

  if not hasattr ( brusselator_parameters, "b_default" ):
    brusselator_parameters.b_default = 3.0

  if not hasattr ( brusselator_parameters, "t0_default" ):
    brusselator_parameters.t0_default = 0.0

  if not hasattr ( brusselator_parameters, "y0_default" ):
    brusselator_parameters.y0_default = np.array ( [ 0.0, 0.0 ] )

  if not hasattr ( brusselator_parameters, "tstop_default" ):
    brusselator_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    brusselator_parameters.a_default = a_user

  if ( b_user is not None ):
    brusselator_parameters.b_default = b_user

  if ( t0_user is not None ):
    brusselator_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    brusselator_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    brusselator_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = brusselator_parameters.a_default
  b = brusselator_parameters.b_default
  t0 = brusselator_parameters.t0_default
  y0 = brusselator_parameters.y0_default
  tstop = brusselator_parameters.tstop_default
  
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
  brusselator_ode_test ( )
  timestamp ( )

