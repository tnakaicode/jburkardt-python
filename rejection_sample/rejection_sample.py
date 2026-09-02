#! /usr/bin/env python3
#
def rejection_sample_test ( ):

#*****************************************************************************80
#
## rejection_sample_test() tests rejection_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'rejection_sample_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test rejection_sample().' )

  chebyshev2_sample_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rejection_sample_test():' )
  print ( '  Normal end of execution.' )

  return

def chebyshev2_sample_test ( ):

#*****************************************************************************80
#
## chebyshev2_sample_test() tests chebyshev2_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'chebyshev2_sample_test():' )
  print ( '  chebyshev2_sample() uses acceptance/rejection sampling' )
  print ( '  on the Chebyshev2 density 2/pi * sqrt(1-x^2)' )

  n = 100000

  s, n2 = chebyshev2_sample ( n )

  print ( '' )
  print ( '  Number of samples N = ', n )
  print ( '  Number of trials N2 = ', n2 )
  print ( '  N2/N =       ', n2 / n )
  print ( '  Area ratio = ', 2.0 / ( np.pi / 2.0 ) )

  x = np.linspace ( -1.0, +1.0, 42 )
  y = 2.0 / np.pi * np.sqrt ( 1.0 - x**2 )

  plt.clf ( )
  plt.hist ( s, bins = 41, density = True )
  plt.plot ( x, y, 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.axis ( 'equal' )
  filename = 'chebyshev2_sample.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def chebyshev2_sample ( n ):

#*****************************************************************************80
#
## chebyshev2_sample() samples the Chebyshev2 PDF.
#
#  Discussion:
#
#    The Chebyshev2 PDF uses the density
#
#      rho(x) = 2/pi * sqrt(1-x^2)
#
#    for -1 <= X <= 1.
#
#    This PDF is easy to work with, but we want to use it as a demonstration
#    of rejection sampling.  In particular, we can compare this PDF to
#    a uniform PDF with maximum value 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to compute.
#
#  Output:
#
#    real S(N), the sample points.
#
#    integer N2, the number of trials required to produce
#    N acceptable points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  pdfmax = 2.0 / np.pi

  s = np.zeros ( n )

  i = 0
  j = 0

  while ( i < n ):

    while ( True ):

      j = j + 1
#
#  Select X at random in [-1,+1]
#
      x = - 1.0 + 2.0 * rng.random ( )
#
#  Select Y at random in [0,PDFMAX].
#
      y = pdfmax * rng.random ( )
#
#  Evaluate Z 
#
      z = 2.0 / np.pi * np.sqrt ( 1.0 - x**2 )
#
#  Acceptance test:
#
      if ( y <= z ):
        break

    s[i] = x
    i = i + 1

  n2 = j

  return s, n2

def cvt_1d_sample ( n ):

#*****************************************************************************80
#
## cvt_1d_sample() samples a PDF for a 1D CVT problem.
#
#  Discussion:
#
#    The Chebyshev points X have an asymptotic density
#
#      rho(x) = 1/pi * 1/sqrt(1-x^2)
#
#    Denote by H(I) the size of any of the disjoint intervals
#    containing X(I), and note that it there is a sort of 
#    equidistribution property so that
#
#      h(x(i)) proportional to 1 / rho(x(i))
#
#    It is known that if points X2 forming a CVT in 1D are generated 
#    according to a density rho2(x2), and H2(I) represents the diameter of the 
#    CVT interval, that we expect
#
#      h2(x2(i)) proportional to 1 / rho2(x2(i))^3
#
#    Therefore, we expect that if we can use the density
#
#      rho2(x) = rho(x)^(1/3)
#
#    that the CVT points will tend to the locations of the Chebyshev points.
#
#
#    As it turns out, the computation of the CVT requires sampling with
#    respect to the density rho, which in turn requires computing the
#    incomplete integral or CDF(x) of the density, and then inverting to
#    get X(CDF).  For the given density function above, Mathematica
#    is unable to determine an inverse function.
#
#    Therefore, to compute X(CDF), we must try using rejection sampling.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to compute.
#
#  Output:
#
#    real S(N), the sample points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  s = np.zeros ( n )

  pdfmax = 2.0 / np.pi

  i = 0

  while ( i < n ):

    while ( True ):
#
#  Select X at random in [-1,+1]
#
      x = - 1.0 + 2.0 * rng.random ( )
#
#  Select Y at random in [0,PDFMAX].
#
      y = pdfmax * rng.random ( )
#
#  Evaluate Z 
#
      z = 1.0 / np.sqrt ( np.pi ) / np.sqrt ( 1.0 - x**2 )**( 1.0 / 6.0 )
#
#  Acceptance test:
#
      if ( y <= z ):
        break;

    s[i] = x
    i = i + 1

  return s

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
  rejection_sample_test ( )
  timestamp ( )

