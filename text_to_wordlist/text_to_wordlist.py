#! /usr/bin/env python3
#
def text_to_wordlist_test ( ):

#*****************************************************************************80
#
## text_to_wordlist_test() tests text_to_wordlist().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'text_to_wordlist_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Normal end of execution' )

  filename = 'alice_in_wonderland.txt'
  text_to_wordlist ( filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'text_to_wordlist_test():' )
  print ( '  Normal end of execution' )

  return

def text_to_wordlist ( filename ):

#*****************************************************************************80
#
## text_to_wordlist() converts a text file to a list of words.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string filename: the name of the text file.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'text_to_wordlist():' )
  print ( '  Convert a text file to a wordlist.' )
  print ( '  Here, we process information from "' + filename + '"' )

  myfile = open ( filename, 'r' )
  string = myfile.read().replace ('\n',' ' )
  myfile.close ( )

  print ( '  This file is now a string of ', len ( string ), 'characters.' )

  print ( '' )
  print ( '  Here are the first 20 characters:' )
  print ( string[0:20] )

  mylist = []
  for word in string.split( ' ' ):
    if ( word != '' ):
      mylist.append ( word )

  print ( '  The string is now a list of ', len ( mylist ), 'words.' )
  print ( '' )
  print ( '  Here are the first 20 words:' )

  print ( mylist[0:20] )

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
  text_to_wordlist_test ( )
  timestamp ( )

