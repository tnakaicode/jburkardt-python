#! /usr/bin/env python3
#
def levenshtein_matrix ( s, t ):

#*****************************************************************************80
#
## levenshtein_matrix() computes the Levenshtein distance matrix between strings.
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
#    16 March 2018
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
#    integer D(M+1,N+1), the matrix used to determine the Levenshtein
#    distance between the two strings.  The distance is the value in D(M+1,N+1).
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

  return d

def levenshtein_matrix_test ( ):

#*****************************************************************************80
#
## levenshtein_matrix_test() tests levenshtein_matrix().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'levenshtein_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  levenshtein_matrix() computes the Levenshtein matrix' )
  print ( '  associated with the computation of the Levenshtein' )
  print ( '  distance between two strings.' )

  s = 'water'
  t = 'wine'
  m = len ( s )
  n = len ( t )
  d = levenshtein_matrix ( s, t )

  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  for i in range ( 0, m + 1 ):
    for j in range ( 0, n + 1 ):
      print ( ' %2d' % ( d[i,j] ), end = '' )
    print ( '' )

  s = 'sitting'
  t = 'kitten'
  m = len ( s )
  n = len ( t )
  d = levenshtein_matrix ( s, t )

  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  for i in range ( 0, m + 1 ):
    for j in range ( 0, n + 1 ):
      print ( ' %2d' % ( d[i,j] ), end = '' )
    print ( '' )

  s = 'sunday'
  t = 'saturday'
  m = len ( s )
  n = len ( t )
  d = levenshtein_matrix ( s, t )

  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  for i in range ( 0, m + 1 ):
    for j in range ( 0, n + 1 ):
      print ( ' %2d' % ( d[i,j] ), end = '' )
    print ( '' )

  s = 'pheromones'
  t = 'photographer'
  m = len ( s )
  n = len ( t )
  d = levenshtein_matrix ( s, t )

  print ( '' )
  print ( '  S = "%s"' % ( s ) )
  print ( '  T = "%s"' % ( t ) )
  for i in range ( 0, m + 1 ):
    for j in range ( 0, n + 1 ):
      print ( ' %2d' % ( d[i,j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'levenshtein_matrix_test():' )
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
  levenshtein_matrix_test ( )
  timestamp ( )
 
