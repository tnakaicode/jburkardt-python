#! /usr/bin/env python3
#
def jeopardy ( filename = 'names.txt' ):

#*****************************************************************************80
#
## jeopardy() prints a random first name from a class roster file.
#
#  Discussion:
#
#    Pick a student, by first name, from a class roster.
#
#    The class roster is assumed to be a plain text file.
#    Each line lists one student.
#    The line lists the student's ID#, first name, last name.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string filename: the name of the class roster file.
#
  import numpy as np
#
#  We will create a list of names in the list "name".
#  Initialize it as an empty list, and set the length n to 0.
#
  n = 0
  name = []
#
#  Open the roster file.
#  Read each line, split it into words, and copy the second word into "name".
#
  try:
    input = open ( filename, 'r' )
  except:
    print ( 'jeopardy(filename) could not open "' + filename + '"' )
    return

  for line in input:
    words = line.split()
    name.append ( words[1] )
    if ( False ):
      print ( line, end = '' )
    if ( False ):
      print ( n, name[n] )
    n = n + 1

  input.close ( )

  if ( False ):
    print ( 'The file "' + filename + '" contains', n, 'records.' )
#
#  Pick a random integer n: 0 <= r < n
#
  r = np.random.randint ( low = 0, high = n )
#
#  Print the second word from record r.
#
  print ( 'Python Jeopardy winner is #' + str ( r ) + ': "' + name[r] + '"!' )

  return

def jeopardy_test ( ):

#*****************************************************************************80
#
## jeopardy_test() tests jeopardy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'jeopardy_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test jeopardy()' )
  print ( '' )

  for i in range ( 0, 5 ):
    jeopardy ( 'names.txt' )
#
#  Terminate.
#
  print ( '' )
  print ( 'jeopardy_test():' )
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

if ( __name__ == "__main__" ):
  timestamp ( )
  jeopardy_test ( )
  timestamp ( )
