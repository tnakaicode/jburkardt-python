#! /usr/bin/env python3
#
def langford_deriv ( t, xyz ):

#*****************************************************************************80
#
## langford_deriv() evaluates the right hand side of langford_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Langford,
#    Numerical studies of torus bifurcations,
#    Internationale Schriftenreihe zur numerischen Mathematik,
#    Volume 70, Birkhaeuser, 1984, pages 285-295.
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

  a, b, c, d, e, f, t0, xyz0, tstop = langford_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = ( z - b ) * x - d * y
  dydt = d * x + ( z - b ) * y
  dzdt = c + a * z - z**3 / 3.0 \
    - ( x**2 + y**2 ) * ( 1.0 + e * z ) + f * z * x**3

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def langford_ode_test ( ):

#*****************************************************************************80
#
## langford_ode_test() tests langford_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'langford_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve langford_ode().' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  a, b, c, d, e, f, t0, xyz0, tstop = langford_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a =     ', a )
  print ( '    b =     ', b )
  print ( '    c =     ', c )
  print ( '    d =     ', d )
  print ( '    e =     ', e )
  print ( '    f =     ', f )
  print ( '    t0 =    ', t0 )
  print ( '    xyz0 =  ', xyz0 )
  print ( '    tstop = ', tstop )

  t, x, y, z = langford_ode_solve_ivp ( )
  langford_ode_plot_components ( t, x, y, z )
  langford_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'langford_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def langford_ode_solve_ivp ( ):

#*****************************************************************************80
#
## langford_ode_solve_ivp() solves langford_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2024
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
  from scipy.integrate import odeint
 
  a, b, c, d, e, f, t0, xyz0, tstop = langford_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
#
#  To get an accurate result, we need to use the LSODA method, rather
#  than the default 'RKF45'.
#
  sol = solve_ivp ( langford_deriv, tspan, xyz0, method = 'LSODA' )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def langford_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## langford_ode_plot_components() plots X(T), Y(T) and Z(T) for langford_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2024
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
  plt.title ( 'langford_ode() Time Series Plot' )
  filename = 'langford_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def langford_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## langford_ode_plot_3d() plots (X,Y,Z) for langford_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2024
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
  ax.set_title ( 'langford_ode() 3D Plot' )
  filename = 'langford_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def langford_parameters ( a_user = None, b_user = None, c_user = None, \
  d_user = None, e_user = None, f_user = None, t0_user = None, \
  xyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## langford_parameters() returns parameters for langford_ode().
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
#    07 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real a_user, b_user, c_user, d_user, e_user, f_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real xyz0_user[3]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real a, b, c, d, e, f: problem parameters.
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
  if not hasattr ( langford_parameters, "a_default" ):
    langford_parameters.a_default = 0.95

  if not hasattr ( langford_parameters, "b_default" ):
    langford_parameters.b_default = 0.7

  if not hasattr ( langford_parameters, "c_default" ):
    langford_parameters.c_default = 0.6

  if not hasattr ( langford_parameters, "d_default" ):
    langford_parameters.d_default = 3.5

  if not hasattr ( langford_parameters, "e_default" ):
    langford_parameters.e_default = 0.25

  if not hasattr ( langford_parameters, "f_default" ):
    langford_parameters.f_default = 0.1

  if not hasattr ( langford_parameters, "t0_default" ):
    langford_parameters.t0_default = 0.0

  if not hasattr ( langford_parameters, "xyz0_default" ):
    langford_parameters.xyz0_default = np.array ( [ 0.1, 1.0, 0.0 ] )

  if not hasattr ( langford_parameters, "tstop_default" ):
    langford_parameters.tstop_default = 2000.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    langford_parameters.a_default = a_user

  if ( b_user is not None ):
    langford_parameters.b_default = b_user

  if ( c_user is not None ):
    langford_parameters.c_default = c_user

  if ( d_user is not None ):
    langford_parameters.d_default = d_user

  if ( e_user is not None ):
    langford_parameters.e_default = e_user

  if ( f_user is not None ):
    langford_parameters.f_default = f_user

  if ( t0_user is not None ):
    langford_parameters.t0_default = t0_user

  if ( xyz0_user is not None ):
    langford_parameters.xyz0_default = xyz0_user

  if ( tstop_user is not None ):
    langford_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = langford_parameters.a_default
  b = langford_parameters.b_default
  c = langford_parameters.c_default
  d = langford_parameters.d_default
  e = langford_parameters.e_default
  f = langford_parameters.f_default
  t0 = langford_parameters.t0_default
  xyz0 = langford_parameters.xyz0_default
  tstop = langford_parameters.tstop_default
  
  return a, b, c, d, e, f, t0, xyz0, tstop

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
  langford_ode_test ( )
  timestamp ( )

