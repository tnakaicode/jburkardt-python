def string_simulation ( ):

#*****************************************************************************80
#
## string_simulation() simulates the behavior of a string.
#
#  Discussion:
#
#    This program solves the 1D wave equation of the form:
#
#      Utt = c^2 Uxx
#
#    over the spatial interval (X1,X2) and time interval (T1,T2),
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
#    (Equation to advance from time T to time T+dT, except for FIRST step)
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
#    05 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    real ALPHA, the CFL stability parameter.
#
#    real C, the wave speed.
#
#    real DT, the time step.
#
#    real DX, the spatial step.
#
#    integer M, the number of time steps.
#
#    integer N, the number of spatial intervals.
#
#    real T1, T2, the initial and final times.
#
#    real U(M+1,N+1), the computed solution.
#
#    real X1, X2, the left and right spatial endpoints.
#
  import numpy as np

  m = 30
  n = 40
  c = 0.25
  t1 = 0.0
  t2 = 3.0
  x1 = 0.0
  x2 = 1.0

  print ( '' )
  print ( 'string_simulation():' )
  print ( '  Simulate the behavior of a vibrating string.' )

  dx = ( x2 - x1 ) / n
  dt = ( t2 - t1 ) / m
  alpha = ( c * dt / dx ) ** 2
  print ( '  ALPHA = ( C * dT / dX )^2 = ', alpha )
#
#  Warn the user if ALPHA will cause an unstable computation.
#
  if ( 1.0 < alpha ):
    print ( '' )
    print ( '  Warning!' )
    print ( '  ALPHA is greater than 1.' )
    print ( '  The computation is unstable.' )
#
#  Time step 0: 
#  Use the initial condition for U.
#
  u = np.zeros ( m + 1, n + 1 )

  u[0,0] = 0.0
  for i in range ( 1, n ):
    x = i * dx
    u[0,i] = f ( x )
  u[0,n] = 0.0
#
#  Time step 1:
#  Use the initial condition for dUdT.
#
  u[1,0] = 0.0
  for i in range ( 1, n ):
    x = i * dx
    u[1,i] = \
        ( alpha / 2.0 ) * u[0,i-1] \
      + ( 1.0 - alpha ) * u[0,i]   \
      + ( alpha / 2.0 ) * u[0,i+1] \
      + dt * g ( x )
  u[1,n] = 0.0
#
#  Time steps 2 through M:
#
  for j in range ( 2, m + 1 ):
    u[j,0] = 0.0
    for i in range ( 1, n ):
      u[j,i] = \
                        alpha   * u[j-1,i-1] \
        + 2.0 * ( 1.0 - alpha ) * u[j-1,i]   \
        +               alpha   * u[j-1,i+1] \
        -                         u[j-2,i]
    u[j,n] = 0.0
#
#  Write data file.
#
  data_filename = 'string_simulation_data.txt'
  data_unit = open ( data_filename, 'wt' )

  for i in range ( 0, m + 1 ):
    t = i * dt
    for j in range ( 0, n + 1 ):
      x = j * dx
      s = ( '%10.4f  %10.4f  %10.4f' % ( x, t, u[i,j] ) )
      fprintf ( data_unit,  )
      data_unit.write ( s )
    data_unit.write ( '\n' )
  data_unit.close ( )

  print ( '' )
  print ( '  Plot data written to the file "' + data_filename + '".' )
#
#  Write gnuplot command file.
#
  command_filename = 'string_simulation_commands.txt'
  command_unit = open ( command_filename, 'wt' )

  command_unit.write ( 'set term png' )
  command_unit.write ( 'set output "string_simulation.png"' )
  command_unit.write ( 'set grid' )
  command_unit.write ( 'set style data lines' )
  command_unit.write ( 'unset key' )
  command_unit.write ( 'set xlabel "<---X--->"' )
  command_unit.write ( 'set ylabel "<---Time--->"' )
  command_unit.write ( 'splot "' + data_filename + '" using 1:2:3 with lines' )
  command_unit.write ( 'quit' )

  command_unit.close ( )

  print ( '  gnuplot commands written to the "' + command_filename + '".' )

  return

def f ( x ):

#*****************************************************************************80
#
## f() supplies the initial condition.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the location.
#
#  Output:
#
#    real VALUE, the value of the solution at time 0 and location X.
#
  if ( 0.25 <= x and x <= 0.50 ):
    value = ( x - 0.25 ) * ( 0.50 - x )
  else:
    value = 0.0

  return value

def value = g ( x ):

#*****************************************************************************80
#
## g() supplies the initial derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the location.
#
#  Output:
#
#    real VALUE, the value of the time derivative of the solution 
#    at time 0 and location X.
#
  value = 0.0

  return value


