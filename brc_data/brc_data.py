#! /usr/bin/env python3
#
def brc_data_test ( ):

#*****************************************************************************80
#
## brc_data_test() test brc_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 October 2024
#
#  Author:
#
#    Original C version by Danny van Kooten.
#    This version by John Burkardt.
#
#  Local:
#
#    integer n: the number of observations to generate.
#
  from time import time
  import numpy as np
  import platform

  print ( "" )
  print ( "brc_data_test():" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  Generate data for the billion record challenge." )

  n = 100000

  seconds = time ( )
  c, t = brc_data ( n )
  seconds = time ( ) - seconds
  print ( '  Run time was', seconds, 'seconds.' )
#
#  Stupid "write" inserts a space between initial quote and string.
#  Had to do more silly things to suppress this.
#
  filename = 'brc_obs.csv'
  output = open ( filename, 'w' )
  for i in range ( 0, n ):
    s = ( '"%s",%6.2f\n' % ( c[i], t[i] ) )
    s = s.replace ( ' ', '' )
    output.write ( s )
  output.close ( )

  print ( '  Observations written to "' + filename + '"' )
  print ( "  Number of observations is ", n )
#
#  Terminate.
#
  print ( "" )
  print ( "brc_data_test():" )
  print ( "  Normal end of execution." )

  return

def brc_data ( n ):

#*****************************************************************************80
#
## brc_data() generates a data file for the one billion row challenge.
#
#  Discussion:
#
#    Originally called "1brc_data" but MATLAB won't allow "1" as the
#    beginning of a function name.  Everybody has their sore spot!
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 October 2024
#
#  Author:
#
#    Original C version by Danny van Kooten.
#    This version by John Burkardt.
#
#  Input:
#
#    integer n: the number of observations to generate.
#
#  Output:
#
#    cell_array c(ncities): the city names.
#
#    real t(ncities): the temperatures.
#
  from numpy.random import default_rng
  import csv

  rng = default_rng ( )
#
#  Load the data file.
#
  filename = 'brc_data.csv'
  csv_file = open ( filename )
  csv_reader = csv.reader ( csv_file, delimiter = ',' )
  print ( '  Reading data from "' + filename + '"' )

  city_list = []
  temp_list = []
  line_count = 0

  for row in csv_reader:
#
#  I often allow a final empty line in a CSV file.
#  The CSV reader will choke if I don't break at that point.
#
    if ( len ( row ) == 0 ):
      print ( '' )
      print ( '  Last line of file is empty!' )
      break
#
#  Remove double quotes around city name.'
#
    row[0] = row[0].replace ( '"', '' )

#   print ( '  ', line_count, ' ' + row[0] + ' has mean temperature', row[1] )

    city_list.append ( row[0] )
    temp_list.append ( row[1] )

    line_count = line_count + 1

  csv_file.close ( )
#
#  Figure out number of cities.
#
  ncities = len ( city_list )
  print ( "  Number of weather stations is ", ncities )
#
#  For each observation, choose a city "c" uniformly at random, 
#  generate a temperature measurement "t" with normal distribution
#  with variance of 10, and write it to the file.
#
#  This "list comprehension" is awkward and unnatural.
#  Also, t is somehow of type "U6" until I force it to be a float.
#
  index = rng.integers ( low = 0, high = ncities, size = n, endpoint = False )
  c = [ city_list[i] for i in index ]

  normal = rng.standard_normal ( size = n )
  t = [ float ( temp_list[i] ) for i in index ]
  t = t + 10.0 * normal

  return c, t

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
  brc_data_test ( )
  timestamp ( )

