#! /usr/bin/env python3
#
def ladders_test ( ):

#*****************************************************************************80
#
## ladders_test() tests ladders().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ladders_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  ladders() moves from a starting word to a goal word' )
  print ( '  by changing one letter at a time.' )
#
#  Set start and end words.
#
  for begin_word, end_word in [ [ 'COLD', 'WARM' ], ['BLACK', 'WHITE' ] ]:
#
#  Capitalize the words.
#
    begin_word = begin_word.upper ( )
    end_word = end_word.upper ( )

    path = ladders ( begin_word, end_word )

    print ( '' )
    print ( '  Ladders returns the path:' )
    print ( path )
#
#  Terminate.
#
  print ( '' )
  print ( 'ladders_test():' )
  print ( '  Normal end of execution.' )

  return

def ladders ( begin_word, end_word ):

#*****************************************************************************80
#
## ladders() seeks a path between start and goal words.
#
#  Discussion:
#
#    Only 5-letter words are considered.
#    Only one letter at a time may be changed.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 August 2025
#
#  Author:
#
#    Original Python version by Parineeth MR.
#    This version by John Burkardt.
#
#  Reference:
#
#    Parineeth MR,
#    The Big Book of Coding Interviews in Python,
#    Third Edition, 2018,
#    ISBN13: 978-1983861185
#
#  Input:
#
#    string begin_word: the starting word.
#
#    string end_word: the final word.
#
#    list word_list[*]: the list of usable words.
#
#  Output:
#
#    path[*]: a list of words which form the path, or None if no path was found.
#
#  Local:
#
#    visited(): the set of words visited so far.
#
  import queue

  filename = 'sowpods.txt'
  print ( '' )
  print ( '  Initial word list is "' + filename + '"' )

  all_words = word_list_read ( filename )
  print ( '  Word 5 is ' + all_words[95] )
  print ( '  Number of words is ', len ( all_words ) )

  word_length = len ( begin_word )
  if ( len ( end_word ) != word_length ):
    print ( '' )
    print ( 'ladders(): Fatal error!' )
    print ( 'starting and ending words must have same length!' )
    return

  print ( '' )
  print ( '  Starting word is "' + begin_word + '"' )
  print ( '  Goal word is     "' + end_word + '"' )
  print ( '  Word length is ', word_length )

  word_list = word_list_trim ( all_words, word_length )
  print ( '  Word 95 is ' + word_list[95] )
  print ( '  Number of words is ', len ( word_list ) )

  q = queue.Queue ( )

  visited = set ( )

  reverse_path = {}

  q.put ( begin_word )
  visited.add ( begin_word )

  while ( not q.empty ( ) ):

    cur_word = q.get ( )
#
#  If the current word matches the goal word, we have succeeded.
#  Construct path by reversing reverse_path.
#
    if ( cur_word == end_word ):
      path = []
      path.insert ( 0, cur_word )
      cur_word = reverse_path.get ( cur_word )
      while ( cur_word ):
        path.insert ( 0, cur_word )
        cur_word = reverse_path.get ( cur_word )
      return path
#
#  The current word does not match the goal word.
#  Look at all words that can be generated from the current word.
#  Assume we are dealing with uppercase characters only.
#
    for i in range ( len ( cur_word ) ):
      char_list = list ( cur_word )
      for c in range ( ord ( 'A' ), ord ( 'Z' ) + 1 ):
        char_list[i] = chr(c)
        new_word = ''.join(char_list)
        if ( new_word in word_list and new_word not in visited ):
          q.put ( new_word )
          visited.add ( new_word )
          reverse_path[new_word] = cur_word

  return None

def word_list_read ( filename ):

#*****************************************************************************80
#
## word_list_read() reads words from a file into a list.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string filename: the name of the file containing a list of words.
#
#  Output:
#
#    list my_list[*]: the list of words.
#
  my_file = open ( filename )
  letters = my_file.read().replace('\n',' ' )
  my_file.close ( )

  my_words = []
  for letter in letters.split ( ' ' ):
    if ( letter != '' ):
      my_words.append ( letter )

  return my_words

def word_list_trim ( all_words, word_length ):

#*****************************************************************************80
#
## word_list_trim() returns all words of given length from a list.
#
#  Discussion:
#
#    The words are all put into uppercase as well.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    list all_words[]: a list of words.
#
#    integer word_length: the desired word length.
#
#  Output:
#
#    list word_list[*]: the list of words of the given length.
#
  word_list = []
  for word in all_words:
    if ( len ( word ) == word_length ):
      word_list.append ( word.upper ( ) )

  return word_list

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
  ladders_test ( )
  timestamp ( )

