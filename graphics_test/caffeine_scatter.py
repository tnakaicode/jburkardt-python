#! /usr/bin/env python3
#
def caffeine_scatter ( ):

#*****************************************************************************80
#
## caffeine_scatter: scatter plot of cataract incidence / caffeine intake..
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'caffeine_scatter:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read a data file of cataract incidence versus caffeine intake.' )
  print ( '  Display the data as a scatter plot.' )
#
#  Load the data.
#
  filename = 'caffeine_data.txt'
  data = np.loadtxt ( filename )
#
#  Split the data.
#
  cataracts = data[:,0]
  caffeine = data[:,1]
#
#  Plot the data.
#
  plt.scatter ( caffeine, cataracts )
  plt.grid ( True )
  plt.xlabel ( '<--- Daily caffeine intake (mg) --->', fontsize = 16 )
  plt.ylabel ( '<--- Blindness due to cataracts (%) --->', fontsize = 16 )
  plt.title ( 'Caffeine and cataracts', fontsize = 16 )
  filename = 'caffeine_scatter.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'caffeine_scatter' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  caffeine_scatter ( )
  timestamp ( )
 
