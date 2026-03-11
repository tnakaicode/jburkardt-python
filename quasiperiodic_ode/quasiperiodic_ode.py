#! /usr/bin/env python3
#
def quasiperiodic_deriv ( t, y ):

#*****************************************************************************80
#
## quasiperiodic_deriv() returns the right hand side of quasiperiodic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#  Input:
#
#    real T, the current time.
#
#    real Y(4,1), the current state values.
#
#  Output:
#
#    real YPRIME(4,1), the time derivatives of the current state values.
#
  import numpy as np

  yprime = np.zeros ( 4 )

  yprime[0] = y[1]
  yprime[1] = y[2]
  yprime[2] = y[3]
  yprime[3] = - ( np.pi**2 + 1.0 ) * y[2] - np.pi**2 * y[0]

  return yprime

def quasiperiodic_exact ( t ):

#*****************************************************************************80
#
## quasiperiodic_exact() returns the exact solution for quasiperiodic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the current time.
#
#  Output:
#
#    real Y(:,4): the exact solution.
#
  import numpy as np

  p =   np.cos ( t ) +            np.cos ( np.pi * t )
  q = - np.sin ( t ) - np.pi    * np.sin ( np.pi * t )
  r = - np.cos ( t ) - np.pi**2 * np.cos ( np.pi * t )
  s =   np.sin ( t ) + np.pi**3 * np.sin ( np.pi * t )

  y = np.array ( [ p, q, r, s ] )
  y = np.transpose ( y )
 
  return y

def quasiperiodic_ode_test ( ):

#*****************************************************************************80
#
## quasiperiodic_ode_test() tests quasiperiodic_ode().
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
  print ( 'quasiperiodic_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve quasiperiodic_ode().' )

  t0, y0, tstop = quasiperiodic_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  quasiperiodic_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'quasiperiodic_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def quasiperiodic_solve_ivp ( ):

#*****************************************************************************80
#
## quasiperiodic_solve_ivp() applies solve_ivp() to quasiperiodic_ode().
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

  t0, y0, tstop = quasiperiodic_parameters ( )

  f = quasiperiodic_deriv
  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( f, tspan, y0 )
  t = sol.t
  y = sol.y
  y2 = quasiperiodic_exact ( t )

  plt.plot ( t, y[0,:], 'bo', linewidth = 2, label = 'solve_ivp' )
  plt.plot ( t, y2[:,0], 'r-', linewidth = 2, label = 'exact' )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  plt.legend ( )
  plt.title ( 'quasiperiodic_ode().' )

  filename = 'quasiperiodic_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return


def quasiperiodic_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## quasiperiodic_parameters() returns the parameters of quasiperiodic_ode().
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
#    real Y0_USER(4): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0(4): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( quasiperiodic_parameters, "t0_default" ):
    quasiperiodic_parameters.t0_default = 0.0

  if not hasattr ( quasiperiodic_parameters, "y0_default" ):
    quasiperiodic_parameters.y0_default = \
      np.array ( [ 2.0, 0.0, -(1.0+np.pi**2), 0.0 ] )

  if not hasattr ( quasiperiodic_parameters, "tstop_default" ):
    quasiperiodic_parameters.tstop_default = 20.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    quasiperiodic_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    quasiperiodic_parameters.y0_default = y0_user.copy()

  if ( tstop_user is not None ):
    quasiperiodic_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = quasiperiodic_parameters.t0_default
  y0 = quasiperiodic_parameters.y0_default.copy ( )
  tstop = quasiperiodic_parameters.tstop_default
  
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
  quasiperiodic_ode_test ( )
  timestamp ( )

