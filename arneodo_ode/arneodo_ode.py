#! /usr/bin/env python3
#
def arneodo_deriv ( t, xyz ):

#*****************************************************************************80
#
## arneodo_deriv() evaluates the right hand side of arneodo_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alain Arneodo, Pierre Coullet, Edward Spiegel, Charles Tresser,
#    Asymptotic Chaos,
#    Physica D: Nonlinear Phenomena,
#    Volume 14, Number 3, 1985, pages 327-347.
#
#    Stephen Lucas, Evelyn Sander, Laura Taalman,
#    Modeling dynamical systems for 3D printing,
#    Notices of the American Mathematical Society,
#    Volume 67, Number 11, December 2020, pages 1692-1705.
#
#  Input:
#
#    real t: the value of the independent variable.
#
#    real xyz[3]: the values of the dependent variables at time T.
#
#  Output:
#
#    real dxyzdt(3), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  alpha, beta, delta, t0, xyz0, tstop = arneodo_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = y
  dydt = z
  dzdt = - alpha * x - beta * y - z + delta * x * x * x

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def arneodo_ode_test ( ):

#*****************************************************************************80
#
## arneodo_ode_test() tests arneodo_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'arneodo_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve arneodo_ode().' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  alpha, beta, delta, t0, xyz0, tstop = arneodo_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta =  ', beta )
  print ( '    delta = ', delta )
  print ( '    t0 =    ', t0 )
  print ( '    xyz0 =  ', xyz0 )
  print ( '    tstop = ', tstop )

  t, x, y, z = arneodo_ode_solve_ivp ( )
  arneodo_ode_plot_components ( t, x, y, z )
  arneodo_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'arneodo_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def arneodo_ode_solve_ivp ( ):

#*****************************************************************************80
#
## arneodo_ode_solve_ivp() solves arneodo_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(:), X(:), Y(:), Z(:), values of the discrete solution.
#
  import numpy as np
  from scipy.integrate import solve_ivp
 
  alpha, beta, delta, t0, xyz0, tstop = arneodo_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( arneodo_deriv, tspan, xyz0, method = 'LSODA' )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def arneodo_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## arneodo_ode_plot_components() plots X(T), Y(T) and Z(T) for arneodo_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:), the value of the independent variable.
#
#    real X(:), Y(:), Z(:), the values of the dependent variables at time T.
#
  import matplotlib.pyplot as plt
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( t, x, linewidth = 2, color = 'b' )
  plt.plot ( t, y, linewidth = 2, color = 'r' )
  plt.plot ( t, z, linewidth = 2, color = 'g' )
  plt.grid ( True )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- X(T), Y(T), Z(T) --->' )
  plt.title ( 'arneodo_ode() Time Series Plot' )
  filename = 'arneodo_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def arneodo_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## arneodo_ode_plot_3d() plots (X,Y,Z) for arneodo_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:), the value of the independent variable.
#
#    real X(:), Y(:), Z(:), the values of the dependent variables at time T.
#
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
#
#  Plot the data.
#
  fig = plt.figure ( )
  plt.clf ( )
# ax = fig.gca ( projection = '3d' )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( x, y, z, linewidth = 1, color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<--- X(T) --->' )
  ax.set_ylabel ( '<--- Y(T) --->' )
  ax.set_zlabel ( '<--- Z(T) --->' )
  ax.set_title ( 'arneodo_ode() 3D Plot' )
  filename = 'arneodo_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def arneodo_parameters ( alpha_user = None, beta_user = None, \
  delta_user = None, t0_user = None, xyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## arneodo_parameters() returns parameters for arneodo_ode().
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
#    09 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user, beta_user, delta_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real xyz0_user[3]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real alpha, beta, delta: problem parameters.
#
#    real t0: the initial time.
#
#    real xyz0[3]: the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( arneodo_parameters, "alpha_default" ):
    arneodo_parameters.alpha_default = -5.5

  if not hasattr ( arneodo_parameters, "beta_default" ):
    arneodo_parameters.beta_default = 3.5

  if not hasattr ( arneodo_parameters, "delta_default" ):
    arneodo_parameters.delta_default = -1.0

  if not hasattr ( arneodo_parameters, "t0_default" ):
    arneodo_parameters.t0_default = 0.0

  if not hasattr ( arneodo_parameters, "xyz0_default" ):
    arneodo_parameters.xyz0_default = np.array ( [ 0.2, 0.2, -0.75 ] )

  if not hasattr ( arneodo_parameters, "tstop_default" ):
    arneodo_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    arneodo_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    arneodo_parameters.beta_default = beta_user

  if ( delta_user is not None ):
    arneodo_parameters.delta_default = delta_user

  if ( t0_user is not None ):
    arneodo_parameters.t0_default = t0_user

  if ( xyz0_user is not None ):
    arneodo_parameters.xyz0_default = xyz0_user

  if ( tstop_user is not None ):
    arneodo_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = arneodo_parameters.alpha_default
  beta = arneodo_parameters.beta_default
  delta = arneodo_parameters.delta_default
  t0 = arneodo_parameters.t0_default
  xyz0 = arneodo_parameters.xyz0_default
  tstop = arneodo_parameters.tstop_default
  
  return alpha, beta, delta, t0, xyz0, tstop

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
#    06 April 2013
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
  arneodo_ode_test ( )
  timestamp ( )

