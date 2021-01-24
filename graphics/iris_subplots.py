#! /usr/bin/env python3
#
def iris_subplots ( ):

#*****************************************************************************80
#
## iris_subplots makes a plot of a 4x4 array of subplots of Iris data.
#
#  Discussion:
#
#    4 data values are available for multiple specimens of 3 varieties
#    of Iris.  These data values are the sepal length, sepal width, 
#    petal length, and petal width.
#
#    It is desired to create, for each pair of data values, a scatter plot.
#
#    By identifying the data for each variety by a separate color, it is
#    possible to detect patterns in the data.
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

  print ( '' )
  print ( 'iris_subplots:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  For each of 3 varieties of iris, a number of specimens' )
  print ( '  have been collected.  For each specimen, measurements' )
  print ( '  made of sepal length, sepal width, petal length and' )
  print ( '  petal width.' )
  print ( '' )
  print ( '  Create a 4x4 array of scatter plots that compare each' )
  print ( '  pair of values.  Moreoever, use colors to distinguish the' )
  print ( '  data belonging to each of the three varieties.' )
#
#  Read 3 sets of data.
#
  setosa = np.loadtxt ( 'iris_setosa_data.txt' );
  versicolor = np.loadtxt ( 'iris_versicolor_data.txt' );
  virginica = np.loadtxt ( 'iris_virginica_data.txt' );

  label = [ 'Sepal len', 'Sepal wid', 'Petal len', 'Petal wid' ];
#
#  Plot the data.
#
# f, ax = plt.subplots ( 4, 4, sharex='col', sharey='row' )
  f, ax = plt.subplots ( 4, 4 )

  f.suptitle ( '4x4 Iris Subplots' )

  for i in range ( 0, 4 ):
    for j in range ( 0, 4 ):
      ax[i,j].scatter (     setosa[:,i],     setosa[:,j], s = 10, color = 'r' )
      ax[i,j].scatter ( versicolor[:,i], versicolor[:,j], s = 10, color = 'g' )
      ax[i,j].scatter (  virginica[:,i],  virginica[:,j], s = 10, color = 'b' )
      ax[i,j].set_xlabel ( label[i], fontsize = 10 )
      ax[i,j].set_ylabel ( label[j], fontsize = 10 )
      ax[i,j].set_xticks ( [] )
      ax[i,j].set_yticks ( [] )

  filename = 'iris_subplots.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'iris_subplots' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  iris_subplots ( )
  timestamp ( )
 
