#! /usr/bin/env python3
#
def f1 ( x ):

#*****************************************************************************80
#
## f1() evaluates a nonlinear system of 1 equation.
#
#  Discussion:
#
#    This is Kepler's equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  e = 0.8
  m = 5.0
  fx = np.zeros ( 1 )
  fx[0] = x[0] - m - e * np.sin ( x[0] )

  return fx

def f2 ( x ):

#*****************************************************************************80
#
## f2() evaluates a nonlinear system of 2 equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  fx = np.zeros ( 2 )

  fx[0] = x[0] * x[0] - 10.0 * x[0] + x[1] * x[1] + 8.0
  fx[1] = x[0] * x[1] * x[1] + x[0] - 10.0 * x[1] + 8.0

  return fx

def f3 ( x ):

#*****************************************************************************80
#
## f3() evaluates a nonlinear system of 4 equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  fx = np.zeros ( 4 )

  for i in range ( 0, 4 ):
    fx[i] = ( x[i] - ( i + 1 ) )**2

  return fx

def f4 ( x ):

#*****************************************************************************80
#
## f4() evaluates a nonlinear system of 8 equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  n = 8

  fx = np.zeros ( n )

  for i in range ( 0, n ):

    fx[i] = ( 3.0 - 2.0 * x[i] ) * x[i] + 1.0

    if ( 0 < i ):
      fx[i] = fx[i] - x[i-1]

    if ( i < n - 1 ):
      fx[i] = fx[i] - 2.0 * x[i+1]

  return fx

def fsolve_test ( ):

#*****************************************************************************80
#
## fsolve_test() tests fsolve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fsolve_test' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  fsolve() seeks a solution x of one or more nonlinear' )
  print ( '  equations f(x)=0.' )
  print ( '  In MATLAB, fsolve() is in the Optimization toolbox.' )
  print ( '  In Octave, fsolve() is directly available.' )
  print ( '  In Python, fsolve() is available in scipy.optimize.' )
  print ( '  In R, fsolve() is available in the pracma library.' )

  fsolve_test01 ( )
  fsolve_test02 ( )
  fsolve_test03 ( )
  fsolve_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fsolve_test' )
  print ( '  Normal end of execution.' )

  return

def fsolve_test01 ( ):

#*****************************************************************************80
#
## fsolve_test01() tests fsolve() on 1 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import fsolve
  import numpy as np

  print ( '' )
  print ( 'fsolve_test01' )
  print ( '  Use fsolve() to solve 1 nonlinear equation.' )

  x0 = np.array ( [ 0.0 ] )
  fx0 = f1 ( x0 )
  r8vec2_print ( x0, fx0, 'Initial X and F(X)' )

  x = fsolve ( f1, x0 )
  fx = f1 ( x )
  r8vec2_print ( x, fx, 'Final X and F(X)' )

  return

def fsolve_test02 ( ):

#*****************************************************************************80
#
## fsolve_test02() tests fsolve() on 2 functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import fsolve
  import numpy as np

  print ( '' )
  print ( 'fsolve_test02' )
  print ( '  Use fsolve() to solve 2 nonlinear equations.' )

  x0 = np.array ( [ 3.0, 0.0 ] )
  fx0 = f2 ( x0 )
  r8vec2_print ( x0, fx0, 'Initial X and F(X)' )

  x = fsolve ( f2, x0 )
  fx = f2 ( x )
  r8vec2_print ( x, fx, 'Final X and F(X)' )

  return

def fsolve_test03 ( ):

#*****************************************************************************80
#
## fsolve_test03() tests fsolve() on 4 functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import fsolve
  import numpy as np

  print ( '' )
  print ( 'fsolve_test03' )
  print ( '  Use fsolve() to solve 4 nonlinear equations.' )

  x0 = np.zeros ( 4 )
  fx0 = f3 ( x0 )
  r8vec2_print ( x0, fx0, 'Initial X and F(X)' )

  x = fsolve ( f3, x0 )
  fx = f3 ( x )
  r8vec2_print ( x, fx, 'Final X and F(X)' )

  return

def fsolve_test04 ( ):

#*****************************************************************************80
#
## fsolve_test04() tests fsolve() on 8 functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import fsolve
  import numpy as np

  print ( '' )
  print ( 'fsolve_test04' )
  print ( '  Use fsolve() to solve 8 nonlinear equations.' )

  x0 = np.zeros ( 8 )
  fx0 = f4 ( x0 )
  r8vec2_print ( x0, fx0, 'Initial X and F(X)' )

  x = fsolve ( f4, x0 )
  fx = f4 ( x )
  r8vec2_print ( x, fx, 'Final X and F(X)' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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
  fsolve_test ( )
  timestamp ( )

