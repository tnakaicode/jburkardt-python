#! /usr/bin/env python3
#
def root_test ( ):

#*****************************************************************************80
#
## root_test() tests root().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'root_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  root() seeks a solution x of one or more nonlinear' )
  print ( '  equations f(x)=0.' )

  root_test01 ( )
  root_test02 ( )
  root_test03 ( )
  root_test04 ( )
  root_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'root_test():' )
  print ( '  Normal end of execution.' )

  return

def root_test01 ( ):

#*****************************************************************************80
#
## root_test01() tests root_scalar() on 1 function of 1 variable.
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
  from scipy.optimize import root_scalar
  import numpy as np

  print ( '' )
  print ( 'root_test01' )
  print ( '  Use root_scalar() to solve 1 equation in 1 unknown.' )

  x0 = 0.0
  fx0 = f1_scalar ( x0 )
  print ( '    Initial X0 = ', x0, '  f(x0) = ', fx0 )

  sol = root_scalar ( f1_scalar, x0 = x0 )
  x = sol.root
  fx = f1_scalar ( x )
  print ( '    Final X = ', x, '  f(x) = ', fx )

  return

def root_test02 ( ):

#*****************************************************************************80
#
## root_test02() tests root() on 1 function of 1 variable.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2026
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import root
  import numpy as np

  print ( '' )
  print ( 'root_test02' )
  print ( '  Use root() to solve 1 nonlinear equation.' )

  x0 = np.array ( [ 0.0 ] )
  fx0 = f1 ( x0 )
  r8vec2_print ( x0, fx0, '  Initial X and F(X)' )

  sol = root ( f1, x0 )
  x = sol.x
  fx = f1 ( x )
  r8vec2_print ( x, fx, '  Final X and F(X)' )

  return

def root_test03 ( ):

#*****************************************************************************80
#
## root_test03() tests root() on 2 functions in 2 unknowns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2026
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import root
  import numpy as np

  print ( '' )
  print ( 'root_test03():' )
  print ( '  Use root() to solve 2 nonlinear equations in 2 variables.' )

  x0 = np.array ( [ 3.0, 0.0 ] )
  fx0 = f2 ( x0 )
  r8vec2_print ( x0, fx0, '  Initial X and F(X)' )

  sol = root ( f2, x0 )
  x = sol.x
  fx = f2 ( x )
  r8vec2_print ( x, fx, '  Final X and F(X)' )

  return

def root_test04 ( ):

#*****************************************************************************80
#
## root_test04() tests root() on 4 functions in 4 unknowns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2026
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import root
  import numpy as np

  print ( '' )
  print ( 'root_test04' )
  print ( '  Use root() to solve 4 nonlinear equations in 4 variables.' )

  x0 = np.zeros ( 4 )
  fx0 = f3 ( x0 )
  r8vec2_print ( x0, fx0, '  Initial X and F(X)' )

  sol = root ( f3, x0 )
  x = sol.x
  fx = f3 ( x )
  r8vec2_print ( x, fx, '  Final X and F(X)' )

  return

def root_test05 ( ):

#*****************************************************************************80
#
## root_test05() tests root() on 8 functions in 8 unknowns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2026
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import root
  import numpy as np

  print ( '' )
  print ( 'root_test05():' )
  print ( '  Use root() to solve 8 nonlinear equations in 8 variables.' )

  x0 = np.zeros ( 8 )
  fx0 = f4 ( x0 )
  r8vec2_print ( x0, fx0, '  Initial X and F(X)' )

  sol = root ( f4, x0 )
  x = sol.x
  fx = f4 ( x )
  r8vec2_print ( x, fx, '  Final X and F(X)' )

  return

def f1_scalar ( x ):

#*****************************************************************************80
#
## f1_scalar() evaluates a nonlinear system of 1 equation in 1 unknown.
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
#    07 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: the variable values.
#
#  Output:
#
#    real FX, the function value at X.
#
  import numpy as np

  e = 0.8
  m = 5.0
  fx = x - m - e * np.sin ( x )

  return fx

def f1 ( x ):

#*****************************************************************************80
#
## f1() evaluates a nonlinear system of 1 equation in one unknown.
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
## f2() evaluates a nonlinear system of 2 equations in 2 unknowns.
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
## f3() evaluates a nonlinear system of 4 equations in 4 unknowns..
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
## f4() evaluates a nonlinear system of 8 equations in 8 unknowns.
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
  root_test ( )
  timestamp ( )

