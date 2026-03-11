#! /usr/bin/env python3
#
def rucklidge_deriv ( t, xyz ):

#*****************************************************************************80
#
## rucklidge_deriv() evaluates the right hand side of rucklidge_ode().
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
#    Alastair Rucklidge,
#    Chaos in models of double convection,
#    Journal of Fluid Mechanics,
#    Volume 237, 1992, pages 209-229.
#
#    Stephen Lucas, Evelyn Sander, Laura Taalman,
#    Modeling dynamical systems for 3D printing,
#    Notices of the American Mathematical Society,
#    Volume 67, Number 11, December 2020, pages 1692-1705.
#
#  Input:
#
#    real T, the value of the independent variable.
#
#    real XYZ[3], the values of the dependent variables at time T.
#
#  Output:
#
#    real DXYZDT(3), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  kappa, lamda, t0, xyz0, tstop = rucklidge_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxyzdt = np.zeros ( 3 )

  dxyzdt[0] = kappa * x - lamda * y - y * z
  dxyzdt[1] = x
  dxyzdt[2] = - z + y * y

  return dxyzdt

def rucklidge_ode_test ( ):

#*****************************************************************************80
#
## rucklidge_ode_test() tests rucklidge_ode().
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
  print ( 'rucklidge_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve rucklidge_ode().' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  kappa, lamda, t0, xyz0, tstop = rucklidge_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    kappa = ', kappa )
  print ( '    lamda = ', lamda )
  print ( '    t0 =    ', t0 )
  print ( '    xyz0 =  ', xyz0 )
  print ( '    tstop = ', tstop )

  t, x, y, z = rucklidge_ode_solve_ivp ( )
  rucklidge_ode_plot_components ( t, x, y, z )
  rucklidge_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'rucklidge_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def rucklidge_ode_solve_ivp ( ):

#*****************************************************************************80
#
## rucklidge_ode_solve_ivp() solves rucklidge_ode() using solve_ivp().
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
 
  kappa, lamda, t0, xyz0, tstop = rucklidge_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( rucklidge_deriv, tspan, xyz0 )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def rucklidge_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## rucklidge_ode_plot_components() plots X(T), Y(T) and Z(T) for rucklidge_ode().
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
  plt.title ( 'rucklidge_ode() Time Series Plot' )
  filename = 'rucklidge_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def rucklidge_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## rucklidge_ode_plot_3d() plots (X,Y,Z) for rucklidge_ode().
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
  ax.set_title ( 'rucklidge_ode() 3D Plot' )
  filename = 'rucklidge_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def rucklidge_parameters ( kappa_user = None, lamda_user = None, \
  t0_user = None, xyz0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## rucklidge_parameters() returns parameters for rucklidge_ode().
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
#    real kappa_user: problem parameter.
#
#    real lamda_user: problem parameter.
#
#    real t0_user: the initial time.
#
#    real xyz0_user[3]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real kappa: problem parameter.
#
#    real lamda: problem parameter.
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
  if not hasattr ( rucklidge_parameters, "kappa_default" ):
    rucklidge_parameters.kappa_default = -2.0

  if not hasattr ( rucklidge_parameters, "lamda_default" ):
    rucklidge_parameters.lamda_default = -6.7

  if not hasattr ( rucklidge_parameters, "t0_default" ):
    rucklidge_parameters.t0_default = 0.0

  if not hasattr ( rucklidge_parameters, "xyz0_default" ):
    rucklidge_parameters.xyz0_default = np.array ( [ 1.0, 0.0, 4.5 ] )

  if not hasattr ( rucklidge_parameters, "tstop_default" ):
    rucklidge_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( kappa_user is not None ):
    rucklidge_parameters.kappa_default = kappa_user

  if ( lamda_user is not None ):
    rucklidge_parameters.lamda_default = lamda_user

  if ( t0_user is not None ):
    rucklidge_parameters.t0_default = t0_user

  if ( xyz0_user is not None ):
    rucklidge_parameters.xyz0_default = xyz0_user

  if ( tstop_user is not None ):
    rucklidge_parameters.tstop_default = tstop_user
#
#  Return values.
#
  kappa = rucklidge_parameters.kappa_default
  lamda = rucklidge_parameters.lamda_default
  t0 = rucklidge_parameters.t0_default
  xyz0 = rucklidge_parameters.xyz0_default
  tstop = rucklidge_parameters.tstop_default
  
  return kappa, lamda, t0, xyz0, tstop

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
  rucklidge_ode_test ( )
  timestamp ( )

