#! /usr/bin/env python3
#
def cvt_1d_sampling ( g_num = 0, it_num = 0, s_num = 0 ):

#*****************************************************************************80
#
## cvt_1d_sampling() carries out the Lloyd algorithm in a 1D interval.
#
#  Discussion:
#
#    This program is a variation of the cvt_1d_lloyd() method.
#
#    Instead of using an exact technique to determine the Voronoi
#    regions, it uses sampling.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G_NUM, the number of generators.
#    A value of 50 is reasonable.
#
#    integer IT_NUM, the number of CVT iterations.
#    A value of 20 or 50 might be reasonable.
#
#    integer S_NUM, the number of sample points to use
#    when estimating the Voronoi regions.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'cvt_1d_sampling():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Generate a centroidal Voronoi tessellation (CVT)' )
  print ( '  of the unit interval, using random starting points' )
  print ( '  and random sampling to estimate Voronoi regions.' )

  if ( g_num <= 0 ):
    prompt = '  Enter number of generators:  '
    inp = raw_input ( prompt )
    g_num = int ( inp )

  if ( it_num <= 0 ):
    prompt = '  Enter number of iterations:  '
    inp = raw_input ( prompt )
    it_num = int ( inp )

  if ( s_num <= 0 ):
    prompt = '  Enter number of sample points:  '
    inp = raw_input ( prompt )
    s_num = int ( inp )

  print ( '' )
  print ( '  Number of generators is %d' % ( g_num ) )
  print ( '  Number of iterations is %d' % ( it_num ) )
  print ( '  Number of samples    is %d' % ( s_num ) )
#
#  Random number generator is randomly seeded.
#
  rng = default_rng ( )
#
#  Initialize the generators.
#
  g = rng.random ( size = g_num )
#
#  Force two generators to lie on the boundary.
#
  g[0] = 0.0
  g[1] = 1.0
#
#  Sort them.
#
  g = np.sort ( g )
#
#  Print the initial generators.
#
  print ( '' )
  print ( '  Initial generators:' )
  print ( g )
#
#  Initialize the plotting arrays.
#
  g_plot = np.zeros ( [ it_num + 1, g_num ] )

  step = np.zeros ( it_num + 1 )
  e = 1.0E-10 * np.ones ( it_num + 1 )
  gm = 1.0E-10 * np.ones ( it_num + 1 )
#
#  Carry out the iteration.
#
  for it in range ( 1, it_num + 1 ):

    step[it] = it

    g_plot[it,:] = g.copy ( )

    s = rng.random ( size = s_num )
#
#  For each sample point, find K, the index of the nearest generator.
#
    k = [ np.argmin ( [ np.inner ( gg - ss, gg - ss ) for gg in g ] ) for ss in s ]
#
#  For each generator, M counts the number of sample points it is nearest to.
#  Note that for a nonuniform density, we just set W to the density.
#
    w = np.ones ( s_num )
    m = np.bincount ( k, weights = w )
#
#  G is the average of the sample points it is nearest to.
#  Where M is zero, we shouldn't modify G.
#
    g_new = np.bincount ( k, weights = s )

    print ( 'len (m) = ', len ( m ) )
    print ( m )
    for i in range ( 0, g_num ):
      if ( 0 < m[i] ):
        g_new[i] = g_new[i] / float ( m[i] )
#
#  Compute the energy.
#
    e[it] = 0.0
    for i in range ( 0, s_num ):
      e[it] = e[it] + ( s[i] - g_new[k[i]] ) ** 2
#
#  Display the log of the energy.
#
    subfig3 = plt.subplot ( 2, 2, 3 )
    plt.plot ( step[0:it+1], np.log ( e[0:it+1] ), 'm-*', linewidth = 2 )
    plt.title ( 'Log (Energy)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Energy' )
    plt.grid ( True )
#
#  Compute the generator motion.
#
    for i in range ( 0, g_num ):
      gm[it] = gm[it] + ( g_new[i] - g[i] ) ** 2
#
#  Display the generator motion.
#
    subfig4 = plt.subplot ( 2, 2, 4 )
    plt.plot ( step[0:it+1], np.log ( gm[0:it+1] ), 'm-*', linewidth = 2 )
    plt.title ( 'Log (Average generator motion)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Energy' )
    plt.grid ( True )
#
#  Put a title on the plot.
#
    super_title = 'Iteration ' + str ( it )
    plt.suptitle ( super_title )
#
#  Save the first and last plots.
#
    if ( it == 0 ):
      filename = 'initial.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "', filename, '"' )
    elif ( it == it_num - 1 ):
      filename = 'final.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )

    plt.show ( block = False )
    plt.close ( )
#
#  Update the generators.
#
    g = g_new.copy ( )

  return

def cvt_1d_sampling_test ( ):

#*****************************************************************************80
#
## cvt_1d_sampling_test() tests cvt_1d_sampling().
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
  print ( 'cvt_1d_sampling_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test cvt_1d_sampling()' )

  cvt_1d_sampling ( 16, 20, 1000 )
#
#  Terminate.
#
  print ( '' )
  print ( 'cvt_1d_sampling_test()' )
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
  cvt_1d_sampling_test ( )
  timestamp ( )

