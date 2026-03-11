#! /usr/bin/env python3
#
def tsp_moler_test ( ):

#*****************************************************************************80
#
## tsp_moler_test() tests tsp_moler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import csv
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_moler_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )

  rng = default_rng ( )
#
#  Using readtable() and csv file format allows me to read the state 
#  abbreviations and latitudes and longitudes together.  
#  However, dealing with the output of readtable() is a little messy,
#  error prone and non-intuitive (but so is almost any attempt to
#  work with csv data).
#
  state = np.zeros ( 0, dtype = str )
  lat = np.zeros ( 0, dtype = float )
  lon = np.zeros ( 0, dtype = float )

  input = open ( 'state_capitals_48_ll.csv', 'r' )
  csvreader = csv.reader ( input )
  for row in csvreader:
    state = np.append ( state, row[0] )
    lat = np.append ( lat, float ( row[1] ) )
    lon = np.append ( lon, float ( row[2] ) )

  state_num = len ( state )
#
#  Verify that the data has been read correctly.
#
  print ( '' )
  print ( '  First 5 latitudes and longitudes:' )
  for i in range ( 0, 5 ):
    print ( '  %s  %12.4f  %12.4f' % ( state[i], lat[i], lon[i] ) )
#
#  Compute the distance matrix.
#
  D = distances ( lon, lat )

  print ( '' )
  print ( '  5x5 initial block of distance matrix' )
  print ( D[0:5,0:5] )
#
#  Call the TSP solver.
#
  p_len, p = traveler ( D, rng ) 
#
#  Report the results.
#
  print ( '' )
  print ( '  Length of path = ', p_len )
  print ( '' )
  print ( '  Itinerary:' )
  print ( '  ', end = '' )
  for i in range ( 0, state_num ):
    print ( state[p[i]] + '->', end = '' )
    if ( ( ( i + 1 ) % 15 ) == 0 ):
      print ( '' )
      print ( '  ', end = '')
  print ( state[p[0]] )
#
#  Give the mileages.
#
  print ( '' )
  print ( '  Mileage per leg:' )
  print ( '')
  for leg in range ( 0, state_num ):
    i = p[leg]
    j = p[leg+1]
    print ( '  %s -> %s  %g' % ( state[i], state[j], D[i,j] ) )
#
#  Plot (longitude,latitude) as (X,Y).
#
  plt.clf ( )
  plt.plot ( lon, lat, 'bo', markersize = 10 )
  for leg in range ( 0, state_num ):
    i = p[leg]
    j = p[leg+1]
    x = [ lon[i], lon[j] ]
    y = [ lat[i], lat[j] ]
    plt.plot ( x, y, 'r-' )
  for i in range ( 0, state_num ):
    x = lon[i]
    y = lat[i]
    plt.text ( x, y, state[i] )
  plt.grid ( True )
  plt.xlabel ( '<-- Longitude -->' )
  plt.ylabel ( '<-- Latitude -->' )
  filename = 'tsp_moler_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "'+ filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_moler_test():' )
  print ( '  Normal end of execution.' )

  return

def distances ( lon, lat ):

#*****************************************************************************80
#
## distances() computes a distance table from longitude and latitude data.
#
#  Discussion:
#
#    The distances are computed on the surface of a sphere representing
#    the earth.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2023
#
#  Author:
#
#    Original MATLAB version by Cleve Moler.
#    This version by John Burkardt.
#
#  Reference:
#
#    Great circle distance matrix between pairs of cities.
#    https://en.wikipedia.org/wiki/Great-circle_distance.
#
#    Cleve Moler,
#    USA Traveling Salesman Tour,
#    Posted 17 September 2018,
#    logs.mathworks.com/cleve/2018/09/17/usa-traveling-salesman-tour/?s_tid=srchtitle_traveling#20salesman_1
#
#  Usage:
#
#    D = distances ( lon, lat )
#
#  Input:
#
#   real lon(*), lat(*): the longitude and latitude of several cities,
#   in degrees.
#
#  Output:
#
#    real D(*,*):  D(k,j) is the distance in miles between cities k and j.
#
#  Local:
#
#    real R: the radius of the earth in miles.
#
  import numpy as np

  R = 3959

  n = len ( lon )
  D = np.zeros ( [ n, n ] )
  lat = np.deg2rad ( lat )
  lon = np.deg2rad ( lon )

  for k in range ( 0, n ):
    for j in range ( 0, k ):
      D[k,j] = R * np.arccos ( np.sin ( lat[k] ) * np.sin ( lat[j] ) + \
        np.cos ( lat[k] ) * np.cos ( lat[j] ) * np.cos ( lon[k] - lon[j] ) )
      D[j,k] = D[k,j]

  return D

def path_length ( p, D ):

#*****************************************************************************80
#
## path_length() computes the current path length.
#
#  Discussion:
#
#    This function calculates the total length of the current path p
#    in the traveling salesman problem, using a distance matrix D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2023
#
#  Author:
#
#    Original MATLAB version by Cleve Moler.
#    This version by John Burkardt.
#
#  Reference:
#
#    Cleve Moler,
#    USA Traveling Salesman Tour,
#    Posted 17 September 2018,
#    logs.mathworks.com/cleve/2018/09/17/usa-traveling-salesman-tour/?s_tid=srchtitle_traveling#20salesman_1
#
#  Usage:
#
#    p_len = path_length ( p, D )
#
#  Input:
#
#    integer p(n): the sequence of cities in the current path.
#
#    real D(n,n): the city-to-city distance matrix.
#
#  Output:
#
#    real p_len: the current length of the path.
#
  n = D.shape[0]

  c2 = p[n-1]
  p_len = 0.0

  for i in range ( 0, n ):
    c1 = c2
    c2 = p[i]
    p_len = p_len + D[c1,c2]

  return p_len

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

def traveler ( D, rng ):

#*****************************************************************************80
#
## traveler() seeks an optimal path for the traveling salesperson problem.
#
#  Discussion:
#
#    This is a functional form of an old MATLAB demo called "travel".
#
#    It is a pretty good, but certainly not the best, solution of the
#    Traveling Salesman Problem (TSP).  
#
#    The goal is to form a closed circuit of a number of cities that 
#    requires the shortest total distance.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2023
#
#  Author:
#
#    Original MATLAB version by Cleve Moler.
#    This version by John Burkardt.
#
#  Reference:
#
#    Cleve Moler,
#    USA Traveling Salesman Tour,
#    Posted 17 September 2018,
#    logs.mathworks.com/cleve/2018/09/17/usa-traveling-salesman-tour/?s_tid=srchtitle_traveling#20salesman_1
#
#  Usage:
#
#   p_len, p = traveler ( D )
#
#  Input:
#
#   real D(n,n): distances between cities.
#
#    rng(): the current random number generator.
#
#  Output:
#
#   real p_len: the length of the itinerary in miles.
#
#   integer p(n+1): the cities listed in the order in which they will be
#   visited, including a return to the starting city.
#
  import numpy as np

  n = D.shape[0]
#
#  Choose an initial path at random.
#
  p = rng.permutation ( n )
  p_len = path_length ( p, D )

  for iter in range ( 0, 10000 ):
#
#  Try to reverse a portion of the path.
#
    pt1 = rng.integers ( 0, n )
    pt2 = rng.integers ( 0, n )

    lo = min ( pt1, pt2 )
    hi = max ( pt1, pt2 )

    q = np.arange ( n )
    q[lo:hi+1] = np.flip ( q[lo:hi+1] )
    pnew = p[q]
#
#  If better, take it.
#
    lennew = path_length ( pnew, D )
    if ( lennew < p_len ):
      p = pnew.copy()
      p_len = lennew
      iterp = iter
#
#  Try a single point insertion.
#
    pt1 = rng.integers ( 0, n )
    pt2 = rng.integers ( 0, n - 1 )

    q = np.arange ( n )
    q = np.delete ( q, pt1 )
    q = np.insert ( q, pt2+1, pt1 )
    pnew = p[q]
#
#  If better, take it.
#
    lennew = path_length ( pnew, D )
    if ( lennew < p_len ):
      p = pnew.copy()
      p_len = lennew
      iterp = iter
#
#  Close the permutation.
#
  p = np.append ( p, p[0] )

  return p_len, p

if ( __name__ == "__main__" ):
  timestamp ( )
  tsp_moler_test ( )
  timestamp ( )

