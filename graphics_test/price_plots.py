#! /usr/bin/env python3
#
def price_plots ( ):

#*****************************************************************************80
#
## price_plots() reads price data and plots 3 prices on one display.
#
#  Discussion:
#
#    The file price_data.txt contains average monthly prices for 11
#    consumer products, between February 2008 and February 2018.
#
#    There are 241 records, each containing 13 items:
#    month, year, 11 prices
#
#    Columns 3, 10 and 13 contain the prices of bananas, gas, and milk.
#    We want a single plot that shows the variation in these three prices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 August 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' );
  print ( 'price_plots():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Use line plots to display variation in price of three' )
  print ( '  quantities over time.' )
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
#  Plot the results
#
  plt.plot ( month, price[:,2], linewidth = 3 )
  plt.plot ( month, price[:,9], linewidth = 3 )
  plt.plot ( month, price[:,12], linewidth = 3 )
  plt.grid ( True )
  plt.legend ( [ 'Bananas', 'Gas', 'Milk' ] )
  plt.xlabel ( '<-- Month index -->', fontsize = 16 )
  plt.ylabel ( '<-- Price ($) -->', fontsize = 16 )
  plt.title ( 'Prices, Feb 2008-Feb 2018', fontsize = 16 )
#
#  Save a copy of the plot.
#
  filename = 'price_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'price_plots():' )
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
  price_plots ( )
  timestamp ( )

