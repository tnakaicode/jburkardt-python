#! /usr/bin/env python3
#
def president_heights_barh ( ):

#*****************************************************************************80
#
## president_heights_barh makes a horizontal bar plot of Presidential heights.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'president_heights_barh:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  plt.clf ( )

  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'president_heights_barh:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  president_heights_barh ( )
  timestamp ( )

