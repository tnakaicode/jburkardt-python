#! /usr/bin/env python3
#
def kdv_exact_test ( ):

#*****************************************************************************80
#
## kdv_exact_test() tests kdv_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'kdv_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test kdv_exact().' )

  kdv_exact_rational_test ( )
  kdv_exact_sech_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'kdv_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def kdv_exact_rational_test ( ):

#*****************************************************************************80
#
## kdv_exact_rational_test() tests kdv_exact_rational().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'kdv_exact_rational_test():' )
  print ( '  Test kdv_exact_rational().' )

  _, _, t0, tstop = kdv_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    t0    =', t0 )
  print ( '    tstop =', tstop )

  print ( '' )
  print ( '  Evaluate solution and residual at selected points (X,T)' )
  
  x = np.linspace ( 0.0, 1.0, 6 )
  t = np.linspace ( t0, tstop, 6 )

  print ( '' )
  print ( '      X       T       U(X,T)      Resid(X,T)' )
  print ( '' )
  for j in range ( 0, 6 ):
    for i in range ( 0, 6 ):
      if ( x[i] == 0.0 and t[j] == 0.0 ):
        print ( '  %8.2f  %8.2f  ********  ********' % ( x[i], t[j] ) )
      else:
        u, ut, ux, uxx, uxxx = kdv_exact_rational ( x[i], t[j] )
        r = kdv_residual ( u, ut, ux, uxxx )
        print ( '  %8.2f  %8.2f  %8.2f  %g' % ( x[i], t[j], u, r ) )
    print ( '' )

  return

def kdv_exact_rational ( x, t ):

#*****************************************************************************80
#
## kdv_exact_rational(): exact solution of KDV PDE using rational function().
#
#  Discussion:
#
#    This solution u(x,t) satisfies the Korteweg-Devries PDE:
#      u' - 6 u ux + uxxx = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2023
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
#    real x: the position.
#
#    real t: the time.
#
#  Output:
#
#    real u, ut, ux, uxx, uxxx:
#    the values of the solution and its derivatives.
#
  u = 6.0 * x * ( x**3 - 24.0 * t ) \
    / ( x**3 + 12.0 * t )**2

  ut = - 288.0 * x * ( x**3 - 6.0 * t ) \
    / ( x**3 + 12.0 * t )**3

  ux = - 12.0 * ( x**6 - 84.0 * t * x**3 + 144.0 * t**2 ) \
    / ( x**3 + 12.0 * t )**3

  uxx =  36.0 * ( x**8 - 192.0 * t * x**5 + 1440.0 * t**2 * x**2 ) \
    / ( x**3 + 12.0 * t )**4

  uxxx = - 144.0 * x * ( x**9 - 360.0 * t * x**6 \
    + 6480.0 * t**2 * x**3 - 8640.0 * t**3 )\
    / ( x**3 + 12.0 * t )**5

  return u, ut, ux, uxx, uxxx 

def kdv_exact_sech_test ( ):

#*****************************************************************************80
#
## kdv_exact_sech_test() tests kdv_exact_sech().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'kdv_exact_sech_test():' )
  print ( '  Test kdv_exact_sech().' )

  a, v, t0, tstop = kdv_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    a     =', a )
  print ( '    v     =', v )
  print ( '    t0    =', t0 )
  print ( '    tstop =', tstop )

  print ( '' )
  print ( '  Evaluate solution and residual at selected points (X,T)' )
  
  x = np.linspace ( 0.0, 1.0, 6 )
  t = np.linspace ( t0, tstop, 6 )

  print ( '' )
  print ( '      X       T       U(X,T)      Resid(X,T)' )
  print ( '' )
  for j in range ( 0, 6 ):
    for i in range ( 0, 6 ):
      u, ut, ux, uxx, uxxx = kdv_exact_sech ( x[i], t[j] )
      r = kdv_residual ( u, ut, ux, uxxx )
      print ( '  %8.2f  %8.2f  %8.2f  %g' % ( x[i], t[j], u, r ) )
    print ( '' )

  return

def kdv_exact_sech ( x, t ):

#*****************************************************************************80
#
## kdv_exact_sech(): exact solution of KDV PDE using sech().
#
#  Discussion:
#
#    This solution u(x,t) satisfies the Korteweg-Devries PDE:
#      u' - 6 u ux + uxxx = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Solitons and the KdV equation,
#    03 November 2023,
#    https://www.johndcook.com/blog/2023/11/03/solitons-and-the-kdv-equation/
#
#  Input:
#
#    real x: the position.
#
#    real t: the time.
#
#  Output:
#
#    real u, ut, ux, uxx, uxxx:
#    the values of the solution and its derivatives.
#
  import numpy as np
#
#  Retrieve parameters a and v.
#
  a, v, _, _ = kdv_parameters ( )

  argument = 0.5 * np.sqrt ( v ) * ( x - v * t - a )
  sa = sech ( argument )
  ta = np.tanh ( argument )

  u =    - 0.5  * v      * sa**2

  ut =   - 0.5  * v**2.5 * sa**2 * ta

  ux =     0.5  * v**1.5 * sa**2 * ta

  uxx =  + 0.25 * v**2   * sa**4 \
         - 0.5  * v**2   * sa**2 * ta**2

  uxxx =        - v**2.5 * sa**4 * ta \
         + 0.5  * v**2.5 * sa**2 * ta**3

  return u, ut, ux, uxx, uxxx 

def kdv_parameters ( a_user = None, v_user = None, t0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## kdv_parameters(): parameters for the Korteweg-Devries PDE.
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
#    04 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real a_user: the phase
#
#    real v_user: the velocity
#
#    real t0_user: the initial time
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real a: the phase.
#
#    real v: the velocity
#
#    real t0: the initial time
#
#    real tstop: the final time.
#

#
#  Initialize defaults.
#
  if not hasattr ( kdv_parameters, "a_default" ):
    kdv_parameters.a_default = 0.0

  if not hasattr ( kdv_parameters, "v_default" ):
    kdv_parameters.v_default = 1.0

  if not hasattr ( kdv_parameters, "t0_default" ):
    kdv_parameters.t0_default = 0.0

  if not hasattr ( kdv_parameters, "tstop_default" ):
    kdv_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    kdv_parameters.y0_default = a_user

  if ( v_user is not None ):
    kdv_parameters.y0_default = v_user

  if ( t0_user is not None ):
    kdv_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    kdv_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = kdv_parameters.a_default
  v = kdv_parameters.v_default
  t0 = kdv_parameters.t0_default
  tstop = kdv_parameters.tstop_default
  
  return a, v, t0, tstop

def kdv_residual ( u, ut, ux, uxxx ):

#*****************************************************************************80
#
## kdv_residual(): evaluate the residual of KDV PDE.
#
#  Discussion:
#
#    The residual of the Korteweg-Devries PDE:
#      u' - 6 u ux + uxxx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Solitons and the KdV equation,
#    03 November 2023,
#    https://www.johndcook.com/blog/2023/11/03/solitons-and-the-kdv-equation/
#
#  Input:
#
#    real u, ut, ux, uxxx:
#    the values of the solution and its derivatives.
#
#  Output:
#
#    real r: the residual.
#
  r = ut - 6.0 * u * ux + uxxx

  return r

def sech ( x ):

#*****************************************************************************80
#
## sech() evaluates the hyperbolic secant function.
#
#  Discussion:
#
#    Oddly, numpy does not include this function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real sech: the value of sech(x).
#
  import numpy as np

  value = 1.0 / np.cosh ( x )

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
  kdv_exact_test ( )
  timestamp ( )

