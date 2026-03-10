#! /usr/bin/env python3
#
def arclength_test ( ):

#*****************************************************************************80
#
## arclength_test() tests arclength().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'arclength_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test arclength().' )

  arclength_x_test ( )
  arclength_t_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'arclength_test():' )
  print ( '  Normal end of execution.' )

  return

def arclength_t ( t1, t2, dxdt, dydt, n ):

#*****************************************************************************80
#
## arclength_t() estimates arclength for a curve of the form (x(t),y(t)).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real t1, t2: the parameter range over which the curve extends.
#
#    function dxdt, dydt: functions which evaluate dx/dt and dy/dt.
#
#    integer n: the number of intervals to use.
#
#  Output:
#
#    real s: the estimated arclength.
#
  import numpy as np

  dt = ( t2 - t1 ) / n

  t = np.linspace ( t1, t2, n + 1 )
  fx = dxdt ( t )
  fy = dydt ( t )

  s = dt * ( np.sum ( np.sqrt ( fx**2 + fy**2 ) ) \
    - 0.5 * np.sqrt ( fx[0]**2 + fy[0]**2 ) \
    - 0.5 * np.sqrt ( fx[n]**2 + fy[n]**2 ) )

  return s

def arclength_t_test ( ):

#*****************************************************************************80
#
## arclength_t_test() tests arclength_t().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'arclength_t_test():' )
  print ( '  arclength_t() estimates the arclength of a curve (x(t),y(t))' )
  print ( '  over a range t1 <= t <= t2 using n intervals.' )
#
#  Circle.
#
  t1 = 0.0
  t2 = 2.0 * np.pi
  n = 2

  s_true = 2.0 * np.pi

  print ( '' )
  print ( '   n    s        |error|' )
  print ( '' )
  for i in range ( 0, 5 ):
    s = arclength_t ( t1, t2, dxdt1, dydt1, n )
    e = abs ( s - s_true )
    print ( '  %2d  %8.6f  %8.6f' % ( n, s, e ) )
    n = n * 2
#
#  Ellipse
#
  t1 = 0.0
  t2 = 2.0 * np.pi
  n = 2

  s_true = 69.03933778699452855

  print ( '' )
  print ( '   n    s        |error|' )
  print ( '' )
  for i in range ( 0, 5 ):
    s = arclength_t ( t1, t2, dxdt2, dydt2, n )
    e = np.abs ( s - s_true )
    print ( '  %2d  %8.6f  %8.6f' % ( n, s, e ) )
    n = n * 2
#
#  Astroid
#
  t1 = 0.0
  t2 = 2.0 * np.pi
  n = 2

  s_true = 6.0

  print ( '' )
  print ( '   n    s        |error|' )
  print ( '' )
  for i in range ( 0, 10 ):
    s = arclength_t ( t1, t2, dxdt3, dydt3, n )
    e = np.abs ( s - s_true )
    print ( '  %2d  %8.6f  %8.6f' % ( n, s, e ) )
    n = n * 2
#
#  Cycloid
#
  t1 = 0.0
  t2 = 2.0 * np.pi
  n = 2

  s_true = 8.0

  print ( '' )
  print ( '   n    s        |error|' )
  print ( '' )
  for i in range ( 0, 5 ):
    s = arclength_t ( t1, t2, dxdt4, dydt4, n )
    e = abs ( s - s_true )
    print ( '  %2d  %8.6f  %8.6f' % ( n, s, e ) )
    n = n * 2

  return

def dxdt1 ( t ):

#*****************************************************************************80
#
## dxdt1 returns the x derivative of test function 1.
#
#  Discussion:
#
#    x(t) = cos ( t )
#    y(t) = sin ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  value = - np.sin ( t )

  return value

def dydt1 ( t ):

#*****************************************************************************80
#
## dydt1 returns the y derivative of test function 1.
#
#  Discussion:
#
#    x(t) = cos ( t )
#    y(t) = sin ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  value = np.cos ( t )

  return value

def dxdt2 ( t ):

#*****************************************************************************80
#
## dxdt2 returns the x derivative of test function 2.
#
#  Discussion:
#
#    x(t) = 15 * cos ( t )
#    y(t) = 6 * sin ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  a = 15.0
  value = - a * np.sin ( t )

  return value

def dydt2 ( t ):

#*****************************************************************************80
#
## dydt2 returns the y derivative of test function 2.
#
#  Discussion:
#
#    x(t) = 15 cos ( t )
#    y(t) = 6 sin ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  b = 6.0
  value = b * np.cos ( t )

  return value

def dxdt3 ( t ):

#*****************************************************************************80
#
## dxdt3 returns the x derivative of test function 3.
#
#  Discussion:
#
#    x(t) = cos^3 ( t )
#    y(t) = sin^3 ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  value = - 3.0 * np.sin ( t ) * ( np.cos ( t ) )**2

  return value

def dydt3 ( t ):

#*****************************************************************************80
#
## dydt3 returns the y derivative of test function 3.
#
#  Discussion:
#
#    x(t) = cos^3 ( t )
#    y(t) = sin^3 ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  value = 3.0 * np.cos ( t ) * ( np.sin ( t ) )**2

  return value

def dxdt4 ( t ):

#*****************************************************************************80
#
## dxdt4 returns the x derivative of test function 4.
#
#  Discussion:
#
#    x(t) = t - sin ( t )
#    y(t) = 1 - cos ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  value = 1.0 - np.cos ( t )

  return value

def dydt4 ( t ):

#*****************************************************************************80
#
## dydt4 returns the y derivative of test function 4.
#
#  Discussion:
#
#    x(t) = t - sin ( t )
#    y(t) = 1 - cos ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at T.
#
  import numpy as np

  value = np.sin ( t )

  return value

def arclength_x ( x1, x2, dydx, n ):

#*****************************************************************************80
#
## arclength_x() estimates arclength for a curve of the form (x,f(x)).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x1, x2: the range over which the curve extends.
#
#    function handle dydx: a function which evaluates dy/dx.
#
#    integer n: the number of intervals to use.
#
#  Output:
#
#    real s: the estimated arclength.
#
  import numpy as np

  dx = ( x2 - x1 ) / n

  x = np.linspace ( x1, x2, n + 1 )
  dy = dydx ( x )

  s = dx * ( np.sum ( np.sqrt ( 1.0 + dy**2 ) ) \
    - 0.5 * np.sqrt ( 1.0 + dy[0]**2 ) \
    - 0.5 * np.sqrt ( 1.0 + dy[n]**2 ) )

  return s

def arclength_x_test ( ):

#*****************************************************************************80
#
## arclength_x_test() tests arclength_x().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'arclength_x_test():' )
  print ( '  arclength_x() estimates the arclength of a curve (x,y(x))' )
  print ( '  over a range x1 <= x <= x2 using n intervals.' )

  x1 = 1.0
  x2 = 4.0
  n = 2

  s_true = 14.0 / 3.0

  print ( '' )
  print ( '   n    s        |error|' )
  print ( '' )
  for i in range ( 0, 5 ):
    s = arclength_x ( x1, x2, dydx1, n )
    e = np.abs ( s - s_true )
    print ( '  %2d  %8.6f  %8.6f' % ( n, s, e ) )
    n = n * 2

  x1 = 0.0
  x2 = 1.0
  n = 2

  s_true = ( 8.0 / 27.0 ) * ( np.sqrt ( ( 13.0 / 4.0 )**3 ) - 1.0 )

  print ( '' )
  print ( '   n    s        |error|' )
  print ( '' )
  for i in range ( 0, 5 ):
    s = arclength_x ( x1, x2, dydx2, n )
    e = np.abs ( s - s_true )
    print ( '  %2d  %8.6f  %8.6f' % ( n, s, e ) )
    n = n * 2

  return

def dydx1 ( x ):

#*****************************************************************************80
#
## dydx1 returns the derivative of test function 1.
#
#  Discussion:
#
#    y(x) = 2/3 ( x - 1 )^(3/2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at X.
#
  import numpy as np

  value = np.sqrt ( x - 1.0 )

  return value

def dydx2 ( x ):

#*****************************************************************************80
#
## dydx2 returns the derivative of test function 2.
#
#  Discussion:
#
#    y(x) = x^(3/2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: the argument.
#
#  Output:
#
#    real VALUE: the derivative value at X.
#
  import numpy as np

  value = 1.5 * np.sqrt ( x )

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
  arclength_test ( )
  timestamp ( )

