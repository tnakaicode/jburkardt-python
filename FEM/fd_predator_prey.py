#! /usr/bin/env python3
#
def fd_predator_prey_test ( ):

#*****************************************************************************80
#
## FD_PREDATOR_PREY_TEST tests FD_PREDATOR_PREY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'FD_PREDATOR_PREY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
#
#  Set parameters.
#
  p0 = np.array ( [ 5000, 100 ] )
  tspan = np.array ( [ 0.0, 5.0 ] )
  step_num = 1000
#
#  Report parameters:
#
  print ( '' )
  print ( '  Initial number of prey is %d' % ( p0[0] ) )
  print ( '  Initial number of predators is %d' % ( p0[1] ) )
  print ( '  Time span is [%g,%g]' % ( tspan[0], tspan[1] ) )
  print ( '  Number of time steps will be %d' % ( step_num ) )
#
#  Compute table of T, Prey(T), Pred(T).
#
  trf = fd_predator_prey ( p0, tspan, step_num )
#
#  Make some plots.
#
  time_plot ( step_num, trf )
  phase_plot ( step_num, trf )
#
#  Write data to files.
#
  filename = 'trf_%d.txt' % ( step_num )
  r8mat_write ( filename, 3, step_num + 1, trf )
  print ( '  T, R, F values written to "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FD_PREDATOR_PREY' )
  print ( '  Normal end of execution.' )

def fd_predator_prey ( p0, tspan, step_num ):

#*****************************************************************************80
#
## FD_PREDATOR_PREY solves a pair of predator-prey ODE's.
#
#  Discussion:
#
#    The physical system under consideration is a pair of animal populations.
#
#    The PREY reproduce rapidly for each animal alive at the beginning of the
#    year, two more will be born by the end of the year.  The prey do not have
#    a natural death rate instead, they only die by being eaten by the predator.
#    Every prey animal has 1 chance in 1000 of being eaten in a given year by
#    a given predator.
#
#    The PREDATORS only die of starvation, but this happens very quickly.
#    If unfed, a predator will tend to starve in about 1/10 of a year.
#    On the other hand, the predator reproduction rate is dependent on
#    eating prey, and the chances of this depend on the number of available prey.
#
#    The resulting differential equations can be written:
#
#      PREY(0) = 5000
#      PRED(0) =  100
#
#      d PREY / dT =    2 * PREY(T) - 0.001 * PREY(T) * PRED(T)
#      d PRED / dT = - 10 * PRED(T) + 0.002 * PREY(T) * PRED(T)
#
#    Here, the initial values (5000,100) are a somewhat arbitrary starting point.
#
#    The pair of ordinary differential equations that result have an interesting
#    behavior.  For certain choices of the interaction coefficients (such as
#    those given here), the populations of predator and prey will tend to
#    a periodic oscillation.  The two populations will be out of phase the number
#    of prey will rise, then after a delay, the predators will rise as the prey
#    begins to fall, causing the predator population to crash again.
#
#    In this program, the pair of ODE's is solved with a simple finite difference
#    approximation using a fixed step size.  In general, this is NOT an efficient
#    or reliable way of solving differential equations.  However, this program is
#    intended to illustrate the ideas of finite difference approximation.
#
#    In particular, if we choose a fixed time step size DT, then a derivative
#    such as dPREY/dT is approximated by:
#
#      d PREY / dT = approximately ( PREY(T+DT) - PREY(T) ) / DT
#
#    which means that the first differential equation can be written as
#
#      PREY(T+DT) = PREY(T) + DT * ( 2 * PREY(T) - 0.001 * PREY(T) * PRED(T) ).
#
#    We can rewrite the equation for PRED as well.  Then, since we know the
#    values of PRED and PREY at time 0, we can use these finite difference
#    equations to estimate the values of PRED and PREY at time DT.  These values
#    can be used to get estimates at time 2*DT, and so on.  To get from time
#    T_START = 0 to time T_STOP = 5, we simply take STEP_NUM steps each of size
#    DT = ( T_STOP - T_START ) / STEP_NUM.
#
#    Because finite differences are only an approximation to derivatives, this
#    process only produces estimates of the solution.  And these estimates tend
#    to become more inaccurate for large values of time.  Usually, we can reduce
#    this error by decreasing DT and taking more, smaller time steps.
#
#    In this example, for instance, taking just 100 steps gives nonsensical
#    answers.  Using STEP_NUM = 1000 gives an approximate solution that seems
#    to have the right kind of oscillatory behavior, except that the amplitude
#    of the waves increases with each repetition.  Using 10000 steps, the
#    approximation begins to become accurate enough that we can see that the
#    waves seem to have a fixed period and amplitude.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2009
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
#  Parameters:
#
#    Input, real P0(2), the initial number of prey and predators.
#
#    Input, real TSPAN(2), the initial and final times.
#
#    Input, integer STEP_NUM, the number of time steps.
#
  import numpy as np

  print ( '' )
  print ( 'FD_PREDATOR_PREY' )
  print ( '' )
  print ( '  A finite difference approximate solution of a pair' )
  print ( '  of ordinary differential equations for a population' )
  print ( '  of predators and prey.' )
  print ( '' )
  print ( '  The exact solution shows wave behavior, with a fixed' )
  print ( '  period and amplitude.  The finite difference approximation' )
  print ( '  can provide a good estimate for this behavior if the stepsize' )
  print ( '  DT is small enough.' )

  t_start = tspan[0]
  t_stop =  tspan[1]
  dt = ( t_stop - t_start ) / step_num

  trf = np.zeros ( [ 3, step_num+1 ] )

  trf[0,0] = t_start
  trf[1,0] = p0[0]
  trf[2,0] = p0[1]

  for i in range ( 0, step_num ):
    trf[0,i+1] = trf[0,i] + dt
    trf[1,i+1] = trf[1,i] + dt * (    2 * trf[1,i] - 0.004 * trf[1,i] * trf[2,i] )
    trf[2,i+1] = trf[2,i] + dt * ( - 10 * trf[2,i] + 0.003 * trf[1,i] * trf[2,i] )

  return trf

def time_plot ( step_num, trf ):

#*****************************************************************************80
#
## TIME_PLOT plots (T,PREY(T)) and (T,PREDATOR(T)).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 August 2017
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
#  Parameters:
#
#    Input, integer STEP_NUM, the number of time steps.
#
#    Input, real TRF(3,STEP_NUM+1), the values of T, PREY and PREDATOR
#    at time steps 0 through STEP_NUM.
#
  import matplotlib.pyplot as plt

  plt.plot ( trf[0,:], trf[1,:], 'g-', linewidth = 3 )
  plt.plot ( trf[0,:], trf[2,:], 'r-', linewidth = 3 )
  plt.title ( 'Predator Prey System Solved by Finite Differences' )
  plt.grid ( True )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'Populations' )
  filename = 'trf_%d_time.png' % ( step_num )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def phase_plot ( step_num, trf ):

#*****************************************************************************80
#
## PHASE_PLOT plots (PREY(T),PREDATOR(T)).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 August 2017
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
#  Parameters:
#
#    Input, integer STEP_NUM, the number of time steps.
#
#    Input, real TRF(3,STEP_NUM+1), the values of T, PREY and PREDATOR
#    at time steps 0 through STEP_NUM.
#
  import matplotlib.pyplot as plt

  plt.plot ( trf[1,:], trf[2,:], 'b-', linewidth = 3 )
  plt.title ( 'Predator Prey System Solved by Finite Differences' )
  plt.grid ( True )
  plt.xlabel ( 'Rabbits' )
  plt.ylabel ( 'Foxes' )
  filename = 'trf_%d_phase.png' % ( step_num )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_WRITE writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_write_test ( ):

#*****************************************************************************80
#
## R8MAT_WRITE_TEST tests R8MAT_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8MAT_WRITE, which writes an R8MAT to a file.' )

  filename = 'r8mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  fd_predator_prey_test ( )
  timestamp ( )
