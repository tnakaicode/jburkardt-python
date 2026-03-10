#! /usr/bin/env python3
#
def double_c_data_test ( ):

#*****************************************************************************80
#
## double_c_data_test() tests double_c_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'double_c_data_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test double_c_data().' )

  n0 = 25
  n1 = 25
  x, y, c = double_c_data ( n0, n1 )
  filename = 'double_c_data_' + str ( n0 ) + '_' + str ( n1 ) + '.txt'
  double_c_write ( filename, x, y, c )

  n0 = 100
  n1 = 100
  x, y, c = double_c_data ( n0, n1 )
  filename = 'double_c_data_' + str ( n0 ) + '_' + str ( n1 ) + '.txt'
  double_c_write ( filename, x, y, c )

  n0 = 100
  n1 = 400
  x, y, c = double_c_data ( n0, n1 )
  filename = 'double_c_data_' + str ( n0 ) + '_' + str ( n1 ) + '.txt'
  double_c_write ( filename, x, y, c )

  n0 = 500
  n1 = 500
  x, y, c = double_c_data ( n0, n1 )
  filename = 'double_c_data_' + str ( n0 ) + '_' + str ( n1 ) + '.txt'
  double_c_write ( filename, x, y, c )

  n0 = 800
  n1 = 600
  x, y, c = double_c_data ( n0, n1 )
  double_c_plot ( x, y, c )
#
#  Terminate.
#
  print ( '' )
  print ( 'double_c_data_test():' )
  print ( '  Normal end of execution.' )

  return

def double_c_data ( n0, n1 ):

#*****************************************************************************80
#
## double_c_data() generates "double C" data that is difficult to separate.
#
#  Discussion:
#
#    The data comprises a "C" shape and its reverse, which do not intersect,
#    but which nestle together fairly closely.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#   integer N0, N1, the number of points to be generated in set 0 and 
#   set 1, respectively.
#
#  Output:
#
#   real X(N), Y(N), the coordinates of the data points.  The points
#   have been shuffled so that data belonging to the two components is
#   interleaved.
#
#   integer C(N), is 0 or 1, depending on which set the corresponding
#   data point belongs to.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = n0 + n1

  x = np.zeros ( n )
  y = np.zeros ( n )
  c = np.zeros ( n, dtype = int )
#
#  Generate first set.
#
  r = 2.0 + 3.0 * rng.random ( n0 )
  t = np.pi * ( 0.5 + rng.random ( n0 ) )
  x[0:n0] = 1.0 + r * np.cos ( t )
  y[0:n0] =       r * np.sin ( t )
  c[0:n0] = np.zeros ( n0, dtype = int )
#
#  Generate the second set.
#
  r = 2.0 + 3.0 * rng.random ( n1 )
  t = np.pi * ( 1.5 + rng.random ( n1 ) )
  x[n0:n0+n1] = 0.0 + r * np.cos ( t )
  y[n0:n0+n1] = 3.5 + r * np.sin ( t )
  c[n0:n0+n1] = np.ones ( n1, dtype = int )
#
#  Generate a random permutation.
#  Because I want the same permutation on all three objects, I can't
#  apply random.shuffle directly, but have to construct an index array.
#  After that, I have to go through a series of clumsy and somewhat
#  idiotic contortions to get what I want.
#
  p = np.arange ( n0 + n1, dtype = int )
  p = np.random.shuffle ( p )
#
#  Apply the random permutation to the data.
#
  x = x[p]
  y = y[p]
  c = c[p]

  x = x.flatten ( )
  y = y.flatten ( )
  c = c.flatten ( )

  return x, y, c

def double_c_plot ( x, y, c ):

#*****************************************************************************80
#
## double_c_plot() displays the "double C" data.
#
#  Discussion:
#
#    The data comprises a "C" shape and its reverse, which do not intersect,
#    but which nestle together fairly closely.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#   real X(N), Y(N), the coordinates of the data points.  The points
#   have been shuffled so that data belonging to the two components is
#   interleaved.
#
#   integer C(N), is 0 or 1, depending on which set the corresponding
#   data point belongs to.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n0 = np.sum ( c == 0 )
  n1 = np.sum ( c == 1 )

  plt.plot ( x[c == 0], y[c == 0], 'r.' )
  plt.plot ( x[c == 1], y[c == 1], 'b.' )

  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- Y -->' )
  s = 'Double C Data, N0 = ' + str ( n0 ) + ' N1 = ' + str ( n1 )
  plt.title ( s )
  plt.legend ( [ 'Set 0', 'Set 1' ] )
  plt.grid ( True )
  plt.axis ( 'equal' )

  filename = 'double_c_data_' + str ( n0 ) + '_' + str ( n1 ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def double_c_write ( filename, x, y, c ):

#*****************************************************************************80
#
## double_c_write() writes double C data to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the output filename.
#
#    real X(N), Y(N), the coordinates of the data points.
#
#    integer C(N), is 0 or 1, depending on which set the corresponding
#    data point belongs to.
#

#
#  Open the file.
#
  output = open ( filename, 'w' )
#
#  Write the data.
#
  n = len ( x )

  for i in range ( 0, n ):
    s = '  %g' % ( x[i] )
    output.write ( s )
    s = '  %g' % ( y[i] )
    output.write ( s )
    s = '  %d\n' % ( c[i] )
    output.write ( s )
#
#  Close the file.
#
  output.close ( )

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
#    21 August 2019
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
  double_c_data_test ( )
  timestamp ( )

