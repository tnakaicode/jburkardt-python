#! /usr/bin/env python3
#
def svd_lls ( h, w, h_name, w_name, prefix ):

#*****************************************************************************80
#
## svd_lls() finds a linear least squares relation between data vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real H(N), W(N), two vectors of data.
#
#    string H_NAME, W_NAME, names for the two sets of data.
#
#    string PREFIX, the prefix to be used for the three plot files.
#
#  Output:
#
#    real SLOPE, B, the slope and intercept of the least squares relations.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'svd_lls():' )
  print ( '  Find best linear relation between two data vectors.' )
#
#  Data statistics.
#
  hmin = np.min ( h )
  hmean = np.mean ( h )
  hmax = np.max ( h )

  wmin = np.min ( w )
  wmean = np.mean ( w )
  wmax = np.max ( w )

  print ( '' )
  print ( '           Min  Mean  Max' )
  print ( '  %s: %g  %g  %g' % ( h_name, hmin, hmean, hmax ) )
  print ( '  %s: %g  %g  %g' % ( w_name, wmin, wmean, wmax ) )
#
#  Data for centered variables.
#
  h2 = h - hmean
  w2 = w - wmean
  h2min = np.min ( h2 )
  h2max = np.max ( h2 )
  w2min = np.min ( w2 )
  w2max = np.max ( w2 )
#
#  Create data matrix, get SVD, and determine the slope.
#  Note that Numpy's SVD has A=U*S*V, NOT A=U*S*V'.
#
  A = np.array ( [ h2, w2 ] )
  U, svec, V = np.linalg.svd ( A )
  slope = U[1,0] / U[0,0]
  b = wmean - slope * hmean
#
#  Report numerics.
#
  print ( '' )
  print ( '  Linear relationship:' )
  print ( '    %s-mean = %g * ( %s - mean )' % ( w_name, slope, h_name ) )
  print ( '' )
  print ( '  Affine relationship:' )
  print ( '    %s = %g * %s + %g' % ( w_name, slope, h_name, b ) )
#
#  #1: Plot the data.
#
  plt.clf ( )
  plt.plot ( \
    np.insert ( h, 0, 0.0 ), \
    np.insert ( w, 0, 0.0 ), \
    'bo', linewidth = 1 )
  plt.plot ( \
    np.array ( [ 0, hmax ] ), \
    np.array ( [ 0, 0 ] ), \
    'k-', linewidth = 3 )
  plt.plot ( \
    np.array ( [ 0, 0 ] ), \
    np.array ( [ 0, wmax ] ), \
    'k-', linewidth = 3 )
  label = '<-- ' + h_name + ' -->'
  plt.xlabel ( label )
  label = '<-- ' + w_name + ' -->'
  plt.ylabel ( label )
  label = 'Data for ' + h_name + ' versus ' + w_name
  plt.title ( label )
  plt.grid ( True )
  filename = prefix + '_plot01.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  #2: Plot the linear relationship.
#
  plt.clf ( )
  plt.plot ( \
    h2, w2, 'bo', linewidth = 1 )
  plt.plot ( \
    np.array ( [ h2min, h2max ] ), \
    np.array ( [ slope * h2min, slope * h2max ] ), \
    'r-', linewidth = 3 )
  plt.plot ( \
    np.array ( [ h2min, h2max ] ), \
    np.array ( [ 0, 0 ] ), \
    'k-', linewidth = 3 )
  plt.plot ( \
    np.array ( [ 0, 0 ] ), \
    np.array ( [ w2min, w2max ] ), \
    'k-', linewidth = 3 )
  plt.grid ( True )
  label = '<-- ' + h_name + ' - ' + str ( hmean )
  plt.xlabel ( label )
  label = '<-- ' + w_name + ' - ' + str ( wmean )
  plt.ylabel ( label )
  label = '(' + w_name + ' - wmean) = slope * (' + h_name + ' - hmean)'
  plt.title ( label )
  filename = prefix + '_plot02.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  #3: Plot the affine relationship.
#
  plt.clf ( )
  plt.plot ( \
    np.insert ( h, 0, 0.0 ), \
    np.insert ( w, 0, 0.0 ), \
    'bo', 'linewidth', 1 )
  plt.plot ( \
    np.array ( [ hmin, hmax ] ), \
    np.array ( [ slope * hmin + b, slope * hmax + b ] ), \
    'r-', linewidth = 3 )
  plt.plot ( \
    np.array ( [ 0, hmax ] ), \
    np.array ( [ 0, 0 ] ), 'k-', \
    linewidth = 3 )
  plt.plot ( \
    np.array ( [ 0, 0 ] ), \
    np.array ( [ 0, wmax ] ), \
    'k-', linewidth = 3 )
  plt.grid ( True )
  label = '<-- ' + h_name + ' -->'
  plt.xlabel ( label )
  label = '<-- ' + w_name + ' -->'
  plt.ylabel ( label )
  label = w_name + ' slope * ' + h_name + ' + b'
  plt.title ( label )
  filename = prefix + '_plot03.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return slope, b

def svd_lls_test ( ):

#*****************************************************************************80
#
## svd_lls_test() tests svd_lls().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'svd_lls_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  svd_lls() uses the SVD for linear least squares.' )

  data = np.loadtxt ( 'sex_age_height_weight.txt' )
  h = data[:,2]
  w = data[:,3]
  slope, intercept = svd_lls ( h, w, 'Height', 'Weight', 'hw' )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_lls_test():' )
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
  svd_lls_test ( )
  timestamp ( )
