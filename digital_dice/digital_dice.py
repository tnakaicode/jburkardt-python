#! /usr/bin/env python3
#
def digital_dice_test ( ):

#*****************************************************************************80
#
## digital_dice_test() tests digital_dice().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
  from numpy.random import default_rng 
  import numpy as np
  import platform

  print ( '' )
  print ( 'digital_dice_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test digital_dice().' )

  rng = default_rng ( )

  trial_num = 10000
  aandb ( trial_num, rng )
  
  for trial_num in [ 100, 10000, 1000000 ]:
    average ( trial_num, rng )

  for trial_num in [ 10000, 100000 ]:
    baby_boom ( trial_num, rng )

  trial_num = 100000
  broke ( trial_num, 1, 1, 1, 0.5, rng )
  broke ( trial_num, 1, 2, 3, 0.5, rng )
  broke ( trial_num, 2, 3, 4, 0.5, rng )
  broke ( trial_num, 3, 3, 3, 0.5, rng )
  broke ( trial_num, 4, 7, 9, 0.5, rng )
  broke ( trial_num, 1, 1, 1, 0.4, rng )
  broke ( trial_num, 1, 2, 3, 0.4, rng )
  broke ( trial_num, 2, 3, 4, 0.4, rng )
  broke ( trial_num, 3, 3, 3, 0.4, rng )
  broke ( trial_num, 4, 7, 9, 0.4, rng )

  trial_num = 1000000
  for n in range ( 1, 6 ):
    bus ( trial_num, n, rng )

  trial_num = 1000000
  for n in [ 3, 10, 20, 30 ]:
    car ( trial_num, n, rng )

  trial_num = 1000000
  chess ( trial_num, 0.9, 0.8, rng )
  chess ( trial_num, 0.9, 0.4, rng )
  chess ( trial_num, 0.4, 0.3, rng )
  chess ( trial_num, 0.4, 0.1, rng )

  trial_num = 100000
  committee ( trial_num, rng )

  deli ( 30, 40, 1, rng )
  deli ( 30, 40, 2, rng )
  deli ( 50, 25, 1, rng )
  deli ( 50, 25, 2, rng )

  dinner ( )

  trial_num = 1000000
  dish ( trial_num, rng )

  easywalk ( 1000 )

  trial_num = 100000
  election ( trial_num, 3, 2, 2, False, rng )
  election ( trial_num, 3, 3, 2, True, rng )
  election ( trial_num, 7, 7, 4, False, rng )
  election ( trial_num, 25, 2, 17, True, rng )

  trial_num = 10000
  estimate ( trial_num, rng )

  floss ( 40 )
  floss ( 150 )

  trial_num = 10000000
  forgetful_burglar ( trial_num, rng )

  trial_num = 10000
  gameb ( trial_num, rng )

  trial_num = 1000000
  for n in range ( 1, 4 ):
    gs ( trial_num, n, rng )

  trial_num = 1000000
  m = 24
  guess_rank ( trial_num, m, rng )

  trial_num = 10000000
  jury ( trial_num, rng )

  trial_num = 10000
  p = 0.4
  kelvin ( trial_num, p, rng )

  trial_num = 1000000
  malt ( trial_num, rng )

  trial_num = 1000000
  a = 49
  for m in range ( 3, 6 ):
    missing ( trial_num, a, m, rng )

  trial_num = 1000000
  monotone ( trial_num, rng )

  trial_num = 1000000
  obtuse ( trial_num, rng )

  trial_num = 1000000
  obtuse1 ( trial_num, rng )

  trial_num = 10000
  optimal ( trial_num, 11, 2, rng )
  optimal ( trial_num, 50, 5, rng )

  trial_num = 1000000
  for n in range ( 1, 6 ):
    patrol ( trial_num, n, rng )

  for trial_num in [ 100, 10000 ]:
    pierror ( trial_num, rng )

  trial_num = 1000000
  ranking ( trial_num, 24, rng )

  trial_num = 50000
  rhs ( trial_num, rng )

  rolls ( )

  trial_num = 1000000
  smoker ( trial_num, rng )

  trial_num = 1000000
  smokerb ( trial_num, rng )

  trial_num = 10000
  spin ( trial_num, rng )

  trial_num = 1000000
  for k in [ 0, 1, 2, 3, 9 ]:
    steve ( trial_num, k, rng )

  for n in [ 5, 10, 20, 50, 100 ]:
    stopping ( n )

  trial_num = 1000000
  sylvester_quadrilateral ( trial_num, rng )

  trial_num = 10000
  umbrella ( trial_num, 1, 1, rng )
  umbrella ( trial_num, 2, 2, rng )

  trial_num = 100000
  for m in [ 2, 5, 10, 20, 50, 100 ]:
    walk ( trial_num, m, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'digital_dice_test():' )
  print ( '  Normal end of execution.' )

  return

def aandb ( trial_num, rng ):

#*****************************************************************************80
#
## aandb(): Parrondo's paradox.
#
#  Discussion:
#
#    In game A, you flip a biased coin, which shows heads with probabiity]
#    1/2 - epsilon you win a dollar on heads.
#    In game B, you have two biased coins.  If, at the time just before you
#    decide to flip, your capital M is a multiple of 3 dollars, you chose
#    coin 1, which shows heads with probability 1/10 - epsilon, otherwise
#    you choose coin 2, which shows heads with probability 3/4 - epsilon.
#    Both games A and B are losing games for you.
#    But, paradoxically, if you randomly switch back and forth between
#    one game and the other, you end up winning over the long term.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
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
  print ( 'aandb():' )
  print ( '  In game A, you flip a biased coin, which shows heads with probabiity]' )
  print ( '  1/2 - epsilon you win a dollar on heads.' )
  print ( '  In game B, you have two biased coins.  If, at the time just before you' )
  print ( '  decide to flip, your capital M is a multiple of 3 dollars, you chose' )
  print ( '  coin 1, which shows heads with probability 1/10 - epsilon, otherwise' )
  print ( '  you choose coin 2, which shows heads with probability 3/4 - epsilon.' )
  print ( '  Both games A and B are losing games for you.' )
  print ( '  But, paradoxically, if you randomly switch back and forth between' )
  print ( '  one game and the other, you end up winning over the long term.' )
  print ( '' )
  print ( '  Use graphics to display the winnings.' )

  epsilon = 0.005
  mtotal = np.zeros ( 100 )

  for loop in range ( 0, trial_num ):

    m = 0
    sample_function = np.zeros ( 100 )

    for flips in range ( 0, 100 ):

      which_game = rng.random ( )

      if ( which_game < 0.5 ):

        outcome = rng.random ( )
        if ( outcome < 0.5 - epsilon ):
          m = m + 1
        else:
          m = m - 1

      else:

        if ( ( m % 3 ) == 0 ):

          outcome = rng.random ( )
          if ( outcome < 0.1 - epsilon ):
            m = m + 1
          else:
            m = m - 1

        else:

          outcome = rng.random ( )
          if ( outcome < 0.75 - epsilon ):
            m = m + 1
          else:
            m = m - 1

      sample_function[flips] = m

    mtotal = mtotal + sample_function

  mtotal = mtotal / trial_num
#
#  Graphics.
#
  plt.clf ( )
  flips = np.linspace ( 1, 100, 100 )
  plt.plot ( flips, mtotal, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'Parrondo''s A and B Paradox' )
  plt.xlabel ( 'Number of coin flips' )
  plt.ylabel ( 'Ensemble average of capital.' )
  filename = 'aandb.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def average ( trial_num, rng ):

#*****************************************************************************80
#
## average() uses a Monte Carlo approach to estimate pi.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num, the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'average():' )
  print ( '  Use a Monte Carlo sample to estimate pi.' )

  sum = 0.0
  for loop in range ( 0, trial_num ):
    x = rng.random ( )
    sum = sum + np.sqrt ( 1.0 - x * x )

  sum = 4.0 * sum / trial_num

  print ( '' )
  print ( '  Estimate for pi = ', sum )
  print ( '  Error =           ', np.pi - sum )

  sum = 0.0
  for loop in range ( 0, trial_num ):
    x = rng.random ( )
    sum = sum + ( np.sqrt ( 1.0 - x * x ) + np.sqrt ( 1 - ( 1 - x )**2 ) ) / 2.0
  sum = 4.0 * sum / trial_num

  print ( '  Antithetic estimate for pi = ', sum )
  print ( '  Error =                      ', np.pi - sum )

  return

def baby_boom ( trial_num, rng ):

#*****************************************************************************80
#
## baby_boom() simulates the likelihood of a given number of sons in a family.
#
#  Discussion:
#
#    There are given probabilities of a man having 0, 1, 2, 3, 4, 5, 6 or 7 sons.
#    What are the chances of having 2 or 4 sons in the second generation?
#    Of having 6 sons in the third generation?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'baby_boom():' )
  print ( '  There are given probabilities of a man having 0, 1, 2, 3, 4, 5, 6 or 7 sons.' )
  print ( '  What are the chances of having:' )
  print ( '    2 sons in the second generation?' )
  print ( '    4 sons in the second generation?' )
  print ( '    6 sons in the third generation?' )

  p0 = 0.4825
  p1 = 0.2126
  p2 = p1 * 0.5893
  p3 = p2 * 0.5893
  p4 = p3 * 0.5893
  p5 = p4 * 0.5893
  p6 = p5 * 0.5893

  zero = p0
  one = zero + p1
  two = one + p2
  three = two + p3
  four = three + p4
  five = four + p5
  six = five + p6

  answer = np.zeros ( 3 )

  for loop in range ( 0, trial_num ):

    gen2 = np.zeros ( 7, dtype = int )
    gen3 = np.zeros ( 49, dtype = int )
    gen1 = baby_boom_result ( zero, one, two, three, four, five, six, rng )
    for loop1 in range ( 0, gen1 ):
      gen2[loop1] = baby_boom_result ( zero, one, two, three, four, five, six, rng )

    index = 0
    for loop2 in range ( 0, gen1 ):
      for loop3 in range ( 0, gen2[loop2] ):
        gen3[index] = baby_boom_result ( zero, one, two, three, four, five, six, rng )
        index = index + 1

    n = np.sum ( gen2 )

    if ( n == 2 ):
      answer[0] = answer[0] + 1
    elif ( n == 4 ):
      answer[1] = answer[1] + 1

    if ( np.sum ( gen3 ) == 6 ):
      answer[2] = answer[2] + 1

  answer = answer / trial_num

  print ( '' )
  print ( '  Estimated probabilities:' )
  print ( '  2 males in generation 2 =', answer[0] )
  print ( '  4 males in generation 2 =', answer[1] )
  print ( '  6 males in generation 3 =', answer[2] )

  return

def baby_boom_result ( zero, one, two, three, four, five, six, rng ):

#*****************************************************************************80
#
## baby_boom_result() randomly determines the number of sons born.
#
#  Discussion:
#
#    This is a utility functioned needed by the baby boom code.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    real ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, the probability
#    of having no more than 0, 1, 2, 3, 4, 5, or 6 sons.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer SONS, a randomly chosen number of sons.
#
  luck = rng.random ( )

  if ( luck < zero ):
    sons = 0
  elif ( luck < one ):
    sons = 1
  elif ( luck < two ):
    sons = 2
  elif ( luck < three ):
    sons = 3
  elif ( luck < four ):
    sons = 4
  elif ( luck < five ):
    sons = 5
  elif ( luck < six ):
    sons = 6
  else:
    sons = 7

  return sons

def broke ( trial_num, l, m, n, p, rng ):

#*****************************************************************************80
#
## broke(): average number of flips til odd man out is lost.
#
#  Discussion:
#
#    Three players begin with L, M and N dollars.
#    On each turn, each player flips a coin.
#    All coins have the same bias P.
#    If one player is "odd man out", he pays a dollar to each other player.
#    When a player is bankrupt, the game is over.
#    What is the average number of turns required?
#
#    If P = 0.5 (no bias) then the average is 4*L*M*N/3/(L+M+N-2)
#
#    L  M  N    P  FLIPS
#
#    1  1  1  0.5    4/3
#    1  2  3  0.5    2
#    2  3  4  0.5   32/7
#    3  3  3  0.5   36/7
#    4  7  9  0.5 1008/54
#
#    1  1  1  04   100/72
#
#    1  2  3  0.4   2.0814 (estimate)
#    2  3  4  0.4   4.7721 (estimate)
#    3  3  3  0.4   5.36   (estimate)
#    4  7  9  0.4  19.4875 (estimate
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer L, M, N, the number of dollars each player has at the start.
#
#    real P, the bias on the coins.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'broke():' )
  print ( '  Three players begin with L, M and N dollars.' )
  print ( '  On each turn, each player flips a coin.' )
  print ( '  All coins have the same bias P =', p )
  print ( '  If one player is "odd man out", he pays a dollar to each other player.' )
  print ( '  When a player is bankrupt, the game is over.' )
  print ( '  What is the average number of turns required?' )

  total_flips = 0

  for sequences in range ( 0, trial_num ):

    sequence_flips = 0

    man = [ l, m, n ]

    while ( 0 < man[0] and 0 < man[1] and 0 < man[2] ):

      flip = rng.random ( size = 3 )

      for j in range ( 0, 3 ):
        if ( flip[j] < p ):
          flip[j] = 1
        else:
          flip[j] = 0

      test = np.sum ( flip )

      if ( test == 1 or test == 2 ):

        if ( test == 1 ):

          for j in range ( 0, 3 ):
            if ( flip[j] == 0 ):
              flip[j] = -1
            else:
              flip[j] = 2

        else:

          for j in range ( 0, 3 ):
            if ( flip[j] == 0 ):
              flip[j] = 2
            else:
              flip[j] = -1

        man = man + flip

      sequence_flips = sequence_flips + 1

    total_flips = total_flips + sequence_flips

  total_flips = total_flips / trial_num

  print ( '' )
  print ( '  Average number of turns = ', total_flips )

  return

def bus ( trial_num, n, rng ):

#*****************************************************************************80
#
## bus() estimates the waiting time, given that there are N bus lines.
#
#  Discussion:
#
#    N bus lines are available at a bus stop.
#    In any hour, each bus line will come to the stop at a random time.
#    A passenger arrives at the bus stop at a random time.
#    What is the average wait for a bus?
#
#  Example:
#
#    N    Average wait
#
#    1    0.4996
#    2    0.3335
#    3    0.2503
#    4    0.2001
#    5    0.1667
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer N, the number of bus lines.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'bus():' )
  print ( '  A bus stop is serviced by', n, 'bus linesp.' )
  print ( '  In any hour, each bus line will come to the stop at a random time.' )
  print ( '  A passenger arrives at the bus stop at a random time.' )
  print ( '  What is the average wait for a bus?' )

  total_waiting_time = 0

  for loop in range ( 0, trial_num ):

    bus_arrivals = rng.random ( size = n )
    bus_arrivals[0] = 0.0

    ride_arrival = rng.random ( )

    bus_arrivals.sort( )

    if ( bus_arrivals[n-1] < ride_arrival ):

      waiting_time = 1 - ride_arrival

    else:

      test = 1
      j = 1

      while ( test == 1 ):

        if ( ride_arrival < bus_arrivals[j] ):
          waiting_time = bus_arrivals[j] - ride_arrival
          test = 0
        else:
          j = j + 1

    total_waiting_time = total_waiting_time + waiting_time

  total_waiting_time = total_waiting_time / trial_num

  print ( '' )
  print ( '  Estimated waiting time = ', total_waiting_time )
  print ( '  Theoretical time = ', 1.0 / ( n + 1 ) )

  return

def car ( trial_num, n, rng ):

#*****************************************************************************80
#
## car() estimates probability I am my nearest neighbor's nearest neighbor.
#
#  Discussion:
#
#    Park N cars in a line, and compute each car's nearest neighbor.
#
#    Estimate the probability that a given car is the nearest neighbor
#    of its nearest neighbor.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer N, the number of cars.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'car():' )
  print ( '  Park', n, 'cars in a line, and compute each car\'s nearest neighbor' )
  print ( '  Estimate the probability that a given car is the nearest neighbor' )
  print ( '  of its nearest neighbor.' )

  total_mn = 0

  for loop in range ( 0, trial_num ):

    pos = rng.random ( size = n )
#
#  Sort.
#
    pos.sort ( )
#
#  Find nearest neighbor.
#
    nn = np.zeros ( n )

    nn[0] = 2
    nn[n-1] = n - 1
    for j in range ( 2, n ):
      if ( pos[j-1] - pos[j-2] < pos[j] - pos[j-1] ):
        nn[j-1] = j - 1
      else:
        nn[j-1] = j + 1

    mn = 0
    if ( nn[1] == 1 ):
      mn = mn + 1

    j = 2
    while ( j < n ):
      if ( nn[j-1] == j + 1 and nn[j] == j ):
        mn = mn + 1
        j = j + 2
      else:
        j = j + 1

    total_mn = total_mn + mn

  total_mn = 2 * total_mn / n / trial_num

  print ( '' )
  print ( '  Estimated probability   = ', total_mn )
  print ( '  Theoretical probability = ', 2/3 )

  return

def chess ( trial_num, p, q, rng ):

#*****************************************************************************80
#
## chess() compares two options for a chess tournament.
#
#  Discussion:
#
#    Player A must play three games of chess, against players B and C.
#    C is the stronger player.
#    A has a choice of two schedules of opponents: BCB or CBC.
#    A will win the tournament by winning two games in immediate succession.
#    What is the better schedule?
#
#  Examples:
#
#    Theoretical results include:
#
#      P    Q      P1      P2
#
#    0.9  0.8  0.7920  0.8640
#    0.9  0.4  0.3960  0.5760
#    0.4  0.3  0.1920  0.2040
#    0.4  0.1  0.0640  0.0760
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#   
#  Input:
#
#    integer trial_num: the number of trials.
#
#    real P, the probability that A will beat B in one game.
#
#    real Q, the probability that A will beat C in one game.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'chess():' )
  print ( '  A has to play three games of chess against B and C.' )
  print ( '  A beats B with probability P, C with probability Q' )
  print ( '  A has a choice of schedules: BCB or CBC.' )
  print ( '  To win the tournament, A must win two successive games.' )
  print ( '  Which schedule is better?' )

  prob = np.array ( [ \
    [ p, q, p ], \
    [ q, p, q ] ] )

  won_game = np.zeros ( [ 2, 3 ] )
  won_matches = np.zeros ( 2 )

  for loop in range ( 0, trial_num ):

    won_game = np.zeros ( [ 2, 3 ] )

    result = rng.random ( size = 3 )

    for game in range ( 0, 3 ):
      for sequence in range ( 0, 2 ):
        if ( result[game] < prob[sequence,game] ):
          won_game[sequence,game] = 1

    for sequence in range ( 0, 2 ):
      if ( won_game[sequence,0] + won_game[sequence,1] == 2 or \
           won_game[sequence,1] + won_game[sequence,2] == 2 ):
        won_matches[sequence] = won_matches[sequence] + 1

  won_matches[0] = won_matches[0] / trial_num
  won_matches[1] = won_matches[1] / trial_num

  print ( '' )
  print ( '  Estimated win probability for BCB is = ', won_matches[0] )
  print ( '  Estimated win probability for CBC is = ', won_matches[1] )

  return

def committee ( trial_num, rng ):

#*****************************************************************************80
#
## committee() simulates the committee problem.
#
#  Discussion:
#
#    From a faculty of 6 professors, 6 associate professors, 10
#    assistant professors, and 12 instructors, a committee of size 6
#    is formed randomly.  What is the probablity that there is at least
#    one person of each rank in the committee?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'committee():' )
  print ( '  From a faculty of 6 professors, 6 associate professors, 10' )
  print ( '  assistant professors, and 12 instructors, a committee of size 6' )
  print ( '  is formed randomly.  What is the probablity that there is at least' )
  print ( '  one person of each rank in the committee?' )

  structure = 0

  for loop in range ( 0, trial_num ):

    count = 0

    select = np.zeros ( 6 )
    mix = rng.permutation ( 34 )
    select[0:6] = mix[0:6]

    rank = np.ones ( 4 )

    for i in range ( 0, 6 ):

      if ( select[i] < 6 ):
        count = count + rank[0]
        rank[0] = 0
      elif ( 6 <= select[i] and select[i] < 12 ):
        count = count + rank[1]
        rank[1] = 0
      elif ( 12 <= select[i] and select[i] < 22 ):
        count = count + rank[2]
        rank[2] = 0
      else:
        count = count + rank[3]
        rank[3] = 0

    if ( count == 4 ):
      structure = structure + 1

  structure = structure / trial_num

  print ( '' )
  print ( '  Estimated probability  = ', structure )
  print ( '  Theoretical probablity = ', 1 - 835144/1344904 )

  return

def deli ( lam, mu, clerk_count, rng ):

#*****************************************************************************80
#
## deli() simulates the operation of a deli.
#
#  Discussion:
#
#    A deli is open for 36,000 seconds.
#    There are 1 or 2 clerks.
#    Customers arrive at random.
#    The amount of time it takes to service a customer is random.
#    Customers are served in order.
#    A clerk serves one customer at a time.
#    Newly arrived customers wait in a queue if no clerk is available.
#    What is the average and maximal times spent per customer?
#    What is the average and maximal queue length?
#    What percentage of time are the clerks idle?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    real LAM, the average customer arrival rate per hour.
#
#    real MU, the average customer service rate per hour.
#
#    integer CLERK_COUNT, is 1 or 2, the number of clerks.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'deli():' )
  print ( '  A deli is open for 36,000 seconds.' )
  print ( '  There are 1 or 2 clerks.' )
  print ( '  Customers arrive at random.' )
  print ( '  The amount of time it takes to service a customer is random.' )
  print ( '  Customers are served in order.' )
  print ( '  A clerk serves one customer at a time.' )
  print ( '  Newly arrived customers wait in a queue if no clerk is available.' )
  print ( '  What is the average and maximal times spent per customer?' )
  print ( '  What is the average and maximal queue length?' )
  print ( '  What percentage of time are the clerks idle?' )

  clock = 0
  clerk_busy1 = 0
  clerk_busy2 = 0
  queue_length = 0
  service_time_remaining1 = 0
  service_time_remaining2 = 0
  queue = np.zeros ( [ 2, 300 ] )
  clerk_idle_time1 = 0
  clerk_idle_time2 = 0

  close_deli = int ( np.ceil ( lam * 30 ) )

  customer_arrival_time = np.zeros ( close_deli, dtype = int )
  customer_arrival_time[0] = int ( np.ceil ( - 3600 * np.log ( rng.random ( ) ) / lam ) )
  for i in range ( 1, close_deli ):
    customer_arrival_time[i] = customer_arrival_time[i-1] \
      + int ( np.ceil ( - 3600 * np.log ( rng.random ( ) ) / lam ) )

  customer_service_time = np.zeros ( close_deli, dtype = int )
  for i in range ( 0, close_deli ):
    customer_service_time[i] = int ( np.ceil ( - 3600 * np.log ( rng.random ( ) ) / mu ) )

  total_time = 0
  max_total_time = 0
  total_queue_length = 0
  max_queue_length = 0
  new_customer = 0

  if ( clerk_count == 1 ):
    clerk_busy2 = 1
    service_time_remaining2 = 10 ** 10

  while ( clock < 36000 ):

    if ( 0 < service_time_remaining1 ):
      service_time_remaining1 = service_time_remaining1 - 1

    if ( 0 < service_time_remaining2 ):
      service_time_remaining2 = service_time_remaining2 - 1

    if ( ( clerk_busy1 == 0 or clerk_busy2 == 0 ) and ( 0 < queue_length ) ):
      if ( clerk_busy1 == 0 ):
        clerk_busy1 = 1
        service_time_remaining1 = queue[1,0]
      else:
        clerk_busy2 = 1
        service_time_remaining2 = queue[1,0]

      total_time = total_time + queue[0,0] + queue[1,0]

      if ( max_total_time < queue[0,0] + queue[1,0] ):
        max_total_time = queue[0,0] + queue[1,0]

      for i in range ( 0, queue_length - 1 ):
        queue[0,i] = queue[0,i+1]
        queue[1,i] = queue[1,i+1]

      queue_length = queue_length - 1

    if ( ( clock == customer_arrival_time[new_customer] ) and \
      ( clerk_busy1 == 0 or clerk_busy2 == 0 ) ):

      if ( clerk_busy1 == 0 ):
        clerk_busy1 = 1
        service_time_remaining1 = customer_service_time[new_customer]
      else:
        clerk_busy2 = 1
        service_time_remaining2 = customer_service_time[new_customer]

      total_time = total_time + customer_service_time[new_customer]

      if ( max_total_time < customer_service_time[new_customer] ):
        max_total_time = customer_service_time[new_customer]

      new_customer = new_customer + 1

    elif ( ( clock == customer_arrival_time[new_customer] ) and \
      ( clerk_busy1 == 1 and clerk_busy2 == 1 ) ):

      queue_length = queue_length + 1
      print ( 'clock = ', clock, 'queue_length =', queue_length )
      queue[0,queue_length-1] = 1
      queue[1,queue_length-1] = customer_service_time[new_customer]
      new_customer = new_customer + 1

    if ( clerk_busy1 == 0 ):
      clerk_idle_time1 = clerk_idle_time1 + 1

    if ( clerk_busy2 == 0 ):
      clerk_idle_time2 = clerk_idle_time2 + 1

    for i in range ( 0, queue_length ):
      queue[0,i] = queue[0,i] + 1

    if ( service_time_remaining1 == 0 ):
      clerk_busy1 = 0

    if ( service_time_remaining2 == 0 ):
      clerk_busy2 = 0

    total_queue_length = total_queue_length + queue_length

    if ( max_queue_length < queue_length ):
      max_queue_length = queue_length

    clock = clock + 1

  print ( '' )
  print ( '  Average total time at deli', total_time / ( new_customer - 1 - queue_length ) )
  print ( '  Maximum time at deli      ', max_total_time )
  print ( '  Average queue length      ', total_queue_length / clock )
  print ( '  Maximum queue length      ', max_queue_length )
  print ( '  Percent idle time clerk1  ', 100 * clerk_idle_time1 / clock )
  print ( '  Percent idle time clerk2  ', 100 * clerk_idle_time2 / clock )

  return


def dinner ( ):

#*****************************************************************************80
#
## dinner() simulates the dinner table label problem.
#
#  Discussion:
#
#    N guests sit down at a dinner table, without noticing the name tags.
#    What are the chances that no one sits at their assigned seat?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
  import numpy as np

  print ( '' )
  print ( 'dinner():' )
  print ( '  N guests sit down at a dinner table, without noticing the name tags.' ) 
  print ( '  What are the chances that no one sits at their assigned seat?' )

  pkzero = np.zeros ( 20 )
  pkone = np.zeros ( 20 )

  pkone[0] = 1
  for n in range ( 2, 21 ):
    pkzero[n-1] = ( ( n - 1 ) / n ) * pkone[n-2]
    pkone[n-1] = pkzero[n-2] / n + ( n - 1 ) * pkone[n-2] / n

  print ( '' )
  print ( '  N  P(derangement)' )
  print ( '' )
  for n in range ( 0, 20 ):
    print ( '  %2d  %20.16g' % ( n + 1, pkzero[n] ) )

  return

def dish ( trial_num, rng ):

#*****************************************************************************80
#
## dish() counts how often a single dishwasher breaks 4 out of 5 dishes.
#
#  Discussion:
#
#    Five dishwashers are at work.  During the week, 5 dishes are broken.
#    What are the chances that at least 4 out of 5 dishes are broken
#    by the same clumsy dishwasher?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'dish():' )
  print ( '  Five dishwashers work together.  Five dishes are broken.' )
  print ( '  What are the chances that at least four of the dishes' )
  print ( '  are broken by the same particular dishwasher?' )

  clumsy = 0

  for k in range ( 0, trial_num ):

    broken_dishes = 0
    for j in range ( 0, 5 ):
      r = rng.random ( )
      if ( r < 0.2 ):
        broken_dishes = broken_dishes + 1

    if ( 3 < broken_dishes ):
      clumsy = clumsy + 1

  clumsy = clumsy / trial_num

  print ( '' )
  print ( '  Probability dishwasher #1 breaks at least 4 out of 5 dishes = ', clumsy )
  print ( '  Theoretical probability is ', 21 / 3125 )

  return

def easywalk ( m ):

#*****************************************************************************80
#
## easywalk() exactly analyzes a walk from the corner of (M+1,M+1) to (1,1).
#
#  Discussion:
#
#    A pedestrian begins M blocks east and M blocks north of a destination.
#    At each intersection, there is a stop light which is set randomly,
#    and switches after 1 minute.
#    Until reaching avenue 1 or street 1, the pedestrian always crosses
#    the intersection in accordance with the stop light.
#    Thereafter, the pedestrian must wait at each stop light encountered.
#    What is the average wait for stop lights?
#
#  Example:
#
#      M       Time
#
#      2    0.75
#      5    1.23046875
#     10    1.762
#     20    2.5074
#     50    3.97946
#    100    5.6348479
#   1000   17.839
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer M, the number of blocks east and north.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'easywalk():' )
  print ( '  A pedestrian begins', m, 'blocks east and', m, 'blocks north of a destination.' )
  print ( '  At each intersection, there is a stop light which is set randomly,' )
  print ( '  and switches after 1 minute.' )
  print ( '  Until reaching avenue 1 or street 1, the pedestrian always crosses' )
  print ( '  the intersection in accordance with the stop light.' )
  print ( '  Thereafter, the pedestrian must wait at each stop light encountered.' )
  print ( '  What is the exact expected wait for stop lights?' )
  print ( '  Use graphics to display the expected results.' )

  E = np.zeros ( [ m + 1, m + 1 ] )

  for j in range ( 0, m + 1 ):
    E[j,0] = j / 2
    E[0,j] = j / 2

  for k in range ( 1, m + 1 ):
    for j in range ( 1, m + 1 ):
      E[j,k] = ( E[j-1,k] + E[j,k-1] ) / 2

  x = np.zeros ( m + 1 )
  y = np.zeros ( m + 1 )
  for k in range ( 0, m + 1 ):
    x[k] = k + 1
    y[k] = E[k,k]
#
#  Graphics.
#
  plt.clf ( )
  plt.plot ( x, y, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'easywalk' )
  plt.xlabel ( 'MxM city blocks' )
  plt.ylabel ( 'Expected number of stoplights to wait for.' )
  filename = 'easywalk.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
 
  return

def election ( trial_num, N, n, m, may_vote_for_self, rng ):

#*****************************************************************************80
#
## election() models papal and imperial elections.
#
#  Discussion:
#
#    N voters participate in an election.
#    n of the voters are candidates.
#    Voting rules may allow a voter to vote for themselves, or not.
#    M votes are required in order for a leader to be chosen.
#    What is the probability that, on a single vote, a leader will be chosen?
#
#  Example:
#
#    N  n  m  self  leader
#
#    3  2  2     0   1.000
#    3  2  2     1   1.000
#    3  3  2     0   0.750
#    3  3  2     1   0.778
#    7  7  4     0   0.05989
#    7  7  4     1   0.07099
#   25  2 17     0   0.09278
#   25  2 17     1   0.10891
#   25  3 17     0   0.00094
#   25  3 17     1   0.00115
#   25  4 17     0   0.00004
#   25  4 17     1   0.00005
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer N, the number of voters.
#
#    integer n, the number of candidates.
#
#    integer m, the number of votes required for a leader.
#
#    logical, may_vote_for_self, is 1 if a voter may vote for themself.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'election():' )
  print ( '  ', n, ' voters participate in an election.' )
  print ( '  n of the voters are candidates.' )
  print ( '  Voting rules may allow a voter to vote for themselves, or not.' )
  print ( '  ', m, ' votes are required in order for a leader to be chosen.' )
  print ( '  What is the probability that, on a single vote, a leader will be chosen?' )

  leader = 0
 
  for loop in range ( 0, trial_num ):

    result = np.zeros ( n )

    for ballot in range ( 0, N ):

      select = rng.integers ( low = 0, high = n, endpoint = False )

      if ( not may_vote_for_self ):
        while ( select == ballot ):
          select = rng.integers ( low = 0, high = n, endpoint = False )

      result[select] = result[select] + 1

    most = np.max ( result )
    if ( m <= most ):
      leader = leader + 1

  leader = leader / trial_num

  print ( '' )
  print ( '  Probability a leader was selected =', leader )

  return

def estimate ( trial_num, rng ):

#*****************************************************************************80
#
## estimate() estimates the number of runners in a marathon.
#
#  Discussion:
#
#    N runners participate in a marathon.
#    Each runner wears a tag with their index, from 1 to N.
#    We observe the values of K of these tags.
#    We want to estimate N.
#
#  Modified:
#
#    17 January 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
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
  print ( 'estimate():' )
  print ( '  N runners participate in a marathon.' )
  print ( '  Each runner wears a tag with their index, from 1 to N.' )
  print ( '  We observe the values of K of these tags.' )
  print ( '  We want to estimate N.' )
  print ( '' )
  print ( '  Produce illustrative plots for several cases.' )

  fig, axs = plt.subplots ( 2, 2 )

  sizes = np.array ( [ [ 2, 5 ], [ 10, 20 ] ] )

  for i in range ( 0, 2 ):
    for j in range ( 0, 2 ):

      s = sizes[1,j]
      error = np.zeros ( trial_num )

      for loop in range ( 0, trial_num ):

        N = rng.integers ( low = 900, high = 1000, endpoint = True )
        population = rng.permutation ( N )
        n = ( s * N ) // 100
        new_N = N
        new_n = n
        observed = np.zeros ( n )
        jj = 1

        for k in range ( 1, N + 1 ):
          p = new_n / new_N
          new_N = new_N - 1
          if ( rng.random ( ) < p ):
            observed[jj-1] = population[k-1]
            jj = jj + 1
            new_n = new_n - 1

        maximum = np.max ( observed )
        error[loop-1] = ( ( ( n + 1 ) / n ) * maximum - 1 - N ) * 100 / N

      axs[i,j].hist ( error, 100 )
#     axs[i,j].xlabel ( 'Percent error' )
#     axs[i,j].ylabel ( 'Number of simulations' )
      label =  'sample size' + str ( sizes[i,j] )
      axs[i,j].set_title ( label )

  filename = 'estimate.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def floss ( n ):

#*****************************************************************************80
#
## floss() considers the dental floss problem.
#
#  Discussion:
#
#    A person buys two rolls of dental floss.
#    Each roll supplies N feet of floss.
#    The person randomly selects a roll and takes 1 foot of floss.
#    When one roll runs out, how many feet remain in the other roll?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer N, the number of feet of floss in a full roll.
#
  from scipy.special import comb

  print ( '' )
  print ( 'floss():' )
  print ( '  A person buys two rolls of dental floss.' )
  print ( '  Each roll has', n, 'feet of floss.' )
  print ( '  The person randomly selects a roll and takes 1 foot of floss.' )
  print ( '  When one roll runs out, how many feet remain in the other roll?' )

  total = 0
  for k in range ( 1, n + 1 ):
    total = total + k * comb ( 2 * n - k - 1, n - k ) / ( 2 ** ( 2 * n - k - 1 ) )

  print ( '' )
  print ( '  Average remaining floss =', total )
 
  return

def forgetful_burglar ( trial_num, rng ):

#*****************************************************************************80
#
## forgetful_burglar(): the forgetful burglar problem.
#
#  Discussion:
#
#    In a town of 201 homes, a burglar starts at home 101.
#    He randomly moves one or two homes left or right.
#    What is the typical number of moves he will make before revisiting a home?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'forgetful_burglar():' )
  print ( '  In a town of 201 homes, a burglar starts at home 101.' )
  print ( '  He randomly moves one or two homes left or right.' )
  print ( '  What is the typical number of moves he will make before revisiting a home?' )

  duration = np.zeros ( 50 )

  for loop in range ( 0, trial_num ):

    go = True
    here_you_are = 100
    where_youve_been = np.zeros ( 201 )
    where_youve_been[here_you_are] = 1

    steps = 0

    while ( go ):

      r = rng.random ( )

      if ( r < 0.25 ):
        here_you_are = here_you_are - 2
      elif ( r < 0.5 ):
        here_you_are = here_you_are - 1
      elif ( r < 0.75 ):
        here_you_are = here_you_are + 1
      else:
        here_you_are = here_you_are + 2

      if ( where_youve_been[here_you_are] == 1 ):
        go = False
        duration[steps] = duration[steps] + 1
      else:
        where_youve_been[here_you_are] = 1

      steps = steps + 1

  duration = duration / trial_num

  print ( '' )
  print ( '   K    Prob(K)' )
  print ( '' )
  for k in range ( 0, 10 ):
    print ( '  %2d  %g' % ( k + 1, duration[k] ) )
#
#  Graphics.
#
  s = np.linspace ( 0, 49, 50 )
  plt.clf ( )
  plt.bar ( s, duration )
  plt.grid ( True )
  plt.title ( 'Forgetful Burglar:' )
  plt.xlabel ( 'Number of burglaries before repeat' )
  plt.ylabel ( 'Probability' )
  filename = 'fb.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def gameb ( trial_num, rng ):

#*****************************************************************************80
#
## gameb(): Game B of Parrondo's paradox.
#
#  Discussion:
#
#    In game B, you have two biased coins.  If, at the time just before you
#    decide to flip, your capital M is a multiple of 3 dollars, you chose
#    coin 1, which shows heads with probability 1/10 - epsilon, otherwise
#    you choose coin 2, which shows heads with probability 3/4 - epsilon.
#
#    Game B is a losing game for you, and this code simply demonstrates
#    that using many simulations.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
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
  print ( 'gameb():' )
  print ( '  In game B, you have two biased coins.  If, at the time just before you' )
  print ( '  decide to flip, your capital M is a multiple of 3 dollars, you chose' )
  print ( '  coin 1, which shows heads with probability 1/10 - epsilon, otherwise' )
  print ( '  you choose coin 2, which shows heads with probability 3/4 - epsilon.' )
  print ( '  Game B is a losing game for you, and this code simply demonstrates' )
  print ( '  that using many simulations.' )
  print ( '' )
  print ( '  Produce a plot showing how the player loses.' )

  epsilon = 0.005
  mtotal = np.zeros ( 100 )

  for loop in range ( 0, trial_num ):

    m = 0
    sample_function = np.zeros ( 100 )

    for flips in range ( 0, 100 ):

      if ( ( m % 3 ) == 0 ):
        outcome = rng.random ( )
        if ( outcome < 0.1 - epsilon ):
          m = m + 1
        else:
          m = m - 1
      else:
        outcome = rng.random ( )
        if ( outcome < 0.75 - epsilon ):
          m = m + 1
        else:
          m = m - 1

      sample_function[flips] = m

    mtotal = mtotal + sample_function

  mtotal = mtotal / trial_num
#
#  Graphics.
#
  plt.clf ( )
  flips = np.linspace ( 1, 100, 100 )
  plt.plot ( flips, mtotal, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'Parrondo Paradox' )
  plt.xlabel ( 'Number of coin flips' )
  plt.ylabel ( 'Ensemble average of capital.' )
  filename = 'gameb.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
 
  return

def gs ( trial_num, n, rng ):

#*****************************************************************************80
#
## gs(): the Gamow-Stern elevator problem.
#
#  Discussion:
#
#    A building has 7 floors, and there are n elevators, each of which
#    is at a randomly chosen floor.
#    A person on floor 2 requests an elevator, wishing to go up.
#    What is the probability that the first elevator to arrive is going down?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer N, the number of elevators.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'gs():' )
  print ( '  A building has 7 floors, and there are n elevators, each of which' )
  print ( '  is at a randomly chosen floor.' )
  print ( '  A person on floor 2 requests an elevator, wishing to go up.' )
  print ( '  What is the probability that the first elevator to arrive is going down?' )

  G = 1 / 6

  total_going_down = 0
  elevator = np.zeros ( [ n, 4 ] )

  for loop in range ( 0, trial_num ):

    for j in range ( 0, n ):

      if ( rng.random ( ) < 0.5 ):
        elevator[j,0] = 0
      else:
        elevator[j,0] = 1

      elevator[j,1] = rng.random ( )

      if ( elevator[j,1] < G ):

        if ( elevator[j,0] == 0 ):
          elevator[j,2] = G + elevator[j,1]
        else:
          elevator[j,2] = G - elevator[j,1]

        elevator[j,3] = 1

      else:

        if ( elevator[j,0] == 0 ):
          elevator[j,2] = elevator[j,1] - G
        else:
          elevator[j,2] = ( 11 / 6 ) - elevator[j,1]

        elevator[j,3] = 0

    minn = elevator[0,2]
    index = 0
    for k in range ( 1, n ):
      if ( elevator[k,2] < minn ):
        minn = elevator[k,2]
        index = k

    if ( elevator[index,3] == 0 ):
      total_going_down = total_going_down + 1

  total_going_down = total_going_down / trial_num

  print ( '' )
  print ( '  Estimated probability of down elevator = ', total_going_down )
  print ( '  Theoretical probability is ', 0.5 + 0.5 * ( 2/3 ) ** n )

  return

def guess_rank ( trial_num, m, rng ):

#*****************************************************************************80
#
## guess_rank() estimates the average result of randomly guessing ranks of M items.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer m: the number of items to be ranked.
#
#    rng(): the current random number generator.
#

  print ( '' )
  print ( 'guess_rank():' )
  print ( '  Given  M = ', m, 'items of ranks 1 through M,' )
  print ( '  randomly guess the rank of each item. ' )
  print ( '  On average, how many ranks will we guess correctly?' )

  total_correct = 0

  for k in range ( 0, trial_num ):

    correct = 0
    term = rng.permutation ( m )

    for j in range ( 0, m ):
      if ( term[j] == j ):
        correct = correct + 1

    total_correct = total_correct + correct

  print ( '' )
  print ( '  Average number of correct pairings =', total_correct / trial_num )
  print ( '  Expected value is 1.' )

  return

def jury ( trial_num, rng ):

#*****************************************************************************80
#
## jury() estimates the probability that an appeals court makes a mistake.
#
#  Discussion:
#
#    There are 5 judges on an appeals court.
#    Each judge has a probability of making a correct ruling.
#    What is the probability that a majority of the judges will rule incorrectly?
#
#    Variation: suppose the worst judge (#5) always simply agrees with the
#    best judge (#1).  How does this change the probability?
#
#  Example:
#
#    With the given data, the probability of a mistaken judgement should
#    be about 0.0070419.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'jury():' )
  print ( '  There are 5 judges on an appeals court.' )
  print ( '  Each judge has a probability of making a correct ruling.' )
  print ( '  What is the probability that a majority of the judges will rule incorrectly?' )

  p = [ 0.95, 0.95, 0.90, 0.90, 0.80 ]

  mistakes = 0

  for loop in range ( 0, trial_num ):

    votes = np.zeros ( 5 )
    for k in range ( 0, 5 ):
      if ( p[k] < rng.random ( ) ):
        votes[k] = 1

    result = np.sum ( votes )
    if ( 2 < result ):
      majority = 1
    else:
      majority = 0
 
    mistakes = mistakes + majority

  mistakes = mistakes / trial_num

  print ( '' )
  print ( '  Probability of a mistaken judgement = ', mistakes )

  return

def kelvin ( trial_num, p, rng ):

#*****************************************************************************80
#
## kelvin() looks at Kelvin's fair results from a biased coin.
#
#  Discussion:
#
#    A biased coin comes up head with probability p.
#    To get a unbiased random value, toss the coin twice.
#    If you get TH, call it heads if you get HT, call it tails.
#    If you get TT or HH, do another double toss.
#    On average, how many double tosses are necessary?
#
#  Example:
#
#     10,000 trials, average number of double tosses is 2.085.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    real p: probability of heads.
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'kelvin():' )
  print ( '  A biased coin comes up heads with probability ', p )
  print ( '  To get a unbiased random value, toss the coin twice.' )
  print ( '  If you get TH, call it heads if you get HT, call it tails.' )
  print ( '  If you get TT or HH, do another double toss.' )
  print ( '  On average, how many double tosses are necessary?' )

  total_number_of_double_tosses = 0

  for loop in range ( 0, trial_num ):

    number_of_double_tosses = 0
    decision = False

    while ( not decision ):

      if ( rng.random ( ) < p ):
        toss1 = 1
      else:
        toss1 = 0

      if ( rng.random ( ) < p ):
        toss2 = 1
      else:
        toss2 = 0

      number_of_double_tosses = number_of_double_tosses + 1

      if ( toss1 + toss2 == 1 ):
        decision = True

    total_number_of_double_tosses = total_number_of_double_tosses + number_of_double_tosses

  total_number_of_double_tosses = total_number_of_double_tosses / trial_num

  print ( '' )
  print ( '  Average number of double tosses = ', total_number_of_double_tosses )
  print ( '  Theoretical value               = ', 1 / 0.48 )

  return

def malt ( trial_num, rng ):

#*****************************************************************************80
#
## malt() estimates the chances that Lil and Bill will meet at the malt shop.
#
#  Discussion:
#
#    Lil and Bill agree to meet in the malt shop between 3:30 and 4:00.
#    Each arrives at a random time.
#    Lil will wait 5 minutes, then leave.
#    Bill will wait 7 minutes, then leave.
#    What is the probability of a meeting?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#

  print ( '' )
  print ( 'malt():' )
  print ( '  Lil and Bill agree to meet in the malt shop between 3:30 and 4:00.' )
  print ( '  Each arrives at a random time.' )
  print ( '  Lil will wait 5 minutes, then leave.' )
  print ( '  Bill will wait 7 minutes, then leave.' )
  print ( '  What is the probability of a meeting?' )

  meetings = 0

  for loop in range ( 0, trial_num ):

    L = 30 * rng.random ( )
    B = 30 * rng.random ( )
#
#  Does the interval [B,B+7] intersect the interval [L,L+5].
#
    if ( B < L and L < B + 7 ):
      meetings = meetings + 1
    elif ( L < B and B < L + 5 ):
      meetings = meetings + 1

  meetings = meetings / trial_num

  print ( '' )
  print ( '  Estimated meeting probability = ', meetings )
  print ( '  Theoretical probability is ', 1 - 1154/1800 )

  return

def missing ( trial_num, A, M, rng ):

#*****************************************************************************80
#
## missing() simulates the missing senator problem.
#
#  Discussion:
#
#    There are 100 senators.
#    A bill needs a majority of present senators to pass.
#    A senators are against the bill.
#    M senators are missing the vote.
#    What is the probability that the bill will be defeated?
#
#  Example:
#
#    A = 49, M = 3, p = 0.12878787
#    A = 49, M = 4, p = 0.06373
#    A = 49, M = 5, p = 0.193845
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer A, M, the number of senators against the bill, and the
#    number who are missing.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'missing():' )
  print ( '  There are 100 senators.' )
  print ( '  A bill needs a majority of present senators to pass.' )
  print ( '  A = ', A, 'senators are against the bill.' )
  print ( '  M = ', M, 'senators are missing the vote.' )
  print ( '  What is the probability that the bill will be defeated?' )

  defeats = 0

  for loop in range ( 0, trial_num ):

    votes = np.zeros ( 100 )
    for k in range ( 0, A ):
      votes[k] = -1

    for k in range ( A, 100 ):
      votes[k] = 1

    for k in range ( 0, M ):

      go = True
      while ( go ):
        j = rng.integers ( low = 0, high = 100, endpoint = False )

        if ( votes[j] != 0 ):
          votes[j] = 0
          go = False

    vote = np.sum ( votes )
    if ( vote < 0 ):
      defeats = defeats + 1

  defeats = defeats / trial_num

  print ( '' )
  print ( '  Probability of defeat = ', defeats )

  return

def monotone ( trial_num, rng ):

#*****************************************************************************80
#
## monotone() computes the expected monotone length of a random sequence.
#
#  Discussion:
#
#    Generate a sequence of random values until the next value is not larger
#    than the previous one.   Estimate the expected average length of
#    this sequence.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'monotone():' )
  print ( '  Expected value of the number of random numbers that' )
  print ( '  can be generated, which are monotone increasing.' )

  total = 0

  for k in range ( 0, trial_num ):

    length = 0
    x_max = 0
    stop = False

    while ( not stop ):

      x = rng.random ( )
      if ( x_max < x ):
        x_max = x
      else:
        stop = True

      length = length + 1

    total = total + length

  total = total / trial_num

  print ( '' )
  print ( '  Extimated expected length = ', total )
  print ( '  Theoretical value is        ', np.exp ( 1.0 ) )

  return

def obtuse ( trial_num, rng ):

#*****************************************************************************80
#
## obtuse() estimates the probability that a random triangle is obtuse.
#
#  Discussion:
#
#    We generate a "random" triangle as half of a rectangle whose
#    height is 1, and whose width is <= L.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'obtuse():' )
  print ( '  Define a "random" triangle as half of a rectangle' )
  print ( '  with height 1 and width <= L.' )
  print ( '  What are the chances the triangle is obtuse?' )

  for L in [ 1.0, 2.0 ]:

    obtuse_num = 0

    print ( '' )
    print ( '  Using value L = ', L )

    for k in range ( 0, trial_num ):

      r = rng.random ( size = 6 )
      r[3:6] = L * r[3:6]

      d1 = ( r[0] - r[1] )**2 + ( r[3] - r[4] )**2
      d2 = ( r[1] - r[2] )**2 + ( r[4] - r[5] )**2
      d3 = ( r[2] - r[0] )**2 + ( r[5] - r[3] )**2

      if ( d2 + d3 <= d1 or \
           d1 + d3 <= d2 or \
           d1 + d2 <= d3 ):
        obtuse_num = obtuse_num + 1

    prob = obtuse_num / trial_num

    print ( '' )
    print ( '  Estimated likelihoood of obtuse triangle = ', prob )
    if ( L == 1.0 ):
      print ( '  Expected value =', 97/150 + np.pi/40 )
    elif ( L == 2.0 ):
      print ( '  Expected value =', 1199/1200 + 13*np.pi/128 - 0.75 * np.log(2) )

  return

def obtuse1 ( trial_num, rng ):

#*****************************************************************************80
#
## obtuse1(): probability that three points in [0,1] define an obtuse triangle.
#
#  Discussion:
#
#    We generate a "random" triangle by choosing two random values to
#    break the unit interval into three pieces.  We ask for the probability
#    that the resulting triangle is obtuse.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
# 
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'obtuse1():' )
  print ( '  Define a "random" triangle by splitting the unit' )
  print ( '  interval into three random pieces.' )
  print ( '  What are the chances the triangle is obtuse?' )

  obtuse_num = 0

  for k in range ( 0, trial_num ):

    point1 = rng.random ( )
    point2 = rng.random ( )

    if ( point2 < point1 ):
      temp = point1
      point1 = point2
      point2 = temp

    a = point1
    b = point2 - point1
    c = 1.0 - point2

    if ( c < a + b and b < a + c and a < b + c ):

      d1 = a**2
      d2 = b**2
      d3 = c**2

      if ( d1 < d2 + d3 and d2 < d1 + d3 and d3 < d1 + d2 ):
        obtuse_num = obtuse_num + 1

  prob = obtuse_num / trial_num

  print ( '' )
  print ( '  Estimated likelihoood of obtuse triangle = ', prob )
  print ( '  Theoretical value is ', 9/4 - 3.0 * np.log ( 2.0 ) )

  return

def optimal ( trial_num, n, top, rng ):

#*****************************************************************************80
#
## optimal() simulates the dating problem.
#
#  Discussion:
#
#    A dating club offers N potential partners.
#    It turns out that any of TOP of these partners would be acceptable.
#    The dater gets 1 date with each partner, but immediately after the
#    date, must either marry that partner, or move to the next date.
#    The dater plans to date a sample of the partners without a marriage
#    offer, and then marry the next partner who is better than all
#    the sample dates. 
#    As the sample size is varied, what are the chances of happiness?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer N, the size of the dating pool.
#
#    integer TOP, the number of acceptable choices.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'optimal():' )
  print ( '  A dating club offers ', n, ' potential partners.' )
  print ( '  It turns out that any of #d of these partners would be acceptable.', top )
  print ( '  The dater gets 1 date with each partner, but immediately after the' )
  print ( '  date, must either marry that partner, or move to the next date.' )
  print ( '  The dater plans to date a sample of the partners without a marriage' )
  print ( '  offer, and then marry the next partner who is better than all' )
  print ( '  the sample dates. ' )
  print ( '  As the sample size is varied, what are the chances of happiness?' )
  print ( '' )
  print ( '  Use graphics to display result.' )

  sample_max = 1 + ( 4 * n ) // 5
  results = np.zeros ( sample_max )

  for sample_size in range ( 0, sample_max ):

    check = np.zeros ( sample_size + 1 )
    success = 0

    for loop in range ( 0, trial_num ):

      order = rng.permutation ( n )
      for j in range ( 0, sample_size + 1 ):
        check[j] = order[j]

      best_in_sample = np.min ( check )
      exit = False
      k = sample_size

      while ( not exit ):

        if ( order[k] < best_in_sample ):
          select = order[k]
          exit = True
        else:
          k = k + 1

        if ( k == n - 1 ):
          select = order[n-1]
          exit = True

      for k in range ( 0, top ):
        if ( select == k ):
          success = success + 1

    results[sample_size] = success

  results = results / trial_num
#
#  Graphics.
#
  s = np.linspace ( 1, sample_max, sample_max )
  plt.clf ( )
  plt.bar ( s, results )
  plt.grid ( True )
  plt.xlabel ( 'Sample lot size' )
  plt.ylabel ( 'Probability of happiness' )
  plt.title ( 'The optimal dating problem.' )
  filename = 'optimal.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def patrol ( trial_num, number, rng ):

#*****************************************************************************80
#
## patrol() simulates the highway patrol car problem.
#
#  Discussion:
#
#    Consider a divided highway, and suppose it could be divided by
#    a grassy median or a concrete barrier.
#    Suppose NUMBER police cars patrol the highway.
#    Suppose an accident occurs at a randomly chosen location and lane.
#    Suppose all patrol cars immediately head towards the accident.
#    If a grassy median, then patrol cars in the wrong lane can 
#    immediately reverse direction.
#    For the concrete barrier, patrol cars in the wrong lane must
#    continue to the end of the highway and then turn around.
#    Estimate the average time required by a patrol car to reach the accident.
#
#  Example:
#
#    Number   Grass Concrete
#
#         1  0.3333   0.9997
#         2  0.2085   0.6671
#         3  0.1500   0.5005
#         4  0.1167   0.3999
#         5  0.0545   0.2001
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer NUMBER, the number of patrol cars.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'patrol():' )
  print ( '  Consider a divided highway, and suppose it could be divided by' )
  print ( '  a grassy median or a concrete barrier.' )
  print ( '  Suppose ', number, ' police cars patrol the highway.' )
  print ( '  Suppose an accident occurs at a randomly chosen location and lane.' )
  print ( '  Suppose all patrol cars immediately head towards the accident.' )
  print ( '  If a grassy median, then patrol cars in the wrong lane can ' )
  print ( '  immediately reverse direction.' )
  print ( '  For the concrete barrier, patrol cars in the wrong lane must' )
  print ( '  continue to the end of the highway and then turn around.' )
  print ( '  Estimate the average time required by a patrol car to reach the accident.' )

  total_grass_distance = 0
  total_concrete_distance = 0

  for loop in range ( 0, trial_num ):

    gdist = np.zeros ( number )
    cdist = np.zeros ( number )
    y = np.zeros ( number )
    patlane = np.zeros ( number )
#
#  Choose the lane in which the accident occurs.
#
    if ( rng.random ( ) < 0.5 ):
      acclane = 1
    else:
      acclane = 2

    x = rng.random ( )
    for k in range ( 0, number ):
      y[k] = rng.random ( )
      if ( rng.random ( ) < 0.5 ):
        patlane[k] = 1
      else:
        patlane[k] = 2

    for k in range ( 0, number ):

      if ( acclane == patlane[k] ):

        if ( acclane == 1 ):

          if ( y[k] < x ):
            gdistance = x - y[k]
            cdistance = x - y[k]
          else:
            gdistance = y[k] - x
            cdistance = 2 + x - y[k]

        else:

          if ( x > y[k] ):
            gdistance = x - y[k]
            cdistance = 2 - x + y[k]
          else:
            gdistance = y[k] - x
            cdistance = y[k] - x

      else:

        if ( patlane[k] == 1 ):
          gdistance = abs ( x - y[k] )
          cdistance = 2 - x - y[k]
        else:
          gdistance = abs ( x - y[k] )
          cdistance = x + y[k]

      gdist[k] = gdistance
      cdist[k] = cdistance

    min_gdistance = np.min ( gdist )
    min_cdistance = np.min ( cdist )
    total_grass_distance = total_grass_distance + min_gdistance
    total_concrete_distance = total_concrete_distance + min_cdistance

  total_grass_distance = total_grass_distance / trial_num
  total_concrete_distance = total_concrete_distance / trial_num

  print ( '' )
  print ( '  Average grass distance    = ', total_grass_distance )
  print ( '  Average concrete distance = ', total_concrete_distance )

  return

def pierror ( trial_num, rng ):

#*****************************************************************************80
#
## pierror() estimates pi by counting random points in a square.
#
#  Discussion:
#
#    The square has area 1, the quarter circle area pi/4.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#    
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'pierror():' )
  print ( '  Estimate pi by counting random points in the unit' )
  print ( '  square which are also in the quarter circle.' )
  print ( '' )

  p = 0
  for k in range ( 0, trial_num ):
    x = rng.random ( )
    y = rng.random ( )
    if ( x**2 + y**2 < 1.0 ):
      p = p + 1

  pi_estimate = p / trial_num
  abs_err = abs ( np.pi - pi_estimate )
 
  print ( '  Points used =      ', trial_num )
  print ( '  Estimate for pi is ', pi_estimate )
  print ( '  Absolute error is  ', abs_err )

  return

def ranking ( trial_num, m, rng ):

#*****************************************************************************80
#
## ranking() simulates the result of guessing on a ranking test.
#
#  Discussion:
#
#    A list of M items is given.
#    The test taker is required to give a rank for each.
#    For each item, the test taker randomly chooses a value between 1 and M.
#    What is the average number of correct rankings?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer m, the number of items to be ranked.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'ranking():' )
  print ( '  A list of M =', m, ' items is given.' )
  print ( '  The test taker is required to give a rank for each.' )
  print ( '  For each item, the test taker randomly chooses a value between 1 and M.' )
  print ( '  What is the average number of correct rankings?' )

  total_correct = 0

  for k in range ( 0, trial_num ):

    correct = 0
    term = np.zeros ( m )
    for j in range ( 0, m ):
      term[j] = int ( np.floor ( m * rng.random ( ) ) )

    for j in range ( 0, m ):
      if ( term[j] == j ):
        correct = correct + 1

    total_correct = total_correct + correct

  total_correct = total_correct / trial_num

  print ( '' )
  print ( '  Average number of correct matches = ', total_correct )

  return

def rhs ( trial_num, rng ):

#*****************************************************************************80
#
## rhs() histograms the random harmonic series.
#
#  Discussion:
#
#    Compute and histogram 50,000 values of the partial sums of 
#      sum ( 1 <= k < infinity ) t(i) / k
#    where t(i) is randomly +1 or -1.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
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
  print ( 'rhs():' )
  print ( '  Random Harmonic Series:' ) 
  print ( '  Compute and histogram many values of the partial sums of ' )
  print ( '    sum ( 1 <= k < infinity ) t(i) / k' )
  print ( '  where t(i) is randomly +1 or -1.' )

  sums = np.zeros ( trial_num )

  for loop in range ( 0, trial_num ):

    total = 0
    for k in range ( 1, 101 ):
      t = rng.random ( )
      if ( t < 0.5 ):
        t = 1.0
      else:
        t = -1.0

      total = total + t / k

    sums[loop] = total
#
#  Graphics
#
  plt.clf ( )
  plt.hist ( sums, bins = 50 )
  plt.xlabel ( 'Partial sums' )
  plt.ylabel ( 'Number of partial sums' )
  plt.title ( 'Random Harmonic Series' )
  plt.grid ( True )
  filename = 'rhs.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def rolls ( ):

#*****************************************************************************80
#
## rolls() simulates the toilet paper problem.
#
#  Discussion:
#
#    Two rolls of toilet paper are installed in a toilet, with 200 sheets.
#    There are two kinds of people, with probabilities p and 1-p.
#      big choosers take one sheet from the larger roll
#      little choosers take one sheet from the smaller roll (unless empty).
#    When one roll becomes empty, how many sheets are on the other roll?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rolls():' )
  print ( '  Two rolls of toilet paper are installed in a toilet, with 200 sheets.' )
  print ( '  There are two kinds of people, with probabilities p and 1-p.' )
  print ( '  * big choosers take one sheet from the larger roll' )
  print ( '  * little choosers take one sheet from the smaller roll (unless empty).' )
  print ( '  When one roll becomes empty, how many sheets are on the other roll?' )
  print ( '  Use graphics to display results.' )

  M = np.zeros ( [ 200, 200 ] )
  curve = np.zeros ( 1000 )
  prob = 0

  for loop in range ( 0, 1000 ):

    prob = prob + 1
    p = prob / 1000
    M[0,0] = 1
    for m in range ( 2, 201 ):
      M[m-1,0] = ( 1.0 - p ) * m + p * M[m-2,0]

    M[1,1] = M[1,0]
    diagonal = 3
    for m in range ( 3, 201 ):
      for n in range ( 2, diagonal ):
        M[m-1,n-1] = p * M[m-2,n-1] + ( 1.0 - p ) * M[m-1,n-2]

      M[m-1,m-1] = M[m-1,m-2]
      diagonal = diagonal + 1

    curve[prob-1] = M[199,199]
#
#  Graphics.
#
  p = np.linspace ( 1, 1000, 1000 ) / 1000.0
  plt.clf ( )
  plt.plot ( p, curve, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'The Toilet Paper Problem' )
  plt.xlabel ( 'p' )
  plt.ylabel ( 'M200(p)' )
  filename = 'rolls.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def smoker ( trial_num, rng ):

#*****************************************************************************80
#
## smoker() considers the two matchbook problem.
#
#  Discussion:
#
#    A smoker buys two packs of 40 matches.
#    He then repeatedly selects a match from a randomly chosen pack.
#    When one pack runs out, how many matches have been used in total?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
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
  print ( 'smoker():' )
  print ( '  A smoker buys two packs of 40 matches.' )
  print ( '  He then repeatedly selects a match from a randomly chosen pack.' )
  print ( '  When one pack runs out, how many matches have been used in total?' )

  total = 0
  matches = np.linspace ( 1, 80, 80 )
  freq = np.zeros ( 80 )

  for k in range ( 0, trial_num ):

    booklet1 = 40
    booklet2 = 40

    while ( 0 < booklet1 and 0 < booklet2 ):

      r = rng.random ( )
      if ( r < 0.5 ):
        booklet1 = booklet1 - 1
      else:
        booklet2 = booklet2 - 1

    s = ( 40 - booklet1 ) + ( 40 - booklet2 )
    total = total + s
    freq[s-1] = freq[s-1] + 1

  ave = total / trial_num

  print ( '' )
  print ( '  Average total number of matches used = ', ave )
#
#  Graphics.
#
  plt.clf ( )
  plt.bar ( matches, freq )
  plt.title ( 'The Smoker Matchbook Problem' )
  plt.grid ( True )
  plt.xlabel ( 'Number of matches removed from both booklets' )
  plt.ylabel ( 'Number of simulations' )
  filename = 'smoker.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def smokerb ( trial_num, rng ):

#*****************************************************************************80
#
## smokerb() considers a second version of the two matchbook problem.
#
#  Discussion:
#
#    A smoker buys two packs of 40 matches.
#    He then repeatedly selects a match from a randomly chosen pack.
#    At some point, the pack he chooses will be empty.
#    How many matches have been used by then?
#
#    This is a variation of the problem, because the process does not stop
#    when a pack is empty, but later, after a pack has been emptied, and
#    then selected again.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
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
  print ( 'smokerb():' )
  print ( '  A smoker buys two packs of 40 matches.' )
  print ( '  He then repeatedly selects a match from a randomly chosen pack.' )
  print ( '  At some point, the pack he chooses will be empty.' )
  print ( '  How many matches have been used by then?' )

  total = 0
  matches = np.linspace ( 1, 80, 80 )
  freq = np.zeros ( 80 )

  for k in range ( 0, trial_num ):

    booklet1 = 40
    booklet2 = 40

    while ( 0 < booklet1 and 0 < booklet2 ):

      r = rng.random ( )
      if ( r < 0.5 ):
        booklet1 = booklet1 - 1
      else:
        booklet2 = booklet2 - 1

    empty = False

    while ( not empty ):
      r = rng.random ( )
      if ( r < 0.5 ):
        if ( 0 < booklet1 ):
          booklet1 = booklet1 - 1
        else:
          empty = True
      else:
        if ( 0 < booklet2 ):
          booklet2 = booklet2 - 1
        else:
          empty = True

    s = ( 40 - booklet1 ) + ( 40 - booklet2 )
    total = total + s
    freq[s-1] = freq[s-1] + 1

  total = total / trial_num
  print ( '' )
  print ( '  Average total number of matches used = ', total )
#
#  Graphics.
#
  plt.clf ( )
  plt.bar ( matches, freq )
  plt.title ( 'The Smoker Matchbook Problem #2' )
  plt.grid ( True )
  plt.xlabel ( 'Number of matches removed from both booklets' )
  plt.ylabel ( 'Number of simulations' )
  filename = 'smokerb.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def spin ( trial_num, rng ):

#*****************************************************************************80
#
## spin() simulates a game involving two spinning disks.
#
#  Discussion:
#
#    A game involves two spinnable disks, each divided into three sectors.
#    A player spins disk 1 or 2 according to the following rules:
#    * if the player spins disk i, and it stops in region Pij, he
#      moves from disk i to disk j
#    * if the spinner stops in region Pi3, the game ends.
#    * if the game ends in P13, the player wins.
#    What is the probablity that the player, starting with disk 1, wins?
#
#  Example:
#
#     10,000 games, P estimate is 0.6574
#    100,000 games, P estimate is 0.6498.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'spin():' )
  print ( '  A game involves two spinnable disks, each divided into three sectors.' )
  print ( '  A player spins disk 1 or 2 according to the following rules:' )
  print ( '  * if the player spins disk i, and it stops in region Pij, he' )
  print ( '    moves from disk i to disk j' )
  print ( '  * if the spinner stops in region Pi3, the game ends.' )
  print ( '  * if the game ends in P13, the player wins.' )
  print ( '  What is the probablity that the player, starting with disk 1, wins?' )

  p = np.array ( [  \
    [ 0.20, 0.40 ], \
    [ 0.30, 0.35 ] ] )

  wins = 0

  for loop in range ( 0, trial_num ):

    keep_going = True
    disk = 0

    while ( keep_going ):

      spin_pointer = rng.random ( )

      if ( spin_pointer < p[disk,0] ):
        disk = 0
      else:
        if ( spin_pointer < p[disk,0] + p[disk,1] ):
          disk = 1
        else:
          keep_going = False
          if ( disk == 0 ):
            wins = wins + 1

  wins = wins / trial_num

  print ( '' )
  print ( '  Probabiity of winning = ', wins )
  print ( '  Theoretical value     = ', 0.65 )

  return

def steve ( trial_num, k, rng ):

#*****************************************************************************80
#
## steve(): Steve's elevator problem.
#
#  Discussion:
#
#    Steve gets on an elevator going up.  There are 11 higher floors.
#    Steve wishes to go up 9 floors.
#    There are K additional riders in the elevator, each of whom has
#    randomly chosen one of the 11 higher floors as destination.
#    On average, how many times will the elevator stop until Steve
#    reaches his floor?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer K, the number of elevator riders in addition to Steve.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'steve():' )
  print ( '  Steve gets on an elevator going up.  There are 11 higher floors.' )
  print ( '  Steve wishes to go up 9 floors.' )
  print ( '  There are', k, 'additional riders in the elevator, each of whom has' )
  print ( '  randomly chosen one of the 11 higher floors as destination.' )
  print ( '  On average, how many times will the elevator stop until Steve' )
  print ( '  reaches his floor?' )

  stop_sum = 0

  for loop in range ( 0, trial_num ):

    x = np.zeros ( 11 )
#
#  Steve is one passenger, going to 8.
#
    x[8] = 1
#
#  Generate k more passengers.
#
    for j in range ( 0, k ):
      rider = rng.integers ( low = 0, high = 11, size = k, endpoint = False )
      x[rider] = 1
#
#  Count the number of stops the elevator will make on the 8 floors previous
#  to 9.
#
    stops = 1 + np.sum ( x[0:8] )

    stop_sum = stop_sum + stops

  stop_sum = stop_sum / trial_num

  print ( '' )
  print ( '  Estimated number of stops = ', stop_sum )
  print ( '  Theoretical number =        ', 9 - 8 * ( 10/11 ) ** k )

  return

def stopping ( n ):

#*****************************************************************************80
#
## stopping() analyzes an optimal stopping problem.
#
#  Discussion:
#
#    From a population of N indexed values, the highest is sought.
#    Values are to be discovered in order of index.
#    When value I is discovered:
#    * it may be rejected, and the next value discovered, or
#    * it may be accepted, and the process is terminated.
#    A strategy is to view S items in a row, and then accept 
#    the very next item that is larger than max(S).
#    Given N, what is S, and what are the chances that this process will
#    produce the maximum?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2018
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer N, the number of choices.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'stopping():' )
  print ( '  From a population of', n, 'indexed values, the highest is sought.' )
  print ( '  Values are to be discovered in order of index.' )
  print ( '  When value I is discovered:' )
  print ( '  * it may be rejected, and the next value discovered, or' )
  print ( '  * it may be accepted, and the process is terminated.' )
  print ( '  A strategy is to view S items in a row, and then accept ' )
  print ( '  the very next item that is larger than max(S).' )
  print ( '  Given N, what is S, and what are the chances that this process will' )
  print ( '  produce the maximum?' )

  prob = np.zeros ( n )

  for r in range ( 2, n + 1 ):
    s = 0
    for j in range ( r, n + 1 ):
      s = s + 1 / ( j - 1 )
    prob[r-1] = ( r - 1 ) * s / n

  index = np.argmax ( prob )
  best = n / index

  print ( '' )
  print ( '  Population size N      = ', n )
  print ( '  Optimal sample size S  = ', index )
  print ( '  Ratio N / S            = ', n / index )
  print ( '  Probability of success = ', prob[index] )

  return

def sylvester_quadrilateral ( trial_num, rng ):

#*****************************************************************************80
#
## sylvester_quadrilateral(): probability 4 random points form concave quadrilateral.
#
#  Discussion:
#
#    The four points are chosen randomly within the unit circle.
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#    
#  Input:
#
#    integer trial_num: the number of trials.
#
#    rng(): the current random number generator.
#
  from scipy.spatial import ConvexHull
  import numpy as np

  print ( '' )
  print ( 'sylvester_quadrilateral():' )
  print ( '  Estimate the probability that four points, chosen' )
  print ( '  uniformly at random in the unit circle, form a ' )
  print ( '  concave (=nonconvex) quadrilateral.' )

  concave = 0

  for k in range ( 0, trial_num ):

    points = np.zeros ( [ 4, 2 ] )

    for i in range ( 0, 4 ):
      r = np.sqrt ( rng.random ( ) )
      theta = 2.0 * np.pi * rng.random ( )
      points[i,0] = r * np.cos ( theta )
      points[i,1] = r * np.sin ( theta )

    hull = ConvexHull ( points )

    if ( len ( hull.vertices ) == 4 ):
      concave = concave + 1

  concave = concave / trial_num

  print ( '' )
  print ( '  Estimated   concave probability = ', concave )
  print ( '  Theoretical concave probability = ', 35 / 12 / np.pi ** 2 )

  return

def umbrella ( trial_num, xi, yi, rng ):

#*****************************************************************************80
#
## umbrella() simulates the umbrella problem.
#
#  Discussion:
#
#    A person has XI umbrellas at home, and YI at the office.
#    With probability P, it will be raining at any given time.
#    If it is raining, the person takes an umbrella from one place to the other.
#    How many walks will the person take before running out of umbrellas?
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer XI, YI, the number of umbrellas at home, and at the office.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'umbrella():' )
  print ( '  A person has XI umbrellas at home, and YI at the office.' )
  print ( '  With probability P, it will be raining at any given time.' )
  print ( '  If it is raining, the person takes an umbrella from one place to the other.' )
  print ( '  How many walks will the person take before running out of umbrellas?' )
  print ( '  Use graphics to display results.' )

  duration = np.zeros ( 99 )

  for P in range ( 1, 100 ):

    p = P / 100
    walk_sum = 0

    for loop in range ( 0, trial_num ):
      x = xi
      y = yi
      walks = 0
      location = -1
      wet = 0

      while ( wet == 0 ):

        if ( p < rng.random ( ) ):

          walks = walks + 1
          location = - location

        else:

          if ( location == -1 ):

            if ( x == 0 ):
              walk_sum = walk_sum + walks
              wet = 1
            else:
              x = x - 1
              walks = walks + 1
              y = y + 1
              location = -location

          else:

            if ( y == 0 ):
              walk_sum = walk_sum + walks
              wet = 1
            else:
              y = y - 1
              walks = walks + 1
              x = x + 1
              location = - location

    duration[P-1] = walk_sum / trial_num
#
#  Graphics.
#
  p = np.linspace ( 1, 99, 99 ) / 100.0
  plt.clf ( )
  plt.plot ( p, duration, linewidth = 3 )
  plt.grid ( True )
  plt.title ( 'umbrella' )
  plt.xlabel ( 'Probability of rain' )
  plt.ylabel ( 'Average number of walks before getting wet' )
  filename = 'umbrella.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def walk ( trial_num, m, rng ):

#*****************************************************************************80
#
## walk() simulates a walk from the corner of (M+1,M+1) to (1,1).
#
#  Discussion:
#
#    A pedestrian begins M blocks east and M blocks north of a destination.
#    At each intersection, there is a stop light which is set randomly,
#    and switches after 1 minute.
#    Until reaching avenue 1 or street 1, the pedestrian always crosses
#    the intersection in accordance with the stop light.
#    Thereafter, the pedestrian must wait at each stop light encountered.
#    What is the average wait for stop lights?
#
#  Example:
#
#      M       Time
#
#      2    0.74936
#      5    1.22906
#     10    1.75866
#     20    2.50673
#     50    3.99415
#    100    5.63352
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
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton, 2008,
#    ISBN: 978-0-691-15821-1.
#
#  Input:
#
#    integer trial_num: the number of trials.
#
#    integer M, the number of blocks east and north.
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'walk():' )
  print ( '  A pedestrian begins M blocks east and M blocks north of a destination.' )
  print ( '  At each intersection, there is a stop light which is set randomly,' )
  print ( '  and switches after 1 minute.' )
  print ( '  Until reaching avenue 1 or street 1, the pedestrian always crosses' )
  print ( '  the intersection in accordance with the stop light.' )
  print ( '  Thereafter, the pedestrian must wait at each stop light encountered.' )
  print ( '  What is the average wait for stop lights?' )

  total_wait = 0

  for loop in range ( 0, trial_num ):

    j = m + 1
    k = m + 1
    wait = 0

    while ( 1 < j and 1 < k ):
      if ( rng.random ( ) < 0.5 ):
        j = j - 1
      else:
        k = k - 1

    if ( j == 1 ):
      z = k
    else:
      z = j

    while ( 1 < z ):
      if ( rng.random ( ) < 0.5 ):
        wait = wait + 1
      z = z - 1

    total_wait = total_wait + wait

  total_wait = total_wait / trial_num

  print ( '' )
  print ( '  Estimated waiting time = ', total_wait )

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
  digital_dice_test ( )
  timestamp ( )

