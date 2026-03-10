#! /usr/bin/env python3
#
def fly_simulation_test ( ):

#*****************************************************************************80
#
## fly_simulation_test() tests fly_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fly_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  A fly lands at random on a plate of radius 1.' )
  print ( '  D is the distance of the fly to the center.' )
  print ( '  Use simulation to analyze the behavior of D.' )

  n = 10000
  fly_cdf_plot ( n )
  fly_histogram_plot ( n )
  fly_pdf_plot ( n )
  fly_stats_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fly_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def fly_cdf_plot ( n ):

#*****************************************************************************80
#
## fly_cdf_plot() plots the estimated CDF for the fly simulation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of times the experiment is carried out.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fly_cdf_plot()' )
  print ( '  A fly lands at random on a plate of radius 1.' )
  print ( '  D is the distance from the center.' )
  print ( '  Estimate the CDF for D with a plot.' )

  d = fly_simulation ( n )
#
#  Create a CDF histogram.
#
  plt.clf ( )
  bin_num = 20
  plt.hist ( d, bins = bin_num, cumulative = True, density = True )
  d2 = np.linspace ( 0.0, 1.0, 21 )
  plt.plot ( d2, d2**2, 'r-', linewidth = 3 )
  plt.grid ( 'True' )
  plt.xlabel ( 'Distance from center' )
  plt.ylabel ( 'Cumulative Probability' )
  plt.title ( 'CDF for fly simulation' )
  plt.legend ( [ 'Exact CDF', 'Observed CDF' ] )
  filename = 'fly_cdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def fly_histogram_plot ( n ):

#*****************************************************************************80
#
## fly_histogram_plot() histograms the fly simulation data.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of times the experiment is carried out.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fly_histogram_plot()' )
  print ( '  A fly lands at random on a plate of radius 1.' )
  print ( '  D is the distance from the center.' )
  print ( '  Make a histogram of the D data.' )

  d = fly_simulation ( n )

  plt.clf ( )
  bin_num = 20
  plt.hist ( d, bins = bin_num )
  plt.grid ( 'True' )
  plt.xlabel ( 'Distance from center' )
  plt.ylabel ( 'Frequency' )
  s = 'Distance from center, ' + str ( n ) + ' simulations'
  plt.title ( s )
  filename = 'fly_histogram.png'
  plt.savefig ( filename )
  print ( 'Graphics saved as "' + filename + '"' )

  return

def fly_pdf_plot ( n ):

#*****************************************************************************80
#
## fly_pdf_plot() plots the estimated PDF for the fly simulation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of times the experiment is carried out.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fly_pdf_plot()' )
  print ( '  A fly lands at random on a plate of radius 1.' )
  print ( '  D is the distance from the center.' )
  print ( '  Estimate the PDF for D with a plot.' )

  d = fly_simulation ( n )
#
#  Compare a histogram of the data with a plot of the exact PDF.
#
  plt.clf ( )
  bin_num = 20
  plt.hist ( d, bins = bin_num, density = True )
  d2 = np.linspace ( 0.0, 1.0, bin_num )
  plt.plot ( d2, 2.0 * d2, 'r-', linewidth = 3 )
  plt.grid ( 'True' )
  plt.xlabel ( 'Distance from center' )
  plt.ylabel ( 'Probability' )
  plt.title ( 'PDF for fly simulation' )
  filename = 'fly_pdf.png'
  plt.savefig ( filename )
  print ( 'Graphics saved as "' + filename + '"' )

  return

def fly_simulation ( n ):

#*****************************************************************************80
#
## fly_simulation() estimates the average distance of a fly from the origin.
#
#  Discussion:
#
#    A fly lands at a random point on a dish of radius 1.
#    On average, how far is the fly from the center of the dish?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of times the experiment is carried out.
#
#  Output:
#
#    real d[n]: the observed distances.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  d = np.zeros ( n )

  for i in range ( 0, n ):
    [ r1, r2 ] = rng.random ( 2 )
    d[i] = np.sqrt ( r1 )
#   theta = 2.0 * np.pi * r2
#   x = r * np.cos ( theta )
#   y = r * np.sin ( theta )

  return d

def fly_stats_test ( ):

#*****************************************************************************80
#
## fly_stats_test() tests fly_stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  exact = 2.0 / 3.0

  print ( '' )
  print ( 'fly_stats_test()' )
  print ( '  A fly lands at random on a plate of radius 1.' )
  print ( '  D is the distance from the center.' )
  print ( '  The exact average distance is', exact )
  print ( '  Compute statistics for a sequence of experiments of size n.' )
  print ( '' )
  print ( '  n   dmin dmean dmax dstd ||dmean-exact||' )
  print ( '' )

  for n in [ 10, 100, 1000, 10000 ]:
    d = fly_simulation ( n )
    d_min = np.min ( d )
    d_mean = np.mean ( d )
    d_max = np.max ( d )
    d_std = np.std ( d )
    print ( '  %5d  %6.4f  %6.4f  %6.4f  %6.4f  %6.4f' \
    % ( n, d_min, d_mean, d_max, d_std, np.abs ( d_mean - exact ) ) )

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
  fly_simulation_test ( )
  timestamp ( )

