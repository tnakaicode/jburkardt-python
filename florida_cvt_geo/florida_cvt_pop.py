#! /usr/bin/env python3
#
def file_column_count ( filename ):

#*****************************************************************************80
#
## FILE_COLUMN_COUNT counts the number of words in a typical column of a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the file.
#
#    Output, integer COLUMN_COUNT, the number of words in a typical column.
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
## FILE_COLUMN_COUNT_TEST tests FILE_COLUMN_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FILE_COLUMN_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of columns in a typical text file line.' )

  filename = 'r8vec2_write_test.txt'
  column_count = file_column_count ( filename )

  print ( '' )
  print ( '  Number of columns in "%s" is %d' % ( filename, column_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_COLUMN_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def file_row_count ( filename ):

#*****************************************************************************80
#
## FILE_ROW_COUNT counts the number of rows (lines) in a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the file.
#
#    Output, integer ROW_COUNT, the number of rows in the file.
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
## FILE_ROW_COUNT_TEST tests FILE_ROW_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FILE_ROW_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of rows in a text file.' )

  filename = 'r8vec2_write_test.txt'
  row_count = file_row_count ( filename )

  print ( '' )
  print ( '  Number of rows in "%s" is %d' % ( filename, row_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_ROW_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_cdf_pop ( pop ):

#*****************************************************************************80
#
## FLORIDA_CDF_POP constructs a CDF for the Florida population census data.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, int POP(N), the population of the city.
#
#    Output, real CDF(N+1), the CDF for the population.
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
## FLORIDA_CDF_POP_TEST tests FLORIDA_CDF_POP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_CDF_POP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_CDF_POP constructs a cumulative distribution function (CDF)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_CDF_POP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_census_reader ( filename ):

#*****************************************************************************80
#
## FLORIDA_CENSUS_READER reads a simplified Florida census file.
#
#  Discussion:
#
#    Each line has a geometric location ID, population, longitude, latitude.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Output, real LON(M), LAT(M), the longitude and latitude.
#
#    Output, integer POP(M), the population.
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
## FLORIDA_CENSUS_READ_TEST tests FLORIDA_CENSUS_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_CENSUS_READER_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_CENSUS_READER reads data from a cut down census file.' )

  filename = 'florida_census.txt'
  lon, lat, pop = florida_census_reader ( filename )

  n = len ( lon )

  print ( '' )
  print ( ' Index  Longitude    Latitude    Population' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %14.6g  %14.6g  %8d' % ( i, lon[i], lat[i], pop[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_CENSUS_READER_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_centroid_pop ( gen_lon, gen_lat, sample_num, pop_lon, pop_lat, \
  pop_cdf, seed ):

#*****************************************************************************80
#
## FLORIDA_CENTROID_POP estimates centroids of Voronoi regions, given generators.
#
#  Discussion:
#
#    The calculation is based on population sampling.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Parameters:
#
#    Input, real GEN_LON(*), GEN_LAT(*), the longitude and latitude 
#    of generators to be displayed on a map of Florida.
#
#    Input, integer SAMPLE_NUM, the number of samples to use.
#
#    Input, real POP_LON(M), POP_LAT(M), the longitude and latitude for
#    the population data points.
#
#    Input, real POP_CDF(M+1), the CDF for the population.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real CEN_LON(*), CEN_LAT(*), the longitude and latitude 
#    of the population centroids of the Voronoi regions.
#
#    Output, integer SEED, a seed for the random number generator.
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
  indx, seed = florida_sample_pop ( sample_num, pop_cdf, seed )
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

  return cen_lon, cen_lat, seed

def florida_centroid_pop_test ( ):

#*****************************************************************************80
#
## FLORIDA_CENTROID_POP_TEST tests FLORIDA_CENTROID_POP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_CENTROID_POP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_CENTROID_POP can estimate the centroids of' )
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
  seed = 123456789
  cen_lon, cen_lat, seed = florida_centroid_pop ( gen_lon, \
    gen_lat, sample_num, pop_lon, pop_lat, pop_cdf, seed )
#
#  Show generators, centroids, and Voronoi region together.
# 
  filename = 'florida_centroid_pop.png'

  plot_title = 'Population centroids (red) of Voronoi cells for cities (black).'

  florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, filename, \
    plot_title )
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_CENTROID_POP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_cvt_pop ( gen_lon, gen_lat, pop_lon, pop_lat, pop_cdf ):

#*****************************************************************************80
#
## FLORIDA_CVT_POP estimates a CVT for Florida based on population data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real GEN_LON(N), GEN_LAT(N), points to be used as the initial
#    generators.
#
#    Input, real POP_LON(M), POP_LAT(M), the longitude and latitude for
#    the population data points.
#
#    Input, real POP_CDF(M+1), the CDF for the population.
#
#    Output, real GEN_LON(N), GEN_LAT(N), improved estimates of the CVT
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
  seed = 123456789

  for step in range ( 1, 11 ):

    cen_lon, cen_lat, seed = florida_centroid_pop ( gen_lon, gen_lat, \
      sample_num, pop_lon, pop_lat, pop_cdf, seed )

    filename = ''
    plot_title = ( 'CVT Step %d' % ( step ) )
    florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, filename, plot_title )

    filename = ''
    plot_title = ( 'Generators after step %d' % ( step ) )
    florida_point_display ( cen_lon, cen_lat, filename, plot_title )

    gen_lon = cen_lon
    gen_lat = cen_lat

  return gen_lon, gen_lat

def florida_cvt_pop_test ( ):

#*****************************************************************************80
#
## FLORIDA_CVT_POP_TEST tests FLORIDA_CVT_POP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_CVT_POP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_CVT_POP can estimate the population centroidal' )
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
  seed = 123456789
  indx, seed = florida_sample_pop ( n, pop_cdf, seed )
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
  seed = 123456789
  cen_lon, cen_lat, seed = florida_centroid_pop ( gen_lon, gen_lat, \
    sample_num, pop_lon, pop_lat, pop_cdf, seed );
#
#  Show generators, centroids, and Voronoi region together.
#
  filename = 'florida_cvt_pop.png'
  plot_title = ( '%d-Generator population CVT' % ( n ) )
  florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, filename, plot_title )
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_CVT_POP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_pdf_pop ( pop ):

#*****************************************************************************80
#
## FLORIDA_PDF_POP constructs a PDF for the Florida population census data.
#
#  Discussion:
#
#    Given the population counts for sites indexed 1 through N,
#    PDF(I) will be the populations of district I divided by the total.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, int POP(N), the population for each census location.
#
#    Output, real PDF(N), the PDF for the population.
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
## FLORIDA_PDF_POP_TEST tests FLORIDA_PDF_POP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_PDF_POP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_PDF_POP constructs a probability distribution function (PDF)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_PDF_POP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_point_display ( p_lon, p_lat, filename, plot_title ):

#*****************************************************************************80
#
## FLORIDA_POINT_DISPLAY displays points within the boundaries of Florida.
#
#  Discussion:
#
#    The points are assumed to be given in terms of longitude and latitude.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Parameters:
#
#    Input, real P_LON(*), P_LAT(*), the longitude and latitude of the points.
#
#    Input, string FILENAME, a name for the graphics file.
#    If FILENAME is '', the plot is not saved.
#
#    Input, string PLOT_TITLE, a title for the plot.
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

  return

def florida_point_display_test ( ):

#*****************************************************************************80
#
## FLORIDA_POINT_DISPLAY_TEST tests FLORIDA_POINT_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_POINT_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_POINT_DISPLAY can display a set of points' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_POINT_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_sample_pop ( n, cdf, seed ):

#*****************************************************************************80
#
## FLORIDA_SAMPLE_POP randomly samples the Florida population data.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of random samples requested.
#
#    Input, real CDF(M+1), the CDF for the population.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer INDX(N), a sequence of indices between 0 and N - 1.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np

  rvec, seed = r8vec_uniform_01 ( n, seed )

  indx = np.zeros ( n, dtype = np.int32 )

  m = len ( cdf )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( rvec[j] <= cdf[i+1] ):
        indx[j] = i
        break      

  return indx, seed

def florida_sample_pop_test ( ):

#*****************************************************************************80
#
## FLORIDA_SAMPLE_POP_TEST tests FLORIDA_SAMPLE_POP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_SAMPLE_POP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_SAMPLE_POP randomly samples census districts' )
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
  seed = 123456789
  indx, seed = florida_sample_pop ( n, cdf, seed )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_SAMPLE_POP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_shape_display ( lon, lat, filename, plot_title ):

#*****************************************************************************80
#
## FLORIDA_SHAPE_DISPLAY displays the shape of Florida.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Parameters:
#
#    Input, real LON(*), LAT(*), the longitude and latitude of the points.
#
#    Input, string FILENAME, a name for the graphics file.
#
#    Input, string PLOT_TITLE, a title for the plot.
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

  return

def florida_shape_display_test ( ):

#*****************************************************************************80
#
## FLORIDA_SHAPE_DISPLAY_TEST tests FLORIDA_SHAPE_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_SHAPE_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_SHAPE_DISPLAY displays the shape of Florida.' )

  filename = 'florida_shape.txt'
  m = r8vec2_header_read ( filename )
  lon, lat = r8vec2_data_read ( filename, m )

  filename = 'florida_shape_display.png'
  plot_title = 'The shape of Florida'

  florida_shape_display ( lon, lat, filename, plot_title )
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_SHAPE_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_shape_read ( ):

#*****************************************************************************80
#
## FLORIDA_SHAPE_READ extracts the low resolution Florida polygon.
#
#  Discussion:
#
#    The MATLAB Mapping Toolbox includes information about high and
#    low resolution polygonal models of US States.  We want to examine
#    the low resolution polygonal model of Florida.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Parameters:
#
#    Output, real LON(*), LAT(*), the longitude and latitude of the
#    polygonal vertices, listed in counterclockwise order.
#
  filename = 'florida_shape.txt'
  m = r8vec2_header_read ( filename )
  lon, lat = r8vec2_data_read ( filename, m )

  return lon, lat

def florida_shape_read_test ( ):

#*****************************************************************************80
#
## FLORIDA_SHAPE_READ_TEST tests FLORIDA_SHAPE_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_SHAPE_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_SHAPE_READ returns informaition defining' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_SHAPE_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_voronoi_display ( g_lon, g_lat, p_lon, p_lat, filename, plot_title ):

#*****************************************************************************80
#
## FLORIDA_VORONOI_DISPLAY displays generators, and their Voronoi diagram.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2016
#
#  Parameters:
#
#    Input, real G_LON(*), G_LAT(*), the longitude and latitude of 
#    generators to be displayed on a map of Florida, using black dots.
#
#    Input, real P_LON(*), P_LAT(*), additional points, to be shown using
#    red dots.
#
#    Input, string FILENAME, a name for the graphics file.
#    If FILENAME is '', the plot is not saved.
#
#    Input, string PLOT_TITLE, a title for the plot.
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

  return

def florida_voronoi_display_test ( ):

#*****************************************************************************80
#
## FLORIDA_VORONOI_DISPLAY_TEST tests FLORIDA_VORONOI_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_VORONOI_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FLORIDA_VORONOI_DISPLAY can display a set of points' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_VORONOI_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_data_read ( filename, m ):

#*****************************************************************************80
#
## R8VEC2_DATA_READ reads the data from an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is an pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Input, integer M, the number of rows in the file.
#
#    Output, real X(M), Y(M), the data.
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
## R8VEC2_DATA_READ_TEST tests R8VEC2_DATA_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8VEC2_DATA_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_DATA_READ reads data from an R8VEC2.' )

  m = 5
  filename = 'r8vec2_write_test.txt'
  x, y = r8vec2_data_read ( filename, m )
  r8vec2_print ( m, x, y, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_DATA_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_header_read ( filename ):

#*****************************************************************************80
#
## R8VEC2_HEADER_READ reads the header from an R8VEC2 file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Output, integer M, the number of rows in the file.
#
  n = file_column_count ( filename )

  if ( n != 2 ):
    print ( '' )
    print ( 'R8VEC2_HEADER_READ - Fatal error!' )
    print ( '  The number of columns is not 2, but %d.' % ( n ) )
    exit ( 'R8VEC2_HEADER_READ - Fatal error!' )

  m = file_row_count ( filename )

  return m

def r8vec2_header_read_test ( ):

#*****************************************************************************80
#
## R8VEC2_HEADER_READ_TEST tests R8VEC2_HEADER_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8VEC2_HEADER_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_HEADER_READ counts rows in a file containing an R8VEC2.' )

  filename = 'r8vec2_write_test.txt'
  m = r8vec2_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_HEADER_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
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
## R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT_SOME prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_PRINT, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vectors.
#
#    Input, real X1(N), X2(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines to print.
#
#    Input, string TITLE, a title.
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
## R8VEC2_PRINT_SOME_TEST tests R8VEC2_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8VEC2_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT_SOME prints some of a pair of R8VEC\'s.' )

  r8vec2_print_some ( n, a, b, 10, '  Square and square root:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
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

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def florida_cvt_pop_tests ( ):

#*****************************************************************************80
#
## FLORIDA_CVT_POP_TESTS tests the FLORIDA_CVT_POP library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'FLORIDA_CVT_POP_TESTS' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the FLORIDA_CVT_POP library.' )

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
  r8_uniform_01_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec2_data_read_test ( )
  r8vec2_header_read_test ( )
  r8vec2_print_test ( )
  r8vec2_print_some_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'FLORIDA_CVT_POP_TESTS' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  florida_cvt_pop_tests ( )
  timestamp ( )
 
