#! /usr/bin/env python3
#
def rkf45 ( f, neqn, y, yp, t, tout, relerr, abserr, flag ):

#*****************************************************************************80
#
## rkf45() carries out the Runge-Kutta-Fehlberg method.
#
#  Discussion:
#
#    This routine is primarily designed to solve non-stiff and mildly stiff
#    differential equations when derivative evaluations are inexpensive.
#    It should generally not be used when the user is demanding
#    high accuracy.
#
#    This function integrates a system of NEQN first-order ordinary differential
#    equations of the form:
#
#      dY(i)/dT = F(T,Y(1),Y(2), ...  ,Y(NEQN))
#
#    where the Y(1:NEQN) are given at T.
#    Typically the subroutine is used to integrate from T to TOUT but it
#    can be used as a one-step integrator to advance the solution a
#    single step in the direction of TOUT.  On return, the parameters in
#    the call list are set for continuing the integration.  The user has
#    only to call again (and perhaps define a new value for TOUT).
#
#    Before the first call, the user must
#
#    * supply the function  F(T,Y) to evaluate the right hand side YP;
#
#    * initialize the parameters:
#      NEQN, Y(1:NEQN), T, TOUT, RELERR, ABSERR, FLAG.
#      In particular, T should initially be the starting point for integration,
#      Y should be the value of the initial conditions, and FLAG should
#      normally be +1.
#
#    Normally, the user only sets the value of FLAG before the first call, and
#    thereafter, the program manages the value.  On the first call, FLAG should
#    normally be +1 (or -1 for single step mode.)  On normal return, FLAG will
#    have been reset by the program to the value of 2 (or -2 in single
#    step mode), and the user can continue to call the routine with that
#    value of FLAG.
#
#    (When the input magnitude of FLAG is 1, this indicates to the program
#    that it is necessary to do some initialization work.  An input magnitude
#    of 2 lets the program know that that initialization can be skipped,
#    and that useful information was computed earlier.)
#
#    The function returns with all the information needed to continue
#    the integration.  If the integration reached TOUT, the user need only
#    define a new TOUT and call again.  In the one-step integrator
#    mode, returning with FLAG = -2, the user must keep in mind that
#    each step taken is in the direction of the current TOUT.  Upon
#    reaching TOUT, indicated by the output value of FLAG switching to 2,
#    the user must define a new TOUT and reset FLAG to -2 to continue
#    in the one-step integrator mode.
#
#    In some cases, an error or difficulty occurs during a call.  In that case,
#    the output value of FLAG is used to indicate that there is a problem
#    that the user must address.  These values include:
#
#    * 3, integration was not completed because the input value of RELERR, the
#      relative error tolerance, was too small.  RELERR has been increased
#      appropriately for continuing.  If the user accepts the output value of
#      RELERR, then simply reset FLAG to 2 and continue.
#
#    * 4, integration was not completed because more than MAXNFE derivative
#      evaluations were needed.  This is approximately (MAXNFE/6) steps.
#      The user may continue by simply calling again.  The function counter
#      will be reset to 0, and another MAXNFE function evaluations are allowed.
#
#    * 5, integration was not completed because the solution vanished,
#      making a pure relative error test impossible.  The user must use
#      a non-zero ABSERR to continue.  Using the one-step integration mode
#      for one step is a good way to proceed.
#
#    * 6, integration was not completed because the requested accuracy
#      could not be achieved, even using the smallest allowable stepsize.
#      The user must increase the error tolerances ABSERR or RELERR before
#      continuing.  It is also necessary to reset FLAG to 2 (or -2 when
#      the one-step integration mode is being used).  The occurrence of
#      FLAG = 6 indicates a trouble spot.  The solution is changing
#      rapidly, or a singularity may be present.  It often is inadvisable
#      to continue.
#
#    * 7, it is likely that this routine is inefficient for solving
#      this problem.  Too much output is restricting the natural stepsize
#      choice.  The user should use the one-step integration mode with
#      the stepsize determined by the code.  If the user insists upon
#      continuing the integration, reset FLAG to 2 before calling
#      again.  Otherwise, execution will be terminated.
#
#    * 8, invalid input parameters, indicates one of the following:
#      NEQN <= 0;
#      T = TOUT and |FLAG| /= 1;
#      RELERR < 0 or ABSERR < 0;
#      FLAG == 0  or FLAG < -2 or 8 < FLAG.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2011
#
#  Author:
#
#    Original FORTRAN77 version by Herman Watts, Lawrence Shampine.
#    MATLAB version by John Burkardt.
#    This version by Peter Monk.
#
#  Reference:
#
#    Erwin Fehlberg,
#    Low-order Classical Runge-Kutta Formulas with Stepsize Control,
#    NASA Technical Report R-315, 1969.
#
#    Lawrence Shampine, Herman Watts, S Davenport,
#    Solving Non-stiff Ordinary Differential Equations - The State of the Art,
#    SIAM Review,
#    Volume 18, pages 376-411, 1976.
#
#  Input:
#
#    function F, a user-supplied function to evaluate the
#    derivatives dYdT(T), of the form:
#     def f ( t, y ):
#         <statements>
#         return(yp)
#
#    integer NEQN, the number of equations to be integrated.
#
#    real Y(NEQN), the current solution vector at T.
#
#    real YP(NEQN), the current value of the
#    derivative of the dependent variable.  The user should not set or alter
#    this information.
#
#    real T, the current value of the independent variable.
#
#    real TOUT, the output point at which solution is
#    desired.  TOUT = T is allowed on the first call only, in which case
#    the routine returns with FLAG = 2 if continuation is possible.
#
#    real RELERR, ABSERR, the relative and absolute
#    error tolerances for the local error test.  At each step the code
#    requires:
#      abs ( local error ) <= RELERR * abs ( Y ) + ABSERR
#    for each component of the local error and the solution vector Y.
#    RELERR cannot be "too small".  If the routine believes RELERR has been
#    set too small, it will reset RELERR to an acceptable value and return
#    immediately for user action.
#
#    integer FLAG, indicator for status of integration.
#    On the first call, set FLAG to +1 for normal use, or to -1 for single
#    step mode.
#
#  Output:
#
#    real Y(NEQN), the updated solution vector at T.
#
#    real YP(NEQN), the updated value of the
#    derivative of the dependent variable.  The user should not set or alter
#    this information.
#
#    real T, the updated value of the independent variable.
#
#    integer FLAG, a value of 2 or -2 indicates normal progress,
#    while any other value indicates a problem that should be addressed.
#
  import numpy as np

  global abserr_save, flag_save, h, init, kflag, kop, nfe, relerr_save

  try:
    abserr_save
  except NameError:
    abserr_save = -1.0
    h = -1.0
    flag_save = -1000
    init = -1000
    kflag = -1000
    kop = -1
    nfe = -1
    relerr_save = -1.0

  maxnfe = 3000000
  remin = 1.0E-12
#
#  Check the input parameters.
#
  if ( neqn < 1 ):
    flag = 8
    print ( 'neqn=' % ( neqn ) )
    return (y, yp, t, flag)

  if ( relerr < 0.0 ):
    flag = 8
    print ( 'relerr=' % ( relerr ) )
    return ( y, yp, t, flag )

  if ( abserr < 0.0 ):
    flag = 8
    print ( 'abserr=' % ( abserr ) )
    return ( y, yp, t, flag )

  if ( flag == 0) or (8 < flag) or ( flag < -2 ):
    flag = 8
    print ( 'flag=', flag )
    return ( y, yp, t, flag )
    
  mflag = np.abs ( flag )
#
#  Is this a continuation call?
#
  if ( mflag != 1 ):

    if ( t == tout) and ( kflag != 3 ):
      flag = 8
      print ( 't=',t,'tout=',tout,'kflag=',kflag )
      return ( y, yp, t, flag )

    if ( mflag == 2 ):
      if ( kflag == 3 ):
        flag = flag_save
        mflag = np.abs ( flag )
      elif ( init == 0 ):
        flag = flag_save
      elif ( kflag == 4 ):
        nfe = 0
      elif ( kflag == 5) and (abserr == 0.0 ):
        print ( '' )
        print ( 'rkf45 - Fatal error!' )
        print ( '  KFLAG = 5 and ABSERR = 0.' )
        raise Exception ( 'rkf45 - Fatal error!')
      elif ( kflag == 6) and (relerr <= relerr_save) and (abserr <= abserr_save ):          
        print ( '' )
        print ( 'rkf45 - Fatal error!' )
        print ( '  KFLAG = 6 and' )
        print ( '  RELERR <= RELERR_SAVE and' )
        print ( '  ABSERR <= ABSERR_SAVE' )
        raise Exception ( 'rkf45 - Fatal error!')
#
#  FLAG = 3, 4, 5, 6, 7 or 8.
#
    else:

      if ( flag == 3 ):
        flag = flag_save
        if ( kflag == 3 ):
          mflag = np.abs ( flag )
      elif ( flag == 4 ):
        nfe = 0
        flag = flag_save
        if ( kflag == 3 ):
          mflag = np.abs ( flag )
      elif ( flag == 5) and ( 0.0 < abserr ):
        flag = flag_save
        if ( kflag == 3 ):
          mflag = np.abs ( flag )
#
#  Integration cannot be continued because the user did not respond to
#  the instructions pertaining to FLAG = 5, 6, 7 or 8.
#
      else:
        print ( '' )
        print ( 'rkf45 - Fatal error!' )
        print ( '  Integration cannot continue because the user' )
        print ( '  did not respond to the instructions pertaining' )
        print ( '  to the output flag warning FLAG = 5, 6, 7 or 8.' )
        raise Exception ( 'rkf45 - Fatal error!') 
#
#  Save the input value of FLAG.
#  Set the continuation flag KFLAG for subsequent input checking.
#
  flag_save = flag
  kflag = 0
#
#  Save RELERR and ABSERR for checking input on subsequent calls.
#
  relerr_save = relerr
  abserr_save = abserr
#
#  Restrict the relative error tolerance to be at least
#
#    2 * EPS + REMIN
#
#  to avoid limiting precision difficulties arising from impossible
#  accuracy requests.
#
  relerr_min = 2.0 * np.finfo(np.double).eps + remin
#
#  Is the relative error tolerance too small?
#
  if ( relerr < relerr_min ):
    relerr = relerr_min
    flag = 3
    kflag = 3
    return ( y, yp, t, flag )

  dt = tout - t
#
#  Initialization:
#
#  Set the initialization completion indicator, INIT;
#  set the indicator for too many output points, KOP;
#  evaluate the initial derivatives;
#  set the counter for function evaluations, NFE;
#  estimate the starting stepsize.
#
  if ( mflag == 1 ):
    init = 0
    kop = 0
    yp = f ( t, y )
    nfe = 1
    if ( t == tout ):
      flag = 2
      return ( y, yp, t, flag )

  if ( init == 0 ):
    init = 1
    h = np.abs ( dt )
    toln = 0.0;
    for k in range ( 0, neqn ):
      tol = relerr * np.abs ( y[k] ) + abserr
      if ( 0.0 < tol ):
        toln = tol
        ypk = np.abs ( yp[k] )
        if ( tol < ypk * h**5 ):
          h = ( tol / ypk )**0.2
    if ( toln <= 0.0 ):
      h = 0.0

    h1 = np.maximum ( np.abs ( t ), np.abs ( dt ) )
    h2 = 26.0 * np.finfo(np.double).eps * h1
    h = np.maximum ( h, h2 )
    if ( flag < 0 ):
      flag_save = - 2
    else:
      flag_save = + 2
#
#  Set the stepsize for integration in the direction from T to TOUT.
#
  if ( dt < 0.0 ):
    h = - np.abs ( h )
  else:
    h = + np.abs ( h )
#
#  Test to see if too may output points are being requested.
#
  if ( 2.0 * np.abs ( dt ) <= np.abs ( h ) ):
    kop = kop + 1
#
#  Unnecessary frequency of output.
#
  if ( kop == 2000 ):
    kop = 0
    print ( 'Unnecessary frequency of output.' )
    flag = 7
    return ( y, yp, t, flag )
#
#  If we are too close to the output point, then simply extrapolate and return.
#
  if ( np.abs ( dt ) <= 26.0 * np.finfo(np.double).eps * np.abs ( t ) ):
    t = tout
    y = y + dt * yp
    yp = f ( t, y )
    nfe = nfe + 1
    flag = 2
    print ( 'too close' )
    return ( y, yp, t, flag )
#
#  Initialize the output point indicator.
#
  output = 0
#
#  To avoid premature underflow in the error tolerance function,
#  scale the error tolerances.
#
  scale = 2.0 / relerr
  ae = scale * abserr
#
#  Step by step integration.
#
  while ( True ):
      hfaild = 0
#
#  Set the smallest allowable stepsize.
#
      hmin = 26.0 * np.finfo(np.double).eps * np.abs ( t )
#
#  Adjust the stepsize if necessary to hit the output point.
#
#  Look ahead two steps to avoid drastic changes in the stepsize and
#  thus lessen the impact of output points on the code.
#
      dt = tout - t
      if ( 2.0 * np.abs ( h ) > np.abs ( dt ) ):
#
#  Will the next successful step complete the integration to the output point?
#
          if ( np.abs ( dt ) <= np.abs ( h ) ):
              output = 1
              h = dt
          else:
              h = 0.5 * dt
#
#  Here begins the core integrator for taking a single step.
#
#  The tolerances have been scaled to avoid premature underflow in
#  computing the error tolerance function ET.
#  To avoid problems with zero crossings, relative error is measured
#  using the average of the magnitudes of the solution at the
#  beginning and end of a step.
#  The error estimate formula has been grouped to control loss of
#  significance.
#
#  To distinguish the various arguments, H is not permitted
#  to become smaller than 26 units of roundoff in T.
#  Practical limits on the change in the stepsize are enforced to
#  smooth the stepsize selection process and to avoid excessive
#  chattering on problems having discontinuities.
#  To prevent unnecessary failures, the code uses 9/10 the stepsize
#  it estimates will succeed.
#
#  After a step failure, the stepsize is not allowed to increase for
#  the next attempted step.  This makes the code more efficient on
#  problems having discontinuities and more effective in general
#  since local extrapolation is being used and extra caution seems
#  warranted.
#
#  Test the number of derivative function evaluations.
#  If okay, try to advance the integration from T to T+H.
#
      while ( True ):
#
#  Have we done too much work?
#
          if ( maxnfe < nfe ):
              flag = 4
              kflag = 4
              return ( y, yp, t, flag )
#
#  Advance an approximate solution over one step of length H.
#
          f1, f2, f3, f4, f5, f6  = fehl ( f, neqn, y, t, h, yp )
          f1 = f6.copy()
          nfe = nfe + 5
#
#  Compute and test allowable tolerances versus local error estimates
#  and remove scaling of tolerances.  The relative error is
#  measured with respect to the average of the magnitudes of the
#  solution at the beginning and end of the step.
#
          eeoet = 0.0
          for k in range ( 0, neqn ):
              et = np.abs ( y[k] ) + np.abs ( f1[k] ) + ae
              if ( et <= 0.0 ):
                  flag = 5
                  return(y, yp, t, flag)
              ee = np.abs( ( -2090.0 * yp[k] + ( 21970.0 * f3[k] - 15048.0 * f4[k] )) \
                        + ( 22528.0 * f2[k] - 27360.0 * f5[k] ) )
              eeoet = np.maximum ( eeoet, ee / et )
          esttol = np.abs ( h ) * eeoet * scale / 752400.0
          if ( esttol <= 1.0 ):
              break
#
#  Unsuccessful step.  Reduce the stepsize, try again.
#  The decrease is limited to a factor of 1/10.
#
          hfaild = 1
          output = 0

          if ( esttol < 59049.0 ):
              s = 0.9 / esttol**0.2
          else:
              s = 0.1

          h = s * h
          if ( np.abs ( h ) < hmin ):
              flag = 6
              kflag = 6
              return ( y, yp, t, flag )
#
#  We left the loop because we took a successful step.
#  Store the solution for T+H, and evaluate the derivative there.
#
      t = t + h
      y = f1.copy()
      yp = f ( t, y )
      nfe = nfe + 1
#
#  Choose the next stepsize.  The increase is limited to a factor of 5.
#  If the step failed, the next stepsize is not allowed to increase.
#
      if ( 0.0001889568 < esttol ):
        s = 0.9 / esttol**0.2
      else:
        s = 5.0

      if ( hfaild ):
          s = np.minimum ( s, 1.0 )
      if ( h < 0.0 ):
          h = - np.maximum ( s * np.abs ( h ), hmin )
      else:
          h = + np.maximum ( s * np.abs ( h ), hmin )
#
#  End of core integrator
#
#  Should we take another step?
#
      if ( output ):
        t = tout
        flag = 2
        return ( y, yp, t, flag )

      if ( flag <= 0 ):
        break
#
#  One step integration mode.
#
  flag = - 2
  return ( y, yp, t, flag )

def fehl ( f, neqn, y, t, h, yp ):

#*****************************************************************************80
#
## fehl() takes one Fehlberg fourth-fifth order step.
#
#  Discussion:
#
#    This routine integrates a system of NEQN first order ordinary differential
#    equations of the form
#      dY(i)/dT = F(T,Y(1:NEQN))
#    where the initial values Y and the initial derivatives
#    YP are specified at the starting point T.
#
#    The routine advances the solution over the fixed step H and returns
#    the fifth order (sixth order accurate locally) solution
#    approximation at T+H in array S.
#
#    The formulas have been grouped to control loss of significance.
#    The routine should be called with an H not smaller than 13 units of
#    roundoff in T so that the various independent arguments can be
#    distinguished.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    Original FORTRAN77 version by Herman Watts, Lawrence Shampine.
#    This version by John Burkardt.
#
#  Reference:
#
#    Erwin Fehlberg,
#    Low-order Classical Runge-Kutta Formulas with Stepsize Control,
#    NASA Technical Report R-315, 1969.
#
#    Lawrence Shampine, Herman Watts, S Davenport,
#    Solving Non-stiff Ordinary Differential Equations - The State of the Art,
#    SIAM Review,
#    Volume 18, pages 376-411, 1976.
#
#  Input:
#
#    function F, evaluates the derivatives dYdT, of the form:
#      function yp = f ( t, y )
#
#    integer NEQN, the number of equations to be integrated.
#
#    real Y(NEQN), the current value of the dependent variable.
#
#    real T, the current value of the independent variable.
#
#    real H, the step size to take.
#
#    real YP(NEQN), the current derivative of the dependent variable.
#
#  Output:
#
#    real F1(NEQN), F2(NEQN), F3(NEQN), F4(NEQN), F5(NEQN), derivative 
#    values needed for the computation.
#
#    real S(NEQN), the estimate of the solution at T+H.
#
  ch = h / 4.0
  f5 = y + ch * yp
  f1 = f ( t + ch, f5 )
  ch = 3.0 * h / 32.0
  f5 = y + ch * ( yp + 3.0 * f1 )
  f2 = f ( t + 3.0 * h / 8.0, f5 )
  ch = h / 2197.0
  f5 = y + ch * ( 1932.0 * yp + ( 7296.0 * f2 - 7200.0 * f1 ) )
  f3 = f ( t + 12.0 * h / 13.0, f5 )
  ch = h / 4104.0
  f5 = y + ch * (( 8341.0 * yp - 845.0 * f3) + ( 29440.0 * f2 - 32832.0 * f1 ) )
  f4 = f ( t + h, f5 )
  ch = h / 20520.0
  f1 = y + ch * ( ( -6080.0 * yp + ( 9295.0 * f3 - 5643.0 * f4 ) ) + \
                  ( 41040.0 * f1 - 28352.0 * f2 ) )
  f5 = f ( t + h / 2.0, f1 )
#
#  Ready to compute the approximate solution at T+H.
#
  ch = h / 7618050.0
  s = y + ch * ( ( 902880.0 * yp + ( 3855735.0 * f3 - 1371249.0 * f4 ) ) \
      + ( 3953664.0 * f2 + 277020.0 * f5 ) )

  return ( f1, f2, f3, f4, f5, s )

def rkf45_test ( ):

#*****************************************************************************80
#
## rkf45_test() tests rkf45().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rkf45_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rkf45().' )

  rkf45_test04 ( )
  rkf45_test05 ( )
  rkf45_test06 ( )
#
#  Terminate.
#
  print ( '')
  print ( 'rkf45_test():')
  print ( '  Normal end of execution.' )

  return

def rkf45_test04 ( ):

#*****************************************************************************80
#
## rkf45_test04() solves a scalar ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rkf45_test04():' )
  print ( '  Solve a scalar equation using rkf45():' )
  print ( '' )
  print ( '  Y'' = 0.25 * Y * ( 1 - Y / 20 )' )

  neqn = 1
  abserr = np.sqrt ( np.finfo(np.double).eps )
  relerr = np.sqrt ( np.finfo(np.double).eps )
  flag = 1
  t_start = 0.0
  t_stop = 20.0
  n_step = 5
  t_out = 0.0
  t = t_out
  y = np.array ( [ 1.0 ] )
  yp = f1 ( t, y )
  print ( '' )
  print ( '  FLAG     T             Y            Y''           Y_Exact         Error' )
  print ( '%4d  %12f  %12f  %12f  %12f  %12e' %(\
    flag, t, y[0], yp[0], y1x ( t ), y[0] - y1x ( t ) ) )

  for i_step in range( 1 , n_step+1 ):
    t = ( ( n_step - i_step + 1 ) * t_start + ( i_step - 1 ) * t_stop ) / ( n_step)
    t_out = ( ( n_step - i_step ) * t_start  + ( i_step ) * t_stop ) / ( n_step)
    y, yp, t, flag = rkf45 ( f1, neqn, y, yp, t, t_out, relerr, abserr, flag )
    print ( '%4d  %12f  %12f  %12f  %12f  %12e' %(\
      flag, t, y[0], yp[0], y1x ( t ), y[0] - y1x ( t ) ) )

  return

def f1 ( t, y ):

#*****************************************************************************80
#
## f1() evaluates the derivative for the ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the value of the independent variable.
#
#    real Y, the value of the dependent variable.
#
#  Output:
#
#    real YP, the value of the derivative dY(1:NEQN)/dT.
#
  import numpy as np

  yp = np.zeros ( 1 )
  yp[0] = 0.25 * y[0] * ( 1.0 - y[0] / 20.0 )

  return ( yp )

def rkf45_test05 ( ):

#*****************************************************************************80
#
## rkf45_test05() solves a vector ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2006
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rkf45_test05():' )
  print ( '  Solve a vector equation using rkf45()' )
  print ( '' )
  print ( '  Y''(1) =  Y(2)' )
  print ( '  Y''(2) = -Y(1)' )

  neqn = 2
  abserr = np.sqrt ( np.finfo(np.double).eps )
  relerr = np.sqrt ( np.finfo(np.double).eps )
  flag = 1
  t_start = 0.0
  t_stop = 2.0 * np.pi
  n_step = 12
  tarray = np.linspace ( t_start, t_stop, n_step + 1 )
  t = tarray[0]
  y = np.zeros ( neqn )
  y[0] = 1.0
  yp = f2 ( t, y )
  print ( '' )
  print ( '  FLAG       T          Y(1)          Y(2)' )
  print ( '%4d  %12f  %12f  %12f' %( flag, t, y[0], y[1] ) )
  for i in range ( 0, n_step ):
    t = tarray[i]
    t_out = tarray[i+1]
    y, yp, t, flag = rkf45 ( f2, neqn, y, yp, t, t_out, relerr, abserr, flag )
    print ( '%4d  %12f  %12f  %12f' %( flag, t, y[0], y[1] ) )

  return

def f2 ( t, y ):

#*****************************************************************************80
#
## f2() evaluates the derivative for the ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the value of the independent variable.
#
#    real Y(NEQN), the value of the dependent variable.
#
#  Output:
#
#    real YP(NEQN), the value of the derivatives dY(1:NEQN)/dT.
#
  import numpy as np

  yp = np.zeros ( 2 )
  yp[0] =  y[1]
  yp[1] = -y[0]

  return ( yp )

def y1x ( t ):

#*****************************************************************************80
#
## y1x() evaluates the exact solution of the ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the value of the independent variable.
#
#  Output:
#
#    real Y1X, the exact solution.
#
  import numpy as np

  value = 20.0 / ( 1.0 + 19.0 * np.exp ( - 0.25 * t ) )

  return ( value )

def rkf45_test06 ( ):

#*****************************************************************************80
#
## rkf45_test06() solves a scalar ODE and uses one-step integration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rkf45_test06():' )
  print ( '  Solve a scalar equation using rkf45()' )
  print ( '' )
  print ( '  Y'' = 0.25 * Y * ( 1 - Y / 20 )' )
  print ( '' )
  print ( '  Use the special SINGLE_STEP mode' )
  print ( '  which returns after every step.' )
  neqn = 1
  abserr = np.sqrt ( np.finfo(np.double).eps )
  relerr = np.sqrt ( np.finfo(np.double).eps )
  flag = -1
  t_start = 0.0
  t_stop = 20.0
  n_step = 5
  tarray = np.linspace ( t_start, t_stop, n_step + 1 )
  t = tarray[0]
  y = np.zeros ( 1 )
  y[0] = 1.0
  yp = f1 ( t, y )
  print ( '' )
  print ( '  FLAG     T             Y            dY/dt         Y_Exact      Error' )
  print ( '%4d  %12f  %12f  %12f  %12f    %12e' %(\
    flag, t, y[0], yp[0], y1x ( t ), y[0] - y1x ( t ) ) )
  for i in range ( 0, n_step ):
    t = tarray[i]
    t_out = tarray[i+1]
#
#  As long as FLAG is negative, we are heading towards T_OUT, but
#  have not reached it.
#
    while ( flag < 0 ):
      y, yp, t, flag  = rkf45 ( f1, neqn, y, yp, t, t_out, relerr, abserr, flag )
      print ( '%4d  %12f  %12f  %12f  %12f    %12e' %(\
        flag, t, y[0], yp[0], y1x ( t ), y[0] - y1x ( t ) ) )
#
#  FLAG is returned as +2 when we reach T_OUT.  Reset it to -2
# to continue to the next T_OUT in one step mode.
#
    flag = -2 
 
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
  rkf45_test ( )
  timestamp ( )

