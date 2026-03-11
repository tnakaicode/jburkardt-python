#! /usr/bin/env python3
#
def sensitive_deriv ( t, y ):

#*****************************************************************************80
#
## sensitive_deriv() evaluates the derivative of sensitive_ode().
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
#    John D Cook,
#    Sensitive dependence on initial conditions in ODE's,
#    12 November 2013,
#    https://www.johndcook.com/blog/2013/11/12/sensitive-dependence-on-initial-conditions/
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT[2]: the value of the derivative.
#
  import numpy as np

  dydt = np.zeros ( 2 )
  dydt[0] = y[1]
  dydt[1] = y[0]

  return dydt

def sensitive_exact ( t ):

#*****************************************************************************80
#
## sensitive_exact() evaluates the exact solution of sensitive_ode().
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
#    John D Cook,
#    Sensitive dependence on initial conditions in ODE's,
#    12 November 2013,
#    https://www.johndcook.com/blog/2013/11/12/sensitive-dependence-on-initial-conditions/
#
#  Input:
#
#    real T: the times.
#
#  Output:
#
#    real Y[:,2], the exact solution values.
#
  import numpy as np

  t0, y0, tstop = sensitive_parameters ( )

  ep = y0[0] - 1.0

  n = t.shape[0]

  y = np.zeros ( [ n, 2 ] )
  for i in range ( 0, n ):
    y[i,0] =   ( 1.0 - ep / 2.0 ) * np.exp ( - t[i] ) \
           +           ep / 2.0   * np.exp (   t[i] )
    y[i,1] = - ( 1.0 - ep / 2.0 ) * np.exp ( - t[i] ) \
             +         ep / 2.0   * np.exp (   t[i] )

  return y

def sensitive_solve_ivp ( ):

#*****************************************************************************80
#
## sensitive_solve_ivp() solves sensitive_ode() using solve_ivp().
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
  print ( 'sensitive_solve_ivp():' )
  print ( '  Use solve_ivp() to solve sensitive_ode()' )
  print ( '' )

  ep = 1.0E-06
  print ( '  Initial condition perturbation ep = ', ep )

  plt.clf ( )

  for k in range ( 0, 3 ):
#
#  Get the parameters.
#
    t0, y0, tstop = sensitive_parameters ( )

    if ( k == 0 ):
      y0[0] = 1.0 + ep
    elif ( k == 1 ):
      y0[0] = 1.0
    else:
      y0[0] = 1.0 - ep

    t0, y0, tstop = sensitive_parameters ( t0, y0, tstop )

    print ( '' )
    print ( '  parameters:' )
    print ( '    t0 =    ', t0 )
    print ( '    y0 =    ', y0 )
    print ( '    tstop = ', tstop )
#
#  Estimate the solution.
#
    f = sensitive_deriv
    tspan = np.array ( [ t0, tstop ] )
    n = 101
    t = np.linspace ( t0, tstop, 101 )

    sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot the solution curve.
#
    plt.plot ( t, sol.y[0], linewidth = 2 )

  plt.title ( 'sensitive_ode(): solve_ivp()' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y(T) --->' )
  plt.legend ( [ 'Y''(0)=1+ep', 'Y''(0)=1', 'Y''(0)=1-ep' ] )
  filename = 'sensitive_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + "'" )
  plt.close ( )

  return

def sensitive_ode_test ( ):

#*****************************************************************************80
#
## sensitive_ode_test() solves sensitive_ode().
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
  print ( 'sensitive_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve sensitive_ode().' )
#
#  Get parameters.
#
  t0, y0, tstop = sensitive_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  sensitive_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sensitive_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def sensitive_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## sensitive_parameters() returns the parameters of sensitive_ode().
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
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( sensitive_parameters, "t0_default" ):
    sensitive_parameters.t0_default = 0.0

  if not hasattr ( sensitive_parameters, "y0_default" ):
    sensitive_parameters.y0_default = np.array ( [ 1.0, -1.0 ] )

  if not hasattr ( sensitive_parameters, "tstop_default" ):
    sensitive_parameters.tstop_default = 15.0
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    sensitive_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    sensitive_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    sensitive_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = sensitive_parameters.t0_default
  y0 = sensitive_parameters.y0_default
  tstop = sensitive_parameters.tstop_default
  
  return t0, y0, tstop

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
  sensitive_ode_test ( )

