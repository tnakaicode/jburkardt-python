#! /usr/bin/env python3
#
def levenshtein_distance ( s, t ):

#*****************************************************************************80
#
## levenshtein_distance() computes the Levenshtein distance between strings.
#
#  Discussion:
#
#    Let S and T be source and target strings.  Consider the task of
#    converting S to T in the minimal number of steps, involving
#    * Insertion: insert a new character
#    * Deletion: delete a character
#    * Substitution: swap one character for another.
#    The Levenshtein distance from S to T is the minimal number of such
#    steps required to transform S into T.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, T, two strings to be compared.  S is thought of as
#    the "source" string and T the "target" string.
#
#  Output:
#
#    integer DISTANCE, the Levenshtein distance between the
#    two strings.
#
  import numpy as np

  m = len ( s )
  n = len ( t )

  d = np.zeros ( [ m + 1, n + 1 ] )

  d[0,0] = 0
#
#  Source prefixes can be transformed into empty string by
#  dropping all characters,
#
  for i in range ( 1, m + 1 ):
    d[i,0] = i
#
#  Target prefixes can be reached from empty source prefix
#  by inserting every character.
#
  for j in range ( 1, n + 1 ):
    d[0,j] = j

  for j in range ( 1, n + 1 ):
    for i in range ( 1, m + 1 ):
      if ( s[i-1] == t[j-1] ):
        substitution_cost = 0
      else:
        substitution_cost = 1

      d[i,j] = min ( d[i-1,j] + 1, \
               min ( d[i,j-1] + 1, \
                     d[i-1,j-1] + substitution_cost ) ) 

  distance = d[m,n]

  return distance

def levenshtein_distance_test ( ):

#*****************************************************************************80
#
## levenshtein_distance_test() tests levenshtein_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'levenshtein_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  levenshtein_distance() computes the Levenshtein distance' )
  print ( '  between two strings.' )

  s = 'water'
  t = 'wine'
  d1 = levenshtein_distance ( s, t )
  d2 = 3
  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  print ( '  Computed distance = %d, correct distance = %d' % ( d1, d2 ) )

  s = 'kitten'
  t = 'sitting'
  d1 = levenshtein_distance ( s, t )
  d2 = 3
  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  print ( '  Computed distance = %d, correct distance = %d' % ( d1, d2 ) )

  s = 'saturday'
  t = 'sunday'
  d1 = levenshtein_distance ( s, t )
  d2 = 3
  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  print ( '  Computed distance = %d, correct distance = %d' % ( d1, d2 ) )

  s = 'pheromones'
  t = 'photographer'
  d1 = levenshtein_distance ( s, t )
  d2 = 8
  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  print ( '  Computed distance = %d, correct distance = %d' % ( d1, d2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'levenshtein_distance_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  levenshtein_distance_test ( )
  timestamp ( )
 
