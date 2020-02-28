#! /usr/bin/env python3
#
def rk4 ( t0, u0, dt, f ):

#*****************************************************************************80
#
## RK4 takes one Runge-Kutta step.
#
#  Discussion:
#
#    It is assumed that an initial value problem, of the form
#
#      du/dt = f ( t, u )
#      u(t0) = u0
#
#    is being solved.
#
#    If the user can supply current values of t, u, a stepsize dt, and a
#    function to evaluate the derivative, this function can compute the
#    fourth-order Runge Kutta estimate to the solution at time t+dt.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T0, the current time.
#
#    Input, real U0, the solution estimate at the current time.
#
#    Input, real DT, the time step.
#
#    Input, function value = F ( T, U ), a function which evaluates
#    the derivative, or right hand side of the problem.
#
#    Output, real U1, the fourth-order Runge-Kutta solution estimate
#    at time T0+DT.
#

#
#  Get four sample values of the derivative.
#
  f1 = f ( t0,            u0 )
  f2 = f ( t0 + dt / 2.0, u0 + dt * f1 / 2.0 )
  f3 = f ( t0 + dt / 2.0, u0 + dt * f2 / 2.0 )
  f4 = f ( t0 + dt,       u0 + dt * f3 )
#
#  Combine them to estimate the solution U1 at time T1 = T0 + DT.
#
  u1 = u0 + dt * ( f1 + 2.0 * f2 + 2.0 * f3 + f4 ) / 6.0

  return u1

def rk4_test ( ):

#*****************************************************************************80
#
## RK4_TEST tests RK4 on a scalar ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'RK4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RK4 takes one Runge-Kutta step for a scalar ODE.' )

  print ( '' )
  print ( '          T          U(T)' )
  print ( '' )

  dt = 0.1
  t0 = 0.0
  tmax = 12.0 * np.pi
  u0 = 0.5

  t_num = int ( 2 + ( tmax - t0 ) / dt )

  t = np.zeros ( t_num )
  u = np.zeros ( t_num )

  i = 0
  t[0] = t0
  u[0] = u0

  while ( True ):
#
#  Print (T0,U0).
#
    print ( '  %4d  %14.6f  %14.6g' % ( i, t0, u0 ) )
#
#  Stop if we've exceeded TMAX.
#
    if ( tmax <= t0 ):
      break
#
#  Otherwise, advance to time T1, and have RK4 estimate 
#  the solution U1 there.
#
    t1 = t0 + dt
    u1 = rk4 ( t0, u0, dt, rk4_test_f )

    i = i + 1
    t[i] = t1
    u[i] = u1
#
#  Shift the data to prepare for another step.
#
    t0 = t1
    u0 = u1
#
#  Terminate.
#
  print ( '' )
  print ( 'Rk4_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rk4_test_f ( t, u ):

#*****************************************************************************80
#
## RK4_TEST_F evaluates the right hand side of a particular ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T, the current time.
#
#    Input, real U, the current solution value.
#
#    Output, real VALUE, the value of the derivative, dU/dT.
#  
  import numpy as np

  value = u * np.cos ( t )
  
  return value

def rk4vec ( t0, m, u0, dt, f ):

#*****************************************************************************80
#
## RK4VEC takes one Runge-Kutta step for a vector ODE.
#
#  Discussion:
#
#    Thanks  to Dante Bolatti for correcting the final function call to:
#      call f ( t1, m, u3, f3 )
#    18 August 2016.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T0, the current time.
#
#    Input, integer M, the spatial dimension.
#
#    Input, real U0(M), the solution estimate at the current time.
#
#    Input, real DT, the time step.
#
#    Input, function uprime = F ( t, m, u  ) 
#    which evaluates the derivative UPRIME(1:M) given the time T and
#    solution vector U(1:M).
#
#    Output, real U(M), the fourth-order Runge-Kutta solution 
#    estimate at time T0+DT.
#
  import numpy as np
#
#  Get four sample values of the derivative.
#
  f0 = f ( t0, m, u0 )

  t1 = t0 + dt / 2.0
  u1 = np.zeros ( m )
  u1[0:m] = u0[0:m] + dt * f0[0:m] / 2.0
  f1 = f ( t1, m, u1 )

  t2 = t0 + dt / 2.0
  u2 = np.zeros ( m )
  u2[0:m] = u0[0:m] + dt * f1[0:m] / 2.0
  f2 = f ( t2, m, u2 )

  t3 = t0 + dt
  u3 = np.zeros ( m )
  u3[0:m] = u0[0:m] + dt * f2[0:m]
  f3 = f ( t3, m, u3 )
#
#  Combine them to estimate the solution U at time T1.
#
  u = np.zeros ( m )
  u[0:m] = u0[0:m] + ( dt / 6.0 ) * ( \
            f0[0:m] \
    + 2.0 * f1[0:m] \
    + 2.0 * f2[0:m] \
    +       f3[0:m] )

  return u

def rk4vec_test ( ):

#*****************************************************************************80
#
## RK4VEC_TEST02 tests RK4VEC on a vector ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'RK4VEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RK4VEC takes one Runge-Kutta step for a vector ODE.' )

  n = 2
  dt = 0.1
  tmax = 12.0 * np.pi

  print ( '' )
  print ( '          T          U1(T)            U2(T)' )
  print ( '' )

  t0 = 0.0
  i = 0

  u0 = np.zeros ( 2 )
  u0[0] = 0.0
  u0[1] = 1.0

  while ( True ):
#
#  Print (T0,U0).
#
    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( i, t0, u0[0], u0[1] ) )
#
#  Stop if we've exceeded TMAX.
#
    if ( tmax <= t0 ):
      break

    i = i + 1
#
#  Otherwise, advance to time T1, and have RK4 estimate 
#  the solution U1 there.
#
    t1 = t0 + dt
    u1 = rk4vec ( t0, n, u0, dt, rk4vec_test_f )
#
#  Shift the data to prepare for another step.
#
    t0 = t1
    u0 = u1.copy ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RK4VEC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rk4vec_test_f ( t, n, u ):

#*****************************************************************************80
#
## RK4VEC_TEST_F evaluates the right hand side of a particular ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T, the current time.
#
#    Input, real U(N), the current solution value.
#
#    Output, real VALUE, the value of the derivative, dU/dT.
#  
  import numpy as np

  value = np.array ( [ u[1], - u[0] ] )
  
  return value

def rk4_tests ( ):

#*****************************************************************************80
#
## RK4_TESTS tests the RK4 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 August 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RK4_TESTS:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the RK4 library.' )

  from rk4 import rk4_test
  from rk4 import rk4vec_test

  rk4_test ( )
  rk4vec_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RK4_TESTS:' )
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
  rk4_tests ( )
  timestamp ( )

