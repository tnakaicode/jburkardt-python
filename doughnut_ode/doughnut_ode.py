#! /usr/bin/env python3
#
def doughnut_ode_test ( ):

#*****************************************************************************80
#
## doughnut_ode_test() tests doughnut_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2025
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'doughnut_ode_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Solve doughnut_ode().' )
#
#  Data
#
  m, n, t0, y0, tstop = doughnut_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    beta  = ', m )
  print ( '    rho   = ', n )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  doughnut_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'doughnut_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def doughnut_deriv ( t, y ):

#*****************************************************************************80
#
## doughnut_deriv() evaluates the right hand side of doughnut_ode().
#
#  Discussion:
#
#    The trajectory should remain on a torus.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Differential equation on a doughnut,
#    https://www.johndcook.com/blog/2025/10/08/diffeq-donut/
#    Posted 08 October 2025.
#
#    Richard Parris,
#    A Three-Dimensional System with Knotted Trajectories. 
#    The American Mathematical Monthly, 
#    Volume 84, Number 6 , June/July 1977, pages 468-469.
#
#  Input:
#
#    real T: the value of the independent variable.
#
#    real Y(M): the values of the dependent variables at time T.
#
#  Output:
#
#    real DYDT(M): the right hand side of the ODE.
#
  import numpy as np

  m, n, _, _, _ = doughnut_parameters ( )

  dy1dt = - m * y[1] + n * y[0] * y[2]
  dy2dt =   m * y[0] + n * y[1] * y[2]
  dy3dt =   0.5 * n * ( 1.0 - y[0]**2 - y[1]**2 + y[2]**2 )

  dydt = np.array ( [ dy1dt, dy2dt, dy3dt ] )

  return dydt

def doughnut_solve_ivp ( ):

#*****************************************************************************80
#
## doughnut_solve_ivp() uses solve-ivp() to solve doughnut_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 October 2025
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits.mplot3d import Axes3D
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'doughnut_solve_ivp' )
  print ( '  Use solve_ivp() to solve doughnut_ode().' )
#
#  Get the parameter values.
#
  _, _, t0, y0, tstop = doughnut_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  sol = solve_ivp ( doughnut_deriv, tspan, y0 )
#
#  Compute the approximate solution at equally spaced times.
#
  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  nstep = len ( t )
  print ( '' )
  print ( '  Number of variable size steps = ', nstep )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( x, y, z, linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->' )
  ax.set_ylabel ( '<-- Y -->' )
  ax.set_zlabel ( '<-- Z -->' )
  ax.set_title ( 'doughnut_ode()' )
  filename = 'doughnut_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def doughnut_parameters ( m_user = None, n_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## doughnut_parameters() returns parameters for doughnut_ode().
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#    Suggested choices for m, n, (y0) include:
#
#      3,  5, (1, 1, 3.0)
#      4,  5, (1, 1, 0.3)
#      pi, 5, (1, 1, 0.3)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real m_user, n_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real y0_user(3): the initial condition.
#
#    real tstop_user: the final time.
#
#  output:
#
#    real m, n: problem parameters.
#
#    real t0: the initial time.
#
#    real y0(3): the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np

  if not hasattr ( doughnut_parameters, "m_default" ):
    doughnut_parameters.m_default = 3.0

  if not hasattr ( doughnut_parameters, "n_default" ):
    doughnut_parameters.n_default = 5.0

  if not hasattr ( doughnut_parameters, "t0_default" ):
    doughnut_parameters.t0_default = 0.0

  if not hasattr ( doughnut_parameters, "y0_default" ):
    doughnut_parameters.y0_default = np.array ( [ 1.0, 1.0, 3.0 ] )

  if not hasattr ( doughnut_parameters, "tstop_default" ):
    doughnut_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( m_user is not None ):
    doughnut_parameters.m_default = m_user

  if ( n_user is not None ):
    doughnut_parameters.n_default = n_user

  if ( t0_user is not None ):
    doughnut_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    doughnut_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    doughnut_parameters.tstop_default = tstop_user
#
#  Return values.
#
  m = doughnut_parameters.m_default
  n = doughnut_parameters.n_default
  t0 = doughnut_parameters.t0_default
  y0 = doughnut_parameters.y0_default
  tstop = doughnut_parameters.tstop_default
  
  return m, n, t0, y0, tstop

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
  doughnut_ode_test ( )
  timestamp ( )

