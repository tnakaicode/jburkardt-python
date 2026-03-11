#! /usr/bin/env python3
#
def lorenz96_ode_test ( ):

#*****************************************************************************80
#
## lorenz96_ode_test() tests lorenz96_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lorenz96_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve lorenz96_ode().' )

  n, force, perturb, t0, xyz0, tstop = lorenz96_parameters ( )

  print ( '' )
  print ( '  parameter values:' )
  print ( '    n =       ', n )
  print ( '    force =   ', force )
  print ( '    perturb = ', perturb )
  print ( '    t0 =      ', t0 )
  print ( '    xyz0 =    ', xyz0 )
  print ( '    tstop =   ', tstop )

  t, y = lorenz96_ode_solve_ivp ( )
  lorenz96_ode_plot_components ( t, y )
  lorenz96_ode_plot_3d ( t, y )
#
#  Terminate.
#
  print ( '' )
  print ( 'lorenz96_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def lorenz96_deriv ( t, y ):

#*****************************************************************************80
#
## lorenz96_deriv() evaluates the right hand side of lorenz96_ode().
#
#  Discussion:
#
#    dy(i)/dt = ( y(i+1) - y(i-2) ) * y(i-1) - y(i) + force
#    where force is a constant independent of i
#    and the indices wrap around.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the value of the independent variable.
#
#    real Y[N], the values of the dependent variables at time T.
#
#  Output:
#
#    real DYDT[N], the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  n, force, _, _, _, _ = lorenz96_parameters ( )

  i = np.arange ( 0, n )
  ip1 = np.roll ( i, -1 )
  im1 = np.roll ( i, +1 )
  im2 = np.roll ( i, +2 )

  dydt = ( y[ip1] - y[im2] ) * y[im1] - y[i] + force

  return dydt

def lorenz96_ode_solve_ivp ( ):

#*****************************************************************************80
#
## lorenz96_ode_solve_ivp() solves lorenz96_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T[*], Y[N,*], values of the discrete solution.
#
  import numpy as np
  from scipy.integrate import solve_ivp
 
  _, _, _, t0, y0, tstop = lorenz96_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  sol = solve_ivp ( lorenz96_deriv, tspan, y0 )

  return sol.t, sol.y

def lorenz96_ode_plot_components ( t, y ):

#*****************************************************************************80
#
## lorenz96_ode_plot_components() plots each Y[I,*] for lorenz96_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T[*], the value of the independent variable.
#
#    real Y[N,*], the values of the dependent variables at time T.
#
  import matplotlib.pyplot as plt
#
#  Plot the data.
#
  n, _, _, _, _, _ = lorenz96_parameters ( )

  for i in range ( 0, n ):
    plt.clf ( )
    plt.plot ( t, y[i,:], linewidth = 2 )
    plt.grid ( True )
    plt.xlabel ( '<--- Time --->' )
    plt.ylabel ( '<--- Y[' + str ( i ) + '] --->' )
    plt.title ( 'lorenz96_ode(): Y[' + str ( i ) + ']' )
    filename = 'lorenz96_ode_y' + str ( i ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )

  return

def lorenz96_ode_plot_3d ( t, y ):

#*****************************************************************************80
#
## lorenz96_ode_plot_3d() plots (Y0, Y1, Y2) for lorenz96_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:), the value of the independent variable.
#
#    real Y[N,:], the values of the dependent variables at time T.
#
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( y[0,:], y[1,:], y[2,:], linewidth = 1, color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<--- Y0(T) --->' )
  ax.set_ylabel ( '<--- Y1(T) --->' )
  ax.set_zlabel ( '<--- Y2(T) --->' )
  ax.set_title ( 'lorenz96_ode(): 3D Plot' )
  filename = 'lorenz96_ode_3d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def lorenz96_parameters ( n_user = None, force_user = None, \
  perturb_user = None, t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## lorenz96_parameters() returns parameters for lorenz96_ode().
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
#    29 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real n_user: problem parameter.
#
#    real force_user: problem parameter.
#
#    real perturb_user: problem parameter.
#
#    real t0_user: the initial time.
#
#    real y0_user: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real n: problem parameter.
#
#    real force: problem parameter.
#
#    real perturb: problem parameter.
#
#    real t0: the initial time.
#
#    real y0: the initial condition.
#
#    real tstop: the final time.
#
  from numpy.random import default_rng
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( lorenz96_parameters, "n_default" ):
    lorenz96_parameters.n_default = 4

  if not hasattr ( lorenz96_parameters, "force_default" ):
    lorenz96_parameters.force_default = 8.0

  if not hasattr ( lorenz96_parameters, "perturb_default" ):
    lorenz96_parameters.perturb_default = 0.001

  if not hasattr ( lorenz96_parameters, "t0_default" ):
    lorenz96_parameters.t0_default = 0.0

  if not hasattr ( lorenz96_parameters, "y0_default" ):
    rng = default_rng ( )
    s = lorenz96_parameters.perturb_default \
      * rng.standard_normal ( size = lorenz96_parameters.n_default )
    lorenz96_parameters.y0_default = lorenz96_parameters.force_default \
      * np.ones ( lorenz96_parameters.n_default ) + s

  if not hasattr ( lorenz96_parameters, "tstop_default" ):
    lorenz96_parameters.tstop_default = 30.0
#
#  Update defaults if input was supplied.
#
  if ( n_user is not None ):
    lorenz96_parameters.n_default = n_user

  if ( force_user is not None ):
    lorenz96_parameters.force_default = force_user

  if ( perturb_user is not None ):
    lorenz96_parameters.perturb_default = perturb_user

  if ( t0_user is not None ):
    lorenz96_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    lorenz96_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    lorenz96_parameters.tstop_default = tstop_user
#
#  Return values.
#
  n = lorenz96_parameters.n_default
  force = lorenz96_parameters.force_default
  perturb = lorenz96_parameters.perturb_default
  t0 = lorenz96_parameters.t0_default
  y0 = lorenz96_parameters.y0_default
  tstop = lorenz96_parameters.tstop_default
  
  return n, force, perturb, t0, y0, tstop

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  lorenz96_ode_test ( )
  timestamp ( )

