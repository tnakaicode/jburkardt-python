#! /usr/bin/env python3
#
def levenshtein_distance ( s, t ):

#*****************************************************************************80
#
## LEVENSHTEIN_DISTANCE computes the Levenshtein distance between strings.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, T, two strings to be compared.  S is thought of as
#    the "source" string and T the "target" string.
#
#    Output, integer DISTANCE, the Levenshtein distance between the
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
## LEVENSHTEIN_DISTANCE_TEST tests LEVENSHTEIN_DISTANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
  print ( '' )
  print ( 'LEVENSHTEIN_DISTANCE_TEST:' )
  print ( '  LEVENSHTEIN_DISTANCE computes the Levenshtein distance' )
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

  return

def levenshtein_matrix ( s, t ):

#*****************************************************************************80
#
## LEVENSHTEIN_MATRIX computes the Levenshtein distance matrix between strings.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, T, two strings to be compared.  S is thought of as
#    the "source" string and T the "target" string.
#
#    Output, integer D(M+1,N+1), the matrix used to determine the Levenshtein
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
## LEVENSHTEIN_MATRIX_TEST tests LEVENSHTEIN_MATRIX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
  print ( '' )
  print ( 'LEVENSHTEIN_MATRIX_TEST:' )
  print ( '  LEVENSHTEIN_MATRIX computes the Levenshtein matrix' )
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

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def levenshtein_test ( ):

#*****************************************************************************80
#
## LEVENSHTEIN_TEST tests the LEVENSHTEIN library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LEVENSHTEIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the LEVENSHTEIN library.' )

  levenshtein_distance_test ( )
  levenshtein_matrix_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEVENSHTEIN_TEST' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  levenshtein_test ( )
  timestamp ( )
