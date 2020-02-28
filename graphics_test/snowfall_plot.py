#! /usr/bin/env python3
#
def snowfall_plot ( ):

#*****************************************************************************80
#
## snowfall_plot plots yearly snowfall data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'snowfall_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a line plot of snowfall data.' )
#
#  Read the data.
#
  filename = 'snowfall_data.txt'
  data = np.loadtxt ( filename )

  year = data[:,0]
  total = data[:,9]
#
#  Plot the data.
#
  plt.plot ( year, total, linewidth = 3, color = 'b' )
  plt.grid ( True )
  plt.xlabel ( '<--- Year --->', fontsize = 16 )
  plt.ylabel ( '<--- Total Snowfall (inches) --->', fontsize = 16 )
  plt.title ( 'Yearly Snowfall at Michigan Tech', fontsize = 16 )

  filename = 'snowfall_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snowfall_plot' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  snowfall_plot ( )
  timestamp ( )
 
