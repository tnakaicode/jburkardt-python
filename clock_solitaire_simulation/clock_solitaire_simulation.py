#! /usr/bin/env python3
#
def card_rank ( n ):

#*****************************************************************************80
#
## card_rank() is given the index of a card and returns its rank.
#
#  Discussion:
#
#    The index and rank are 0-based.
#
#    index:  0  1  2  3  4  5  6  7  8  9 10 11 12
#           13 14 15 16 17 19 19 20 21 22 23 24 25
#           26 27 28 29 30 31 32 33 34 35 36 37 38
#           39 40 41 42 43 44 45 46 47 48 49 50 51
#           --------------------------------------
#    rank:   0  1  2  3  4  5  6  7  8  9 10 11 12
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the index of the card.  0 <= index <= 51.
#
#  Output:
#
#    integer R: the rank of the card.  0 <= r <= 12.
#
  r = n % 13

  return r

def card_suit ( card_index ):

#*****************************************************************************80
#
## card_suit() is given the index of a card and returns its suit.
#
#  Discussion:
#
#    The index is 0-based.
#                                                   Suit:
#    index:  0  1  2  3  4  5  6  7  8  9 10 11 12   'H'
#           13 14 15 16 17 19 19 20 21 22 23 24 25   'C'
#           26 27 28 29 30 31 32 33 34 35 36 37 38   'D'
#           39 40 41 42 43 44 45 46 47 48 49 50 51   'S'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer card_index: the card index.  0 <= index <= 51.
#
#  Output:
#
#    character S: the card suit.  suit is 'H', 'C', 'D' or 'S'.
#
  suits = [ 'H', 'C', 'D', 'S' ]
  suit_index = int ( card_index // 13 )
  s = suits[suit_index]

  return s

def card_symbol ( card_index, card_used ):

#*****************************************************************************80
#
## card_symbol() is given the index of a card and returns its symbol.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer card_index: the card index.
#
#    bool card_used: True if the card has been used.
#
#  Output:
#
#    string SYMBOL: the card rank and suit, as in '5H' or '10C' or 'QD'.
#
  r = card_index % 13

  rank_symbol1 = [ \
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ' ]
  rs1 = rank_symbol1 [ r ]
  rank_symbol2 = [ \
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K' ]
  rs2 = rank_symbol2 [ r ]

  suit_index = card_index // 13
  suits = [ 'H', 'C', 'D', 'S' ]
  suit = suits[suit_index]

  if ( card_used ):
    symbol = ' ' + rs1 + rs2 + suit + ' '
  else:
    symbol = '[' + rs1 + rs2 + suit + ']'

  return symbol

def clock_solitaire_simulation_test ( ):

#*****************************************************************************80
#
## clock_solitaire_simulation_test() tests clock_solitaire_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'clock_solitaire_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  clock_solitaire_simulation() simulates the game of' )
  print ( '  clock solitaire.' )

  rng = default_rng ( )

  print ( '' )
  print ( 'piles_deal() randomly initializes the card piles.' )
  piles, used = piles_deal ( rng )
  print ( 'piles_print() prints the current piles.' )
  piles_print ( piles, used )

  win = play ( rng )
  print ( '' )
  if ( win ):
    print ( 'play() played one game and won.' )
  else:
    print ( 'play() played one game and lost.' )

  n = 1000
  play_many ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'clock_solitaire_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def piles_deal ( rng ):

#*****************************************************************************80
#
## piles_deal() deals the cards in a simulation of clock solitaire.
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
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer piles(13,4): contains a permutation of the card indices.
#
#    bool used(13,4): initially False, indicating whether a card has been used.
#
  import numpy as np

  piles = rng.permutation ( 52 )

  piles = np.reshape ( piles, [ 13, 4 ] )
#
#  Cards are initially NOT used.
#
  used = np.zeros ( [ 13, 4 ], dtype = bool )

  return piles, used

def piles_print ( piles, used ):

#*****************************************************************************80
#
## piles_print() prints the piles in a game of clock solitaire.
#
#  Example:
#
#      A    2    3    4    5    6    7    8    9   10    J    Q    K
#    [01D][04D][06H][07S][11D][03S][03H][03C][13C][08C][10H][06C][02C]
#    [09D][01H][10S][02D][10C][09H][04S][07C][05S][12D][05D][08D][13S]
#    [04C][11S][12C][02H][12H][02S][09S][08S][09C][01C][05C][08H][05H]
#    [03D][11H][01S][07D][10D][12S][11C][06D][06S][13D][13H][04H][07H]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PILES(13,4): the indices of the cards.
#
#    bool used(13,4): initially False, indicating whether a card has been used.
#
  print ( '' )
  print ( '  A    2    3    4    5    6    7    8    9   10    J    Q    K' )
  print ( '' )
  for j in range ( 0, 4 ):
    for i in range ( 0, 13 ):
      symbol = card_symbol ( piles[i,j], used[i,j] )
      print ( symbol, end = '' )
    print ( '' )

  return

def play ( rng ):

#*****************************************************************************80
#
## play() plays a game of clock solitaire.
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
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    logical WIN: is true if this game was won.
#
  import numpy as np

  verbose = False
#
#  Lay out the cards in 13 piles of 4 cards each.
#
  piles, used = piles_deal ( rng )

  k = 0

  while ( True ):
#
#  On first step, choose a pile i at random.
#
    if ( k == 0 ):
      i = rng.integers ( low = 0, high = 12, endpoint = True )
#
#  Select the top card from pile i.
#
    j = piles[i,0]
#
#  If this card has already been used, we have lost.
#
    if ( used[i,0] ):
      win = False
      if ( verbose ):
        print ( '  Lost.  Pile', i, 'is exhausted.' )
      return win
#
#  Turn the card over.
#
    used[i,0] = True
#
#  Move the top card to the bottom.
#  Manipulating Python arrays is grotesquely incompetently arranged.
#
    piles[i,:] = np.roll ( piles[i,:], 3 )
    used[i,:] = np.roll ( used[i,:], 3 )
#
#  Report.
#
    k = k + 1
    jrank = card_rank ( j )
    jsuit = card_suit ( j )

    if ( verbose ):
      print ( '  %2d  %2d  %2d  %2d  %s' % ( k, i, j, jrank+1, jsuit ) )

    if ( k == 52 ):
      break
#
#  Determine the next pile.
#
    i = jrank

  win = True

  return win

def play_many ( n, rng ):

#*****************************************************************************80
#
## play_many() plays many games of clock solitaire.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of games to play.
#
#    rng(): the current random number generator.
#
  verbose = False

  print ( '' )
  print ( 'play_many() will play', n, 'clock solitaire games.' )

  wins = 0
  for game in range ( 0, n ):
    win = play ( rng )
    if ( win ):
      wins = wins + 1
      if ( verbose ):
        print ( '  Game', game, ', wins = ', wins )

  print ( '  Won', wins, 'out of', n )
  print ( '  Win ratio is       ', wins / n )
  print ( '  Expected win ratio ', 1.0 / 13.0 )

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
  clock_solitaire_simulation_test ( )
  timestamp ( )



