#! /usr/bin/env python3
#
def high_card_simulation_test ( ):

#*****************************************************************************80
#
## high_card_simulation_test() tests high_card_simulation().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'high_card_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test high_card_simulation().' )

  rng = default_rng ( )

  high_card_simulation_test01 ( rng )
  high_card_simulation_test02 ( rng )
  high_card_simulation_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'high_card_simulation_test()' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def high_card_probability ( n ):

#*****************************************************************************80
#
## high_card_probability() determines winning probabilities for the high card game.
#
#  Discussion:
#
#    The high card game presents the player with a deck of cards, each
#    having an unknown value.  The player is allowed to go throught the
#    deck once, looking at the cards one at a time.  At any time, the player
#    may decide to take a particular card, winning that amount and stopping
#    the game.  If the player continues to the end, by default the last card
#    indicates the amount won.
#
#    An optimal strategy for selecting the highest card is as follows:
#    * look at, but do not select, the first k-1 cards
#    * stop at the first card, from k to n, that is higher than the 
#      first k-1 cards.
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
#    integer N, the number of cards.  
#
#  Output:
#
#    real P(N).  P(K) is the probability that a strategy that skips
#    K-1 cards will win, given that the deck has N cards.
#
  import numpy as np

  p = np.zeros ( n )
  
  for r in range ( 0, n ):
    s = 0.0
    for i in range ( r + 1, n ):
      s = s + 1.0 / i
    p[r] = ( 1 + r * s ) / n

  return p

def high_card_shuffle ( n, rng ):

#*****************************************************************************80
#
## high_card_shuffle() generates a sequence of numeric "cards" for a game.
#
#  Discussion:
#
#    In this game, you know that the deck contains N cards.  You win by 
#    choosing the highest card in the deck.  You don't know what this card
#    is, and you must choose your card by saying "stop" as, one by one,
#    the cards of the deck are exposed.  
#
#    A random guesser would get the high card with probability 1/N.
#
#    An intelligent guesser can do much better.
#
#    It is the goal of this program so "shuffle" a deck of cards suitable
#    for this game.  The problem is that we know the highest card in an
#    ordinary deck.  Let's replace the cards by integers.  Then if we know
#    in advance the range of the cards (say, they must lie between 1 and 
#    1,000), it may be true that we can guess the card that is the maximum.
#
#    However, this program produces a sequence of integer card values for
#    which no information can be gained from the values.  It does this
#    by regarding the card values as binary integers between 1 and 2^N - 1.
#    We can make a perfectly information-free sequence as follows:
#
#      Card 1 sets bit N-1 to 1.
#      Card 2 sets bit N-2 to 1, bit  N-1 randomly.
#      ...
#      Card I sets bit N-I to 1, bits N-1 down to N-I+1 randomly.
#      ...
#      Card N sets bit N-N to 1, bits N-1 down to 1 randomly.
#
#    The I-th card has equal probability to fall in any of the I intervals
#    defined by the I-1 previous cards.  So, knowing the previous cards tells
#    you absolutely nothing about where the next card will fall, and each
#    card is, at the moment you see it, as good a guess for the maximum as
#    the unseen cards.
#
#    For example, the command "high_card_shuffle(7)" might yield
#
#      64    96    80     8     4    82    29
#    or
#      64    32    16    24    12    58    73
#    or
#      64    96    48     8   100    26    93
#    or
#      64    96    16    56    76   122    71
#
#    in which the highest card is #2, #7, #5, or #6 respectively.
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
#    integer N, the number of cards.  N probably needs to be less than 32.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer SEQUENCE(N), a set of N integer values that can be used
#    as the cards in the high card guessing game.
#
  import numpy as np

  if ( 32 <= n ):
    print ( '' )
    print ( 'high_card_shuffle(): Fatal error!' )
    print ( '  This program can only handle N < 32.' )
    raise Exception ( 'high_card_shuffle - Fatal error!' )
 
  sequence = np.zeros ( n )

  for i in range ( 0, n ):
    c = 2 ** ( n - i - 1 )
    k = rng.integers ( low = 0, high = 1, size = i, endpoint = True )
    for j in range ( 0, i ):
      c = c + k[j] * 2 ** ( n - i + j )
    sequence[i] = c

  return sequence

def high_card_simulation ( deck_size, skip_num, trial_num, rng ):

#*****************************************************************************80
#
## high_card_simulation() simulates a game of choosing the highest card in a deck.
#
#  Discussion:
#
#    You are given a deck of DECK_SIZE cards.
#
#    Your goal is to select the high card.  For convenience, we can assume 
#    the cards are a permutation of the integers from 1 to DECK_SIZE, but in
#    fact the user mustn't see such values or else it's obvious which is the
#    largest card.
#
#    However, your choice is made under the following rules:  You may turn over
#    one card at a time.  When a card is turned over, you may declare that to be
#    your choice, or else turn over another card.  If you have not chosen a card
#    by the end, then your choice is the final card.
#
#    If you have no idea what to do, and simply decide in advance to pick
#    a card "at random", that is, for example, you decide to pick the 15th card
#    before having seen any cards, then your probability of winning 
#    is 1/DECK_SIZE.
#
#    The question is, can you do better than that?
#
#    Your strategy is as follows: always look at the first SKIP_NUM cards without
#    choosing them.  Then choose the very next card you encounter that is larger
#    than the cards you skipped.
#
#    Using this program, you can easily see that skipping 5 cards is much better
#    than picking one at random, skipping 10 is even better, and so on.  Of course,
#    you can't skip too many cards, and in fact, the results seem to be best for
#    somewhere around 30 to 35 cards skipped.  For problems like this, the
#    optimal value is somewhere around 1 / e, where E is the base of the natural
#    logarithm system.
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
#    integer DECK_SIZE, the number of cards in the deck.
#    2 <= DECK_SIZE.  Default value is 52
#
#    integer SKIP_NUM, the number of initial cards you plan to examine
#    but will NOT select.  If SKIP_NUM is 0, you don't look at any cards first.
#    0 <= SKIP_NUM < DECK_SIZE.  Default value is DECK_SIZE/3.
#
#    integer TRIAL_NUM, the number of times we will simulate this process.
#    Default value is 100.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P, the estimated probability that your strategy of skipping
#    SKIP_NUM cards and then selecting the next card that is bigger, will
#    result in choosing the highest card.
#
  import numpy as np
#
#  Check values.
#
  if ( deck_size < 2 ):
    print ( '' )
    print ( 'high_card_simulation(): Fatal error!' )
    print ( '  DECK_SIZE must be at least 2.' )
    print ( '  Your value was ', deck_size )
    raise Exception ( 'high_card_simulation(): Fatal error!' )

  skip_num = int ( skip_num )

  if ( skip_num < 0 ):
    skip_num = 0

  if ( deck_size <= skip_num ):
    print ( '' )
    print ( 'high_card_simulation(): Fatal error!' )
    print ( '  SKIP_NUM must be less than DECK_SIZE.' )
    print ( '  Your DECK_SIZE =', deck_size )
    print ( '  Your SKIP_NUM =', skip_num )
    raise Exception ( 'high_card_simulation(): Fatal error!' )

  if ( trial_num < 1 ):
    print ( '' )
    print ( 'high_card_simulation(): Fatal error!' )
    print ( '  TRIAL_NUM must be at least 1.' )
    print ( '  Your value was', trial_num )
    raise Exception ( 'high_card_simulation(): Fatal error!' )

  correct = 0
  
  for trial in range ( 0, trial_num ):

    cards = np.arange ( 0, deck_size )
    cards = rng.permutation ( cards )

    if ( 1 <= skip_num ):
      skip_max = np.max ( cards[0:skip_num] )
    else:
      skip_max = - np.Inf

    true_max = np.max ( cards )
#
#  In case you don't encounter a card larger than SKIP_MAX,
#  we'll assume you pick the last card in the deck, even though
#  you know it's a loser.
#
    choice = cards[deck_size-1]
#
#  Turn over the remaining cards in the deck, but stop
#  immediately when you find one bigger than SKIP_MAX.
#
    for card in range ( skip_num + 1, deck_size ):
      if ( skip_max < cards[card] ):
        choice = cards[card]
        break
#
#  Record successful choices.
#
    if ( choice == true_max ):
      correct = correct + 1
#
#  Estimate the probability.
#
  p = correct / trial_num

  return p

def high_card_simulation_test01 ( rng ):

#*****************************************************************************80
#
## high_card_simulation_test01() varies the skip number.
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
#    rng(): the current random number generator.
#
  import numpy as np

  deck_size = 100
  trial_num = 100

  print ( '' )
  print ( 'high_card_simulation_test01():' )
  print ( '  Using', deck_size, 'cards and', trial_num, 'trials,' )
  print ( '  estimate the chances of' )
  print ( '  picking the high card by skipping a given number of initial cards.' )
  print ( '' )
  print ( '  Skip   Deck Size    Chance of Winning' )
  print ( '' )

  for i in range ( 0, 10 ):

    skip_num = 1 + np.floor ( i * deck_size / 10 )

    p = high_card_simulation ( deck_size, skip_num, trial_num, rng )

    print ( '  %3d  %3d  %12g' % ( skip_num, deck_size, p ) )

  return

def high_card_simulation_test02 ( rng ):

#*****************************************************************************80
#
## high_card_simulation_test02() plots the results for a deck of 100 cards.
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
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  deck_size = 100
  trial_num = 1000

  print ( '' )
  print ( 'high_card_simulation_test02():' )
  print ( '  Using', deck_size, 'cards and', trial_num, 'trials,' )
  print ( '  compute the chances of picking the high card with ' )
  print ( '  a skip of 0 through 99.' )

  s = np.zeros ( deck_size )
  p = np.zeros ( deck_size )

  for i in range ( 0, deck_size - 1 ):
    s[i] = i
    p[i] = high_card_simulation ( deck_size, s[i], trial_num, rng )

  plt.clf ( )
  plt.plot ( s, p, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.title ( 'Estimated chance of winning per given skip number' )
  plt.xlabel ( 'Number of cards to skip before choice' )
  plt.ylabel ( 'Chance of correct choice.' )
  filename = 'high_card_simulation_test02.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def high_card_simulation_test03 ( ):

#*****************************************************************************80
#
## high_card_simulation_test03() plots the results for a deck of 100 cards.
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
  import matplotlib.pyplot as plt
  import numpy as np

  deck_size = 100

  print ( '' )
  print ( 'high_card_simulation_test03():' )
  print ( '  high_card_probability() computes the exact probability of ' )
  print ( '  winning a high card game with a deck of', deck_size, 'cards' )
  print ( '  assuming we skip the first K cards and select the next card' )
  print ( '  that is bigger.' )

  s = np.arange ( 0, deck_size )
  p = high_card_probability ( deck_size )

  print ( '' )
  print ( '    K   Prob(K)' )
  print ( '' )
  for i in range ( 0, deck_size ):
    print ( '  %3d  %8g' % ( s[i], p[i] ) )

  plt.clf ( )
  plt.plot ( s, p, 'r', linewidth = 2 )
  plt.grid ( True )
  plt.title ( 'Exact chance of winning per given skip number' )
  plt.xlabel ( 'Number of cards to skip before choice' )
  plt.ylabel ( 'Chance of correct choice.' )
  filename = 'high_card_simulation_test03.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

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
  high_card_simulation_test ( )
  timestamp ( )

