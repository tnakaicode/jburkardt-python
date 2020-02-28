#! /usr/bin/env python3
#
def cvt_2d_sampling ( g_num = 0, it_num = 0, s1d_num = 0 ):

#*****************************************************************************80
#
## CVT_2D_SAMPLING carries out the Lloyd algorithm in a 2D unit box.
#
#  Discussion:
#
#    This program is a variation of the CVT_2D_LLOYD method.
#
#    Instead of using an exact technique to determine the Voronoi
#    regions, it uses sampling.
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
#    Input, integer G_NUM, the number of generators.
#    A value of 50 is reasonable.
#
#    Input, integer IT_NUM, the number of CVT iterations.
#    A value of 20 or 50 might be reasonable.
#
#    Input, integer S1D_NUM, the number of sample points to use
#    when estimating the Voronoi regions.
#    A value of 1,000 is too low.  A value of 1,000,000 is somewhat high.
#
  import numpy as np
  import matplotlib.pyplot as plt
  import platform
  from scipy.spatial import Delaunay
  from scipy.spatial import Voronoi
  from scipy.spatial import voronoi_plot_2d
  from scipy import argmin
  from scipy import inner

  print ( '' )
  print ( 'CVT_2D_SAMPLING' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use sampling to approximate Lloyd\'s algorithm' )
  print ( '  in the 2D unit square.' )

  if ( g_num <= 0 ):
    prompt = '  Enter number of generators:  '
    inp = raw_input ( prompt )
    g_num = int ( inp )

  if ( it_num <= 0 ):
    prompt = '  Enter number of iterations:  '
    inp = raw_input ( prompt )
    it_num = int ( inp )

  if ( s1d_num <= 0 ):
    prompt = '  Enter number of sample points:  '
    inp = raw_input ( prompt )
    s1d_num = int ( inp )

  s_num = s1d_num * s1d_num

  print ( '' )
  print ( '  Number of generators is %d' % ( g_num ) )
  print ( '  Number of iterations is %d' % ( it_num ) )
  print ( '  Number of 1d samples is %d' % ( s1d_num ) )
  print ( '  Number of 2d samples is %d' % ( s_num ) )
#
#  Initialize the generators.
#
  seed = 123456789
  gx, seed = r8vec_uniform_01 ( g_num, seed )
  gy, seed = r8vec_uniform_01 ( g_num, seed )
#
#  Generate a fixed grid of sample points.
#  Since MESHGRID's documentation is too obscure, let's just do it the hard way.
#
  s_1d = np.linspace ( 0.0, 1.0, s1d_num )
  sx = np.zeros ( s_num )
  sy = np.zeros ( s_num )
  s = np.zeros ( [ s_num, 2 ] )
  k = 0
  for j in range ( 0, s1d_num ):
    for i in range ( 0, s1d_num ):
      sx[k] = s_1d[i]
      sy[k] = s_1d[j]
      s[k,0] = s_1d[i]
      s[k,1] = s_1d[j]
      k = k + 1
#
#  Carry out the iteration.
#
#  ERROR: I want to plot log ( E ) and log ( GM ) every step.
#  I should initialize E and GM to NAN's, assuming that, like
#  MATLAB, they won't plot.
#
  step = np.zeros ( it_num )
  e = 1.0E-10 * np.ones ( it_num )
  gm = 1.0E-10 * np.ones ( it_num )

  for it in range ( 0, it_num ):

    step[it] = it
#
#  Compute the Delaunay triangle information T for the current nodes.
#  Since my version of NUMPY is too old, I can't use the STACK command
#  to combine two vectors into an array.
#
    g = np.zeros ( [ g_num, 2 ] )
    g[:,0] = gx[:]
    g[:,1] = gy[:]
    tri = Delaunay ( g )
#
#  Display the Voronoi cells.
#
    subfig1 = plt.subplot ( 2, 2, 1 )   
    vor = Voronoi ( g )
    voronoi_plot_2d ( vor, ax = subfig1 )
#
#  Display the Delaunay triangulation.
#
    subfig2 = plt.subplot ( 2, 2, 2 )
    plt.triplot ( gx, gy, tri.simplices.copy( ) )
    plt.plot ( gx, gy, 'o' )
#
#  For each sample point, find K, the index of the nearest generator.
#
    k = [ argmin ( [ inner ( gg - ss, gg - ss ) for gg in g ] ) for ss in s ]
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
    gx_new = np.bincount ( k, weights = sx )
    gy_new = np.bincount ( k, weights = sy )

    for i in range ( 0, g_num ):
      if ( 0 < m[i] ):
        gx_new[i] = gx_new[i] / float ( m[i] )
        gy_new[i] = gy_new[i] / float ( m[i] )
#
#  Compute the energy.
#
    e[it] = 0.0
    for i in range ( 0, s_num ):
      e[it] = e[it] + ( sx[i] - gx_new[k[i]] ) ** 2 \
                    + ( sy[i] - gy_new[k[i]] ) ** 2
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
      gm[it] = gm[it] + ( gx_new[i] - gx[i] ) ** 2 \
                      + ( gy_new[i] - gy[i] ) ** 2
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
      print ( '  Graphics saved as "', filename, '"' )
#
#  Show the plot.
#  Apparently, SHOW can only come AFTER SAVEFIG, or you save nothing.
#
#   plt.show ( )
#
#  Clear the figure.
#
    plt.clf ( )
#
#  Update the generators.
#
    gx = gx_new
    gy = gy_new
#
#  Terminate.
#
  print ( '' )
  print ( 'CVT_2D_SAMPLING' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

def r8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8MAT_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_01 - Fatal error!' )

  r = numpy.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = floor ( seed / 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i][j] = seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01_TEST tests R8MAT_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_01 computes a random R8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_01 ( m, n, seed )

  print ( '' )
  print ( '  Random R8MAT:' )
  print ( '' )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      print ( '  %8.4g' % ( v[i,j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST:' )
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
    print ( '%6d:  %12g' % ( i, a[i] ) )

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

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  cvt_2d_sampling ( 16, 20, 100 )
  timestamp ( )

