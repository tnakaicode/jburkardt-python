#! /usr/bin/env python3
#
def roessler_deriv ( t, y ):

#*****************************************************************************80
#
## roessler_deriv() evaluates the right hand side of roessler_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Otto Roessler,
#    An Equation for Continuous Chaos,
#    Physics Letters, 
#    Volume 57A, Number 5, pages 397–398, 1976.
#
#  Input:
#
#    real T, the value of the independent variable.
#
#    real Y[3], the values of the dependent variables at time T.
#
#  Output:
#
#    real DYDT(3), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  alpha, beta, mu, t0, y0, tstop = roessler_parameters ( )

  dydt = np.zeros ( 3 )

  dydt[0] = - y[1] - y[2]
  dydt[1] = y[0] + alpha * y[1]
  dydt[2] = beta + ( y[0] - mu ) * y[2]

  return dydt

def roessler_ode_test ( ):

#*****************************************************************************80
#
## roessler_ode_test() tests roessler_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'roessler_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve roessler_ode().' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  alpha, beta, mu, t0, y0, tstop = roessler_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta =  ', beta )
  print ( '    mu =    ', mu )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  t, x, y, z = roessler_ode_solve_ivp ( )
  roessler_ode_plot_components ( t, x, y, z )
  roessler_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'roessler_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def roessler_ode_solve_ivp ( ):

#*****************************************************************************80
#
## roessler_ode_solve_ivp() solves roessler_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2020
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
 
  alpha, beta, mu, t0, y0, tstop = roessler_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( roessler_deriv, tspan, y0 )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def roessler_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## roessler_ode_plot_components() plots X(T), Y(T) and Z(T) for roessler_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2020
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
  plt.title ( 'roessler_ode() Time Series Plot' )
  filename = 'roessler_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def roessler_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## roessler_ode_plot_3d() plots (X,Y,Z) for roessler_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2020
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
  ax.set_title ( 'roessler_ode() 3D Plot' )
  filename = 'roessler_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def roessler_parameters ( alpha_user = None, beta_user = None, \
  mu_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## roessler_parameters() returns parameters for roessler_ode().
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
#    real ALPHA_USER: problem parameter.
#
#    real BETA_USER: problem parameter.
#
#    real MU_USER: problem parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[3]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real ALPHA: problem parameter.
#
#    real BETA: problem parameter.
#
#    real MU: problem parameter.
#
#    real T0: the initial time.
#
#    real Y0[3]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( roessler_parameters, "alpha_default" ):
    roessler_parameters.alpha_default = 0.2

  if not hasattr ( roessler_parameters, "beta_default" ):
    roessler_parameters.beta_default = 0.2

  if not hasattr ( roessler_parameters, "mu_default" ):
    roessler_parameters.mu_default = 5.7

  if not hasattr ( roessler_parameters, "t0_default" ):
    roessler_parameters.t0_default = 0.0

  if not hasattr ( roessler_parameters, "y0_default" ):
    roessler_parameters.y0_default = np.array ( [ 8.0, 1.0, 1.0 ] )

  if not hasattr ( roessler_parameters, "tstop_default" ):
    roessler_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    roessler_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    roessler_parameters.beta_default = beta_user

  if ( mu_user is not None ):
    roessler_parameters.mu_default = mu_user

  if ( t0_user is not None ):
    roessler_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    roessler_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    roessler_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = roessler_parameters.alpha_default
  beta = roessler_parameters.beta_default
  mu = roessler_parameters.mu_default
  t0 = roessler_parameters.t0_default
  y0 = roessler_parameters.y0_default
  tstop = roessler_parameters.tstop_default
  
  return alpha, beta, mu, t0, y0, tstop

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
  roessler_ode_test ( )
  timestamp ( )

