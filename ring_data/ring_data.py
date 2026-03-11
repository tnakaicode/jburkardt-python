#! /usr/bin/env python3
#
def ring_data_test ( ):

#*****************************************************************************80
#
## ring_data_test() tests ring_data().
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
  print ( 'ring_data_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  ring_data() creates, plots, and saves ring data.' )

  ring_num = 3
  ring_pop = np.array ( [ 40, 60, 100 ] )
  ring_rad1 = np.array ( [ 1.0, 6.0, 9.0 ] )
  ring_rad2 = np.array ( [ 3.0, 7.0, 10.0 ] )
  
  ring_input_print ( ring_num, ring_pop, ring_rad1, ring_rad2 )

  m, p, ident = ring_data_generate ( ring_num, ring_pop, ring_rad1, ring_rad2 )

  ring_data_print ( m, p, ident )

  ring_data_plot ( m, p, ident, ring_num )

  ring_data_write ( m, p, ident, 'ring_data.dat' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ring_data_test():' )
  print ( '  Normal end of execution.' )

  return

def annulus_sample ( pc, r1, r2, n ):

#*****************************************************************************80
#
## annulus_sample() samples a circular annulus.
#
#  Discussion:
#
#    A circular annulus with center PC, inner radius R1 and
#    outer radius R2, is the set of points P so that
#
#      R1^2 <= (P(1)-PC(1))^2 + (P(2)-PC(2))^2 <= R2^2
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
#  Reference:
#
#    Peter Shirley,
#    Nonuniform Random Point Sets Via Warping,
#    Graphics Gems, Volume III,
#    edited by David Kirk,
#    AP Professional, 1992, 
#    ISBN: 0122861663,
#    LC: T385.G6973.
#
#  Input:
#
#    real PC(2), the center.
#
#    real R1, R2, the inner and outer radii.
#
#    integer N, the number of points to generate.
#
#  Output:
#
#    real P(N,2), sample points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  u = rng.random ( n )

  theta = u * 2.0 * np.pi

  v = rng.random ( n )

  r = np.sqrt ( ( 1.0 - v ) * r1 * r1 + v * r2 * r2 )

  p = np.zeros ( [ n, 2 ] )
  p[:,0] = pc[0] + r * np.cos ( theta )
  p[:,1] = pc[1] + r * np.sin ( theta )

  return p

def ring_data_generate ( ring_num, ring_pop, ring_rad1, ring_rad2 ):

#*****************************************************************************80
#
## ring_data_generate() generates ring data.
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
#    integer RING_NUM, the number of rings.
#
#    integer RING_POP(RING_NUM), the number of points to be created
#    in each ring.
#
#    real RING_RAD1(RING_NUM), RING_RAD2(RING_NUM), the inner and
#    outer radius of each ring.
#
#  Output:
#
#    integer M, the total number of points.
#
#    real P[M,2], the coordinates of the points.
#
#    integer IDENT(M), the index of the ring to which each point belongs.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  pc = np.zeros ( 2 )

  m = np.sum ( ring_pop )
  p = np.zeros ( [ m, 2 ] )
  ident = np.zeros ( m, dtype = int )

  m2 = 0

  for i in range ( 0, ring_num ):
    m1 = m2
    m2 = m1 + ring_pop[i]
    p[m1:m2,:] = annulus_sample ( pc, ring_rad1[i], ring_rad2[i], ring_pop[i] )
    ident[m1:m2] = i
#
#  Permute the data.
#
  perm = perm0_random ( m, rng )
  p[:,0] = p[perm,0]
  p[:,1] = p[perm,1]
  ident = ident[perm]

  return m, p, ident

def perm0_random ( n, rng ):

#*****************************************************************************80
#
## perm0_random() selects a random permutation of N objects.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer P[N], a permutation of the digits 0 through N-1.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p[i] = i

  for i in range ( 0, n - 1 ):
    j = rng.integers ( low = i, high = n, endpoint = False )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def ring_data_plot ( m, p, ident, ring_num ):

#*****************************************************************************80
#
## ring_data_plot() plots the ring data.
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
#    integer M, the total number of points.
#
#    real P[M,2], the coordinates of the points.
#
#    integer IDENT(M), the index of the ring to which each point belongs.
#
#    integer ring_num: the number of rings.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt

  rng = default_rng ( )

  ring_color = rng.random ( [ ring_num, 3 ] )

  plt.clf ( )
  for i in range ( 0, m ):
    plt.plot ( p[i,0], p[i,1], '.', \
      markersize = 20, \
      markerfacecolor = ring_color[ident[i],:] )
  plt.axis ( 'equal' )
  plt.title ( 'ring data' )
  plt.grid  ( True )

  filename = 'ring_data.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def ring_data_print ( m, p, ident ):

#*****************************************************************************80
#
## ring_data_print() prints ring data.
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
#    integer M, the total number of points.
#
#    real P[M,2], the coordinates of the points.
#
#    integer IDENT(M), the index of the ring to which each point belongs.
#
  import numpy as np

  print ( '' )
  print ( 'RING_DATA_PRINT:' )
  print ( '' )
  print ( '     I    ID           R           X           Y' )
  print ( '' )

  for i in range ( 0, m ):
    r = np.sqrt ( p[i,0]**2 + p[i,1]**2 ) 
    print ( '  %4d  %4d  %10.4f  %10.4f  %10.4f' \
      % ( i, ident[i], r, p[i,0], p[i,1] ) )

  return

def ring_data_write ( m, p, ident, filename ):

#*****************************************************************************80
#
## ring_data_write() writes the ring data to a file.
#
#  Discussion:
#
#    Each data line records x, y, id.
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
#    integer M, the number of points.
#
#    real P(M,2), the ring data.
#
#    integer IDENT(M), an identifier for the ring.
#
#    string FILENAME, the output filename.
#

#
#  Open the file.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    s = ( '  %g' % ( p[i,0] ) )
    output.write ( s )
    s = ( '  %g' % ( p[i,1] ) )
    output.write ( s )
    s = ( '  %d\n' % ( ident[i] ) )
    output.write ( s )
#
#  Close the file.
#
  output.close ( )

  return

def ring_input_print ( ring_num, ring_pop, ring_rad1, ring_rad2 ):

#*****************************************************************************80
#
## ring_input_print() prints ring input data.
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
#    integer RING_NUM, the number of rings.
#
#    integer RING_POP(RING_NUM), the number of points to be created
#    in each ring.
#
#    real RING_RAD1(RING_NUM), RING_RAD2(RING_NUM), the inner and
#    outer radius of each ring.
#
  print ( '' )
  print ( 'RING_INPUT_PRINT:' )
  print ( '' )
  print ( '     I   Pop        Rad1        Rad2' )
  print ( '' )

  for i in range ( 0, ring_num ):
    print ( '  %4d  %4d  %10.4f  %10.4f' \
      % ( i, ring_pop[i], ring_rad1[i], ring_rad2[i] ) )

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
  ring_data_test ( )
  timestamp ( )


