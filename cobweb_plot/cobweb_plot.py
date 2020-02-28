#! /usr/bin/env python3  
#
def cobweb_plot ( f, x0, N, a = 0, b = 1 ):

#*****************************************************************************80
#
## cobweb_plot makes a cobweb plot of a function iteration.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 February 2020
#
#  Author:
#
#    John D Cook.
#    Modifications by John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Cobweb plots,
#    https://www.johndcook.com/blog/2020/01/19/cobweb-plots/
#    Posted 19 January 2020.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Plot the function.
#
  t = np.linspace ( a, b, N )
  plt.plot ( t, f ( t ), 'k' )
#
#  Plot the dotted line y = x.
#
  plt.plot ( t, t, "k:" )
#   
#  Plot the iterates.
#
  x = x0
  y = f ( x0 )
  for _ in range ( N ):
    fy = f ( y )
    plt.plot ( [x, y], [y,  y], 'b', linewidth = 1 )
    plt.plot ( [y, y], [y, fy], 'b', linewidth = 1 )
    x = y
    y = fy
#
#  Give x and y axis the same scale.
#
  plt.axis ( 'equal' )
#
#  Save a copy of the figure.
#
  filename = 'cobweb_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Show the figure.
#
  plt.show()
  plt.close()

  return

def cobweb_plot_test ( ):

#*****************************************************************************80
#
## cobweb_plot_test tests cobweb_plot
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 February 2020
#
#  Author:
#
#    John D Cook.
#    Modifications by John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cobweb_plot_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test cobweb_plot.' )

  cobweb_plot ( np.cos, 1.0, 20 )
#
#  Terminate.
#
  print ( '' )
  print ( 'cobweb_plot_test:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  cobweb_plot_test ( )
  timestamp ( )
