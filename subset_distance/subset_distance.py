#! /usr/bin/env python3
#
def subset_distance_hamming ( t1, t2 ):

#*****************************************************************************80
#
## subset_distance_hamming() computes the Hamming distance between two sets.
#
#  Discussion:
#
#    The sets T1 and T2 are assumed to be subsets of a set of N elements.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer T1(M), T2(M), two subsets of the master set.
#    T1(I) = 0 if the I-th element is in the subset T1, and is
#    1 otherwise T2 is defined similarly.
#
#  Output:
#
#    integer DIST, the Hamming distance between T1 and T2,
#    defined as the number of elements of the master set which are
#    in either T1 or T2 but not both.
#
  import numpy as np

  dist = np.sum ( t1 != t2 )

  return dist

def subset_distance_histogram ( m, n ):

#*****************************************************************************80
#
## subset_distance_histogram() histograms subset distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the size of the master set.
#
#    integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    s1 = subset_sample ( m )
    s2 = subset_sample ( m )
    t[i] = subset_distance_hamming ( s1, s2 )

  bins = m + 1
  plt.hist ( t, bins = bins, rwidth = 0.95, \
    range = np.array ( [ 0, m ] ), density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  title_string = \
    'Hamming distance between random subsets of a ' + str ( m ) + '-set'
  plt.title ( title_string )

  return
 
def subset_distance_pdf ( m ):

#*****************************************************************************80
#
## subset_distance_pdf() plots the PDF for the subset distance problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import comb
  import matplotlib.pyplot as plt
  import numpy as np

  d = np.linspace ( 0.0, m, m + 1 )

  pdf = np.zeros ( m + 1, dtype = float )
  for k in range ( 0, m + 1 ):
    pdf[k] = comb ( m, k ) / 2.0**m

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  title_string =  \
    'PDF for distance of random subsets of a ' + str ( m ) + ' set'
  plt.title ( title_string )

  return

def subset_distance_stats ( m, n ):

#*****************************************************************************80
#
## subset_distance_stats() estimates subset distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the size of the master set.
#
#    integer N, the number of sample points to use.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random subsets of an M set.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    s1 = subset_sample ( m )
    s2 = subset_sample ( m )
    t[i] = subset_distance_hamming ( s1, s2 )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var
 
def subset_distance_test ( ):

#*****************************************************************************80
#
## subset_distance_test() tests subset_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test subset_distance().' )

  m = 16
  n = 10000
  mu, var = subset_distance_stats ( m, n )
  mu_exact = m / 2.0
  var_exact = m / 4.0
  print ( '' )
  print ( '  Master set size = ', m )
  print ( '  Using N = ' + str ( n ) + ' sample points,' )
  print ( '  Estimated mean distance = ', mu )
  print ( '  Exact mean distance     = ', mu_exact )
  print ( '  Estimated variance      = ', var )
  print ( '  Exact variance          = ', var_exact )

  m = 16
  n = 10000
  subset_distance_histogram ( m, n )
  filename = 'subset_distance_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  subset_distance_pdf ( m )
  filename = 'subset_distance_pdf.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  n = 10000
  subset_distance_histogram ( m, n )
  subset_distance_pdf ( m )
  filename = 'subset_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'subset_distance_test()::' )
  print ( '  Normal end of execution.' )

  return

def subset_sample ( m ):

#*****************************************************************************80
#
## subset_sample() returns a random subset of an M set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    Input, integer M, the size of the set.
#
#  Output:
#
#    integer S(M), defines the subset using 0 and 1 values.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  s = rng.integers ( low = 0, high = 1, size = m, endpoint = True )
 
  return s

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
  subset_distance_test ( )
  timestamp ( )

