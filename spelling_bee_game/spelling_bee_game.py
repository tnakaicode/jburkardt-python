#! /usr/bin/env python3
#
def spelling_bee_game_test ( ):

#*****************************************************************************80
#
## spelling_bee_game_test() tests spelling_bee_game().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 July 2025
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt.
#
#  Input:
#
#    string filename: the word list filename.
#
  import sys

  print ( '' )
  print ( 'spelling_bee_game_test ( ):' )
  print ( '  Solve a New York Times spelling bee puzzle' )

  letters = sys.argv[1]

  assert ( len ( letters ) == 7 )

  filename = 'sowpods.txt'

  spelling_bee_game ( letters, filename, 4 )

  return

def get_words ( filename ):

#*****************************************************************************80
#
## get_words() reads the word list and converts a capitalized version.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 January 2025
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt.
#
#  Input:
#
#    string filename: the word list filename.
#
  with open ( filename ) as fi:
    words = [ word.strip().upper() for word in fi ]

  return words

def spelling_bee_game ( letters, filename, min_length = 4 ):

#*****************************************************************************80
#
## spelling_bee_game() solves a spelling bee puzzle.
#
#  Discussion:
#
#    letters is a string of the letters to solve for, with the central letter,
#    which must be in every solution word first.
#
#  Discussion:
#
#    21-07-2025: Input word is now automatically capitalized.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 January 2025
#
#  Author:
#
#    Original Python version by Christian Hill.
#    This version by John Burkardt.
#
#  Input:
#
#    string letters[7]: the letters from which new words are to be formed.
#
#    string filename: the word list filename.
#
#    integer min_length: the minimum length of a new word.
#    The default is 4.
#

#
#  Capitalize the letters.
#
  letters = letters.upper()

  central_letter = letters[0]
  letter_set = set ( letters )
  words = get_words ( filename )
#
#  Consider adding each word to the list of valid words.
#
  valid_words = []

  for word in words:

    if len ( word ) < min_length:
      continue

    if ( central_letter not in word ):
      continue

    if set(word).issubset(letter_set):
      valid_words.append(word)

  print ( '' )
  print ( '  The "dictionary" being used is "' + filename + '"' )
  print ( '  The challenge word is "' + letters + '"' )
  print ( '  ', len ( valid_words ), 'matching words were found:' )
  print ( '' )
#
#  Print the solution words, sorted by length and, within each word length,
#  sorted alphabetically.
#
  i = 0
  for valid_word in sorted ( valid_words, key = lambda word: ( len ( word ), word ) ):
    i = i + 1
    print ( i, valid_word )

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

if __name__ == '__main__':
  timestamp ( )
  spelling_bee_game_test ( )
  timestamp ( )

