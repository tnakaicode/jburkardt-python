#! /usr/bin/env python3
#
def price_plots ( ):

#*****************************************************************************80
#
## price_plots reads price data and plots 3 prices on one display.
#
#  Discussion:
#
#    The blood level concentration of a medicinal drug, in mg / l, has been 
#    recorded over time.  
#
#    The concentration level must reach 800 mg / liter to be medicinally
#    effective but becomes toxic at 1000 mg / liter.
#
#    It is desired to plot the concentration level, as well as two horizontal
#    lines representing the medicinal and toxic levels.
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

  print ( '' );
  print ( 'price_plots:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Simulate the variation over time of the concentration' )
  print ( '  of a medicinal drug in the bloodstream.' )
#
#  Read the data.
#
  data = np.genfromtxt ( 'price_data.csv', dtype = None, delimiter=',', names = True )
#
#  Extract price columns for bananas, gas, and milk.
#
  bananas = data['Bananas']
  gas = data['Gas']
  milk = data['Milk']

  n = len ( bananas )
  index = np.linspace ( 1, n, n )
#   
#  Plot the results
#
  plt.plot ( index, bananas, linewidth = 3 )
  plt.plot ( index, gas, linewidth = 3 )
  plt.plot ( index, milk, linewidth = 3 )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Display the plot.
#
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'price_plots:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  price_plots ( )
