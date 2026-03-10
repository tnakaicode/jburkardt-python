#! /usr/bin/env python3
#
def anishchenko_deriv ( t, xyz ):

#*****************************************************************************80
#
## anishchenko_deriv() evaluates the right hand side of anishchenko_ode().
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
#    Vadim Anishchenko, Vladimir Astakhov,
#    Experimental study of the mechanism of the appearance and the
#    structure of a strange attractor in an oscillator with inertial
#    nonlinearity,
#    Radiotekhnika i Elektronika,
#    Volume 28, 1983, pages 1109-1115.
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

  mu, eta, t0, xyz0, tstop = anishchenko_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = mu * x + y - x * z
  dydt = - x
  dzdt = - eta * z + eta * np.heaviside ( x, 0.5 ) * x * x

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def anishchenko_ode_test ( ):

#*****************************************************************************80
#
## anishchenko_ode_test() tests anishchenko_ode().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'anishchenko_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve anishchenko_ode().' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  mu, eta, t0, xyz0, tstop = anishchenko_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    mu =    ', mu )
  print ( '    eta =   ', eta )
  print ( '    t0 =    ', t0 )
  print ( '    xyz0 =  ', xyz0 )
  print ( '    tstop = ', tstop )

  t, x, y, z = anishchenko_ode_solve_ivp ( )
  anishchenko_ode_plot_components ( t, x, y, z )
  anishchenko_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'anishchenko_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def anishchenko_ode_solve_ivp ( ):

#*****************************************************************************80
#
## anishchenko_ode_solve_ivp() solves anishchenko_ode() using solve_ivp().
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
#  Output:
#
#    real T(:), X(:), Y(:), Z(:), values of the discrete solution.
#
  import numpy as np
  from scipy.integrate import solve_ivp
  
  mu, eta, t0, xyz0, tstop = anishchenko_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( anishchenko_deriv, tspan, xyz0, method = 'LSODA' )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def anishchenko_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## anishchenko_ode_plot_components() plots X(T), Y(T) and Z(T) for anishchenko_ode().
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
  plt.title ( 'anishchenko_ode() Time Series Plot' )
  filename = 'anishchenko_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def anishchenko_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## anishchenko_ode_plot_3d() plots (X,Y,Z) for anishchenko_ode().
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
  ax.set_title ( 'anishchenko_ode() 3D Plot' )
  filename = 'anishchenko_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def anishchenko_parameters ( mu_user = None, eta_user = None, \
  t0_user = None, xyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## anishchenko_parameters() returns parameters for anishchenko_ode().
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
#    real mu_user, eta_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real xyz0_user[3]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real mu, eta: problem parameters.
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
  if not hasattr ( anishchenko_parameters, "mu_default" ):
    anishchenko_parameters.mu_default = 1.2

  if not hasattr ( anishchenko_parameters, "eta_default" ):
    anishchenko_parameters.eta_default = 0.5

  if not hasattr ( anishchenko_parameters, "t0_default" ):
    anishchenko_parameters.t0_default = 0.0

  if not hasattr ( anishchenko_parameters, "xyz0_default" ):
    anishchenko_parameters.xyz0_default = np.array ( [ -0.1, 0.5, -0.6 ] )

  if not hasattr ( anishchenko_parameters, "tstop_default" ):
    anishchenko_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( mu_user is not None ):
    anishchenko_parameters.mu_default = mu_user

  if ( eta_user is not None ):
    anishchenko_parameters.eta_default = eta_user

  if ( t0_user is not None ):
    anishchenko_parameters.t0_default = t0_user

  if ( xyz0_user is not None ):
    anishchenko_parameters.xyz0_default = xyz0_user

  if ( tstop_user is not None ):
    anishchenko_parameters.tstop_default = tstop_user
#
#  Return values.
#
  mu = anishchenko_parameters.mu_default
  eta = anishchenko_parameters.eta_default
  t0 = anishchenko_parameters.t0_default
  xyz0 = anishchenko_parameters.xyz0_default
  tstop = anishchenko_parameters.tstop_default
  
  return mu, eta, t0, xyz0, tstop

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
  anishchenko_ode_test ( )
  timestamp ( )

