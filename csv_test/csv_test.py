#! /usr/bin/env python3
#
def csv_reader_test ( ):

#*****************************************************************************80
#
## csv_reader_test tests csv.reader.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2020
#
#  Author:
#
#    John Burkardt
#
  import csv
  import platform

  print ( '' )
  print ( 'csv_reader_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test csv.reader()' );

  csv_file = open ( 'basketball.csv')
  csv_reader = csv.reader ( csv_file, delimiter = ',')

  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print ( '' )
      print ( f'Column names are {", ".join(row)}' )
    else:
      print ( '' )
      print(f'{row[1]} plays {row[2]}, height {row[3]} cm, weight {row[4]} pounds.')
      print(f'{row[1]} earns ${row[5]}.')
      if ( row[6] == 'yes' ):
        print(f'{row[1]} has a shoe sponsorship.')
      else:
        print(f'{row[1]} does not have a shoe sponsorship.')
      print(f'{row[1]}\'s career status is {row[7]}.')
      print(f'{row[1]}\'s age is {row[8]}.')
    line_count = line_count + 1

  csv_file.close ( )

  print ( '' )
  print ( f'Processed {line_count} lines.' )

  print ( '' )
  print ( 'csv_reader_test' )
  print ( '  Normal end of execution.' );

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
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  csv_reader_test ( )
  timestamp ( )
 
