#! /usr/bin/env python3
#
def runge_test ( ):

#*****************************************************************************80
#
## runge_test() tests runge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'runge_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test runge.' )

  runge_antideriv_test ( )
  runge_deriv_test ( )
  runge_deriv2_test ( )
  runge_fun_test ( )
  runge_power_series_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'runge_test():' )
  print ( '  Normal end of execution.' )

  return

def runge_antideriv ( x ):

#*****************************************************************************80
#
## runge_antideriv() evaluates the antiderivative of the Runge function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument of the function.
#
#  Output:
#
#    real value: the value of the antiderivative.
#
  import numpy as np

  value = np.arctan ( 5.0 * x ) / 5.0

  return value

def runge_antideriv_test ( ):

#*****************************************************************************80
#
## runge_antideriv_test() tests runge_antideriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'runge_antideriv_test():' )
  print ( '  runge_antideriv() evaluates the antiderivative of runge(x).' )

  a = -1.0
  b = +1.0
  x = np.linspace ( a, b, 101 )
  y = runge_antideriv ( x )

  plt.clf ( )

  plt.plot ( x, y, 'g-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = antideriv runge(x)' )
  filename = 'runge_antideriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def runge_deriv2 ( x ):

#*****************************************************************************80
#
## runge_deriv2() evaluates the second derivative of the Runge function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument of the function.
#
#  Output:
#
#    real value, the value of the second derivative.
#
  u = - 50.0 * x
  up = - 50.0
  v = ( 1.0 + 25.0 * x * x )**2
  vp = 2.0 * ( 1.0 + 25.0 * x * x ) * ( 50.0 * x )

  value = ( up * v - u * vp ) / v**2

  return value

def runge_deriv2_test ( ):

#*****************************************************************************80
#
## runge_deriv2_test() tests runge_deriv2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'runge_deriv2_test():' )
  print ( '  runge_deriv2() evaluates the second derivative of runge(x).' )

  a = -1.0
  b = +1.0
  x = np.linspace ( a, b, 101 )
  y = runge_deriv2 ( x )

  plt.clf ( )

  plt.plot ( x, y, 'r-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = runge"(x)' )
  filename = 'runge_deriv2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def runge_deriv ( x ):

#*****************************************************************************80
#
## runge_deriv() evaluates the derivative of the Runge function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument of the function.
#
#  Output:
#
#    real value: the value of the derivative.
#
  value = - 50.0 * x / ( 1.0 + 25.0 * x * x )**2

  return value

def runge_deriv_test ( ):

#*****************************************************************************80
#
## runge_deriv_test() tests runge_deriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'runge_deriv_test():' )
  print ( '  runge_deriv() evaluates the derivative of runge(x).' )

  a = -1.0
  b = +1.0
  x = np.linspace ( a, b, 101 )
  y = runge_deriv ( x )

  plt.plot ( x, y, 'r-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = runge\'(x)' )
  filename = 'runge_deriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def runge_fun ( x ):

#*****************************************************************************80
#
## runge_fun() evaluates the Runge function.
#
#  Discussion:
#
#    This function causes a breakdown for
#    polynomial interpolation over equally spaced nodes in [-1,+1].
#
#    Runge originally considered the function 1/(1+x^2) over the
#    interval [-5,+5].  For convenience, a rescaled version is considered
#    over the interval [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument of the function.
#
#  Output:
#
#    real value: the value of the function.
#
  value = 1.0 / ( 1.0 + 25.0 * x * x )

  return value

def runge_fun_test ( ):

#*****************************************************************************80
#
## runge_fun_test() tests runge_fun().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'runge_fun_test():' )
  print ( '  runge_fun() evaluates the runge function.' )

  a = -1.0
  b = +1.0
  x = np.linspace ( a, b, 101 )
  y = runge_fun ( x )

  plt.plot ( x, y, 'b-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = runge(x)' )
  filename = 'runge_fun.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def runge_power_series ( x, n ):

#*****************************************************************************80
#
## runge_power_series() evaluates a power series for the Runge function.
#
#  Discussion:
#
#    The Runge function considered here has the form
#      f(x) = 1 / ( 1 + 25x^2 )
#
#    The power series is 1 - (5x)^2 + (5x)^4 - (5x)^6 + (5x)^8 - (5x)^10 ...
#
#    The power series is only well defined in the open interval 
#      -1/5 < x < 1/5
#    where successive terms gradually go to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument of the function.
#
#    integer n: the number of terms to be computed.
#
#  Output:
#
#    real value: the value of the function.
#
  value = 0.0
  term = 1.0
  for i in range ( 0, n ):
    value = value + term
    term = - term * ( 5.0 * x )**2

  return value

def runge_power_series_test ( ):

#*****************************************************************************80
#
## runge_power_series_test() tests runge_power_series().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'runge_power_series_test():' )
  print ( '  runge_power_series() evaluates a power series' )
  print ( '  for the runge function, valid in (-0.2, +0.2).' )

  a = -0.2
  b = +0.2
  x = np.linspace ( a, b, 101 )
  y1 = runge_fun ( x )
  y2 = runge_power_series ( x, 8 )

  plt.clf ( )

  plt.plot ( x, y1, 'b-', linewidth = 2 )
  plt.plot ( x, y2, 'ro' )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = np.min ( y1 )
  ymax = np.max ( y1 )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'runge(x) versus power series' )
  filename = 'runge_power_series.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"\n' )
#
#  Terminate.
#
  print ( '' )
  print ( 'runge_power_series_test():' )
  print ( '  Normal end of execution.' )

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
  runge_test ( )
  timestamp ( )

