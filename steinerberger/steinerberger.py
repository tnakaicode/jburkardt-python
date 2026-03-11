#! /usr/bin/env python3
#
def steinerberger_test ( ):

#*****************************************************************************80
#
## steinerberger_test() tests steinerberger().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2025
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import quad
  from scipy.optimize import minimize_scalar
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'steinerberger_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test steinerberger().' )
#
#  Plots.
#
  print ( '' )
  print ( '  Plot f(n,x) for several values of n' )
  print ( '' )
  for n in [ 1, 5, 10, 25, 50, 100 ]:
    x = np.linspace ( 0.0, 1.0, 5001 )
    fx = steinerberger_function ( n, x )
    plt.clf ( )
    plt.plot ( x, fx, linewidth = 2 )
    plt.title ( 'Steinerberger f(' + str ( n ) + ',x)' )
    plt.grid ( True )
    filename = 'steinerberger_' + str ( n ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Integral estimates.
#
  print ( '' )
  print ( '  Integrate f(n,x) for several values of n' )
  print ( '' )
  print ( '   n           exact        estimate      error' )
  print ( '' )
  xmin = 0.0
  xmax = 1.0
  for n in [ 1, 5, 10, 25, 50, 100 ]:
    exact = 2.0 * harmonic_number ( n ) / np.pi
    q, err_est = quad ( lambda x: steinerberger_function ( n, x ), xmin, xmax )
    err = abs ( exact - q )
    print ( ' %3d  %14.6g  %14.6g  %14.6g' % ( n, exact, q, err ) )
#
#  Minimization.
#
  print ( '' )
  print ( '  Minimize f(n,x) for several values of n' )
  print ( '' )
  options = []

  xmin = 0.21
  xmax = 0.75
  for n in [ 1, 5, 10, 25, 50, 100 ]:
    result = minimize_scalar ( lambda x: steinerberger_function ( n, x ), \
      bounds = [ xmin, xmax ], method = 'bounded' )
    x = result.x
    fx = steinerberger_function ( n, x )
    its = result.nit
    print ( ' %3d  %4d  %14.6g  %14.6g' % ( n, its, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'steinerberger_test():' )
  print ( '  Normal end of execution.' )

  return

def harmonic_number ( n ):

#*****************************************************************************80
#
## harmonic_number() computes the Nth harmonic number.
#
#  Discussion:
#
#    H(N) = Sum ( 1 <= I <= N ) 1 / I
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the index of the harmonic number.
#
#  Output:
#
#    real VALUE: the value of the harmonic number.
#
  value = 0.0

  for i in range ( 1, n + 1 ):
    value = value + 1.0 / i

  return value

def steinerberger_function ( n, x ):

#*****************************************************************************80
#
## steinerberger_function() evaluates the Steinerberger function.
#
#  Discussion:
#
#    f(n,x) = sum ( 1 <= k <= n ) abs ( sin ( pi * k * x ) ) / k
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Pushing numerical integration software to its limits,
#    https://www.johndcook.com/blog/2023/06/12/stressing-numerical-integration/
#    Posted 12 June 2023.
#
#    John D Cook,
#    Plotting a function with lots of local minima,
#    https://www.johndcook.com/blog/2023/06/12/lots-of-local-minima/
#    Posted 12 June 2023.
#
#    Stefan Steinerberger,
#    A amusing sequence of functions,
#    Mathematics Magazine,
#    Volume 91, Number 4, October 2018, pages 262-266.
#
#  Input:
#
#    integer N: the index of the function.
#
#    real X: the evaluation point.
#
#  Output:
#
#    real VALUE: the function value.
#
  import numpy as np

  value = 0.0 * x
  for k in range ( 1, n + 1 ):
    value = value + abs ( np.sin ( k * np.pi * x ) ) / k

  return value

def steinerberger_integral01 ( n ):

#*****************************************************************************80
#
## steinerberger_integral01() returns the Steinerberger integral from 0 to 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Pushing numerical integration software to its limits,
#    https://www.johndcook.com/blog/2023/06/12/stressing-numerical-integration/
#    Posted 12 June 2023.
#
#    John D Cook,
#    Plotting a function with lots of local minima,
#    https://www.johndcook.com/blog/2023/06/12/lots-of-local-minima/
#    Posted 12 June 2023.
#
#    Stefan Steinerberger,
#    A amusing sequence of functions,
#    Mathematics Magazine,
#    Volume 91, Number 4, October 2018, pages 262-266.
#
#  Input:
#
#    integer N: the index of the function.
#
#  Output:
#
#    real VALUE: the value of the integral from 0 to 1.
#
  import numpy as np

  h = harmonic_number ( n )
  value = 2.0 * h / np.pi

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
  steinerberger_test ( )
  timestamp ( )


