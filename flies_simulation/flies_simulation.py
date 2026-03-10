#! /usr/bin/env python3
#
def flies_simulation_test ( ):

#*****************************************************************************80
#
## flies_simulation_test() tests flies_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'flies_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Two flies land at random on a plate of radius 1.' )
  print ( '  Their pairwise distance D is the quantity of interest.' )
  print ( '  Plot PDF, CDF, and statistics by simulation.' )

  n = 10000
  flies_cdf_plot ( n )
  flies_pdf_plot ( n )
  flies_stats_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'flies_simulation_test()' )
  print ( '  Normal end of execution.' )

  return

def flies_cdf_plot ( n ):

#*****************************************************************************80
#
## flies_cdf_plot() plots the estimated CDF for the flies simulation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 August 2022
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
  print ( 'flies_cdf_plot()' )
  print ( '  Two flies land at random on a plate of radius 1.' )
  print ( '  D is the distance between them.' )
  print ( '  Estimate the CDF for D with a plot.' )

  d = flies_simulation ( n )
#
#  Create a CDF histogram.
#
  plt.clf ( )
  bin_num = 21
  plt.hist ( d, bins = bin_num, cumulative = True, density = True )
  plt.grid ( 'True' )
  plt.xlabel ( 'Distance between flies' )
  plt.ylabel ( 'Cumulative Probability' )
  plt.title ( 'CDF for flies simulation' )
  filename = 'flies_cdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def flies_pdf_plot ( n ):

#*****************************************************************************80
#
## flies_pdf_plot() plots the estimated PDF for the flies simulation.
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
  print ( 'flies_pdf_plot():' )
  print ( '  Two flies land at random on a plate of radius 1.' )
  print ( '  D is the distance between them.' )
  print ( '  Estimate the PDF for D with a plot.' )
#
#  Observe many experiments.
#
  d = flies_simulation ( n )
#
#  Evaluate the exact PDF.
#
  d2 = np.linspace ( 0.0, 2.0, 101 )
  pdf = d2 * ( 4.0 * np.arccos ( d2 / 2 ) \
    - d2 * np.sqrt ( 4.0 - d2 ** 2 ) ) / np.pi;
#
#  Compare a histogram of the data with a plot of the exact PDF.
#
  plt.clf ( )
  bin_num = 21
  plt.hist ( d, bins = bin_num, density = True )
  plt.plot ( d2, pdf, 'r-', linewidth = 3 )
  plt.grid ( 'True' )
  plt.legend ( [ 'Exact', 'Observed' ] )
  plt.xlabel ( 'Distance between flies' )
  plt.ylabel ( 'Probability' )
  plt.title ( 'PDF for flies simulation' )
  filename = 'flies_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def flies_simulation ( n ):

#*****************************************************************************80
#
## flies_simulation() reports the distance between flies randomly placed in a circle.
#
#  Discussion:
#
#    Two flies land at a random on a dish of radius 1.
#    What is the distance between them?
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
#
#  Pick a random location in the circle for fly #1.
#
    r1 = np.sqrt ( rng.random ( ) )
    t1 = 2.0 * np.pi * rng.random ( )
    x1 = r1 * np.cos ( t1 )
    y1 = r1 * np.sin ( t1 )
#
#  Pick a random location in the circle for fly #2.
#
    r2 = np.sqrt ( rng.random ( ) )
    t2 = 2.0 * np.pi * rng.random ( )
    x2 = r2 * np.cos ( t2 )
    y2 = r2 * np.sin ( t2 )
#
#  Measure the distance between them.
#
    d[i] = np.sqrt ( ( x1 - x2 )**2 + ( y1 - y2 )**2 )

  return d

def flies_stats_test ( ):

#*****************************************************************************80
#
## flies_stats_test() tests flies_stats().
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

  print ( '' )
  print ( 'flies_stats_test()' )
  print ( '  Two flies land at random on a plate of radius 1.' )
  print ( '  D is the distance between them.' )
  print ( '  Compute statistics for a sequence of experiments of size n.' )
  print ( '' )
  print ( '  n   dmin dmean dmax dstd' )
  print ( '' )

  for n in [ 10, 100, 1000, 10000 ]:
    d = flies_simulation ( n )
    d_min = np.min ( d )
    d_mean = np.mean ( d )
    d_max = np.max ( d )
    d_std = np.std ( d )
    print ( '  %5d  %6.4f  %6.4f  %6.4f  %6.4f' \
    % ( n, d_min, d_mean, d_max, d_std ) )

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
  flies_simulation_test ( )
  timestamp ( )

