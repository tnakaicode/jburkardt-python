#! /usr/bin/env python3
#
def grazing_deriv ( t, y ):

#*****************************************************************************80
#
## grazing_deriv() evaluates the right hand side of grazing_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Thompson, Bruce Stewart,
#    Nonlinear Dynamics and Chaos,
#    Second Edition,
#    Wiley, 2002,
#    ISBN: 0-471-87645-3,
#    LC: QA871.T47.
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

  a, c1, c2, d1, d2, k, r1, t0, y0, tstop = grazing_parameters ( )

  u = y[0]
  v = y[1]

  dudt = r1 * u * ( 1.0 - u / k ) - c1 * v * ( 1.0 - np.exp ( - d1 * u ) )
  dvdt = - a * v                  + c2 * v * ( 1.0 - np.exp ( - d2 * u ) )

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def grazing_ode_test ( ):

#*****************************************************************************80
#
## grazing_ode_test() solves grazing_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'grazing_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve grazing_ode().' )

  a, c1, c2, d1, d2, k, r1, t0, y0, tstop = grazing_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a     = ', a )
  print ( '    c1    = ', c1 )
  print ( '    c2    = ', c2 )
  print ( '    d1    = ', d1 )
  print ( '    d2    = ', d2 )
  print ( '    k     = ', k )
  print ( '    r1    = ', r1 )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  grazing_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'grazing_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def grazing_parameters ( a_user = None, c1_user = None, c2_user = None, \
  d1_user = None, d2_user = None, k_user = None, r1_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## grazing_parameters() returns parameter values for grazing_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Thompson, Bruce Stewart,
#    Nonlinear Dynamics and Chaos,
#    Second Edition,
#    Wiley, 2002,
#    ISBN: 0-471-87645-3,
#    LC: QA871.T47.
#
#  Input:
#
#    real A_USER, the rate at which herbivores decline when the plant
#    density is low
#
#    real C1_USER, the maximum rate of food intake per herbivore,
#
#    real C2_USER, the rate at which herbivore decline is ameliorated
#    in cases of high plant density
#
#    real D1_USER, the grazing efficiency of the herbivore when 
#    the plant density is low
#
#    real D2_USER, the demographic efficiency of the plant, the ability
#    to regrow from a sparse state
#
#    real K_USER, the maximum ungrazed plant density
#
#    real R1_USER: the intrinsic rate of increase of the plants
#
#    real T0_USER: the initial time.
#
#    real Y0_USER(2): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A, the rate at which herbivores decline when the plant
#    density is low
#
#    real C1, the maximum rate of food intake per herbivore,
#
#    real C2, the rate at which herbivore decline is ameliorated
#    in cases of high plant density
#
#    real D1, the grazing efficiency of the herbivore when 
#    the plant density is low
#
#    real D2, the demographic efficiency of the plant, the ability
#    to regrow from a sparse state
#
#    real K, the maximum ungrazed plant density
#
#    real R1: the intrinsic rate of increase of the plants
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
  if not hasattr ( grazing_parameters, "a_default" ):
    grazing_parameters.a_default = 1.1

  if not hasattr ( grazing_parameters, "c1_default" ):
    grazing_parameters.c1_default = 1.2

  if not hasattr ( grazing_parameters, "c2_default" ):
    grazing_parameters.c2_default = 1.5

  if not hasattr ( grazing_parameters, "d1_default" ):
    grazing_parameters.d1_default = 0.001

  if not hasattr ( grazing_parameters, "d2_default" ):
    grazing_parameters.d2_default = 0.001

  if not hasattr ( grazing_parameters, "k_default" ):
    grazing_parameters.k_default = 3000

  if not hasattr ( grazing_parameters, "r1_default" ):
    grazing_parameters.r1_default = 0.8

  if not hasattr ( grazing_parameters, "t0_default" ):
    grazing_parameters.t0_default = 0.0

  if not hasattr ( grazing_parameters, "y0_default" ):
    grazing_parameters.y0_default = np.array ( [ 3000.0, 5.0 ] )

  if not hasattr ( grazing_parameters, "tstop_default" ):
    grazing_parameters.tstop_default = 100.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    grazing_parameters.a_default = a_user

  if ( c1_user is not None ):
    grazing_parameters.c1_default = c1_user

  if ( c2_user is not None ):
    grazing_parameters.c2_default = c2_user

  if ( d1_user is not None ):
    grazing_parameters.d1_default = d1_user

  if ( d2_user is not None ):
    grazing_parameters.d2_default = d2_user

  if ( k_user is not None ):
    grazing_parameters.k_default = k_user

  if ( r1_user is not None ):
    grazing_parameters.r1_default = r1_user

  if ( t0_user is not None ):
    grazing_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    grazing_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    grazing_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = grazing_parameters.a_default
  c1 = grazing_parameters.c1_default
  c2 = grazing_parameters.c2_default
  d1 = grazing_parameters.d1_default
  d2 = grazing_parameters.d2_default
  k = grazing_parameters.k_default
  r1 = grazing_parameters.r1_default
  t0 = grazing_parameters.t0_default
  y0 = grazing_parameters.y0_default
  tstop = grazing_parameters.tstop_default
  
  return a, c1, c2, d1, d2, k, r1, t0, y0, tstop

def grazing_solve_ivp ( ):

#*****************************************************************************80
#
## grazing_solve_ivp() solves grazing_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'grazing_solve_ivp():' )
  print ( '  Solve grazing_ode() using solve_ivp().' )

  a, c1, c2, d1, d2, k, r1, t0, y0, tstop = grazing_parameters ( )

  f = grazing_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot the solution.
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'g', linewidth = 2 )
  plt.plot ( t, sol.y[1], 'r', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'Population' )
  plt.title ( 'grazing_ode(): solve_ivp: time plot' )
  filename = 'grazing_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'Grass' )
  plt.ylabel ( 'Grass eaters' )
  plt.title ( 'grazing_ode(): solve_ivp: phase plot' )
  filename = 'grazing_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

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
  grazing_ode_test ( )
  timestamp ( )

