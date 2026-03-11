#! /usr/bin/env python3
#
def text_strip_test():

#*****************************************************************************80
#
## text_strip_test() tests text_strip().
#
#  Discussion:
#
#    text_strip input output
#
#  Modified:
#
#    25 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import sys

  print ( "" )
  print ( "text_strip_test():" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  text_strip() strips a file of newlines and other odd characters." )
  print ( '' )
#
#  Read information.
#
  input_file = sys.argv[1]
  with open ( input_file ) as file:
    data = file.read()
  file.close ( )
#
#  Get regular expression library.
#
  import re
#
#  Preserve alphanumerics, hyphen, left and right single and double quotes.
#
  data = re.sub ( r"[^a-zA-Z0-9.,:;-?!\u002d\u2018\u2019\u201c\u201d\s]", "", data )
#
#  Newline -> blank, Carriage return -> blank.
#
  data = re.sub ( r"\n", " ", data )
  data = re.sub ( r"\r", " ", data )
#
#  Multiple consecutive blanks to one blank.
#
  data = re.sub ( r"\s+", " ", data )

  output_file = sys.argv[2]
  with open ( output_file, 'w' ) as file:
    file.write( data )
  file.close ( )
#
#  Terminate.
#
  print ( "" )
  print ( "text_strip_test():" )
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
  text_strip_test ( )
  timestamp ( )

