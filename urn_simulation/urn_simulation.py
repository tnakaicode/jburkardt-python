#! /usr/bin/env python3
#
def ksub_random2 ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random2() selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This algorithm is designated Algorithm RKS2 in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#    A Bebbington,
#    A simple method of drawing a sample without replacement,
#    Journal of Applied Statistics,
#    Volume 24, 1975, page 136.
#
#  Input:
#
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K).  A(I) is the I-th element of the
#    output set.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_random - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    raise Exception ( 'ksub_random - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_random2(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    raise Exception ( 'ksub_random2(): Fatal error!' )

  a = np.zeros ( k, dtype = np.int32 )

  if ( k == 0 ):
    return a

  need = k
  have = 0

  available = n
  candidate = 0

  while ( True ):

    candidate = candidate + 1

    r = rng.random ( )

    if ( available * r <= need ):

      need = need - 1;
      a[have] = candidate
      have = have + 1

      if ( need <= 0 ):
        break

    available = available - 1

  return a

def urn_50_50_test ( rng ):

#*****************************************************************************80
#
## urn_50_50_test() tests urn_sample() with 50 white and 50 black balls.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'urn_50_50_test():' )
  print ( '  urn_sample() simulates drawing balls from an urn.' )
  print ( '  Here, we start with 50 white and 50 black balls:' )

  marble_num = 100
  draw_num = 10
  color_num = 2
  color_count = np.array ( [ 50, 50 ] )

  draws = 10000
  draw_color = np.zeros ( [ color_num, draws ] )
  for j in range ( 0, draws ):
    draw_color[:,j] = urn_sample ( marble_num, draw_num, \
      color_num, color_count, rng )

  print ( '' )
  print ( '  ', marble_num, 'marbles in urn' )
  print ( '  ', draw_num, 'are drawn without replacement' )
  print ( '  ', draws, 'repetitions of the draw' )
  print ( '  ', color_num, 'colors, distributed as follows:' )
  print ( color_count )
  print ( '' )
#
#  We have to shift the data left half a step so that the
#  histograms and density function match up.
#
  draw_color = draw_color - 0.5
#
#  Draw plot for 2 color case.
#
  plt.clf ( )
  plt.hist ( draw_color[0,:], density = True )
  wmax = np.max ( draw_color[0,:] )
  w = np.arange ( 0, wmax+1 )
  pw = urn_two_color_pdf ( w, draw_num, color_count )
  plt.plot ( w, pw, 'r-', linewidth = 3 )
  plt.grid ( 'True' )
  plt.xlabel ( 'Number of white marbles drawn' )
  plt.ylabel ( 'Probability' )
  plt.title ( 'PDF for number of white marbles' )
  filename = 'urn_50_50_test.png'
  plt.savefig ( filename )
  print ( 'Graphics saved as "' + filename + '"' )

  return

def urn_sample ( marble_num, draw_num, color_num, color_count, rng ):

#*****************************************************************************80
#
## urn_sample() simulates the sampling of an urn of colored marbles.
#
#  Discussion:
#
#    An urn contains a number of marbles of various colors.  
#
#    A random sample of marbles is drawn, and the colors are reported.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MARBLE_NUM, the number of marbles.
#
#    integer DRAW_NUM, the number of marbles to draw.
#
#    integer COLOR_NUM, the number of colors.
#
#    integer COLOR_COUNT(COLOR_NUM), the number of marbles of each color.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer DRAW_COLOR(COLOR_NUM), the number of marbles drawn,
#    of each color.
#
  import numpy as np
#
#  Randomly sample DRAW_NUM distinct integers from 1:MARBLE_NUM.
#
  y = ksub_random2 ( marble_num, draw_num, rng )
#
#  Ascending sort Y.
#
  y = np.sort ( y )
#
#  Assume the balls are colored in order.
#  Count the balls of each color by counting integers between limits.
#
  draw_color = np.zeros ( color_num )
  t = 0
  for i in range ( 0, color_num ):
    b = t
    t = t + color_count[i]
    draw_color[i] = ( ( b < y ) & ( y <= t ) ).sum()

  return draw_color

def urn_simulation_test ( ):

#*****************************************************************************80
#
## urn_simulation_test() tests urn_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'urn_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test urn_simulation().' )
 
  rng = default_rng ( )

  urn_50_50_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'urn_simulation_test():' )
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

def urn_two_color_pdf ( w, draw_num, color_count ):

#*****************************************************************************80
#
## urn_two_color_pdf() returns the PDF for a two-color urn problem.
#
#  Discussion:
#
#    Only the probabilities for the white marbles are returned.
#    The probabilities for the black marbles are obvious.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer W(W_NUM), the number of white marbles returned.
#
#    integer DRAW_NUM, the total number of marbles drawn.
#
#    integer COLOR_COUNT(2), the number of white marbles, and the
#    number of black balls.
#
#  Output:
#
#    real PW(W_NUM), PW(I) is the probability of drawing exactly W(I)
#    white marbles.
#
  from scipy.special import comb
  import numpy as np

  marble_num = np.sum ( color_count )
  w_num = w.shape[0]
  pw = np.zeros ( w_num )

  for i in range ( 0, w_num ):
    pw[i] = comb ( color_count[0], w[i] ) \
          * comb ( color_count[1], draw_num - w[i] ) \
          / comb ( marble_num, draw_num )

  return pw

if ( __name__ == "__main__" ):
  timestamp ( )
  urn_simulation_test ( )
  timestamp ( )

