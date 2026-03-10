#! /usr/bin/env python3
#
def price_subplots ( ):

#*****************************************************************************80
#
## price_subplots() reads price data and makes 6 subplots.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'price_subplots():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make 6 subplots of price data over time.' )
#
#  Read the data.
#
  price = np.loadtxt ( 'price_data.txt' )

  month_num = price.shape[0]
  month = np.arange ( month_num )

  label = [ \
    'Month', 'Year', 'Bananas', 'Oranges', 'Bread', \
    'Tomatoes', 'Chicken', 'Electricity', 'Eggs', 'Gasoline', \
    'Beef', 'Heating gas', 'Milk' ];
#
#  Plot the data.
#
  m = 2
  n = 3
  f, ax = plt.subplots ( m, n )

  f.suptitle ( '2x3 Price Subplots' )
#
#  Create 6 plots:
#
#  (0,0)  (0,1)  (0,2)
#  (1,0)  (1,1)  (1,2)
#
  k = 1
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      ax[i,j].plot ( month, price[:,k] )
      ax[i,j].set_title ( label[k] )

  filename = 'price_subplots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'iris_subplots():' )
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
  price_subplots ( )
  timestamp ( )
 
