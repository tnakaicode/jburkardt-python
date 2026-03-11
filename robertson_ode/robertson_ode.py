#! /usr/bin/env python3
#
def robertson_conserved ( t, y ):

#*****************************************************************************80
#
## robertson_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Gerhard Wanner,
#    Solving Ordinary Differential Equations II: 
#    Stiff and Differential-algebraic Problems,
#    Springer-Verlag, second revised edition, 1996.
#
#  Input:
#
#    real Y[3,:]: the current solution.
#
#  Output:
#
#    real H(:): the conserved quantity.
#
  import numpy as np

  h = np.sum ( y, axis = 0 )

  return h

def robertson_deriv ( t, y ):

#*****************************************************************************80
#
## robertson_deriv() evaluates the derivative of robertson_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Gerhard Wanner,
#    Solving Ordinary Differential Equations II: 
#    Stiff and Differential-algebraic Problems,
#    Springer-Verlag, second revised edition, 1996.
#
#  Input:
#
#    real T, Y(3): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(3): the value of the derivative.
#
  import numpy as np

  y1 = y[0]
  y2 = y[1]
  y3 = y[2]

  dydt = np.zeros(3)

  dydt[0] = - 0.04 * y1 + 10000.0 * y2 * y3
  dydt[1] =   0.04 * y1 - 10000.0 * y2 * y3 - 30000000.0 * y2 * y2
  dydt[2] =                                 + 30000000.0 * y2 * y2  

  return dydt

def robertson_ode_test ( ):

#*****************************************************************************80
#
## robertson_ode_test() tests robertson_ode().
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
  print ( 'robertson_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve robertson_ode().' )

  t0, y0, tstop = robertson_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  robertson_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'robertson_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def robertson_solve_ivp ( ):

#*****************************************************************************80
#
## robertson_solve_ivp() applies solve_ivp() to robertson_ode().
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

  t0, y0, tstop = robertson_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )
#
#  Use the LSODA solver, that is suitable for stiff systems.
#
  sol = solve_ivp ( robertson_deriv, tspan, y0, method = 'LSODA' )

  plt.plot ( sol.t, sol.y[0,:], linewidth = 3 )
  plt.plot ( sol.t, sol.y[1,:], linewidth = 3 )
  plt.plot ( sol.t, sol.y[2,:], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y(t)  --->' )
  plt.title ( 'robertson_ode()' )
  plt.legend ( [ 'y1', 'y2', 'y3' ] )
  filename = 'robertson_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = robertson_conserved ( sol.t, sol.y )

  plt.clf ( )
  plt.plot ( sol.t, h, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y1+y2+y3  --->' )
  plt.title ( 'robertson_ode(): conservation' )
  filename = 'robertson_ode_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def robertson_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## robertson_parameters() returns parameters for robertson_ode().
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
#    28 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
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
  if not hasattr ( robertson_parameters, "t0_default" ):
    robertson_parameters.t0_default = 0.0

  if not hasattr ( robertson_parameters, "y0_default" ):
    robertson_parameters.y0_default = np.array ( [ 1.0, 0.0, 0.0 ] )

  if not hasattr ( robertson_parameters, "tstop_default" ):
    robertson_parameters.tstop_default = 40.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    robertson_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    robertson_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    robertson_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = robertson_parameters.t0_default
  y0 = robertson_parameters.y0_default
  tstop = robertson_parameters.tstop_default
  
  return t0, y0, tstop

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
  robertson_ode_test ( )
  timestamp ( )

