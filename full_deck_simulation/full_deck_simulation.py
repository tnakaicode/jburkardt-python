#! /usr/bin/env python3
#
def coupon_complete_pdf ( type_num, box_num ):

#*****************************************************************************80
#
## coupon_complete_pdf() evaluates the Complete Coupon Collection PDF.
#
#  Discussion:
#
#    PDF(TYPE_NUM,BOX_NUM) is the probability that, given an inexhaustible 
#    supply of boxes, inside each of which there is one of TYPE_NUM distinct
#    coupons, which are uniformly distributed among the boxes, that it will 
#    require opening exactly BOX_NUM boxes to achieve at least one of each
#    kind of coupon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Herbert Wilf,
#    Some New Aspects of the Coupon Collector's Problem,
#    SIAM Review,
#    Volume 48, Number 3, September 2006, pages 549-565.
#
#  Input:
#
#    integer BOX_NUM, the number of boxes that had to be opened
#    in order to just get at least one of each coupon.
#    0 <= BOX_NUM.  If BOX_NUM < TYPE_NUM, then PDF is surely 0.
#
#    integer TYPE_NUM, the number of distinct coupons.
#    1 <= TYPE_NUM.
#
#  Output:
#
#    real PDF, the value of the PDF.
#

#
#  Nonsense cases.
#
  if ( box_num < 0 ):

    pdf = 0.0

  elif ( type_num < 1 ):

    pdf = 0.0
#
#  Degenerate but meaningful case.
#
  elif ( type_num == 1 ):

    if ( box_num == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0
#
#  Easy cases.
#
  elif ( box_num < type_num ):

    pdf = 0.0
#
#  General case.
#
  else:

    factor = 1.0
    for i in range ( 1, type_num + 1 ):
      factor = factor * float ( i ) / float ( type_num )

    for i in range ( type_num + 1, box_num + 1 ):
      factor = factor / float ( type_num )
    
    pdf = factor * stirling2_value ( box_num - 1, type_num - 1 )

  return pdf

def full_deck_expected ( card_num ):

#*****************************************************************************80
#
## full_deck_expected(): expected value of the general full deck problem.
#
#  Discussion:
#
#    The expected value, given a deck of N distinct cards, is n*Hn, where
#    Hn is the n-th harmonic number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Herbert Wilf,
#    Some New Aspects of the Coupon Collector's Problem,
#    SIAM Review,
#    Volume 48, Number 3, September 2006, pages 549-565.
#
#  Input:
#
#    integer card_num: the number of cards in the deck.
#
#  Output:
#
#    real ev: the expected number of cards that must be collected in order
#    to acquire at least one of every kind.
#
  ev = 0.0
  for i in range ( 1, card_num + 1 ):
    ev = ev + card_num / i

  return ev

def full_deck_expected_test ( ):

#*****************************************************************************80
#
## full_deck_expected_test() tests full_deck_expected().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'full_deck_expected_test():' )
  print ( '  full_deck_expected() reports the expected value for' )
  print ( '  the number of cards drawn before seeing every card,' )
  print ( '  for the general full deck process, using M cards.' )
  print ( '' )
  print ( '    M     Expected' )
  print ( '' )
  for m in [ 10, 52, 100, 365, 500 ]:
    ev = full_deck_expected ( m )
    print ( '  %3d  %10.2f' % ( m, ev ) )

  return

def full_deck_histogram ( n ):

#*****************************************************************************80
#
## full_deck_histogram() histograms full_deck statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of trials to make.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'full_deck_histogram():' )
  print ( '  Create a histogram of the full deck process.' )

  m = np.zeros ( n, dtype = int )
  for i in range ( 0, n ):
    deck = full_deck_try ( )
    m[i] = np.sum ( deck )

  plt.hist ( m, bins = 20, rwidth = 0.95, density = True )

  if ( False ):
    type_num = 52
    m_min = np.min ( m )
    m_max = np.max ( m )
    index = np.arange ( m_min, m_max + 1 )
    pdf = np.zeros ( m_max + 1 - m_min )
    for i in range ( m_min, m_max + 1 ):
      pdf[i] = coupon_complete_pdf ( type_num, i )
    plt.plt ( index, pdf, 'r-', linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<-- Number of draws -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Number of draws needed to see full deck' )
  filename = 'full_deck_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
 
  return

def full_deck_simulation_test ( ):

#*****************************************************************************80
#
## full_deck_simulation_test() tests full_deck_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'full_deck_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  full_deck_simulation() simulates a process in which' )
  print ( '  a card is drawn from a deck of 52 cards, then returned.' )
  print ( '  The process is continued until all cards have been seen' )
  print ( '  at least once.' )

  full_deck_try_test ( )
  full_deck_stats_test ( )
  full_deck_expected_test ( )
  n = 2000
  full_deck_histogram ( n )
  full_deck_variance_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'full_deck_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def full_deck_stats ( n ):

#*****************************************************************************80
#
## full_deck_stats() returns statistics for N tries of the full deck problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of times the process will be carried out.
#
#  Output:
#
#    integer tries_min, real tries_mean, integer tries_max, real tries_var: 
#    the minimum, average, maximum and variance for the number of cards drawn 
#    over all the processes.
#
  import numpy as np

  m = np.zeros ( n )
  for i in range ( 0, n ):
    deck = full_deck_try ( )
    m[i] = np.sum ( deck )

  tries_min = np.min ( m )
  tries_max = np.max ( m )
  tries_mean = np.mean ( m )
  tries_var = np.var ( m )

  return tries_min, tries_mean, tries_max, tries_var

def full_deck_stats_test ( ):

#*****************************************************************************80
#
## full_deck_stats_test() tests full_deck_stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'full_deck_stats_test():' )
  print ( '  full_deck_stats() reports statistics for N instances' )
  print ( '  of the 52-card full deck process.' )
  print ( '' )
  print ( '       N  Min    Mean  Max    Var' )
  print ( '' )

  for n in [ 10, 20, 50, 100, 1000, 10000 ]:
    tmin, tmean, tmax, tvar = full_deck_stats ( n )
    print ( '   %5d  %3d  %6.2f  %2d  %6.2f' % ( n, tmin, tmean, tmax, tvar ) )

  return

def full_deck_try ( ):

#*****************************************************************************80
#
## full_deck_try() returns all the cards drawn for a full deck problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer deck(52): the number of times each card was drawn.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng()

  deck = np.zeros ( 52, dtype = int )
  while ( True ):
    card = rng.integers ( low = 0, high = 52, endpoint = False )
    deck[card] = deck[card] + 1
    if ( np.all ( 0 < deck ) ):
      break

  return deck

def full_deck_try_test ( ):

#*****************************************************************************80
#
## full_deck_try_test() tests full_deck_try().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'full_deck_try_test():' )
  print ( '  full_deck_try() repeatedly draws a random card' )
  print ( '  from a 52-card deck until all cards have been seen' )
  print ( '  at least once.' )
  print ( '' )
  print ( '  Try  Min    Mean Max  Total' )
  print ( '' )

  for i in range ( 0, 10 ):
    cards = full_deck_try ( )
    print ( '   %2d  %3d  %6.2f  %2d   %4d' % \
      ( i, np.min ( cards ), np.mean ( cards ), np.max ( cards ), np.sum ( cards ) ) )

  return

def full_deck_variance ( card_num ):

#*****************************************************************************80
#
## full_deck_variance() returns the variance of the full deck problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Herbert Wilf,
#    Some New Aspects of the Coupon Collector's Problem,
#    SIAM Review,
#    Volume 48, Number 3, September 2006, pages 549-565.
#
#  Input:
#
#    integer card_num: the number of cards in the deck.
#
#  Output:
#
#    real variance: the variance in the number of cards that must be 
#    collected in order to acquire at least one of every kind.
#
  variance = 0.0
  for i in range ( 2, card_num + 1 ):
    variance = variance + ( i - 1 ) / ( card_num - i + 1 )**2

  variance = card_num * variance

  return variance

def full_deck_variance_test ( ):

#*****************************************************************************80
#
## full_deck_variance_test() tests full_deck_variance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'full_deck_variance_test():' )
  print ( '  full_deck_variance() reports the variance for' )
  print ( '  the number of cards drawn in the 52-card full deck process.' )
  print ( '' )
  print ( '    N     Variance' )
  print ( '' )
  for n in [ 10, 52, 100, 365, 500 ]:
    variance = full_deck_variance ( n )
    print ( '  %3d  %10.2f' % ( n, variance ) )

  return

def stirling2_value ( n, m ):

#*****************************************************************************80
#
## stirling2_value() computes a Stirling number of the second kind.
#
#  Discussion:
#
#    S2(N,M) represents the number of distinct partitions of N elements
#    into M nonempty sets.  For a fixed N, the sum of the Stirling
#    numbers S2(N,M) is represented by B(N), called "Bell's number",
#    and represents the number of distinct partitions of N elements.
#
#    For example, with 4 objects, there are:
#
#    1 partition into 1 set:
#
#      (A,B,C,D)
#
#    7 partitions into 2 sets:
#
#      (A,B,C) (D)
#      (A,B,D) (C)
#      (A,C,D) (B)
#      (A) (B,C,D)
#      (A,B) (C,D)
#      (A,C) (B,D)
#      (A,D) (B,C)
#
#    6 partitions into 3 sets:
#
#      (A,B) (C) (D)
#      (A) (B,C) (D)
#      (A) (B) (C,D)
#      (A,C) (B) (D)
#      (A,D) (B) (C)
#      (A) (B,D) (C)
#
#    1 partition into 4 sets:
#
#      (A) (B) (C) (D)
#
#    So S2(4,1) = 1, S2(4,2) = 7, S2(4,3) = 6, S2(4,4) = 1, and B(4) = 15.
#
#
#  First terms:
#
#    N/M: 1    2    3    4    5    6    7    8
#
#    1    1    0    0    0    0    0    0    0
#    2    1    1    0    0    0    0    0    0
#    3    1    3    1    0    0    0    0    0
#    4    1    7    6    1    0    0    0    0
#    5    1   15   25   10    1    0    0    0
#    6    1   31   90   65   15    1    0    0
#    7    1   63  301  350  140   21    1    0
#    8    1  127  966 1701 1050  266   28    1
#
#  Recursion:
#
#    S2(N,1) = 1 for all N.
#    S2(I,I) = 1 for all I.
#    S2(I,J) = 0 if I < J.
#
#    S2(N,M) = M * S2(N-1,M) + S2(N-1,M-1)
#
#  Properties:
#
#    sum ( 1 <= K <= M ) S2(I,K) * S1(K,J) = Delta(I,J)
#
#    X^N = sum ( 0 <= K <= N ) S2(N,K) X_K
#    where X_K is the falling factorial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the first index.
#
#    integer M, the second index.
#
#  Output:
#
#    integer VALUE, the Stirling number S[N-1,M-1].
#
  import numpy as np

  s2 = np.zeros ( ( n, m ) )

  if ( n <= 0 ):
    return s2

  if ( m <= 0 ):
    return s2

  s2[0,0] = 1
  for j in range ( 1, m ):
    s2[0,j] = 0

  for i in range ( 1, n ):

    s2[i,0] = 1

    for j in range ( 1, m ):
      s2[i,j] = ( j + 1 ) * s2[i-1,j] + s2[i-1,j-1]

  return s2[n-1,m-1]

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
  full_deck_simulation_test ( )
  timestamp ( )

