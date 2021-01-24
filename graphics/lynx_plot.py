#! /usr/bin/env python3
#
def lynx_plot ( ):

#*****************************************************************************80
#
## lynx_plot draws a curve with datapoints marked.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2016
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import platform

  print ( '' )
  print ( 'lynx_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lynx_plot' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lynx_plot ( )
  timestamp ( )
 
