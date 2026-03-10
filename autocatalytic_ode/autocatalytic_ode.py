#! /usr/bin/env python3
#
def autocatalytic_deriv ( t, wxyz ):

#*****************************************************************************80
#
## autocatalytic_deriv() evaluates the right hand side of autocatalytic_ode().
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
#  Reference:
#
#    Peter Gray, Stephen Scott,
#    Chemical oscillations and instabilities,
#    Interational Series of Monographs on Chemistry,
#    Volume 21, Oxford University Press, 1990.
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
#    real wxyz[4]: the values of the dependent variables at time T.
#
#  Output:
#
#    real dwxyzdt(4), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  alpha, beta, t0, xyz0, tstop = autocatalytic_parameters ( )

  w = wxyz[0]
  x = wxyz[1]
  y = wxyz[2]
  z = wxyz[3]

  dwdt = - alpha * w
  dxdt =   alpha * w - beta * x - x * y*y
  dydt =               beta * x + x * y*y - y
  dzdt =                                    y

  dwxyzdt = np.array ( [ dwdt, dxdt, dydt, dzdt ] )

  return dwxyzdt

def autocatalytic_ode_test ( ):

#*****************************************************************************80
#
## autocatalytic_ode_test() tests autocatalytic_ode().
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
  print ( 'autocatalytic_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve autocatalytic_ode().' )
  print ( '  Plot solution components (T,W(T)), (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  alpha, beta, t0, wxyz0, tstop = autocatalytic_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    beta =  ', beta )
  print ( '    t0 =    ', t0 )
  print ( '    wxyz0 = ', wxyz0 )
  print ( '    tstop = ', tstop )

  t, w, x, y, z = autocatalytic_ode_solve_ivp ( )
  autocatalytic_ode_plot_components ( t, w, x, y, z )
  autocatalytic_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'autocatalytic_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def autocatalytic_ode_solve_ivp ( ):

#*****************************************************************************80
#
## autocatalytic_ode_solve_ivp() solves autocatalytic_ode() using solve_ivp().
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
#    real T(:), W(:), X(:), Y(:), Z(:), values of the discrete solution.
#
  import numpy as np
  from scipy.integrate import solve_ivp
 
  alpha, beta, t0, wxyz0, tstop = autocatalytic_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( autocatalytic_deriv, tspan, wxyz0, method = 'LSODA' )

  t = sol.t
  w = sol.y[0,:]
  x = sol.y[1,:]
  y = sol.y[2,:]
  z = sol.y[3,:]

  return t, w, x, y, z

def autocatalytic_ode_plot_components ( t, w, x, y, z ):

#*****************************************************************************80
#
## autocatalytic_ode_plot_components() plots W(T), X(T), Y(T) and Z(T).
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
#    real W(:), X(:), Y(:), Z(:), the values of the dependent variables at time T.
#
  import matplotlib.pyplot as plt
#
#  Plot the data.
#
  plt.clf ( )
# plt.plot ( t, w, linewidth = 2, color = 'c' )
  plt.plot ( t, x, linewidth = 2, color = 'b' )
  plt.plot ( t, y, linewidth = 2, color = 'r' )
# plt.plot ( t, z, linewidth = 2, color = 'g' )
  plt.grid ( True )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- X(T), Y(T) --->' )
  plt.legend ( [ 'X(T)', 'Y(T)' ] )
  plt.title ( 'autocatalytic_ode() Time Series Plot' )
  filename = 'autocatalytic_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def autocatalytic_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## autocatalytic_ode_plot_3d() plots (X,Y,Z) for autocatalytic_ode().
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
  ax.set_title ( 'autocatalytic_ode() 3D Plot' )
  filename = 'autocatalytic_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def autocatalytic_parameters ( alpha_user = None, beta_user = None, \
  t0_user = None, wxyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## autocatalytic_parameters() returns parameters for autocatalytic_ode().
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
#    08 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user, beta_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real wxyz0_user[4]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real a, b, c: problem parameters.
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
  if not hasattr ( autocatalytic_parameters, "alpha_default" ):
    autocatalytic_parameters.alpha_default = 0.002

  if not hasattr ( autocatalytic_parameters, "beta_default" ):
    autocatalytic_parameters.beta_default = 0.08

  if not hasattr ( autocatalytic_parameters, "t0_default" ):
    autocatalytic_parameters.t0_default = 0.0

  if not hasattr ( autocatalytic_parameters, "wxyz0_default" ):
    autocatalytic_parameters.wxyz0_default = np.array ( [ 500.0, 0.0, 0.0, 0.0 ] )

  if not hasattr ( autocatalytic_parameters, "tstop_default" ):
    autocatalytic_parameters.tstop_default = 1000.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    autocatalytic_parameters.alpha_default = alpha_user

  if ( beta_user is not None ):
    autocatalytic_parameters.beta_default = beta_user

  if ( t0_user is not None ):
    autocatalytic_parameters.t0_default = t0_user

  if ( wxyz0_user is not None ):
    autocatalytic_parameters.wxyz0_default = wxyz0_user

  if ( tstop_user is not None ):
    autocatalytic_parameters.tstop_default = tstop_user
#
#  Return values.
#
  alpha = autocatalytic_parameters.alpha_default
  beta = autocatalytic_parameters.beta_default
  t0 = autocatalytic_parameters.t0_default
  wxyz0 = autocatalytic_parameters.wxyz0_default
  tstop = autocatalytic_parameters.tstop_default
  
  return alpha, beta, t0, wxyz0, tstop

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
  autocatalytic_ode_test ( )
  timestamp ( )

