#! /usr/bin/env python3
#
def sinc_test ( ):

#*****************************************************************************80
#
## sinc_test() tests sinc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'sincu_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test sinc().' )

  sincn_antideriv_test ( )
  sincn_deriv_test ( )
  sincn_deriv2_test ( )
  sincn_fun_test ( )

  sincu_antideriv_test ( )
  sincu_deriv_test ( )
  sincu_deriv2_test ( )
  sincu_fun_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sinc_test():' )
  print ( '  Normal end of execution.' )

  return

def sincn_antideriv ( x ):

#*****************************************************************************80
#
## sincn_antideriv(): antiderivative of the normalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  from scipy.special import sici
  import numpy as np

  pix = np.pi * x
  value, _ = sici ( pix )
  value = value / np.pi

  return value

def sincn_antideriv_test ( ):

#*****************************************************************************80
#
## sincn_antideriv_test() tests sincn_antideriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincn_antideriv_test():' )
  print ( '  sincn_antideriv() evaluates the antiderivative of sincn(x).' )

  a = -7.0
  b = +7.0
  x = np.linspace ( a, b, 101 )
  y = sincn_antideriv ( x )

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
  plt.title ( 'y = antideriv sincn(x)' )
  filename = 'sincn_antideriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincn_deriv ( x ):

#*****************************************************************************80
#
## sincn_deriv() evaluates the derivative of the normalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  import numpy as np

  value = np.zeros_like ( x )

  nz = np.where ( x != 0.0 )

  value[nz] = ( np.pi * x[nz] * np.cos ( np.pi * x[nz] ) \
    - np.sin ( np.pi * x[nz] ) ) / np.pi / x[nz]**2
  value[x==0.0] = 0.0

  return value

def sincn_deriv_test ( ):

#*****************************************************************************80
#
## sincn_deriv_test() tests sincn_deriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincn_deriv_test():' )
  print ( '  sincn_deriv() evaluates the derivative of sincn(x).' )

  a = -7.0
  b = +7.0
  x = np.linspace ( a, b, 101 )
  y = sincn_deriv ( x )

  plt.plot ( x, y, 'r-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = sincn\'(x)' )
  filename = 'sincn_deriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincn_deriv2 ( x ):

#*****************************************************************************80
#
## sincn_deriv2(): second derivative of the normalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  import numpy as np

  value = np.zeros_like ( x )

  eps = 1.0e-10
  nz = np.where ( eps < np.abs ( x ) )

  value[nz] = \
    ( ( 2.0 - np.pi**2 * x[nz]**2 ) * np.sin ( np.pi * x[nz] ) \
    - 2.0 * np.pi * x[nz] * np.cos ( np.pi * x[nz] ) ) / np.pi / x[nz]**3
  value[np.abs(x) <= eps ] = - np.pi**2 / 3.0

  return value

def sincn_deriv2_test ( ):

#*****************************************************************************80
#
## sincn_deriv2_test() tests sincn_deriv2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincn_deriv2_test():' )
  print ( '  sincn_deriv2() evaluates the second derivative of sincn(x).' )

  a = -7.0
  b = +7.0
  x = np.linspace ( a, b, 101 )
  y = sincn_deriv2 ( x )

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
  plt.title ( 'y = sincn"(x)' )
  filename = 'sincn_deriv2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincn_fun ( x ):

#*****************************************************************************80
#
## sincn_fun() evaluates the normalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  import numpy as np

  value = np.zeros_like ( x )

  nz = np.where ( x != 0.0 )

  value[nz] = np.sin ( np.pi * x[nz] ) / np.pi / x[nz]
  value[x==0.0] = 1.0

  return value

def sincn_fun_test ( ):

#*****************************************************************************80
#
## sincn_fun_test() tests sincn_fun().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincn_fun_test():' )
  print ( '  sincn_fun() evaluates the normalized sinc() function.' )

  a = -7.0
  b = +7.0
  x = np.linspace ( a, b, 101 )
  y = sincn_fun ( x )

  plt.plot ( x, y, 'b-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = sincn(x)' )
  filename = 'sincn_fun.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincu_antideriv ( x ):

#*****************************************************************************80
#
## sincu_antideriv(): antiderivative of the unnormalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  from scipy.special import sici
  import numpy as np

  value, _ = sici ( x )

  return value

def sincu_antideriv_test ( ):

#*****************************************************************************80
#
## sincu_antideriv_test() tests sincu_antideriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincu_antideriv_test():' )
  print ( '  sincu_antideriv() evaluates the antiderivative of sincu(x).' )

  a = -20.0
  b = +20.0
  x = np.linspace ( a, b, 101 )
  y = sincu_antideriv ( x )

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
  plt.title ( 'y = antideriv sincu(x)' )
  filename = 'sincu_antideriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincu_deriv2 ( x ):

#*****************************************************************************80
#
## sincu_deriv2(): second derivative of the unnormalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  import numpy as np

  value = np.zeros_like ( x )

  nz = np.where ( x != 0.0 )

  value[nz] = \
    ( ( 2.0 - x[nz]**2 ) * np.sin ( x[nz] ) \
    - 2.0 * x[nz] * np.cos ( x[nz] ) ) / x[nz]**3
  value[x==0.0] = - 1.0 / 3.0

  return value

def sincu_deriv2_test ( ):

#*****************************************************************************80
#
## sincu_deriv2_test() tests sincu_deriv2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincu_deriv2_test():' )
  print ( '  sincu_deriv2() evaluates the second derivative of sincu(x).' )

  a = -20.0
  b = +20.0
  x = np.linspace ( a, b, 101 )
  y = sincu_deriv2 ( x )

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
  plt.title ( 'y = sincu"(x)' )
  filename = 'sincu_deriv2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincu_deriv ( x ):

#*****************************************************************************80
#
## sincu_deriv() evaluates the derivative of the unnormalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  import numpy as np

  value = np.zeros_like ( x )

  nz = np.where ( x != 0.0 )

  value[nz] = ( x[nz] * np.cos ( x[nz] ) - np.sin ( x[nz] ) ) / x[nz]**2
  value[x==0.0] = 0.0

  return value

def sincu_deriv_test ( ):

#*****************************************************************************80
#
## sincu_deriv_test() tests sincu_deriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincu_deriv_test():' )
  print ( '  sincu_deriv() evaluates the derivative of sincu(x).' )

  a = -20.0
  b = +20.0
  x = np.linspace ( a, b, 101 )
  y = sincu_deriv ( x )

  plt.plot ( x, y, 'r-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = sincu\'(x)' )
  filename = 'sincu_deriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def sincu_fun ( x ):

#*****************************************************************************80
#
## sincu_fun() evaluates the unnormalized sinc() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2025
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
  import numpy as np

  value = np.zeros_like ( x )

  nz = np.where ( x != 0.0 )

  value[nz] = np.sin ( x[nz] ) / x[nz]
  value[x==0.0] = 1.0

  return value

def sincu_fun_test ( ):

#*****************************************************************************80
#
## sincu_fun_test() tests sincu_fun().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sincu_fun_test():' )
  print ( '  sincu_fun() evaluates the unnormalized sinc() function.' )

  a = -20.0
  b = +20.0
  x = np.linspace ( a, b, 101 )
  y = sincu_fun ( x )

  plt.plot ( x, y, 'b-', linewidth = 2 )

  plt.plot ( [a,b], [0,0], 'k-', linewidth = 2 )

  ymin = min ( y )
  ymax = max ( y )
  if ( ymin <= 0.0 and 0.0 <= ymax ):
    plt.plot ( [0, 0], [ymin,ymax], 'k-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'y = sincu(x)' )
  filename = 'sincu_fun.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

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
  sinc_test ( )
  timestamp ( )

