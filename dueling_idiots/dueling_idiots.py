#! /usr/bin/env python3
#
def dueling_idiots_test ( ):

#*****************************************************************************80
#
## dueling_idiots_test() tests dueling_idiots().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB code by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'dueling_idiots_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test dueling_idiots().' )

  rng = default_rng ( )

  N = 100
  ash ( N )

  for n in [ 10, 100, 1000, 10000, 100000 ]:
   balls ( n )

  baseball ( )

  for N in [ 3, 4, 5, 6 ]:
    for q in [ 0.0, 0.3, 0.9 ]:
      biased ( N, q, rng )

  print ( '' )
  n = 6
  for k in range ( 0, 4 ):
    print ( 'binomial: ', n, 'choose', k, '=', binomial ( n, k ) )

  n = 200
  brownian ( 200 )

  n = 5
  bulb ( n )

  n = 10
  bulb ( n )

  casino ( )

  cc ( rng )

  chess ( 6, 0.1 )

  chess ( 6, 0.0 )

  correlation ( 5, rng )

# cpm ( )

  n = 1000
  esim ( n )
  n = 10000
  esim ( n )

  n = 100000
  flycircle ( n, rng )

  n = 100000
  flysquare ( n, rng )

  trial_num = 1000
  gas ( trial_num, rng )

  n = 10000
  generator ( n, rng )

  idiots1 ( rng )

  idiots2 ( )

  n = 10000
  p = 0.40
  kids ( n, p, rng )

  markov ( )

  coin_num = 10
  people_num = 2
  match ( coin_num, people_num )
  coin_num = 10
  people_num = 3
  match ( coin_num, people_num )
  coin_num = 10
  people_num = 4
  match ( coin_num, people_num )
  coin_num = 50
  people_num = 2
  match ( coin_num, people_num )

  monty ( rng )

  needle ( )

  n = 10000
  normal ( n )

  for N in range ( 2, 8 ):
    odd ( N, rng )

  onedwalk ( )

  n = 10000
  onewaytodoit ( n, rng )

  onion ( rng )

  a = 100.0
  paradox ( a )

  paths ( rng )

# pert ( 50 )

  n = 10000
  pisim ( n, rng )

  nmax = 100
  radar ( nmax, 0.1, 0.1, 0.15 )

  m = 10000
  randomsum ( m, rng )

  spider ( )

  stirling1 ( )

  stirling2 ( )

  stirling3 ( )

  theory ( )

  thief ( rng )

  for ps, N in [ [ 0.2, 13 ], [ 0.2, 40 ], [ 0.05, 40 ] ]:
    tub ( ps, N )

  underdog1 ( )

  underdog2 ( )

  n = 2
  xplusy ( n, rng )
  n = 6
  xplusy ( n, rng )

  xpowery ( )

  n = 20000
  xyhisto ( n, rng )

  n = 10000
  z ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'dueling_idiots_test():' )
  print ( '  Normal end of execution.' )

  return

def ash ( N ):

#*****************************************************************************80
#
## ash() is a special case of chess() using P = Q = 1/3.
#
#  Discussion:
#
#    A champ plays a chump at N games of chess.
#    P is the probability that an individual game is won by the champ.
#    Q is the probability that an individual game ends in a tie.
#
#  Example:
#
#    For N = 100, the probablity of a tied match is 0.04877.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, the number of games in the match.
#
  import numpy as np

  print ( '' )
  print ( 'ash():' )
  print ( '  A champ plays a chump at', N, 'games of chess.' )
  print ( '  P is the probability an individual game is won by the champ.' )
  print ( '  Q is the probability an individual game ends in a tie.' )
  print ( '  For this code, P = Q = 1/3.' )

  q = 1.0 / 3.0
  p = 1.0 / 3.0
  g = ( 1.0 - p - q ) * p
  RZ = np.zeros ( N )

  C = np.zeros ( [ N, N ] )
  for k in range ( 1, N + 1 ):
    C[k-1,k-1] = p ** k

  for n in range ( 1, N + 1 ):

    if ( ( n % 2 ) == 0 ):

      for d in range ( 0, n + 1, 2 ):
        top = ( n + d ) // 2
        bottom = ( n - d ) // 2
        I = binomial ( n, bottom ) * binomial ( top, bottom )
        I = I * ( g ** bottom ) * ( q ** d )
        RZ[n-1] = RZ[n-1] + I

    else:

      for d in range ( 1, n + 1, 2 ):
        top = ( n + d ) // 2
        bottom = ( n - d ) // 2
        I = binomial ( n, bottom ) * binomial ( top, bottom )
        I = I * ( g ** bottom ) * ( q ** d )
        RZ[n-1] = RZ[n-1] + I

  g = 1.0 - p - q

  for c in range ( 2, N + 1 ):

    k = 1
    n = c

    while ( n <= N ):

      C[k-1,n-1] = C[k-1,n-2] * q + C[k,n-2] * g
      if ( k == 1 ):
        C[k-1,n-1] = C[k-1,n-1] + RZ[n-2] * p
      else:
        C[k-1,n-1] = C[k-1,n-1] + C[k-2,n-2] * p

      k = k + 1
      n = n + 1

  total = np.sum ( C[:,N-1] )

  print ( '' )
  print ( '  Probability of a tie is           ', RZ[N-1] )
  print ( '  Probability the champ wins is     ', total )
  print ( '  Probability the challenger wins is', 1.0 - RZ[N-1] - total )

  return
 
def balls ( n ):

#*****************************************************************************80
#
## balls() simulates a problem involving numbered balls in an urn.
#
#  Discussion:
#
#    An urn contains N numbered balls.  A ball is drawn repeatedly from the
#    urn, examined, and replaced.  This file calculates:
#    (1) E(n), the average number of drawings (with replacement) of numbered 
#        balls before a repetition occurs
#    (2) T, the largest number of drawings that still allows
#        the probability there is NOT a repetition is still greater than 1/2.
#
#  Example:
#
#          N      E(N)     T
#
#         10    3.6602     4
#        100   12.2100    12
#      1,000   39.3032    37
#     10,000  124.9991   118
#    100,000  395.9997   372
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, the number of balls in the urn.
#
  print ( '' )
  print ( 'balls():' )
  print ( '  An urn contains', n, 'numbered balls.' )
  print ( '  A ball is drawn repeatedly from the' )
  print ( '  urn, examined, and replaced.  This file calculates:' )
  print ( '  (1) E(n), the average number of drawings (with replacement) of numbered ' )
  print ( '    balls before a repetition occurs' )
  print ( '  (2) T, the largest number of drawings that still allows' )
  print ( '    the probability there is NOT a repetition is still greater than 1/2.' )

  F = 1 / n
  E = F
  j = 1
  NF = F * ( n - j ) / n

  while ( 0 < NF ):
    F = NF
    j = j + 1
    NF = F * ( n - j ) / n
    E = E + j * j * F

  print ( '' )
  print ( '  E =', E )

  j = 0
  Prod = 1
  while ( 0.5 < Prod ):
    Prod = Prod * ( ( n - j ) / n )
    j = j + 1

  T = j - 1
  print ( '  T = ', T )

  return

def baseball ( ):

#*****************************************************************************80
#
## baseball() models a baseball season.
#
#  Discussion:
#
#    This function calculates and plots (as a function of p) the ratio
#    of the probabilities of a team winning at least 81p games out of
#    81 games to the probability of winning at least 162p games out
#    of 162 games, where p is the probability of winning any individual game.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'baseball()' )
  print ( '  Calculate and plot (as a function of p) the ratio' )
  print ( '  of the probabilities of a team winning at least 81p games out of' )
  print ( '  81 games to the probability of winning at least 162p games out' )
  print ( '  of 162 games, where p is the probability of winning any individual game.' )
  print ( '' )

  res = 0.001

  p = np.linspace ( 0.001, 0.999, 999 )
  ratio = np.zeros ( 999 )

  for i in range ( 0, 999 ):

    s81 = int ( np.ceil ( 81 * p[i] ) )
    s162 = int ( np.ceil ( 162 * p[i] ) )
#
#  Numerator sum.
#
    sumnum = 0.0
    for k in range ( s81, 82 ):
      bc = binomial ( 81, k )
      sumnum = sumnum + bc * ( p[i] ** k ) * ( ( 1.0 - p[i] ) ** ( 81.0 - k ) )
#
#  Denominator sum.
#
    sumden = 0.0
    for k in range ( s162, 163 ):
      bc = binomial ( 162, k )
      sumden = sumden + bc * ( p[i] ** k ) * ( ( 1.0 - p[i] ) ** ( 162.0 - k ) )

    ratio[i] = sumnum / sumden
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( p, ratio )
  plt.grid ( True )
  plt.title ( 'Ratio of Probabilities of Winning At Least np Games Out of n, n=81/np=162' )
  plt.xlabel ( 'p, probability of winning any individual game' )
  plt.ylabel ( 'ratio' )
  filename = 'baseball.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return
             
def biased ( N, q, rng ):

#*****************************************************************************80
#
## biased() plays odd-man-out with a biased coin.
#
#  Discussion:
#
#    A game of odd man out is played, in which N people each flip a coin.
#    If one person's coin doesn't match all the others, that person 
#    is the odd man out and the game is over.
#
#    In this version, N-1 people have fair coins, and one has a biased coin
#    whose probability of heads is Q.
#
#    Estimate the average number of games played.
#
#  Example:
#
#    N    Q  Games
#
#    3  0.0  1.336
#    3  0.3  1.316
#    3  0.9  1.321
#
#    4  0.0  2.064
#    4  0.3  2.032
#    4  0.9  2.051
#
#    5  0.0  3.15
#    5  0.3  3.167
#    5  0.9  3.242
#
#    6  0.0  5.323
#    6  0.3  5.210
#    6  0.9  5.190
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, the number of people.
#
#    real Q, the biased probability of one coin.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'biased():' )
  print ( '  A game of odd man out is played:', N, 'people each flip a coin.' )
  print ( '  If one person\'s coin does not match all the others, that person ' )
  print ( '  is the odd man out and the game is over.' )
  print ( '  In this version, N-1 people have fair coins, and one has a biased coin' )
  print ( '  whose probability of heads is Q = ', q )
  print ( '  Estimate the average number of games played.' )

  duration = np.zeros ( 100 )

  for game in range ( 0, 1000 ):

    gameover = 0
    flip = 1

    while ( gameover == 0 ):

      s = 0

      fair = N - 1

      for n in range ( 0, fair ):
        coin = rng.random ( )
        if ( coin < 0.5 ):
          s = s + 1

      coin = rng.random ( )

      if ( coin < q ):
        s = s + 1

      if ( s == 1 or s == N - 1 ):
        gameover = 1
      else:
        flip = flip + 1

    duration[flip-1] = duration[flip-1] + 1

  average = 0.0
  for i in range ( 0, 100 ):
    average = average + ( i + 1 ) * duration[i]
  average = average / 1000

  print ( '' )
  print ( '  Average number of games =', average )
  print ( '  Theoretical number      =', 2 ** ( N - 1 ) / N )

  return

def binomial ( top, bottom ):

#*****************************************************************************80
#
## binomial() computes the binomial coefficient N-choose-K.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer TOP, BOTTOM, the values of N and K.
#
  from math import factorial

  if ( top == 0 or top == 1 ):
    num = 1
  else:
    num = factorial ( top )

  if ( bottom == 0 or bottom == 1 ):
    den1 = 1
  else:
    den1 = factorial ( bottom )

  test = top - bottom
  if ( test == 0 or test == 1  ):
    den2 = 1
  else:
    den2 = factorial ( test )
 
  bc = ( num / den1 ) / den2

  return bc

def brownian ( n ):

#*****************************************************************************80
#
## brownian() models a Brownian walk in two dimensions.
#
#  Discussion:
#
#    This code simulates Brownian motion, a random walk by a particle
#    suspended in a fluid and being hit by molecules.  At successive
#    increments of time, the particle performs independent motions of random
#    length, uniform from -1 to 1, in arbitrary units, in both the x and the y
#    directions.  The walk duration, that is, the total number of steps, 
#    where a step is a delta-x and a delta-y pair, is defined by the user. 
#    A walk always starts at the origin.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, the walk duration, in steps.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'brownian()' )
  print ( '  Simulate Brownian motion, a random walk by a particle' )
  print ( '  suspended in a fluid and being hit by molecules.' )
  print ( '' )

  xpos = np.zeros ( n )
  ypos = np.zeros ( n )
  for i in range ( 1, n ):
    deltax = np.random.uniform ( -1.0, +1.0 )
    deltay = np.random.uniform ( -1.0, +1.0 )
    xpos[i] = xpos[i-1] + deltax
    ypos[i] = ypos[i-1] + deltay
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( xpos, ypos )
  plt.grid ( True )
  plt.xlabel ( 'x direction' )
  plt.ylabel ( 'y direction' )
  plt.title ( 'Two-Dimensional Brownian Motion' )
  filename = 'brownian.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def bulb ( n ):

#*****************************************************************************80
#
## bulb() analyzes the light bulb problem.
#
#  Discussion:
#
#    This code calculates and plots the probability of a bulb,
#    wired in series/parallel with sheets of switches, glowing.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, the number of switches.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bulb():' )
  print ( '  Calculate and plot the probability of a bulb glowing,' )
  print ( '  wired in series/parallel with ', n, 'sheets of switches.' )

  r = np.linspace ( 0.005, 1.0, 200 )

  p1 = np.zeros ( 200 )
  p2 = np.zeros ( 200 )

  for i in range ( 0, 200 ):
    p1[i] = ( 1.0 - ( 1.0 - r[i] ** n ) ** n ) ** n
    p2[i] = 1.0 - ( ( 1.0 - r[i] ** n ) ** ( n * n ) )
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( r, p1, '-' )
  plt.plot ( r, p2, '.' )
  plt.grid ( True )
  plt.title ( 'Solid Line for Series Sheets, Dots for Parallel Sheets' )
  plt.xlabel ( 'probability, p, an individual switch is closed' )
  plt.ylabel ( 'probability bulb glows, P(10,p)' )
  filename = 'bulb.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def casino ( ):

#*****************************************************************************80
#
## casino() simulates the game "Chuck-a-Luck".
#
#  Discussion:
#
#    This function simulates 10,000 games of "Chuck-a-Luck" and
#    calculates the average winnings. That is, you bet $1 each
#    game and the winnings (W) are how much MORE money you have
#    over and above the $10,000 betting money. The average
#    winnings are, of course, W/10,000.
#
#    Three dice are rolled, and you can bet on any number between
#    1 and 6.  If one die comes up with your number, you win as
#    much as you bet.  If two or three dice come up with your number,
#    you win twice or three times your bet.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import numpy as np

  print ( '' )
  print ( 'casino():' )
  print ( '  Simulate 10,000 games of "Chuck-a-Luck" and' )
  print ( '  calculate the average winnings. That is, you bet $1 each' )
  print ( '  and the winnings (W) are how much MORE money you have' )
  print ( '  over and above the $10,000 betting money. The average' )
  print ( '  winnings are, of course, W/10,000.' )
  print ( '' )
  print ( '  Three dice are rolled, and you can bet on any number between' )
  print ( '  1 and 6.  If one die comes up with your number, you win as' )
  print ( '  much as you bet.  If two or three dice come up with your number,' )
  print ( '  you win twice or three times your bet.' )

  W = 0

  for games in range ( 0, 100000 ):

    bet = np.random.randint ( low = 1, high = 7 )

    die1 = np.random.randint ( low = 1, high = 7 )
    die2 = np.random.randint ( low = 1, high = 7 )
    die3 = np.random.randint ( low = 1, high = 7 )

    matches = 0

    if ( bet == die1 ):
      matches = matches + 1
 
    if ( bet == die2 ):
      matches = matches + 1

    if ( bet == die3 ):
      matches = matches + 1

    if ( matches == 0 ):
      W = W - 1
    else:
      W = W + matches

  W = W / 100000

  print ( '' )
  print ( '  Average winnings per game is', W, 'dollars.' )

  return
            
def cc ( rng ):

#*****************************************************************************80
#
## cc() computes the correlation between elements of a random vector.
#
#  Discussion:
#
#    This function generates a random vector, X, of length
#    20,009 and then calculates the correlation coefficient
#    X(n) and X(n+j) for j = 0,1,2,...,9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'cc():' )
  print ( '  Generate a random vector, X, of length' )
  print ( '  20,009 and calculate the correlation coefficient' )
  print ( '  X(n) and X(n+j) for j = 0,1,2,...,9.' )

  n = 20000
  x = rng.random ( size = n + 9 )

  print ( '' )
  print ( '  J  Cor(X(i),X(i+j))' )
  print ( '' )

  for j in range ( 0, 10 ):
    summation = np.dot ( x[0:n], x[j:n+j] )
    coefficient = ( 12 * summation / n ) - 3.0
    print ( '  %2d  %g' % ( j, coefficient ) )

  return

def chess ( N, q ):

#*****************************************************************************80
#
## chess() simulates an N-game chess tournament.
#
#  Discussion:
#
#    This function computes the probabilities, in an N-game chess
#    match, of the match ending in a tie, in a win for the champ, or
#    in a win for the challenger. The probability the champ wins an
#    individual game is p, and the probability an individual
#    game ends in a tie is q.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, number of games in the match.
#
#    real Q, probability of a drawn game.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'chess():' )
  print ( '  Compute the probabilities, in an N-game chess' )
  print ( '  match, of the match ending in a tie, in a win for the champ, or' )
  print ( '  in a win for the challenger. The probability the champ wins an' )
  print ( '  individual game is p, and the probability an individual' )
  print ( '  game ends in a tie is q.' )
  print ( '' )

  answer = np.zeros ( [ 3, 100 ] )
  p = np.linspace ( 0.01, 1.0 - q, 100 )

  for i in range ( 0, 100 ):

    g = ( 1.0 - p[i] - q ) * p[i]
    RZ = np.zeros ( N )         
    C = np.zeros ( [ N, N ] )
    for k in range ( 1, N + 1 ):
      C[k-1,k-1] = p[i] ** k

    for n in range ( 1, N + 1 ):

      if ( ( n % 2 ) == 0 ):

        for d in range ( 0, n + 1, 2 ):
          top = ( n + d ) // 2
          bottom = ( n - d ) // 2
          I = binomial ( n, bottom ) * binomial ( top, bottom )
          I = I * ( g ** bottom ) * ( q ** d )
          RZ[n-1] = RZ[n-1] + I

      else:

        for d in range ( 1, n + 1, 2 ):
          top = ( n + d ) // 2
          bottom = ( n - d ) // 2
          I = binomial ( n, bottom ) * binomial ( top, bottom )
          I = I * ( g ** bottom ) * ( q ** d )
          RZ[n-1] = RZ[n-1] + I

    g = 1.0 - p[i] - q

    for c in range ( 2, N + 1 ):

      k = 1
      n = c

      while ( n <= N ):

        C[k-1,n-1] = C[k-1,n-2] * q + C[k,n-2] * g
        if ( k == 1 ):
          C[k-1,n-1] = C[k-1,n-1] + RZ[n-2] * p[i]
        else:
          C[k-1,n-1] = C[k-1,n-1] + C[k-2,n-2] * p[i]

        k = k + 1
        n = n + 1

    SUM = np.sum ( C[:,N-1] )

    Q = np.round ( 100 * ( 1.0 - q ) )

    if ( i <= Q ):
      answer[0,1] = RZ[N-1]
      answer[1,i] = SUM
      answer[2,i] = 1 - answer[0,i] - answer[1,i]
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( p, answer[0,:], 'bh' )
  plt.plot ( p, answer[1,:], 'g.' )
  plt.plot ( p, answer[2,:], 'r-' )
  plt.title ( 'Tie is hexagrams, Champ wins is dots, Challenger wins is solid' )
  plt.xlabel ( 'probability, p, of the Champ winning a game' )
  plt.ylabel ( 'probability' )
  plt.grid ( True )
  filename = 'chess.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def correlation ( j, rng ):

#*****************************************************************************80
#
## correlation() plots the scatter diagram of (X(I), X(I+J)).
#
#  Discussion:
#
#    Plotting X(I) versus X(I+J) can exhibit patterns if there is
#    correlation in the data.  If not, the scatter plot will be patternless.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer J, the offset to use in the correlation.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'correlation():' )
  print ( '  Plotting X(I) versus X(I+J) can exhibit patterns if there is' )
  print ( '  correlation in the data.  If not, the scatter plot will be patternless.' )

  n = 1000
  stop = n + j
  data = rng.random ( size = stop )

  x = np.zeros ( n )
  y = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = data[i]
    y[i] = data[i+j]
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( x, y, '.' )
  plt.xlabel ( 'j = 9' )
  plt.title ( '1000-Point Scatter Diagram for random data' )
  filename = 'correlation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def esim ( n ):

#*****************************************************************************80
#
## esim() estimates E by a binning process.
#
#  Discussion:
#
#    Sample N points in the unit interval.
#    Put them into N bins of equal width.
#    Let Z be the number of empty bins.
#    N/Z is an estimate of E. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of random values.
#
  import numpy as np

  print ( '' )
  print ( 'esim():' )
  print ( '  Sample n =', n, 'points in the unit interval.' )
  print ( '  Put them into n bins of equal width.' )
  print ( '  Let z be the number of empty bins.' )
  print ( '  n/z is an estimate of E. ' )

  bin = np.zeros ( n )
  x = np.random.randint ( low = 0, high = n, size = n )

  for j in range ( 0, n ):
    bin[x[j]] = bin[x[j]] + 1

  empty = np.sum ( bin == 0 )

  e_estimate = n / empty
  print ( '' )
  print ( '  Estimate for E = ', e_estimate )
  print ( '  Exact value =    ', np.e )

  return

def flycircle ( n, rng ):

#*****************************************************************************80
#
## flycircle() models two flies landing at random points in the unit circle.
#
#  Discussion:
#
#    Two flies land at random spots in the unit circle.
#    What is the probability they are more than 1 unit apart?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Paul Nahin
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'flycircle()' )
  print ( '  Two flies land at random spots in the unit circle.' )
  print ( '  What is the probability they are more than 1 unit apart?' )

  summation = 0
  radius = 1.0 / np.sqrt ( np.pi )
  factor = 2.0 * np.pi

  for fly in range ( 0, n ):
    r1 = radius * rng.random ( )
    a1 = factor * rng.random ( )
    r2 = radius * rng.random ( )
    a2 = factor * rng.random ( )
    x1 = r1 * np.cos ( a1 )
    y1 = r1 * np.sin ( a1 )
    x2 = r2 * np.cos ( a2 )
    y2 = r2 * np.sin ( a2 )
    distance2 = ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2
    if ( 1 <= distance2 ):
      summation = summation + 1

  summation = summation / n

  print ( '' )
  print ( '  Probability flies are more than 1 unit apart = ', summation )

  return

def flysquare ( n, rng ):

#*****************************************************************************80
#
## flysquare() simulates two flies landing at random in the unit square.
#
#  Discussion:
#
#    Two flies land at random spots in the unit square.
#    What is the probability they are more than 1 unit apart?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'flysquare():' )
  print ( '  Two flies land at random spots in the unit square.' )
  print ( '  What is the probability they are more than 1 unit apart?' )

  summation = 0

  for fly in range ( 0, n ):
    x1 = rng.random ( )
    y1 = rng.random ( )
    x2 = rng.random ( )
    y2 = rng.random ( )
    distance2 = ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2
    if ( 1.0 <= distance2 ):
      summation = summation + 1

  summation = summation / n

  print ( '' )
  print ( '  Probability flies are more than 1 unit apart =', summation )

  return

def gas ( trial_num, rng ):

#*****************************************************************************80
#
## gas() simulates the diffusion of a gas.
#
#  Discussion:
#
#    This code simulates the diffusion of gas molecules in a sealed
#    container by using the Ehrenfest ball exchange rules. The simulation
#    starts with n molecules (i.e., balls) of one type (i.e., black) on
#    one side of the container, and n more molecules of another type (i.e.,
#    white balls) on the other side. The two urns play the roles of the
#    two sides of the container. 
#
#    To simulate the ball (molecule)
#    movements, the program selects two random numbers from 0 to 1, which
#    are then compared to the current probabilities of selecting a black
#    ball from urn I and a white ball from urn II. If BOTH random numbers
#    are greater than these two probabilities then a white ball has been
#    selected from urn I and a black ball has been selected from urn II,
#    and so the number black balls in urn I is increased by one while the
#    number of white balls in urn II is increased by one. If BOTH random
#    numbers are less than or equal to these two probabilities then a
#    black ball has been selected from urn I and a white ball has been
#    selected from urn II and so the number of black balls in urn I is
#    decreased by one while the number of white balls in urn II is decreased
#    by one. If one of the random numbers is greater than its corresponding
#    probability while the other random number is less than its
#    corresponding probability, then no action is taken because then a
#    white (black) ball moves from urn I to urn II at the same time a white
#    (black) ball moves in the opposite direction. That is, there is no
#    net change. Then, the ball selection probabilities are recalculated and
#    another ball exchange is simulated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gas():' )
  print ( '  Simulate the diffusion of gas molecules in a sealed' )
  print ( '  container, using the Ehrenfest ball exchange rules.' )

  n = 50
  nb1 = n
  nw2 = n
  pb1 = nb1 / n
  pw2 = nw2 / n

  system = np.zeros ( trial_num )

  for trials in range ( 0, trial_num ):

    system[trials] = pb1
    ball1 = rng.random ( )
    ball2 = rng.random ( )

    if ( pb1 < ball1 and pw2 < ball2 ):
      nb1 = nb1 + 1
      nw2 = nw2 + 1
    elif ( ball1 <= pb1 and ball2 <= pw2 ):
      nb1 = nb1 - 1
      nw2 = nw2 - 1

    pb1 = nb1 / n
    pw2 = nw2 / n
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( system )
  plt.plot ( [0,1000], [0.5,0.5], 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( 'time steps' )
  plt.ylabel ( 'fraction of balls in urn 1 that are black' )
  plt.title ( 'The Ehrenfest Ball Exchange Process' )
  filename = 'gas.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def generator ( n, rng ):

#*****************************************************************************80
#
## generator() histograms a set of uniform random values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'generator():' )
  print ( '  Create a histogram of', n, 'uniform random values.' )
  
  y = rng.random ( size = n )
#
#  Graphics.
#
  plt.clf ( )
  plt.hist ( y, bins = 50 )
  plt.grid ( True )
  plt.title ( 'Uniform Random Numbers' )
  plt.xlabel ( '<-- 0 <= x <= 1 -->' )
  plt.ylabel ( 'Frequency' )
  filename = 'generator.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def idiots1 ( rng ):

#*****************************************************************************80
#
## idiots1() models a duel between two idiots.
#
#  Discussion:
#
#    A and B fight a duel, but they only have one gun, a six-shot revolver.
#    A will spin the cylinder and fire at B.
#    If the gun doesn't fire, then B will spin the cylinder and fire at A.
#    They continue to alternate until one of them is shot.
#    What is the probablity that A will win?
#    What is the average number of trigger pulls?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'idiots1():' )
  print ( '  A and B fight a duel, but they only have one gun, a six-shot revolver.' )
  print ( '  A will spin the cylinder and fire at B.' )
  print ( '  If the gun does not fire, then B will spin the cylinder and fire at A.' )
  print ( '  They continue to alternate until one of them is shot.' )
  print ( '  What is the probablity that A will win?' )
  print ( '  What is the average number of trigger pulls?' )
#
#  duel_num = total number of duels.
#
  duel_num = 10000
#
#  Assume no duel exceeds 100 trigger-pulls
#
  duration = np.zeros ( 100 )
  duration_max = 0    
  a = 0
  nd = 0
  tp = 0

  while ( nd < duel_num ):
#
#  A takes a shot.
#
    tp = tp + 1
    if ( rng.random ( ) <= 1 / 6 ):
      duration_max = max ( duration_max, tp )
      duration[tp-1] = duration[tp-1] + 1
      tp = 0
      a = a + 1
      nd = nd + 1
#
#  B takes a shot.
#
    else:
      tp = tp + 1
      if ( rng.random ( ) <= 1 / 6 ):
        duration_max = max ( duration_max, tp )
        duration[tp-1] = duration[tp-1] + 1
        tp = 0
        nd = nd + 1

  a = a / duel_num

  average = 0.0
  for k in range ( 1, duration_max + 1 ):
    average = average + k * duration[k-1]
  average = average / duel_num

  print ( '' )
  print ( '  The probability A wins is', a )
  print ( '  The average number of trigger-pulls/duel is', average )
  print ( '  Maximum number of trigger pulls was ', duration_max )
#
#  Graphics.
#
  x = np.linspace ( 1, duration_max, duration_max )

  plt.clf ( )
  plt.bar ( x, duration[0:duration_max] )
  plt.title ( 'Relative Frequency of the Number of Trigger-Pulls per Duel')
  plt.xlabel ( 'duration of duels, in units of trigger-pulls' )
  plt.ylabel ( 'number of duels' )
  plt.grid ( True )
  filename = 'idiots1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def idiots2 ( ):

#*****************************************************************************80
#
## idiots2() simulates a duel in which the N-th turn involves N shots.
#
#  Discussion:
#
#    Evaluate the theoretical probability that idiot A
#    wins the duel with idiot B, using the revised duelling rules
#    described in the problem assignment. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import numpy as np

  print ( '' )
  print ( 'idiots2():' )
  print ( '  Simulate a Russian-roulette duel between A and B.' )
  print ( '  A fires at B one time.' )
  print ( '  If A misses, B fires at A two times.' )
  print ( '  If B misses, A fires at B three times, and so on.' )
  print ( '  Each shot is preceded by spinning the revolver cylinder,' )
  print ( '  so there is a 1/6 chance that the revolver will fire.' )
  print ( '  Calculate the probability that A survives.' )

  S = 0
  T = 1
  r = 5 / 6
  e = 3
  incr = 7                    
  startp = 0
  stopp = 2

  for k in range ( 0, 30 ):

    for i in range ( startp, stopp + 1 ):
      S = S + r ** i

    M = r ** e
    T = T + M * S
    startp = stopp + 1
    stopp = startp + 1
    e = e + incr
    incr = incr + 4

  print ( '  Probability that A survives = ', T / 6 )

  return

def kids ( n, p, rng ):

#*****************************************************************************80
#
## kids() simulates a family planning problem.
#
#  Discussion:
#
#    Simulate n families that have children
#    until a child is born that is the same sex as the first
#    child, where p is the probability of a boy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    real p: the probability that a child will be a boy.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'kids():' )
  print ( '  Simulate n =', n, 'families that have children' )
  print ( '  until a child is born that is the same sex as the first' )
  print ( '  child, where the probability of a boy is p = ', p )

  total = 0
  s = 0

  for family in range ( 0, n ):

    c = rng.random ( )
    s = s + 1

    if ( c < p ):
      first = 0
    else:
      first = 1

    while ( 0 < s ):

      c = rng.random ( )
      s = s + 1

      if ( c < p ):
        if ( first == 0 ):
          total = total + s
          s = 0

      if ( p < c ):
        if ( first == 1 ):
          total = total + s
          s = 0

  total = total / n

  print ( '' )
  print ( '  Average number of children in each family = ', total )

  return

def markov ( ):

#*****************************************************************************80
#
## markov() follows a Markov chain process.
#
#  Discussion:
#
#    We have four states, 1, 2, 3, 4.
#    If we are in state I, then on the next step we will move to state J
#    with a probility P(I,J).
#    Simulate this process over many steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'markov()' )
  print ( '  We have four states, 1, 2, 3, 4.' )
  print ( '  If we are in state I, then on the next step we will move to state J' )
  print ( '  with a proability P(I,J).' )
  print ( '  Simulate this process over many steps.' )
  print ( '  Display the results graphically.' )

  p0 = np.array ( [ 1.00, 0.00, 0.00, 0.00 ] )

  r1 = np.array ( [ 0.97, 0.03, 0.00, 0.00 ] )
  r2 = np.array ( [ 0.00, 0.98, 0.02, 0.00 ] )
  r3 = np.array ( [ 0.00, 0.00, 0.99, 0.01 ] )
  r4 = np.array ( [ 0.00, 0.00, 0.00, 1.00 ] )

  A = np.array ( [ r1, r2, r3, r4 ] )
  B = A.copy ( )

  prob0 = np.zeros ( 800 )
  prob1 = np.zeros ( 800 )
  prob2 = np.zeros ( 800 )
  prob3 = np.zeros ( 800 )

  for n in range ( 0, 800 ):

    p = np.dot ( p0, B )
    C = np.dot ( A, B )
    B = C.copy ( )

    prob3[n] = p[3]
    prob2[n] = p[2]
    prob1[n] = p[1]
    prob0[n] = p[0]
#
#  Graphics.
#
  plt.clf ( )
  n = np.linspace ( 1, 800, 800 )
  plt.plot ( n, prob3,  )
  plt.plot ( n, prob2, '.' )
  plt.plot ( n, prob1, '+' )
  plt.plot ( n, prob0, '*' )
  plt.legend ( [ 'state 3', 'state 2', 'state 1', 'state 0' ] )
  plt.xlabel ( 'time n (in microseconds)' )
  plt.ylabel ( 'probability' )
  plt.title ( 'Probability the Path is in State k at Time n' )
  plt.grid ( True )
  filename = 'markov.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def match ( n, people_num ):

#*****************************************************************************80
#
## match() computes the probablity of a coin flipping match.
#
#  Discussion:
#
#    This code computes the probability that N people,
#    flipping fair coins n times, will each get the same
#    number of heads.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n, the number of times a person flips a coin.
#
#    integer people_num, the number of people.
#
  print ( '' )
  print ( 'match()' )
  print ( '  Compute the probability that', people_num, 'people,' )
  print ( '  flipping fair coins', n, 'times, will each get the same' )
  print ( '  number of heads.' )

  summation = 0
  for k in range ( 0, n + 1 ):
    bc = binomial ( n, k )
    summation = summation + ( bc ) ** people_num

  summation = summation / ( 2 ** ( people_num * n ) )

  print ( '' )
  print ( '  Match probability is', summation )

  return

def monty ( rng ):

#*****************************************************************************80
#
## monty() simulates the Let's Make a Deal puzzle.
#
#  Discussion:
#
#    There are three doors.
#    A prize is behind one of the doors.
#    You name a door.
#    The host then opens one of the other doors, which is guaranteed not to
#    conceal a prize.
#    You may now choose to switch your choice to the remaining door, or not.
#    What is the better strategy?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  n = 10000

  print ( '' )
  print ( 'monty():' )
  print ( '  There are three doors.' )
  print ( '  A prize is behind one of the doors.' )
  print ( '  You name a door.' )
  print ( '  The host then opens one of the other doors, which is guaranteed not to' )
  print ( '  conceal a prize.' )
  print ( '  You may now choose to switch your choice to the remaining door, or not.' )
  print ( '  What is the better strategy?' )

  WNS = 0
  WWS = 0
  switch1 = 1 / 3
  switch2 = 2 / 3

  for game in range ( 0, n ):
#
#  Place the prize.
#
    choice = rng.random ( )

    if ( choice <= switch1 ):
      prize = 1
    elif ( choice <= switch2 ):
      prize = 2
    else:
      prize = 3
#
#  Pick a door.
#
    choice = rng.random ( )
    if ( choice <= switch1 ):
      select = 1
    elif ( choice <= switch2 ):
      select = 2
    else:
      select = 3
#
#  If prize is behind your selected door, win if you don't switch.
#  If prize is not behind your selected door, win if you do switch.
#
    if ( select == prize ):
      WNS = WNS + 1
    else:
      WWS = WWS + 1

  print ( '' )
  print ( '  Number of trials is     ', n)
  print ( '  No-switch strategy wins:', WNS )
  print ( '  Switch strategy wins:   ', WWS )

  return

def needle ( ):

#*****************************************************************************80
#
## needle() studies a needle dropped onto a table.
#
#  Discussion:
#
#    A circular table top has radius r.
#    A needle of length 2*a <= 2*r is dropped onto the table.
#    * how many times does one end stick out over the edge?
#    * how manu times do both ends stick out?
#    * how many times does neither end stick out?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'needle():' )
  print ( '  A circular table top has radius r.' )
  print ( '  A needle of length 2*a <= 2*r is dropped onto the table.' )
  print ( '  * how many times does one end stick out over the edge?' )
  print ( '  * how manu times do both ends stick out?' )
  print ( '  * how many times does neither end stick out?' )
  print ( '' )

  ratio = np.linspace ( 0.0, 1.0, 101 )

  factor1 = np.arcsin ( ratio )
  factor2 = np.sqrt ( 1.0 - ratio ** 2 )
  prob1 = 1.0 - ( 2.0 / np.pi ) * ( ratio * factor2 + factor1 )
  factor3 = np.sqrt ( 1.0 - 0.25 * ratio ** 2 )
  factor4 = np.arcsin ( 0.5 * ratio )
  prob3 = ( 2.0 / np.pi ) * \
    ( ratio * factor3 + 2.0 * factor4 - ratio * factor2 - factor1 )
  prob2 = 1.0 - ( prob1 + prob3 )
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( ratio, prob1 )
  plt.xlabel ( 'a/r' )
  plt.ylabel ( 'probability' )
  plt.grid ( True )
  plt.title ( 'Probability Neither End of Needle Sticks-Out Over Edge' )
  filename = 'needle1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.plot ( ratio, prob2 )
  plt.xlabel ( 'a/r' )
  plt.ylabel ( 'probability' )
  plt.grid ( True )
  plt.title ( 'Probability One End of Needle Sticks-Out Over Edge' )
  filename = 'needle2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.plot ( ratio, prob3 )
  plt.xlabel ( 'a/r' )
  plt.ylabel ( 'probability' )
  plt.grid ( True )
  plt.title ( 'Probability Both Ends of Needle Stick-Out Over Edge' )
  filename = 'needle3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def normal ( n ):

#*****************************************************************************80
#
## normal() displays a histogram of normal random numbers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'normal():' )
  print ( '  Display a histogram of', n, 'normal random numbers.' )

  y = np.random.normal ( loc = 0.0, scale = 1.0, size = n )
#
#  Graphics.
#
  plt.clf ( )
  plt.hist ( y, bins = 50 )
  plt.grid ( True )
  plt.title ( 'Normal Random Numbers' )
  plt.xlabel ( '<--  X -->' )
  plt.ylabel ( 'Frequency' )
  filename = 'normal.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def odd ( N, rng ):

#*****************************************************************************80
#
## odd() simulates the game of odd man out.
#
#  Discussion:
#
#    This code simulates 1,000 games of odd-person-out, for N people as
#    defined by the user, with each person flipping a fair coin. The elements 
#    of the row vector duration are the number of games of length i, i.e.,
#    duration(i)=# of games that require i flips to complete, where i=1,2,3...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N, the number of players.  This should be a relatively
#    small number like 3, 4 or 5.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'odd():' )
  print ( '  Simulate 1,000 games of odd-person-out, for N people.' )
  print ( '  Each person flips a fair coin. The elements ' )
  print ( '  of the row vector duration are the number of games of length i, i.e.,' )
  print ( '  duration(i)=# of games that require i flips to complete, where i=1,2,3...' )

  duration_size = 100
  duration = np.zeros ( duration_size )
  duration_max = 0

  for game in range ( 0, 1000 ):

    gameover = 0
    flip = 1

    while ( gameover == 0 ):

      s = 0
      for n in range ( 0, N ):
        coin = rng.random ( )
        if ( coin < 0.5 ):
          s = s + 1

      if ( s == 1 or s == N - 1 ):
        gameover = 1
      else:
        flip = flip + 1

    if ( flip <= duration_size ):
      duration[flip-1] = duration[flip-1] + 1

    duration_max = max ( duration_max, flip )

  average = 0.0
  for i in range ( 0, duration_size ):
    average = average + ( i + 1 ) * duration[i]
  average = average / 1000

  print ( '' )
  print ( '  Assuming ', N, 'players, the average number of flips is ', average )
#
#  Graphics.
#
  x = np.linspace ( 1, duration_max, duration_max )
  plt.clf ( )
  plt.bar ( x, duration[0:duration_max] )
  plt.title ( 'Duration of Odd-Person-Out Games' )
  plt.xlabel ( 'duration of games, in units of flips' )
  plt.ylabel (' number of games' )
  plt.grid ( True )
  filename = 'odd.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def onedwalk ( ):

#*****************************************************************************80
#
## onedwalk() models a random walk in one dimension.
#
#  Discussion:
#
#    This code simulates the one-dimensional, symmetrical walk
#    with an absorbing barrier at x = 3.
#    How long is the average walk?
#
#    1 <--> 3 <--> 4 --> 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'onedwalk():' )
  print ( '  Simulate the one-dimensional, symmetrical walk' )
  print ( '  with an absorbing barrier at the right.' )
  print ( '  The map and connections:' )
  print ( '    1 <--> 3 <--> 4 --> 2' )
  print ( '  We start at location 1, and will stop at location 2.' )
  print ( '  How long is the average walk?' )

  web = np.array ( [ \
    [ 1, 3, 0 ], \
    [ 0, 0, 0 ], \
    [ 2, 1, 4 ], \
    [ 2, 2, 3 ] ] )

  d = np.zeros ( 100 )

  for walks in range ( 0, 10000 ):

    position = 1
    steps = 0

    while ( position != 2 ):
      choices = web[position-1,0]
      choice = np.random.randint ( 1, choices+1 )
      position = web[position-1,choice]
      steps = steps + 1

    d[steps-1] = d[steps-1] + 1

  average = 0.0
  for i in range ( 0, 50 ):
    average = average + ( i + 1 ) * d[i]

  average = average / 10000

  print ( '' )
  print ( '  Average walk duration = ', average )
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( d )
  plt.title ( 'Distribution of Walk Durations' )
  plt.xlabel ( 'number of steps' )
  plt.ylabel ( 'number of walks' )
  filename = 'onedwalk.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def onewaytodoit ( n, rng ):

#*****************************************************************************80
#
## onewaytodoit() shows how to generate normal random values.
#
#  Discussion:
#
#    This code generates n normal random values by using the 
#    Box-Muller transformation on uniform random numbers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of values to use.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'onewaytodoit():' )
  print ( '  This program generates', n, 'normal random values using the ' )
  print ( '  Box-Muller transformation on uniform rnadom numbers.' )
  print ( '  Display results as a histogram.' )

  y = np.zeros ( n )

  scale = 2 * np.pi
  for i in range ( 0, n, 2 ):
    u = rng.random ( )
    theta = scale * rng.random ( )
    factor = np.sqrt ( - 2.0 * np.log ( u ) )
    x1 = factor * np.cos ( theta )
    x2 = factor * np.sin ( theta )
    y[i] = x1
    y[i+1] = x2
#
#  Graphics.
#
  plt.clf ( )
  plt.hist ( y, bins = 100 )
  plt.grid ( True )
  plt.title ( 'Histogram of a Normal Random Number Generator' )
  plt.xlabel ( '<-- Value -->' )
  plt.ylabel ( 'Frequency' )
  filename = 'onewaytodoit.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def onion ( rng ):

#*****************************************************************************80
#
## onion() randomly slices the unit interval.
#
#  Discussion:
#
#    This code uniformly slices the unit interval, from left to right,
#    ten times, and forms the sum of the successive widths of the slices. 
#    It does this 5000 times and then plots the distribution function of the sum.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'onion():' )
  print ( '  Uniformly slice the unit interval, from left to right,' )
  print ( '  ten times, and form the sum of the widths of the slices.' )
  print ( '  Do this 5000 times and plot the distribution function of the sum.' )

  rsum = np.zeros ( 5000 )

  for cutting in range ( 0, 5000 ):

    total_thickness = 0.0
    L = 1.0

    for dice in range ( 0, 10 ):
      slice = L * rng.random ( )
      total_thickness = total_thickness + slice
      L = slice
 
    index = round ( 100 * total_thickness + 0.5 )
    rsum[index-1] = rsum[index-1] + 1
#
#  Graphics.
#
  x = np.linspace ( 0.01, 5.0, 500 )

  dist = np.zeros ( 500 )
  dist[0] = rsum[0]
  for index in range ( 1, 500 ):
    dist[index] = dist[index-1] + rsum[index]

  plt.clf ( )
  plt.plot ( x, dist/5000 )
  plt.grid ( True )
  plt.xlabel ( 'thickness' )
  plt.ylabel ( 'probability' )
  plt.title ( 'Distribution of Total Thickness from 5,000 Cuttings' )
  filename = 'onion.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def paradox ( a ):

#*****************************************************************************80
#
## paradox() looks at the average lifetime of a complex system.
#
#  Discussion:
#
#    A simple system has an average lifetime of A.
#    For reliability, a complex system is constructed of three simple systems.
#    The complex system will only fail if at least two of the simple systems fail.
#    What is the average lifetime of the complex system?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    real A, the average lifetime of a single system.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'paradox():' )
  print ( '  A simple system has an average lifetime of A.' )
  print ( '  For reliability, a complex system is constructed of three simple systems.' )
  print ( '  The complex system fails if at least two of the simple systems fail.' )
  print ( '  What is the average lifetime of the complex system?' )

  s = np.zeros ( 200 )
  r = np.zeros ( 200 )

  for i in range ( 0, 200 ):
    s[i] = 1.0 - np.exp ( - ( i + 1 ) / a )
    r[i] = s[i] * s[i] * ( 3.0 - 2.0 * s[i] )
#
#  Graphics.
#
  t = np.linspace ( 1.0, 200.0, 200 )

  plt.clf ( )
  plt.plot ( t, s, '-' )
  plt.plot ( t, r, '.' )
  plt.ylabel ( 'probability of failure by time t' )
  plt.xlabel ( 'time t' )
  plt.grid ( True )
  plt.title ( 'Average Lifetime of a system is 100' )
  plt.legend ( [ 'system', 'SYSTEM' ] )
  filename = 'paradox.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def paths ( rng ):

#*****************************************************************************80
#
## paths() estimates the length of the average walk across a square.
#
#  Discussion:
#
#    This code estimates the distribution and density functions
#    of the random variable L denoting random path lengths
#    across a unit square.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'paths():' )
  print ( '  Estimate the distribution and density functions' )
  print ( '  of the random variable L denoting random path lengths' )
  print ( '  across a unit square.' )
  print ( '' )

  length = np.zeros ( 142 )

  for n in range ( 0, 100000 ):

    x = rng.random ( )
    angle = np.pi * rng.random ( )
    A1 = np.arctan ( 1.0 / ( 1.0 - x ) )

    if ( angle < A1 ):
      L = ( 1.0 - x ) / np.cos ( angle )
    elif ( A1 < angle and angle < np.pi - np.arctan ( 1.0 / x ) ):
      L = 1.0 / np.sin ( angle )
    else:
      L = - x / np.cos ( angle )

    index = int ( np.round ( 100 * L + 0.5 ) ) - 1
    length[index] = length[index] + 1
#
#  Graphics.
#
  x = np.linspace ( 0.01, 1.42, 142 )

  dist = np.zeros ( 142 )
  dist[0] = length[0]
  for index in range ( 1, 142 ):
    dist[index] = dist[index-1] + length[index]

  plt.clf ( )
  plt.plot ( x, length/1000 )
  plt.grid ( True )
  plt.xlabel ( 'length' )
  plt.ylabel ( 'magnitude' )
  plt.title ( 'Density of L from 100,000 Paths' )
  filename = 'paths_density.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.plot ( x, dist/100000 )
  plt.grid ( True )
  plt.xlabel ( 'length' )
  plt.ylabel ( 'probability' )
  plt.title ( 'Distribution of L from 100,000 Paths' )
  filename = 'paths_distribution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def pisim ( n, rng ):

#*****************************************************************************80
#
## pisim() estimates PI by sampling points in a square.
#
#  Discussion:
#
#    Sample N points (x,y) in a square.
#    The number of points M with x^2+y^2 <= 1 lie inside the quarter circle.
#    M/N is an estimate of pi/4. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'pisim():' )
  print ( '  Sample n = ', n, 'points (x,y) in a square.' )
  print ( '  The number of points M with x^2+y^2 <= 1 lie inside the quarter circle.' )
  print ( '  M/N is an estimate of pi/4. ' )

  darts = 0
 
  for i in range ( 0, n ):
    x = rng.random ( )
    y = rng.random ( )
    if ( x**2 + y**2 < 1.0 ):
      darts = darts + 1

  pi_estimate = 4.0 * darts / n

  print ( '' )
  print ( '  Estimate for PI is', pi_estimate )

  return

def radar ( nmax, p, ps, pn ):

#*****************************************************************************80
#
## radar() analyzes the problem of radar detection and identification.
#
#  Discussion:
#
#    As the number of observations N increases, compute
#    * PD, the probability of detection.
#    * PFA, the probability of false alarm.
#
#    Present the results graphically.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer nmax: the total number of observations.
#
#    real P, the minimum decimal fraction of observations to 
#    declare a target.
#
#    real PS, the 0/1 signal threshold probability.
#
#    real PN, the 0/1 noise threshhold probability.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'radar():' )
  print ( '  As the number of observations nmax increases, compute' )
  print ( '  * PD, the probability of detection.' )
  print ( '  * PFA, the probability of false alarm.' )

  ops = 1.0 - ps
  opn = 1.0 - pn

  pdv = np.zeros ( nmax )
  pfav = np.zeros ( nmax )

  for n in range ( 1, nmax + 1 ):
    m = int ( np.floor ( n * p ) ) + 1
    pd = 0
    pfa = 0
    for k in range ( m, n + 1 ):
      factor = binomial ( n, k )
      pd = pd + factor * ( ps ** k ) * ops ** ( n - k )
      pfa = pfa + factor * ( pn ** k ) * opn ** ( n - k )

    pdv[n-1] = pd
    pfav[n-1] = pfa
#
#  Graphics.
#
  x = np.linspace ( 1, nmax, nmax )

  plt.clf ( )
  plt.plot ( x, pdv, '-' )
  plt.plot ( x, pfav, ':' )
  plt.grid ( True )
  plt.legend ( [ 'Probability of Detection','Probability of False Alarm' ] )
  plt.xlabel ( 'number of observations' )
  plt.ylabel ( 'probability' )
  plt.title ( 'Probabilities of Detection or False Alarm' )
  filename = 'radar.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def randomsum ( m, rng ):

#*****************************************************************************80
#
## randomsum() carries out a process that estimates e.
#
#  Discussion:
#
#    Add a sequence of random values until you exceed 1.
#    Let N be the number of terms in this sequence.
#    Repeating this process m times, let D(N) be the number of times
#    that N terms were required.
#
#    Then e can be approximated by 1*D(1) + 2*D(2) + ... * I * D(I) + ...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer m: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'randomsum():' )
  print ( '  Add a sequence of random values until you exceed 1.' )
  print ( '  Let N be the number of terms in this sequence.' )
  print ( '  Repeating this process', m, 'times, let D(N) be the number of times' )
  print ( '  that N terms were required.' )
  print ( '  Then E can be approximated by 1*D(1) + 2*D(2) + ... * I * D(I) + ...' )

  d = np.zeros ( 20 )
  k = 1

  for k in range ( 0, m ):
 
    n = 0
    summation = 0
    while ( summation < 1.0 ):
      summation = summation + rng.random ( )
      n = n + 1

    d[n-1] = d[n-1] + 1
 
  e = 0.0
  for n in range ( 0, 20 ):
    e = e + ( n + 1 ) * d[n]
  e = e / m

  print ( '' )
  print ( '  Estimate for e = ', e )
  print ( '  Exact value =    ', np.exp ( 1.0 ) )

  return
                                     
def spider ( ):

#*****************************************************************************80
#
## spider() simulates a spider's random walk on a 2D web.
#
#  Discussion:
#
#    A web consists of locations 1 through 9.
#    The web is connected, and each location is connected to some of the others.
#    A spider begins at location 1, and a fly is trapped at location 2.
#    By choosing random moves on the web, how long does it take
#    the spider to find the fly?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'spider():' )
  print ( '  A web consists of locations 1 through 9.' )
  print ( '  The web is connected, and each location is connected to some of the others.' )
  print ( '  A spider begins at location 1, and a fly is trapped at location 2.' )
  print ( '  By choosing random moves on the web, how long does it take' )
  print ( '  the spider to find the fly?' )

  t1 = np.array ( [ 3,0,3,1,2,2,3,4,2 ] )
  t2 = np.array ( [ 4,0,2,1,3,5,1,1,2 ] )
  t3 = np.array ( [ 7,0,5,0,6,7,6,3,8 ] )
  t4 = np.array ( [ 8,0,8,0,0,0,8,7,0 ] )
  t5 = np.array ( [ 0,0,0,0,0,0,0,9,0 ] )

  web = np.array ( [ t1, t2, t3, t4, t5 ] )
  web = np.transpose ( web )

  d = np.zeros ( 250 )

  for walks in range ( 0, 10000 ):

    position = 1
    steps = 0

    while ( position != 2 ):
      choices = web[position-1,0]
      choice = np.random.randint ( low = 0, high = choices ) + 2
      position = web[position-1,choice-1]
      steps = steps + 1

    d[steps-1] = d[steps-1] + 1

  average = 0
  for i in range ( 1, 51 ):
    average = average + i * d[i-1]
  average = average / 10000

  print ( '' )
  print ( '  Average number of steps to reach the fly = ', average )
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( d )
  plt.title ( 'Distribution of Walk Durations on the Web (10,000 walks)' )
  plt.xlabel ( 'number of steps' )
  plt.ylabel ( 'number of walks' )
  filename = 'spider.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def stirling1 ( ):

#*****************************************************************************80
#
## stirling1() compares the logarithms of n! and Stirling's approximation.
#
#  Discussion:
#
#    Compare the logarithms of n! and Stirling's approximation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  from scipy.special import gamma
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy as sp

  print ( '' )
  print ( 'stirling1():' )
  print ( '  Compare the logarithms of n! and Stirling\'s approximation' )

  f = np.zeros ( 170 )
  s = np.zeros ( 170 )

  for i in range ( 0, 170 ):
    n = i + 1
    f[i] = np.log ( gamma ( n + 1 ) )
    s[i] = n * np.log ( n ) - n
#
#  Graphics.
#
  plt.clf ( )  
  plt.plot ( f - s, 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'n' )
  plt.ylabel ( 'Absolute Error' )
  plt.title ( 'ln(n!) - [nln(n)-n]' )
  filename = 'stirling1_error_abs.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )  
  plt.semilogx ( f / s, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'n' )
  plt.ylabel ( 'Relative Error' )
  plt.title ( 'ln(n!)/[nln(n)-n]' )
  filename = 'stirling1_error_rel.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def stirling2 ( ):

#*****************************************************************************80
#
## stirling2() compares n! to Stirling's approximation.
#
#  Discussion:
#
#    Stirling approximates n! by sqrt(2*pi*n) * n^n * exp(-n).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  from scipy.special import gamma
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stirling2():' )
  print ( '  Stirling approximates n! by sqrt(2*pi*n) * n^n * exp(-n).' )
  print ( '  Display a plot of absolute and relative errors.' )

  f = np.zeros ( 150 )
  s = np.zeros ( 150 )

  for n in range ( 1, 151 ):
    f[n-1] = gamma ( n + 1 )
    s[n-1] = np.sqrt ( 2.0 * np.pi * n ) \
      * ( n ** 50 ) * ( n ** ( n - 50 ) ) * np.exp ( - n )
#
#  Graphics.
#
  plt.clf ( )
  plt.semilogy ( f - s, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'n' )
  plt.ylabel ( 'Absolute Error' )
  plt.title ( 'n! - Stirling' )
  filename = 'stirling2_error_abs.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.plot ( f / s, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'n' )
  plt.ylabel ( 'Relative Error' )
  plt.title ( 'n!/Stirling' )
  filename = 'stirling2_error_rel.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def stirling3 ( ):

#*****************************************************************************80
#
## stirling3() compares n factorial and Stirling's approximation. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  from scipy.special import gamma
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stirling3():' )
  print ( '  Compare n factorial and Stirling\'s approximation.' )
  print ( '  Present the results graphically.' )

  f = np.zeros ( 150 )
  s = np.zeros ( 150 )

  for n in range ( 1, 151 ):
    f[n-1] = gamma ( n + 1 )
    s[n-1] = np.sqrt ( 2 * np.pi * n ) \
      * ( n ** 50 ) * np.exp ( -n ) * ( n ** ( n - 50 ) )
#
#  Graphics.
#
  plt.clf ( )
  plt.semilogy ( f - s, 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'n' )
  plt.ylabel ( 'Absolute Error' )
  plt.title ( 'n! - sqrt(2pi*n)(n^n)e^-n' )
  filename = 'stirling3_error_abs.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.plot ( f / s, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'n' )
  plt.ylabel ( 'Relative Error' )
  plt.title ( 'n! / [sqrt(2pi*n)(n^n)e^-n]' )
  filename = 'stirling3_error_rel.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def theory ( ):

#*****************************************************************************80
#
## theory() plots the theoretical distribution for the PATHS problem.
#
#  Discussion:
#
#    A line is drawn through the unit square by choosing a point x 
#    in [0,1] and then choosing a random angle between 0 and 180 degrees.
#    This m-file plots the theoretical distribution of the length of
#    the line between x and the intersection with the square's boundary.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'theory():' )
  print ( '  A line is drawn through the unit square by choosing a point x ' )
  print ( '  in [0,1] and then choosing a random angle between 0 and 180 degrees.' )
  print ( '  Plot the theoretical distribution of the length of' )
  print ( '  the line between x and the intersection with the square\'s boundary.' )

  factor = 2.0 / np.pi

  F = np.zeros ( 1414 )

  for l in range ( 0, 1414 ):

    lscale = ( l + 1 ) / 1000.0
    if ( l + 1 < 1000 ):
      F[l] = factor * lscale
    else:
      F[l] = factor \
        * ( 1.0 + 2.0 * np.arccos ( 1.0 / lscale ) - np.sqrt ( lscale ** 2 - 1.0 ) )
#
#  Graphics.
#
  plt.clf ( )
  x = np.linspace ( 0.001, 1.414, 1414 )
  plt.plot ( x, F )
  plt.grid ( True )
  plt.xlabel ( 'length' )
  plt.ylabel ( 'probability' )
  plt.title ( 'Theoretical Distribution Function' )
  filename = 'theory.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def thief ( rng ):

#*****************************************************************************80
#
## thief() simulates the Thief of Baghdad problem.
#
#  Discussion:
#
#    A thief is in a room with three doors.
#    He chooses one at random.
#    One door leads immediately to freedom.
#    Another leads back to the room, after S hours.
#    The third leads back to the room, after L hours.
#    If the thief is returned to the room, he randomly tries a door again.
#    How long is the average imprisonment?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'thief()' )
  print ( '  A thief is in a room with three doors.' )
  print ( '  He chooses one at random.' )
  print ( '  One door leads immediately to freedom.' )
  print ( '  Another leads back to the room, after S hours.' )
  print ( '  The third leads back to the room, after L hours.' )
  print ( '  If the thief is returned to the room, he randomly tries a door again.' )
  print ( '  How long is the average imprisonment?' )

  long = 3.0
  short = 1.0
  total = 0.0
  p1 = 1.0 / 3.0
  p2 = 2.0 / 3.0

  for thiefn in range ( 0, 10000 ):

    time = 0
    trytoescape = 1

    while ( 0 < trytoescape ):

      door = rng.random ( )

      if ( door < p1 ):
        total = total + time
        trytoescape = 0
      elif ( door < p2 ):
        time = time + short
      else:
        time = time + long

  total = total / 10000
  print ( '' )
  print ( '  Estimated average total time in prison = ', total )
  print ( '  Exact value is ', long + short )

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

def tub ( ps, N ):

#*****************************************************************************80
#
## tub() optimizes the allocation of search boats for the Unsinkable Tub.
#
#  Discussion:
#
#    This code computes the optimal allocation of search boats
#    looking for the UNSINKABLE TUB.
#
#    The tub is sinking either 10 miles south (probability P1) or 
#    10 miles north of the station (probability P2 = 1 - P1).
#
#    N search boats are available, and each has a PS probability of locating
#    the tub.  How can we maximize the chance of locating the tub?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    real PS, the probability a search boat will find the tub.
#
#    integer N, the number of search boats available.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'tub():' )
  print ( '  Compute the optimal allocation of search boats' )
  print ( '  looking for the UNSINKABLE TUB.' )
  print ( '  The tub is sinking either 10 miles south (probability P1) or ' )
  print ( '  10 miles north of the station (probability P2 = 1 - P1).' )
  print ( '  ', N, ' search boats are available.' )
  print ( '  Each searcher has a probability of locating the tub PS = ', ps )
  print ( '  How can we maximize the chance of locating the tub?' )
  print ( '' )

  p = np.linspace ( 0.001, 0.999, 999 )
  answer = np.zeros ( 999 )

  for i in range ( 0, 999 ):

    p1 = p[i]
    p2 = 1.0 - p1
    n = ( N + ( np.log ( p2 / p1 ) / np.log ( 1.0 - ps ) ) ) / 2.0
    nl = int ( np.floor ( n ) )
    nu = nl + 1
    Pl = p1 * ( 1.0 - ( 1.0 - ps ) ** nl ) + p2 * ( 1.0 - ( 1.0 - ps ) ** ( N - nl ) )
    Pu = p1 * ( 1.0 - ( 1.0 - ps ) ** nu ) + p2 * ( 1.0 - ( 1.0 - ps ) ** ( N - nu ) )

    n = min ( n, N )
    n = max ( n, 0 )

    if ( 0 < n and n < N ):
      if ( Pu < Pl ):
        n = nl
      else:
        n = nu

    answer[i] = n
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( p, answer )
  plt.grid ( True )
  plt.ylabel ( 'n, Search boats assigned to Island #1' )
  plt.xlabel ( 'p1, probability the UNSINKABLE TUB is at Island #1' )
  plt.title ( 'The Unsinkable Tub' )
  filename = 'tub.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def underdog1 ( ):

#*****************************************************************************80
#
## underdog1() estimates the chances of an underdog winning the World Series.
#
#  Discussion:
#
#    The World Series of Baseball involves up to 7 games between two teams.
#    Suppose the stronger team has probability p of winning any one game.
#    What is the probability w that the weaker team will actually win the series?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'underdog1():' )
  print ( '  The World Series of Baseball involves up to 7 games between two teams.' )
  print ( '  Suppose the stronger team has probability P of winning any one game.' )
  print ( '  What is the probability that the weaker team will actually win the series?' )
  print ( '' )

  p = np.linspace ( 0.5, 1.0, 51 )
  w = np.zeros ( 51 )

  for i in range ( 0, 51 ):
    common = ( 1.0 - p[i] ) ** 4
    w[i] = common * ( 1.0 + 4.0 * p[i] + 10.0 * p[i] **2 + 20.0 * p[i] ** 3 )
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( p, w )
  plt.grid ( True )
  plt.xlabel ( 'probability p of stronger team winning an individual game' )
  plt.ylabel ( 'probability w that weaker team wins the World Series' )
  plt.title ( 'The Stronger Team Does NOT Always Win!' )
  filename = 'underdog1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def underdog2 ( ):

#*****************************************************************************80
#
## underdog2() estimates the duration of a World Series.
#
#  Discussion:
#
#    The World Series of Baseball involves up to 7 games between two teams.
#    Suppose the stronger team has probability P of winning any one game.
#    What is the average duration of the World Series?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'underdog2():' )
  print ( '  The World Series of Baseball involves up to 7 games between two teams.' )
  print ( '  Suppose the stronger team has probability P of winning any one game.' )
  print ( '  What is the average duration of the World Series?' )
  print ( '' )

  n = 100
  p = np.linspace ( 0.01, 1.0, n )
  duration = np.zeros ( n )
  
  for i in range ( 0, n ):

    common1 = ( 1.0 - p[i] ) ** 4
    common2 = p[i] ** 4

    duration[i] = \
        4 *  1 * ( common1             + common2 ) \
      + 5 *  4 * ( common1 * p[i]      + common2 * ( 1.0 - p[i] ) ) \
      + 6 * 10 * ( common1 * p[i] ** 2 + common2 * ( 1.0 - p[i] ) ** 2 ) \
      + 7 * 20 * ( common1 * p[i] ** 3 + common2 * ( 1.0 - p[i] ) ** 3 )
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( p, duration )
  plt.grid ( True )
  plt.xlabel ( 'Probability, p, of a team winning one game' )
  plt.ylabel ( 'Games played' )
  plt.title ( 'Duration of best-out-of-7 World Series' )
  filename = 'underdog2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def xplusy ( n, rng ):

#*****************************************************************************80
#
## xplusy() creates a histogram of the sum of N random variables.
#
#  Discussion:
#
#    This code produces 5,000 values of the sum of N random
#    variables, each variable uniform from 0 to 1, and independent.
#    It then plots a histogram of the sums using 100 bins.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of variables in each sum.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'xplusy():' )
  print ( '  Produce 5000 values of the sum of', n, 'random' )
  print ( '  variables, each variable uniform from 0 to 1, and independent.' )
  print ( '  Plot a histogram of the sums.' )

  mean = n / 2
  sd = np.sqrt ( n / 12 )
  z = np.zeros ( 5000 )
  for sumn in range ( 0, 5000 ):
    z[sumn] = np.sum ( rng.random ( size = n ) )
#
#  Graphics.
#
  plt.clf ( )
  plt.hist ( z, bins = 50 )
  plt.grid ( True )
  plt.xlabel ( 'sum' )
  plt.ylabel ( 'number of values per bin' )
  plt.title ( 'Sum of N Random Variables' )
  filename = 'xplusy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def xpowery ( ):

#*****************************************************************************80
#
## xpowery() plots the PDF of X^Y.
#
#  Discussion:
#
#    This code plots the probability density function of X^Y,
#    where X and Y are independent, and both uniform from 0 to 1.
#    This PDF involves the exponential integral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  from scipy.special import exp1
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'xpowery():' )
  print ( '  Plot the probability density function of X^Y,' )
  print ( '  where X and Y are independent, and both uniform from 0 to 1.' )

  z = np.linspace ( 0.01, 1.0, 100 )
  pdf = exp1 ( - np.log ( z ) ) / z
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( z, pdf )
  plt.grid ( True )
  plt.title ( 'PDF of Z = X^Y, with X and Y uniform from 0 to 1' )
  plt.ylabel ( 'pdf(z)' )
  plt.xlabel ( '<-- z -->' )
  filename = 'xpowery.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def xyhisto ( n, rng ):

#*****************************************************************************80
#
## xyhisto() makes a histogram of X^Y.
#
#  Discussion:
#
#    This code produces n values of X raised to the Y power,
#    where X and Y are both uniform from 0 to 1, and independent. It
#    then plots a histogram of the values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'xyhisto():' )
  print ( '  Produce', n, 'values of X raised to the Y power,' )
  print ( '  where X and Y are uniform random values.' )

  x = rng.random ( n )
  y = rng.random ( n )
  z = x ** y
#
#  Graphics.
#
  plt.clf ( )
  plt.hist ( z, bins = 50 )
  plt.grid ( True )
  plt.xlabel ( '<-- z -->' )
  plt.ylabel ( 'Frequency' )
  plt.title ( 'Z=X^Y for random X and Y' )
  filename = 'xyhisto.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def z ( n, rng ):

#*****************************************************************************80
#
## z() uses a histogram to approximate the distribution of Z=X/(X-Y).
#
#  Discussion:
#
#    This code simulates the random variable Z=X/(X-Y),
#    where X and Y are independent and uniform from 0 to 1.
#    The output is a histogram of Z.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer n: the number of trials.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'z():' )
  print ( '  Simulate the random variable Z=X/(X-Y),' )
  print ( '  where X and Y are uniform random values.' )

  vector = np.zeros ( n )

  index = 0

  while ( index < n ):
    x = rng.random ( )
    y = rng.random ( )
    z = x / ( x - y )
    if ( abs ( z ) < 3 ):
      vector[index] = z
      index = index + 1
#
#  Graphics.
#
  plt.clf ( )
  plt.hist ( vector, bins = 50 )
  plt.title ( 'Histogram of Z=X/(X-Y)' )
  plt.xlabel ( '-3.0 <= Z=X/(X-Y) <= +3.0' )
  plt.ylabel ( 'Frequency' )
  filename = 'z.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  dueling_idiots_test ( )
  timestamp ( )

