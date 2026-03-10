#! /usr/bin/env python3
#
def gnuplot_test ( ):

#*****************************************************************************80
#
## gnuplot_test() tests gnuplot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gnuplot_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gnuplot().' )

  damped_sine ( )
  mark_points ( )
  orbital_fill_contour ( )
  string_simulation ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gnuplot_test():' )
  print ( '  Normal end of execution.' )

  return

def damped_sine ( ):

#*****************************************************************************80
#
## damped_sine() evaluates and plots the damped sine correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 101

  print ( '' )
  print ( 'damped_sine():' )
  print ( '  Demonstrating how a correlation function can be' )
  print ( '  evaluated and plotted using gnuplot().' )
#
#  damped_sine
#
  rho0 = 1.0
  rho = np.linspace ( -12.0, +12.0, n )
  c = np.ones ( n )
  i = np.where ( rho != 0.0 )
  c[i] = rho0 * np.sin ( np.abs ( rho[i] ) / rho0 ) / np.abs ( rho[i] )

  correlation_plot ( n, rho, c, 'damped_sine', 'Damped sine correlation' )

  return

def correlation_plot ( n, rho, c, header, title ):

#*****************************************************************************80
#
## correlation_plot() makes a plot of a correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real C(N), the correlations.
#
#    string HEADER, an identifier for the files.
#
#    string TITLE, a title for the plot.
#
  data_filename = header + '_data.txt'
  data_unit = open ( data_filename, 'wt' )
  for i in range ( 0, n ):
    s = ( '  %14.6g  %14.6g\n' % ( rho[i], c[i] ) )
    data_unit.write ( s )
  data_unit.close ( )
  print ( '  Created data file "' + data_filename + '"' )

  command_filename = header + '_commands.txt'
  command_unit = open ( command_filename, 'wt' )
  command_unit.write ( '# ' + command_filename + '\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '# Usage:\n' )
  command_unit.write ( '#  gnuplot < ' + command_filename + '\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "' + header + '.png"\n' )
  command_unit.write ( 'set xlabel "Distance Rho"\n' )
  command_unit.write ( 'set ylabel "Correlation C(Rho)"\n' )
  command_unit.write ( 'set title "' + title + '"\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set style data lines\n' )
  command_unit.write ( 'plot "' + data_filename + \
    '" using 1:2 lw 3 linecolor rgb "blue"\n' )
  command_unit.write ( 'quit\n' )
  command_unit.close ( )
  print ( '  Created command file "' + command_filename + '"' )

  return





def mark_points ( ):

#*****************************************************************************80
#
## mark_points() shows how to add marked points to a plot.
#
#  Discussion:
#
#    You can't add more items to a gnuplot() plot once it's created, 
#    so if you want to plot some points, and then include some markers,
#    then you have to create some auxilliary data files identifying those
#    marked points, and refer to them in an extra-long single plot() command.
#   
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 101

  print ( '' )
  print ( 'mark_points():' )
  print ( '  Plot a damped sine function over a range.' )
  print ( '  Mark the first data point green, and the last one red..' )

  rho0 = 1.0
  rho = np.linspace ( -12.0, +12.0, n )
  c = np.ones ( n )
  i = np.where ( rho != 0.0 )
  c[i] = rho0 * np.sin ( np.abs ( rho[i] ) / rho0 ) / np.abs ( rho[i] )

  mark_points_plot ( n, rho, c, 'mark_points', 'Marking points in gnuplot' )

  return

def mark_points_plot ( n, rho, c, header, title ):

#*****************************************************************************80
#
## mark_points_plot() adds two marked points to a plot.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real C(N), the correlations.
#
#    string HEADER, an identifier for the files.
#
#    string TITLE, a title for the plot.
#

#
#  Create the main data file.
#
  data_filename = header + '_data.txt'
  data_unit = open ( data_filename, 'wt' )
  for i in range ( 0, n ):
    s = ( '  %14.6g  %14.6g\n' % ( rho[i], c[i] ) )
    data_unit.write ( s )
  data_unit.close ( )
  print ( '  Created data file "' + data_filename + '"' )
#
#  Create a data file for the green point.
#
  start_data_filename = header + '_start_data.txt'
  data_unit = open ( start_data_filename, 'wt' )
  s = ( '  %14.6g  %14.6g\n' % ( rho[0], c[0] ) )
  data_unit.write ( s )
  data_unit.close ( )
  print ( '  Created data file "' + start_data_filename + '"' )
#
#  Create a data file for the red point.
#
  end_data_filename = header + '_end_data.txt'
  data_unit = open ( end_data_filename, 'wt' )
  s = ( '  %14.6g  %14.6g\n' % ( rho[n-1], c[n-1] ) )
  data_unit.write ( s )
  data_unit.close ( )
  print ( '  Created data file "' + end_data_filename + '"' )
#
#  Create the command file.
#
  command_filename = header + '_commands.txt'
  command_unit = open ( command_filename, 'wt' )
  command_unit.write ( '# ' + command_filename + '\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '# Usage:\n' )
  command_unit.write ( '#  gnuplot < ' + command_filename + '\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "' + header + '.png"\n' )
  command_unit.write ( 'set xlabel "Distance Rho"\n' )
  command_unit.write ( 'set ylabel "Correlation C(Rho)"\n' )
  command_unit.write ( 'set title "' + title + '"\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set style data lines\n' )
  command_unit.write ( 'plot "' + data_filename + \
    '" using 1:2 lw 3 linecolor rgb "blue", \\\n' )
  command_unit.write ( '     "' + start_data_filename + \
    '" using 1:2 with points pointtype 7 pointsize 3 linecolor rgb "green", \\\n' )
  command_unit.write ( '     "' + end_data_filename + \
    '" using 1:2 with points pointtype 7 pointsize 3 linecolor rgb "red"\n' )
  command_unit.write ( 'quit\n' )
  command_unit.close ( )
  print ( '  Created command file "' + command_filename + '"' )

  return


def orbital_fill_contour ( ):

#*****************************************************************************80
#
## orbital_fill_contour() creates a color contour plot of orbital data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'orbital_fill_contour():' )
  print ( '  Color contour plot of orbital data using gnuplot().' )

  command_filename = 'orbital_fill_contour_commands.txt'
  command_unit = open ( command_filename, 'wt' )
  command_unit.write ( '# orbital_fill_contour_commands.txt\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '# Usage:\n' )
  command_unit.write ( '#  gnuplot < orbital_fill_contour_commands.txt\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "orbital_fill_contour.png"\n' )
  command_unit.write ( 'set xlabel "<--- X --->"\n' )
  command_unit.write ( 'set ylabel "<--- Y --->"\n' )
  command_unit.write ( 'set title "Orbital Data"\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'unset surface\n' )
  command_unit.write ( 'set contour base\n' )
  command_unit.write ( 'set view map\n' )
  command_unit.write ( 'set pm3d\n' )
  command_unit.write ( 'splot "orbital_gnuplot_data.txt" with pm3d\n' )
  command_unit.write ( 'quit\n' )
  command_unit.close ( )
  print ( '  Created command file "orbital_fill_contour_commands.txt"' )

  return

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
  u = np.zeros ( [ m + 1, n + 1 ] )

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
      s = ( '%10.4f  %10.4f  %10.4f\n' % ( x, t, u[i,j] ) )
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

  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "string_simulation.png"\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set style data lines\n' )
  command_unit.write ( 'unset key\n' )
  command_unit.write ( 'set xlabel "<---X--->"\n' )
  command_unit.write ( 'set ylabel "<---Time--->"\n' )
  command_unit.write ( 'splot "' + data_filename + '" using 1:2:3 with lines\n' )
  command_unit.write ( 'quit\n' )

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

def g ( x ):

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
  gnuplot_test ( )
  timestamp ( )

