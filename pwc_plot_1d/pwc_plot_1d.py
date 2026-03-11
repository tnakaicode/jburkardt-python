#! /usr/bin/env python3
#
def pwc_plot_1d_test ( ):

#*****************************************************************************80
#
## pwc_plot_1d_test() tests pwc_plot_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'pwc_plot_1d_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test pwc_plot().' )

  pwc_bars_1d_test ( )
  pwc_lines_1d_test ( )
  pwc_patch_1d_test ( )
  interval_width_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pwc_plot_1d_test():' )
  print ( '  Normal end of execution.' )

  return

def interval_width_test ( ):

#*****************************************************************************80
#
## interval_width_test() tests pwc_lines_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'interval_width_test()' )
  print ( '  pwc_lines_1d() displays a piecewise' )
  print ( '  constant function of a 1D argument as a broken line.' ) 
#
#  N is the number of intervals.
#
  n = 10
#
#  Select N-1 internal nodes.
#
  x = rng.random ( n - 1 )
#
#  Add nodes at 0.0 and 1.0.
#
  x = np.insert ( x, 0, 0.0 )
  x = np.insert ( x, n, 1.0 )
#
#  Shift to [5,10].
#
  x = x + 5.0
#
#  Sort the nodes.
#
  x.sort ( )
#
#  Let Y be the width of each interval.
#
  y = x[1:n+1] - x[0:n]
#
#  Get the sequence of points that can be used to draw the function.
#
  xp, yp = pwc_lines_1d ( x, y )
#
#  Plot.
#
  plt.clf ( )
  plt.plot ( xp, yp, 'b-o', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Width --->' )
  plt.title ( 'Interval widths.' )
  filename = 'interval_width_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def pwc_bars_1d ( x, y ):

#*****************************************************************************80
#
## pwc_bars_1d defines the lines forming a piecewise constant plot.
#
#  Discussion:
#
#    Given X1, Y1, X2, Y2, X3, ..., XN, YN, XN+1
#
#    such that F(X) = Y(I) for XI <= X <= XI+1, we can plot
#    this piecewise constant function by asking MATLAB to plot
#    a sequence of 3*N+1 points (XP,YP).
#
#    This version of the function draws the "seams" between neighboring bars.
#
#               +-+
#        +------+ |
#        |      | |
#    +---+      | +---+
#    |   |      | |   |
#    +   +      + +   +
#
#    N = 4, uses 13 points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N+1), the break points.
#
#    real Y(N), the function values.
#
#  Output:
#
#    real XP(3*N+1), YP(3*N+1), a sequence of points that
#    define the piecewise constant plot.
#
  import numpy as np

  n = len ( y )

  xp = np.zeros ( 3 * n + 1 )
  yp = np.zeros ( 3 * n + 1 )

  k = 0

  for i in range ( 0, n ):

    if ( i == 0 ):
      xp[k] = x[i]
      yp[k] = 0.0
      k = k + 1

    xp[k] = x[i]
    yp[k] = y[i]
    k = k + 1

    xp[k] = x[i+1]
    yp[k] = y[i]
    k = k + 1

    xp[k] = x[i+1]
    yp[k] = 0.0
    k = k + 1

  return xp, yp

def pwc_bars_1d_test ( ):

#*****************************************************************************80
#
## pwc_bars_1d_test() tests pwc_bars_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pwc_bars_1d_test():' )
  print ( '  pwc_bars_1d() displays a piecewise' )
  print ( '  constant function of a 1D argument as a sequence of bars.' ) 
#
#  Define the piecewise constant function.
#
  x = np.array ( [ 0.0,    4.0,    11.0,    13.0,    17.0 ] )
  y = np.array ( [     2.0,    4.0,     5.0,     2.0      ] )
#
#  Get the sequence of points that can be used to draw the function.
#
  xp, yp = pwc_bars_1d ( x, y )
#
#  Plot.
#
  plt.clf ( )
  plt.plot ( xp, yp, 'b-o', linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'pwc_bars_1d piecewise constant plot.' )
  filename = 'pwc_bars_1d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def pwc_lines_1d ( x, y ):

#*****************************************************************************80
#
## pwc_lines_1d defines the lines forming a piecewise constant plot.
#
#  Discussion:
#
#    Given X1, Y1, X2, Y2, X3, ..., XN, YN, XN+1
#
#    such that F(X) = Y(I) for XI <= X <= XI+1, we can plot
#    this piecewise constant function by asking MATLAB to plot
#    a sequence of 2*N+2 points (XP,YP).
#
#               +-+
#        +------+ |
#        |        |
#    +---+        +---+
#    |                |
#    +                +
#
#    N = 4, uses 10 points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N+1), the break points.
#
#    real Y(N), the function values.
#
#  Output:
#
#    real XP(2*N+2), YP(2*N+2), a sequence of points that
#    define the piecewise constant plot.
#
  import numpy as np

  n = len ( y )

  xp = np.zeros ( 2 * n + 2 )
  yp = np.zeros ( 2 * n + 2 )

  k = 0
#
#  Essentially, we draw N+1 vertical lines and connect them.
#
  for i in range ( 0, n + 1 ):

    if ( i == 0 ):

      xp[k] = x[i]
      yp[k] = 0.0
      k = k + 1

      xp[k] = x[i]
      yp[k] = y[i]
      k = k + 1

    elif ( i < n ):

      xp[k] = x[i]
      yp[k] = y[i-1]
      k = k + 1

      xp[k] = x[i]
      yp[k] = y[i]
      k = k + 1

    else:

      xp[k] = x[i]
      yp[k] = y[i-1]
      k = k + 1

      xp[k] = x[i]
      yp[k] = 0.0
      k = k + 1

      break

  return xp, yp

def pwc_lines_1d_test ( ):

#*****************************************************************************80
#
## pwc_lines_1d_test() tests pwc_lines_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pwc_lines_1d_test()' )
  print ( '  pwc_lines_1d() displays a piecewise' )
  print ( '  constant function of a 1D argument as a broken line.' ) 
#
#  Define the piecewise constant function.
#
  x = np.array ( [ 0.0,    4.0,    11.0,    13.0,    17.0 ] )
  y = np.array ( [     2.0,    4.0,     5.0,     2.0      ] )
#
#  Get the sequence of points that can be used to draw the function.
#
  xp, yp = pwc_lines_1d ( x, y )
#
#  Plot.
#
  plt.clf ( )
  plt.plot ( xp, yp, 'b-o', linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'pwc_lines_1d piecewise constant plot.' )
  filename = 'pwc_lines_1d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def pwc_patch_1d ( x, y ):

#*****************************************************************************80
#
## pwc_patch_1d() plots a piecewise constant function of X as color patches.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N+1), the breakpoint coordinates, in ascending order.
#
#    real Y(N), the interval values.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = len ( y )

  x_min = np.min ( x )
  x_max = np.max ( x )
  x_range = x_max - x_min
  y_min = -0.1 * x_range
  y_max =  0.1 * x_range
  yp = np.array ( [ y_min, y_min, y_max, y_max, y_min ] )

  plt.clf ( )

  for i in range ( 0, n ):
    xp = np.array ( [ x[i], x[i+1], x[i+1], x[i], x[i] ] )
    plt.fill ( xp, yp, y[i] )

  plt.xlabel ( '<--- X --->' )
  plt.title ( 'Color plot of interval widths' )
  plt.axis ( [ x_min, x_max, y_min, y_max ] )
  filename = 'pwc_patch_1d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def pwc_patch_1d_test ( ):

#*****************************************************************************80
#
## pwc_patch_1d_test() tests pwc_patch_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'pwc_patch_1d_test():' )
  print ( '  pwc_patch_1d() displays a piecewise' )
  print ( '  constant function of a 1D argument as a color patch plot.' ) 
#
#  N is the number of intervals.
#
  n = 20
#
#  Select N-1 internal nodes.
#
  x = rng.random ( n - 1 )
#
#  Add nodes at 0.0 and 1.0.
#
  x = np.insert ( x, 0, 0.0 )
  x = np.insert ( x, n, 1.0 )
#
#  Shift to [5,10].
#
  x = x + 5.0
#
#  Sort the nodes.
#
  x.sort ( )
#
#  Let Y be the width of each interval.
#
  y = x[1:n+1] - x[0:n]
#
#  Request a plot.
#
  pwc_patch_1d ( x, y )

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
  pwc_plot_1d_test ( )
  timestamp ( )

