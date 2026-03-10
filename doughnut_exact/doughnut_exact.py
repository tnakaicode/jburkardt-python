#! /usr/bin/env python3
#
def doughnut_exact_test ( ):

#*****************************************************************************80
#
## doughnut_exact_test() tests doughnut_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2025
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'doughnut_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test doughnut_exact().' )

  m, n, t0, y0, tstop = doughnut_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    m     = ', m )
  print ( '    n     = ', n )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )
  print ( '' )

  t = np.linspace ( t0, tstop, 1001 )
  y = doughnut_exact ( t )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( y[:,0], y[:,1], y[:,2], linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->' )
  ax.set_ylabel ( '<-- Y -->' )
  ax.set_zlabel ( '<-- Z -->' )
  ax.set_title ( 'doughnut_exact()' )
  filename = 'doughnut_exact.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'doughnut_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def doughnut_exact ( t ):

#*****************************************************************************80
#
## doughnut_exact(): exact solution of doughnut ODE.
#
#  Discussion:
#
#    The formula assumes that t0 = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Rational solution to the Korteweg-De Vries equation,
#    13 November 2023,
#    https://www.johndcook.com/blog/2023/11/13/rational-kdv/
#
#  Input:
#
#    real t(:): the time.
#
#  Output:
#
#    real y(:,3): the exact solution at time t.
#
  import numpy as np

  tnum = len ( t )

  m, n, _, y0, _ = doughnut_parameters ( )

  y = np.zeros ( [ tnum, 3 ] )

  a = y0[0]
  b = y0[1]
  c = y0[2]

  delta = 1.0 + a * a + b * b + c * c
  
  y[:,0] = ( 2.0 * a * np.cos ( m * t ) - 2.0 * b * np.sin ( m * t ) ) \
         / ( delta - 2.0 * c * np.sin ( n * t ) + ( 2.0 - delta ) * np.cos ( n * t ) )

  y[:,1] = ( 2.0 * a * np.sin ( m * t ) + 2.0 * b * np.cos ( m * t ) ) \
         / ( delta - 2.0 * c * np.sin ( n * t ) + ( 2.0 - delta ) * np.cos ( n * t ) )

  y[:,2] = ( 2.0 * c * np.cos ( n * t ) + ( 2.0 - delta ) * np.sin ( n * t ) ) \
         / ( delta - 2.0 * c * np.sin ( n * t ) + ( 2.0 - delta ) * np.cos ( n * t ) )

  return y

def doughnut_parameters ( m_user = None, n_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## doughnut_parameters() returns parameters for doughnut_ode().
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#    Suggested choices for m, n, (y0) include:
#
#      3,  5, (1, 1, 3.0)
#      4,  5, (1, 1, 0.3)
#      pi, 5, (1, 1, 0.3)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real m_user, n_user: problem parameters.
#
#    real t0_user: the initial time.
#
#    real y0_user(3): the initial condition.
#
#    real tstop_user: the final time.
#
#  output:
#
#    real m, n: problem parameters.
#
#    real t0: the initial time.
#
#    real y0(3): the initial condition.
#
#    real tstop: the final time.
#
  import numpy as np

  if not hasattr ( doughnut_parameters, "m_default" ):
    doughnut_parameters.m_default = 3.0

  if not hasattr ( doughnut_parameters, "n_default" ):
    doughnut_parameters.n_default = 5.0

  if not hasattr ( doughnut_parameters, "t0_default" ):
    doughnut_parameters.t0_default = 0.0

  if not hasattr ( doughnut_parameters, "y0_default" ):
    doughnut_parameters.y0_default = np.array ( [ 1.0, 1.0, 3.0 ] )

  if not hasattr ( doughnut_parameters, "tstop_default" ):
    doughnut_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( m_user is not None ):
    doughnut_parameters.m_default = m_user

  if ( n_user is not None ):
    doughnut_parameters.n_default = n_user

  if ( t0_user is not None ):
    doughnut_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    doughnut_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    doughnut_parameters.tstop_default = tstop_user
#
#  Return values.
#
  m = doughnut_parameters.m_default
  n = doughnut_parameters.n_default
  t0 = doughnut_parameters.t0_default
  y0 = doughnut_parameters.y0_default
  tstop = doughnut_parameters.tstop_default
  
  return m, n, t0, y0, tstop

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
  doughnut_exact_test ( )
  timestamp ( )

