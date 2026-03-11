#! /usr/bin/env python3
#
def markov_letters_test ( ):

#*****************************************************************************80
#
## markov_letters_test() tests markov_letters().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'markov_letters_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  Test markov_letters().' )
 
  header = 'abc'
  unigram_frequency_print_test ( header )
  bigram_frequency_print_test ( header )

  header = 'quick_brown_fox'
  unigram_frequency_print_test ( header )
  bigram_frequency_print_test ( header )

  header = 'panjandrum'
  unigram_frequency_print_test ( header )
  unigram_frequency_print_sorted_test ( header )
  unigram_frequency_plot_test ( header )
  bigram_frequency_print_test ( header )
  bigram_probability_print ( header )

  header = 'alice_in_wonderland'
  unigram_frequency_print_test ( header )
  unigram_frequency_print_sorted_test ( header )
  unigram_frequency_plot_test ( header )
  unigram_frequency_plot_sorted_test ( header )
  bigram_probability_print ( header )

  header = 'die_verwandlung'
  unigram_frequency_print_test ( header )
  unigram_frequency_print_sorted_test ( header )
  unigram_frequency_plot_test ( header )
  unigram_frequency_plot_sorted_test ( header )
  bigram_frequency_print_test ( header )
  bigram_probability_print ( header )
#
#  Terminate.
#
  print ( '' )
  print ( 'markov_letters_test():' )
  print ( '  Normal end of execution.' )

  return

def bigram_frequency_print_test ( header ):

#*****************************************************************************80
#
## bigram_frequency_print_test() tests bigram_frequency().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
  print ( '' )
  print ( 'bigram_frequency_print_test():' )
  print ( '  bigram analysis of "' + header + '.txt"' )

  c = unigram_chars ( )
  freq = bigram_frequency ( header )
  bigram_frequency_print ( c, freq, header )

  return

def bigram_frequency ( header ):

#*****************************************************************************80
#
## bigram_frequency() counts letter-pair frequencies in a file.
#
#  Discussion:
#
#    A sequence of two letters is known as a "bigram".
#
#    Capital and lower case letters are merged.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
#  Output:
#
#    integer FREQ(26,26): counts the number of times character i
#    was immediately followed by character j.
#
  import numpy as np
  import re
#
#  Read the data.
#
  filename = header + '.txt'
  input = open ( filename )
  data = input.read ( )
  input.close ( )
#
#  Clean the data.
#
  data = data.lower ( )
  data = re.sub ( 'r[^a-z]+', ' ', data )
#
#  Count the pairs.
#
  freq = np.zeros ( [ 26, 26 ], dtype = int )

  i1 = -1
  for c in data:
    i2 = char_to_int ( c )
    if ( 0 <= i2 and i2 < 26 ):
      if ( 0 <= i1 and i1 < 26 ):
        freq[i1,i2] = freq[i1,i2] + 1
    i1 = i2

  return freq

def bigram_frequency_print ( c, freq, header ):

#*****************************************************************************80
#
## bigram_frequency_print() prints the letter-pair frequency table.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string C(26): the characters.
#
#    integer FREQ(26,26): the number of times character i
#    was immediately followed by character j.
#
#    string header: an identifier for the data.
#
  import numpy as np

  filename = header + '.txt'

  s = np.sum ( freq, dtype = int )

  print ( '' )
  print ( '  ' + filename )
  print ( '' )

  print ( '   ', end = '' )
  for j in range ( 0, len ( c ) ):
    print ( '  %c' % ( c[j] ), end = '' )
  print ( '' )
  print ( '' )
  for i in range ( 0, len ( c ) ):
    print ( '  %c' % ( c[i] ), end = '' )
    for j in range ( 0, len ( c ) ):
      print ( '%3d' % ( freq[i,j] ), end = '' )
    print ( '' )

  return

def bigram_probability_print ( header ):

#*****************************************************************************80
#
## bigram_probability_print() prints the letter-pair probability table.
#
#  Discussion:
#
#    Each row of the frequency table is divided by its sum and multiplied 
#    by 100.  (Percentages are easier to read than true probabilities.)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
  import numpy as np

  c = unigram_chars ( )
  freq = bigram_frequency ( header )

  print ( '' )
  print ( 'bigram_probability_print():' )
  print ( '  Analysis of "' + header + '.txt"' )
  print ( '' )

  for j in range ( 0, len ( c ) ):
    print ( '  %c' % ( c[j] ), end = '' )
  print ( '' )
  print ( '' )
  for i in range ( 0, len ( c ) ):
    print ( '  %c' % ( c[i] ), end = '' )
    s2 = np.sum ( freq[i,:] )
    if ( s2 != 0 ):
      freq[i,:] = 100.0 * freq[i,:] / s2
    for j in range ( 0, len ( c ) ):
      print ( '%3.0f' % ( freq[i,j] ), end = '' )
    print ( '' )

  return

def char_to_int ( c ):

#*****************************************************************************80
#
## char_to_int() converts a lowercase character to an integer.
#
#  Discussion:
#
#    a     0
#    b     1
#    ... ...
#    z    25
#    ?    26  (any character not a-z)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C: the character.
#
#  Output:
#
#    integer i: the index.
#
  if ( ord ( c ) < ord ( 'a' ) or ord ( 'z' ) < ord ( c ) ):
    i = 26
  else:
    i = ord ( c ) - ord ( 'a' )

  return i

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
#    15 February 2026
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def unigram_chars ( ):

#*****************************************************************************80
#
## unigram_chars() returns the unigram values as a vector.
#
#  Discussion:
#
#    This is simply an array of the alphabetic characters, and a space.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    char c[26]: the unigram values.
#
  import numpy as np

  s = "abcdefghijklmnopqrstuvwxyz"

  c = np.zeros ( len ( s ), dtype = str )
  for i in range ( 0, len ( c ) ):
    c[i] = s[i]

  return c

def unigram_frequency ( header ):

#*****************************************************************************80
#
## unigram_frequency() counts letter frequencies in a file.
#
#  Discussion:
#
#    An instance of a single letter is known as a "unigram".
#
#    Capital and lower case letters are merged.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
#  Output:
#
#    integer freq(26): counts the number of occurrences of character i.
#
  import numpy as np
  import re
#
#  Get the data.
#
  filename = header + '.txt'
  input = open ( filename )
  data = input.read ( )
  input.close ( )
#
#  Clean the data.
#
  data = data.lower ( )
  data = re.sub ( 'r[^a-z]+', ' ', data )
#
#  Count the data.
#
  c = unigram_chars ( )
  freq = np.zeros ( len ( c ), dtype = int )
  for i in range ( len ( c ) ):
    freq[i] = data.count ( c[i] )

  return freq

def unigram_frequency_plot ( c, freq, header ):

#*****************************************************************************80
#
## unigram_frequency_plot() plots a letter frequency table.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C(26): the unigrams.
#
#    integer FREQ(26): the number of occurences of character i.
#
#    string header: an identifier for the data.
#
  import matplotlib.pyplot as plt
  import numpy as np

# c = unigram_chars ( )
  locations = np.arange ( 0, len ( c ) )

  plt.clf ( )
  plt.bar ( locations, freq )
  plt.grid ( True )
  plt.xlabel ( '<-- Character -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.xticks ( ticks = locations, labels = c )
  plt.title ( header )

  filename = header + '_frequency.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def unigram_frequency_plot_test ( header ):

#*****************************************************************************80
#
## unigram_frequency_plot_test() tests unigram_frequency_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
  print ( '' )
  print ( 'unigram_frequency_plot_test():' )
  print ( '  Plot unigram frequency of "' + header + '.txt"' )

  freq = unigram_frequency ( header )
  c = unigram_chars ( )
  unigram_frequency_plot ( c, freq, header )

  return

def unigram_frequency_plot_sorted_test ( header ):

#*****************************************************************************80
#
## unigram_frequency_plot_sorted_test() tests unigram_frequency_plot_sorted().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
  import numpy as np

  print ( '' )
  print ( 'unigram_frequency_plot_test():' )
  print ( '  Plot sorted unigram frequency of "' + header + '.txt"' )

  freq = unigram_frequency ( header )
  index = np.argsort ( freq )
  index = np.flip ( index )
  c = unigram_chars ( )

  c_sorted = c[index]
  freq_sorted = freq[index]
  header_sorted = header + '_sorted'
  unigram_frequency_plot ( c_sorted, freq_sorted, header_sorted )

  return

def unigram_frequency_print ( c, freq, header ):

#*****************************************************************************80
#
## unigram_frequency_print() prints a letter frequency table.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C(26): the unigrams.
#
#    integer FREQ(26): the number of occurences of character i.
#
#    string header: an identifier for the data.
#
  import numpy as np

  s = np.sum ( freq )

  print ( '' )
  print ( '  ' + header )
  print ( '' )
  for i in range ( len ( c ) ):
    print ( '  ', c[i], '  ', freq[i] )

  return

def unigram_frequency_print_test ( header ):

#*****************************************************************************80
#
## unigram_frequency_print_test() tests unigram_frequency().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
  print ( '' )
  print ( 'unigram_frequency_print_test():' )
  print ( '  unigram analysis of "' + header + '.txt"' )

  freq = unigram_frequency ( header )
  c = unigram_chars ( )
  unigram_frequency_print ( c, freq, header )

  return

def unigram_frequency_print_sorted_test ( header ):

#*****************************************************************************80
#
## unigram_frequency_print_sorted_test() tests unigram_frequency_print_sorted().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string header: an identifier for the data.
#
  import numpy as np

  print ( '' )
  print ( 'unigram_frequency_print_sorted_test():' )
  print ( '  unigram analysis of "' + header + '.txt"' )

  freq = unigram_frequency ( header )
  index = np.argsort ( freq )
  index = np.flip ( index )
  c = unigram_chars ( )

  c_sorted = c[index]
  freq_sorted = freq[index]
  header_sorted = header + '_sorted'
  unigram_frequency_print ( c_sorted, freq_sorted, header_sorted )

  return

def unigram_string ( ):

#*****************************************************************************80
#
## unigram_string() returns the unigram values as a string.
#
#  Discussion:
#
#    This is simply an array of the alphabetic characters, and a space.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string S(26): the unigram values.
#
  s = "abcdefghijklmnopqrstuvwxyz"

  return s

if ( __name__ == '__main__' ):
  timestamp ( )
  markov_letters_test ( )
  timestamp ( )

