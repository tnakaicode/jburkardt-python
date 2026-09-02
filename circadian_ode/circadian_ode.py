#! /usr/bin/env python3
#
def circadian_ode_test ( ):

#*****************************************************************************80
#
## circadian_ode_test() tests circadian_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'circadian_ode_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Solve circadian_ode().' )

  kappa1, kappa2, kappas, \
  k1, k2, k3, k4, kd, ki, km, \
  n, nud, num, nus, \
  v1, v2, v3, v4, \
  t0, u0, tstop = circadian_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    kappa1 = ', kappa1 )
  print ( '    kappa2 = ', kappa2 )
  print ( '    kappas = ', kappas )
  print ( '    k1     = ', k1 )
  print ( '    k2     = ', k2 )
  print ( '    k3     = ', k3 )
  print ( '    k4     = ', k4 )
  print ( '    kd     = ', kd )
  print ( '    ki     = ', ki )
  print ( '    km     = ', km )
  print ( '    n      = ', n )
  print ( '    nud    = ', nud )
  print ( '    num    = ', num )
  print ( '    nus    = ', nus )
  print ( '    v1     = ', v1 )
  print ( '    v2     = ', v2 )
  print ( '    v3     = ', v3 )
  print ( '    v4     = ', v4 )
  print ( '    t0     = ', t0 )
  print ( '    u0     = ', u0 )
  print ( '    tstop  = ', tstop )

  t, M, P0, P1, P2, PN = circadian_ode_solve_ivp ( )
#
#  Plot the time series.
#
  plt.clf ( )
  plt.plot ( t, M,  linewidth = 2, color = 'r' )
  plt.plot ( t, P0, linewidth = 2, color = 'g' )
  plt.plot ( t, P1, linewidth = 2, color = 'b' )
  plt.plot ( t, P2, linewidth = 2, color = 'c' )
  plt.plot ( t, PN, linewidth = 2, color = 'm' )
  plt.grid ( True )
  plt.xlabel ( '<--- Time --->' )
  plt.legend ( [ 'M(T)', 'P0(T)', 'P1(T)', 'P2(T)', 'PN(T)' ] )
  plt.title ( 'circadian_ode() Time Series' )
  filename = 'circadian_time.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Plot the phase plane.
#
  PT = P0 + P1 + P2 + PN

  plt.clf ( )
  plt.plot ( PT, M, linewidth = 2, color = 'r' )
  plt.grid ( True )
  plt.xlabel ( '<--- PT --->' )
  plt.ylabel ( '<--- M --->' )
  plt.title ( 'circadian_ode() Phase Plane' )
  filename = 'circadian_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'circadian_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def circadian_deriv ( t, u ):

#*****************************************************************************80
#
## circadian_deriv() evaluates the right hand side of circadian_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Goldbeter,
#    A model for circadian oscillation in the Drosophilia period protein (PER),
#    Proceedings of the Royal Society of London, B,
#    Volume 261, pages 319-324, 1995.
#
#  Input:
#
#    real t: the value of the independent variable.
#
#    real u[5]: the values of the dependent variables at time T.
#
#  Output:
#
#    real dudt(5), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  kappa1, kappa2, kappas, \
    k1, k2, k3, k4, kd, ki, km, \
    n, nud, num, nus, \
    v1, v2, v3, v4, \
    t0, u0, tstop = circadian_parameters ( )

  M  = u[0]
  P0 = u[1]
  P1 = u[2]
  P2 = u[3]
  PN = u[4]

  dMdt  =   nus * ki**n / ( ki**n + PN**n ) \
          - num * M     / ( km   + M )

  dP0dt =   kappas * M \
          - v1 * P0 / ( k1 + P0 ) \
          + v2 * P1 / ( k2 + P1 )

  dP1dt =   v1 * P0 / ( k1 + P0 ) \
          - v2 * P1 / ( k2 + P1 ) \
          - v3 * P1 / ( k3 + P1 ) \
          + v4 * P2 / ( k4 + P2 )

  dP2dt =   v3 * P1 / ( k3 + P1 ) \
          - v4 * P2 / ( k4 + P2 ) \
          - kappa1 * P2 \
          + kappa2 * PN \
          - nud * P2 / ( kd + P2 )

  dPNdt = kappa1 * P2 - kappa2 * PN

  dudt = np.array ( [ dMdt, dP0dt, dP1dt, dP2dt, dPNdt ] )

  return dudt

def circadian_ode_solve_ivp ( ):

#*****************************************************************************80
#
## circadian_ode_solve_ivp() solves circadian_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real t(:), M(:), P0(:), P1(:), P2(:), PN(:): values of the discrete solution.
#
  import numpy as np
  from scipy.integrate import solve_ivp
 
  kappa1, kappa2, kappas, \
    k1, k2, k3, k4, kd, ki, km, \
    n, nud, num, nus, \
    v1, v2, v3, v4, \
    t0, u0, tstop = circadian_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( circadian_deriv, tspan, u0, method = 'LSODA' )

  t  = sol.t
  M  = sol.y[0,:]
  P0 = sol.y[1,:]
  P1 = sol.y[2,:]
  P2 = sol.y[3,:]
  PN = sol.y[4,:]

  return t, M, P0, P1, P2, PN

def circadian_parameters ( \
  kappa1_user = None, kappa2_user = None, kappas_user = None,\
  k1_user = None, k2_user = None, k3_user = None, k4_user = None, \
  kd_user = None, ki_user = None, km_user = None, \
  n_user = None, nud_user = None, num_user = None, nus_user = None, \
  v1_user = None, v2_user = None, v3_user = None, v4_user = None, \
  t0_user = None, u0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## circadian_parameters() returns parameters for circadian_ode().
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
#    26 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Goldbeter,
#    A model for circadian oscillation in the Drosophilia period protein (PER),
#    Proceedings of the Royal Society of London, B,
#    Volume 261, pages 319-324, 1995.
#
#  Input:
#
#    real kappa1_user, kappa2_user, kappas_user,
#    k1_user, k2_user, k3_user, k4_user, kd_user, ki_user, km_user,
#    n_user, nud_user, num_user, nus_user,
#    v1_user, v2_user, v3_user, v4_user:
#    user requested values for problem parameters.
#
#    real t0_user: the initial time.
#
#    real u0_user[5]: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real kappa1, kappa2, kappas,
#    k1, k2, k3, k4, kd, ki, km,
#    n, nud, num, nus,
#    v1, v2, v3, v4:
#    current values for problem parameters.
#
#    real t0: the initial time.
#
#    real u0[5]: the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( circadian_parameters, "kappa1_default" ):
    circadian_parameters.kappa1_default = 1.9

  if not hasattr ( circadian_parameters, "kappa2_default" ):
    circadian_parameters.kappa2_default = 1.3

  if not hasattr ( circadian_parameters, "kappas_default" ):
    circadian_parameters.kappas_default = 0.38

  if not hasattr ( circadian_parameters, "k1_default" ):
    circadian_parameters.k1_default = 2.0

  if not hasattr ( circadian_parameters, "k2_default" ):
    circadian_parameters.k2_default = 2.0

  if not hasattr ( circadian_parameters, "k3_default" ):
    circadian_parameters.k3_default = 2.0

  if not hasattr ( circadian_parameters, "k4_default" ):
    circadian_parameters.k4_default = 2.0

  if not hasattr ( circadian_parameters, "kd_default" ):
    circadian_parameters.kd_default = 0.2

  if not hasattr ( circadian_parameters, "ki_default" ):
    circadian_parameters.ki_default = 1.0

  if not hasattr ( circadian_parameters, "km_default" ):
    circadian_parameters.km_default = 0.5

  if not hasattr ( circadian_parameters, "n_default" ):
    circadian_parameters.n_default = 4

  if not hasattr ( circadian_parameters, "nud_default" ):
    circadian_parameters.nud_default = 0.95

  if not hasattr ( circadian_parameters, "num_default" ):
    circadian_parameters.num_default = 0.65

  if not hasattr ( circadian_parameters, "nus_default" ):
    circadian_parameters.nus_default = 0.76

  if not hasattr ( circadian_parameters, "v1_default" ):
    circadian_parameters.v1_default = 3.2

  if not hasattr ( circadian_parameters, "v2_default" ):
    circadian_parameters.v2_default = 1.58

  if not hasattr ( circadian_parameters, "v3_default" ):
    circadian_parameters.v3_default = 5.0

  if not hasattr ( circadian_parameters, "v4_default" ):
    circadian_parameters.v4_default = 2.5

  if not hasattr ( circadian_parameters, "t0_default" ):
    circadian_parameters.t0_default = 0.0

  if not hasattr ( circadian_parameters, "u0_default" ):
    circadian_parameters.u0_default = np.array ( [ 0.5, 0.25, 0.25, 0.25, 1.00 ] )
#   circadian_parameters.u0_default = np.array ( [ 0.1, 0.25, 0.25, 0.25, 0.25 ] )
#   circadian_parameters.u0_default = np.array ( [ 1.9, 0.8,  0.8,  0.8,  0.8 ] )

  if not hasattr ( circadian_parameters, "tstop_default" ):
    circadian_parameters.tstop_default = 72.0
#
#  Update defaults if input was supplied.
#
  if ( kappa1_user is not None ):
    circadian_parameters.kappa1_default = kappa1_user

  if ( kappa2_user is not None ):
    circadian_parameters.kappa2_default = kappa2_user

  if ( kappas_user is not None ):
    circadian_parameters.kappas_default = kappas_user

  if ( k1_user is not None ):
    circadian_parameters.k1_default = k1_user

  if ( k2_user is not None ):
    circadian_parameters.k2_default = k2_user

  if ( k3_user is not None ):
    circadian_parameters.k3_default = k3_user

  if ( k4_user is not None ):
    circadian_parameters.k4_default = k4_user

  if ( kd_user is not None ):
    circadian_parameters.kd_default = kd_user

  if ( ki_user is not None ):
    circadian_parameters.ki_default = ki_user

  if ( km_user is not None ):
    circadian_parameters.km_default = km_user

  if ( n_user is not None ):
    circadian_parameters.n_default = n_user

  if ( nud_user is not None ):
    circadian_parameters.nud_default = nud_user

  if ( num_user is not None ):
    circadian_parameters.num_default = num_user

  if ( nus_user is not None ):
    circadian_parameters.nus_default = nus_user

  if ( v1_user is not None ):
    circadian_parameters.v1_default = v1_user

  if ( v2_user is not None ):
    circadian_parameters.v2_default = v2_user

  if ( v3_user is not None ):
    circadian_parameters.v3_default = v3_user

  if ( v4_user is not None ):
    circadian_parameters.v4_default = v4_user

  if ( t0_user is not None ):
    circadian_parameters.t0_default = t0_user

  if ( u0_user is not None ):
    circadian_parameters.u0_default = u0_user

  if ( tstop_user is not None ):
    circadian_parameters.tstop_default = tstop_user
#
#  Return values.
#
  kappa1 = circadian_parameters.kappa1_default
  kappa2 = circadian_parameters.kappa2_default
  kappas = circadian_parameters.kappas_default
  k1 = circadian_parameters.k1_default
  k2 = circadian_parameters.k2_default
  k3 = circadian_parameters.k3_default
  k4 = circadian_parameters.k4_default
  kd = circadian_parameters.kd_default
  ki = circadian_parameters.ki_default
  km = circadian_parameters.km_default
  n = circadian_parameters.n_default
  nud = circadian_parameters.nud_default
  num = circadian_parameters.num_default
  nus = circadian_parameters.nus_default
  v1 = circadian_parameters.v1_default
  v2 = circadian_parameters.v2_default
  v3 = circadian_parameters.v3_default
  v4 = circadian_parameters.v4_default
  t0 = circadian_parameters.t0_default
  u0 = circadian_parameters.u0_default
  tstop = circadian_parameters.tstop_default
  
  return kappa1, kappa2, kappas, \
    k1, k2, k3, k4, kd, ki, km, \
    n, nud, num, nus, \
    v1, v2, v3, v4, \
    t0, u0, tstop

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
  circadian_ode_test ( )
  timestamp ( )

