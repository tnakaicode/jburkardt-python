#! /usr/bin/env python3
#
def markov_text_test():

#*****************************************************************************80
#
## markov_text_test() tests markov_text().
#
#  Discussion:
#
#    markov_text filename context length
#
#  Modified:
#
#    25 May 2024
#
#  Local:
#
#    string filename: the name of a text file to be read.
#
#    integer context: the number of words in succession that form
#    the context of a given word.  A value of 0 yields gibberish.
#    A value of 3 or 4 results in mostly plausible text.
#
#    integer length: the number of words to be generated.
#
  import numpy as np
  import platform
  import sys

  print ( "" )
  print ( "markov_text_test():" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  markov_text() uses Markov methods to imitate a given text." )
  print ( '' )

  filename = sys.argv[1]
  with open ( filename, encoding = 'utf8' ) as file:
    data = file.read()

  context = int ( sys.argv[2] )
  rule = makerule ( data, context )

  length = int ( sys.argv[3] )
  string = makestring ( rule, length )

  print ( string )

  return

def makerule ( data, context ):

#*****************************************************************************80
#
## makerule() makes a rule dict for the given data.
#
#  Discussion:
#
#    This function makes a rule for selecting the next word in a string,
#    based on usage patterns in a given input text.
#
#  Modified:
#
#    07 November 2024
#
#  Input:
#
#    list data[]: the individual words from a text.
#
#    integer context: the number of words in succession that form
#    the context of a given word.  A value of 0 yields gibberish.
#    A value of 3 or 4 results in mostly plausible text.
#
  rule = {}
  words = data.split ( ' ' )
  index = context

  for word in words[index:]:

    key = ' '.join(words[index-context:index])

    if key in rule:
      rule[key].append(word)
    else:
      rule[key] = [word]

    index = index + 1
 
  return rule

def makestring ( rule, length ):  

#*****************************************************************************80
#
## makestring() makes a string using the given rule.
#
#  Discussion:
#
#    This function generates a string of LENGTH words, using a specified rule.
#
#  Modified:
#
#    07 November 2024
#
#  Input:
#
#    dict rule: a rule to use when generating the string.
#
#    integer length: the number of words to be generated.
#
  import random
#
#  Choose a set of starting words at random.
#
  oldwords = random.choice ( list(rule.keys())).split(' ')
  string = ' '.join(oldwords) + ' '
 
  for i in range ( length ):

    try:
      key = ' '.join(oldwords)
      newword = random.choice ( rule[key] )
      string = string + newword + ' '
 
      for word in range ( len(oldwords) ):
        oldwords[word] = oldwords[(word + 1) % len(oldwords)]
      oldwords[-1] = newword
 
    except KeyError:
      raise Exception ( 'makestring(): Fatal error!' )
      return string

  return string

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
#    06 April 2013
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
  markov_text_test ( )
  timestamp ( )

