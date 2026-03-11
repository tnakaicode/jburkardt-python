#! /usr/bin/env python3
#
def lindberg_exact_test ( ):

#*****************************************************************************80
#
## lindberg_exact_test() tests lindberg_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import warnings

  print ( '' )
  print ( 'lindberg_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  lindberg_exact() evaluates the exact solution of the Lindberg ODE.' )
#
#  Disable warnings.
#
  print ( '' )
  print ( '  Because of many overflows, underflows, and divides by zero' )
  print ( '  we are simply going to suppress ALL warnings (sorry!)' )

  warnings.filterwarnings ( "ignore" )
#
#  Get parameters.
#
  t0, y0, tstop = lindberg_parameters ( )
#
#  Report the parameters.
#
  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )
#
#  Evaluate residual.
#
  lindberg_resid_test ( )
#
#  Plot components.
#
  lindberg_plot_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lindberg_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def lindberg_exact ( t ):

#*****************************************************************************80
#
## lindberg_exact() evaluates the exact solution of the Lindberg ODE.
#
#  Discussion:
#
#    The formula was supplied by Wenlong Pei.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t(n): the evaluation points.
#
#  Output:
#
#    real y(n,4): the function values.
#
#    real dydt(n,4): the derivative values.
#
  import numpy as np

  n = t.shape[0]
  y = np.zeros ( [ n, 4 ] )
  dydt = np.zeros ( [ n, 4 ] )

  g1 = 10.0**4 * ( t + 2.0 * np.exp ( - t ) - 2.0 )
  g2 = 10.0**4 * ( 1.0 - np.exp ( - t ) - t * np.exp ( -t ) )

  dg1dt = 10.0**4 * ( 1.0 - 2.0 * np.exp ( - t ) )
  dg2dt = 10.0**4 * (  t * np.exp ( - t ) )

  y[:,0] = np.exp ( g1 ) * ( np.cos ( g2 ) + np.sin ( g2 ) )
  y[:,1] = np.exp ( g1 ) * ( np.cos ( g2 ) - np.sin ( g2 ) )
  y[:,2] = 1.0 - 2.0 * np.exp ( - t )
  y[:,3] = t * np.exp ( - t )

  dydt[:,0] = np.exp ( g1 ) * dg1dt * ( np.cos ( g2 ) + np.sin ( g2 ) ) \
            + np.exp ( g1 ) * ( - np.sin ( g2 ) + np.cos ( g2 ) ) * dg2dt

  dydt[:,1] = np.exp ( g1 ) * dg1dt * ( np.cos ( g2 ) - np.sin ( g2 ) ) \
            + np.exp ( g1 ) * ( - np.sin ( g2 ) - np.cos ( g2 ) ) * dg2dt

  dydt[:,2] = 2.0 * np.exp ( - t )
  dydt[:,3] = ( 1.0 - t ) * np.exp ( - t )

  return y, dydt

def lindberg_parameters ( t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## lindberg_parameters() returns the parameters of lindberg_ode().
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
#    28 January 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time.
#
#    real Y0_USER(4): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0(4): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( lindberg_parameters, "t0_default" ):
    lindberg_parameters.t0_default = 0.0

  if not hasattr ( lindberg_parameters, "y0_default" ):
    lindberg_parameters.y0_default = np.array ( [ 1.0, 1.0, -1.0, 0.0 ] )

  if not hasattr ( lindberg_parameters, "tstop_default" ):
    lindberg_parameters.tstop_default = 3.91
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    lindberg_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    lindberg_parameters.y0_default = y0_user.copy()

  if ( tstop_user is not None ):
    lindberg_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = lindberg_parameters.t0_default
  y0 = lindberg_parameters.y0_default.copy ( )
  tstop = lindberg_parameters.tstop_default
  
  return t0, y0, tstop

def lindberg_plot_test ( ):

#*****************************************************************************80
#
## lindberg_plot_test() plots the Lindberg ODE solution components.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lindberg_plot_test():' )
  print ( '  Plot the Lindberg ODE solution components.' )

  t0, y0, tstop = lindberg_parameters ( )

  t = np.linspace ( t0, tstop, 101 )
  y, dydt = lindberg_exact ( t )

  plt.clf ( )
  plt.plot ( t, np.log ( np.abs ( y[:,0] ) ), 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- log(|y1(t)|) -->' )
  plt.title ( 'lindberg exact log(|y1|)' )
  filename = 'lindberg_exact_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, np.log ( np.abs ( y[:,1] ) ), 'b-',linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- log(|y2|)(t) -->' )
  plt.title ( 'lindberg exact log(|y2|)' )
  filename = 'lindberg_exact_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, y[:,2], 'b-',linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y3(t) -->' )
  plt.title ( 'lindberg exact y3' )
  filename = 'lindberg_exact_y3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, y[:,3], 'b-',linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y4(t) -->' )
  plt.title ( 'lindberg exact y4' )
  filename = 'lindberg_exact_y4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def lindberg_resid ( t, y, dydt ):

#*****************************************************************************80
#
## lindberg_resid() returns the residual of the Lindberg ODE.
#
#  Discussion:
#
#    Note that components y1(t) and y2(t) first sink to extraordinarily
#    small values, and then undergo explosive growth, sometime before t=1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Bengt Lindberg,
#    On a dangerous property of methods for stiff differential equations,
#    BIT Numerical Mathematics,
#    Volume 14, 1974, pages 430-436.
#
#    Daniel Watanabe, Qasim Sheikh,
#    One-leg formulas for stiff ordinary differential equations,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 5, Number 2, June 1984, pages 489-496.
#
#  Input:
#
#    real T(N): selected time values.
#
#    real Y(N,4): corresponding solution values.
#
#    real DYDT(N,4): corresponding derivate values.
#
#  Output:
#
#    real R(N,4): the residuals.
#
  import numpy as np

  n = t.shape[0]
  r = np.zeros ( [ n, 4 ] )

  r[:,0] = dydt[:,0] - (   10.0**4 * y[:,0] * y[:,2] + 10.0**4 * y[:,1] * y[:,3] )  
  r[:,1] = dydt[:,1] - ( - 10.0**4 * y[:,0] * y[:,3] + 10.0**4 * y[:,1] * y[:,2] )
  r[:,2] = dydt[:,2] - (   1.0 - y[:,2] )
  r[:,3] = dydt[:,3] - ( - 0.5 * y[:,2] - y[:,3] + 0.5 )
 
  return r

def lindberg_resid_test ( ):

#*****************************************************************************80
#
## lindberg_resid_test() computes residuals of the Lindberg ODE exact solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'lindberg_resid_test():' )
  print ( '  Compute the residuals of the exact solution components' )
  print ( '  of the Lindberg ODE.' )
  print ( '  Report the reslative errors.' )

  t0, y0, tstop = lindberg_parameters ( )

  n = 21
  t = np.linspace ( t0, tstop, n )

  y, dydt = lindberg_exact ( t )
  r = lindberg_resid ( t, y, dydt )
#
#  Limit magnitude of y1 and y2.
#
  for i in range ( 0, n ):
    for j in range ( 0, 4 ):
      y[i,j] = min ( y[i,j],  1.0E+6 )
      y[i,j] = max ( y[i,j], -1.0E+6 )

  for i in range ( 0, n ):
    for j in range ( 0, 4 ):
      if ( abs ( y[i,j] < np.finfo(float).eps ) ):
        y[i,j] = 0.0
#
#  Compute relative error.
#
  e = r / y
#
#  If e is NAN, reset e to -1, and reset r to 0.
#  Then if r is 0, reset e to 0.
#
  TF = np.isnan ( e );
  r[TF] = 0.0;
  e[TF] = -1.0;

  TF = np.where ( r == 0.0 )
  e[TF] = 0.0;

  print ( '' )
  print ( '  Relative error in Y1, Y2, Y3, Y4 at selected T values:' )

  print ( e )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  lindberg_exact_test ( )
  timestamp ( )

