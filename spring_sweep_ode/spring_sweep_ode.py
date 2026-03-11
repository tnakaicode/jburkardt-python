#! /usr/bin/env python3
#
def spring_deriv ( t, y ):

#*****************************************************************************80
#
## spring_deriv() returns the right hand side of spring_ode().
#
#  Discussion:
#
#    Y1 is the displacement
#    Y2 is the velocity
#
#    M is the mass.
#    B is the damping.
#    K is the spring stiffness.
#
#    The second order ODE:
#
#      m * x'' + b * x' + k * x = 0
#
#    is transformed into a pair of first order ODE's
#    using the variables:
#
#      y(1) = x,
#      y(2) = x'
#
#    so that
#
#      y'(1) = y(2)
#      y'(2) = - ( k / m ) y(1) - ( b / m ) y(2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the current time.
#
#    real Y(2), the current state values.
#
#  Output:
#
#    real dydt(2), the time derivatives of the current state values.
#
  import numpy as np

  m, b, k, t0, y0, tstop = spring_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - ( k / m ) * u - ( b / m ) * v

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def spring_parameters ( m_user = None, b_user = None, k_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## spring_parameters() returns parameters for spring_ode().
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
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real M_USER: the mass
#
#    real B_USER: the damping coefficient
#
#    real K_USER: the spring stiffness.
#
#    real T0_USER: the initial time, in seconds
#
#    real Y0_USER(2): the initial values.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real M: the mass
#
#    real B: the damping coefficient
#
#    real K: the spring stiffness.
#
#    real T0: the initial time, in seconds
#
#    real Y0(2): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize the defaults.
#
  if not hasattr ( spring_parameters, "m_default" ):
    spring_parameters.m_default = 5.0

  if not hasattr ( spring_parameters, "b_default" ):
    spring_parameters.b_default = 0.1

  if not hasattr ( spring_parameters, "k_default" ):
    spring_parameters.k_default = 1.5

  if not hasattr ( spring_parameters, "t0_default" ):
    spring_parameters.t0_default = 0.0

  if not hasattr ( spring_parameters, "y0_default" ):
    spring_parameters.y0_default = np.array ( [ 0.0, 1.0 ] )

  if not hasattr ( spring_parameters, "tstop_default" ):
    spring_parameters.tstop_default = 25.0
#
#  Update defaults if input was supplied.
#
  if ( m_user is not None ):
    spring_parameters.m_default = m_user

  if ( b_user is not None ):
    spring_parameters.b_default = b_user

  if ( k_user is not None ):
    spring_parameters.k_default = k_user

  if ( t0_user is not None ):
    spring_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    spring_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    spring_parameters.tstop_default = tstop_user
#
#  Return values.
#
  m = spring_parameters.m_default
  b = spring_parameters.b_default
  k = spring_parameters.k_default
  t0 = spring_parameters.t0_default
  y0 = spring_parameters.y0_default
  tstop = spring_parameters.tstop_default
  
  return m, b, k, t0, y0, tstop

def spring_peak_display ( bmat, kmat, pmat ):

#*****************************************************************************80
#
## spring_peak_display() displays the peak values for spring_ode() solutions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real bmat(M,N), kmat(M,N), the values of B and K for which
#    the ODE was solved.
#
#    real pmat(M,N), the maximum value of the ODE solution for
#    a given pair of K and B values.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( bmat, kmat, pmat, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'spring_ode() sweep' )
  ax.set_xlabel ( '<--- Damping B --->' )
  ax.set_ylabel ( '<--- Stiffness K --->' )
  ax.set_zlabel ( '<--- Peak displacement --->' )
  filename = 'spring_sweep_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def spring_sweep ( bmat, kmat ):

#*****************************************************************************80
#
## spring_sweep() finds peak values of spring_ode() over a mesh of parameter values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real bmat(M,N), a table of B values.
#
#    real kmat(M,N), a table of K values.
#
#  Output:
#
#    real pmat(M,N), a vector containing the maximum value of
#    the ODE solution over a fixed time interval, for every combination
#    of B and K values.
#
  from scipy.integrate import solve_ivp
  import numpy as np

  print ( '' )
  print ( 'spring_sweep():' )
  print ( '  Tabulate the maximum solution value of spring_ode()' )
  print ( '  over a range of K and B values.' )

  bnum, knum = bmat.shape
#
#  Define an array to hold the results, and initialize it to NAN.
#
  pmat = np.zeros ( [ bnum, knum ] )
#
#  Solve the ODE for every pair of K and B values.
#
  m, b, k, t0, y0, tstop = spring_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  f = spring_deriv
  t = np.linspace ( t0, tstop, 101 )

  for i in range ( 0, bnum ):
    for j in range ( 0, knum ):
#
#  Replace default values of B and K.
#
      b = bmat[i,j]
      k = kmat[i,j]
      m, b, k, t0, y0, tstop = spring_parameters ( m, b, k, t0, y0, tstop )
#
#  Solve the ODE.
#
      sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Retrieve the maximum value achieved by this solution.
#
      pmat[i,j] = np.max ( sol.y[0] )

  return pmat

def spring_sweep_ode_test ( ):

#*****************************************************************************80
#
## spring_sweep_ode_test(): parameter sweep of spring_ode().
#
#  Discussion:
#
#    This is a parameter sweep study of a 2nd order ODE system.
#
#      m*x'' + b*x' + k*x = 0
#
#    We solve the ODE for a time span of 0 to 25 seconds, with initial
#    conditions X(0) = 0 and X'(0) = 1. We sweep the parameters "b" and "k"
#    and record the peak values of X for each condition. At the end, we plot a
#    surface of the results.
#
#    The results can be displayed by calling sweep_ode_display.m.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'spring_sweep_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Sweep through sets of values of parameters B and K,' )
  print ( '  computing the solution of spring_ode() corresponding to each set.' )
  print ( '  For each solution X(T), determine the maximum value over time.' )
  print ( '  Construct a contour plot of XMAX(B,K).' )
#
#  Initialization:
#
  bnum = 50
  bvec = np.linspace ( 0.1, 5.0, bnum )
  knum = 71
  kvec = np.linspace ( 1.5, 5.0, knum )

  bmat, kmat = np.meshgrid ( bvec, kvec )
#
#  Solve the ODE for every pair of K and B values and return the maximum
#  value over the time interval.
#
  pmat = spring_sweep ( bmat, kmat )
#
#  Display the results.
#
  spring_peak_display ( bmat, kmat, pmat )
#
#  Terminate.
#
  print ( '' )
  print ( 'spring_sweep_ode_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

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
  spring_sweep_ode_test ( )
  timestamp ( )
 
