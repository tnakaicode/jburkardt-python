#! /usr/bin/env python3
#
def least_squares_plots ( ):

#*****************************************************************************80
#
## least_squares_plots: plot data, least squares line, exact formula.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'least_squares_plots:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compare 15 data points with the least squares line' )
  print ( '    y = A * x + B' )
  print ( '  which minimizes the root-mean-square error.' )
  print ( '  The data is actually perturbed values of a quadratic' )
  print ( '  formula, which is shown for comparison:' )
  print ( '    y = 1/2 x^2 + 1' )
#
#  Read the data.
#
  filename = 'least_squares1_data.txt'
  xy_data = np.loadtxt ( filename )

  filename = 'least_squares2_data.txt'
  xy_lsq = np.loadtxt ( filename )

  filename = 'least_squares3_data.txt'
  xy_exact = np.loadtxt ( filename )
#
#  Plot the data.
#
  plt.plot ( xy_lsq[:,0], xy_lsq[:,1], linewidth = 3, color = 'r' )
  plt.scatter ( xy_data[:,0], xy_data[:,1], color = 'b' )
  plt.plot ( xy_exact[:,0], xy_exact[:,1], linewidth = 3, color = 'g' )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  plt.title ( '  Formula (green), Data (blue), least squares fit (red).', fontsize = 16 )

  filename = 'least_squares_plots.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'least_squares_plots' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  least_squares_plots ( )
  timestamp ( )
 
