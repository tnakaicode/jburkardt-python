#! /usr/bin/env python3
#
def bioconvection_deriv ( t, xyz ):

#*****************************************************************************80
#
## bioconvection_deriv() evaluates the right hand side of bioconvection_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Andriy Avramenko, Yulia Kovetska, Igor Shevchuk,
#    Lorenz approach for analysis of bioconvection instability of
#    gyrotactic motile microorganisms,
#    Chaos, Solitons and Fractals,
#    Volume 166, 2023.
#
#  Input:
#
#    real t: the value of the independent variable.
#
#    real xyz(3): the values of the dependent variables.
#
#  Output:
#
#    real dxyzdt(3): the right hand side of the ODE.
#
  import numpy as np

  a, b, sc, t0, xyz0, tstop = bioconvection_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = sc * ( y - x )
  dydt = a * x + x * z - y
  dzdt = - x * y - b * z

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def bioconvection_solve_ivp ( ):

#*****************************************************************************80
#
## bioconvection_solve_ivp() uses solve_ivp() to solve bioconvection_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from scipy.integrate import solve_ivp

  print ( '' )
  print ( 'bioconvection_solve_ivp' )
  print ( '  Use solve_ivp() to solve bioconvection_ode().' )
#
#  Get the parameter values.
#
  a, b, sc, t0, xyz0, tstop = bioconvection_parameters ( )

  tspan = [ t0, tstop ]
#
#  Compute the approximate solution at equally spaced times.
#
  sol = solve_ivp ( bioconvection_deriv, tspan, xyz0 )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  n = len ( t )
  print ( '' )
  print ( '  Number of variable size steps = ', n )

  return t, x, y, z

def bioconvection_ode_test ( ):

#*****************************************************************************80
#
## bioconvection_ode_test() tests bioconvection_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bioconvection_ode_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve bioconvection_ode().' )
#
#  Data
#
  a, b, sc, t0, xyz0, tstop = bioconvection_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a     = ', a )
  print ( '    b     = ', b )
  print ( '    sc    = ', sc )
  print ( '    t0    = ', t0 )
  print ( '    xyz0  = ', xyz0 )
  print ( '    tstop = ', tstop )
#
#  Solve system using solve_ivp().
#
  t, x, y, z = bioconvection_solve_ivp ( )
  bioconvection_ode_plot_components ( t, x, y, z )
  bioconvection_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'bioconvection_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def bioconvection_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## bioconvection_ode_plot_components() plots X(T), Y(T) and Z(T) for bioconvection_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2024
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
#
  import matplotlib.pyplot as plt
#
#  Plot the data.
#
  plt.plot ( t, x, linewidth = 2, color = 'b' )
  plt.plot ( t, y, linewidth = 2, color = 'r' )
  plt.plot ( t, z, linewidth = 2, color = 'g' )
  plt.grid ( True )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- X(T), Y(T), Z(T) --->' )
  plt.title ( 'bioconvection_ode(): Time Series Plot' )
  plt.savefig ( 'bioconvection_ode_components.png' )
  print ( '' )
  print ( '  Graphics data saved as "bioconvection_ode_components.png"' )
  plt.show ( block = False )
  plt.close ( )

  return

def bioconvection_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## bioconvection_ode_plot_3d() plots (X,Y,Z) for bioconvection_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2024
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
# ax = fig.gca ( projection = '3d' )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( x, y, z, linewidth = 1, color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<--- X(T) --->' )
  ax.set_ylabel ( '<--- Y(T) --->' )
  ax.set_zlabel ( '<--- Z(T) --->' )
  ax.set_title ( 'bioconvection_ode(): 3D Plot' )
  filename = 'bioconvection_ode_3d.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def bioconvection_parameters ( a_user = None, b_user = None, sc_user = None, \
  t0_user = None, xyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## bioconvection_parameters() returns parameters for bioconvection_ode().
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
#    29 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real a_user, b_user, sc_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real xyz0_user(3): the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real a, b, sc: problem parameters.
#
#    real t0: the initial time.
#
#    real xyz0(3): the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( bioconvection_parameters, "a_default" ):
    bioconvection_parameters.a_default = 49.6

  if not hasattr ( bioconvection_parameters, "b_default" ):
    bioconvection_parameters.b_default = 3.3

  if not hasattr ( bioconvection_parameters, "sc_default" ):
    bioconvection_parameters.sc_default = 5.0

  if not hasattr ( bioconvection_parameters, "t0_default" ):
    bioconvection_parameters.t0_default = 0.0

  if not hasattr ( bioconvection_parameters, "xyz0_default" ):
    bioconvection_parameters.xyz0_default = np.array ( [ 0.0, 100.0, 0.0 ] )

  if not hasattr ( bioconvection_parameters, "tstop_default" ):
    bioconvection_parameters.tstop_default = 25.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    bioconvection_parameters.a_default = a_user

  if ( b_user is not None ):
     bioconvection_parameters.b_default = b_user

  if ( sc_user is not None ):
    bioconvection_parameters.sc_default = sc_user

  if ( t0_user is not None ):
    bioconvection_parameters.t0_default = t0_user

  if ( xyz0_user is not None ):
    bioconvection_parameters.xyz0_default = xyz0_user

  if ( tstop_user is not None ):
    bioconvection_parameters.tstop_default = tstop_user
#
#  The returned values are the defaults, or overridden by user input.
#
  a = bioconvection_parameters.a_default
  b = bioconvection_parameters.b_default
  sc = bioconvection_parameters.sc_default
  t0 = bioconvection_parameters.t0_default
  xyz0 = bioconvection_parameters.xyz0_default
  tstop = bioconvection_parameters.tstop_default
  
  return a, b, sc, t0, xyz0, tstop

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
  bioconvection_ode_test ( )
  timestamp ( )

