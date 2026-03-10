#! /usr/bin/env python3
#
def schoolyear_barh ( ):

#*****************************************************************************80
#
## schoolyear_barh() makes a horizontal bar plot of schoolyear lengths.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2019
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
  print ( 'schoolyear_barh():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Create a horizontal bar plot of the length of schoolyears.' )
#
#  Read the values from the file.
#
  types = [ 'U20', 'i4' ]
  data = np.genfromtxt ( 'schoolyear_data.csv', dtype = types, delimiter=',', \
    names = True )

  days = data['Days']
  country = data['Country']

  n = len ( days )
  index = np.linspace ( 1, n, n )
#
#  Create the bar plot.
#
  plt.barh ( index, np.flip ( days ) )
  plt.grid ( True )
  plt.title ( 'Schoolyear lengths', fontsize = 16 )
  plt.xlabel ( '<-- Days -->', fontsize = 16 )
  plt.yticks ( index, np.flip ( country ), fontsize = 6 )
  filename = 'schoolyear_barh.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'schoolyear_barh():' )
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
  schoolyear_barh ( )
  timestamp ( )

