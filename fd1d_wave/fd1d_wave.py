#! /usr/bin/env python3
#
def fd1d_wave_test ( ):

#*****************************************************************************80
#
## fd1d_wave_test() tests fd1d_wave().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fd1d_wave_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test fd1d_wave().' )

  fd1d_wave_test01 ( )
  fd1d_wave_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fd1d_wave_test():' )
  print ( '  Normal end of execution.' )

  return

def fd1d_wave_alpha ( x_num, x1, x2, t_num, t1, t2, c ):

#*****************************************************************************80
#
## fd1d_wave_alpha() computes ALPHA for the 1D wave equation.
#
#  Discussion:
#
#    The explicit timestepping procedure uses the quantity ALPHA, which
#    is determined by this function.
#
#    If the spatial region bounds are X1 <= X <= X2, containing X_NUM equally
#    spaced nodes, including the endpoints, and the time domain similarly
#    extends from T1 <= T <= T2 containing T_NUM equally spaced time values,
#    then
#
#      ALPHA = C * DT / DX
#            = C * ( ( T2 - T1 ) / ( T_NUM - 1 ) )
#                / ( ( X2 - X1 ) / ( X_NUM - 1 ) ).
#
#    For a stable computation, it must be the case that ALPHA < 1.
#
#    If ALPHA is greater than 1, then the middle coefficient 1-C^2 DT^2 / DX^2 
#    is negative, and the sum of the magnitudes of the three coefficients becomes 
#    unbounded.  In such a case, the user must reduce the time step size 
#    appropriately.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Input:
#
#    integer X_NUM, the number of nodes in the X direction.
#
#    real X1, X2, the first and last X coordinates.
#
#    integer T_NUM, the number of time steps, including the 
#    initial condition.
#
#    real T1, T2, the first and last T coordinates.
#
#    real C, a parameter which gives the speed of waves.
#
#  Output:
#
#    real ALPHA, the stability coefficient.
#
  import numpy as np

  t_delta = ( t2 - t1 ) / ( t_num - 1 )
  x_delta = ( x2 - x1 ) / ( x_num - 1 )
  alpha = c * t_delta / x_delta

  print ( '' )
  print ( '  Stability condition ALPHA = C * DT / DX = ', alpha )

  if ( 1.0 < np.abs ( alpha ) ):
    print ( '' )
    print ( 'fd1d_wave_alpha(): Warning!' )
    print ( '  The stability condition |ALPHA| <= 1 fails.' )
    print ( '  Computed results are liable to be inaccurate.' )

  return alpha

def fd1d_wave ( x_num, x1, x2, t_num, t1, t2, c, u_x1, u_x2, u_t1, ut_t1 ):

#*****************************************************************************80
#
## fd1d_wave() computes a finite difference solution of the 1D wave equation.
#
#  Discussion:
#
#    This program solves the 1D wave equation of the form:
#
#      c^2 Uxx = Utt
#
#    over the spatial interval [X1,X2] and time interval [T1,T2],
#    with initial conditions:
#
#      U(T1,X)  = U_T1(X),
#      Ut(T1,X) = UT_T1(X),
#
#    and boundary conditions of Dirichlet type:
#
#      U(T,X1) = U_X1(T),
#      U(T,X2) = U_X2(T).
#
#    The value C represents the propagation speed of waves.
#
#    The program uses the finite difference method, and marches
#    forward in time, solving for all the values of U at the next
#    time step by using the values known at the previous two time steps.
#
#    Central differences may be used to approximate both the time
#    and space derivatives in the original differential equation.
#
#    Thus, assuming we have available the approximated values of U
#    at the current and previous times, we may write a discretized
#    version of the wave equation as follows:
#
#      Uxx(T,X) = ( U(T,   X+dX) - 2 U(T,X) + U(T,   X-dX) ) / dX^2
#      Utt(T,X) = ( U(T+dt,X   ) - 2 U(T,X) + U(T-dt,X   ) ) / dT^2
#
#    If we multiply the first term by C^2 and solve for the single
#    unknown value U(T+dt,X), we have:
#
#      U(T+dT,X) =        (     C^2 * dT^2 / dX^2 ) * U(T,   X+dX)
#                  +  2 * ( 1 - C^2 * dT^2 / dX^2 ) * U(T,   X   )
#                  +      (     C^2 * dT^2 / dX^2 ) * U(T,   X-dX)
#                  -                                  U(T-dT,X   )
#
#    (Equation to advance from time T to time T+dT, except for FIRST step!)
#
#    However, on the very first step, we only have the values of U
#    for the initial time, but not for the previous time step.
#    In that case, we use the initial condition information for dUdT
#    which can be approximated by a central difference that involves
#    U(T+dT,X) and U(T-dT,X):
#
#      dU/dT(T,X) = ( U(T+dT,X) - U(T-dT,X) ) / ( 2 * dT )
#
#    and so we can estimate U(T-dT,X) as
#
#      U(T-dT,X) = U(T+dT,X) - 2 * dT * dU/dT(T,X)
#
#    If we replace the "missing" value of U(T-dT,X) by the known values
#    on the right hand side, we now have U(T+dT,X) on both sides of the
#    equation, so we have to rearrange to get the formula we use
#    for just the first time step:
#
#      U(T+dT,X) =   1/2 * (     C^2 * dT^2 / dX^2 ) * U(T,   X+dX)
#                  +       ( 1 - C^2 * dT^2 / dX^2 ) * U(T,   X   )
#                  + 1/2 * (     C^2 * dT^2 / dX^2 ) * U(T,   X-dX)
#                  +  dT *                         dU/dT(T,   X   )
#
#    (Equation to advance from time T to time T+dT for FIRST step.)
#
#    It should be clear now that the quantity ALPHA = C * DT / DX will affect
#    the stability of the calculation.  If it is greater than 1, then
#    the middle coefficient 1-C^2 DT^2 / DX^2 is negative, and the
#    sum of the magnitudes of the three coefficients becomes unbounded.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Input:
#
#    integer X_NUM, the number of intervals in the X direction.
#    The number of nodes is X_NUM + 1.
#
#    real X1, X2, the first and last X coordinates.
#
#    integer T_NUM, the number of time steps.  The total number
#    of times at which a solution is known is T_NUM + 1.
#
#    real T1, T2, the first and last T coordinates.
#
#    real C, a parameter which gives the speed of waves.
#
#  Output:
#
#    real U(T_NUM+1,X_NUM+1), the solution of the discretized 
#    wave equation for the discrete set of positions and times.
#
  import numpy as np

  t_delta = ( t2 - t1 ) / t_num
  x_delta = ( x2 - x1 ) / x_num
  alpha = c * t_delta / x_delta

  print ( '' )
  print ( '  Stability condition ALPHA = C * DT / DX = ', alpha )

  if ( 1.0 < np.abs ( alpha ) ):
    print ( '' )
    print ( 'fd1d_wave(): Warning!' )
    print ( '  The stability condition |ALPHA| <= 1 fails.' )
    print ( '  Computed results are liable to be inaccurate.' )

  u = np.zeros ( t_num + 1, x_num + 1 )
#
#  The boundary conditions.
#
  u[:,0]     = u_x1 ( t_num )
  u[:,x_num] = u_x2 ( t_num )
#
#  The initial data.
#
  u[0,:]       = u_t1 ( x_num )
  ut[0,:]      = ut_t1 ( x_num )
#
#  For the first step in time, we cannot refer to two previous
#  spatial rows of solution data.  Instead, we must use the
#  initial derivative information.
#
  t = 0
  for x in range ( 1, x_num ):
    u[t+1,x] =       alpha**2   * u[t,x+1] / 2 \
           + ( 1.0 - alpha**2 ) * u[t,x] \
           +         alpha**2   * u[t,x-1] / 2 \
           +         t_delta    * ut[t,x]
#
#  All subsequent steps in time rely on two previous rows of solution data.
#
  for t in range ( 1, t_num ):
    for x in range ( 1, x_num ):

      u[t+1,x] =               alpha**2   * u[t,  x+1] \
               + 2.0 * ( 1.0 - alpha**2 ) * u[t,  x  ] \
               +               alpha**2   * u[t,  x-1] \
               -                            u[t-1,x  ]

  return u

def fd1d_wave_start ( x_num, x_vec, t, t_delta, alpha, u_x1, u_x2, ut_t1, u1 ):

#*****************************************************************************80
#
## fd1d_wave_start() takes the first step for the wave equation.
#
#  Discussion:
#
#    This program solves the 1D wave equation of the form:
#
#      Utt = c^2 Uxx
#
#    over the spatial interval [X1,X2] and time interval [T1,T2],
#    with initial conditions:
#
#      U(T1,X)  = U_T1(X),
#      Ut(T1,X) = UT_T1(X),
#
#    and boundary conditions of Dirichlet type:
#
#      U(T,X1) = U_X1(T),
#      U(T,X2) = U_X2(T).
#
#    The value C represents the propagation speed of waves.
#
#    The program uses the finite difference method, and marches
#    forward in time, solving for all the values of U at the next
#    time step by using the values known at the previous two time steps.
#
#    Central differences may be used to approximate both the time
#    and space derivatives in the original differential equation.
#
#    Thus, assuming we have available the approximated values of U
#    at the current and previous times, we may write a discretized
#    version of the wave equation as follows:
#
#      Uxx(T,X) = ( U(T,   X+dX) - 2 U(T,X) + U(T,   X-dX) ) / dX^2
#      Utt(T,X) = ( U(T+dt,X   ) - 2 U(T,X) + U(T-dt,X   ) ) / dT^2
#
#    If we multiply the first term by C^2 and solve for the single
#    unknown value U(T+dt,X), we have:
#
#      U(T+dT,X) =        (     C^2 * dT^2 / dX^2 ) * U(T,   X+dX)
#                  +  2 * ( 1 - C^2 * dT^2 / dX^2 ) * U(T,   X   )
#                  +      (     C^2 * dT^2 / dX^2 ) * U(T,   X-dX)
#                  -                                  U(T-dT,X   )
#
#    (Equation to advance from time T to time T+dT, except for FIRST step!)
#
#    However, on the very first step, we only have the values of U
#    for the initial time, but not for the previous time step.
#    In that case, we use the initial condition information for dUdT
#    which can be approximated by a central difference that involves
#    U(T+dT,X) and U(T-dT,X):
#
#      dU/dT(T,X) = ( U(T+dT,X) - U(T-dT,X) ) / ( 2 * dT )
#
#    and so we can estimate U(T-dT,X) as
#
#      U(T-dT,X) = U(T+dT,X) - 2 * dT * dU/dT(T,X)
#
#    If we replace the "missing" value of U(T-dT,X) by the known values
#    on the right hand side, we now have U(T+dT,X) on both sides of the
#    equation, so we have to rearrange to get the formula we use
#    for just the first time step:
#
#      U(T+dT,X) =   1/2 * (     C^2 * dT^2 / dX^2 ) * U(T,   X+dX)
#                  +       ( 1 - C^2 * dT^2 / dX^2 ) * U(T,   X   )
#                  + 1/2 * (     C^2 * dT^2 / dX^2 ) * U(T,   X-dX)
#                  +  dT *                         dU/dT(T,   X   )
#
#    (Equation to advance from time T to time T+dT for FIRST step.)
#
#    It should be clear now that the quantity ALPHA = C * DT / DX will affect
#    the stability of the calculation.  If it is greater than 1, then
#    the middle coefficient 1-C^2 DT^2 / DX^2 is negative, and the
#    sum of the magnitudes of the three coefficients becomes unbounded.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Input:
#
#    integer X_NUM, the number of nodes in the X direction.
#
#    real X_VEC(X_NUM), the spatial coordinates of the nodes.
#
#    real T, the time after the first step has been taken.
#    In other words, T = T1 + T_DELTA.
#
#    real T_DELTA, the time step.
#
#    real ALPHA, the stability coefficient, computed by FD1D_WAVE_ALPHA.
#
#    real U_X1(T), U_X2(T), functions for the left and right boundary 
#    conditions.
#
#    real UT_T1(X), the function that evaluates dUdT at the initial time.
#
#    real U1(X_NUM), the initial condition.
#
#  Output:
#
#    real U2(X_NUM), the solution at the first time step.
#
  import numpy as np

  ut = ut_t1 ( x_num, x_vec )

  u2 = np.zeros ( x_num )

  u2[0] = u_x1 ( t )
  u2[1:x_num-1] =         alpha**2   * u1[2:x_num] / 2 \
                  + ( 1 - alpha**2 ) * u1[1:x_num-1] \
                  +       alpha**2   * u1[0:x_num-2] / 2 \
                  +        t_delta   * ut[1:x_num-1]
  u2[x_num-1] = u_x2 ( t )

  return u2

def fd1d_wave_step ( x_num, t, alpha, u_x1, u_x2, u1, u2 ):

#*****************************************************************************80
#
## fd1d_wave_step() computes a step of the 1D wave equation.
#
#  Discussion:
#
#    This program solves the 1D wave equation of the form:
#
#      Utt = c^2 Uxx
#
#    over the spatial interval [X1,X2] and time interval [T1,T2],
#    with initial conditions:
#
#      U(T1,X)  = U_T1(X),
#      Ut(T1,X) = UT_T1(X),
#
#    and boundary conditions of Dirichlet type:
#
#      U(T,X1) = U_X1(T),
#      U(T,X2) = U_X2(T).
#
#    The value C represents the propagation speed of waves.
#
#    The program uses the finite difference method, and marches
#    forward in time, solving for all the values of U at the next
#    time step by using the values known at the previous two time steps.
#
#    Central differences may be used to approximate both the time
#    and space derivatives in the original differential equation.
#
#    Thus, assuming we have available the approximated values of U
#    at the current and previous times, we may write a discretized
#    version of the wave equation as follows:
#
#      Uxx(T,X) = ( U(T,   X+dX) - 2 U(T,X) + U(T,   X-dX) ) / dX^2
#      Utt(T,X) = ( U(T+dt,X   ) - 2 U(T,X) + U(T-dt,X   ) ) / dT^2
#
#    If we multiply the first term by C^2 and solve for the single
#    unknown value U(T+dt,X), we have:
#
#      U(T+dT,X) =        (     C^2 * dT^2 / dX^2 ) * U(T,   X+dX)
#                  +  2 * ( 1 - C^2 * dT^2 / dX^2 ) * U(T,   X   )
#                  +      (     C^2 * dT^2 / dX^2 ) * U(T,   X-dX)
#                  -                                  U(T-dT,X   )
#
#    (Equation to advance from time T to time T+dT, except for FIRST step!)
#
#    However, on the very first step, we only have the values of U
#    for the initial time, but not for the previous time step.
#    In that case, we use the initial condition information for dUdT
#    which can be approximated by a central difference that involves
#    U(T+dT,X) and U(T-dT,X):
#
#      dU/dT(T,X) = ( U(T+dT,X) - U(T-dT,X) ) / ( 2 * dT )
#
#    and so we can estimate U(T-dT,X) as
#
#      U(T-dT,X) = U(T+dT,X) - 2 * dT * dU/dT(T,X)
#
#    If we replace the "missing" value of U(T-dT,X) by the known values
#    on the right hand side, we now have U(T+dT,X) on both sides of the
#    equation, so we have to rearrange to get the formula we use
#    for just the first time step:
#
#      U(T+dT,X) =   1/2 * (     C^2 * dT^2 / dX^2 ) * U(T,   X+dX)
#                  +       ( 1 - C^2 * dT^2 / dX^2 ) * U(T,   X   )
#                  + 1/2 * (     C^2 * dT^2 / dX^2 ) * U(T,   X-dX)
#                  +  dT *                         dU/dT(T,   X   )
#
#    (Equation to advance from time T to time T+dT for FIRST step.)
#
#    It should be clear now that the quantity ALPHA = C * DT / DX will affect
#    the stability of the calculation.  If it is greater than 1, then
#    the middle coefficient 1-C^2 DT^2 / DX^2 is negative, and the
#    sum of the magnitudes of the three coefficients becomes unbounded.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Input:
#
#    integer X_NUM, the number of nodes in the X direction.
#
#    real T, the new time, that is, the current time + T_DELTA.
#
#    real ALPHA, the stability coefficient, computed by FD1D_WAVE_ALPHA.
#
#    real U_X1(T), U_X2(T), functions for the left and right boundary 
#    conditions.
#
#    real U1(X_NUM), the solution at the old time.
#
#    real U2(X_NUM), the solution at the current time.
#
#  Output:
#
#    real U3(X_NUM), the solution at the new time.
#
  import numpy as np

  u3 = np.zeros ( x_num )

  u3[0]         = u_x1 ( t )
  u3[1:x_num-1] =             alpha**2   * u2[2:x_num] \
                  + 2 * ( 1 - alpha**2 ) * u2[1:x_num-1] \
                  +           alpha**2   * u2[0:x_num-2] \
                  -                        u1[1:x_num-1]
  u3[x_num-1]     = u_x2 ( t )

  return u3

def fd1d_wave_test01 ( ):

#*****************************************************************************80
#
## fd1d_wave_test01() tests the FD1D finite difference wave computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np

  x_num = 16
  x1 = 0.0
  x2 = 1.5
  x_vec = np.linspace ( x1, x2, x_num )

  t_num = 41
  t1 = 0.0
  t2 = 4.0
  t_vec = np.linspace ( t1, t2, t_num )
  t_delta = ( t2 - t1 ) / ( t_num - 1 )

  c = 1.0
  alpha = fd1d_wave_alpha ( x_num, x1, x2, t_num, t1, t2, c )

  u = np.zeros ( [ t_num, x_num ] )
#
#  Load the initial condition.
#
  u1 = u_t1_01 ( x_num, x_vec )
  u[0,:] = u1.copy()
#
#  Take the first step.
#
  t = t_vec[1]
  u2 = fd1d_wave_start ( x_num, x_vec, t, t_delta, alpha, u_x1_01, \
    u_x2_01, ut_t1_01, u1 )
  u[1,:] = u2.copy()
#
#  Take all the other steps.
#
  for i in range ( 2, t_num ):
    t = t_vec[i]
    u3 = fd1d_wave_step ( x_num, t, alpha, u_x1_01, u_x2_01, u1, u2 )
    u[i,:] = u3.copy()
    u1 = u2.copy()
    u2 = u3.copy()

  u_min = np.min ( np.min ( u ) )
  u_max = np.max ( np.max ( u ) )
#
#  Plot the solution as it evolves in time.
#
  for i in range ( 0, t_num ):
    t = t_vec[i]
    plt.clf ( )
    plt.plot ( x_vec, u[i,:], 'b-' )
    plt.grid ( True )
    plt.axis ( [ x1, x2, u_min-1.0, u_max+1.0 ] )
    s = ( 'Step %d Time %f' % ( i, t ) )
    plt.title ( s )
    plt.xlabel ( '<-- X -->' )
    plt.ylabel ( 'Vertical displacement' )
    plt.show ( block = False )
    plt.close ( )
#
#  Plot the entire solution as a surface.
#    
  T, X = np.meshgrid ( t_vec, x_vec )
  T = np.transpose ( T )
  X = np.transpose ( X )

  fig = plt.figure ( )
  plt.clf ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( T, X, u, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Wave test01_plot', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  filename = 'test01_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Write the solution to a file.
#
  filename = 'test01_plot.txt'
  np.savetxt ( filename, u )
  print ( '  Solution data saved as "' + filename + '"' )

  return

def u_x1_01 ( t ):

#*****************************************************************************80
#
## u_x1_01() evaluates U at the boundary X1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the time.
#
#  Output:
#
#    real U, the value of U(T,X1).
#
  if ( t == 0.10 ):
    u = 2.0
  elif ( t == 0.20 ):
    u = 10.0
  elif ( t == 0.30 ):
    u = 8.0
  elif ( t == 0.40 ):
    u = 5.0
  else:
    u = 0.0

  return u

def u_x2_01 ( t ):

#*****************************************************************************80
#
## u_x2_01() evaluates U at the boundary X2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the time.
#
#  Output:
#
#    real U, the value of U(T,X2).
#
  u = 0.0

  return u

def u_t1_01 ( x_num, x_vec ):

#*****************************************************************************80
#
## u_t1_01() evaluates U at the initial time T1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of nodes.
#
#    real X_VEC(X_NUM), the coordinates of the nodes.
#
#  Output:
#
#    real U(X_NUM), the value of U at the initial time,
#    and every node.
#
  import numpy as np

  u = np.zeros ( x_num )

  return u

def ut_t1_01 ( x_num, x_vec ):

#*****************************************************************************80
#
## ut_t1_01() evaluates dUdT at the initial time T1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of nodes.
#
#    real X_VEC(X_NUM), the coordinates of the nodes.
#
#  Output:
#
#    real UT(X_NUM), the value of dU/dt at the initial time,
#    and every node.
#
  import numpy as np

  ut = np.zeros ( x_num )

  return ut
 
def fd1d_wave_test02 ( ):

#*****************************************************************************80
#
## fd1d_wave_test02() tests the FD1D finite difference wave computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np

  x_num = 16
  x1 = 0.0
  x2 = 1.5
  x_vec = np.linspace ( x1, x2, x_num )

  t_num = 41
  t1 = 0.0
  t2 = 4.0
  t_vec = np.linspace ( t1, t2, t_num )
  t_delta = ( t2 - t1 ) / ( t_num - 1 )

  c = 1.0
  alpha = fd1d_wave_alpha ( x_num, x1, x2, t_num, t1, t2, c )

  u = np.zeros ( [ t_num, x_num ] )
#
#  Load the initial condition.
#
  u1 = u_t1_02 ( x_num, x_vec )
  u[0,:] = u1.copy()
#
#  Take the first step.
#
  t = t_vec[1]
  u2 = fd1d_wave_start ( x_num, x_vec, t, t_delta, alpha, u_x1_02, u_x2_02, \
    ut_t1_02, u1 )
  u[1,:] = u2.copy()
#
#  Take all the other steps.
#
  for i in range ( 2, t_num ):
    t = t_vec[i]
    u3 = fd1d_wave_step ( x_num, t, alpha, u_x1_02, u_x2_02, u1, u2 )
    u[i,:] = u3.copy()
    u1 = u2.copy()
    u2 = u3.copy()

  u_min = np.min ( np.min ( u ) )
  u_max = np.max ( np.max ( u ) )
#
#  Plot the solution as it evolves in time.
#
  for i in range ( 0, t_num ):
    t = t_vec[i]
    plt.clf ( )
    plt.plot ( x_vec, u[i,:], 'b-' )
    plt.grid ( True )
    plt.axis ( [ x1, x2, u_min-1.0, u_max+1.0 ] )
    s = ( 'Step %d Time %f' % ( i, t ) )
    plt.title ( s )
    plt.xlabel ( '<-- X -->' )
    plt.ylabel ( 'Vertical displacement' )
    plt.show ( block = False )
    plt.close ( )
#
#  Plot the entire solution as a surface.
#    
  T, X = np.meshgrid ( t_vec, x_vec )
  T = np.transpose ( T )
  X = np.transpose ( X )

  fig = plt.figure ( )
  plt.clf ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( T, X, u, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Wave test01_plot', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  filename = 'test02_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Write the solution to a file.
#
  filename = 'test02_plot.txt'
  np.savetxt ( filename, u )
  print ( '  Solution data saved as "' + filename + '"' )

  return

def u_x1_02 ( t ):

#*****************************************************************************80
#
## u_x1_02() evaluates U at the boundary X1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the time.
#
#  Output:
#
#    real U, the value of U(T,X1).
#
  u = 0.0

  return u

def u_x2_02 ( t ):

#*****************************************************************************80
#
## u_x2_02() evaluates U at the boundary X2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the time.
#
#  Output:
#
#    real U, the value of U(T,X2).
#
  u = 0.0

  return u

def u_t1_02 ( x_num, x_vec ):

#*****************************************************************************80
#
## u_t1_02() evaluates U at the initial time T1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of nodes.
#
#    real X_VEC(X_NUM), the spatial node coordinates.
#
#  Output:
#
#    real U(X_NUM), the value of U at the initial time,
#    and every node.
#
  import numpy as np

  u = np.sin ( 2.0 * np.pi * x_vec )

  return u

def ut_t1_02 ( x_num, x_vec ):

#*****************************************************************************80
#
## ut_t1_02() evaluates dUdT at the initial time T1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of nodes.
#
#    real X_VEC(X_NUM), the spatial node coordinates.
#
#  Output:
#
#    real UT(X_NUM), the value of dU/dt at the initial time,
#    and every node.
#
  import numpy as np

  ut = np.zeros ( x_num )

  return ut

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
  fd1d_wave_test ( )
  timestamp ( )

