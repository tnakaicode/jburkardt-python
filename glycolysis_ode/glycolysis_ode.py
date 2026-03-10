#! /usr/bin/env python3
#
def glycolysis_deriv ( t, y ):

#*****************************************************************************80
#
## glycolysis_deriv() evaluates the right hand side of glycolysis_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Evgeni Selkov,
#    Self-oscillations in Glycolysis,
#    European Journal of Biochemistry,
#    Volume 4, 1968, pages 79-86.
#
#  Input:
#
#    real T, the current time.
#
#    real Y(2), the current solution.
#
#  Output:
#
#    real DYDT(2), the right hand side.
#
  import numpy as np

  u = y[0]
  v = y[1]

  a, b, t0, y0, tstop = glycolysis_parameters ( )
  dudt = - u + a * v + u**2 * v
  dvdt =   b - a * v - u**2 * v

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def glycolysis_equilibrium ( ):

#*****************************************************************************80
#
## glycolysis_equilibrium() returns the equilibrium solution of glycolysis_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real Y_EQUI(2): the equilibrium solution.
#
  import numpy as np

  a, b, t0, y0, tstop = glycolysis_parameters ( )

  y_equi = np.array ( [ b, b/(a+b**2) ] )

  return y_equi

def glycolysis_equilibrium_test ( ):

#*****************************************************************************80
#
## glycolysis_equilibrium_test() verifies the equilibrium solution.
#
#  Discussion:
#
#    For any (positive) parameter choices, the equilibrium solution 
#    should satisfy dy/dt=[0,0].
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'glycolysis_equilibrium_test():' )
  print ( '  Verify that dy/dt=[0,0] for any parameter values.' )

  a_save, b_save, t0, y0, tstop = glycolysis_parameters ( )

  print ( '' )
  print ( '  (a,b) y_equi, t_equi, dydt' )
  print ( '' )
  for i in range ( 0, 5 ):
    a = rng.random ( )
    b = rng.random ( )
    glycolysis_parameters ( a, b, t0, y0, tstop )
    y_equi = glycolysis_equilibrium ( )
    t_equi = rng.random ( )
    dydt = glycolysis_deriv ( t_equi, y_equi )
    print ( '  (',a,',',b,'): ', y_equi, ',', t_equi, ',', dydt )
#
#  Restore default parameters.
#
  glycolysis_parameters ( a_save, b_save, t0, y0, tstop )
  
  return

def glycolysis_solve_ivp ( ):

#*****************************************************************************80
#
## glycolysis_solve_ivp() solves glycolysis_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'glycolysis_solve_ivp()' )
  print ( '  Use solve_ivp() to solve glycolysis_ode().' )

  a, b, t0, y0, tstop = glycolysis_parameters ( )

  f = glycolysis_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 1001
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot the solution.
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'g', linewidth = 2 )
  plt.plot ( t, sol.y[1], 'r', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'Concentration' )
  plt.title ( 'glycolysis_ode(): solve_ivp, time plot' )
  plt.legend ( [ 'ADP', 'FDP' ] )
  filename = 'glycolysis_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'ADP' )
  plt.ylabel ( 'F6P' )
  plt.title ( 'glycolysis_ode(): solve_ivp, Phase Plot' )
  filename = 'glycolysis_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def glycolysis_ode_test ( ):

#*****************************************************************************80
#
## glycolysis_ode_test() solves glycolysis_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'glycolysis_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve glycolysis_ode().' )

  alpha, gamma, t0, y0, tstop = glycolysis_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    alpha = ', alpha )
  print ( '    gamma = ', gamma )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )
#
#  Verify the equilibrium solution.
#
  glycolysis_equilibrium_test ( )
#
#  Solve the ODE.
#
  glycolysis_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'glycolysis_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def glycolysis_parameters ( a_user = None, b_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## glycolysis_parameters() returns parameters for glycolysis_ode().
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
#    29 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER, B_USER: the parameter values
#
#    real T0_USER: the initial time.
#
#    real Y0_USER(2): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A, B: the parameter values
#
#    real T0: the initial time.
#
#    real Y0(2): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( glycolysis_parameters, "a_default" ):
    glycolysis_parameters.a_default = 0.08

  if not hasattr ( glycolysis_parameters, "b_default" ):
    glycolysis_parameters.b_default = 0.6

  if not hasattr ( glycolysis_parameters, "t0_default" ):
    glycolysis_parameters.t0_default = 0.0

  if not hasattr ( glycolysis_parameters, "y0_default" ):
    glycolysis_parameters.y0_default = np.array ( [ 0.9, 0.7 ] )

  if not hasattr ( glycolysis_parameters, "tstop_default" ):
    glycolysis_parameters.tstop_default = 50.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    glycolysis_parameters.a_default = a_user

  if ( b_user is not None ):
    glycolysis_parameters.b_default = b_user

  if ( t0_user is not None ):
    glycolysis_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    glycolysis_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    glycolysis_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = glycolysis_parameters.a_default
  b = glycolysis_parameters.b_default
  t0 = glycolysis_parameters.t0_default
  y0 = glycolysis_parameters.y0_default.copy()
  tstop = glycolysis_parameters.tstop_default
  
  return a, b, t0, y0, tstop

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

if ( __name__ == "__main__" ):
  timestamp ( )
  glycolysis_ode_test ( )
  timestamp ( ) 

