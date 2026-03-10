#! /usr/bin/env python3
#
def president_heights_barh ( ):

#*****************************************************************************80
#
## president_heights_barh() makes a horizontal bar plot of Presidential heights.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 April 2019
#
#  Author:
#
#    John Burkardt
#
  import csv
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'president_heights_barh():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Create a horizontal bar plot of the height in inches of US presidents.' )
#
#  Read the values from the file.
#
  types = ['U20', 'i4' ]
  data = np.genfromtxt ( 'president_heights_data.csv', dtype = types, delimiter=',', names=True)
  reader = csv.reader ( 'president_heights_data.csv', delimiter=',' )

  height = data['Height']
  names = data['Name']

  n = len ( height )
  index = np.linspace ( 1, n, n )
#
#  Create the bar plot.
#
  plt.barh ( index, height )
  plt.grid ( True )
  plt.title ( 'US President Heights', fontsize = 16 )
  plt.xlabel ( '<-- Height (inches) -->', fontsize = 16 )
  plt.yticks ( index, names, fontsize = 6 )
  filename = 'president_heights_barh.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'president_heights_barh():' )
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
  president_heights_barh ( )
  timestamp ( )

