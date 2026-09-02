#! /usr/bin/env python3
#
def cities_test ( ):

#*****************************************************************************80
#
## cities_test() tests cities().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cities_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test cities().' )

  dist_table_check_test ( 'spaeth2_09' )
  dms_to_dist_test ( 'usca312' )
  dms_to_xy_test ( 'usca312' )
  point_to_dist_test ( 'wg22' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cities_test():' )
  print ( '  Normal end of execution.' )

  return

def dist_table_check ( n, dist_table ):

#*****************************************************************************80
#
## dist_table_check() checks a distance table.
#
#  Discussion:
#
#    1) All entries must be nonnegative.
#    2) Diagonal entries must be zero.
#    3) Off-diagonal entries must be symmetric.
#    4) The triangle inequality must be observed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of cities.
#
#    real DIST_TABLE(N,N), the distance table.
#
#  Output:
#
#    integer CHECK, the result of the check.
#    0, the matrix passed the checks.
#    1, Not all entries are nonnegative.
#    2, Not all diagonal entries are zero.
#    3, Not all off-diagonal entries are symmetric.
#    4, Not all entries satisfy the triangle inequality.
#
  import numpy as np

  if ( np.any ( dist_table < 0.0 ) ):
    check = 1
    return check

  for i in range ( 0, n ):
    if ( dist_table[i,i] != 0.0 ):
      check = 2
      return check


  for i in range ( 0, n ):
    for j in range ( 0, i ):
      if ( dist_table[i,j] != dist_table[j,i] ):
        check = 3
        return check

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        if ( dist_table[i,j] + dist_table[j,k] < dist_table[i,k] ):
          print ( '  dist_table[',i,',',j,']', \
                  '+ dist_table[',j,',',k,']', \
                  '< dist_table[',i,',',k,']' )
          print ( dist_table[i,j], \
                  dist_table[j,k], \
                  dist_table[i,k] )
          check = 4
          return check

  check = 0

  return check

def dist_table_check_test ( prefix ):

#*****************************************************************************80
#
## dist_table_check_test() tests dist_table_check().
#
#  Discussion:
#
#    Read a distance matrix and check it for consistency.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, the common file prefix.
#
  import numpy as np

  print ( '' )
  print ( 'dist_table_check_test():' )
  print ( '  dist_table_check() checks a distance table.' )

  dist_table_filename = prefix + '_dist.txt'

  print ( '' )
  print ( '  The distance table filename is "' + dist_table_filename + '"' )

  dist = np.loadtxt ( dist_table_filename )

  n1, n2 = dist.shape

  if ( n1 != n2 ):
    print ( '' )
    print ( '  The distance table is not square.' )
    raise Exception ( '  dist_table_check_test(): Fatal error!' )

  check = dist_table_check ( n1, dist )

  print ( '' )
  if ( check == 0 ):
    print ( '  0: The distance table passed all checks.' )
  elif ( check == 1 ):
    print ( '  1: The table failed the nonnegativity check.' )
  elif ( check == 2 ):
    print ( '  2: The table failed the zero self-distance check.' )
  elif ( check == 3 ):
    print ( '  3: The table failed the symmetry check.' )
  elif ( check == 4 ):
    print ( '  4: The table failed the triangle check.' )

  return

def dms_to_dist_test ( prefix ):

#*****************************************************************************80
#
## dms_to_dist_test() tests dms_to_dist.
#
#  Discussion:
#
#    Get the DMS coordinates of a set of cities, and compute
#    the city-to-city distance table, using distances on a sphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, the common file prefix.
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'dms_to_dist_test():' )
  print ( '  Get the DMS coordinates of a set of cities.' )
  print ( '  Compute the city-to-city distance table,' )
  print ( '  assuming the cities lie on a sphere (the earth).' )
#
#  Read D/M/S/L from file.
#
  dms_filename = prefix + '_dms.txt'
  print ( '  The DMS data is read from "' + dms_filename + '"' )

  w = []
  n = 0
  f = open ( dms_filename )
  for line in f:
    n = n + 1
    w.append ( line.split ( ) )
  f.close () 

  print ( '' )
  print ( '  The number of data items is', n )
#
#  Convert integer DMSL to real degrees.
#
  lat = np.zeros ( n )
  lon = np.zeros ( n )
  for i in range ( 0, n ):
    d = int ( w[i][0] )
    m = int ( w[i][1] )
    s = int ( w[i][2] )
    if ( w[i][3] == 'S' ):
      ns = -1
    else:
      ns = + 1
    lat[i] = ns * ( d + m / 60.0 + s / 3600.0 )
     
    d = int ( w[i][4] )
    m = int ( w[i][5] )
    s = int ( w[i][6] )
    if ( w[i][7] == 'W' ):
      ew = -1
    else:
      ew = + 1
    lon[i] = ew * ( d + m / 60.0 + s / 3600.0 )
#
#  Print.
#
  latlon = np.vstack ( ( lat, lon ) )
  latlon = np.transpose ( latlon )
  print ( '' )
  print ( '  lat, lon in degrees:' )
  pprint.pprint ( latlon )
 
  dist = ll_degrees_to_dist ( n, lat, lon )

  dist = np.round ( dist )

  print ( '' )
  print ( '  Initial 5x5 section of distance matrix:' )
  pprint.pprint ( dist[0:5,0:5] )

  print ( '' )
  print ( '  Physical distance from Atlanta to Boston  = ', dist[11,33] )
  print ( '  Road distance is 1037' )
  print ( '  Physical distance from Boston to Chicago  = ', dist[33,57] )
  print ( '  Road distance is  963' )
  print ( '  Physical distance from Chicago to Atlanta = ', dist[57,11] )
  print ( '  Road distance is  674' )

  return

def dms_to_xy ( n, lat, lon ):

#*****************************************************************************80
#
## dms_to_xy(): converts Latitude/Longitude in degrees to XY coordinates.
#
#  Discussion:
#
#    Essentially, the latitude and longitude information is treated
#    as though the Earth were a cylinder.  As long as the 
#    data is relatively close on the sphere (and far from either
#    pole) the distortion will not be too severe.  If the data
#    is closely clustered, and also near the equator, the
#    positions will be relatively accurate.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data items.
#
#    real LAT[n], LON[n], the latitude and longitude in degrees.
#
#  Output:
#
#    real POINT_XY[n,2], the point coordinates, in miles.
#
  import numpy as np

  radius = 3958.89

  xy = np.zeros ( [ n, 2 ] )

  for j in range ( 0, n ):
    xy[j,0] = lon[j] * radius * np.pi / 180.0
    xy[j,1] = lat[j] * radius * np.pi / 180.0

  return xy

def dms_to_xy_test ( prefix ):

#*****************************************************************************80
#
## dms_to_xy_test() tests dms_to_xy().
#
#  Discussion:
#
#    Get the DMS coordinates of a set of cities, and compute
#    the XY coordinates.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character PREFIX, the common file prefix.
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'dms_to_xy_test():' )
  print ( '  dms_to_xy() takes latitude and longitude' )
  print ( '  information, and assigns pseudo XY coordinates.' )
#
#  Read D/M/S/L from file.
#
  dms_filename = prefix + '_dms.txt'
  print ( '  The DMS data is read from "' + dms_filename + '"' )

  w = []
  n = 0
  f = open ( dms_filename )
  for line in f:
    n = n + 1
    w.append ( line.split ( ) )
  f.close () 

  print ( '' )
  print ( '  The number of data items is', n )
#
#  Convert integer DMSL to real degrees.
#
  lat = np.zeros ( n )
  lon = np.zeros ( n )
  for i in range ( 0, n ):
    d = int ( w[i][0] )
    m = int ( w[i][1] )
    s = int ( w[i][2] )
    if ( w[i][3] == 'S' ):
      ns = -1
    else:
      ns = + 1
    lat[i] = ns * ( d + m / 60.0 + s / 3600.0 )
     
    d = int ( w[i][4] )
    m = int ( w[i][5] )
    s = int ( w[i][6] )
    if ( w[i][7] == 'W' ):
      ew = -1
    else:
      ew = + 1
    lon[i] = ew * ( d + m / 60.0 + s / 3600.0 )
#
#  Print.
#
  latlon = np.vstack ( ( lat, lon ) )
  latlon = np.transpose ( latlon )
  print ( '' )
  print ( '  lat, lon in degrees:' )
  pprint.pprint ( latlon )

  xy = dms_to_xy ( n, lat, lon )

  print ( '' )
  print ( '  xy coordinates' )
  pprint.pprint ( xy )

  return

def ll_degrees_to_dist ( n, lat_dms, lon_dms ):

#*****************************************************************************80
#
## ll_degrees_to_dist() creates a distance table from latitudes and longitudes.
#
#  Discussion:
#
#    A distance function is used which is appropriate for the earth.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data items.
#
#    real lat_dms(n), lon_dms(n), the latitude and longitude, 
#    in degrees.
#
#  Output:
#
#    real DIST(N,N), the distance matrix.  Distances 
#    are measured in miles.
#
  import numpy as np

  dist = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      dist[i,j] = ll_degrees_to_distance_earth ( \
        lat_dms[i], lon_dms[i], \
        lat_dms[j], lon_dms[j] )
      dist[j,i] = dist[i,j]

  return dist

def ll_degrees_to_distance_earth ( lat1_dms, lon1_dms, lat2_dms, lon2_dms ):

#*****************************************************************************80
#
## ll_degrees_to_distance_earth() finds the distance between two points on the earth.
#
#  Discussion:
#
#    The positions of the the points are given as longitude and
#    latitude, measured in degrees, minutes, and seconds.
#
#    The distance is measured on the surface of the earth, which
#    is approximated by a sphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer LAT1_DMS, LON1_DMS, the latitude and 
#    longitude of the first point.
#
#    integer LAT2_DMS, LON2_DMS, the latitude and 
#    longitude of the second point.
#
#  Output:
#
#    real DIST, the distance between the points, in miles.
#
  import numpy as np

  lat1_rad = lat1_dms * np.pi / 180.0
  lon1_rad = lon1_dms * np.pi / 180.0

  lat2_rad = lat2_dms * np.pi / 180.0
  lon2_rad = lon2_dms * np.pi / 180.0

  theta = np.arccos ( \
      np.sin ( lat1_rad ) * np.sin ( lat2_rad ) \
    + np.cos ( lat1_rad ) * np.cos ( lat2_rad ) * np.cos ( lon1_rad - lon2_rad ) )

  radius = 3958.89

  dist = radius * theta

  return dist

def ll_degrees_to_xyz ( n, lat, lon ):

#*****************************************************************************80
#
## ll_degrees_to_xyz(): Latitude/Longitude in degrees to XYZ coordinates.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data items.
#
#    real LAT(N), LON(N), the latitude and longitude, in degrees.
#
#  Output:
#
#    real X(N), Y(N), Z(N) the point coordinates, in miles.
#
  import numpy as np

  lat = lat * np.pi / 180.0
  lon = lon * np.pi / 180.0

  r = 3958.89
  
  x = r * np.cos ( lat ) * np.cos ( lon )
  y = r * np.cos ( lat ) * np.sin ( lon )
  z = r * np.sin ( lat )

  return x, y, z

def ll_rad_dist_sphere ( lat1, long1, lat2, long2, radius ):

#*****************************************************************************80
#
## ll_rad_dist_sphere(): spherical distance, latitude and longitude in radians.
#
#  Discussion:
#
#    On a sphere of given radius, the positions of two points are given as
#    longitude and latitude, in radians.
#
#    This function determines the spherical distance or great circle distance,
#    between the two points.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 September 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real LAT1, LONG1, LAT2, LONG2, the latitude and
#    longitude of the two points, in radians.
#
#    real RADIUS, the radius of the sphere.
#
#  Output:
#
#    real DIST, the distance between the points.
#
  import numpy as np

  theta = np.arccos ( \
      np.sin ( lat1 ) * np.sin ( lat2 ) \
    + np.cos ( lat1 ) * np.cos ( lat2 ) * np.cos ( long1 - long2 ) )

  dist = radius * theta

  return dist

def point_to_dist ( dim_num, point_num, point ):

#*****************************************************************************80
#
## point_to_dist() creates a distance matrix from point coordinates.
#
#  Discussion:
#
#    The euclidean distance is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#
#    integer POINT_NUM, the number of points.
#
#    real point(point_num,dim_num): the  point coordinates.
#
#  Output:
#
#    real DIST(POINT_NUM,POINT_NUM), the distance matrix.
#
  import numpy as np

  dist = np.zeros ( [ point_num, point_num ] )

  for i in range ( 0, point_num ):
    for j in range ( i + 1, point_num ):
      dist[i,j] = np.linalg.norm ( point[i,:] - point[j,:] )
      dist[j,i] = dist[i,j]

  return dist

def point_to_dist_test ( prefix ):

#*****************************************************************************80
#
## point_to_dist_test() tests point_to_dist().
#
#  Discussion:
#
#    Get the XY coordinates of a set of cities, and compute
#    the city-to-city distance table.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, the common file prefix.
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'point_dist_test():' )
  print ( '  point_dist() computes a distance table from point locations.' )

  point_filename = prefix + '_xy.txt'

  print ( '' )
  print ( '  The point filename is "' + point_filename + '"' )

  xy = np.loadtxt ( point_filename )

  point_num, dim_num = xy.shape

  print ( '' )
  print ( '  The spatial dimension is', dim_num )
  print ( '  The number of points is', point_num )

  dist = point_to_dist ( dim_num, point_num, xy )

  dist = np.round ( dist )

  print ( '' )
  print ( '  Initial 5x5 section of distance matrix:' )
  pprint.pprint ( dist[0:5,0:5] )

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
  cities_test ( )
  timestamp ( )

