#! /usr/bin/env python3
#
def biochemical_nonlinear_conserved ( t, y ):

#*****************************************************************************80
#
## biochemical_nonlinear_conserved() evaluates two conserved quantities.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemes for biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T: the current time.
#
#    real Y(4): the current solution.
#
#    real A, B: parameter values.
#
#  Output:
#
#    real H(2): the conserved quantities.
#
  import numpy as np

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  E = np.array ( [ \
    [ 1.0, 0.0, a, a ], \
    [ 0.0, 1.0, b, b ] ] )

  h = np.matmul ( E, y )

  return h

def biochemical_nonlinear_deriv ( t, cnpd ):

#*****************************************************************************80
#
## biochemical_nonlinear_deriv(): derivative of biochemical_nonlinear_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T, CNPD(4): the arguments of the derivative.
#
#  Output:
#
#    real DCNPDDT(4): the value of the derivative.
#
  import numpy as np

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  c = cnpd[0]
  n = cnpd[1]
  p = cnpd[2]
  d = cnpd[3]

  S = np.array ( [
    [ -a,    0.0 ], \
    [ -b,    0.0 ], \
    [  1.0, -1.0 ], \
    [  0.0,  1.0 ] ] )

  r = np.array ( [ \
    rmax * c / ( kc + c ) * n * ( kn + n ) * p , \
    e * p ] )
  
  dcnpddt = np.matmul ( S, r )

  return dcnpddt

def biochemical_nonlinear_ode_test ( ):

#*****************************************************************************80
#
## biochemical_nonlinear_ode_test() tests biochemical_nonlinear_ode().
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
  print ( 'biochemical_nonlinear_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve biochemical_nonlinear_ode().' )

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    a =     ', a )
  print ( '    b =     ', b )
  print ( '    kc =    ', kc )
  print ( '    kn =    ', kn )
  print ( '    rmax =  ', rmax )
  print ( '    e =     ', e )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  biochemical_nonlinear_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'biochemical_nonlinear_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def biochemical_nonlinear_solve_ivp ( ):

#*****************************************************************************80
#
## biochemical_nonlinear_solve_ivp() applies solve_ivp() to biochemical_nonlinear_ode().
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

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( biochemical_nonlinear_deriv, \
    t_span = tspan, y0 = y0, t_eval = t )

  plt.clf ( )
  plt.plot ( t, sol.y[0,:], 'r-', linewidth = 3 )
  plt.plot ( t, sol.y[1,:], 'g-', linewidth = 3 )
  plt.plot ( t, sol.y[2,:], 'b-', linewidth = 3 )
  plt.plot ( t, sol.y[3,:], 'm-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---    --->' )
  plt.title ( 'biochemical_nonlinear_ode()' )
  plt.legend ( ( 'C', 'N', 'P', 'D' ) )
  filename = 'biochemical_nonlinear_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def biochemical_nonlinear_parameters ( a_user = None, b_user = None, \
  kc_user = None, kn_user = None, rmax_user = None, e_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## biochemical_nonlinear_parameters() returns parameters for biochemical_nonlinear_ode().
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
#    04 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER, B_USER: parameters;
#
#    real KC_USER, KN_USER: parameters
#
#    real RMAX_USER: a parameter.
#
#    real E_USER: a parameter.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[4]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real A, B: parameters;
#
#    real KC, KN: parameters
#
#    real RMAX: a parameter.
#
#    real E: a parameter.
#
#    real T0: the initial time.
#
#    real Y0[4]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( biochemical_nonlinear_parameters, "a_default" ):
    biochemical_nonlinear_parameters.a_default = 1.0

  if not hasattr ( biochemical_nonlinear_parameters, "b_default" ):
    biochemical_nonlinear_parameters.b_default = 1.0

  if not hasattr ( biochemical_nonlinear_parameters, "kc_default" ):
    biochemical_nonlinear_parameters.kc_default = 1.0

  if not hasattr ( biochemical_nonlinear_parameters, "kn_default" ):
    biochemical_nonlinear_parameters.kn_default = 1.0

  if not hasattr ( biochemical_nonlinear_parameters, "rmax_default" ):
    biochemical_nonlinear_parameters.rmax_default = 1.0

  if not hasattr ( biochemical_nonlinear_parameters, "e_default" ):
    biochemical_nonlinear_parameters.e_default = 0.3

  if not hasattr ( biochemical_nonlinear_parameters, "t0_default" ):
    biochemical_nonlinear_parameters.t0_default = 0.0

  if not hasattr ( biochemical_nonlinear_parameters, "y0_default" ):
    biochemical_nonlinear_parameters.y0_default = np.array ( [ 29.98, 9.98, 0.01, 0.01 ] )

  if not hasattr ( biochemical_nonlinear_parameters, "tstop_default" ):
    biochemical_nonlinear_parameters.tstop_default = 13.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    biochemical_nonlinear_parameters.a_default = a_user

  if ( b_user is not None ):
    biochemical_nonlinear_parameters.b_default = b_user

  if ( kc_user is not None ):
    biochemical_nonlinear_parameters.kc_default = kc_user

  if ( kn_user is not None ):
    biochemical_nonlinear_parameters.kn_default = kn_user

  if ( rmax_user is not None ):
    biochemical_nonlinear_parameters.rmax_default = rmax_user

  if ( e_user is not None ):
    biochemical_nonlinear_parameters.e_default = e_user

  if ( t0_user is not None ):
    biochemical_nonlinear_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    biochemical_nonlinear_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    biochemical_nonlinear_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = biochemical_nonlinear_parameters.a_default
  b = biochemical_nonlinear_parameters.b_default
  kc = biochemical_nonlinear_parameters.kc_default
  kn = biochemical_nonlinear_parameters.kn_default
  rmax = biochemical_nonlinear_parameters.rmax_default
  e = biochemical_nonlinear_parameters.e_default
  t0 = biochemical_nonlinear_parameters.t0_default
  y0 = biochemical_nonlinear_parameters.y0_default
  tstop = biochemical_nonlinear_parameters.tstop_default

  return a, b, kc, kn, rmax, e, t0, y0, tstop

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
  biochemical_nonlinear_ode_test ( )
  timestamp ( )

