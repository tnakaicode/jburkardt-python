#! /usr/bin/env python3
#
def file_column_count ( filename ):

#*****************************************************************************80
#
## file_column_count() counts the number of words in a typical column of a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer COLUMN_COUNT, the number of words in a typical column.
#
  column_count = -1

  input = open ( filename, 'r' )

  column_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      elif ( column_count == 0 ):
        column_count = wc
        break

  input.close ( )

  return column_count

def file_column_count_test ( ):

#*****************************************************************************80
#
## file_column_count_test() tests file_column_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_column_count_test:' )
  print ( '  Count the number of columns in a typical text file line.' )

  filename = 'r8vec2_write_test.txt'
  column_count = file_column_count ( filename )

  print ( '' )
  print ( '  Number of columns in "%s" is %d' % ( filename, column_count ) )

  return

def file_row_count ( filename ):

#*****************************************************************************80
#
## file_row_count() counts the number of rows (lines) in a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer ROW_COUNT, the number of rows in the file.
#
  row_count = -1

  input = open ( filename, 'r' )

  row_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      else:
        row_count = row_count + 1

  input.close ( )

  return row_count

def file_row_count_test ( ):

#*****************************************************************************80
#
## file_row_count_test() tests file_row_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_row_count_test:' )
  print ( '  Count the number of rows in a text file.' )

  filename = 'r8vec2_write_test.txt'
  row_count = file_row_count ( filename )

  print ( '' )
  print ( '  Number of rows in "%s" is %d' % ( filename, row_count ) )

  return

def florida_cdf_pop ( pop ):

#*****************************************************************************80
#
## florida_cdf_pop() constructs a CDF for the Florida population census data.
#
#  Discussion:
#
#    Given the population counts for sites indexed 1 through N,
#    CDF(I) will be the sum of populations 0 through I-1, divided
#    by the total population.
#
#    Then a random number 0 <= R <= 1 can be used to randomly sample
#    the population, by finding I such that CDF(I) <= R < CDF(I+1).
#
#    This, in turn, can be used to identify a particular location
#    in Florida, using the index I to reference its longitude and latitude.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    int POP(N), the population of the city.
#
#    real CDF(N+1), the CDF for the population.
#
  import numpy as np

  n = len ( pop )
  cdf = np.zeros ( n + 1, dtype = np.float64 )
  for i in range ( 0, n ):
    cdf[i+1] = cdf[i] + pop[i]
#
#  Normalize.
#
  pop_sum = np.sum ( pop )
  cdf = cdf / float ( pop_sum )

  return cdf

def florida_cdf_pop_test ( ):

#*****************************************************************************80
#
## florida_cdf_pop_test() tests florida_cdf_pop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_cdf_pop_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  florida_cdf_pop() constructs a cumulative distribution function (CDF)' )
  print ( '  from a vector of population data.' )
  print ( '' )
  print ( '  Note that CDF is indexed 1 through N+1.' )
#
#  Read the longitude, latitude, population of each census tract.
#
  filename = 'florida_census.txt'

  lon, lat, pop = florida_census_reader ( filename )
#
#  Construct the CDF.
#
  cdf = florida_cdf_pop ( pop )
#
#  Get the size of the data.
#
  n = len ( lon )
#
#  Print some of the data.
#
  print ( '' )
  print ( '       #        POP             CDF' )
  print ( '' )
  print ( '%8d                         %14.6g' % ( 0, cdf[0] ) )
  for i in range ( 0, n ):
    if ( i < 10 or n - 10 <= i ):
      print ( '%8d  %8d  %14.6g' % ( i, pop[i], cdf[i+1] ) )
    elif ( i == 10 ):
      print ( '........  ...........  ........  ..............' )

  return

def florida_census_reader ( filename ):

#*****************************************************************************80
#
## florida_census_reader() reads a simplified Florida census file.
#
#  Discussion:
#
#    Each line has a geometric location ID, population, longitude, latitude.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    real LON(M), LAT(M), the longitude and latitude.
#
#    integer POP(M), the population.
#
  import numpy as np

  m = 4245

  input = open ( filename, 'r' )

  pop = np.zeros ( m, dtype = np.int32 )
  lon = np.zeros ( m, dtype = np.float64 )
  lat = np.zeros ( m, dtype = np.float64 )

  i = 0
  for line in input:

    data = line.split ( )
    id = int ( data[0] )
    pop[i] = int ( data[1] )
    lon[i] = float ( data[2] )
    lat[i] = float ( data[3] )
    i = i + 1

  input.close ( )

  return lon, lat, pop

def florida_census_reader_test ( ):

#*****************************************************************************80
#
## florida_census_reader_test() tests florida_census_reader().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_census_reader_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_census_reader reads data from a cut down census file.' )

  filename = 'florida_census.txt'
  lon, lat, pop = florida_census_reader ( filename )

  n = len ( lon )

  print ( '' )
  print ( ' Index  Longitude    Latitude    Population' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %14.6g  %14.6g  %8d' % ( i, lon[i], lat[i], pop[i] ) )

  return

def florida_centroid_pop ( gen_lon, gen_lat, sample_num, pop_lon, pop_lat, \
  pop_cdf ):

#*****************************************************************************80
#
## florida_centroid_pop() estimates centroids of Voronoi regions, given generators.
#
#  Discussion:
#
#    The calculation is based on population sampling.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Input:
#
#    real GEN_LON(*), GEN_LAT(*), the longitude and latitude 
#    of generators to be displayed on a map of Florida.
#
#    integer SAMPLE_NUM, the number of samples to use.
#
#    real POP_LON(M), POP_LAT(M), the longitude and latitude for
#    the population data points.
#
#    real POP_cdf(M+1), the CDF for the population.
#
#  Output:
#
#    real CEN_LON(*), CEN_LAT(*), the longitude and latitude 
#    of the population centroids of the Voronoi regions.
#
  import numpy as np
#
#  Initialize the counts for each generator.
#
  n = len ( gen_lon )
  cen_lat = np.zeros ( n, dtype = np.float64 )
  cen_lon = np.zeros ( n, dtype = np.float64 )
  cen_count = np.zeros ( n, dtype = np.int32 )
#
#  Choose random persons in Florida.
#
  indx = florida_sample_pop ( sample_num, pop_cdf )
#
#  Associate each sample person with one of the generators.
#
  for s in range ( 0, sample_num ):

    d_min = np.Inf
    i_min = -1
    for i in range ( 0, n ):
      d = ( pop_lat[indx[s]] - gen_lat[i] ) ** 2 \
        + ( pop_lon[indx[s]] - gen_lon[i] ) ** 2
      if ( d < d_min ):
        d_min = d
        i_min = i

    cen_lat[i_min] = cen_lat[i_min] + pop_lat[indx[s]]
    cen_lon[i_min] = cen_lon[i_min] + pop_lon[indx[s]]
    cen_count[i_min] = cen_count[i_min] + 1
#
#  Set the centroid estimates.
#
  for i in range ( 0, n ):
    if ( cen_count[i] == 0 ):
      cen_lon[i] = gen_lon[i]
      cen_lat[i] = gen_lat[i]
    else:
      cen_lon[i] = cen_lon[i] / cen_count[i]
      cen_lat[i] = cen_lat[i] / cen_count[i]

  return cen_lon, cen_lat

def florida_centroid_pop_test ( ):

#*****************************************************************************80
#
## florida_centroid_pop_test() tests florida_centroid_pop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_centroid_pop_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_centroid_pop can estimate the centroids of' )
  print ( '  the Voronoi cells associated with a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )
#
#  Set the generator data.
#
  names = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  gen_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )

  gen_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )
#
#  Read the longitude, latitude, population of each census tract.
#
  filename = 'florida_census.txt'

  pop_lon, pop_lat, pop_count = florida_census_reader ( filename )
#
#  Construct the CDF.
#
  pop_cdf = florida_cdf_pop ( pop_count )
#
#  Estimate the centroids.
#
  sample_num = 5000

  cen_lon, cen_lat = florida_centroid_pop ( gen_lon, \
    gen_lat, sample_num, pop_lon, pop_lat, pop_cdf )
#
#  Show generators, centroids, and Voronoi region together.
# 
  filename = 'florida_centroid_pop.png'

  plot_title = 'Population centroids (red) of Voronoi cells for cities (black).'

  florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, filename, \
    plot_title )

  return

def florida_cvt_pop ( gen_lon, gen_lat, pop_lon, pop_lat, pop_cdf ):

#*****************************************************************************80
#
## florida_cvt_pop() estimates a CVT for Florida based on population data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real GEN_LON(N), GEN_LAT(N), points to be used as the initial
#    generators.
#
#    real POP_LON(M), POP_LAT(M), the longitude and latitude for
#    the population data points.
#
#    real POP_cdf(M+1), the CDF for the population.
#
#  Output:
#
#    real GEN_LON(N), GEN_LAT(N), improved estimates of the CVT
#    generators.
#

#
#  The N points are are first estimate of the CVT generators.
#
  n = len ( gen_lon )
#
#  Display the points.
#
  filename = ''
  plot_title = 'Initial CVT Generator Estimates'
  florida_point_display ( gen_lon, gen_lat, filename, plot_title )
#
#  Prepare for random sampling.
#
  sample_num = 5000

  for step in range ( 1, 11 ):

    cen_lon, cen_lat = florida_centroid_pop ( gen_lon, gen_lat, \
      sample_num, pop_lon, pop_lat, pop_cdf )

    filename = ''
    plot_title = ( 'CVT Step %d' % ( step ) )
    florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, filename, \
      plot_title )

    filename = ''
    plot_title = ( 'Generators after step %d' % ( step ) )
    florida_point_display ( cen_lon, cen_lat, filename, plot_title )

    gen_lon = cen_lon
    gen_lat = cen_lat

  return gen_lon, gen_lat

def florida_cvt_pop_test ( ):

#*****************************************************************************80
#
## florida_cvt_pop_test() tests florida_cvt_pop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_cvt_pop_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_cvt_pop can estimate the population centroidal' )
  print ( '  Voronoi tessellation (CVT) of a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )
#
#  Read the longitude, latitude, population and geoid of each census tract.
#
  filename = 'florida_census.txt'
  pop_lon, pop_lat, pop_count = florida_census_reader ( filename )
#
#  Construct the CDF.
#
  pop_cdf = florida_cdf_pop ( pop_count )
#
#  Select N locations uniformly at random with respect to population.
#
  n = 27
  indx = florida_sample_pop ( n, pop_cdf )
  gen_lat = pop_lat[indx[0:n]]
  gen_lon = pop_lon[indx[0:n]]
#
#  Estimate the CVT.
#
  gen_lon, gen_lat = florida_cvt_pop ( gen_lon, gen_lat, pop_lon, pop_lat, \
    pop_cdf )
#
#  Estimate the centroids.
#
  sample_num = 5000
  cen_lon, cen_lat = florida_centroid_pop ( gen_lon, gen_lat, \
    sample_num, pop_lon, pop_lat, pop_cdf )
#
#  Show generators, centroids, and Voronoi region together.
#
  filename = 'florida_cvt_pop.png'
  plot_title = ( '%d-Generator population CVT' % ( n ) )
  florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, filename, plot_title )

  return

def florida_pdf_pop ( pop ):

#*****************************************************************************80
#
## florida_pdf_pop() constructs a PDF for the Florida population census data.
#
#  Discussion:
#
#    Given the population counts for sites indexed 1 through N,
#    PDF(I) will be the populations of district I divided by the total.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    int POP(N), the population for each census location.
#
#    real PDF(N), the PDF for the population.
#
  import numpy as  np
#
#  Normalize.
#
  n = len ( pop )
  pdf = np.zeros ( n )
  pop_sum = float ( np.sum ( pop ) )
  pdf[0:n] = pop[0:n] / pop_sum

  return pdf

def florida_pdf_pop_test ( ):

#*****************************************************************************80
#
## florida_pdf_pop_test() tests florida_pdf_pop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_pdf_pop_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_pdf_pop constructs a probability distribution function (PDF)' )
  print ( '  from a vector of population data.' )
#
#  Read the longitude, latitude, population and geoid of each census tract.
#
  filename = 'florida_census.txt'

  lon, lat, pop = florida_census_reader ( filename )
#
#  Construct the PDF.
#
  pdf = florida_pdf_pop ( pop )
#
#  Get the size of the data.
#
  n = len ( lon )
#
#  Print some of the data.
#
  print ( '' )
  print ( '       #        POP             PDF' )
  print ( '' )
  for i in range ( 0, n ):
    if ( i < 10 or n - 10 <= i ):
      print ( '%8d  %8d  %14.6g' % ( i, pop[i], pdf[i] ) )
    elif ( i == 10 ):
      print ( '........  ........  ..............' )

  return

def florida_point_display ( p_lon, p_lat, filename, plot_title ):

#*****************************************************************************80
#
## florida_point_display() displays points within the boundaries of Florida.
#
#  Discussion:
#
#    The points are assumed to be given in terms of longitude and latitude.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 November 2016
#
#  Input:
#
#    real P_LON(*), P_LAT(*), the longitude and latitude of the points.
#
#    string FILENAME, a name for the graphics file.
#    If FILENAME is '', the plot is not saved.
#
#    string PLOT_TITLE, a title for the plot.
#
  import matplotlib.pyplot as plt

  f_lon, f_lat = florida_shape_read ( )

  plt.plot ( f_lon, f_lat, linewidth = 2, color = 'g' )

  plt.plot ( p_lon, p_lat, 'ro', markersize = 15 )

  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( 'Longitude' )
  plt.ylabel ( 'Latitude' )
  plt.title ( plot_title )
  if ( 0 < len ( filename ) ):
    plt.savefig ( filename )
    print ( '' )
    print ( '  Graphics data saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def florida_point_display_test ( ):

#*****************************************************************************80
#
## florida_point_display_test() tests florida_point_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_point_display_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_point_display can display a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )

  name = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  p_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )

  p_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )

  filename = 'florida_point_display.png'
  plot_title = 'Seven Florida Cities'
  florida_point_display ( p_lon, p_lat, filename, plot_title )

  return

def florida_sample_pop ( n, cdf ):

#*****************************************************************************80
#
## florida_sample_pop() randomly samples the Florida population data.
#
#  Discussion:
#
#    M census districts have been given, and for each district,
#    a total population was listed.
#
#    A CDF vector CDF(1:M+1) was created, such that CDF(I) is the probability
#    that a person resides in a district of index less than or equal to I.
#
#    We now ask for N random samples of the population, which means we will
#    return N values I between 1 and M, selected randomly and weighted by
#    population.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of random samples requested.
#
#    real CDF(M+1), the CDF for the population.
#
#  Output:
#
#    integer INDX(N), a sequence of indices between 0 and N - 1.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  rvec = rng.random ( size = n )

  indx = np.zeros ( n, dtype = np.int32 )

  m = len ( cdf )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( rvec[j] <= cdf[i+1] ):
        indx[j] = i
        break      

  return indx

def florida_sample_pop_test ( ):

#*****************************************************************************80
#
## florida_sample_pop_test() tests florida_sample_pop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_sample_pop_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_sample_pop randomly samples census districts' )
  print ( '  weighted by population.' )
#
#  Read the longitude, latitude, population and geoid of each census tract.
#
  filename = 'florida_census.txt'

  lon, lat, pop = florida_census_reader ( filename )
#
#  Construct the PDF, just for printing convenience.
#
  pdf = florida_pdf_pop ( pop )
#
#  Construct the CDF.
#
  cdf = florida_cdf_pop ( pop )
#
#  Get N random samples.
#
  n = 50

  indx = florida_sample_pop ( n, cdf )
#
#  Print some of the data.
#
  print ( '' )
  print ( '       #      INDX        POP             PDF' )
  print ( '' )

  for i in range ( 0, n ):
    if ( i <= 9 or n - 10 <= i ):
      print ( '%8d  %8d  %8d  %14.6f' % ( i, indx[i], pop[indx[i]], pdf[indx[i]] ) )
    elif ( i == 10 ):
      print ( '........  ........  ...........  ........  ..............' )
#
#  Plot the sample points.
#
  filename = 'florida_sample_pop.png'
  plot_title = '50 spots uniformly sampled by populiation'
  florida_point_display ( lon[indx[0:n]], lat[indx[0:n]], filename, plot_title )

  return

def florida_shape_display ( lon, lat, filename, plot_title ):

#*****************************************************************************80
#
## florida_shape_display() displays the shape of Florida.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Input:
#
#    real LON(*), LAT(*), the longitude and latitude of the points.
#
#    string FILENAME, a name for the graphics file.
#
#    string PLOT_TITLE, a title for the plot.
#
  import matplotlib.pyplot as plt

  plt.plot ( lon, lat, linewidth = 2, color = 'r' )
  plt.axis ( 'equal' )
  plt.grid ( 'on' )
  plt.xlabel ( 'Longitude' )
  plt.ylabel ( 'Latitude' )
  plt.title ( plot_title )
  if ( 0 < len ( filename ) ):
    plt.savefig ( filename )
    print ( '' )
    print ( '  Plot saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def florida_shape_display_test ( ):

#*****************************************************************************80
#
## florida_shape_display_test() tests florida_shape_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'florida_shape_display_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_shape_display displays the shape of Florida.' )

  filename = 'florida_shape.txt'
  m = r8vec2_header_read ( filename )
  lon, lat = r8vec2_data_read ( filename, m )

  filename = 'florida_shape_display.png'
  plot_title = 'The shape of Florida'

  florida_shape_display ( lon, lat, filename, plot_title )

  return

def florida_shape_read ( ):

#*****************************************************************************80
#
## florida_shape_read() extracts the low resolution Florida polygon.
#
#  Discussion:
#
#    The MATLAB Mapping Toolbox includes information about high and
#    low resolution polygonal models of US States.  We want to examine
#    the low resolution polygonal model of Florida.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Output:
#
#    real LON(*), LAT(*), the longitude and latitude of the
#    polygonal vertices, listed in counterclockwise order.
#
  filename = 'florida_shape.txt'
  m = r8vec2_header_read ( filename )
  lon, lat = r8vec2_data_read ( filename, m )

  return lon, lat

def florida_shape_read_test ( ):

#*****************************************************************************80
#
## florida_shape_read_test() tests florida_shape_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_shape_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_shape_read returns informaition defining' )
  print ( '  a low-resolution polygonal model of Florida.' )

  lon, lat = florida_shape_read ( )
#
#  Print some of the information.
#
  n = len ( lon )
  r8vec2_print_some ( n, lon, lat, 10, \
    '  Longitude/Latitude, Florida Polygon Vertices:' ) 
#
#  Show generators, centroids, and Voronoi region together.
# 
  filename = 'florida_shape_read.png';
  plot_title = 'Low resolution polygonal outline of Florida';
  florida_shape_display ( lon, lat, filename, plot_title );

  return

def florida_voronoi_display ( g_lon, g_lat, p_lon, p_lat, filename, plot_title ):

#*****************************************************************************80
#
## florida_voronoi_display() displays generators, and their Voronoi diagram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 November 2016
#
#  Input:
#
#    real G_LON(*), G_LAT(*), the longitude and latitude of 
#    generators to be displayed on a map of Florida, using black dots.
#
#    real P_LON(*), P_LAT(*), additional points, to be shown using
#    red dots.
#
#    string FILENAME, a name for the graphics file.
#    If FILENAME is '', the plot is not saved.
#
#    string PLOT_TITLE, a title for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy.spatial as spatial
#
#  Determine the Voronoi diagram for the generators.
#
  g_num = len ( g_lon )
  g = np.zeros ( [ g_num, 2 ] )
  g[:,0] = g_lon[:]
  g[:,1] = g_lat[:]

  vor = spatial.Voronoi ( g )
#
#  Plot the Voronoi diagram.
#
  spatial.voronoi_plot_2d ( vor )
#
#  Get the Florida information.
#
  f_lon, f_lat = florida_shape_read ( )
#
#  Draw the outline of Florida.
#
  plt.plot ( f_lon, f_lat, linewidth = 2, color = 'g' )
#
#  Include the auxilliary points.
#
  plt.plot ( p_lon, p_lat, 'ro', markersize = 15 )
#
#  More plot stuff.
#
  plt.axis ( 'equal' )
  plt.grid ( 'on' )
  plt.xlabel ( 'Longitude' )
  plt.ylabel ( 'Latitude' )
  plt.title ( plot_title )
  if ( 0 < len ( filename ) ):
    plt.savefig ( filename )
    print ( '' )
    print ( '  Graphics data saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def florida_voronoi_display_test ( ):

#*****************************************************************************80
#
## florida_voronoi_display_test() tests florida_voronoi_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_voronoi_display_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_voronoi_display can display a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes,' )
  print ( '  and the Voronoi diagram they generate.' )

  name = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  g_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )

  g_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )

  p_lon = []
  p_lat = []

  filename = 'florida_voronoi_display.png'
  plot_title = 'Voronoi diagram for 7 Florida cities'

  florida_voronoi_display ( g_lon, g_lat, p_lon, p_lat, filename, plot_title )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec2_data_read ( filename, m ):

#*****************************************************************************80
#
## r8vec2_data_read() reads the data from an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is an pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#  Output:
#
#    real X(M), Y(M), the data.
#
  import numpy as np

  input = open ( filename, 'r' )

  x = np.zeros ( m )
  y = np.zeros ( m )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      data = line.split ( )
      x[i] = data[0]
      y[i] = data[1]
      i = i + 1

  input.close ( )

  return x, y

def r8vec2_data_read_test ( ):

#*****************************************************************************80
#
## r8vec2_data_read_test() tests r8vec2_data_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8vec2_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_data_read reads data from an R8VEC2.' )

  m = 5
  filename = 'r8vec2_write_test.txt'
  x, y = r8vec2_data_read ( filename, m )
  r8vec2_print ( m, x, y, '  Data read from file:' )

  return

def r8vec2_header_read ( filename ):

#*****************************************************************************80
#
## r8vec2_header_read() reads the header from an R8VEC2 file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of rows in the file.
#
  n = file_column_count ( filename )

  if ( n != 2 ):
    print ( '' )
    print ( 'r8vec2_header_read - Fatal error!' )
    print ( '  The number of columns is not 2, but %d.' % ( n ) )
    raise Exception ( 'r8vec2_header_read - Fatal error!' )

  m = file_row_count ( filename )

  return m

def r8vec2_header_read_test ( ):

#*****************************************************************************80
#
## r8vec2_header_read_test() tests r8vec2_header_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_header_read counts rows in a file containing an R8VEC2.' )

  filename = 'r8vec2_write_test.txt'
  m = r8vec2_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )

  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
## r8vec2_print_some() prints some of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_print, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vectors.
#
#    real X1(N), X2(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

  return

def r8vec2_print_some_test ( ):

#*****************************************************************************80
#
## r8vec2_print_some_test() tests r8vec2_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 100
  a = np.zeros ( n )
  b = np.zeros ( n )

  for i in range ( 0, n ):
    x = float ( i + 1 )
    a[i] = x * x
    b[i] = np.sqrt ( x )

  print ( '' )
  print ( 'r8vec2_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print_some prints some of a pair of R8VEC\'s.' )

  r8vec2_print_some ( n, a, b, 10, '  Square and square root:' )

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

  return None

def florida_cvt_pop_tests ( ):

#*****************************************************************************80
#
## florida_cvt_pop_tests() tests florida_cvt_pop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_cvt_pop_tests():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test florida_cvt_pop().' )

  file_column_count_test ( )
  file_row_count_test ( )
  florida_cdf_pop_test ( )
  florida_census_reader_test ( )
  florida_centroid_pop_test ( )
  florida_cvt_pop_test ( )
  florida_pdf_pop_test ( )
  florida_point_display_test ( )
  florida_sample_pop_test ( )
  florida_shape_display_test ( )
  florida_shape_read_test ( )
  florida_voronoi_display_test ( )
  r8vec2_data_read_test ( )
  r8vec2_header_read_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'florida_cvt_pop_tests():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  florida_cvt_pop_tests ( )
  timestamp ( )
 
