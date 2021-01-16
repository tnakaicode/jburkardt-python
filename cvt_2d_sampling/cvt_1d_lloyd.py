#! /usr/bin/env python3
#
def cvt_1d_lloyd ( n = 0, it_num = 0, init = 0, prefix = '' ):

#*****************************************************************************80
#
## CVT_1D_LLOYD: Lloyd's Centroidal Voronoi Tessellation (CVT) algorithm in 1D.
#
#  Discussion:
#
#    For points in a 1D interval, the exact computation of the Voronoi regions
#    is simple.  Problems in higher dimensions or complicated geometries
#    can require approximation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of generators.
#
#    Input, integer IT_NUM, the number of iterations to take.
#
#    Input, integer INIT, 
#    1, for random initialization,
#    2, for a "squashed" initialization.
#
#    Optional input, string PREFIX, a prefix for the graphics filenames.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'CVT_1D_LLOYD' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
    seed = 123456789
    g[1:n+1], seed = r8vec_uniform_01 ( n, seed )
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
  plt.clf ( )
  print ( '' )
  print ( '  Created plot file "%s".' % ( filename ) )
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
  plt.clf ( )
  print ( '  Created plot file "%s".' % ( filename ) )
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
  plt.clf ( )
  print ( '  Created plot file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CVT_1D_LLOYD' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647;

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = numpy.zeros ( n );

  for i in range ( 0, n ):

    k = floor ( seed / 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  cvt_1d_lloyd ( 10, 20, 1, 'random_' )
  cvt_1d_lloyd ( 10, 20, 2, 'squashed_' )
  timestamp ( )

