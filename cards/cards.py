#! /usr/bin/env python3
#
def cards_test ( ):

#*****************************************************************************80
#
## cards_test() tests cards().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cards_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Tests cards().' )
  print ( '' )

  deck_shuffle_perfect_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cards_test():' )
  print ( '  Normal end of execution.' )
  return

def card_index ( rank, suit ):

#*****************************************************************************80
#
## card_index() determines the index of a card from its rank and suit.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer rank: the rank, from 0 to 12.
#
#    integer suit: the suit index, from 0 to 3.
#  Output:
#
#    integer index: a card index, from 0 to 51.
#
#
  index = 4 * suit + rank

  return index

def card_rank ( index ):

#*****************************************************************************80
#
## card_rank() determines the rank of a card from its index.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index: a card index, from 0 to 51.
#
#  Output:
#
#    integer rank: the rank, from 0 to 12.
#
  rank = ( index % 13 )

  return rank

def card_suit ( index ):

#*****************************************************************************80
#
## card_suit() determines the suit of a card from its index.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index: a card index, from 0 to 51.
#
#  Output:
#
#    integer suit: the suit index, from 0 to 3.
#
  suit = index // 13

  return suit

def card_symbols ( ):

#*****************************************************************************80
#
## card_symbols() returns a list of 52 card symbols.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    list symbol_list[52]: symbols for the 52 cards in a deck, from 'AH'
#    through 'KS'.
#
  rank_list = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ];
  suit_list = [ 'H', 'C', 'D', 'S' ]

  symbol_list = []
  for suit in suit_list:
    for rank in rank_list:
      symbol = rank + suit
      symbol_list.append ( symbol )

  print ( symbol_list )

  return

def deck_shuffle_perfect ( deck ):

#*****************************************************************************80
#
## deck_shuffle_perfect() performs a perfect shuffle on a deck of cards.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer deck[52]: the indices of the cards in a deck.
#
  import numpy as np

  deck_size = len ( deck )
  deck_size_half = deck_size // 2
  deck_shuffled = np.zeros ( deck_size, dtype = int )
  deck_shuffled[0:deck_size:2] = deck[0:deck_size_half]
  deck_shuffled[1:deck_size:2] = deck[deck_size_half:]

  return deck_shuffled

def deck_shuffle_perfect_test ( ):

#*****************************************************************************80
#
## deck_shuffle_perfect_test() tests deck_shuffle_perfect().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'deck_shuffle_perfect_test():' )
  print ( '  Test deck_shuffle_perfect(), which does a perfect shuffle' )
  print ( '  of a deck of cards.' )

  deck_size = 52
  deck = np.arange ( deck_size, dtype = int )
  print ( '' )
  print ( '  Starting deck:' )
  print ( deck )
#
#  Now do a perfect shuffle.
#
  deck = deck_shuffle_perfect ( deck )
  print ( '' )
  print ( '  Deck after 1 perfect shuffle:' )
  print ( deck )
#
#  Now do 7 more perfect shuffles.
#
  for i in range ( 0, 7 ):
    deck = deck_shuffle_perfect ( deck )
  print ( '' )
  print ( '  Deck after 7 more perfect shuffles:' )
  print ( deck )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  cards_test ( )
  timestamp ( )

