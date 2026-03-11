#! /usr/bin/env python3
#
def logistic_exact_test ( ):

#*****************************************************************************80
#
## logistic_exact_test() tests logistic_exact().
#
#  Discussion:
#
#    The governing equation is
#
#      dydt = r * y * ( k - y ) / k
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'logistic_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
#
#  Get parameter values.
#
  r, k, t0, y0, tstop = logistic_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    r =     ', r )
  print ( '    k =     ', k )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  print ( '' )
  print ( '  Evaluate exact solution for varied values of y0:' )

  t = np.linspace ( t0, tstop, 101 )

  plt.clf ( )

  for y0 in [ 0.05, 0.1, 0.2, 0.5 ]:

    print ( '  Evaluate for y0 = ', y0 )

    logistic_parameters ( r, k, t0, y0, tstop )
    y = logistic_exact ( t )

    plt.plot ( t, y, linewidth = 2 )

  s = ( 'logistic_exact(): Y(0) = 0.05, 0.1, 0.2, 0.5' )
  plt.title ( s )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y(T) --->' )
  plt.legend ( [ '0.05', '0.1', '0.2', '0.5' ] )
  filename = 'logistic_exact.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'logistic_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def logistic_exact ( t ):

#*****************************************************************************80
#
## logistic_exact() evaluates the exact solution for logistic_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  import numpy as np

  r, k, t0, y0, tstop = logistic_parameters ( )

  y = ( k * y0 * np.exp ( r * ( t - t0 ) ) ) \
    / ( k + y0 * ( np.exp ( r * ( t - t0 ) ) - 1.0 ) )

  return y


def logistic_parameters ( r_user = None, k_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## logistic_parameters() returns parameter values for logistic_ode().
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
#    02 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r_user: the growth rate.
#
#    real k_user: the carrying capacity.
#
#    real t0_user: the initial time.
#
#    real y0_user: the initial condition.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real r: the growth rate.
#
#    real k: the carrying capacity.
#
#    real t0: the initial time.
#
#    real y0: the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( logistic_parameters, "r_default" ):
    logistic_parameters.r_default = 1.0

  if not hasattr ( logistic_parameters, "k_default" ):
    logistic_parameters.k_default = 1.0

  if not hasattr ( logistic_parameters, "t0_default" ):
    logistic_parameters.t0_default = 0.0

  if not hasattr ( logistic_parameters, "y0_default" ):
    logistic_parameters.y0_default = 0.5

  if not hasattr ( logistic_parameters, "tstop_default" ):
    logistic_parameters.tstop_default = 8.0
#
#  Update defaults if input was supplied.
#
  if ( r_user is not None ):
    logistic_parameters.r_default = r_user

  if ( k_user is not None ):
    logistic_parameters.k_default = k_user

  if ( t0_user is not None ):
    logistic_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    logistic_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    logistic_parameters.tstop_default = tstop_user
#
#  Return values.
#
  r = logistic_parameters.r_default
  k = logistic_parameters.k_default
  t0 = logistic_parameters.t0_default
  y0 = logistic_parameters.y0_default
  tstop = logistic_parameters.tstop_default
  
  return r, k, t0, y0, tstop

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
  logistic_exact_test ( )
  timestamp ( )

