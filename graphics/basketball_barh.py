#! /usr/bin/env python3
#
def basketball_barh ( ):

#*****************************************************************************80
#
## basketball_barh makes a horizontal bar plot of basketball sponsorships.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'basketball_barh:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Create a horizontal bar plot of basketball sponsorships.' )
#
#  Read the values from the file.
#
  types = [ 'i4', 'U4', 'U7', 'i4', 'i4', 'i4', 'U3', 'U10', 'i4' ]
  data = np.genfromtxt ( 'basketball_data.csv', dtype = types, delimiter=',', names=True)

  name = data['Name']
  sponsorship = data['Sponsorship']

  n = len ( name )
  index = np.linspace ( 1, n, n )
#
#  Create the bar plot.
#
  plt.barh ( index, np.flip ( sponsorship ) )
  plt.grid ( True )
  plt.title ( 'Basketball sponsorship ($)', fontsize = 16 )
  plt.xlabel ( '<-- Sponsorship (1000$) -->', fontsize = 16 )
  plt.yticks ( index, np.flip ( name ), fontsize = 6 )
  filename = 'basketball_barh.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'basketball_barh:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  basketball_barh ( )
  timestamp ( )

