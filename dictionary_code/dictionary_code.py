#! /usr/bin/env python3
#
def dictionary_code_test ( ):

#*****************************************************************************80
#
## dictionary_code_test() tests dictionary_code().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'dictionary_code_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test dictionary_code().' )

  dictionary_encode ( )
  dictionary_decode ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'dictionary_code_test():' )
  print ( '  Normal end of execution.' )

  return

def dictionary_decode ( ):

#*****************************************************************************80
#
## dictionary_decode() applies dictionary decoding to a text file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dictionary_decode():' )
  print ( '  Apply dictionary decoding to a file.' )
  print ( '' )
#
#  Read the dictionary file.
#
  filename = 'gettysburg_address_dictionary.txt'
  file = open ( filename, 'r' )
  word_unique_list = [ line.rstrip() for line in file ]
  file.close ( )
#
#  Read the encoded text file.
#
  filename = 'gettysburg_address_encoded.txt'
  file = open ( filename, 'r' )
  indices = np.loadtxt ( file, dtype = int )
  file.close ( )
#
#  Replace each index in the encoded text file by the corresponding
#  word from the dictionary.
#
  word_num = len ( indices )

  for index in indices:
    print ( word_unique_list[index] )
#
#  Terminate.
#
  print ( '' )
  print ( 'dictionary_decode():' )
  print ( '  Normal end of execution.' )

  return

def dictionary_encode ( ):

#*****************************************************************************80
#
## dictionary_encode() applies dictionary encoding to a text file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'dictionary_encode():' )
  print ( '  Apply dictionary encoding to a file.' )
#
#  Read a text into a cell array.
#
  filename = 'gettysburg_address2.txt'
  file = open ( filename, 'r' )
  data_string = file.read ( )
  word_list = data_string.split()
  word_num = len ( word_list )
  file.close ( )
#
#  Count characters and words in input file.
#
  char_num = 0
  for word in word_list:
    char_num = char_num + len ( word )

  print ( '  Text contains ', char_num, ' characters.' )
  print ( '  Text contains ', word_num, ' words.' )
#
#  Collect the unique words in the text.
#
  word_unique_list = list ( set ( word_list ) )
  word_unique_num = len ( word_unique_list )
  print ( '  Text contains ', word_unique_num, ' unique words.' )
#
#  Sort the unique words.
#
  word_unique_list = sorted ( word_unique_list )
#
#  Print the unique words.
#
  i = 0
  for word in word_unique_list:
    print ( '  %4d  %s' % ( i, word ) )
    i = i + 1
#
#  Write the unique words to a "dictionary" file.
#
  filename = 'gettysburg_address_dictionary.txt'
  output = open ( filename, 'wt' )
  for word in word_unique_list:
    print ( word, file = output )
  output.close ( )
#
#  Replace each word in the original text by the index of 
#  that word in the dictionary.
#
  filename = 'gettysburg_address_encoded.txt'
  output = open ( filename, 'wt' )
  for word in word_list:
    index = word_unique_list.index ( word )
    print ( index, file = output )
  output.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'dictionary_encode():' )
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
  dictionary_code_test ( )
  timestamp ( )


