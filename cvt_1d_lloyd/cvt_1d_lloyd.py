#! /usr/bin/env python3
#
def cvt_1d_lloyd ( n = 0, it_num = 0, init = 0, prefix = '' ):

#*****************************************************************************80
#
## cvt_1d_lloyd(): Lloyd's Centroidal Voronoi Tessellation (CVT) algorithm in 1D.
#
#  Discussion:
#
#    For points in a 1D interval, the exact computation of the Voronoi regions
#    is simple.  Problems in higher dimensions or complicated geometries
#    can require approximation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of generators.
#
#    integer IT_NUM, the number of iterations to take.
#
#    integer INIT, 
#    1, for random initialization,
#    2, for a "squashed" initialization.
#
#    string PREFIX, a prefix for the graphics filenames.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'cvt_1d_lloyd():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Apply Lloyd\'s algorithm repeatedly to a set of N points' )
  print ( '  in a 1D interval, seeking the Centroidal Voronoi ' )
  print ( '  Tessellation (CVT) solution.' )

  if ( n <= 0 ):
    prompt = '  Enter number of generators:  '
    s = raw_input ( prompt )
    n = int ( s )

  if ( it_num <= 0 ): 
    prompt = '  Enter number of iterations:  '
    s = raw_input ( prompt )
    it_num = int ( s )

  if ( init <= 0 ):
    prompt = '  Enter 1 for random initializion, 2 for squashed:  '
    s = raw_input ( prompt )
    init = int ( s )

  print ( '' )
  print ( '  Number of generators is %d' % ( n ) )
  print ( '  Number of iterations is %d' % ( it_num ) )
  print ( '  Initialization option is %d' % ( init ) )
  print ( '  Optional prefix for graphics files is "%s"' % ( prefix ) )
#
#  Allocate the array for current generators.
#
  g = np.zeros ( n + 2 )
#
#  For convenience, bracket the data with an initial 0.0 and final 1.0 point.
#  These extra two points make it easier to compute the centroids of the
#  intervals containing the original points.  Other than that, they do nothing.
#
  g[0] = 0.0

  if ( init == 1 ):
    g[1:n+1] = rng.random ( size = n )
  else:
    g[1:n+1] = np.linspace ( 0.01, 0.02, n )

  g[n+1] = 1.0
#
#  Sort the generators.
#
  g.sort ( )
#
#  Print the generators.
#
  r8vec_print ( n, g[1:n+2], '  Initial generators:' )
#
#  Initialize the plotting arrays.
#
  g_new = np.zeros ( n + 2 )
  g_plot = np.zeros ( [ n + 2, it_num + 1 ] )
  step = np.zeros ( it_num )
  e = np.zeros ( it_num )
  gm = np.zeros ( it_num )

  g_plot[0:n+2,0] = g[0:n+2]
#
#  Carry out IT_NUM iterations.
#
  for it in range ( 0, it_num ):

    step[it] = it
#
#  Compute the new generators.
#
    j = 0
    g_new[j] = 0.0
    j = 1
    g_new[j] = (           g[j-1]          + 0.5 * ( g[j] + g[j+1] ) ) / 2.0
    for j in range ( 2, n ):
      g_new[j] = ( 0.5 * ( g[j-1] + g[j] ) + 0.5 * ( g[j] + g[j+1] ) ) / 2.0
    j = n
    g_new[j] =   ( 0.5 * ( g[j-1] + g[j] ) +                g[j+1]   ) / 2.0
    j = n + 1
    g_new[j] = 1.0
#
#  Compute the energy of this set of generators.
#
    e[it] = 0.0
    for j in range ( 1, n + 1 ):
      xl = ( g[j-1] + g[j] ) / 2.0
      xr = ( g[j+1] + g[j] ) / 2.0
      x = g[j]
      e[it] = e[it] + ( ( xr - x ) ** 3 - ( xl - x ) ** 3 ) / 3.0
#
#  Compute the motion, the change in G from the previous step.
#
    gm[it] = np.linalg.norm ( g_new - g )
#
#  Update the generators.
#
    g[0:n+2] = g_new[0:n+2]
#
#  Save a copy of G for the plot.
#
    g_plot [ 0:n+2, it+1 ] = g[0:n+2]
#
#  Print the final generators.
#
  r8vec_print ( n, g[1:n+2], '  Final generators:' )
#
#  Plot the total energy.
#
  plt.plot ( step, np.log ( e ), 'g-*', linewidth = 2.0 )
  plt.title ( 'Log (Energy)' )
  plt.grid ( True )
  plt.xlabel ( '<--- Step --->' )
  plt.ylabel ( '<--- Log(Energy) --->' )
  filename = prefix + 'energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.close ( )

#
#  Plot the total generator motion.
#
  plt.plot ( step, np.log ( gm ), 'b-*', linewidth = 2.0 )
  plt.title ( 'Log (Generator motion)' )
  plt.grid ( True )
  plt.xlabel ( '<--- Step --->' )
  plt.ylabel ( '<--- Log(Motion) --->' )
  filename = prefix + 'motion.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.close ( )
#
#  Plot the individual generators.
#
  step2 = np.zeros ( it_num + 1 )
  step2 = np.linspace ( 0, it_num, it_num + 1 )
  for i in range ( 1, n + 2 ):
    plt.plot ( g_plot[i,0:it_num+2], step2, 'r-', linewidth = 2.0 )
  plt.grid ( True )
  plt.title ( 'Generator evolution.' )
  plt.xlabel ( 'Generator positions' )
  plt.ylabel ( 'Iterations' ) 
  filename = prefix + 'evolution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.close ( )

  return

def cvt_1d_lloyd_test ( ):

#*****************************************************************************80
#
## cvt_1d_lloyd_test() tests cvt_1d_lloyd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cvt_1d_lloyd_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test cvt_1d_lloyd()' )

  cvt_1d_lloyd ( 10, 20, 1, 'random_' )
  cvt_1d_lloyd ( 10, 20, 2, 'squashed_' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cvt_1d_lloyd_test():' )
  print ( '  Normal end of execution.' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an r8vec().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g' % ( i, a[i] ) )

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
  cvt_1d_lloyd_test ( )
  timestamp ( )

