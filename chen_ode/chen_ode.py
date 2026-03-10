#! /usr/bin/env python3
#
def chen_deriv ( t, xyz ):

#*****************************************************************************80
#
## chen_deriv() evaluates the right hand side of chen_ode().
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
#    Guanrong Chen, Tetsushi Ueta,
#    Yet another chaotic attractor,
#    International Journal of Bifurcation and Chaos 
#    in Applied Sciences and Engineering,
#    Volume 9, Number 7, 1999, pages 1465-1466.
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

  a, b, c, t0, xyz0, tstop = chen_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = a * ( y - x )
  dydt = ( c - a ) * x - x * z + c * y
  dzdt = x * y - b * z

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def chen_ode_test ( ):

#*****************************************************************************80
#
## chen_ode_test() tests chen_ode().
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
  print ( 'chen_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve chen_ode().' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  a, b, c, t0, xyz0, tstop = chen_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a =     ', a )
  print ( '    b =     ', b )
  print ( '    c =     ', c )
  print ( '    t0 =    ', t0 )
  print ( '    xyz0 =  ', xyz0 )
  print ( '    tstop = ', tstop )

  t, x, y, z = chen_ode_solve_ivp ( )
  chen_ode_plot_components ( t, x, y, z )
  chen_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'chen_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def chen_ode_solve_ivp ( ):

#*****************************************************************************80
#
## chen_ode_solve_ivp() solves chen_ode() using solve_ivp().
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
  
  a, b, c, t0, xyz0, tstop = chen_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( chen_deriv, tspan, xyz0, method = 'LSODA' )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def chen_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## chen_ode_plot_components() plots X(T), Y(T) and Z(T) for chen_ode().
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
  plt.title ( 'chen_ode() Time Series Plot' )
  filename = 'chen_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def chen_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## chen_ode_plot_3d() plots (X,Y,Z) for chen_ode().
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
  ax.set_title ( 'chen_ode() 3D Plot' )
  filename = 'chen_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def chen_parameters ( a_user = None, b_user = None, c_user = None, \
  t0_user = None, xyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## chen_parameters() returns parameters for chen_ode().
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
#    real a_user, b_user, c_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real xyz0_user[3]: the initial condition.
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
  if not hasattr ( chen_parameters, "a_default" ):
    chen_parameters.a_default = 40.0

  if not hasattr ( chen_parameters, "b_default" ):
    chen_parameters.b_default = 3.0

  if not hasattr ( chen_parameters, "c_default" ):
    chen_parameters.c_default = 28.0

  if not hasattr ( chen_parameters, "t0_default" ):
    chen_parameters.t0_default = 0.0

  if not hasattr ( chen_parameters, "xyz0_default" ):
    chen_parameters.xyz0_default = np.array ( [ -0.1, 0.5, -0.6 ] )

  if not hasattr ( chen_parameters, "tstop_default" ):
    chen_parameters.tstop_default = 15.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    chen_parameters.a_default = a_user

  if ( b_user is not None ):
    chen_parameters.b_default = b_user

  if ( c_user is not None ):
    chen_parameters.c_default = c_user

  if ( t0_user is not None ):
    chen_parameters.t0_default = t0_user

  if ( xyz0_user is not None ):
    chen_parameters.xyz0_default = xyz0_user

  if ( tstop_user is not None ):
    chen_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = chen_parameters.a_default
  b = chen_parameters.b_default
  c = chen_parameters.c_default
  t0 = chen_parameters.t0_default
  xyz0 = chen_parameters.xyz0_default
  tstop = chen_parameters.tstop_default
  
  return a, b, c, t0, xyz0, tstop

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
  chen_ode_test ( )
  timestamp ( )

