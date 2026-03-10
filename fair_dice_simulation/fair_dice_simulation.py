#! /usr/bin/env python3
#
def fair_dice_simulation ( n, filename ):

#*****************************************************************************80
#
## fair_dice_simulation() simulates N throws of two fair dice.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of times the dice are thrown.
#
#    string filename: the name of the graphics file to be created.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'fair_dice_simulation():' )
  print ( '  Simulate', n, 'throws of a pair of fair dice.' )
#
#  PDF is the probability density function for the probability of the
#  results 1 through 12, after rolling two dice.
#
  pdf = np.array ( [ 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 ] ) / 36
#
#  CDF(X) is the probability of rolling the value X or less.
#
  cdf = np.cumsum ( pdf )
#
#  Now we simulate rolling the dice N times.
#  SCORE(I) will hold the result we got on the I-th roll.
#
  score = np.zeros ( n )
#
#  Each value of R is a random number between 0 and 1.
#
  r = rng.random ( n )
#
#  Each R corresponds to the result X for which CDF(X-1) < R <= CDF(X).
#
#  WHERE is a vector the same shape as R, containing a 1 for those
#  entries in R whose probability corresponds to a roll of X.
#
#  The entries of WHERE with a 1 in them will now set the corresponding
#  entries of SCORE to X.
#
  for x in range ( 2, 13 ):
    where = ( ( cdf[x-2] < r ) & ( r <= cdf[x-1] ) )
    score[where] = x
#
#  Compute the frequency of each score X.
#
#  MATCH is a vector of those indices of SCORE which are equal to X.
#
#  The frequency of the result X is the same as the number of entries
#  in MATCH.
#
  freq = np.zeros ( 11 )
  for x in range ( 2, 13 ):
    match = ( score == x )
    freq[x-2] = np.sum ( match )
#
#  The estimated probability density is the number of occurences of
#  the given roll divided by the number of trials.
#
  pdf_est = freq / n
#
#  Plot the estimated PDF versus the PDF
#
  x = np.linspace ( 2, 12, 11 )

  plt.clf ( )
  plt.bar ( x-0.2, pdf[1:], 0.4 )
  plt.bar ( x+0.2, pdf_est, 0.4 )
  plt.grid ( True )
  s = 'Exact (blue) and estimated (red) PDF, N =' + str ( n )
  plt.title ( s )
  plt.xlabel ( 'Score' )
  plt.ylabel ( 'Probability' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def fair_dice_simulation_test ( ):

#*****************************************************************************80
#
## fair_dice_simulation_test() tests fair_dice_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fair_dice_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test fair_dice_simulation().' )

  n = 1000
  filename = 'fair_dice_' + str ( n ) + '.png'
  fair_dice_simulation ( n, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'fair_dice_simulation_test():' )
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
  fair_dice_simulation_test ( )
  timestamp ( )


