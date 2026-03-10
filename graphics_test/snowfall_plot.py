#! /usr/bin/env python3
#
def snowfall_plot ( ):

#*****************************************************************************80
#
## snowfall_plot() plots yearly snowfall data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'snowfall_plot():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
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
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snowfall_plot():' )
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
#    06 April 2013
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
  snowfall_plot ( )
  timestamp ( )
 
