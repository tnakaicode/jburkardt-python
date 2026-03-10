#! /usr/bin/env python3
#
def columns ( input_name, output_name, clo, chi ):

#*****************************************************************************80
#
## columns() copies selected columns from one file to another.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string input_name: the name of the input file.
#
#    string output_name: the name of the output file.
#
#    integer clo, chi: the range of columns to be read.
#    This uses Python's 0-based index and omitting last index conventions.
#
  import numpy as np
#
#  Read the text file.
#
  input_pointer = open ( input_name, 'r' )
  contents = input_pointer.readlines ( )
  input_pointer.close ( )

  print ( '  Number of lines of text is ', len ( contents ) )
#
#  Write a text file of just the selected columns.
#
  output_pointer = open ( output_name, 'w' )
  for i in range ( 0, len ( contents ) ):
    output_pointer.write ( contents[i][clo:chi] )
    output_pointer.write ( '\n' )
  output_pointer.close ( )

  print ( '  Wrote column data to "' + output_name + '"' )

  return

def columns_test ( ):

#*****************************************************************************80
#
## columns_test() tests columns().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'columns_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  columns() copies specific text columns from one file to another.' )

  file_in = 'knuth_words.txt'
  file_out = 'knuth_5.txt'
  clo = 0
  chi = 5

  print ( '' )
  print ( '  Read text from "' + file_in + '"' )
  print ( '  Copy columns ', clo, ':', chi )
  print ( '  Write copied text to "' + file_out + '"' )

  columns ( file_in, file_out, clo, chi )
#
#  Terminate.
#
  print ( '' )
  print ( 'columns_test():' )
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
  columns_test ( )
  timestamp ( )

