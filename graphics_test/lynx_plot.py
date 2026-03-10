#! /usr/bin/env python3
#
def lynx_plot ( ):

#*****************************************************************************80
#
## lynx_plot() draws a curve with datapoints marked.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2016
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
  print ( 'lynx_plot():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a curve by connecting a series of data points.' )
  print ( '  Mark the data points.' )
#
#  Read the pairs "Year, Lynx harvest" from the file.
#
  x = []
  y = []

  file = open ( 'lynx_data.txt', 'r' )

  for line in file:
    line = line.strip ( )
    columns = line.split ( )
    x.append ( float ( columns[0] ) )
    y.append ( float ( columns[1] ) )

  file.close ( )
#
#  Plot the data.
#
  plt.plot ( x, y, linewidth = 2, color = 'g' )
  plt.plot ( x, y, 'ko' )
  plt.grid ( True )
  plt.xlabel ( '<--- Year --->', fontsize = 16 )
  plt.ylabel ( '<--- Lynx Harvest --->', fontsize = 16 )
  plt.title ( 'Lynx Population Records', fontsize = 16 )

  filename = 'lynx_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )

  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lynx_plot():' )
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
  lynx_plot ( )
  timestamp ( )
 
